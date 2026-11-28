# R262-cut-h2-same-metric-complete-banded-newton

**数值记录。** 2026-11-28 17:31:02 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `c2eceb7cdfa5546767cb5ebb02fcf49196c1c279`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

固定h2实际全部位置空间与同一g：按真实局部五次支撑完整组装JᵀJ及五邻块，带状Cholesky直接求实际阻尼Newton步；新的411角/全span径网对合并后的真实保存系数另作观察。实际主曲率与全谱目标进入接受，未将近似Krylov停滞直接判为物理障碍。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-cut-h2-same-metric-complete-banded-newton；实际源码逐文件摘要列于下方。开始 2026-11-28 17:29:52 UTC，结束 2026-11-28 17:31:02 UTC。退出码 0。

```json
{
  "entrySHA256": "dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2",
  "stateSHA256": "8e4d090c855f1a5de8f4698ada7cf212c636dc7741480b807c50b33a5ff6cdce",
  "parentSHA256": "9a3958fa2f008855599a34e01cb96090dbffeaf741502c34e714152ad140332e",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "actualPositionVariables": 3871,
  "actualMetricVariables": 0,
  "radialSpans": 80,
  "angularModes": 48,
  "lowerScalarDiagonals": 294,
  "normalAndRhsAgreement": [
    1.0304533270556364e-15,
    4.146438844275626e-16
  ],
  "initial": {
    "peak": 0.010205345259900729,
    "rms": 0.002698986533659683,
    "curvature": 7.584558968381117,
    "worstMetric": [
      0.8992104859301235,
      4.828744263850979,
      4.57815956497283
    ],
    "worstCurvature": [
      1.0391000000000001,
      2.0943951023931953,
      2.0943951023931944
    ],
    "minimumSupport": 0.36108985068998606,
    "minimumZs": 0.2295985601460588,
    "minimumArea": 0.11999999946243713
  },
  "initialIndependent": {
    "peak": 0.010182982483804505,
    "rms": 0.0027753864313237895,
    "curvature": 7.462058638871766,
    "worstMetric": [
      0.9007000000000001,
      4.82493824990582,
      4.573328521305147
    ],
    "worstCurvature": [
      1.2898765124258238,
      3.435199443644914,
      3.6408691287768695
    ],
    "minimumSupport": 0.36107404898507395,
    "minimumZs": 0.22961953989471567,
    "minimumArea": 0.12020687651814196
  },
  "accepted": {
    "actualCompletedSteps": 1
  },
  "attempts": [
    {
      "step": 1,
      "seconds": 3.3070911830000114,
      "accepted": true
    },
    {
      "step": 2,
      "seconds": 3.439341909999712,
      "accepted": false
    }
  ],
  "final": {
    "peak": 0.010101911176666112,
    "rms": 0.0026350816654107582,
    "curvature": 8.68845667197169,
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
    "minimumSupport": 0.35834634093050577,
    "minimumZs": 0.2297722919182028,
    "minimumArea": 0.11999999946243713
  },
  "secondaryAcceptanceGrid": {
    "peak": 0.01007600650123406,
    "rms": 0.0027091053306020564,
    "curvature": 8.461984169789996,
    "worstMetric": [
      0.8966308851756504,
      4.82493824990582,
      4.573328521305147
    ],
    "worstCurvature": [
      1.0407043315691007,
      0.009786893001837361,
      0.001958503448158202
    ],
    "minimumSupport": 0.35830943051884256,
    "minimumZs": 0.2297946436455413,
    "minimumArea": 0.12020687651814196
  },
  "initialFreshHoldout": {
    "peak": 0.01016571236349765,
    "rms": 0.0018181501231267876,
    "curvature": 7.465645194706825,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.9926862086586258,
    "worstPhysicalRadialAndNativeTheta": [
      0.8988384771176657,
      4.823223757701117
    ],
    "radialRows": 879,
    "angles": 411
  },
  "independent": {
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
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- low35-h2-direct.json: SHA-256 `9575a3e0d1efec0dc6a943ed2b7726d891f70afc5cfd41141fbaee4c8cd8c4a2` (5177 bytes).
- low35-h2-direct.npz: SHA-256 `8e4d090c855f1a5de8f4698ada7cf212c636dc7741480b807c50b33a5ff6cdce` (42894 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
