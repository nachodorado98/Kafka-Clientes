FROM python:3.10-slim

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y nano

# Solventa error de psycopg2
RUN apt-get update \
	&& apt-get install -y libpq-dev gcc \
	&& rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "run:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
