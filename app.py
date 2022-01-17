import json
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html'), 200

@app.route('/terminal', methods=['GET'])
def command():

    if request.method == 'GET':
        command = request.args.get('command')
        history = json.loads(request.args.get('history'))

        if (len(command) == 0):
            return render_template('components/command_line.html'), 200

        else:
            command = command.split()[0]

            if(command == 'ls' or command == 'cd'):
                return render_template('components/no_directory.html'), 200

            elif(command == 'history'):
                return render_template('components/history.html', history=history),200
            
            elif(command == 'neofetch'):
                return render_template('components/neofetch.html'), 200      

            elif(command == 'clear'):
                return render_template('components/welcome.html'), 302

            elif(command == 'about'):
                return render_template('components/about.html'), 200

            elif(command == 'contact'):
                return render_template('components/contact.html'), 200

            elif(command == 'skills'):
                return render_template('components/skills.html'), 200

            elif(command == 'help'):
                return render_template('components/help.html'), 200
            
            else:
                return render_template('components/command_not_found.html', command = command), 200

class FlaskConfig:

    ENV = 'development'
    DEBUG = False
    TEST = False

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

if __name__ == '__main__':
    app.config.from_object(FlaskConfig())

    app.run(host='0.0.0.0', port=5000)