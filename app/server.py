from flask import Flask, Response, request
from recommend import make_recommendations
import json

app = Flask(__name__)


# try:
#     mongo = pymongo.MongoClient(host="localhost", port=27017, serverSelectionTimeoutMS = 1000)
#     db = mongo.company
#     mongo.server_info()
# except:
#     print("ERROR - Cannot connect to DB")

#######################################
@app.route("/recommend", methods=["POST"])
def recommend_courses():
    data = request.get_json()
    res = make_recommendations(data["subjects"])
    if res == "invalid input":
        return Response(
            response = {
                "error": "invalid input format",
                "status": 400
            }
        )
    return Response(
        response=json.dumps({
            "recommendations": res
        })
    )

@app.route("/", methods=["GET"])
def home_route():
    return "Elective subject recommendation"


#######################################

