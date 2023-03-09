import os
import requests

def main():
    test_flask()

def test_flask():
    # Launch the Flask app
    #os.system('python app.py &')
    
    # Test cases
    response = requests.post('http://127.0.0.1:5000/score')
    
    
    # Close the Flask app
    response = requests.post('http://127.0.0.1:5000/shutdown')
    #os.system('kill %1')

if __name__ == "__main__":
    main()
