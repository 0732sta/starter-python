#print after line SEQUENCE (filter)
def sequence_filter(line):
    #return true or false, if false it can remove the line
    return '>' not in line

    #same as "ipsum_file = open('file/ipsum.txt')"
with open('file/dna_sequence.txt') as dna_file:
    lines=dna_file.readlines()
    print(list(filter(sequence_filter,lines)))

