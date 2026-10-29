from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)

# table -> (page title, icon, [(column, label), ...])
TABLES = {
    "teachers":  ("Teachers",  "👩‍🏫", [("name", "Name"), ("department", "Department"), ("room", "Room"), ("availability", "Availability")]),
    "transport": ("Transport", "🚌", [("route", "Route"), ("bus_number", "Bus Number"), ("timing", "Timing")]),
    "library":   ("Library",   "📚", [("book_name", "Book Name"), ("status", "Status")]),
    "labs":      ("Labs",      "🧪", [("lab_name", "Lab Name"), ("room", "Room"), ("availability", "Availability")]),
    "canteen":   ("Canteen",   "🍽️", [("item", "Item"), ("price", "Price (₹)")]),
}

# The "database": a dictionary of lists. Each row = [id, value1, value2, ...]
DATA = {
    "teachers":  [["Dr. R. Kumar", "Computer Science", "SJT 301", "Mon-Fri 10-12"],
                  ["Dr. S. Priya", "Chemistry", "TT 204", "Tue, Thu 2-4"],
                  ["Prof. A. Ravi", "Mathematics", "SMV 110", "Mon, Wed 11-1"]],
    "transport": [["Katpadi - Campus", "B12", "7:30 AM"], ["Vellore Fort - Campus", "B07", "8:00 AM"],
                  ["Campus - Katpadi", "B12", "5:30 PM"]],
    "library":   [["Python Crash Course", "Available"], ["Database System Concepts", "Issued"], ["Let Us C", "Available"]],
    "labs":      [["Python Lab", "SJT 512", "Free after 3 PM"], ["Chemistry Lab", "TT 101", "Booked"],
                  ["Electronics Lab", "SMV 220", "Free"]],
    "canteen":   [["Masala Dosa", "50"], ["Veg Biryani", "90"], ["Tea", "15"], ["Samosa", "20"]],
}
DATA = {t: [[i + 1] + r for i, r in enumerate(rows)] for t, rows in DATA.items()}  # add ids

def search(t, q):
    return [r for r in DATA[t] if any(q.lower() in str(v).lower() for v in r[1:])]

@app.route("/")
def home():
    q = request.args.get("q", "").strip()
    results = {t: search(t, q) for t in TABLES} if q else {}
    return render_template("home.html", tables=TABLES, q=q, results={t: r for t, r in results.items() if r})

@app.route("/<t>", methods=["GET", "POST"])
def table(t):
    if t not in TABLES: abort(404)
    title, icon, cols = TABLES[t]
    if request.method == "POST":
        if "delete" in request.form:
            DATA[t] = [r for r in DATA[t] if str(r[0]) != request.form["delete"]]
        else:
            vals = [request.form.get(c, "").strip() for c, _ in cols]
            if all(vals):
                DATA[t].append([max((r[0] for r in DATA[t]), default=0) + 1] + vals)
        return redirect(f"/{t}")
    q = request.args.get("q", "").strip()
    return render_template("table.html", tables=TABLES, t=t, title=title, icon=icon, cols=cols, rows=search(t, q), q=q)

if __name__ == "__main__":
    app.run(debug=True)
