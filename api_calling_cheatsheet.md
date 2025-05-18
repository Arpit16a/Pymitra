
# 🧠 API Calling in Python: The Ultimate Cheatsheet

This cheatsheet is meant for **absolute understanding** of APIs and how to interact with them using Python — every term, every step, and every trick.

---

## 📌 What is an API?

**API (Application Programming Interface)** is a set of rules and protocols that allows two software applications to communicate with each other.

Think of it like a **waiter in a restaurant**:
- You (the client) tell the waiter (API) what you want.
- The waiter goes to the kitchen (server) and brings your food (response).

---

## ⚙️ Types of APIs

- **REST API** (most common)
- SOAP (older, XML-based)
- GraphQL (modern, flexible query language)

We'll focus on **REST APIs**, which use standard HTTP methods:

| HTTP Method | Action         |
|-------------|----------------|
| GET         | Fetch data     |
| POST        | Send new data  |
| PUT/PATCH   | Update data    |
| DELETE      | Remove data    |

---

## 🛠 Tools Required

- `requests` library (install via pip)
```bash
pip install requests
```

---

## 🔐 Terminologies You MUST Know

| Term              | Meaning |
|-------------------|--------|
| **Endpoint**      | URL to access the API (e.g., `https://api.example.com/weather`) |
| **Base URL**      | Common part of all endpoints |
| **API Key**       | Secret token to authenticate your request |
| **Headers**       | Metadata (e.g., content-type, auth token) |
| **Payload/Data**  | Data you send with POST/PUT |
| **Response**      | Data returned by server |
| **Status Code**   | Tells if request was successful (200, 404, etc.) |
| **JSON**          | Format in which data is usually sent/received |

---

## 🚀 Basic GET Request Example

```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)

# Check status
print(response.status_code)  # e.g., 200

# Get JSON data
data = response.json()
print(data)
```

---

## 📤 GET with Params

```python
params = {"city": "Mumbai", "units": "metric"}
response = requests.get("https://api.example.com/weather", params=params)
print(response.json())
```

📎 `params` will be encoded into the URL:
```
https://api.example.com/weather?city=Mumbai&units=metric
```

---

## 🔒 Using API Key (via URL or Headers)

### 1. In URL (not secure but common)
```python
url = f"https://api.example.com/weather?apikey={API_KEY}"
```

### 2. In Headers (more secure)
```python
headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get(url, headers=headers)
```

---

## 🧾 Reading Response

```python
print(response.status_code)       # HTTP status (200, 404, etc.)
print(response.headers)           # Metadata about response
print(response.text)              # Raw response
print(response.json())            # Parsed JSON (dict)
```

---

## 📦 POST Request with Payload

```python
url = "https://api.example.com/login"
data = {"username": "user1", "password": "abc123"}

response = requests.post(url, json=data)  # Use json= for JSON body
print(response.json())
```

---

## 🧪 Common Status Codes

| Code | Meaning             |
|------|----------------------|
| 200  | OK                  |
| 201  | Created             |
| 400  | Bad Request         |
| 401  | Unauthorized        |
| 403  | Forbidden           |
| 404  | Not Found           |
| 500  | Server Error        |

---

## ❌ Error Handling in API

```python
try:
    response = requests.get(url)
    response.raise_for_status()  # raises HTTPError for bad codes
    data = response.json()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except requests.exceptions.RequestException as err:
    print(f"Request error: {err}")
except Exception as e:
    print(f"Something went wrong: {e}")
```

---

## 🧰 Tips

- Always check status codes before accessing `.json()`
- Use `try-except` for production-level safety
- Use `headers` to set content types or auth tokens
- Use tools like [Postman](https://postman.com) to test APIs visually

---

## 🧪 Bonus: Convert Response to Pandas

```python
import pandas as pd

url = "https://api.example.com/students"
response = requests.get(url)
data = response.json()

# Assume data is a list of dictionaries
df = pd.DataFrame(data)
print(df.head())
```

---

## 📁 Useful APIs to Practice

| API                 | Purpose                   | URL |
|---------------------|---------------------------|-----|
| OpenWeatherMap      | Weather Data              | https://openweathermap.org/api |
| Joke API            | Random Jokes              | https://official-joke-api.appspot.com/random_joke |
| News API            | Latest Headlines          | https://newsapi.org/ |
| CoinGecko API       | Crypto Prices             | https://www.coingecko.com/en/api |

---

## 📎 Real-world Use Case: Weather App

```python
import requests

def get_weather(city="Delhi"):
    API_KEY = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"Weather in {city}: {desc}, {temp}°C"
    else:
        return "Failed to fetch weather"
```

---

## 🔐 Authentication Methods

| Method           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **API Key**      | A unique token passed via query params or headers                           |
| **Bearer Token** | A secure token usually passed in headers as `Authorization: Bearer <token>` |
| **Basic Auth**   | Base64-encoded username/password combo in headers                           |
| **OAuth2**       | Standard for secure delegated access (commonly used with Google, GitHub)    |

### 📍 1. Basic Authentication
```python
from requests.auth import HTTPBasicAuth

url = "https://api.example.com/data"
response = requests.get(url, auth=HTTPBasicAuth("username", "password"))
print(response.json())
```

### 📍 2. Bearer Token (OAuth-style)
```python
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
response = requests.get("https://api.example.com/secure", headers=headers)
```

### 📍 3. API Key in Headers (Preferred)
```python
headers = {
    "x-api-key": "YOUR_API_KEY"
}
response = requests.get("https://api.example.com/data", headers=headers)
```

### 📍 4. API Key in URL (Less Secure)
```python
url = "https://api.example.com/data?apikey=YOUR_API_KEY"
response = requests.get(url)
```

### 🛑 Note:
- Use `https://` for secure requests.
- Avoid storing keys/tokens directly in code — use environment variables or config files.

---

This is your complete reference for API calling in Python. Bookmark it. Practice each section. 🔥
