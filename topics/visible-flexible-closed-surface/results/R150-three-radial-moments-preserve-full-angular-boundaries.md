# R150：三个径向矩直接保留完整角边界

**状态：已证明。** R148 的两矩构造可按准确无限 Fourier 函数定义，但有限物理角截断的实际原型丢失了明显的中央边界信息。本结论直接对完整角函数作用：只解一个与角度无关的 $3\times3$ 正 Gram 系统，无需截断边界。非线性 Gauss 与实际位置几何仍须另行求解。

## 1. 准确的三个矩恒等式

沿用 R148 的固定物理 $(s,u)$、正函数 $a\in C^2[C,L]$、$J(s)=\int_s^L a^{-2}$、$I=J(C)$ 和 $c=a'/a$。完整实周期边界满足必要条件
$$
\int_0^{2\pi}(a_L^2m_L-a_C^2m_C)\,du=0. \tag{1}
$$
取任一周期原函数 $A(u)$ 使
$$
A_u=a_L^2m_L-a_C^2m_C,
$$
并记
$$
N(u)=a_Ln_L-a_Cn_C-a_C^2I(m_C)_u. \tag{2}
$$
从左端解完整 Codazzi，准确得到
$$
m(s,u)=\frac{a_C^2m_C(u)+\partial_u\int_C^s a(t)l(t,u)\,dt}{a(s)^2},
$$
$$
n(s,u)=\frac{a_Cn_C(u)+\partial_u\int_C^s m(r,u)\,dr+
\int_C^s a'(t)l(t,u)\,dt}{a(s)}. \tag{3}
$$
交换积分后，右端条件等价于
$$
\partial_u\int_C^L a l=A_u,
\qquad
\partial_u^2\int_C^L aJ l+\int_C^L a'l=N. \tag{4}
$$
因此下列三个完整函数矩是一个明确的充分选择：
$$
\int_C^L a l=A,\qquad \int_C^L aJ l=0,
\qquad \int_C^L a'l=N. \tag{5}
$$
第一矩的常数可任取；第二矩选零是构造选择，不是原方程的必要条件。它们不修改任一指定边界。

## 2. 一个正 Gram 矩阵即可解全部角度

取非负 $b\in C^1[C,L]$，在两端开放邻域为零。令
$$
f(s)=(1,J(s),c(s))^T,\quad \mu(s)=a(s)b(s),\quad
H=\int_C^L\mu(s)f(s)f(s)^T\,ds. \tag{6}
$$
假定在某个 $b>0$ 的开放区间中
$$
h(s)=a(s)a''(s)-(a'(s))^2
$$
不是常函数。则 $H$ 严格正定。证明：若 $v^THv=0$，则连续函数 $v_0+v_1J+v_2c$ 在该区间恒为零。当 $v_2=0$，由 $J'=-a^{-2}\ne0$ 得 $v_1=v_0=0$；当 $v_2\ne0$，求导得 $c'$ 是 $J'$ 的常数倍，故 $a^2c'=h$ 为常数，矛盾。因此只有 $v=0$ 给零二次型。

给任意具有正确两端 $l$ 迹的完整 baseline $l^b(s,u)$，定义
$$
T(u)=\begin{pmatrix}A(u)\\0\\N(u)\end{pmatrix}
-\int_C^L a(s)f(s)l^b(s,u)\,ds,
\qquad v(u)=H^{-1}T(u),
$$
$$
l(s,u)=l^b(s,u)+b(s)f(s)^Tv(u). \tag{7}
$$
由 (6)，三个矩的增量正好是 $Hv=T$，所以 (5) 成立，(3) 满足两端全部 $n,m$ 迹。$b$ 的端点消失保证两端 $l$ 迹及 baseline 的已有开放 collar 也保持。这里求逆的唯一矩阵为明确正的 $H$，没有未知 $n$ 的分母，也没有有限角采样条件。

## 3. 当前受保护前缀确实给非退化

当前 `peak-spacer34/cyl032` 的准确中央柱结束于 $C_0=.32$。其后的第一个长度 $.00625$ 的相位 Hermite 段具有起点 $p=p'=p''=0$，但终点 $p=2.5666201386442822\times10^{-8}\ne0$；半径 bump 的支撑从 $.34$ 之后才开始。因此这整段相位与 $a$ 不随当前七个设计参数改变。

在该段内部 $p$ 是非零多项式，$a'=\sin p$、$a''=\cos p\,p'$，而 $a>0$。设 $p$ 在起点的第一个非零 Taylor 项为 $\gamma(s-C_0)^j$，其中 $j\ge3$、$\gamma\ne0$。则
$$
h(s)=a(C_0)j\gamma(s-C_0)^{j-1}
+O((s-C_0)^j),
$$
故 $h$ 不是常数。它在该 Hermite 段是解析函数，因而也不可能在任意内部开子区间变为常数。选择 $b$ 在这样一个子区间为正即可。$J$ 受到后续半径设计的影响，在该保护段仅改变一个加法常数；(6) 的三个函数的线性独立性不受此影响。因此在整个所选正度量设计域内，$H$ 均严格正定。

这使用真实存在的保护 Hermite 段。当前最终切口之前是 phase bridge，未假设那里存在开放的 $a'=-1$ 平坦段。

## 4. 当前圆柱到平尾只需三个完整角函数

当前 $m_C=l_C=0$。选径向函数 $\chi$，左端为0、右端为1，并取
$$
l^b(s,u)=\chi(s)l_L(u).
$$
记 $d=\int a f\chi$，$e_0=(1,0,0)^T$、$e_2=(0,0,1)^T$。定义三个准确径向系数
$$
\begin{pmatrix}g_A(s)&g_N(s)&g_l(s)\end{pmatrix}
=b(s)f(s)^TH^{-1}\begin{pmatrix}e_0&e_2&-d\end{pmatrix}
+\begin{pmatrix}0&0&\chi(s)\end{pmatrix}. \tag{8}
$$
于是
$$
l(s,u)=g_A(s)A(u)+g_N(s)N(u)+g_l(s)l_L(u),
\quad N=a_Ln_L-a_Cn_C. \tag{9}
$$
设 $\Phi=(A,N,l_L)^T$，并逐分量定义
$$
M(s)=a(s)^{-2}\int_C^s a(t)g(t)\,dt,
$$
$$
R(s)=a(s)^{-1}\int_C^s a'(t)g(t)\,dt,
\qquad S(s)=a(s)^{-1}\int_C^s M(t)\,dt.
$$
则完整场直接为
$$
l=g\Phi,\quad m=M\Phi_u,\quad
n=\frac{a_C}{a}n_C+R\Phi+S\Phi_{uu}. \tag{10}
$$
所有角函数按其原定义求值；这里没有 Fourier 近似。需要注意，$\Phi_{uu}$ 是原函数的真实材料角二阶导数，不能把 seed-normal 的导数冒称为材料导数。

### 平尾原函数也有闭式

当前准确尾的切口半径为 $r=a_L$，$y=r\sin u$，
$$
n_L=\kappa(y)\cos^2u,\quad m_L=-\kappa(y)\sin u\cos u,
\quad l_L=\kappa(y)\sin^2u.
$$
因此可以选
$$
A(u)=-\int_0^{r\sin u}t\kappa(t)\,dt, \tag{11}
$$
因为 $A_u=r^2m_L$。$\kappa$ 为偶函数，所以 (11) 是偶的 $\pi$ 周期函数。

对 R132 的 degree-$K$ Bernstein 尾，设平坦半径 $r_f$、宽度 $w$、控制 $p_i$，
$q=\operatorname{clip}((|y|-r_f)/w,0,1)$，记
$$
\omega_i=630\binom Ki B(i+5,K-i+5).
$$
用正则化不完全 Beta 多项式 $I_q$，准确有
$$
\int_0^y t\kappa(t)\,dt=
\sum_{i=0}^Kp_i\omega_i\left[
r_f I_q(i+5,K-i+5)
+w\frac{i+5}{K+10}I_q(i+6,K-i+5)\right]. \tag{12}
$$
证明只需把 $t=r_f+wq$ 代入 $\kappa\,dt=630q^4(1-q)^4\sum p_iB_i^K(q)\,dq$；被积函数 $t\kappa(t)$ 为奇函数，故从0到负 $y$ 的积分与正 $|y|$ 相同。所有参数均为整数，(12) 也可当作准确分段多项式定义。

## 5. 对称、正则性与参数列

若边界为 D2，则 $A,N,l_L$ 为偶的 $\pi$ 周期函数，故 (10) 中 $n,l$ 偶、$m$ 奇。若这些准确角函数为 $C^3$，则 (10) 至少给角向 $C^1$ 的三场；这是该显式构造的充分输入正则性，不是给最终曲面增设更高阶验收门。baseline、更一般边界和参数族也可在相应分片或弱导数函数空间处理，但必须说明采用的定义。

固定物理端点和 $b,\chi$ 后，参数方向导数满足
$$
\dot H=\int(\dot a\,bff^T+ab\dot f f^T+ab f\dot f^T),
\qquad \dot v=H^{-1}(\dot T-\dot H v),
$$
其中 $\dot J=-2\int_s^L\dot a/a^3$、$\dot c=(\dot a'-c\dot a)/a$。其余径向系数按积分及乘积法则求导。

在当前中央与切口半径受保护、$m_C=0$ 的设计中，$A,N,l_L$ 对中央和尾控制是仿射或线性的；$H,g,M,R,S$ 只依赖物理半径参数。故完整 lifting 的中央/尾列是明确的完整角函数列，不需差分改变物理度量。把该 lifting 接到旧 raw 接口时必须相应改变中央边界 correction 的定义；不可把已经包含在 lifting 中的中央控制再加一次。

## 6. 不从 Codazzi 推出 Gauss 或位置

由 (3) 或 (10) 所得的准确 lifting 满足两条完整 Codazzi。因此在任何真实角坐标 $u=U(s,\xi)$ 中，只要把全部链式项保留，其已知 lifting forcing 仍准确为零。但有限 correction 的角导数与移动图系数仍可能产生高模，不能把 lifting 的性质转移给任意 correction。

尚须实际求解 $nl-m^2=-a''/a$，支付有限径向积分误差、真实二 jet 接合、位置和标架 monodromy、全域 metric、曲率与 reach、强比例、同 $g$ 加密以及完整网格。$H$ 正定也不是曲率或嵌入保证。数值实现 (8)–(12) 时应分别记录积分误差与完整边界值的消费误差，不再使用 R148 有限原型中明显不足的角截断。


## 7. 实际简单 baseline 的失败原型

`fd2d_full_function_moment_lifting_probe.py` 已按 coast09 的同一38参数和物理度量实际消费 (8)–(12)，直接使用完整角函数及其材料角导数，未作 Fourier 或角投影。$3\times3$ Gram 的有限特征值为约 $.027914,.351926,1.647715$，条件数约59；六个材料角的真导数差分 scaled error 小于 $4.35\times10^{-9}$。16点径向规则控制由独立24点规则消费后，采样完整边界缺陷约 $1.756\times10^{-7}$。

**这个简单 baseline 不是合格初猜。** 同一次真实消费得到格内 Gauss 残差约 $21660.36$，形式主曲率约 $1216.40$，$n$ 在内部变成很大的负值。公式 (10) 中 $S\Phi_{uu}$ 允许完整中央角函数的二阶导数被放大；准确线性 Codazzi 和完整端点匹配并不控制该效应。不能把这个实际失败隐藏在准确构造定理后面，也不应继续为此坏场积分实际位置或制作几何证书。

该族仍可用不同的实际 baseline 或不同矩选择研究，但每个候选都必须重新实付其完整缺陷。当前主线保持已有证据的自然角图与明确 coast correction reset。完整源、控制、实际报告和真退出记录在 `notes/2026-11-12-fd2d-full-function-moment-lifting01-closed-manifest.json`。
