from abjad.cfg.cfg import ABJADPATH, HOME
import os


_config_file_dict = {
   'DEBUG': {
      'comment': "# Live debugging. Set for live debugging during development.",
      'value': False,
   },
   'abjad_output': {
      'comment': "# Set to the one directory you wish all Abjad generate files\n" + \
                 "# (such as PDFs, LilyPond, MIDI or log files) to be saved.",
      'value': os.path.join(HOME, '.abjad', 'output'),
   },
   'abjad_templates': {      
      'comment': "# List of directories where Abjad will look for LilyPond" + \
                 "# templates.",
      'value': [os.path.join(ABJADPATH, 'templates')],
   },
   'accidental_spelling': {      
      'comment': "# Default accidental spelling.",
      'value': 'mixed',
   },
   'lilypond_path': {      
      'comment': "# Lilypond executable path.  Set to override dynamic lookup.",
      'value': '',
   },
   'lilypond_includes': {      
      'comment': "# List of LilyPond files that Abjad will '\include' in all \n" + \
                 "# generated *.ly files.",
      'value': None,
   },
   'lilypond_lang': {      
      'comment': "# Language to use in all generated LilyPond files.",
      'value': 'english',
   },
   'pdf_viewer': {      
      'comment': "# PDF viewer to use to view generated PDF files.\n" + \
                 "# When None your environment should know how to open PDFs.",
      'value': None,
   },
   'midi_player': {      
      'comment': "# MIDI player to play MIDI files.\n" + \
                 "# When None your environment should know how to open MIDIs.",
      'value': None,
   },
}
