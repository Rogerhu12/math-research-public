# R262-actual-cut-curvature-continuation-25

**数值记录。** 2026-11-28 18:22:10 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `df9158623426311c6e931bbb6bcb1582e1a249b5`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

真正的全幅曲率原函数和收缩cut连续输入，第1个实际幅度lambda=.25，最终c=.545/low=.35。原物理材料角两jets和新空间位置保持一致，使用上一真实态/割线作初值；各步可选择自己的g，只有最终态再固定g加密。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-actual-cut-curvature-continuation-25；实际源码逐文件摘要列于下方。开始 2026-11-28 18:21:45 UTC，结束 2026-11-28 18:22:10 UTC。退出码 0。

```json
{
  "sourceSHA": "ca24a872478c3a0f577317e16481f7de01d781b2c49db5b433124a58daa72231",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "0b8205e328c7f9b64c1b01cdf4034ef2124b36f487f4144a9f78fdde760b8ed7",
  "lam": 0.25,
  "low": 0.35,
  "numericalPhysicalCoordinates": {
    "S": 2.021775895105453,
    "T": 2.4717758951054534,
    "halfSleeve": 0.13625,
    "gateLength": 0.1,
    "liftEnd": 1.5
  },
  "nativeD3Correction": {
    "angularModes": 18,
    "radialSpans": 20,
    "independentRealPositionVariables": 361,
    "positiveMetricVariables": 38
  },
  "initial": {
    "peak": 0.16377335190015363,
    "rms": 0.014195407541090258,
    "curvature": 11.74105324436316,
    "positiveMetricCoefficientLower": 1.0,
    "areaRatioMinimum": 0.9978271758925927,
    "worstPhysicalRadialAndNativeTheta": [
      0.19875,
      3.1415926535897927
    ],
    "radialRows": 178,
    "angles": 120
  },
  "accepted": {
    "actualCompletedSteps": 5
  },
  "finalTraining": {
    "peak": 0.0025461088198060664,
    "rms": 0.0005223191980132078,
    "curvature": 6.171903659143913,
    "positiveMetricCoefficientLower": 0.9699317604551138,
    "areaRatioMinimum": 0.9983725734985615,
    "worstPhysicalRadialAndNativeTheta": [
      0.3802440237988269,
      3.4033920413889422
    ],
    "radialRows": 178,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.002980203675133766,
    "rms": 0.0005298609378869409,
    "curvature": 6.128951977343679,
    "positiveMetricCoefficientLower": 0.9699317604551138,
    "areaRatioMinimum": 0.9983332282921334,
    "worstPhysicalRadialAndNativeTheta": [
      0.3693323523953841,
      5.525980924006662
    ],
    "radialRows": 260,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.7762842733865514,
    "minimumAbsoluteHeight": 0.0,
    "heightRange": [
      0.0,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.23166331104357107,
    "maximumOriginNorm": 1.8929905124757471,
    "minimumArea": 0.12056053070089826,
    "leastSupportAtPrefixParameterAndNativeTheta": [
      0.3693323523953841,
      1.0471975511965976
    ],
    "scope": "finite actual physical prefix; global radial offsets remain in the source metadata"
  },
  "predictor": "zero"
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-true-three-arcs-cut-amplitude-continuation.py: SHA-256 `ca24a872478c3a0f577317e16481f7de01d781b2c49db5b433124a58daa72231` (17296 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `91b0653ff3423fec27402e6f4b25cab1ebaefd4681794857c2c450b7354575ee` (111563 bytes).
- 2ecf-r262-true-three-arcs-cut-amplitude-continuation.py: SHA-256 `ca24a872478c3a0f577317e16481f7de01d781b2c49db5b433124a58daa72231` (17296 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- c545-low35-lam25.json: SHA-256 `882b115e0297541f4af82ea3864ce10b8b0de97929406f39cceae8e0c8d3338b` (10565 bytes).
- c545-low35-lam25.npz: SHA-256 `0b8205e328c7f9b64c1b01cdf4034ef2124b36f487f4144a9f78fdde760b8ed7` (10882 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
