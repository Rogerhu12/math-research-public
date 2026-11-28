# R319-wider-two-moment-actual-full-cut-design

**数值记录。** 2026-11-28 17:23:50 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `f6d5b3190da29d2409ebfe03514da7ce56b5765d`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

同一两矩宽法角轮廓的真实全幅.350 cut设计：重新选自己的正g并更新真实XYZ。源身份、圈钟、实际位置/六jets一致；其结果不作为原R317冻结g精化，后继需固定该新g再加密。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R319-wider-two-moment-actual-full-cut-design；实际源码逐文件摘要列于下方。开始 2026-11-28 17:23:30 UTC，结束 2026-11-28 17:23:50 UTC。退出码 0。

```json
{
  "sourceSHA": "29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "639df9782b3da6c064513f8d64e532a623c74817149caab1b71aa751fdaf6361",
  "lam": 1.0,
  "low": 0.63,
  "phase": 1.15,
  "anchor": 1.0471975511965976,
  "centralOriginalComparison": {
    "schema": "actual-R262-original-physical-two-derivatives-versus-wider-two-moment-adjacent-low-ports",
    "inputSHA": "359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0",
    "entrySHA": "29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902",
    "comparisonSHA": "a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e",
    "cutSHA": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
    "normalPlateau": [
      -0.536,
      0.536
    ],
    "normalTransition": [
      0.536,
      0.576
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
      -0.3778248033946554,
      -0.376143427008282
    ],
    "sourceRadiusCoefficients": [
      0.6221751966053446,
      0.4238546934102538,
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
      1.1049583042321627
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
          "rms": 0.0041099597868871065
        },
        "unitTangent": {
          "maximum": 0.06968505411868954,
          "atPhysicalU": 2.2549517581918925,
          "rms": 0.025423182088176937
        },
        "normalAngle": {
          "maximum": 0.06969916145583138,
          "atPhysicalU": 2.2549517581918925,
          "rms": 0.025425714222797904
        },
        "signedCurvature": {
          "maximum": 0.5760309530090034,
          "atPhysicalU": 4.0036898563815235,
          "rms": 0.24956158242620233
        },
        "curvatureVector": {
          "maximum": 0.5784216469255987,
          "atPhysicalU": 4.0036898563815235,
          "rms": 0.25196030067443426
        },
        "newCurvatureRange": [
          0.63,
          5.157089341489664
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
          "rms": 0.004109959786746649
        },
        "unitTangent": {
          "maximum": 0.06968505412133386,
          "atPhysicalU": 4.028233548987694,
          "rms": 0.025423182088951595
        },
        "normalAngle": {
          "maximum": 0.06969916145847731,
          "atPhysicalU": 4.028233548987694,
          "rms": 0.02542571422357288
        },
        "signedCurvature": {
          "maximum": 0.5760309530096205,
          "atPhysicalU": 2.2794954507980627,
          "rms": 0.2495615801015258
        },
        "curvatureVector": {
          "maximum": 0.5784216469262283,
          "atPhysicalU": 4.0036898563815235,
          "rms": 0.2519602983534874
        },
        "newCurvatureRange": [
          0.63,
          5.157089341489664
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
    "rms": 0.011989684551278284,
    "curvature": 5.157089341489664,
    "positiveMetricCoefficientLower": 1.0,
    "areaRatioMinimum": 0.9888186440193859,
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
    "peak": 0.007332031391184378,
    "rms": 0.0006418979786400506,
    "curvature": 6.337208551207148,
    "positiveMetricCoefficientLower": 0.9668205354346655,
    "areaRatioMinimum": 0.9964919064953117,
    "worstPhysicalRadialAndNativeTheta": [
      0.4833333333333333,
      3.5604716740684323
    ],
    "radialRows": 142,
    "angles": 120
  },
  "finalIndependent": {
    "peak": 0.007332031391184378,
    "rms": 0.0005517320571208849,
    "curvature": 6.2720346446059745,
    "positiveMetricCoefficientLower": 0.9668205354346655,
    "areaRatioMinimum": 0.9964919064953117,
    "worstPhysicalRadialAndNativeTheta": [
      0.4833333333333333,
      3.5604716740684323
    ],
    "radialRows": 224,
    "angles": 195
  },
  "independentPhysicalGeometry": {
    "minimumOutwardSupport": 0.6004342365604964,
    "minimumAbsoluteHeight": 0.0,
    "heightRange": [
      0.0,
      1.772114248895824
    ],
    "minimumAxialDerivative": 0.2283537138345827,
    "maximumOriginNorm": 1.893224973762332,
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

- 2ecf-r262-adjacent-low-ports-two-moment-physical-cut.py: SHA-256 `29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902` (13494 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `7693790913541fcf9e6f45501cc30d10b9e7478b7393d9badd9e6e8f1d90bb12` (66092 bytes).
- 2ecf-r262-adjacent-low-ports-two-moment-physical-cut.py: SHA-256 `29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902` (13494 bytes).
- full-cut.json: SHA-256 `9a8aedfcad1cbc3b3a969e6b6a8fe99f6d1c0ad9ec8c36e84898a6321be1fbd1` (13352 bytes).
- full-cut.npz: SHA-256 `639df9782b3da6c064513f8d64e532a623c74817149caab1b71aa751fdaf6361` (11146 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
