# R322-actual-original-two-moment-060-comparison

**数值记录。** 2026-11-28 17:24:30 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46170239008](https://github.com/Rogerhu12/math-research-public/actions/runs/46170239008), attempt 1；计算源码提交 `0b0469bb6ab3ff3b311e52561be0c06bb8be98ba`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

只恢复已有完整原中央数据，以原74项与真实U0比较R322宽.060两矩输入。两个准确矩保持R317真实圆心及周长；本次新位置/切向/曲率数据不是先前R317或R21比较的重复登记。全角有限观察与R322严格中央/两导结论分开。

```json
{
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
  "momentAdjustments": [
    -0.5190218744366856,
    -0.5511349532277723
  ],
  "R317SourceSHA": "94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6",
  "axisRadii": [
    0.9029504732702968,
    1.1043094282349941
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
        "rms": 0.004107913713989402
      },
      "unitTangent": {
        "maximum": 0.07841456846225267,
        "atPhysicalU": 0.14572817484913592,
        "rms": 0.02624408576793699
      },
      "normalAngle": {
        "maximum": 0.07843467233009782,
        "atPhysicalU": 0.14572817484913592,
        "rms": 0.026247418309287937
      },
      "signedCurvature": {
        "maximum": 0.8813408835612733,
        "atPhysicalU": 4.273670475049396,
        "rms": 0.3287683279836021
      },
      "curvatureVector": {
        "maximum": 0.8846391398675376,
        "atPhysicalU": 4.275204455837282,
        "rms": 0.33065610896140174
      },
      "newCurvatureRange": [
        0.63,
        4.391699459896279
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
        "rms": 0.004107913713850607
      },
      "unitTangent": {
        "maximum": 0.0784146766589713,
        "atPhysicalU": 4.0428063664726075,
        "rms": 0.026244085768992384
      },
      "normalAngle": {
        "maximum": 0.07843478061007315,
        "atPhysicalU": 4.0428063664726075,
        "rms": 0.026247418310343912
      },
      "signedCurvature": {
        "maximum": 0.8813441576898415,
        "atPhysicalU": 6.1980493734519335,
        "rms": 0.3287683310135411
      },
      "curvatureVector": {
        "maximum": 0.8846410889559528,
        "atPhysicalU": 4.102631617200148,
        "rms": 0.3306561119895448
      },
      "newCurvatureRange": [
        0.63,
        4.391699459896279
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

- 2ecf-r262-adjacent-low-ports-two-moment-060-physical-cut.py: SHA-256 `e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e` (13494 bytes).
- actual-low-port-comparison.json: SHA-256 `2afc59ac84d98e5dfccf1c05a32d516b09415a1bcf5679f77f6e8d53a194b55d` (3681 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
