from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd


application = Flask(__name__)
app=application

model = pickle.load(open("Model/modelforPrediction.pkl", "rb"))

## Route for homepage

@app.route('/')
def index():
    return render_template('index.html')

## Route for Single data point prediction
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        word_freq_make = float(request.form.get('word_freq_make'))
        word_freq_address = float(request.form.get('word_freq_address'))
        word_freq_all = float(request.form.get('word_freq_all'))
        word_freq_3d = float(request.form.get('word_freq_3d'))
        word_freq_our = float(request.form.get('word_freq_our'))
        word_freq_over = float(request.form.get('word_freq_over'))
        word_freq_remove = float(request.form.get('word_freq_remove'))
        word_freq_internet = float(request.form.get('word_freq_internet'))
        word_freq_order = float(request.form.get('word_freq_order'))
        word_freq_mail = float(request.form.get('word_freq_mail'))

        word_freq_receive = float(request.form.get('word_freq_receive'))
        word_freq_will = float(request.form.get('word_freq_will'))
        word_freq_people = float(request.form.get('word_freq_people'))
        word_freq_report = float(request.form.get('word_freq_report'))
        word_freq_addresses = float(request.form.get('word_freq_addresses'))
        word_freq_free = float(request.form.get('word_freq_free'))
        word_freq_business = float(request.form.get('word_freq_business'))
        word_freq_email = float(request.form.get('word_freq_email'))
        word_freq_you = float(request.form.get('word_freq_you'))
        word_freq_credit = float(request.form.get('word_freq_credit'))

        word_freq_your = float(request.form.get('word_freq_your'))
        word_freq_font = float(request.form.get('word_freq_font'))
        word_freq_000 = float(request.form.get('word_freq_000'))
        word_freq_money = float(request.form.get('word_freq_money'))
        word_freq_hp = float(request.form.get('word_freq_hp'))
        word_freq_hpl = float(request.form.get('word_freq_hpl'))
        word_freq_george = float(request.form.get('word_freq_george'))
        word_freq_650 = float(request.form.get('word_freq_650'))
        word_freq_lab = float(request.form.get('word_freq_lab'))
        word_freq_labs = float(request.form.get('word_freq_labs'))
        
        word_freq_telnet = float(request.form.get('word_freq_telnet'))
        word_freq_857 = float(request.form.get('word_freq_857'))
        word_freq_data = float(request.form.get('word_freq_data'))
        word_freq_415 = float(request.form.get('word_freq_415'))
        word_freq_85 = float(request.form.get('word_freq_85'))
        word_freq_technology = float(request.form.get('word_freq_technology'))
        word_freq_1999 = float(request.form.get('word_freq_1999'))
        word_freq_parts = float(request.form.get('word_freq_parts'))
        word_freq_pm = float(request.form.get('word_freq_pm'))
        word_freq_direct = float(request.form.get('word_freq_direct'))

        word_freq_cs = float(request.form.get('word_freq_cs'))
        word_freq_meeting = float(request.form.get('word_freq_meeting'))
        word_freq_original = float(request.form.get('word_freq_original'))
        word_freq_project = float(request.form.get('word_freq_project'))
        word_freq_re = float(request.form.get('word_freq_re'))
        word_freq_edu = float(request.form.get('word_freq_edu'))
        word_freq_table = float(request.form.get('word_freq_table'))
        word_freq_conference = float(request.form.get('word_freq_conference'))
        char_freq_colon = float(request.form.get('char_freq_;'))
        char_freq_bracket = float(request.form.get('char_freq_('))

        char_freq_square_bracket = float(request.form.get('char_freq_['))
        char_freq_exclamatory = float(request.form.get('char_freq_!'))
        char_freq_rupees = float(request.form.get('char_freq_$'))
        char_freq_hash = float(request.form.get('char_freq_#'))
        capital_run_length_average = float(request.form.get('capital_run_length_average'))
        capital_run_length_longest = float(request.form.get('capital_run_length_longest'))
        capital_run_length_total = float(request.form.get('capital_run_length_total'))


        predict=model.predict([['word_freq_make', 'word_freq_address', 'word_freq_all', 'word_freq_3d','word_freq_our', 'word_freq_over', 'word_freq_remove','word_freq_internet', 'word_freq_order', 'word_freq_mail','word_freq_receive', 'word_freq_will', 'word_freq_people','word_freq_report', 'word_freq_addresses', 'word_freq_free','word_freq_business', 'word_freq_email', 'word_freq_you','word_freq_credit', 'word_freq_your', 'word_freq_font', 'word_freq_000','word_freq_money', 'word_freq_hp', 'word_freq_hpl', 'word_freq_george','word_freq_650', 'word_freq_lab', 'word_freq_labs', 'word_freq_telnet','word_freq_857', 'word_freq_data', 'word_freq_415', 'word_freq_85','word_freq_technology', 'word_freq_1999', 'word_freq_parts','word_freq_pm', 'word_freq_direct', 'word_freq_cs', 'word_freq_meeting','word_freq_original', 'word_freq_project', 'word_freq_re','word_freq_edu', 'word_freq_table', 'word_freq_conference','char_freq_colon', 'char_freq_bracket', 'char_freq_square_bracket', 'char_freq_exclamatory','char_freq_rupees', 'char_freq_hash', 'capital_run_length_average','capital_run_length_longest', 'capital_run_length_total']])
       
        if predict[0] ==1 :
            result = 'Spam'
        else:
            result ='Not Spam'
            
        return render_template('single_prediction.html',result=result)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")