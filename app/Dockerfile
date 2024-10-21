FROM python:3.9-slim

WORKDIR D:/desafio_verx/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "dev", "main.py", "--host=127.0.0.1", "--port=8000"]