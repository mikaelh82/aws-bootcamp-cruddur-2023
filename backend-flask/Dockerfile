# Use a lightweight Python 3.10 image
FROM python:3.10-slim-buster

# Set the working directory inside the container
WORKDIR /backend-flask

# Copy requirements file to the container and install dependencies
COPY requirements.txt .
# Install OpenTelemetry bootstrap and required packages first

RUN pip install --upgrade pip

# Install all dependencies, including the updated requirements.txt with OpenTelemetry instrumentation libraries
RUN pip install -r requirements.txt
COPY . .

# Set environment variables (these can be overridden by Docker Compose or runtime)
ENV FLASK_ENV=development
ENV PORT=4567
# Use * for permissive CORS, but you should override this for specific URLs in production
ENV BACKEND_URL=*
ENV FRONTEND_URL=*

# Expose the port to other containers (not the host, that's handled by docker-compose)
EXPOSE ${PORT}

# Command to run the Flask application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=4567"]