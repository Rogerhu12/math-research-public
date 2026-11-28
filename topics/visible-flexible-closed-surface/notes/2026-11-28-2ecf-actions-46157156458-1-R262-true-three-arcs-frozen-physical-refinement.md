# R262-true-three-arcs-frozen-physical-refinement

**数值记录。** 2026-11-28 16:00:20 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46157156458](https://github.com/Rogerhu12/math-research-public/actions/runs/46157156458), attempt 1；计算源码提交 `028e568341f1fa8c5109f4df08a5ddaa475ca5c6`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

选择两次已公布完整设计中独立谱峰较小者，保留两条整连续正目标；对每个真实物理单元插入中点，角模式18到30，实际Boehm包含后只更新空间。

```json
{
  "schema": "R262-three-true-circular-arcs-frozen-physical-metric-h-refinement-v1",
  "entrySHA256": "0ac91cf431ec69f6246d490931dac97d37004d84b9d5438b633f2a302256640f",
  "physicalSourceSHA256": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
  "comparisonSHA256": "a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e",
  "parentSHA256": "538a7ecc1c65ae01d070056eb7b7fdd5b495e1083bce6c038a34bef1ed01d49b",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "historicalMatch": false,
  "stateSHA256": "a405277f3c7b1d6ce22c2edc490be177d9f6c3f74d9fba0505bfa5acae30b586",
  "low": 0.35,
  "high": 1.5497530223978673,
  "lam": 1.0,
  "anchor": 1.0471975511965976,
  "angularModes": 30,
  "radialSpans": 40,
  "actualPositionDOFs": 1209,
  "metricDOFs": 0,
  "knotTransferMaxActual0th1st2nd": [
    1.734723475976807e-17,
    1.942890293094024e-16,
    6.217248937900877e-15
  ],
  "initialTraining": {
    "peak": 0.025626058246238134,
    "rms": 0.0016910998849183365,
    "curvature": 6.69338236652208,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.9875414300133353,
    "worstPhysicalRadialAndNativeTheta": [
      0.9133333333333334,
      4.964492094561648
    ],
    "radialRows": 228,
    "angles": 162
  },
  "initialShifted": {
    "peak": 0.026778846455874732,
    "rms": 0.001491763021817351,
    "curvature": 6.6958577058485,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.987439548302391,
    "worstPhysicalRadialAndNativeTheta": [
      0.9133333333333334,
      4.959803786436633
    ],
    "radialRows": 384,
    "angles": 273
  },
  "initialGeometry": {
    "minimumOutwardSupport": 0.2953694783566644,
    "at": [
      0.9800000000000001,
      3.141592653589793
    ],
    "minimumRadialHeightDerivative": 0.19783123037361366,
    "heightRange": [
      0.0,
      1.772114288708474
    ],
    "maximumOriginNorm": 1.8946830787114195,
    "minimumArea": 0.11999999946243713
  },
  "accepted": {
    "acceptedSteps": 4
  },
  "training": {
    "peak": 0.009808166978255303,
    "rms": 0.0011783879046821995,
    "curvature": 7.518247366852215,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.9926156583265625,
    "worstPhysicalRadialAndNativeTheta": [
      0.8466666666666667,
      4.731781527629071
    ],
    "radialRows": 228,
    "angles": 162
  },
  "independent": {
    "peak": 0.010603353774122486,
    "rms": 0.0010689757419913898,
    "curvature": 7.5503286161470955,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.992612052586979,
    "worstPhysicalRadialAndNativeTheta": [
      0.9800000000000001,
      4.959803786436633
    ],
    "radialRows": 384,
    "angles": 273
  },
  "independentGeometry": {
    "minimumOutwardSupport": 0.3819383308203389,
    "at": [
      1.0133333333333334,
      5.397095071551695
    ],
    "minimumRadialHeightDerivative": 0.2290868826509428,
    "heightRange": [
      0.0,
      1.7721142684268067
    ],
    "maximumOriginNorm": 1.8936070260477276,
    "minimumArea": 0.12028601205932246
  },
  "scope": "The genuine full plateaux, original material angle, compact cut and both fixed radial functions are retained. Reports are finite grid observations; strict geometry and continuous Gram bounds are separate."
}
```


## 可重算输出的身份

- three-arcs-low35.json: SHA-256 `6eb4be1404f4531d40d15e5c70ab37e184d1128599b19212b7513aaae9af5a4d` (9831 bytes).
- three-arcs-low35.npz: SHA-256 `538a7ecc1c65ae01d070056eb7b7fdd5b495e1083bce6c038a34bef1ed01d49b` (10895 bytes).
- three-arcs-low35-fixed-h1.json: SHA-256 `b31ffc1008184747f18ea1f45f4a4fe224f9720be75e768a8f8bbb097cf27917` (7283 bytes).
- three-arcs-low35-fixed-h1.npz: SHA-256 `a405277f3c7b1d6ce22c2edc490be177d9f6c3f74d9fba0505bfa5acae30b586` (25990 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
