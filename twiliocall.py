from twilio.rest import Client
from flask import Flask, redirect, url_for,render_template
app= Flask(__name__)
import os

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/oncall")
def click():
    account_sid = 'ACe97016ec1e8b3ad790572a389c0cda'
    auth = '03db640dc6a105d6fd4c850162e58407'
  
    client = Client(account_sid, auth)

    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to='+918746878795',
                            from_='+918747917217'
                        )

    print(call.sid)
    return render_template('in.html')
    

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure




if __name__=="__main__":
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
    
