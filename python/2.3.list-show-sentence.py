sentence = input("Sentence:")
sentence_width = len(sentence)
screen_with = sentence_width + 20
box_width = sentence_width + 20
left_margin = (screen_with - box_width) // 2

print();
print(' '* left_margin + '+' + '-'*(box_width - 2) + '+')
print(' '*left_margin + '|  ' + ' '*sentence_width + '   |')
print(' '*left_margin + '|  ' + sentence + '   |')
print(' '*left_margin + '|  ' + ' '*sentence_width + '   |')
print(' '* left_margin + '+' + '-'*(box_width - 2) + '+')

