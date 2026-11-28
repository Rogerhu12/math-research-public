# R322-width060-two-moment-actual-frozen-full-span-h1

**数值记录。** 2026-11-28 17:27:00 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `70a3bc950b2229e08623eae09224de37e2dd6716`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

R322新.060两矩真实母线自己的g固定后做实际Boehm和角精化。每span独立径行、769加全六个真实法角窗观察，完整原X+C+W与全部新XYZ保持自己的源身份；不当作R317旧g的精化。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R322-width060-two-moment-actual-frozen-full-span-h1；实际源码逐文件摘要列于下方。开始 2026-11-28 17:26:15 UTC，结束 2026-11-28 17:27:00 UTC。退出码 0。

```json
{
  "entrySHA256": "e0af8a9fbff62592d14091d6701deec3bcd5052eb6ea7fec0445b89f4791ed97",
  "physicalSourceSHA256": "e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "parentSHA256": "c986b8d94d933bf9fd5a280f90ce860b318e78d59763945a508a3a9da20b3c98",
  "stateSHA256": "100f7c8b312cb8be95cb8a46db340345ee560e4ba0d1ad7bc13da05cd49d2a9a",
  "angularModes": 30,
  "radialSpans": 40,
  "actualPositionDOFs": 1209,
  "metricDOFs": 0,
  "knotTransferMaxActual0th1st2nd": [
    5.204170427930421e-18,
    5.551115123125783e-17,
    1.1657341758564144e-15
  ],
  "initialTraining": {
    "peak": 0.0076056723050109696,
    "rms": 0.0008031204237892689,
    "curvature": 4.3916994598962855,
    "positiveMetricCoefficientLower": 0.9666693638357047,
    "areaRatioMinimum": 0.996340856778301,
    "worstPhysicalRadialAndNativeTheta": [
      0.4752373555555555,
      3.5682286929661844
    ],
    "radialRows": 290,
    "angles": 162
  },
  "initialShifted": {
    "peak": 0.007605770894065563,
    "curvature": 4.391667381895644,
    "areaRatioMinimum": 0.9963219905955679,
    "worstPhysicalRadialAndNativeTheta": [
      0.47366467407407403,
      5.6663056053693674
    ],
    "positiveMetricCoefficientLower": 0.9666693638357047,
    "minimumOutwardSupport": 0.5988221405064631,
    "minimumRadialHeightDerivative": 0.2282882108788585,
    "heightRange": [
      0.0,
      1.7721142884249084
    ],
    "maximumOriginNorm": 1.8932256639131697,
    "minimumArea": 0.12000400497223701,
    "uniformPeak": 0.007605770894065563,
    "additionalTransitionPeak": 0.006162157506650493,
    "rms": 0.000818402360630475,
    "radialRows": 413,
    "angles": 847,
    "uniformShiftedNativeAngles": 769,
    "actualMaterialTransitionAngles": 78,
    "maximumNativeAngleInversionError": 8.881784197001252e-16,
    "radialCoverage": {
      "interiorPerActualSpan": 9,
      "numberOfSpans": 41,
      "sampledActualSpans": [
        0.35,
        2.021775895105453
      ],
      "gateInteriorRows": 59
    }
  },
  "initialGeometry": {
    "minimumOutwardSupport": 0.5989761564115741,
    "at": [
      0.5641262444444445,
      1.0471975511965976
    ],
    "minimumRadialHeightDerivative": 0.22828609892079824,
    "heightRange": [
      0.0,
      1.772114288708474
    ],
    "maximumOriginNorm": 1.8932207602632836,
    "minimumArea": 0.11999999946243713
  },
  "accepted": {
    "actualCompletedSteps": 3
  },
  "training": {
    "peak": 0.0026887825067702887,
    "rms": 0.0004438181840330702,
    "curvature": 7.937980739062683,
    "positiveMetricCoefficientLower": 0.9666693638357047,
    "areaRatioMinimum": 0.9985691246629761,
    "worstPhysicalRadialAndNativeTheta": [
      0.4641262444444444,
      5.1972026614942255
    ],
    "radialRows": 290,
    "angles": 162
  },
  "independent": {
    "peak": 0.0026971963690405904,
    "curvature": 7.9377033358221745,
    "areaRatioMinimum": 0.9985572632339671,
    "worstPhysicalRadialAndNativeTheta": [
      0.4662572666666666,
      3.0843985090510975
    ],
    "positiveMetricCoefficientLower": 0.9666693638357047,
    "minimumOutwardSupport": 0.5930142274424429,
    "minimumRadialHeightDerivative": 0.2255114895050522,
    "heightRange": [
      0.0,
      1.7721142884249084
    ],
    "maximumOriginNorm": 1.8931429611976693,
    "minimumArea": 0.12000400497223701,
    "uniformPeak": 0.0026971963690405904,
    "additionalTransitionPeak": 0.00255614079119695,
    "rms": 0.00044022183431375185,
    "radialRows": 413,
    "angles": 847,
    "uniformShiftedNativeAngles": 769,
    "actualMaterialTransitionAngles": 78,
    "maximumNativeAngleInversionError": 8.881784197001252e-16,
    "radialCoverage": {
      "interiorPerActualSpan": 9,
      "numberOfSpans": 41,
      "sampledActualSpans": [
        0.35,
        2.021775895105453
      ],
      "gateInteriorRows": 59
    }
  },
  "independentGeometry": {
    "minimumOutwardSupport": 0.5930142274424429,
    "minimumRadialHeightDerivative": 0.2255114895050522,
    "heightRange": [
      0.0,
      1.7721142884249084
    ],
    "maximumOriginNorm": 1.8931429611976693,
    "minimumArea": 0.12000400497223701
  },
  "trainingActualSpanCoverage": {
    "interiorPerActualSpan": 6,
    "numberOfSpans": 41,
    "sampledActualSpans": [
      0.35,
      2.021775895105453
    ],
    "gateInteriorRows": 41
  },
  "trueSpatialMomentCoefficients": [
    -0.5190218744366847,
    -0.5511349532277711
  ],
  "trueNormalEndpointAngles": [
    0.536,
    0.596
  ],
  "R317SourceSHA": "94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6"
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-two-moment-060-frozen-metric-refinement.py: SHA-256 `e0af8a9fbff62592d14091d6701deec3bcd5052eb6ea7fec0445b89f4791ed97` (16735 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- 2ecf-r262-two-moment-060-frozen-metric-refinement.py: SHA-256 `e0af8a9fbff62592d14091d6701deec3bcd5052eb6ea7fec0445b89f4791ed97` (16735 bytes).
- fixed-h1.json: SHA-256 `f97f7ce7e3c795b91990dd76aa228f46a4dfd5d12ec69b41342fb00bade0ae6b` (8751 bytes).
- fixed-h1.npz: SHA-256 `100f7c8b312cb8be95cb8a46db340345ee560e4ba0d1ad7bc13da05cd49d2a9a` (26225 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
