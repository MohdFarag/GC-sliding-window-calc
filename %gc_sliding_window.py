""" 
Description: 
    - Sliding window program to compute the %GC in sequence of nucleotides.
Input:
    - DNA sequence
    - The window size (assume the window increment is |)
Return:
    - Nucleotide number
    - %GC for each window
"""

import argparse
import os

def get_args():
    parser = argparse.ArgumentParser(
        description="",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument('mode', metavar='mode', help='Do you want to write a sequence (1) or read a file (2)')
    parser.add_argument('sequence', metavar='seq', help='Enter a DNA sequence or path of the .fasta file')
    parser.add_argument('size', metavar='size', help='Enter window size')

    args = parser.parse_args()

    return args.mode, args.sequence, args.size


# Get window from sequence
def get_chunks(dna, window_size=4, increment=1):
    for i in range(0, len(dna) - window_size + 1, increment):
        chunk = dna[i:i + window_size]
        assert len(chunk) == window_size
        yield chunk

# Valid letters in DNA sequence
LETTERS_OF_DNA = ['A','G','T','C','N']

# Get sequence of nucleotides
def getSequence():
    # Get the mode of read input from the user
    mode = get_args()[0]
    if mode == "1":
        # Enter the sequence
        sequence = get_args()[1]

    elif mode == "2":
        file_name = get_args()[1]
        try:
            path = f"{os.path.dirname(os.path.realpath(__file__))}\{file_name}"
            with open(path, "r", encoding='utf-8-sig') as file:
                # Read the text from a file
                sequence = file.read()
        except Exception as e:
            if "No such file or directory" in e.__str__():
                raise Exception("**ERROR** No such file or directory")
        
        sequence = sequence.split("\n")[1:]
        sequence = "".join(sequence)
        # Remove spaces and line breaks from file
        sequence.replace('\n', '').replace('\r', '')
    else:
        raise Exception("**ERROR** Invalid mode")
        
    return sequence

def main(): 
    sequence = getSequence()

    # Go through all the letters in sequence to check the validity of it.
    for letter in sequence:
        if letter.upper() in LETTERS_OF_DNA:
            # If letter is valid => pass to next letter;
            pass
        else:
            # If one letter is not valid => break;
            raise Exception("**ERROR** Invalid sequence")

    # Convert the sequence to upper letters to unify the sequence
    sequence = sequence.upper()

    # Enter the window size
    window_size = get_args()[2]
    
    # Check is the window size entered is valid or not
    try:
        window_size = int(window_size)
    except:
        raise Exception("**ERROR** Invalid window size.")

    if window_size > len(sequence):
            raise Exception("**ERROR** window size must not be larger than sequence length.")



    print("\nStart processing ...\n")

    c = 1
    for chunk in get_chunks(sequence, window_size):
        g_count = float(chunk.count("G")) # Count G in sequence
        c_count = float(chunk.count("C")) # Count C in sequence
        a_count = float(chunk.count("A")) # Count A in sequence
        t_count = float(chunk.count("T")) # Count T in sequence
        n_count = float(chunk.count("N")) # Count N in sequence

        print(f"Window {c}: {chunk}")
        print(f"Nucleotide number: {len(chunk)}")
        print(f"There are {g_count} Gs, {c_count} Cs, {a_count} As and {t_count} Ts, in the DNA strand.")
        print(f"GC content is: {(g_count+c_count)*100/(a_count+t_count+g_count+c_count+n_count)}%")
        print("======================")
        
        c += 1

    print("\nEnd processing ...\n")

if __name__ == "__main__":
    main()
    
"""
Resources:
- https://www.geeksforgeeks.org/window-sliding-technique/
- https://en.wikipedia.org/wiki/GC-content#:~:text=In%20molecular%20biology%20and%20genetics,)%20or%20cytosine%20(C).
"""
