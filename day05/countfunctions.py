def count_char(file_string):
    return len(file_string.replace('\n', ''))
     
def count_word(test_string):
    return len(test_string.replace('\n', ' ').split(' '))

def count_line(test_string):
    return len(test_string.split('\n'))
