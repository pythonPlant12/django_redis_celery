# I recommend alpine to use for containerised environments as it is lightweight Linux
# distribution and it is also focused on security 
FROM python:3.11.4-alpine

# Defining a work directory inside the image
WORKDIR /usr/src/app

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Ensure Python output is sent directly to the terminal without buffering 
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements file to the app directory on building image 
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# I'll COPY entrypoint file with will be executed everytime I run a container
# Also, I run in a terminal chmod+x ./entrypoint.sh to make sure that I have
# and execute permissions of this file
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

# I'll specify the path to the entrypoint file
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
