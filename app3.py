import os, sys
print("Running app.py from:", os.path.abspath(sys.argv[0]))
from flask import Flask, jsonify, send_from_directory
from waitress import serve   # ✅ Import Waitress
import os                    # ✅ Import os so we can use environment variables

app = Flask(__name__, static_folder="static")


# Example dataset
FOOD_BANKS = [
    {
        "id": 991,
        "name": "Carroll County Food Sunday Headquarters",
        "lat": 39.57605,
        "lng": -76.99411,
        "address": "10 Distillery Drive, Westminster, MD",
        "hours": "Tues, Wed, Thurs: 10:00-11:15 and 1:00-2:15, Sat: 9:00-11:15",
        "phone": "(410) 857-7926",
        "website": "https://ccfoodsunday.org/"
    },
    {
        "id": 992,
        "name": "Rock of Help - Ebenezer United Methodist Church",
        "lat": 39.43991,
        "lng": -77.05448,
        "address": "4901 Woodbine Rd, Sykesville, MD",
        "hours": "3rd Sat of the month 9am–11am",
        "phone": "(410) 795-6136",
        "website": "https://www.ebenezerumchurch.org/rock-of-help-food-pantry"
    },
    {
        "id": 993,
        "name": "Wesley Freedom Pantry - Food Distribution Center",
        "lat": 39.40512,
        "lng": -76.96079,
        "address": "961 Johnsville Rd, Sykesville, MD",
        "hours": "Certain Days 8:30am–11:30am, Meals Mon, Thu, and Fri at noon",
        "phone": "(410) 795-2777",
        "website": "https://https://www.wesleyfreedom.org/groceries-meals"
    },
    {
    "id": 1,
    "name": "Maryland Food Bank – Baltimore Office",
    "lat": 39.241,
    "lng": -76.686,
    "address": "2200 Halethorpe Farms Road, Baltimore, MD 21227",
    "hours": "Mon–Fri 8:00am–4:30pm",
    "phone": "(410) 737-8282",
    "website": "https://mdfoodbank.org"
  },
  {
    "id": 2,
    "name": "Manna House",
    "lat": 39.331,
    "lng": -76.614,
    "address": "435 E 25th St, Baltimore, MD 21218",
    "hours": "Daily breakfast 8:30–10:30am",
    "phone": "(410) 889-3001",
    "website": "https://mannahouseinc.org"
  },
  {
    "id": 3,
    "name": "Franciscan Center of Baltimore",
    "lat": 39.312,
    "lng": -76.621,
    "address": "101 W 23rd St, Baltimore, MD 21218",
    "hours": "Mon–Fri 10:00am–1:00pm",
    "phone": "(410) 467-5340",
    "website": "https://fcbmore.org"
  },
  {
    "id": 4,
    "name": "Our Daily Bread Employment Center",
    "lat": 39.295,
    "lng": -76.609,
    "address": "725 Fallsway, Baltimore, MD 21202",
    "hours": "Daily lunch 10:30am–12:30pm",
    "phone": "(667) 600-3400",
    "website": "https://catholiccharities-md.org"
  },
  {
    "id": 5,
    "name": "Moveable Feast",
    "lat": 39.309,
    "lng": -76.617,
    "address": "901 N Milton Ave, Baltimore, MD 21205",
    "hours": "Mon–Fri 9:00am–5:00pm",
    "phone": "(410) 327-3420",
    "website": "https://mfeast.org"
  },
  {
    "id": 6,
    "name": "Macedonia Project Food Pantry",
    "lat": 39.332,
    "lng": -76.541,
    "address": "New Creation Christian Church, Baltimore, MD 21206",
    "hours": "Tues & Thurs 11:00am–1:00pm",
    "phone": "(410) 488-5650",
    "website": "https://foodpantries.org/li/macedonia_project_food_pantry"
  },
  {
    "id": 7,
    "name": "St. Vincent de Paul of Baltimore",
    "lat": 39.290,
    "lng": -76.612,
    "address": "2300 N Charles St, Baltimore, MD 21218",
    "hours": "Mon–Fri 9:00am–5:00pm",
    "phone": "(410) 662-0500",
    "website": "https://vincentbaltimore.org"
  },
  {
    "id": 8,
    "name": "Beans and Bread Center",
    "lat": 39.283,
    "lng": -76.593,
    "address": "402 S Bond St, Baltimore, MD 21231",
    "hours": "Mon–Sat 10:30am–12:30pm",
    "phone": "(410) 732-1892",
    "website": "https://catholiccharities-md.org/services/beans-and-bread"
  },
  {
    "id": 9,
    "name": "Paul’s Place",
    "lat": 39.281,
    "lng": -76.633,
    "address": "1118 Ward St, Baltimore, MD 21230",
    "hours": "Mon–Fri 8:00am–4:00pm",
    "phone": "(410) 625-0775",
    "website": "https://paulsplaceoutreach.org"
  },
  {
    "id": 10,
    "name": "Helping Up Mission",
    "lat": 39.293,
    "lng": -76.606,
    "address": "1029 E Baltimore St, Baltimore, MD 21202",
    "hours": "Mon–Fri 9:00am–5:00pm",
    "phone": "(410) 675-7500",
    "website": "https://helpingupmission.org"
  },
   {
    "id": 11,
    "name": "Westminster Rescue Mission",
    "lat": 39.570,
    "lng": -76.995,
    "address": "658 Lucabaugh Mill Road, Westminster, MD 21157",
    "hours": "Mon–Fri 9:00am–4:00pm",
    "phone": "(410) 848-2222",
    "website": "https://westminsterrescuemission.org"
  },
  {
    "id": 12,
    "name": "Taneytown Food Pantry (Trinity Evangelical Lutheran Church)",
    "lat": 39.656,
    "lng": -77.174,
    "address": "38 West Baltimore St, Taneytown, MD 21787",
    "hours": "Thursdays 9:30–11:15am",
    "phone": "(410) 756-6626",
    "website": "https://trinitytaneytown.org"
  },
  {
    "id": 13,
    "name": "Carpenters Table Food Pantry",
    "lat": 39.656,
    "lng": -77.174,
    "address": "Trinity Evangelical Lutheran Church, Taneytown, MD",
    "hours": "Thursdays 9:30–11:15am",
    "phone": "(410) 756-6626",
    "website": "https://foodpantries.org/li/carpenters_table_taneytown"
  },
  {
    "id": 14,
    "name": "Hampstead Food Pantry (St. John’s United Methodist Church)",
    "lat": 39.610,
    "lng": -76.850,
    "address": "1205 N Main St, Hampstead, MD 21074",
    "hours": "Wed 6:00–7:30pm, Sat 9:00–11:00am",
    "phone": "(410) 374-2394",
    "website": "https://stjohnshampstead.org"
  },
  {
    "id": 15,
    "name": "Manchester Food Pantry",
    "lat": 39.662,
    "lng": -76.889,
    "address": "Manchester Baptist Church, 2933 Manchester Baptist Rd, Manchester, MD",
    "hours": "2nd & 4th Sat 9:00–11:00am",
    "phone": "(410) 374-4876",
    "website": "https://foodpantries.org/li/manchester_food_pantry"
  },
  {
    "id": 17,
    "name": "Mt. Airy Net Food Pantry",
    "lat": 39.376,
    "lng": -77.154,
    "address": "403 S Main St, Mt. Airy, MD 21771",
    "hours": "Mon–Thurs 10:00am–4:00pm",
    "phone": "(301) 829-0472",
    "website": "https://mtairynet.org"
  },
  {
    "id": 18,
    "name": "Silver Run Food Pantry",
    "lat": 39.608,
    "lng": -77.038,
    "address": "St. Mary’s United Church of Christ, 1441 Mayberry Rd, Westminster, MD",
    "hours": "3rd Sat 9:00–11:00am",
    "phone": "(410) 848-1385",
    "website": "https://foodpantries.org/li/silver_run_food_pantry"
  },
  {
    "id": 19,
    "name": "Salvation Army – Carroll County Service Center",
    "lat": 39.570,
    "lng": -76.995,
    "address": "300 Hahn Rd, Westminster, MD 21157",
    "hours": "Monthly Pantry on the Go (call for schedule)",
    "phone": "(410) 876-9358",
    "website": "https://sa-md.org/centralmaryland/carroll-county-services"
  },
  {
    "id": 20,
    "name": "St. Paul’s United Methodist Church Pantry",
    "lat": 39.3666,
    "lng": -76.97017,
    "address": "7538 Main St, Sykesville, MD 21784",
    "hours": "2nd Saturday of the Month 9:00am–12:00pm",
    "phone": "(410) 795-0714",
    "website": "https://stpaulssykesville.com/support/"
    },
    {
    "id": 21,
    "name": "Brian’s Safe Haven",
    "lat": 39.657,
    "lng": -77.174,
    "address": "2325 Feeser Rd, Taneytown, MD 21787",
    "hours": "Tues & Thurs 10:00am–2:00pm",
    "phone": "(443) 500-1139",
    "website": "https://briansafehaven.com"
  },
  {
    "id": 22,
    "name": "United Way / Westminster Rescue Mission Outreach",
    "lat": 39.570,
    "lng": -76.995,
    "address": "Behind McDonald’s, shopping center parking lot, Westminster, MD",
    "hours": "2nd Wed of the month at 3:45pm",
    "phone": "(410) 848-2222",
    "website": "https://westminsterrescuemission.org"
  },
  {
    "id": 23,
    "name": "Elders Baptist Church Pantry",
    "lat": 39.40579,
    "lng": -76.953,
    "address": "1216 Liberty Road, Sykesville, MD",
    "hours": "Every other Thursday from 4:30pm-6pm",
    "phone": "(410) 975-9481",
    "website": "https://www.eldersbaptist.org/food_pantry"
  },
  {
    "id": 24,
    "name": "Carroll County Food Sunday at St. Joseph Catholic Church",
    "lat": 39.40628,
    "lng": -76.96487,
    "address": "915 Liberty Road, Sykesville, MD",
    "hours": "Wednesdays from 10am-12pm",
    "phone": "(410) 795-7838",
    "website": "https://saintjoseph.cc/ccfs/"
  }



]

# Serve the Leaflet map page
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Serve the food bank data as JSON
@app.route("/api/foodbanks")
def list_foodbanks():
    print("API called — dataset length:", len(FOOD_BANKS))
    return jsonify({"items": FOOD_BANKS})

if __name__ == "__main__":
    # ✅ Option 3: Auto-reload in development
    if os.environ.get("FLASK_ENV") == "development":
        # Use Flask’s built-in server with debug mode
        app.run(host="127.0.0.1", port=9090, debug=True)
    else:
        # Use Waitress in production
        serve(app, host="0.0.0.0", port=9090)
