FROM python:3.13.2-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --retries 10 --timeout 60 -r requirements.txt


COPY . . 

CMD ["uvicorn", "bin.main:create_app","--host", "0.0.0.0", "--port", "8000", "--reload"]