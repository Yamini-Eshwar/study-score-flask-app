from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return "hello, welcome lets start learning flask"


if __name__ == "__main__":
    app.run(debug=True) # This is Flasks built-in server which is simple, good for learning, practise but not production.
                        # Its good only, but not good at handling many users or securing connections.
                        # So in real time, Flask app runs behind a WSGI Server (like Gunicorn)
                        # Then Nginx sits in front of Gunicorn and handles all incoming traffic
                        # Nginx passes requests to Gunicorn, and Gunicorn talks to your Flask app.




