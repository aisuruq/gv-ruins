FROM python:3.12.10-slim

RUN apt-get update && apt-get install -y build-essential libpq-dev

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 

CMD ["uvicorn", "bin.main:create_app","--host", "0.0.0.0", "--port", "8000", "--reload"]