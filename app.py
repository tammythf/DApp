
#1. Importing Models
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def serve_html():
    return send_from_directory('DAPP 241026', 'DApp Storage Space.html')

#2. For Render Deployment
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)