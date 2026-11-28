# R319-actual-0350-inlet-profile-first-directed-six-jet

**数值记录。** 2026-11-28 18:15:31 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `0b52d82c3d44e5fd2860c6aad829509a2a16a90e`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

R319真实三入口列本身的首个外原W单元闭区间六jet：N/k、准确原X+C+W口差、ez/k²与新XYZ、冻结g同算。归一化法角矩用24阶解析矩和严格余项；全三个扇区而不借反射。此单元只是局部连续结果，所报两形状平方与相对Gram上端均来自本实际状态，不代全域或整闭reach。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R319-actual-0350-inlet-profile-first-directed-six-jet；实际源码逐文件摘要列于下方。开始 2026-11-28 18:14:56 UTC，结束 2026-11-28 18:15:31 UTC。退出码 0。

```json
{
  "schema": "R317-R319-actual-native-and-three-angular-profiles-closed-box-Gram-and-geometry-v1",
  "completed": true,
  "allSelectedPassed": false,
  "wholeOriginalCutPrefixCovered": false,
  "physicalProfilesPresent": true,
  "fullNativeAnglePeriod": "2pi/3",
  "analyticMomentAudit": {
    "scale": [
      "902817449780889679/1152921504606846976",
      "14445079196494252117/18446744073709551616"
    ],
    "A": [
      "16656496291652076761/18446744073709551616",
      "16656496291652086773/18446744073709551616"
    ],
    "B": [
      "5099534778321584357/4611686018427387904",
      "5099534778321586451/4611686018427387904"
    ],
    "taylorDegree": 24,
    "TaylorRemainder": "sum |b_j| ((max |m+j|) w)^25/25!, 0<=both gates<=1",
    "normalizedPhysicalHalfPeriod": "pi/3",
    "sourceSHA256": "79ab0364deea643c13f332eadd880f179f2f310c8ab71f7fff36f784c2728d79"
  },
  "leafUpperRelativeGramExact": "11922460265786364465/147573952589676412928",
  "leafUpperRelativeGram": 0.0807897332596105,
  "unresolvedMetricBoxes": 0,
  "unresolvedGeometryBoxes": 3841,
  "leafUpperOriginAndArmMixedSquares": [
    "6227478174601299093/4611686018427387904",
    "6479514835238565845/576460752303423488"
  ],
  "unresolvedShapeBoxes": 0,
  "selected": [
    25
  ],
  "closed": [
    {
      "element": 25,
      "unresolved": 3841
    }
  ],
  "originalFieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA256": "828793b5b8556e9b3e4d4e969f1688df7dc8dc9f990f8d00753adfb992a4c7ea",
  "sourceSHA256": "08fb9f50d939382e32b9eed8f387d81300241618a78f3f9c523ca4dc446ecf7a",
  "kernelSHA256": "ce0593ff10e6b0b07d2d4cae0eceaf649bc44d42785fd25f9cc161350a0a87d1",
  "nativeSourceCells": 2569,
  "commonRefinedRows": 3,
  "acceptedBoxes": 4724,
  "unresolvedBoxes": 3841,
  "firstUnresolved": [
    {
      "element": 25,
      "cell": 535,
      "native": [
        "48959986852908185897539821449739380921125045107213936016361310619544524081820442600895567116073420023087173169744483354143985325199978441/139707150368955118875431541532171465024200719518761927539294707361932378660098869242726409158435415811791855872660754015297558789197135872",
        "73533706615023093722512737575731494479395054529081629782447497869588817679655429697663020412860320924254433566639622628154321545079410523/209560725553432678313147312298257197536301079278142891308942061042898567990148303864089613737653123717687783808991131022946338183795703808"
      ],
      "depth": 2,
      "firstAngleIndex": 307
    },
    {
      "element": 25,
      "cell": 535,
      "native": [
        "73533706615023093722512737575731494479395054529081629782447497869588817679655429697663020412860320924254433566639622628154321545079410523/209560725553432678313147312298257197536301079278142891308942061042898567990148303864089613737653123717687783808991131022946338183795703808",
        "147254865901367817197431485953707835154205082794684711080706059619721698473160390987965380303221023627756214757325040450185330204717706769/419121451106865356626294624596514395072602158556285782617884122085797135980296607728179227475306247435375567617982262045892676367591407616"
      ],
      "depth": 2,
      "firstAngleIndex": 215
    },
    {
      "element": 25,
      "cell": 535,
      "native": [
        "147254865901367817197431485953707835154205082794684711080706059619721698473160390987965380303221023627756214757325040450185330204717706769/419121451106865356626294624596514395072602158556285782617884122085797135980296607728179227475306247435375567617982262045892676367591407616",
        "792158417600651/2251799813685248"
      ],
      "depth": 2,
      "firstAngleIndex": 163
    },
    {
      "element": 25,
      "cell": 536,
      "native": [
        "792158417600651/2251799813685248",
        "12692745219946063/36028797018963968"
      ],
      "depth": 2,
      "firstAngleIndex": 146
    },
    {
      "element": 25,
      "cell": 536,
      "native": [
        "12692745219946063/36028797018963968",
        "6355477879140855/18014398509481984"
      ],
      "depth": 2,
      "firstAngleIndex": 125
    },
    {
      "element": 25,
      "cell": 536,
      "native": [
        "6355477879140855/18014398509481984",
        "12729166296617357/36028797018963968"
      ],
      "depth": 2,
      "firstAngleIndex": 106
    }
  ],
  "acceptedDirectedMinima": {
    "height": 0.34999989692759975,
    "support": 0.8598039330276321,
    "area2": 0.03941457708095682,
    "curvatureFormMin": 0.0008841484275436737
  },
  "limits": {
    "curvature": "200/23",
    "support": "23/200",
    "height": "87/250"
  },
  "sleeveExact": "7/20",
  "actualCuffExact": "2702159776422297/18014398509481984",
  "metricClock": "new radial spline coefficients evaluated at origin+(Sf-origin)(s-origin)/(S-origin), with actual algebraic S; old W evaluated with actual T1",
  "seconds": 31.05954551100058,
  "scope": "Only the explicitly selected outer prefix cover. Each box consumes all six jets, original tail interface, optional Cauchy profiles and a common frozen metric. The central belt and post-prefix full tail are separate."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r317-actual-inlet-profiles-directed-whole-geometry.py: SHA-256 `08fb9f50d939382e32b9eed8f387d81300241618a78f3f9c523ca4dc446ecf7a` (20864 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `91b0653ff3423fec27402e6f4b25cab1ebaefd4681794857c2c450b7354575ee` (111563 bytes).
- 2ecf-r317-actual-inlet-profiles-directed-whole-geometry.py: SHA-256 `08fb9f50d939382e32b9eed8f387d81300241618a78f3f9c523ca4dc446ecf7a` (20864 bytes).
- 2ecf-r317-directed-normal-angle-moments-and-inlet-jets.py: SHA-256 `79ab0364deea643c13f332eadd880f179f2f310c8ab71f7fff36f784c2728d79` (8284 bytes).
- 2ecf-r262-adjacent-low-ports-support-physical-cut.py: SHA-256 `94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6` (12244 bytes).
- h1-inlet-first-directed.json: SHA-256 `b95f30b738e066ad5443c79244273a0c7bd2e0ad3d2705e4bbcf52ea4eaa7a28` (6690 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
