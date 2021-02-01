# FROM python:3.8
# RUN mkdir /server
# WORKDIR /server
# COPY requirements.txt /server/requirements.txt
# RUN pip install -r requirements.txt
# COPY . .
FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]