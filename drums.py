#!/usr/local/bin/python3

import mingus, random
import mingus.core.notes as notes
import mingus.core.value as value

from mingus.containers import Composition
from mingus.containers import Track
from mingus.containers import Bar
from mingus.containers import Note, NoteContainer

from mingus.midi import midi_file_out

drum_scale = {
  "snare": Note("E", 2),
  "bass": Note("C", 2),
  "hightom": Note("B", 2),
  "midtom": Note("A", 2),
  "lowtom": Note("G", 2),
  "crash": Note("A", 3),
  "hatclosed": Note("G#", 2),
  "hatopen": Note("A#", 2),
  "ride": Note("B", 3),
  }

values = [value.quarter, value.eighth, value.sixteenth, value.triplet(value.eighth), value.triplet(value.sixteenth)]
#for i in range(0, 24):
#  bar =
drum_track = Track()

for note in drum_scale:
  drum_track.add_notes(drum_scale[note])

print(drum_track)
midi_file_out.write_Track("drum_scale.mid", drum_track)
