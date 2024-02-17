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

# response = request.get("http://127.0.0.1:8000/calculator?x=5&y=10")
# calculated_value = simplecalculator(x, y)

#------------ testing on terminal --------------
if __name__ == "__main__":
    print(hello())
    print('our app is working')
    x = int(input('define x:'))
    y = int(input('define y:'))
    print(simplecalculator(x, y))
