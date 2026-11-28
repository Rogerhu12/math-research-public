# R319-actual-0350-two-free-scalars-all-full-rings

**数值记录。** 2026-11-28 17:23:23 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `6b9f18a6cc8ad2626658a0021520df1583636887`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

R319同一冻结g上真正自由的逐环高度Z与水平切角β，由全D3中心化角原函数重建三维闭环，目标角速度进入完整E/F及所有交块带状求解；每span不同径行、16/27/49真法角。母场、投影初值、优化场在三网分别报；CubicSpline角积分及Pqq角导是有限求值，准确连续定义的G恒等式不冒作当前有限插值场证书。新专用状态需自身全几何。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R319-actual-0350-two-free-scalars-all-full-rings；实际源码逐文件摘要列于下方。开始 2026-11-28 17:22:23 UTC，结束 2026-11-28 17:23:23 UTC。退出码 0。

```json
{
  "schema": "R317-full-D3-rings-open-height-and-horizontal-angle-with-fixed-angular-speed-v1",
  "entrySHA": "6f84c4d84a940aa34f7236b39e5c5fbbd33164b1ce5c0c1c62c62091e8a8dcd3",
  "twoScalarSHA": "6d18eff6ca9268fe29e2dd6194643d807362729c2792e988b2cde9d579a52195",
  "parentSHA": "104a8843272816e31129ff8fabce2dbfad6ad98b41f16975496f91dc1b19181d",
  "stateSHA": "a665ad95facc4a48dbb5fce2d8b00c4e7c0364fc1493cfe31028b7a4bc57ddc1",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "angularStrength": 1.0,
  "freePhysicalScalars": 975,
  "frozenMetricVariables": 0,
  "radialSpans": 40,
  "grid": [
    {
      "actualRadial": 399,
      "sectorNodes": 125,
      "materialTargets": {
        "fullUniform": 264,
        "additionalMaterialTargets": 108,
        "perTransitionInterior": 16,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "original": {
        "peak": 0.005017893073137871,
        "rms": 0.0010667141725034586,
        "curvature": 8.66788718014024
      }
    },
    {
      "actualRadial": 503,
      "sectorNodes": 189,
      "materialTargets": {
        "fullUniform": 387,
        "additionalMaterialTargets": 174,
        "perTransitionInterior": 27,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "original": {
        "peak": 0.005018990348916327,
        "rms": 0.0010989146037125412,
        "curvature": 8.667220001556904
      }
    },
    {
      "actualRadial": 615,
      "sectorNodes": 324,
      "materialTargets": {
        "fullUniform": 663,
        "additionalMaterialTargets": 306,
        "perTransitionInterior": 49,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "original": {
        "peak": 0.005016507112003386,
        "rms": 0.001119378338134046,
        "curvature": 8.666722450135738
      }
    }
  ],
  "initial": {
    "peak": 0.008753694577811189,
    "rms": 0.0013100546294473427,
    "curvature": 8.666572195403404,
    "minimumHorizontalAngularSpeed": 0.11999999946289142,
    "minimumSupport": 0.5953391588769188,
    "minimumArea": 0.11999999946243714,
    "minimumZs": 0.22779151711966464,
    "angularComponent": 0.00014173043922616202,
    "worstMetric": [
      0.5446326307569678,
      1.2851969946503699,
      1.459826523705399
    ],
    "worstCurvature": [
      0.4756934185876708,
      2.0943951023931953,
      2.0943951023931944
    ]
  },
  "initialSecondary": {
    "peak": 0.008776587407493123,
    "rms": 0.0013270689967190494,
    "curvature": 8.665901789542335,
    "minimumHorizontalAngularSpeed": 0.11999999946289142,
    "minimumSupport": 0.595360101245213,
    "minimumArea": 0.11999999946243714,
    "minimumZs": 0.2277823476627292,
    "angularComponent": 0.0001416430158729387,
    "worstMetric": [
      0.5417333333333334,
      1.27449624447958,
      1.442567239899837
    ],
    "worstCurvature": [
      0.47506666666666664,
      2.0943951023931953,
      2.0943951023931944
    ]
  },
  "accepted": {
    "actualCompletedSteps": 5
  },
  "physicalJacobianCheck": [
    2.9461588308840166e-12,
    7.45985198726051e-13
  ],
  "projectedInitialHoldout": {
    "peak": 0.008768664070130602,
    "rms": 0.0013470666590569614,
    "curvature": 8.665402597026405,
    "minimumHorizontalAngularSpeed": 0.11999999946289142,
    "minimumSupport": 0.5953693998746838,
    "minimumArea": 0.11999999946243714,
    "minimumZs": 0.22785828283307216,
    "angularComponent": 0.00014171964390785607,
    "worstMetric": [
      0.5399545167058113,
      1.269904722718046,
      1.4351080546390003
    ],
    "worstCurvature": [
      0.47471448177486675,
      2.0943951023931953,
      2.0943951023931944
    ]
  },
  "independent": {
    "peak": 0.007154181327954313,
    "rms": 0.0020787271619242937,
    "curvature": 8.689809135964055,
    "minimumHorizontalAngularSpeed": 0.11999999946289142,
    "minimumSupport": 0.6047627577833948,
    "minimumArea": 0.11999999946243714,
    "minimumZs": 0.22827075610811656,
    "angularComponent": 0.00014171964390785607,
    "worstMetric": [
      1.2013682272422794,
      0.4264605412112841,
      0.17103697342900254
    ],
    "worstCurvature": [
      0.47232506549552095,
      2.0943951023931953,
      2.0943951023931944
    ]
  },
  "scope": "The continuous curve definition uses its D3-centered angular primitive. At unit angular strength the exact target G is prescribed on the part q<=liftEnd before blending back to the actual boundary speed. Reported E,F, curvature and support are finite quadrature observations from independent material-angle grids."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-adjacent-two-open-scalars-full-angular-target.py: SHA-256 `6f84c4d84a940aa34f7236b39e5c5fbbd33164b1ce5c0c1c62c62091e8a8dcd3` (9630 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `7693790913541fcf9e6f45501cc30d10b9e7478b7393d9badd9e6e8f1d90bb12` (66092 bytes).
- 2ecf-r262-adjacent-two-open-scalars-full-angular-target.py: SHA-256 `6f84c4d84a940aa34f7236b39e5c5fbbd33164b1ce5c0c1c62c62091e8a8dcd3` (9630 bytes).
- 2ecf-r262-centred-full-ring-height-and-angle.py: SHA-256 `6d18eff6ca9268fe29e2dd6194643d807362729c2792e988b2cde9d579a52195` (7471 bytes).
- h1-two-open-scalars.json: SHA-256 `c975d54b4e3fb0104c8f7f1606b03c1791d3f0c6d566ca2cb8329381a9b13b9a` (11574 bytes).
- h1-two-open-scalars.npz: SHA-256 `a665ad95facc4a48dbb5fce2d8b00c4e7c0364fc1493cfe31028b7a4bc57ddc1` (9586 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
