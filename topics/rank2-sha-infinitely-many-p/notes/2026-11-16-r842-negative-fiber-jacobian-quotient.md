# R842 续注：负水平实际行的 Jacobian 纤维商与精确剩余长度

日期：2026-11-16。**状态：下述原 $F_t\widetilde q$ 判据、实际商长度及最高系数已证明；该行在 $\mathscr W_T$ 上的限制，以及它与其它边界组成的指定 $[b_0]$，仍未判定。**

接
[全部非固定负水平残数的实际纤维商](2026-11-16-r842-complete-negative-fiber-trace-and-original-source.md)。
以下不增加任何来源列，不改 $F,q,G$，也不把未加前缀的来源满射用于受限核。

## 1. 原纤维与要判定的行

保持原 $r=2$ 来源
$$
R=q\,t^rG,\qquad q=Y\widetilde q,\qquad
G\in\mathcal H_3,\qquad
F(t,0)=\lambda d^cH(t),\quad \deg H\le2.
\tag{1}
$$
取非固定负水平点 $Q=(t_Q,0)$，在原剩余域 $k_Q$ 上置
$$
x=Y,\quad T_0=t-t_Q,\quad
n=\operatorname{ord}_{t_Q}F(t,0)\in\{1,2\},\quad
\ell=\operatorname{ord}_xF(t_Q,x)\le b<p.
$$
前注已付真实 Cartier 纤维
$$
D_Q=V(T_0)\subset C,\qquad
A_Q=\mathcal O_{D_Q}=k_Q[x]/(x^\ell),\qquad
D_Q\subset Z.
\tag{2}
$$
这里只取该底纤维的 $Q$ 局部分量。非有理点先用原可分剩余域，
所有最终行再取剩余域迹。

仍用原
$$
W=t^{r+1-s}(1-t)^{3s},\quad c_s=\frac{3(-1)^s}{17},
\quad D_x=x\partial_x.
$$
前注的全部分支 trace 公式给
$$
\mathfrak b_Q(G)
=-c_st_Q^rW(t_Q)\operatorname{CT}_x
\left[S_Q(x)(D_x+1)^2
\bigl(\widetilde q(t_Q,x)G(t_Q,x)\bigr)\right].
\tag{3}
$$
这里 $S_Q=\sum_i1/T_i'(x)$，$T_i$ 为原 $F$ 的 $T_0$-Weierstrass 多项式的全部根。
式 (3) 已含奇点的全部 conductor 分支；不对各支自由赋值。

定义两个**原多项式**的局部次数
$$
u=\min\{\ell,\operatorname{ord}_xF_t(t_Q,x)\},\qquad
v=\min\{\ell,\operatorname{ord}_x\widetilde q(t_Q,x)\},
$$
$$
\boxed{d_Q=\max\{0,\ell-u-v\}.}
\tag{4}
$$
恒零级数的次数取 $+\infty$。
$F_t$ 和 $\widetilde q$ 在这里都取原固定 $t$、$Y$ 规范。
改变 $F$ 的局部单位框只将 $F_t\bmod F(t_Q,x)$ 乘以单位，
所以 (4) 及以下 annihilator 商不依赖该框。

## 2. 二次 trace 的准确消失阶

**引理。** 若 $u<\ell$，则
$$
\boxed{\operatorname{ord}_xS_Q=u+1-\ell.}
\tag{5}
$$
若 $u=\ell$，则 $S_Q\in xk_Q[[x]]$。

若 $n=1$，Weierstrass 多项式为 $T_0+a_1(x)$，
$F_t(Q)$ 为单位，故 $u=0$。
前注给 $S_Q=-1/a_1'$；
$\operatorname{ord}a_1=\ell<p$，所以 (5) 成立。

现设 $n=2$，写真正的单位分解
$$
F=U(T_0,x)\bigl(T_0^2+a(x)T_0+b(x)\bigr),\qquad U(0,0)\ne0.
\tag{6}
$$
则 $\operatorname{ord}b=\ell$，且
$$
F_t(t_Q,x)=U_T(0,x)b(x)+U(0,x)a(x).
$$
因此
$$
u=\min\{\ell,\operatorname{ord}a\}.
\tag{7}
$$
记两根为 $T_1,T_2$。由于 $T_1+T_2=-a$，
$$
\boxed{
S_Q=\frac{T_1'+T_2'}{T_1'T_2'}
=-\frac{a'}{\operatorname{Norm}(T_0')}.
}
\tag{8}
$$
这个式子与前注的显式分式完全相同：
若 $\Delta=a^2-4b$，
$$
\operatorname{Norm}(T_0')
=-\frac{(b')^2-aa'b'+b(a')^2}{\Delta}.
$$
没有约去可能导致误读的局部零点；(8) 是同一可分总商环中的恒等式。

在每个正规化分支上，原参数次数满足
$$
n_i=\operatorname{ord}x\le2,\qquad
m_i=\operatorname{ord}T_0\le b<p.
$$
故 $m_i/n_i$ 非零，求导首项不失效，
$\operatorname{ord}_xT_i'=m_i/n_i-1$。
按全部驯分歧共轭计根，常数项的 Norm 给
$\sum_i\operatorname{ord}_xT_i=\ell$，于是准确有
$$
\boxed{\operatorname{ord}_x\operatorname{Norm}(T_0')=\ell-2.}
\tag{9}
$$
分裂、非分裂与奇异支均使用此同一计算。

若 $u<\ell$，由 (7) 有 $1\le u<\ell<p$，
所以 $\operatorname{ord}a'=u-1$；
(8)、(9) 给 (5)。
若 $u=\ell$，则 $a\in x^\ell k_Q[[x]]$，
$\operatorname{ord}a'\ge\ell-1$，即使更高项的正特征导数消失也只会提高该阶；
故 (8) 属于 $(x)$。证毕。

## 3. 真 Jacobian 商及最高系数

**定理。** 原行 (3) 因子化为实际有限商
$$
\boxed{
\mathcal J_Q
=A_Q/\operatorname{ann}_{A_Q}
\bigl(F_t(t_Q,x)\widetilde q(t_Q,x)\bigr)
\simeq k_Q[x]/(x^{d_Q}).
}
\tag{10}
$$
$d_Q=0$ 时约定右侧为零空间。
若 $d_Q>0$，该行在 (10) 上非零，并且其最高 jet 系数为单位。
因此精确有
$$
\boxed{
\mathfrak b_Q\equiv0\text{ 于原完整纤维来源}
\iff
F_t(t_Q,x)\widetilde q(t_Q,x)=0\text{ 于 }A_Q.
}
\tag{11}
$$

证明。若 $u=\ell$，引理已使 (3) 恒零。
否则置 $d=\ell-u\in\{1,\ldots,\ell\}$，则
$$
S_Q=s_0x^{1-d}+\text{更高项},\qquad s_0\ne0.
$$
若 $v\ge d$，(3) 同样恒零。
若 $v<d$，写 $\widetilde q(t_Q,x)=q_vx^v+\cdots$，$q_v\ne0$。
因为 $D_x+1$ 保每个 $(x^j)$，(3) 杀 $(x^{d-v})$。
且取原纤维值 $G=x^{d-v-1}$ 时，只有所显示的首项贡献，得到
$$
\boxed{
\mathfrak b_Q(x^{d_Q-1})
=-c_st_Q^rW(t_Q)\,s_0\,d^2q_v\ne0.
}
\tag{12}
$$
全部因子在原非固定点均为单位；
特别 $1\le d\le\ell<p$ 支付了 $d^2$，没有忽略 Euler 的正特征核。

另一方面，$F_t\widetilde q$ 在 $A_Q$ 的次数为
$\min(\ell,u+v)$；
其 annihilator 正是 $(x^{d_Q})$。
所以 (10) 是同一实际纤维的商，而非任选的更小 jet。
这也证明 (11)。证毕。

这里“最高系数为单位”只表示 (12) 的一条真实行。
当 $d_Q>1$ 时，它不是整个商到一维的单射，更不赋 $\mathscr W_T$ 的评价像。

## 4. 原移动二次因子的具体边界

若 $\deg H=2$，R797 的原常数-charge 关系
$$
\lambda^3d^{3c}\widetilde q(t,0)=A_1,\qquad A_1\in k^\times
$$
使每个非固定 $H$ 根处 $\widetilde q(Q)$ 为单位。
于是 $v=0$，(10) 的长度为 $\ell-u$，且
$$
\mathfrak b_Q=0\iff F_t|_{D_Q}=0.
\tag{13}
$$

若 $H$ 在该点为简单根，$u=0$，整条长度为 $\ell$；
若为二重根，$u\ge1$，长度至多 $\ell-1\le b-1$。
因此双根情形不是由“水平长度为二”决定边界：
原横纤维中 $F_t$ 的实际像决定它是否为零。

例如：

- 光滑二重水平切点有 $\ell=1,u=1$，边界为零。
- 节点首部 $T_0^2+\alpha xT_0+\beta x^2$，
  $\beta(\alpha^2-4\beta)\ne0$：
  $\alpha\ne0$ 时 $\ell=2,u=1$，只读一个真实值，
  $S_Q(0)=-\alpha/\beta$；$\alpha=0$ 时
  $F_t(t_Q,x)\in(x^2)$，故 $u=\ell=2$，整行确为零。
- 对准确模型 $T_0^2-x^3$，$F_t(0,x)=0$，整行确为零。
  对准确模型 $(T_0-a_0x^2)^2-x^3$，$a_0\ne0$，
  则 $\ell=3,u=2$，整行非零，且 $S_Q(0)=-16a_0/9$。
  这些只是解释精确判据的局部模型，不是声称原强接触候选已命中它们。

对全部点取原剩余域迹。前注已证明
$\mathcal H_3\to H^0(D_-,N^3)$ 满射，$\deg D_-\le2b$；
故也得到同预算的真实满射
$$
\mathcal H_3\twoheadrightarrow
\bigoplus_Q H^0\!\left(D_Q,
N^3|_{D_Q}\otimes_{A_Q}\mathcal J_Q\right).
\tag{14}
$$
剩余域迹配对非退化，所以未加前缀的全部负水平分量恒零，
当且仅当每个原局部乘积 $F_t\widetilde q$ 在 $D_Q$ 为零。
不同点的行不能在这个未受限的完整来源上被强制互相抵消。

(14) 不传给 $\mathscr W_T$，也不删除正水平、原固定角、$P$ 主部和其它 normal/carry。
当前仍须把 (10) 的这些明确原商与同一个高前缀兼容对 $(V_0,V_1)$ 联立，
再判断整个指定 $[b_0]$；原物理 $T=s-r-13$、全部原来源与同一修正保持。
