from flask import Flask,render_template,request
import urllib.request # urllib.request is a Python module for fetching URLs (Uniform Resource Locators)
app = Flask(__name__) # instance of a Flask class

dict = {}
url = "https://terriblytinytales.com/test.txt" # given url of txt file
file = urllib.request.urlopen(url) # storing the data from opening the url
for i in file: # Iterate through each line of the text
    decode_line = i.decode('utf-8') # decode the line to a readable format using line.decode("utf-8")
    for word in decode_line.split(): # reading each word
        if word not in dict.keys(): # to check if word is in dict or not
            dict[word] = 0
        dict[word] += 1

sorted_order = sorted(dict.items(), key=lambda x: x[1], reverse=True) # sort the dictionary in descending order if we not use reverse then it will sort by default ascending order

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
        dict1=sorted_order[:input] # break the dictionary to the users input number (Top Words )
        return render_template('Output.html',content=dict1,user=input) # Finally see the tabular data to send dictinory and user input to html file.

if __name__ == '__main__':
    app.run(debug=True)
