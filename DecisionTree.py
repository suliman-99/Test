import joblib
import pandas as pd

def decision_tree_score(sex, age, mmse, cdr):
    new_data = pd.DataFrame({
        'M/F': [sex],
        'Age': [age],
        'MMSE': [mmse],
        'CDR': [cdr]
    })
    # load model
    DecisionTreeclf = joblib.load('Assets/Tree.joblib')

    Result = DecisionTreeclf.predict(new_data)
    if Result == 1:
      print("Patient is Safe")
    else:
      print("Patient not Safe")

    return Result