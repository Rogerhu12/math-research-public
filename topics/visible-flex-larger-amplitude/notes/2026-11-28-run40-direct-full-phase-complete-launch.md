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
