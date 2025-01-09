from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    pod_name = os.getenv('POD_NAME', 'Unknown Pod')
    #return f'This is the pod: {pod_name}'
    #return f'Hello'
    return f'''
    <html>
        <head>
            <title>Pod Info</title>
        </head>
        <body style="background-color: green; color: white; text-align: center; padding-top: 20%;">
            <h1>Hello, the pod name is {pod_name}</h1>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
