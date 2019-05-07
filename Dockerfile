FROM python:3.7-alpine3.8

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.8/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# install selenium
RUN pip install selenium==3.13.0

RUN mkdir /var/lib/jenkins/workspace/ta_workshop/ta_workshop_testproject/dc && \
touch /var/lib/jenkins/workspace/ta_workshop/ta_workshop_testproject/dc/x
RUN chown -R jenkins:jenkins /var/lib/jenkins/workspace/ta_workshop/ta_workshop_testproject/dc
VOLUME /var/lib/jenkins/workspace/ta_workshop/ta_workshop_testproject/dc

WORKDIR /var/lib/jenkins/workspace/ta_workshop/ta_workshop_testproject/dc
COPY . /var/lib/jenkins/workspace/ta_workshop/ta_workshop_testproject/dc

RUN pip install -r Requirements.txt

# run all tests
CMD ["pytest Tests", "--junitxml=test-reports.xml"]
