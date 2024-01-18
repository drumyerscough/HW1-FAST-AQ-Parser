# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest
import os

def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # check if fasta is empty
    parser = FastaParser(os.path.join('tests', 'blank.fa'))
    assert len(list(parser)) > 0

    # check if fasta is malformed
    parser = FastaParser(os.path.join('tests', 'bad.fa'))
    for header, seq in parser:
        # has header
        assert type(header) == str and header.startswith('>')
        # has a sequence and is only letters
        assert len(seq) > 0 and type(seq) == str and seq.isalpha()


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    parser = FastaParser(os.path.join('tests', 'test.fq'))
    for record in parser:
        assert record[0] == None

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # check if fasta is empty
    parser = FastqParser(os.path.join('tests', 'blank.fq'))
    assert len(list(parser)) > 0

    # check if fasta is malformed
    parser = FastqParser(os.path.join('tests', 'bad.fq'))
    for header, seq, qual in parser:
        # has header
        assert type(header) == str and header.startswith('>')
        # has a sequence, is string, and is only letters
        assert len(seq) > 0 and type(seq) == str and seq.isalpha()
        # has score, is string, and is ascii
        assert len(qual) > 0 and type(qual) == str and qual.isascii()

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    parser = FastqParser(os.path.join('tests', 'test.fa'))
    for record in parser:
        assert record[0] == None