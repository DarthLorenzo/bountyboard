#!/bin/env python
import os
from app import app

if __name__ == '__main__':
    app.run(os.getenv('SERVER_NAME'), int( os.getenv('SERVER_PORT') ), debug=True)
