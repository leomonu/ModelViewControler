from flask import Flask, json,jsonify,request
app = Flask(__name__)
tasks  = [
    {
        "id":1,
        "title":u"Buy Groceries",
        "description":u"Milk,Tea,Vegetables",
        "done": False
    },
    {
         "id":2,
         "title":u"Learn Python",
         "description":u"Learn Data Analysis",
         "done": False
         
    }
] 
@app.route("/add-data",methods = ["POST"])
def addTasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide the data",

        },400)
    task = {
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done": False
    }
    tasks.append(task)

    return jsonify({
        "status":"success",
        "message":"Task added successfully",
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks,

    })
    
if(__name__ == "__main__"):
    app.run(debug = True)