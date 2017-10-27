FROM nikolaik/python-nodejs:latest

WORKDIR /app

ADD package.json /tmp
ADD requirements.txt /app

RUN pip install -r requirements.txt && cd /tmp && npm install

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
# cp -rf /tmp/node_modules app/.
CMD ["python3", "app.py"]
