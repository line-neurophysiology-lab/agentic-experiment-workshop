# Agentic AI for experiment implementation

Workshop materials for a short demonstration of specification-driven experiment development with an AI coding agent.

The demonstration uses a simple auditory 1-back task:

> Press SPACE when the sound repeats.

## Repository structure

- `agentic-experiment-demo-template/` — starting point used during the live demonstration.
- `agentic-experiment-demo-finished/` — completed reference implementation.
- `trial-experiment-template/` — experiment-neutral template for developing a new trial-based experiment idea.

Start with `agentic-experiment-demo-template/WORKSHOP_GUIDE.md` for the live progression.

## Environment

Use Python 3.10 or 3.11. The three projects use the same PsychoPy dependency, so one environment at the repository root is sufficient.

### Conda

```bash
conda create -n agentic-workshop python=3.11 -y
conda activate agentic-workshop
python -m pip install --upgrade pip
python -m pip install -r agentic-experiment-demo-finished/requirements.txt
```

### Python virtual environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r agentic-experiment-demo-finished/requirements.txt
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\activate
```

## Run the completed demonstration

```bash
cd agentic-experiment-demo-finished
python main.py
```

Press SPACE when the current sound repeats the immediately preceding sound. Press Escape to stop.

## Run the tests

The tests for the scientific logic do not require PsychoPy:

```bash
cd agentic-experiment-demo-finished
python -m unittest discover -s tests -v
```

## Safety and scope

- Use synthetic participant identifiers during development and teaching.
- Physical trigger output is disabled by default.
- Do not treat the demonstration as a validated research instrument.
- Audio timing, trigger timing, and acquisition hardware require empirical validation before research use.

The included WAV stimuli are used with permission.
