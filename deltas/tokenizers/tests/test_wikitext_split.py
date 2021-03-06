from nose.tools import eq_

from ..wikitext_split import wikitext_split


def test_wikitext_split():

    input = "As a sentence, this includes punctuation. \n" + \
            "\n" + \
            "==Header!==\n" + \
            "克·科伊尔 foobar!" + \
            "And then we have another sentence here!\n" + \
            "https://website.gov?param=value\n" + \
            "peoples' ain't d’encyclopédie\n" + \
            "mailto:email@email.mail"

    expecteds = ['As', ' ', 'a', ' ', 'sentence', ',', ' ', 'this', ' ',
                 'includes', ' ', 'punctuation', '.', ' \n\n',
                 '==', 'Header', '!', '==', '\n',
                 '克', '·', '科', '伊', '尔', ' ', 'foobar', '!',
                 'And', ' ', 'then', ' ', 'we', ' ', 'have', ' ', 'another',
                 ' ', 'sentence',
                 ' ', 'here', '!', '\n', 'https://website.gov?param=value', '\n',
                 'peoples\'', ' ', 'ain\'t', ' ', 'd’encyclopédie', '\n',
                 'mailto:email@email.mail']

    tokens = list(wikitext_split.tokenize(input))

    for token, expected in zip(tokens, expecteds):
        eq_(token, expected)
