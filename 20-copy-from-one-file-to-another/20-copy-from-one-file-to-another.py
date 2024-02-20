# copy from one file to another program.

# ---> give the actual path of the file
infile = open(
    "D:/python programs/20-copy-from-one-file-to-another/sample.txt", "r")

outfile = open(
    "D:/python programs/20-copy-from-one-file-to-another/sample-copy.txt", "w")

print("Use readline() method")
line = infile.readline()
while line != "":
    outfile.write(line)
    line = infile.readline()

print("File copied successfully")
print("JOB DONE")
infile.close()
outfile.close()
