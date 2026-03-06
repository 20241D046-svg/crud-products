FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN flake8 .
RUN PYTHONPATH=. pytest --maxfail=1 --disable-warnings -q

EXPOSE 8000

CMD ["python", "-c", "import crud; print('CRUD app ready')"]