FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt ./
RUN python -m pip install --upgrade pip setuptools wheel \
	&& pip install --no-cache-dir -r requirements.txt
COPY . .

# manage.py lives in the `listador_jogos/` directory in this repo
RUN python listador_jogos/manage.py collectstatic --noinput
RUN python listador_jogos/manage.py migrate
EXPOSE 8000
CMD ["python", "listador_jogos/manage.py", "runserver", "0.0.0.0:8000"]