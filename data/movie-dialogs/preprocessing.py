with open('movie_characters_metadata.txt', 'r') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

gender_dict = {}
for line in lines:
    components = line.split('+++$+++')
    char_id = components[0].strip()
    char_gender = components[4].strip()
    gender_dict[char_id] = char_gender

with open('movie_lines.txt', 'rb') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

female_lines = []
male_lines = []
for line in lines:
    components = line.split('+++$+++')
    char_id = components[1].strip()
    saying = components[4].decode('utf-8', errors='replace').encode('ascii', errors='replace').strip()
    if char_id in gender_dict:
        if gender_dict[char_id] == 'f':
            female_lines.append(saying)
        elif gender_dict[char_id] == 'm':
            male_lines.append(saying)

with open('all-male/input.txt', 'w') as f:
    f.write('\n'.join(male_lines))

with open('all-female/input.txt', 'w') as f:
    f.write('\n'.join(female_lines))
