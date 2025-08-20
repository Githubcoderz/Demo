
Data = []

def setup_function():
    global Data
    Data = [1, 2, 3]

def teardown_function():
    global Data
    Data = []

def test_sum_of_sampleData():
    assert sum(Data) == 6

def test_product_of_sampleData():
    product = 1
    for num in Data:
        product *= num
    assert product == 6