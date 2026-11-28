# Run39b — 原真实闭场的材料轨线、跨图与完整切映射

会话 Astra-larger-e4e2a2bf-20261126。完整7件独立源/参数/工作流一次刊出触发；实际run/job/source/entry/轨线/误差均尚未观察，保留null。它延续39自然返回点的真实全时费用，不修改仍运行33–35，不把旧39结论再登记成新研究。

## 原点、同一目标与完整重生费用

39实际run46146451800/1、job140983460924、原源c3e685703f28928dfe8cb8d9b71d2d3ed99285ef，完整11阶段自然RC0。原完整terminal文件75633B/SHA2561642366bf3aaa09cc3e5d9b4c31af5b2ea55ffb168cb0b4fd2f7193e19299351/Git09d8aaf5feb9005946f91ac44d31689f4d03cfc3；原summary65540B/06a7fa77c1063560fc6414da23af584ec5d92117946b6f51ec6cafb01f0ef192。

raw NPZ只在原runner，故新job先依原13 whole inputs中的parent原参数完整重生11阶段，保全部原预算与独立耗时/原stdout/所有NPZ身份；只作为本次消费实际系数的必要重生。所有stage的原/重生物理与材料系数、全point、NPZ、设计、完整配置逐条比较。若有差异，后续写作独立重生点，不能冒原点。选定stage6的physical a4dd5cf469cb8545c5dd0d070e28268a4c300e0bad307e703ee41a0d510aa872是真固定g*；stage6、9、10分别计算各自材料X，两个fixed层使用同一目标，不更换g。

## 新的实际全时计算

每点解qdot=−X(q)，Jdot=−DX(q)J，t∈[0,π]，J0=I。X=X0+G^−1 T A，DX用完整真实二jet和法方程导数。两端管带及真帽的笛卡尔图实际切换，保存位置/切向/场的转图误差和原基差；正则帽中心没有极坐标退化。每个真实材料初点比较R_t DF(q(t))J+e_z db(q0)与原标记目标的完整2×2广义特征值。

三种实际场分别取固定握持、标记斜坡、正反弯、两rim/两head/两cap中心和内点、24角探测选的两方向速度极值、原真实check Gram/Killing/K/support/speed与三图Killing极点，约24/25条完整轨线/场。每个地址都跑完整两级DOP853：rtol2e−7/atol2e−9/maxstepπ/28与2e−9/2e−11/π/58；每步3/7内探针，33时间样本并包含原6相。四个独立point worker，所有失败及部分轨线均保；不删难点、不缩预算。有限轨线/双容差不代空间连续上界、全域reach或数学成功。

## 完整新件身份

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_body_flow_actual.py",
    "bytes": 9244,
    "sha256": "98d5aaa7a45ee7b51626f6e13f804965802eeef4fc43da68aea25636c0698eac",
    "git_blob_sha": "68e91b81977056522920f6ed517fa199dfe6c1d2"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_body_flow_field.py",
    "bytes": 10290,
    "sha256": "7339a1501a8edc44c65ffa977847b4ac5a9fe0ce4540cbaba4122bdb4cbf7a0b",
    "git_blob_sha": "bdf6c7925a87a4bc515cc2c0b3b5339116317ecb"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_body_flow_track.py",
    "bytes": 11825,
    "sha256": "1425b51ce99d8c908e421096aa7e4f0f91233124a9da3224efc91395fb8a6109",
    "git_blob_sha": "8bbba1b825cc4236955392aad4134890db3fe663"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/bent-body-actual-flow-design-v1.json",
    "bytes": 3286,
    "sha256": "ec4068b8e2783135ace2104dd9dd7129bdc2e30ac8ae484671ac121b67d25d1f",
    "git_blob_sha": "bccdaa0ba3e0eab9f7bb81084d21ce46866440f8"
  },
  {
    "path": ".github/workflows/visible-larger-run39b-bent-body-flow.yml",
    "bytes": 3760,
    "sha256": "23ff23601ea9423620942bb2329e272e7b4e99a630072e3ce2dd2f95f85cb89e",
    "git_blob_sha": "5cc0fd00753147456cf1dbebf95700a5d2c23943"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/run39b-bent-body-flow-request.json",
    "bytes": 16496,
    "sha256": "17b9d3493d0cdbcc87e0ea3d4c1769367c3c8e205c259d8fe7aa3099d395a975",
    "git_blob_sha": "6664330da403ec275f9f9ae1e2896cfd1e126650"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/run39b-complete-actual-flow-delivery.json",
    "bytes": 23131,
    "sha256": "a087954ae99f6141c1f918c88bff39ca33625df10d6382d612d95e8e408d25f3",
    "git_blob_sha": "7293b8113cd94c8d788d776201826d8e0fac4231"
  }
]
```

## 原完整参数与入口

```json
{
  "schema": "bent-body-three-actual-material-flows/v1",
  "parent_run": "46146451800",
  "parent_attempt": "1",
  "parent_source_commit": "c3e685703f28928dfe8cb8d9b71d2d3ed99285ef",
  "original_observation": {
    "path": "topics/visible-flex-larger-amplitude/notes/run39-bent-body-killing-46146451800-1.json",
    "bytes": 75633,
    "sha256": "1642366bf3aaa09cc3e5d9b4c31af5b2ea55ffb168cb0b4fd2f7193e19299351",
    "git_blob_sha": "09d8aaf5feb9005946f91ac44d31689f4d03cfc3",
    "observed_main_commit": "cbdab722838e00ebf9a45fde3750b2b9247d4632"
  },
  "original_parent_summary": {
    "path": "/home/runner/work/_temp/run39-bent-body-killing-46146451800-1/field/summary.json",
    "bytes": 65540,
    "sha256": "06a7fa77c1063560fc6414da23af584ec5d92117946b6f51ec6cafb01f0ef192"
  },
  "full_parent_replay": "Run the unchanged bent_body_killing.py with the complete original parameters. Preserve its separate stdout, original 11 stage files and independent runtime. Compare every scientific stage identity. An independently diverged field is reported with its own provenance.",
  "phase_interval": [
    0,
    3.141592653589793
  ],
  "phases": [
    0,
    0.39269908169872414,
    0.7853981633974483,
    1.5707963267948966,
    2.356194490192345,
    3.141592653589793
  ],
  "time_samples": 33,
  "integrators": [
    {
      "id": "complete-dop853-first",
      "rtol": 2e-7,
      "atol": 2e-9,
      "max_step_divisions": 28,
      "inner_step_probes": 3
    },
    {
      "id": "complete-dop853-second",
      "rtol": 2e-9,
      "atol": 2e-11,
      "max_step_divisions": 58,
      "inner_step_probes": 7
    }
  ],
  "parallel_point_workers": 4,
  "seam_probe_angles": 24,
  "spatial_protocol": "Per field and actual source geometry: upper flat grip and marker slope, upper/lower real bend, both y-rims, right meridian, both turned head interiors, both regular cap centers and two analytic cap interiors, two signed seam-speed extrema on each cap. Add every available actual independent-check Killing, chart speed, curvature, support and fixed Gram extremum plus three chart-group Killing extrema. Each address runs both integrators across the whole interval.",
  "stage_selection": "The Run39 frozen source physical field and both fixed-source material vectors on their original charts; two refinements each with that same Gstar. No fitted angular radius, mixed prior point or image-only transport.",
  "mark_mechanism": "On the original upper marked material disk the generator equals polar rotation and the physical perturbation vanishes on an open neighborhood. Mark heights and their material gradients use the geometry-specific original cubic radii and heights. Outside their closed supports the derivatives vanish.",
  "trajectory_formula": "dq/dt=-X(q) and dJ/dt=-DX(q)J with J(0)=I. X=X0+G^-1 T A. Use true Fs,Fv,Fss,Fsv,Fvv; G=T T^T. Every finite sample compares the complete derivative of R_t F(q(t))+b(q0)e_z with the marked physical target Gram at q0 by its symmetric generalized eigenvalues.",
  "error_interpretation": "Pointwise double-precision finite paths, original-basis comparison and independent integration refinements. Per-step dense probes estimate missed chart exits; no interval enclosure, spatial supremum, reach or global isometry claim."
}

```

```json
{
  "entry": {
    "script": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_body_flow_actual.py",
    "argv": [
      "--params",
      "{immutable_science_worktree}/topics/visible-flex-larger-amplitude/computations/bent-body-actual-flow-design-v1.json",
      "--parent-params",
      "{immutable_science_worktree}/topics/visible-flex-larger-amplitude/computations/bent-body-killing-design-v1.json",
      "--geometry-source",
      "{immutable_science_worktree}/topics/visible-flex-larger-amplitude/scripts/resume_20261126/r745_equal_meridian_jacobi_two_jets.py",
      "--parent-observation",
      "{immutable_science_worktree}/topics/visible-flex-larger-amplitude/notes/run39-bent-body-killing-46146451800-1.json",
      "--out",
      "{runner_temp}/run39b-bent-body-flow-{run}-{attempt}/field"
    ],
    "flags": [
      [
        "--parent-params",
        "parent_parameters"
      ],
      [
        "--geometry-source",
        "geometry_source"
      ],
      [
        "--parent-observation",
        "original_observation"
      ]
    ],
    "source_freeze": "All 13 whole scientific inputs are read from the immutable launch tree with file SHA-256 and Git blob verification by the shared supervisor before normal execution."
  },
  "runner": {
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
    "scientific_summary": "Report a separate parent replay identity and timing, every original/replay stage identity difference and each actual flow point. Report coarse/fine pullback errors and actual crossing, basis and endpoint differences, preserving failed attempts.",
    "raw_fields": "Full regenerated NPZ coordinates, trajectories, failed partial time histories and detailed scalar logs stay on the runner. Publish point identities and complete per-point raw-file length and SHA.",
    "public_attempt": "notes/run39b-bent-body-flow-<run>-<attempt>.json and one marked H line after checked pull/rebase, inclusive topic capacity accounting.",
    "success": "Field equality and velocity alone provide no global metric, reach, held, Euclidean quotient, control of unsampled material or interval certificate."
  },
  "actual": {
    "run": null,
    "attempt": null,
    "original_point_reproduction": null,
    "selected_point_sha256": null,
    "recorded_trajectory": null,
    "gram_extrema": null,
    "global_metric": null,
    "reach": null,
    "held": null,
    "e_rigid": null
  }
}
```

共享observer14863B/c47dde7a与Run36控制函数未改；公开4CPU/16GB，Python3.12.14、numpy2.3.5/scipy1.17.0，job360分钟，无新科学wall cutoff，8秒观察/90秒live/20秒发布重试，真实pull≤2700秒并仅README差异立即应用。原始大raw和逐点完整轨线只留runner，main保完整轻报告与whole身份。已读七整件，尚未观察任何新科学返回。
