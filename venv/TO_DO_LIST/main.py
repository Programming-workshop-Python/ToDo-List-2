from flask import Flask, render_template,  request
from datetime import datetime
from flask import jsonify
import insert_data as f1
import json
import pandas as pd

app = Flask(__name__)



@app.route('/create_task', methods=['POST'])
def first_page() -> str:
    task = request.form['task_name']
    exp = request.form['exp_date']
    exp=exp.replace('T', ' ')
    f1.insert(task, exp)
    return render_template('created.html', created_task = task)


@app.route('/view_tasks', methods=['POST'])
def second_page():
    try:
        opt = request.form["options"]
        f1.delete(opt)
    except: pass
    json_string = f1.read()
    json_string = json.dumps(json_string)
    parsed_string = json.loads(json_string)
    df = pd.DataFrame(data=parsed_string)
    df = df.set_index('id')
    radio = list()
    for index, row in df.iterrows():
        radio.append('<input type= "radio" name="options" value= "{}" id = "A{}">'.format(index,index))
    df.insert(2, '', radio)
    df_html = df.to_html(index=False)
    df_html=df_html.replace('&gt;', '>')
    df_html=df_html.replace('&lt;', '<')
    return render_template('all_tasks.html', table_html = df_html)


@app.route('/')
@app.route('/entry', methods=['POST'])
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='To Do List!')

if __name__ == '__main__':
    app.run(debug=True)
