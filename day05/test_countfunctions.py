import countfunctions as cf

def test_char_count():
    test_string = 'asdasd asd this is a file\nrtr'
    assert(cf.count_char(test_string) == 28)
    
    test_string = 'asdasd asd this is a file'
    assert(cf.count_char(test_string) == 25)

    test_string = 'asdasd asd this is a file1'
    assert(cf.count_char(test_string) == 26)

def test_word_count():
    test_string = 'asdasd asd this is a file\nrtr'
    assert(cf.count_word(test_string) == 7)
    
    test_string = 'asdasd asd this is a file'
    assert(cf.count_word(test_string) == 6)

    test_string = 'asdasd asd this is a file a'
    assert(cf.count_word(test_string) == 7)

def test_line_count():
    test_string = 'asdasd asd this is a file\nrtr'
    assert(cf.count_line(test_string) == 2)
    
    test_string = 'asdasd \nasd this \nis a file\nasd'
    assert(cf.count_line(test_string) == 4)

    test_string = 'asdasd asd this is a file a'
    assert(cf.count_line(test_string) == 1)
