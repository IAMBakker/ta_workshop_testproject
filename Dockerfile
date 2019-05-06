FROM python:3.7-alpine3.8

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.8/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# install selenium
RUN pip install selenium==3.13.0

COPY . /tests
WORKDIR /tests
RUN pip install -r requirements.txt

CMD ["python", "-m", "unittest", "discover", "-s", "./Tests/API/", "-p", "*Test.py"]

#CMD ["python", "-m", "unittest", "discover", "-s", "./Tests/UI/", "-p", "*Test.py"]
