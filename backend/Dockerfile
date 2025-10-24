# step 1: Use a official Python image
FROM python:3.11-slim

# step 2: Set working directory
WORKDIR /app

# step 3: Copy dependencies first
COPY requirements.txt .

# step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# step 5: Copy all backend code
COPY . .

# step 6: Expose backend port
EXPOSE 8000

# step 7: Run FastAPI server
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]


