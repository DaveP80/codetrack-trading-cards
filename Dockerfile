FROM python:3.11-alpine
# update apk repo
RUN apk update
RUN apk add chromium chromium-chromedriver
# upgrade pip
RUN pip install --upgrade pip setuptools
# install selenium
RUN pip install selenium
# Copy the requirements.txt file to /app
COPY requirements.txt /app/requirements.txt
# Install Python dependencies listed in requirements.txt
RUN pip install -r /app/requirements.txt
# Copy the Python script 'app.py' to /app
COPY main.py /app/
COPY open_gen.py /app/
WORKDIR app/
# Specify the default command to execute when the container starts
ENTRYPOINT [ "python3", "main.py"]