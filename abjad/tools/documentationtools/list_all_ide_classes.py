# -*- encoding: utf-8 -*-


def list_all_ide_classes(modules=None):
    r'''Lists all public classes defined in Abjad IDE.

    ::

        >>> all_classes = documentationtools.list_all_ide_classes()  # doctest: +SKIP

    '''
    from abjad.tools import documentationtools
    return documentationtools.list_all_classes('ide')