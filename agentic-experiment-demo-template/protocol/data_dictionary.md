# Trial-level data dictionary

| Column | Type | Meaning |
|---|---|---|
| `participant_id` | text | Synthetic session identifier |
| `seed` | integer | Randomization seed |
| `trial` | integer | One-based trial number |
| `stimulus` | text | WAV filename |
| `stimulus_category` | category | `f`, `sf`, or `l` |
| `is_go` | boolean | Intended immediate repetition |
| `stimulus_trigger` | integer | Condition/category trigger code |
| `responded` | boolean | Space pressed within response window |
| `response_trigger` | integer/blank | 12 on response; blank otherwise |
| `correct` | boolean | Whether response matched go/no-go status |
| `reaction_time_ms` | integer/blank | Software response time; blank without response |

One row represents one completed trial. Missing responses are blank, not zero.
