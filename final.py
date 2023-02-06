import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine 
 
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'dbtestmongo',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)
#establishing connection to database 
class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}
#row name 
@app.route('/')
def query_records():
    name = 'Satyamgupta'
    user = User.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())
		
if __name__ == "__main__":
    app.run(debug=True)		
