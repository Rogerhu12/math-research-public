# R106 补充：完整约化根有限部的实际粗界

2026-11-13，constructive-route。

**已证明，25 个准确 BigInt 门已经实际执行通过。** 本篇补齐一个此前只有
条件接口的量：对同一准确 $p_5\pm10^{-9}$ 族，在完整原始标签带
$|\Im x|\le1/1024$，从任一真实根到旧固定 cut 的**约化密度**
有限部满足
$$
\left|\operatorname{FP}
 \frac12\int_0^{\rho_c}D_{\rm red}(\rho,\Theta)J\,d\rho\right|
<2\cdot10^{19}. \tag{106F.1}
$$
两个根各自适用这个绝对值界。它没有包含 R106 (106.27) 中的
$S$ 积分、普通 cut 通量和根端有限项，因而不是完整 $b$ 的界。

这个数很粗，**不能据此声称 R104 的有效 cutoff 已与当前六维低块接合**。
其用途是使根有限部成为已有真实、有限、全参数、非均值的量；
后续有效计算仍应保留实际有符号 Fourier 参考并支付小余项。
本篇的公式也给出直接的改进位置：把已付复根盘内的 $|q|,|k_*|$
重算为实际紧界，或直接保留该盘内的有限射线 Taylor 多项式，
即可使用同一证明放大复 $s$ 圆盘，不必重建有限部规范。

## 1. 完整原件与参数身份

本篇仅使用以下三个已发布的原件：

- notes/2026-11-13-R106-whole-parameter-root-density.json，
  SHA256 e465844f0880356afd80829a4fc782856db7fc61e513be2669d84a61e80f8a09；
- notes/2026-11-12-beta-step3-true-derivative-collar-h1e5-domain500.json，
  SHA256 b387ede87055d0a990cafca12002b8baead5a2415d2d4cef610dde99405efd08；
- scripts/fourfold_phase_beta_interval.py，
  SHA256 ff159224bc1870b7580ef6e5f0370a4fcc385ed556d947003a0bb1667e6f4b0f。

前两项分别已经给出当前整个 $p_5\pm10^{-9}$ 上
$$
|G_p|\le M_G^*<0.046635,\qquad
|G_p\circ\Theta\,J|<M_N:=491/10000
\tag{106F.2}
$$
和更大的整 $\Delta_5=p_3\pm10^{-5}$ 的真实完整几何复盘。
这里 $G=\rho^{5/2}D_{\rm red}$，是 R106 的原 height 约化密度，
不是 grounded 密度；整个真实平移核零阶和 $\ell$ 口径均保留。

共同复域为
$$
|\rho|\le R=1/2500,\qquad |\Im\theta|\le S=1/320.
$$
R106T 的实际根初值和导数在全部原始标签带上满足
$$
|\Im\Theta_0|\le s_\theta=\frac{8221101}{8000000000},\qquad
|J_0|\le J_*=\frac{8223669}{7812500}. \tag{106F.3}
$$
这里 $\Theta_0$ 是实际全前腿在对应真实根上的值。
它不必是恒等映射，其导数也没有被置为 $1$。

## 2. 从原无限 primitive 预算得到真实复域特征系数界

此节只用已完成 collar 报告中的 base_input_budget 及完整正实部下界，
没有拿新的八角点值外推到复域。报告实际向外端点给
$$
|a_{\rm circ}|<11/10,\qquad
|T_i|<73/10,\qquad |Z|<3/10
$$
于复径向盘半径大于 $1/400$、归一角带宽大于 $31/100$。
$t(p)$ 的整个真实参数区间已经包括在原字段中。

R33 的准确无限角原函数在旋转柱坐标中的第 $n=4k$ 模，
水平原函数算子的逐行绝对和为 $1/(|n|-1)$（$k\ne0$）；
竖向为 $1/|n|$，零模与 $Z$ 按原规范保留。
令 $\sigma=31/100$，则
$$
e^{-(\sigma-4S)}<3/4,
$$
因为准确有理数
$1+(\sigma-4S)+(\sigma-4S)^2/2>4/3$。
因此完整无限 Fourier 和而非有限截断给
$$
|F_i|
\le |a_{\rm circ}|\max_i|T_i|
 \left(1+2\sum_{k\ge1}\frac{e^{-k(\sigma-4S)}}{4k-1}\right)+|Z|
<25. \tag{106F.4}
$$
这里
$2\sum_{k\ge1}q^k/(4k-1)\le(2/3)q/(1-q)\le2$。
准确 $F_\theta=a_{\rm circ}T$ 同时给 $|(F_\theta)_i|<81/10$。

在径向外盘 $R_0=1/400$ 上应用 Cauchy，令
$d_r=R_0-R=21/10000$，即得每个分量
$$
|(F_r)_i|\le\frac{25}{d_r},\qquad
|(F_{r\theta})_i|\le\frac{81}{10d_r}. \tag{106F.5}
$$
这两个导数是物理导数；对旋转基的 $\theta$ 导数，
已经使用准确的 $F_\theta=a_{\rm circ}T$，没有漏掉基旋转。

仍记 $C=F_\theta\times F_r$，$G=C\cdot C$，
$a_0=-C\cdot F_{\theta\theta}/G$，
$b_0=C\cdot F_{r\theta}/G$。
原 whole-complex collar 门实际给
$$
\operatorname{Re}G>9/5,\qquad \operatorname{Re}a_0>1/5.
$$
故由三个分量、叉积的两项和 (106F.5)，
$$
|q|=\left|\frac{b_0}{a_0}\right|
\le\frac{6(25/d_r)(81/10)(81/(10d_r))}
 {(9/5)(1/5)}
=\frac{303750000000}{49}<7\cdot10^9. \tag{106F.6}
$$
径向换向只改变 $q$ 的符号，不改变此界。

原报告还给真实曲率消根因子
$\kappa_K(\rho)= -K_0(t-\rho)/\rho$ 的正实部，
且 $|\kappa_K|<81$；这里对复数用已付正实部上界加虚部模上界，
并未把复数误作实数。
因此
$$
k_*=\frac{\sqrt{\kappa_K}}{a_0},\qquad |k_*|<50. \tag{106F.7}
$$
平方根在已付右半平面取与真实负区相同的分支。
$\kappa_K$ 是目标曲率因子；$k_*$ 是特征速度中实际消去 height
后的同一个因子，未把 R106 的散度根因子直接换成 $\kappa_K$。

## 3. 一个实际支付的复平方根时间盘

沿指向负区的径向坐标 $\rho=s^2$，
$$
\Theta_s=2s\,q(s^2,\Theta)-2\sigma s^2k_*(s^2,\Theta). \tag{106F.8}
$$
取
$$
R_s=\frac1{2500000},\qquad
a_s=R_s/2=\frac1{5000000},\qquad S_i=\frac1{450}.
$$
对任意复 $s$，按 $z\in[0,1]$ 积分到 $zs$。
(106F.6)–(106F.7) 的先验位移为
$$
\mathcal D=(7\cdot10^9)R_s^2+\frac23\,50R_s^3
<0.0011200000000000021334. \tag{106F.9}
$$
准确门给 $s_\theta+\mathcal D<S_i<S$，$R_s^2<R$。
因此逐段 Picard 延拓始终留在该真实解析域内，
并对复参数 $s$ 全纯；不需要把全部实时间流免费延伸到一个未知复时间盘。
连续族中的每个根初值均使用 (106F.3)。

对物理角导数在余量 $S-S_i$ 使用 Cauchy：
$$
\int_0^1|s\,\partial_\theta v(zs,\Theta)|\,dz
\le\frac{\mathcal D}{S-S_i}
<1.2406153846153869784616<4/3.
$$
故真实雅可比满足
$$
|J(s)|\le J_*e^{4/3}<4J_* . \tag{106F.10}
$$
$e^{4/3}<4$ 在程序中用20阶准确正项 Taylor 和几何余项实际核验，
不是浮点近似。定义完整非均值分子
$$
N(s,x)=G_p(s^2,\Theta(s,x))J(s,x).
$$
则在此复 $s$ 盘上
$$
|N|<4M_N. \tag{106F.11}
$$
而从 $a_s$ 到原固定 cut 的整个实区间上，仍有已付的更紧界 $|N|<M_N$。

## 4. 消奇、有限部和准确费用

R106 (106.26) 对原 $D_{\rm red}$ 已证明
$$
N(s)=N_0+N_2s^2+O(s^4),\qquad N_1=N_3=0. \tag{106F.12}
$$
为明确本篇的任意根初始标签也适用，$N_3$ 在该标签下是
$-\frac{2\sigma}{3}J_0\partial_\theta(k_{*0}G_0)$。
原密度准确给 $k_{*0}G_0=-1/16$，故该项仍严格为零；
$J_0$ 不必为 $1$。这就是没有额外对数减项的原因。

令 $s_c=\sqrt{t(p)-r_c}$。原准确 root/cut 区间已给 $s_c>a_s$。
有限部可以在任意这样的中点准确拆成
$$
\begin{aligned}
\operatorname{FP}\int_0^{s_c}\frac{N(s)}{s^4}\,ds
={}&\int_0^{a_s}\frac{N-N_0-N_2s^2}{s^4}\,ds
+\int_{a_s}^{s_c}\frac{N}{s^4}\,ds\\
&-\frac{N_0}{3a_s^3}-\frac{N_2}{a_s}.
\end{aligned} \tag{106F.13}
$$
该积分正是 (106F.1)：$\tfrac12\,d\rho=s\,ds$，
没有从物理角或 endpoint 约定额外借四倍因子。

由 (106F.11) 的圆盘 Cauchy 系数界，
$$
|N_0|\le4M_N,\qquad |N_2|\le4M_N/R_s^2,
$$
$$
\left|\int_0^{a_s}\frac{N-N_0-N_2s^2}{s^4}\,ds\right|
\le\frac{4M_N}{R_s^3}
 \sum_{j\ge1}\frac{(a_s/R_s)^j}{j}
=\frac{4M_N\log2}{R_s^3}
<\frac{4M_N}{R_s^3}.
$$
另一个真实积分的完整费用为 $M_N/(3a_s^3)$。
由于 $R_s=2a_s$，四项之和恰可取
$$
\frac{19}{6}\frac{M_N}{a_s^3}
=\frac{58306250000000000000}{3}
<2\cdot10^{19}, \tag{106F.14}
$$
从而证明 (106F.1)。所有无穷 Taylor 项及外侧实积分均已计入。

## 5. 执行、可用性与后续实际输入

程序 scripts/fourfold_subprincipal_root_finite_part_exact.mjs
逐原 SHA 读取 §1 三项输入，执行25个准确门；
实际报告为 notes/2026-11-13-R106-coarse-root-finite-part.json。
V8 运行的纯实现与 Node 包装中的函数逐字相同，原生恢复后入口为

~~~sh
node scripts/fourfold_subprincipal_root_finite_part_exact.mjs \
  . notes/2026-11-13-R106-coarse-root-finite-part.json
~~~

粗常数的主要来源已经完全定位：把整个径向外盘的 Fourier majorant
用于 $F_r,F_{r\theta}$，把 $|q|$ 放大到了 $7\cdot10^9$，
使复 $s$ 盘仅有 $4\cdot10^{-7}$。它不是实际 $q$ 如此大的证据。
更紧的同盘 $q,k_*$ 模数可以代入 (106F.9)–(106F.14)，但必须来自
同一连续复盘，不能把刚跑过的根点或根角 strip 值外推到整个径向盘。

本界若进一步转成 Sobolev/Fourier 乘子界仍会非常大；
它没有给出当前六维低块所需的有效高频阈值，也未支付 R104 的强
$4/3$ 余项。下一有用计算是有符号、完整 Fourier 非均值参考及小的全尾费用，
不是把这个粗上界当作已经通过的有限低高接线。
