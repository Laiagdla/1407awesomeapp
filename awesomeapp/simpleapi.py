#----- imports ---
from fastapi import FastAPI


#----- body or main -------
api = FastAPI()

#
# Define a root `/` endpoint
# 'http://localhost:8000/'
@api.get('/')
def index():
    return {'status': 'online'}

# 'http://localhost:8000/hi'
@api.get('/hi')
def hello():
    return 'hi'

# 'http://localhost:8000/calculator'
@api.get('/calculator')
def simplecalculator(x: int, y: int):
    return x + y

# this two lines of code are equivalent, but requests.get and api is making us able to run code over the internet
# calculated_value = simplecalculator(x, y)
# response = requests.get("http://127.0.0.1:8000/calculator?x=5&y=10").json()

#------------ testing on terminal --------------
if __name__ == "__main__":
    print(hello())
    print('our app is working')
    x = int(input('define x:'))
    y = int(input('define y:'))
    print(simplecalculator(x, y))
