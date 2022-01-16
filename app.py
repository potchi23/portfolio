import html
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html'), 200

@app.route('/terminal', methods=['GET'])
def command():
    status = 404
    if request.method == 'GET':
        command = request.args.get('command')

        data=''
        
        if (len(command) == 0):
            status = 200

        elif(command == 'clear'):
            with open('templates/components/welcome.html', 'r') as welcome:
                data += welcome.read()
            
            status = 302

        elif(command == 'about'):
            with open('templates/components/about.html', 'r') as about:
                data += about.read()

            status = 200

        elif(command == 'contact'):
            with open('templates/components/contact.html', 'r') as about:
                data += about.read()

            status = 200

        elif(command == 'skills'):
            with open('templates/components/skills.html', 'r') as about:
                data += about.read()

            status = 200

        else:
            data += '<p>-bash: ' + html.escape(command) + ': command not found</p>'

            status = 200
        
        with open('templates/components/command-line.html', 'r') as command_line:
                data += command_line.read()

        response = data
        return response, status


class FlaskConfig:

    ENV = 'production'
    DEBUG = False
    TEST = False

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


if __name__ == '__main__':
    app.config.from_object(FlaskConfig())

    app.run(host='0.0.0.0', port=5000)