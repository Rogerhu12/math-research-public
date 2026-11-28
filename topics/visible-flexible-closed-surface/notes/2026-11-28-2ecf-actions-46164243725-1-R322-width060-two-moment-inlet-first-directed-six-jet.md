# R322-width060-two-moment-inlet-first-directed-six-jet

**数值记录。** 2026-11-28 18:17:50 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `e245d3b9c248198413b6a99550833a4845a3532d`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

R322新实际三入口列状态的首个原外W单元，全三扇区真实六jet、冻结g、曲率/支撑/高度与两位置条件；解析24阶法角矩重新有向解准确a,b，三入口列自己的链导数。只登记本明列局部闭盒，不冒全外核。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R322-width060-two-moment-inlet-first-directed-six-jet；实际源码逐文件摘要列于下方。开始 2026-11-28 18:17:30 UTC，结束 2026-11-28 18:17:50 UTC。退出码 0。

```json
{
  "schema": "R322-W060-true-native-and-three-profiles-directed-full-Gram-and-geometry",
  "completed": true,
  "allSelectedPassed": true,
  "wholeOriginalCutPrefixCovered": false,
  "physicalProfilesPresent": true,
  "fullNativeAnglePeriod": "2pi/3",
  "analyticMomentAudit": {
    "scale": [
      "1",
      "1"
    ],
    "A": [
      "16656496291652076761/18446744073709551616",
      "16656496291652086773/18446744073709551616"
    ],
    "B": [
      "10185456700416119879/9223372036854775808",
      "636591043776206071/576460752303423488"
    ],
    "taylorDegree": 24,
    "TaylorRemainder": "sum |b_j| ((max |m+j|) w)^25/25!, 0<=both gates<=1",
    "normalizedPhysicalHalfPeriod": "pi/3",
    "sourceSHA256": "69f051bcaeb5d7914482f4e71856e39a28ed11dc11dfb293d9537f0113a42b63",
    "det": [
      "-11530083210858395393/4722366482869645213696",
      "-11530083210857332991/4722366482869645213696"
    ],
    "additiveConstant": [
      "-2393565921598635729/4611686018427387904",
      "-9574263686390200643/18446744073709551616"
    ],
    "additiveCos3": [
      "-5083322716137059781/9223372036854775808",
      "-10166645432268318075/18446744073709551616"
    ],
    "width": "0.060",
    "imposedSourceRadius": "exact R317 A",
    "momentReferenceSHA": "79ab0364deea643c13f332eadd880f179f2f310c8ab71f7fff36f784c2728d79"
  },
  "leafUpperRelativeGramExact": "7639246508318921821/36893488147419103232",
  "leafUpperRelativeGram": 0.20706219151179198,
  "unresolvedMetricBoxes": 0,
  "unresolvedGeometryBoxes": 0,
  "leafUpperOriginAndArmMixedSquares": [
    "12432867732161116473/9223372036854775808",
    "3237698286222673343/288230376151711744"
  ],
  "unresolvedShapeBoxes": 0,
  "selected": [
    25
  ],
  "closed": [
    {
      "element": 25,
      "unresolved": 0
    }
  ],
  "originalFieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA256": "6eac8473f4d90c5e7ed160701278bbf421e82c30c4cd53557bde939275a218bc",
  "sourceSHA256": "e8ec4d64406718a7a7ccff345481fe617b9b3ef5e8ec5a589d8fceb3cfd64d98",
  "kernelSHA256": "ce0593ff10e6b0b07d2d4cae0eceaf649bc44d42785fd25f9cc161350a0a87d1",
  "nativeSourceCells": 2569,
  "commonRefinedRows": 3,
  "acceptedBoxes": 654,
  "unresolvedBoxes": 0,
  "firstUnresolved": [],
  "acceptedDirectedMinima": {
    "height": 0.3499999900581561,
    "support": 0.7429226227929897,
    "area2": 0.0392182169438394,
    "curvatureFormMin": 0.023540820503976014
  },
  "limits": {
    "curvature": "200/23",
    "support": "23/200",
    "height": "87/250"
  },
  "sleeveExact": "7/20",
  "actualCuffExact": "2702159776422297/18014398509481984",
  "metricClock": "new radial spline coefficients evaluated at origin+(Sf-origin)(s-origin)/(S-origin), with actual algebraic S; old W evaluated with actual T1",
  "seconds": 16.367670915000417,
  "scope": "Only the explicitly selected outer prefix cover. Each box consumes all six jets, original tail interface, optional Cauchy profiles and a common frozen metric. The central belt and post-prefix full tail are separate."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r322-actual-060-profiles-directed-whole-geometry.py: SHA-256 `e8ec4d64406718a7a7ccff345481fe617b9b3ef5e8ec5a589d8fceb3cfd64d98` (20868 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `91b0653ff3423fec27402e6f4b25cab1ebaefd4681794857c2c450b7354575ee` (111563 bytes).
- 2ecf-r322-actual-060-profiles-directed-whole-geometry.py: SHA-256 `e8ec4d64406718a7a7ccff345481fe617b9b3ef5e8ec5a589d8fceb3cfd64d98` (20868 bytes).
- 2ecf-r322-directed-two-moment-060-normal-angle-and-inlet-jets.py: SHA-256 `69f051bcaeb5d7914482f4e71856e39a28ed11dc11dfb293d9537f0113a42b63` (6125 bytes).
- 2ecf-r262-adjacent-low-ports-two-moment-060-physical-cut.py: SHA-256 `e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e` (13494 bytes).
- h1-inlet-first-directed.json: SHA-256 `94c6fde9cbb40fdb2655050b511c2137b86db0ec398d0c0b98b12e854f88a866` (4617 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
