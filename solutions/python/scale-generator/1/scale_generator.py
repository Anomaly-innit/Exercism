SHARPS = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
FLATS = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
SHARP_TONICS = ["C", "a", "G", "D", "A", "E", "B", "F#", "e", "b", "f#", "c#", "g#", "d#"]
FLAT_TONICS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]

class Scale:
    def __init__(self, tonic):
        self.tonic = tonic

    def chromatic(self):
        if self.tonic in SHARP_TONICS:
            notes = SHARPS
        elif self.tonic in FLAT_TONICS:
            notes = FLATS
        
        note_name = self.tonic.capitalize()  
        index = notes.index(note_name)
        return notes[index:] + notes[:index]
            
            
    def interval(self, intervals):
        notes = self.chromatic()
        steps = {"m": 1, "M": 2, "A": 3}
        
        result = [notes[0]]
        position = 0
        
        for char in intervals:
            position = (position + steps[char]) % 12
            result.append(notes[position])
        return result