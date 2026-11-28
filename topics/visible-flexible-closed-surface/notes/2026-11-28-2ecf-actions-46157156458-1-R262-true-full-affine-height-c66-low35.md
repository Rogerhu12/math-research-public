# R262-true-full-affine-height-c66-low35

**数值记录。** 2026-11-28 16:02:05 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

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
  "stateSHA": "55705f602c1068d84611e34f3c15462b296fc1b6c938853f552ef42c79fe7d5a",
  "lam": 1.0,
  "low": 0.35,
  "high": 1.5497530223978673,
  "anchor": 1.0471975511965976,
  "numericalPhysicalCoordinates": {
    "originalS": 2.021775895105453,
    "originalT": 2.4717758951054534,
    "newS": 2.6817758951054533,
    "newT": 3.1317758951054535,
    "halfSleeve": 0.66,
    "verticalShoulder": 0.22,
    "dropEnd": 1.9,
    "maximumVerticalVelocity": 0.8062998544528336,
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
      "newMaterialQ": 0.66,
      "oldHeight": [
        0.0,
        0.0
      ],
      "newHeight": [
        0.66,
        0.66
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.027958951757484085,
      "oldAxialAcceleration": 3.764061057452068e-18,
      "newZqRange": [
        1.0,
        1.0
      ]
    },
    {
      "s": 0.22,
      "newMaterialQ": 0.88,
      "oldHeight": [
        0.21798358342601556,
        0.2199702333835162
      ],
      "newHeight": [
        0.8458279012811576,
        0.8478145512386582
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.03564653924385414,
      "oldAxialAcceleration": 1.0962884676184759,
      "newZqRange": [
        0.6514545321520182,
        0.6791363483955928
      ]
    },
    {
      "s": 1.68,
      "newMaterialQ": 2.34,
      "oldHeight": [
        1.6400476042174927,
        1.6463140215242973
      ],
      "newHeight": [
        1.7038297012942558,
        1.7100961186010604
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.1581059869033979,
      "oldAxialAcceleration": 3.8533249937622487,
      "newZqRange": [
        0.1291651305773419,
        0.15600798586678877
      ]
    },
    {
      "s": 1.5,
      "newMaterialQ": 2.16,
      "oldHeight": [
        1.480368128102102,
        1.490817670014892
      ],
      "newHeight": [
        1.6325805774409012,
        1.6430301193536914
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.09719543175134045,
      "oldAxialAcceleration": 2.7959180399068666,
      "newZqRange": [
        0.545691291980019,
        0.5590012252844012
      ]
    },
    {
      "s": 1.9,
      "newMaterialQ": 2.56,
      "oldHeight": [
        1.7333530235578183,
        1.7360755096691503
      ],
      "newHeight": [
        1.7333530235578183,
        1.7360755096691503
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.35601049269622054,
      "oldAxialAcceleration": 0.16859516073293251,
      "newZqRange": [
        0.23208320440329241,
        0.23582628429573627
      ]
    },
    {
      "s": 2.021775895105453,
      "newMaterialQ": 2.6817758951054533,
      "oldHeight": [
        1.7704871098371728,
        1.772114288708474
      ],
      "newHeight": [
        1.7704871098371728,
        1.772114288708474
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.4720594751453478,
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
      0.01855298485542456,
      1.0
    ]
  },
  "originalIndependent": {
    "peak": 3.19935199747723e-10,
    "curvature": 5.087032023630916,
    "changedSourceZqRange": [
      0.016904070427276152,
      1.0
    ]
  },
  "fullAxialRedistributionLP": {
    "trueRawIntegral": "3426915926632336560071594545426511/5192296858534827628530496329220096",
    "trueVelocityScale": "3426915926632986396239138222243840/3426915926632336560071594545426511",
    "requiredTotalDrop": 0.66,
    "selectedShoulderKnotCount": 15,
    "nonnegativeRawVelocityUpper": 0.8062998544526807,
    "relativeReferenceScales": "midrange E,G of the trapezoid, used only inside affine Rayleigh design",
    "angularNodes": 120,
    "radialRows": 112,
    "realSignedDirections": 16,
    "normalizedRayleighLinearMinimax": 0.03589039676635904,
    "maximumActualDropSpeed": 0.8062998544528336,
    "maximumAngularSpreadOldZs": 0.04381494932180652,
    "maximumMaterialNormalizedAngularZ": 0.021924867674879542
  },
  "unfittedRadialMetric": {
    "peak": 0.7879064070820361,
    "rms": 0.3223192612149333,
    "curvature": 11.399370000327366,
    "positiveMetricCoefficientLower": 1.0,
    "areaRatioMinimum": 0.4592967645747059,
    "worstPhysicalRadialAndNativeTheta": [
      0.7826229271375948,
      0.0
    ],
    "radialRows": 161,
    "angles": 120
  },
  "initial": {
    "peak": 0.05035704439044334,
    "rms": 0.01950092563291765,
    "curvature": 11.399370000327366,
    "positiveMetricCoefficientLower": 0.020000000000000018,
    "areaRatioMinimum": 0.9681261220760079,
    "worstPhysicalRadialAndNativeTheta": [
      0.8804507930297942,
      4.817108735504349
    ],
    "radialRows": 161,
    "angles": 120
  },
  "accepted": {
    "acceptedSteps": 1
  },
  "finalTraining": {
    "peak": 0.04800599066067801,
    "rms": 0.0031843221300622204,
    "curvature": 10.870751579430912,
    "positiveMetricCoefficientLower": 0.0068748956056119415,
    "areaRatioMinimum": 0.9946747528252226,
    "worstPhysicalRadialAndNativeTheta": [
      0.10108879475527266,
      1.0471975511965976
    ],
    "radialRows": 161,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.04800599066067801,
    "rms": 0.003140454152741513,
    "curvature": 10.869952068491976,
    "positiveMetricCoefficientLower": 0.0068748956056119415,
    "areaRatioMinimum": 0.994647962808787,
    "worstPhysicalRadialAndNativeTheta": [
      0.10108879475527266,
      1.0471975511965976
    ],
    "radialRows": 244,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.5749188894913213,
    "minimumAbsoluteHeight": 0.66,
    "heightRange": [
      0.66,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.005978162421444604,
    "maximumOriginNorm": 1.9467001249569482,
    "minimumArea": 0.10928231854205227,
    "leastSupportAtPrefixParameterAndNativeTheta": [
      0.13740224529842887,
      1.0471975511965976
    ],
    "scope": "finite actual physical prefix; global radial offsets remain in the source metadata"
  },
  "fullDomain": "Original material s in [0,S] includes every old cross section. In the new material q=c+s, the old tail s>=S has exactly its original position, metric, and true cuff; pure translation of the material chart adds c to its endpoint coordinate. Positive/negative original cap shapes are replaced by their true flat disks. No new displacement, total height, or old bound is assigned to the compact changed prefix.",
  "scope": "The full-amplitude material inlet has both genuine circular arcs. The actual thick arms are external to this prefix experiment. Closed shape, quantitative reach and full-domain metric tolerance require their own continuous certificates."
}
```


## 可重算输出的身份

- affine-height-c66-low35.json: SHA-256 `dc7deec89837e4052bedbe4c0e8efe95acecfb77a33655197cff7f7e96020685` (10437 bytes).
- affine-height-c66-low35.npz: SHA-256 `55705f602c1068d84611e34f3c15462b296fc1b6c938853f552ef42c79fe7d5a` (11635 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
