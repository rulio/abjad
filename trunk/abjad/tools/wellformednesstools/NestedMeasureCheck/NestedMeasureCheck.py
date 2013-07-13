from abjad.tools import componenttools
from abjad.tools import iterationtools
from abjad.tools import measuretools
from abjad.tools.wellformednesstools.Check import Check


class NestedMeasureCheck(Check):
    '''Do we have any nested measures?
    '''

    def _run(self, expr):
        violators = []
        total = 0
        for t in iterationtools.iterate_measures_in_expr(expr):
            parentage = t.select_parentage(include_self=False)
            if parentage.get_first(measuretools.Measure):
                violators.append(t)
            total += 1
        return violators, total
