# Experiment specification

## Objective

Demonstrate a short auditory 1-back task derived from SSD-stimuli-EEG. The participant responds when an audio file is identical to the immediately preceding file.

## Block

- 12 trials per demonstration block.
- Exactly four go trials.
- Trial 1 is always no-go.
- Go: repeat the preceding file exactly.
- No-go: select any active stimulus other than the preceding file.
- Sequence generation is deterministic from an integer seed.
- Active categories: face and scrambled face. Letter WAV files are retained but excluded from this block.

## Response and timing

- Response key: Space.
- Abort key: Escape.
- Response window: 1.2 seconds from the software audio-play command.
- Inter-trial interval: 0.4 seconds.
- A trial remains active until both the response window and audio playback have ended.
- Audio stimuli must never overlap.
- The inter-trial interval begins only after the current trial has ended.
- Only the first Space press within the response window is recorded.
- These software timings are not validated measures of physical audio onset.

## Trigger map

| Event | Code |
|---|---:|
| passive start | 1 |
| passive face | 2 |
| passive scrambled face | 3 |
| passive letter | 4 |
| one-back start | 5 |
| go face | 6 |
| go scrambled face | 7 |
| go letter | 8 |
| no-go face | 9 |
| no-go scrambled face | 10 |
| no-go letter | 11 |
| button press | 12 |

Triggers are logged but hardware output is disabled by default.

## Acceptance criteria

- The same seed produces the same sequence.
- Exactly four trials are true repetitions.
- No no-go trial accidentally repeats the preceding file.
- Every completed trial produces one CSV row.
- CSV fields conform to the data dictionary.
- Consecutive audio stimuli do not overlap, including after an early response.
