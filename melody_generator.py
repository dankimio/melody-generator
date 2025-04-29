import pretty_midi
import os
import time
import argparse

# Default parameters for melody generation
DEFAULT_TEMPO = 120  # Default tempo in BPM (beats per minute)
DEFAULT_DURATION = 15  # Default duration of the melody in seconds
DEFAULT_OUTPUT_DIR = 'output'  # Default directory for output MIDI files
DEFAULT_VELOCITY = 100  # Default note velocity (loudness) in MIDI (0-127)
NOTE_OVERLAP_RATIO = 0.9  # Ratio to prevent note overlap (0.9 means notes are 90% of their full duration)

# MIDI note numbers for C major scale (C4 to C5)
C_MAJOR_SCALE = [60, 62, 64, 65, 67, 69, 71, 72]  # C4, D4, E4, F4, G4, A4, B4, C5

def generate_placeholder_melody(parameters):
    """Generates a simple placeholder MIDI file based on parameters."""
    # Create a PrettyMIDI object
    midi_data = pretty_midi.PrettyMIDI()
    # Create an Instrument instance for a cello instrument
    instrument_program = pretty_midi.instrument_name_to_program('Cello')
    instrument = pretty_midi.Instrument(program=instrument_program)

    # Use parameters (simplified for placeholder)
    tempo = parameters.get('tempo', DEFAULT_TEMPO)
    duration_seconds = parameters.get('length', DEFAULT_DURATION)
    output_dir = parameters.get('output_dir', DEFAULT_OUTPUT_DIR)
    # Key parameter is complex to implement simply, ignoring for placeholder
    # Genre/Mood/Preferences ignored for placeholder

    # Calculate note duration based on tempo
    note_duration = 60.0 / tempo # Duration of a quarter note in seconds
    start_time = 0.0

    # Add notes
    num_notes = int(duration_seconds / note_duration)
    for i in range(num_notes):
        note_number = C_MAJOR_SCALE[i % len(C_MAJOR_SCALE)]
        note = pretty_midi.Note(
            velocity=DEFAULT_VELOCITY,
            pitch=note_number,
            start=start_time,
            end=start_time + note_duration * NOTE_OVERLAP_RATIO
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

def main():
    parser = argparse.ArgumentParser(description='Generate a simple MIDI melody.')
    parser.add_argument('--tempo', type=int, default=DEFAULT_TEMPO,
                      help=f'Tempo in BPM (default: {DEFAULT_TEMPO})')
    parser.add_argument('--length', type=int, default=DEFAULT_DURATION,
                      help=f'Duration in seconds (default: {DEFAULT_DURATION})')
    parser.add_argument('--output-dir', type=str, default=DEFAULT_OUTPUT_DIR,
                      help=f'Output directory for MIDI file (default: {DEFAULT_OUTPUT_DIR})')
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
