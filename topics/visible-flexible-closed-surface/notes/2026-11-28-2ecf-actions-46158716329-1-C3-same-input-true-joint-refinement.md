# C3-same-input-true-joint-refinement

**数值记录。** 2026-11-28 15:15:40 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46158716329](https://github.com/Rogerhu12/math-research-public/actions/runs/46158716329), attempt 1；计算源码提交 `6990e09ba612942b90a99536b684990959f56165`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

实际旧小相位系数经准确 Boehm 和零角频补入更大空间；同一连续初相度量及全部物理参数保持。

```json
{
  "results": [
    {
      "delta": 0.0009765625,
      "eta": 0.4990234375,
      "variables": 1731,
      "zeroCorrectionIndependent": {
        "peak": 0.0034502737665965213,
        "rms": 0.0008017517455276155,
        "curvature": 5.489931686394778,
        "minAreaSquared": 0.8590233480506331,
        "minimumPolarAngularDeterminant": 0.6301235631193541,
        "minimumHeightRateAtFixedPolarAngle": 0.999549898704409,
        "capHeightAnalyticSupportLower": 1.42,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          5.595961914206819
        ]
      },
      "warmTraining": {
        "peak": 0.0005075133196900338,
        "rms": 0.00019461561244215264,
        "curvature": 5.493240494474696,
        "minAreaSquared": 0.8587518306231136,
        "minimumPolarAngularDeterminant": 0.6301235631193541,
        "minimumHeightRateAtFixedPolarAngle": 0.9977838464522725,
        "capHeightAnalyticSupportLower": 1.4199993786176415,
        "minimumActiveHeight": 0.78,
        "point": [
          0.9136252000000001,
          0.8344855486097889
        ]
      },
      "finalTraining": {
        "peak": 0.00042174526555955276,
        "rms": 0.0001640950562160462,
        "curvature": 5.560226015586017,
        "minAreaSquared": 0.8588089130251787,
        "minimumPolarAngularDeterminant": 0.6301235631193541,
        "minimumHeightRateAtFixedPolarAngle": 0.9935757132837384,
        "capHeightAnalyticSupportLower": 1.419998939302305,
        "minimumActiveHeight": 0.78,
        "point": [
          0.8672252,
          4.172427743048944
        ]
      },
      "finalIndependent": {
        "peak": 0.00042652943486933275,
        "rms": 0.00014661301317278518,
        "curvature": 5.559955075489032,
        "minAreaSquared": 0.858809039310197,
        "minimumPolarAngularDeterminant": 0.6301235631193541,
        "minimumHeightRateAtFixedPolarAngle": 0.9935397185331778,
        "capHeightAnalyticSupportLower": 1.419998939302305,
        "minimumActiveHeight": 0.78,
        "point": [
          0.8676190476190477,
          1.014472627721704
        ]
      },
      "unmodifiedNativeRampMismatchForComparison": 3.1063960641877513e-12,
      "completeObservedPeak": 0.00042652943486933275,
      "stateSHA256": "6babf5f566a520dae0e4f828d061a1cc56e83aed00dbb8375bac7e0bf1c960c7",
      "acceptedSteps": 6
    }
  ],
  "definedFamily": {
    "phaseSpan": [
      0.0,
      0.0009765625
    ],
    "coefficientInterpolation": "affine in actual physical coefficients and cap displacement, shortest SO3 arc between proper cap rotations",
    "independentInteriorPhases": [
      {
        "delta": 0.00048828125,
        "interval": [
          0.0,
          0.0009765625
        ],
        "completeMaterial": {
          "peak": 0.00021327864753048172,
          "rms": 7.338486020339263e-05,
          "curvature": 5.515163658958449,
          "minAreaSquared": 0.8589207111050317,
          "minimumPolarAngularDeterminant": 0.6301235006077692,
          "minimumHeightRateAtFixedPolarAngle": 0.9967688454292531,
          "capHeightAnalyticSupportLower": 1.4199994696511526,
          "minimumActiveHeight": 0.78,
          "point": [
            0.8676190476190477,
            1.014472627721704
          ]
        }
      }
    ],
    "scope": "finite observations along a defined C2-continuous family, not a continuous error or reach bound"
  }
}
```


## 可重算输出的身份

- C3-joint-finer.json: SHA-256 `52438cc500acb8adeeac6bdcb706cc6c4deea171ebab073dbefa6a1600e4b384` (8190 bytes).
- C3-joint-finer-phase1.npz: SHA-256 `6babf5f566a520dae0e4f828d061a1cc56e83aed00dbb8375bac7e0bf1c960c7` (14843 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
