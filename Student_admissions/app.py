from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

app = Flask(__name__)


# To renderHomepage
@app.route('/', methods=['POST', 'GET'])
def home_page():
    return render_template('home.html')


# This will be called from UI
@app.route('/result', methods=['POST'])
def student_management():
    if request.method == 'POST':
        operation = request.form['operation']
        Serial_No = request.form['Serial No']
        GRE_Score = request.form['GRE Score']
        TOEFL_SCore = request.form['TOEFL SCore']
        SOP = request.form['SOP']
        LOR = request.form['LOR']
        CGPA = request.form['CGPA']
        Research = request.form['Research']
        Chance_of_Admit = request.form['Chance of Admit']

        dbConn = pymongo.MongoClient("mongodb://localhost:27017/")  # opening a connection to Mongo
        dbname = 'demoDB'
        db = dbConn[dbname]
        collection_name = 'mongo_demo'
        collection = db[collection_name]
        my_dict = {'Serial No': Serial_No, 'GRE Score': GRE_Score, 'TOEFL SCore': TOEFL_SCore, 'SOP': SOP,
                   'LOR': LOR, 'CGPA': CGPA, 'Research': Research, 'Chance of Admit': Chance_of_Admit}
        print(my_dict)
        print('xxxxxxxxxx')
        my_db_query = {k: v for k, v in my_dict.items() if v}
        print(my_db_query)
        print('xxxxxxxxxx')
        results = list(collection.find(my_db_query))
        print(results)

        if operation == 'Add':
            if not results:
                x = collection.insert_one(my_db_query)
                print('The record is added')
                return 'The record is added'
            else:
                print('The record is already present')
                return 'The record is already present'

        if operation == 'Search':
            for result in results:
                print(result)
            return render_template('results.html', results=results)

        if operation == 'View List':
            results = list(collection.find({}))
            return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
