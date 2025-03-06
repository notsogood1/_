FROM python:3.9-slim-buster

WORKDIR /workspace

COPY backend/requirements.txt backend/

RUN pip install --no-cache-dir -r backend/requirements.txt

COPY . .

EXPOSE 5000
