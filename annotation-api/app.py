from flask import Flask, jsonify, abort, make_response
from flask import request
import requests
import os
from PIL import Image
from StringIO import StringIO
import numpy as np

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

caffe_root = '/home/ubuntu/caffe/'  # this file is expected to be in {caffe_root}/examples/caffe-test-mnist-jpg/
import caffe

if not os.path.isfile(caffe_root + 'examples/mnist/lenet_iter_10000.caffemodel'):
    print("Cannot find trained caffemodel...")

caffe.set_mode_cpu()
net = caffe.Net(caffe_root + 'examples/mnist/lenet.prototxt',
                caffe_root + 'examples/mnist/lenet_iter_10000.caffemodel',
                caffe.TEST)

net.blobs['data'].reshape(1,1,28,28)

def save_image(r, name):
    with open(name, 'wb') as f:
        f.write(r.content)

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
    save_image(r,"test_image2.jpg")
    img = Image.open(StringIO(r.content))
    arr = np.array(img) 
    print arr.shape 
    tmp=arr[:,:,0]
    if (tmp.shape[0] != 28 or tmp.shape[1] != 28):
        abort(400)
    else:
        #temp=tmp.reshape(1,1,28,28)
        net.blobs['data'].data[...] =tmp;
        out = net.forward()
        print("Predicted class is #{}.".format(out['prob'].argmax()))
        image['done'] = True
        image['label'] = out['prob'].argmax()
    return jsonify({'image': image}), 201

@app.route('/annotation/api/v1.0/images')
def hello(name=None):
    return render_template('images.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

if __name__ == '__main__':
    app.run(debug=True)
