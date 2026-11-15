# actual103：完整 noJ 邻词均未改善，原完整 R273 十档仍拒绝

/root GPT-6 Astra Pro（AI-assisted），2026-11-15。原全部科学计算由公开仓库 Actions 完成，root只读原日志、字段与字节身份。

## 实际运行与首因

[run43681829913](https://github.com/Rogerhu12/math-research-public/actions/runs/43681829913)，source `301d0b6429ae273cf745fdb7fe8e4696f9786e89`，job132713895446。实际 job failure/入口exit2；worker自身exit0并返回原未收敛响应。首因是原 multiple-shooting iteration0 的十档 line search 均未降低原 norm，非桥接异常、QR失败或新身份门。原最大32轮、每轮10档、η1、tol $2	imes10^{-9}$ 均未改。实际零接受，未返回要求的最终完整J，没有final audit，不可作接受锚。

原 failed73 初猜 SHA `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6`；本轮实际 fresh-withJ norm 与完整 noJ base 均为 `6.0618737006888706e-5`。

## 三次完整 noJ 建议评价

每点都实际调用原完整 evaluate，含129248残差行（cut112、stage576×224、far112），没有局部重组冒全模型。node11/Q76/column75 的三个 binary64 小端词为：

| 点 | 值 | 原词 | 原完整 noJ norm | 严格小于基值 |
|---|---|---|---|---|
| base | 7.191817341159996e-16 | `6e1cafdb47e9c93c` | 6.0618737006888706e-5 | false |
| −1 ULP | 7.191817341159995e-16 | `6d1cafdb47e9c93c` | 6.848278937534994e-5 | false |
| +1 ULP | 7.191817341159997e-16 | `6f1cafdb47e9c93c` | 6.749978282929229e-5 | false |

三次最大行均为 stage10/row187/Pi76/global2539，原 σ 为 `5.170054771158893e-15`，三次无非有限残差。原 noJ 的 minA/minD 字段在这些建议记录中为正无穷占位，不能把它们写成新的连续域下界。没有邻词被选为方向；实际走 `same-fresh-withJ-complete-R273-QR`。

## 完整 R273 方向与原十档

原完整 QR 成功：129248×129248，增广258496行，576 stage、577节点、224块宽、577份节点惩罚、1153次QR、1152次formation，原readback全部129248行。factor及常数464891392B，在原2GiB上限内；原报告无形成下溢到binary64零。工作longdouble报告64有效位，不冒binary128或严格误差界。

实际该完整仿射方向的原 exact dyadic 残差最大值十进制显示 `9.685623139820915231897967296720853552003562611702521449132211420E-11`，最大行为stage9/Q1/global2128。它是固定有限J/r/σ仿射模型的精确读回，不是 nonlinear noJ 接受。实际方向SHA `4b4b1aaacd96910635a03f97d45957ae995c724997a0e18b66ac1d06408e294a`。

| trial | 原 step | 实际原完整 noJ norm | 原拒绝原因 |
|---:|---:|---:|---|
| 0 | 1 | 0.00019266928302730032 | residual-not-decreasing |
| 1 | 0.5 | 0.00013090599247904327 | residual-not-decreasing |
| 2 | 0.25 | 0.00012144901300393549 | residual-not-decreasing |
| 3 | 0.125 | 0.00011814265821233656 | residual-not-decreasing |
| 4 | 0.0625 | 6.569760416151993e-05 | residual-not-decreasing |
| 5 | 0.03125 | 0.00010632854139856965 | residual-not-decreasing |
| 6 | 0.015625 | 6.848278937534994e-05 | residual-not-decreasing |
| 7 | 0.0078125 | 6.0618737006888706e-05 | residual-not-decreasing |
| 8 | 0.00390625 | 6.0618737006888706e-05 | residual-not-decreasing |
| 9 | 0.001953125 | 6.0618737006888706e-05 | residual-not-decreasing |

十档全部拒绝；最后三档回到基norm。最初完整native响应记录minA `0.9999999999759498`、minD `0.9999999999999858`，没有当前接受解。既不把仿射残差变小冒非线性收敛，也不从这一点、两邻词和一个方向推断普遍浮点误差底线、局部最优或无解。

## 原件身份与清理范围

| 对象 | bytes | SHA-256 |
|---|---:|---|
| 实际紧凑summary（排序紧凑JSON含LF，root重建字节核一致） | 3327 | `865250bd67903a6f65285cd5a7f09add5ba7aa4d1d73c6dbdb67b703134fa5d2` |
| 原完整response | 1332010 | `6cdeafa8dcca216312a6e0a630d581ad16a26c87e66ceb83b8ab9eae8f170697` |
| 实际job log | 88780 | `434923f06c8f800058f89befc184682dc20be0728c637b09315148d2c4445adc` |

原result SHA `2151903c5f30a967aafe21b06b3e82ad2a8e9572b4b393ea3d17480d759fd7f7`，proposal result `d711bde12b4ffe2b609841a7a1fed164817960edbb4f332c2aed017c7e6878d6`，QR result `c55e57ce2f921f8991beae70bbb82ba5127bcb6b34676f4a907689f8d9bc51ad`，fresh snapshot `8fa0728db0bb0d16a1378813013c608f1a038099750cd2fcd66e45d93f21cb2f`。source driver `c8c072e0d65567ba86e9fb72d3708ef5771c8b4ee475e9fcec611371cd447c79`，proposal `436cfde61ed98720f0e0802978dc4874c42eb42a0193e426b5c5e9e3e0261037`，原 evaluate `9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9`。

可重算raw未上传artifact、Git或Release。结束后自身solver输出和临时原source已删除；parent91临时目录清理记录PermissionError，不能宣称三目录全部即时删除，runner生命期结束后由平台回收。该清理错误不是本次数学停止原因。

## 继续方向

不要重复failed95/103作为接受锚或继续猜相同词。下一步根据原cellFlow/noJ primal的表示与精度及已有高精度矩阵实验，寻找保持同一数学方程、原域和原接受阈值的具体改进；在没有实际新结果之前，fullDN、当前H的原FD及闭面流水线继续标为未完成。并行31-query原域/RMS链及低三方程完整三列方向继续工作。
