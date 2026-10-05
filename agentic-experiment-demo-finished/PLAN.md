# Implementation plan

## Outcome

Create a minimal, reproducible PsychoPy auditory 1-back task that demonstrates specification-driven agentic experiment implementation.

## Completed milestones

- [x] Record scientific rules and exclusions.
- [x] Define the trial-level data contract.
- [x] Discover and classify the supplied WAV files.
- [x] Implement deterministic 1-back randomization.
- [x] Implement the original trigger vocabulary with safe simulation by default.
- [x] Implement PsychoPy presentation and response collection.
- [x] Prevent consecutive sounds from overlapping, including after an early response.
- [x] Export timestamped trial-level CSV data.
- [x] Test randomization, triggers, and export independently of PsychoPy.

## Scientist validation still required

- [ ] Confirm stimulus content and category labels.
- [ ] Confirm response window and inter-trial interval.
- [ ] Measure audio and trigger latency on the acquisition computer.
- [ ] Verify the parallel-port address and trigger decoding with EEG acquisition.
- [ ] Approve the protocol before collecting research data.
