"""
Simple test script to verify the API endpoints are working.
Run this after starting the API server.
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_endpoints():
    print("Testing API endpoints...\n")
    
    # Test root endpoint
    print("1. Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}\n")
    
    # Test project ideas endpoint
    print("2. Testing project ideas endpoint...")
    payload = {
        "course": "BTech CSE",
        "academic_year": 3,
        "difficulty_level": "All",
        "project_type": "both"
    }
    response = requests.post(f"{BASE_URL}/projects", json=payload)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        projects = response.json()
        print(f"   Found {len(projects)} projects")
        if projects:
            print(f"   First project: {projects[0]['title']}")
    print()
    
    # Test hackathons endpoint
    print("3. Testing hackathons endpoint...")
    response = requests.get(f"{BASE_URL}/hackathons?months_ahead=3")
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        hackathons = response.json()
        print(f"   Found {len(hackathons)} hackathons")
    print()
    
    # Test SIH endpoint
    print("4. Testing SIH problems endpoint...")
    response = requests.get(f"{BASE_URL}/sih")
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        problems = response.json()
        print(f"   Found {len(problems)} SIH problems")
    print()
    
    # Test success prediction
    print("5. Testing success prediction...")
    params = {
        "course": "BTech AI",
        "project_title": "Fake News Detection System",
        "difficulty": "Beginner",
        "hardware_required": "None"
    }
    response = requests.get(f"{BASE_URL}/predict-success", params=params)
    print(f"   Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"   Success Percentage: {result['success_percentage']}%")
    print()
    
    print("All tests completed!")

if __name__ == "__main__":
    try:
        test_endpoints()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Make sure the server is running on http://localhost:8000")
        print("Start the server with: python api.py")

