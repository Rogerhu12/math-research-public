# phase-wider-finer-induced-g-actual-XYZ

**数值记录。** 2026-11-28 15:03:39 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46157156458](https://github.com/Rogerhu12/math-research-public/actions/runs/46157156458), attempt 1；计算源码提交 `06dac51fc5dc50479610a51575f8d10dddefeab3`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

固定紧初相真实诱导度量，后相位完整独立 XYZ 与上帽 SE(3) 自由；这允许非轴对称 g。高臂仍为点点固定 H，首端真实相位和所有两 jets 均保留。有限观察不代全时连续存在。

```json
{
  "parameters": {
    "deltas": [
      0.0009765625
    ],
    "c": 0.78,
    "length": 0.58,
    "gate": 0.1,
    "cap_radius": 0.94,
    "cap_height": 0.32,
    "spans": 12,
    "modes": 10,
    "angles": 96,
    "radial": 40,
    "independent": 192,
    "test_radial": 63,
    "steps": 18
  },
  "results": [
    {
      "delta": 0.0009765625,
      "eta": 0.4990234375,
      "variables": 699,
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
        "peak": 0.0034374757813219314,
        "rms": 0.0013891736684919806,
        "curvature": 5.4377231192782824,
        "minAreaSquared": 0.8590292115740277,
        "point": [
          1.0915315,
          5.563236990731926
        ]
      },
      "finalTraining": {
        "peak": 0.0005716417087519847,
        "rms": 0.00020044660345976448,
        "curvature": 5.47585562795744,
        "minAreaSquared": 0.8587998129989863,
        "point": [
          0.8835000000000001,
          1.0471975511965976
        ]
      },
      "finalIndependent": {
        "peak": 0.0005712101765833596,
        "rms": 0.00020089776623260453,
        "curvature": 5.5290145995935305,
        "minAreaSquared": 0.8587924343203347,
        "point": [
          0.8825241269841271,
          1.0471975511965976
        ]
      },
      "independentFullRamp": 3.1063960641877513e-12,
      "completeObservedPeak": 0.0005712101765833596,
      "stateSHA256": "0b3ff10cf6d46a7ab2b670cea9ac973d6f1955e38a7c152b8e4e00b3296963f2",
      "acceptedSteps": 4
    }
  ]
}
```


## 可重算输出的身份

- phase-wider-finer.json: SHA-256 `b0db958fb08d6a95f1df53da7086bb5a2d01568f06beb60098a5ce635381b4e1` (3954 bytes).
- phase-wider-finer-phase1.npz: SHA-256 `0b3ff10cf6d46a7ab2b670cea9ac973d6f1955e38a7c152b8e4e00b3296963f2` (6326 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
