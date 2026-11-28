# R319-actual-0350-frozen-full-physical-inlet-profiles-with-required-source

**数值记录。** 2026-11-28 17:43:39 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `553c80e99520efaf578ffb74d1a7160b2159caa7`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

恢复缺失真实源码后继续本项先前五秒退出的实际任务；不重跑任何已成功数学结果。R319同一g真正扩大空间：加入自己NormalCurve半径与导数所给N/k、实际柱接原场差、ez/k²三列；训练/第二/曲率/独立角网对全部六个.012法角区间各加13/21/33/47真角及端点，原A+C+W和全部新列直接求六jets。新状态含inletNativeXYZ+physicalInletProfiles，旧只认native消费者不得继承。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R319-actual-0350-frozen-full-physical-inlet-profiles-with-required-source；实际源码逐文件摘要列于下方。开始 2026-11-28 17:42:29 UTC，结束 2026-11-28 17:43:39 UTC。退出码 0。

```json
{
  "entrySHA256": "4a04812dce749f7973e2431fac484e9fabeba194f5cc7a59b226b71cd8b9eafa",
  "stateSHA256": "828793b5b8556e9b3e4d4e969f1688df7dc8dc9f990f8d00753adfb992a4c7ea",
  "parentSHA256": "104a8843272816e31129ff8fabce2dbfad6ad98b41f16975496f91dc1b19181d",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "physicalSourceSHA256": "94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6",
  "cutSHA256": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
  "actualPositionVariables": 1326,
  "initial": {
    "peak": 0.005005991304944628,
    "rms": 0.0010775055934202265,
    "curvature": 8.662159665447234,
    "worstMetric": [
      0.4726905973284028,
      3.5488361457218036,
      3.7994208445999447
    ],
    "worstCurvature": [
      0.4726905973284028,
      0.0,
      0.0
    ],
    "minimumSupport": 0.5953704531769622,
    "minimumZs": 0.22783213356831966,
    "minimumArea": 0.11999999946243713
  },
  "initialSecondary": {
    "peak": 0.00501819900078727,
    "rms": 0.0011051101645967248,
    "curvature": 8.6164970330449,
    "worstMetric": [
      0.47506666666666664,
      3.552642159666963,
      3.8042518882676277
    ],
    "worstCurvature": [
      0.4770940738969057,
      4.198577097788228,
      4.190748708234545
    ],
    "minimumSupport": 0.5953769812340786,
    "minimumZs": 0.22778261512588172,
    "minimumArea": 0.12020687651814196
  },
  "initialGuard": {
    "peak": 0.005015491526023546,
    "curvature": 8.652160258809936,
    "minimumSupport": 0.5953751363493306,
    "minimumArea": 0.12006358917684039,
    "minimumZs": 0.22778057389803724,
    "worstMetric": [
      0.476,
      3.553960601211251,
      3.805917767398694
    ],
    "worstCurvature": [
      0.476,
      4.194216098834041,
      4.1898755752766705
    ],
    "rms": 0.0009558940584999548,
    "radialRows": 163,
    "angles": 789
  },
  "accepted": {
    "actualCompletedSteps": 4
  },
  "attempts": [
    {
      "step": 1,
      "accepted": true
    },
    {
      "step": 2,
      "accepted": true
    },
    {
      "step": 3,
      "accepted": true
    },
    {
      "step": 4,
      "accepted": true
    }
  ],
  "normalAndRhsAgreement": [
    7.694875346966423e-16,
    3.837405946643046e-16
  ],
  "finalAngularGuard": {
    "peak": 0.0023321881814236103,
    "curvature": 7.801932878984552,
    "minimumSupport": 0.5967582370911707,
    "minimumArea": 0.12006358917684039,
    "minimumZs": 0.22982946736893675,
    "worstMetric": [
      0.4526666666666666,
      5.203432391697084,
      5.177429485150468
    ],
    "worstCurvature": [
      0.49066666666666664,
      4.215919675024645,
      4.194240051893546
    ],
    "rms": 0.000576208802727295,
    "radialRows": 163,
    "angles": 789
  },
  "initialIndependent": {
    "peak": 0.004985380613161538,
    "curvature": 8.656685113484457,
    "minimumSupport": 0.5955978158076362,
    "minimumArea": 0.11999999946243713,
    "minimumZs": 0.22787810038312792,
    "worstMetric": [
      0.4711333333333333,
      5.645445622021796,
      5.896630675562983
    ],
    "worstCurvature": [
      0.4711333333333333,
      2.0943951023931953,
      2.0943951023931944
    ],
    "rms": 0.0009483735926995851,
    "radialRows": 163,
    "angles": 1161
  },
  "independent": {
    "peak": 0.0023774520011325935,
    "curvature": 7.97286177838614,
    "minimumSupport": 0.5967794932765207,
    "minimumArea": 0.11999999946243713,
    "minimumZs": 0.22947932279398134,
    "worstMetric": [
      0.4711333333333333,
      1.0508210721349942,
      1.0537198317952328
    ],
    "worstCurvature": [
      0.5122,
      2.0943951023931953,
      2.0943951023931944
    ],
    "rms": 0.000578110765398915,
    "radialRows": 163,
    "angles": 1161
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-adjacent-cut-true-normal-angle-cauchy-refinement.py: SHA-256 `4a04812dce749f7973e2431fac484e9fabeba194f5cc7a59b226b71cd8b9eafa` (14237 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `549d65009e9ef037a5d23c71577965aedd6ca7ec014883867e84cd12bfe3ec7e` (88830 bytes).
- 2ecf-r262-adjacent-cut-true-normal-angle-cauchy-refinement.py: SHA-256 `4a04812dce749f7973e2431fac484e9fabeba194f5cc7a59b226b71cd8b9eafa` (14237 bytes).
- 2ecf-r262-adjacent-low-ports-support-physical-cut.py: SHA-256 `94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6` (12244 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- 2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py: SHA-256 `ffa687858a059ab60e14987d55acdd1a7d63c62855f7804f2d2ccc2966cebfd0` (14160 bytes).
- h1-physical-inlet.json: SHA-256 `20df8aee50afc87fc3980f5a8021954a2cf0c8068e448a7e997e7488a0b32f25` (14496 bytes).
- h1-physical-inlet.npz: SHA-256 `828793b5b8556e9b3e4d4e969f1688df7dc8dc9f990f8d00753adfb992a4c7ea` (18105 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
