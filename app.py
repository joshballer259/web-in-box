from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Joshua Krupa</h1>
    <h2>UVU Student ID: YOUR_STUDENT_ID</h2>
    <p>Welcome to my Web in a Box application!</p>
    """

@app.route("/api")
def api():
    return jsonify(
        student_id="11071973",
        course="Web in a Box",
        message="Hello from my Flask application!",
        meme="It works on my machine!"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)