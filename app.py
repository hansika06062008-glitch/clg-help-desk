from flask import Flask, render_template, request, redirect, abort
import mysql.connector

app = Flask(__name__)
DB = dict(host="localhost", user="root", password="your_password", database="helpdesk")

# table -> (page title, icon, [(column, label), ...])
TABLES = {
    "teachers":  ("Teachers",  "👩‍🏫", [("name", "Name"), ("department", "Department"), ("room", "Room"), ("availability", "Availability")]),
    "transport": ("Transport", "🚌", [("route", "Route"), ("bus_number", "Bus Number"), ("timing", "Timing")]),
    "library":   ("Library",   "📚", [("book_name", "Book Name"), ("status", "Status")]),
    "labs":      ("Labs",      "🧪", [("lab_name", "Lab Name"), ("room", "Room"), ("availability", "Availability")]),
    "canteen":   ("Canteen",   "🍽️", [("item", "Item"), ("price", "Price (₹)")]),
}

def run(sql, args=(), fetch=True):
    con = mysql.connector.connect(**DB)
    cur = con.cursor()
    cur.execute(sql, args)
    rows = cur.fetchall() if fetch else None
    con.commit(); con.close()
    return rows

@app.route("/")
def home():
    q = request.args.get("q", "").strip()
    results = {}
    if q:  # search every table at once
        for t, (title, _, cols) in TABLES.items():
            where = " OR ".join(f"{c} LIKE %s" for c, _ in cols)
            rows = run(f"SELECT * FROM {t} WHERE {where}", [f"%{q}%"] * len(cols))
            if rows: results[t] = rows
    return render_template("home.html", tables=TABLES, q=q, results=results)

@app.route("/<t>", methods=["GET", "POST"])
def table(t):
    if t not in TABLES: abort(404)
    title, icon, cols = TABLES[t]
    if request.method == "POST":
        if "delete" in request.form:
            run(f"DELETE FROM {t} WHERE id=%s", (request.form["delete"],), False)
        else:
            vals = [request.form.get(c, "").strip() for c, _ in cols]
            if all(vals):
                run(f"INSERT INTO {t} ({','.join(c for c, _ in cols)}) VALUES ({','.join(['%s'] * len(cols))})", vals, False)
        return redirect(f"/{t}")
    q = request.args.get("q", "").strip()
    where = " OR ".join(f"{c} LIKE %s" for c, _ in cols)
    rows = run(f"SELECT * FROM {t} WHERE {where}", [f"%{q}%"] * len(cols))
    return render_template("table.html", tables=TABLES, t=t, title=title, icon=icon, cols=cols, rows=rows, q=q)

if __name__ == "__main__":
    app.run(debug=True)
