# Melody Generator

A simple command-line tool for generating MIDI melodies using Python. This tool creates basic melodies in C major scale using a cello instrument.

## Features

- [ ] Generate MIDI melodies with customizable parameters
- [ ] Adjustable tempo and duration
- [ ] Custom output directory and filename support
- [ ] Simple C major scale-based melody generation
- [ ] Uses the PrettyMIDI library for MIDI file generation

## Requirements

- [ ] Python 3.x
- [ ] pip (Python package installer)

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd melody_generator
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The script can be run from the command line with various options:

```bash
python melody_generator.py [options]
```

### Command Line Options

- [ ] `--tempo`: Set the tempo in BPM (default: 120)
- [ ] `--length`: Set the duration in seconds (default: 15)
- [ ] `--output-dir`: Specify the output directory (default: 'static')
- [ ] `--output-file`: Specify a custom output filename (optional)

### Examples

Basic usage with defaults:

```bash
python melody_generator.py
```

Custom tempo and length:

```bash
python melody_generator.py --tempo 140 --length 30
```

Custom output directory and filename:

```bash
python melody_generator.py --output-dir "my_melodies" --output-file "my_song.mid"
```

Full example with all options:

```bash
python melody_generator.py --tempo 160 --length 20 --output-dir "output" --output-file "fast_melody.mid"
```

## Output

The script generates a MIDI file in the specified output directory. If no output filename is provided, it will generate one with a timestamp (e.g., `melody_1234567890.mid`).

## Current Limitations

- Only generates melodies in C major scale
- Uses a cello instrument only
- Basic melody generation without complex musical patterns
- No support for different keys or scales
- No support for different instruments

## Future Improvements

- [ ] Add support for different musical scales and keys
- [ ] Implement more complex melody patterns
- [ ] Add support for multiple instruments
- [ ] Include rhythm variations
- [ ] Add support for different musical styles
