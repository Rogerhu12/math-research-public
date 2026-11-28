# Run40 — 整个轴向闭面的真实有限相位物理求解

会话 Astra-larger-e4e2a2bf-20261126。完整6件源/参数/工作流现刊触发，实际run/job/科学入口/point/误差当前均null。独立消费已刊R744/R746/R747/R748真实闭源，不消费38、39、39b数值，也不借它们的g或时间。R748完整1809B源已main e33bfacdb5807b739a040079dc46a32a55fb6385；manifest中其先前observed_main=null保写包当时的原事实。

## 同一完整初度量与全部物理自由

所有5设计、每个阶段从开始都用同一R747零相位真F0回拉g，整个周期中央、两端、两个完整帽及正则中心没有删除任何材料区域。相位固定[0,π/2]，逐正时间结真的求解三空间分量，时间自然三次样条完整定义F_t，不假定Killing场、Haar或只转动一个固定像。

5个粗设计全部原预算执行：legacy真原命名端帽、offset-cap-only、R748 legacy-developable、R748 offset-developable，以及R748只锁原完整中央的比较支。其余4支真实握持区以外三分量全自由。若锁柱比较支赢，后续3层在原锁场基上严格扩充：原global/cap/roll每一原列保留，历史3/4/8span与当时角模完整纳入，再加(free−locked)三分量中央列；同名旧系数逐字拷贝、新列零，故原形场逐点逐相位保留。原非嵌套3→4、8→12的卷端样条不再以LS代替精确包含。普通free支仍是明确的LS暖启，不声称它完全同旧场。

所有端有真正C² v^(5/2)(1−v)^4形变和全角自由，帽和接缝都有物理自由。R748的正帽中心真first jet由germ mask精确保留，额外场在该点邻域C³，不消其终态非C³法向germ；这只保护非全等机制，完整嵌入/reach/held仍须候选实际支付。R747的C⁴冻结入口障碍不被假定为C²不可能。

## 原全部数值预算

```json
{
  "schema": "direct-evolving-closed-end/v1",
  "source_sha256": {
    "r748_developable_axial_caps.py": "947245856229ddeb95b83c763403e86bdd867c63b63b6013929d2e2a13a87b46",
    "r747_offset_arclength_closed_two_jets.py": "09b29cd06eec6887bf8f103f104cdd9ca598b691c3e7503fa2220dbafc71e3ac",
    "r746_axial_translation_closed_two_jets.py": "e5ab4d4a0921cb83c7eefc485147883d6dcea92ff9df6f3f3da8604440f174ef",
    "r744_extruded_closed_two_jets.py": "35bb8a1612dd22a8e215a7682ead0c9836b26f3a6c6b525a876fff178a3d6c24",
    "r742_tilted_disk_two_jets.py": "5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd",
    "r740_rolled_disk_seed.py": "b812afa381e2775433710edb9cfa9bd54f0b1b892935c21f2f785675bb4d866f",
    "bent_end_phase_fields.py": "5305a955f3f5a0f37a3097388b025889584ce2033fe82bcab0140ab8330b31ba",
    "bent_body_atlas.py": "873bcabafc61a7223736d7806201e289349f838359e59c539f27fafc066ad102"
  },
  "designs": [
    {
      "id": "legacy-named-free",
      "angle": "legacy",
      "mode": "named",
      "central": "free"
    },
    {
      "id": "offset-cap-only-free",
      "angle": "arc",
      "mode": "cap-only",
      "central": "free"
    },
    {
      "id": "legacy-developable-full",
      "angle": "legacy",
      "mode": "dev",
      "central": "free",
      "bend": 0.000244140625,
      "fade": [
        0.71,
        1.09
      ]
    },
    {
      "id": "offset-developable-full",
      "angle": "arc",
      "mode": "dev",
      "central": "free",
      "bend": 0.000244140625,
      "fade": [
        0.71,
        1.09
      ]
    },
    {
      "id": "legacy-developable-boundary",
      "angle": "legacy",
      "mode": "dev",
      "central": "locked",
      "bend": 0.000015625,
      "fade": [
        1,
        1.095
      ]
    }
  ],
  "metric_loss_scale": 1.5,
  "curvature_cap": 9.55,
  "bend_weight": 0.8,
  "support_goal": 0.103,
  "support_weight": 8,
  "normal_displace_goal": 0.045,
  "normal_displace_weight": 1.5,
  "travel_goal": 0.35,
  "travel_weight": 0.6,
  "jacobian_probe": 5e-8,
  "dense_jacobian_entries": 42000000,
  "coarse": {
    "id": "all-five-coarse",
    "degree": 3,
    "cap_degree": 3,
    "roll_spans": 3,
    "roll_modes": 3,
    "intervals": 2,
    "mesh": [
      27,
      11,
      8,
      7
    ],
    "check": [
      69,
      21,
      15,
      13
    ],
    "max_nfev": 52,
    "inner": 85,
    "regularizer": 0.000007,
    "extra_check": false
  },
  "refinements": [
    {
      "id": "fixed-target-space-time-1",
      "degree": 4,
      "cap_degree": 4,
      "roll_spans": 4,
      "roll_modes": 5,
      "intervals": 4,
      "mesh": [
        35,
        13,
        10,
        9
      ],
      "check": [
        77,
        25,
        17,
        15
      ],
      "max_nfev": 60,
      "inner": 95,
      "regularizer": 0.000004,
      "extra_check": true,
      "previous_roll_spaces": [
        [
          3,
          3
        ]
      ]
    },
    {
      "id": "fixed-target-space-time-2",
      "degree": 5,
      "cap_degree": 6,
      "roll_spans": 8,
      "roll_modes": 7,
      "intervals": 8,
      "mesh": [
        49,
        17,
        12,
        11
      ],
      "check": [
        103,
        33,
        21,
        19
      ],
      "max_nfev": 68,
      "inner": 105,
      "regularizer": 0.000002,
      "extra_check": true,
      "previous_roll_spaces": [
        [
          3,
          3
        ],
        [
          4,
          5
        ]
      ]
    },
    {
      "id": "fixed-target-space-time-3",
      "degree": 7,
      "cap_degree": 8,
      "roll_spans": 12,
      "roll_modes": 9,
      "intervals": 16,
      "mesh": [
        65,
        21,
        16,
        14
      ],
      "check": [
        127,
        41,
        27,
        23
      ],
      "max_nfev": 76,
      "inner": 125,
      "regularizer": 0.000001,
      "extra_check": true,
      "previous_roll_spaces": [
        [
          3,
          3
        ],
        [
          4,
          5
        ],
        [
          8,
          7
        ]
      ]
    }
  ],
  "cloud_grid": [
    27,
    9,
    5,
    5
  ],
  "moment_grid": [
    125,
    33,
    25,
    19
  ],
  "geometry_phases": [
    0,
    0.2617993877991494,
    0.5235987755982988,
    0.7853981633974483,
    1.0471975511965976,
    1.3089969389957472,
    1.5707963267948966
  ]
}

```

5粗支各2个非零时间结，随后选中支4/8/16个非零时间结，每结各自原max_nfev52/60/68/76、inner85/95/105/125，所有停止理由/返回点保。每层在独立空间格验证全部真实Gram算子/K/support/area/correction，并增加中点及精化时每区间两异位时间点；末层含端点共65个时间核查样本。最后对选中粗层和3精化层，均付原7相位完整cloud有序弦、D/held样本和实体有向矩。训练值不代独立核查，全有限格不代连续上界。

## 六件整体身份

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_end_phase.py",
    "bytes": 14744,
    "sha256": "0b2ce5d260bdc4160b972d7b36cc0567660c6bbc18d56eb722265e6f0b04b701",
    "git_blob_sha": "269265194f8f7230ba9d46ea501efb8d838e52a6"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_end_phase_fields.py",
    "bytes": 10301,
    "sha256": "5305a955f3f5a0f37a3097388b025889584ce2033fe82bcab0140ab8330b31ba",
    "git_blob_sha": "bb38c6577c143a2cebb7fe76d5cd9a24eb9fa1fb"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/bent-end-phase-design-v1.json",
    "bytes": 4374,
    "sha256": "d9a5c7e543b187fc6ce00cad5b0ed1661a74ad6c9054d623b0f51675e708b4bd",
    "git_blob_sha": "aab93de98359b55bc9327659e8ee4b143e15bc38"
  },
  {
    "path": ".github/workflows/visible-larger-run40-bent-end-phase.yml",
    "bytes": 3468,
    "sha256": "2f8e45c4c8fc977d123f7036830346cc1ca3dcfca3f781870b5451e2e908288a",
    "git_blob_sha": "f8b2fd0ad981410cf6ab7ac1fdc1062537ede134"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/run40-bent-end-phase-request.json",
    "bytes": 16626,
    "sha256": "7191ea67e6c3c33a7a5b87974bd27878ebb86dbaa5e39a85c8e2ff3b88b9facc",
    "git_blob_sha": "6bdb6e6d065a586b07aee728fc7bb7776a885c9b"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/run40-complete-bent-end-phase-source-and-launch-delivery.json",
    "bytes": 19865,
    "sha256": "f84c8c4a3a8dcde2d543979c09ce3fe8df7d8ecbc684f6a0c27d4d0af2ba9f49",
    "git_blob_sha": "0fb15ec3c351cdfe90831e9b0f798df1d38961c0"
  }
]
```

## 全原入口及公共环境

```json
{
  "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_end_phase.py",
  "argv": [
    "--params",
    "{immutable_science_worktree}/topics/visible-flex-larger-amplitude/computations/bent-end-phase-design-v1.json",
    "--geometry-source",
    "{immutable_science_worktree}/topics/visible-flex-larger-amplitude/scripts/resume_20261126/r748_developable_axial_caps.py",
    "--out",
    "{runner_temp}/run40-bent-end-phase-{run}-{attempt}/field"
  ],
  "public_runner": {
    "runner": "ubuntu-latest public GitHub Actions, 4 vCPU, 16 GB",
    "python": "3.12.14",
    "dependencies": [
      "numpy==2.3.5",
      "scipy==1.17.0"
    ],
    "environment": {
      "PYTHONUNBUFFERED": "1",
      "PYTHONDONTWRITEBYTECODE": "1",
      "PYTHONHASHSEED": "0",
      "OPENBLAS_NUM_THREADS": "1",
      "OMP_NUM_THREADS": "1",
      "MKL_NUM_THREADS": "1"
    }
  },
  "output_contract": {
    "scientific_summary": "Whole small actual per-stage JSON with true coordinates, shape and metric/geometry outcomes, full runtime and failure status.",
    "raw_fields": "Complete raw arrays stay on the public runner; publish their length and SHA. No raw repository copy or external artifact.",
    "public_attempt": "notes/run40-bent-end-phase-<run>-<attempt>.json with its handoff marker after normal checked pull/rebase and inclusive 200 MB topic accounting.",
    "interpretation": "Independent finite point and grid values have their actual numerical meaning and do not establish an interval, a uniform embedding or exact isometry."
  },
  "actual": {
    "run": null,
    "attempt": null,
    "scientific_source_commit": null,
    "actual_point_sha256": null,
    "physical_coefficients": null,
    "fixed_metric_identity": null,
    "all_phase_gram": null,
    "reach": null,
    "held": null,
    "euclidean_separation": null,
    "global_certificate": null
  }
}
```

共享observer14863B/c47dde7a与Run36控制函数未改，10件科学输入按原whole身份固定。4CPU/16GB，Python3.12.14/numpy2.3.5/scipy1.17.0；job360分钟，未加子进程wallclock剪裁，8秒观察/120秒live/20秒发布重试；≤2700秒真实pull双README且有变只读差异立即照做。普通push遇竞态即pull/rebase后循环；只有main轻报告和whole身份，所有大raw/完整系数矩阵/NPZ留runner。以上代码已完整读过；实际数值必须等新进程返回。

## 原五粗及前两层同g真细化完整返回

公开run46148644102/1、job140990119811，科学固定源8561fc2b7a68f1cbede10f9421acbee8bd40b6bf，PID2569。根完整读取固定 [原实际记录](https://github.com/Rogerhu12/math-research-public/blob/a5a8e03bc5e4ec769716356854d5cbe67f2255a2/topics/visible-flex-larger-amplitude/notes/run40-bent-end-phase-46148644102-1.json)，70794B/SHA256 `2ef616a8c183431d6b8b53d83ab378de1d337755254d7e39652176ad20c8990e`/Git `c4f558c280b02f2670d9e178ad26c7ba1355eec7`。本时刻尚非科学终态，后续16区间整层及整像/体矩仍继续原预算。

|阶段/设计|实际完整合点|独立时空Gram峰|K工作峰|最小support|score|
|---|---|---:|---:|---:|---:|
|0 / legacy-named-free|6fb78b46b0983a07d5183a821ebaf3c2dd691f94a4c40bbec8969d706d9cd2c9|9.135032045701506|38287.37226017895|-1.0637522960275003|2818.339538370984|
|1 / offset-cap-only-free|d71c994767568f85358266a339eb1d9ceec0621e0ef3468bc0292c9a99774ee8|1929.8482581349583|1083052464.4066625|-1.1060737573720687|79387977.28696251|
|2 / legacy-developable-full|1db01286038f88882d8cad076296d8d956cf34ff851ea53b0eac4761b4124ff3|9.323266658414182|46110.550178704965|-1.1056477807957394|3392.08011315195|
|3 / offset-developable-full|571417a538a7499221b183a675f34dfe93b5070a5212f6a02f154c821362cd67|1930.5321968221297|12396225.856801046|-1.1066882613176303|910557.3460533055|
|4 / legacy-developable-boundary|2d25884b0f8cc8aecabba4c48e8bfef96b59a52ac0e94493f609e2dc783d1c8b|9.132224342164221|2885.3296246505834|-0.35860838965003805|221.30717906665444|
|5 / legacy-developable-boundary-expanded|ba153412e990b9237ebf450d298cd8628ca1c2d45a65b35376ae146010ec1577|8.040081916241995|2815.8379714384128|-0.1488750228236189|214.4922075089944|
|6 / legacy-developable-boundary-expanded|cce19ff7f718dd1f246f5a542ee2686e9a4f595afff8a5de19df9ad311f5c345|6.968190732291204|2087.580156559493|-0.5354668776994621|161.19993791948852|

五个原粗设计全部执行，最小原score选择原锁中央比较支；主精化依正式源明确转为 `central=expanded`，精确保留全部旧列后新增握外中央三物理自由，未把原锁比较支冒主求解。第一、二层完整合点 ba153412、cce19ff7 的同g独立时空Gram为8.040081916241995、6.968190732291204，K为2815.8379714384128、2087.580156559493；负support原值保留，不能直接冒已自交或完整reach结论。所有阶段零相位六jet差均0，完整原时结、独立相位、最大值真实材料地址、NPZ和系数/时间身份如下。当前仍不符合1e−6或全时几何要求。

以下逐字保留整份原小报告（含原request/冻结输入、所有7个完整阶段及本时刻unknown）。

```json
{
  "schema": "visible-larger-run40-actual-full-dynamic-bent-body-v1",
  "run_number": 40,
  "handoff_marker": "<!--run40-bent-end-phase-->",
  "run": "46148644102",
  "attempt": "1",
  "source_commit": "8561fc2b7a68f1cbede10f9421acbee8bd40b6bf",
  "initial_readme_checked_commit": "cd52bde3d4104ff72e4fb1ec96a8e9bfc70a0576",
  "command_identity_sha256": "fbba49570bf0cec1463a4dbecbf38ab3700f1c48901636542e02b73646c3a2b0",
  "request": {
    "path": "topics/visible-flex-larger-amplitude/computations/run40-bent-end-phase-request.json",
    "bytes": 16626,
    "sha256": "7191ea67e6c3c33a7a5b87974bd27878ebb86dbaa5e39a85c8e2ff3b88b9facc"
  },
  "scientific_inputs": {
    "script": {
      "role": "complete Run40 direct finite-phase physical shape search",
      "name": "bent_end_phase.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_end_phase.py",
      "bytes": 14744,
      "sha256": "0b2ce5d260bdc4160b972d7b36cc0567660c6bbc18d56eb722265e6f0b04b701",
      "git_blob_sha": "269265194f8f7230ba9d46ea501efb8d838e52a6"
    },
    "physical_fields": {
      "role": "complete original closed axial geometry, accurate jets and fractional phase directions",
      "name": "bent_end_phase_fields.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_end_phase_fields.py",
      "bytes": 10301,
      "sha256": "5305a955f3f5a0f37a3097388b025889584ce2033fe82bcab0140ab8330b31ba",
      "git_blob_sha": "bb38c6577c143a2cebb7fe76d5cd9a24eb9fa1fb"
    },
    "parameters": {
      "role": "complete dynamic time grids, whole chart and physical budgets",
      "name": "bent-end-phase-design-v1.json",
      "path": "topics/visible-flex-larger-amplitude/computations/bent-end-phase-design-v1.json",
      "bytes": 4374,
      "sha256": "d9a5c7e543b187fc6ce00cad5b0ed1661a74ad6c9054d623b0f51675e708b4bd",
      "git_blob_sha": "aab93de98359b55bc9327659e8ee4b143e15bc38"
    },
    "r740_source": {
      "role": "complete R740 geometric source for the elliptic starts",
      "name": "r740_rolled_disk_seed.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r740_rolled_disk_seed.py",
      "bytes": 10834,
      "sha256": "b812afa381e2775433710edb9cfa9bd54f0b1b892935c21f2f785675bb4d866f",
      "git_blob_sha": "72ef28649a33d115ef9a646a581f61dc3f3ddece"
    },
    "r742_source": {
      "role": "complete R742 tilted seed analytic two-position-jets six-field provider",
      "name": "r742_tilted_disk_two_jets.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r742_tilted_disk_two_jets.py",
      "bytes": 9706,
      "sha256": "5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd",
      "git_blob_sha": "eacaa69d88eae15963aee90d948391abfb9c745a"
    },
    "r744_source": {
      "role": "complete R744 extruded closed physical body atlas and six positional derivatives",
      "name": "r744_extruded_closed_two_jets.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r744_extruded_closed_two_jets.py",
      "bytes": 10327,
      "sha256": "35bb8a1612dd22a8e215a7682ead0c9836b26f3a6c6b525a876fff178a3d6c24",
      "git_blob_sha": "729efd888029dbaf9953617edfde81c0c7394fdd"
    },
    "r746_source": {
      "role": "R746 original full axial-translation closed source and proof",
      "name": "r746_axial_translation_closed_two_jets.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r746_axial_translation_closed_two_jets.py",
      "bytes": 5465,
      "sha256": "e5ab4d4a0921cb83c7eefc485147883d6dcea92ff9df6f3f3da8604440f174ef",
      "git_blob_sha": "f17399df53201a251da42198019f1c5a229baa62"
    },
    "r747_source": {
      "role": "complete R747 offset-ring arclength transport on closed physical body",
      "name": "r747_offset_arclength_closed_two_jets.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r747_offset_arclength_closed_two_jets.py",
      "bytes": 7820,
      "sha256": "09b29cd06eec6887bf8f103f104cdd9ca598b691c3e7503fa2220dbafc71e3ac",
      "git_blob_sha": "b9af0788b2ffea92bd6755d05a43fdb2509007f9"
    },
    "geometry_source": {
      "role": "complete R748 physically bending developable cap germs on the closed axial geometry",
      "name": "r748_developable_axial_caps.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r748_developable_axial_caps.py",
      "bytes": 1809,
      "sha256": "947245856229ddeb95b83c763403e86bdd867c63b63b6013929d2e2a13a87b46",
      "git_blob_sha": "5d60e4e2683faa5564072f120280421d32e515bf"
    },
    "atlas": {
      "role": "Run39 actual closed material atlas and field anchoring data",
      "name": "bent_body_atlas.py",
      "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_body_atlas.py",
      "bytes": 7229,
      "sha256": "873bcabafc61a7223736d7806201e289349f838359e59c539f27fafc066ad102",
      "git_blob_sha": "493b8aeed145723f91c69acd834da0617974b1ac"
    }
  },
  "actual_frozen_inputs": {
    "script": {
      "original_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_end_phase.py",
      "git_blob_sha": "269265194f8f7230ba9d46ea501efb8d838e52a6",
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_end_phase.py",
      "bytes": 14744,
      "sha256": "0b2ce5d260bdc4160b972d7b36cc0567660c6bbc18d56eb722265e6f0b04b701"
    },
    "physical_fields": {
      "original_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_end_phase_fields.py",
      "git_blob_sha": "bb38c6577c143a2cebb7fe76d5cd9a24eb9fa1fb",
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_end_phase_fields.py",
      "bytes": 10301,
      "sha256": "5305a955f3f5a0f37a3097388b025889584ce2033fe82bcab0140ab8330b31ba"
    },
    "parameters": {
      "original_path": "topics/visible-flex-larger-amplitude/computations/bent-end-phase-design-v1.json",
      "git_blob_sha": "aab93de98359b55bc9327659e8ee4b143e15bc38",
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/computations/bent-end-phase-design-v1.json",
      "bytes": 4374,
      "sha256": "d9a5c7e543b187fc6ce00cad5b0ed1661a74ad6c9054d623b0f51675e708b4bd"
    },
    "r740_source": {
      "original_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r740_rolled_disk_seed.py",
      "git_blob_sha": "72ef28649a33d115ef9a646a581f61dc3f3ddece",
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261126/r740_rolled_disk_seed.py",
      "bytes": 10834,
      "sha256": "b812afa381e2775433710edb9cfa9bd54f0b1b892935c21f2f785675bb4d866f"
    },
    "r742_source": {
      "original_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r742_tilted_disk_two_jets.py",
      "git_blob_sha": "eacaa69d88eae15963aee90d948391abfb9c745a",
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261126/r742_tilted_disk_two_jets.py",
      "bytes": 9706,
      "sha256": "5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd"
    },
    "r744_source": {
      "original_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r744_extruded_closed_two_jets.py",
      "git_blob_sha": "729efd888029dbaf9953617edfde81c0c7394fdd",
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261126/r744_extruded_closed_two_jets.py",
      "bytes": 10327,
      "sha256": "35bb8a1612dd22a8e215a7682ead0c9836b26f3a6c6b525a876fff178a3d6c24"
    },
    "r746_source": {
      "original_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r746_axial_translation_closed_two_jets.py",
      "git_blob_sha": "f17399df53201a251da42198019f1c5a229baa62",
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261126/r746_axial_translation_closed_two_jets.py",
      "bytes": 5465,
      "sha256": "e5ab4d4a0921cb83c7eefc485147883d6dcea92ff9df6f3f3da8604440f174ef"
    },
    "r747_source": {
      "original_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r747_offset_arclength_closed_two_jets.py",
      "git_blob_sha": "b9af0788b2ffea92bd6755d05a43fdb2509007f9",
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261126/r747_offset_arclength_closed_two_jets.py",
      "bytes": 7820,
      "sha256": "09b29cd06eec6887bf8f103f104cdd9ca598b691c3e7503fa2220dbafc71e3ac"
    },
    "geometry_source": {
      "original_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261126/r748_developable_axial_caps.py",
      "git_blob_sha": "5d60e4e2683faa5564072f120280421d32e515bf",
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261126/r748_developable_axial_caps.py",
      "bytes": 1809,
      "sha256": "947245856229ddeb95b83c763403e86bdd867c63b63b6013929d2e2a13a87b46"
    },
    "atlas": {
      "original_path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_body_atlas.py",
      "git_blob_sha": "493b8aeed145723f91c69acd834da0617974b1ac",
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_body_atlas.py",
      "bytes": 7229,
      "sha256": "873bcabafc61a7223736d7806201e289349f838359e59c539f27fafc066ad102"
    }
  },
  "command": [
    "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
    "-u",
    "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_end_phase.py",
    "--params",
    "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/computations/bent-end-phase-design-v1.json",
    "--geometry-source",
    "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/source/topics/visible-flex-larger-amplitude/scripts/resume_20261126/r748_developable_axial_caps.py",
    "--out",
    "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/field"
  ],
  "runner_scope": "public ubuntu-latest 4 vCPU 16 GB",
  "python": "3.12.14 (main, Aug 13 2026, 02:45:55) [GCC 15.2.0]",
  "machine": "x86_64",
  "system": "Linux-7.0.0-1020-azure-x86_64-with-glibc2.43",
  "actual_logical_cpu_count": 4,
  "actual_cpu_affinity": [
    0,
    1,
    2,
    3
  ],
  "setup_python_step": "success",
  "run_started_utc": "2026-11-28T13:14:57Z",
  "phase": "candidate-return",
  "terminal": false,
  "child_started": true,
  "child_pid": 2569,
  "child_returncode": null,
  "latest_observed_scalar_line": {
    "ordinal": 29,
    "utc": "2026-11-28T13:51:12Z",
    "original": {
      "event": "stage",
      "stage": 6,
      "point": "cce19ff7f718dd1f246f5a542ee2686e9a4f595afff8a5de19df9ad311f5c345",
      "score": 161.19993791948852,
      "gram": 6.968190732291204,
      "K": 2087.580156559493,
      "support": -0.5354668776994621
    }
  },
  "scientific_summary": {
    "file": {
      "path": "/home/runner/work/_temp/run40-bent-end-phase-46148644102-1/field/summary.json",
      "bytes": 31190,
      "sha256": "51c043182974b32dd5693c37e8b38fd8384110bcc9c8434d4e0fe31c2dee31d0"
    },
    "complete_small_json": {
      "continuation": "The complete locked coarse field is embedded by name in a strict superset; new central directions vanish only on the actual grip and at the protected positive cap-center first jet.",
      "elapsed_seconds": 2165.3237700669997,
      "numpy": "2.3.5",
      "params_sha256": "d9a5c7e543b187fc6ce00cad5b0ed1661a74ad6c9054d623b0f51675e708b4bd",
      "schema": "direct-finite-axial-flex/v1",
      "scipy": "1.17.0",
      "scope": "Actual finite phase geometry and Gram estimates on complete spatial chart grids and independent time refinements. Continuous exact isometry, tube bounds for corrected fields, and convergence require separate evidence.",
      "selected_coarse_design": {
        "angle": "legacy",
        "bend": 1.5625e-05,
        "central": "locked",
        "fade": [
          1,
          1.095
        ],
        "id": "legacy-developable-boundary",
        "mode": "dev"
      },
      "selected_design": {
        "angle": "legacy",
        "bend": 1.5625e-05,
        "central": "expanded",
        "fade": [
          1,
          1.095
        ],
        "id": "legacy-developable-boundary-expanded",
        "mode": "dev"
      },
      "source_sha256": "0b2ce5d260bdc4160b972d7b36cc0567660c6bbc18d56eb722265e6f0b04b701",
      "sources": {
        "bent_body_atlas.py": "873bcabafc61a7223736d7806201e289349f838359e59c539f27fafc066ad102",
        "bent_end_phase_fields.py": "5305a955f3f5a0f37a3097388b025889584ce2033fe82bcab0140ab8330b31ba",
        "r740_rolled_disk_seed.py": "b812afa381e2775433710edb9cfa9bd54f0b1b892935c21f2f785675bb4d866f",
        "r742_tilted_disk_two_jets.py": "5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd",
        "r744_extruded_closed_two_jets.py": "35bb8a1612dd22a8e215a7682ead0c9836b26f3a6c6b525a876fff178a3d6c24",
        "r746_axial_translation_closed_two_jets.py": "e5ab4d4a0921cb83c7eefc485147883d6dcea92ff9df6f3f3da8604440f174ef",
        "r747_offset_arclength_closed_two_jets.py": "09b29cd06eec6887bf8f103f104cdd9ca598b691c3e7503fa2220dbafc71e3ac",
        "r748_developable_axial_caps.py": "947245856229ddeb95b83c763403e86bdd867c63b63b6013929d2e2a13a87b46"
      },
      "stages": [
        {
          "all_time_check": {
            "K": {
              "chart": "end-",
              "index": 10953,
              "phase": 1.5707963267948966,
              "u": 5.2987508541658,
              "v": 0.1141193550663743,
              "value": 38287.37226017895
            },
            "area_min": {
              "chart": "cap-",
              "index": 16351,
              "phase": 1.5707963267948966,
              "u": 2.2571193300256,
              "v": 0.007,
              "value": 3.9475925928472435e-05
            },
            "gram": {
              "chart": "cylinder",
              "index": 1866,
              "phase": 1.5707963267948966,
              "u": 2.4611193300256,
              "v": -0.71,
              "value": 9.135032045701506
            },
            "max_physical_correction": {
              "chart": "end+",
              "index": 7964,
              "phase": 1.5707963267948966,
              "u": 6.7188651784632,
              "v": 0.1505792129150562,
              "value": 0.4922123839079797
            },
            "support": {
              "chart": "end+",
              "index": 6900,
              "phase": 1.5707963267948966,
              "u": 4.3673961049922,
              "v": 0.053352925318571165,
              "value": -1.0637522960275003
            }
          },
          "check_phase_columns": [
            "phase",
            "max_gram",
            "rms_gram",
            "max_abs_principal",
            "min_support"
          ],
          "check_phases": [
            [
              0.0,
              0.0,
              0.0,
              9.259259259259263,
              0.1337907860455484
            ],
            [
              0.39269908169872414,
              3.2372415688022493,
              0.28594939703555106,
              225.12146226611205,
              -0.6072579367293994
            ],
            [
              0.7853981633974483,
              3.3399830288100407,
              0.500051726961044,
              792.3667214796465,
              -0.7792403205370103
            ],
            [
              1.1780972450961724,
              6.488063544251405,
              0.7869682528570578,
              1766.7596925671508,
              -0.7464263217172468
            ],
            [
              1.5707963267948966,
              9.135032045701506,
              1.2690608572722641,
              38287.37226017895,
              -1.0637522960275003
            ]
          ],
          "coefficient_count_per_phase": 282,
          "configuration": {
            "cap_degree": 3,
            "check": [
              69,
              21,
              15,
              13
            ],
            "degree": 3,
            "extra_check": false,
            "id": "all-five-coarse",
            "inner": 85,
            "intervals": 2,
            "max_nfev": 52,
            "mesh": [
              27,
              11,
              8,
              7
            ],
            "regularizer": 7e-06,
            "roll_modes": 3,
            "roll_spans": 3
          },
          "design": {
            "angle": "legacy",
            "central": "free",
            "id": "legacy-named-free",
            "mode": "named"
          },
          "knots": [
            {
              "adjoint_abs": 3.122502256758253e-17,
              "cost": 3.6211203395398366,
              "directional_fd_relative": 7.956282142767494e-08,
              "index": 1,
              "nfev": 52,
              "njev": 51,
              "optimality": 0.15914127463995642,
              "phase": 0.7853981633974483,
              "point_sha256": "5f9b87be6b64f944085499a23a82266b2c6dee14380c5a7aca88ad32370983d7",
              "status": 0,
              "train_gram": 4.253636251331377
            },
            {
              "adjoint_abs": 1.0547118733938987e-15,
              "cost": 14.701530140912448,
              "directional_fd_relative": 3.2860670326312976e-07,
              "index": 2,
              "nfev": 48,
              "njev": 32,
              "optimality": 3188.8712610107195,
              "phase": 1.5707963267948966,
              "point_sha256": "7c17987aee5feb6a01cc5e0b10783d94a773bd7d7d3e3731ef44053836c6defd",
              "status": 3,
              "train_gram": 7.292437548482917
            }
          ],
          "npz_bytes": 7314,
          "npz_sha256": "bfd806a1b11f8ff5f6565366def6d3578d27b02b204201706099adef96a801df",
          "point_sha256": "6fb78b46b0983a07d5183a821ebaf3c2dd691f94a4c40bbec8969d706d9cd2c9",
          "previous_point_sha256": null,
          "score": 2818.339538370984,
          "shape": [
            3,
            282
          ],
          "stage": 0,
          "time_data_sha256": "0d7d31e13447bbb5b53f61053604003afd523dffb09d2a496ecca66fd551327a",
          "worst_gram_by_chart": {
            "cap+": [
              0.7892879709902884,
              1.5707963267948966,
              6.1102447537643,
              1.0
            ],
            "cap-": [
              0.7951881489137689,
              1.5707963267948966,
              6.1102447537643,
              1.0
            ],
            "cap-cartesian+": [
              0.00016194905934593153,
              1.5707963267948966,
              0.59502,
              0.0
            ],
            "cap-cartesian-": [
              0.5852535863223274,
              1.5707963267948966,
              0.59502,
              0.0
            ],
            "cylinder": [
              9.135032045701506,
              1.5707963267948966,
              2.4611193300256,
              -0.71
            ],
            "end+": [
              8.606326148710597,
              1.5707963267948966,
              5.3130155540114,
              0.08981278316725305
            ],
            "end-": [
              8.318046552625189,
              1.5707963267948966,
              1.7484650434224,
              0.1141193550663743
            ]
          },
          "zero_phase_sixjet_difference": 0.0
        },
        {
          "all_time_check": {
            "K": {
              "chart": "cap+",
              "index": 12003,
              "phase": 1.1780972450961724,
              "u": 0.2161193300256,
              "v": 0.4691666666666666,
              "value": 1083052464.4066625
            },
            "area_min": {
              "chart": "cap+",
              "index": 12003,
              "phase": 1.1780972450961724,
              "u": 0.2161193300256,
              "v": 0.4691666666666666,
              "value": 2.339053169327759e-06
            },
            "gram": {
              "chart": "cap+",
              "index": 12866,
              "phase": 1.5707963267948966,
              "u": 2.2561193300256,
              "v": 0.75,
              "value": 1929.8482581349583
            },
            "max_physical_correction": {
              "chart": "end-",
              "index": 10395,
              "phase": 1.5707963267948966,
              "u": 4.4630155540114,
              "v": 0.016893067469889275,
              "value": 0.2025082879502671
            },
            "support": {
              "chart": "cap-",
              "index": 17441,
              "phase": 1.1780972450961724,
              "u": 4.5930155540114,
              "v": 0.7191666666666667,
              "value": -1.1060737573720687
            }
          },
          "check_phase_columns": [
            "phase",
            "max_gram",
            "rms_gram",
            "max_abs_principal",
            "min_support"
          ],
          "check_phases": [
            [
              0.0,
              0.0,
              0.0,
              9.259259259259263,
              0.1337907860455484
            ],
            [
              0.39269908169872414,
              161.1832216740281,
              10.641073929580056,
              85.63562262266052,
              0.008142370924729692
            ],
            [
              0.7853981633974483,
              580.3678383232889,
              38.23211818053282,
              15255.553793185674,
              -1.1060249905378543
            ],
            [
              1.1780972450961724,
              1202.3576342481977,
              78.87137757648003,
              1083052464.4066625,
              -1.1060737573720687
            ],
            [
              1.5707963267948966,
              1929.8482581349583,
              126.83136868840221,
              84884.89475425522,
              -1.105409606923716
            ]
          ],
          "coefficient_count_per_phase": 282,
          "configuration": {
            "cap_degree": 3,
            "check": [
              69,
              21,
              15,
              13
            ],
            "degree": 3,
            "extra_check": false,
            "id": "all-five-coarse",
            "inner": 85,
            "intervals": 2,
            "max_nfev": 52,
            "mesh": [
              27,
              11,
              8,
              7
            ],
            "regularizer": 7e-06,
            "roll_modes": 3,
            "roll_spans": 3
          },
          "design": {
            "angle": "arc",
            "central": "free",
            "id": "offset-cap-only-free",
            "mode": "cap-only"
          },
          "knots": [
            {
              "adjoint_abs": 3.469446951953614e-18,
              "cost": 39.73035058308027,
              "directional_fd_relative": 1.4460687258060896e-07,
              "index": 1,
              "nfev": 52,
              "njev": 29,
              "optimality": 54.111464497309655,
              "phase": 0.7853981633974483,
              "point_sha256": "1bdac09dd29ddb33fc29e78e5ca80a5baafca8e21e8d44f17d174eaa554e07ba",
              "status": 0,
              "train_gram": 580.3678383232889
            },
            {
              "adjoint_abs": 8.440110832452774e-10,
              "cost": 76.94240560181426,
              "directional_fd_relative": 1.4361632813928988e-05,
              "index": 2,
              "nfev": 25,
              "njev": 14,
              "optimality": 21686.32008732866,
              "phase": 1.5707963267948966,
              "point_sha256": "0ec40860803ec1b847bf933a8544d7756767a76291eadd43f5a64c17a0c1338d",
              "status": 3,
              "train_gram": 1929.8482581349583
            }
          ],
          "npz_bytes": 7314,
          "npz_sha256": "92e400d02fa152c1745ee645874e4d825151d87b8b244ff39c4c0ff71bca5da7",
          "point_sha256": "d71c994767568f85358266a339eb1d9ceec0621e0ef3468bc0292c9a99774ee8",
          "previous_point_sha256": null,
          "score": 79387977.28696251,
          "shape": [
            3,
            282
          ],
          "stage": 1,
          "time_data_sha256": "0d7d31e13447bbb5b53f61053604003afd523dffb09d2a496ecca66fd551327a",
          "worst_gram_by_chart": {
            "cap+": [
              1929.8482581349583,
              1.5707963267948966,
              2.2561193300256,
              0.75
            ],
            "cap-": [
              1929.7672329356833,
              1.5707963267948966,
              2.2561193300256,
              0.99925
            ],
            "cap-cartesian+": [
              0.0005154852943042124,
              1.5707963267948966,
              0.59502,
              0.0
            ],
            "cap-cartesian-": [
              0.359513280458188,
              1.5707963267948966,
              0.59502,
              0.0
            ],
            "cylinder": [
              4.062795504092159,
              1.1780972450961724,
              2.4585222055711,
              0.71
            ],
            "end+": [
              4.0239445566045,
              1.5707963267948966,
              5.3130155540114,
              0.16273249886461683
            ],
            "end-": [
              3.834628295461223,
              1.5707963267948966,
              1.5886193300256,
              0.16273249886461683
            ]
          },
          "zero_phase_sixjet_difference": 0.0
        },
        {
          "all_time_check": {
            "K": {
              "chart": "end+",
              "index": 6243,
              "phase": 1.5707963267948966,
              "u": 2.5261193300256,
              "v": 0.08981278316725305,
              "value": 46110.550178704965
            },
            "area_min": {
              "chart": "cap-",
              "index": 16351,
              "phase": 1.5707963267948966,
              "u": 2.2571193300256,
              "v": 0.007,
              "value": 3.9496613638049956e-05
            },
            "gram": {
              "chart": "cylinder",
              "index": 1866,
              "phase": 1.5707963267948966,
              "u": 2.4611193300256,
              "v": -0.71,
              "value": 9.323266658414182
            },
            "max_physical_correction": {
              "chart": "end+",
              "index": 7964,
              "phase": 1.5707963267948966,
              "u": 6.7188651784632,
              "v": 0.1505792129150562,
              "value": 0.48843106408595266
            },
            "support": {
              "chart": "end+",
              "index": 6900,
              "phase": 1.5707963267948966,
              "u": 4.3673961049922,
              "v": 0.053352925318571165,
              "value": -1.1056477807957394
            }
          },
          "check_phase_columns": [
            "phase",
            "max_gram",
            "rms_gram",
            "max_abs_principal",
            "min_support"
          ],
          "check_phases": [
            [
              0.0,
              0.0,
              0.0,
              9.259259259259263,
              0.1337907860455484
            ],
            [
              0.39269908169872414,
              3.237110264907294,
              0.2856113730378569,
              219.29214757539327,
              -0.6063196811993656
            ],
            [
              0.7853981633974483,
              3.338647664914078,
              0.49991140671456186,
              782.0147702658692,
              -0.7770620704356654
            ],
            [
              1.1780972450961724,
              6.621219053975288,
              0.7878408696628428,
              1686.588906891422,
              -0.7444874579018494
            ],
            [
              1.5707963267948966,
              9.323266658414182,
              1.2713582942475334,
              46110.550178704965,
              -1.1056477807957394
            ]
          ],
          "coefficient_count_per_phase": 282,
          "configuration": {
            "cap_degree": 3,
            "check": [
              69,
              21,
              15,
              13
            ],
            "degree": 3,
            "extra_check": false,
            "id": "all-five-coarse",
            "inner": 85,
            "intervals": 2,
            "max_nfev": 52,
            "mesh": [
              27,
              11,
              8,
              7
            ],
            "regularizer": 7e-06,
            "roll_modes": 3,
            "roll_spans": 3
          },
          "design": {
            "angle": "legacy",
            "bend": 0.000244140625,
            "central": "free",
            "fade": [
              0.71,
              1.09
            ],
            "id": "legacy-developable-full",
            "mode": "dev"
          },
          "knots": [
            {
              "adjoint_abs": 2.42861286636753e-17,
              "cost": 3.6270742590565574,
              "directional_fd_relative": 9.155819100176197e-08,
              "index": 1,
              "nfev": 52,
              "njev": 51,
              "optimality": 0.15842217563742678,
              "phase": 0.7853981633974483,
              "point_sha256": "1a85b53e3cfdbd2223c29c4af30a6be1665f5d9feedacc75c7786f3a29ddedab",
              "status": 0,
              "train_gram": 4.251201828623754
            },
            {
              "adjoint_abs": 1.9984014443252818e-15,
              "cost": 14.496030090633404,
              "directional_fd_relative": 5.046660136569319e-07,
              "index": 2,
              "nfev": 40,
              "njev": 18,
              "optimality": 2008.6727821850507,
              "phase": 1.5707963267948966,
              "point_sha256": "865595dce532ba732e6a87b7859a56e22a004f859460bf846b63491799c2fe7e",
              "status": 3,
              "train_gram": 7.338552661981355
            }
          ],
          "npz_bytes": 7314,
          "npz_sha256": "a0adb5943788627844c8756a99a5dbcff5c7000148f60f7f5c202eb8c5176b5b",
          "point_sha256": "1db01286038f88882d8cad076296d8d956cf34ff851ea53b0eac4761b4124ff3",
          "previous_point_sha256": null,
          "score": 3392.08011315195,
          "shape": [
            3,
            282
          ],
          "stage": 2,
          "time_data_sha256": "0d7d31e13447bbb5b53f61053604003afd523dffb09d2a496ecca66fd551327a",
          "worst_gram_by_chart": {
            "cap+": [
              0.7876892820470967,
              1.5707963267948966,
              6.1102447537643,
              1.0
            ],
            "cap-": [
              0.79353958365571,
              1.5707963267948966,
              6.1102447537643,
              1.0
            ],
            "cap-cartesian+": [
              0.0001714665095411603,
              1.5707963267948966,
              0.59502,
              0.0
            ],
            "cap-cartesian-": [
              0.5846653819096719,
              1.5707963267948966,
              0.59502,
              0.0
            ],
            "cylinder": [
              9.323266658414182,
              1.5707963267948966,
              2.4611193300256,
              -0.71
            ],
            "end+": [
              8.643047568734556,
              1.5707963267948966,
              5.3130155540114,
              0.08981278316725305
            ],
            "end-": [
              8.297407401080232,
              1.5707963267948966,
              1.6861193300256,
              0.1141193550663743
            ]
          },
          "zero_phase_sixjet_difference": 0.0
        },
        {
          "all_time_check": {
            "K": {
              "chart": "cap+",
              "index": 11831,
              "phase": 1.5707963267948966,
              "u": 0.0194998810064,
              "v": 0.7191666666666667,
              "value": 12396225.856801046
            },
            "area_min": {
              "chart": "cap-",
              "index": 15462,
              "phase": 1.5707963267948966,
              "u": 0.2161193300256,
              "v": 0.75,
              "value": 2.4392843449458474e-06
            },
            "gram": {
              "chart": "cap-",
              "index": 16324,
              "phase": 1.5707963267948966,
              "u": 2.2561193300256,
              "v": 0.99925,
              "value": 1930.5321968221297
            },
            "max_physical_correction": {
              "chart": "end-",
              "index": 10376,
              "phase": 1.5707963267948966,
              "u": 4.3858202171175,
              "v": 0.053352925318571165,
              "value": 0.19130205799890357
            },
            "support": {
              "chart": "cap-",
              "index": 17462,
              "phase": 0.7853981633974483,
              "u": 4.6480155540114,
              "v": 0.6358333333333333,
              "value": -1.1066882613176303
            }
          },
          "check_phase_columns": [
            "phase",
            "max_gram",
            "rms_gram",
            "max_abs_principal",
            "min_support"
          ],
          "check_phases": [
            [
              0.0,
              0.0,
              0.0,
              9.259259259259263,
              0.1337907860455484
            ],
            [
              0.39269908169872414,
              161.2509063399328,
              10.64720475695789,
              82.5343636744709,
              0.01611780611354653
            ],
            [
              0.7853981633974483,
              580.6373607641478,
              38.25369796081848,
              4716.838489704892,
              -1.1066882613176303
            ],
            [
              1.1780972450961724,
              1202.9016075838572,
              78.9107088181844,
              265702.60801807855,
              -1.1066444388136858
            ],
            [
              1.5707963267948966,
              1930.5321968221297,
              126.88567334871135,
              12396225.856801046,
              -1.1060588298821643
            ]
          ],
          "coefficient_count_per_phase": 282,
          "configuration": {
            "cap_degree": 3,
            "check": [
              69,
              21,
              15,
              13
            ],
            "degree": 3,
            "extra_check": false,
            "id": "all-five-coarse",
            "inner": 85,
            "intervals": 2,
            "max_nfev": 52,
            "mesh": [
              27,
              11,
              8,
              7
            ],
            "regularizer": 7e-06,
            "roll_modes": 3,
            "roll_spans": 3
          },
          "design": {
            "angle": "arc",
            "bend": 0.000244140625,
            "central": "free",
            "fade": [
              0.71,
              1.09
            ],
            "id": "offset-developable-full",
            "mode": "dev"
          },
          "knots": [
            {
              "adjoint_abs": 3.469446951953614e-17,
              "cost": 39.89072399578232,
              "directional_fd_relative": 1.7193429042843205e-07,
              "index": 1,
              "nfev": 48,
              "njev": 27,
              "optimality": 243.2489522560362,
              "phase": 0.7853981633974483,
              "point_sha256": "eb13e236ba1624f26c029560ab3b60a65b54033f035397913b8930f7384e2d64",
              "status": 3,
              "train_gram": 580.6373607641478
            },
            {
              "adjoint_abs": 3.841705620288849e-09,
              "cost": 1151481.1262056818,
              "directional_fd_relative": 0.0004532304886131802,
              "index": 2,
              "nfev": 35,
              "njev": 18,
              "optimality": 97995919539.25829,
              "phase": 1.5707963267948966,
              "point_sha256": "a707aa4bb0994c2c5d39aa482e8dc6ecbe501b9b564116fe83c7abced91136aa",
              "status": 3,
              "train_gram": 1930.5321968221294
            }
          ],
          "npz_bytes": 7314,
          "npz_sha256": "f64467182ebc3c52f2613bcc13f20460e788192b920abf165bea146727348ba9",
          "point_sha256": "571417a538a7499221b183a675f34dfe93b5070a5212f6a02f154c821362cd67",
          "previous_point_sha256": null,
          "score": 910557.3460533055,
          "shape": [
            3,
            282
          ],
          "stage": 3,
          "time_data_sha256": "0d7d31e13447bbb5b53f61053604003afd523dffb09d2a496ecca66fd551327a",
          "worst_gram_by_chart": {
            "cap+": [
              1930.4435467184853,
              1.5707963267948966,
              2.2561193300256,
              0.75
            ],
            "cap-": [
              1930.5321968221297,
              1.5707963267948966,
              2.2561193300256,
              0.99925
            ],
            "cap-cartesian+": [
              0.000569491852623306,
              1.5707963267948966,
              0.59498,
              0.0
            ],
            "cap-cartesian-": [
              0.34226111000037124,
              1.5707963267948966,
              0.59502,
              0.0
            ],
            "cylinder": [
              3.7597658169976067,
              1.1780972450961724,
              2.4585222055711,
              0.71
            ],
            "end+": [
              4.056111268782219,
              1.5707963267948966,
              5.3130155540114,
              0.16273249886461683
            ],
            "end-": [
              3.879354805597012,
              1.5707963267948966,
              1.5886193300256,
              0.16273249886461683
            ]
          },
          "zero_phase_sixjet_difference": 0.0
        },
        {
          "all_time_check": {
            "K": {
              "chart": "end+",
              "index": 5234,
              "phase": 1.5707963267948966,
              "u": 0.2556193300256,
              "v": 0.12627264101593494,
              "value": 2885.3296246505834
            },
            "area_min": {
              "chart": "cap-",
              "index": 16351,
              "phase": 1.5707963267948966,
              "u": 2.2571193300256,
              "v": 0.007,
              "value": 5.2462021116184004e-05
            },
            "gram": {
              "chart": "end-",
              "index": 11144,
              "phase": 1.5707963267948966,
              "u": 5.7044978039651,
              "v": 0.029046353419449902,
              "value": 9.132224342164221
            },
            "max_physical_correction": {
              "chart": "end-",
              "index": 11190,
              "phase": 1.5707963267948966,
              "u": 5.8059345414149,
              "v": 0.053352925318571165,
              "value": 0.08580077035075574
            },
            "support": {
              "chart": "end-",
              "index": 10879,
              "phase": 1.5707963267948966,
              "u": 5.197314116716,
              "v": 0.016893067469889275,
              "value": -0.35860838965003805
            }
          },
          "check_phase_columns": [
            "phase",
            "max_gram",
            "rms_gram",
            "max_abs_principal",
            "min_support"
          ],
          "check_phases": [
            [
              0.0,
              0.0,
              0.0,
              9.259259259259263,
              0.1337907860455484
            ],
            [
              0.39269908169872414,
              3.190003854800583,
              0.22200589736109988,
              217.87044569769793,
              0.13379078604554842
            ],
            [
              0.7853981633974483,
              3.240271386586657,
              0.43855626835150413,
              812.680754913987,
              0.01049297067593516
            ],
            [
              1.1780972450961724,
              4.882069092628411,
              0.8010530757100967,
              2224.7204493232407,
              -0.297817401240744
            ],
            [
              1.5707963267948966,
              9.132224342164221,
              1.358798375508955,
              2885.3296246505834,
              -0.35860838965003805
            ]
          ],
          "coefficient_count_per_phase": 282,
          "configuration": {
            "cap_degree": 3,
            "check": [
              69,
              21,
              15,
              13
            ],
            "degree": 3,
            "extra_check": false,
            "id": "all-five-coarse",
            "inner": 85,
            "intervals": 2,
            "max_nfev": 52,
            "mesh": [
              27,
              11,
              8,
              7
            ],
            "regularizer": 7e-06,
            "roll_modes": 3,
            "roll_spans": 3
          },
          "design": {
            "angle": "legacy",
            "bend": 1.5625e-05,
            "central": "locked",
            "fade": [
              1,
              1.095
            ],
            "id": "legacy-developable-boundary",
            "mode": "dev"
          },
          "knots": [
            {
              "adjoint_abs": 1.734723475976807e-16,
              "cost": 4.393043215167217,
              "directional_fd_relative": 3.098239158223887e-08,
              "index": 1,
              "nfev": 52,
              "njev": 35,
              "optimality": 1.8470148860063569,
              "phase": 0.7853981633974483,
              "point_sha256": "e83c9178caf62169ece9baacbbb78af7cb499db53c4d5846aab201a4f4df985d",
              "status": 0,
              "train_gram": 4.161199149498904
            },
            {
              "adjoint_abs": 1.7763568394002505e-15,
              "cost": 19.5131418801288,
              "directional_fd_relative": 2.154989927879751e-07,
              "index": 2,
              "nfev": 52,
              "njev": 35,
              "optimality": 9.977058594655736,
              "phase": 1.5707963267948966,
              "point_sha256": "ce33cdf00260ad1e1916690ab405d8aa1afdbe52d1e3f98f8964d1a353f3f4a1",
              "status": 0,
              "train_gram": 9.210829597176238
            }
          ],
          "npz_bytes": 7314,
          "npz_sha256": "11590459abb470cb23156ed12706f3886c05e8d11824753e1f12ffe6b0997e28",
          "point_sha256": "2d25884b0f8cc8aecabba4c48e8bfef96b59a52ac0e94493f609e2dc783d1c8b",
          "previous_point_sha256": null,
          "score": 221.30717906665444,
          "shape": [
            3,
            282
          ],
          "stage": 4,
          "time_data_sha256": "0d7d31e13447bbb5b53f61053604003afd523dffb09d2a496ecca66fd551327a",
          "worst_gram_by_chart": {
            "cap+": [
              0.32964098763151445,
              1.5707963267948966,
              2.6317387790448,
              1.0
            ],
            "cap-": [
              0.34682147323017065,
              1.5707963267948966,
              2.6317387790448,
              1.0
            ],
            "cap-cartesian+": [
              0.00023271848338264948,
              1.1780972450961724,
              0.59498,
              0.0
            ],
            "cap-cartesian-": [
              0.09525945241480734,
              1.5707963267948966,
              0.59502,
              0.0
            ],
            "cylinder": [
              3.33066907387547e-16,
              1.1780972450961724,
              2.4611193300256,
              -1.0
            ],
            "end+": [
              9.070007479422928,
              1.5707963267948966,
              5.7044978039651,
              0.029046353419449902
            ],
            "end-": [
              9.132224342164221,
              1.5707963267948966,
              5.7044978039651,
              0.029046353419449902
            ]
          },
          "zero_phase_sixjet_difference": 0.0
        },
        {
          "all_time_check": {
            "K": {
              "chart": "end-",
              "index": 11450,
              "phase": 1.5707963267948966,
              "u": 2.7278582280641,
              "v": 0.06795206006548088,
              "value": 2815.8379714384128
            },
            "area_min": {
              "chart": "cap-",
              "index": 20343,
              "phase": 1.2610843256788589,
              "u": 4.7420155540114,
              "v": 0.007,
              "value": 4.414838484227801e-05
            },
            "gram": {
              "chart": "end+",
              "index": 8788,
              "phase": 1.5707963267948966,
              "u": 5.2936184187229,
              "v": 0.08922031047721199,
              "value": 8.040081916241995
            },
            "max_physical_correction": {
              "chart": "end+",
              "index": 8190,
              "phase": 1.3744467859455345,
              "u": 4.4730155540114,
              "v": 0.11048856088894307,
              "value": 0.21504341725604365
            },
            "support": {
              "chart": "end+",
              "index": 8781,
              "phase": 0.8683852439801347,
              "u": 5.2936184187229,
              "v": 0.014781434036153117,
              "value": -0.1488750228236189
            }
          },
          "check_phase_columns": [
            "phase",
            "max_gram",
            "rms_gram",
            "max_abs_principal",
            "min_support"
          ],
          "check_phases": [
            [
              0.0,
              0.0,
              0.0,
              9.259259259259263,
              0.1337907860455484
            ],
            [
              0.08298708058268649,
              1.7515107091417224,
              0.08426305202567809,
              67.52109026771892,
              0.1242254846211151
            ],
            [
              0.19634954084936207,
              2.4109434763868745,
              0.13157609333545695,
              141.79391200250078,
              0.0834407674977574
            ],
            [
              0.3097120011160377,
              3.06481613571078,
              0.18331544148671383,
              200.18976440672293,
              0.0377131852862278
            ],
            [
              0.39269908169872414,
              3.5195501689552726,
              0.21707762991323895,
              260.0691664863094,
              0.005966063845488879
            ],
            [
              0.47568616228141064,
              3.550199444768925,
              0.24909119036007035,
              326.46059586622397,
              -0.024121484138059365
            ],
            [
              0.5890486225480862,
              3.6079567355379014,
              0.2964906252847698,
              424.9123059852303,
              -0.04159842746878618
            ],
            [
              0.7024110828147618,
              3.658134288061147,
              0.3462022214047702,
              581.8192213342309,
              0.016811534176925477
            ],
            [
              0.7853981633974483,
              3.6716714943520823,
              0.38375995548503117,
              929.652784535662,
              -0.025248819497387054
            ],
            [
              0.8683852439801347,
              3.7158386379714994,
              0.42480168855276823,
              1385.691138000866,
              -0.1488750228236189
            ],
            [
              0.9817477042468103,
              4.841378916202617,
              0.49305998983666477,
              2029.9759711798042,
              -0.14562544634914504
            ],
            [
              1.095110164513486,
              5.771828185346029,
              0.5721446982206241,
              2459.8416935186087,
              -0.08766922286540502
            ],
            [
              1.1780972450961724,
              6.290514664709246,
              0.6336824828996553,
              2613.118743395142,
              -0.05632931983363951
            ],
            [
              1.2610843256788589,
              6.273969642055596,
              0.6954373783930273,
              2707.4317381320852,
              -0.03252187150938679
            ],
            [
              1.3744467859455345,
              6.422299307055351,
              0.7893809825709642,
              2743.812904273668,
              -0.0585963744628705
            ],
            [
              1.4878092462122101,
              7.1417577123238765,
              0.9080884799745538,
              2784.267101327785,
              -0.0714077090899829
            ],
            [
              1.5707963267948966,
              8.040081916241995,
              1.0131945578871466,
              2815.8379714384128,
              -0.08228669851947698
            ]
          ],
          "coefficient_count_per_phase": 714,
          "configuration": {
            "cap_degree": 4,
            "check": [
              77,
              25,
              17,
              15
            ],
            "degree": 4,
            "extra_check": true,
            "id": "fixed-target-space-time-1",
            "inner": 95,
            "intervals": 4,
            "max_nfev": 60,
            "mesh": [
              35,
              13,
              10,
              9
            ],
            "previous_roll_spaces": [
              [
                3,
                3
              ]
            ],
            "regularizer": 4e-06,
            "roll_modes": 5,
            "roll_spans": 4
          },
          "design": {
            "angle": "legacy",
            "bend": 1.5625e-05,
            "central": "expanded",
            "fade": [
              1,
              1.095
            ],
            "id": "legacy-developable-boundary-expanded",
            "mode": "dev"
          },
          "knots": [
            {
              "adjoint_abs": 7.771561172376096e-16,
              "cost": 0.4050446255729659,
              "directional_fd_relative": 7.785167521719847e-09,
              "index": 1,
              "nfev": 60,
              "njev": 53,
              "optimality": 0.4619274473310346,
              "phase": 0.39269908169872414,
              "point_sha256": "6bf0034c00777d65702d89c0c65e3cfcbc6a1cc9fed6abf3b89a8e8cb81bd764",
              "status": 0,
              "train_gram": 2.403039686508978
            },
            {
              "adjoint_abs": 5.684341886080802e-14,
              "cost": 1.4152069789662516,
              "directional_fd_relative": 4.7394893193059405e-09,
              "index": 2,
              "nfev": 60,
              "njev": 54,
              "optimality": 1.202473497711384,
              "phase": 0.7853981633974483,
              "point_sha256": "e6db6719fb787ac1668e44e0098a40acdd298272bc30b2f954723249886658ca",
              "status": 0,
              "train_gram": 2.5117046832823036
            },
            {
              "adjoint_abs": 8.185452315956354e-12,
              "cost": 4.808272481184064,
              "directional_fd_relative": 1.0778004123072802e-08,
              "index": 3,
              "nfev": 60,
              "njev": 44,
              "optimality": 2.4016469863964716,
              "phase": 1.1780972450961724,
              "point_sha256": "05eda9bb973d6ab848ead1a543c98d1de60d459e7d4508b5ef66cc5aa7e7791a",
              "status": 0,
              "train_gram": 4.085552115525054
            },
            {
              "adjoint_abs": 1.509903313490213e-14,
              "cost": 11.469103406385978,
              "directional_fd_relative": 1.3423497406461598e-07,
              "index": 4,
              "nfev": 41,
              "njev": 24,
              "optimality": 21.82001987813675,
              "phase": 1.5707963267948966,
              "point_sha256": "2df5dae9b1b68f223adf2afd341adb20567e19d57065b42e01312edad69aa67e",
              "status": 3,
              "train_gram": 7.778115427168751
            }
          ],
          "npz_bytes": 29122,
          "npz_sha256": "bbbeee782bf4770c90137412370ebd0a9d16e7886b958eb303b4bab71ebdc294",
          "point_sha256": "ba153412e990b9237ebf450d298cd8628ca1c2d45a65b35376ae146010ec1577",
          "previous_point_sha256": "2d25884b0f8cc8aecabba4c48e8bfef96b59a52ac0e94493f609e2dc783d1c8b",
          "score": 214.4922075089944,
          "shape": [
            5,
            714
          ],
          "stage": 5,
          "time_data_sha256": "0552a4c74e53e15ed02fa563f63e5f2fbd13654901124cb163447ff6c6cb2418",
          "worst_gram_by_chart": {
            "cap+": [
              0.4549523368352425,
              1.5707963267948966,
              4.5664355736282,
              1.0
            ],
            "cap-": [
              0.4654076929835843,
              1.3744467859455345,
              4.6480155540114,
              1.0
            ],
            "cap-cartesian+": [
              0.00013974172622234412,
              1.5707963267948966,
              0.59498,
              0.0
            ],
            "cap-cartesian-": [
              0.25991748527137304,
              1.3744467859455345,
              0.59498,
              0.0
            ],
            "cylinder": [
              6.290514664709246,
              1.1780972450961724,
              2.4611193300256,
              0.71
            ],
            "end+": [
              8.040081916241995,
              1.5707963267948966,
              5.2936184187229,
              0.08922031047721199
            ],
            "end-": [
              7.945833493944934,
              1.5707963267948966,
              5.2936184187229,
              0.08922031047721199
            ]
          },
          "zero_phase_sixjet_difference": 0.0
        },
        {
          "all_time_check": {
            "K": {
              "chart": "end+",
              "index": 8711,
              "phase": 1.5707963267948966,
              "u": 0.2556193300256,
              "v": 0.14794194986400155,
              "value": 2087.580156559493
            },
            "area_min": {
              "chart": "cap-",
              "index": 27897,
              "phase": 1.4159403262368777,
              "u": 4.7420155540114,
              "v": 0.007,
              "value": 4.611619177618771e-05
            },
            "gram": {
              "chart": "end+",
              "index": 12422,
              "phase": 1.5707963267948966,
              "u": 5.4430155540114,
              "v": 0.037347047722999814,
              "value": 6.968190732291204
            },
            "max_physical_correction": {
              "chart": "end-",
              "index": 15679,
              "phase": 1.5293027865035533,
              "u": 2.530357142494,
              "v": 0.11391274920523178,
              "value": 0.21348555534454022
            },
            "support": {
              "chart": "end+",
              "index": 11188,
              "phase": 1.2195907853875156,
              "u": 4.0932707573761,
              "v": 0.020332447393614932,
              "value": -0.5354668776994621
            }
          },
          "check_phase_columns": [
            "phase",
            "max_gram",
            "rms_gram",
            "max_abs_principal",
            "min_support"
          ],
          "check_phases": [
            [
              0.0,
              0.0,
              0.0,
              9.259259259259265,
              0.1337907860455484
            ],
            [
              0.041493540291343244,
              1.3672440792836333,
              0.059798971216817196,
              71.95468748786689,
              0.12368724783537657
            ],
            [
              0.09817477042468103,
              2.0306348249992063,
              0.08815464734586148,
              153.92669568009572,
              0.1103782479475458
            ],
            [
              0.15485600055801885,
              2.093947365314666,
              0.10974409099585042,
              217.37934803934672,
              0.09860060279880888
            ],
            [
              0.19634954084936207,
              2.099172431026981,
              0.12530748656565482,
              244.13868302963309,
              0.0917877430452572
            ],
            [
              0.23784308114070532,
              2.6275502520697476,
              0.13872212772218734,
              254.01432518128937,
              0.0866391929086822
            ],
            [
              0.2945243112740431,
              2.752583715058248,
              0.1535580501701793,
              249.8849342644476,
              0.07274162812255228
            ],
            [
              0.3512055414073809,
              2.7651971490199267,
              0.1681077084968519,
              263.8504473883956,
              0.05131736845273941
            ],
            [
              0.39269908169872414,
              2.791701590958847,
              0.1795331426442415,
              294.4137249389386,
              0.03473977089817704
            ],
            [
              0.43419262199006736,
              2.8285873887284665,
              0.19227061556960717,
              339.85206039220736,
              0.020696373341254078
            ],
            [
              0.4908738521234052,
              2.8876691571848587,
              0.21157624216306423,
              416.71534125513404,
              0.033486784745971145
            ],
            [
              0.547555082256743,
              2.9458814186660796,
              0.23361362338963237,
              513.3164034286629,
              0.02342197289484524
            ],
            [
              0.5890486225480862,
              2.980767526488468,
              0.2501834478582108,
              592.0798296899287,
              0.01580614157102815
            ],
            [
              0.6305421628394294,
              3.3538512910774774,
              0.26627477835662616,
              666.902305517621,
              0.012741303266026807
            ],
            [
              0.6872233929727672,
              3.8148269278600053,
              0.2877751371711263,
              746.2605638926996,
              0.0021409989995660045
            ],
            [
              0.7439046231061051,
              4.166264573824653,
              0.30774890967963464,
              786.5450756351772,
              -0.009828666309962056
            ],
            [
              0.7853981633974483,
              4.348488620684954,
              0.32216677245967634,
              790.9909896538321,
              -0.017372488370680755
            ],
            [
              0.8268917036887915,
              4.473164110689504,
              0.3375239803446189,
              777.5428828471726,
              -0.02393683136416208
            ],
            [
              0.8835729338221293,
              4.566557179522729,
              0.3629053877725605,
              744.2016459541478,
              -0.02750648187144386
            ],
            [
              0.9402541639554671,
              4.612607632358486,
              0.3932623900101613,
              760.8340075529112,
              -0.017385349105269718
            ],
            [
              0.9817477042468103,
              4.635503429555184,
              0.41632006452060516,
              834.4640587676477,
              0.005038645619764748
            ],
            [
              1.0232412445381536,
              4.6487334156222655,
              0.439213583468706,
              846.7413505231566,
              -0.03702065077102698
            ],
            [
              1.0799224746714913,
              4.675590086266093,
              0.47059691049244756,
              943.0835571039622,
              -0.06144046894801275
            ],
            [
              1.1366037048048292,
              4.688114591525482,
              0.504607875274048,
              1063.915620194934,
              -0.047860239577659475
            ],
            [
              1.1780972450961724,
              4.672419767543438,
              0.5322204155857927,
              1127.634925798663,
              -0.3380338620771252
            ],
            [
              1.2195907853875156,
              4.6280757012619445,
              0.5617177320603567,
              1382.624818569223,
              -0.5354668776994621
            ],
            [
              1.2762720155208536,
              4.652271916869166,
              0.6094611890927069,
              1438.5587355378743,
              -0.23859479843313208
            ],
            [
              1.3329532456541913,
              4.8719036475910364,
              0.6614260686273028,
              1310.5862755440896,
              -0.061137511041962744
            ],
            [
              1.3744467859455345,
              5.016637062094574,
              0.6990886312505933,
              1321.6606723823675,
              -0.07941240963928523
            ],
            [
              1.4159403262368777,
              5.107404152506827,
              0.7350892382035379,
              1478.8412098635163,
              -0.08736074728250418
            ],
            [
              1.4726215563702154,
              5.718873570779759,
              0.7827561423521513,
              1628.156342794632,
              -0.09415565303442064
            ],
            [
              1.5293027865035533,
              6.42923254604762,
              0.8335206320316627,
              1909.0134571582685,
              -0.15117233705447117
            ],
            [
              1.5707963267948966,
              6.968190732291204,
              0.8757121232371243,
              2087.580156559493,
              -0.5012150524641072
            ]
          ],
          "coefficient_count_per_phase": 1638,
          "configuration": {
            "cap_degree": 6,
            "check": [
              103,
              33,
              21,
              19
            ],
            "degree": 5,
            "extra_check": true,
            "id": "fixed-target-space-time-2",
            "inner": 105,
            "intervals": 8,
            "max_nfev": 68,
            "mesh": [
              49,
              17,
              12,
              11
            ],
            "previous_roll_spaces": [
              [
                3,
                3
              ],
              [
                4,
                5
              ]
            ],
            "regularizer": 2e-06,
            "roll_modes": 7,
            "roll_spans": 8
          },
          "design": {
            "angle": "legacy",
            "bend": 1.5625e-05,
            "central": "expanded",
            "fade": [
              1,
              1.095
            ],
            "id": "legacy-developable-boundary-expanded",
            "mode": "dev"
          },
          "knots": [
            {
              "adjoint_abs": 3.608224830031759e-16,
              "cost": 0.2033317908404902,
              "directional_fd_relative": 2.9377370202470178e-08,
              "index": 1,
              "nfev": 55,
              "njev": 37,
              "optimality": 0.08899890440994522,
              "phase": 0.19634954084936207,
              "point_sha256": "a8d7e25d4885609577c45124299401ca6c325557ef69233e2a4e4241a5ad1872",
              "status": 2,
              "train_gram": 2.170201262354805
            },
            {
              "adjoint_abs": 4.440892098500626e-16,
              "cost": 0.29655428233564596,
              "directional_fd_relative": 3.2103556437410214e-08,
              "index": 2,
              "nfev": 68,
              "njev": 49,
              "optimality": 0.06489465442357387,
              "phase": 0.39269908169872414,
              "point_sha256": "e566141880a6d54e7d3faca1b8424dcbb506f99f0b4d2f97c3b25d56d8962444",
              "status": 0,
              "train_gram": 2.7650197452293126
            },
            {
              "adjoint_abs": 2.498001805406602e-16,
              "cost": 0.4871279180153607,
              "directional_fd_relative": 2.4496156948880513e-08,
              "index": 3,
              "nfev": 68,
              "njev": 57,
              "optimality": 0.43954233115199204,
              "phase": 0.5890486225480862,
              "point_sha256": "7222ceb486c0b9b3e3880ed29c4a706e57f69f2625790fd2c99723a9398cfb06",
              "status": 0,
              "train_gram": 2.952651513380867
            },
            {
              "adjoint_abs": 4.932165786897258e-14,
              "cost": 0.7592953874000883,
              "directional_fd_relative": 1.8522799202134087e-06,
              "index": 4,
              "nfev": 68,
              "njev": 57,
              "optimality": 0.5200580046950436,
              "phase": 0.7853981633974483,
              "point_sha256": "219692534ae037f71b652e5bde5a0517cbe4f2a50b0dd81a66ea41f95558382e",
              "status": 0,
              "train_gram": 3.0378467840416743
            },
            {
              "adjoint_abs": 4.58869053865385e-13,
              "cost": 1.3069130756366232,
              "directional_fd_relative": 5.36752607315258e-06,
              "index": 5,
              "nfev": 68,
              "njev": 56,
              "optimality": 2.638523146420646,
              "phase": 0.9817477042468103,
              "point_sha256": "879aae5f1cc5469eb2554369368f135326c1341cb7b1479673fdf340620aaafe",
              "status": 0,
              "train_gram": 3.1614159167338736
            },
            {
              "adjoint_abs": 3.5371705564557487e-13,
              "cost": 2.2059150529931837,
              "directional_fd_relative": 3.868906182587454e-06,
              "index": 6,
              "nfev": 57,
              "njev": 38,
              "optimality": 11.85207993672578,
              "phase": 1.1780972450961724,
              "point_sha256": "47328686ef6633d24c2dbab2e3e7f9abd03941bc3f9524305d891595de9a8048",
              "status": 3,
              "train_gram": 3.0990243793977963
            },
            {
              "adjoint_abs": 2.736699755701011e-13,
              "cost": 3.8550475301962077,
              "directional_fd_relative": 1.8130910031971094e-06,
              "index": 7,
              "nfev": 68,
              "njev": 53,
              "optimality": 3.7240119482023823,
              "phase": 1.3744467859455345,
              "point_sha256": "783bb089d5cea937a7666bf0159682c53586c8a0bf8a7749905754b6a3b9ceb5",
              "status": 0,
              "train_gram": 3.6326440351357627
            },
            {
              "adjoint_abs": 3.552713678800501e-15,
              "cost": 5.673245952425774,
              "directional_fd_relative": 9.661840190569248e-07,
              "index": 8,
              "nfev": 65,
              "njev": 46,
              "optimality": 114.9363877965316,
              "phase": 1.5707963267948966,
              "point_sha256": "5f91c3743cc97acd02c42cd2c8f3c87e29d5ca9b512d5d924344abd015255070",
              "status": 3,
              "train_gram": 5.198027626393641
            }
          ],
          "npz_bytes": 118530,
          "npz_sha256": "fc6de0def675fbd6acf155742c11ed4e3fb24c0ed513ae0fbb8da14a7376234a",
          "point_sha256": "cce19ff7f718dd1f246f5a542ee2686e9a4f595afff8a5de19df9ad311f5c345",
          "previous_point_sha256": "ba153412e990b9237ebf450d298cd8628ca1c2d45a65b35376ae146010ec1577",
          "score": 161.19993791948852,
          "shape": [
            9,
            1638
          ],
          "stage": 6,
          "time_data_sha256": "a152b9e9c55abd479545fda1aa65117b00106f4a472b9c50078e909199a3fbcf",
          "worst_gram_by_chart": {
            "cap+": [
              0.4733109913873964,
              1.5707963267948966,
              4.5930155540114,
              1.0
            ],
            "cap-": [
              0.48733981554223416,
              1.5707963267948966,
              4.5689401184272,
              1.0
            ],
            "cap-cartesian+": [
              0.000112313090361662,
              1.3744467859455345,
              0.59502,
              0.0
            ],
            "cap-cartesian-": [
              0.18765922738020288,
              1.4726215563702154,
              0.59498,
              0.0
            ],
            "cylinder": [
              3.434052117771686,
              1.4159403262368777,
              2.4611193300256,
              -0.725625
            ],
            "end+": [
              6.968190732291204,
              1.5707963267948966,
              5.4430155540114,
              0.037347047722999814
            ],
            "end-": [
              6.96498911392696,
              1.5707963267948966,
              5.4105155540114,
              0.037347047722999814
            ]
          },
          "zero_phase_sixjet_difference": 0.0
        }
      ],
      "target": "The R747 common initial physical pullback on every original material point, no masks omitted in verification. This g, material chart and [0,pi/2] are identical in every design and refinement."
    }
  },
  "whole_runner_field_files": null,
  "scientific_sampled_success_inferred_by_launcher": false,
  "exact_metric_or_global_geometry_inferred_by_launcher": false,
  "dependency_command": [
    "/opt/hostedtoolcache/Python/3.12.14/x64/bin/python",
    "-m",
    "pip",
    "install",
    "--disable-pip-version-check",
    "--no-input",
    "--only-binary=:all:",
    "numpy==2.3.5",
    "scipy==1.17.0"
  ],
  "dependency_returncode": 0,
  "actual_numeric_versions": {
    "numpy": "2.3.5",
    "scipy": "1.17.0"
  },
  "scientific_environment": {
    "PYTHONUNBUFFERED": "1",
    "PYTHONDONTWRITEBYTECODE": "1",
    "PYTHONHASHSEED": "0",
    "OPENBLAS_NUM_THREADS": "1",
    "OMP_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1"
  },
  "child_started_utc": "2026-11-28T13:15:06Z",
  "observed_utc": "2026-11-28T13:51:14Z",
  "original_scalar_line_count": 29
}
```


## 原16区间终层与自然完整返回（2026-11-28 UTC）

ROOT读固定提交`a7fcb8b9a37f7a8798b071d0e16fc403fe405276`的[完整原终态](run40-bent-end-phase-46148644102-1.json)，70611B / SHA256 `69114b54a54dcf207b3f3cd53806987a1c7535a28e045b2c9d991cca2cebd5c8` / Git `62cd14f5f1549f18290f53ad9f27001e72ee05e0`，全部身份核同，并核十实际冻结输入与原request一致。官方run46148644102/1、job140990119811，源`8561fc2b7a68f1cbede10f9421acbee8bd40b6bf`、七步骤success；真PID2569从13:15:06Z运行至18:03:43Z自然return0，官方18:03:50Z完成。成功退出只说明原有限科学阶段已做完。

原全部五粗、4/8/16三精化共八阶段都完成，各原interval对应完整knots；最高层16个原求解均自然返回，13个达到原nfev76、另3个status3自然停止于70/50/58，不是外部减预算。最高层mesh[65,21,16,14]，独立check[127,41,27,23]，degree7/cap_degree8/roll_modes9/spans12，inner125、regularizer1e−6和原65检查相全部保留。

|stage|设计|完整独立相数|relative Gram|max abs principal|
|---:|---|---:|---:|---:|
|0|legacy-named-free|5|9.135032045701506|38287.37226017895|
|1|offset-cap-only-free|5|1929.8482581349583|1083052464.4066625|
|2|legacy-developable-full|5|9.323266658414182|46110.550178704965|
|3|offset-developable-full|5|1930.5321968221297|12396225.856801046|
|4|legacy-developable-boundary|5|9.132224342164221|2885.3296246505834|
|5|legacy-developable-boundary-expanded|17|8.040081916241995|2815.8379714384128|
|6|legacy-developable-boundary-expanded|33|6.968190732291204|2087.580156559493|
|7|legacy-developable-boundary-expanded|65|8.070534438767147|275522.64527050033|

最终完整时间场点`515e3d3206cbc6cc96b690a3d75791fe205c0be70e2bcee0e3c118f9c653e9ac`，真正前点`cce19ff7f718dd1f246f5a542ee2686e9a4f595afff8a5de19df9ad311f5c345`，shape17×3438，原NPZ468226B / SHA256 `89e95ccafb965543dc7434f5738bc4680abdd5ebe14cc55a4f2dd25a225618f6`；时间节点原小端SHA `a6d7c4ab616f4e28e63d90de4d2ce2a9b8b194a72f11cd2ff308f1944c6c2ec2`。完整summary原58946B/SHA256 `f85172bc9967926efa94fbeca13ca2ba0e0ad73c8405d917524b1f2671e5e338` 已全文嵌在终态，不另截取伪造更小必要结果。

最高有限Gram8.070534438767147在cylinder、t1.395193556091206、u2.2175133096772、v−.7304999999999999；最高主曲率275522.64527050033在end+、t1.227184630308513、u4.270776655973、v.15961003924372968；最小面积密度.00004641327844131543在cap−、t1.493368326515887。零相六jet差仍0，但不推非零相度量。

七额外整面点云时刻各4136点，有限D峰2.962083559875463、sample held峰1.8361170494603458、有序逆法球弦峰321.68974640028307。它们是原点云检查，不是七份完整三角网；不能借未来mesh补成已交付。全点云、体积/矩、各图最坏地址在原终态完整保留。真实固定g精化Gram8.040081916241995→6.968190732291204→8.070534438767147没有趋向0，明确未达本题1e−6和准确解精化标准，连续全管也未证。所有原解析限定结论仍在前文，不因这一失败删去。

该run原末次已发布双README真pull为`0d4fc710a23b0752666f5c52e9b8bdb66c68e348`，不从旧observer未持久化的内存事件补写更晚pull。已自然完成，活动marker撤去；源参/原输出身份和本完整结论保留，后续继续新完整场。
