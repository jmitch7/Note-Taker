# This is a client that will take notes for you and retrieve previous notes that you have taken.
print('Welcome to notetaker!\n')
current_notes = {}

while True:
    response = input('Would you like to make new note or view old note? '
                     '\n"1" for new note \n"2" for old note \n"3" to exit and view all notes: ')
    if response == '1' or response == 'Make new note' or response == 'make new note' or response == 'new note' or response == 'New note':
        title = str(input('Title: '))
        content = str(input('Content: '))

        current_notes[title] = content
    elif response == '2' or response == 'view old note' or response == 'View old note' or response == 'old note' or response == 'Old note':
        show_this_note = input('Which note would you like to view? ')
        print('\n' + current_notes[show_this_note] + '\n')
    elif response == '3':
        break
# Make this line show a list of all current notes    elif response == '4'
    else:
        print('\nThat is not a valid response\n')

print('\n\n')
print('Here are your notes:')
for titles, contents in current_notes.items():
    print("\n\t" + titles + ': ' + contents)
