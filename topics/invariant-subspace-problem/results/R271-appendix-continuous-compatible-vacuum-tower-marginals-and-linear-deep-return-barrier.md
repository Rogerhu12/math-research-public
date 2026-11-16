# R271 附录：原连续尾相容真空塔的精确边际约束与同源全深返回的线性门槛

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明；范围为原连续尾的真相容塔。** 本稿不使用任意有限池代替原尾。对 $b_i=(i+1)^{-2}$ 的无限尾，即使相容塔允许复系数及全部 primitive 修正，其相对各层最短直接真空预像的范数也不能在高度 $j\asymp x$ 上有绝对常数。若第一列取真实 MP，则整个高层区间都有线性下界。后者给同一完整源 $a=H_C(s)^{-1}g$ 的全深顺次修复一个准确必要条件。

这不是原实际 $a$ 的坏例，不否定其未付的特殊加权能量衰减，也不否定原 same-$w$ 边界。本稿仅排除在全深修复中免费使用统一相干相对塔常数；线性 $O(h)$ 上界仍未被排除。

依赖范围：

- [完整强前缀 Gram 比较及真实远尾方差同源极限](R271-appendix-actual-strong-head-gram-comparison-and-true-far-variance-source-limit.md)；
- [原同一 Bernoulli 池的精确相容塔与完整源短缩](R271-appendix-compatible-bernoulli-vacuum-towers-and-same-test-exact-kernel-approximation.md)；
- [原连续尾各固定孔层的完整有界右逆](R234-appendix-quartic-head-powers-and-super-four-thirds-hole-weights.md)，§1(1.1)。最后一条只用于确认 canonical MP 塔的固定层自然域，不用于其范数估计。

## 1. 原无限尾、完整相容性与归一化

令整数 $x\ge1$，在原 Boolean 孔层 $\mathcal H_j$ 上取
$$
D=D_x=\sum_{i\ge x}b_iE_i,\qquad b_i=(i+1)^{-2},\qquad z_i=b_i^2,
$$
$$
S=S_x=\sum_{i\ge x}z_i,\qquad
\omega_j=(D^*)^j\Omega,\qquad
\sigma_j^2=\|\omega_j\|^2=(j!)^2e_j(z).
\tag{1.1}
$$
$D$ 在全孔直和上有界，因为 $\sum b_i<\infty$。每个 $e_j(z)$ 有限且严格正。

令 $L\ge1$，考虑任意真正 Hilbert 相容塔
$$
v_j\in\mathcal H_j,\qquad
v_0=\Omega,\qquad Dv_j=v_{j-1}\quad(1\le j\le L).
\tag{1.2}
$$
不要求 $v_j$ 坐标非负，不要求后续列各自最小，也不删除 primitive 修正。由 $D^jv_j=\Omega$，
$$
\langle v_j,\omega_j\rangle=1
$$
（若采用另一内积线性约定，取相应共轭；以下坐标等式不变）。

在所有 $j$ 子集上定义概率及复密度
$$
\mu_j(I)=\frac{z_I}{e_j(z)},\qquad
f_j(I)=\frac{j!e_j(z)}{b_I}(v_j)_I,
$$
$$
\nu_j(I)=\mu_j(I)f_j(I)=j!b_I(v_j)_I.
\tag{1.3}
$$
它们满足
$$
\sum_I|\nu_j(I)|\le j!\sqrt{e_j(z)}\,\|v_j\|<\infty,
$$
$$
\mathbb E_{\mu_j}f_j=1,\qquad
\boxed{\mathcal M_j:=\mathbb E_{\mu_j}|f_j|^2
=\sigma_j^2\|v_j\|^2\ge1.}
\tag{1.4}
$$
因此 $\nu_j$ 是总质量 $1$ 的有限复测度，而非未经证明的正概率。

直接逐坐标使用 (1.2)，对每个 $|I|=j-1$ 有
$$
\boxed{
\sum_{i\notin I}\nu_j(I\cup\{i\})=j\,\nu_{j-1}(I).
}
\tag{1.5}
$$
全部求和绝对收敛。换言之，$j$ 层的均匀删除边际正好是前一层。特别，对任意有限位置集合 $A$，令 $N_A(I)=|I\cap A|$，存在同一个复数
$$
p_A=\sum_{i\in A}\nu_1(\{i\})
$$
使所有高度满足
$$
\boxed{\mathbb E_{\nu_j}N_A=j\,p_A.}
\tag{1.6}
$$
这条约束保留了完整相容性。分别最小的直接列 $\omega_j/\sigma_j^2$ 通常不满足它。

## 2. 固定大小原乘积测度的两个初等事实

记
$$
m_A(j)=\mathbb E_{\mu_j}N_A,\qquad
V_A(j)=\operatorname{Var}_{\mu_j}N_A.
$$
由于 $\mathbb E_{\mu_j}(f_j-1)=0$，(1.6) 和 Cauchy--Schwarz 给
$$
\boxed{
|j p_A-m_A(j)|^2
\le(\mathcal M_j-1)V_A(j).
}
\tag{2.1}
$$
这对复 $f_j$ 同样成立。

还需要真实的负相关。对不同 $i,\ell$，把两位置删去后的初等对称和记为 $e_r^{i\ell}$，则
$$
\begin{aligned}
&\mathbb E_{\mu_j}n_i\,\mathbb E_{\mu_j}n_\ell
-\mathbb E_{\mu_j}(n_i n_\ell)\\
&\quad=
\frac{z_i z_\ell}{e_j(z)^2}
\left[(e_{j-1}^{i\ell})^2-e_{j-2}^{i\ell}e_j^{i\ell}\right]\ge0.
\end{aligned}
\tag{2.2}
$$
所用非归一 log-concavity 可自足证明：若无内零的非负序列 $a_k$ log-concave，则乘一个因子 $1+zt$ 后的系数 $c_k=a_k+za_{k-1}$ 满足
$$
\begin{aligned}
c_k^2-c_{k-1}c_{k+1}
={}&a_k^2-a_{k-1}a_{k+1}\\
&+z(a_ka_{k-1}-a_{k-2}a_{k+1})\\
&+z^2(a_{k-1}^2-a_{k-2}a_k)\ge0.
\end{aligned}
$$
中项由相邻比值单调得到。从常数多项式开始归纳，再对有限位置头取极限，即得 (2.2) 所需的无限尾结论。

因此
$$
\boxed{
V_A(j)\le\sum_{i\in A}p_i(j)(1-p_i(j))
\le\min\{|A|/4,\ m_A(j)\}\le\min\{|A|/4,j\}.
}
\tag{2.3}
$$
所有下界均将 (2.1) 与 (2.3) 在同一个原测度上使用；没有套任意协方差逆。

另由直接计数，
$$
\boxed{
\frac{m_A(j)}j=
\frac{\mathbb E_{\mu_{j-1}}\sum_{i\in A\setminus I}z_i}
{\mathbb E_{\mu_{j-1}}\sum_{i\notin I}z_i}.
}
\tag{2.4}
$$
特别，若 $z_{\max}=(x+1)^{-4}$、$S_A=\sum_{i\in A}z_i$，则
$$
\frac{m_A(j)}j\ge \frac{S_A-(j-1)z_{\max}}{S}
\tag{2.5}
$$
只要右侧非负。证明中只把分母从上控制为 $S$，没有更换条件分布。

## 3. 不固定第一列也必有线性代价

取原前 $x$ 个尾位置
$$
A=\{x,x+1,\ldots,2x-1\}.
$$
原积分界给
$$
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3},\qquad
\frac{S_A}{S_x}=1-\frac{S_{2x}}{S_x}
\ge1-\left(\frac{x+1}{2x}\right)^3.
\tag{3.1}
$$

### 定理 3.1

若 $x\ge16$，且相容塔 (1.2) 的高度满足
$$
L\ge\left\lceil\frac{7x}4\right\rceil,
$$
则
$$
\boxed{
\max_{1\le j\le L}\sigma_j^2\|v_j\|^2
\ge1+\frac{x}{32768}.
}
\tag{3.2}
$$
所有列都可有符号或复系数，第一列亦可自由选择。

**证明。** 取
$$
j_1=\lfloor x/16\rfloor,\qquad
j_2=\lceil7x/4\rceil.
$$
由 $x\ge16$，
$$
\frac{S_A}{S_x}\ge\frac56,\qquad
\frac{z_{\max}}{S_x}\le\frac3{x+1},\qquad
j_1\ge\frac{x}{32}.
$$
应用 (2.5)，得
$$
\frac{m_A(j_1)}{j_1}\ge\frac56-\frac3{16}=\frac{31}{48}.
$$
而 $N_A\le x$，故
$$
\frac{m_A(j_2)}{j_2}\le\frac47.
$$
两个实均值的差至少 $25/336>1/14$。对于同一个复数 $p_A$，至少一个 $j\in\{j_1,j_2\}$ 满足
$$
\left|p_A-\frac{m_A(j)}j\right|\ge\frac1{28}.
$$
(2.1)、$V_A(j)\le j$ 及 $j\ge x/32$ 于是给
$$
\mathcal M_j-1\ge\frac j{784}
\ge\frac{x}{25088}\ge\frac{x}{32768}.
$$
证毕。

此结论只排全塔绝对常数，并没有排掉线性 $O(h)$ 预算。

## 4. 第一列取真实 MP 时的整个高层区间

由于 $D:\mathcal H_1\to\mathcal H_0$ 的第一行是 $b$，
$$
D^\dagger\Omega=\frac1S\sum_{i\ge x}b_i e_i.
\tag{4.1}
$$
故只要 (1.2) 的第一列取 (4.1)，(1.6) 中
$$
p_A=S_A/S.
$$
后续列仍可任取相容的 Hilbert 预像。

### 定理 4.1

对 $x\ge4$、每个合法高度 $j\ge\lceil3x/2\rceil$，
$$
\boxed{
\sigma_j^2\|v_j\|^2
\ge1+c_*x,\qquad
c_*=\frac{18769}{262144}.
}
\tag{4.2}
$$

**证明。** (3.1) 给
$$
p_A\ge1-(5/8)^3=\frac{387}{512}.
$$
因此
$$
j p_A-m_A(j)\ge\frac{3x}2\frac{387}{512}-x
=\frac{137x}{1024}.
$$
用 (2.1) 和 $V_A(j)\le x/4$，得到
$$
\mathcal M_j-1\ge
\frac{(137x/1024)^2}{x/4}
=\frac{18769}{262144}x.
$$
证毕。

特别，canonical 塔
$$
v_j=(D^\dagger)^j\Omega
\tag{4.3}
$$
满足此界。原完整固定孔层右逆保证每一步 $D^\dagger:\mathcal H_{j-1}\to\mathcal H_j$ 有界且全域定义；有限 $j$ 的顺次复合合法。这不声称全孔直和 $D^\dagger$ 有界，也不将 $(D^\dagger)^j$ 换成 $(D^j)^\dagger$。

## 5. 同一完整源的全深修复准确平方

取原强头
$$
C=A_m+D_{[m,x)},\qquad x=m+R,\qquad C^h=0,\qquad h=2^m+R.
$$
给定 $s\ge S_x$，令
$$
H_C(s)=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{s^jj!},\qquad
a=H_C(s)^{-1}g,
$$
$$
E_j=\frac{\|C^ja\|^2}{s^jj!},\qquad
F_s=\sum_{j=0}^{h-1}\frac{(-C)^ja\otimes\omega_j}{s^jj!}.
\tag{5.1}
$$
这是完整强头 inverse，不压 forcing 原支持。取 canonical 塔 (4.3)，定义
$$
z=\sum_{j=0}^{h-1}(-C)^ja\otimes v_j.
\tag{5.2}
$$
相容性和 $C^h=0$ 给 $(C+D_x)z=0$。其原总尾孔数不超过 $R+h-1$，所以当 $Q\ge R+h-1$ 时，$z$ 属于同一原 $K_{m,Q}$。

由于各项在不同远孔层，且 $\langle v_j,\omega_j\rangle=1$，
$$
\boxed{
\|F_s-z\|^2=
\sum_{j=1}^{h-1}
\left[
s^jj!\|v_j\|^2-2+\frac{\sigma_j^2}{s^jj!}
\right]E_j.
}
\tag{5.3}
$$
这是完整同源平方，未对 $h$ 个顺次修复项作三角求和。它也恰是有限 Neumann 修复的总量：
$$
F_s-z=
\sum_{r=0}^{h-1}(-C)^r(D_x^\dagger)^{r+1}(C+D_x)F_s.
\tag{5.4}
$$
核对 (5.4) 时，对 $j\ge1$ 有
$D^\dagger D\omega_j=\omega_j$，因为
$\omega_j\in\operatorname{Ran}D^*\subset(\ker D)^\perp$。
于是每个固定远孔层的中间项逐一 telescoping，仅留下
$\omega_j/(s^jj!)-(D^\dagger)^j\Omega$；最高 $C^h$ 项为零。
全部运算只涉及有限个确定孔层，其完整 MP 域已由 §4 支付。

令
$$
y_j=\frac{\sigma_j^2}{s^jj!}\in(0,1],\qquad
\mathcal M_j=\sigma_j^2\|v_j\|^2.
$$
(5.3) 的系数准确为
$$
\frac{\mathcal M_j}{y_j}-2+y_j
=\frac{\mathcal M_j-1}{y_j}+\frac{(1-y_j)^2}{y_j}
\ge\mathcal M_j-1.
$$
故定理 4.1 直接给
$$
\boxed{
\|F_s-z\|^2
\ge c_*x\sum_{j=\lceil3x/2\rceil}^{h-1}E_j,
\qquad x\ge4.
}
\tag{5.5}
$$
空和按零理解。

原 $R=d=2^m$、$x=m+d$、$h=2d$，在 $m\ge10$ 时有
$h-1\ge\lceil7x/4\rceil$，且 $R+h-1=3d-1<4d$。因此 §§3--5 同时适用于原
$$
4d\le Q\le e^{26d^3}
$$
窗口里的这个真实候选，而非另造的有限池或改权模型。

## 6. 结论的准确边界

已付强前缀比较给
$$
\epsilon_m=\sum_{j\ge1}E_j\longrightarrow0
$$
且保持实际 $V_Q/K_Q/u_f$。它尚未给 (5.5) 所需的
$$
x_m\sum_{j\ge3x_m/2}E_j\longrightarrow0.
$$
因此，仅靠无速率 $\epsilon_m\to0$ 不能宣称 canonical 全深修复小。

反过来，(5.5) 也没有证明原实际 $a_m$ 不满足这一更强能量条件。它不排更优的同源 full-kernel 最小化，不排与全部 primitive/零源联合的 Schur 抵消，也不排原 same-$w$ 两费预算。定理 3.1 的自由第一列说明改选一条公共真空塔仍不能免费获得全高度常数；真正后继须保实际源能量，或保完整源依赖的最小化。
