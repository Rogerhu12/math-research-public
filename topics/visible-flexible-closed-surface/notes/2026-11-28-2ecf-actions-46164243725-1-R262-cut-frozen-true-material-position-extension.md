# R262-cut-frozen-true-material-position-extension

**数值记录。** 2026-11-28 18:19:19 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `26bd962332526818551d11464a23737c40e8a18f`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

保留h2全部native真实XYZ系数、两条整连续g、真中央和原尾；只增加准确U0(theta)材料角下的新位置列，以U'和U''真实链式及实际转置继续求解。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-cut-frozen-true-material-position-extension；实际源码逐文件摘要列于下方。开始 2026-11-28 18:18:44 UTC，结束 2026-11-28 18:19:19 UTC。退出码 0。

```json
{
  "entrySHA256": "d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f",
  "nativeStateSHA256": "9a3958fa2f008855599a34e01cb96090dbffeaf741502c34e714152ad140332e",
  "stateSHA256": "0b927c787140ee0c823dd9cea78ac95612aaeaff1f8fbb25399e609a9061eae1",
  "actualMetricVariables": 0,
  "materialPositionVariables": 1975,
  "materialModes": 24,
  "radialSpans": 80,
  "initial": {
    "peak": 0.010183601803246659,
    "rms": 0.0026146262386204525,
    "curvature": 7.584558968381117,
    "worstMetric": [
      0.8970333333333335,
      4.8332194670612205,
      4.583881802341847
    ],
    "worstCurvature": [
      1.0391000000000001,
      2.0943951023931953,
      2.0943951023931944
    ],
    "minimumSupport": 0.3610751645237467,
    "minimumZs": 0.2296099717941093,
    "minimumArea": 0.11999999946243713
  },
  "initialIndependent": {
    "peak": 0.010951221153375398,
    "rms": 0.002694604929052388,
    "curvature": 7.457517521755526,
    "worstMetric": [
      0.9749379453484452,
      4.955295628858127,
      4.756354983227104
    ],
    "worstCurvature": [
      1.2898765124258238,
      4.933703926771599,
      4.723685941824514
    ],
    "minimumSupport": 0.36121213534943575,
    "minimumZs": 0.2295920545518305,
    "minimumArea": 0.12025172637476216
  },
  "training": {
    "peak": 0.010183601803246659,
    "rms": 0.0026146262386204525,
    "curvature": 7.584558968381117,
    "worstMetric": [
      0.8970333333333335,
      4.8332194670612205,
      4.583881802341847
    ],
    "worstCurvature": [
      1.0391000000000001,
      2.0943951023931953,
      2.0943951023931944
    ],
    "minimumSupport": 0.3610751645237467,
    "minimumZs": 0.2296099717941093,
    "minimumArea": 0.11999999946243713
  },
  "independent": {
    "peak": 0.010951221153375398,
    "rms": 0.002694604929052388,
    "curvature": 7.457517521755526,
    "worstMetric": [
      0.9749379453484452,
      4.955295628858127,
      4.756354983227104
    ],
    "worstCurvature": [
      1.2898765124258238,
      4.933703926771599,
      4.723685941824514
    ],
    "minimumSupport": 0.36121213534943575,
    "minimumZs": 0.2295920545518305,
    "minimumArea": 0.12025172637476216
  },
  "accepted": {
    "actualCompletedSteps": 0
  },
  "adjointRelativeDifference": 5.457235586803408e-14
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `91b0653ff3423fec27402e6f4b25cab1ebaefd4681794857c2c450b7354575ee` (111563 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- h2-material24.json: SHA-256 `f6bb24d43c3f091de3caeaf06ce990afc2c0674acecd66110b7fe8c253590044` (2741 bytes).
- h2-material24.npz: SHA-256 `0b927c787140ee0c823dd9cea78ac95612aaeaff1f8fbb25399e609a9061eae1` (1885 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
