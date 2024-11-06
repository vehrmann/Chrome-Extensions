from flask import Flask, request, jsonify
from flask_cors import CORS
from deutschland.bundesanzeiger import Bundesanzeiger

app = Flask(__name__)
CORS(app)

@app.route('/solve-captcha', methods=['POST'])

def solve_captcha():
    data = request.get_json()
    captcha_src = data.get('text', '')

    ba = Bundesanzeiger()
    img_response = ba._Bundesanzeiger__get_response(captcha_src)
    captcha_content = ba.captcha_callback(img_response.content)
    return jsonify({'result': captcha_content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)