# Agentic experiment demo — finished product

This is the completed counterpart to `agentic-experiment-demo-template`. It shows the end state of the workshop progression: scientific specification → agent instructions → plan → modular implementation → tests → inspectable output.

## Run

Use Python 3.10 or 3.11:

```bash
pip install -r requirements.txt
python main.py
```

Press Space only when the current sound exactly repeats the preceding sound. Press Escape to stop. CSV files are written to `data/synthetic/`.

## Test

```bash
python -m unittest discover -s tests -v
```

The tests do not require PsychoPy.

## Safety

Triggers are simulated by default. Do not set `USE_PARALLEL_PORT = True` until the scientist has validated the address, codes, pulse duration, audio latency, and EEG acquisition setup.
