# 原 run10 实际终态：科学步骤取消，完整场与后继读数未自然返回

记录时间：2026-11-27 15:09:03 UTC。本条只登记实际公开 API、原完整小分卷与原队列；不重新执行科学，不把取消解释成数学失败，不把随后独立 Fejér 目标的运行当作本分支完成。

## 1. 实际终态与可确认范围

公开运行 [45972294636/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45972294636) 的 API 已返回 `status=completed`、`conclusion=cancelled`，API 的 `updated_at` 为 `2026-11-27T15:06:33Z`。实际 job `140415391810` 同样为 `completed/cancelled`；其第 5 个工作流步骤 `Execute public research and publish independent compact records` 已 `completed/cancelled`。这里的工作流步骤 5 对应整个研究控制器，控制器正在执行的科学阶段也编号 5，两个编号的职责分开记录。

运行创建与开始时间均为 `2026-11-27T09:16:11Z`，工作流声明的 350 分钟预算与该终态接近。**尚没有已读、尺寸合规的原日志或 annotation 证明具体取消原因，因此本记录不将原因写成超时、人为取消、科学异常或数值失败。** 通用 GitHub fetch 拒绝 job-detail/annotation 端点；现有 job-log 专用接口只能整读，尚未取得全日志字节数，故没有无界读取未知大小日志。此访问边界不改变实际 cancelled 终态。

最新公开索引仍是 `2026-11-27 15:04:42 UTC` 的运行中快照，明确仅阶段 1–4 完整返回。没有阶段 5 的自然退出码、完整 report 返回记录或实际最终 13 成员 checkpoint 身份；后继纯读和均值/剖面费用步骤也没有实际返回。后续字段均保持未知，不补空历史、不造成功或失败的场结论。

完整终态 API 关键原字段如下。完整 run API 文本的实际 UTF-8 身份为 `7e02da5771922fe88fbe52eadfa9e72d21b5fbb5abb58190667b22fbab3088dc` / 13356 B；下表/JSON只是明确选出的状态字段，不冒充原全文。

```json
{
  "id": 45972294636,
  "run_attempt": 1,
  "name": "Visible larger amplitude analytic-normal independent envelope continuation 20261127 10",
  "head_sha": "7d96daac44afee4c6adac7cddaecd6705fc60cb5",
  "event": "push",
  "created_at": "2026-11-27T09:16:11Z",
  "run_started_at": "2026-11-27T09:16:11Z",
  "updated_at": "2026-11-27T15:06:33Z",
  "status": "completed",
  "conclusion": "cancelled",
  "workflow_id": 432552626,
  "html_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/45972294636"
}
```

实际完整 job/step 状态响应：

```json
{
  "jobs": [
    {
      "id": 140415391810,
      "name": "Continue full analytic normal research with actual complete inputs",
      "status": "completed",
      "conclusion": "cancelled",
      "run_id": 45972294636,
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
}
```

## 2. 固定的公开证据位置

| 内容 | 仓库路径 | Git blob | UTF-8 字节 | SHA256 |
|---|---|---|---:|---|
| 末次已刊索引 | notes/2026-11-27-public-actions-45972294636-1.md | aa0cd34df366739dd42964932653d655a4063ea2 | 7962 | cb16cc9f03be8d286d130a5410277aae150063d9520fcd9211b3bc636ad96258 |
| 完整实际阶段 1–4 | notes/2026-11-27-public-actions-45972294636-1-part-001.md | e914a571f6fe2c228e6662ad2b144363c8486881 | 38575 | 0b1de8d544053aa5e67f80b144a65274c2f111825845482e68c5c278ef9f7cee |
| 原三后继完整队列 | computations/resume-20261127-followups-10.json | 9ff6a4417bf86c034b879abf9a72c84129b38b0f | 92609 | 26ed8e7b68467931cfb5198c7eac76941d3f82ebb5db8a928d5d7a79a2a74a34 |

上述路径都相对 `topics/visible-flex-larger-amplitude/`。阶段 1–4 的原记录包含各次完整命令、全部输入/输出文件记录、实际 source commit 和原紧凑返回值；其 38,575 B 原字节在本次终态核查时仍完全相同。此条没有移动、删除或把三后继对象标成已完成。

原完整科学/纯读 ready 为 `computations/run10-detached-closure-values-complete-ready.json`，87,763 B / `ab9d21b4f7f9169ccb241cce418e218ab66dda88d98749498d1b69326ef48b85`，blob `04e986cf6c3a8b734d51f14cd49672ea8d1fbb89`。完整参数/来源表为 `computations/run10-detached-closure-values-complete-parameter-and-source-provenance.json`，33,613 B / `26b5b3d389cadd652f11c5599c110fb7c5dd5d3ce37891cd95e3b24060826d27`，blob `39cf32f1701f1424d3a01d3371b60ed8a6e8e197`。

## 3. 已真正返回的四个必要步骤

四项均返回 0；其必要输入生成/源码再生成功不等于科学场成功。以下保每项实际 source commit、源码、parent 与所有实际输出文件记录，不保存任何数组或 raw 科学正文。

```json
[
  {
    "actual_stage": 1,
    "name": "warm",
    "state": "completed",
    "returncode": 0,
    "seconds": 148.002461665,
    "source_commit": "7d96daac44afee4c6adac7cddaecd6705fc60cb5",
    "source_sha256": "067b3f2e14145a6f88b2d171c555f1174f0505b45a5aaf670c3ec2610f7c286d",
    "parent_sha256": null,
    "outputs": [
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/accepted099.json.gz",
        "sha256": "b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff",
        "bytes": 2614352
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/continue0991.json.gz",
        "sha256": "63dce2f6987f18e0dd0b05b3ed97654236fb142b4887ed562d72549bb39cd3ab",
        "bytes": 2703908
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/continue0992.json.gz",
        "sha256": "b34a0e23061aaf53877629d9e7722b9166b504075a403a5378acaeeaed1e3241",
        "bytes": 2709296
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/continue0993m112.json.gz",
        "sha256": "0d597d1b1fc3f7efbef6569acae602b9d85258d7c0709c4a0163a8e238033639",
        "bytes": 3642489
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/continue0995m112.json.gz",
        "sha256": "3d35c188b1794db6204fd7de10e675ff97bec919959199ce14bc02a81d426641",
        "bytes": 3696156
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/fullclosed-hold-warm.json",
        "sha256": "1fed8f9b49202ae67c2d317c3a30d855d7a5d9f486fe034591a23fada2b08268",
        "bytes": 554141
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/fullclosed-hold-warm.npz",
        "sha256": "3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c",
        "bytes": 8767118
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/fullclosed-mode-damped-warm.json",
        "sha256": "3f6ad46f770f73bad0ca1901efd38859decfd1b15ccd403e54ff116259afe8fa",
        "bytes": 2939
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/fullclosed-mode-damped-warm.npz",
        "sha256": "79c161cc11a0743209ca3947e2b0f51f7ab7046e14ebfadf519f5d6e7259edba",
        "bytes": 8809245
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/inward-scalar-parameter-carrier.json.gz",
        "sha256": "731eb4b6303696b0a18a190e4d1efb4b7cd6043787b55c436b931c638bf1ebbb",
        "bytes": 15640
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/pulse-a5-complete-base.json.gz",
        "sha256": "aa7af21dc95861841c2d6cbbe4d5034cce671e796fe8a4346aeb8aa887d8b2c4",
        "bytes": 14227847
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/pulse-a5-fullfield-n4096-c2.json.gz",
        "sha256": "9703326c1ff976041588353ace351b216f1f774ab27501ad46ec56cf8bfff4a3",
        "bytes": 9098302
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/pulse-a5-fullfield-n4096.json.gz",
        "sha256": "2ec511cfe1a18af9378d8e08e7399b23d37a7a3519fbcce5c3527f51fd870192",
        "bytes": 9109258
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/refine0992m112.json.gz",
        "sha256": "2ee73bb9246f6d8e96532684c318383de9df12f25f7530c4113c9a0cb9a4942d",
        "bytes": 3608162
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/rebuild-closed-warm-manifest.json",
        "sha256": "411abb2b60652851f700c5499c77440bfb660270e16ed60df3dbb483c6bc6c4b",
        "bytes": 4835
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/rebuild-prefix-manifest.json",
        "sha256": "85ff76b5618601b2493d3e3ea18b7ed0249f0f40c07348a97e415908029f79df",
        "bytes": 7762
      }
    ]
  },
  {
    "actual_stage": 2,
    "name": "followup:independent-axisymmetric-R690-reference-prepare-v2-first-20261127-10",
    "state": "completed",
    "returncode": 0,
    "seconds": 308.62119226799996,
    "source_commit": "e9f49a8951b3ad27a7ecf4acb6e0d5017448015d",
    "source_sha256": "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3",
    "parent_sha256": "3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c",
    "outputs": [
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/report.json",
        "sha256": "35fdae489de9a7ee205b4f03f805b30107cec382abbdd242ece43f87d857d286",
        "bytes": 29809
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/reference.npz",
        "sha256": "512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b",
        "bytes": 866207
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/observations.npz",
        "sha256": "71f0048e2c6c973625fd110c6980c24242d2cf67b7dd7da5dd9e889fde26a22d",
        "bytes": 227202
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/locations.json",
        "sha256": "4ae7125b692ed565b2ecd9df5901c3de0ba52c6569869953318b4d029dc0e267",
        "bytes": 106450
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/supplied-location-provenance.json",
        "sha256": "907f6a60c9572432e906908c9a42d92c29ace96dc122b92dd8fe251c401f1788",
        "bytes": 223619
      }
    ]
  },
  {
    "actual_stage": 3,
    "name": "followup:freeze-actual-run10-public-reference-and-restore-whole-run05-carrier-20261127",
    "state": "completed",
    "returncode": 0,
    "seconds": 338.91556337600014,
    "source_commit": "2ac24f7178faae6c2901e97b1f7ebfa3ec8e5d0e",
    "source_sha256": "fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a",
    "parent_sha256": "512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b",
    "outputs": [
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/run10-actual-public-reference-run05-carrier/report.json",
        "sha256": "c5fc7c39188acd62c1dca920c56cbe59a18ca5a29fa945b828f967c38c430c7e",
        "bytes": 769363
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/run10-actual-public-reference-run05-carrier/run05-observations-restored.npz",
        "sha256": "dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0",
        "bytes": 227202
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/run10-actual-public-reference-run05-carrier/independent-fixed-target-definition.json",
        "sha256": "b24080447828d8ffb49ae146dd5672d34bf6f5cec512054633b6f849c2bdabfb",
        "bytes": 97335
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/run10-actual-public-reference-run05-carrier/material-envelope-carrier-binding.json",
        "sha256": "4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf",
        "bytes": 430908
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/run10-actual-public-reference-run05-carrier/actual-public-warm-immutable.md",
        "sha256": "b23954c94ac4f69969dae9768d9ebdc1b77f5a65b82377b48d1cd63c84330583",
        "bytes": 22533
      },
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/run10-actual-public-reference-run05-carrier/actual-public-reference-immutable.md",
        "sha256": "b23954c94ac4f69969dae9768d9ebdc1b77f5a65b82377b48d1cd63c84330583",
        "bytes": 22533
      }
    ]
  },
  {
    "actual_stage": 4,
    "name": "followup:replay-complete-run10-public-input-sources-20261127",
    "state": "completed",
    "returncode": 0,
    "seconds": 5.847329209000009,
    "source_commit": "e17966cfcce07326d2fad6a25d9748f34ae39164",
    "source_sha256": "52fc53b272d734aaa1a02ef7e57f2545e4e8ec8a622495f15e1ba113b25b6235",
    "parent_sha256": "512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b",
    "outputs": [
      {
        "path": "/home/runner/work/_temp/visible-larger-research-45972294636-1/research/run10-public-input-source-stage/report.json",
        "sha256": "586b69846afacd8bc40e1f549c1ca80b426fbb703bad994d3f44ca11b8c62147",
        "bytes": 1491
      }
    ]
  }
]
```

实际参考是 `512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b`，完整模型 `081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5`，实际 carrier `71f0048e2c6c973625fd110c6980c24242d2cf67b7dd7da5dd9e889fde26a22d`；完整 target canonical `e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049` 与 whole target 文件 SHA `b24080447828d8ffb49ae146dd5672d34bf6f5cec512054633b6f849c2bdabfb` 不混用。实际全 binding 文件为 `4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf`。

当前参考 scalar 的实际完整积分叶为 **2218**，`scalar_tolerance_reached=false`；旧 run05 carrier 再生中的 **2397** 叶属于其明确独立的历史恢复职责。这两个叶数不替换，也没有把未达精度目标写成已认证。M160/J923/N2048/P7377 与全标量参数 `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa` 仍按原记录保留。

## 4. 真正开始但没有自然返回的科学步骤

实际子进程是在源码提交 `9dce039498a177d870ccc87970df7bd05e419a98` 下启动，launcher 全 SHA `22069c4bb56a4ca4820b3f608cf720a36b036534e6b1e90b5f467f8eed21e604`，PID `4475`。完整 scientific driver 是 `fullclosed_run10_detached_closure_so3_qp.py` / `c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1`，normal 为 `6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4`；后继完整 pure reader 为 `2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e`。这些源和原 75 个角色继续按已刊全参数/来源表定位。

末次实际有界进度写于 `2026-11-27 15:04:38 UTC`，观察于 `2026-11-27T15:04:41Z`。完整小进度身份与全部原 43 个标量如下；它是运行中的观察，既不代表已接受方向，也不代表最终字段/geometry、连续证明或精化成功。

```json
{
  "step_id": "complete-run10-detached-closure-values-first-20261127",
  "scientific_source_commit": "9dce039498a177d870ccc87970df7bd05e419a98",
  "scientific_source_sha256": "22069c4bb56a4ca4820b3f608cf720a36b036534e6b1e90b5f467f8eed21e604",
  "pid": 4475,
  "observations": {
    "run10-detached-closure-values-first/actual-normal-evaluation-progress.json": {
      "phase": "normal_chain_enter",
      "at": "2026-11-27 15:04:38 UTC",
      "point": "a45bc0249e792ac0f3c574f41ef6787989b2a271abc39e28548c29f4ccf690f9",
      "stage": null,
      "scope_order": 2,
      "scope_angles": 8,
      "cached_angle_roots": 513,
      "observer_scientific_calls": 0,
      "scientific_complete_inferred": false,
      "closure_logical_requests": 1861924,
      "closure_logical_returns": 1861924,
      "closure_logical_failures": 0,
      "closure_original_attempts": 895509,
      "closure_original_returns": 895509,
      "closure_original_failures": 0,
      "closure_original_angle_jet_requests": 3572563,
      "closure_original_angle_jet_returns": 3572563,
      "closure_cache_hits": 966415,
      "closure_cache_hit_angle_jets": 1726023,
      "closure_cache_misses": 672110,
      "closure_forced_original_requests": 214005,
      "closure_forced_stage_rereads": 207520,
      "closure_forced_endpoint_rereads": 6485,
      "closure_bypass_no_scope": 9394,
      "closure_bypass_caller_environment": 0,
      "closure_bypass_current_environment": 0,
      "closure_bypass_tensor_or_data_tracking": 0,
      "closure_bypass_optional_failure": 0,
      "closure_binding_failures": 0,
      "closure_key_checks": 1638525,
      "closure_point_word_checks": 1638525,
      "closure_stored_values": 672110,
      "closure_optional_cache_failures": 0,
      "closure_scopes_started": 6486,
      "closure_scopes_closed": 6485,
      "closure_scopes_with_exception": 0,
      "closure_scopes_disabled_at_entry": 0,
      "closure_scope_stage_completions": 207520,
      "closure_progress_writes": 12976,
      "closure_progress_write_failures": 0,
      "closure_progress_events": 12976,
      "closure_peak_cache_entries": 130,
      "closure_peak_cache_bytes": 112320
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "run10-detached-closure-values-first/actual-normal-evaluation-progress.json",
      "bytes": 3065,
      "sha256": "51b224a8f0f1e31369b1f7d56fa23ebb11f7ff13af52569dd91c1dc893d4857d",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "8403a62ae8a22fbd21fa3e15e913a2ee6036e045d64ac6567183dbd3f74bd724",
  "observed_utc": "2026-11-27T15:04:41Z"
}
```

由此只能确认当时同一 child 的完整 closure 请求已有 1,861,924 次实际返回、原积分 895,509 次返回、命中 966,415 次、当时记录的 closure failures 为 0；最后 point 是 `a45bc0249e792ac0f3c574f41ef6787989b2a271abc39e28548c29f4ccf690f9`。**这些计数不排除之后异常，也不证明该点已接受或最终完成；没有完整 report 时不能据它恢复最终 typed 列表、最终根或控制词。**

## 5. 原完整参数及未返后继

原三完整队列对象的 149/7/32 个参数全部如下原样保留；373/357/48 个原 summary selectors 仍在上表固定 blob 的完整队列中，未裁剪。第一项确已启动，第二/三项只见准入，没有实际运行返回证据。下列 `actual_return_seen=false` 表达“尚无已刊完整返回”，不擅断言 runner 从未内部开始后继。

```json
[
  {
    "id": "complete-run10-detached-closure-values-first-20261127",
    "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_run10_detached_closure_actions.py",
    "parent_bundle": "axisymmetric-R690-reference-v2-first/reference.npz",
    "args": [
      "--repo",
      "{repo}",
      "--reference-bundle",
      "{work}/axisymmetric-R690-reference-v2-first/reference.npz",
      "--preparation-report",
      "{work}/axisymmetric-R690-reference-v2-first/report.json",
      "--carrier",
      "{work}/axisymmetric-R690-reference-v2-first/observations.npz",
      "--node-report",
      "{work}/fullclosed_solver/data/fullclosed-hold-warm.json",
      "--scalar-input",
      "{work}/fullclosed_solver/data/pulse-a5-complete-base.json.gz",
      "--angles",
      "2048",
      "--stage-block",
      "64",
      "--angle-block",
      "8",
      "--integration-order",
      "8",
      "--norm-kind",
      "jet-sum",
      "--radial-norm-length",
      ".05",
      "--angular-transition",
      "24",
      "--torch-threads",
      "4",
      "--damping",
      ".01",
      "--directions",
      "1",
      "--maxiter",
      "16",
      "--restoration-directions",
      "4",
      "--restoration-damping",
      ".01",
      "--restoration-maxiter",
      "64",
      "--line-trials",
      "15",
      "--active-rows",
      "192",
      "--qp-atol",
      "0",
      "--qp-rtol",
      "1e-6",
      "--reach-ratio",
      ".03",
      "--reach-safety-factor",
      ".992",
      "--active-band",
      ".025",
      "--marked-diameter-budget",
      "4.2",
      "--witness-lower-budget",
      ".9",
      "--amplitude-height-floor",
      "1.01",
      "--spectral-p",
      "4",
      "--spectral-epsilon",
      ".001",
      "--spectral-scale",
      ".05",
      "--legacy-fraction",
      ".5",
      "--target",
      "1e-9",
      "--outdir",
      "{work}/run10-detached-closure-values-first",
      "--panels",
      "128",
      "--endpoint-bubble-1-left",
      "1/32",
      "--endpoint-bubble-1-middle",
      "1/4",
      "--endpoint-bubble-1-right",
      "15/32",
      "--endpoint-bubble-2-left",
      "17/32",
      "--endpoint-bubble-2-middle",
      "3/4",
      "--endpoint-bubble-2-right",
      "31/32",
      "--endpoint-root-tolerance",
      "2e-12",
      "--endpoint-root-iterations",
      "24",
      "--endpoint-root-backtracks",
      "18",
      "--endpoint-root-armijo",
      "1e-4",
      "--moment-definition-sha256",
      "05dc5ed735db9860ae745eeb4caecde142111ff13f40b33bd8e29701039b968e",
      "--moment-input",
      "{repo}/topics/visible-flex-larger-amplitude/computations/frozen-zero-moment-Q-actual16-parameters.json",
      "--moment-input-sha256",
      "df11d8a4b36eb9ce113b5961863191c9b58cb2473af9c48e1714026041a42e2c",
      "--endpoint-control-radius",
      "2",
      "--gamma-left",
      "1/16",
      "--gamma-middle",
      "1/8",
      "--gamma-right",
      "3/16",
      "--moment-input-binding",
      "supported-smooth-triangle-reference",
      "--normal-stages",
      "32",
      "--seed-boundary-total-length",
      "1/16",
      "--seed-profile-delta",
      "1/128",
      "--seed-radial-quadrature-order",
      "8",
      "--seed-profile-quadrature-order",
      "16",
      "--seed-mean-maxiter",
      "128",
      "--seed-mean-tolerance",
      "2e-12",
      "--seed-mean-backtracks",
      "24",
      "--seed-mean-armijo",
      "1e-4",
      "--seed-scalar-iterations",
      "64",
      "--manifest",
      "{work}/axisymmetric-R690-reference-v2-first/locations.json",
      "--material-envelope-binding",
      "{work}/run10-actual-public-reference-run05-carrier/material-envelope-carrier-binding.json",
      "--envelope-near-active-rows",
      "32",
      "--independent-envelope-branch",
      "--pending-parallel-envelope-run",
      "45909290354/1",
      "--pending-parallel-envelope-source",
      "45909290354/1=cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5",
      "--pending-parallel-envelope-run",
      "45929088658/1",
      "--pending-parallel-envelope-source",
      "45929088658/1=95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9",
      "--pending-parallel-envelope-run",
      "45943410994/1",
      "--pending-parallel-envelope-source",
      "45943410994/1=ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"
    ],
    "outputs": [
      "run10-detached-closure-values-first/report.json",
      "run10-detached-closure-values-first-command.json"
    ],
    "summary_scalar_count": 373,
    "actual_return_seen": false
  },
  {
    "id": "actual-run10-detached-closure-values-first-20261127",
    "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_run10_detached_closure_so3_report.py",
    "parent_bundle": "axisymmetric-R690-reference-v2-first/reference.npz",
    "args": [
      "--repo",
      "{repo}",
      "--report",
      "{work}/run10-detached-closure-values-first/report.json",
      "--output",
      "{work}/postprocess/run10-detached-closure-values-first-readout.json",
      "--verify-final-bundle"
    ],
    "outputs": [
      "postprocess/run10-detached-closure-values-first-readout.json"
    ],
    "summary_scalar_count": 357,
    "actual_return_seen": false
  },
  {
    "id": "all-actual-run10-reference-seed-batches-mean-profile-fees-first-20261127",
    "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/run10_all_recorded_reference_seed_fees.py",
    "parent_bundle": "axisymmetric-R690-reference-v2-first/reference.npz",
    "args": [
      "--repo",
      "{repo}",
      "--report",
      "{work}/run10-detached-closure-values-first/report.json",
      "--reference-bundle",
      "{work}/axisymmetric-R690-reference-v2-first/reference.npz",
      "--carrier",
      "{work}/axisymmetric-R690-reference-v2-first/observations.npz",
      "--node-report",
      "{work}/fullclosed_solver/data/fullclosed-hold-warm.json",
      "--scalar-input",
      "{work}/fullclosed_solver/data/pulse-a5-complete-base.json.gz",
      "--preparation-report",
      "{work}/axisymmetric-R690-reference-v2-first/report.json",
      "--outdir",
      "{work}/run10-all-recorded-reference-seed-fees",
      "--execution-mode",
      "complete-recorded-batches",
      "--seconds",
      "600",
      "--per-batch-seconds",
      "60",
      "--panels",
      "128",
      "--precision-bits",
      "160",
      "--width-goal",
      "1/100000000",
      "--taylor-order",
      "48",
      "--profile-series-order",
      "48"
    ],
    "outputs": [
      "run10-all-recorded-reference-seed-fees/report.json"
    ],
    "summary_scalar_count": 48,
    "actual_return_seen": false
  }
]
```

## 6. 保留的责任与后续边界

- 原科学 5 没有自然完整返回；其初始/最终指标、接受方向数、最终 13 成员文件、完整末点根及所有新增 typed/protected/发现顺序保持未知。
- 原 pure 与 all-batch mean/profile 未返回；不能把准备好的源或进度计数改写为费用已经支付。
- 原 run07/08/09 等完整未返来源责任及此 run10 自身未知历史均保留。新 Fejér 目标显式不同，不能把 run12 的新图、新 mesh 或其运行进度当作原 run10 同题续接；旧物理值/证书不迁移。
- 本条不触发旧输入重跑，不重写任何 queue/source。当前 run12 独立全问题继续，M320/N4096/J1845 的准备也必须保持各自真目标、真输入和模式边界。
- 原 raw 文件始终只留 runner；没有为跨 runner 把旧 scientific 输出拆成“参数”、转存 Git、Release 或 artifact。

本终态只结束了该工作流的执行窗口，没有完成原研究目标，也没有提供不可解结论。
