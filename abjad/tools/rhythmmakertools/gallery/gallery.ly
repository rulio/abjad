% 2014-02-02 14:19

\version "2.19.1"
\language "english"

\include "stylesheet.ily"

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 4/16
				s1 * 1/4
					^ \markup {
						\override
							#'(font-name . "Courier")
							\column
								{
									"EvenRunRhythmMaker()"
								}
						}
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 1/2
				s1 * 1/2
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				\time 1/2
				s1 * 1/2
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				\time 4/16
				s1 * 1/4
			}
			{
				\time 5/16
				s1 * 5/16
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									1-1
				}
		} {
			{
				\time 4/16
				{
					c'16 [
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 5/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 1/2
				{
					c'2
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8 [
					c'8 ]
				}
			}
			{
				\time 1/2
				{
					c'2
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8 [
					c'8 ]
				}
			}
			{
				\time 4/16
				{
					c'16 [
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 5/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
	\header {
		title = \markup {
			\fontsize
				#4.5
				\override
					#'(font-name . "Times")
					"Even-run rhythm-maker"
			}
	}
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 1/11
				s1 * 1/11
			}
			{
				\time 3/8
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				\time 1/11
				s1 * 1/11
			}
			{
				\time 3/8
				s1 * 3/8
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									1-2
				}
		} {
			{
				\time 1/11
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/11 {
					c'8
				}
			}
			{
				\time 3/8
				{
					c'8 [
					c'8
					c'8 ]
				}
			}
			{
				{
					c'8 [
					c'8
					c'8 ]
				}
			}
			{
				{
					c'8 [
					c'8
					c'8 ]
				}
			}
			{
				{
					c'8 [
					c'8
					c'8 ]
				}
			}
			{
				{
					c'8 [
					c'8
					c'8 ]
				}
			}
			{
				\time 1/11
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/11 {
					c'8
				}
			}
			{
				\time 3/8
				{
					c'8 [
					c'8
					c'8 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 3/15
				s1 * 1/5
			}
			{
				s1 * 1/5
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 5/24
				s1 * 5/24
			}
			{
				s1 * 5/24
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				s1 * 1/6
			}
			{
				\time 2/8
				s1 * 1/4
			}
			{
				\time 3/28
				s1 * 3/28
			}
			{
				s1 * 3/28
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 1/9
				s1 * 1/9
			}
			{
				s1 * 1/9
			}
			{
				\time 1/8
				s1 * 1/8
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									1-3
				}
		} {
			{
				\time 3/15
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/15 {
					c'8 [
					c'8
					c'8 ]
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/15 {
					c'8 [
					c'8
					c'8 ]
				}
			}
			{
				\time 3/16
				{
					c'16 [
					c'16
					c'16 ]
				}
			}
			{
				\time 5/24
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'16 [
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'16 [
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 5/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8 [
					c'8 ]
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8 [
					c'8 ]
				}
			}
			{
				\time 2/8
				{
					c'8 [
					c'8 ]
				}
			}
			{
				\time 3/28
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/7 {
					c'16 [
					c'16
					c'16 ]
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/7 {
					c'16 [
					c'16
					c'16 ]
				}
			}
			{
				\time 3/16
				{
					c'16 [
					c'16
					c'16 ]
				}
			}
			{
				\time 1/9
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/9 {
					c'8
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/9 {
					c'8
				}
			}
			{
				\time 1/8
				{
					c'8
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 9/16
				s1 * 9/16
			}
			{
				\time 1/5
				s1 * 1/5
			}
			{
				\time 9/16
				s1 * 9/16
			}
			{
				\time 1/5
				s1 * 1/5
			}
			{
				\time 9/16
				s1 * 9/16
			}
			{
				s1 * 9/16
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									1-4
				}
		} {
			{
				\time 9/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 1/5
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/5 {
					c'4
				}
			}
			{
				\time 9/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 1/5
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/5 {
					c'4
				}
			}
			{
				\time 9/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\pageBreak

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 4/16
				s1 * 1/4
					^ \markup {
						\override
							#'(font-name . "Courier")
							\column
								{
									"EvenRunRhythmMaker("
									"    beam_specifier=BeamSpecifier("
									"        beam_each_division=True,"
									"        beam_divisions_together=True,"
									"        ),"
									"    )"
								}
						}
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 1/2
				s1 * 1/2
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				\time 1/2
				s1 * 1/2
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				\time 4/16
				s1 * 1/4
			}
			{
				\time 5/16
				s1 * 5/16
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									2-1
				}
		} {
			{
				\time 4/16
				{
					\set stemLeftBeamCount = #0
					\set stemRightBeamCount = #2
					c'16 [
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #1
					c'16
				}
			}
			{
				\time 5/16
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #0
					c'16 ]
				}
			}
			{
				\time 1/2
				{
					c'2
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					\set stemLeftBeamCount = #0
					\set stemRightBeamCount = #1
					c'8 [
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #0
					c'8 ]
				}
			}
			{
				\time 1/2
				{
					c'2
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					\set stemLeftBeamCount = #0
					\set stemRightBeamCount = #1
					c'8 [
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				\time 4/16
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #1
					c'16
				}
			}
			{
				\time 5/16
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #0
					c'16 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 1/11
				s1 * 1/11
			}
			{
				\time 3/8
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				\time 1/11
				s1 * 1/11
			}
			{
				\time 3/8
				s1 * 3/8
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									2-2
				}
		} {
			{
				\time 1/11
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/11 {
					\set stemLeftBeamCount = #0
					\set stemRightBeamCount = #1
					c'8 [
				}
			}
			{
				\time 3/8
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				\time 1/11
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/11 {
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				\time 3/8
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #0
					c'8 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 3/15
				s1 * 1/5
			}
			{
				s1 * 1/5
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 5/24
				s1 * 5/24
			}
			{
				s1 * 5/24
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				s1 * 1/6
			}
			{
				\time 2/8
				s1 * 1/4
			}
			{
				\time 3/28
				s1 * 3/28
			}
			{
				s1 * 3/28
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 1/9
				s1 * 1/9
			}
			{
				s1 * 1/9
			}
			{
				\time 1/8
				s1 * 1/8
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									2-3
				}
		} {
			{
				\time 3/15
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/15 {
					\set stemLeftBeamCount = #0
					\set stemRightBeamCount = #1
					c'8 [
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/15 {
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				\time 3/16
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #1
					c'16
				}
			}
			{
				\time 5/24
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #1
					c'16
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #1
					c'16
				}
			}
			{
				\time 5/16
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #1
					c'16
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				\time 2/8
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				\time 3/28
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/7 {
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #1
					c'16
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/7 {
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #1
					c'16
				}
			}
			{
				\time 3/16
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #1
					c'16
				}
			}
			{
				\time 1/9
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/9 {
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/9 {
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
			}
			{
				\time 1/8
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #0
					c'8 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 9/16
				s1 * 9/16
			}
			{
				\time 1/5
				s1 * 1/5
			}
			{
				\time 9/16
				s1 * 9/16
			}
			{
				\time 1/5
				s1 * 1/5
			}
			{
				\time 9/16
				s1 * 9/16
			}
			{
				s1 * 9/16
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									2-4
				}
		} {
			{
				\time 9/16
				{
					\set stemLeftBeamCount = #0
					\set stemRightBeamCount = #2
					c'16 [
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #0
					c'16 ]
				}
			}
			{
				\time 1/5
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/5 {
					c'4
				}
			}
			{
				\time 9/16
				{
					\set stemLeftBeamCount = #0
					\set stemRightBeamCount = #2
					c'16 [
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #0
					c'16 ]
				}
			}
			{
				\time 1/5
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/5 {
					c'4
				}
			}
			{
				\time 9/16
				{
					\set stemLeftBeamCount = #0
					\set stemRightBeamCount = #2
					c'16 [
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #1
					c'16
				}
			}
			{
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #2
					c'16
					\set stemLeftBeamCount = #2
					\set stemRightBeamCount = #0
					c'16 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\pageBreak

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 4/16
				s1 * 1/4
					^ \markup {
						\override
							#'(font-name . "Courier")
							\column
								{
									"EvenRunRhythmMaker("
									"    beam_specifier=BeamSpecifier("
									"        beam_each_division=False,"
									"        beam_divisions_together=False,"
									"        ),"
									"    )"
								}
						}
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 1/2
				s1 * 1/2
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				\time 1/2
				s1 * 1/2
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				\time 4/16
				s1 * 1/4
			}
			{
				\time 5/16
				s1 * 5/16
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									3-1
				}
		} {
			{
				\time 4/16
				{
					c'16
					c'16
					c'16
					c'16
				}
			}
			{
				\time 5/16
				{
					c'16
					c'16
					c'16
					c'16
					c'16
				}
			}
			{
				\time 1/2
				{
					c'2
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8
					c'8
				}
			}
			{
				\time 1/2
				{
					c'2
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8
					c'8
				}
			}
			{
				\time 4/16
				{
					c'16
					c'16
					c'16
					c'16
				}
			}
			{
				\time 5/16
				{
					c'16
					c'16
					c'16
					c'16
					c'16
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 1/11
				s1 * 1/11
			}
			{
				\time 3/8
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				\time 1/11
				s1 * 1/11
			}
			{
				\time 3/8
				s1 * 3/8
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									3-2
				}
		} {
			{
				\time 1/11
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/11 {
					c'8
				}
			}
			{
				\time 3/8
				{
					c'8
					c'8
					c'8
				}
			}
			{
				{
					c'8
					c'8
					c'8
				}
			}
			{
				{
					c'8
					c'8
					c'8
				}
			}
			{
				{
					c'8
					c'8
					c'8
				}
			}
			{
				{
					c'8
					c'8
					c'8
				}
			}
			{
				\time 1/11
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/11 {
					c'8
				}
			}
			{
				\time 3/8
				{
					c'8
					c'8
					c'8
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 3/15
				s1 * 1/5
			}
			{
				s1 * 1/5
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 5/24
				s1 * 5/24
			}
			{
				s1 * 5/24
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				s1 * 1/6
			}
			{
				\time 2/8
				s1 * 1/4
			}
			{
				\time 3/28
				s1 * 3/28
			}
			{
				s1 * 3/28
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 1/9
				s1 * 1/9
			}
			{
				s1 * 1/9
			}
			{
				\time 1/8
				s1 * 1/8
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									3-3
				}
		} {
			{
				\time 3/15
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/15 {
					c'8
					c'8
					c'8
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/15 {
					c'8
					c'8
					c'8
				}
			}
			{
				\time 3/16
				{
					c'16
					c'16
					c'16
				}
			}
			{
				\time 5/24
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'16
					c'16
					c'16
					c'16
					c'16
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'16
					c'16
					c'16
					c'16
					c'16
				}
			}
			{
				\time 5/16
				{
					c'16
					c'16
					c'16
					c'16
					c'16
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8
					c'8
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8
					c'8
				}
			}
			{
				\time 2/8
				{
					c'8
					c'8
				}
			}
			{
				\time 3/28
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/7 {
					c'16
					c'16
					c'16
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/7 {
					c'16
					c'16
					c'16
				}
			}
			{
				\time 3/16
				{
					c'16
					c'16
					c'16
				}
			}
			{
				\time 1/9
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/9 {
					c'8
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/9 {
					c'8
				}
			}
			{
				\time 1/8
				{
					c'8
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 9/16
				s1 * 9/16
			}
			{
				\time 1/5
				s1 * 1/5
			}
			{
				\time 9/16
				s1 * 9/16
			}
			{
				\time 1/5
				s1 * 1/5
			}
			{
				\time 9/16
				s1 * 9/16
			}
			{
				s1 * 9/16
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									3-4
				}
		} {
			{
				\time 9/16
				{
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
				}
			}
			{
				\time 1/5
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/5 {
					c'4
				}
			}
			{
				\time 9/16
				{
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
				}
			}
			{
				\time 1/5
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/5 {
					c'4
				}
			}
			{
				\time 9/16
				{
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
				}
			}
			{
				{
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\pageBreak

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 4/16
				s1 * 1/4
					^ \markup {
						\override
							#'(font-name . "Courier")
							\column
								{
									"EvenRunRhythmMaker("
									"    tie_specifier=TieSpecifier("
									"        tie_across_divisions=True,"
									"        tie_split_notes=True,"
									"        ),"
									"    )"
								}
						}
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 1/2
				s1 * 1/2
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				\time 1/2
				s1 * 1/2
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				\time 4/16
				s1 * 1/4
			}
			{
				\time 5/16
				s1 * 5/16
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									4-1
				}
		} {
			{
				\time 4/16
				{
					c'16 [
					c'16
					c'16
					c'16 ] ~
				}
			}
			{
				\time 5/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16 ] ~
				}
			}
			{
				\time 1/2
				{
					c'2 ~
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8 [
					c'8 ] ~
				}
			}
			{
				\time 1/2
				{
					c'2 ~
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8 [
					c'8 ] ~
				}
			}
			{
				\time 4/16
				{
					c'16 [
					c'16
					c'16
					c'16 ] ~
				}
			}
			{
				\time 5/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 1/11
				s1 * 1/11
			}
			{
				\time 3/8
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				\time 1/11
				s1 * 1/11
			}
			{
				\time 3/8
				s1 * 3/8
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									4-2
				}
		} {
			{
				\time 1/11
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/11 {
					c'8 ~
				}
			}
			{
				\time 3/8
				{
					c'8 [
					c'8
					c'8 ] ~
				}
			}
			{
				{
					c'8 [
					c'8
					c'8 ] ~
				}
			}
			{
				{
					c'8 [
					c'8
					c'8 ] ~
				}
			}
			{
				{
					c'8 [
					c'8
					c'8 ] ~
				}
			}
			{
				{
					c'8 [
					c'8
					c'8 ] ~
				}
			}
			{
				\time 1/11
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/11 {
					c'8 ~
				}
			}
			{
				\time 3/8
				{
					c'8 [
					c'8
					c'8 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 3/15
				s1 * 1/5
			}
			{
				s1 * 1/5
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 5/24
				s1 * 5/24
			}
			{
				s1 * 5/24
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				s1 * 1/6
			}
			{
				\time 2/8
				s1 * 1/4
			}
			{
				\time 3/28
				s1 * 3/28
			}
			{
				s1 * 3/28
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 1/9
				s1 * 1/9
			}
			{
				s1 * 1/9
			}
			{
				\time 1/8
				s1 * 1/8
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									4-3
				}
		} {
			{
				\time 3/15
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/15 {
					c'8 [
					c'8
					c'8 ] ~
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/15 {
					c'8 [
					c'8
					c'8 ] ~
				}
			}
			{
				\time 3/16
				{
					c'16 [
					c'16
					c'16 ] ~
				}
			}
			{
				\time 5/24
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'16 [
					c'16
					c'16
					c'16
					c'16 ] ~
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'16 [
					c'16
					c'16
					c'16
					c'16 ] ~
				}
			}
			{
				\time 5/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16 ] ~
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8 [
					c'8 ] ~
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'8 [
					c'8 ] ~
				}
			}
			{
				\time 2/8
				{
					c'8 [
					c'8 ] ~
				}
			}
			{
				\time 3/28
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/7 {
					c'16 [
					c'16
					c'16 ] ~
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/7 {
					c'16 [
					c'16
					c'16 ] ~
				}
			}
			{
				\time 3/16
				{
					c'16 [
					c'16
					c'16 ] ~
				}
			}
			{
				\time 1/9
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/9 {
					c'8 ~
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/9 {
					c'8 ~
				}
			}
			{
				\time 1/8
				{
					c'8
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 9/16
				s1 * 9/16
			}
			{
				\time 1/5
				s1 * 1/5
			}
			{
				\time 9/16
				s1 * 9/16
			}
			{
				\time 1/5
				s1 * 1/5
			}
			{
				\time 9/16
				s1 * 9/16
			}
			{
				s1 * 9/16
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									4-4
				}
		} {
			{
				\time 9/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16 ] ~
				}
			}
			{
				\time 1/5
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/5 {
					c'4 ~
				}
			}
			{
				\time 9/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16 ] ~
				}
			}
			{
				\time 1/5
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/5 {
					c'4 ~
				}
			}
			{
				\time 9/16
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16 ] ~
				}
			}
			{
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16
					c'16 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\pageBreak

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 4/16
				s1 * 1/4
					^ \markup {
						\override
							#'(font-name . "Courier")
							\column
								{
									"EvenRunRhythmMaker("
									"    exponent=1,"
									"    )"
								}
						}
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 1/2
				s1 * 1/2
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				\time 1/2
				s1 * 1/2
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				\time 4/16
				s1 * 1/4
			}
			{
				\time 5/16
				s1 * 5/16
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									5-1
				}
		} {
			{
				\time 4/16
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\time 5/16
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\time 1/2
				{
					c'4
					c'4
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'16 [
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 1/2
				{
					c'4
					c'4
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'16 [
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 4/16
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\time 5/16
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 1/11
				s1 * 1/11
			}
			{
				\time 3/8
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				s1 * 3/8
			}
			{
				\time 1/11
				s1 * 1/11
			}
			{
				\time 3/8
				s1 * 3/8
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									5-2
				}
		} {
			{
				\time 1/11
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/11 {
					c'16 [
					c'16 ]
				}
			}
			{
				\time 3/8
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 1/11
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/11 {
					c'16 [
					c'16 ]
				}
			}
			{
				\time 3/8
				{
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 3/15
				s1 * 1/5
			}
			{
				s1 * 1/5
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 5/24
				s1 * 5/24
			}
			{
				s1 * 5/24
			}
			{
				\time 5/16
				s1 * 5/16
			}
			{
				\time 2/12
				s1 * 1/6
			}
			{
				s1 * 1/6
			}
			{
				\time 2/8
				s1 * 1/4
			}
			{
				\time 3/28
				s1 * 3/28
			}
			{
				s1 * 3/28
			}
			{
				\time 3/16
				s1 * 3/16
			}
			{
				\time 1/9
				s1 * 1/9
			}
			{
				s1 * 1/9
			}
			{
				\time 1/8
				s1 * 1/8
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									5-3
				}
		} {
			{
				\time 3/15
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/15 {
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/15 {
					c'16 [
					c'16
					c'16
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 3/16
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\time 5/24
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\time 5/16
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\time 2/12
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'16 [
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 2/3 {
					c'16 [
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 2/8
				{
					c'16 [
					c'16
					c'16
					c'16 ]
				}
			}
			{
				\time 3/28
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/7 {
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/7 {
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\time 3/16
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\time 1/9
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/9 {
					c'16 [
					c'16 ]
				}
			}
			{
				\tweak #'edge-height #'(0.7 . 0)
				\times 8/9 {
					c'16 [
					c'16 ]
				}
			}
			{
				\time 1/8
				{
					c'16 [
					c'16 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}

\score {
	\new Score <<
		\context TimeSignatureContext = "TimeSignatureContext" {
			{
				\time 9/16
				s1 * 9/16
			}
			{
				\time 1/5
				s1 * 1/5
			}
			{
				\time 9/16
				s1 * 9/16
			}
			{
				\time 1/5
				s1 * 1/5
			}
			{
				\time 9/16
				s1 * 9/16
			}
			{
				s1 * 9/16
			}
		}
		\context RhythmicStaff = "Note-entry staff" \with {
			instrumentName = \markup {
				\hcenter-in
					#9
					\override
						#'(box-padding . 0.75)
						\box
							\italic
								\fontsize
									#2
									5-4
				}
		} {
			{
				\time 9/16
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\time 1/5
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/5 {
					c'8 [
					c'8 ]
				}
			}
			{
				\time 9/16
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				\time 1/5
				\tweak #'edge-height #'(0.7 . 0)
				\times 4/5 {
					c'8 [
					c'8 ]
				}
			}
			{
				\time 9/16
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
				}
			}
			{
				{
					c'32 [
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32
					c'32 ]
					\bar "|."
					\override Staff.BarLine #'extra-offset = #'(1.6 . 0)
				}
			}
		}
	>>
}