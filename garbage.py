#!/usr/local/bin/python3

import os, subprocess

import mingus, random
import mingus.core.notes as notes
import mingus.core.value as value

from mingus.containers import Composition
from mingus.containers import Track
from mingus.containers import Bar
from mingus.containers import Note, NoteContainer

from mingus.midi import midi_file_out


durations = [value.whole, value.half, value.quarter, value.eighth, value.sixteenth, value.triplet(value.eighth), value.triplet(value.sixteenth)]

gypsy_scale = ["C", "C#", "E", "F", "G", "G#", "B", None, None]
gypsy_track = Track()

for note in gypsy_scale:
  gypsy_track.add_notes(note)

# print(gypsy_track)
# midi_file_out.write_Track("gypy_scale.mid", gypsy_track)
drums = {
  "snare": Note("E", 2),
  "kick": Note("C", 2),
  "hightom": Note("B", 2),
  "midtom": Note("A", 2),
  "lowtom": Note("G", 2),
  "crash": Note("A", 3),
  "hatclosed": Note("G#", 2),
  "hatopen": Note("A#", 2),
  "ride": Note("B", 3),
}

version = input("song version #: ")

gypsy_track = Track()
gypsy_bar = Bar()
# for bar in range(0,20):
#   gypsy_bar.empty()

for i in range(0,100):
  print(gypsy_bar.current_beat)
  print(gypsy_bar.space_left())
# while not gypsy_bar.is_full():
  duration = random.choice(durations)
  if duration == value.triplet(value.eighth) or duration == value.triplet(value.sixteenth):
    first  = random.choice([0,1,2,3,4])
    second = random.choice([-1,1])
    third  = second*2
    # if you get a triplet just put three in there for good measure
    gypsy_bar.place_notes(gypsy_scale[first],        duration=duration)
    gypsy_bar.place_notes(gypsy_scale[first+second], duration=duration)
    gypsy_bar.place_notes(gypsy_scale[first+third],  duration=duration)
  else:
    note = random.choice(gypsy_scale)
    if note is None:
      gypsy_bar.place_rest(duration=duration)
    else:
      gypsy_bar.place_notes(note, duration=duration)
print(gypsy_bar)
midi_file_out.write_Bar("gypsy_bar_" + version + ".mid", gypsy_bar)
gypsy_track.add_bar(gypsy_bar)

print(gypsy_track)

drum_track = Track()
kick = drums["kick"]
snare = drums["snare"]
hat = drums["hatclosed"]
# for dbar in range(0, 20):
drum_bar = Bar()
drum_bar.place_notes(NoteContainer([kick, hat]), value.eighth)
drum_bar.place_notes(hat, value.eighth)
drum_bar.place_notes(NoteContainer([kick, hat, snare]), value.eighth)
drum_bar.place_notes(hat, value.eighth)
drum_bar.place_notes(NoteContainer([kick, hat]), value.eighth)
drum_bar.place_notes(hat, value.eighth)
drum_bar.place_notes(NoteContainer([kick, hat, snare]), value.eighth)
drum_bar.place_notes(hat, value.eighth)
drum_track.add_bar(drum_bar)

midi_file_out.write_Bar("drum_bar_" + version + ".mid", drum_bar)

print(drum_track)

# song = Composition()
# song.add_track(gypsy_track)
# song.add_track(drum_track)

# midi_file_out.write_Composition("garbage_" + version + ".mid", song)






# track = Track()
# for i in range(0,12):
#   track.add_notes(notes.int_to_note(i))

# midi_file_out.write_Track("test.mid", track)
