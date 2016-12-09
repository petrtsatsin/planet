# planet test task

Goal: Write a web service to calssify MNIST images.

## Implementation
I used flask and caffe for image processing.

## Requirements

flask, caffe

## How to run
I assume the you have caffe and flask installed.
Clone repository:
git clone 
To run server localy:
cd planet/annotation-api
export FLASK_APP=app
flask run
Query a localhost
curl -i -H "Content-Type: application/json" -X POST -d '{"url":"https://s3.amazonaws.com/petrtsatsin/mnist/test.png"}' http://localhost:5000/annotation/api/v1.0/classify
curl -i -H "Content-Type: application/json" GET http://localhost:5000/annotation/api/v1.0/info

If you don't want to installanithing I provide an public ami with everything preinstalled and latest version on the app.
Just create a EC2 machine from this ami. It will work on free tier micro instances.
cd to /ubuntu/planet/annotation-api
export FLASK_APP=app
fask run
Queries are same as before.

If don't want to create an EC2 instance I actually have the application deployed on EC2. 
Just query:
curl -i -H "Content-Type: application/json" -X POST -d '{"url":"https://s3.amazonaws.com/petrtsatsin/mnist/test.png"}' ec2-54-161-187-164.compute-1.amazonaws.com:9001/annotation/api/v1.0/classify

