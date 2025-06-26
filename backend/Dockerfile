FROM python:3.10-slim

WORKDIR /app

COPY backend/ .  # ⬅️ Only copy the contents of backend folder

RUN ls -l

RUN pip install flask flask-cors

EXPOSE 5000

CMD ["python", "app.py"]
