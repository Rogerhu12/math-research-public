# R262-true-full-gate-frozen-h2

**数值记录。** 2026-11-28 17:29:47 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `e97e14f214903f676e8a29d1a4fac27596ff066d`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

真实同g加密：每个实际物理B样条单元增加独立径行，覆盖完整cut过渡门；旧父场先在该完整新网观察，Boehm准确包含后40→80单元和30→48角频，仅更改空间位置。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-true-full-gate-frozen-h2；实际源码逐文件摘要列于下方。开始 2026-11-28 17:28:37 UTC，结束 2026-11-28 17:29:47 UTC。退出码 0。

```json
{
  "entrySHA256": "494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "parentSHA256": "a405277f3c7b1d6ce22c2edc490be177d9f6c3f74d9fba0505bfa5acae30b586",
  "stateSHA256": "9a3958fa2f008855599a34e01cb96090dbffeaf741502c34e714152ad140332e",
  "angularModes": 48,
  "radialSpans": 80,
  "actualPositionDOFs": 3871,
  "metricDOFs": 0,
  "knotTransferMaxActual0th1st2nd": [
    2.7755575615628914e-17,
    2.8189256484623115e-16,
    3.6415315207705135e-14
  ],
  "initialTraining": {
    "peak": 0.01030942842433737,
    "rms": 0.001811013696979847,
    "curvature": 7.557625711668868,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.9924320065529171,
    "worstPhysicalRadialAndNativeTheta": [
      0.8377570183769978,
      4.7414778012512615
    ],
    "radialRows": 663,
    "angles": 216
  },
  "initialShifted": {
    "peak": 0.010340117865199902,
    "rms": 0.001865375135033428,
    "curvature": 7.557244245279068,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.9924284456611386,
    "worstPhysicalRadialAndNativeTheta": [
      0.9729693735215966,
      4.961954751931542
    ],
    "radialRows": 787,
    "angles": 321
  },
  "initialGeometry": {
    "minimumOutwardSupport": 0.3693948240199602,
    "at": [
      0.9970333333333335,
      5.410520681182421
    ],
    "minimumRadialHeightDerivative": 0.22910628349630677,
    "heightRange": [
      0.0,
      1.772114288708474
    ],
    "maximumOriginNorm": 1.893608773515887,
    "minimumArea": 0.11999999946243713
  },
  "training": {
    "peak": 0.010201683469556777,
    "rms": 0.001738081873253985,
    "curvature": 7.584558968381117,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.9927230131384456,
    "worstPhysicalRadialAndNativeTheta": [
      0.8983345044847391,
      4.828744263850979
    ],
    "radialRows": 663,
    "angles": 216
  },
  "independent": {
    "peak": 0.010182982483804505,
    "rms": 0.001790138562363982,
    "curvature": 7.462058638871766,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.9926969776634537,
    "worstPhysicalRadialAndNativeTheta": [
      0.9007000000000001,
      4.82493824990582
    ],
    "radialRows": 787,
    "angles": 321
  },
  "independentGeometry": {
    "minimumOutwardSupport": 0.3612571174517064,
    "at": [
      0.9989751514295642,
      5.412151830016061
    ],
    "minimumRadialHeightDerivative": 0.22961953989471567,
    "heightRange": [
      0.0,
      1.7721142740452964
    ],
    "maximumOriginNorm": 1.8935967213138116,
    "minimumArea": 0.12020687651814196
  },
  "accepted": {
    "actualCompletedSteps": 1
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- low35-h2.json: SHA-256 `38ac7a51880b2ba90a0a5392b0a563b1a63b03dab5d632980dc28651eb58df52` (5868 bytes).
- low35-h2.npz: SHA-256 `9a3958fa2f008855599a34e01cb96090dbffeaf741502c34e714152ad140332e` (73143 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
