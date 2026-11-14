# 新wc01全160格：首个真实非线性有限DN响应

2026-11-12，numerical_recovery。**有限数值证据，非无限尾或强目标闭曲面证明。**

## 实际求解与保存

`2026-11-12-fd2d-numerical-gc-layered64-full160-03-response.json`
为实际完整响应，796816B，SHA256
`ddfcc5031283f5b3f4b739598a5ec3554aba168a922ad73d62fcd2d2c21af9d6`。
session66020，launch782b49，completione2cfee，工具exit0、Node自然exit0，482.038363472秒。
完整关闭资料见同stem `-completion-and-closed-manifest.json`。

固定物理输入wc01 cfg SHA
`d4d41047c5afa1df90e17e3814e896a7cd91f64c79d0e11116e071cb97e17994`。
全部修改格0…159确实进入非线性方程；160之后的原source用于有限far196线性图。
M4、材料偶模spacing2、N64、parts2、每stage32步、linearSteps256，原floor .05、tol2e−9。
唯一非零cut高度系数为REAL cosine $h_2=-10^{-9}$，不另乘$\sqrt2$。
上半物理高度约定仍是$z=-h_{worker}$。

03从02真实accepted2原样复制canonical状态。完整全F/J先复现
.0016237283781452912；直接无量纲L的相同Q/L试步经完整2880段F接受到
`1.6067532721703842e−14`。随后完整F/J再次给同一值，并执行原实际两jet/audit。
没有放宽方程、floor、tol或接受规则。
此前raw次正规数丢试步的实际定位与修复见
`2026-11-12-fd2d-numerical-gc-deep-entry.md`。

## 完整有限响应中的数值

| 量 | 实际返回值 |
|---|---:|
| normalized shooting residual | $1.6067532721703842\,10^{-14}$ |
| 全有限采样minA | .9950578044371454 |
| 全有限采样minD | .9999999983990018 |
| 实际诱导metric采样最大相对算子误差 | $1.8006670960632826\,10^{-15}$ |
| formal height主曲率采样峰 | 6.996605030552903 |
| 全有限physical Darboux峰 | $1.6227227350293808\,10^{-19}$ |
| 直接normalized Darboux峰 | $7.834228057945758\,10^{-14}$ |
| physical holonomy采样峰 | $2.1873030308988874\,10^{-24}$ |
| height peak-to-valley | $1.9999999999993032\,10^{-9}$ |
| cut mean slope correction | $1.180000000021251\,10^{-16}$ |
| cut mean second correction | $3.162399998529961\,10^{-15}$ |

这些是同一真实有限轨道的有限角/径向采样结果，不是连续全域上界。
`formalCurvature`保留原字段含义，不替换真实发展图的连续曲率或全局reach证明。
完整56项physical-height Jacobian已包含：4个slope、4个second、两个mean修正、4个height行，
列为4个REAL材料偶模cut高度。

实际cut半径.5000000000000001，背景slope .0999999999999999、second −1.3999999999999981；
这保留浮点源的实际返回值，不把它覆写成名义十进制常数。
可用`TailGCJetPort.from_worker_record(response, spacing=2)`消费此响应。
切口本身的近似n,m端口不自动支付真实位置/标架/两jet接合，相关范围仍按R117/R126。

## 原完整均值积分的恢复

v7响应协议尚未打印solver已经计算的`meanHeightToCut`。
为避免丢掉这个真实量，`scripts/fd2d-gc-tail-retained-means.mjs`
只读最后完成的full-J全部90个V8块，逐一验证保存时SHA、key、覆盖顺序和维数，
按原`flows.reduce`的次序累加2880个已算scalar，没有再次求ODE或插值。

准确复现的binary64原序和为

$$
\texttt{finite meanHeightToCut}=0.01656419930131588.
$$

同stem `-retained-means-data.json.gz` 保全部实际stage标量，25730B，SHA256
`67da713a34c7a0d5ac4253dded74236025eb43b10c4be325b79c2af8e7de84a7`；
`-retained-means-report.json` 保完整key/inputHash与90块来源。
提取脚本实际工具chunkd9d237、exit0。

这是node160处均值高度锚为0的**有限160格积分**。
它和另一个网格上的背景积分略有数值差异；不把两者差全部说成非线性效应。
原未改无限深尾的贡献和有限Robin误差仍须按最终构造处理。
03的保存足以恢复实际有限端口，不能由极小末态单独宣称无限非线性平接已经证明。

## 后续真实请求

04已从该完整响应启动，session59895/launchfb5476，独立运行树
`/workspace/scratch/fd2dbfd2c83e/visible-flex-gc-layered64-nonlinear-04`。
v8的Q/L幅度warm也直接保留无量纲L；相同物理曲线缩放不再经过次正规raw斜率。
其数学定义仍是Q与非均值L同乘scale，均值由原完整root重新决定。
worker现在将原`meanHeightToCut`直接写入每个响应。

三项明确请求为$h_2=-2\,10^{-9},-4\,10^{-9},-8\,10^{-9}$，
每项都要求原真实全F/J、actual两jet和finite audit。
只有每个实际响应返回后才写它的结果；当前计划本身不构成响应。
父代理继续新的强前缀/外层设计，geometry继续优化前谷。
这里的极小有限尾仅是完整强目标求解的可恢复数值起点。
