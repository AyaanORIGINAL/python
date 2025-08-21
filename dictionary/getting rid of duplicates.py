student_data = {
    'id1': {
        'name': 'Ayaan',
        'class': 6,
        'subjects': ['Math', 'Science', 'English']
    },
    'id2': {
        'name': 'Asif',
        'class': 7,
        'subjects': ['Math', 'English', 'Bangla']
    },
    'id3': {
        'name': 'Zayan',
        'class': 5,
        'subjects': ['Bangla', 'Math', 'English']

    },
}
print(student_data['id1']['name'])

result = {}
for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)