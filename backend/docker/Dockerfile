FROM python:3.13.2

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . . 

CMD ["uvicorn", "bin.main:create_app","--host", "0.0.0.0", "--port", "8000", "--reload"]