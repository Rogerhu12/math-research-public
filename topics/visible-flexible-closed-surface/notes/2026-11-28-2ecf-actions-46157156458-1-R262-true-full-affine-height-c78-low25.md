# R262-true-full-affine-height-c78-low25

**数值记录。** 2026-11-28 16:01:20 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46157156458](https://github.com/Rogerhu12/math-research-public/actions/runs/46157156458), attempt 1；计算源码提交 `028e568341f1fa8c5109f4df08a5ddaa475ca5c6`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

所有原圈保留，真实两导和全部材料角进入带固定总高度的有符号Rayleigh线性设计；之后对该实际空间重算完整Gram并执行XYZ/正目标步。c=.66 的新中央使用R310的.350至.650锥缩窗定义，外部几何各自仍待连续证明。

```json
{
  "schema": "R262-all-original-rings-true-three-arc-sleeve-affine-height-and-positive-metric-design-v1",
  "sourceSHA": "c7206ae67efe98ce0b775be4d43ae4b5f4022675a5fe1370d1da1b998beb2226",
  "comparisonSHA": "a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "historicalMatch": false,
  "originalDataSHA": "359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0",
  "stateSHA": "557720b3a497a5c396216e17a32ef34da2cdecf180fc051f1dd5e7adaf1294e5",
  "lam": 1.0,
  "low": 0.25,
  "high": 1.6343304104590775,
  "anchor": 1.0471975511965976,
  "numericalPhysicalCoordinates": {
    "originalS": 2.021775895105453,
    "originalT": 2.4717758951054534,
    "newS": 2.801775895105453,
    "newT": 3.251775895105453,
    "halfSleeve": 0.78,
    "verticalShoulder": 0.22,
    "dropEnd": 1.9,
    "maximumVerticalVelocity": 0.7121108420151476,
    "liftEnd": 1.5
  },
  "nativeD3Correction": {
    "angularModes": 18,
    "radialSpans": 20,
    "independentRealPositionVariables": 361,
    "positiveMetricVariables": 38
  },
  "circlePort": {
    "unitSpeedCenters": [
      -0.8421975511965977,
      2.2993951023931958
    ],
    "phaseInterval": [
      0,
      0.41
    ],
    "realDefinition": "integrate i exp(i beta) with D3 centered reflection; circular segments exact by expm1; nonconstant turn integrated by positive 100-node Gauss-Legendre"
  },
  "trueOriginalPrefixAtProbeRows": [
    {
      "s": 0.0,
      "newMaterialQ": 0.78,
      "oldHeight": [
        0.0,
        0.0
      ],
      "newHeight": [
        0.78,
        0.78
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.02985425825509373,
      "oldAxialAcceleration": 3.764061057452068e-18,
      "newZqRange": [
        1.0,
        1.0
      ]
    },
    {
      "s": 0.22,
      "newMaterialQ": 1.0,
      "oldHeight": [
        0.21798358342601556,
        0.2199702333835162
      ],
      "newHeight": [
        0.9518328890418885,
        0.9538195389993891
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.05517371398932422,
      "oldAxialAcceleration": 1.0962884676184759,
      "newZqRange": [
        0.5683415566079169,
        0.5960233728514914
      ]
    },
    {
      "s": 1.68,
      "newMaterialQ": 2.46,
      "oldHeight": [
        1.6400476042174927,
        1.6463140215242973
      ],
      "newHeight": [
        1.702942868593249,
        1.7092092859000536
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.16598109749562262,
      "oldAxialAcceleration": 3.8533249937622487,
      "newZqRange": [
        0.09392549503565173,
        0.12076835032509858
      ]
    },
    {
      "s": 1.5,
      "newMaterialQ": 2.2800000000000002,
      "oldHeight": [
        1.480368128102102,
        1.490817670014892
      ],
      "newHeight": [
        1.6417887797914554,
        1.6522383217042456
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.11672260649681052,
      "oldAxialAcceleration": 2.7959180399068666,
      "newZqRange": [
        0.475721763233395,
        0.4890316965377772
      ]
    },
    {
      "s": 1.9,
      "newMaterialQ": 2.6799999999999997,
      "oldHeight": [
        1.7333530235578183,
        1.7360755096691503
      ],
      "newHeight": [
        1.7333530235578183,
        1.7360755096691503
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.3638856032884453,
      "oldAxialAcceleration": 0.16859516073293251,
      "newZqRange": [
        0.23208320440329241,
        0.23582628429573627
      ]
    },
    {
      "s": 2.021775895105453,
      "newMaterialQ": 2.801775895105453,
      "oldHeight": [
        1.7704871098371728,
        1.772114288708474
      ],
      "newHeight": [
        1.7704871098371728,
        1.772114288708474
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.4799345857375725,
      "oldAxialAcceleration": 4.208485167806926,
      "newZqRange": [
        0.4393476898879976,
        0.45474489994648043
      ]
    }
  ],
  "originalTraining": {
    "peak": 3.735483726693316e-10,
    "curvature": 5.112724679500947,
    "changedSourceZqRange": [
      0.023877100298515974,
      1.0
    ]
  },
  "originalIndependent": {
    "peak": 3.19935199747723e-10,
    "curvature": 5.087032023630916,
    "changedSourceZqRange": [
      0.023877650233657954,
      1.0
    ]
  },
  "fullAxialRedistributionLP": {
    "trueRawIntegral": "253124471853572833661640655164643/324518553658426726783156020576256",
    "trueVelocityScale": "253124471853572855537772980600832/253124471853572833661640655164643",
    "requiredTotalDrop": 0.78,
    "selectedShoulderKnotCount": 15,
    "nonnegativeRawVelocityUpper": 0.7121108420151476,
    "relativeReferenceScales": "midrange E,G of the trapezoid, used only inside affine Rayleigh design",
    "angularNodes": 120,
    "radialRows": 112,
    "realSignedDirections": 16,
    "normalizedRayleighLinearMinimax": 0.0596990868917744,
    "maximumActualDropSpeed": 0.7121108420151476,
    "maximumAngularSpreadOldZs": 0.04381494932180652,
    "maximumMaterialNormalizedAngularZ": 0.021924867674879542
  },
  "unfittedRadialMetric": {
    "peak": 0.7990147748988785,
    "rms": 0.3642991212128396,
    "curvature": 13.393450202709019,
    "positiveMetricCoefficientLower": 1.0,
    "areaRatioMinimum": 0.4457674027335603,
    "worstPhysicalRadialAndNativeTheta": [
      0.9130600816605273,
      1.0471975511965976
    ],
    "radialRows": 161,
    "angles": 120
  },
  "initial": {
    "peak": 0.0690770135125175,
    "rms": 0.032748980188373536,
    "curvature": 13.393450202709019,
    "positiveMetricCoefficientLower": 0.020000000000000018,
    "areaRatioMinimum": 0.9496218128182674,
    "worstPhysicalRadialAndNativeTheta": [
      1.5652458542751897,
      1.0471975511965976
    ],
    "radialRows": 161,
    "angles": 120
  },
  "accepted": {
    "acceptedSteps": 3
  },
  "finalTraining": {
    "peak": 0.043279363327475506,
    "rms": 0.020299752104137387,
    "curvature": 12.790420817744643,
    "positiveMetricCoefficientLower": 0.0006307326266392632,
    "areaRatioMinimum": 0.9689455298895123,
    "worstPhysicalRadialAndNativeTheta": [
      0.11,
      1.0471975511965976
    ],
    "radialRows": 161,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.04374128965947821,
    "rms": 0.020241101902836088,
    "curvature": 12.793082014097047,
    "positiveMetricCoefficientLower": 0.0006307326266392632,
    "areaRatioMinimum": 0.9688822559185188,
    "worstPhysicalRadialAndNativeTheta": [
      0.11777335311293902,
      1.0471975511965976
    ],
    "radialRows": 244,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.4354229257649538,
    "minimumAbsoluteHeight": 0.78,
    "heightRange": [
      0.78,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.026587462410113224,
    "maximumOriginNorm": 1.9486831723319649,
    "minimumArea": 0.10164594611986465,
    "leastSupportAtPrefixParameterAndNativeTheta": [
      0.4318356280807764,
      5.235987755982988
    ],
    "scope": "finite actual physical prefix; global radial offsets remain in the source metadata"
  },
  "fullDomain": "Original material s in [0,S] includes every old cross section. In the new material q=c+s, the old tail s>=S has exactly its original position, metric, and true cuff; pure translation of the material chart adds c to its endpoint coordinate. Positive/negative original cap shapes are replaced by their true flat disks. No new displacement, total height, or old bound is assigned to the compact changed prefix.",
  "scope": "The full-amplitude material inlet has both genuine circular arcs. The actual thick arms are external to this prefix experiment. Closed shape, quantitative reach and full-domain metric tolerance require their own continuous certificates."
}
```


## 可重算输出的身份

- affine-height-c78-low25.json: SHA-256 `21c8c82bd0f4a0150517e602e0833d4cbceebdbeac6039bd9f51bab85c604fbd` (11405 bytes).
- affine-height-c78-low25.npz: SHA-256 `557720b3a497a5c396216e17a32ef34da2cdecf180fc051f1dd5e7adaf1294e5` (11644 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
