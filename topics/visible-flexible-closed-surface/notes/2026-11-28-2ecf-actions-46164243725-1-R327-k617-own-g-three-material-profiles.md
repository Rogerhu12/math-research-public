# R327-k617-own-g-three-material-profiles

**数值记录。** 2026-11-28 18:03:01 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `e4b8533d475bac67a8baa44ff74ca4ca9f443cd6`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

冻结同一g，由真新母线计算三个C²入口剖面并作全帯Newton。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R327-k617-own-g-three-material-profiles；实际源码逐文件摘要列于下方。开始 2026-11-28 18:01:26 UTC，结束 2026-11-28 18:03:01 UTC。退出码 0。

```json
{
  "entrySHA256": "cee69956d395cc156a4f3132cb5dae9d7f36272bf3a5f83c29e652549fc37145",
  "stateSHA256": "84a1fc268b840796a47ba8787652966ee8c16e53f3e8599fe8b67159bfbff022",
  "parentSHA256": "1a0432b6a16c9f120ffbcbcd8adff31f08a953d47fa36659613f07912ce99a12",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "physicalSourceSHA256": "bc1836eb40110bb5fd9abfeeb8819ecf22b95ef334140109f6652dfcafb35917",
  "cutSHA256": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
  "actualPositionVariables": 1326,
  "initial": {
    "peak": 0.0018891267372815519,
    "rms": 0.000423919906631516,
    "curvature": 4.878519660895347,
    "worstMetric": [
      0.41666666666666663,
      3.6070137874549477,
      3.8696291882501486
    ],
    "worstCurvature": [
      0.40917790779134344,
      0.0,
      0.0
    ],
    "minimumSupport": 0.6001724906804458,
    "minimumZs": 0.22675856779555167,
    "minimumArea": 0.11999999946243713
  },
  "initialSecondary": {
    "peak": 0.0018926612022487014,
    "rms": 0.0004308397646522572,
    "curvature": 4.879124621795251,
    "worstMetric": [
      0.41666666666666663,
      3.6113635176779866,
      3.8745608005675387
    ],
    "worstCurvature": [
      0.4084,
      2.0943951023931957,
      2.094395102393195
    ],
    "minimumSupport": 0.6001319853110532,
    "minimumZs": 0.22681709622750865,
    "minimumArea": 0.11999999946243715
  },
  "initialGuard": {
    "peak": 0.0018908257305197077,
    "curvature": 4.87834026402488,
    "minimumSupport": 0.6002858271845105,
    "minimumArea": 0.11999999946243715,
    "minimumZs": 0.22678754177116442,
    "worstMetric": [
      0.41666666666666663,
      3.608219541687759,
      3.8710007256325696
    ],
    "worstCurvature": [
      0.4093333333333333,
      4.1887902047863905,
      4.188790204786386
    ],
    "rms": 0.000385449537420574,
    "radialRows": 163,
    "angles": 991
  },
  "accepted": {
    "actualCompletedSteps": 5
  },
  "attempts": [
    {
      "step": 1,
      "accepted": true
    },
    {
      "step": 2,
      "accepted": true
    },
    {
      "step": 3,
      "accepted": true
    },
    {
      "step": 4,
      "accepted": true
    }
  ],
  "normalAndRhsAgreement": [
    7.116271822659555e-16,
    4.134259639424823e-16
  ],
  "finalAngularGuard": {
    "peak": 0.001417119128657694,
    "curvature": 5.04387409754456,
    "minimumSupport": 0.6028357253883072,
    "minimumArea": 0.11999999946243715,
    "minimumZs": 0.22139622189178035,
    "worstMetric": [
      0.476,
      5.2793949083641944,
      5.314022569145569
    ],
    "worstCurvature": [
      0.4833333333333333,
      4.375965050388234,
      4.233971116578084
    ],
    "rms": 0.0005182777657781385,
    "radialRows": 163,
    "angles": 991
  },
  "initialIndependent": {
    "peak": 0.001891658453310039,
    "curvature": 4.875133706208144,
    "minimumSupport": 0.6003072032774257,
    "minimumArea": 0.11999999946243713,
    "minimumZs": 0.2268535885217006,
    "worstMetric": [
      0.41666666666666663,
      3.6090268546429454,
      3.871917117063455
    ],
    "worstCurvature": [
      0.40446666666666664,
      0.0,
      0.0
    ],
    "rms": 0.00038448093729151706,
    "radialRows": 163,
    "angles": 1445
  },
  "independent": {
    "peak": 0.0014313872700291957,
    "curvature": 5.044232921249802,
    "minimumSupport": 0.6028407637370208,
    "minimumArea": 0.11999999946243713,
    "minimumZs": 0.22149310778677134,
    "worstMetric": [
      0.4711333333333333,
      5.188881983783834,
      5.151322671468207
    ],
    "worstCurvature": [
      0.4833333333333333,
      4.374883100505962,
      4.233622561660733
    ],
    "rms": 0.0005197815944193364,
    "radialRows": 163,
    "angles": 1445
  },
  "trueTransitionAngleGrids": [
    {
      "fullUniform": 216,
      "additionalMaterialTargets": 174,
      "perTransitionInterior": 13,
      "originalMaterialInverseError": 5.329070518200751e-15
    },
    {
      "fullUniform": 321,
      "additionalMaterialTargets": 270,
      "perTransitionInterior": 21,
      "originalMaterialInverseError": 5.329070518200751e-15
    },
    {
      "fullUniform": 579,
      "additionalMaterialTargets": 414,
      "perTransitionInterior": 33,
      "originalMaterialInverseError": 5.329070518200751e-15
    },
    {
      "fullUniform": 867,
      "additionalMaterialTargets": 582,
      "perTransitionInterior": 47,
      "originalMaterialInverseError": 7.993605777301127e-15
    }
  ],
  "coordinateEvaluatorsAgreement": [
    0.0,
    0.0
  ],
  "metricVariables": 0,
  "additionalPhysicalVariables": 117,
  "curvatureBias": 0.3061034881472919,
  "materialEdges": [
    0.79,
    0.8681880555637657,
    1.0471975511965976
  ],
  "radialTuning": [
    0.48,
    -0.221,
    0.135
  ]
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r327-k617-all-span-physical-inlet-profiles.py: SHA-256 `cee69956d395cc156a4f3132cb5dae9d7f36272bf3a5f83c29e652549fc37145` (13986 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `c20429e2ce897d7c7239b0ee1ce85f48f1ad5ec558e41720fd967248d614f05a` (105935 bytes).
- 2ecf-r327-k617-all-span-physical-inlet-profiles.py: SHA-256 `cee69956d395cc156a4f3132cb5dae9d7f36272bf3a5f83c29e652549fc37145` (13986 bytes).
- 2ecf-r262-material-curvature-k617-cut.py: SHA-256 `bc1836eb40110bb5fd9abfeeb8819ecf22b95ef334140109f6652dfcafb35917` (13939 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- 2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py: SHA-256 `ffa687858a059ab60e14987d55acdd1a7d63c62855f7804f2d2ccc2966cebfd0` (14160 bytes).
- h1-physical-inlet.json: SHA-256 `ce9a2a6368c49e35b42e9a63760dd58c5010c2c45110ab7ea99c1a0382456b9c` (16259 bytes).
- h1-physical-inlet.npz: SHA-256 `84a1fc268b840796a47ba8787652966ee8c16e53f3e8599fe8b67159bfbff022` (18100 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
