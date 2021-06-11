import flask
import joblib
import pandas as pd

xgbmodel = joblib.load('finalized_model.sav')

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=["GET","POST"])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))

    if flask.request.method == "POST":
        SeniorCitizen= flask.request.form['SeniorCitizen']
        Partner = flask.request.form['Partner']
        Dependants = flask.request.form['Dependants']
        Tenure = flask.request.form['Tenure']
        OnlineSecurity = flask.request.form['OnlineSecurity']
        OnlineBackup = flask.request.form['OnlineBackup']
        DeviceProtection = flask.request.form['DeviceProtection']
        TechSupport = flask.request.form['TechSupport']
        Contract = flask.request.form['Contract']
        PaperlessBilling = flask.request.form['PaperlessBilling']
        PaymentMethod =flask.request.form['PaymentMethod']
        MonthlyCharges = flask.request.form['MonthlyCharges']

        input_variables = pd.DataFrame([[SeniorCitizen,Partner,Dependants,Tenure
        ,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,Contract,
        PaperlessBilling,PaymentMethod,MonthlyCharges]],columns=['SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'OnlineSecurity',
       'OnlineBackup', 'DeviceProtection', 'TechSupport', 'Contract',
       'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges'])

        prediction = xgbmodel.predict(input_variables)[0]
        if prediction == 0:
            result = 'YES'
        else:
            result = 'NO'

        return flask.render_template('main.html',original_input = {
            'SeniorCitizen':SeniorCitizen, 'Partner':Partner, 'Dependents':Dependants, 'tenure':Tenure, 'OnlineSecurity':OnlineSecurity,
            'OnlineBackup':OnlineBackup, 'DeviceProtection':DeviceProtection, 'TechSupport':TechSupport, 'Contract':Contract,
            'PaperlessBilling':PaperlessBilling, 'PaymentMethod':PaymentMethod, 'MonthlyCharges':MonthlyCharges}, result=result)

    if __name__ == '__main__':
        app.run(debug=True)
        