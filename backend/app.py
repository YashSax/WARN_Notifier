from flask import Flask
import json
from datetime import datetime, timedelta

    
app = Flask(__name__)

states = ['ak','al','az','ca','co','ct','dc','de','fl','ga','hi','ia','id','il','in','ks','ky','la','md','me','mi','mo','mt','ne','nj','nm','ny','oh','ok','or','ri','sc','sd','tn','tx','ut','va','vt','wa','wi'] 

@app.route('/<state>')
def index(state):
    if state not in states:
        return f"Error: Invalid state. Must be one of: {states}"
    
    with open("./warn_data/update_dates.json", "r") as f:
        update_dates = json.load(f)
    
    curr_date = datetime.now().date()
    state_date = datetime.strptime(update_dates[state], "%Y-%m-%d").date()
    one_day = timedelta(days=1)

    if abs(state_date - curr_date) < one_day:
        df = 
    

if __name__ == "__main__":
    app.run(debug=True)
