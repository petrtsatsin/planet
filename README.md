# planet test task

Goal: Write a web service to calssify MNIST images.

## Implementation
I used flask and caffe for image processing.

## Requirements

flask, caffe

## How to run
I assume the you have caffe and flask installed.
Clone repository ```git clone```. 

To run server localy:
```{r, engine='bash', count_lines}
cd path/to/planet/annotation-api 
export FLASK_APP=app
flask run
```
Query a localhost
```{r, engine='bash', count_lines}
curl -i -H "Content-Type: application/json" -X POST -d '{"url":"https://s3.amazonaws.com/petrtsatsin/mnist/test.png"}' http://localhost:5000/annotation/api/v1.0/classify
curl -i -H "Content-Type: application/json" GET http://localhost:5000/annotation/api/v1.0/info
```

If you don't want to install anithing I provide public am `ami-d16e6ec6` with everything preinstalled and latest version of the app.
Just create a EC2 machine from this ami. It will work on free tier micro instances.
```{r, engine='bash', count_lines}
ssh to your ec2 machine
cd to /ubuntu/planet/annotation-api
export FLASK_APP=app
flask run
```
Queries are same as before.

If don't want to create an EC2 instance I actually have the application deployed on EC2. 
Just query:
```{r, engine='bash', count_lines}
curl -i -H "Content-Type: application/json" -X POST -d '{"url":"https://s3.amazonaws.com/petrtsatsin/mnist/test.png"}' ec2-54-161-187-164.compute-1.amazonaws.com:9001/annotation/api/v1.0/classify
```
###Any Questions:
Ping me at ptsatsin@gmail.com
