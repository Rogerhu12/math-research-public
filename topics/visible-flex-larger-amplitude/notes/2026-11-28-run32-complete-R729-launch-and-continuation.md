# Run32：R728物理母体与R729全行恢复的完整独立执行

会话Astra-larger-e4e2a2bf-20261126（AI-assisted），2026-11-28 08:15:55 UTC。本条记录完整参数与启动提交，不将准备状态冒实际运行或数学成功。

## 已刊完整源码和本次完整发布

完整源码8件431128B已在main`6c07ca019af58f0102a40a00c63027948ee0332a`。完整24runtime/138角色中的20共享体仍是31实际源码，原137role逐字保、新增R729 kernel一项。见[源总表](../computations/fixed-fejer-r728-R729-common-slack-complete-source-delivery.json)。[R729完整证明](../results/R729-common-slack-all-row-dual-coercivity-and-feasible-recovery.md)提供准确全行对偶收敛/可行恢复/gap；有限轮次和binary64数值gap不冒证书。

本次完整出版参数6件245295B与launch7件218741B，共13件464036B（题内461825B、题外workflow2211B）。没有待补的本32源码/参数/launch附件。它们的准备时null保持原字；本次真实主线提交另由log/H及此note的Git历史给出。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-complete-parameter-binding.json",
    "bytes": 22016,
    "sha": "8469f30893db495b86f8602c4afddc8b0c7de284",
    "sha256": "0c8f4e8f15936600d64c55aabc9e1f2aeebdb5a470c86b813f4f45f139594587"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-science-complete-ready.json",
    "bytes": 78562,
    "sha": "e37465ec696609b7d0ed87a4bd7819faec3b46c5",
    "sha256": "4ce7a7e09cd27d7ac7388683da8deb1ca6117c27a99e89debb39efacbbd18815"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-pure-complete-ready.json",
    "bytes": 67817,
    "sha": "63400f463d39cb92f79aa22b2686de33098fc125",
    "sha256": "7368155f3a3424d517525a35035f4ed60cad90554919df8e5a26a6916230f70a"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_R729_run32_parameters.mjs",
    "bytes": 45853,
    "sha": "476841b30e5610c5d4d4427cffc316376194389f",
    "sha256": "5103b5cff2fe4dd9b4e6c330e65e39af352e87415200d0bd164f2be148082ce3"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run32-R729-complete-bhalf-parameters.md",
    "bytes": 17535,
    "sha": "052a36004e558351d20b64055339256826dbb389",
    "sha256": "00b92d170b98b94195e5d4cb5cc46ff9da566e847fb8fde9ea826ddbac7635dc"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-bhalf-complete-parameter-delivery.json",
    "bytes": 13512,
    "sha": "739592eac6394174a90863d0fc903f597b40163c",
    "sha256": "38c4d00bc80d96733f3f6aad4388608a49158476ec8c94207c4441c22519f742"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/public_actions_controller_parallel32_geometry_locations.py",
    "bytes": 21888,
    "sha": "cbb8556396d455849430bb642fb25935d270643f",
    "sha256": "3b64dc1d2a6e517ac06edf230d4647e7d8f9008ce2e7e664d702f40c3cea6290"
  },
  {
    "path": ".github/workflows/visible-larger-20261128-parallel32.yml",
    "bytes": 2211,
    "sha": "925cbdc3edec3db0465c86784d09f55336f504c3",
    "sha256": "77525a254c23d2ec0e038e4578b908736dada858ae5435fed70b8ed19fe7bbda"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-followups-32.json",
    "bytes": 78678,
    "sha": "294e50f0292b52270f33cb344f43f3c6ef14c425",
    "sha256": "c913ea85839cddfb5cfd5a1fea3ca4cd864c04aff89b29b13f9ed6d4fd4f89b9"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/resume-20261128-actions-request-32.json",
    "bytes": 40137,
    "sha": "400edd6988db4ac714710a3091adc75d313ef25b",
    "sha256": "1d6ca2d776175ea9f5d79008c5a59317b5c68f85d83ffd3ab6aac3cb8ce94e92"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_R729_run32_complete_launch.mjs",
    "bytes": 45182,
    "sha": "11dca424e2ff96771ae9f0bc0324082f1cb87e85",
    "sha256": "205139d958cefd803eda4797a889a46dd4bc60e877148cc74ef5394de80a1f6a"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-run32-R729-complete-common-slack-launch-preparation.md",
    "bytes": 16989,
    "sha": "8f9b485dfeb0d9777e74a4ac401ed8422950059d",
    "sha256": "a90052f4677f0deef50d850e75e7452721abb4d0b7bb6bc765f850a4d0888964"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-r728-R729-run32-complete-launch-delivery.json",
    "bytes": 13656,
    "sha": "90b5f82413ae08c2e3fa8bf2cc98bb25e4d0a1cc",
    "sha256": "6b8b78ae8252174d513894415b908c4602db06b98bf188c8db50d008420c1bb9"
  }
]
```

## 实际执行合同

active request与queue parent均为`visible-larger-resume-20261128-32`，namespace `fixed-fejer-r728-R729-bhalf-first`。完整初三步queue78678B：maker6词/14 formal、reference26词/62 formal、science157词/575 formal；原458选择器全部保，新4×29等R729诊断另列。原64 live保持。两输入源不变，只第二step描述ID为run32。全变量/域/M160/J923/N2048/32stage及原4恢复/64QP/15line、metric1/16、两damping.01和所有外部peer原CLI保。

当前相对31唯一新算法是R729恢复QP分支；R728的固定(-,+)半波、完整Slerp mean、全部原normal/geometry source和外层接受仍同定义。原QP先原样返回，只有restoration的两指定dependent状态才用剩余原整数限做全行CCD sweep；CG advance、sweep和coordinate visit分开。原qp对象/旧Pg不改；实际选中方向、全部原C复读、dual/gap与adoption独立字段归因。完整finite错误与fallback保，没有新数值准入门。

完整capacity-wait controller保350min admission checkpoint与官方360min窗口；在途child照原逻辑等自然返回，不能把时间或退出视为完成。真实pull/双README diff随原循环，root云核不冒pull。新独立workflow只由本次request路径的普通push触发，cancel-in-progress=false，使用原公开runner和固定依赖。32新workflow路径在固定1557946f API返回404，未覆盖别人的现有workflow。

## 下一整步骤

science自然返回完整report后，按同activeID把整个pure步骤放入同queue；7词/564 formal含全部原445字段，whole pure-only queue61349B/SHA1283608eb05ea62e5f5fbe55363678a1f9f82e3c3d169da868e251d67a33c60c/blobe84be365394a452436849f08d3586fd29eca6bb7。初三步＋pure合计139934B超过原95000，所以保留完整先后次序；当前finish_when_done=false。未因限制删参数、字段或原预算。

本次尚无32实际run/job、输入、science model、full point、QP触发/方向采用、nonlinear acceptance、final13、typed或准确费用，后继只按本32真实返回登记。原31初Gram.822374918515021、原28首QP的2advance/dependent-zero都是外部已记录事实，不能填作本32实际字段。原25/28及其他历史和未读peer义务完整保参数总表，不造跨runner raw或未知父。

## 历史原字与范围

完整[参数总表](../computations/fixed-fejer-r728-R729-bhalf-complete-parameter-delivery.json)与[launch总表](../computations/fixed-fejer-r728-R729-run32-complete-launch-delivery.json)给出全父文件、完整JSON pointers、再生器、全部源和当前参数。31运行所需闭包早已8591发布，31另12份非runtime附件仍按其原whole blob保护待刊；不把这一点误称32缺少实际runtime。原旧参数词法整理的whole读者仍须按[对应固定历史](2026-11-28-complete-ready-json-lexical-format.md)整恢复原字，不沿旧SHA读格式后新体。

所有科学raw只在runner，Git只全源码/参数/配方和必要紧凑实际结论；无Python/AST/fixture/benchmark前门，也未减README完成标准。

## 2026-11-28 08:29:52 UTC — 32真实运行两输入返回，完整科学已启动

公开真实run46125006601/1，初始head386079ffa43eb45577620becb418727b8bbe153c，created08:16:03Z；job140917553486 started08:16:06Z、research step08:16:52Z，官方仍in_progress。加载controller3b64dc1d2a6e517ac06edf230d4647e7d8f9008ce2e7e664d702f40c3cea6290。

必要输入1真实source1c2d176da71670f6774c24ff3a3d812a79b90c11，退出0/6.170766205999996秒，完整report65320B/SHA3d816ecda90fe26f92e6c0680f43b3b45bdda1acefec6784321a7c63c8d6ba10。必要输入2真实source0e94d7b0776a5e43517a3a60a1b03f1e6135a0d3，退出0/516.758671284秒，完整report84974B/SHA1603b082901c58606d49a27b8f427d6d516066648c24cc53981a0bc3292dd53f。真实reference212eb5fde565e76db7255f8c5605764268340b9c1636953ab0a8f8b254bf24cb、carrier84060403d6ad8a4fdd17532028bda7b4a15a6671cd6bc5950ae4f0c828cd118e；所有输入/输出whole身份、原完整6/26参数词和2项源码均保下面完整小卷。M160/J923/P7377/N2048、height1.947054437068418，原2218完整leaf/whole_tail=true/unresolved_tail_dropped=false；accuracy_reached=false保原义，既不改称已付容差，也不虚称原输入因此不完整。

本run实际material binding35712B/SHA86ee65c5f2f16b9f9dc50759c1b5aa1755d9b508a91458a7f68d048a5372a437；locations SHAa05fe46a35808fecfb43bebf304581989c2d5242cf22a98e2da203dd831e7a70、历史provenance SHA5bd092a5cbb3274c3917fd79ff69f1efcd22327bfdf84821d2f95668a303b49c。虽reference/carrier与其它run同字，运行/报告/binding仍是自己的，未借旧物理场。

08:26:04Z真实science child source20911541326908882a45a1a1815ec8a05ebb4420/PID3496，launcher SHAda440c59c6fbd798b0dc1711a274e5480de9a8ecb1e71d1382976180ea3bd7f3。两progress文件首次均FileNotFoundError，完整错误保whole索引；此时尚无自身model/point/Phi/Gram/geometry/接受或退出值。未把输入完成当科学完成，也未继承31自己的初始值；自然science返后才换完整61349B pure队列。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46125006601-1-part-001.md",
    "bytes": 5756,
    "sha256": "75eccb395732129db2d59a639abef181873a817edd059ca52c7035990b4c14f8",
    "git_blob_sha": "b0834201050eb9f74b1c08aa03f63db32a1919ef",
    "fixed_commit": "81ab3893dbff4e248adc6c3e97ebd928a03c196e",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  },
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46125006601-1-part-001.md",
    "bytes": 16606,
    "sha256": "9093d0d9ba35852e8b5857066ea7a8ca4999e5ae962d5835302ea67b9852ed83",
    "git_blob_sha": "86914149fcfbe442a9dd8f3c6af42fceac10ee85",
    "fixed_commit": "4e9655966fa8476ad9027bbbf686b70407377d94",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  },
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46125006601-1.md",
    "bytes": 49115,
    "sha256": "dea19624b0e33666f4b19474416823d7554b499f23dec04a0345ecd7f287f40e",
    "git_blob_sha": "9eaf6e8c5c829fd7b799f42785bb65d3a368191c",
    "fixed_commit": "4e9655966fa8476ad9027bbbf686b70407377d94",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```

## 2026-11-28 09:07:42 UTC — 32自身完整初geometry与首trial统计

完整索引固定3a38882e887dae0688835ccd9b1b41c7eb6d24c6，observed2026-11-28T09:01:24Z，source20911541326908882a45a1a1815ec8a05ebb4420/PID3496、driver501313cc50c2a877f98318193a8878242ec13c2f8a0664740a4ea8c47eb4baa7。自身真实model78717b20b1fa33db5ccc018be03ee6c9d93a0b89615fdfd25d1049492c0fce40；math source4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94、target957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9。与31同model/数值来自本次计算，未借31字段或证书。

initial/current=7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47，accepted0；Phi14106.361942260944/Gram.822374918515021，initial/current_geometry_complete=true。全六族reach.7631911760908718、body−.04189769456408332、distance_plus−.09518118442527368、distance_minus−3.04023779712659、cap−.06715131487906445、height−1.0411715967426867。K14.23819037053068/D_point_lower4.109115766386664，热点cell509/u.6193095930415985/phi1.303883669702795/branch0/s=null；distance_plus_phi=π/2。仍不可行，held改善不支付reach。

首restoration alpha1完整trial1ec67648343c521e4ee605fd8867a040794a614998c81ea9d970f507ff1d4092，于08:56:44.221360Z返自身Phi14108.010873083527/Gram.8249934419612122；trial_accepted=null，几何未返。点不同于31首trial，但live字段未给R729触发/采用/全扫数/gap，不据点差归因。complete_report=false、stop_reason=null、observer_failures0。全原575/564正式读数待科学自然返回，随后才以原61349B整pure同ID接续。

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46125006601-1.md",
    "bytes": 55163,
    "sha256": "a97d390d424050384f094130e9579b371854b066687bd3e4d3abb35ba6fbef99",
    "git_blob_sha": "c19fc8b6b9b1b17ec90e04747ea6b34a70ea96cd",
    "fixed_commit": "3a38882e887dae0688835ccd9b1b41c7eb6d24c6",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```

## 2026-11-28 10:08:22 UTC — run32官方failure与最后自身完整状态

官方run46125006601/1、job140917553486 completed/failure，job终止2026-11-28T09:41:53Z，研究步骤终止2026-11-28T09:41:49Z。该run自身实际异常尚未取得，原因未知，不能用33的根README异常或运行时长代替。子科学未观察到自然完成，不把job failure当数学报告。

仍自身初始7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47/accepted0；1ec676首trial仅统计Phi14108.010873083527、Gram.8249934419612122。该trial几何/acceptance及R729真实触发/采用/gap未返；不得由与31点不同推断fallback已采用，不借31自身几何。

下方完整官方jobs与末观察保全部源/model/点/六族/K位置、原错误及null；未返final/typed/pure/证书不补造。原全部参数、预算、源责任继续保留；移除失效槽并接新34/33恢复运行。

```json
{
  "official_jobs": {
    "total_count": 1,
    "jobs": [
      {
        "id": 140917553486,
        "run_id": 46125006601,
        "workflow_name": "Visible larger amplitude R728 R729 common slack 20261128 32",
        "head_branch": "main",
        "run_url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/runs/46125006601",
        "run_attempt": 1,
        "node_id": "CR_kwDOVt5L2s8AAAAgz1c5Tg",
        "head_sha": "386079ffa43eb45577620becb418727b8bbe153c",
        "url": "https://api.github.com/repos/Rogerhu12/math-research-public/actions/jobs/140917553486",
        "html_url": "https://github.com/Rogerhu12/math-research-public/actions/runs/46125006601/job/140917553486",
        "status": "completed",
        "conclusion": "failure",
        "created_at": "2026-11-28T08:16:04Z",
        "started_at": "2026-11-28T08:16:06Z",
        "completed_at": "2026-11-28T09:41:53Z",
        "name": "Construct the same fixed target and solve complete R728 with R729 common slack",
        "steps": [
          {
            "name": "Set up job",
            "status": "completed",
            "conclusion": "success",
            "number": 1,
            "started_at": "2026-11-28T08:16:07Z",
            "completed_at": "2026-11-28T08:16:07Z"
          },
          {
            "name": "Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
            "status": "completed",
            "conclusion": "success",
            "number": 2,
            "started_at": "2026-11-28T08:16:07Z",
            "completed_at": "2026-11-28T08:16:15Z"
          },
          {
            "name": "Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
            "status": "completed",
            "conclusion": "success",
            "number": 3,
            "started_at": "2026-11-28T08:16:15Z",
            "completed_at": "2026-11-28T08:16:21Z"
          },
          {
            "name": "Install the recorded numerical and automatic differentiation dependencies",
            "status": "completed",
            "conclusion": "success",
            "number": 4,
            "started_at": "2026-11-28T08:16:21Z",
            "completed_at": "2026-11-28T08:16:52Z"
          },
          {
            "name": "Execute public research and publish independent compact records",
            "status": "completed",
            "conclusion": "failure",
            "number": 5,
            "started_at": "2026-11-28T08:16:52Z",
            "completed_at": "2026-11-28T09:41:49Z"
          },
          {
            "name": "Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065",
            "status": "completed",
            "conclusion": "skipped",
            "number": 9,
            "started_at": "2026-11-28T09:41:49Z",
            "completed_at": "2026-11-28T09:41:49Z"
          },
          {
            "name": "Post Run actions/checkout@11d5960a326750d5838078e36cf38b85af677262",
            "status": "completed",
            "conclusion": "success",
            "number": 10,
            "started_at": "2026-11-28T09:41:49Z",
            "completed_at": "2026-11-28T09:41:49Z"
          },
          {
            "name": "Complete job",
            "status": "completed",
            "conclusion": "success",
            "number": 11,
            "started_at": "2026-11-28T09:41:49Z",
            "completed_at": "2026-11-28T09:41:49Z"
          }
        ],
        "check_run_url": "https://api.github.com/repos/Rogerhu12/math-research-public/check-runs/140917553486",
        "labels": [
          "ubuntu-latest"
        ],
        "runner_id": 1000012747,
        "runner_name": "GitHub Actions 1000012747",
        "runner_group_id": 0,
        "runner_group_name": "GitHub Actions"
      }
    ]
  },
  "complete_latest_observation": {
    "step_id": "complete-fixed-fejer-r728-R729-bhalf-first-20261128",
    "scientific_source_commit": "20911541326908882a45a1a1815ec8a05ebb4420",
    "scientific_source_sha256": "da440c59c6fbd798b0dc1711a274e5480de9a8ecb1e71d1382976180ea3bd7f3",
    "pid": 3496,
    "observations": {
      "fixed-fejer-r728-R729-bhalf-first/actual-normal-evaluation-progress.json": {
        "phase": "normal_chain_enter",
        "at": "2026-11-28 09:36:36 UTC",
        "point": "1ec67648343c521e4ee605fd8867a040794a614998c81ea9d970f507ff1d4092",
        "cached_angle_roots": 1441,
        "closure_original_returns": 47129,
        "closure_logical_failures": 0
      },
      "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json": {
        "math_at": "2026-11-28T08:56:44.221360+00:00",
        "math_event": "trial-statistics-returned",
        "math_driver": "501313cc50c2a877f98318193a8878242ec13c2f8a0664740a4ea8c47eb4baa7",
        "math_model": "78717b20b1fa33db5ccc018be03ee6c9d93a0b89615fdfd25d1049492c0fce40",
        "math_source": "4b63c9ab05875aea79cdd537fe4134dcd3be36345d75281cc154fabf10d49c94",
        "math_target": "957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9",
        "initial_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
        "initial_Phi": 14106.361942260944,
        "initial_Gram": 0.822374918515021,
        "initial_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
        "initial_violation": 0.7631911760908718,
        "initial_geometry_complete": true,
        "current_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
        "current_Phi": 14106.361942260944,
        "current_Gram": 0.822374918515021,
        "current_geometry_point": "7e06e86e65d3edffa946bacbfc47a8e3f09ba95bfe5ff5d2ee53816b1c68ac47",
        "current_violation": 0.7631911760908718,
        "current_geometry_complete": true,
        "current_state": "initial statistics returned; no accepted direction",
        "trial_point": "1ec67648343c521e4ee605fd8867a040794a614998c81ea9d970f507ff1d4092",
        "trial_Phi": 14108.010873083527,
        "trial_Gram": 0.8249934419612122,
        "trial_accepted": null,
        "accepted_directions": 0,
        "complete_report": false,
        "stop_reason": null,
        "observer_failures": 0,
        "current_g_reach": 0.7631911760908718,
        "current_g_body_diameter": -0.04189769456408332,
        "current_g_distance_plus": -0.09518118442527368,
        "current_g_distance_minus": -3.04023779712659,
        "current_g_cap_diameter": -0.06715131487906445,
        "current_g_height_floor": -1.0411715967426867,
        "current_K": 14.23819037053068,
        "current_D_point_lower": 4.109115766386664,
        "current_K_cell": 509,
        "current_K_u": 0.6193095930415985,
        "current_K_phi": 1.303883669702795,
        "current_K_branch": 0,
        "current_K_s": null,
        "trial_alpha": 1,
        "trial_phase": "restoration",
        "current_distance_plus_phi": 1.5707963267948966
      }
    },
    "complete_small_progress_file_identities": [
      {
        "path": "fixed-fejer-r728-R729-bhalf-first/actual-normal-evaluation-progress.json",
        "bytes": 3360,
        "sha256": "811fc40d20f543ea21f4c1af0e7372fd2de4eeb02fc41951aac0b8fab55ce00d",
        "two_complete_bounded_reads_agreed": true
      },
      {
        "path": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "bytes": 8811,
        "sha256": "5b08de498c6f1ef834b6bde82aae3ddc0b8e15602f02bbda6dc5990627c7e55d",
        "two_complete_bounded_reads_agreed": true
      }
    ],
    "observation_errors": [
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "latest_trial_geometry.point_sha256",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "latest_trial_geometry.positive_physical_g",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "latest_trial_geometry.complete",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "last_completed_trial.point_sha256",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "last_completed_trial.actual_positive_physical_g",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "last_completed_trial.accepted",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "last_completed_trial.geometry.maximum_physical_families",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "last_completed_trial.statistics.Phi",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "last_completed_trial.statistics.max_relative_gram",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "latest_trial_geometry.maximum_absolute_principal_curvature",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "latest_trial_geometry.returned_locations.curvature.cell",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "latest_trial_geometry.returned_locations.curvature.u",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "latest_trial_geometry.returned_locations.curvature.phi",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "latest_trial_geometry.returned_locations.curvature.branch",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      },
      {
        "report": "fixed-fejer-r728-R729-bhalf-first/actual-mathematical-progress.json",
        "field": "latest_trial_geometry.returned_locations.curvature.s",
        "error": "TypeError: 'NoneType' object is not subscriptable"
      }
    ],
    "child_exit_code": null,
    "child_natural_return_not_observed": true,
    "observations_are_not_a_completed_step_or_a_scientific_certificate": true,
    "observation_identity_sha256": "d1d3b6958763acbe01928b6fe09dc0fe14b98ad5bd959480c4c9938069482cfb",
    "observed_utc": "2026-11-28T09:36:44Z"
  }
}
```

原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/2026-11-28-public-actions-46125006601-1.md",
    "bytes": 55164,
    "sha256": "26dca16a43df1983195c0c8819ad1bdfdea29c4cd85cc5b8dbe70658790c9911",
    "git_blob_sha": "046fe32a8fb426dbc7c497efa2d4627d7e4c6090",
    "fixed_commit": "df0c989652a0f243a1bae3cb37e116932455cc99",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```
