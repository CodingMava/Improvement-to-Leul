# 1. Grab a lightweight version of Python
FROM python:3.9-slim

# 2. Create a folder inside the container called /app
WORKDIR /app

# 3. Copy your requirements file into the container
COPY requirements.txt .

# 4. Install Flask
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your files (app.py and the templates folder)
COPY . .

# 6. Expose port 5000 so the outside world can see the UI
EXPOSE 5000

# 7. The command to start the app
CMD ["python", "app.py"]