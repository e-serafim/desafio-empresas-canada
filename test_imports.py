import pandas
import bertopic
import nltk
import seaborn
import matplotlib
import numpy
import sklearn
    
def test_pandas():
    assert pandas.__version__=='1.3.2'
    
def test_bertopic():
    assert bertopic.__version__=='0.15.0'

def test_numpy():
    assert numpy.__version__=='1.23.5'

def test_nltk():
    assert nltk.__version__=='3.5'
    
def test_seaborn():
    assert seaborn.__version__=='0.11.0'
    
def test_matplotlib():
    assert matplotlib.__version__=='3.3.2'
    
def test_sklearn():
    assert sklearn.__version__=='0.23.2'