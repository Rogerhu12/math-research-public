# 同一真实 a237：新圆参考与 R621 全域法向曲率

日期：2026-11-26 UTC；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

**状态：新公开 Actions 范围，未取得本 scope 的科学终态。**
本范围消费 [R621 完整法向分块界](../results/R621-normal-projected-covariant-blocks-and-reach-input.md)，
不改变材料场、原物理模型、等距门或 README 完成标准。

## 1. 实际 q 与比较面都换成最新同一状态

唯一非圆输入为
[run45887805731 原终态](2026-11-27-r582-physical-paid-resume-original-terminal.md)
的实际保留97q：
`a2377220dacda9eefe63f25a2000441f0169a0db5de9bc23840f90e5037a895e`，
p=.181，原完整11025×3072 η=`4.8302220914394944e-5`，
原物理/工作几何违约均0。未接受的 raw `a14dedce…` 不是本范围对象。
原 FINAL 364198 B/SHA-256
`e3371193ba4dcaa4df4d8298c856dce0663d2c4793d0cf205d625203af35ae47`。

比较圆面使用同一个 a237 的全部8个 log-radius 控制、8个 height 控制、
末帽高 `.6942718843124706`，圆 core 半径仍为 `.38`。
`SameFieldMeanGeometry(reference_q=q)` 独立构造该新参考；
材料 seed 商的旧冻结参考半径不改变。

[f1 全域几何原终态](2026-11-27-r582-retained-continuous-original-terminal.md)
已经为另一个 q 支付完整覆盖；本范围不移交它的圆参考、C0/C1/C2或 reach。
f1 所付527.88478224科学秒与其原全部费用继续保留；
新圆参考、新 C0/C1、新法向曲率都在本次为 a237 真正重算。
这里的新输入与几何不同，不能把旧 f1 的成功单元代入新 q。

## 2. 同场、无限尾与完整覆盖

先认证新圆面的全部紧区间二jets与曲率，使用原 R608 对所有
`abs(q[64:80])<3/5` 控制统一成立的无限尾引理，向外重叠尾入口。
准确全解析 H、原 μ/ν、原背景与自由包络、所有系数均保留。
R611旧 `CompactGeometry` 仅供应共享 H 的区间积分，
不调用它带旧 Q 的 `jets` 给新圆面授资格。
只有新圆面通过 R599 的全部条件才继续材料场重建；其 reach、D另付。

随后以原4609 B paid seed与原 positive chart 重建同一端点场一次：
rtol=`2e-11`、atol=`2e-13`、max_step=`.15`，保原factor8/core规则。
原七点诊断关闭为已支付身份，不重做旧优化、fine、Jacobian或方向门。
实际62878端点的 **knots连同全部endpoint jets** 必须给出原SHA
`0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`。
这不是只检查结位置。必要新ODE、端jets、材料准备和区间积分全部计费。

原完整97坐标、材料 quintic、全部 tail gates、完整圆角核心、
所有 B-spline 与全解析振荡高度进入原 same-field 盒。
相同区间同时取得 u/v 的值、s、ss、theta 及当前/参考 a/z 六jets。
原全角对称性给连续 T、T_s、T_ss 的零均值，R504 的连续 primitive 界直接适用。
有限 FFT 的观察误差不宣布为零，也不把数值 zero seed suffix 当成解析 H 的零尾。

证明分片覆盖整个 `[0,L]` 并保全部真实非零材料knots与命名gate；
只有已经从全部端jets证实的零seed后缀可合并冗余单元，数学场不改变。
同一材料z的完整中央柱、原正交镜像下半面、两完整Cartesian平帽均保留。
帽轴不使用除以a的圈坐标；完整盘差与曲率单独由原平盘定义处理。

## 3. 一次盒遍历中的 R621 组合

每个材料单元只取得一次上述角场与 mean 盒，再调用
`radial_block_with_normal_curvature(current,reference,u,v,difference=...)`。
原三个连续界 C0、C1 与完整协变 C2 仍全部计算和记录。
新增界先用同一参考法向投影三个协变块，再计入当前法向倾斜，
并把同一单元的两个参考主曲率和非对角块一起组成2×2特征值上界。
该 helper 返回的 `R621_principal_curvature_upper` 是原实际曲面的曲率界，
不是对全局完整 C2 范数再作一次三角估计。

精化目标为 C0≤`.0025`、α≤`.015`、实际K≤`18`。
β仍按原完整定义报告，**不再因为β>4而触发细化**。
目标只是组织细化：到深度/预算后仍有效的宽界照实进入全域最大值；
K不会被裁成18，也不会因为某个目标未满足就抹掉该单元。
若区间量尚无定义、非有限或为负，异常分支先清除无效bound；
继续细化或在容量处保留真正未决，不会把无效字典当作有效宽界接受。
无法证明局部浸入也同样处理。

四个全域上界各保留其 attainer 的同一单元小诊断，包括原完整协变块、
参考法向块、当前法向块、normal倾斜和该单元参考主曲率。
它们来自同一次调用，不引入第二遍科学观察。

## 4. 实际全局 K 进入 R604

只有全部材料域、柱、镜像与帽闭合后，才取全局

$$
\delta=\max C0,\qquad \alpha=\max C1,
\qquad K=\max K_{\rm R621}.
$$

λ的上界由向外区间 `1+α` 给出，法向投影差ν≤α；
不再由 `(1/rho+全局β)/(1−α)^2` 生成 K。
旧完整β仍在输出中，便于准确理解前一证书损失。

保持 R604 原近远弦证明：正项 artanh 前64项与严格几何尾包围，
在x≤3/4范围做32次二分并验证
`2λrho artanh(x)≤3/(2K)`，利用准确的3<π。
这个有限搜索上端只是一项保守限制，不再假设λKρ≥1。
每个被选择的短弦阈值都由原不等式实际成立来资格化。
其后仍为原向外算式

$$
\operatorname{reach}(X)\ge
\min\!\left\{\frac1K,
\frac{(d_*-2\delta)^2}{d_*^2/\rho+2\nu d_*+4\delta}\right\},
\qquad D_X\le D_0+2\delta.
$$

只有实际结果 `reach/D≥.03` 才标这一比例通过；K预算本身不授资格。
新圆完整、当前全覆盖、浸入/单射、实际 reach 下界与比例门分开输出。

## 5. 发布输入与费用范围

新科学范围1800秒，预留30秒尾记录；job上限40分钟。
原参考容量100000、范数细化预算250000、原单元最多6次二分保持。
范数容量限制细化，不能作为截去未覆盖材料的手段；
时限若留下未决则输出未完成，不把最大已见值升级成全域界。
所有原优化与 f1 几何费用在两份原收据中保留，新费用独立输出。

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| `scripts/r582_a237_normal_curvature_reach_20261127.py` | 23122 | `577211e39b11d3102cee6154bd209ada0a41a6138bedb7c69a56a67ca6f911ae` |
| `scripts/r621_normal_projected_curvature_20261127.py` | 8096 | `fa40dd40424cf6e0bea8f40b9bbfc485b32e971f3b5869359e0e59213c276b4a` |
| `computations/request-r582-a237-normal-curvature-20261127.json` | 18337 | `a156c7f369a0a64aa2ba60221ea4255c7c583c1f04ccb6122667ac4091110fe2` |
| `.github/workflows/visible-r582-a237-normal-curvature-20261127.yml` | 5539 | `f58e1d0481d1ac368acdf9caee3ac7c58b61c49db6f030a5425ae7c175ccbb8f` |

lane `actual-a237-normal-curvature`；stdin9089 B/SHA-256
`b9b22a3973c894d1c740acc13996a40ba92ed982459766203060879e37572ddc`。
34个源码/workflow绑定及精确稀疏路径齐备。
公开规则读至 `9515618fa868fa2a0851e00c7e05987ebcaee55b`，
私库规则读至 `1a995ebf0c19ea771ef0684a4f22bf94da9a960e`；
运行入口仍先实际pull双仓并查本会话认领、删除认证环境，再执行科学。
本地只完成源码、AST、JSON/hash和原日志/坐标提取，没有本地科学求值。

科学输出仅stdout与小attainer/叶流SHA，不保存可重算叶表、网格、
端点数组、artifact或缓存。即使本项reach比例通过，仍不支付同g等距、
大振幅时间族、固定g精化、无限核误差或 README 其余完成条件。
