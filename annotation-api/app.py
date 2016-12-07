#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
from flask import request
import requests

app = Flask(__name__)

info = [
    {
        'service': u'Annotate MNIST image',
        'description': u'Given an MNIST digit returns label', 
        'request': u'curl blah blah'
    }
]

images = [

]

@app.route('/annotation/api/v1.0/info', methods=['GET'])
def get_tasks():
    
    return jsonify({'info': info})

#@app.route('/annotation/api/v1.0/tasks/<int:task_id>', methods=['GET'])
#def get_task(task_id):
#    task = [task for task in tasks if task['id'] == task_id]
#    if len(task) == 0:
#        abort(404)
#    return jsonify({'task': task[0]})

@app.route('/annotation/api/v1.0/classify', methods=['POST'])
def create_task():
    if not request.json or not 'url' in request.json:
        abort(400)
    image = {
        'url': request.json['url'],
        'done': False,
        'label': 'unknown',
        'model': 'mnist_v1'
    }
    images.append(image)
    r = requests.get(image['url'])
    with open('test_file.png', 'wb') as f:
        f.write(r.content)
    return jsonify({'image': image}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
