# -*- encoding: utf-8 -*-
from abjad import *


def test_marktools_LilyPondComment_contents_string_01():
    r'''LilyPondComment contents string is read / write.
    '''

    comment = marktools.LilyPondComment('contents string')
    assert comment.contents_string == 'contents string'

    comment.contents_string = 'new contents string'
    assert comment.contents_string == 'new contents string'