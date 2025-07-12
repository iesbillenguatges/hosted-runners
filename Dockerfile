FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask redis
EXPOSE 5000
CMD ["python", "redis_app.py"]
