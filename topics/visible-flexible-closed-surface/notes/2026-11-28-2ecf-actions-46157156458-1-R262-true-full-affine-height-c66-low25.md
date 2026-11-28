# R262-true-full-affine-height-c66-low25

**数值记录。** 2026-11-28 16:01:42 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

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
  "stateSHA": "4ab60b1a91637cb1a5a411dbb7c398620a4651426d482b0d11018962abde9e35",
  "lam": 1.0,
  "low": 0.25,
  "high": 1.6343304104590775,
  "anchor": 1.0471975511965976,
  "numericalPhysicalCoordinates": {
    "originalS": 2.021775895105453,
    "originalT": 2.4717758951054534,
    "newS": 2.6817758951054533,
    "newT": 3.1317758951054535,
    "halfSleeve": 0.66,
    "verticalShoulder": 0.22,
    "dropEnd": 1.9,
    "maximumVerticalVelocity": 0.7259825753046915,
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
      "oldHorizontalDistanceToUnitSleeve": 0.02985425825509373,
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
        0.8345142034081809,
        0.8365008533656816
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.05517371398932422,
      "oldAxialAcceleration": 1.0962884676184759,
      "newZqRange": [
        0.5706583632204791,
        0.5983401794640537
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
        1.7030750561732972,
        1.7093414734801018
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.16598109749562262,
      "oldAxialAcceleration": 3.8533249937622487,
      "newZqRange": [
        0.09873213220212296,
        0.1255749874915698
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
        1.635723687809279,
        1.646173229722069
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.11672260649681052,
      "oldAxialAcceleration": 2.7959180399068666,
      "newZqRange": [
        0.5895349615630335,
        0.6028448948674158
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
      "oldHorizontalDistanceToUnitSleeve": 0.3638856032884453,
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
      0.023249353341076195,
      1.0
    ]
  },
  "originalIndependent": {
    "peak": 3.19935199747723e-10,
    "curvature": 5.087032023630916,
    "changedSourceZqRange": [
      0.023297366497146532,
      1.0
    ]
  },
  "fullAxialRedistributionLP": {
    "trueRawIntegral": "1285093472487370988532503741999879/1947111321950560360698936123457536",
    "trueVelocityScale": "1285093472487369898589676833341440/1285093472487370988532503741999879",
    "requiredTotalDrop": 0.66,
    "selectedShoulderKnotCount": 15,
    "nonnegativeRawVelocityUpper": 0.7259825753046921,
    "relativeReferenceScales": "midrange E,G of the trapezoid, used only inside affine Rayleigh design",
    "angularNodes": 120,
    "radialRows": 112,
    "realSignedDirections": 16,
    "normalizedRayleighLinearMinimax": 0.050009137738804416,
    "maximumActualDropSpeed": 0.7259825753046915,
    "maximumAngularSpreadOldZs": 0.04381494932180652,
    "maximumMaterialNormalizedAngularZ": 0.021924867674879542
  },
  "unfittedRadialMetric": {
    "peak": 0.7901767256362136,
    "rms": 0.323134188052733,
    "curvature": 13.654823460871544,
    "positiveMetricCoefficientLower": 1.0,
    "areaRatioMinimum": 0.4538777821021355,
    "worstPhysicalRadialAndNativeTheta": [
      0.7076215632869086,
      0.0
    ],
    "radialRows": 161,
    "angles": 120
  },
  "initial": {
    "peak": 0.06729685830522558,
    "rms": 0.02832208599412736,
    "curvature": 13.654823460871544,
    "positiveMetricCoefficientLower": 0.020000000000000018,
    "areaRatioMinimum": 0.9540494271098293,
    "worstPhysicalRadialAndNativeTheta": [
      1.5652458542751897,
      0.0
    ],
    "radialRows": 161,
    "angles": 120
  },
  "accepted": {
    "acceptedSteps": 1
  },
  "finalTraining": {
    "peak": 0.05413302441476597,
    "rms": 0.014621868752895575,
    "curvature": 13.51867708602266,
    "positiveMetricCoefficientLower": 4.289462487405693e-05,
    "areaRatioMinimum": 0.9767931064789541,
    "worstPhysicalRadialAndNativeTheta": [
      0.11,
      1.0471975511965976
    ],
    "radialRows": 161,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.0541424351155142,
    "rms": 0.014557733496770276,
    "curvature": 13.52220955433586,
    "positiveMetricCoefficientLower": 4.289462487405693e-05,
    "areaRatioMinimum": 0.9751542528447124,
    "worstPhysicalRadialAndNativeTheta": [
      0.11162950985888072,
      1.0471975511965976
    ],
    "radialRows": 244,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.46366229452281993,
    "minimumAbsoluteHeight": 0.66,
    "heightRange": [
      0.66,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.022418734780265553,
    "maximumOriginNorm": 1.9479036891958224,
    "minimumArea": 0.11005433378451972,
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

- affine-height-c66-low25.json: SHA-256 `ef36d44dae641a2723dc7cd6b90fa34b83a51d62186c14b84920623b81625cd8` (10372 bytes).
- affine-height-c66-low25.npz: SHA-256 `4ab60b1a91637cb1a5a411dbb7c398620a4651426d482b0d11018962abde9e35` (11645 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
