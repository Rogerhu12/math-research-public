# R262-adjacent-low-ports-actual-frozen-metric-h1

**数值记录。** 2026-11-28 17:21:33 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `76f531ca7f1f1097ab3a71948cada8c46bde630c`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

R319真.350中央/原U0、完整cut及原场身份保持。每个实际细span训练≥6新径行、独立≥9不同径行，门内不复用13旧行；独立769均匀native角加6个.012法角窗的78个真逆材料角，全部源和XYZ直接六jets，分8径行消费。固定同一g真Boehm/角扩充后的实际误差，非连续证书。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-adjacent-low-ports-actual-frozen-metric-h1；实际源码逐文件摘要列于下方。开始 2026-11-28 17:20:48 UTC，结束 2026-11-28 17:21:33 UTC。退出码 0。

```json
{
  "entrySHA256": "3d8e26872bd4a0347ed417b8c37cfb1e50c935e50572e423d639c33857217bf8",
  "physicalSourceSHA256": "94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "parentSHA256": "c3b6b1ff7396223ea6c3923e5b27e1939442b754a9e65e1c3d7266477cf3275c",
  "stateSHA256": "104a8843272816e31129ff8fabce2dbfad6ad98b41f16975496f91dc1b19181d",
  "angularModes": 30,
  "radialSpans": 40,
  "actualPositionDOFs": 1209,
  "metricDOFs": 0,
  "knotTransferMaxActual0th1st2nd": [
    5.204170427930421e-18,
    5.551115123125783e-17,
    1.1102230246251565e-15
  ],
  "initialTraining": {
    "peak": 0.007482377162313232,
    "rms": 0.0007504401202161538,
    "curvature": 8.07261620978463,
    "positiveMetricCoefficientLower": 0.967089044875546,
    "areaRatioMinimum": 0.9966782162208474,
    "worstPhysicalRadialAndNativeTheta": [
      0.4752373555555555,
      3.5682286929661844
    ],
    "radialRows": 290,
    "angles": 162
  },
  "initialShifted": {
    "peak": 0.00750402039695887,
    "curvature": 8.06984170194474,
    "areaRatioMinimum": 0.9966552685028239,
    "worstPhysicalRadialAndNativeTheta": [
      0.47366467407407403,
      3.558292849514577
    ],
    "positiveMetricCoefficientLower": 0.967089044875546,
    "minimumOutwardSupport": 0.5973602433589823,
    "minimumRadialHeightDerivative": 0.22830347104712057,
    "heightRange": [
      0.0,
      1.7721142884249084
    ],
    "maximumOriginNorm": 1.8932263584095375,
    "minimumArea": 0.12000400497223701,
    "uniformPeak": 0.00750402039695887,
    "additionalTransitionPeak": 0.005110677859469857,
    "rms": 0.0007722372173679903,
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
    "minimumOutwardSupport": 0.597510062042782,
    "at": [
      0.5641262444444445,
      1.0471975511965976
    ],
    "minimumRadialHeightDerivative": 0.22830190576858425,
    "heightRange": [
      0.0,
      1.772114288708474
    ],
    "maximumOriginNorm": 1.8932214813334172,
    "minimumArea": 0.11999999946243713
  },
  "accepted": {
    "actualCompletedSteps": 3
  },
  "training": {
    "peak": 0.004968847584416945,
    "rms": 0.0005432173500282422,
    "curvature": 8.667429412838755,
    "positiveMetricCoefficientLower": 0.967089044875546,
    "areaRatioMinimum": 0.997255666972581,
    "worstPhysicalRadialAndNativeTheta": [
      0.4752373555555555,
      3.5682286929661844
    ],
    "radialRows": 290,
    "angles": 162
  },
  "independent": {
    "peak": 0.005014478377888508,
    "curvature": 8.663717095207275,
    "areaRatioMinimum": 0.9972368395896155,
    "worstPhysicalRadialAndNativeTheta": [
      0.47366467407407403,
      3.550122257437621
    ],
    "positiveMetricCoefficientLower": 0.967089044875546,
    "minimumOutwardSupport": 0.5954115961289634,
    "minimumRadialHeightDerivative": 0.22780022393956267,
    "heightRange": [
      0.0,
      1.7721142884249084
    ],
    "maximumOriginNorm": 1.8931956513783934,
    "minimumArea": 0.12000400497223701,
    "uniformPeak": 0.005014478377888508,
    "additionalTransitionPeak": 0.0041413674744318636,
    "rms": 0.0005661085030605615,
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
    "minimumOutwardSupport": 0.5954115961289634,
    "minimumRadialHeightDerivative": 0.22780022393956267,
    "heightRange": [
      0.0,
      1.7721142884249084
    ],
    "maximumOriginNorm": 1.8931956513783934,
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
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-adjacent-low-ports-frozen-metric-refinement.py: SHA-256 `3d8e26872bd4a0347ed417b8c37cfb1e50c935e50572e423d639c33857217bf8` (16657 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `7693790913541fcf9e6f45501cc30d10b9e7478b7393d9badd9e6e8f1d90bb12` (66092 bytes).
- 2ecf-r262-adjacent-low-ports-frozen-metric-refinement.py: SHA-256 `3d8e26872bd4a0347ed417b8c37cfb1e50c935e50572e423d639c33857217bf8` (16657 bytes).
- fixed-h1.json: SHA-256 `e5d629cc49f24312703b943e455cfbf3f5887b54ffc1c94087e9582801257bd8` (8571 bytes).
- fixed-h1.npz: SHA-256 `104a8843272816e31129ff8fabce2dbfad6ad98b41f16975496f91dc1b19181d` (26186 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
