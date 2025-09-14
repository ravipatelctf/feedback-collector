from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": f"Welcome to the Feedback Collector app"}


@app.route("/greet")
def greet():
    name = request.args.get("name")
    return {"message": f"Hello {name}, welcome to our feedback portal!"}


@app.route("/submit-feedback", methods = ['POST'])
def submit_feedback():
    data = request.get_json()
    name = data.get("name")
    message = data.get("message")
    rating = data.get("rating")
    return {
        "status": "success",
        "reply": f"Thanks {name}! We appreciate your feedback."
    }


@app.route("/location")
def location():
    city = request.args.get("city")
    return {"message": f"You're chechking data for {city}."}


@app.route("/add-numbers", methods = ['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    sum = num1 + num2
    return {"result": sum}


@app.route("/contact-form", methods = ['POST'])
def contact_form():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    return {"reply": f"Thanks {name}, we'll contact you soon at {email}"}


@app.route("/convert-temp")
def convert_temp():
    celsius = int(request.args.get("celsius"))
    fahrenheit = celsius * 1.8 + 32
    return {"temerature_in_celsius": celsius, "temperature_in_fahrenheit": fahrenheit}


@app.route("/billing", methods = ['POST'])
def billing():
    data = request.get_json()
    item_name = data.get("item_name")
    unit_price = data.get("unit_price")
    quantity = data.get("quantity")
    return {"total_amount": unit_price * quantity}


@app.route("/goals", methods = ['POST'])
def goals():
    data = request.get_json()
    goals = data.get("goals")
    return {"goals_count": len(goals)}


@app.route("/emergency", methods = ['POST'])
def emergency():
    data = request.get_json()
    name = data.get("name")
    issue = data.get("issue")
    location = data.get("location")
    return {"alert": f"Help request from {name} at {location}. Issue: {issue}"}


@app.route("/event")
def event():
    event_name = request.args.get("event_name")
    date = request.args.get("date")
    return {"confirmation": f"{event_name} is scheduled on {date}"}


@app.route("/delete-item", methods = ['POST'])
def delete_item():
    data = request.get_json()
    item_name = data.get("item_name")
    return {"message": f"{item_name} has been removed."}


if __name__ == '__main__':
    app.run(debug=True)