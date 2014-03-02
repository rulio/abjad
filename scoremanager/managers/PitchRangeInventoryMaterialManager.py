# -*- encoding: utf-8 -*-
from abjad import *
from scoremanager.managers.MaterialManager import MaterialManager
from scoremanager.editors.PitchRangeInventoryEditor \
    import PitchRangeInventoryEditor


class PitchRangeInventoryMaterialManager(MaterialManager):

    ### CLASS VARIABLES ###

    _output_material_checker = staticmethod(
        lambda x: isinstance(x, pitchtools.PitchRangeInventory))

    _output_material_editor = PitchRangeInventoryEditor

    _output_material_maker = pitchtools.PitchRangeInventory

    _output_material_module_import_statements = [
        'from abjad import *',
        ]

    generic_output_name = 'pitch range inventory'

    ### INITIALIZER ###

    def __init__(self, filesystem_path=None, session=None):
        superclass = super(PitchRangeInventoryMaterialManager, self)
        superclass.__init__(filesystem_path=filesystem_path, session=session)

    ### SPECIAL METHODS ###

    @staticmethod
    def __illustrate__(pitch_range_inventory, **kwargs):
        chords = []
        for pitch_range in pitch_range_inventory:
            pair = (pitch_range.start_pitch, pitch_range.stop_pitch)
            chord = Chord(pair, Duration(1))
            chords.append(chord)
        result = scoretools.make_piano_score_from_leaves(chords)
        score, treble_staff, bass_staff = result
        illustration = lilypondfiletools.make_basic_lilypond_file(score)
        rests = iterate(score).by_class(Rest)
        scoretools.replace_leaves_in_expr_with_skips(list(rests))
        override(score).time_signature.stencil = False
        override(score).bar_line.transparent = True
        override(score).span_bar.transparent = True
        moment = schemetools.SchemeMoment(1, 4)
        set_(score).proportional_notation_duration = moment
        return illustration
