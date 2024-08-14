# Metrics-Pipeline
Overview

A data ingestion pipeline that captures and stores user metrics such as talked_time, microphone_used, speaker_used, and voice_sentiment in a PostgreSQL database. Built with Flask and Docker.

Setup

Prerequisites
Docker & Docker Compose
Postman or a similar tool for testing API endpoints
Quick Start
Clone the Repository: Get the project files onto your local machine.
Build and Run: Use Docker Compose to set up and launch the Flask app and PostgreSQL database.
Verify the Database: Ensure the database is initialized and tables are set up.
Ingest Data: Use Postman to send POST requests to the Flask API to ingest metrics.
Stop the Containers: Bring down the Docker containers when done.
Usage

Endpoints: Available for ingesting different types of metrics.
Database: Access the PostgreSQL database to view or manage the stored metrics.
Troubleshooting

404 Errors: Check that the correct URL is used and the Flask server is running.
Database Connection Issues: Ensure the environment variables are correctly configured and the PostgreSQL container is running.
Port Conflicts: Make sure required ports are available on your machine.
