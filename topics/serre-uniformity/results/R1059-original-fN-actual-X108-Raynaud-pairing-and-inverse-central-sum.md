# R1059：原 f_N 的实际 X0(108) Raynaud 配对与逆中心有限和

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；o1_theta / root。

**已证明：R1049 的同一个固定 theta 输入，通过原 $X_0(108)$ 上实际函数、微分和 Cartier 配对，准确化成一个带全部原标量的有限和。** 本篇不以抽象 CM 同源、同表示或 bundle 配对的非退化性替代指定全局配对的非零。

## 1. 原 theta、固定 q 系数和结论

令
$$
p=6N+5,\quad n=(p-2)/3=2N+1,\quad
\zeta^2+\zeta+1=0,\quad s=\zeta-\zeta^2,\quad s^2=-3.
$$
固定模曲线上的公式适用于 $p\ge5$；接回原 $f_N$ 时保持 R1049 的 $p\ge41$ 范围。

R1049 的
$$
\Theta(q)=\sum_{\alpha\in\mathbf Z[\zeta],\ \alpha\equiv1\bmod3}
 \alpha q^{\operatorname{Norm}\alpha}
$$
准确是
$$
a(q)=f_{27}(q)=\eta(3\tau)^2\eta(9\tau)^2.
\tag{1059.1}
$$
核准方式如下。$\mu_6\to(\mathbf Z[\zeta]/3)^\times$ 是双射，每个素于三的理想有唯一 primary 生成元。$\psi((\alpha))=\alpha$ 是无穷型一、导子 $3\mathcal O$ 的 Hecke 角色；导子不能降到 $(s)$，因为 $\zeta\equiv1\bmod s$ 而单位条件不允许该无穷型杀掉 $\zeta$。其 theta 级数的权为二、level 为 $3\operatorname{Norm}(3\mathcal O)=27$，有限 character 与 $\chi_{-3}$ 相消，首项为 $q$。另一方面 eta 乘积的两个模二十四条件都等于 $24$，character 平凡，在各 cusp 的零阶为一；$X_0(27)$ 的 genus 为一，故此 cusp-form 空间一维，得到 (1059.1)。

只对所需单系数定义
$$
A_p=[q^p]a(q)E_\Theta(q^4),\qquad
E_\Theta(q)=\sum_{m\ge1}\frac{a_m}{m}q^m.
\tag{1059.2}
$$
它仅读 $m\le(p-1)/4<p$，所有分母都是单位；没有把整个 Eichler 级数未经处理地模 $p$ 化。R1049 §6 已给
$$
f_N=\frac{t^2\delta'_p}{4(p+1)}A_p,\qquad
t^3=4,\quad\delta'_p=\pm1.
\tag{1059.3}
$$
本文的新准确式是
$$
\boxed{\quad
A_p=(-1)^N3^{3N+1}
\sum_{i=0}^{2N+1}\frac{(-1)^i\binom{2N+1}{i}^2}{3i+1}.
\quad}
\tag{1059.4}
$$
所以在原范围，
$$
\boxed{\quad
f_N=\frac{t^2\delta'_p(-1)^N3^{3N+1}}{4(p+1)}S_n,
\qquad
S_n=\sum_{i=0}^{n}\frac{(-1)^i\binom ni^2}{3i+1}.
\quad}
\tag{1059.5}
$$
所有显示在 $S_n$ 外的因子均为原已知单位。$S_n$ 的全 $p$ 非零性仍须证明。

## 2. 实际 canonical 关系给原模函数

在原 $X_0(108)$ 上使用首项归一为 $q$ 的固定新形式，置
$$
b=4f_{27}(q^4),\quad c=f_{27}(q^2),\quad
g=f_{36}(q)=\eta(6\tau)^4,\quad d=f_{36}(q^3),\quad h=f_{108}(q).
$$
本篇 $b$ 只表示这条固定旧形式，与 R1052 的 CM 参数无关。
Harrison Definition 4.2 的准确基是
$$
e_5=a+b,\quad e_6=2c,\quad e_7=g+3d,\quad
e_8=h,\quad e_9=a-b,\quad e_{10}=g-3d.
$$

为逐项核准所需 canonical 关系，临时写
$A=e_1,B=e_2,C=e_3,D=e_4,u=e_5,v=e_6,w=e_7,H=e_8,k=e_9,l=e_{10}$。
Harrison 第12页二次关系给
$$
\begin{aligned}
q_1&=3u^2-Bw-k^2-Dl,\\
q_2&=Bu-2vw-Ak,\\
q_3&=Du-Ck+2vl,\\
q_4&=Aw+Cl-2uk,\\
q_5&=w^2-l^2-3v^2 .
\end{aligned}
$$
其中 $q_3$ 是原两条关系 $Du-AH+vl$ 与 $AH-Ck+vl$ 之和；其余是原关系或负号。直接展开，
$$
u q_1+w q_2+l q_3+k q_4+2v q_5
=3\{u(u^2-k^2)-2v^3\}=0.
$$
将原 $Bw-4H^2+2k^2+Dl=0$ 加到 $q_1=0$，另得
$4H^2=3u^2+k^2$。

Harrison Theorem 4.4 的实际 projective 自同构将
$$
(u,v,k)\longmapsto((\rho/s)w,(\rho^2/s)H,-\rho l),
\qquad \rho^3=2.
$$
把它代入已经得到的三次零式，乘 $s^3/\rho^3$，便得
$$
w^3+3wl^2-4H^3=0.
$$
这是确切坐标变换；其在微分上的共同负号不影响齐次零式。因此原形式满足
$$
h^2=a^2+ab+b^2,\qquad ab(a+b)=4c^3,\qquad h^3=g^3+27d^3.
\tag{1059.6}
$$
而 eta 乘积本身给 $c^2=gd$。

置原模函数
$$
x=c/g=\eta(18\tau)^2/\eta(6\tau)^2,\quad U=h/g,\quad
A_+=(a-\zeta b)/g,\quad A_-=(a-\zeta^2b)/g.
$$
于是
$$
U^3=1+27x^6,\quad A_+A_-=U^2,\quad A_+^3-A_-^3=-12sx^3.
$$
所以 $(A_+^3+A_-^3)^2=4(1-27x^6)^2$。在原 cusp $\infty$，两者首值均为一，准确选定和的正号，得到
$$
A_+^3=(1-3sx^3)^2,\qquad A_-^3=(1+3sx^3)^2.
$$
定义实际函数
$$
z=\frac{1-3sx^3}{A_+},\qquad w_0=\frac{1+3sx^3}{A_-}.
$$
它们准确满足
$$
\boxed{\quad
z^3=1-3sx^3,\quad w_0^3=1+3sx^3,\quad
z^2=A_+,\quad w_0^2=A_-,\quad zw_0=U.
\quad}
\tag{1059.7}
$$
最后一个式子的 $\mu_3$ 相位由 $\infty$ 的值 $z=w_0=U=1$ 固定，未另选一个抽象 Fermat 模型。

## 3. 实际平滑模型与原微分尺度

(1059.7) 的 projective closure 是 $\mathbf P^3$ 中的两个三次方程。对特征不为二、三的域，Jacobian 两行若线性相关，先由 $z,w_0$ 的偏导迫两者为零，再由两方程迫其余齐次坐标为零，矛盾。因此它平滑。两组 cubic branch 点不交，给独立的三次 Kummer 类，故曲线几何连通。adjunction 给 genus 十。

$x,z,w_0$ 是原 $X_0(108)$ 的实际函数，给非恒定映射到此 genus 十曲线；源的 genus 也为十，特征零 Riemann–Hurwitz 迫映射次数一。因此 (1059.7) 是原曲线的实际模型。两边在所有 $p>3$ 都有平滑 proper 模型；genus 至少二的 good 模型的 generic 同构唯一延拓，在此可于未分歧底读同一个同构。没有从任意同源模型猜测模 $p$ 的格指数。

记 $\Omega=g\,dq/q$。准确微分恒等式是
$$
\boxed{\qquad \Omega=\frac{dx}{z^2w_0^2}.\qquad}
\tag{1059.8}
$$
为保留标量，核其完整 divisor。右侧在九个 $x=\infty$ 点各有二阶零；在 $z=0$ 或 $w_0=0$，$dx$ 含相应二次因子，故没有其它零极。

另一方面，原 eta quotient 在 cusp $a/c$ 的阶数为
$$
\operatorname{ord}_{a/c}x=
\frac{108}{12c\gcd(c,108/c)}
\left(\frac{\gcd(c,18)^2}{18}
-\frac{\gcd(c,6)^2}{6}\right).
$$
当 $c\in\{1,2,3,4,6,12\}$ 时是 $-1$，各 cusp 重数总为
$1+1+2+1+2+2=9$；其余 $c\in\{9,18,27,36,54,108\}$ 时是 $+1$。内部没有零极。
$\Omega$ 是实际 $X_0(108)\to X_0(36)$ 的 elliptic 微分拉回；该映射在内部不分歧，在 cusp 的分歧指数是
$$
e=3\gcd(c^2,36)/\gcd(c^2,108).
$$
它在前九点恰为三、其它点为一。故 $\Omega$ 的 divisor 也恰是这九点各二阶。两微分之比为常数；原 $\infty$ 处
$x=q(1+O(q^6))$、$z,w_0=1+O(q^3)$、$\Omega=(1+O(q^6))dq$，
将常数严格固定为一。

因此实际微分为
$$
u=(a-\zeta b)\,dq/q=\frac{dx}{w_0^2},\qquad
\nu=(a-\zeta^2 b)\,dq/q=\frac{dx}{z^2},
$$
$$
\omega_h=h\,dq/q=\frac{dx}{zw_0}.
\tag{1059.9}
$$
这些身份保留实际 CM 子格和原 $q$ 尺度。两个原退化映射
$X_0(108)\to X_0(27)$ 各为六次，分别是 $q\mapsto q$ 与 $q\mapsto q^4$；
第二条微分中的因子四已经包含在 $b$ 中。它不等于映射次数。
(1059.7) 中两个 forgetful elliptic 映射则各为三次，二者也不混同。

## 4. Raynaud 配对及其完整半线性

若两条全局正则微分 $\omega,\nu$ 的 Cartier 值为零，取实际有理原函数
$dF_\omega=\omega$，定义
$$
\beta(\omega,\nu)=\mathscr C(F_\omega\nu).
\tag{1059.10}
$$
更换 primitive 时差为 $G^p$，增量为
$G\mathscr C(\nu)=0$，所以定义无歧义。局部原函数的全部负 Laurent 项因其微分正则而为 $p$ 倍指数，组成一个 $p$ 次幂，故该配对也是全局正则微分。由
$\mathscr C(d(F_\omega F_\nu))=0$，它交替，并满足
$$
\beta(\lambda\omega,\mu\nu)
=(\lambda\mu)^{1/p}\beta(\omega,\nu).
\tag{1059.11}
$$
这正是 Raynaud 的局部 exact differential bundle 配对。本篇直接核所需性质，并不从该 bundle 的完美性推出选定两条全局微分的值非零。

## 5. 在原曲线上直接构造 primitive 并计算

写 $\kappa=3s$。因为 $p-2=3n$，
$$
\nu=z^{-p}(1-\kappa x^3)^n dx,\qquad
u=w_0^{-p}(1+\kappa x^3)^n dx.
$$
取
$$
R_-(x)=\sum_{i=0}^{n}
 \binom ni(-\kappa)^i\frac{x^{3i+1}}{3i+1}.
$$
其次数 $p-1$，全部 $3i+1$ 位于 $1,\ldots,p-1$，所以
$R_-/z^p$ 是 $\nu$ 的实际有理 primitive，且在原 $\infty$（即 $x=0$）为零。正号同理给 $u$ 的 primitive。于是原 $\omega_a=a\,dq/q$ 和 $\omega_b=b\,dq/q$ 也有在此点正则、值零的实际 primitive。

Cartier 乘法性给
$$
\beta(\nu,u)=\frac1{zw_0}
 \mathscr C\left(R_-(x)(1+\kappa x^3)^n dx\right).
$$
括号的多项式次数为 $2p-3$，故 Cartier 只读取 $x^{p-1}$ 一项，下一可能次数 $2p-1$ 尚未进入。其系数准确为
$$
c_p=\kappa^n
\sum_{i=0}^n\frac{(-1)^i\binom ni^2}{3i+1}
=\kappa^nS_n.
$$
因此
$$
\beta(\nu,u)=c_p^{1/p}\omega_h.
\tag{1059.12}
$$

令 $\eta_p=\beta(\omega_b,\omega_a)$。$(\nu,u)$ 对 $(\omega_a,\omega_b)$ 的矩阵 determinant 为 $-s$，而 $p\equiv2\bmod3$ 给 $s^p=-s$，所以 (1059.11) 准确成为
$$
\beta(\nu,u)=(-s)^{1/p}\beta(\omega_a,\omega_b)
=-s\,\eta_p.
\tag{1059.13}
$$
这里使用 $(-s)^{1/p}=s$，没有把 Cartier 当作 $\mathbf F_{p^2}$ 线性。

取 $\omega_b$ 的上述实际 primitive $F_b$，$F_b(\infty)=0$。在 $0<j<p$ 的 $q$ 次数，其系数由
$dF_b=4a(q^4)dq/q$ 唯一确定：
$$
F_b(q)=\sum_{4m<p}\frac{a_m}{m}q^{4m}+O(q^p).
$$
可能的 $q^{p}$ 倍次项与 $a(q)$ 首项 $q$ 相乘，不贡献 $q^p$。故
$\eta_p=\mathscr C(F_b\omega_a)$ 的首个 $dq$ 系数恰为 (1059.2) 的 $A_p$。由 (1059.12)–(1059.13)，它已是 $\omega_h$ 的常数倍；$\omega_h$ 的 $dq$ 首项为一，因此
$$
\eta_p=A_p\omega_h,\qquad -s A_p=c_p^{1/p}.
$$
取 $p$ 次方，$A_p\in\mathbf F_p$ 给 $sA_p=c_p$，于是
$$
A_p=(3s)^nS_n/s=(-1)^N3^{3N+1}S_n,
$$
证明 (1059.4)，连同 R1049 的原单位证明 (1059.5)。

## 6. 同一个明确剩余和

还可准确写成
$$
S_n={}_3F_2\left(\begin{matrix}-n,-n,1/3\\1,4/3\end{matrix};-1\right)
=\frac23\sum_{i=0}^n
 \frac{(-1)^i\binom ni^2}{2i-n}\quad\text{于 }\mathbf F_p.
\tag{1059.14}
$$
第一式由 $(1/3)_i/(4/3)_i=1/(3i+1)$ 逐项得到。第二式用 $3n+2=p$；$n$ 奇，且 $|2i-n|<p$，全部中心分母都非零。该式给精确目标，尚未将它评为 Gamma 乘积或证明其单位。

本文未支付原 primitive/Legendre 同一标签的两重筛选，也未把这个 $f_N$ 值视为原 bare、核范数或 R1058 的 $DQ(1-Q)\lambda$ 最低值。后继继续该明确有限和的非零性，以及 open.md 的其它分支；主目标仍 OPEN。

## 原始来源与本次核对

- Michael Harrison, *A new automorphism of X0(108)*, arXiv:1108.5595v3（2014），[作者论文 PDF](https://arxiv.org/pdf/1108.5595)：第9页固定 eta 形式，Definition 4.2，第12页二次关系和 Theorem 4.4。本文只取所需明确关系，随后组合、函数和全部微分尺度在上文逐式推导。
- Michel Raynaud, *Sections des fibrés vectoriels sur une courbe*, Bull. Soc. Math. France 110 (1982), 103–125，[原文 PDF](https://www.numdam.org/article/BSMF_1982__110__103_0.pdf)，§4.1（印刷第118页）：局部 exact differential bundle 的 Cartier 交替配对。上文独立核了本次所用性质。
- [R1049](R1049-original-fN-theta-first-direction-moment.md) §6：同一个原 primary theta、全部模六相位与 $f_N$ 的尺度。

o1_theta 推导实际模型、微分和有限和；root 实读 Harrison 的相关完整关系及 Theorem 4.4、Raynaud §4.1，逐式核组合、九个极点/全部 cusp 分歧、good 模型延拓、primitive 次数、Cartier 的 $\zeta$ 半线性及最终标量。无数学程序执行，无窗口重算；原指定非零性未由这次来源识别自动获得。
