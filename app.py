from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Te funciona, maquina"

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
=======
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 9af9f5ae1c5721497b2e88aafb1a035a4150c48a
