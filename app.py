from flask import Flask, request, jsonify
import json
import requests as r
import os

app = Flask(__name__)

botToken = os.environ['BOT_TOKEN']
ethan = os.environ['ETHAN_USER_ID']

@app.route('/', methods=['POST'])
def reactor():
    posted_data = json.loads(request.data)
    print posted_data # debugging statement
    if posted_data['type'] == 'url_verification':
        challenge = posted_data['challenge']
        return jsonify({'challenge': challenge})
    elif posted_data['type'] == "event_callback" and posted_data['event']['user'] == ethan:
        channel = posted_data['event']['channel']
        # print channel # debugging
        timestamp = posted_data['event']['ts']
        # print timestamp # debugging
        res = r.post('https://slack.com/api/reactions.add', data={
            'token':botToken,
            'name': 'older_man',
            'channel': channel,
            'timestamp': timestamp
        })
        print res.json()
        return 'ok', 200
    else:
        return 'not_correct_user_to_react_to', 204

if __name__ == '__main__':
    app.run(
        debug = True
    )