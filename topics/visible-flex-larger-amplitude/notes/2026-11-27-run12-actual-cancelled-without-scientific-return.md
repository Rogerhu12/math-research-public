# 公开 run12 的真实取消终态：完整科学步骤未自然回传

## 1. 已核终态

在 **2026-11-27 19:48:01 UTC** 的实际只读观察中，公开运行 [46011377225/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46011377225) 的官方 API 为 `completed / cancelled`。Job `140547455454` 及其第 5 个 research step 也为 `completed / cancelled`。这是运行终态，不是原完整求解器的正常完成记录。

官方 run 的 `created_at`、`run_started_at` 均为 `2026-11-27T13:56:02Z`；`updated_at` 为 `2026-11-27T19:46:23Z`。后者是官方 run 更新时间，不冒充本工具未返回的单独 job 完成时间。初始实际 head 为 `ed9fbfec354330d11b0e46ef61a4d0565b88dfc6`。请求声明的 workflow 上限为 350 分钟、controller admission budget 为 20000 秒；请求明确运行中的科学 child 不因 admission budget 自动被记作完成。本记录没有独立核实取消的具体主体或日志原因。

完整官方 job 包装返回及准确 run 字段投影如下；字段投影不是完整 raw API 响应的别名：

```json
{
  "observed_at_utc": "2026-11-27 19:48:01 UTC",
  "official_run_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46011377225",
  "official_api_run_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46011377225",
  "official_run_fields": {
    "id": 46011377225,
    "name": "Visible larger amplitude predetermined complete fixed input 20261127 12",
    "head_sha": "ed9fbfec354330d11b0e46ef61a4d0565b88dfc6",
    "path": ".github/workflows/visible-larger-20261127-parallel12.yml",
    "run_number": 1,
    "event": "push",
    "status": "completed",
    "conclusion": "cancelled",
    "workflow_id": 432798115,
    "created_at": "2026-11-27T13:56:02Z",
    "updated_at": "2026-11-27T19:46:23Z",
    "run_started_at": "2026-11-27T13:56:02Z",
    "run_attempt": 1,
    "html_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46011377225",
    "jobs_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46011377225/jobs"
  },
  "complete_job_wrapper_response": {
    "jobs": [
      {
        "id": 140547455454,
        "name": "Construct the predetermined fixed input and run complete-field research",
        "status": "completed",
        "conclusion": "cancelled",
        "run_id": 46011377225,
        "logs_url": null,
        "steps": [
          {
            "name": "Set up job",
            "status": "completed",
            "conclusion": "success",
            "number": 1
          },
          {
            "name": "Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
            "status": "completed",
            "conclusion": "success",
            "number": 2
          },
          {
            "name": "Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
            "status": "completed",
            "conclusion": "success",
            "number": 3
          },
          {
            "name": "Install the recorded numerical and automatic differentiation dependencies",
            "status": "completed",
            "conclusion": "success",
            "number": 4
          },
          {
            "name": "Execute public research and publish independent compact records",
            "status": "completed",
            "conclusion": "cancelled",
            "number": 5
          },
          {
            "name": "Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
            "status": "completed",
            "conclusion": "skipped",
            "number": 9
          },
          {
            "name": "Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
            "status": "completed",
            "conclusion": "success",
            "number": 10
          },
          {
            "name": "Complete job",
            "status": "completed",
            "conclusion": "success",
            "number": 11
          }
        ]
      }
    ]
  },
  "job_detail_timestamp_not_returned_by_available_wrapper": true,
  "cancellation_reason_not_established_by_this_record": true
}
```

## 2. 原公共小卷仍只有两个真实输入返回

终态观察时，公共索引仍保存 **19:41:24 UTC** 的进行中记录，而不是一份新增自然科学返回。已完成阶段只列出原两次必要输入：

- 阶段 1：`prepare-complete-fixed-fejer-r690-inputs-20261127`，`completed`，exit `0`，5.893721085999999 秒；实际 source commit `97051366b05adc2a6aa27c845f712c5b79edfdff`，完整入口 SHA-256 `89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60`。
- 阶段 2：`prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run12`，`completed`，exit `0`，430.2165345 秒；实际 source commit `6e7fc7dc687960599e398087f9e1f574bdc2a738`，完整入口 SHA-256 `e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb`。

这两记录的原完整命令、全部实际输入、输出 record、source commit、完整输出 SHA 和紧凑数值仍逐字在下列原分卷内。本次未修改、删除或重新执行这些输入阶段，也未把终态当作新的科学返回。

```json
{
  "last_index": {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46011377225-1.md",
    "bytes": 9684,
    "sha256": "5d4d4d3367e7e272fa9f21de47022de3ef708ed24db63889325fcf84bf085451",
    "git_blob_sha": "2da2e686db6e3f63f5afc16e7ca5e89c6556becd"
  },
  "complete_returned_part": {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46011377225-1-part-001.md",
    "bytes": 16600,
    "sha256": "5c093747e64ca227983e72590db4f5fc9bcc6fc950889504ee85edc8df30472a",
    "git_blob_sha": "2daddb631388db54dd4309857297294c332faf1a"
  }
}
```

完整公开路径：

- `topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46011377225-1.md`。
- `topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46011377225-1-part-001.md`。

原分卷的两个 JSON 对象均完整存在；未见第三个自然返回对象或第二卷。其完整返回对象的关键实际字段如下，其余完整原字段以以上固定整 blob 为准：

```json
[
  {
    "name": "followup:prepare-complete-fixed-fejer-r690-inputs-20261127",
    "state": "completed",
    "returncode": 0,
    "seconds": 5.893721085999999,
    "scope": "Necessary complete deterministic new mathematical input. Restore the exact accepted099 scalar-parameter source; extract the whole e640 projection; construct the fixed seven-mode RN-even Fejer chart, all 923 exact affine nodes and complete FullHold node/radius error ledger. No warm/BVP/pulse field, old core, old final, F/J/normal root or geometric certificate is used. This is a new fixed target; original branches and old literal-address provenance are retained explicitly.",
    "step_id": "prepare-complete-fixed-fejer-r690-inputs-20261127",
    "source_commit": "97051366b05adc2a6aa27c845f712c5b79edfdff",
    "source_sha256": "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60",
    "command": [
      "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
      "-u",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/followup-sources/0001-167d7c1a5813-97051366b05a/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py",
      "--repo",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/followup-sources/0001-167d7c1a5813-97051366b05a",
      "--outdir",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs",
      "--panels",
      "128"
    ],
    "input_files": [
      {
        "role": "source",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py",
        "commit": "97051366b05adc2a6aa27c845f712c5b79edfdff",
        "sha256": "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60"
      },
      {
        "role": "followup_queue",
        "path": "topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-12.json",
        "path_commit": "ed9fbfec354330d11b0e46ef61a4d0565b88dfc6",
        "checkout_commit": "97051366b05adc2a6aa27c845f712c5b79edfdff",
        "sha256": "6abc9ba8570ef97dbc957955958e4c314632cec33b1f3687a5aad305417e8e1b"
      }
    ],
    "outputs": [
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/report.json",
        "sha256": "255094e105fcddf87f35c326dce107f8524e83961bc21ee09153ba7af56aec32",
        "bytes": 65332
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz",
        "sha256": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
        "bytes": 4334
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
        "sha256": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
        "bytes": 144306
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json",
        "sha256": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
        "bytes": 40488
      }
    ],
    "missing_outputs": [],
    "summary_errors": []
  },
  {
    "name": "followup:prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run12",
    "state": "completed",
    "returncode": 0,
    "seconds": 430.2165345,
    "scope": "Necessary complete reference construction for the one predeclared Fejer RN-even64 chart and complete original R690 scalar. Consume all real fixed-input products from the independent formula maker, preserve all 923 exact nodes, 7377 positive observations and every eight-Gauss/reference scalar jet. The scalar integer table uses a predeclared 2218-leaf rule; H is the original complete normalized-c Gauss seed and remains free. Reinterpret the full ordered eleven-payload historical literals explicitly on the new target and mesh, without claiming same physical s/point or inheriting unknown old history, field values, certificates, or completion. This is necessary input construction, not a scientific fixture or proof.",
    "step_id": "prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run12",
    "source_commit": "6e7fc7dc687960599e398087f9e1f574bdc2a738",
    "source_sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
    "command": [
      "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
      "-u",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/followup-sources/0002-a73af5287d15-6e7fc7dc6879/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
      "--repo",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/followup-sources/0002-a73af5287d15-6e7fc7dc6879",
      "--fixed-input",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz",
      "--fixed-input-report",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/report.json",
      "--node-report",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
      "--scalar-input",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json",
      "--manifest",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/followup-sources/0002-a73af5287d15-6e7fc7dc6879/topics/visible-flex-larger-amplitude/scripts/resume_20261120/a04_historical_location_seeds.json",
      "--outdir",
      "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference",
      "--angles",
      "2048",
      "--seed-integration-order",
      "8",
      "--panels",
      "128",
      "--scalar-leaf-count",
      "2218",
      "--scalar-integral-tolerance",
      "1e-18",
      "--scalar-tail-cutoff",
      "1/8"
    ],
    "input_files": [
      {
        "role": "source",
        "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
        "commit": "6e7fc7dc687960599e398087f9e1f574bdc2a738",
        "sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
      },
      {
        "role": "followup_queue",
        "path": "topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-12.json",
        "path_commit": "ed9fbfec354330d11b0e46ef61a4d0565b88dfc6",
        "checkout_commit": "97051366b05adc2a6aa27c845f712c5b79edfdff",
        "sha256": "6abc9ba8570ef97dbc957955958e4c314632cec33b1f3687a5aad305417e8e1b"
      }
    ],
    "outputs": [
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/report.json",
        "sha256": "a35e7ed22d3453d69cc746ff6b706735717bb74131d43ece0b7ddda440403900",
        "bytes": 84966
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/reference.npz",
        "sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
        "bytes": 894879
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/observations.npz",
        "sha256": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
        "bytes": 205842
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/locations.json",
        "sha256": "ba4cd7ba201044b950dab70f4ea5606d79a6202c8ef5b534bb4a611d014eb5a7",
        "bytes": 106771
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/supplied-location-provenance.json",
        "sha256": "e5526478ae6f6e6a141ebdb67636e4231f37862bb5b5b260c09c5830f0ade329",
        "bytes": 223955
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/fixed-target-definition.json",
        "sha256": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
        "bytes": 30919
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-46011377225-1/research/fixed-fejer-reference/material-envelope-carrier-binding.json",
        "sha256": "a6992516e83b53e153bf5d2b9ef8985f7542bff615e2b3edd6e467a2d105f52b",
        "bytes": 35712
      }
    ],
    "missing_outputs": [],
    "summary_errors": []
  }
]
```

## 3. 未自然返回的真实科学 child

最后公开 scalar 记录的 step 为：

`complete-fixed-fejer-immutable-point-first-20261127-run12`

其实际 child PID 为 `3347`；实际 scientific source commit 为 `a3df4eae39988724cca2cc3c38927e583c24eb2e`，实际 launcher SHA-256 为 `0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf`。该 child 的退出码在已发布观察里仍为 null。没有把 GitHub 的 `cancelled` 换成一个未观察到的 Python/launcher exit code。

该入口对应已刊完整 Fejér M160/J923/N2048、7377 material radial observations、完整 1,333,370 个外层变量、原 32 段 normal partition 和原完整数值预算。正式数学目标是预先公开的 RN-even64 Fejér 七项图及完整 R690 标量律；它没有借旧 warm 选出的未知图。原 request 与完整 argv 责任继续保存在原已刊输入/求解计划及完整 followup 队列：

`topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-12.json`

已刊完整求解族中的 driver `477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd`、normal `1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778` 和 pure reader `274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b` 限定这一未返责任。新 stage-point/meridian-cache/batching 源没有替换该运行中的旧源。

## 4. 完整最后标量观察及边界

最后发布的 actual normal 数据时间为 **19:41:20 UTC**。它确实记录了 full point `507253778ce58f9025ca9078abb81bcecd3698e2f540c6bfaeaec9c06ab34902`，当前 scope requested angular order 为 2，scope angle count 为 1，已缓存角数为 1228。closure 请求/返回均为 1,769,743，逻辑失败为 0；原 closure 返回 848,643，缓存命中 921,100；scope started/closed 为 6171/6170。

这些是最后一次被公共索引捕获的 mutable scalar 观察。它们没有报告该 full point 已被接受、没有给出新的 Phi/Gram/完整 geometry 数值，也不能给出自然结束时的最后点。原 closure/key 计时仅覆盖它们各自的 instrumented scope，不是整个 F/J/求解时间。

以下保留这一完整已发布观察对象，含真实小文件 byte/SHA 与全部 48 个被选标量，不从其他运行补字段：

```json
{
  "step_id": "complete-fixed-fejer-immutable-point-first-20261127-run12",
  "scientific_source_commit": "a3df4eae39988724cca2cc3c38927e583c24eb2e",
  "scientific_source_sha256": "0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf",
  "pid": 3347,
  "observations": {
    "fixed-fejer-immutable-point-first/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-27 19:41:20 UTC",
      "point": "507253778ce58f9025ca9078abb81bcecd3698e2f540c6bfaeaec9c06ab34902",
      "stage": null,
      "scope_order": 2,
      "scope_angles": 1,
      "cached_angle_roots": 1228,
      "observer_scientific_calls": 0,
      "scientific_complete_inferred": false,
      "closure_logical_requests": 1769743,
      "closure_logical_returns": 1769743,
      "closure_logical_failures": 0,
      "closure_original_attempts": 848643,
      "closure_original_returns": 848643,
      "closure_original_failures": 0,
      "closure_original_angle_jet_requests": 3299853,
      "closure_original_angle_jet_returns": 3299853,
      "closure_cache_hits": 921100,
      "closure_cache_hit_angle_jets": 1609476,
      "closure_cache_misses": 635190,
      "closure_forced_original_requests": 203610,
      "closure_forced_stage_rereads": 197440,
      "closure_forced_endpoint_rereads": 6170,
      "closure_bypass_no_scope": 9843,
      "closure_bypass_caller_environment": 0,
      "closure_bypass_current_environment": 0,
      "closure_bypass_tensor_or_data_tracking": 0,
      "closure_bypass_optional_failure": 0,
      "closure_binding_failures": 0,
      "closure_key_checks": 1556290,
      "closure_point_word_checks": 12341,
      "closure_stored_values": 635190,
      "closure_optional_cache_failures": 0,
      "closure_scopes_started": 6171,
      "closure_scopes_closed": 6170,
      "closure_scopes_with_exception": 0,
      "closure_scopes_disabled_at_entry": 0,
      "closure_scope_stage_completions": 197440,
      "closure_progress_writes": 12346,
      "closure_progress_write_failures": 0,
      "closure_progress_events": 12346,
      "closure_peak_cache_entries": 130,
      "closure_peak_cache_bytes": 112320,
      "closure_immutable_point_entry_checks": 6171,
      "closure_immutable_point_key_checks": 1556290,
      "closure_immutable_point_exit_checks": 6170,
      "closure_original_closure_seconds": 4718.555816532234,
      "closure_binding_and_key_seconds": 425.37479448285956
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-immutable-point-first/actual-normal-evaluation-progress.json",
      "bytes": 3403,
      "sha256": "d1b1a68a6f94f4d222b543d4cd1b86a4117a528f0fff9f26d59d166786f3e76c",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "1c90a22ed7c883fca76c60acfcf194ce6120223efc6733865f952875ca60fca9",
  "observed_utc": "2026-11-27T19:41:22Z"
}
```

## 5. 未返报告、checkpoint 和历史的处理

本次公开证据没有返回这一科学阶段的 complete report、最终 checkpoint record、pure readout 或后续费用结果。原 runner 内是否已有 incomplete report、initial/accepted checkpoint、方向矩阵或 partial root packet，只能由真实文件进一步确定；本记录没有读取这些 raw 文件，也不将其假定为空或不存在。

因此，当前没有可由本记录提供的、已验证 `complete=True` 且同 source/model/point 的完整 13 成员 `final.npz`。不能用最后 mutable point SHA 代替完整点数组，不能把进度中的根字或输入 reference 充作 final，也不能构造一次没有发生的 accepted transition。纯 reader、同场费用及其他未返后继继续是未完成责任。

这一运行可能产生的永久地点、typed row、保护角色、发现顺序和未发布末场均没有被置空。原已知 P0/G/history 输入与其来源仍保完整记录。新固定目标的地址重解释和潜在完整有限包络责任继续依原已刊明确政策；它不把 run12 的未知实际历史伪称已逐字继承。

## 6. 本次实际操作范围

本次只读取官方公开 run/job 元数据、已存在且小于 100000 字节的索引/分卷，以及原 source/参数身份。没有取消、重跑、修改 job、缩减原科学预算、生成数值 fixture 或变更 Git refs。取消原因尚未由有界原日志证实；本记录不凭墙钟时间推定具体数值失败或约束种类。后续完整求解须使用真实可用输入和明确完整来源的新入口，其结果仍待实际自然返回。
