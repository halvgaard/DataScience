# Run this project

Create a containerized FastAPI app with one endpoint that returns `Hello World`

1. Build the docker image by running:`docker build -t YOURTAGNAME .`
	- For example `docker build -t helloworld:0.1 .`
2. After the image is built, you can view it by running: `docker images`
3. Run a new container: `docker run -p YOURPORT:YOURPORT --name CONTAINERNAME IMAGENAME`
	- For example `docker run -p 8000:8000 --name testcontainer helloworld:0.1`
4. Test the running app: `curl localhost:YOURPORT` which should give: `{'message':'Hello World'}`  as a response
	- For example `curl localhost:8000`

