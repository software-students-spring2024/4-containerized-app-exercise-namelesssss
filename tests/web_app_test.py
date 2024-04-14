import pytest
import sys
sys.path.append("web-app")
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

'''
def test_transcribe_audio():
    file_path = "path"
    # this will be testing audio file
    print("transcribe_audio test has passed! ")
'''

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    print("home page test has passed!")

def test_analyze_passage(client):
    #  return jsonify({"fixed_passage": fixed_passage, "error_analysis": error_analysis})
    passage = "This is a test passage."
    response = client.post('/analyze', json={"passage": passage})
    assert response.status_code == 200
    res = response.json
    assert "fixed_passage" in res
    assert "error_analysis" in res
    print("analyze_passage test has passed!")

if __name__ == "__main__":
    test_analyze_passage(client)
    test_home_page(client)
    # test_transcribe_audio()