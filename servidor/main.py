from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Joder, toca reiniciar el servidor para que tome los cambios. :('


if __name__ == "__main__":
    app.run()
