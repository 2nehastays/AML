import os
import requests
import subprocess

def main():
    test_flask()

def test_flask():
    # Launch the Flask app
    subprocess.check_call(['docker', 'build', '-t', 'test-flask-app', '.'])

    container_id = subprocess.check_output(['docker', 'run', '-d', '-p', '5000:5000', 'test-flask-app']).decode().strip()

    os.system('python app.py &')

    
    # Test cases
    response = requests.post('http://127.0.0.1:5000/score')
    
    
    # Close the Flask app
    response = requests.post('http://127.0.0.1:5000/shutdown')
    subprocess.check_call(['docker', 'stop', container_id])

if __name__ == "__main__":
    main()
