from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def hello():
    """
    This function return a welcome message.
    For default the route use a GET methos HTTP
    :return:
    """
    return 'Welcome to Flask'

@app.route('/welcome/<user>/<edad>')
def user(user, edad):
    """
    This function return a message with the username and age.
    For send arguments on the url, the arguments most be enclosed in square brackets
    :param user:
    :param edad:
    :return:
    """
    ip = request.remote_addr
    return 'Welcome {}, nos acabas de informar que tienes {} de edad y su ip es {}'.format(user, edad, ip)

@app.route('/request')
def request_function():
    """
    This function return a message with some atributes of the request object
    :param user:
    :param edad:
    :return:
    """
    return """<h2>A continuación se muestran algunos de los atributos del objeto request: </h2>
                <ul>                
                    <li><p><b>form:</b> <i>A dictionary with all the form fields submitted with the request.</i></p></li>
                    <li><p><b>args:</b> <i>A dictionary with all the arguments passed in the query string of the URL.</i></p></li>
                    <li><p><b>values:</b> <i>A dictionary that combines the values in form and args.</i></p></li>
                    <li><p><b>cookies:</b> <i>A dictionary with all the cookies included in the request.</i></p></li>
                    <li><p><b>headers:</b> <i>A dictionary with all the HTTP headers included in the request.</i></p></li>
                    <li><p><b>files:</b> <i>A dictionary with all the file uploads included with the request.</i></p></li>
                </ul>
             """

