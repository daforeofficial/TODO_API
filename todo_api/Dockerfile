FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Copy requirements and install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /code/

EXPOSE 8000

# Use gunicorn to run the Django application
CMD ["gunicorn", "--bind", "127.0.0.1:8000", "todo_api.wsgi:application"]
