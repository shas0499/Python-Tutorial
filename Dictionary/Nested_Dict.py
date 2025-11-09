Course = {
    'PHP': {
        'Duration': '3 months',
        'Fees': 3000,
        'Trainer': 'Shaswata'
    },
    'Python': {
        'Duration': '2 months',
        'Fees': 2000,
        'Trainer': 'Shaswata'
    },
    'Java': {
        'Duration': '4 months',
        'Fees': 4000,
        'Trainer': 'Shaswata'
    }
}
print(Course)
print(Course['PHP'])
print(Course['PHP']['Fees'])

#Iterate through nested dictionary
for key, value in Course.items():
    print(key, " : ", value)

#Update value
Course['Java']['Fees'] = 4500
print(Course)

print('Thank You...')