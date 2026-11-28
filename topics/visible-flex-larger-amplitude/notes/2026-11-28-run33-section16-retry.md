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

## 2026-11-28 10:46:51 UTC — 33 retry实际初场及首个恢复trial

本次 run46133839513/1、job140944661119 的两个完整输入均自然返回0。science 已在自身 source `bffd5bbf0e5b5be0ded252f50613e2ca88489558`、PID3463 上执行；模型 `61c6542b3cfe39dea9fbf8c002c8ea204f5dad193ddaffe94bc7c908822682d7`，初始/current 7e06，accepted0。下面原观察对象保存全部初/current/trial/六族/实际K地点、源码/文件身份及错误；首trial291f394只开始，未返回接受或final。不借原28 accepted4。

```json
{
  "step_id": "complete-fixed-fejer-halfwave-R729-bhalf-first-20261128",
  "scientific_source_commit": "bffd5bbf0e5b5be0ded252f50613e2ca88489558",
  "scientific_source_sha256": "9b76e1c751f02495576278546b24f352993bdba6d6859fb3d826a255044bcc8b",
  "pid": 3463,
  "observations": {
    "fixed-fejer-halfwave-R729-bhalf-first/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-28 10:40:03 UTC",
      "point": "291f3943db2d5de24f7911923412fb8013b0d3cc739c09a0b5f6038a183151ad",
      "cached_angle_roots": 48,
      "closure_original_returns": 14100,
      "closure_logical_failures": 0
    },
    "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json": {
      "math_at": "2026-11-28T10:38:58.883513+00:00",
      "math_event": "trial-start",
      "math_driver": "a359ab4907b22719b01ed5a6de65e61859d313c68d4a4d3b4fe0e0822d7effd3",
      "math_model": "61c6542b3cfe39dea9fbf8c002c8ea204f5dad193ddaffe94bc7c908822682d7",
      "math_source": "4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 681.6517423825408,
      "initial_Gram": 0.4061652531176999,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 0.5305849371949052,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 681.6517423825408,
      "current_Gram": 0.4061652531176999,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 0.5305849371949052,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "trial_point": "291f3943db2d5de24f7911923412fb8013b0d3cc739c09a0b5f6038a183151ad",
      "trial_accepted": null,
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0,
      "current_g_reach": 0.5305849371949052,
      "current_g_body_diameter": -0.03813552733778258,
      "current_g_distance_plus": 0.11391238912344381,
      "current_g_distance_minus": -3.0936337267043594,
      "current_g_cap_diameter": -0.06715131487906445,
      "current_g_height_floor": -1.0411715967426867,
      "current_K": 12.32709940409259,
      "current_D_point_lower": 4.117175466515689,
      "current_K_cell": 885,
      "current_K_u": 0.8306046932331322,
      "current_K_phi": 1.5707963267948966,
      "current_K_branch": 1,
      "current_K_s": 2.1573631007205925,
      "trial_alpha": 1,
      "trial_phase": "restoration",
      "current_distance_plus_phi": 1.5707963267948966
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-halfwave-R729-bhalf-first/actual-normal-evaluation-progress.json",
      "bytes": 3335,
      "sha256": "f607050231d8c319694aae146c7a2c538180571b258a8dba59609f27b15eaddd",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "bytes": 7911,
      "sha256": "54cedbfad49c004c2abc743903c22c09eb9fe52b134204e6526069d17964ee85",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.actual_positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.geometry.maximum_physical_families",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.maximum_absolute_principal_curvature",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.returned_locations.curvature.cell",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.returned_locations.curvature.u",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.returned_locations.curvature.phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.returned_locations.curvature.branch",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-halfwave-R729-bhalf-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.returned_locations.curvature.s",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "88751d984e29169bdf894ae63e10a84dc7e76cfe3bcfa3c40b0da7f818d5a4c0",
  "observed_utc": "2026-11-28T10:40:07Z"
}
```

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46133839513-1.md",
    "bytes": 61748,
    "sha256": "5326d6e5ad912071af97a2d8216cb8a94805c343a69c933ef481ede66c5a2209",
    "git_blob_sha": "1c3735cd5312424d9bad8fc61bc2d6a49ef11227",
    "fixed_commit": "f8f98158b141106bd27cf05a6949555b463b29df",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  },
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46133839513-1-part-001.md",
    "bytes": 16604,
    "sha256": "46eb0ef0e4db851e30954d3f496c28043893538c4990f2bfbfaadbc83781aba5",
    "git_blob_sha": "c15191e2c012ee71bb31b8f405039a13c101c8a8",
    "fixed_commit": "f8f98158b141106bd27cf05a6949555b463b29df",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```

## 2026-11-28 11:40:18 UTC — 33首完整试探实拒；同方向半步已启

本retry run46133839513/1、source bffd5bbf0e5b5be0ded252f50613e2ca88489558/PID3463、model61c6542b3cfe39dea9fbf8c002c8ea204f5dad193ddaffe94bc7c908822682d7不变。首restoration全步alpha1，point291f3943db2d5de24f7911923412fb8013b0d3cc739c09a0b5f6038a183151ad，自身Phi731.1417800730309/Gram.4097559009463338先返回；随后完整试探几何actual positive g=16.64809271107871，maximum family=reach，previous_completed_trial_accepted=false，故已实际拒绝，不是只看Phi猜拒。

11:34:27.823746Z trial-start已转同restoration方向alpha.5，point8e3194c153c542c010e1f54cb0f0b4b0d24b8f1f6da3d3a288215630f4771cb0；11:35:45索引normal指该点，cached56/closures54139/logical failures0。新半步统计/几何尚未返。当前仍原7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47、accepted0、Phi681.6517423825408/Gram.4061652531176999/reachg.5305849371949052及原完整六族/K。science仍in_progress/child null，complete_report=false/stop_reason=null，whole pure未执行；两份whole原索引保全部旧新原字段及TypeError未返记录。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46133839513-1.md",
    "bytes": 61394,
    "sha256": "e28f61106aca2608d7a10a91427bbac4840f883de8453cf4a4cce48466bbecf7",
    "git_blob_sha": "554ba36ce70955c4e92c0c730f6a78e327700aca",
    "fixed_commit": "1a430eac92fc16a1e7b484c589b1205a0053afbb",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  },
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46133839513-1.md",
    "bytes": 60750,
    "sha256": "9d2f33181fcc344255df83d25f07a488f7de7489919d6c8837ee9780d00e3131",
    "git_blob_sha": "621b8f72cefe003af4be862fc6eabf53187beed5",
    "fixed_commit": "2731808f63b8ca8d368217e1f443c0bbe08fc25f",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```

## 2026-11-28 12:00:18 UTC — 33半步试探实际统计已返，仍待其全几何

46133839513/1同原source bffd5bbf0e5b5be0ded252f50613e2ca88489558/PID3463/model61c6542b3cfe39dea9fbf8c002c8ea204f5dad193ddaffe94bc7c908822682d7。11:45:20.621729+00:00恢复半步alpha.5点8e3194c153c542c010e1f54cb0f0b4b0d24b8f1f6da3d3a288215630f4771cb0实际统计Phi705.3748228317756/Gram.4078179189091087。当前接受点仍7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47、accepted0，其原Phi681.6517423825408/Gram.4061652531176999和完整六族费用保。

前一全步291f3943db2d5de24f7911923412fb8013b0d3cc739c09a0b5f6038a183151ad完整几何g16.64809271107871/reach、accepted=false不变。半步自己的完整几何尚未返回，不能用前全步或初点代它。11:50:53 normal_chain_enter为此半步、513 cached roots/66533 original closure returns/0 logical failures。所有原变量/观察/预算与自然science后whole pure62854继续。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46133839513-1.md",
    "bytes": 60395,
    "sha256": "d0a9f8620d006ce1b8b5e79b3e1fbe6959065667f2de8af8ccce91d883687803",
    "git_blob_sha": "37862f090b0a81eb23656e29fa30a407abb32bae",
    "fixed_commit": "6552609ae10573a8c3dd46a6b4599c583d3bc329",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```
