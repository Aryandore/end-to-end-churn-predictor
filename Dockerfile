# 1. Start with a base generic Python image (like buying a blank laptop)
FROM python:3.9-slim

# 2. Create a folder inside the container
WORKDIR /app

# 3. Copy only the requirements first (for caching speed)
COPY requirements.txt .

# 4. Install the libraries inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your code (src and models) into the container
COPY . .

# 6. Open the door (Expose port 8000)
EXPOSE 8000

# 7. The command to run when the container starts
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]