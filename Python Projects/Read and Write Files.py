# This will create a new .txt file
fw = open('sample.txt', 'w')
fw.write('Writing things into a text file \n')
fw.write('We can write all sorts of strange things \n')
fw.close()

# This will read the file and print it out
fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

