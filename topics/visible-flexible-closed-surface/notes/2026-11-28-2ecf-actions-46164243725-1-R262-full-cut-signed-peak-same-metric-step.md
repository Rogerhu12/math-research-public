# R262-full-cut-signed-peak-same-metric-step

**数值记录。** 2026-11-28 17:33:41 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `e271b4f28d1b5222ff14309935a9a12cdbeb5e84`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

同一既定g的真实峰特征方向约束：完整带状空间代价，加两真网30处正负极值特征行的低秩修正；精确矩阵二次Gram线搜索至1/8192并局部优化，实际κ参与接受。末411角网只作独立观察。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-full-cut-signed-peak-same-metric-step；实际源码逐文件摘要列于下方。开始 2026-11-28 17:31:46 UTC，结束 2026-11-28 17:33:41 UTC。退出码 0。

```json
{
  "entrySHA256": "fd5328daf8db8db3597b587a39935bb6ac0d2b41535c20c957c47b6c971246e1",
  "stateSHA256": "e3c6728a7f1d0b21a1368338ab28f1c4c4a960a378b63b9fc5dee8890889cf12",
  "parentSHA256": "8e4d090c855f1a5de8f4698ada7cf212c636dc7741480b807c50b33a5ff6cdce",
  "actualPositionVariables": 3871,
  "actualMetricVariables": 0,
  "normalAndRhsAgreement": [
    9.031402404028358e-16,
    4.3806215860714677e-16
  ],
  "exactQuadraticLineAgreement": 6.487865800153259e-16,
  "initial": {
    "peak": 0.01010191117666581,
    "rms": 0.0026350816654107582,
    "curvature": 8.688456671971686,
    "worstMetric": [
      0.8992104859301235,
      4.828744263850979,
      4.57815956497283
    ],
    "worstCurvature": [
      1.0412001088800613,
      2.0943951023931953,
      2.0943951023931944
    ],
    "minimumSupport": 0.35834634093050544,
    "minimumZs": 0.22977229191820284,
    "minimumArea": 0.11999999946243713
  },
  "initialIndependent": {
    "peak": 0.010076006501234058,
    "rms": 0.0027091053306020564,
    "curvature": 8.461984169789996,
    "worstMetric": [
      0.8966308851756504,
      4.82493824990582,
      4.573328521305147
    ],
    "worstCurvature": [
      1.0407043315691007,
      2.0846082093913583,
      2.0924365989450364
    ],
    "minimumSupport": 0.35830943051884256,
    "minimumZs": 0.22979464364554128,
    "minimumArea": 0.12020687651814196
  },
  "accepted": {
    "actualCompletedSteps": 4
  },
  "final": {
    "peak": 0.010022505219916794,
    "rms": 0.002631905923651728,
    "curvature": 8.676149830164992,
    "worstMetric": [
      0.8992104859301235,
      4.828744263850979,
      4.57815956497283
    ],
    "worstCurvature": [
      1.0412001088800613,
      2.0943951023931953,
      2.0943951023931944
    ],
    "minimumSupport": 0.3599412010768666,
    "minimumZs": 0.22791293560549475,
    "minimumArea": 0.11999999946243713
  },
  "secondaryAcceptanceGrid": {
    "peak": 0.009997527036372269,
    "rms": 0.0027046254047949103,
    "curvature": 8.605366914471903,
    "worstMetric": [
      0.9007000000000001,
      4.82493824990582,
      4.573328521305147
    ],
    "worstCurvature": [
      1.2443349964454815,
      5.059823681949916,
      4.925361856446887
    ],
    "minimumSupport": 0.35991263848603244,
    "minimumZs": 0.22786878283138703,
    "minimumArea": 0.12020687651814196
  },
  "initialFreshHoldout": {
    "peak": 0.01007086869790675,
    "rms": 0.0017735924808546485,
    "curvature": 8.549549942844255,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.9929201823133221,
    "worstPhysicalRadialAndNativeTheta": [
      0.9005098969933563,
      4.838511313193039
    ],
    "radialRows": 879,
    "angles": 411
  },
  "independent": {
    "peak": 0.00999128154479459,
    "rms": 0.0017698015473466557,
    "curvature": 8.559428586885812,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.9929758739040587,
    "worstPhysicalRadialAndNativeTheta": [
      0.8988384771176657,
      4.823223757701117
    ],
    "radialRows": 879,
    "angles": 411
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-cut-frozen-metric-active-eigenstrain.py: SHA-256 `fd5328daf8db8db3597b587a39935bb6ac0d2b41535c20c957c47b6c971246e1` (11512 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- 2ecf-r262-cut-frozen-metric-active-eigenstrain.py: SHA-256 `fd5328daf8db8db3597b587a39935bb6ac0d2b41535c20c957c47b6c971246e1` (11512 bytes).
- fixed-g-active-peaks.json: SHA-256 `458e7e7252f2e21d1559eb6787ffa0ba1a2c453c58556eef198f52e11650e0d0` (18421 bytes).
- fixed-g-active-peaks.npz: SHA-256 `e3c6728a7f1d0b21a1368338ab28f1c4c4a960a378b63b9fc5dee8890889cf12` (42870 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
