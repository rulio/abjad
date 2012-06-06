from abjad.tools.gracetools.get_grace_containers_attached_to_leaf import get_grace_containers_attached_to_leaf


def detach_grace_containers_attached_to_leaf(leaf):
    r'''.. versionadded:: 2.0

    Detach grace containers attached to `leaf`::

        >>> staff = Staff("c'8 d'8 e'8 f'8")
        >>> grace_container = gracetools.GraceContainer([Note("cs'16")], kind='grace')
        >>> grace_container(staff[1])
        Note("d'8")

    ::

        >>> f(staff)
        \new Staff {
            c'8
            \grace {
                cs'16
            }
            d'8
            e'8
            f'8
        }

    ::

        >>> gracetools.get_grace_containers_attached_to_leaf(staff[1])
        (GraceContainer(cs'16),)

    ::

        >>> gracetools.detach_grace_containers_attached_to_leaf(staff[1])
        (GraceContainer(),)

    ::

        >>> f(staff)
        \new Staff {
            c'8
            d'8
            e'8
            f'8
        }

    ::

        >>> gracetools.get_grace_containers_attached_to_leaf(staff[1])
        ()

    Return tuple.
    '''

    grace_containers = get_grace_containers_attached_to_leaf(leaf)

    for grace_container in grace_containers:
        grace_container.detach()

    return grace_containers
