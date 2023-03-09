import pytest
from score import score
import joblib
from textblob import TextBlob
#from pre_processing_func import get_model






# def test_score():
#     # Test that the function produces some output without crashing
#     text = "hello world"
#     #model = get_model()
#     model = joblib.load('best_model.pkl')
#     threshold = 0.5
#     prediction, propensity = score(text, model, threshold)

#     # test that output formats are as expected
#     #assert isinstance(prediction, bool)
#     #assert isinstance(propensity, float)
    
#     # Test that the input/output formats/types are as expected
    
#     with pytest.raises(TypeError):
#         score(text, "model", threshold)
    
    
    

# Test that the prediction value is always either 0 or 1   
def test_prediction_0_1():
    text1 = "'Please call our customer service representative on 0800 169 6031 between 10am-9pm as you have WON a guaranteed Â£1000 cash or Â£5000 prize!'"
    text2 = "hello world"
    model = joblib.load('best_model.pkl')
    #model = 'model.pkl'

    threshold = 0.5
    prediction1, propensity1 = score(text1, model, threshold)
    prediction2, propensity2 = score(text2, model, threshold)
    assert prediction1 in [0, 1]
    assert prediction2 in [0, 1]
    
    # Test that the propensity score is always between 0 and 1
    assert 0 <= propensity1 <= 1
    assert 0 <= propensity2 <= 1

    
def test_threshold_to_0():
    text1 = "'Please call our customer service representative on 0800 169 6031 between 10am-9pm as you have WON a guaranteed Â£1000 cash or Â£5000 prize!'"
    text2 = "hello world"
    threshold = 0
    #model = 'model.pkl'
    model = joblib.load('best_model.pkl')
    prediction1, propensity1 = score(text1, model, threshold)
    prediction2, propensity2 = score(text2, model, threshold)
    assert prediction1 == 1
    assert prediction2 == 1

    
def test_threshold_to_1():
    model = joblib.load('best_model.pkl')
    text1 = "'Please call our customer service representative on 0800 169 6031 between 10am-9pm as you have WON a guaranteed Â£1000 cash or Â£5000 prize!'"
    text2 = "hello world"
    threshold = 1
    #model = 'model.pkl'

    prediction1, propensity1 = score(text1, model, threshold)
    prediction2, propensity2 = score(text2, model, threshold)
    assert prediction1 == 0
    assert prediction2 == 0
    

def test_spam_input():
    model = joblib.load('best_model.pkl')
    text = "'Please call our customer service representative on 0800 169 6031 between 10am-9pm as you have WON a guaranteed Â£1000 cash or Â£5000 prize!'"
    #model = 'model.pkl'

    threshold = 0.5
    prediction, propensity = score(text, model, threshold)
    assert prediction == 1    


def test_non_spam_input():
    model = joblib.load('best_model.pkl')
    text = "hello world"
    #model = 'model.pkl'

    threshold = 0.5
    prediction, propensity = score(text, model, threshold)
    assert prediction == 0

