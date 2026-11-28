# R262-new-fine-target-frozen-real-radial-and-angular-refinement

**数值记录。** 2026-11-28 17:40:10 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `3e283c80f1b4a84689d9a0d25e5328e99611792b`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

把上一条实际选定的两条完整正目标固定为同一g；真实径单元再二分、角48→64，Boehm包含原位置后仅更新空间，以新全门和独立411角观察同一个问题的误差。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-new-fine-target-frozen-real-radial-and-angular-refinement；实际源码逐文件摘要列于下方。开始 2026-11-28 17:38:30 UTC，结束 2026-11-28 17:40:10 UTC。退出码 0。

```json
{
  "parentSHA256": "721a81fd1004054a752342d4d67799d0ebe03c211a829bb34d333bb699cd94d9",
  "stateSHA256": "4c7425d7e0aef943214617c83044f6f7b859090c4094e5777925cac0f00b597f",
  "actualPositionVariables": 10335,
  "actualMetricVariables": 0,
  "radialSpans": 160,
  "angularModes": 64,
  "initial": {
    "peak": 0.009739494609814579,
    "rms": 0.002560506053710512,
    "curvature": 8.68909614767354,
    "worstMetric": [
      0.8992104859301235,
      4.828744263850979,
      4.57815956497283
    ],
    "worstCurvature": [
      1.2776274352463115,
      3.0543261909900767,
      2.9853077789638682
    ],
    "minimumSupport": 0.36422754985511574,
    "minimumZs": 0.22440656042461776,
    "minimumArea": 0.11999999946243713
  },
  "initialIndependent": {
    "peak": 0.009724486767404884,
    "rms": 0.0026173654466099157,
    "curvature": 8.687069864572827,
    "worstMetric": [
      0.8985166666666667,
      4.82493824990582,
      4.573328521305147
    ],
    "worstCurvature": [
      1.2766866268929582,
      0.949328621178224,
      0.8721535432814781
    ],
    "minimumSupport": 0.3641483894609033,
    "minimumZs": 0.22441340554877065,
    "minimumArea": 0.12020687651814196
  },
  "accepted": {
    "actualCompletedSteps": 0
  },
  "final": {
    "peak": 0.009739494609814579,
    "rms": 0.002560506053710512,
    "curvature": 8.68909614767354,
    "worstMetric": [
      0.8992104859301235,
      4.828744263850979,
      4.57815956497283
    ],
    "worstCurvature": [
      1.2776274352463115,
      3.0543261909900767,
      2.9853077789638682
    ],
    "minimumSupport": 0.36422754985511574,
    "minimumZs": 0.22440656042461776,
    "minimumArea": 0.11999999946243713
  },
  "initialFreshHoldout": {
    "peak": 0.009712207333002475,
    "rms": 0.0017017645681144749,
    "curvature": 8.688796013654004,
    "positiveMetricCoefficientLower": 0.9733266735358357,
    "areaRatioMinimum": 0.9934498351846548,
    "worstPhysicalRadialAndNativeTheta": [
      0.8985166666666667,
      4.823223757701117
    ],
    "radialRows": 1279,
    "angles": 411
  },
  "independent": {
    "peak": 0.009712207333002475,
    "rms": 0.0017017645681144749,
    "curvature": 8.688796013654004,
    "positiveMetricCoefficientLower": 0.9733266735358357,
    "areaRatioMinimum": 0.9934498351846548,
    "worstPhysicalRadialAndNativeTheta": [
      0.8985166666666667,
      4.823223757701117
    ],
    "radialRows": 1279,
    "angles": 411
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `82a1e922cb947b8f7986d7b6a123c9bbed2ed878e85b1c0a2dedce3159e6ee97` (78638 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- new-g-frozen-h3.json: SHA-256 `29ab41c0a698a1b65925190bb1b217ea6bf830315bbb1784098ccceec4e0cc1f` (3920 bytes).
- new-g-frozen-h3.npz: SHA-256 `4c7425d7e0aef943214617c83044f6f7b859090c4094e5777925cac0f00b597f` (84176 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
