__author__ = 'shaloba'


from application import app
from application import controllers

if __name__ == '__main__':
    """
        Running the service
    """
    app.run(host=app.config['HOST'], port=app.config['PORT'])
