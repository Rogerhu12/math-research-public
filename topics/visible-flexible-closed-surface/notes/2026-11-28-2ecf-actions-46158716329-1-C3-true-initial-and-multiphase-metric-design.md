# C3-true-initial-and-multiphase-metric-design

**数值记录。** 2026-11-28 15:15:53 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46158716329](https://github.com/Rogerhu12/math-research-public/actions/runs/46158716329), attempt 1；计算源码提交 `6990e09ba612942b90a99536b684990959f56165`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

该项真实改变初相和各相位共同寻找同一诱导度量，和前两项固定旧初相 g 区分。初相全域空间位移的准确有理控制界来自真实已存系数；有限曲率导引和相位观察不代全时 reach 或精确等距。

```json
{
  "parameters": {
    "deltas": [
      0.03125,
      0.125,
      0.25,
      0.5
    ],
    "base_budget": 0.018,
    "base_trust": 0.0035,
    "curvature_guide": 8.65,
    "freeze_initial": false,
    "ramp_spans": 3,
    "phase_interior": 1,
    "c": 0.78,
    "length": 0.58,
    "gate": 0.1,
    "cap_radius": 0.94,
    "cap_height": 0.32,
    "spans": 6,
    "modes": 5,
    "angles": 48,
    "radial": 19,
    "independent": 144,
    "test_radial": 45,
    "steps": 20
  },
  "phases": [
    0.0,
    0.03125,
    0.125,
    0.25,
    0.5
  ],
  "variables": 1344,
  "initialFullObservations": [
    {
      "peak": 6.729675497761745e-16,
      "rms": 1.5669690354726798e-16,
      "curvature": 5.452928591769499,
      "minAreaSquared": 0.8590687174696539,
      "minimumPolarAngularDeterminant": 0.6301234797705743,
      "minimumHeightRateAtFixedPolarAngle": 0.9995498987044111,
      "capHeightAnalyticSupportLower": 1.42,
      "minimumActiveHeight": 0.78,
      "point": [
        1.0285515555555556,
        4.363323129985824
      ]
    },
    {
      "peak": 0.1164668417975528,
      "rms": 0.02281292931206708,
      "curvature": 5.452143651424369,
      "minAreaSquared": 0.858855352116738,
      "minimumPolarAngularDeterminant": 0.6301368816871082,
      "minimumHeightRateAtFixedPolarAngle": 0.9995498987044098,
      "capHeightAnalyticSupportLower": 1.42,
      "minimumActiveHeight": 0.78,
      "point": [
        1.097777777777778,
        2.443460952792061
      ]
    },
    {
      "peak": 0.547760126904814,
      "rms": 0.09318434662136485,
      "curvature": 5.452557005303989,
      "minAreaSquared": 0.858854309594744,
      "minimumPolarAngularDeterminant": 0.6301265217625399,
      "minimumHeightRateAtFixedPolarAngle": 0.999549898704411,
      "capHeightAnalyticSupportLower": 1.42,
      "minimumActiveHeight": 0.78,
      "point": [
        1.097777777777778,
        5.541420375081996
      ]
    },
    {
      "peak": 1.352463425595126,
      "rms": 0.19819252681391952,
      "curvature": 5.451442111950394,
      "minAreaSquared": 0.8590207134215294,
      "minimumPolarAngularDeterminant": 0.6301356477343794,
      "minimumHeightRateAtFixedPolarAngle": 0.99954989870441,
      "capHeightAnalyticSupportLower": 1.42,
      "minimumActiveHeight": 0.78,
      "point": [
        1.097777777777778,
        2.399827721492203
      ]
    },
    {
      "peak": 3.9135929187634,
      "rms": 0.4785982204594802,
      "curvature": 5.452682657093439,
      "minAreaSquared": 0.8588588471094797,
      "minimumPolarAngularDeterminant": 0.6301585592932771,
      "minimumHeightRateAtFixedPolarAngle": 0.9995498987044108,
      "capHeightAnalyticSupportLower": 1.42,
      "minimumActiveHeight": 0.78,
      "point": [
        1.097777777777778,
        5.497787143782138
      ]
    }
  ],
  "finalSameMetricObservations": [
    {
      "peak": 8.881784213631142e-16,
      "rms": 1.6119429046876645e-16,
      "curvature": 5.452824490364026,
      "minAreaSquared": 0.8591919768098969,
      "minimumPolarAngularDeterminant": 0.6301234797705743,
      "minimumHeightRateAtFixedPolarAngle": 0.9698044208886221,
      "capHeightAnalyticSupportLower": 1.42,
      "minimumActiveHeight": 0.78,
      "point": [
        0.8390625,
        3.097959422289935
      ]
    },
    {
      "peak": 0.08944721365908427,
      "rms": 0.017600864449168294,
      "curvature": 5.453819170533279,
      "minAreaSquared": 0.860033959956308,
      "minimumPolarAngularDeterminant": 0.6301368816871082,
      "minimumHeightRateAtFixedPolarAngle": 0.9702705478038794,
      "capHeightAnalyticSupportLower": 1.4202354418925789,
      "minimumActiveHeight": 0.78,
      "point": [
        1.097777777777778,
        2.443460952792061
      ]
    },
    {
      "peak": 0.42263478447405817,
      "rms": 0.07210559449920033,
      "curvature": 5.504381172351355,
      "minAreaSquared": 0.8722428412137705,
      "minimumPolarAngularDeterminant": 0.6301265217625843,
      "minimumHeightRateAtFixedPolarAngle": 0.968104599305491,
      "capHeightAnalyticSupportLower": 1.4237038271970692,
      "minimumActiveHeight": 0.78,
      "point": [
        1.092996,
        5.541420375081996
      ]
    },
    {
      "peak": 1.051951806756772,
      "rms": 0.15483706945060943,
      "curvature": 5.731500710335693,
      "minAreaSquared": 0.8597881781312077,
      "minimumPolarAngularDeterminant": 0.6301356477343794,
      "minimumHeightRateAtFixedPolarAngle": 0.9615418738456852,
      "capHeightAnalyticSupportLower": 1.433729576355743,
      "minimumActiveHeight": 0.78,
      "point": [
        1.097777777777778,
        2.399827721492203
      ]
    },
    {
      "peak": 3.089445829990074,
      "rms": 0.38225927933150144,
      "curvature": 8.381734342971107,
      "minAreaSquared": 0.7795277483240232,
      "minimumPolarAngularDeterminant": 0.6032133932010019,
      "minimumHeightRateAtFixedPolarAngle": 0.9267469232590776,
      "capHeightAnalyticSupportLower": 1.45977822124833,
      "minimumActiveHeight": 0.78,
      "point": [
        1.097777777777778,
        5.497787143782138
      ]
    }
  ],
  "genuineIntermediatePhases": [
    {
      "delta": 0.015625,
      "data": {
        "peak": 0.04375089487385952,
        "rms": 0.008792610401945879,
        "curvature": 5.452338068346128,
        "minAreaSquared": 0.8595417925164316,
        "minimumPolarAngularDeterminant": 0.6301448170409063,
        "minimumHeightRateAtFixedPolarAngle": 0.9700874047423146,
        "capHeightAnalyticSupportLower": 1.4201177209462894,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          2.443460952792061
        ]
      }
    },
    {
      "delta": 0.078125,
      "data": {
        "peak": 0.24581851753053943,
        "rms": 0.0444939263457955,
        "curvature": 5.477109391716498,
        "minAreaSquared": 0.8666263252843426,
        "minimumPolarAngularDeterminant": 0.6301307832601464,
        "minimumHeightRateAtFixedPolarAngle": 0.9695747357334151,
        "capHeightAnalyticSupportLower": 1.421969634544824,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          2.443460952792061
        ]
      }
    },
    {
      "delta": 0.1875,
      "data": {
        "peak": 0.7137879187507091,
        "rms": 0.11200573643422906,
        "curvature": 5.606273467891455,
        "minAreaSquared": 0.8687152739053426,
        "minimumPolarAngularDeterminant": 0.6301381752226118,
        "minimumHeightRateAtFixedPolarAngle": 0.9649499435013463,
        "capHeightAnalyticSupportLower": 1.4287167017764062,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          2.399827721492203
        ]
      }
    },
    {
      "delta": 0.375,
      "data": {
        "peak": 1.937342229432322,
        "rms": 0.25877184109239176,
        "curvature": 6.834758962446431,
        "minAreaSquared": 0.8192841582129015,
        "minimumPolarAngularDeterminant": 0.6237098560519158,
        "minimumHeightRateAtFixedPolarAngle": 0.9455832522656578,
        "capHeightAnalyticSupportLower": 1.4467538988020365,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          2.356194490192345
        ]
      }
    }
  ],
  "initialWNormRigorousUpper": "15762598695803/18014398509481984",
  "acceptedSteps": 1
}
```


## 可重算输出的身份

- C3-multiphase-design.json: SHA-256 `91986229dc8ade6b9c1bff2cb9f55fdc9b6ab5e5c221cf376c59a4e4d54337f0` (11866 bytes).
- C3-multiphase-design-phase3.npz: SHA-256 `96d907151594f6d6f7418e96d6e138d7cf442c2e40da96090fa9c7f3b52b5a3a` (3407 bytes).
- C3-multiphase-design-phase4.npz: SHA-256 `4cc658108d3b6db0b07c476f6af2f5b46754e72d7d8fbab15604285e3a2a65ed` (3404 bytes).
- C3-multiphase-design-phase0.npz: SHA-256 `c1e5b2328c09729c7b89cb9ce943c1abd6e3c32fda860c749c1e3091e6ca8c88` (3332 bytes).
- C3-multiphase-design-phase1.npz: SHA-256 `180d17f535917f67fbd9ff8e058f3fbd7a6ac1b30c7d3cda658acf7f5552273f` (3422 bytes).
- C3-multiphase-design-phase2.npz: SHA-256 `e72da23d9b696ed6ed46aedec8064a04dee19f3e6da3c7352b6b5f15805ab256` (3409 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
