# 1. Use an official Python "Base Image"
FROM python:3.11-slim

# 2. Set the "Working Directory" inside the container
WORKDIR /app

# 3. Copy the list of libraries (requirements.txt) first
# This makes building faster in the future
COPY requirements.txt .

# 4. Install the libraries
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your backend code (like main.py) into the container
COPY . .

# 6. Tell the container to run your FastAPI app when it starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]