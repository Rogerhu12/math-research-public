# R318：真实挠点范数函数、translated sigma 全归一与原非齐次中央行

日期：2026-11-13。**状态：以下四原轨道的实际 Miller 常数、范数常数准确为一的挠点函数、translated sigma 的完整归一公式，以及原非挠来源的完整除法多项式中央等式和 $p^{5k+1}$ 尾界均已证明。本文没有把非零形式变量处的 translated sigma 值宣布为代数，也没有由范数恒等式删掉原中央核。**

本篇将 R313 的挠点极限和 R317 的原非挠修正接到真正的全局有理函数。涉及的除法多项式恒等式在本文直接证明；Katagiri–Kobayashi 的相关公式在 §4 作准确规范对照。

全文使用原曲线 $E_b:y^2=x^3+b$、$b=17$ 和 $dz=dx/(2y)$。记
$$
\begin{aligned}
X&=x^3,\qquad C_3(X)=X^3-204bX^2-384b^2X+64b^3,\\
D(X)&=(X+4b)C_3(X),\\
B(X)&=(X+b)(7X^2-4bX+16b^2)/7,\\
g&=B(X)/D(X)=S/H,\qquad A_r=B(r)/D'(r).
\end{aligned}
$$
对每个 $D(r)=0$，取 $P_r=(a_r,y_r)$、$a_r^3=r$；它的三个 $\mu_3$ 共轭合成十二个正号原极 $P_a$，留数为 $\varrho_a=A_r/(6a_r^2y_r)$。正负两点合计二十四极，且
$g\,dz=\sum_a\varrho_a\xi_{P_a}$。这里 $H$ 是 R308 的真实参考 $H_3$，并非任意选取的 theta frame。

## 1. 实际 prime-to-$p$ 挠点函数及其整性

固定 R313 的一个素数 $p$，令
$$
N=p+1,\qquad \phi=[-p].
$$
对每个原极 $P_a$，记其唯一的 $N$ 挠点提升为 $T_a$。这些 $T_a$ 非零、不是二挠点，且在好约化整数模型中互异。以下先固定其中一个 $T$，其准确阶记为 $r\mid N$。

取标准 Miller 函数 $m_T$，使
$$
\operatorname{div}(m_T)=r(T)-r(O),
\qquad m_T=t^{-r}(1+\cdots),\quad t=-x/y.
$$
该函数可由原椭圆群的直线/竖线递推构造。定义
$$
\boxed{
f_T=\left(\frac{m_T}{m_{-T}}\right)^{N/r}.}                \tag{1}
$$
于是
$$
\operatorname{div}(f_T)=N(T)-N(-T),\qquad f_T(O)=1.
$$
这两个条件唯一确定 $f_T$，与 Miller 计算路径无关。

其整性也可以直接从实际递推证明。所有中间点是 prime-to-$p$ 挠点，好约化在该挠点群上单射。两个不同且不互为负点的中间点具有不同的约化横坐标，所以直线斜率的分母是单位。倍点若遇二挠点，准确改用竖线；否则 $2y$ 是单位。原直线、竖线的 Laurent 首项都是单位，故归一 $m_T$ 及 $m_{-T}$ 在 $O$ 具有整 Laurent 系数和单位首项。相除后
$$
\boxed{f_T\in1+t\mathcal O_p[[t]].}                       \tag{2}
$$
这一步支付实际原点归一，没有逐层挑选一个未记录的单位。

## 2. 全部 Miller 常数及准确范数

由 (1) 或唯一性，
$$
\boxed{f_T(-P)=f_T(P)^{-1}.}                             \tag{3}
$$
令
$$
c_T=-\frac{f_T'(O)}{2N}\in\overline{\mathbb Q}\cap\mathcal O_p.
$$
这里导数相对于原 $dz=dx/(2y)$；因 $t=z+\cdots$，与一次正式参数导数相同。

实际第三类恒等式为
$$
\boxed{\frac{df_T}{f_T}=N(\xi_T-2c_T\,dz),\qquad
\xi_T=\frac{2y(T)}{x-x(T)}\,dz.}                          \tag{4}
$$
证明中，左右具有同一极与同一留数，其差是一个全纯微分。在 $O$，
$\xi_T/dz=0$，所以定义中的 $-2Nc_T$ 准确确定该常数。

更具体地，若 $h_T$ 是 $D_z\log m_T$ 在 $O$ 的常数项，则
$$
\boxed{c_T=-h_T/r.}                                      \tag{5}
$$
Miller 递推给
$$
h_{m+n}=h_m+h_n+\operatorname{slope}([m]T,[n]T).
$$
在和为零的步骤，使用真正竖线，最后一项为零。因为
$\ell(z)=-z^{-3}(1+s z+\cdots)$ 而竖线从 $z^{-2}$ 开始，这个常数正是原直线斜率 $s$。所以 (5) 是完整、代数且整的有限算法。

现在 $[-p]T=T$，故
$\operatorname{div}(\operatorname{Norm}_\phi f_T)
=\operatorname{div}(f_T)$。商原本可能是一个常数，但在 $O$ 精确为
$$
\operatorname{Norm}_\phi f_T(O)
=\prod_{R\in E[p]}f_T(R)=1.
$$
这里 $E[p]$ 是奇数阶群，非零点成对 $R,-R$，每对由 (3) 相消，且 $f_T(O)=1$。所有点均避开 $T,-T$，因为 $(N,p)=1$。因此
$$
\boxed{\operatorname{Norm}_{[-p]}f_T=f_T.}                \tag{6}
$$
没有剩余 root-of-unity、Gaussian 或未定范数常数。

同样证明对任何奇数 $n$ 且 $nT=T$，
$$
\operatorname{Norm}_{[n]}f_T=f_T.                         \tag{7}
$$
沿兼容的原 $p$ 挠点塔 $[-p]Q_{m+1}=Q_m$，由 (2)、(6)，
$f_T(Q_m)$ 是实际 $p$ 进单位，完整纤维乘积准确满足
$$
\prod_{R\in E[p]}f_T(Q_{m+1}+R)=f_T(Q_m).
$$
这些是实际范数相容值。未因此把它们当作原固定模数的既有全局 Euler 类。

## 3. 四个原轨道、全部 CM 相位和挠点极限

对 $[\omega](x,y)=(\omega x,y)$，唯一的除子和原点归一给
$$
f_{\omega T}(\omega z)=f_T(z),\qquad
c_{\omega T}=\omega^{-1}c_T,\qquad c_{-T}=-c_T.            \tag{8}
$$
原留数则是 $\varrho_{\omega P}=\omega\varrho_P$。因此所有相位在原三点轨道内准确匹配，不能将新点的留数另行重定。

置
$$
c_\infty=2\sum_a\varrho_a c_{T_a}.
$$
由 (4)，R313 的真实极限微分准确为
$$
\boxed{
g_\infty\,dz
=\frac1N\sum_a\varrho_a\,d\log f_{T_a}+c_\infty\,dz.}       \tag{9}
$$
四轨道表达是
$$
\boxed{
c_\infty=\sum_{D(r)=0}
             \frac{A_r\,c_{T_r}}{a_r^2y_r}
=\frac1{168b}
 +\sum_{C_3(r)=0}\frac{A_r\,c_{T_r}}{a_r^2y_r}.}          \tag{10}
$$
最后一个固定常数已完整支付：当 $a^3=-4b$、$y^2=-3b$ 时，
三挠切线斜率为 $3a^2/(2y)$，所以 $c_T=-a^2/(2y)$；
合并三条原留数及正负点即为 $1/(168b)$。

(6) 对 $d\log$ 给真正的特征零固定式。因为全纯微分在
$[-p]_*$ 下乘 $-p$，
$$
\boxed{\phi_*(g_\infty dz)=
            g_\infty dz-Nc_\infty dz.}                  \tag{11}
$$
这与 R313 的全部同源迹规范一致。

仍用原 $H=H_3$，R312 的真实中央投影给
$$
\boxed{
L_\infty
=\frac1N\sum_a\varrho_a\,
 \mathcal L_H\left(H\,\frac{d\log f_{T_a}}{dz}\right).}    \tag{12}
$$
若写成未归一的导数，必须保留
$$
\mathcal L_H\left(H\,\frac{d\log f_T}{dz}\right)
=\mathcal J_{H(d\log f_T/dz)}'(0)+2Nc_T\,\mathcal J_H'(0).
                                                                    \tag{13}
$$
所以 (12) 确实杀掉 (9) 的全纯方向，但不允许在原始 $\mathcal J'$ 中漏掉其参考补偿。

在 $p=59$，实际 Miller 算法给如下完整数据，$\delta^2=-3$：

| 原 $r\bmod59$ | $50$ | $57$ | $32$ | $16$ |
|---|---:|---:|---:|---:|
| $c_{T_r}$ | $23\delta$ | $55$ | $26$ | $41\delta$ |
| $A_rc_{T_r}/(a_r^2y_r)$ | $32$ | $14$ | $51$ | $5$ |

于是 $c_\infty=43$，而 $-60c_\infty=16\pmod{59}$。
这独立对上 R313 的完整有理 Cartier 平方常数 $16$，不只是核对一个未知比例。

## 4. translated sigma 的准确规范与全值比

在复一致化中，把准周期映射 $\eta$ 线性延至 $\Lambda\otimes\mathbb Q$。若 $T$ 的一个提升为 $z_T$，定义
$$
\sigma_T(w)=e^{-\eta(z_T)(w+z_T/2)}\sigma(z_T+w).
$$
其原点归一
$$
s_T(w)=\frac{\sigma_T(w)}{\sigma_T(0)}
$$
与改变提升产生的常数相位无关。

这些 normalized germs 不需假设非零 $w$ 处的值代数。它们可完全代数地定义如下：
$$
Z_T(0)=c_T,\quad Z_T'(w)=-x(T+\exp_Ew),\quad
s_T(0)=1,\quad s_T'/s_T=Z_T.                              \tag{14}
$$
(4) 和 Weierstrass sigma 的准周期公式证明
$c_T=\zeta(z_T)-\eta(z_T)$，所以 (14) 是同一个 translated sigma 的原点归一，未另换 gauge。

也可直接看见全部常数。准周期与 Legendre 公式使
$$
\left(-\frac{\sigma(z-z_T)}{\sigma(z+z_T)}
                  e^{2\eta(z_T)z}\right)^N
$$
是椭圆函数，具有 (1) 的除子及原点值一，故它恰是 $f_T$。等价地，
$$
\boxed{f_T(z)=\left(\frac{s_T(-z)}{s_T(z)}\right)^N.}      \tag{15}
$$

原点附近的全部系数是代数的，因为
$$
\begin{aligned}
Z_T(w)&=c_T-\sum_{m\ge0}
          \frac{\partial_P^m x(T)}{(m+1)!}w^{m+1},\\
\log s_T(w)&=c_Tw-\sum_{m\ge0}
          \frac{\partial_P^m x(T)}{(m+2)!}w^{m+2}.
\end{aligned}                                                       \tag{16}
$$
所有点变量导数都是原曲线上的有理函数。对于 $w\in p\mathcal O_p$，
这些级数收敛，$\log s_T(w)\in p\mathcal O_p$，所以
$s_T(w)\in1+p\mathcal O_p$。这给单位与收敛范围；它不把该解析值声明为代数数。

令 $F_n$ 为 $\sigma(nz)/\sigma(z)^{n^2}$ 规范的除法函数。
本篇用的 $n$ 都为奇数，故其对数导数与原奇数除法多项式 $\psi_n$ 相同。
当 $nT=T$，有完整的全值比
$$
\boxed{
\frac{F_n(T+\exp_Ew)}{F_n(T)}
=\frac{s_T(nw)}{s_T(w)^{n^2}}.}                          \tag{17}
$$
证明时，$nz_T=z_T+\gamma$ 的准周期因子在分子除以 $F_n(T)$ 后准确消去；两个指数因子都是 $e^{n^2\eta(z_T)w}$，也准确相消。因此 (17) 保留了真实代数单位 $F_n(T)$，不需要将其任意设为一，也不需要默许一个缺失的符号。

求对数导数给
$$
\boxed{
\frac1n D_w\log F_n(T+\exp_Ew)
=Z_T(nw)-nZ_T(w).}                                      \tag{18}
$$
所有 $n=(-p)^k$ 都满足 $nT=T$，故 (17)–(18) 对每一层成立。

这与 Katagiri–Kobayashi《$p$-adic properties of division polynomials and algebraic sigma functions》
[arXiv:2609.07024v1](https://arxiv.org/abs/2609.07024)
的 Definition 3.1、Theorem 2.7、Lemma 3.7 相容。
其方程为 $y_{\rm std}^2=4x^3-g_2x-g_3$；本题准确取
$y_{\rm std}=2y$、$g_2=0$、$g_3=-4b$，所以它的参数
$-2x/y_{\rm std}$ 正是这里的 $-x/y$，微分也同为 $dz$。
在其更强的 $n\equiv1\pmod{2r^2}$ 条件下，相位已经为一；
本篇则通过保留实际 $F_n(T)$ 支付一般层的全部相位。
(14)–(18) 已由原曲线与 sigma 乘法直接证明，不以非零形式变量处的 sigma 值代数性作输入。

## 5. 原非挠点的完整除法多项式来源

现在回到所有十二个原 $P_a$ 和原留数 $\varrho_a$，不把它们换成 $T_a$。令
$$
n=(-p)^k,\qquad k\ge1,
$$
并定义真正的全局有理函数
$$
u_{n,a}(z)=\frac{\psi_n(z-P_a)}{\psi_n(z+P_a)}.
$$
因为 $n$ 是奇数，$\psi_n$ 为偶函数，故
$$
u_{n,a}(O)=1,\qquad u_{n,a}(-z)=u_{n,a}(z)^{-1}.          \tag{19}
$$
原三挠点的阶与 $n$ 互素，另外十八点非挠，所以这些原点值没有零除问题。

置
$$
R_n(z)=\sum_a\varrho_a\,D_z\log u_{n,a}(z),\qquad
A_n=-\frac2n\sum_a\varrho_a D_z\log\psi_n(P_a).
$$
$A_n$ 是 R313 的同一个完整迹常数：
$$
[n]_*\eta=(g_n+A_n)\,dz.
$$

由 $\sigma(nv)=\psi_n(v)\sigma(v)^{n^2}$，分别取
$v=z-P_a,z+P_a$，再作对数导数，得到
$$
n\,\xi_{nP_a}(nz)/dz
=n^2\,\xi_{P_a}(z)/dz
+D_z\log u_{n,a}(z)+2D_z\log\psi_n(P_a).
$$
因此完整原来源满足
$$
\boxed{
R_n(z)=n\,g_n(nz)-n^2g(z)+nA_n.}                         \tag{20}
$$
特别 $R_n(O)=nA_n$。这里同时保留原输入点、全部留数、真正的 $n^2$ 次幂和加法坐标 $nz$；不把 $g_n(nz)$ 改成 $g_n(z)$。

这些全局主函数本身还满足真实的范数一关系
$$
\boxed{\operatorname{Norm}_{[n]}u_{n,a}=1.}               \tag{21}
$$
其除子在推到 $[n]$ 后为零，所以范数为常数。在 $O$，奇数核的正负点由 (19) 成对相消，给常数一。于是 $[n]_*(R_n dz)=0$；将 (20) 的三个完整项推送也逐项相消。这个事实并不使原中央行杀掉 $R_n$。

若 $V_n(0)=0$、$V_n'=g_n$，积分 (20) 的唯一原点归一是
$$
\boxed{
\sum_a\varrho_a\log u_{n,a}(z)
=V_n(nz)-n^2V_0(z)+nA_nz.}                              \tag{22}
$$
(22) 保留整个 normalized logarithm，而不是只保留一个代数值的极限。

## 6. 完整原中央等式及快速误差

沿 R301、R308、R310–317 始终用同一个
$$
H,\quad \widehat H=e^{-\kappa z^d}H,\quad
\mathcal J_T(u)=\sum_{h\ge0}
[z^{dh}](e^{-\kappa z^d}T)\kappa^{-h}(u)_h.
$$
(20) 直接给整个原权变量中的等式
$$
\boxed{
\frac{\mathcal J_{HR_n}(u)-nA_n\mathcal J_H(u)}
     {n^2\mathcal J_H(u)}
=-\frac{\mathcal J_S(u)}{\mathcal J_H(u)}
 +\frac1n\frac{\mathcal J_{H g_n(nz)}(u)}{\mathcal J_H(u)}.}          \tag{23}
$$
所有 reference mass 已显示在分子中。求中央导数得到
$$
\boxed{
L_0=-\frac1{n^2}\mathcal L_H(HR_n)
       +\frac1n\mathcal L_H(Hg_n(nz)).}                  \tag{24}
$$
这不是将 $\mathcal J$ 与同源、缩放或 $d\log$ 交换；它是对完整来源恒等式逐项应用同一个原解析观察。

末项有统一而很强的界。R313 的 $g_n$ 在原整参数中属于
$t^6\mathcal O_p[[t^6]]$，且 $t/z$ 在原半径内为单位。
因此在 $R=p^{-1/(2p)}$ 上
$$
\|\widehat H(z)g_n(nz)\|_R\le p^{-6k}R^6.
$$
完整 Newton 界给
$$
\boxed{
\frac1n\frac{\mathcal J_{H g_n(nz)}}{\mathcal J_H}
\in p^{5k+1}\mathbb Z_p\langle u\rangle.}                 \tag{25}
$$
具体地，若 $b_h=[z^{dh}](\widehat H g_n(nz))$，则
$$
v_p(b_h\kappa^{-h})\ge
6k+\left\lceil\frac{6-dh}{2p}\right\rceil+h
\ge6k+1\qquad(h\ge1).
$$
常数项为零；$(u)_h$ 的系数整，完整级数的一致收敛由同一估计及阶乘界给出。除以 $n$ 后得到 (25)，而 $\mathcal J_H$ 是原已付单位。
特别
$$
\boxed{
L_0\equiv-\frac1{n^2}\mathcal L_H(HR_n)
                        \pmod{p^{5k+1}}.}               \tag{26}
$$
整个 Tate 代数同余 (25) 也保留全部高位，不只保一个数值系数。

对有理输入除以 $n^2$ 的局部整性可以从 (20) 直接看见：
$$
\frac{R_n-nA_n}{n^2}
=-g+\frac1n g_n(nz).
$$
因此本篇的非齐次项是真正的全局主函数对数导数，经准确常数减法和准确 $n^2$ 归一后，收敛到原 $-g$。这没有声称 $u_{n,a}$ 在全局函数域中存在一个 $n^2$ 次方根，也没有将局部整性换成原全局单位格的中心除法。

## 7. 所得接口及精确证书

R313 的挠点极限现在有 (9)、(12) 的真实范数固定 $d\log$ 来源。原非挠点与该极限之间则保有 (18)、(20)–(24) 的完整解析和除法多项式修正。两部分的常数、相位和尺度都已计算，不能把其中任何一个 algebraic sigma 值极限直接替代原中央斜率。

生产文件
[check-jzero-torsion-norm-and-full-division-log.py](../scripts/check-jzero-torsion-norm-and-full-division-log.py)
及其 JSON 有 **85 项精确检查全部 PASS**。证书直接核定原三挠 Miller 函数的微分、$1/(168b)$ 常数、全部非齐次系数，并用 R317 的原点标签重做四条真实 Miller 路径。其 $c_\infty=43$、迹常数 $16$ 与 R313 的完整 Cartier 证书独立相合。

要推进原主目标，仍需要从 (12) 或 (23) 的真正完整行取得跨素数非零，或将其接到一个已经证明原始性的算术输入。范数一、代数常数或局部整归一各自都没有完成这一步。

直接依赖：
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R310](R310-jzero-actual-rankzero-frame-third-kind-and-central-transpose.md)、
[R312](R312-original-central-projection-fixed-poles-and-complete-kernels.md)、
[R313](R313-jzero-frobenius-square-actual-trace-and-central-first-layer.md)、
[R315](R315-original-pole-kernel-first-polynomial-and-actual-trace-orbits.md)、
[R317](R317-four-original-cm-orbits-full-taylor-and-first-frobenius-defect.md)。

