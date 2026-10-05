# Experiment specification

## Objective

Implement a short auditory 1-back demonstration. The participant presses Space when the current audio file is identical to the immediately preceding audio file.

## Block rules

- 12 trials.
- Exactly four go trials.
- Trial 1 is no-go.
- A go trial repeats the immediately preceding file exactly.
- A no-go trial must not repeat the immediately preceding file.
- The integer seed must reproduce the complete sequence.
- Use face and scrambled-face WAV files. Retain letter files but do not use them in this block.

## Interaction and timing

- Response: Space.
- Abort: Escape.
- Response window: 1.2 seconds from the software audio-play command.
- Inter-trial interval: 0.4 seconds.

## Active trigger codes

| Event | Code |
|---|---:|
| one-back start | 5 |
| go face | 6 |
| go scrambled face | 7 |
| no-go face | 9 |
| no-go scrambled face | 10 |
| button press | 12 |

Hardware trigger output must default to off. Simulated events should remain observable.

## Acceptance criteria

- Same seed, same sequence.
- Exactly four true repetitions and no accidental no-go repetitions.
- One output row per completed trial.
- Output matches the data dictionary.
- Scientific logic is tested without requiring PsychoPy.
