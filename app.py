from flask import *
import json, time

app=Flask(__name__)

# using index or my own custome route works for the page
@app.route('/', methods=['GET'])
# def index():
def home_page():    
    # returned as a dictionary
    home_page_data = {
        "home_page":"Home",
        "message":"Succesfully loaded the Home page",
        "Timestamp":time.time(),
        "created_with": "Flask"
    }
    # json.dumps will convert the data set in the home page route into json data 

    Response= json.dumps(home_page_data)
    # returns data in the format we have defined in the routes in ascending order
    return jsonify(home_page_data)
       

    #this provides the response in one line not structured as the format above 
    # return jsonify(response)


    #NB # this two return stattements can be used either of each and will work well
    # returns as the json file 
   

      # json_dump = json.dumps(home_page_data)
       # return json(json_dump)



# with this we get the data returned from the get method just after running the port 

@app.route('/user-request/', methods=['GET'] )
def user_request_page():
    user_query = str(request.args.get("user"))
    home_page_data = {
        "home_page" : "request",
        "message" : f'Succesfully got the request for {user_query}',
        "Timestampt" : time.time()

    }
    # using this method is providing data in the format we have defined above as a json format
    Response = json.dumps(home_page_data)
    return jsonify(home_page_data)

    # this format is only giving us data in json but no proper formating 
    # json_dump = json.dumps(home_page_data)
    # return jsonify(json_dump)


# to get the data from the api we use the routes port/user-request/?user="input"
# example http://127.0.0.1:7777/user-request/?user=%22Wakadinali%22 
# {"home_page": "request", "message": "Succesfully got the request for \"Wakadinali\"", "Timestampt": 1687547923.5501237}

# another example http://127.0.0.1:7777/user-request/?user=%22geoff%22
# we have the response as {"home_page": "request", "message": "Succesfully got the request for \"geoff\"", "Timestampt": 1687548211.1001363}

if __name__ == '__main__' :
    app.run(port=7777, debug=True)   