from uvicorn import run

if __name__ == "__main__":
    run(
            "server.api:app",
            host="localhost",
            port=8000,
            reload=True
    )
