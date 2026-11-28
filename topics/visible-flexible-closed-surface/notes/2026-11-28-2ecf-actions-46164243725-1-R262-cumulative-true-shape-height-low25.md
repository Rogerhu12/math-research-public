# R262-cumulative-true-shape-height-low25

**数值记录。** 2026-11-28 18:18:40 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `4bfe369fa7d1bd358cf3f3e64b92fbc9f74214bd`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

真实新输入：R311中央半高.545，全部原圈保留；实际累计B样条降量、全角Rayleigh与R312三形状量一同进入线性设计，原场和真实XYZ新位置继续消费。该支重新选g；不计为旧cut固定g的精化。LP不可行时如实登记具体原因后换输入。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-cumulative-true-shape-height-low25；实际源码逐文件摘要列于下方。开始 2026-11-28 18:18:20 UTC，结束 2026-11-28 18:18:40 UTC。退出码 0。

```json
{
  "schema": "R262-cumulative-height-and-strong-shape-affine-LP-with-physical-XYZ-v1",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "b489b460892563eda8dd85fdaef7570631634408f63523fac74bafea544a7d6b",
  "sourceSHA": "b60d62963ed27a7d108bab8a1bb404d51f489481b813508f163c549ae31aced8",
  "lam": 1.0,
  "low": 0.25,
  "nativeD3Correction": {
    "angularModes": 18,
    "radialSpans": 20,
    "independentRealPositionVariables": 361,
    "positiveMetricVariables": 38
  },
  "initialTrueShapeObservations": {
    "plane": 0.5426990506963667,
    "sphere": 0.00494201083602297,
    "mixed": 0.037602947200167325,
    "exteriorZ": 0.19700000000000006,
    "least": 0.00494201083602297
  },
  "finalTrueShapeObservations": {
    "plane": 0.549062147653264,
    "sphere": 0.004772160599830766,
    "mixed": 0.0377785356384579,
    "exteriorZ": 0.19700000000000006,
    "least": 0.004772160599830766
  },
  "initial": {
    "peak": 0.06606221097475631,
    "rms": 0.02629855836384633,
    "curvature": 10.111463215228,
    "positiveMetricCoefficientLower": 0.020000000000000018,
    "areaRatioMinimum": 0.9706804583095567,
    "worstPhysicalRadialAndNativeTheta": [
      0.8239388958327336,
      5.026548245743669
    ],
    "radialRows": 161,
    "angles": 120
  },
  "finalTraining": {
    "peak": 0.03973670180986266,
    "rms": 0.013558904410442156,
    "curvature": 10.086733153739527,
    "positiveMetricCoefficientLower": 0.009751275165955198,
    "areaRatioMinimum": 0.984915853235849,
    "worstPhysicalRadialAndNativeTheta": [
      0.29348359767659804,
      1.0471975511965976
    ],
    "radialRows": 161,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.03974656978640301,
    "rms": 0.013535115015281665,
    "curvature": 10.222205745714234,
    "positiveMetricCoefficientLower": 0.009751275165955198,
    "areaRatioMinimum": 0.9831589639163951,
    "worstPhysicalRadialAndNativeTheta": [
      0.29443338278234754,
      5.235987755982988
    ],
    "radialRows": 244,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.4984786835813948,
    "minimumAbsoluteHeight": 0.545,
    "heightRange": [
      0.545,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.23131617419293615,
    "maximumOriginNorm": 1.9102278394001693,
    "minimumArea": 0.11282105131136308,
    "leastSupportAtPrefixParameterAndNativeTheta": [
      0.4318356280807764,
      5.235987755982988
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
- low25.json: SHA-256 `ac096363db0560855b9700285b35401499e681c9679b9e80365b22388d5f6c14` (11029 bytes).
- low25.npz: SHA-256 `b489b460892563eda8dd85fdaef7570631634408f63523fac74bafea544a7d6b` (11631 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
