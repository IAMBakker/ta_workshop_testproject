FROM python:3.7-alpine3.8

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.8/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories


# install chromedriver
RUN apk update
RUN apk add firefox

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
RUN tar -xvzf geckodriver*
RUN chmod +x geckodriver
RUN mv geckodriver /usr/local/bin/
#RUN apk add chromium chromium-chromedriver


# install selenium
RUN pip install selenium==3.13.0

RUN mkdir /output_folder
VOLUME /output_folder

COPY . /docker_test
WORKDIR /docker_test

RUN pip install -r requirements.txt

CMD pytest --junitxml=/output_folder/test-reports.xml