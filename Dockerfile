FROM python:3.7-alpine3.8

# update apk repo - alpine linux package repos
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.8/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories

RUN apk update
RUN apk add postgresql-dev

# creating an output directory which will be assigned a volume during runtime (jenkins workspace)
RUN mkdir /output_folder
VOLUME /output_folder

# creating a workspace directory where the test project will be built
COPY . /docker_test
WORKDIR /docker_test

# let pip retrieve dependencies
RUN pip install -r requirements.txt

# the command that will be executed when we run the container
CMD pytest -s -v --junitxml=/output_folder/test-reports.xml