# phase-wider-induced-g-actual-XYZ

**数值记录。** 2026-11-28 15:03:32 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46157156458](https://github.com/Rogerhu12/math-research-public/actions/runs/46157156458), attempt 1；计算源码提交 `06dac51fc5dc50479610a51575f8d10dddefeab3`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

固定紧初相真实诱导度量，后相位完整独立 XYZ 与上帽 SE(3) 自由；这允许非轴对称 g。高臂仍为点点固定 H，首端真实相位和所有两 jets 均保留。有限观察不代全时连续存在。

```json
{
  "parameters": {
    "deltas": [
      0.0009765625,
      0.00390625,
      0.015625
    ],
    "c": 0.78,
    "length": 0.58,
    "gate": 0.1,
    "cap_radius": 0.94,
    "cap_height": 0.32,
    "spans": 8,
    "modes": 6,
    "angles": 64,
    "radial": 25,
    "independent": 192,
    "test_radial": 63,
    "steps": 18
  },
  "results": [
    {
      "delta": 0.0009765625,
      "eta": 0.4990234375,
      "variables": 279,
      "zeroCorrectionIndependent": {
        "peak": 0.0034502737665965213,
        "rms": 0.001392314803240204,
        "curvature": 5.489931686394778,
        "minAreaSquared": 0.8590233480506331,
        "point": [
          1.097777777777778,
          5.595961914206819
        ]
      },
      "warmTraining": {
        "peak": 0.0034501208403218647,
        "rms": 0.0013840582066499245,
        "curvature": 5.440706808840641,
        "minAreaSquared": 0.8591689325701328,
        "point": [
          1.0952000000000002,
          2.454369260617026
        ]
      },
      "finalTraining": {
        "peak": 0.0005751694603281163,
        "rms": 0.00023156813070842857,
        "curvature": 5.44097601558583,
        "minAreaSquared": 0.8588279233194006,
        "point": [
          0.9328000000000001,
          5.497787143782138
        ]
      },
      "finalIndependent": {
        "peak": 0.0005800992975711805,
        "rms": 0.0002329448620064793,
        "curvature": 5.493483808950385,
        "minAreaSquared": 0.8586903531858006,
        "point": [
          1.0206193650793651,
          4.1560652813114976
        ]
      },
      "independentFullRamp": 3.1063960641877513e-12,
      "completeObservedPeak": 0.0005800992975711805,
      "stateSHA256": "fccf4a9ff0993e70f2675c932a34547d6907cc4b859967e80422c6d94e7f983c",
      "acceptedSteps": 3
    },
    {
      "delta": 0.00390625,
      "eta": 0.49609375,
      "variables": 279,
      "zeroCorrectionIndependent": {
        "peak": 0.013872096336589791,
        "rms": 0.0055693760643852844,
        "curvature": 5.489868691939039,
        "minAreaSquared": 0.858988033320664,
        "point": [
          1.097777777777778,
          5.595961914206819
        ]
      },
      "warmTraining": {
        "peak": 0.002324632607367796,
        "rms": 0.0009272605925094483,
        "curvature": 5.484628951431175,
        "minAreaSquared": 0.8578140560974852,
        "point": [
          0.9176504000000001,
          5.497787143782138
        ]
      },
      "finalTraining": {
        "peak": 0.002324632607367796,
        "rms": 0.0009272605925094483,
        "curvature": 5.484628951431175,
        "minAreaSquared": 0.8578140560974852,
        "point": [
          0.9176504000000001,
          5.497787143782138
        ]
      },
      "finalIndependent": {
        "peak": 0.002340478338891273,
        "rms": 0.0009327733755124742,
        "curvature": 5.542867994755726,
        "minAreaSquared": 0.8576949542359973,
        "point": [
          0.9228571428571429,
          5.497787143782138
        ]
      },
      "independentFullRamp": 3.290524044674084e-12,
      "completeObservedPeak": 0.002340478338891273,
      "stateSHA256": "c6cb43a9d69ef1032b411eb6085ef790cb7b16415f9fc31085b4e7e2ae04615d",
      "acceptedSteps": 0
    },
    {
      "delta": 0.015625,
      "eta": 0.484375,
      "variables": 279,
      "zeroCorrectionIndependent": {
        "peak": 0.056635512580562,
        "rms": 0.022284981309942175,
        "curvature": 5.488860705263957,
        "minAreaSquared": 0.8588981107040214,
        "point": [
          1.097777777777778,
          5.595961914206819
        ]
      },
      "warmTraining": {
        "peak": 0.010429805143835432,
        "rms": 0.003802549130208735,
        "curvature": 5.927410105396675,
        "minAreaSquared": 0.8542505892138539,
        "point": [
          1.3504,
          5.792311455056181
        ]
      },
      "finalTraining": {
        "peak": 0.009095849486166215,
        "rms": 0.00374369348508867,
        "curvature": 6.11376733861329,
        "minAreaSquared": 0.8526064336202543,
        "point": [
          0.9176504000000001,
          2.356194490192345
        ]
      },
      "finalIndependent": {
        "peak": 0.009095121957457698,
        "rms": 0.00376595105355793,
        "curvature": 6.256897422580529,
        "minAreaSquared": 0.8524351602814961,
        "point": [
          0.9193495238095238,
          2.356194490192345
        ]
      },
      "independentFullRamp": 3.670228210278945e-12,
      "completeObservedPeak": 0.009095121957457698,
      "stateSHA256": "adcc2bbc9b57a2a76a7fbc3cec95fd02e8557da63b9c485f4c824870ec063275",
      "acceptedSteps": 6
    }
  ]
}
```


## 可重算输出的身份

- phase-wider.json: SHA-256 `046c37295e41688ba1399c01e6253af320fe4944ea8d5da2ec78c60b3694d8f1` (8895 bytes).
- phase-wider-phase2.npz: SHA-256 `c6cb43a9d69ef1032b411eb6085ef790cb7b16415f9fc31085b4e7e2ae04615d` (3057 bytes).
- phase-wider-phase1.npz: SHA-256 `fccf4a9ff0993e70f2675c932a34547d6907cc4b859967e80422c6d94e7f983c` (3060 bytes).
- phase-wider-phase3.npz: SHA-256 `adcc2bbc9b57a2a76a7fbc3cec95fd02e8557da63b9c485f4c824870ec063275` (3043 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
