from asyncio.windows_events import NULL
from flask import Flask, render_template,request
# from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

student_dummy_data = [
   { 1: [
                {"id": 1, "name": "John", "marks": [
                                    {"test_1":{"maths": None, "english": None, "science": None}},
                                    {"test_2":{"maths": None, "english": None, "science": None}},
                                 ]
                },
                
                 {"id": 2, "name": "tim", "marks": [
                                                {"test_1":{"maths": None, "english": None, "science": None}},
                                                {"test_2":{"maths": None, "english": None, "science": None}},]
                }   
         ]
   },
   
   
    { 2: [
                {"id": 1, "name": "tewo", "marks": [
                                                {"test_1":{"maths": None, "english": None, "science": None}},
                                                {"test_2":{"maths": None, "english": None, "science": None}},]
                },
                
                 {"id": 2, "name": "naruto", "marks": [
                                                    {"test_1":{"maths": None, "english": None, "science": None}},
                                                    {"test_2":{"maths": None, "english": None, "science": None}},]
                },
                  {"id": 3, "name": "thre", "marks": [
                                                {"test_1":{"maths": None, "english": None, "science": None}},
                                                {"test_2":{"maths": None, "english": None, "science": None}},]
                },
                   {"id": 4, "name": "four", "marks": [
                                                {"test_1":{"maths": None, "english": None, "science": None}},
                                                {"test_2":{"maths": None, "english": None, "science": None}},]
                },
                   {"id": 5, "name": "four", "marks": [
                                                {"test_1":{"maths": None, "english": None, "science": None}},
                                                {"test_2":{"maths": None, "english": None, "science": None}},]
                },
                   {"id": 6, "name": "four", "marks": [
                                                {"test_1":{"maths": None, "english": None, "science": None}},
                                                {"test_2":{"maths": None, "english": None, "science": None}},]
                },
                   {"id": 7, "name": "four", "marks": [
                                                {"test_1":{"maths": None, "english": None, "science": None}},
                                                {"test_2":{"maths": None, "english": None, "science": None}},]
                },
                   
                ]
   },]



@app.route("/")
def uploadmarks():
    grade = "2"
    subject="maths"
    test = "test_1"
    student_list=student_dummy_data[int(grade)-1][2]
    id = f"{test}_{int(grade)-1}_{subject}_{1}"
    # print(student_list)
    if request.method == 'POST':
        print("post")
        # id="{{test}}_{{class}}_{{subject}}_{{student['id']}}"
        print("post", request.form[str(id)])
        # print("post", request.form["student_id"])
    
    return render_template('uploadmarks.html', subject=subject, test=test, grade=grade, student_list=student_list)
    
if __name__ == "__main__":
    app.run(debug=True)