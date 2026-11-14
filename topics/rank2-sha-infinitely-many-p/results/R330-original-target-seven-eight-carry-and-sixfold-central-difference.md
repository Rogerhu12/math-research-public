# R330：原目标七／八输入的真实 carry、六重中央差分与固定负矩首项

日期：2026-11-13。**状态：以下同一个原目标 $S$ 的两套完整输入核、准确二变一合并边界、全部 tame 输出 carry、无损中央返回、六重差分、所有输入环带及完整负权深区展开和尾界均已证明。固定负矩的非零未作为已知输入，本文不由一个非零来源或单位第一矩宣布主目标完成。**

沿 R297、R300、R316，固定
$$
E_b:y^2=x^3+b,\quad b=17,\quad
\delta=\sqrt{-3},\quad
\gamma=(5+\delta)/2,\quad\bar\gamma=(5-\delta)/2.
$$
原微分为 $dz=dx/(2y)$，$\sigma=z+\cdots$、$\Theta=x\sigma^2$。
本篇均为普通 $p>7$、$p\equiv1\pmod3$；所有 $2,\delta,\gamma,\bar\gamma$ 在原普通嵌入中都是 $p$ 进单位。

## 1. 始终是原目标的两套完整输入

R297 的准确原来源为
$$
S=\frac1{28}\sigma(z)^2\sigma(2z)^2
\Theta(z)\Theta(2z)\sigma(\gamma z)\sigma(\bar\gamma z).
\tag{1}
$$
原 $\sigma(\delta z)=\delta\sigma(z)\Theta(z)$ 给等价的七输入式
$$
\boxed{
S=\frac{\sigma(z)\sigma(\delta z)\sigma(2z)^2
             \Theta(2z)\sigma(\gamma z)\sigma(\bar\gamma z)}
           {28\delta}.}
\tag{2}
$$
(2) 的六条 sigma 尺度为
$$
(a_1,\ldots,a_6)=(1,\delta,2,2,\gamma,\bar\gamma).
$$
它们满足
$$
\prod_i a_i=28\delta,\qquad
1+3+4+4+8+7+7=34.
\tag{3}
$$
所以首项仍为 $z^6$，theta 次数仍是原 $34$，没有改目标归一。

两个 CM7 方向的准确因子是
$$
\frac{\sigma(\gamma z)}{\sigma(z)^7}
=\gamma\left(X+\frac{-2+6\delta}{7}b\right),\qquad X=x^3,
$$
以及其共轭式。因此
$$
\boxed{
\frac{\sigma(\gamma z)\sigma(\bar\gamma z)}
     {\sigma(z)^{14}}
=7X^2-4bX+16b^2.}
\tag{4}
$$
连同原倍点式，(2) 准确返回
$$
S=\frac17\sigma^{34}x^2
 (X+b)(X-8b)(7X^2-4bX+16b^2).
$$
CM7 的两个方向及其实际首项相位在 (4) 中均已支付。

## 2. 完整原测度及全部 $p$-core

仍用同一个 $E_{17}$ 形式周期 $\Omega_p$。置
$$
\pi=\psi_{17}(\mathfrak p),\quad
\bar\pi=\psi_{17}(\bar{\mathfrak p}),\quad
\varepsilon=\psi_0(\mathfrak p)/\psi_{17}(\mathfrak p)\in\mu_6,
$$
$$
\varkappa=p/\bar\pi^2,\quad
\lambda_\sigma=\varepsilon^3/\bar\pi,\quad
\lambda_\Theta=\varepsilon/\bar\pi.
\tag{5}
$$
R316 已付
$$
\nu_\sigma|_{p\mathbf Z_p}
=\lambda_\sigma[\varkappa]_*\nu_\sigma,\qquad
\nu_\Theta|_{p\mathbf Z_p}
=\lambda_\Theta[\varkappa]_*\nu_\Theta.
\tag{6}
$$
这里原总质量为
$$
\nu_\sigma(\mathbf Z_p)=0,\qquad
\nu_\Theta(\mathbf Z_p)=1.
\tag{7}
$$

七输入的真正求和变量与乘积测度为
$$
y_7=\sum_{i=1}^6a_ix_i+2t,\qquad
\nu_7=\nu_\sigma^{\otimes6}\otimes\nu_\Theta,
$$
$$
\boxed{\nu_S=\frac1{28\delta}(y_7)_*\nu_7.}
\tag{8}
$$
八输入沿 (1)，保留两条尺度一的 sigma、一条尺度一的 $\Theta$，
两条尺度二的 sigma、$\Theta(2z)$、及两条 CM7 sigma。其线性和记为
$y_8$，其测度为 $\nu_8=\nu_\sigma^{\otimes6}\otimes\nu_\Theta^{\otimes2}$，
且
$$
\boxed{\nu_S=\frac1{28}(y_8)_*\nu_8.}
\tag{9}
$$
两式都是原加法卷积，不是七个或八个乘法 Mellin 值的积。

全部输入同时在 $p$ 内时，准确系数分别为
$$
\boxed{
\lambda_7=\lambda_\sigma^6\lambda_\Theta
=\frac{\varepsilon}{\bar\pi^7},\qquad
\lambda_8=\lambda_\sigma^6\lambda_\Theta^2
=\frac{\varepsilon^2}{\bar\pi^8}.}
\tag{10}
$$
另一方面，R300 对这个原目标给出完整
$$
\boxed{
T_p\nu_S=\nu_S,\qquad
\nu_S|_{p^n\mathbf Z_p}=\bar\pi^{-n}[\varkappa^n]_*\nu_S.}
\tag{11}
$$
原 $S(0)=0$ 与 (11) 使原 principal 单位质量准确为
$$
J_S(0):=\nu_S(\mathbf Z_p^\times)=0.
\tag{12}
$$

## 3. 两套真实输出 carry，含全部 tame 和质量

对 $r=7,8$，令 $\mathcal D_r$ 表示至少一个原输入为单位。
按 (8)、(9) 的各自常数，定义
$$
\mathfrak C_{r,n}
=\text{原常数}\cdot(y_r/p^n)_*
 \left(\mathbf1_{\mathcal D_r,\ v_p(y_r)=n}\nu_r\right).
\tag{13}
$$
它们都是单位群上的实际测度，$\mathfrak C_{r,0}=\nu_S^\times$。
对 $n\ge1$，取全部输出的第 $n$ 环带，再减所有输入都在 $p$ 内的部分，得到
$$
\boxed{
\mathfrak C_{7,n}
=(1-\varepsilon\bar\pi^{-6})\,
 \bar\pi^{-n}[\bar\pi^{-2n}]_*\nu_S^\times,}
\tag{14}
$$
$$
\boxed{
\mathfrak C_{8,n}
=(1-\varepsilon^2\bar\pi^{-7})\,
 \bar\pi^{-n}[\bar\pi^{-2n}]_*\nu_S^\times.}
\tag{15}
$$
第二项的 $\bar\pi$ 次数由原输入数和输出归一共同给出，不能互换。

令 $d=p-1$，对任意 tame 指数 $j$ 定义
$$
M_{S,j}(u)=\int_{\mathbf Z_p^\times}
   \tau(x)^j\langle x\rangle^{du}\,d\nu_S(x).
$$
写 $c_7=1-\varepsilon\bar\pi^{-6}$、
$c_8=1-\varepsilon^2\bar\pi^{-7}$。两套完整行都是
$$
\boxed{
M_{\mathfrak C_{r,n},j}(u)
=c_r\bar\pi^{-n}\tau(\bar\pi)^{-2nj}
       \langle\bar\pi\rangle^{-2ndu}M_{S,j}(u).}
\tag{16}
$$
一般 tame 的中央导数仍含
$$
M_{S,j}'(0)-2nd\log_p\bar\pi\,M_{S,j}(0).
\tag{17}
$$
只有对本题原 principal 行 $j=0$，(12) 才准确消掉第二项：
$$
\boxed{
M_{\mathfrak C_{r,n},0}'(0)
=c_r\bar\pi^{-n}J_S'(0).}
\tag{18}
$$
没有把其他 tame 的质量一起删去。原 $\mu_6$ 不变性还使
$M_{S,j}$ 在 $6\nmid j$ 时为零，但合法的其他 tame 仍保留在 (16)。

## 4. 二变一合并的真实边界与无损中央返回

这一步解释 (14)、(15) 的差究竟来自哪些原输入。

把 (1) 中一条尺度一的 sigma 和尺度一的 $\Theta$ 的变量记为 $a,b_0$。
原乘法式在测度中是
$$
\boxed{[\delta]_*\nu_\sigma
       =\delta(\nu_\sigma*\nu_\Theta).}
\tag{19}
$$
故七输入的合并变量是 $(a+b_0)/\delta$。在统一的八输入空间上，
$\mathcal D_7\subset\mathcal D_8$。差集准确为
$$
\mathcal B=\left\{
a,b_0\in\mathbf Z_p^\times,\quad a+b_0\in p\mathbf Z_p,\quad
\text{其余六个输入全部在 }p\mathbf Z_p
\right\}.
\tag{20}
$$
这里的“其余六个”是五条 sigma 和 $\Theta(2z)$。没有遗漏“两个单位相加后变成非单位”的区域。

置 $\nu_B=\nu_\sigma*\nu_\Theta=\delta^{-1}[\delta]_*\nu_\sigma$。
原二输入的 primitive 部分在 $p$ 内的准确分布为
$$
\begin{aligned}
\nu_B|_p
-(a+b_0)_*(\mathbf1_{a,b_0\in p}\nu_\sigma\otimes\nu_\Theta)
&=\lambda_\sigma(1-\lambda_\Theta)[\varkappa]_*\nu_B.
\end{aligned}
\tag{21}
$$
其余六输入再用 (6)，得到整个边界的未缩放输出测度
$$
\boxed{
\nu_{\mathcal B}
=\frac{\varepsilon}{\bar\pi^7}
       (1-\varepsilon/\bar\pi)[\varkappa]_*\nu_S.}
\tag{22}
$$
这是对实际区域 (20) 的计算，不是只相减两个形式公式。

于是对 $n\ge1$，
$$
\boxed{
\mathfrak C_{8,n}-\mathfrak C_{7,n}
=\frac{\varepsilon}{\bar\pi^{n+6}}
 (1-\varepsilon/\bar\pi)
       [\bar\pi^{-2n}]_*\nu_S^\times.}
\tag{23}
$$
R316 已证明 $1-\varepsilon/\bar\pi=1-\bar\pi_0^{-1}$ 对所有这些普通素数为单位。
所以 (23) 的整体系数是单位，(12) 又给
$$
\boxed{
(M_{\mathfrak C_{8,n},0}-M_{\mathfrak C_{7,n},0})'(0)
=\frac{\varepsilon}{\bar\pi^{n+6}}
 (1-\varepsilon/\bar\pi)\,J_S'(0).}
\tag{24}
$$
因此原中央非零与这个明确单位相消边界的中央非零等价，并且两者赋值完全相同。式 (24) 不以边界测度本身非零来代替它的中央导数非零。

## 5. 真正原目标的六重中央差分

令
$$
K_{j,u}(v)=\mathbf1_{v\in\mathbf Z_p^\times}
                     \tau(v)^j\langle v\rangle^{du}.
$$
六条 $\nu_\sigma$ 的总质量都为零，所以 (8) 准确改写为
$$
\boxed{
M_{S,j}(u)=\frac1{28\delta}
\int \Delta_{a_1x_1}\cdots\Delta_{a_6x_6}
             K_{j,u}(2t)\,
       d\nu_\sigma(x_1)\cdots d\nu_\sigma(x_6)d\nu_\Theta(t).}
\tag{25}
$$
这里
$$
\Delta_{h_1}\cdots\Delta_{h_6}K(v)
=\sum_{I\subset\{1,\ldots,6\}}(-1)^{6-|I|}
               K\left(v+\sum_{i\in I}h_i\right).
\tag{26}
$$
全部六十四个顶点各自带其真正的单位指示函数；不把跨单位边界的顶点抹去。

对原 principal 中央行，
$$
\boxed{
J_S'(0)=\frac d{28\delta}
\int\Delta_{a_1x_1}\cdots\Delta_{a_6x_6}
 \{\mathbf1_{2t\in\mathbf Z_p^\times}\log_p\langle2t\rangle\}
 \,d\nu_\sigma^{\otimes6}d\nu_\Theta.}
\tag{27}
$$
(27) 中差分作用于花括号内整个函数，包括其单位条件。
它是原目标的完整六重差分，没有换成伴随来源。

### 5.1 全部输入环带的整重构

保留 Theta 的质量一边界，令
$$
\eta_\Theta=\nu_\Theta^\times-(1-\lambda_\Theta)\delta_0,
\qquad \eta_\sigma=\nu_\sigma^\times.
$$
则
$$
\nu_\sigma=\sum_{n\ge0}\lambda_\sigma^n
                  [\varkappa^n]_*\eta_\sigma,\qquad
\nu_\Theta=\delta_0+\sum_{n\ge0}\lambda_\Theta^n
                  [\varkappa^n]_*\eta_\Theta.
\tag{28}
$$
这由有限望远镜和质量零余项证明。代入 (25) 后，Theta 的零点项仍然存在；
六条 sigma 均取实际环带。只有至少一个活动输入的深度为零的项可以贡献输出单位行。

在一个正深度输入上用质量零性作有限差分。其改变在 $p$ 内，不改变固定剩余类的单位条件；在单位圆盘上展开 (25)。与 R316 同样的阶乘估计给：总输入深度至少 $N$ 的尾，在同一 $u$ 单位闭盘内属于
$$
p^N\mathcal O\langle u\rangle.
\tag{29}
$$
$tame$ 因子在同一单位剩余圆盘内常值，故 (29) 同时适用于所有 $j$ 和中央导数。
这支付原六／七个质量零输入的完整尾，而不使用未经证明的测度可数可加性。

## 6. 六条 sigma 都在深区时的完整负权级数

固定 $n_i\ge1$，令
$$
N=\sum_{i=1}^6n_i,\qquad m=\min_i n_i.
$$
考虑原输入子区域
$$
x_i\in p^{n_i}\mathbf Z_p\quad(1\le i\le6),\qquad
t\in\mathbf Z_p^\times.
\tag{30}
$$
由于六条 sigma 都在 $p$ 内，输出为单位恰好等价于 Theta 输入为单位。
其整条行记为 $D_{\boldsymbol n,j}(u)$。

定义原完整矩
$$
\mu_{\sigma,r}=\int_{\mathbf Z_p}x^r\,d\nu_\sigma(x),\qquad
\mu_{\sigma,1}=\Omega_p,
$$
以及真实负矩行
$$
M_{\Theta,j,-R}(u)=
\int_{\mathbf Z_p^\times}
     \tau(t)^j t^{-R}\langle t\rangle^{du}\,d\nu_\Theta(t).
\tag{31}
$$
$\mu_{\sigma,r}=0$ 除非 $r\equiv1\pmod6$。用 (6) 后在单位 $2t$ 周围展开，
得到完整、统一收敛的式
$$
\boxed{\begin{aligned}
D_{\boldsymbol n,j}(u)
={}&\frac{\lambda_\sigma^N\tau(2)^j\langle2\rangle^{du}}
          {28\delta}\\
&\times\sum_{\substack{r_i\ge1\\r_i\equiv1\ (6)}}
 \frac{(du)_R}{r_1!\cdots r_6!}\,
 2^{-R}M_{\Theta,j,-R}(u)
 \prod_{i=1}^6
  \left(a_i^{r_i}\varkappa^{n_ir_i}\mu_{\sigma,r_i}\right),
 \qquad R=\sum_i r_i .
\end{aligned}}
\tag{32}
$$
所有 $\gamma,\bar\gamma,\delta,2$ 均保在各自的 $a_i^{r_i}$ 中。
$M_{\Theta,j,-R}$ 是同一参考测度的准确 tame／负权行，不能用零权质量代替它。
因 $R$ 总为六的倍数，(32) 也与原 $\mu_6$ tame 条件相容。

### 6.1 固定负六次矩的准确首项与全部尾

(32) 最小的 $R$ 是六，只能由全部 $r_i=1$ 给出。
利用 (3) 的尺度乘积，
$$
\boxed{\begin{aligned}
D_{\boldsymbol n,j}(u)
={}&\frac{(\lambda_\sigma\varkappa)^N\Omega_p^6}{64}
 (du)_6\,\tau(2)^j\langle2\rangle^{du}
                         M_{\Theta,j,-6}(u)\\
&\pmod{p^{N+6m}\mathcal O\langle u\rangle}.
\end{aligned}}
\tag{33}
$$

完整尾界如下。写 $r_i=1+6k_i$、$K=\sum k_i$。每项的额外尺度赋值至少
$6\sum n_ik_i$；矩、负矩行和 $(du)_R$ 均整。又
$$
\sum_i v_p(r_i!)\le\frac{6K}{p-1}.
$$
当前普通素数至少为十三。当 $K=1$ 时所有阶乘均为单位；当 $K\ge2$，
上式不超过 $K-1$。所以全部 $K\ge1$ 项的赋值至少
$$
N+6mK-(K-1)\ge N+6m.
$$
该界随 $K$ 增长，证明整个 Tate 级数的收敛及 (33)，也允许求中央导数。

每个深区行在 $u=0$ 的质量为零。对 principal 行求导，
$(du)_6'(0)=-120d$，得到
$$
\boxed{
D_{\boldsymbol n,0}'(0)
=-\frac{15d}{8}
 \left(\frac{\varepsilon^3p}{\bar\pi^3}\right)^N
 \Omega_p^6 I_{-6}(\Theta)
 \pmod{p^{N+6m}\mathcal O},}
\tag{34}
$$
其中
$$
\boxed{I_{-6}(\Theta)=
 \int_{\mathbf Z_p^\times}t^{-6}\,d\nu_\Theta(t).}
\tag{35}
$$
这是一个固定负权的准确算术输入。若该矩为单位，(34) 就给该真实深区中央行的准确赋值 $N$；本文尚未把这种单位性当作已证。其他输入区域仍在 (25)、(28) 中，不能仅由一个深区非零删掉它们可能的贡献。

## 7. CM7 范数与相位在中央核中的准确位置

(4) 已付全部 CM7 除法相位，(3) 又使最小负矩项的尺度乘积准确约去原 $28\delta$。
完整 (32) 的高项却仍读各个相对尺度 $a_i^{r_i}$，不能只保留它们的总范数。

同样，在全核中把 $y_7$ 写成 $\gamma(y_7/\gamma)$，
原 principal 单位 Mellin 只多一个 $\langle\gamma\rangle^{du}$。
其中央导数多出的项是
$$
d\log_p\gamma\cdot J_S(0)=0.
\tag{36}
$$
所以 $\log_p\gamma+\log_p\bar\gamma=\log_p7$ 本身不产生一个独立的已知中央常数。
相对比例 $\gamma/\bar\gamma$ 仍在 $y_7/\gamma$ 的实际相加核和 (32) 内。
这一步准确保留了已知范数所能给出的信息，而没有将相加卷积拆成乘法 Mellin。

## 8. 证书与后继算术输入

[check-jzero-target-seven-eight-carry-and-sixfold-central.py](../scripts/check-jzero-target-seven-eight-carry-and-sixfold-central.py)
及其 JSON 的 **25 项精确检查全部 PASS**：它们核定两个 CM7 原方向、
原目标的七／八因子与次数、真实尺度首项、全部输入 core 相位、二变一边界系数、
六重差分的原低阶消去以及固定负矩首系数。证明 (14)–(35) 使用的是原测度恒等式和完整尾估计，不以有限素数样本代替。

本篇给出的实际非零接口是 (24) 和 (34)：前者无损地返回同一个原目标中央导数，
后者精确定位一个真实深区的固定负矩输入。要继续推进，需要控制 (35) 的真实算术值，
并在同一 (25) 中处理其余输入区域；不能由 norm-one、非零来源或某一局部深区的非零直接宣布无穷素数结论。

直接依赖：
[R295](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)、
[R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)、
[R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)、
[R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)、
[R319](R319-jzero-ramified-three-minimal-unit-and-mixed-scaled-return.md)、
[R323](R323-new-pure-five-factor-source-and-complete-central-kernels.md)。

