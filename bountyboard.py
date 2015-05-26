#!/bin/env python
from config import SERVER_NAME
from config import SERVER_PORT
from app import app

if __name__ == '__main__':
    # app.run(SERVER_NAME, int(SERVER_PORT), debug=True)
    app.run(debug=True)