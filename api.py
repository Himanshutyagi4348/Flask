#put and delete --->>http verbs
#working with api---->json
from flask import Flask,request,jsonify
app=Flask(__name__)
##initiate data into my to do list
items=[
    {"id":1,"name":'item1',"description":'this is item 1'},
    {"id":2,"name":'item2',"description":'this is item 2'}
]

@app.route("/")
def home():
    return "Welcome to my first flask project : TO DO LIST"

##get: retrive all the 
@app.route("/items",methods=['GET'])
def get_items():
    return jsonify(items)

##get : retrive a specific item by id---->API
@app.route("/getitem/<int:id>",methods=['GET']) 
def get_item(id):
    item=next((item for item in items if item["id"]==id),None)
    if item is None:
        return jsonify({"error":'item is not found'})
    return jsonify(item)

# ##post : create a new task  
@app.route("/items",methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"Error":"item is not found"})
    new_item={
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json['name'],
        "description":request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)


##put : update an existing item
@app.route("/items/<int:item_id>",methods=['PUT'])
def update(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item==None:
        return jsonify({"error":'item is not found'})
    item["name"]=request.json.get("name",item["name"])
    item["description"]=request.json.get("description",item["description"])
    return jsonify(item)
##delete :delete an item
@app.route("/delete/<int:id>",methods=['DELETE'])
def delete_item(id):
    item=next((item for item in items if item["id"]!=id),None)
    return jsonify({"result":'item deleted'}) 



if __name__=="__main__":
    app.run(debug=True) 