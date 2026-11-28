# R321-two-moment-physical-inlet-first-directed-six-jet

**数值记录。** 2026-11-28 18:17:26 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `b39cbf57943470c6f004b2a9c01bee7cbad0a925`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

R321新实际三入口列状态的首个原外W单元，全三扇区真实六jet、冻结g、曲率/支撑/高度与两位置条件；解析24阶法角矩重新有向解准确a,b，三入口列自己的链导数。只登记本明列局部闭盒，不冒全外核。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R321-two-moment-physical-inlet-first-directed-six-jet；实际源码逐文件摘要列于下方。开始 2026-11-28 18:17:06 UTC，结束 2026-11-28 18:17:26 UTC。退出码 0。

```json
{
  "schema": "R321-W040-true-native-and-three-profiles-directed-full-Gram-and-geometry",
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
      "5095720762572136897/4611686018427387904",
      "10191441525146572451/9223372036854775808"
    ],
    "taylorDegree": 24,
    "TaylorRemainder": "sum |b_j| ((max |m+j|) w)^25/25!, 0<=both gates<=1",
    "normalizedPhysicalHalfPeriod": "pi/3",
    "sourceSHA256": "f540ca339ff4ba26cbfac44c864bc67b8cddc8d9f24e94d60cf8b6c8ebcd0ffd",
    "det": [
      "-12898760803479902721/4722366482869645213696",
      "-12898760803478778687/4722366482869645213696"
    ],
    "additiveConstant": [
      "-13939274905842551759/36893488147419103232",
      "-13939274905835013407/36893488147419103232"
    ],
    "additiveCos3": [
      "-216831922907197009/576460752303423488",
      "-13877243066050263493/36893488147419103232"
    ],
    "width": "0.040",
    "imposedSourceRadius": "exact R317 A",
    "momentReferenceSHA": "79ab0364deea643c13f332eadd880f179f2f310c8ab71f7fff36f784c2728d79"
  },
  "leafUpperRelativeGramExact": "15277944091619003137/73786976294838206464",
  "leafUpperRelativeGram": 0.2070547521905675,
  "unresolvedMetricBoxes": 0,
  "unresolvedGeometryBoxes": 0,
  "leafUpperOriginAndArmMixedSquares": [
    "6223049149967638625/4611686018427387904",
    "12955727316311965999/1152921504606846976"
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
  "stateSHA256": "f638dc99f7edd7a54dbbd3fff3614aa593812088004d642ae50ec1c8a0f1b95f",
  "sourceSHA256": "bfc3168639a76837721ced25b1fd40455e706fb90f8de6e59aa6b8e5e1a5d60c",
  "kernelSHA256": "ce0593ff10e6b0b07d2d4cae0eceaf649bc44d42785fd25f9cc161350a0a87d1",
  "nativeSourceCells": 2569,
  "commonRefinedRows": 3,
  "acceptedBoxes": 648,
  "unresolvedBoxes": 0,
  "firstUnresolved": [],
  "acceptedDirectedMinima": {
    "height": 0.349999989954257,
    "support": 0.7430134421248766,
    "area2": 0.03921806658622927,
    "curvatureFormMin": 0.016419740081056268
  },
  "limits": {
    "curvature": "200/23",
    "support": "23/200",
    "height": "87/250"
  },
  "sleeveExact": "7/20",
  "actualCuffExact": "2702159776422297/18014398509481984",
  "metricClock": "new radial spline coefficients evaluated at origin+(Sf-origin)(s-origin)/(S-origin), with actual algebraic S; old W evaluated with actual T1",
  "seconds": 16.439112219999515,
  "scope": "Only the explicitly selected outer prefix cover. Each box consumes all six jets, original tail interface, optional Cauchy profiles and a common frozen metric. The central belt and post-prefix full tail are separate."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r321-actual-profiles-directed-whole-geometry.py: SHA-256 `bfc3168639a76837721ced25b1fd40455e706fb90f8de6e59aa6b8e5e1a5d60c` (20860 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `91b0653ff3423fec27402e6f4b25cab1ebaefd4681794857c2c450b7354575ee` (111563 bytes).
- 2ecf-r321-actual-profiles-directed-whole-geometry.py: SHA-256 `bfc3168639a76837721ced25b1fd40455e706fb90f8de6e59aa6b8e5e1a5d60c` (20860 bytes).
- 2ecf-r321-directed-two-moment-normal-angle-and-inlet-jets.py: SHA-256 `f540ca339ff4ba26cbfac44c864bc67b8cddc8d9f24e94d60cf8b6c8ebcd0ffd` (6125 bytes).
- 2ecf-r262-adjacent-low-ports-two-moment-physical-cut.py: SHA-256 `29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902` (13494 bytes).
- h1-inlet-first-directed.json: SHA-256 `270ca5c02055df60d69a193cb1a24d73cf207518fed6a24fc693d0b632856e0e` (4621 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
