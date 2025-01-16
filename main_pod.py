import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    pod_name = os.getenv("POD_NAME", "Unknown Pod")
    script = """
    fetch("https://api.thecatapi.com/v1/images/search").then(response => response.json()).then(data => {
        document.getElementById("cat").src = data[0].url;
    }).catch(error => {
        console.error("Error fetching cat image:", error);
    });
    """
    
    return f"""
    <html>
        <head>
            <title>Pod Info</title>
        </head>
        <body style="background-color: red; color: white; text-align: center; padding-top: 20%;">
            <h1>Hello, the pod name is {pod_name}</h1>
            <img src="" alt="" id="cat">
        </body>
        <script>
            {script}
        </script>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
