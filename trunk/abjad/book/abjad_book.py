from abjad.book.parser._AbjadHTMLTag import _AbjadHTMLTag
from abjad.book.parser._AbjadLatexTag import _AbjadLatexTag
from abjad.book.parser._AbjadTeSTTag import _AbjadReSTTag
import getopt
import os
import sys


def _usage( ):
   usage = '''

USAGE 
   abjad-book [--skip-rendering] INPUT OUTPUT 
   
OPTIONS
   --skip-rendering
      when give, abjad-book will skip all image rendering and simply execute
      the code and write its output to OUTPUT.

DESCRIPTION
   `abjad-book` Processes  Abjad snippets embedded in HTML, LaTeX, or ReST 
document. All Abjad code placed between the <abjad> </abjad> tags in either 
HTML, LaTeX or ReST type documents is executed and replaced with tags 
appropriate to the given file type. All output generated by the code snippet 
is captured and inserted in the OUTPUT file.

Apart from the special opening and closing Abjad tags, abjad-book also
has a special line-level suffix tag: `<hide`. All lines ending with the  
`<hide` tag will be interpreted by Abjad but will not be displayed in the 
OUTPUT document. 

The opening <abjad> tag can also be followed by a list of `attribute=value`
pair. Currently only the `hide` attribute is recognized. You can make all of
the Abjad code block invisible in the OUTPUT file with the following opening 
tag:
<abjad>[hide = True]

This is useful for generating and embedding rendered score images without
showing any of the Abjad code.

Use the write_expr_to_ly(expr, name, template, title) function to have Abjad call 
LilyPond on the Abjad snippet and embed the rendered image in the document.

All Abjad snippets *must* start with no indentation in the document. 

Example:

   1. Create an HTML, LaTex or ReST document with embedded Abjad code
      between <abjad></abjad> tags. The code *must* be fully flushed 
      to the left, with no tabs or spaces. The content of an HTML file
      with embedded Abjad might look like this:

      This is an <b>HTML</b> document. Here is Abjad code:

      <abjad>
      v = Voice(notetools.make_repeated_notes(8))
      BeamSpanner(v)
      write_expr_to_ly(v, 'example1') <hide ## this will insert an image. 
      show(v)
      </abjad>

      More ordinary <b>HTML</b> text here.


   2. Call `abjad-book` on the file just created:

       $ abjad-book file.htm.raw  file.html
   '''
   return usage


def _abjad_book( ):
   ## get input parameters
   try:
      opts, args = getopt.getopt(sys.argv[1:], '', ['skip-rendering'])
   except getopt.GetoptError, err:
      print str(err)
      print _usage( )
      sys.exit(2)

   ## parse commandline options
   skip_rendering = False
   for o, a in opts:
      if o == '--skip-rendering':
         skip_rendering = True
      else:
         assert False, 'unhandled option'

   ## get input and output files
   if len(args) < 2:
      print _usage( )
      sys.exit(2)
   fn = args[0]
   out_fn = args[1]
   print "Processing '%s'. Will write output to '%s'..." % (fn, out_fn)

   ## parse file name
   fn_dir = os.path.dirname(os.path.abspath(fn))
   fn = os.path.basename(fn)
   
   ## chage to file dir and read input file
   os.chdir(fn_dir)
   file = open(fn, 'r')
   lines = file.read( ).splitlines( ) ## send lines with no trailing '\n'
   file.close( )

   ## create Abjad tag parser type based on file extension
   if '.htm' in fn:
      a = _AbjadHTMLTag(lines, skip_rendering)
   elif '.tex' in fn:
      a = _AbjadLatexTag(lines, skip_rendering)
   elif '.rst' in fn:
      a = _AbjadReSTTag(lines, skip_rendering)

   ## open and write to output file
   file = open(out_fn, 'w')
   file.writelines(a.process( ))
   file.close( )



if __name__ == '__main__':
   _abjad_book( )
