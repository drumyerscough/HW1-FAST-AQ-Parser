from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)
import os

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    fa_parser = FastaParser(os.path.join('data', 'test.fa'))
    # Create instance of FastqParser
    fq_parser = FastqParser(os.path.join('data', 'test.fq'))

    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    for record in fa_parser:
        print(record[0], transcribe(record[1]))
    
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    for record in fq_parser:
        print(record[0], transcribe(record[1]))

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    for record in fa_parser:
        print(record[0], reverse_transcribe(record[1]))

    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    for record in fq_parser:
        print(record[0], reverse_transcribe(record[1]))

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
