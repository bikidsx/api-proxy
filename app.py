from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def proxy():
    try:
        url = request.args.get('url')  # Get the URL parameter from the request
        
        if not url:
            return jsonify({'error': 'URL parameter is missing.'}), 400
        
        response = requests.get(url)  # Make a GET request to the provided URL
        
        # Return the response from the API as JSON
        return jsonify(response.json())
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4009)
