import pretty_midi
import os
import time

def generate_placeholder_melody(parameters):
    """Generates a simple placeholder MIDI file based on parameters."""
    try:
        # Create a PrettyMIDI object
        midi_data = pretty_midi.PrettyMIDI()
        # Create an Instrument instance for a cello instrument
        instrument_program = pretty_midi.instrument_name_to_program('Cello')
        instrument = pretty_midi.Instrument(program=instrument_program)

        # Use parameters (simplified for placeholder)
        tempo = parameters.get('tempo', 120)
        duration_seconds = parameters.get('length', 15)
        # Key parameter is complex to implement simply, ignoring for placeholder
        # Genre/Mood/Preferences ignored for placeholder

        # Calculate note duration based on tempo
        # Let's create a simple C major scale pattern
        notes = [60, 62, 64, 65, 67, 69, 71, 72] # C4 to C5
        note_duration = 60.0 / tempo # Duration of a quarter note in seconds
        start_time = 0.0

        # Add notes
        num_notes = int(duration_seconds / note_duration)
        for i in range(num_notes):
            note_number = notes[i % len(notes)]
            note = pretty_midi.Note(
                velocity=100, pitch=note_number, start=start_time, end=start_time + note_duration * 0.9 # Slightly shorter to avoid overlap
            )
            instrument.notes.append(note)
            start_time += note_duration
            if start_time >= duration_seconds:
                break

        # Add the instrument to the PrettyMIDI object
        midi_data.instruments.append(instrument)

        # Define path to save the MIDI file
        static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')
        if not os.path.exists(static_dir):
            os.makedirs(static_dir)
        
        timestamp = int(time.time())
        filename = f"melody_{timestamp}.mid"
        filepath = os.path.join(static_dir, filename)
        
        # Write out the MIDI data
        midi_data.write(filepath)

        # Return the relative path for web access
        return f"/static/{filename}"

    except Exception as e:
        print(f"Error generating placeholder MIDI: {e}")
        raise
