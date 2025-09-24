# Import the Flask class
from flask import Flask

# Create the Flask application object
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    # This function runs when someone visits the root URL
    return "<h1>Bazinga!</h1><p>Hello from Sheldon’s first Flask app on Azure.</p>"

# Entry point for running the app locally
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
