from flask import Flask, request, Response
import json

# 일부 과정 생략 

app = Flask(__name__)
 
@app.route('/analysis', methods=['GET', 'POST'])
def create():
    payload = request.json
    print(payload)

    description = payload['child']
    print(description)
    
    emotions = predict(description)
    emotions = emotions[0]
    results = { 
     "pleasure" : str(emotions[0]),
     "anxiety" : str(emotions[1]),
     "sorrow" :str(emotions[2]),
     "embarrassed" : str(emotions[3]),
     "anger" : str(emotions[4]),
     "hurt" : str(emotions[5])
     }
    json_data = json.dumps(results)
    response = Response(json_data, content_type='application/json')

    return response

app.run(port=7000)