# R262-actual-cut-curvature-continuation-75

**数值记录。** 2026-11-28 18:23:15 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `4ce6265f87578e1254a35deece0104ab05f1616f`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

真正的全幅曲率原函数和收缩cut连续输入，第3个实际幅度lambda=.75，最终c=.545/low=.35。原物理材料角两jets和新空间位置保持一致，使用上一真实态/割线作初值；各步可选择自己的g，只有最终态再固定g加密。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-actual-cut-curvature-continuation-75；实际源码逐文件摘要列于下方。开始 2026-11-28 18:22:50 UTC，结束 2026-11-28 18:23:15 UTC。退出码 0。

```json
{
  "sourceSHA": "ca24a872478c3a0f577317e16481f7de01d781b2c49db5b433124a58daa72231",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "0d9683df4ff2f1da7d671f80a13bce2185c52b5d1e73729cb3ce60b37a0cb75f",
  "lam": 0.75,
  "low": 0.35,
  "numericalPhysicalCoordinates": {
    "S": 2.021775895105453,
    "T": 2.4717758951054534,
    "halfSleeve": 0.40875000000000006,
    "gateLength": 0.30000000000000004,
    "liftEnd": 1.5
  },
  "nativeD3Correction": {
    "angularModes": 18,
    "radialSpans": 20,
    "independentRealPositionVariables": 361,
    "positiveMetricVariables": 38
  },
  "initial": {
    "peak": 0.06863217001058944,
    "rms": 0.014095340691534881,
    "curvature": 7.24919782329666,
    "positiveMetricCoefficientLower": 0.8467075222703985,
    "areaRatioMinimum": 0.971817050968255,
    "worstPhysicalRadialAndNativeTheta": [
      1.3924341124466024,
      3.508111796508602
    ],
    "radialRows": 178,
    "angles": 120
  },
  "accepted": {
    "actualCompletedSteps": 5
  },
  "finalTraining": {
    "peak": 0.004845703805719309,
    "rms": 0.0008204845060989127,
    "curvature": 8.418417653907632,
    "positiveMetricCoefficientLower": 0.8764072420254753,
    "areaRatioMinimum": 0.9968811994074805,
    "worstPhysicalRadialAndNativeTheta": [
      0.7994546759473655,
      5.497787143782138
    ],
    "radialRows": 178,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.006463366319072206,
    "rms": 0.00080741331433718,
    "curvature": 8.298180255353714,
    "positiveMetricCoefficientLower": 0.8764072420254753,
    "areaRatioMinimum": 0.9968865764861178,
    "worstPhysicalRadialAndNativeTheta": [
      0.7938672223458167,
      5.525980924006662
    ],
    "radialRows": 260,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.3226940986553159,
    "minimumAbsoluteHeight": 0.0,
    "heightRange": [
      0.0,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.2593064911871038,
    "maximumOriginNorm": 1.8997377298897007,
    "minimumArea": 0.12056053070089826,
    "leastSupportAtPrefixParameterAndNativeTheta": [
      0.8234804180189232,
      1.0471975511965976
    ],
    "scope": "finite actual physical prefix; global radial offsets remain in the source metadata"
  },
  "predictor": "two-state secant on corresponding gate and outer control rows",
  "seedSHA256": "8869693cc2bd99b13bb29641434fa23e535b95a6fab5aefb6ce4d5fe4421a2f5",
  "previousSHA256": "0b8205e328c7f9b64c1b01cdf4034ef2124b36f487f4144a9f78fdde760b8ed7"
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-true-three-arcs-cut-amplitude-continuation.py: SHA-256 `ca24a872478c3a0f577317e16481f7de01d781b2c49db5b433124a58daa72231` (17296 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `91b0653ff3423fec27402e6f4b25cab1ebaefd4681794857c2c450b7354575ee` (111563 bytes).
- 2ecf-r262-true-three-arcs-cut-amplitude-continuation.py: SHA-256 `ca24a872478c3a0f577317e16481f7de01d781b2c49db5b433124a58daa72231` (17296 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- c545-low35-lam75.json: SHA-256 `5d0083dd2f29cd76df452972e89a6ab42a036c5971d4c162ba1579c13d8999bc` (10847 bytes).
- c545-low35-lam75.npz: SHA-256 `0d9683df4ff2f1da7d671f80a13bce2185c52b5d1e73729cb3ce60b37a0cb75f` (10872 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
