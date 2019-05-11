# Use an official Python runtime as an image
FROM python:3.7-alpine

# Sets the working directory for following COPY and CMD instructions
WORKDIR /app

# Copy the src directory and requirement file
COPY src ./src
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "src/server.py"]