# R319-actual-0350-frozen-compensated-heat-orbit

**数值记录。** 2026-11-28 18:17:01 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `991e2237fa29e2a81d2bc92df4ab7f40c6677516`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

在同一个实际R319三入口列状态与固定g上，加入正Jackson初密度的真实逆曲率热轨道、准确入口抬升、角依赖补偿高度及晚段C²门。完整XYZ/三列与一个物理热增益共同更新，真实完整Gram/曲率决定接受；独立621均匀角加六窗47真角。保存heat专用状态键，旧native/profile几何消费者拒收；先报告热增益1的真实完整观察，即使最后热步不接受。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R319-actual-0350-frozen-compensated-heat-orbit；实际源码逐文件摘要列于下方。开始 2026-11-28 18:15:36 UTC，结束 2026-11-28 18:17:01 UTC。退出码 0。

```json
{
  "schema": "R317-active-physical-compensated-inverse-curvature-heat-cut-v1",
  "entrySHA256": "2f318cd9a7afde09d8e5116a1b2ec3237a27184a7de1ae4c4a3643c65c0c0a8d",
  "heatSourceSHA256": "67f0d8cb4fa8c4538496a0fcfb14046d039f4f17ed774e4e1dfade7c08967180",
  "parentSHA256": "828793b5b8556e9b3e4d4e969f1688df7dc8dc9f990f8d00753adfb992a4c7ea",
  "stateSHA256": "9e24574c94ca05816cb3c1c54d90fd74a4aa0605d0cdc8d37b4379b14d2f9325",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "heatTime": 0.06969281271382982,
  "lateGate": 0.46,
  "JacksonOrder": 64,
  "heightPolynomialOrder": 48,
  "initialGain": 0.0,
  "finalHeatGain": -0.009479284109318534,
  "actualPositionVariables": 1327,
  "metricVariables": 0,
  "physicalAmplitudeDifferentialAgreement": 1.6798749870897117e-10,
  "grids": [
    {
      "angular": {
        "fullUniform": 216,
        "additionalMaterialTargets": 90,
        "perTransitionInterior": 13,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "rows": 407,
      "correctedRows": 77,
      "maxPhysicalDisplacement": 0.011067844430683564,
      "initialSectionLift": 3.877821032793882e-05
    },
    {
      "angular": {
        "fullUniform": 321,
        "additionalMaterialTargets": 150,
        "perTransitionInterior": 23,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "rows": 519,
      "correctedRows": 103,
      "maxPhysicalDisplacement": 0.011075452707862731,
      "initialSectionLift": 3.8759219351040505e-05
    },
    {
      "angular": {
        "fullUniform": 621,
        "additionalMaterialTargets": 294,
        "perTransitionInterior": 47,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "rows": 627,
      "correctedRows": 130,
      "maxPhysicalDisplacement": 0.011073373424277163,
      "initialSectionLift": 3.877821032793882e-05
    }
  ],
  "initial": {
    "peak": 0.0024024126925288325,
    "rms": 0.0006030949842936822,
    "curvature": 8.048202413182848,
    "worstMetric": [
      0.4658656560964175,
      3.141592653589793,
      3.1415926535897913
    ],
    "worstCurvature": [
      0.5038199345862868,
      2.0943951023931953,
      2.0943951023931944
    ],
    "minimumSupport": 0.5966936761987102,
    "minimumZs": 0.22938364775916512,
    "minimumArea": 0.11999999946243713
  },
  "initialShifted": {
    "peak": 0.0024037607028447594,
    "rms": 0.0006020479263058293,
    "curvature": 8.041584820420006,
    "worstMetric": [
      0.46373400213771554,
      3.141592653589793,
      3.1415926535897913
    ],
    "worstCurvature": [
      0.5063270185735232,
      4.198577097788228,
      4.190748708234545
    ],
    "minimumSupport": 0.5966619977867941,
    "minimumZs": 0.22939282585380905,
    "minimumArea": 0.12020687651814196
  },
  "unitHeatGainOnParent": [
    {
      "peak": 0.2017870897874805,
      "rms": 0.025369234397849428,
      "curvature": 6.902325438254607,
      "worstMetric": [
        0.6644924951188476,
        5.235987755982989,
        5.2359877559829835
      ],
      "worstCurvature": [
        0.4327611829260125,
        4.30514548825268,
        4.213940116718384
      ],
      "minimumSupport": 0.6430221738049184,
      "minimumZs": 0.22938364775916512,
      "minimumArea": 0.11999999946243713
    },
    {
      "peak": 0.20223761280332297,
      "rms": 0.02572456062188704,
      "curvature": 7.006105710711492,
      "worstMetric": [
        0.6587993691596059,
        5.235987755982989,
        5.2359877559829835
      ],
      "worstCurvature": [
        0.43178923981085976,
        4.296446027806602,
        4.211810828305119
      ],
      "minimumSupport": 0.6429875464156649,
      "minimumZs": 0.22939282585380905,
      "minimumArea": 0.12020687651814196
    }
  ],
  "accepted": {
    "actualCompletedSteps": 5
  },
  "initialIndependent": {
    "peak": 0.0024032910928126214,
    "rms": 0.0006048554672764904,
    "curvature": 8.04545486948572,
    "worstMetric": [
      0.4632449898992523,
      5.241046681351087,
      5.245093666282662
    ],
    "worstCurvature": [
      0.5028605324372962,
      2.0943951023931953,
      2.0943951023931944
    ],
    "minimumSupport": 0.5967683716460552,
    "minimumZs": 0.22938364775916512,
    "minimumArea": 0.11999999946243713
  },
  "independent": {
    "peak": 0.002084638165450877,
    "rms": 0.0006804445369805837,
    "curvature": 8.480169468405656,
    "worstMetric": [
      0.46819999999999995,
      5.210693129142491,
      5.190476842827032
    ],
    "worstCurvature": [
      1.2611574783750101,
      2.0943951023931953,
      2.0943951023931944
    ],
    "minimumSupport": 0.5959676060900636,
    "minimumZs": 0.23096885091910815,
    "minimumArea": 0.11999999946243713
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-adjacent-compensated-heat-cut-refinement.py: SHA-256 `2f318cd9a7afde09d8e5116a1b2ec3237a27184a7de1ae4c4a3643c65c0c0a8d` (10472 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `91b0653ff3423fec27402e6f4b25cab1ebaefd4681794857c2c450b7354575ee` (111563 bytes).
- 2ecf-r262-adjacent-compensated-heat-cut-refinement.py: SHA-256 `2f318cd9a7afde09d8e5116a1b2ec3237a27184a7de1ae4c4a3643c65c0c0a8d` (10472 bytes).
- 2ecf-adjacent-positive-heat-orbit.py: SHA-256 `67f0d8cb4fa8c4538496a0fcfb14046d039f4f17ed774e4e1dfade7c08967180` (5858 bytes).
- 2ecf-r262-adjacent-low-ports-support-physical-cut.py: SHA-256 `94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6` (12244 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- 2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py: SHA-256 `ffa687858a059ab60e14987d55acdd1a7d63c62855f7804f2d2ccc2966cebfd0` (14160 bytes).
- 2ecf-r262-adjacent-cut-true-normal-angle-cauchy-refinement.py: SHA-256 `4a04812dce749f7973e2431fac484e9fabeba194f5cc7a59b226b71cd8b9eafa` (14237 bytes).
- h1-physical-heat.json: SHA-256 `155750433eb570c1d254849ce59060e53deeea1a58a4ac0b2d419799a1747e5f` (11116 bytes).
- h1-physical-heat.npz: SHA-256 `9e24574c94ca05816cb3c1c54d90fd74a4aa0605d0cdc8d37b4379b14d2f9325` (19386 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
