FROM python:3.8
RUN mkdir /server
WORKDIR /server
COPY requirements.txt /server/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . .