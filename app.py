from flask import Flask, request, render_template
from trip_scraper import scrape_itinerary  

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    itinerary = None
    if request.method == "POST":
        destination = request.form.get("destination", "").strip()
        days = request.form.get("days", "").strip()
        trip_type = request.form.get("trip_type", "").strip()

        if destination and days and trip_type:  # Ensure values are not empty
            query = f"{destination}, {days}, {trip_type}"
            itinerary = scrape_itinerary(query)

    return render_template("index.html", itinerary=itinerary)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
