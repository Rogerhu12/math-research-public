# R262-adjacent-low-ports-actual-full-cut-design

**数值记录。** 2026-11-28 17:20:43 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `10c7a13e8a5bdf470619a697023b14fdb2db15e4`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

R319实际半高.350母带配R317相邻同κ=.63圆口、phase1.15；真实原74项/U0对比已由run46167097874完成，当前消费同一真实原场作新的361XYZ/38g全幅短cut求解，gate=.40。输入中央位置/两导保持同一原函数。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-adjacent-low-ports-actual-full-cut-design；实际源码逐文件摘要列于下方。开始 2026-11-28 17:20:23 UTC，结束 2026-11-28 17:20:43 UTC。退出码 0。

```json
{
  "sourceSHA": "94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "c3b6b1ff7396223ea6c3923e5b27e1939442b754a9e65e1c3d7266477cf3275c",
  "lam": 1.0,
  "low": 0.63,
  "phase": 1.15,
  "anchor": 1.0471975511965976,
  "centralOriginalComparison": {
    "schema": "actual-R262-unit-speed-original-versus-adjacent-true-low-circle-traces",
    "inputSHA": "359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0",
    "entrySHA": "94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6",
    "comparisonSHA": "a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e",
    "cutSHA": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
    "normalPlateau": [
      -0.536,
      0.536
    ],
    "normalTransition": [
      0.536,
      0.548
    ],
    "k": 0.63,
    "phase": 1.15,
    "anchor": 1.0471975511965976,
    "supportCoefficients": [
      0.09999976505231697,
      0.00017340635052370438,
      -2.0726030862500148e-05,
      2.732239542665825e-09,
      1.364904959536114e-09,
      -6.697024595314116e-10,
      2.5420195020236015e-11,
      2.7693941053364423e-11,
      2.279645039764186e-11,
      7.050341026639808e-10,
      5.749608505622311e-11,
      2.4233142751359304e-10
    ],
    "exteriorRadiusScale": 0.7830693123282108,
    "axisRadii": [
      0.9029504732702968,
      1.1057853370643296
    ],
    "planarMouthWidth": 0.27,
    "materialCenters": [
      -0.4721975511965977,
      1.6221975511965974
    ],
    "heldRelativeTranslation": 0.8401130130430713,
    "gridComparisons": [
      {
        "angles": 4096,
        "position": {
          "maximum": 0.006929257907418514,
          "atPhysicalU": 3.838019931289874,
          "rms": 0.004118259759296128
        },
        "unitTangent": {
          "maximum": 0.057702482096467285,
          "atPhysicalU": 1.9098060809176232,
          "rms": 0.02530208048168757
        },
        "normalAngle": {
          "maximum": 0.057710490297559286,
          "atPhysicalU": 1.9098060809176232,
          "rms": 0.025303982215203375
        },
        "signedCurvature": {
          "maximum": 1.4163992517989277,
          "atPhysicalU": 0.0,
          "rms": 0.24753118012201777
        },
        "curvatureVector": {
          "maximum": 1.4163992517989277,
          "atPhysicalU": 0.0,
          "rms": 0.25093160855760627
        },
        "newCurvatureRange": [
          0.63,
          6.52912393129986
        ],
        "sourceCurvatureRange": [
          0.5579517226306827,
          5.112724679500932
        ]
      },
      {
        "angles": 8192,
        "position": {
          "maximum": 0.006929258898231644,
          "atPhysicalU": 0.350514610031869,
          "rms": 0.004118259759153316
        },
        "unitTangent": {
          "maximum": 0.05770248209722969,
          "atPhysicalU": 1.9098060809176232,
          "rms": 0.025302080484321508
        },
        "normalAngle": {
          "maximum": 0.05771049029832201,
          "atPhysicalU": 1.9098060809176232,
          "rms": 0.025303982217838493
        },
        "signedCurvature": {
          "maximum": 1.4163992517989277,
          "atPhysicalU": 0.0,
          "rms": 0.2475311788212064
        },
        "curvatureVector": {
          "maximum": 1.4163992517989277,
          "atPhysicalU": 0.0,
          "rms": 0.2509316072428266
        },
        "newCurvatureRange": [
          0.63,
          6.52912393129986
        ],
        "sourceCurvatureRange": [
          0.5579517226306827,
          5.112724679500932
        ]
      }
    ]
  },
  "cutSHA": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
  "numericalPhysicalCoordinates": {
    "S": 2.021775895105453,
    "T": 2.4717758951054534,
    "halfSleeve": 0.35,
    "gateLength": 0.4,
    "liftEnd": 1.5
  },
  "nativeD3Correction": {
    "angularModes": 18,
    "radialSpans": 20,
    "independentRealPositionVariables": 361,
    "positiveMetricVariables": 38
  },
  "initial": {
    "peak": 0.2611947069805245,
    "rms": 0.011992425580116378,
    "curvature": 6.52912393129986,
    "positiveMetricCoefficientLower": 1.0,
    "areaRatioMinimum": 0.9904231699584716,
    "worstPhysicalRadialAndNativeTheta": [
      0.5833333333333333,
      1.0471975511965976
    ],
    "radialRows": 142,
    "angles": 120
  },
  "accepted": {
    "actualCompletedSteps": 3
  },
  "finalTraining": {
    "peak": 0.007249474214010187,
    "rms": 0.0006134936519817363,
    "curvature": 8.070321067023045,
    "positiveMetricCoefficientLower": 0.967089044875546,
    "areaRatioMinimum": 0.9967280438857555,
    "worstPhysicalRadialAndNativeTheta": [
      0.4833333333333333,
      3.5604716740684323
    ],
    "radialRows": 142,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.007249474214010187,
    "rms": 0.0005327204975928232,
    "curvature": 7.947717501315805,
    "positiveMetricCoefficientLower": 0.967089044875546,
    "areaRatioMinimum": 0.9967280438857556,
    "worstPhysicalRadialAndNativeTheta": [
      0.4833333333333333,
      3.5604716740684323
    ],
    "radialRows": 224,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.5996926877955757,
    "minimumAbsoluteHeight": 0.0,
    "heightRange": [
      0.0,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.22835882913278732,
    "maximumOriginNorm": 1.8932251735400278,
    "minimumArea": 0.12056053070089826,
    "leastSupportAtPrefixParameterAndNativeTheta": [
      0.55,
      1.0471975511965976
    ],
    "scope": "finite actual physical prefix; global radial offsets remain in the source metadata"
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-adjacent-low-ports-support-physical-cut.py: SHA-256 `94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6` (12244 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `7693790913541fcf9e6f45501cc30d10b9e7478b7393d9badd9e6e8f1d90bb12` (66092 bytes).
- 2ecf-r262-adjacent-low-ports-support-physical-cut.py: SHA-256 `94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6` (12244 bytes).
- full-cut.json: SHA-256 `3a0e0281c9e64abffa69ed2295b5924fc5d43bf2fc3cf398eef42508344d70cb` (12721 bytes).
- full-cut.npz: SHA-256 `c3b6b1ff7396223ea6c3923e5b27e1939442b754a9e65e1c3d7266477cf3275c` (11149 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
