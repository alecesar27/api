FROM python:3.9-slim

WORKDIR D:/desafio_verx/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["fastapi", "dev", "main.py", "--port=80"]