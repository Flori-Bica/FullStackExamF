from flask_app.controllers import magazines, users
from flask_app import app

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5050)
