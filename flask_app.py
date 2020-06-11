from flask import Flask, jsonify, request

app = Flask(__name__)

# creating our inventory items
inventory = [
    {'item_id' : '1',
    'item_name' : 'soda',
    'item_price' : 100,
    'item_quantity' : 40},

    {'item_id' : '2',
    'item_name' : 'crisps',
    'item_price' : 75,
    'item_quantity' : 24},

    {'item_id' : '3',
    'item_name' : 'biscuits',
    'item_price' : 250,
    'item_quantity' : 93},
]

# displaying all items
@app.route('/snacks/all', methods=['GET'])
def getAllSnacks():
    return jsonify(inventory)

# to get a specific item based on its id
@app.route('/snacks/<snack_id>', methods=['GET'])
def getSnack(snack_id):
    snack_list = [snack for snack in inventory if (snack['item_id'] == snack_id)]
    return jsonify(snack_list)

# to update an existing item
@app.route('/snacks/<snack_id>', methods=['PUT'])
def updateSnack(snack_id):
    snack_list = [ snack for snack in inventory if (snack['item_id'] == snack_id)]
    if 'item_name' in request.json:
        snack_list[0]['item_name'] = request.json['item_name']
    if 'item_price' in request.json:
        snack_list[0]['item_price'] = request.json['item_price']
    if 'item_quantity' in request.json:
        snack_list[0]['item_quantity'] = request.json['item_quantity']
    return jsonify(snack_list[0])

# to create a new item
@app.route('/snacks/all', methods=['POST'])
def createSnack():
    new_item = {
    'item_id' : request.json['item_id'],
    'item_name' : request.json['item_name'],
    'item_price' : request.json['item_price'],
    'item_quantity' : request.json['item_quantity']
    }
    inventory.append(new_item)
    return jsonify(new_item)

# to delete an item
@app.route('/snacks/<snack_id>', methods=['DELETE'])
def deleteSnack(snack_id):
    snack_list = [ snack for snack in inventory if (snack['item_id'] == snack_id)]
    if len(snack_list) == 0:
        abort(404)

    inventory.remove(snack_list[0])
    return jsonify('Success! Item deleted.')


# to run our app
if __name__ == "__main__":
    app.run(debug = True)
