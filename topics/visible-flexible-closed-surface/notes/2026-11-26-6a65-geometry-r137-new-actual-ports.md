# R137 的新实际入口与完整出口：空间截面的失败和水平投影后的 .35 段

日期：2026-11-26。会话：Astra-visible-flex-6a65e705。

本记录消费既有 [R137](../results/R137-flat-coast-ruling-two-jets-and-actual-inlet-consumer.md)，不重新登记 ruling 公式。本次产物是一个从真实强场截面取得、再明确改变输入的准确形式 flat 段，和它的完整 Cartesian 两端口。它没有消掉相邻非 flat 段，也没有把近似入口的度量误差当成准确入口。

## 1. 来源、改变了什么

来源是 [固定峰行三次真实 LM](2026-11-26-6a65-geometry-fixed-peak-three-accepted.md) 的第三态，SHA-256 为 `5ecb4119827baa02480304ab52a5638ad617843bb0ed2ec9d51a0a906f550288`。该态的 gap 为 1，外段延长量为 .05，时钟比例为 1，真实 cutoff 高度约 .51007661。这个输入有完整近似场，但没有准确的 E/F 度量证书。

脚本 [6a65-geometry-r137-inlet-samples.cjs](../scripts/6a65-geometry-r137-inlet-samples.cjs) 从同一个 `createGapLengthState` 和实际 `position.slice` 取 512 个全周期点及 `X,Xs,Xu,Xss,Xsu,Xuu`。没有从第二基本形式另积分位置。

脚本 [6a65-geometry-r137-exact-inlet-consumer.py](../scripts/6a65-geometry-r137-exact-inlet-consumer.py) 把所取位置定义成一个新的有限实 Fourier 曲线，阶数明确写入参数。可选 `--planar` 的含义是：将该新曲线的 z 坐标换成旧截面 z 的平均值，保留 x/y 的 Fourier 曲线。这是真正的输入变更；报告同时记录位置、前两阶导数和完整端口两jets的差。没有分别投影 T、d、m、n 后假定它们兼容。

## 2. 新入口为何具有准确形式

设新曲线为 $\Gamma(\theta)$，周长为 $P$，定义

$$
a=\frac P{2\pi},\qquad
u=\frac1a\int_0^\theta|\Gamma_\vartheta|\,d\vartheta,
\qquad T=\frac{\Gamma_u}{a}.
$$

只要 $\Gamma_\theta\ne0$，这是严格单调、周期为 $2\pi$ 的弧长参数。写

$$
q=|T_u|,\quad U=T_u/q,\quad V=T\times U,\quad
r=v/q,\quad c=\sqrt{1-r^2},
$$

并要求真正的全角条件 $q>v>0$。定义

$$
d=-rU+cV,\quad N=d\times T=cU+rV,
\quad n=\frac{qc}{a},\quad m=\frac{d_u\cdot N}{a}.
$$

于是 $d,T,N$ 是正交单位标架，$n>0$。由 $d\cdot T_u=-v$ 及各单位向量的导数正交性，直接得到

$$
\Gamma_u=aT,\quad d_u=vT+amN,\quad
T_u=-vd+anN,\quad N_u=-amd-anT.
$$

因此这些是 R137 所要求的准确入口恒等式，而不是拟合残差方程。所有导数由同一 Fourier 曲线、弧长链式法则和以上公式计算。段内的新度量明确定义为

$$
g=d\sigma^2+(a+v\sigma)^2du^2.
$$

该段上必须将旧设计的 rho 修正设为零，将任何改变径向时钟的支撑放在段外；本记录没有把旧场的非仿射 `a(s)` 偷换成这条仿射函数。

数值实现用 128 个面板、每面板 16 点 Gauss 求周长和弧长反函数。数学定义使用准确积分；本次没有证明上述求积的连续余项，也没有把有限角点的 `q>v`、`D>0` 提升为全角证明。

## 3. 哪个实际入口失败了，为什么换输入

最初使用旧坐标 `.3735625`，即延长后物理坐标 `.38188815831468886`。这处旧半径背景的正坡尾部只是候选入口；原 `.05` 时钟与 rho 使它并非已有准确 flat 段。

32 阶新 Fourier 曲线、$v=.05$、1024 角点给出：

| 量 | 实际有限结果 |
|---|---:|
| 位置投影最大差 | .000110584 |
| 第二角导数投影最大差 | .184703 |
| $\min q$ | .1118583 |
| $\max|m/n|$ | 2753.75 |
| 入口最大主曲率 | 796462.25 |
| 首个抽样 ruling focus 距离 | $4.21525\cdot10^{-6}$ |

长度 .02、.05、.1、.2 均由真实 R137 消费器拒绝，未输出出口。这一输入没有可用的曲率或长度。一次 96 阶诊断在材料反函数的非原角点遇到 `D<=0`，自然 `exit 1`；不能将原均匀角点上偶然通过的短长度称作可用全角域。消费脚本随后保留这种反函数失败的记录，并尝试较短候选，而不是丢掉失败。

改用旧坐标 `.12`，即物理坐标 `.1200000418421323`，96 阶新曲线在原角点的位置差为 $4.04110\cdot10^{-8}$，第二角导数差为 .000441346。$v=.05$ 时，新的入口主曲率约 7.49908，长度 .05 的真实材料反函数和 Cartesian 出口成功；但是首个抽样 focus 只有 .0698423。把坡度降至 .01 后，focus 反而缩短到 .0461379，.1 以上长度全部失败。

这说明小坡度并不消除空间截面的扭率项。该截面的 z 振幅仅约 .000373，却足以使 $m/n$ 及其角导数控制长 coast。仅查看 $\min q$ 或旧场的主曲率不够。

## 4. 明确水平投影后，得到长度 .35 的实际两端口

现在采用同一 `.12` 实际截面的 96 阶水平投影，新高度为

$$
z_0=.11998895044131055,
\quad a\simeq1.0040052591923612,
\quad v=.003,
\quad L=.35.
$$

位置改变量的有限最大值为 .000200074432；不是零，也没有称为原解的同一条截面。新的完整入口与旧场差为：

| 端口量 | 最大向量差 |
|---|---:|
| X | .000200074432 |
| X_s | .08389715238 |
| X_u | .00200414519 |
| X_ss | 9.228253815 |
| X_su | .8069830746 |
| X_uu | .02278683643 |

2048 个全周期材料角的实际入口和段内端点原则给出：

| 量 | 实际有限结果 |
|---|---:|
| $\min |T_u|$ | .2050397068 |
| $\min n$ | .2041998852 |
| $\max |m|$ | .01849278742 |
| $\max |m/n|$ | .07759891104 |
| $\max |(m/n)_u|$ | 1.195538248 |
| 首个抽样 ruling focus 距离 | .8419064201 |
| 全段 $\min D$（这些角点） | .5866169890 |
| 出端 $\min U_t$ | .5836663481 |
| 全段 rank-one 最大主曲率（这些角点） | 7.499203402 |
| 出端自己法向的最大主曲率 | 7.469860937 |
| 出端完整相对度量误差 | $1.689\cdot10^{-15}$ 以下 |
| 全 ruling 包球半径 | 1.510661843 |
| 全 ruling 最大 $|y|$ | .4406956625 |
| 全 ruling 最大 $|z|$ | .4699889227 |
| 对 $(0,A_q,0)$ 的全 ruling 最小距离 | 1.007182244 |

其中半径、宽、高用 R137 的直线段凸函数端点原则；held 用每根真实 ruling 上二次距离的截断极小点，不是只检查两端。曲率用 $a n(1+k^2)/(a+wB)$ 的两端控制，且出端另外从 Cartesian 两jets计算自己的第一、第二基本形式。材料角反函数全 2048 点实际收敛后，才保存完整 `X,X_s,X_u,X_ss,X_su,X_uu` 出口。

同参数 L=.4 也通过有限消费，但出端高度 .519989 已高于该来源态的真实 cuff 高度 .510077，且小半轴处半径不足现 R210 喉部条件。因此本次选择 L=.35 作为后续连接输入，不能仅凭 L=.4 的局部度量和曲率就说它适用于原完整帽预算。

## 5. 如何返回非 flat 连接段

完整左、右端口分别是作为圆周函数的

$$
(P_-,V_-,A_-)=(X(0,u),X_\sigma(0,u),X_{\sigma\sigma}(0,u)),
$$

$$
(P_+,V_+,A_+)=(X(L,u),X_\sigma(L,u),X_{\sigma\sigma}(L,u)).
$$

它们的角导数来自同一个准确 master curve 和材料反函数；不得把 `P,V,A` 分别 Fourier 投影后仍声称是这条准确 coast 的出口。对于任一相邻非 flat 连接区间 $[s_0,s_1]$，必须在接点分别等于对应端口的 X、Xs、Xss；由圆周函数恒等同时保证 Xu、Xsu、Xuu。该连接区间的标量半径还须在 coast 端满足

$$
f=a\ \text{或}\ a+vL,\qquad f_s=v,\qquad f_{ss}=0.
$$

可消费的自由场定义是：取满足这六个向量圆周函数端值的 quintic Hermite 插值，再加一个在两端连同前两径向导数为零的周期向量场。每一候选都由完整位置求 E、F、G 和自己的曲率；不能沿用旧单位 T 提供器自动 G 正确的说法。也不能只用 R218 的两个法向矩来替代这些完整 Cartesian 端迹条件。此处给出了具体端口，尚未求出相邻连接区间的准确解。

## 6. 实际进程、复生参数与数据纪律

最终 L=.35 消费调用自然 `exit 0`，实际 wall time 约 4.63 秒；此前 v=.05、v=.01 和水平投影候选分别记录，未把拒绝态算成已接受场。

复生先按固定峰行 note 冷重生第三态，再运行：

```bash
node --max-old-space-size=128 \
  topics/visible-flexible-closed-surface/scripts/6a65-geometry-r137-inlet-samples.cjs \
  topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json \
  "$PEAK_THIRD_STATE" "$SCRATCH_INLET_JSON" .12 512

python topics/visible-flexible-closed-surface/scripts/6a65-geometry-r137-exact-inlet-consumer.py \
  "$SCRATCH_INLET_JSON" "$FRESH_SCRATCH_OUTPUT_PREFIX" \
  --degree 96 --planar --v .003 --angles 2048 --lengths .35
```

原始数组只保留在 scratch；按根 README §15，不上传 npz、完整位置样本或可复生报告。最终采样 JSON 的 SHA-256 为 `f769f83810594260caf12fd3f9cf061d3eaf6e53b49a75ccd0503010dc891286`；消费脚本本轮 SHA 为 `eaaa4ebe16aaea435b6fab6299018753d43ef91bbc28779e7375810e7dd252cd`。最终短报告、入口、出口的 SHA 分别为：

```text
8bf4ace9558a2921242b157afea6ae815e50a057dd6109b57c35fbe8ae7afc90
f99b6a27e696ec422a4e58b784ba1ace56802cfa22b32a57d959d3e05b7cd5df
e6bd8370ca2dc126410a75073c3f466398579bb13ea18cfb7c0958739e6da8e3
```

结论身份保持清楚：已经提供新输入下真实可消费的长准确形式局部段及完整两端口；全角连续域证书、弧长求积余项、相邻非 flat 区间、固定端完整族和全曲面非局部 reach 仍未支付。这些缺项不是本课题完成标准的豁免。
