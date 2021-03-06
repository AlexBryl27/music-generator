import json


def generate_sequence(note, octave_number):
    sequence = []
    octave = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    i = octave.index(note)
    for _ in range(31):
        sequence.append(note + str(octave_number))
        if i == 11:
            i = -1
        note = octave[i + 1]
        i += 1
        if note == 'C':
            octave_number += 1
    return sequence

string_map = {
    7: generate_sequence('B', 1),
    6: generate_sequence('E', 2),
    5: generate_sequence('A', 2),
    4: generate_sequence('D', 3),
    3: generate_sequence('G', 3),
    2: generate_sequence('B', 3),
    1: generate_sequence('E', 4)
}

with open('string_map.json', 'w') as f:
    json.dump(string_map, f)