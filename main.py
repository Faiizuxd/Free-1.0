from flask import Flask

app = Flask(__name__)

@app.route('/')
def hacked_message():
    return '''
    <html>
    <head>
        <title>Server Hacked</title>
        <style>
            body {
                background-color: black;
                color: red;
                font-size: 40px;
                font-weight: bold;
                text-align: center;
                margin-top: 20%;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        This server fucked by faiizu
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
