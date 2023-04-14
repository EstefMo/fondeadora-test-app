# Base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PORT=8000
ENV PYTHONUNBUFFERED=1
ENV WEB_CONCURRENCY=1
ENV APP_MODULE=main:app

# Expose port
EXPOSE $PORT

# Start server
CMD exec uvicorn --host=0.0.0.0 --port=$PORT --workers=$WEB_CONCURRENCY $APP_MODULE