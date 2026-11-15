# R766 — 原主部像上的 normal 泛函、实际单位与指定小障碍

日期：2026-11-15。**状态：以下完整原来源的下降、实际单位构造和有限判据已证明；指定小障碍的取值仍未判定。**

继续 R765 的同一个原 cube 和条件 $k<r_F$。
选定第三行的 normal 泛函确实下降到 R750 的真实主部像
$\mathcal V_{E'}$。
但这个像不能为零：原低列直接给一个该泛函取单位的主部。
真正的剩余条件是同一主部还要满足完整高接触。

本篇把这两个要求放到一个确定的小矩阵；
给出实际单位主部的完整高尾，并给其失败时真正杀全部原 $\mathcal W_D$ 的左行。
没有将普通主部像的满射误作高接触主部像的满射，也没有删除其它 normal 行和同一个 $R$。

## 1. 保持原窗口和所有规范

保 R750、R755、R765 的同一来源：
$$
P^{\rm fact}=qt^rF^3,\quad q=d^{-C_D}Q,\quad d=1+8t,
$$
$$
p=6s-1>101,\quad f_D<p,\quad
1\le\ell\le r\le13<h,\quad
0\le k=2h+r-s<\ell,\quad k<r_F.
\tag{1}
$$
$r_F$ 是 R765 由完整 Gauss 商基计算的准确最低 $t$ 阶。
特别 $k<r$。仍令
$$
N_0=s-13,\qquad T=N_0-r=2h-k-13,\qquad
\mathcal N=\mathcal O_C(C).
$$
保原
$$
M=c_*U_0w^{13}J,\quad
\eta_0=t^hu,\quad t^s=p\epsilon b_s,\quad
e=(\mathcal EF)|_C,\quad q_0=q|_C.
$$
原第三单位行系数为
$$
\boxed{
c_k=3a\,b_s(0)q_0(0)e(0)^3u(0)^2\tau_0^k\ne0,
\quad \tau_0=(t/w)(0).
}
\tag{2}
$$
所有来源、分支、$q_0$ 和 $c_*U_0$ 继续为原固定对象。

## 2. 同一个低 r 右逆和实际主部像

R750 已给真实整低值右逆
$$
\boxed{
\iota_r(f)=
Y^2q_2(t)\,
\pi_r^t\!\left(\frac{f}{\psi^2q_2}\right),
\qquad
q_2=(t-1)/d,\qquad e_3=13.
}
\tag{3}
$$
这里在模 $p$ 公式中使用 $\psi$，整来源使用其同一整 Hensel 提升。
$0\le j<r\le13$ 的全部 $Y^2q_2t^j$ 都是真原列。
$\pi_r^t$ 只截取这个系数多项式；整个来源列及其高尾仍保留。

令
$$
R^{(r)}=R-\iota_r(\pi_r^t(R|_C)).
$$
则原有限自由来源在低值列与其真实核之间整分裂。
对 $R^{(r)}$ 定义
$$
u_R=\frac{R^{(r)}|_C}{q_0t^r}.
$$
按 R750 的完整全局除子
$$
\operatorname{div}(P^{\rm fact})=3C+E,\qquad
E|_C=rP+E',\quad P\notin E',
$$
有同一个实际空间
$$
\mathcal U_D=\{u_R:R\in\overline{\mathcal W}_D\}
\subset H^0(C,\mathcal N^3(E')).
$$
并且准确有
$$
\boxed{
0\longrightarrow H^0(C,\mathcal N^3)
\longrightarrow\mathcal U_D
\xrightarrow{\operatorname{pp}_{E'}}
\mathcal V_{E'}\longrightarrow0.
}
\tag{4}
$$
$\mathcal V_{E'}$ 始终是全部原列的实际主部像；
$E'$ 的奇点、非约化部分和全十九角均按原对象保留。

## 3. 选定 normal 行准确下降

在原目标中，记
$$
\mathcal C_k(y)=
[w^{13+k}\epsilon^2](c_*U_0)^{-1}y.
\tag{5}
$$
因此对每条原来源，
$$
\mathcal C_k(\bar M R)=
[w^k]\frac{a^2}{2}(\mathcal E^2R)(t(w),g(w)).
\tag{6}
$$
前两块越过 $w^s$ 的 carry 另含 $p$，不能在 (6) 的模 $p$ 读取中提供额外项。

R765 的零角门说明：
若 $R|_C=0$，则 $R$ 在原格中 $F$-整除，全部 Euler 值包含 $t^{r_F}$。
所以 (6) 在两个具有同一 restriction 的来源上取值相同。

于是可先定义
$$
\widetilde d_k(u_R)=\mathcal C_k(\bar M R^{(r)}).
\tag{7}
$$
这是 $\mathcal U_D$ 上的真线性泛函，与 $R^{(r)}$ 的代表无关。
它还杀掉 (4) 的整个 $H^0(C,\mathcal N^3)$：
每个这种截面都有实际 $qt^rH$、$H\in\mathcal H_3$ 作代表；
它的所有 Euler 值都包含 $t^r$，而 $k<r$。
不同代表的差又由 $k<r_F$ 杀掉。

因此有唯一泛函
$$
\boxed{
d_k:\mathcal V_{E'}\longrightarrow k,\qquad
\widetilde d_k=d_k\circ\operatorname{pp}_{E'}.
}
\tag{8}
$$
$q_0t^r$ 是 (7) 的同一个全局规范。
$e^3$ 不被吸收入一个任意 frame；它仍准确留在原 forcing 常数 (2) 中。

## 4. 原低列给 d_k 的明确单位值

这里不只给维数判断，而是给完整来源及其高尾。

### k=0

取
$$
R_*=
1-Y^2q_2\,
\pi_r^t\!\left(\frac1{\psi^2q_2}\right)
=1-\iota_r(1).
\tag{9}
$$
它是整个原 $\mathcal W_D^{(r)}$ 的真实元素，
$D\ge3$、$n=0,2$ 的原帽已经足够。
因为其普通支上值消到 $r$，而后项的 charge 恰为2，
$$
\boxed{\widetilde d_0(u_*)=-2a^2\in k^\times.}
\tag{10}
$$
完整归一值是
$$
\boxed{
u_*=
\frac{1-\psi^2q_2\,\pi_r^t(1/(\psi^2q_2))}
{q_0t^r}.
}
\tag{11}
$$
不能把 (11) 的分子仅换成0；其 $r$ 阶以后的真实高尾正是下一节的输入。

### 1≤k<r

原 $n=3$ 具有
$$
q_3=t\,h_7q_2,\quad h_7=7+4t+16t^2,\qquad e_4=14.
$$
因此
$$
R_{\rm seed}=Y^3q_3t^{k-1}=Y^3q_2h_7t^k
$$
是原实际列；$k-1\le11<14$。
取同一个低值右逆
$$
\boxed{
R_*=
Y^3q_2h_7t^k
-Y^2q_2\,\pi_r^t(\psi h_7t^k).
}
\tag{12}
$$
所有 $n=2$ 系数仍有次数 $<r\le13$，故不超过原帽。
普通支上值消到 $r$，而两个 charge 分别为3和2。
所以
$$
\boxed{
\widetilde d_k(u_*)
=-\frac{35a^2}{2}\tau_0^k\in k^\times.
}
\tag{13}
$$
这里 $(3^2-2^2)h_7(0)q_2(0)=5\cdot7\cdot(-1)=-35$。
完整归一高尾为
$$
\boxed{
u_*=
\frac{\psi^2q_2\{\psi h_7t^k-\pi_r^t(\psi h_7t^k)\}}
{q_0t^r}.
}
\tag{14}
$$

用 (10) 或 (13) 的真实单位将 $u_*$、$R_*$ 同除，以下记其主部为 $v_k$。
于是
$$
\boxed{v_k\in\mathcal V_{E'},\qquad d_k(v_k)=1.}
\tag{15}
$$
这没有预付 $u_*$ 的 $T$ 阶消失。

**直接后果。** 在本篇实际范围内，
$$
\boxed{\mathcal V_{E'}\ne0,\qquad d_k\text{ 满射}.}
\tag{16}
$$
R750 增补已付 $\dim\mathcal V_{E'}=e'-\delta_C$，
故还必有 $e'-\delta_C\ge1$。
因此在 $k<r_F$ 的同一范围内，
不能把 $\mathcal V_{E'}=0$ 当成一个可命中的完整非零门：
(9)–(15) 已由原真实列排除了这个情形。

## 5. 唯一剩余高接触小矩阵

置原全局三倍值的 jet 余核
$$
\mathcal Q_T=
k[[t]]/t^T\,/
\operatorname{ev}_T H^0(C,\mathcal N^3).
$$
对一个真实 $v\in\mathcal V_{E'}$，任取其实际原像 $u\in\mathcal U_D$，定义
$$
\boxed{
\mathcal O_T:\mathcal V_{E'}\longrightarrow\mathcal Q_T,
\qquad
\mathcal O_T(v)=[\,\pi_Tu\,].
}
\tag{17}
$$
两个原像的差是 (4) 的 $H^0(C,\mathcal N^3)$，所以 (17) 定义良好。

R750 已付的同源返回给准确解释：
$$
\boxed{
\ker\mathcal O_T
=
\operatorname{pp}_{E'}\!\left(
\mathcal U_D\cap H^0(C,\mathcal N^3(E')(-TP))
\right).
}
\tag{18}
$$
反向是实际构造：若 (17) 为零，减去一个由 $\mathcal H_3$ 返回的三倍截面即可使同一个 $u$ 消到 $T$。
这一步保持 (8)，因为 $d_k$ 杀全部这些三倍截面。

因此存在原 $R$ 同时满足
$$
R|_C=0\bmod t^{N_0},
\qquad
\mathcal C_k(\bar M R)=-c_k
\tag{19}
$$
当且仅当
$$
\boxed{
\exists v\in\ker\mathcal O_T:\quad d_k(v)=-c_k.
}
\tag{20}
$$
从 (18) 回来的来源确实在原 $\mathcal W_D^{(r)}$；
它不是环境主部的任意提升。

因 $c_k\ne0$，有限维线性代数给四个准确等价条件：
$$
\boxed{
\begin{aligned}
(19)\text{ 可解}
&\Longleftrightarrow d_k|_{\ker\mathcal O_T}\ne0\\
&\Longleftrightarrow d_k\notin\operatorname{im}(\mathcal O_T^*)\\
&\Longleftrightarrow
\mathcal O_T(v_k)\in\mathcal O_T(\ker d_k).
\end{aligned}}
\tag{21}
$$
最后一条按 $v=-c_kv_k+v_0$、$v_0\in\ker d_k$ 直接得到；
所有比例常数均为原实际单位。

选以 (15) 的 $v_k$ 为第一列的真实主部基，
其余列取 $\ker d_k$ 的实际基，
则最后一个成员性问题就是
$$
\boxed{\mathcal O_T(v_k)\ \stackrel{?}{\in}\ 
\operatorname{span}\{\mathcal O_T(v_j):d_k(v_j)=0\}.}
\tag{22}
$$
第一列由 (11) 或 (14) 的完整高尾准确给出，
其余列从原 canonical 全列经 (3) 后生成，再作原主部像的基消元。
没有将 $e'$ 个环境方向补成来源。

特别 $\mathcal Q_T=0$ 时，(19) 确实总可解；
这只支付值段加选定 normal 行。
相反，若实际 $\mathcal O_T$ 单射，则 (19) 无解。
两条都是对同一个已给矩阵的条件性结论，没有预付其中任一条件。

## 6. 失败时得到真正的全 M 单位左证书

由 R750，准确有
$$
\mathcal Q_T^*\simeq
\mathcal D_T=H^0(C,\omega_C\mathcal N^{-3}(TP)),
$$
配对为 $\langle[f],\omega\rangle=\operatorname{Res}_P(f\omega)$。
若 (19) 不可解，即 $d_k\in\operatorname{im}\mathcal O_T^*$，
取一个实际
$$
\boxed{
\omega\in\mathcal D_T,\qquad
\operatorname{Res}_P(u\omega)=d_k(\operatorname{pp}_{E'}u)
\quad\text{对所有 }u\in\mathcal U_D.
}
\tag{23}
$$
(23) 只是一组 (22) 的对偶有限方程，未假设其有解。
若用 R750 的其它点留数写法，准确为
$-\mathfrak r(v,\omega)=d_k(v)$；
奇点仍取原 Rosenlicht 分支和。

对整个原目标定义低值修正后的 normal 行
$$
\widehat{\mathcal C}_k(y)
=
\mathcal C_k(y)
-\mathcal C_k\!\left(
\bar M\,\iota_r(\pi_r\mathscr V_\eta y)
\right).
\tag{24}
$$
这里的 $\iota_r$ 是 (3) 的整实际来源右逆；
其第三块高尾也留在 (24) 中。
再用 R750 的同一
$$
\mathfrak n_r(f)=
\frac{f-\iota_r(\pi_rf)|_C}{q_0t^r}\pmod{t^T}.
$$
则
$$
\boxed{
\Lambda_\omega(y)=
\widehat{\mathcal C}_k(y)
-\operatorname{Res}_P\!\left[
\mathfrak n_r(\mathscr V_\eta y)\,\omega
\right]
}
\tag{25}
$$
是真正杀全部 $\bar M\overline{\mathcal W}_D$ 的行。

证明是：对任意原 $R$，(24) 变为
$d_k(\operatorname{pp}_{E'}u_R)$，第二项按 (23) 完全相同。
所以全来源逐列为零，不是只杀 $F$-整除列或 $qt^r\mathcal H_3$。

对原完整首 forcing $\beta=M(P^{\rm fact})/p\bmod p$，
R755 给 $\mathscr V_\eta\beta=0$，故 (24) 的低修正及 (25) 的值项均为零。
于是
$$
\boxed{\Lambda_\omega(\beta)=c_k\in k^\times.}
\tag{26}
$$
所以一旦实际小矩阵证实 (23)，(25)–(26) 就给原 cube 在**完整**原 $M$ 余核中的非零首 Bockstein，排除任何同来源 $p^2$ 提升。

本篇未证明 (23) 总有解。
(25) 把那一个确切缺项与最终全矩阵证书接上，未用维数或单个子格单位代替它。

## 7. 其余 normal 与下一位仍用同一个 R

(21) 只判断完整值段与原第三块第 $13+k$ 行。
即使它可解，也还须在同一个实际来源纤维中满足：
前两块的剩余 normal 行、第三块的其它行、两条完整十三行 carry，
以及原模 $p^3$ 的下一位。

所有这些行仍来自同一个 $R$；
不能先以 (18) 选择一个值解，再任意填写其 normal 数据。
若用整数低值分裂改变 $R$ 一个 $p$ 倍来源，
其差仍按 R750 进入同一个 $p^2$ 修正。

本篇的新事实是 (8) 的真实下降、(9)–(15) 的原列单位、
以及 (22) 与 (25) 的准确小矩阵/全左行对接。
当前尚未判定指定 (22) 的成员性，原非 cube 的实际 $v_F$ 留数也继续保留。

依赖：
[R750](R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R750 全来源增补](../notes/2026-11-15-r750-whole-divisible-source-and-primitive-carry-filter.md)；
[R755](R755-whole-original-cube-carry-filter-and-specified-value-class-invariance.md)；
[R765](R765-original-zero-angle-and-unavoidable-nonfactor-first-correction.md)。
