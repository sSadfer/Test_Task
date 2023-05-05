from app import app
from config import *

if __name__ == '__main__':
    app.run(debug=True, host=Config.host_for_flask, port=Config.port_for_flask)
