"""
Test script for the GET /meetings endpoint.
Verifies that the endpoint returns properly formatted meeting data.
"""
import requests
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_list_meetings():
    """Test the GET /meetings endpoint."""
    print("Testing GET /meetings endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/meetings")
        
        # Check status code
        if response.status_code != 200:
            print(f"❌ FAILED: Expected status 200, got {response.status_code}")
            return False
        
        print(f"✅ Status code: {response.status_code}")
        
        # Parse JSON response
        data = response.json()
        
        # Check for required keys
        if "meetings" not in data:
            print("❌ FAILED: Response missing 'meetings' key")
            return False
        
        if "count" not in data:
            print("❌ FAILED: Response missing 'count' key")
            return False
        
        print(f"✅ Response structure correct")
        print(f"✅ Found {data['count']} meetings")
        
        # Check each meeting has required fields
        for idx, meeting in enumerate(data["meetings"]):
            if "id" not in meeting:
                print(f"❌ FAILED: Meeting {idx} missing 'id'")
                return False
            if "created_at" not in meeting:
                print(f"❌ FAILED: Meeting {idx} missing 'created_at'")
                return False
            if "transcript_preview" not in meeting:
                print(f"❌ FAILED: Meeting {idx} missing 'transcript_preview'")
                return False
            
            # Verify preview is truncated (max 203 chars including "...")
            preview_len = len(meeting["transcript_preview"])
            if preview_len > 203:
                print(f"❌ FAILED: Meeting {idx} preview too long ({preview_len} chars)")
                return False
        
        if data["count"] > 0:
            print(f"✅ All {data['count']} meetings have correct structure")
            print(f"\nSample meeting:")
            print(f"  ID: {data['meetings'][0]['id']}")
            print(f"  Created: {data['meetings'][0]['created_at']}")
            print(f"  Preview: {data['meetings'][0]['transcript_preview'][:50]}...")
        else:
            print("ℹ️  No meetings in database (empty list is valid)")
        
        print("\n✅ ALL TESTS PASSED!")
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ FAILED: Could not connect to server at http://127.0.0.1:8000")
        print("Please make sure the server is running with: uvicorn app.main:app --reload")
        return False
    except Exception as e:
        print(f"❌ FAILED: {type(e).__name__}: {e}")
        return False

if __name__ == "__main__":
    success = test_list_meetings()
    sys.exit(0 if success else 1)
