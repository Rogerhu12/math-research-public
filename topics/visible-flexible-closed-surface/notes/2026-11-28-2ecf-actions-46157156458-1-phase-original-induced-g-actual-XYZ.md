# phase-original-induced-g-actual-XYZ

**数值记录。** 2026-11-28 15:03:24 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

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
    "length": 0.38,
    "gate": 0.1,
    "cap_radius": 0.62,
    "cap_height": 0.3,
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
        "peak": 0.005083893595165568,
        "rms": 0.001775742156483099,
        "curvature": 14.987215530684338,
        "minAreaSquared": 0.38439999999999985,
        "point": [
          1.0005590476190478,
          3.1743175770646865
        ]
      },
      "warmTraining": {
        "peak": 0.005078081950317039,
        "rms": 0.0017651982647347235,
        "curvature": 14.981246331455642,
        "minAreaSquared": 0.3843999999999999,
        "point": [
          0.9972744,
          3.141592653589793
        ]
      },
      "finalTraining": {
        "peak": 0.001386867644903098,
        "rms": 0.0004930291521134648,
        "curvature": 14.98159129847,
        "minAreaSquared": 0.3843999999999998,
        "point": [
          0.9312,
          2.1598449493429825
        ]
      },
      "finalIndependent": {
        "peak": 0.0013986925908659616,
        "rms": 0.0004959613260492534,
        "curvature": 14.987706709548185,
        "minAreaSquared": 0.384398637797256,
        "point": [
          0.9304761904761906,
          2.127120025868089
        ]
      },
      "independentFullRamp": 3.1063960641877513e-12,
      "completeObservedPeak": 0.0013986925908659616,
      "stateSHA256": "176a62d2f8bcdcef51f2fd869ec4d486e1bf8142b91416b27fa609d872c47a13",
      "acceptedSteps": 2
    },
    {
      "delta": 0.00390625,
      "eta": 0.49609375,
      "variables": 279,
      "zeroCorrectionIndependent": {
        "peak": 0.02049080323453553,
        "rms": 0.007103363480800498,
        "curvature": 14.987041926033612,
        "minAreaSquared": 0.38439999999999985,
        "point": [
          1.0005590476190478,
          0.032724923474893676
        ]
      },
      "warmTraining": {
        "peak": 0.005878064996135981,
        "rms": 0.0019793393482880556,
        "curvature": 14.983256267041856,
        "minAreaSquared": 0.38434043056521255,
        "point": [
          0.8856,
          0.6872233929727672
        ]
      },
      "finalTraining": {
        "peak": 0.00578620236123116,
        "rms": 0.0019512767226197816,
        "curvature": 14.982752721646841,
        "minAreaSquared": 0.38434610830132593,
        "point": [
          0.9312,
          2.1598449493429825
        ]
      },
      "finalIndependent": {
        "peak": 0.005811843902692841,
        "rms": 0.0019628887511961048,
        "curvature": 15.004339017935642,
        "minAreaSquared": 0.3843477752852328,
        "point": [
          0.9304761904761906,
          2.127120025868089
        ]
      },
      "independentFullRamp": 3.290524044674084e-12,
      "completeObservedPeak": 0.005811843902692841,
      "stateSHA256": "3acda73d6f2ae17d31daec8d5f5639139ed2b7e913f7a2fad1e2b40525f8e853",
      "acceptedSteps": 1
    },
    {
      "delta": 0.015625,
      "eta": 0.484375,
      "variables": 279,
      "zeroCorrectionIndependent": {
        "peak": 0.08449344934219728,
        "rms": 0.02843871154957187,
        "curvature": 14.98426383707703,
        "minAreaSquared": 0.38439999999999985,
        "point": [
          1.0005590476190478,
          3.1743175770646865
        ]
      },
      "warmTraining": {
        "peak": 0.04176223593587308,
        "rms": 0.008491482115955136,
        "curvature": 15.234618117565702,
        "minAreaSquared": 0.3837130130518311,
        "point": [
          0.8856,
          5.595961914206819
        ]
      },
      "finalTraining": {
        "peak": 0.02387413015403355,
        "rms": 0.007518485924120479,
        "curvature": 15.312405977880147,
        "minAreaSquared": 0.38338212792480403,
        "point": [
          0.9312,
          2.1598449493429825
        ]
      },
      "finalIndependent": {
        "peak": 0.025876272212044738,
        "rms": 0.007562956979363215,
        "curvature": 15.345636722020284,
        "minAreaSquared": 0.38331819784798415,
        "point": [
          0.8859558730158731,
          2.3889194136672383
        ]
      },
      "independentFullRamp": 3.670228210278945e-12,
      "completeObservedPeak": 0.025876272212044738,
      "stateSHA256": "252ada5a721fb221d56a2b8f382637bf91756478b9b38bfcc4adf59a3191e028",
      "acceptedSteps": 2
    }
  ]
}
```


## 可重算输出的身份

- phase-original.json: SHA-256 `1b2ebddffd6afb6feeba6600536881a90b04e38e2e3245921bc50e2459ee3f77` (7196 bytes).
- phase-original-phase2.npz: SHA-256 `3acda73d6f2ae17d31daec8d5f5639139ed2b7e913f7a2fad1e2b40525f8e853` (3051 bytes).
- phase-original-phase3.npz: SHA-256 `252ada5a721fb221d56a2b8f382637bf91756478b9b38bfcc4adf59a3191e028` (3053 bytes).
- phase-original-phase1.npz: SHA-256 `176a62d2f8bcdcef51f2fd869ec4d486e1bf8142b91416b27fa609d872c47a13` (3059 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
