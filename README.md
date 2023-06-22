# FastAPI Backend Application

This is a backend application built with FastAPI that provides endpoints for submitting and searching submissions. The application allows indexing and searching of submissions in memory without using a database.

## Endpoints

- `POST /api/v1/posts`: Submit a new post.
- `GET /api/v1/posts`: Search for post based on title and author.
- `GET /api/v1/posts/<post_id>`: Get a specific post by ID.
- `GET /api/v1/rss`: Generate an RSS feed of the latest post.

## Running the Application with Docker

To run the FastAPI application using Docker, follow these steps:

1. Install Docker on your machine if you haven't already. Refer to the Docker documentation for instructions on how to install Docker for your operating system.

2. Clone the repository and navigate to the project directory:

   ```bash
   git clone <repository_url>
   cd <project_directory>
   docker build -t homework .
   docker run -p 8000:8000 homework
   ```

3. Run generator for submission
   
   ```bash
    ./generator -submit-url=http://localhost:8000/api/v1/posts
   ```

 
4. Run generator for search
   
   ```bash
    ./generator -search-url=http://localhost:8000/api/v1/posts
   ```
