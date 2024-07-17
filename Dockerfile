# Selecting the base image to create a docker container
FROM python:3.8

# Setting the working dir
WORKDIR /usr/local/app

# Creating a user
RUN useradd app

# Copying the Requirements file and installing the dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copying all the files
COPY . ./

# Giving the necessary permissions 
RUN chmod +x run.sh
RUN chown -R app:app .

USER app
# Exposing the port to access from the frontend
EXPOSE 7755


RUN rm core/store.sqlite3 && export FLASK_APP=core/server.py &&flask db upgrade -d core/migrations

CMD ["bash", "run.sh"]