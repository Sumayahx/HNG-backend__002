from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n : int) -> bool:
    n = str(abs(n))   
    digits = [int(d) for d in str(n)]
    power= len(digits)
    return sum(d ** power for d in digits) == n

def get_properties(n: int):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("odd" if n % 2 != 0 else "even")
    return properties

def get_digit_sum(n: int) -> int:
    n = str(abs(n))
    return sum(int(d) for d in str(n))

def get_fun_fact(n: str):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact available.")
    except:
        return "No fun fact available."
    
#API endpoint
@app.get ("/api/classify-number")
async def classify_number(number: str = Query(..., description="The number to classify")):

    if number.isalpha():
        return JSONResponse (
            status_code=400,
            content = {
                "number": number,
                "error": True
            }
        )
    
    number = int(number)
    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": get_properties(number),
        "digit_sum": get_digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    return result