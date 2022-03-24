#How to build a docker image (build hello world using FastAPI) in a container

1. Create the app (src/main.py)
2. Create requirements.txt 
3. Create Dockerfile (touch Dockerfile)
--- Add which python you use (FROM python:3)
--- Copy the whole src folder into /app/src (COPY ./src app/src)
--- Copy the requirements also into /app (COPY ./requirements.txt /app)
--- Install the requirements (RUN pip3 install -r requirements.txt)
--- Define a port (EXPOSE 8000)
--- Run a command to start the server (CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]

4. Build the image (docker build -t fastapi-hello-world:0.1 .)
--- Here -t is a tag you give it 
--- We need to be in the same folder as is the Dockerfile
5. Run the image (docker run -p 8000:8000 --name my-api fastapi-hello-world:0.1)--- --name is also a variable
6. Test it (curl localhost:8000) => {'message': 'Hello World'}


