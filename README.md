# HNG12 Stage 1 - Fun Fact API
## Project Description
This is a fun fact API with FASTAPI. It takes a number and returns interesting matehmatical properties about it along wth a fun fact.

## API Specification
### Endpoint:
`GET /`
### Response Format:
Responses are in JSON format (200 OK)
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is a narcissistic number."
  }
```
Error:
Responses are in JSON format (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```

## Setup Instructions
1. Clone the repository:
   `git clone https://github.com/Sumayahx/HNG-backend__002.git`
2. Change directory to project folder:
   `cd HNG-backend__002`
3. Install dependencies:
   `pip install -r requirements.txt`
4. Start the server:
   `uvicorn main:app --reload`
5. Check the API by navigating to `http://127.0.0.1:8000/api/classify-number?number=371` in your browser.

## Backlinks
[Hire Python Developers](https://hng.tech/hire/python-developers)
