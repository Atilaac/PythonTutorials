text = "this is a simple text.\nthis is a new line here."

textToSave = open('test.txt', 'w')
textToSave.write(text)
textToSave.close()
