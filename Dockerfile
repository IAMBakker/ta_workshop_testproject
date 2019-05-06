FROM python:3.7-alpine3.8

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.8/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# install selenium
RUN pip install selenium==3.13.0

RUN useradd testcontainer
RUN mkdir /data &amp;&amp; touch /data/x
RUN chown -R testcontainer:testcontainer /data
VOLUME /data

WORKDIR /data
COPY . /data

RUN pip install -r Requirements.txt

# run all tests
CMD ["pytest Tests", "--junitxml=test-reports.xml"]
