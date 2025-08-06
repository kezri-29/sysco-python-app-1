from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def infoUrl():
    return jsonify({
        'time': datetime.datetime.now().isoformat(),
        'hostname': socket.gethostname(),
        'message': 'Hello, this is a sample Python Flask application.',
        'deployment': 'kubernetes',
        'env' : 'dev',
        'app_name': 'sysco-python-app-1'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

# '/api/v1/details --> basic details of the application'
# '/api/v1/healthz --> for checking kubernetes health'
