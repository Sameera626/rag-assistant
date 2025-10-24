# Step 1: Use official Python image
FROM python:3.11-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy dependencies first
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy all frontend code
COPY . .

# Step 6: Expose Streamlit port
EXPOSE 8501

# Step 7: Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
