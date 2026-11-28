# R317-actual-original-low-port-comparison

**数值记录。** 2026-11-28 16:49:13 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46167097874](https://github.com/Rogerhu12/math-research-public/actions/runs/46167097874), attempt 1；计算源码提交 `906c1746ea728fb40ab49321cbac7c6a9c953eca`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

只恢复已有原中央数据，直接以完整原74项及真实U0比较R317的新圆口曲线；不是M12支撑参考的代理比较。此任务不恢复旧四场或重复旧结论。新的全角位置/切向/曲率比较为有限网格观察；全连续中央/臂证明已另在R317。

```json
{
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
}
```


## 可重算输出的身份

- 2ecf-r262-adjacent-low-ports-support-physical-cut.py: SHA-256 `94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6` (12244 bytes).
- actual-low-port-comparison.json: SHA-256 `82b541f500133f738245400e26a915e4573d1d2482a6dcafe277f03bf919a9a2` (3097 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
