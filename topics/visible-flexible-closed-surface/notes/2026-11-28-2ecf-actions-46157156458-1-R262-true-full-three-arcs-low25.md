# R262-true-full-three-arcs-low25

**数值记录。** 2026-11-28 15:59:20 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46157156458](https://github.com/Rogerhu12/math-research-public/actions/runs/46157156458), attempt 1；计算源码提交 `028e568341f1fa8c5109f4df08a5ddaa475ca5c6`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

中央完整三重真圆弧及两个真正刚口取 lambda=1，使用原已有高度替换首段，随后接回原实际无限尾。正目标在本次设计后固定；原 H65 或旧 R262 几何不转移到新位置。

```json
{
  "schema": "R262-original-infinite-tail-true-threefold-arc-sleeve-prefix-v2",
  "sourceSHA": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
  "comparisonSHA": "a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "historicalMatch": false,
  "originalDataSHA": "359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0",
  "stateSHA": "032c92782b7b5fb3676d72339db90bd79a8619add9b4f78823c3da8f47db18cb",
  "lam": 1.0,
  "low": 0.25,
  "high": 1.6343304104590775,
  "anchor": 1.0471975511965976,
  "numericalPhysicalCoordinates": {
    "S": 2.021775895105453,
    "T": 2.4717758951054534,
    "halfSleeve": 0.78,
    "gateLength": 0.4,
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
      "q": 0.0,
      "oldHeight": [
        0.0,
        0.0
      ],
      "newHeight": [
        0.0,
        0.0
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.029854258255094024,
      "oldAxialAcceleration": 3.764061057452068e-18,
      "newZqRange": [
        1.0,
        1.0
      ]
    },
    {
      "q": 0.78,
      "oldHeight": [
        0.7638833979297442,
        0.7794062203993366
      ],
      "newHeight": [
        0.78,
        0.78
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.168121088904462,
      "oldAxialAcceleration": 0.8775285924507543,
      "newZqRange": [
        1.0,
        1.0
      ]
    },
    {
      "q": 1.1800000000000002,
      "oldHeight": [
        1.160838115419749,
        1.1729272565929034
      ],
      "newHeight": [
        1.160838115419749,
        1.1729272565929034
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.12337492414049978,
      "oldAxialAcceleration": 0.8264725950567464,
      "newZqRange": [
        0.9854537613966404,
        0.9943035954909679
      ]
    },
    {
      "q": 1.5,
      "oldHeight": [
        1.480368128102102,
        1.490817670014892
      ],
      "newHeight": [
        1.480368128102102,
        1.490817670014892
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.11672260649681061,
      "oldAxialAcceleration": 2.7959180399068666,
      "newZqRange": [
        0.9780328672856874,
        0.9913428005900696
      ]
    },
    {
      "q": 2.021775895105453,
      "oldHeight": [
        1.7704871098371728,
        1.772114288708474
      ],
      "newHeight": [
        1.7704871098371728,
        1.772114288708474
      ],
      "oldHorizontalDistanceToUnitSleeve": 0.47993458573757275,
      "oldAxialAcceleration": 4.208485167806926,
      "newZqRange": [
        0.43934768988799755,
        0.4547448999464805
      ]
    }
  ],
  "originalTraining": {
    "peak": 3.706672538732101e-10,
    "curvature": 5.112724679500947,
    "changedSourceZqRange": [
      0.2317457101393845,
      1.0
    ]
  },
  "originalIndependent": {
    "peak": 3.2067370661542516e-10,
    "curvature": 5.087032023630916,
    "changedSourceZqRange": [
      0.2316988343226134,
      1.0
    ]
  },
  "initial": {
    "peak": 0.24927548101593677,
    "rms": 0.011629125776015834,
    "curvature": 5.762623998669793,
    "positiveMetricCoefficientLower": 1.0,
    "areaRatioMinimum": 0.9399866446586288,
    "worstPhysicalRadialAndNativeTheta": [
      0.9466666666666668,
      1.0471975511965976
    ],
    "radialRows": 142,
    "angles": 120
  },
  "accepted": {
    "acceptedSteps": 4
  },
  "finalTraining": {
    "peak": 0.03050911920321441,
    "rms": 0.0023355168766968997,
    "curvature": 6.535381636342083,
    "positiveMetricCoefficientLower": 0.9467069804851558,
    "areaRatioMinimum": 0.9836573488186453,
    "worstPhysicalRadialAndNativeTheta": [
      0.9133333333333334,
      4.97418836818384
    ],
    "radialRows": 142,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.033438725785390665,
    "rms": 0.002002756033003703,
    "curvature": 6.302895818688302,
    "positiveMetricCoefficientLower": 0.9467069804851558,
    "areaRatioMinimum": 0.9836541826261154,
    "worstPhysicalRadialAndNativeTheta": [
      0.9133333333333334,
      4.945994587959316
    ],
    "radialRows": 224,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.2627522742923783,
    "minimumAbsoluteHeight": 0.0,
    "heightRange": [
      0.0,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.19363763821976845,
    "maximumOriginNorm": 1.8948908678261107,
    "minimumArea": 0.12056053070089826,
    "leastSupportAtPrefixParameterAndNativeTheta": [
      0.9800000000000001,
      3.141592653589793
    ],
    "scope": "finite actual physical prefix; global radial offsets remain in the source metadata"
  },
  "fullDomain": "Beyond the original prefix end the original continuous oscillating tail and its entire physical 5778/input field have the same position, the same old metric, and the same true cuff. Positive/negative original cap shapes are replaced by their true flat disks. No new displacement, total height, or old bound is assigned to the compact changed prefix.",
  "scope": "The full-amplitude material inlet has both genuine circular arcs. The actual thick arms are external to this prefix experiment. Closed shape, quantitative reach and full-domain metric tolerance require their own continuous certificates."
}
```


## 可重算输出的身份

- three-arcs-low25.json: SHA-256 `ff6dc31430e8c4346133fe930dcf93da1ae2105f90880f0c36b7db31b0f2a580` (9840 bytes).
- three-arcs-low25.npz: SHA-256 `032c92782b7b5fb3676d72339db90bd79a8619add9b4f78823c3da8f47db18cb` (10869 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
