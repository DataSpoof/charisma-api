Create a virtual environment
-- uv init
-- uv venv
-- .venv\Scripts\activate

Create a requirements.txt file which will contains all the libraries
-- uv add -r requirements.txt

Create model folder
-- copy the model.h5 file 
-- copy the scaler.pkl file

Create the app folder
-- Create the schema.py
-- Create a utils.py for data preprocessing
-- create a model_loader.py which load h5 and pickle file
-- Create the fastapi application (main.py)

Run the application
uvicorn app.main:app

Test the application using the pytest library
Hey chatgpt these are my codes can you create  the test script to test my apis using pytest

-- create the tests folder
-- create __init__.py file
-- create the test_api.py

Run this using pytest command

Dockerize the whole application 
-- create the Dockerfile
-- create the .dockerignore

Command to run
-- docker login
-- docker build -t charisma-api .
-- docker run -d -p 8000:8000 --name charisma-container charisma-api



