# 20：同一完整 bhalf 输入、较小恢复阻尼的独立续求

会话 Astra-larger-e4e2a2bf-20261126（AI-assisted）。准备时间 2026-11-27 22:54:51 UTC。本提交同时提供完整源码绑定、全部原参数和公开 Actions 启动；真实 run、job、实际源提交和新输入/场身份须由实际返回另记，不能从计划倒填。

## 当前依据与唯一科学参数变化

[完整来源分析及严格比较](2026-11-27-full-restoration-scale-and-mu001-branch.md)已从实际10fa driver、fb4e QP和全坐标源给出：只要完整有限几何违反仍正，程序处于恢复阶段，QP目标没有Phi项。原相同线性可行集的精确QP最优解在降低mu时，其最优非负公共松弛量不增；64步截断、非线性全几何、root/alpha和实际收敛没有因此得到保证。

本独立分支保持19的b/S=1/2、delta=1/32和原同一g，唯一科学标量把argv37 `.01` 改为 `.001`（`--restoration-damping`）。metric damping仍 `.01`，完整坐标范数、1/4个metric/restoration方向、16/64内迭代、15全线搜索、32normal stages以及全部其他域/参数/预算不变。argv71只改独立输出namespace `fixed-fejer-meridian-batched-bhalf-mu001-first`。运行中的19不修改。

19实际bhalf初六族reach=.9684249942095058、distplus=.005863061771032241仍正，Phi3825.0583894874153、Gram.6460503011117507；相较18初reach/distplus/Phi下降而最大Gram误差升高。完整数值与界线见[19实录](2026-11-27-run19-complete-bhalf-launch-and-continuation.md)。这里仅据已经实际返回的有限结果选择独立方向，不继承它的场、接受点、参考报告身份或准确证书。

## 全部交付与原字身份

[完整参数包](../computations/fixed-fejer-bhalf-mu001-complete-parameter-delivery.json) 50679 B / SHA256 `ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4` 含全137角色、18原运行源、原120对、三份完整19父文件、所有旧metadata/失败/typed未知和精确delta。当前10fa/8027/f600及其他原运行体没有代码变化。

| 角色 | 完整文件字节 | SHA256 |
|---|---:|---|
| science | 97019 | `89b437a4986b3172d281b4928353072d15a15f2cebbb7a1fd8d973880d5166ca` |
| pure | 86221 | `f627447f7887bdc9d7f257b4d0772173556683501cd5fa9f1e39890ec7ac7f64` |
| display | 32429 | `1fef7603002bdfbac58623b1d7c8b1cd0492d050f42c22acfd1ce11c3597278e` |
| parameter_constructor | 15064 | `acd5d19439d9a6b00216bb6bfee2fab46087356a3580b97b946961fb6e83daa9` |
| source_analysis_and_choice | 15526 | `42ef2c9012b6c76439f09d0255392eabda6a27d240737e22e1bd74e3a914e313` |
| 完整参数总表 | 50679 | `ce445da032ffedff5e03e40b89e09096cba3e7e147f256968774a6c6e72d21b4` |

完整文件路径与Git blob在上述参数包与[启动总表](../computations/fixed-fejer-bhalf-mu001-complete-launch-delivery.json)。science157/pure7词、458/445 formal、48live完整保，不裁成“运行最小集”。旧408/395formal及原18+30 live来历也完整保。

## 真正执行顺序

初始队列 73243 B / SHA256 `9d82aeee09115e026edb61f997ccde501004f05c602e3fdf4811373c4c7aff23` 包含两项原必要完整输入构造和整个科学step。输入1保持父对象所有字，输入2仅id的run19变run20、26参数及全输出/摘要不变；新runner独立重建参考、原923节点、全7377观察、2218标量叶。原input构造的accuracy_reached若false仍真实保，构造成功不冒科学成功。

两完整science/pure队列带包装共117276 B pretty / 104048 B compact，均超控制器95000上限。两step本身数组103956 B同样超限。因此先整运行science；真正自然返回后保存完整旧对象和全部真实输出身份，再退只已返回的对象、接入完整pure7词/445selectors。没有增加数学或审批门，也没有缩减任何原参数。完整normal/geometry/closed、R716和全mesh后续保持未付责任，在各自完整真实材料具备后接着执行。

## 控制与规则

控制器 19984 B / `1d790c7c805c26762bd982e1cfcd00f3c38d774e272468529af823966557d629` 只把原19四处H槽标签改成20；完整执行逻辑、真实pull/rebase及双README差异检查不变。workflow 2219 B / `7ee7db6e9b1c6d763439e0967ae974661c4facb8ca90c4a67eb945d4bb6aadbc` 只改名称、request/controller路径和独立concurrency标签，原partial checkout、所有原依赖、permissions及350分钟预算保持。

请求 44226 B / `965c1cbf18be6f9314ef6a15019e498ae1a71dc5a00489c90a0e1911b356c39a` 完整保19原请求的历史metadata并明确当前真实10fa/8027/f600与bhalf参数；旧19请求中沿用的bquarter描述只留历史，不冒当前参数。controller20000秒是后续接纳预算，不将活动child超时杀掉；job结束仍非研究完成。17–19现有队列和源保持，16官方cancelled及末科学未知另保[终态](2026-11-27-run16-official-terminal-and-unreturned-observed-solve.md)。

只在授权公开Actions做科学；全部科学raw/逐胞/mesh/checkpoint只runner，Git保全源、全参数、证明与实际小记录。根终端仍不可用，cloud freshHEAD核对并普通非force推送不冒真pull；控制器每次实际pull即比较双README，只读变化并记已读commit。启动前双README已读基准 `1e642976aec7c6e620da2e2bab3112e6ee30ee56`，实际发布时fresh检查；当前hash见request。

新实际run/job/model/point/科学report/accepted/final/所有fee和mesh均未知。该完整分支不是完成结论；继续到README全标准。


## 22:56:26 UTC：官方运行已真实启动

上述完整launch提交 `85cd235221ace28158625a7ced52a24551b509eb` 实际触发 **run46079535427/1**，官方created_at/run_started_at均为 **2026-11-27T22:55:41Z**。Job **140775034500** 当前in_progress；checkout、Python和全部原依赖安装已success，完整公开研究步骤5正in_progress。此时未读到任何完整新input或科学自然返回；提交HEAD只标启动，不倒填各step实际source或未来field。

根还在精确发布父 `52ec703c1a995c63c8af83175045c5de0c43e0f6` 读完整workflows Git树 `82a183256a747fc2758adaeb9a7304609f72864b`（1266项，truncated=false），该父无parallel20路径。先前contents接口的1000项不被当作完整缺席证据；完整Git树身份才确定此次新增路径。

```json
{
  "observed_utc": "2026-11-27 22:56:26 UTC",
  "official_discovery_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs?head_sha=85cd235221ace28158625a7ced52a24551b509eb",
  "official_discovery_complete_response_bytes": 13375,
  "official_discovery_complete_response_sha256": "628611b15556cd013bfb8301ed52776b20e47f778ec8e0a8f5aca0d4c615ae38",
  "selected_official_run_fields": {
    "id": 46079535427,
    "name": "Visible larger amplitude complete bhalf restoration damping 20261127 20",
    "head_branch": "main",
    "head_sha": "85cd235221ace28158625a7ced52a24551b509eb",
    "path": ".github/workflows/visible-larger-20261127-parallel20.yml",
    "run_number": 1,
    "event": "push",
    "status": "in_progress",
    "conclusion": null,
    "workflow_id": 433228578,
    "created_at": "2026-11-27T22:55:41Z",
    "updated_at": "2026-11-27T22:55:44Z",
    "run_started_at": "2026-11-27T22:55:41Z",
    "run_attempt": 1,
    "html_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46079535427",
    "jobs_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46079535427/jobs"
  },
  "complete_bounded_official_jobs": {
    "jobs": [
      {
        "id": 140775034500,
        "name": "Construct the same fixed target and solve the complete bhalf smaller damping",
        "status": "in_progress",
        "conclusion": null,
        "run_id": 46079535427,
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
            "status": "in_progress",
            "conclusion": null,
            "number": 5
          },
          {
            "name": "Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
            "status": "pending",
            "conclusion": null,
            "number": 9
          },
          {
            "name": "Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
            "status": "pending",
            "conclusion": null,
            "number": 10
          }
        ]
      }
    ]
  },
  "initial_commit_is_not_each_future_step_source_commit": true,
  "new_input_reports_observed": false,
  "scientific_natural_return_observed": false,
  "complete_model_or_point_known": false,
  "goal_completed": false
}
```


## 22:56:53 UTC 第一完整输入实际返回0

根在固定提交 `3b34f6064ca3030c4521f779844b64d05690c937` 读取实际第1卷 5756 B / SHA256 `dd6a0a0cce998492ce923197f60ea4afccd1202767a4e900cfb15c877b8359d5`（Git blob b4151ee00a7de76ca65b2591b9b551e607f07ea5）。第一个必要输入构造真正completed/returncode0，用时5.931292771999992秒，实际source commit `ebdf38b0f0754f3a4760d1c52f638457b7b15bbd`，原89cc完整maker。不是将launch HEAD当该step源码。

完整输入报告65332 B / `24fd29704868e7c55763d74c63b8e04919f6481951600122934e22ca5ab0c368`；fixed-reference-input.npz4334 B / `b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98`；完整nodes144306 B / `1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5`；完整scalar40488 B / `2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189`。后三项与19相同是本次完整独立输入构造的实际字节事实，不从旧runner搬回数据。没有下载这些大raw/二进制，全部身份来自完整原小记录。

所有原6参数、实际命令/输出、输入/源、空cleanup元数据、summary_errors和missing_outputs完整保如下。第二个完整参考输入及新完整科学report/model/point此时仍未读到自然返回；maker0不支付后续科学或几何结论。

```json
{
  "name": "followup:prepare-complete-fixed-fejer-r690-inputs-20261127",
  "state": "completed",
  "returncode": 0,
  "seconds": 5.931292771999992,
  "scope": "Necessary complete deterministic new mathematical input. Restore the exact accepted099 scalar-parameter source; extract the whole e640 projection; construct the fixed seven-mode RN-even Fejer chart, all 923 exact affine nodes and complete FullHold node/radius error ledger. No warm/BVP/pulse field, old core, old final, F/J/normal root or geometric certificate is used. This is a new fixed target; original branches and old literal-address provenance are retained explicitly.",
  "metrics": {
    "fixed-fejer-r690-inputs/report.json": {
      "schema": "complete-fixed-fejer-r690-input-preparation-v1",
      "source": "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60",
      "status": "complete",
      "complete": true,
      "seconds": 1.0283899000000076,
      "definition": "5e1c65204a45ae97b64d845f7fe7277ffedd57c758939cc82df068b2f104ce4a",
      "target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "actual_run": "46079535427",
      "actual_attempt": "1",
      "actual_source_commit": "ebdf38b0f0754f3a4760d1c52f638457b7b15bbd",
      "all_input_source_output_rechecked": true,
      "physicalF": 0,
      "J_evaluations": 0,
      "normal_roots": 0
    }
  },
  "outputs": [
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-r690-inputs/report.json",
      "sha256": "24fd29704868e7c55763d74c63b8e04919f6481951600122934e22ca5ab0c368",
      "bytes": 65332
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz",
      "sha256": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
      "bytes": 4334
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
      "sha256": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
      "bytes": 144306
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json",
      "sha256": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
      "bytes": 40488
    }
  ],
  "input_files": [
    {
      "role": "source",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py",
      "commit": "ebdf38b0f0754f3a4760d1c52f638457b7b15bbd",
      "sha256": "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60"
    },
    {
      "role": "followup_queue",
      "path": "topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-20.json",
      "path_commit": "85cd235221ace28158625a7ced52a24551b509eb",
      "checkout_commit": "ebdf38b0f0754f3a4760d1c52f638457b7b15bbd",
      "sha256": "9d82aeee09115e026edb61f997ccde501004f05c602e3fdf4811373c4c7aff23"
    }
  ],
  "source_commit": "ebdf38b0f0754f3a4760d1c52f638457b7b15bbd",
  "source_sha256": "89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60",
  "command": [
    "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
    "-u",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/followup-sources/0001-167d7c1a5813-ebdf38b0f075/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_r690_reference_inputs.py",
    "--repo",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/followup-sources/0001-167d7c1a5813-ebdf38b0f075",
    "--outdir",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-r690-inputs",
    "--panels",
    "128"
  ],
  "cleanup_generated": {
    "deleted": {
      "record_count": 0,
      "recorded_bytes": 0,
      "records_with_bytes": 0,
      "listed_file_count": 0,
      "records_with_file_lists": 0,
      "canonical_metadata_bytes": 2,
      "canonical_metadata_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "canonicalization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
      "detail_scope": "Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"
    },
    "skipped": {
      "record_count": 0,
      "recorded_bytes": 0,
      "records_with_bytes": 0,
      "listed_file_count": 0,
      "records_with_file_lists": 0,
      "canonical_metadata_bytes": 2,
      "canonical_metadata_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "canonicalization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
      "detail_scope": "Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"
    },
    "scope": "Only explicit patterns, newly generated regular caches and an already returned child; never parent/input/output files"
  },
  "step_id": "prepare-complete-fixed-fejer-r690-inputs-20261127",
  "summary_errors": [],
  "missing_outputs": []
}
```

## 2026-11-27 23:16 UTC — 第二输入真实返回及初始完整有限几何

从固定提交 `eedf4ae13a83539afe061260e480dbdce51213b0` 的完整小索引与第1卷读取，先读 bytes/blob，再取全部正文；没有取 runner 科学数组或完整逐胞报告。原两份小文件身份完整如下。索引记录时间为 23:14:33 UTC，独立 active observation 在 23:14:32Z。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46079535427-1.md",
    "bytes": 52334,
    "sha256": "5f59bc747e4f5858b3ef10cde97f7b94d6470a227eb0b5ab218d0c3f2bfc940f",
    "sha": "4b1617e84fece2a0825be0b891101f66cfd63984",
    "fixed_commit": "eedf4ae13a83539afe061260e480dbdce51213b0",
    "git_tree_size": 52334,
    "git_tree_blob": "4b1617e84fece2a0825be0b891101f66cfd63984"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46079535427-1-part-001.md",
    "bytes": 16607,
    "sha256": "de5bde8ed0f0b2ca5d38f5b03cac87e53c36f782cb057e283e2deda55a93f2ff",
    "sha": "c563ae407a5f39797198184e13a70804188772ff",
    "fixed_commit": "eedf4ae13a83539afe061260e480dbdce51213b0",
    "git_tree_size": 16607,
    "git_tree_blob": "c563ae407a5f39797198184e13a70804188772ff"
  }
]
```

第二必要参考输入真实退出0，控制器计时446.51950942400003秒，原报告内部443.237231892秒；实际源码提交 `25e8c73df95535c5c2cac4f839edd9f8beb0cd53`、源码e7175f59全SHA见下。报告84,966 B / `7d212377a44e7f0e47d5bdc198f682c5fc7cfd09eb97976cfd546f7d2271a6b6`。所有七个输出身份、完整原命令、input和cleanup均保以下原对象。参考程序的 complete=true 不改其 accuracy_reached=false；全尾未丢、2218叶为预先指定，仍有精化责任。

```json
{
  "name": "followup:prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run20",
  "state": "completed",
  "returncode": 0,
  "seconds": 446.51950942400003,
  "scope": "Necessary complete reference construction for the one predeclared Fejer RN-even64 chart and complete original R690 scalar. Consume all real fixed-input products from the independent formula maker, preserve all 923 exact nodes, 7377 positive observations and every eight-Gauss/reference scalar jet. The scalar integer table uses a predeclared 2218-leaf rule; H is the original complete normalized-c Gauss seed and remains free. Reinterpret the full ordered eleven-payload historical literals explicitly on the new target and mesh, without claiming same physical s/point or inheriting unknown old history, field values, certificates, or completion. This is necessary input construction, not a scientific fixture or proof.",
  "metrics": {
    "fixed-fejer-reference/report.json": {
      "schema": "R690-fixed-fejer-axisymmetric-SO3-preparation-v1",
      "source": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
      "source_commit": "25e8c73df95535c5c2cac4f839edd9f8beb0cd53",
      "complete": true,
      "seconds": 443.237231892,
      "reference_model": "ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac",
      "fixed_scalar": "d492e4ad97245a8474f1a73a8787aac2fc5691b1f928d0b8ea72224cabd55160",
      "scalar_parameters": "e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa",
      "mathematical_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "full_target": "50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319",
      "fixed_recipe": "5e1c65204a45ae97b64d845f7fe7277ffedd57c758939cc82df068b2f104ce4a",
      "model_chart": "af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103",
      "model_mesh": "ca4b5c626e0e5cf1687c40c25a68a76c4e8fbde391bd8c853399400c784dddfc",
      "core0": "0x1.c000000000000p-2",
      "core1": "-0x1.3333333333333p-4",
      "core2": "0x1.b6db6db6db6dbp-6",
      "M": 160,
      "J": 923,
      "P": 7377,
      "N": 2048,
      "height": 1.947054437068418,
      "reference": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
      "carrier": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
      "nodes": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
      "scalar": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
      "fixed_input": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
      "input_preparation": "24fd29704868e7c55763d74c63b8e04919f6481951600122934e22ca5ab0c368",
      "locations": "96c14cdefdcd23fa33978209fdf11160d232dcdd6d8363d73ff7fe12bc868402",
      "location_provenance": "6ba4cbc5d70c77a418a6d298eb49408c3b5c252eb5b694c5f515537e78135642",
      "target_file": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
      "leaf_target": 2218,
      "actual_leaves": 2218,
      "accuracy_reached": false,
      "integral_width_exact": "20705780131163723599438290019541571913013106551525357578680931811765776678181/14411518807585587200000000000000000000000000000000000000000000000000000000000000000000000",
      "whole_tail": true,
      "unresolved_tail_dropped": false,
      "clock_selects_leaves": false,
      "old_warm_not_required": true,
      "old_surface_used": false,
      "old_directions_replayed": false,
      "old_certificates_inherited": false,
      "physical_field_read": false,
      "new_field_still_required": true,
      "run": "46079535427",
      "attempt": "1"
    },
    "fixed-fejer-reference/material-envelope-carrier-binding.json": {
      "schema": "complete-fixed-fejer-actual-reference-binding-v1",
      "source": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
      "source_commit": "25e8c73df95535c5c2cac4f839edd9f8beb0cd53",
      "run": "46079535427",
      "attempt": "1",
      "mathematical_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "full_reference_definition": "50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319",
      "reference": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
      "preparation": "7d212377a44e7f0e47d5bdc198f682c5fc7cfd09eb97976cfd546f7d2271a6b6",
      "carrier": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
      "fixed_input": "b9e12a03ba2b06c634478288853f0711f3349f8589654d14e11c44cd7577dc98",
      "nodes": "1e71a3851ccfc1449a4f20a90dcfb120600594360051bcd810fdf73b1efb73c5",
      "scalar": "2eb44f9977373b2d4fc36009e884b71d7834f85c1cd996c03b91b7586ea56189",
      "target_file": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
      "history": "6ba4cbc5d70c77a418a6d298eb49408c3b5c252eb5b694c5f515537e78135642",
      "all_six_actual": true,
      "old_values_or_unknown_history_inherited": false
    }
  },
  "outputs": [
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-reference/report.json",
      "sha256": "7d212377a44e7f0e47d5bdc198f682c5fc7cfd09eb97976cfd546f7d2271a6b6",
      "bytes": 84966
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-reference/reference.npz",
      "sha256": "212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb",
      "bytes": 894879
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-reference/observations.npz",
      "sha256": "84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e",
      "bytes": 205842
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-reference/locations.json",
      "sha256": "96c14cdefdcd23fa33978209fdf11160d232dcdd6d8363d73ff7fe12bc868402",
      "bytes": 106771
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-reference/supplied-location-provenance.json",
      "sha256": "6ba4cbc5d70c77a418a6d298eb49408c3b5c252eb5b694c5f515537e78135642",
      "bytes": 223955
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-reference/fixed-target-definition.json",
      "sha256": "777a69e77b34a8fda152442ca7e326a48c91050edaae69ade0355f5c8b8628df",
      "bytes": 30919
    },
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-reference/material-envelope-carrier-binding.json",
      "sha256": "b598a188b419f895df6ac6a82814a540cc35214b59d82946d5288239cb2525af",
      "bytes": 35712
    }
  ],
  "input_files": [
    {
      "role": "source",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
      "commit": "25e8c73df95535c5c2cac4f839edd9f8beb0cd53",
      "sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb"
    },
    {
      "role": "followup_queue",
      "path": "topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-20.json",
      "path_commit": "85cd235221ace28158625a7ced52a24551b509eb",
      "checkout_commit": "ebdf38b0f0754f3a4760d1c52f638457b7b15bbd",
      "sha256": "9d82aeee09115e026edb61f997ccde501004f05c602e3fdf4811373c4c7aff23"
    }
  ],
  "source_commit": "25e8c73df95535c5c2cac4f839edd9f8beb0cd53",
  "source_sha256": "e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb",
  "command": [
    "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
    "-u",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/followup-sources/0002-55e32d8570e2-25e8c73df955/topics/visible-flex-larger-amplitude/scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py",
    "--repo",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/followup-sources/0002-55e32d8570e2-25e8c73df955",
    "--fixed-input",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-r690-inputs/fixed-reference-input.npz",
    "--fixed-input-report",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-r690-inputs/report.json",
    "--node-report",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-r690-inputs/fixed-affine-nodes.json",
    "--scalar-input",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-r690-inputs/fixed-scalar-input.json",
    "--manifest",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/followup-sources/0002-55e32d8570e2-25e8c73df955/topics/visible-flex-larger-amplitude/scripts/resume_20261120/a04_historical_location_seeds.json",
    "--outdir",
    "/home/runner/work/_temp/visible-larger-research-46079535427-1/research/fixed-fejer-reference",
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
  "cleanup_generated": {
    "deleted": {
      "record_count": 0,
      "recorded_bytes": 0,
      "records_with_bytes": 0,
      "listed_file_count": 0,
      "records_with_file_lists": 0,
      "canonical_metadata_bytes": 2,
      "canonical_metadata_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "canonicalization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
      "detail_scope": "Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"
    },
    "skipped": {
      "record_count": 0,
      "recorded_bytes": 0,
      "records_with_bytes": 0,
      "listed_file_count": 0,
      "records_with_file_lists": 0,
      "canonical_metadata_bytes": 2,
      "canonical_metadata_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "canonicalization": "UTF-8 JSON; ensure_ascii=False; sort_keys=True; separators=(',',':'); allow_nan=False",
      "detail_scope": "Complete original entries remain in runner status.json and followup-journal.json; recorded_bytes sums only explicit bytes fields; listed_file_count counts only explicit files lists"
    },
    "scope": "Only explicit patterns, newly generated regular caches and an already returned child; never parent/input/output files"
  },
  "step_id": "prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run20",
  "summary_errors": [],
  "missing_outputs": []
}
```

当前完整科学实际源码提交 `c592e434ac19b1659c179ab6929ed592f104f362`，launcher `f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506`，PID3277。实际 model `0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add` 与19初值相同；真实初点 `7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47`。本次是独立 runner 的原参考初值重建，未继承19的试步或历史。

初始几何事件的准确时间为 **2026-11-27T23:13:27.016759+00:00**，不是后续 trial 时间。初统计 Phi=3825.0583894874153、最大Gram残差=.6460503011117507；本次观察未给初统计独立事件时刻，不回填几何时刻。六个完整有限有符号约束为：

| family | 原真实 g |
|---|---:|
| reach | 0.9684249942095058 |
| body_diameter | -0.038135527545650194 |
| distance_plus | 0.005863061771032241 |
| distance_minus | -3.0936337267043594 |
| cap_diameter | -0.06715131487906445 |
| height_floor | -1.0411715967426867 |

这六值与19原初值逐项相同，符合只改恢复阻尼、不改初始场的参数设计；这不是恢复方向、接受结果或连续费用的相同性结论。reach和distance_plus仍正，有限筛尚不可行。accepted=0、完整科学report=false，trial统计/几何/决定尚未观察，所有对应 None 读数保其原错误而不填零。normal进度累计返8762且逻辑失败0，也不代根的连续唯一性。

以下完整原 active observation 保所有已知字段、小文件整身份、缺值错误和真实源绑定；仅这条本来已有的小投影被读取，没有额外计算或自建前门。

```json
{
  "step_id": "complete-fixed-fejer-meridian-batched-bhalf-mu001-first-20261127",
  "scientific_source_commit": "c592e434ac19b1659c179ab6929ed592f104f362",
  "scientific_source_sha256": "f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506",
  "pid": 3277,
  "observations": {
    "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-normal-evaluation-progress.json": {
      "phase": "initial-complete-geometry-returned",
      "at": "2026-11-27 23:13:27 UTC",
      "point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "cached_angle_roots": 1448,
      "closure_original_returns": 8762,
      "closure_logical_failures": 0
    },
    "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json": {
      "math_at": "2026-11-27T23:13:27.016759+00:00",
      "math_event": "initial-geometry-returned",
      "math_driver": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
      "math_model": "0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add",
      "math_source": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
      "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
      "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_Phi": 3825.0583894874153,
      "initial_Gram": 0.6460503011117507,
      "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "initial_violation": 0.9684249942095058,
      "initial_geometry_complete": true,
      "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_Phi": 3825.0583894874153,
      "current_Gram": 0.6460503011117507,
      "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
      "current_violation": 0.9684249942095058,
      "current_geometry_complete": true,
      "current_state": "initial statistics returned; no accepted direction",
      "accepted_directions": 0,
      "complete_report": false,
      "stop_reason": null,
      "observer_failures": 0,
      "current_g_reach": 0.9684249942095058,
      "current_g_body_diameter": -0.038135527545650194,
      "current_g_distance_plus": 0.005863061771032241,
      "current_g_distance_minus": -3.0936337267043594,
      "current_g_cap_diameter": -0.06715131487906445,
      "current_g_height_floor": -1.0411715967426867
    }
  },
  "complete_small_progress_file_identities": [
    {
      "path": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-normal-evaluation-progress.json",
      "bytes": 3332,
      "sha256": "37e1bc49ea3e8be9c8551916a45a71eab20179ff5e1bd831254aef3f434865cf",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "bytes": 6150,
      "sha256": "182e15bb795593fdc02daabb82019303d3a18f451e1d5f2084dc0b5bf8cd97d9",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "observation_errors": [
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "latest_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "latest_trial_statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "latest_trial_geometry.complete",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "latest_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.point_sha256",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.actual_positive_physical_g",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.accepted",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.geometry.maximum_physical_families",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.Phi",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    },
    {
      "report": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "field": "last_completed_trial.statistics.max_relative_gram",
      "error": "TypeError: 'NoneType' object is not subscriptable"
    }
  ],
  "child_exit_code": null,
  "child_natural_return_not_observed": true,
  "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
  "observation_identity_sha256": "372d185be14eada7de968c4ed797bcba80f5907dab5d0d3d30dfd37c3b550612",
  "observed_utc": "2026-11-27T23:14:32Z"
}
```

继续同一完整157词科学；自然返回后接原pure及完整normal/geometry/closed/R716/mesh，完整final和所有同源输入实际存在才可restart。当前仍不具备本课题README完成证据。

## 2026-11-27 23:39:50 UTC — 第一个真实trial统计返回，几何仍未返

独立20的首trial在23:20:09.363322开始，完整点 `3459061e0d7631ad5f69d6d2b7e02801c576d3941ee13963f379a3896927f28b`。原trial-statistics-returned准确时刻 **23:28:21.769877+00:00**，Phi=3824.783531693056、Gram=.6460723929865344。相比本轮初值，Phi下降而最大Gram误差上升；这仍只是统计。trial geometry、alpha、接受决定未知，current仍初始7e06/accepted0，不能将初g=.9684249942095058写成这个trial的g，也不能以Phi下降推恢复接受或metric改善。

该原观察在固定提交的完整小索引中，含所有source/PID、全部原正常/数学scalar、缺值错误与完整请求，以下精确whole文件记录可逐字恢复；本节只另列整个数学子对象和两份完整小文件身份，不声称它代替整个索引。未取任何runner raw，也未改science。

```json
{
  "complete_original_index": {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46079535427-1.md",
    "fixed_commit": "d749ebc2fadc65a72523efb8397cab253f4d1cca",
    "bytes": 51612,
    "sha256": "6c01c341c27e05bcc3786b2e3e6edd0547054677984571ba3fb497abbcce4894",
    "git_blob_sha": "bc0980094b08eabbe56ae9ab82dc50e80983ca38"
  },
  "complete_mathematical_observation": {
    "math_at": "2026-11-27T23:28:21.769877+00:00",
    "math_event": "trial-statistics-returned",
    "math_driver": "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f",
    "math_model": "0abfbfe4cc5878ca6bfbbbf37c6dbb82610d7c49ce3ece40a8a609406db53add",
    "math_source": "321be35ae07519fcd283e09d209b19fedde570a54fdc65be79fc1caf848f3cc5",
    "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
    "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
    "initial_Phi": 3825.0583894874153,
    "initial_Gram": 0.6460503011117507,
    "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
    "initial_violation": 0.9684249942095058,
    "initial_geometry_complete": true,
    "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
    "current_Phi": 3825.0583894874153,
    "current_Gram": 0.6460503011117507,
    "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
    "current_violation": 0.9684249942095058,
    "current_geometry_complete": true,
    "current_state": "initial statistics returned; no accepted direction",
    "trial_point": "3459061e0d7631ad5f69d6d2b7e02801c576d3941ee13963f379a3896927f28b",
    "trial_Phi": 3824.783531693056,
    "trial_Gram": 0.6460723929865344,
    "trial_accepted": null,
    "accepted_directions": 0,
    "complete_report": false,
    "stop_reason": null,
    "observer_failures": 0,
    "current_g_reach": 0.9684249942095058,
    "current_g_body_diameter": -0.038135527545650194,
    "current_g_distance_plus": 0.005863061771032241,
    "current_g_distance_minus": -3.0936337267043594,
    "current_g_cap_diameter": -0.06715131487906445,
    "current_g_height_floor": -1.0411715967426867
  },
  "original_small_file_identities": [
    {
      "path": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-normal-evaluation-progress.json",
      "bytes": 3367,
      "sha256": "444eccaf863a9f87f3db8c8082bf96e8ad46863baf0694ceca18f30ba4a8973d",
      "two_complete_bounded_reads_agreed": true
    },
    {
      "path": "fixed-fejer-meridian-batched-bhalf-mu001-first/actual-mathematical-progress.json",
      "bytes": 7278,
      "sha256": "f77d9757b01a0f696a6647e242ac1a055ef2bcc23746e4a7174e5d2a9f714445",
      "two_complete_bounded_reads_agreed": true
    }
  ],
  "source_commit": "c592e434ac19b1659c179ab6929ed592f104f362",
  "source_sha256": "f600bc6e8c94428025bc517d7ad00e561a6cde1cb8a96fd709fdf7c8dfc8b506",
  "pid": 3277,
  "complete_original_observation_identity_sha256": "99668f3d44faa13ce332ad72d8b21b1d66db5736fe81b971dbcf7fb50626de94",
  "observed_utc": "2026-11-27T23:34:43Z"
}
```

科学report仍false、未自然返回；完整normal/geometry/R723/R716/mesh等待其真实材料，继续原完整预算。
