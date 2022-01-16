import html
from flask import Flask, request, render_template

app = Flask(__name__)

history = []

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html'), 200

@app.route('/terminal', methods=['GET'])
def command():
    status = 404
    
    if request.method == 'GET':
        command = request.args.get('command')

        response=''

        if (len(command) == 0):
            status = 200

        else:
            history.append(command)
            command = command.split()[0]

            if(command == 'ls' or command == 'cd'):
                with open('templates/components/no_directory.html', 'r') as no_directory:
                    response += no_directory.read()
                
                status = 200

            elif(command == 'history'):
                response += '<p>'

                for h in history:
                    response += h + '</br>'

                response += '</p>'
                
                status = 200
            
            elif(command == 'neofetch'):
                with open('templates/components/neofetch.html', 'r') as welcome:
                    response += welcome.read()
                
                status = 200

            elif(command == 'clear'):
                with open('templates/components/welcome.html', 'r') as welcome:
                    response += welcome.read()
                
                status = 302

            elif(command == 'about'):
                with open('templates/components/about.html', 'r') as about:
                    response += about.read()

                status = 200

            elif(command == 'contact'):
                with open('templates/components/contact.html', 'r') as contact:
                    response += contact.read()

                status = 200

            elif(command == 'skills'):
                with open('templates/components/skills.html', 'r') as skills:
                    response += skills.read()

                status = 200
            
            else:
                response += '<p>-bash: ' + html.escape(command) + ': command not found</p>'

                status = 200
                    
        with open('templates/components/command_line.html', 'r') as command_line:
            response += command_line.read()

        return response, status


class FlaskConfig:

    ENV = 'development'
    DEBUG = True
    TEST = False

    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


if __name__ == '__main__':
    app.config.from_object(FlaskConfig())

    app.run(host='0.0.0.0', port=5000)