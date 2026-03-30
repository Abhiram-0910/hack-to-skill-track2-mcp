FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# We run adk web on the current directory, it will find the 'release_notes_agent' package
CMD ["sh", "-c", "adk web --host 0.0.0.0 --port ${PORT:-8080}"]
