# math-research-ci

Public runner for long computations of a private repository. Jobs run on GitHub-hosted
`ubuntu-latest` (4 CPU, 16 GB RAM, up to ~6 h per job, up to 20 jobs in parallel).

Every 5 minutes this repo claims the request files in the private repo's `ci-queue/` folder
(removing them there) and runs each one as a separate job. Output never goes to this public
repo: stdout/stderr, `status.json` and every file the command writes under the topic folder
are committed back to the private repo.
