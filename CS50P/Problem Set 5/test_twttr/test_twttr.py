from twttr import shorten
import pytest

def main():
    test_cases()
    test_numbers()
    test_punctuation()

def test_cases():
    assert shorten('hi') == 'h'
    assert shorten('HELLO') == 'HLL'
    assert shorten('HElLo') == 'HlL'


def test_numbers():
    assert shorten('123') == '123'

def test_punctuation():
    assert shorten('hello' + ' , ' + 'there') == 'hll , thr'
