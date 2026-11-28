# R321-actual-original-two-moment-comparison

**数值记录。** 2026-11-28 17:13:40 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46169273350](https://github.com/Rogerhu12/math-research-public/actions/runs/46169273350), attempt 1；计算源码提交 `8a62659e732a4289b94dc5a2c8d9878f18dd07b9`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

只恢复已有完整原中央数据，以原74项与真实U0比较R321宽.040两矩输入。两个准确矩保持R317真实圆心及周长；本次新位置/切向/曲率数据不是先前R317或R21比较的重复登记。全角有限观察与R321严格中央/两导结论分开。

```json
{
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
  "momentAdjustments": [
    -0.37782480339465496,
    -0.37614342700828135
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
        "rms": 0.004109959786887102
      },
      "unitTangent": {
        "maximum": 0.06968505411868954,
        "atPhysicalU": 2.2549517581918925,
        "rms": 0.025423182088177003
      },
      "normalAngle": {
        "maximum": 0.06969916145583138,
        "atPhysicalU": 2.2549517581918925,
        "rms": 0.025425714222797973
      },
      "signedCurvature": {
        "maximum": 0.5760309530090034,
        "atPhysicalU": 4.0036898563815235,
        "rms": 0.24956158242620144
      },
      "curvatureVector": {
        "maximum": 0.5784216469255987,
        "atPhysicalU": 4.0036898563815235,
        "rms": 0.2519603006744334
      },
      "newCurvatureRange": [
        0.63,
        5.1570893414896695
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
        "rms": 0.004109959786746648
      },
      "unitTangent": {
        "maximum": 0.06968505412133386,
        "atPhysicalU": 4.028233548987694,
        "rms": 0.02542318208895166
      },
      "normalAngle": {
        "maximum": 0.06969916145847731,
        "atPhysicalU": 4.028233548987694,
        "rms": 0.025425714223572943
      },
      "signedCurvature": {
        "maximum": 0.5760309530096205,
        "atPhysicalU": 2.2794954507980627,
        "rms": 0.24956158010152493
      },
      "curvatureVector": {
        "maximum": 0.5784216469262283,
        "atPhysicalU": 4.0036898563815235,
        "rms": 0.25196029835348654
      },
      "newCurvatureRange": [
        0.63,
        5.1570893414896695
      ],
      "sourceCurvatureRange": [
        0.5579517226306827,
        5.112724679500932
      ]
    }
  ]
}
```


## 可重算输出的身份

- 2ecf-r262-adjacent-low-ports-two-moment-physical-cut.py: SHA-256 `29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902` (13494 bytes).
- actual-low-port-comparison.json: SHA-256 `c4e1435a151ab48fe3b946ea97b203631b1f3e01f6178d829927191a3027c5af` (3686 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
