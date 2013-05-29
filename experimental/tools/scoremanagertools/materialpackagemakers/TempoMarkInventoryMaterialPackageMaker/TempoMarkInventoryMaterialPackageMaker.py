from abjad import *
#from abjad.tools import contexttools
from experimental.tools.scoremanagertools.materialpackagemakers.InventoryMaterialPackageMaker import \
    InventoryMaterialPackageMaker
#from make_illustration_from_output_material import make_illustration_from_output_material
from experimental.tools.scoremanagertools.editors.TempoMarkInventoryEditor import TempoMarkInventoryEditor


class TempoMarkInventoryMaterialPackageMaker(InventoryMaterialPackageMaker):

    ### CLASS VARIABLES ###

    generic_output_name = 'tempo mark inventory'
    #illustration_maker = staticmethod(make_illustration_from_output_material)
    output_material_checker = staticmethod(lambda x: isinstance(x, contexttools.TempoMarkInventory))
    output_material_editor = TempoMarkInventoryEditor
    output_material_maker = contexttools.TempoMarkInventory
    output_material_module_import_statements = [
        'from abjad.tools import contexttools',
        'from abjad.tools import durationtools',
        ]

    ### PUBLIC METHODS ###

    @staticmethod
    #def make_illustration_from_output_material(tempo_mark_inventory, **kwargs):
    def illustration_builder(tempo_mark_inventory, **kwargs):

        notes = []
        for tempo_mark in tempo_mark_inventory:
            note = Note("c'4")
            tempo_mark = contexttools.TempoMark(tempo_mark, target_context=Staff)
            tempo_mark(note)
            notes.append(note)

        staff = stafftools.RhythmicStaff(notes)
        score = Score([staff])
        illustration = lilypondfiletools.make_basic_lilypond_file(score)
        illustration.paper_block.top_system_spacing = layouttools.make_spacing_vector(0, 0, 6, 0)

        score.override.note_head.transparent = True
        score.override.bar_line.transparent = True
        score.override.clef.transparent = True
        score.override.span_bar.transparent = True
        score.override.staff_symbol.transparent = True
        score.override.stem.transparent = True
        score.override.time_signature.stencil = False
        score.set.proportional_notation_duration = schemetools.SchemeMoment(1, 24)

        return illustration
