# R262-affine-height-and-metric-true-frozen-refinement

**数值记录。** 2026-11-28 16:02:33 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46157156458](https://github.com/Rogerhu12/math-research-public/actions/runs/46157156458), attempt 1；计算源码提交 `028e568341f1fa8c5109f4df08a5ddaa475ca5c6`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

父态按已声明的独立误差与有限曲率代价选择；整高度分配、两条g和完整中央幅度均保留，只作真实Boehm/角频空间细化。

```json
{
  "schema": "R262-three-true-circular-arcs-frozen-physical-metric-and-axial-allocation-h-refinement-v2",
  "entrySHA256": "a3289378b74aca1aa2038eb67ae9c547031840c93f5fa01b6de14d74ce2b6247",
  "physicalSourceSHA256": "c7206ae67efe98ce0b775be4d43ae4b5f4022675a5fe1370d1da1b998beb2226",
  "comparisonSHA256": "a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e",
  "parentSHA256": "55705f602c1068d84611e34f3c15462b296fc1b6c938853f552ef42c79fe7d5a",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "historicalMatch": false,
  "stateSHA256": "5d26ec0acaa33eac176bd330c7fefe44bc332df1f535fa743cd01b3ab1156860",
  "low": 0.35,
  "high": 1.5497530223978673,
  "lam": 1.0,
  "anchor": 1.0471975511965976,
  "angularModes": 30,
  "radialSpans": 40,
  "actualPositionDOFs": 1209,
  "metricDOFs": 0,
  "knotTransferMaxActual0th1st2nd": [
    3.469446951953614e-18,
    2.7755575615628914e-17,
    7.216449660063518e-16
  ],
  "initialTraining": {
    "peak": 0.048028030957839585,
    "rms": 0.003119338506007684,
    "curvature": 10.870614865975444,
    "positiveMetricCoefficientLower": 0.0068748956056119415,
    "areaRatioMinimum": 0.9946422163501494,
    "worstPhysicalRadialAndNativeTheta": [
      0.1014161299001945,
      1.0471975511965976
    ],
    "radialRows": 264,
    "angles": 162
  },
  "initialShifted": {
    "peak": 0.04800599066067823,
    "rms": 0.003097260887795682,
    "curvature": 10.870791371522028,
    "positiveMetricCoefficientLower": 0.0068748956056119415,
    "areaRatioMinimum": 0.9946179833092675,
    "worstPhysicalRadialAndNativeTheta": [
      0.10108879475527266,
      1.0471975511965976
    ],
    "radialRows": 424,
    "angles": 273
  },
  "initialGeometry": {
    "minimumOutwardSupport": 0.5749207707549514,
    "at": [
      0.1375,
      1.0471975511965976
    ],
    "minimumRadialHeightDerivative": 0.007093739200409453,
    "heightRange": [
      0.66,
      1.772114288708474
    ],
    "maximumOriginNorm": 1.9467003749889444,
    "minimumArea": 0.10876899979679691
  },
  "accepted": {
    "acceptedSteps": 0
  },
  "training": {
    "peak": 0.048028030957839585,
    "rms": 0.003119338506007684,
    "curvature": 10.870614865975444,
    "positiveMetricCoefficientLower": 0.0068748956056119415,
    "areaRatioMinimum": 0.9946422163501494,
    "worstPhysicalRadialAndNativeTheta": [
      0.1014161299001945,
      1.0471975511965976
    ],
    "radialRows": 264,
    "angles": 162
  },
  "independent": {
    "peak": 0.04800599066067823,
    "rms": 0.003097260887795682,
    "curvature": 10.870791371522028,
    "positiveMetricCoefficientLower": 0.0068748956056119415,
    "areaRatioMinimum": 0.9946179833092675,
    "worstPhysicalRadialAndNativeTheta": [
      0.10108879475527266,
      1.0471975511965976
    ],
    "radialRows": 424,
    "angles": 273
  },
  "independentGeometry": {
    "minimumOutwardSupport": 0.5749207707549514,
    "at": [
      0.1375,
      1.0471975511965976
    ],
    "minimumRadialHeightDerivative": 0.005966869679026496,
    "heightRange": [
      0.66,
      1.7721142684268067
    ],
    "maximumOriginNorm": 1.9467045511510308,
    "minimumArea": 0.10902494690852291
  },
  "geometryFamily": "original-ring-complete axial allocation",
  "scope": "The genuine full plateaux, original material angle, compact cut and both fixed radial functions are retained. Reports are finite grid observations; strict geometry and continuous Gram bounds are separate."
}
```


## 可重算输出的身份

- affine-height-c66-low35.json: SHA-256 `dc7deec89837e4052bedbe4c0e8efe95acecfb77a33655197cff7f7e96020685` (10437 bytes).
- affine-height-c66-low35.npz: SHA-256 `55705f602c1068d84611e34f3c15462b296fc1b6c938853f552ef42c79fe7d5a` (11635 bytes).
- affine-height-c66-low35-fixed-h1.json: SHA-256 `4efd01497733b896744fab7d1cf164ac3b7f73bb2e18f8d6aa7163f74c7cc2fa` (5368 bytes).
- affine-height-c66-low35-fixed-h1.npz: SHA-256 `5d26ec0acaa33eac176bd330c7fefe44bc332df1f535fa743cd01b3ab1156860` (18772 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
