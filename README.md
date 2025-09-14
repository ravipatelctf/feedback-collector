# 📌 Feedback Collector API

A simple **Flask-based REST API** that provides multiple routes for handling feedback, user interaction, basic utilities, and form submissions.  

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/feedback-collector.git
cd feedback-collector
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
python main.py
```

Server will start at:

```
http://127.0.0.1:5000/
```

---

## 🔗 Useful Links

* [Flask Documentation](https://flask.palletsprojects.com/)
* [Python Official Docs](https://docs.python.org/3/)

---

## 📖 API Reference

### 🌐 **GET /**

**Description:** Welcome message
**Response:**

```json
{ "message": "Welcome to the Feedback Collector app" }
```

---

### 🌐 **GET /greet?name=John**

**Description:** Greets the user
**Response:**

```json
{ "message": "Hello John, welcome to our feedback portal!" }
```

---

### 🌐 **POST /submit-feedback**

**Description:** Submit user feedback
**Body:**

```json
{ "name": "Alice", "message": "Great app!", "rating": 5 }
```

**Response:**

```json
{ "status": "success", "reply": "Thanks Alice! We appreciate your feedback." }
```

---

### 🌐 **GET /location?city=Delhi**

**Response:**

```json
{ "message": "You're chechking data for Delhi." }
```

---

### 🌐 **POST /add-numbers**

**Body:**

```json
{ "num1": 10, "num2": 20 }
```

**Response:**

```json
{ "result": 30 }
```

---

### 🌐 **POST /contact-form**

**Body:**

```json
{ "name": "Bob", "email": "bob@example.com", "message": "Need help!" }
```

**Response:**

```json
{ "reply": "Thanks Bob, we'll contact you soon at bob@example.com" }
```

---

### 🌐 **GET /convert-temp?celsius=30**

**Response:**

```json
{ "temerature_in_celsius": 30, "temperature_in_fahrenheit": 86.0 }
```

---

### 🌐 **POST /billing**

**Body:**

```json
{ "item_name": "Book", "unit_price": 100, "quantity": 3 }
```

**Response:**

```json
{ "total_amount": 300 }
```

---

### 🌐 **POST /goals**

**Body:**

```json
{ "goals": ["Learn Flask", "Build API"] }
```

**Response:**

```json
{ "goals_count": 2 }
```

---

### 🌐 **POST /emergency**

**Body:**

```json
{ "name": "John", "issue": "Fire", "location": "Building A" }
```

**Response:**

```json
{ "alert": "Help request from John at Building A. Issue: Fire" }
```

---

### 🌐 **GET /event?event\_name=Conference\&date=2025-09-20**

**Response:**

```json
{ "confirmation": "Conference is scheduled on 2025-09-20" }
```

---

### 🌐 **POST /delete-item**

**Body:**

```json
{ "item_name": "Laptop" }
```

**Response:**

```json
{ "message": "Laptop has been removed." }
```

---

## ✅ Requirements

See [`requirements.txt`](requirements.txt):

* Flask==3.1.2
* Werkzeug==3.1.3
* Jinja2==3.1.6
* click==8.2.1
* blinker==1.9.0
* itsdangerous==2.2.0
* MarkupSafe==3.0.2

---

## 📬 Contact
For feature requests or bug reports, please contact me at **ravipatelctf@gmail.com**
