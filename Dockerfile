FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV OPENAI_API_KEY=""
ENV GOOGLE_MAPS_API_KEY=""

# Default command to show help
CMD ["python3", "code/run_experiment.py", "--help"] 