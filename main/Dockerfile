FROM python:2.7-slim
WORKDIR /app
ADD . /app
RUN pip install -r requirements
EXPOSE 80

CMD ["python", "myapp.py"]
