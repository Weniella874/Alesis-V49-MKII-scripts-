# name=Alesis V49 MKII transport panel

# BEGIN THE SCRIPT!!!

import transport

import midi


# BASIC TRANSPORT CONTROLS

Transport_START = 20

Transport_STOP = 21

Transport_RECORD = 22


def OnMidiMsg(event):

 event.handled = False

 if event.midiId == midi.MIDI_CONTROLCHANGE:

	 # START BUTTON

	 if event.data1 == Transport_START and event.data2 > 0:

		 transport.start()

		 event.handled = True

	 # STOP BUTTON

	 elif event.data1 == Transport_STOP and event.data2 > 0:

		 transport.stop()

		 event.handled = True

	 # RECORD BUTTON`

	 elif event.data1 == Transport_RECORD and event.data2 > 0:

		 transport.record()

		 event.handled = True