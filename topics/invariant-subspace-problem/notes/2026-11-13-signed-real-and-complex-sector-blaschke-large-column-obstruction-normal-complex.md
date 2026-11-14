# 负实 Blaschke 边界：粗逆源的准确 Gram 与大次数全列障碍

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065。

**状态：已证明的中间结论。** 前向零点靠近正单位点时，近圆逆真空源确实可以在原 $H$ 中收敛，却不属于 $\mathcal H_{\sqrt3}$。本稿给出一个算子范数收敛的明确例子和完整有限块 Gram 公式。这个现象没有突破同一固定正常态的全列障碍：负实参数的逆在去掉整体单位相位后有非负 Taylor 系数，完整块 Walsh 列可以直接使用正坐标锥控制。

进一步证明，允许每块任意有限个参数位于
$$
\mathcal R_{\rm signed}=
(-1,0)\ \cup\
\{a:0<|a|\le3/4\}\ \cup\
\{a:|a|<1,\ \operatorname{Re}a\ge3/4\},
\tag{0.1}
$$
只要准确实际逆源构造成功，便仍不能为既有固定 $f$ 满足 R244 的全有限列聚合界。它覆盖全部非零实参数与前稿复区域的任意混合。新的输入具有约 $q/3$ 的 Walsh 次数；证明不把负实边界参数的相位导数积分替代成失效的平方预算。

一般复圆周弧与真正湮灭者专属配对仍未解决。这里固定的 $f$ 已知不是湮灭者，普通 Hilbert ISP 未完成。

## 1. 准确的纯块与实际前提

在物理坐标 $\mathbb C^2$ 中令
$$
E=|1\rangle\langle0|,\quad
\Omega_+=2^{-1/2}(|0\rangle+|1\rangle),\quad
\chi=2^{-1/2}(|0\rangle-|1\rangle),\quad D=I-2E.
$$
于是 $D\Omega_+=\chi$、$D\chi=2\chi-\Omega_+$，且 $\|D\|=1+\sqrt2<3$。
大小为 $q$ 的块记为
$$
T_q=\frac2Q\sum_{j=1}^qE_j,\qquad Q=q+2,\qquad
\Omega=\Omega_+^{\otimes q}.
\tag{1.1}
$$
$T_q^{q+1}=0$，$\|T_q\|<1$。在物理坐标基中，$T_q$ 的所有矩阵元素非负。

对 $a\ne0$、$|a|<1$，仍取在标量点 $1$ 归一的前向因子
$$
\beta_a(z)=\frac{1+\overline a}{1+a}
 \frac{z+a}{1+\overline a z}.
\tag{1.2}
$$
$\beta_a(T_q)$ 是可逆收缩，所以其逆为扩张算子。
第 $i$ 块允许整体单位相位，
$$
R_i=\zeta_i\prod_\ell\beta_{a_{i\ell}}(T_{q_i}),\quad
U_i=R_i^{-1},\quad
g_i=U_i\Omega,\quad n_i=\|g_i\|\ge1.
\tag{1.3}
$$

实际 Walsh 提升满足
$$
V_j1=\chi_j,\qquad
\|V_j-D_j\|\le8\eta_j,\qquad
\eta_j\le e^{-770\,16^j}.
\tag{1.4}
$$
特别 $\|V_j\|<3$。对块内有限 Walsh 向量 $u=\sum_Fu_F\chi_F$，
$$
X_u=\sum_Fu_FV_F,\qquad X_u^0=\sum_Fu_FD_F.
$$
纯块有 $X_u^0\Omega=u$；实际也有 $X_u1=u$。

与既有构造一样，假设准确实际逆块为
$$
\widetilde U_i=\frac{X_{g_i}}{1-\varepsilon_i},\qquad
\widetilde g_i=\frac{g_i}{1-\varepsilon_i},\qquad
0\le\varepsilon_i<\frac12,
\tag{1.5}
$$
并已支付
$$
16q_i5^{q_i}\max(1,n_i)\eta_{\min B_i}\le\varepsilon_i.
\tag{1.6}
$$
假设互不交块的准确源乘积
$$
g^{(m)}=\prod_{i\le m}\widetilde g_i\longrightarrow g
\quad\text{在原 }H\text{ 中}.
\tag{1.7}
$$
使用 R244 时，还保持实际收缩逆积得到 $P$、$Pg=1$ 及同一组一致有界强单位等原前提。其结论给准确最小逆
$$
G=P^{-1}=X_g,\qquad Gu=X_ug
\tag{1.8}
$$
在全部有限 Walsh 列上成立。

固定分块和正常态为
$$
q_i=|B_i|=16^i,\qquad
c_i=2^{-i-2}=\frac1{4q_i^{1/4}},\qquad
f=1+\sum_{i\ge1}c_i\chi_{B_i},
$$
$$
\lambda=\|f\|^2=\frac{49}{48},\qquad
\phi_f(Y)=\langle Yf,f\rangle.
\tag{1.9}
$$
同一个 $f$ 和同一物理分块贯穿全稿。
由 (1.7) 的准确范数乘积、$n_i\ge1$，
$\prod_i(1-\varepsilon_i)^{-1}<\infty$，故 $\sum_i\varepsilon_i<\infty$。
特别 (1.6) 蕴含几何 carry 条件
$$
\sum_iq_i5^{q_i}\eta_{\min B_i}<\infty.
\tag{1.10}
$$
下面明确构造实际例子时只需这一分块条件。
从零选择按物理次序排列的位块也自动满足它：
$\min B_i\ge i$ 给 $\eta_{\min B_i}\le e^{-770q_i}$。

## 2. 负实逆的正系数与完整块列

设 $a=-b$，$0<b<1$。去掉整体相位 $-1$ 后，逆函数为
$$
P_b(T)=\frac{I-bT}{bI-T}.
\tag{2.1}
$$
幂零性给准确有限展开
$$
\boxed{
P_b(T)=b^{-1}I+
 (1-b^2)\sum_{n=1}^q b^{-n-1}T^n.
}
\tag{2.2}
$$
所有系数严格为正。因此任意有限负实逆积 $P(T)$ 都有非负 Taylor 系数，且在物理坐标基中保持非负锥。

对任意复向量 $v$，逐坐标三角不等式给
$$
|P(T)v|\le P(T)|v|.
\tag{2.3}
$$
由于完整 Walsh 块满足 $|\chi_B|=\Omega$，得到
$$
\boxed{\|P(T)\chi_B\|\le\|P(T)\Omega\|.}
\tag{2.4}
$$
这不限制负实因子个数，也不限制 $b$ 距 $1$ 的尺度。

若第 $i$ 块只有负实参数（允许整体相位），则
$X_{\chi_{B_i}}^0g_i=U_i\chi_{B_i}$。
由准确源张量分解，
$$
\|X_{\chi_{B_i}}^0g\|
=\frac{\|g\|}{n_i}\|U_i\chi_{B_i}\|
\le\|g\|.
\tag{2.5}
$$
在整块上用 telescoping，
$$
\|X_{\chi_{B_i}}-X_{\chi_{B_i}}^0\|
\le8q_i3^{q_i}\eta_{\min B_i}\longrightarrow0
\tag{2.6}
$$
由 (1.6) 支付。所以同一个实际最小逆满足
$\sup_i\|G\chi_{B_i}\|<\infty$。

另一方面，$D_F\chi_B$ 在每个命中坐标的 $\chi$ 分量为 $2\chi$。
因 $q_i$ 为偶数，纯完整矩准确为
$$
\boxed{
\phi_f(D_{B_i})=c_i^2\,2^{q_i}+2c_i.
}
\tag{2.7}
$$
真空项为零，两个交叉项各为 $c_i$。
实际误差至多 $\lambda$ 乘 (2.6)，所以实际矩趋于无穷。
因此，全部纯负实逆源族已经在完整块列上失败，而无需加权源结论。

## 3. 正单位点附近确实产生粗加权源

### 3.1 所有次数的准确有限块 Gram

令 $W_r=r^{\mathsf N}$，其中 $\mathsf N$ 为 Walsh 次数算子。
由于
$$
e^{sT_q}\Omega
=\bigotimes_{j=1}^q
 \left[\left(1+\frac sQ\right)\Omega_+
       -\frac sQ\chi_j\right],
$$
对任意复 $s,t$ 有准确核
$$
\boxed{
\langle W_re^{sT_q}\Omega,W_re^{tT_q}\Omega\rangle
=\left(1+\frac{s+\overline t}{Q}
 +\frac{(1+r^2)s\overline t}{Q^2}\right)^q.
}
\tag{3.1}
$$
内积在第一变量线性。

故若
$M_{mn}^{(r)}=\langle W_rT_q^m\Omega,W_rT_q^n\Omega\rangle$，
则
$$
\boxed{
M_{mn}^{(r)}
=\frac{m!n!}{Q^{m+n}}
\sum_{\ell=\max(0,m+n-q)}^{\min(m,n)}
\frac{q!(1+r^2)^\ell}
 {(q-m-n+\ell)!(m-\ell)!(n-\ell)!\ell!}.
}
\tag{3.2}
$$
全部条目非负。公式包括所有重复位和全部次数，没有截掉非对角 Gram 项。

对 (2.2) 的系数
$$
p_0=b^{-1},\qquad p_n=(1-b^2)b^{-n-1}\quad(1\le n\le q),
$$
准确逆真空预算就是
$$
\boxed{
\|P_b(T_q)\Omega\|_r^2
=\sum_{m,n=0}^q p_mp_nM_{mn}^{(r)}.
}
\tag{3.3}
$$

### 3.2 一个原空间算子范数收敛、却不在 $\mathcal H_{\sqrt3}$ 的源

记 $\delta=1-b$。准确恒等式为
$$
P_b(T)-I=\delta(I+T)(bI-T)^{-1}.
\tag{3.4}
$$
若 $q\delta\le1/4$，则
$b^{-q-1}\le e$，因为 $-\log(1-\delta)\le2\delta$。
有限 Neumann 和及 $\|T\|<1$ 给
$$
\boxed{
\|P_b(T)-I\|\le4e\,q\delta.
}
\tag{3.5}
$$

现在对 $i\ge3$ 取
$$
\delta_i=e^{-q_i/100},\qquad b_i=1-\delta_i,
\tag{3.6}
$$
前两个块取恒等算子。于是 $q_i\delta_i<1/4$，并且
$\sum_iq_i\delta_i<\infty$。
(3.5) 表明纯逆算子张量积在算子范数中收敛到有界可逆算子；
纯真空源也在原 $H$ 中收敛。每个纯逆为扩张，逆块为收缩。

加权范数的行为完全不同。由 $p_n\ge\delta$、(3.2) 条目非负，
$$
\|P_b(T_q)\Omega\|_{\sqrt3}
\ge\delta\left\|\sum_{n=0}^qT_q^n\Omega\right\|_{\sqrt3}.
\tag{3.7}
$$
对任意 $s\ge0$，系数 $e^{-s}s^n/n!\le1$。
再次利用整个 Gram 的条目非负性，
$$
\left\|\sum_{n=0}^qT_q^n\Omega\right\|_{\sqrt3}
\ge e^{-s}\|e^{sT_q}\Omega\|_{\sqrt3}.
$$
取 $s=q/2$，由 (3.1)，
$$
e^{-q/2}\|e^{qT_q/2}\Omega\|_{\sqrt3}
=e^{-q/2}
 \left(1+\frac qQ+\frac{q^2}{Q^2}\right)^{q/2}.
$$
而
$$
1+q/Q+q^2/Q^2\ge3q/Q
$$
且
$$
(q/Q)^{q/2}\ge e^{-1}
$$
。
故得到显式下界
$$
\boxed{
\|P_{b_i}(T_{q_i})\Omega\|_{\sqrt3}
\ge e^{-1}
 \exp\left[
 \left(\frac{\log3-1}{2}-\frac1{100}\right)q_i
 \right]\longrightarrow\infty.
}
\tag{3.8}
$$
指数严格为正，例如
$\log3=2\operatorname{arctanh}(1/2)>1+1/12$。

实际提升同样可付清。在同一固定分块的 (1.10) 下，
对充分大块 $n_i<2$，取
$\varepsilon_i=32q_i5^{q_i}\eta_{\min B_i}$；
它们可和且最终小于 $1/2$，满足 (1.6)。
有限初块另行取恒等。
逐 Walsh 系数 Cauchy--Schwarz 与 (1.4) 给准确扰动界
$$
\|X_{g_i}-P_{b_i}(T_i)\|
\le8q_i(3\sqrt2)^{q_i}n_i\eta_{\min B_i}
\le\varepsilon_i.
$$
因此 $\widetilde U_i$ 扩张，逆块收缩，并有
$$
\|\widetilde U_i-I\|
\le2\|P_{b_i}(T_i)-I\|+4\varepsilon_i.
\tag{3.9}
$$
右侧可和，所以实际 $\widetilde U_i$ 的积也在算子范数中收敛到有界可逆 $G$，
其逆块积收敛到 $P=G^{-1}$，且 $g=G1$、$Pg=1$。
实际真空列仍准确为 $g_i/(1-\varepsilon_i)$。

此实际 $g\notin\mathcal H_{\sqrt3}$。
事实上固定任一块时，准确因式分解和其余块范数至少 $1$ 给
$$
\|g\|_{\sqrt3}\ge
\frac{\|g_i\|_{\sqrt3}}{1-\varepsilon_i},
$$
若左侧有限便与 (3.8) 矛盾。
这一例子甚至具有有界的实际 $G$；它说明
$\mathcal H_{\sqrt3}$ 是充分源空间，而非全部合格逆源的必要空间。

负实边界的相位导数可集中在极窄窗口并绕过整周。
本例没有使用、也不推出对应的 $\sum\tau_i^2/q_i<\infty$。
第2节的正坐标锥列仍严格排除此例以及全部负实逆积为固定 $\phi_f$ 提供全列聚合表示。

## 4. 混合族只需要的两个径向必要条件

现在允许 (0.1) 的任意混合。
把每块分成：

- 所有负实参数，归入正系数逆积 $P_i(T)$；
- 其余满足 $|a|\le3/4$ 的参数，记其数目为 $r_i$；
- 其余满足 $\operatorname{Re}a\ge3/4$ 的参数，归入 $H_i(T)$。

边界重叠因子任选一致归类即可。定义
$$
D_i(z)=\prod_{\rm compact}(z+a),\qquad
N_i(z)=\prod_{\rm compact}(1+\overline a z),\qquad
b_i^{\rm c}=\prod_{\rm compact}(1+|a|),
$$
$$
\tau_i^+=\sum_{\rm cap}\frac{1-|a|^2}{|1+a|^2}.
\tag{4.1}
$$
于是准确地，除一个整体单位相位外，
$$
U_i=P_i(T_i)H_i(T_i)N_i(T_i)D_i(T_i)^{-1}.
\tag{4.2}
$$

由 (1.7) 和各块范数至少 $1$，
$g_i\to\Omega$。具体地，
$$
\|g^{(i)}-g^{(i-1)}\|
=\|g^{(i-1)}\|\,
 \|g_i/(1-\varepsilon_i)-\Omega\|,
$$
先得准确实际块趋于 $\Omega$，继而得 $\varepsilon_i\to0$ 和 $g_i\to\Omega$。
因此 $R_i\Omega\to\Omega$。

[Schur 真空密度稿](2026-11-13-schur-zero-count-for-convergent-inverse-vacuum-blocks-normal-next.md)
已证明：对 Schur 前向函数 $B_i$，
若 $\langle B_i(T_i)\Omega,\Omega\rangle\to1$，
则在 $h_i=q_i^{-1/2}$ 上，
$$
B_i(1-h_i)\longrightarrow1.
\tag{4.3}
$$
其证明用准确圆周真空密度在 $h_i$ 窗口上的高斯下界，并控制 Poisson 核的完整外尾；允许随 $i$ 变化的任意有限内函数及整体相位。因此 (4.3) 适用于这里整个前向积。

紧子圆盘每个零点使模至多乘 $e^{-h_i/14}$，故
$$
\boxed{r_i=o(\sqrt{q_i}).}
\tag{4.4}
$$

另一方面，对 cap 参数和 $x=1-h$，
$$
1-|\beta_a(x)|^2
=\frac{(1-x^2)(1-|a|^2)}
 {|1+\overline a x|^2}.
$$
这里 $|1+a|\ge7/4$、$h\le1/2$，从而
$|1+\overline a x|\le |1+a|+h\le(9/7)|1+a|$。
又 $1-x^2\ge h$，所以
$$
1-|\beta_a(1-h)|^2
\ge\frac12h\,\frac{1-|a|^2}{|1+a|^2}.
$$
整个前向积的其他因子模均至多 $1$。于是
$$
|B_i(1-h_i)|\le e^{-h_i\tau_i^+/4}.
$$
结合 (4.3)，得到
$$
\boxed{\tau_i^+=o(\sqrt{q_i}).}
\tag{4.5}
$$
这两个小阶必要条件不对负实因子总数或尺度作任何限制。
没有对混合积使用可能失效的总相位导数比较。

还需一个有用的范数关系。因所有逆因子可交换且分别扩张，
在 (4.2) 中把全部非负实逆放到 $P_i$ 之后，可得
$$
\boxed{\|P_i(T_i)\Omega\|\le n_i.}
\tag{4.6}
$$
这个结论只用扩张性，不依靠其他因子保持正锥。

## 5. 纯块幂的三次衰减及 cap 的绝对系数算子界

### 5.1 纯块幂的严格范数上界

令 $S_q=\sum_{j=1}^qE_j$。
在物理占据数 $k$ 到 $k+n$ 的矩形块上，
$S_q^n$ 每个非零矩阵元为 $n!$，
行和为 $(k+n)!/k!$，
列和为 $(q-k)!/(q-k-n)!$。
Schur 行列和界取到等号，因为两个常数向量互相映射。
所以
$$
\|S_q^n\|
=\max_{0\le k\le q-n}
 \prod_{\ell=0}^{n-1}
 \sqrt{(k+\ell+1)(q-k-\ell)}.
\tag{5.1}
$$
置 $u_\ell=2(k+\ell)+1-q$。有
$$
(k+\ell+1)(q-k-\ell)=\frac{(q+1)^2-u_\ell^2}{4},
$$
$$
\sum_{\ell=0}^{n-1}u_\ell^2\ge\frac{n(n^2-1)}3.
$$
利用 $\sqrt{1-x}\le e^{-x/2}$，得到
$$
\boxed{
\|T_q^n\|
\le\left(\frac{q+1}{q+2}\right)^n
 \exp\left[-\frac{n(n^2-1)}{6(q+1)^2}\right]
\quad(0\le n\le q).
}
\tag{5.2}
$$

取
$$
\rho=\frac57,\qquad L=\log\frac75,\qquad
c_\rho=\frac{2\sqrt2}{3}L^{3/2}.
$$
最大化实变量
$Ln-n^3/[6(q+1)^2]$，其最大值为 $c_\rho(q+1)$。
又 $n/[6(q+1)^2]\le1/(6q)$，因此
$$
\boxed{
\max_{0\le n\le q}\rho^{-n}\|T_q^n\|
\le\exp[c_\rho(q+1)+1/(6q)].
}
\tag{5.3}
$$
常数具有所需严格余量：
$$
c_\rho<\frac15.
\tag{5.4}
$$
例如
$L\le2/5-(2/5)^2/2+(2/5)^3/3=128/375<7/20$，
故 $\sqrt{2L}<21/25$，从而
$c_\rho=(2/3)L\sqrt{2L}<49/250<1/5$。

### 5.2 cap 逆积的绝对系数界

[复近圆扇区稿](2026-11-13-complex-boundary-sector-blaschke-sources-and-mixed-obstruction-normal-complex.md)
的逐系数对数估计给如下简单的标量控制。
若 $H$ 是所有 cap 逆因子的乘积并按 $H(1)=1$ 归一，
令 $\tau^+$ 如 (4.1)，则在 $w=1-z$ 中
$$
|H(z)|\le
\exp\left(\frac{\tau^+|w|}{1-4|w|/7}\right)
\qquad(|w|<7/4).
\tag{5.5}
$$
这是因为各因子为
$(1-B_aw)/(1-A_aw)$，
$|A_a|,|B_a|\le4/7$，
且 $A_a-B_a=(1-|a|^2)/|1+a|^2>0$。

取 $\rho_1=8/11$。在 $|z|\le\rho_1$ 上，
$|1-z|\le19/11$，而
$1-(4/7)(19/11)=1/77$。
所以
$$
\sup_{|z|\le\rho_1}|H(z)|\le e^{133\tau^+}.
$$
若 $H(z)=\sum_{n\ge0}h_nz^n$，Cauchy 界和
$\rho/\rho_1=55/56$ 给
$$
\sum_{n\ge0}|h_n|\rho^n\le56e^{133\tau^+}.
\tag{5.6}
$$
定义真正非负系数的有限算子
$$
V(T_q)=\sum_{n=0}^q|h_n|T_q^n.
$$
则 $|H(T_q)v|\le V(T_q)|v|$，且 (5.3)--(5.6) 给
$$
\boxed{
\|V(T_q)\|
\le56\exp[c_\rho(q+1)+1/(6q)+133\tau^+].
}
\tag{5.7}
$$
(4.5) 因而使右侧为 $\exp[(c_\rho+o(1))q_i]$。
没有把系数绝对值形成的算子误认为原复逆积本身。

## 6. 大次数实际输入及其逆像预算

令
$$
k_i=\lfloor q_i/3\rfloor,\qquad
v_{q,k}=\binom qk^{-1/2}\sum_{|F|=k}\chi_F,
$$
$$
\boxed{
u_i=\frac{D_i(T_i)v_{q_i,k_i}}{b_i^{\rm c}}.
}
\tag{6.1}
$$
$\|v_{q,k}\|=1$，$\|T_i\|<1$，因此 $\|u_i\|\le1$。
Walsh 次数至多 $k_i+r_i<q_i$ 对充分大 $i$ 成立。

紧内分母在 (4.2) 中准确消去：
$$
U_iu_i=\text{单位相位}\cdot
 P_i(T_i)H_i(T_i)\frac{N_i(T_i)}{b_i^{\rm c}}v_{q_i,k_i}.
\tag{6.2}
$$
在物理坐标中，
$$
|v_{q,k}|\le\sqrt{\binom qk}\,\Omega.
\tag{6.3}
$$
令
$N_i^{\rm abs}(T)=\prod_{\rm compact}(I+|a|T)$。
其系数非负，逐坐标主控 $N_i(T)$，并且
$\|N_i^{\rm abs}(T_i)/b_i^{\rm c}\|\le1$。
$P_i,V_i,N_i^{\rm abs}$ 互相可交换且保持非负锥。
因此 (6.2)--(6.3)、(4.6) 给
$$
\|U_iu_i\|
\le\sqrt{\binom{q_i}{k_i}}\,
 \|V_i(T_i)\|\,n_i.
\tag{6.4}
$$

准确源张量分解消掉 $n_i$：
$$
\|X_{u_i}^0g\|
=\frac{\|g\|}{n_i}\|U_iu_i\|
\le\|g\|\sqrt{\binom{q_i}{k_i}}\|V_i(T_i)\|.
\tag{6.5}
$$

此处输入次数约为 $q_i/3$，不能沿用小次数的
$q_i^{(\deg u_i)/2}$ 粗界。
应直接对全部 $2^{q_i}$ 个 Walsh 系数用 Cauchy--Schwarz：
$\sum_F|(u_i)_F|\le2^{q_i/2}\|u_i\|\le2^{q_i/2}$。
结合 (1.4) 的完整 telescoping，
$$
\boxed{
\Delta_i:=\|X_{u_i}-X_{u_i}^0\|
\le8q_i(3\sqrt2)^{q_i}\eta_{\min B_i}
\le\frac{\varepsilon_i}{2n_i}
 \left(\frac{3\sqrt2}{5}\right)^{q_i}\longrightarrow0.
}
\tag{6.6}
$$
因此对同一个实际最小逆，
$$
\boxed{
\|Gu_i\|\le\|g\|
 \left[
 56\sqrt{\binom{q_i}{k_i}}\,
 e^{c_\rho(q_i+1)+1/(6q_i)+133\tau_i^+}
 +\Delta_i
 \right].
}
\tag{6.7}
$$
所有次数和全部实际列已经计入预算。

## 7. 完整块矩的中心平移与严格下界

固定 $q,k$、$|F|=k$。定义纯有限块线性泛函
$$
\ell_{q,k}(p)=2^{-k}\langle p(T_q)D_F\chi_B,\chi_B\rangle.
$$
其值与 $F$ 的位置无关。
逐坐标计算给准确整个生成式
$$
\ell_{q,k}(e^{tT_q})
=(1-t/Q)^{q-k}(1-t/(2Q))^k.
\tag{7.1}
$$
因 $k$ 现在约为 $q/3$，不能仍在标量 $-1$ 处作小次数近似。
正确的均值中心为
$$
\xi_{q,k}=-\frac{q-k/2}{Q}
=-1+\frac{2+k/2}{Q}.
\tag{7.2}
$$
中心化生成函数的对数准确为
$$
\log\ell_{q,k}(e^{t(T_q-\xi_{q,k})})
=-\sum_{n\ge2}
 \frac{q-k+k/2^n}{nQ^n}\,t^n.
\tag{7.3}
$$
在 $0\le t\le Q/2$ 上，对指数 Taylor 系数取绝对值后，
$$
\boxed{
\sum_{m\ge0}
 \frac{|\ell_{q,k}((T_q-\xi_{q,k})^m)|}{m!}\,t^m
\le e^{t^2/q}.
}
\tag{7.4}
$$
因为右侧对数主控来自
$q\sum_{n\ge2}(t/Q)^n/n\le t^2/q$。
这是绝对系数主控，不将 $\ell_{q,k}$ 当作正测度。

当 $q\ge80$、$k=\lfloor q/3\rfloor$ 时，
$(2+k/2)/Q\le3/16$，所以 $\xi_{q,k}\le-13/16$。
每个紧内参数 $|a|\le3/4$ 因而满足
$$
|a+\xi_{q,k}|\ge1/16,\qquad
\frac{|a+\xi_{q,k}|}{1+|a|}\ge1/28.
\tag{7.5}
$$
展开
$$
\frac{D_i(T_i)}{D_i(\xi_i)}
=\prod_{\rm compact}
 \left[I+\frac{T_i-\xi_i}{a+\xi_i}\right],
\quad \xi_i=\xi_{q_i,k_i}.
$$
第 $m$ 次系数模至多 $(16r_i)^m/m!$。
由 (4.4)，最终 $16r_i\le Q_i/2$，故 (7.4) 给
$$
\boxed{
\left|
 \frac{\ell_{q_i,k_i}(D_i(T_i))}{D_i(\xi_i)}-1
\right|
\le e^{256r_i^2/q_i}-1=:E_i\longrightarrow0.
}
\tag{7.6}
$$
同时 (7.5) 给
$|D_i(\xi_i)|/b_i^{\rm c}\ge28^{-r_i}$。

纯代数中 $X_{u_i}^0=D_i(T_i)X_{v_{q_i,k_i}}^0/b_i^{\rm c}$。
对全部 $F$ 求和，(7.1) 给
$$
\langle X_{u_i}^0\chi_{B_i},\chi_{B_i}\rangle
=2^{k_i}\sqrt{\binom{q_i}{k_i}}\,
 \frac{D_i(\xi_i)}{b_i^{\rm c}}\,(1+\theta_i),
\quad|\theta_i|\le E_i.
\tag{7.7}
$$

选单位相位 $\omega_i$ 使 $\omega_iD_i(\xi_i)>0$。
因为 $\deg u_i<q_i$，纯真空与完整块的两个交叉矩都为零。
剩余真空项的模至多 $\lambda$，因 $\|u_i\|\le1$。
所以对充分大 $i$，
$$
\operatorname{Re}\phi_f(X_{\omega_i u_i}^0)
\ge
\frac1{32\sqrt{q_i}}\,
 2^{k_i}\sqrt{\binom{q_i}{k_i}}\,28^{-r_i}
-\lambda.
\tag{7.8}
$$
实际误差的模至多 $\lambda\Delta_i\to0$。

将 (7.8) 与 (6.7) 相除。
$k_i/q_i\to1/3$，$r_i=o(\sqrt{q_i})$，
$\tau_i^+=o(\sqrt{q_i})$，
因此
$$
\boxed{
\liminf_{i\to\infty}\frac1{q_i}
 \log\frac{|\phi_f(X_{\omega_i u_i})|}
              {\|G(\omega_i u_i)\|}
\ge\frac{\log2}{3}-c_\rho>0.
}
\tag{7.9}
$$
最后的余量甚至大于 $1/45$：
$\log2>2/3$（对 $\int_1^2x^{-1}dx$ 用严格 Jensen），
而 $c_\rho<1/5$。
各列非零，因为 $D_i(T_i)$ 可逆。
分母为同一个 $G$ 的准确实际逆像范数。

这证明了区域 (0.1) 的全部混合成功逆源族均违反固定 $\phi_f$ 的全列聚合界。

## 8. 有限个完整逆源的组合

若同一固定分块上有限个完整源 $g^{(\nu)}$ 分别满足上述前提，
而
$$
g=\sum_{\nu=1}^Kz_\nu g^{(\nu)}
$$
确为某个合格 $P$ 的 $P^{-1}1$，结论仍成立。

取各分支紧内分母的共同乘积 $D_i$，令总次数为 $r_i$；
由 (4.4)，有限和仍为 $o(\sqrt{q_i})$。
各分支的 $\tau_{i,\nu}^+=o(\sqrt{q_i})$。
用共同分母定义 (6.1)。
对第 $\nu$ 分支，分母消去后多出的其他分支紧内分母
具有系数绝对值主控 $\prod(T+|a|)$。
这些多出因子连同本支紧内分子，在共同 $b_i^{\rm c}$ 归一后，
算子范数不超过 $1$。
它们保持非负锥并与本支 $P_i,V_i$ 交换，
所以 (6.4)--(6.7) 对每个分支仍成立。
有限三角和只改变常数，并以
$\max_\nu\tau_{i,\nu}^+=o(\sqrt{q_i})$ 控制指数。
矩下界只用共同分母，(7.9) 因此不变。

这里组合完整逆源，没有将正则器之和的逆误认为逆源之和。
一般块内有理线性组合未自动满足前向 Schur 性和系数预算。

## 9. 严格结论边界与依赖

本稿提供两个不同事实：

1. 正单位点附近的前向零点确能给原 $H$ 收敛而加权粗糙的逆真空源；
   (3.1)--(3.3) 是准确全有限 Gram，(3.6)--(3.9) 是可重做的明确参数与实际预算。
2. 对固定非湮灭正常态 (1.9)，这些负实边界因子及 (0.1) 的任意有限块混合
   仍失败于真正有限列；负实正系数结构承担了此前加权论证无法承担的部分。

靠近其余圆周弧的任意复参数、不同物理分块、无真空原像前向族、
真正湮灭者专属配对和慢符号有界分母仍开放。
本稿没有证明一般 $\tau$ 平方可和，也没有把本固定 $f$ 宣称为湮灭者。

完整依赖：

- [R244 聚合逆图准则](../results/R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)；
- [复近圆扇区的平方预算与完整混合障碍](2026-11-13-complex-boundary-sector-blaschke-sources-and-mixed-obstruction-normal-complex.md)；
- [Schur 真空密度、径向控制及紧内零点数](2026-11-13-schur-zero-count-for-convergent-inverse-vacuum-blocks-normal-next.md)；
- [复分母消去的准确生成式](2026-11-13-complex-rational-block-denominator-cancellation-and-growing-order-obstruction-normal-next.md)；
- [R255 实际 Walsh 双输入端点](../results/R255-optimal-sqrt3-degree-threshold-and-normal-factorization.md)（背景；本稿大次数列不用其加权上界）。

本稿写入前比对 main 6115ffb13124e941e99755711c9b388bd72c184e 的根 README 与课题 README，blob 分别仍为 f787a306d90892d8dec765dc59747d60ba39f055、6bd7bd3f74d69473916a3160eafab4b2ab2ad5cd，无规矩变更。GitHub 文件读取不记为 git pull。
