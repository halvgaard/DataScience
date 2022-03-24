# How to run this project

- cd into the main module ('helloworld'), here you find the Dockerfile, you can build the image by running
	`docker build -t YOURTAGNAME .`
		- For example `docker build -t helloworld:0.1`
- after the image is built, you can view by running `docker images`
- run the container by `docker run -p YOURPORT:YOURPORT --name CONTAINERNAME IMAGENAME`
		- For example `docker run -p 8000:8000 --name testcontainer helloworld:0.1`
- you can test the running app by `curl localhost:YOURPORT` which should give you `{'message':'Hello World'}` as a response

