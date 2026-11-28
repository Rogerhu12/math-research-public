# closure-widerg-actual-XYZ

**数值记录。** 2026-11-28 15:03:16 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46157156458](https://github.com/Rogerhu12/math-research-public/actions/runs/46157156458), attempt 1；计算源码提交 `06dac51fc5dc50479610a51575f8d10dddefeab3`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

每个分支冻结自己的径向目标 g，真实 XYZ 系数同时改动整个闭合段。两端全部二 jets 不变，完整 ramp 另行观察；三种 holding frame 对整个空间像同时作刚体变换。几何表为有限点云，不能直接当作连续 reach 或 Hausdorff 下界。

```json
{
  "parameters": {
    "seed": null,
    "c": 0.78,
    "length": 0.58,
    "gate": 0.1,
    "cap_radius": 0.94,
    "cap_height": 0.32,
    "steps": 24,
    "angles": 96,
    "radial": 38,
    "independent": 256,
    "test_radial": 83,
    "spans": 14,
    "modes": 8
  },
  "variables": 312,
  "accepted": 11,
  "initial": {
    "relativeOperatorPeak": 0.9656594789957214,
    "absolutePrincipalCurvaturePeak": 5.4920729610161025,
    "rms": 0.2691784401983087,
    "minimumAreaSquared": 0.8590374844093391,
    "peakAtPhysicalRadialAndMaterialAngle": [
      1.1265060240963856,
      0.0
    ]
  },
  "final": {
    "relativeOperatorPeak": 0.42692681343936967,
    "absolutePrincipalCurvaturePeak": 21.41711966034603,
    "rms": 0.17176602297002777,
    "minimumAreaSquared": 0.8719265771141724,
    "peakAtPhysicalRadialAndMaterialAngle": [
      0.8819277108433736,
      1.3989904785517047
    ]
  },
  "ramp": {
    "radialRows": 257,
    "angles": 256,
    "relativeOperatorPeak": 2.7849471692064166e-12,
    "absolutePrincipalCurvaturePeak": 1.7309974234585956
  },
  "whole": [
    {
      "state": "unmodified",
      "metric": {
        "maximumRelativeOperator": 0.9655500984132148,
        "maximumAbsolutePrincipalCurvature": 5.492896109567166,
        "minimumAreaSquared": 0.8590441637861415,
        "point": [
          "closing",
          0.28546875,
          0.0
        ]
      },
      "initialDiameter": 3.7183732819364472,
      "finalDiameter": 4.170830327731633,
      "diameterQuotient": 0.06084072408668401,
      "held": [
        0.15737418692135036,
        0.3196596092240909,
        0.37247241905168504
      ]
    },
    {
      "state": "actual",
      "metric": {
        "maximumRelativeOperator": 0.4276399198162315,
        "maximumAbsolutePrincipalCurvature": 21.440262955264267,
        "minimumAreaSquared": 0.8723769585736475,
        "point": [
          "closing",
          0.04078125,
          1.734420944169365
        ]
      },
      "initialDiameter": 3.7183732819364472,
      "finalDiameter": 4.170830327731633,
      "diameterQuotient": 0.06084072408668401,
      "held": [
        0.15737418692135036,
        0.3196596092240909,
        0.37247241905168504
      ]
    }
  ]
}
```


## 可重算输出的身份

- r299-arc-m383-h65-field.json: SHA-256 `aba5c06782d855e1e05d1d60d819608b4eb4faf66b2b23c3487c23a5fe5b5f46` (1982 bytes).
- r299-arc-m383-h65-field.npz: SHA-256 `cf81f6c2dfaa36b6881e4f529dcd1b61cb5fb7a520720a6706880b44c07b85c2` (6536244 bytes).
- r303-closure-v2-widerg.json: SHA-256 `9b7589d3046618b62280b3d4897268daf142d2c7235b2500ce4414e8e843b8e8` (6939 bytes).
- r303-closure-v2-widerg.npz: SHA-256 `ca21b38ed7976e88c51e709307d7cfe875cde973b7774efd8d98162ae17ca061` (2657 bytes).
- widerg-actual-whole.json: SHA-256 `d23c39250da4321610d6982259e6b8e7f0a035dd79214f8f91e46724c6b770e4` (4609 bytes).
- widerg-unmodified-whole.json: SHA-256 `b9a9552dfef922115e52bd8adfcdc870d086d2f88d394dcd73975f3f52838652` (4593 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
