FROM python:3.11-slim
COPY buyer.py .
CMD ["python3", "buyer.py"]