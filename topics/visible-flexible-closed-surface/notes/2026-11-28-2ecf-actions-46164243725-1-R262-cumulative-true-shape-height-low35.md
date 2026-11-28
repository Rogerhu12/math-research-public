# R262-cumulative-true-shape-height-low35

**数值记录。** 2026-11-28 18:18:15 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `69fdd5ba5a1f1ebec4ead44dfd2fba24d93b0d8d`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

真实新输入：R311中央半高.545，全部原圈保留；实际累计B样条降量、全角Rayleigh与R312三形状量一同进入线性设计，原场和真实XYZ新位置继续消费。该支重新选g；不计为旧cut固定g的精化。LP不可行时如实登记具体原因后换输入。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-cumulative-true-shape-height-low35；实际源码逐文件摘要列于下方。开始 2026-11-28 18:17:55 UTC，结束 2026-11-28 18:18:15 UTC。退出码 0。

```json
{
  "schema": "R262-cumulative-height-and-strong-shape-affine-LP-with-physical-XYZ-v1",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "561a62430d3540545254d586f6ecd382126e4159b3d62de1d7a3c049f0f983c3",
  "sourceSHA": "b60d62963ed27a7d108bab8a1bb404d51f489481b813508f163c549ae31aced8",
  "lam": 1.0,
  "low": 0.35,
  "nativeD3Correction": {
    "angularModes": 18,
    "radialSpans": 20,
    "independentRealPositionVariables": 361,
    "positiveMetricVariables": 38
  },
  "initialTrueShapeObservations": {
    "plane": 0.4066592804635829,
    "sphere": -6.047743660442251e-05,
    "mixed": 0.1572576526449625,
    "exteriorZ": 0.19700000000000006,
    "least": -6.047743660442251e-05
  },
  "finalTrueShapeObservations": {
    "plane": 0.40668697451946434,
    "sphere": -0.00010538092398926224,
    "mixed": 0.1572648405822541,
    "exteriorZ": 0.19700000000000006,
    "least": -0.00010538092398926224
  },
  "initial": {
    "peak": 0.056101321417102,
    "rms": 0.016864973342442316,
    "curvature": 8.871963164230525,
    "positiveMetricCoefficientLower": 0.020000000000000018,
    "areaRatioMinimum": 0.9678642420527078,
    "worstPhysicalRadialAndNativeTheta": [
      1.0434972361834598,
      3.1415926535897927
    ],
    "radialRows": 161,
    "angles": 120
  },
  "finalTraining": {
    "peak": 0.056101321417102,
    "rms": 0.016864973342442316,
    "curvature": 8.871963164230525,
    "positiveMetricCoefficientLower": 0.020000000000000018,
    "areaRatioMinimum": 0.9678642420527078,
    "worstPhysicalRadialAndNativeTheta": [
      1.0434972361834598,
      3.1415926535897927
    ],
    "radialRows": 161,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.056060805665970825,
    "rms": 0.016859387761940365,
    "curvature": 8.871963164230525,
    "positiveMetricCoefficientLower": 0.020000000000000018,
    "areaRatioMinimum": 0.9678953003426711,
    "worstPhysicalRadialAndNativeTheta": [
      1.0403312858309615,
      3.141592653589793
    ],
    "radialRows": 244,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.5496735510835931,
    "minimumAbsoluteHeight": 0.545,
    "heightRange": [
      0.545,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.23171934281618614,
    "maximumOriginNorm": 1.8941053809239892,
    "minimumArea": 0.10216188661818479,
    "leastSupportAtPrefixParameterAndNativeTheta": [
      0.27480449059685774,
      3.141592653589793
    ],
    "scope": "finite actual physical prefix; global radial offsets remain in the source metadata"
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-cumulative-shape-constrained-height-design.py: SHA-256 `b60d62963ed27a7d108bab8a1bb404d51f489481b813508f163c549ae31aced8` (23321 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `91b0653ff3423fec27402e6f4b25cab1ebaefd4681794857c2c450b7354575ee` (111563 bytes).
- 2ecf-r262-cumulative-shape-constrained-height-design.py: SHA-256 `b60d62963ed27a7d108bab8a1bb404d51f489481b813508f163c549ae31aced8` (23321 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- low35.json: SHA-256 `2b1886346d4df8c9de08927076b90a4b1248fb141a3ab06d58d1b4843589207a` (10446 bytes).
- low35.npz: SHA-256 `561a62430d3540545254d586f6ecd382126e4159b3d62de1d7a3c049f0f983c3` (5277 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
