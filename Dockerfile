FROM python:3.9-slim-buster

# Set environment variable for the app directory
ENV APP_HOME /app

# Create the app directory and set it as the working directory
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files to the container
COPY ./src .

# Expose the port that the app will run on
EXPOSE 8080

# Run the command to start the app
CMD ["waitress-serve", "--call", "app:create_app"]
