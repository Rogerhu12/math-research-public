# Retry of public run 33 after the root README change

The new request `visible-larger-resume-20261128-33-retry-section16` uses the original run33 workflow and controller. Changing the existing request path under an ordinary push starts a fresh GitHub run with a new runner, run ID and work directory. Its active request and queue parent share the new identifier. Both original deterministic input steps and the whole original R729 science step will execute afresh. A successful science return enables the original whole pure step in that new job.

The original run 46130690181/1, job 140934949073, exited at the publication of the second input record. The first input had already been published. The complete 64705-byte job log, SHA-256 ad490cac7f23076de59607b79514f6a2df58009836c9bc73cc3b55c02b6c06ac, records the second input as completed with exit 0 at 09:38:53.3589567 UTC after 499.935978069 seconds. It identifies source checkout 77b0048525a4ae51aad18ab36dc64f5ec849b44a, PID 2969 and the 84971-byte report with SHA-256 c2ac7be69f718960b53a3f8c887ab54d619d517cb1dfb66cfdd58451dab0b423. The ordinary pull in Publisher.sync then found the newly added root README section 16. The controller raised its documented README-change error and the workflow research step failed at 09:38:54 UTC. The original public index consequently contains only the first complete input record. The original job produced no solver field or final. The retry takes neither earlier runner-local input as a substitute for executing the two original steps.

The root rule change was read and acknowledged at f57995b11d7b9e390d61a6f363cdf50bf5febc43. Both fixed README identities at 60e476a228cda7c9d485fd220d0507e58a4b2e2a are in the retry request. The source and parameter families are still the original positive paired-halfwave family from run 28 plus the shared R729 recovery, published at 3ff5795e46cc5a2b50f0ba27d6c747a00bc54d03. All 137 original scientific role pairs remain, with the R729 kernel giving 138 total and 21 runtime sources. The original 157 and 7 scientific/pure argument words, every literal source guard, the original 575/564 formal fields, 64 live fields, 32-stage domain and 4/64/15 restoration budgets are complete. The source, ready files, peer history, original request and queue are immutable whole references in the delivery. The original controller still uses the 350-minute admission checkpoint, 360-minute workflow timeout and 30-second capacity wait.

The fresh three-step queue requires 80280 bytes. The deferred complete pure-only queue requires 62854 bytes and has SHA-256 e96e9bc7135e82e401b86b6fdf62723545cd1a7ce81798ab8aeea337a2bd4639. After the new job's own science returns, serialize the original pure-ready steps with the new parent request ID and finish_when_done=false. All new source checkouts, input hashes, model, point, scientific reports and certificates await actual evidence.

```sh
node topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_run33_section16_retry.mjs --source-repository . --output-repository /tmp/run33-section16
```

The reproducer reads the complete original request and queue by their Git identities if their active paths have advanced. It regenerates the complete replacement request and queue without evaluating any scientific function.

## 新runner已实际启动

官方已返回run46133839513/1、job140944661119，head993d07aa8dc89bff8b8f5ad49c52b64cef960741；job10:09:49Z、研究步骤10:10:37Z开始。此刻in_progress/conclusion=null，尚未取得本次完整索引/输入返回。新source checkout/model/point/最终report/typed仍等待自身实际记录，不借原33两个input数值。原33 failure与新run编号严格区分。

```json
{
  "total_count": 1,
  "jobs": [
    {
      "id": 140944661119,
      "run_id": 46133839513,
      "workflow_name": "Visible larger amplitude halfwave R729 common slack 20261128 33",
      "head_branch": "main",
      "run_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46133839513",
      "run_attempt": 1,
      "node_id": "CR_kwDOVt5L2s8AAAAg0PTafw",
      "head_sha": "993d07aa8dc89bff8b8f5ad49c52b64cef960741",
      "url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/jobs/140944661119",
      "html_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46133839513/job/140944661119",
      "status": "in_progress",
      "conclusion": null,
      "created_at": "2026-11-28T10:09:47Z",
      "started_at": "2026-11-28T10:09:49Z",
      "completed_at": null,
      "name": "Construct the same fixed target and solve original halfwave with R729 common slack",
      "steps": [
        {
          "name": "Set up job",
          "status": "completed",
          "conclusion": "success",
          "number": 1,
          "started_at": "2026-11-28T10:09:49Z",
          "completed_at": "2026-11-28T10:09:50Z"
        },
        {
          "name": "Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
          "status": "completed",
          "conclusion": "success",
          "number": 2,
          "started_at": "2026-11-28T10:09:50Z",
          "completed_at": "2026-11-28T10:09:59Z"
        },
        {
          "name": "Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
          "status": "completed",
          "conclusion": "success",
          "number": 3,
          "started_at": "2026-11-28T10:09:59Z",
          "completed_at": "2026-11-28T10:10:06Z"
        },
        {
          "name": "Install the recorded numerical and automatic differentiation dependencies",
          "status": "completed",
          "conclusion": "success",
          "number": 4,
          "started_at": "2026-11-28T10:10:06Z",
          "completed_at": "2026-11-28T10:10:37Z"
        },
        {
          "name": "Execute public research and publish independent compact records",
          "status": "in_progress",
          "conclusion": null,
          "number": 5,
          "started_at": "2026-11-28T10:10:37Z",
          "completed_at": null
        },
        {
          "name": "Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
          "status": "pending",
          "conclusion": null,
          "number": 9,
          "started_at": null,
          "completed_at": null
        },
        {
          "name": "Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
          "status": "pending",
          "conclusion": null,
          "number": 10,
          "started_at": null,
          "completed_at": null
        }
      ],
      "check_run_url": "https://api.github.com/repos/Rogerhu12/math-research-public/check-runs/140944661119",
      "labels": [
        "ubuntu-latest"
      ],
      "runner_id": 1000012834,
      "runner_name": "GitHub Actions 1000012834",
      "runner_group_id": 0,
      "runner_group_name": "GitHub Actions"
    }
  ]
}
```
