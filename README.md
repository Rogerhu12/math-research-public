# math-research-ci

Public runner for long computations of a private repository. Jobs run on GitHub-hosted
`ubuntu-latest` (4 CPU, 16 GB RAM, up to ~6 h per job, up to 20 jobs in parallel).

Submit a job by committing a JSON file under `requests/` (any subfolder). Each new or
changed request file starts one job. Output never goes to this public repo: the job's
stdout/stderr, `status.json` and every file the command writes under the topic folder are
committed back to the private repo. Public logs show only the exit code.

Request fields: `topic` (folder name under `topics/`), `command` (bash, run from the private
repo root), optional `timeout_minutes` (default 300, max 350), `sparse` (extra paths to
check out), `python` (default 3.12), `node` (default 24).
