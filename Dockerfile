From python:2.7

COPY . /app

WORKDIR /app

RUN pip install -r hey.txt

ENTRYPOINT ["python"]

CMD ["app.py"]