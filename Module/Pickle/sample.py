import pickle

dic = {
    "Name":"Shaswata",
    "Age": 26,
    "Company": "Deloitte",
    "City":"Bangalore"
}

file = open("Details.txt","wb")
pickle.dump(dic,file)
file.close()

file1 = open("Details.txt","rb")
File_read = pickle.load(file1)
print(File_read)