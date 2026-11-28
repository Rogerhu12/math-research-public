# R322-width060-two-moment-actual-full-cut-design

**数值记录。** 2026-11-28 17:26:11 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `9f8cd1c9b6a6c2dad8a5bb48ec26e9196f5b127b`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

同一两矩宽法角轮廓的真实全幅.350 cut设计：重新选自己的正g并更新真实XYZ。源身份、圈钟、实际位置/六jets一致；其结果不作为原R317冻结g精化，后继需固定该新g再加密。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R322-width060-two-moment-actual-full-cut-design；实际源码逐文件摘要列于下方。开始 2026-11-28 17:25:51 UTC，结束 2026-11-28 17:26:11 UTC。退出码 0。

```json
{
  "sourceSHA": "e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "c986b8d94d933bf9fd5a280f90ce860b318e78d59763945a508a3a9da20b3c98",
  "lam": 1.0,
  "low": 0.63,
  "phase": 1.15,
  "anchor": 1.0471975511965976,
  "centralOriginalComparison": {
    "schema": "actual-R262-original-physical-two-derivatives-versus-wider-two-moment-adjacent-low-ports",
    "inputSHA": "359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0",
    "entrySHA": "e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e",
    "comparisonSHA": "a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e",
    "cutSHA": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
    "normalPlateau": [
      -0.536,
      0.536
    ],
    "normalTransition": [
      0.536,
      0.596
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
    "momentAdjustments": [
      -0.5190218744366847,
      -0.5511349532277711
    ],
    "sourceRadiusCoefficients": [
      0.4809781255633153,
      0.24886316719076473,
      -0.006069222268329654,
      -0.001658082469000012,
      -3.90710254601213e-07,
      3.057387109360896e-07,
      2.1631389442864595e-07,
      1.1184885808903847e-08,
      -1.5924016105684545e-08,
      1.6595815889483273e-08,
      -6.338256582949187e-07,
      6.255574054117074e-08,
      -3.13819198630103e-07
    ],
    "R317SourceSHA": "94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6",
    "axisRadii": [
      0.9029504732702968,
      1.1043094282349943
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
          "rms": 0.004107913713989405
        },
        "unitTangent": {
          "maximum": 0.07841456846225267,
          "atPhysicalU": 0.14572817484913592,
          "rms": 0.026244085767936985
        },
        "normalAngle": {
          "maximum": 0.07843467233009782,
          "atPhysicalU": 0.14572817484913592,
          "rms": 0.02624741830928793
        },
        "signedCurvature": {
          "maximum": 0.881340883561271,
          "atPhysicalU": 4.273670475049396,
          "rms": 0.3287683279836017
        },
        "curvatureVector": {
          "maximum": 0.8846391398675332,
          "atPhysicalU": 4.275204455837282,
          "rms": 0.33065610896140135
        },
        "newCurvatureRange": [
          0.63,
          4.3916994598962855
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
          "rms": 0.00410791371385061
        },
        "unitTangent": {
          "maximum": 0.0784146766589713,
          "atPhysicalU": 4.0428063664726075,
          "rms": 0.026244085768992374
        },
        "normalAngle": {
          "maximum": 0.07843478061007315,
          "atPhysicalU": 4.0428063664726075,
          "rms": 0.0262474183103439
        },
        "signedCurvature": {
          "maximum": 0.8813441576898406,
          "atPhysicalU": 6.1980493734519335,
          "rms": 0.32876833101354064
        },
        "curvatureVector": {
          "maximum": 0.8846410889559517,
          "atPhysicalU": 4.102631617200148,
          "rms": 0.3306561119895444
        },
        "newCurvatureRange": [
          0.63,
          4.3916994598962855
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
    "rms": 0.011991909405355557,
    "curvature": 5.023973626547195,
    "positiveMetricCoefficientLower": 1.0,
    "areaRatioMinimum": 0.9885892648511644,
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
    "peak": 0.007321332438465164,
    "rms": 0.0006538584693916617,
    "curvature": 4.3916994598962855,
    "positiveMetricCoefficientLower": 0.9666693638357047,
    "areaRatioMinimum": 0.9963846400997688,
    "worstPhysicalRadialAndNativeTheta": [
      0.4833333333333333,
      3.5604716740684323
    ],
    "radialRows": 142,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.007321332438465165,
    "rms": 0.000572726974285807,
    "curvature": 4.387203916091811,
    "positiveMetricCoefficientLower": 0.9666693638357047,
    "areaRatioMinimum": 0.996384640099769,
    "worstPhysicalRadialAndNativeTheta": [
      0.4833333333333333,
      3.5604716740684323
    ],
    "radialRows": 224,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.6010797955314258,
    "minimumAbsoluteHeight": 0.0,
    "heightRange": [
      0.0,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.22834215027384924,
    "maximumOriginNorm": 1.8932244731204917,
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

- 2ecf-r262-adjacent-low-ports-two-moment-060-physical-cut.py: SHA-256 `e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e` (13494 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- 2ecf-r262-adjacent-low-ports-two-moment-060-physical-cut.py: SHA-256 `e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e` (13494 bytes).
- full-cut.json: SHA-256 `ac4d01372148b2d2b7a0682eb59720d91860624dd0a4f4c9c56b83e7c27b21e8` (13355 bytes).
- full-cut.npz: SHA-256 `c986b8d94d933bf9fd5a280f90ce860b318e78d59763945a508a3a9da20b3c98` (11152 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
