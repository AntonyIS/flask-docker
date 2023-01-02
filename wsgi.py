from flask import Flask
import redis
import pickle


app = Flask(__name__)
db = redis.StrictRedis(
    host='redis-server', 
    port=6379, db=0
    )
data = {
    "count" : 0
}
db.set("visits", pickle.dumps(data))

@app.route("/")
def home():
   
    visits = pickle.loads(db.get('visits'))
    count = visits['count'] 
    v = count
    visits['count'] +=1 
    db.set('visits',pickle.dumps(visits) )
    return {
        "visits": v
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0')