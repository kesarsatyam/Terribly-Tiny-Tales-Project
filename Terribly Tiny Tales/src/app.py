from flask import Flask,render_template,request
app = Flask(__name__)
def program():
    dict = {}
    with open('test.txt', 'r') as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                # print(word)
                if word not in dict.keys():
                    dict[word] = 0
                dict[word] += 1
    sort_orders = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return sort_orders
@app.route('/')
def home_page():
    return render_template('Home.html')
@app.route('/',methods=['POST'])
def pro():
    user_input=request.form['input']
    input = int(user_input)
    if(input > 428):
        return "Please enter the Number below 428"
    else:
        dict1=program()
        dict1=dict1[:input]
        return render_template('Output.html',content=dict1,user=input)

if __name__ == '__main__':
    app.run(debug=True)