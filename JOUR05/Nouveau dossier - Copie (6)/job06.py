def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        elif note % 5 >= 3:
            notes_arrondies.append((note // 5 + 1) * 5)
        else:
            notes_arrondies.append(note)
    return notes_arrondies
