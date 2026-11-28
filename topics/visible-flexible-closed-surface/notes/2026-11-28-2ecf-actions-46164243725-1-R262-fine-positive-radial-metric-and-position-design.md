# R262-fine-positive-radial-metric-and-position-design

**数值记录。** 2026-11-28 17:36:06 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `163bb97bcc7fdafdd4baa16961fc11c78a58ece4`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

另选新共同目标：旧两g经准确有理Boehm保持原函数后，释放细径两列与全部实际空间，完整交叉块同带求解。这里真正改变g，不能计作旧g精化；实际末态选定明确正dyadic目标供下一条固定。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-fine-positive-radial-metric-and-position-design；实际源码逐文件摘要列于下方。开始 2026-11-28 17:33:46 UTC，结束 2026-11-28 17:36:06 UTC。退出码 0。

```json
{
  "entrySHA256": "292171ea82b3b39bbb15186f4f0e969015c9d515857224a82f15324e4c17d898",
  "stateSHA256": "721a81fd1004054a752342d4d67799d0ebe03c211a829bb34d333bb699cd94d9",
  "parentSHA256": "8e4d090c855f1a5de8f4698ada7cf212c636dc7741480b807c50b33a5ff6cdce",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "actualPositionVariables": 3871,
  "actualNewMetricVariables": 158,
  "originalMetricCoefficientCount": 38,
  "fullNormalBandwidth": 306,
  "normalAndRhsAgreement": [
    1.1354569306745211e-15,
    3.658760484143089e-16
  ],
  "positiveFineMetricControlInfimum": 0.9733266735358357,
  "finalMetricCoefficientRoundingBoundExact": "18664319726255691594998271246136819732767141981955489526037302920618328977387835448210695938146430135292539271823030094071813683312773401/4480558846256383831396575002962038896696741609332920185720670677723719898419766843513422914384758771528721461925007408903849046719620485466244536709677056",
  "initial": {
    "peak": 0.0100933834317166,
    "rms": 0.0026289316059449857,
    "curvature": 8.685787063668858,
    "worstMetric": [
      0.8970333333333335,
      4.828744263850979,
      4.57815956497283
    ],
    "worstCurvature": [
      1.039572212519853,
      2.0943951023931953,
      2.0943951023931944
    ],
    "minimumSupport": 0.35834634093050544,
    "minimumZs": 0.22977229191820284,
    "minimumArea": 0.11999999946243713
  },
  "initialSecondary": {
    "peak": 0.010081465043702826,
    "rms": 0.002695673385815172,
    "curvature": 8.459542810688461,
    "worstMetric": [
      0.8975645817851317,
      4.82493824990582,
      4.573328521305147
    ],
    "worstCurvature": [
      1.0421763651672051,
      0.009786893001837361,
      0.001958503448158202
    ],
    "minimumSupport": 0.35843019676327587,
    "minimumZs": 0.22980425023026235,
    "minimumArea": 0.12020687651814196
  },
  "accepted": {
    "actualCompletedSteps": 6
  },
  "secondsPerActualSystem": [
    4.691533815000184,
    6.7371783340004185,
    8.321264254000198,
    8.474080179999874,
    9.063801304000663,
    11.705381093999677
  ],
  "initialHeldOut": {
    "peak": 0.010070578531959416,
    "rms": 0.0017704407175684995,
    "curvature": 8.549169021164523,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.9929201404536728,
    "worstPhysicalRadialAndNativeTheta": [
      0.9007000000000001,
      4.838511313193039
    ],
    "radialRows": 867,
    "angles": 411
  },
  "finalFrozenCandidate": {
    "peak": 0.00971265289032554,
    "rms": 0.0017756399373535677,
    "curvature": 8.68960664144728,
    "positiveMetricCoefficientLower": 0.9733266735358357,
    "areaRatioMinimum": 0.9934538657680141,
    "worstPhysicalRadialAndNativeTheta": [
      0.8982643709624242,
      4.823223757701117
    ],
    "radialRows": 867,
    "angles": 411
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-cut-fine-positive-metric-complete-banded-design.py: SHA-256 `292171ea82b3b39bbb15186f4f0e969015c9d515857224a82f15324e4c17d898` (12592 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- 2ecf-r262-cut-fine-positive-metric-complete-banded-design.py: SHA-256 `292171ea82b3b39bbb15186f4f0e969015c9d515857224a82f15324e4c17d898` (12592 bytes).
- fine-g-design.json: SHA-256 `d31f6419107709049668f973a29ce1da3896dd97e5f8840cfa1e90d07895feb7` (10463 bytes).
- fine-g-design.npz: SHA-256 `721a81fd1004054a752342d4d67799d0ebe03c211a829bb34d333bb699cd94d9` (44346 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
