FROM python:3.10-slim

RUN adduser --disabled-password --gecos '' pyuser
USER pyuser

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
