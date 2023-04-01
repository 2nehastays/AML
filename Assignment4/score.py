# import sklearn
# import pytest
def score(text, model, threshold) :
    # Preprocess the text if necessary
    # ...
    
    # Get the propensity score
    prop_score = model.predict_proba([text])[0][1]
   
    
    # Compare the propensity score to the threshold
    prediction = prop_score >= threshold
    
    return prediction, prop_score
