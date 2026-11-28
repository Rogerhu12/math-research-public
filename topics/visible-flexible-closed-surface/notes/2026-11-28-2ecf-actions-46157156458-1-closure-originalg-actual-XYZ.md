# closure-originalg-actual-XYZ

**数值记录。** 2026-11-28 15:00:18 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46157156458](https://github.com/Rogerhu12/math-research-public/actions/runs/46157156458), attempt 1；计算源码提交 `06dac51fc5dc50479610a51575f8d10dddefeab3`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

每个分支冻结自己的径向目标 g，真实 XYZ 系数同时改动整个闭合段。两端全部二 jets 不变，完整 ramp 另行观察；三种 holding frame 对整个空间像同时作刚体变换。几何表为有限点云，不能直接当作连续 reach 或 Hausdorff 下界。

```json
{
  "parameters": {
    "seed": null,
    "c": 0.65,
    "length": 0.38,
    "gate": 0.1,
    "cap_radius": 0.62,
    "cap_height": 0.3,
    "steps": 18,
    "angles": 96,
    "radial": 38,
    "independent": 256,
    "test_radial": 83,
    "spans": 10,
    "modes": 6
  },
  "variables": 162,
  "accepted": 12,
  "initial": {
    "relativeOperatorPeak": 3.7130200916066523,
    "absolutePrincipalCurvaturePeak": 14.986725059678776,
    "rms": 0.6974819574707476,
    "minimumAreaSquared": 0.3843999999999999,
    "peakAtPhysicalRadialAndMaterialAngle": [
      0.8456416867469879,
      1.5707963267948966
    ]
  },
  "final": {
    "relativeOperatorPeak": 1.7992983110109262,
    "absolutePrincipalCurvaturePeak": 69.25880213286186,
    "rms": 0.48582845064479907,
    "minimumAreaSquared": 0.3495433994481971,
    "peakAtPhysicalRadialAndMaterialAngle": [
      0.815301204819277,
      1.5707963267948966
    ]
  },
  "ramp": {
    "radialRows": 257,
    "angles": 256,
    "relativeOperatorPeak": 2.852215946552239e-12,
    "absolutePrincipalCurvaturePeak": 1.7309974234585956
  },
  "whole": [
    {
      "state": "unmodified",
      "metric": {
        "maximumRelativeOperator": 3.712190605115402,
        "maximumAbsolutePrincipalCurvature": 14.980311123330758,
        "minimumAreaSquared": 0.38439999999999985,
        "point": [
          "closing",
          0.1365625,
          1.5707963267948966
        ]
      },
      "initialDiameter": 3.7013114394922804,
      "finalDiameter": 4.1563177675118785,
      "diameterQuotient": 0.061465555581836244,
      "held": [
        0.16283446927823828,
        0.33627594465342375,
        0.45788208829189114
      ]
    },
    {
      "state": "actual",
      "metric": {
        "maximumRelativeOperator": 1.798549527007352,
        "maximumAbsolutePrincipalCurvature": 69.56025372652255,
        "minimumAreaSquared": 0.34936304554819625,
        "point": [
          "closing",
          0.106875,
          1.5707963267948966
        ]
      },
      "initialDiameter": 3.697938191484034,
      "finalDiameter": 4.1563177675118785,
      "diameterQuotient": 0.06197772275959679,
      "held": [
        0.16298300638749327,
        0.336582694550741,
        0.45829976694479535
      ]
    }
  ]
}
```


## 可重算输出的身份

- r299-arc-m383-h65-field.json: SHA-256 `aba5c06782d855e1e05d1d60d819608b4eb4faf66b2b23c3487c23a5fe5b5f46` (1982 bytes).
- r299-arc-m383-h65-field.npz: SHA-256 `cf81f6c2dfaa36b6881e4f529dcd1b61cb5fb7a520720a6706880b44c07b85c2` (6536244 bytes).
- r303-closure-v2-originalg.json: SHA-256 `cb5a4daa53afd0cf3e4b9db4a6aa7832c38cb247536d7ea6b7143308d8be028a` (7270 bytes).
- r303-closure-v2-originalg.npz: SHA-256 `b2582b569aef1acfe9de03b4d6e648359aeca457ec2ee335993fcfe71db32d39` (1511 bytes).
- originalg-unmodified-whole.json: SHA-256 `f4cbfceaa0ce2e388a45c631079943f80fd5148411623904ab46dac8b19bf572` (4653 bytes).
- originalg-actual-whole.json: SHA-256 `e4dfb38d1934cfeb00394e212ea38ebc4283e03039c214f85d71c0327a8e1ea5` (4649 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
