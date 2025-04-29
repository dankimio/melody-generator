import pretty_midi
import os
import time
import argparse
import random

# Default parameters for melody generation
DEFAULT_TEMPO = 120  # Default tempo in BPM (beats per minute)
DEFAULT_DURATION = 15  # Default duration of the melody in seconds
DEFAULT_OUTPUT_DIR = 'output'  # Default directory for output MIDI files
DEFAULT_VELOCITY = 100  # Default note velocity (loudness) in MIDI (0-127)
NOTE_OVERLAP_RATIO = 0.0  # No overlap between notes

# MIDI note numbers for C major scale (C4 to C5)
C_MAJOR_SCALE = [60, 62, 64, 65, 67, 69, 71, 72]  # C4, D4, E4, F4, G4, A4, B4, C5

def create_midi_instrument():
    """Creates and returns a MIDI instrument (cello) and PrettyMIDI object."""
    midi_data = pretty_midi.PrettyMIDI()
    instrument_program = pretty_midi.instrument_name_to_program('Cello')
    instrument = pretty_midi.Instrument(program=instrument_program)
    return midi_data, instrument

def get_next_note(current_note, scale):
    """Get the next note in the scale with some randomness."""
    current_index = scale.index(current_note)

    # 70% chance to move by step, 30% chance to leap
    if random.random() < 0.7:
        # Move by step (up or down)
        direction = random.choice([-1, 1])
        next_index = current_index + direction
    else:
        # Leap (up to 3 steps)
        leap_size = random.randint(2, 3)
        direction = random.choice([-1, 1])
        next_index = current_index + (leap_size * direction)

    # Ensure we stay within the scale
    next_index = max(0, min(len(scale) - 1, next_index))
    return scale[next_index]

def generate_notes(instrument, tempo, duration_seconds):
    """Generates notes for the melody and adds them to the instrument."""
    note_duration = 60.0 / tempo  # Duration of a quarter note in seconds
    start_time = 0.0

    # Start with a random note from the scale
    current_note = random.choice(C_MAJOR_SCALE)

    while start_time < duration_seconds:
        # Add some variation to note duration
        duration = note_duration * random.choice([0.5, 1.0, 1.5])  # Half, quarter, or dotted quarter note

        # Add some variation to velocity
        velocity = random.randint(DEFAULT_VELOCITY - 20, DEFAULT_VELOCITY + 20)
        velocity = max(40, min(127, velocity))  # Keep within MIDI range

        note = pretty_midi.Note(
            velocity=velocity,
            pitch=current_note,
            start=start_time,
            end=start_time + duration
        )
        instrument.notes.append(note)

        # Move to next note
        current_note = get_next_note(current_note, C_MAJOR_SCALE)
        start_time += duration

def save_midi_file(midi_data, parameters):
    """Saves the MIDI file to the specified location."""
    output_dir = parameters.get('output_dir', DEFAULT_OUTPUT_DIR)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if parameters.get('output_file'):
        filename = parameters['output_file']
    else:
        timestamp = int(time.time())
        filename = f"melody_{timestamp}.mid"

    filepath = os.path.join(output_dir, filename)
    midi_data.write(filepath)
    print(f"Generated MIDI file: {filepath}")
    return filepath

def generate_placeholder_melody(parameters):
    """Generates a simple placeholder MIDI file based on parameters."""
    # Create MIDI instrument
    midi_data, instrument = create_midi_instrument()

    # Get parameters
    tempo = parameters.get('tempo', DEFAULT_TEMPO)
    duration_seconds = parameters.get('length', DEFAULT_DURATION)

    # Generate notes
    generate_notes(instrument, tempo, duration_seconds)

    # Add instrument to MIDI data
    midi_data.instruments.append(instrument)

    # Save the file
    return save_midi_file(midi_data, parameters)

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
