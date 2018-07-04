# Conway's game of life step implementation
# Tyler Chapin
# To run: "python <this file location> <input file location>"

import sys

def inpt_reader(args):
    try:
        inpt_file = args[0]
    except:
        print "Please give an input file."
        exit()

    try:
        inpt = []
        f = open(inpt_file, 'r')
        for line in f:
            row = []
            for val in line.strip():
                row.append(int(val))
            inpt.append(row)
    except:
        print "There was a problem reading the input file."
        exit()
    finally:
        f.close()

    for row in inpt:
        if len(row) != len(inpt[0]):
            print "Improper input."
            exit()
    
    return inpt

def supports_life(inpt, row, col):
    live = inpt[row][col] == 1
    nbr_count = 0
    nbrhood = [-1, 0, 1]

    for y in nbrhood:
        j = row + y
        for x in nbrhood:
            i = col + x
            if x==y==0 or i<0 or j<0 or i>len(inpt[0])-1 or j>len(inpt)-1:
                continue
            nbr_count += inpt[j][i]

    if live:
        return nbr_count == 2 or nbr_count == 3
    else:
        return nbr_count == 3

def write_outpt(outpt, outpt_file):
    with open(outpt_file, 'w') as f:
        out_str = ""
    
        for row in outpt:
            for col in row:
                out_str += str(col)
            out_str += "\n"

        f.write(out_str)

def main(args):
    inpt = inpt_reader(args)
    rows, cols = len(inpt), len(inpt[0])
    outpt = [[0 for x in range(cols)] for y in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if supports_life(inpt, row, col):
                outpt[row][col] = 1
                
    for row in outpt:
        for col in row:
            print col,
        print ""

    #uncomment this line to write to original file:
    #write_outpt(outpt, args[0])

if __name__ == "__main__":
    main(sys.argv[1:])
