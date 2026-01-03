"""
Quick start script for the AI Project & Hackathon Assistant API
Run this file to start the API server.
"""
import uvicorn

if __name__ == "__main__":
    print("Starting AI Project & Hackathon Assistant API...")
    print("API will be available at: http://localhost:8000")
    print("API Documentation at: http://localhost:8000/docs")
    print("Alternative docs at: http://localhost:8000/redoc")
    print("\nPress Ctrl+C to stop the server\n")
    
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

