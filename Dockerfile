#Use an official python runtime as parent image
FROM python:3.11-slim

#Set the working directory in the container
WORKDIR /app

#Copy the current directory contents into container at /app
COPY . /app

#Install any needed packages  specified  in requrements.txt
RUN pip install pyzmq

#Run client.py  when the container launches
CMD ["python","server.py"]
CMD ["python","client.py"]