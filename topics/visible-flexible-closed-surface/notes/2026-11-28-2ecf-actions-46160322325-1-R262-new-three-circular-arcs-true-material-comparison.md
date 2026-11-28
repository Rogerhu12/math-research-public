# R262-new-three-circular-arcs-true-material-comparison

**数值记录。** 2026-11-28 15:32:59 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46160322325](https://github.com/Rogerhu12/math-research-public/actions/runs/46160322325), attempt 1；计算源码提交 `bb810bc03e77a62de49534313dd57d5a81e9e479`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

原完整中央的原生 Fourier 场先变到真实等周长材料 u，再比较三段真圆弧输入。全部位置、切向和曲率是本次独立全角数值观察；不将插值微分或原 R262 的全闭几何证书转给新输入。

```json
{
  "geometry": {
    "period": 2.0943951023931953,
    "lowLength": 0.915,
    "highLength": 1.09,
    "transition": 0.044697551196597574,
    "operatingPhase": 0.41
  },
  "observations": [
    {
      "uniformPhysicalAngles": 12288,
      "rawMeanArcSpeed": 0.9999999999999943,
      "sourceAxes": [
        1.1001524491717345,
        0.9001943691166961
      ],
      "sourceCurvatureRange": [
        0.5579517226306828,
        5.112724679500953
      ],
      "targetHigh": 1.8119429253876196,
      "targetLow": 0.04,
      "targetTransition": 0.044697551196597574,
      "bestRmsAfterDescriptiveRigidAngularSearch": [
        0.039382053181226964,
        0.07286332546528006,
        1.0471975511965976,
        -7.429509189915996e-18
      ],
      "reflectionAnchors": [
        {
          "anchor": 0.0,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.27282140552031847,
            "rmsPosition": 0.17329221920678578,
            "maxTangentAngle": 0.6835846630579359,
            "curvatureRange": [
              0.04,
              1.8119429253876196
            ],
            "maxCurvatureChange": 5.072724679500953,
            "maxPhysicalVelocity": 0.3595550790569896,
            "axisRadii": [
              0.8273310436514161,
              1.0937096818783476
            ],
            "D3ClosureResidual": 6.671610070811202e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        },
        {
          "anchor": 1.0471975511965976,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.07286332546528006,
            "rmsPosition": 0.039382053181226964,
            "maxTangentAngle": 0.25878098000846633,
            "curvatureRange": [
              0.04,
              1.8119429253876196
            ],
            "maxCurvatureChange": 3.3007817541133337,
            "maxPhysicalVelocity": 0.08005645939979851,
            "axisRadii": [
              1.0937096818783476,
              0.8273310436514163
            ],
            "D3ClosureResidual": 6.671610070811202e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        }
      ]
    },
    {
      "uniformPhysicalAngles": 12288,
      "rawMeanArcSpeed": 0.9999999999999943,
      "sourceAxes": [
        1.1001524491717345,
        0.9001943691166961
      ],
      "sourceCurvatureRange": [
        0.5579517226306828,
        5.112724679500953
      ],
      "targetHigh": 1.6343304104590775,
      "targetLow": 0.25,
      "targetTransition": 0.044697551196597574,
      "bestRmsAfterDescriptiveRigidAngularSearch": [
        0.01840556832884417,
        0.029854258255094364,
        1.0471975511965976,
        -1.867725040977748e-17
      ],
      "reflectionAnchors": [
        {
          "anchor": 0.0,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.22981233831013284,
            "rmsPosition": 0.15099254757378414,
            "maxTangentAngle": 0.5837603359101611,
            "curvatureRange": [
              0.25,
              1.6343304104590775
            ],
            "maxCurvatureChange": 4.862724679500953,
            "maxPhysicalVelocity": 0.2982728216904953,
            "axisRadii": [
              0.8703401108616018,
              1.0800686080064745
            ],
            "D3ClosureResidual": 7.401486830834377e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        },
        {
          "anchor": 1.0471975511965976,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.029854258255094364,
            "rmsPosition": 0.01840556832884417,
            "maxTangentAngle": 0.15900060698146268,
            "curvatureRange": [
              0.25,
              1.6343304104590775
            ],
            "maxCurvatureChange": 3.4783942690418757,
            "maxPhysicalVelocity": 0.03453216216891816,
            "axisRadii": [
              1.0800686080064748,
              0.8703401108616019
            ],
            "D3ClosureResidual": 7.629277997537062e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        }
      ]
    },
    {
      "uniformPhysicalAngles": 12288,
      "rawMeanArcSpeed": 0.9999999999999943,
      "sourceAxes": [
        1.1001524491717345,
        0.9001943691166961
      ],
      "sourceCurvatureRange": [
        0.5579517226306828,
        5.112724679500953
      ],
      "targetHigh": 1.5497530223978673,
      "targetLow": 0.35,
      "targetTransition": 0.044697551196597574,
      "bestRmsAfterDescriptiveRigidAngularSearch": [
        0.014635495101312561,
        0.027958951757484894,
        1.0471975511965976,
        -1.812464402353993e-17
      ],
      "reflectionAnchors": [
        {
          "anchor": 0.0,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.21028516356466312,
            "rmsPosition": 0.14054783392731932,
            "maxTangentAngle": 0.5362504329783446,
            "curvatureRange": [
              0.35,
              1.5497530223978675
            ],
            "maxCurvatureChange": 4.762724679500954,
            "maxPhysicalVelocity": 0.2704659892770753,
            "axisRadii": [
              0.8898672856070716,
              1.0721934974142497
            ],
            "D3ClosureResidual": 0.0,
            "unitSpeedError": 2.220446049250313e-16
          }
        },
        {
          "anchor": 1.0471975511965976,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.027958951757484894,
            "rmsPosition": 0.014635495101312561,
            "maxTangentAngle": 0.1680560564978255,
            "curvatureRange": [
              0.35,
              1.5497530223978675
            ],
            "maxCurvatureChange": 3.562971657103086,
            "maxPhysicalVelocity": 0.03199389742669001,
            "axisRadii": [
              1.07219349741425,
              0.8898672856070716
            ],
            "D3ClosureResidual": 7.629277997537062e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        }
      ]
    },
    {
      "uniformPhysicalAngles": 24576,
      "rawMeanArcSpeed": 0.9999999999999943,
      "sourceAxes": [
        1.1001524491717345,
        0.9001943691166961
      ],
      "sourceCurvatureRange": [
        0.5579517226306828,
        5.112724679500953
      ],
      "targetHigh": 1.8119429253876196,
      "targetLow": 0.04,
      "targetTransition": 0.044697551196597574,
      "bestRmsAfterDescriptiveRigidAngularSearch": [
        0.039382053181226104,
        0.07286332546528008,
        1.0471975511965976,
        -4.7079785042614994e-17
      ],
      "reflectionAnchors": [
        {
          "anchor": 0.0,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.27282140552031847,
            "rmsPosition": 0.17329221920679,
            "maxTangentAngle": 0.6835846630579231,
            "curvatureRange": [
              0.04,
              1.8119429253876196
            ],
            "maxCurvatureChange": 5.072724679500953,
            "maxPhysicalVelocity": 0.3595550790569816,
            "axisRadii": [
              0.8273310436514161,
              1.0937096818783476
            ],
            "D3ClosureResidual": 1.850371707708594e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        },
        {
          "anchor": 1.0471975511965976,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.07286332546528006,
            "rmsPosition": 0.039382053181226104,
            "maxTangentAngle": 0.25878098000847327,
            "curvatureRange": [
              0.04,
              1.8119429253876196
            ],
            "maxCurvatureChange": 3.3007817541133337,
            "maxPhysicalVelocity": 0.08005645939980308,
            "axisRadii": [
              1.0937096818783476,
              0.8273310436514163
            ],
            "D3ClosureResidual": 6.671610070811202e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        }
      ]
    },
    {
      "uniformPhysicalAngles": 24576,
      "rawMeanArcSpeed": 0.9999999999999943,
      "sourceAxes": [
        1.1001524491717345,
        0.9001943691166961
      ],
      "sourceCurvatureRange": [
        0.5579517226306828,
        5.112724679500953
      ],
      "targetHigh": 1.6343304104590775,
      "targetLow": 0.25,
      "targetTransition": 0.044697551196597574,
      "bestRmsAfterDescriptiveRigidAngularSearch": [
        0.018405568328844737,
        0.029854258255094364,
        1.0471975511965976,
        -1.5586432431690614e-17
      ],
      "reflectionAnchors": [
        {
          "anchor": 0.0,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.22981233831013284,
            "rmsPosition": 0.15099254757378822,
            "maxTangentAngle": 0.5837628717506718,
            "curvatureRange": [
              0.25,
              1.6343304104590775
            ],
            "maxCurvatureChange": 4.862724679500953,
            "maxPhysicalVelocity": 0.2982728216904877,
            "axisRadii": [
              0.8703401108616018,
              1.0800686080064748
            ],
            "D3ClosureResidual": 5.551115123125783e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        },
        {
          "anchor": 1.0471975511965976,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.029854258255094364,
            "rmsPosition": 0.018405568328844737,
            "maxTangentAngle": 0.1590012518573278,
            "curvatureRange": [
              0.25,
              1.6343304104590775
            ],
            "maxCurvatureChange": 3.4783942690418757,
            "maxPhysicalVelocity": 0.034532162168922347,
            "axisRadii": [
              1.0800686080064748,
              0.8703401108616019
            ],
            "D3ClosureResidual": 8.275113844157575e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        }
      ]
    },
    {
      "uniformPhysicalAngles": 24576,
      "rawMeanArcSpeed": 0.9999999999999943,
      "sourceAxes": [
        1.1001524491717345,
        0.9001943691166961
      ],
      "sourceCurvatureRange": [
        0.5579517226306828,
        5.112724679500953
      ],
      "targetHigh": 1.5497530223978673,
      "targetLow": 0.35,
      "targetTransition": 0.044697551196597574,
      "bestRmsAfterDescriptiveRigidAngularSearch": [
        0.014635495101314972,
        0.027958951757484894,
        1.0471975511965976,
        -3.2946233152728145e-17
      ],
      "reflectionAnchors": [
        {
          "anchor": 0.0,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.2102851635646631,
            "rmsPosition": 0.14054783392732334,
            "maxTangentAngle": 0.5362526106654536,
            "curvatureRange": [
              0.35,
              1.5497530223978675
            ],
            "maxCurvatureChange": 4.762724679500954,
            "maxPhysicalVelocity": 0.2704659892770679,
            "axisRadii": [
              0.8898672856070716,
              1.07219349741425
            ],
            "D3ClosureResidual": 1.850371707708594e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        },
        {
          "anchor": 1.0471975511965976,
          "actualFullInput": {
            "lam": 1.0,
            "maxPosition": 0.027958951757484894,
            "rmsPosition": 0.014635495101314972,
            "maxTangentAngle": 0.1680560564977922,
            "curvatureRange": [
              0.35,
              1.5497530223978675
            ],
            "maxCurvatureChange": 3.562971657103086,
            "maxPhysicalVelocity": 0.031993897426684695,
            "axisRadii": [
              1.07219349741425,
              0.8898672856070716
            ],
            "D3ClosureResidual": 7.629277997537062e-17,
            "unitSpeedError": 2.220446049250313e-16
          }
        }
      ]
    }
  ]
}
```


## 可重算输出的身份

- m12-prefix-data.npz.gz: SHA-256 `359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0` (3112330 bytes).
- true-three-arcs-material-comparison.json: SHA-256 `002308d07a8ad7ec6877598ca9b02c4ba2c2be2d042ff137bd9889a47ededdf6` (55480 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
