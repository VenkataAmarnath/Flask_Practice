# put and delete
# Work with API-(working with JSON)
# What am I developing?
# To-do List app

from flask import Flask, request,jsonify
app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to The sample Flask application for To-Do list"

## Initial data in my To-do list

items=[
    {'id':1,'name':"item1","description":"This is item 1"},
    {'id':2,'name':"item2","description":"This is item 2"}
     ]

# Get : Retrieve all the items
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)  # returns all the items in form of json

# retrieve specific item based on id

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item_id(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({'error':'item not found'})
    return jsonify(item)

#post: create new task/otem

@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({'error':'error'})
    new_item={
        'id':items[-1]['id']+1 if items else 1,
        'name':request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)

    return jsonify(new_item)


# Put: We update existing item
# here diff between post and put:
# POST: We are creating a new task
# PUT: We update existing task
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)

    if item is None:
        return jsonify({"error":"Item not found"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])
    return jsonify(item)



# delete: delete based on item id
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items=[item for item in items if item['id']!=item_id]
    #return jsonify({'result':'Item deleted'})
    return jsonify(items)
if __name__=='__main__':
    app.run(debug=True)
