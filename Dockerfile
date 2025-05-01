from python:3.11-slim
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app/
CMD ["daphne", "quant_admin.asgi:application"]