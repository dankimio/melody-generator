import pretty_midi
import os
import time
import argparse

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
        output_dir = parameters.get('output_dir', 'static')
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

        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Generate filename
        if parameters.get('output_file'):
            filename = parameters['output_file']
        else:
            timestamp = int(time.time())
            filename = f"melody_{timestamp}.mid"

        filepath = os.path.join(output_dir, filename)

        # Write out the MIDI data
        midi_data.write(filepath)
        print(f"Generated MIDI file: {filepath}")

        return filepath

    except Exception as e:
        print(f"Error generating placeholder MIDI: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Generate a simple MIDI melody.')
    parser.add_argument('--tempo', type=int, default=120,
                      help='Tempo in BPM (default: 120)')
    parser.add_argument('--length', type=int, default=15,
                      help='Duration in seconds (default: 15)')
    parser.add_argument('--output-dir', type=str, default='static',
                      help='Output directory for MIDI file (default: static)')
    parser.add_argument('--output-file', type=str,
                      help='Output filename (default: melody_TIMESTAMP.mid)')

    args = parser.parse_args()

    parameters = {
        'tempo': args.tempo,
        'length': args.length,
        'output_dir': args.output_dir,
        'output_file': args.output_file
    }

    generate_placeholder_melody(parameters)

if __name__ == '__main__':
    main()
