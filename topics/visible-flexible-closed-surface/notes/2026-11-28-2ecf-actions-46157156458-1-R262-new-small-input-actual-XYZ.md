# R262-new-small-input-actual-XYZ

**数值记录。** 2026-11-28 16:11:46 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46157156458](https://github.com/Rogerhu12/math-research-public/actions/runs/46157156458), attempt 1；计算源码提交 `06dac51fc5dc50479610a51575f8d10dddefeab3`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

真正改变中央输入后，对完整原前缀及正径向目标执行真实 XYZ 更新；原尾及帽保持各自定义。结果：

```json
{
  "eta": 0.0001220703125,
  "actualEntrySHA256": "152b08a6e60a2aced9ef3aca61543bbc7050471c68614fe1235d4a9e8fa363dc",
  "activeEntrySourceCommit": "0a955b19b178d43ad52e3a13d5483980227c3a63",
  "sourceFieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "historicalSourceBytesMatched": false,
  "actualStages": [
    {
      "stage": 1,
      "spans": 48,
      "modes": 24,
      "metricChosenThisStage": true,
      "fixedContinuousMetricSinceStage": 1,
      "sourceS": 2.021775895105453,
      "initialTraining": {
        "peak": 9.194673966924265e-05,
        "rms": 1.796578736991173e-05,
        "curvature": 5.112998583890547,
        "positiveMetricCoefficientLower": 1.0,
        "areaRatioMinimum": 0.9999724993976341,
        "worstPhysicalRadialAndNativeTheta": [
          0.9714001371014482,
          2.028945255443408
        ],
        "radialRows": 545,
        "angles": 192
      },
      "checks": {
        "adjointRelative": 2.7702786030167244e-15,
        "centralDirectionalRelative": 1.9793331866038873e-11,
        "epsilon": 2e-06
      },
      "finalTraining": {
        "peak": 1.1168896764557346e-05,
        "rms": 3.702139784587144e-06,
        "curvature": 5.112998583890547,
        "positiveMetricCoefficientLower": 0.9999953785539093,
        "areaRatioMinimum": 0.9999939369737801,
        "worstPhysicalRadialAndNativeTheta": [
          0.03948781045127838,
          0.0
        ],
        "radialRows": 545,
        "angles": 192
      },
      "finalIndependent": {
        "peak": 1.1153228772775043e-05,
        "rms": 3.705387734473618e-06,
        "curvature": 5.109844755435199,
        "positiveMetricCoefficientLower": 0.9999953785539093,
        "areaRatioMinimum": 0.9999939322835003,
        "worstPhysicalRadialAndNativeTheta": [
          0.039312309071494925,
          6.273367830137118
        ],
        "radialRows": 754,
        "angles": 320
      },
      "independentPhysicalGeometry": {
        "minimumOutwardSupport": 0.8178131670619998,
        "minimumAbsoluteHeight": 0.0,
        "heightRange": [
          0.0,
          1.7721142870707058
        ],
        "minimumAxialDerivative": 0.23169913392418193,
        "maximumOriginNorm": 1.8928079632049042,
        "minimumArea": 0.12002313116702006,
        "leastSupportAtPrefixParameterAndNativeTheta": [
          0.2842448427193675,
          1.050470043544087
        ],
        "scope": "finite actual physical prefix; global radial offsets remain in the source metadata"
      },
      "stateSHA256": "eafc84de99fd252d5c7638964d7e782908eaf8a2206b6dab379b8e857fa19b4a",
      "acceptedSteps": 2
    },
    {
      "stage": 2,
      "spans": 96,
      "modes": 64,
      "metricChosenThisStage": false,
      "fixedContinuousMetricSinceStage": 1,
      "sourceS": 2.021775895105453,
      "initialTraining": {
        "peak": 1.1153747113468171e-05,
        "rms": 3.705143786631067e-06,
        "curvature": 5.112998583890547,
        "positiveMetricCoefficientLower": 0.9999953785539093,
        "areaRatioMinimum": 0.9999939305461375,
        "worstPhysicalRadialAndNativeTheta": [
          0.03852430787626719,
          0.0
        ],
        "radialRows": 800,
        "angles": 384
      },
      "checks": {
        "adjointRelative": 1.406974625532025e-14,
        "centralDirectionalRelative": 1.0844462448306638e-11,
        "epsilon": 2e-06
      },
      "finalTraining": {
        "peak": 1.1153747113468171e-05,
        "rms": 3.705143786631067e-06,
        "curvature": 5.112998583890547,
        "positiveMetricCoefficientLower": 0.9999953785539093,
        "areaRatioMinimum": 0.9999939305461375,
        "worstPhysicalRadialAndNativeTheta": [
          0.03852430787626719,
          0.0
        ],
        "radialRows": 800,
        "angles": 384
      },
      "finalIndependent": {
        "peak": 1.1160165169778697e-05,
        "rms": 3.707200044285484e-06,
        "curvature": 5.110624732076383,
        "positiveMetricCoefficientLower": 0.9999953785539093,
        "areaRatioMinimum": 0.9999939288798954,
        "worstPhysicalRadialAndNativeTheta": [
          0.04040609496808466,
          6.277049384028044
        ],
        "radialRows": 1058,
        "angles": 512
      },
      "independentPhysicalGeometry": {
        "minimumOutwardSupport": 0.8178081449869793,
        "minimumAbsoluteHeight": 0.0,
        "heightRange": [
          0.0,
          1.7721142880687708
        ],
        "minimumAxialDerivative": 0.23168504162892806,
        "maximumOriginNorm": 1.8928102362193073,
        "minimumArea": 0.1200090353287673,
        "leastSupportAtPrefixParameterAndNativeTheta": [
          0.28419611974171516,
          1.0492428589137786
        ],
        "scope": "finite actual physical prefix; global radial offsets remain in the source metadata"
      },
      "stateSHA256": "feb76fa14c9204d8586886fb289082487eb36fb012b886639a7045488846d8d1",
      "acceptedSteps": 0
    },
    {
      "stage": 3,
      "spans": 192,
      "modes": 96,
      "metricChosenThisStage": false,
      "fixedContinuousMetricSinceStage": 1,
      "sourceS": 2.021775895105453,
      "initialTraining": {
        "peak": 1.1169690898649165e-05,
        "rms": 3.7070037664170783e-06,
        "curvature": 5.112998583890547,
        "positiveMetricCoefficientLower": 0.9999953785539093,
        "areaRatioMinimum": 0.9999939313533636,
        "worstPhysicalRadialAndNativeTheta": [
          0.03972298230018822,
          0.0
        ],
        "radialRows": 1216,
        "angles": 512
      },
      "checks": {
        "adjointRelative": 1.1735057370287905e-13,
        "centralDirectionalRelative": 9.16709963180059e-12,
        "epsilon": 2e-06
      },
      "finalTraining": {
        "peak": 1.1169690898649165e-05,
        "rms": 3.7070037664170783e-06,
        "curvature": 5.112998583890547,
        "positiveMetricCoefficientLower": 0.9999953785539093,
        "areaRatioMinimum": 0.9999939313533636,
        "worstPhysicalRadialAndNativeTheta": [
          0.03972298230018822,
          0.0
        ],
        "radialRows": 1216,
        "angles": 512
      },
      "finalIndependent": {
        "peak": 1.116088090864834e-05,
        "rms": 3.707208567040762e-06,
        "curvature": 5.111168920308265,
        "positiveMetricCoefficientLower": 0.9999953785539093,
        "areaRatioMinimum": 0.999993929167087,
        "worstPhysicalRadialAndNativeTheta": [
          0.039053620559243524,
          0.004908738521234052
        ],
        "radialRows": 1538,
        "angles": 640
      },
      "independentPhysicalGeometry": {
        "minimumOutwardSupport": 0.817807521346325,
        "minimumAbsoluteHeight": 0.0,
        "heightRange": [
          0.0,
          1.7721142882990715
        ],
        "minimumAxialDerivative": 0.2316684720355038,
        "maximumOriginNorm": 1.892810361169815,
        "minimumArea": 0.12000578242342058,
        "leastSupportAtPrefixParameterAndNativeTheta": [
          0.28431223524920435,
          5.237624002156734
        ],
        "scope": "finite actual physical prefix; global radial offsets remain in the source metadata"
      },
      "stateSHA256": "09369a48cbf8398abcee717121ef561c2653da98d1f837a5e81dcaaf3df9e5ba",
      "acceptedSteps": 0
    }
  ],
  "originalTailAndCuffSpatiallyUnchanged": true,
  "continuousMetricCertificateObtained": false,
  "originalWholeGeometryCertificateTransferred": false,
  "elapsedSeconds": 541.2622797449999
}
```


## 可重算输出的身份

- r262-small-input-v2.json: SHA-256 `c0813a6309f0594b96b3de0977a60dec943a740cd77f9f4f61effa85e12fc8fc` (20989 bytes).
- r262-small-input-v2.npz: SHA-256 `09369a48cbf8398abcee717121ef561c2653da98d1f837a5e81dcaaf3df9e5ba` (113653 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
