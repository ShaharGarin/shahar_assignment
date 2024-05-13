import sys

file_args = sys.argv
file_name = file_args[1]
#my_file = open(file_args[1])
#char_count = len(my_file)
def main():
    print(count_file(file_name))

def count_file(file_name):
    with open(file_name , 'r') as file:
        file_content = file.read()
    char_count = len(file_content.replace('\n', ''))
    word_count = len(file_content.replace('\n', ' ').split(' '))
    line_count = len(file_content.split('\n'))

    return f"The number of characters in file is {char_count}.\nThe nmuber of lines in file is {line_count}\nThe umber of words in file is {word_count}"

main()
