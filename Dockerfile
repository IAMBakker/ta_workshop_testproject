FROM python:3.7-alpine3.8

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.8/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# install selenium
RUN pip install selenium==3.13.0

COPY . /docker_test
WORKDIR /docker_test

# run all tests
CMD ["sh", "test.sh"]
RUN sleep 10
RUN ls
COPY /docker_test/test-reports.xml /output_folder