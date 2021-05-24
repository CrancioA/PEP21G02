# try:
#     1/0
#     raise AttributeError
#     raise Exception
# except ZeroDivisionError:
#     print('you should not divide by 0')
# except Exception:
#     print('This is a general exception')
# except AttributeError:
#     print('This is not possible')

#classes
class Note:
    text = 'Default text' #class variable

    def add_text(self, text_to_add):
        self.text = self.text + text_to_add

    def clear_text(self):
        self.text = ''

    def remove_text(self, text_to_remove):
        self.text = self.text.replace(text_to_remove, '')

    def count_lines1(self):
        count1 = 1
        if '\n' in self.text:
            count1 += 1
        return count1

    def count_lines2(self):
        count2 = len(self.text.splitlines())
        return count2

note = Note()
print(type(note))

print('instance value:', note.text)
note.text = 'new text'
print('instance value:', note.text)
note.add_text('ala bala portocala')
print('instance value:', note.text)
# note.clear_text()
# print('instance value:', note.text)
note.remove_text('New text entry')
print('instance value:', note.text)
note.add_text('first line \n'
              'second line')
note.count_lines1()
print('Number of lines first method:', note.count_lines1())
note.count_lines2()
print('Number of lines second method:', note.count_lines2())







