# The Beginner's Guide to Flask-CRUD

### Overview
I created this Flask web application of a simple snacks inventory as the first task of my Flask journey. It has basic CRUD (Create, Read, Update, Delete) functionalities or, as they are known in Flask lingo, POST, GET, PUT, and DELETE methods respectively. This repository contains just one file ***flask_app.py***, and I will explain how to go about working with this.

### Requirements
In order to run this file and explore the CRUD operations listed below, you need to have the following installed on your machine:
  - Python3
  - Postman (you can alternatively get the Chrome extension)
  
### Setting Up
1. Download this zip file onto your machine and extract the ***flask_app.py*** file to a folder or directory of your choice.
2. Open your terminal or command prompt. Navigate to the folder or directory containing this file.
3. Run this command: `python flask_app.py` . You should see a list of results starting with "Serving Flask app..." and ending with the Debugger PIN.
4. To preview the whole inventory in your browser, go to **`127.0.0.1:5000/snacks/all`** in a new tab.
5. However, I recommend using Postman to do this so as to save on switching back and forth between Postman and your browser. Go to Postman. Next to the "Launchpad" tab, click the + icon to open a new tab. In the URL field, input **`localhost:5000/snacks/all`** and click on the blue Send button.

### GET - to retrieve/read an item
##### A) To get the whole inventory
First ensure that the dropdown menu to the left of the URL field is set to GET. Then in the URL field, type **`localhost:5000/snacks/all`** and click on the blue Send button.

##### B) To get a specific item
Ensure the GET option is still in place then input **`localhost:5000/snacks/<id_number>`** in the URL field, replacing **<id_number>** with the item ID number you wish to see. If the ID number you've entered exists, you'll get an output of the specific item. If not, you'll get an empty list.

### POST - to create a new item
To add a new item, first click on the GET option next to the URL field to  preview the dropdown list of options and select POST. While leaving the URL as **`localhost:5000/snacks/all`**, select the "Body" tab that's sandwiched between "Headers" and "Pre-request Script" and select the "raw" option. Once you do this, at the end to the right, a dropdown option written "Text" will appear. Click on it and set it to "JSON".
Next, click on the white space below it to start typing and create a dictionary containing the variables you wish to add. To illustrate, 
```
    {
      "item_id" : "34",
      "item_name" : "popcorn",
      "item_price" : 98,
      "item_quantity" : 1
    }
```
After you are done, click on the blue Send button to the right of the URL field, then go to the POST option to the left of the URL field, reselect GET and click on the Send button. Then click on the "Params" tab to the left of "Authorization" and scroll to the bottom of the list to preview your new addition. Alternatively, you can set the URL to **`localhost:5000/snacks/34`** because that's the ID we specified when creating the new item. Click the blue Send button to preview only this newly added item.

### PUT - to modify/update an existing item
For this, select PUT from the method dropdown option (where you got GET and POST). In the URL field, input **`localhost:5000/snacks/<id_number>`**, replacing **<id_number>** with the ID of the item you wish to change. Then go to the "Body" tab, ensure "raw" and "JSON" are still selected, then edit the variables you wish to change. For example, for item with ID 1 (**`localhost:5000/snacks/1`**), I want to change the name from "soda" to "juice" and the quantity from "40" to "359". In the editor, I will type:
```
    {
      "item_name" : "juice",
      "item_quantity" : 359
    }
```
Unless you wish to change every single variable, it is usually best to select only the ones you want to change. After this, click on the blue Send button, then change your method option from PUT to GET and click on Send again. Then either specify **`localhost:5000/snacks/all`** or **`localhost:5000/snacks/1`** in the URL field, click Send, and select the "Params" tab to view your modified item.

### DELETE - to remove an existing item
In the URL field, input **`localhost:5000/snacks/<id_number>`** while replacing **<id_number>** with the ID of the item you would like to delete. Then select DELETE from the dropdown menu to the left of the URL field, then click on the blue Send button. Afterwards, change back from DELETE to GET, input **`localhost:5000/snacks/all`** in the URL field, and click Send to see that the item you specified has now been removed from your dictionary.

When you are done and wish to close the Flask server, simply go to your terminal and click Ctrl + C (Cmd + C for MacOS users).
