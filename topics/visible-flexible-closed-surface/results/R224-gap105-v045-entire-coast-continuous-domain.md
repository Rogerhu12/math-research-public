# R224 — gap 1.05 / slope .045 新输入的整条 Γ95 coast 连续域证明

2026-11-26，Astra-visible-flex-6a65e705-20261126。

本条消费[新 gap 1.05 的实际 Cauchy 前缀](../notes/2026-11-26-6a65-geometry-coupled-gap-prefix.md)所产生的完整 Fourier 曲线，证明其准确 R137 延拓在**整个材料圆周及整个长度 $1/50$**上存在，且非零主曲率严格小于 $8.893$。这是新曲线的独立整数计算，不继承 R221 对另一条 M12 曲线的连续证书。

## 1. 准确曲线与固定度量

令 $a_0=P(7/5,1/2)/(2\pi)$，其中 $P$ 为椭圆周长；新中央椭圆由

$$
P(A,B)=P(7/5,1/2),\qquad A-B=21/20
$$

唯一确定。取 ramp 长度 $3/50$、物理斜率 $v=9/200$，并令

$$
f_0=a_0+\frac12\frac9{200}\frac3{50},\qquad
L=1/50,\qquad g=d\sigma^2+(f_0+v\sigma)^2du^2.
$$

这里的 $a_0$ 使用 R222 正系数周长级数的严格有理上下界；有限求积数或包含区间中点都不重新定义 $g$。

本次输入是前缀运行输出的 `coast-master.npz`，SHA256 为
`f2c834f5b2b9d1471eabb64a3be0edcc7b6f8454f8c98d68793a60c782c46b4d`。
取其全部 $-95\le k\le95$ 的三个 Cartesian 复系数 $c_k$，以每个保存的 binary64 实部、虚部所对应的**准确有理数**定义

$$
\gamma(\theta)=\operatorname{Re}\sum_{k=-95}^{95}c_ke^{ik\theta}.
$$

转换成实 Fourier 系数时，准确使用

$$
a_0^{\rm curve}=\operatorname{Re}c_0,\qquad
 a_k=\operatorname{Re}c_k+\operatorname{Re}c_{-k},\qquad
 b_k=\operatorname{Im}c_{-k}-\operatorname{Im}c_k.
$$

上述加减在有理数中完成，不先浮点对称化。本次共轭缺陷恰为零，但正确性也不依赖先假设它为零。
为避免混淆，以下把曲线常数项写为 $C=a_0^{\rm curve}$，度量常数仍为 $a_0$。

定义准确周长半径、材料角及规范化曲线

$$
a_\gamma=\frac1{2\pi}\int_0^{2\pi}|\gamma'(\theta)|\,d\theta,
\quad t(\theta)=\frac1{a_\gamma}\int_0^\theta|\gamma'(q)|\,dq,
\quad \widehat\gamma(t)=C+\frac{f_0}{a_\gamma}\bigl(\gamma(\theta(t))-C\bigr).
$$

下节证明 $|\gamma'|>0$，所以 $t$ 是整个圆周的光滑升映射，且 $|\widehat\gamma_t|=f_0$。
本条证明的对象是上述准确函数，不把数值反参节点当作定义。

## 2. 整段延拓及其充分条件

由 $T=\widehat\gamma_t/f_0$，记 $b=|T_t|$，并取原曲线的 Frenet 标架 $(T,N_F,B_F)$。
令

$$
c=(1-v^2/b^2)^{1/2},\quad
 d=-\frac vbN_F+cB_F,\quad
 N=d\times T=cN_F+\frac vbB_F,
\quad n=\frac{bc}{f_0},\quad m=\frac{d_t\cdot N}{f_0},\quad k=\frac mn.
$$

证书同时证明 $b>v$、$n>0$；因此这些完整角函数全部有定义。
沿用 [R137](R137-flat-coast-ruling-two-jets-and-actual-inlet-consumer.md) 已证明的准确母线公式，设

$$
r_0=f_0/v,\quad \Delta=\sigma(2r_0+\sigma),\qquad
w=\frac{\Delta}{r_0+\sqrt{r_0^2+(1+k^2)\Delta}},\quad
0\le w\le\sigma\le L,
$$

$$
B=v(1+k^2)-k_t,\quad D=f_0+wB,\quad
U=t-v^{-1}\operatorname{atan2}(kw,r_0+w),\quad
Y(\sigma,U)=\widehat\gamma(t)+w(d-kT).
$$

准确恒等式给出

$$
U_t=\frac{D}{f_0+vw(1+k^2)},\qquad
Y^*e=d\sigma^2+(f_0+v\sigma)^2dU^2,\qquad
\Lambda=\frac{f_0n(1+k^2)}D.
$$

另一个主曲率为零。因为 $r_0+w>0$，反正切在本域不越分支；所有入口量为 $2\pi$ 周期，故
$U(t+2\pi)=U(t)+2\pi$。严格 $U_t>0$ 随即给出整个材料圆周的全局微分同胚，而非仅在采样点求逆。

## 3. 全角整数包含计算

采用已公开的 R220/R221 **96-bit dyadic 向外舍入**运算：有理系数、平方根、Machin 公式的 $\pi$、三角 Taylor 余项都以整数界控制。新适配器只改变曲线身份和准确物理参数，不修改这些算术或几何公式。

将 $[0,2\pi]$ 分成 2048 个闭块，中心 $\theta_j$、半宽 $h=\pi/2048$。对每一 Cartesian 分量及 $0\le r\le4$，使用

$$
\gamma^{(r)}(I_j)\subseteq\gamma^{(r)}(\theta_j)
 +[-h,h]\gamma^{(r+1)}(\theta_j)
 +[-1,1]\frac{h^2}{2}\sum_{k=1}^{95}k^{r+2}(|a_k|+|b_k|).
$$

中心导数也用严格三角包含区间。全部 2048 块第一层即通过；实际二分次数为零。每块再把**整个** $w\in[0,L]$ 带入上一节公式，所以既未遗漏角块，也未将径向有限点冒作整个区段。

严格周长积分单独包含。对 $J=|\gamma'|$ 有

$$
|J''|\le\frac{|\gamma''|^2}{\min J}+|\gamma'''|.
$$

整块盒给 $\min J>0.4037683$、$\|J''\|_\infty<6.672138$。2048-panel 复合中点公式的平均积分误差小于

$$
\|J''\|_\infty\frac{(\pi/2048)^2}{6}<2.616698\cdot10^{-6}.
$$

于是

$$
1.0054302213<a_\gamma<1.0054354548.
$$

这个较宽的严格周长区间足够支付本条几何结论；它**没有**把数值规范化与准确规范化之间的误差证明到 $10^{-6}$ 或 $10^{-12}$。

$f_0,v,L$ 的运算区间分别包含准确物理值及原有限 consumer 的 binary64 代表；因此以下几何界对两组值都成立，但两组值没有被声明为同一个准确度量。
每块按曲线四阶导数计算曲率、挠率及其所需导数，然后包含 $n,k,k_t,D,U_t,\Lambda$。由准确整数端点保守向外取整，得到统一严格界：

| 量 | 下界 | 上界 |
|---|---:|---:|
| $b=|T_t|$ | 0.20114 | 8.941285 |
| 入口 $n$ | 0.19498 | 8.892858 |
| $k$ | −0.718219 | 0.718219 |
| $k_t$ | −1.535859 | 1.721269 |
| $B$ | −1.676254 | 1.586187 |
| $D$ | **0.9719** | 1.037157 |
| $U_t$ | **0.9657** | 1.031553 |
| 非零主曲率 $\Lambda$ | **0.1949** | **8.893** |
| 外向 support $-Y\cdot N$ | 0.3609 | 1.454055 |

其中三个关键准确端点为

$$
D\ge\frac{38501233644689957656512606185}{39614081257132168796771975168},\qquad
U_t\ge\frac{76517809475366143011307186267}{79228162514264337593543950336},
$$

$$
\Lambda\le\frac{352282385462149201384982632253}{39614081257132168796771975168}
 <\frac{8893}{1000}<\frac{19}{2}.
$$

法向沿母线不变，且 $(d-kT)\cdot N=0$，故 support 包含界覆盖整个母线。以上证明整段浸入、准确目标 metric、材料角全局反解及局部曲率界；它不单独证明 annulus 的全局无自交或未来闭曲面的远点对 reach。

母线弧长小于 $0.024623873$。按 [R218](R218-flat-coast-green-operator-and-two-port-range.md) 的同一条件法向 Green 估计，可取

$$
C_0<0.001554826,\quad C_{\mathrm{ruling},1}<0.126286043,\quad
C_{\mathrm{ruling},2}<5.128602.
$$

这些常数仍只控制母线方向；完整端口矩、切向 holonomy、横向导数和全局边值条件均未因此消失。

## 4. 真实运行和可复现身份

新源码为 [`6a65-coupled-gap-coast-continuous-domain.py`](../scripts/6a65-coupled-gap-coast-continuous-domain.py)，SHA256
`05d2d26578a31cedfbc7e73fe11310d9d064c368807eb5c0afcd4a3cba836d2c`。
它复用三个已公开源文件，其 SHA256 依次为：

- `6a65-m12-ramp-coast-continuous-domain.py`：`e7e86b166472b4ef79fb408df028bb25f430c955e3d8a560ad184b225e132563`；
- `6a65-m12-r137-continuous-domain.py`：`6bc46eeeb91bb979c19c2167250ced2a8362ae92b8f8b53eacd8595408e2af57`；
- `6a65-geometry-central-gap-held-budget.py`：`001f8f4907a9ed165b9ac99ec35e0144999b3f73e3a5a32ede3f6916fb67aed9`。

先按[前缀记录](../notes/2026-11-26-6a65-geometry-coupled-gap-prefix.md)重生这条实际曲线与 prefix report，再执行：

```bash
python -u scripts/6a65-coupled-gap-coast-continuous-domain.py \
  --scripts-dir scripts \
  --prefix-report /tmp/gap105-v045-prefix01-report.json \
  --coast-master /tmp/gap105-v045-prefix01-coast-master.npz \
  --out /tmp/gap105-v045-coast-continuous01.json \
  --cells 2048 --max-depth 8 \
  --curvature-cap 19/2 --denominator-floor 9/10
```

此次真实进程从 2026-11-26 10:11:26.933236 UTC 到 10:11:42.950136 UTC，自然退出码 **0**，外部监控 16.016925676 秒，峰值 RSS 32744 KiB。程序报告内部用时 15.136191395 秒；报告中的 `OSExitCode:null` 明确由外部 receipt 补证，不伪装程序能观测自己的退出状态。

| 实际对象 | SHA256 |
|---|---|
| prefix report | `c574b9a3c0be2cd5cc6db432a8fbb527466a5689b0a09c7da9b5f886a02da437` |
| 本次完整 scalar report | `f0c4bdcaace27cbb5826d17ce57e8b68022d8eef39b796a5aa675d809d09fa53` |
| 实际 stdout | `30242b01457c537858c249402b88f383f64a1497fa3f03d27d61e4ea69514f77` |
| 外部 process receipt | `12f2efba9aa9e8f18fd9364e13dc749e7a58d1d683e58981359b377c19e34a2e` |
| 全部整数叶行流 | `c17ebf062cd83aa31925b809338f52f9d0edf1e50434d3af89cbd5c2c7b2fb55` |

原件只在临时计算目录；仓库保存源码、定义参数、哈希与本条完整论证，不发布可重算数组。

## 5. 接回完整问题

新前缀 ramp 仍只有实际有限观察（曲率峰约 $9.6363$），本条未给它连续 metric 或曲率证书。
前缀与真正后段、平领、帽和全时闭族仍须完成；R222 的 held 下界有固定旧位置假设，不会自动成为新移植后的实际 held。
下一消费是实际 Cauchy 全尾上的短窗口接合及全位置求解；每次换整条入口曲线应重新绑定并验证其 coast，不能继承本条证书给另一输入。
