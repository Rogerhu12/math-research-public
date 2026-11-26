# R233 — 准确 terminal primitive 与整个 16 格归一化 ramp

2026-11-26，Astra-visible-flex-6a65e705-20261126。

本条消费 R227/R228 的原场证书、[R231](R231-first15-full-frequency-normalization-primitive.md) 的前 15 格完整归一化证书以及 R232 的准确 coast 端口差。最后一格确实换成同一个准确 R137 端口的完整 $P,V,A$ 函数，并支付短 Hermite 格的全部 $1/L,1/L^2$ 放大。实际连续结果是：

$$
\|\widehat g-g_f\|_{g_f}
\le
\frac{6040313026775475727407}{9903520314283042199192993792}
<6.100\times10^{-7}<10^{-6}
$$

和

$$
\max|\widehat\kappa_i|
\le
\frac{781816760821481612350249209927}{79228162514264337593543950336}
<9.867915<1000/97
$$

在**整个 16 格准确归一化 ramp** 上成立。右端准确 $C^2$ 接到同一 Γ95 的准确 R137 coast；中央端准确 $C^2$ 接冻结椭圆柱。

这里的函数按准确积分和反参定义，与 R229/R231 一致，不把 literal 浮点求积 consumer 等同于该准确函数。度量误差小不等于准确等距；全后段、全闭 reach、强 held 和全时族仍未由本条支付。

## 1. 同一终点曲线的准确部分弧长

沿用 R232 的 Γ95、准确 $a_\Gamma=\operatorname{mean}|\Gamma'|$、冻结 dyadic 中央椭圆、准确 $a_\ell$，以及新的

$$
f_0=a_\ell+vr/2,\qquad p=f_0/a_\ell,\qquad
b=p\ell,\qquad q=|\Gamma'|,\qquad R=q^2-b^2.
$$

这里 $v,r$ 是保存的准确二进数，不把 R224 原窄目标盒静默搬来。准确端口的 $C_\Gamma$ 沿用 R232 的常数 Fourier 系数定义，正是 FixedRadiusCurve 的缩放中心；它与整段归一化采用的弧长中心 $C(s)$ 是不同对象。第 3 节的位置差按前者计算，第 7 节在 $\lambda=1,\lambda_s=\lambda_{ss}=0$ 时后者消去。R232 已直接验证这一准确 $f_0$ 的完整 coast；本条只收紧同一曲线的积分和材料角界，没有换曲线。

准确恒等式为

$$
q-b=\frac{R}{2b}+E_2,\qquad
E_2=-\frac{R^2}{2b(q+b)^2}\le0.
$$

若 $r_0,r_1$ 是完整 $R,R'$ 的 Fourier 绝对和界，$q\ge q_*$、$b\ge b_*$，并有 $|b'|\le B_1$、$|q'|\le Q_1$，则

$$
|E_2|\le \epsilon_0=
\frac{r_0^2}{2b_*(q_*+b_*)^2},
$$

$$
|E_2'|\le \epsilon_1=
\frac{r_0r_1}{b_*(q_*+b_*)^2}
+r_0^2\left[
\frac{B_1}{2b_*^2(q_*+b_*)^2}
+\frac{Q_1+B_1}{b_*(q_*+b_*)^3}
\right].
$$

本次实际界分别小于 $7.695\cdot10^{-26}$ 和 $1.161\cdot10^{-23}$。

取 $S=R/\ell$、$h=\ell/a_\ell$，并令 $S_0$ 为准确 Fourier 常数项。有

$$
a_\Gamma-f_0=\frac{S_0}{2p}+\operatorname{mean}E_2.
$$

另一方面，

$$
D:=q-\frac{a_\Gamma}{a_\ell}\ell
=\frac{S-hS_0}{2p}
+E_2-h\,\operatorname{mean}E_2
$$

的准确圆周均值是零。因此它的部分积分必须在扣除 $hS_0$ 后估计，不能以原速度误差绝对和粗乘整个圆周。

## 2. 全频卷积、解析尾和有符号均值

源码先对完整 Γ95 作准确整数卷积，得到 Fourier 次数 190 的 $R$，目标 $p$ 的准确参数盒及 $2^{-200}$ 舍入误差均另行加入。然后消费 R231 同一椭圆因式展开，保留两条单边展开到 64 项，并保留其完整解析尾。乘上 $\ell^{-1}$ 后，全部 Fourier 次数为 318。

设有限近似为 $S^\flat$、$h^\flat$，且 $h^\flat_0=1$ 准确成立。构造

$$
T^\flat=S^\flat-h^\flat S^\flat_0,\qquad T^\flat_0=0.
$$

所有这些运算在共同 dyadic 分母下作准确整数卷积；常数项为零在整数层面检查。这里对 $S^\flat_0$ 保留**有符号区间**，而非先取绝对值。

为同时控制 $D'$，解析尾还保留一次 Fourier 权。若单边系数首遗漏项为 $c_{M+1}$，项比不超过 $\zeta<1$，则

$$
T_0\le\frac{|c_{M+1}|}{1-\zeta},\qquad
T_1\le |c_{M+1}|
\left[\frac{M+1}{1-\zeta}+\frac{\zeta}{(1-\zeta)^2}\right].
$$

有限绝对和与一次矩为 $S_0,S_1$ 时，双边乘积的 native 角导数遗漏 Wiener 范数不超过

$$
4(S_1T_0+S_0T_1+T_0T_1).
$$

因子 4 同时支付 $z=e^{2i\theta}$ 的频率 2 和两侧乘积。有限系数舍入及准确 $a_\ell$ 除法误差按相同 Fourier 权加入。这样得到完整 $S,S'$、$h,h'$ 误差，继而完整 $T,T'$ 误差。源码没有省掉 $|k|$ 加权高频尾。

准确 primitive 按

$$
\left|\int_0^\theta \frac{T}{2p}\,d\tau\right|
\le
\frac1{p_-}\sum_{k\ne0}\frac{|T_k|}{|k|}
$$

包含；有限系数误差也用相同零均值原理加入。剩余 $E_2-h\operatorname{mean}E_2$ 准确去均值，因此其部分积分不超过 $\pi(1+\|h\|_\infty)\epsilon_0$。$D,D'$ 的绝对上界还分别支付 $(1+\|h\|_\infty)\epsilon_0$ 和 $\epsilon_1+\|h'\|_\infty\epsilon_0$。

实际有符号平均值结果为

$$
\frac{488326979337}{19807040628566084398385987584}
\le a_\Gamma-f_0\le
\frac{1953308002951}{79228162514264337593543950336}.
$$

它约为 $2.4654213\cdot10^{-17}$，不是假定为零。准确周长半径进一步包含于

$$
\frac{79658596287942949300723383869}{79228162514264337593543950336}
\le a_\Gamma\le
\frac{79658596287942949300734806063}{79228162514264337593543950336}.
$$

这个盒由上述同一 Γ95 的完整 Fourier 残差恒等式得到，并与 R225/R232 的已证盒相交；没有重新做浮点积分。其宽小于 $1.443\cdot10^{-22}$。

准确部分弧长 primitive 不超过

$$
\frac{343684470731721}{79228162514264337593543950336}
<4.338\cdot10^{-15}.
$$

将它和 $D,D'$ 带入 R232 的完整反参链式法则，得到

$$
|\eta-\theta|<1.075\cdot10^{-14},\quad
|\eta'-1|<3.261\cdot10^{-13},\quad
|\eta''|<2.200\cdot10^{-11}.
$$

统一比例 $f_0/a_\Gamma$ 偏离 1 小于 $2.453\cdot10^{-17}$。

## 3. 真正中央角中的完整端口界

R232 的全 2048 角块已经给出准确 $V,A$ 与旧端迹的同角差及准确端口导数界。本条复用这些同对象的已证上界，只消费新的准确反参和比例包含；没有重跑角块、没有把另一组样本当端口。

下表是新完整有理上界再向外取短小十进数。列 $j=0,1,2$ 表示中央 native $\theta$ 导数阶。

| 准确端口与旧端迹之差 | $j=0$ | $j=1$ | $j=2$ |
|---|---:|---:|---:|
| $\Delta P$ | $3.105\cdot10^{-14}$ | $3.286\cdot10^{-12}$ | $7.696\cdot10^{-10}$ |
| $\Delta V$ | $8.469\cdot10^{-12}$ | $6.336\cdot10^{-10}$ | $5.551\cdot10^{-8}$ |
| $\Delta A$ | $3.682\cdot10^{-10}$ | $5.039\cdot10^{-8}$ | $7.651\cdot10^{-6}$ |

这些界包括所有旧 $95<|k|\le384$ 项、Γ95 本身的完整系数、准确统一缩放、准确部分弧长以及一、二阶角逆项。

## 4. 完整最后一格及短格放大

令 $Y_{\rm p}$ 是保存末节点构造的完整 Fourier–quintic **证明用代理场**。实际场是

$$
Y=Y_{\rm p}
+H_0(t)\Delta P
+L H_1(t)\Delta V
+L^2H_2(t)\Delta A,\qquad 0\le t\le1,
$$

其中

$$
H_0=10t^3-15t^4+6t^5,\quad
H_1=-4t^3+7t^4-3t^5,\quad
H_2=\tfrac12t^3-t^4+\tfrac12t^5,
$$

$$
L=\frac{135107988821115}{36028797018963968}.
$$

这些函数左端完整两 jet 为零，右端分别只指定位置、径向速度、径向加速度。因此实际右端确实是同一准确 R137 $P,V,A$，没有把非多项式端口重新投影回有限 Fourier。

若 $d_{pj}$ 控制第 $p=0,1,2$ 类端口的第 $j$ 阶 native 角导数差，则

$$
|\partial_s^i\partial_\theta^j(Y-Y_{\rm p})|
\le
\sum_{p=0}^2 L^{p-i}
\|H_p^{(i)}\|_\infty\,d_{pj}
=:\Delta_{ij}.
$$

源码对每个 Hermite 多项式分成 64 个准确有理子区间，以径向 Bernstein 控制点严格给出 $\|H_p^{(i)}\|_\infty$。$i,j=0,1,2$ 全部计算；没有把 $L^{-1}$ 或 $L^{-2}$ 忽略。实际最相关的界为

$$
\Delta_{10}<2.409\cdot10^{-11},\quad
\Delta_{01}<3.768\cdot10^{-12},\quad
\Delta_{20}<2.203\cdot10^{-8},
$$

$$
\Delta_{11}<2.290\cdot10^{-9},\qquad
\Delta_{02}<8.126\cdot10^{-10},\qquad
\Delta_{21}<2.066\cdot10^{-6}.
$$

特别是最后一个高阶混合量仍进入归一化的 $q_{ss}$ 预算，并未因其比其他差大而丢弃。

## 5. 实际原场 Gram 和自身曲率

代理场的完整 Gram、全高频及目标参数误差按 R227 同一准确算法计算。若 $M_s,M_j$ 分别控制 $|(Y_{\rm p})_s|$、$|\partial_s^j(Y_{\rm p})_\theta|$，则实际 Gram 增量支付

$$
\delta E\le2M_s\Delta_{10}+\Delta_{10}^2,
$$

$$
\delta F\le M_s\Delta_{01}+M_0\Delta_{10}
+\Delta_{10}\Delta_{01},
$$

$$
\delta(\partial_s^rG)
\le\sum_{j=0}^r\binom rj
\left[
M_j\Delta_{r-j,1}
+\Delta_{j1}M_{r-j}
+\Delta_{j1}\Delta_{r-j,1}
\right],\quad r=0,1,2.
$$

真正 $Y_s,Y_\theta,Y_{ss},Y_{s\theta},Y_{\theta\theta}$ 的完整区间盒则在代理场对应盒上加各自 $\Delta_{ij}$。R228 的准确 Cartesian 法向量及正交形算子谱式直接消费这些**实际场**盒和实际 Gram，而不是借代理场或背景面的曲率。

64 个完整角块、整个径向格，0 次分裂，实际给出

$$
\|g_Y-g_*\|_{g_*}\le
\frac{204241161153124433551}{79228162514264337593543950336}
<2.578\cdot10^{-9},
$$

$$
\max|\kappa_i(Y)|\le
\frac{178852685212360836838041754241}{19807040628566084398385987584}
<9.029754.
$$

native 面积密度严格大于 $.4037024543$。所有这些结论都已经包括非多项式准确端口修正。

## 6. 非多项式修正后的完整归一化

还需支付准确 $s$ 依赖角逆；原场好并不足以省略这一步。

对代理场与实际场分别写 $G_{\rm p},G$、$q_{\rm p},q$、$a_{\rm p},a$，以及

$$
e_{\rm p}=(G_{{\rm p},s}-2\omega G_{\rm p})/(2q_{\rm p}),
\quad e=(G_s-2\omega G)/(2q),\quad
\omega=f_s/f.
$$

令 $\Delta G,\Delta G_s$ 为上一节完整扰动上界，且代理分子界为 $N_{\rm p}$。有

$$
|q-q_{\rm p}|\le\frac{\Delta G}{q_-+q_{{\rm p},-}}=:\delta_q,
$$

$$
|e-e_{\rm p}|
\le
\frac{\Delta G_s+2|\omega|\Delta G}{2q_-}
+\frac{N_{\rm p}\Delta G}
{2q_-q_{{\rm p},-}(q_-+q_{{\rm p},-})}
=:\delta_e.
$$

由 $|a-a_{\rm p}|\le\delta_q$，进一步有

$$
\left|\frac qa-\frac{q_{\rm p}}{a_{\rm p}}\right|
\le
\frac{\delta_q}{a_-}
\left(1+\frac{q_{\rm p}^+}{a_{{\rm p},-}}\right)=:\delta_h.
$$

代理场的完整 $m_{\rm p}=\operatorname{mean}e_{\rm p}$ 和 $W_{\rm p}=q_{\rm p}\theta_{{\rm p},s}$ 在本次直接按 R231 的**全频**算法求出，不借前 15 格的最大值。实际均值满足 $|m|\le|m_{\rm p}|+\delta_e$。两个准确角逆的被积函数均扣除各自 $q/a$ 加权均值，故差也准确去均值。由较短互补弧，

$$
|W|\le|W_{\rm p}|+\pi\left[
\left(1+\frac{q_{\rm p}^+}{a_{{\rm p},-}}\right)\delta_e
+\delta_h(|m_{\rm p}|+\delta_e)
\right].
$$

本次实际得到 $|W|<8.198\cdot10^{-8}$、$|m|<4.200\cdot10^{-8}$。它们分别进入 R229/R231 的完整角逆速度和 $\lambda_s,\lambda_{ss}$ 公式；$C_s,C_{ss}$、$G_{ss}$、曲率二阶扰动也全部保留。

最后一格准确归一化后的结果是本条开头的最大度量有理数，以及

$$
\max|\widehat\kappa_i|_{\rm last}
\le
\frac{178879286388696787020600620519}{19807040628566084398385987584}
<9.031097.
$$

与 R231 的前 15 格合并，即得整个 16 格的连续结论。

## 7. 两端准确 $C^2$ 接合

左端继承 R227 的准确中央柱端口；准确 $f$ 在这里一、二阶导数为零。归一化的比例和角逆在此处的径向一、二阶变化均消失，故保留中央柱完整两 jet。

右端实际 Hermite 场按函数匹配准确 coast 的全部 $P,V,A$，所以所有需要的角导数也匹配。准确 coast 的度量为 $ds^2+f(s)^2du^2$，且此处 $f_s=v,f_{ss}=0$。因此该端点上归一化半径满足 $a=f,a_s=f_s,a_{ss}=f_{ss}$，从而 $\lambda=1,\lambda_s=\lambda_{ss}=0$；准确角逆与中央材料角的径向一、二阶差也为零。中心平移项因此不会引入端迹差。归一化场确实准确 $C^2$ 接同一 coast，而不是只有位置集合相邻。

## 8. 完整源码和真实进程

新增两份源码，旧 R231/R232 源码未修改：

| 源码 | SHA256 |
|---|---|
| 6a65-geometry-final-ramp-port-primitive.py | 295c094ef25e7d300a8e10bf7a2041c9b6b4e5762f90e69a6eeeea93b015d520 |
| 6a65-geometry-final-ramp-cell-certificate.py | 98ea52e458557d686167f3fd4c6390a2adc032c82df3dafbc76de1eac98a719f |

terminal primitive 真实进程自然 exit **0**，2.472143025 s，RSS **31800 KiB**。完整最后格进程自然 exit **0**，24.252127614 s，RSS **82872 KiB**。两个程序输出中的退出字段仍留 null，由各自外部 process receipt 记录实际退出。

| 原件 | SHA256 |
|---|---|
| terminal primitive report | 23fd5b56609e5b35725758a5a822ce893e61c6b8204db7b3e29ef592ba221b0f |
| terminal primitive stdout | 912c57b3e79bff866e7150fe7542deb5c096a67b1fcb16d6ca71f2b175bb39a4 |
| terminal primitive process receipt | 02e9793ba05124badf449e1ddee4b3dc4f67dd6d3b84beacee5ba8459bf3ada0 |
| 完整最后格 report | 9e16f7da5211c425b1fb8d6414e521c99f57d40f7c5cdf8b465a55b974c1ad24 |
| 完整最后格 stdout | 6fb80e1bfaf8f2b4433dd55063665e4c60acdd8f16187c415a1587239c0eb111 |
| 完整最后格 process receipt | 88ca35b7b64992e8b471e72d8bed5d21d67ac7cba074bad26a5faf7a73d07ac5 |

两条进程绑定同一已公布 ramp master 0e2865ed7fd2fa5e1061718cc96b8be691f5f7d1a5b9460cf11d564d799f38e7，相关 report 继续绑定同一 coast master、R225/R231/R232 证书及源码身份。仓库不保存 raw 数组或运行报告。本条补齐完整准确归一化 ramp 和准确 coast 接合；下一步继续真正后段和完整闭核。

