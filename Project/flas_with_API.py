from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hellow World!"


@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n 
    while(n>0):
        digit = n%10
        sum += digit **order
        n //= 10
        
    if(sum == copy_n):
        print(f"{copy_n} is an armstrong number")
        result ={
            "Number": copy_n,
            "Armstrong": True,
            "Server Ip": "122.234.213.53"
        }
    else:
        print(f"{copy_n} is not an armstrong number")
        result ={
            "Number": copy_n,
            "Armstrong": False,
            "Server Ip": "122.234.213.53"
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug= True)