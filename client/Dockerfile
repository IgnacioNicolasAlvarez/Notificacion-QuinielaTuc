FROM python:3.10

RUN adduser --disabled-password --gecos '' pyuser
USER pyuser

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED 1

CMD ["python", "scheduler.py"]
