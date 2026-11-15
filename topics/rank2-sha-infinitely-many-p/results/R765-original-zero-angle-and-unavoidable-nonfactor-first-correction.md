# R765 — 原零角与不可避免的非因子型首次修正

日期：2026-11-15。**状态：下述整个原来源上的必要条件已证明；完整 forcing 非零仍未证明。**

保持 R750、R755 的原 cube、整数帽及全部目标。本篇不只排除固定 $qt^r\mathcal H_3$ 内的修正：在显示的零角门下，整个原 $\mathcal W_D$ 中任何 $F$-整除修正都不可能完成首次提升。任何可行的完整修正必须给出一条非零的全局 restriction，在原支上消失至少 $s-13$ 阶，并满足一个确定的、非零右端的 normal 泛函。

该泛函定义于原实际 restriction 像；它不是杀整个 $\mathcal W_D$ 的左行。

## 1. 原范围

保持同一个
$$
P^{\rm fact}=q(t,Y)t^rF(t,Y)^3\in\mathcal W_D,\qquad
q=d^{-C_D}Q,\qquad Q(0,1)\ne0,
$$
$$
p=6s-1>101,\quad f_D<p,\quad
1\le\ell\le r\le13<h,\quad
k=2h+r-s,\quad0\le k<\ell.
\tag{1}
$$
$F$ 是已付十九角整提升，约化不可约，
$F(0,1)=0$、$F_Y(0,1)\ne0$。仍用
$$
d=1+8t,\quad
\eta=\eta_0+p\xi,\quad
\eta_0=t^hu,\quad e=(\mathcal EF)|_C,\quad
\mathcal E=Y\partial_Y,
$$
$$
t^s=p\epsilon b_s,\qquad b_s=(t/w)^s,\qquad
M=c_*U_0w^{13}J.
\tag{2}
$$
$u,e,q_0=q|_C,b_s$ 在 $P=(0,1)$ 都是单位。
所有 mod $p$ 来源仍来自同一个原有限自由格。

置
$$
d_0=r-k=s-2h\in[1,13],\qquad
N_0=s-13=2h+d_0-13\le2h.
\tag{3}
$$
沿原非垂直支 $Y=\psi(t)$ 读取 restriction。
$C$、$\mathcal B_D$ 和所有十九角均不改变。

## 2. 整个 F-整除空间的真实最低 t 阶

令
$$
\mathcal F_D
=\{R\in\overline{\mathcal W}_D:F\mid d^{C_D}R\},
\qquad m=-v_0(F)\ge1.
\tag{4}
$$
这里 $v_0(\sum f_iY^i)=\min_i(4\operatorname{ord}_0f_i-i)$ 是原零角。
因 $F(0,Y)$ 非零且在1有根，$m\ge1$，但不把 $m$ 换成 $\deg_YF$ 或 $\deg F(0,Y)$。

若 $R=d^{-C_D}FH$ 属于 (4)，原完整角界给
$$
v_0(H)\ge m-2.
$$
将 $H=\sum_i h_i(t)Y^i$ 按原 charge 展开，准确有
$$
\operatorname{ord}_0 h_i
\ge \max\left(0,\left\lceil\frac{i+m-2}{4}\right\rceil\right).
\tag{5}
$$
所以每一个真实 $R\in\mathcal F_D$ 都包含全局因子
$$
t^{\,r_F^{\rm low}},\qquad
\boxed{
r_F^{\rm low}=\max\left(0,\left\lceil\frac{m-2}{4}\right\rceil\right).
}
\tag{6}
$$
原 $d$ 在0是单位，不能改变这个结论。

如需准确最小阶，用 R750 全来源增补的完整商基，而不只用 (6)。
具体令
$$
\lambda_\alpha=-2-v_\alpha(F)
\quad(\alpha=0,h_{7,1},h_{7,2}),\quad
\lambda_1=-1-v_1(F),
$$
$$
\lambda_d=2C_D-v_d(F),\qquad
\lambda_\infty=-2C_D-8-v_\infty(F).
$$
对 $0\le i\le D-\deg_YF$，令
$$
a_i(t)=
t^{m_{0,i}}
\prod_{\alpha=h_{7,1},h_{7,2}}(t-\alpha)^{m_{\alpha,i}}
(t-1)^{m_{1,i}}d^{m_{d,i}},
$$
$$
m_{\alpha,i}=\max(0,\lceil(i+\lambda_\alpha)/4\rceil),\quad
m_{1,i}=\max(0,\lceil(i+\lambda_1)/3\rceil),\quad
m_{d,i}=\max(0,\lceil(\lambda_d-i)/2\rceil),
$$
$$
n_i=\left\lfloor\frac{9i-\lambda_\infty}{2}\right\rfloor-\deg a_i .
\tag{7}
$$
全部真实商列恰为 $Y^ia_i(t)t^j$，$0\le j\le n_i$，负帽组省去。设
$$
\boxed{r_F=\min_{n_i\ge0}m_{0,i}.}
\tag{8}
$$
原 $P^{\rm fact}$ 保该集合非空。
所有非零固定角因子在0为单位，而 $\operatorname{ord}_tF=0$，
故 (8) 正是 (4) 中非零来源的最小全局 $t$ 因子阶。
特别 $r_F\ge r_F^{\rm low}$。

(7) 使用原完整 Gauss 双向识别，所以结论覆盖全部 $F$-整除原列及中间十九角，不是选取一个方便的子格。

## 3. 原第三单位行排除整个 F-整除修正

**定理 1。** 若
$$
\boxed{k<r_F,}
\tag{9}
$$
则任何实际首次修正
$$
M(P^{\rm fact}+pR)\in p^2,\qquad R\in\mathcal W_D
\tag{10}
$$
都满足
$$
\boxed{\bar R|_C\ne0.}
\tag{11}
$$
一个只用原零角数的充分门是
$$
k<\max(0,\lceil(m-2)/4\rceil).
\tag{12}
$$
特别当 $\ell=1,\ k=0,\ m\ge3$ 时，(11) 自动成立。

**证明。** 只逆整个真实整单位 $c_*U_0$。
R755 的完整首 Bockstein 对原 $P^{\rm fact}$ 给第三块
$$
\boxed{
\left[(c_*U_0)^{-1}M(P^{\rm fact})/p\right]^{(2)}
=3a\,w^{13}b_s q_0e^3u^2t^k
\pmod{w^{\ell+13}}.
}
\tag{13}
$$
这里 native $\xi$ 项由原 $t^r$ 因子及 $r\ge\ell$ 截掉；
第四 normal 项从 $h+k>\ell$ 起。
只有在这个原 cube 上才能这样消项；没有删除 R755 一般 $F^3H$ 的活 $H_1$ 项。

设 $\tau_0=(t/w)(0)\in k^\times$。
因 $k<\ell$，原第三块第 $13+k$ 行仍可读，其系数准确为
$$
\boxed{
c_k=3a\,b_s(0)q_0(0)e(0)^3u(0)^2\tau_0^k\ne0.
}
\tag{14}
$$
这是模 $p$ 的单位。

若 $\bar R\in\mathcal F_D$，由 (8) 它含全局 $t^{r_F}$。
$\mathcal E$、原 $Y=g(w)e_2(a\epsilon)$ 代入以及 $t=t(w)$ 都保这个前缀。
所以
$$
\left[w^{13+k}\epsilon^2\right]\,
w^{13}\bar J(\bar R)=0
\qquad(k<r_F).
\tag{15}
$$
前两块乘 $w^{13}$ 的越界 carry 含额外 $p$，
在这个模 $p$ 式中不能贡献 (15)；
第三块本身的最低阶至少 $13+r_F$。

(10) 却要求
$$
w^{13}\bar J(\bar R)=
-\overline{(c_*U_0)^{-1}M(P^{\rm fact})/p}.
\tag{16}
$$
(14)、(15) 矛盾。
因 $C$ 是由同一不可约 $F$ 定义的整曲线，
$\bar R|_C=0$ 与 $\bar R\in\mathcal F_D$ 等价，证明 (11)。

证明没有对 $w^{13}$ 作目标中的非整逆，也没有换掉原 $P_{134}$、共同 charge 或两条十三行。式 (15) 只对完整 $F$-整除原空间成立，不对任意 $\bar R$ 成立。证毕。

## 4. 被迫的非零 restriction 必须有完整 N0 接触

对任意完整原来源，R750 的同一值投影满足
$$
\mathscr V_\eta(w^{13}\bar JR)
=R|_C\pmod{t^{N_0}},
\tag{17}
$$
其中先在前两块的已允许行上除显示的 $w^{13}$，再取
$\widehat y_0-\eta_0\widehat y_1/a$。
这是同一个 $R$ 的两个实际 Euler 值；
$\eta_0^2$ 从 $2h\ge N_0$ 起才可删。

另一方面，原 cube 由 R755 已有
$$
\mathscr V_\eta\beta_M(P^{\rm fact})=0.
\tag{18}
$$
直接看其式 (18)，实际首阶是
$2h-d_0+r=2h+k\ge N_0$，同样得到 (18)。

将 (17)、(18) 用于同一个 (16)，得

**定理 2。** 在 (9) 下，任何 (10) 中的完整首次修正都给
$$
\boxed{
0\ne \bar R|_C
\in \operatorname{im}\!\left[
H^0(X,\mathcal O_X(\mathcal B_D))
\longrightarrow H^0(C,\mathcal O_C(\mathcal B_D))
\right]
\cap
H^0(C,\mathcal O_C(\mathcal B_D)(-N_0P)).
}
\tag{19}
$$
特别
$$
\operatorname{ord}_P(\bar R|_C)\ge s-13.
$$
(19) 保整个实际 restriction 像，不能换成所有具有这个高零阶的环境截面。

## 5. 一个确定的 intrinsic normal 泛函

令上一节的整个实际 restriction 像为 $\mathcal U_D^{\rm raw}$。
在 (9) 下，下面的表达与原来源代表无关：
$$
\boxed{
\nu_k:\mathcal U_D^{\rm raw}\longrightarrow k,\qquad
\nu_k(R|_C)
=
[w^k]\frac{a^2}{2}(\mathcal E^2R)(t(w),g(w)).
}
\tag{20}
$$
确实，两个代表的差在 $\mathcal F_D$，由 (8)、(9) 其所有 Euler 值都从 $w^{r_F}$ 起。故 (20) 的差为零。
因为 $k<\ell<h$，该系数也可以在同一 $\psi$ 支上读取；
不需把任何高 normal jet 自由指定。

原修正的 restriction 除 (19) 外还必须满足
$$
\boxed{\nu_k(\bar R|_C)=-c_k\ne0.}
\tag{21}
$$
这就是 (13) 的同一第三行。它把“必须用非 $F$ 列”落实为实际高接触 restriction 空间中的一条确定仿射条件。

(20) 不是全矩阵左核：它一般不杀 $\mathcal U_D^{\rm raw}$，更不能在尚未计算它于 (19) 空间上的像时宣称 (21) 无解。其余前两块、其它第三行及两条十三行仍由同一个 $R$ 联立；升到原模 $p^3$ 时，还必须保 R593/R651 的完整 carry 延拓与同一个第二修正。

本篇没有证明 (19) 中所有截面被 $\nu_k$ 杀掉，
也没有证明指定完整 forcing 非零。
真正剩下的是原全来源的这个高接触像、全部 normal 条件与实际 $v_F$ 的联合，而不是一个还可由 $F$-整除来源任意选择的局部修正。

依赖：
[R750](R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R750 全来源增补](../notes/2026-11-15-r750-whole-divisible-source-and-primitive-carry-filter.md)；
[R755](R755-whole-original-cube-carry-filter-and-specified-value-class-invariance.md)；
[R449](R449-relative-second-cokernel-and-complete-carry-exact-sequences.md)。
