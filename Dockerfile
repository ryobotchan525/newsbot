FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip setuptools wheel && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "run:app"]
