# R318-old-full-cut-frozen-true-Cauchy-inlet-profiles

**数值记录。** 2026-11-28 17:42:00 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `edb2fe6fe42d215fb7fe6e37eb40fab01b4d2360`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

旧c=.78真三圆弧分支在所选细g上固定目标，仅加R318准确物理三剖面，并消费1152曲率角和1725独立角；不将有限native无法准确含N/k的障碍当停止理由，也不把包含新三列的状态送给旧native证书。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R318-old-full-cut-frozen-true-Cauchy-inlet-profiles；实际源码逐文件摘要列于下方。开始 2026-11-28 17:40:15 UTC，结束 2026-11-28 17:42:00 UTC。退出码 0。

```json
{
  "entrySHA256": "ffa687858a059ab60e14987d55acdd1a7d63c62855f7804f2d2ccc2966cebfd0",
  "stateSHA256": "3c260c92f07e443a73bafc32bf45d66305d4acac4cd989f84e1906d6ad9c1245",
  "parentSHA256": "721a81fd1004054a752342d4d67799d0ebe03c211a829bb34d333bb699cd94d9",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "initial": {
    "peak": 0.009739494609814579,
    "rms": 0.0026655876326170504,
    "curvature": 8.687682945318173,
    "worstMetric": [
      0.8992104859301235,
      4.828744263850979,
      4.57815956497283
    ],
    "worstCurvature": [
      1.2767103580421812,
      0.9599310885968813,
      0.8909126765706742
    ],
    "minimumSupport": 0.3642558034432623,
    "minimumZs": 0.22441086647493674,
    "minimumArea": 0.11999999946243713
  },
  "initialSecondary": {
    "peak": 0.009720031906187235,
    "rms": 0.0027332309578338015,
    "curvature": 8.689328233875607,
    "worstMetric": [
      0.8966308851756504,
      4.82493824990582,
      4.573328521305147
    ],
    "worstCurvature": [
      1.2774974551448612,
      0.949328621178224,
      0.8721535432814781
    ],
    "minimumSupport": 0.3642039660300401,
    "minimumZs": 0.22441629938259844,
    "minimumArea": 0.12020687651814196
  },
  "initialGuard": {
    "peak": 0.010214213274092082,
    "curvature": 8.674944160698486,
    "minimumSupport": 0.36396497321268384,
    "minimumArea": 0.12001606318560051,
    "minimumZs": 0.2244143772600236,
    "worstMetric": [
      0.9633333333333335,
      4.955098829490151,
      4.756053377181275
    ],
    "worstCurvature": [
      1.2790324582477006,
      1.1426452446650375,
      1.2179642046842727
    ],
    "rms": 0.002367896872599203,
    "radialRows": 163,
    "angles": 1152
  },
  "accepted": {
    "actualCompletedSteps": 0
  },
  "attempts": [
    {
      "step": 1,
      "accepted": false
    }
  ],
  "normalAndRhsAgreement": [
    9.86211376757255e-16,
    4.3702624584089137e-16
  ],
  "finalAngularGuard": {
    "peak": 0.010214213274092082,
    "curvature": 8.674944160698486,
    "minimumSupport": 0.36396497321268384,
    "minimumArea": 0.12001606318560051,
    "minimumZs": 0.2244143772600236,
    "worstMetric": [
      0.9633333333333335,
      4.955098829490151,
      4.756053377181275
    ],
    "worstCurvature": [
      1.2790324582477006,
      1.1426452446650375,
      1.2179642046842727
    ],
    "rms": 0.002367896872599203,
    "radialRows": 163,
    "angles": 1152
  },
  "initialIndependent": {
    "peak": 0.01031906256933899,
    "curvature": 8.688508202435393,
    "minimumSupport": 0.36423898267820004,
    "minimumArea": 0.11999999946243713,
    "minimumZs": 0.22443576528795978,
    "worstMetric": [
      0.9741000000000002,
      4.953699720443036,
      4.753911166376679
    ],
    "worstCurvature": [
      1.2768413651089703,
      3.2308320970830686,
      3.301373893778597
    ],
    "rms": 0.0023753298615759584,
    "radialRows": 323,
    "angles": 1725
  },
  "independent": {
    "peak": 0.01031906256933899,
    "curvature": 8.688508202435393,
    "minimumSupport": 0.36423898267820004,
    "minimumArea": 0.11999999946243713,
    "minimumZs": 0.22443576528795978,
    "worstMetric": [
      0.9741000000000002,
      4.953699720443036,
      4.753911166376679
    ],
    "worstCurvature": [
      1.2768413651089703,
      3.2308320970830686,
      3.301373893778597
    ],
    "rms": 0.0023753298615759584,
    "radialRows": 323,
    "angles": 1725
  },
  "stateUse": "The three physicalInletProfiles columns multiply N/k, the actual lifted old center-to-sleeve discrepancy at q=c, and the vertical 1/k^2. Use this source profiles() or Audit() for all three. The native part is deliberately named inletNativeXYZ and must be combined with all three columns."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py: SHA-256 `ffa687858a059ab60e14987d55acdd1a7d63c62855f7804f2d2ccc2966cebfd0` (14160 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `82a1e922cb947b8f7986d7b6a123c9bbed2ed878e85b1c0a2dedce3159e6ee97` (78638 bytes).
- 2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py: SHA-256 `ffa687858a059ab60e14987d55acdd1a7d63c62855f7804f2d2ccc2966cebfd0` (14160 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- fine-g-physical-inlet.json: SHA-256 `ba6e90df617732f81f0000acb6743947287f3d886efad3325dc1a12b90d5e43e` (6360 bytes).
- fine-g-physical-inlet.npz: SHA-256 `3c260c92f07e443a73bafc32bf45d66305d4acac4cd989f84e1906d6ad9c1245` (44881 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
