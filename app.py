import os
from datetime import datetime

from flask import Flask, send_from_directory

app = Flask(__name__)

app.config['UPLOAD_DIRECTORY'] = './'
filename = "easter_egg"

@app.route('/download', methods=['GET'])
def get_file():
    return send_from_directory(app.config['UPLOAD_DIRECTORY'], filename, as_attachment=True)

@app.route('/time/<filename>')
def get_current_time_file(filename):
    filename = filename + ".txt"
    with open(filename, 'w') as f:
        current_time = str(datetime.now())
        f.write(current_time)

    return send_from_directory(app.config['UPLOAD_DIRECTORY'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=27015)
