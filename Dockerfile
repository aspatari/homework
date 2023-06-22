# Base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files into the container
COPY poetry.lock pyproject.toml ./

# Install poetry
RUN pip install --no-cache-dir poetry

# Install the Python dependencies using poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the application code into the container
COPY . .

# Expose the port that the FastAPI application will be listening on
EXPOSE 8000

# Run the FastAPI application with uvicorn when the container starts
CMD ["python","app.py"]
