from flask import Flask,render_template,request
app = Flask(__name__) # instance of a Flask class
def program():
    dict = {}
    with open('test.txt', 'r') as file: # reading the file
        for line in file: # reading each line
            for word in line.split(): # reading each word
                if word not in dict.keys(): # to check if word is in dict or not
                    dict[word] = 0
                dict[word] += 1
    sort_orders = sorted(dict.items(), key=lambda x: x[1], reverse=True) # sort the dictionary in descending order if we not use reverse then it will sort by default ascending order
    return sort_orders
@app.route('/') # url routing pattern
def home_page():
    return render_template('Home.html') # render_template which helps to read the html pages
@app.route('/',methods=['POST']) # capture the number when user hit the submit button with method post same in html file.
def pro():
    user_input=request.form['input'] # will retrive the data from html to python code the name should be same which is of placeholder input.
    input = int(user_input)
    if(input > 428): # check the condition
        return "Please enter the Number below 428"
    else:
        dict1=program()
        dict1=dict1[:input] # break the dictionary to the users input number (Top Words )
        return render_template('Output.html',content=dict1,user=input) # Finally see the tabular data to send dictinory and user input to html file.

if __name__ == '__main__':
    app.run(debug=True)
