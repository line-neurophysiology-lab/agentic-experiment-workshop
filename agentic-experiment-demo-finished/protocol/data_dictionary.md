# Trial-level data dictionary

| Column | Type | Meaning |
|---|---|---|
| `participant_id` | text | Synthetic identifier entered at launch |
| `seed` | integer | Seed used to reproduce randomization |
| `trial` | integer | One-based trial number |
| `stimulus` | text | WAV filename |
| `stimulus_category` | category | `f` face, `sf` scrambled face, or `l` letter |
| `is_go` | boolean | Whether the stimulus intentionally repeats the previous file |
| `stimulus_trigger` | integer | Condition/category trigger code |
| `responded` | boolean | Whether Space was pressed in the response window |
| `response_trigger` | integer/blank | 12 when a response occurred; blank otherwise |
| `correct` | boolean | `responded == is_go` |
| `reaction_time_ms` | integer/blank | Software response time in milliseconds; blank without response |

One row represents one presented trial. Empty response values are written as blank cells, not zero.
