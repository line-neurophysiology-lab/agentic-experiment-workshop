# Data dictionary

Define the final columns before implementing export. Remove fields that do not apply and add task-specific fields explicitly.

## Suggested session fields

| Field | Type | Required | Meaning and valid values |
|---|---|---:|---|
| `participant_id` | text | yes | Synthetic identifier during development |
| `session` | integer/text | TBD | Session identity |
| `seed` | integer | yes | Seed needed to reproduce scheduling |
| `protocol_version` | text | recommended | Version of the approved specification |

## Suggested block fields

| Field | Type | Required | Meaning and valid values |
|---|---|---:|---|
| `block` | integer | if blocked | One-based block number |
| `block_condition` | category | TBD | Condition assigned at block level |
| `block_order` | integer | TBD | Presented position or counterbalancing assignment |

## Suggested trial fields

| Field | Type | Required | Meaning and valid values |
|---|---|---:|---|
| `trial` | integer | yes | One-based trial number within the declared scope |
| `trial_condition` | category | TBD | Condition applying to the trial |
| `stimulus` | text | TBD | Stable stimulus identifier or filename |
| `expected_response` | text/blank | TBD | Correct response according to protocol |
| `participant_response` | text/blank | yes | Recorded response; blank convention must be defined |
| `correct` | boolean/blank | TBD | Scored outcome if correctness applies |
| `reaction_time_ms` | integer/blank | TBD | Software response latency and reference event |
| `stimulus_trigger` | integer/blank | TBD | Presented event code |
| `response_trigger` | integer/blank | TBD | Response event code |

## Row and file conventions

- Unit of one row: TBD
- File naming: TBD
- Missing-value representation: TBD
- Boolean serialization: TBD
- Partial/aborted run policy: TBD
- Overwrite policy: never overwrite silently
