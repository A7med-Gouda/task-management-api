# 1. Use official Python image
FROM python:3.11

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy all project files
COPY . .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Run the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
