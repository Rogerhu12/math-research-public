# R271 附录：强联块 gauge 的真实左反馈、返回运输与未封普通末端

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。本文将原逆芽的有限多项式放入同一个强联块源：支付真正左最小化及左零源反馈，构造同一未来的有界原链，保留它全部未闭头旗和普通末端。另从真实返回系统得到一个只付裸费的 divided-difference 余项。这个余项没有删除返回主项；新普通费用与原联块普通费用双边可比，封口问题仍未解决。

依赖：

- [同一顶部强位源流](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)；
- [精确源收缩](R271-appendix-first-row-observability-loss-exact-source-contraction-and-disk-calculus.md)；
- [同源逐幂远孔损耗](R271-appendix-same-source-power-far-occupation-loss-and-left-null-feedback.md)；
- [完整返回的物理有限系统](R271-appendix-complete-return-orthogonal-decomposition-driven-system-and-unique-lift.md)。

## 1. 同一个头、源及有限多项式

固定原 $m\ge10$、$d=2^m$，取强尾位数 $R$，写
$$
C=A_m+D_<,\qquad h=d+R,\qquad D=D_>,\qquad
\delta=\|D\|,\qquad C^h=0.
$$
在第 $n$ 个远孔切口，仍用
$$
U=(E_n^C)^\dagger,\quad L=U^*U,\quad
B=J_b^*J_b,\quad H=G^{-1}=J_f^*J_f,\quad
C_{\rm s}=C|_{\mathscr R_n^C}.
$$
$\mathscr K=\ker E_n^C$ 是这个远孔前缀的真左零源核，不是旧总孔切口的核。

保持原真实逆芽
$$
\rho=\exp(-25d^3/2),\quad r_m=\rho/(2d_0),\quad
d_0=e^{-20},\quad \varepsilon_m=e^{-d^3/4}.
$$
令
$$
q_h(z)=\left[\frac{\psi_m(z)}z\right]_{<h}
=\sum_{k=0}^{h-1}q_kz^k,\qquad q_0=d_0.
\tag{1.1}
$$
当 $h>d$ 时，(1.1) 必须保到 $h-1$ 次，不能换成旧头的 $<d$ 截断。在 $C$ 或 $C_{\rm s}$ 上，它等于真实解析函数的 nilpotent 代入。

假设 $\delta<\rho$，置 $t=\delta/r_m<2d_0<1/4$。原芽在 $r_m$ 圆盘上的非线性估计给
$$
|q_k|\le2d_0^2\varepsilon_m r_m^{-k}\qquad(k\ge1).
$$
记
$$
A_1=\sum_{k=1}^{h-1}|q_k|\delta^k
\le2d_0^2\varepsilon_m\frac{t}{1-t},
\qquad A_0=d_0+A_1,
$$
$$
A_{\rm drv}=\sum_{k=1}^{h-1}k|q_k|\delta^k
\le2d_0^2\varepsilon_m\frac{t}{(1-t)^2}.
\tag{1.2}
$$
特别 $A_1<d_0/2$。这些是固定原多项式在真实远尾半径上的绝对系数界。

## 2. 真左最小化与零源反馈一起支付

取任意同源 $r$，令 $v=Ur$。前稿的逐幂正交展开及首段损耗给
$$
\|C^kv\|^2
\le\delta^{2k}
\left(\|P_{\mathcal N_>\ge k}v\|^2+\alpha(r)^2\right)
\qquad(k\ge1).
\tag{2.1}
$$
准确地说，前稿同时控制
$\|UC_{\rm s}^kr\|^2+\|P_{\mathscr K}C^kv\|^2=\|C^kv\|^2$，
所以 (2.1) 没有删除左零源反馈。

由于 $q_h(C)v$ 是源 $q_h(C_{\rm s})r$ 的可行左向量，
$$
Uq_h(C_{\rm s})r=(I-P_{\mathscr K})q_h(C)v.
$$
又 $v\perp\mathscr K$，故有准确正交分解
$$
q_h(C)v-d_0v
=\bigl(Uq_h(C_{\rm s})r-d_0Ur\bigr)
 +P_{\mathscr K}q_h(C)Ur.
$$
用 (2.1) 逐项求和，得到
$$
\boxed{
\begin{aligned}
&\|Uq_h(C_{\rm s})r-d_0Ur\|^2
 +\|P_{\mathscr K}q_h(C)Ur\|^2\\
&\qquad\le
A_1^2
\left(\|P_{\mathcal N_>\ge1}Ur\|^2+\alpha(r)^2\right).
\end{aligned}
}
\tag{2.2}
$$
常数项的核投影严格为零。对于原同一顶部
$U r_n^C=P_{\mathcal N_>\le n}u_Q$，右边就是这个真实向量的远尾非真空部分与同源裸费。

因此 (2.2) 确实付清了新 $C$、新远孔核的正向反馈。它没有把
$q_h(C)$ 换成旧 $G_{1,m}=p_m(B_m)$，也不把
$\mathscr K_n^C$ 换成旧总孔 $K_{m,n}$。

## 3. 同一未来的原链及所有未闭头旗

取原同一个 $u=u_Q$，并收窄到
$$
n+2h+R<Q.
\tag{3.1}
$$
它仍在原带权母窗口内；与此前 $n+h+R<Q$ 相比只少 $h$ 个切口。定义未修复的右段
$$
c_j^{\rm raw}=-q_h(C)u_{n+j}\qquad(1\le j\le h).
\tag{3.2}
$$
同一真实低输出方程给源和全部内部方程
$$
Dc_1^{\rm raw}=q_h(C_{\rm s})r_n^C,\qquad
Cc_j^{\rm raw}+Dc_{j+1}^{\rm raw}=0\quad(j<h).
\tag{3.3}
$$
为了准确估计原链范数，对 $k<h$ 使用同一未来
$$
C^ku_{n+j}=(-D)^ku_{n+j+k}.
$$
(3.1) 保证所有被读取的行都是真低输出行。对有限序列用算子卷积的三角不等式，
$$
\boxed{
\sum_{j=1}^h\|c_j^{\rm raw}\|^2
\le A_0^2
\sum_{\ell=n+1}^{n+2h-1}\|u_\ell\|^2.
}
\tag{3.4}
$$
没有乘环境 $\|q_h(C)\|$ 或头 Jordan 条件数。

但 (3.2) 仍不一定是完整普通右链。每一段的头旗缺陷准确为
$$
\boxed{
C^{h-j+1}c_j^{\rm raw}
=-q_h(C)(-D)^{h-j+1}u_{n+h+1}
\in E_{j-1,n+j},
}
\tag{3.5}
$$
其中 $D^hu_{n+h+1}=0$ 是同一原顶部已付的真尾旗。特别原链末端为
$$
\boxed{
Cc_h^{\rm raw}
=-Cq_h(C)u_{n+h}
=-\psi_m(C)u_{n+h}
=-q_h(C_{\rm s})r_{n+h}^C.
}
\tag{3.6}
$$
$\psi_m(C)=Cq_h(C)$ 在 $C^h=0$ 的意义下成立。这里没有把 $\psi_m(C)$ 写成 $B_m$。

逐段投影
$b_j=P_j^{\rm lo}c_j^{\rm raw}$
会消掉 (3.5)，给同源合法裸链及真末端。因此 (3.4) 支付裸费。完整普通封口仍须修复全部高返回，不仅删除 (3.6) 这一个显示的末端；其最小代价由完整返回稿的未压缩算子
$(\mathcal C+\mathcal T)|_{\mathscr E_0}$
确定，不能从 (3.4) 直接称为普通 $\lambda$ 的预算。

## 4. 新 gauge 没有减弱普通费用

完整和裸右域分别已经给
$$
\|C_{\rm s}^k\|_H\le\delta^k,\qquad
\|C_{\rm s}^k\|_B\le\delta^k.
$$
因此在两种右度量中
$\|q_h(C_{\rm s})-d_0I\|\le A_1$。特别
$$
\boxed{
(d_0-A_1)\lambda(r)
\le\lambda(q_h(C_{\rm s})r)
\le(d_0+A_1)\lambda(r),
}
\tag{4.1}
$$
并且 $\alpha$ 有完全相同的双边式。故新普通候选的目标与原联块普通费用等价；左端反馈变小并不自动把普通封口变成一个更弱的问题。

## 5. 完整返回上的受控 divided-difference

采用完整返回稿的同一记号
$$
\mathcal R=J_f-J_b,\qquad
\mathcal R^*\mathcal R=H-B,\qquad
\mathcal RC_{\rm s}=-T_0\mathcal R-KJ_b,
$$
$$
T_0^h=0,\qquad\|[T_0,K]\|\le\delta.
$$
逐幂归纳严格给
$$
\mathcal RC_{\rm s}^k
=(-T_0)^k\mathcal R
-\sum_{j=0}^{k-1}(-T_0)^jKJ_bC_{\rm s}^{k-1-j}.
$$
于是
$$
\boxed{
\mathcal Rq_h(C_{\rm s})-q_h(-T_0)\mathcal R
=-\sum_{k=1}^{h-1}q_k
 \sum_{j=0}^{k-1}(-T_0)^jKJ_bC_{\rm s}^{k-1-j}.
}
\tag{5.1}
$$
同一裸源收缩给
$\|J_bC_{\rm s}^{\ell}r\|\le\delta^\ell\alpha(r)$，包括
$\ell=0$ 的原裸费。因此
$$
\boxed{
\|\mathcal Rq_h(C_{\rm s})r-q_h(-T_0)\mathcal Rr\|
\le A_{\rm drv}\,\alpha(r).
}
\tag{5.2}
$$
这是实际返回余项的统一预算，未估计 $\mathcal R$ 的环境范数，也未交换完整逆和商投影。

同时
$$
\|q_h(-T_0)-d_0I\|\le A_1,
\qquad
\|q_h(-T_0)^{-1}\|\le(d_0-A_1)^{-1}.
$$
所以 (5.2) 可以双向运输返回列，但其主项
$q_h(-T_0)\mathcal Rr$ 仍保与 $d_0\mathcal Rr$ 相同的规模。它没有令原返回费用变小。

## 6. 同一未来中的返回代表

令 $P_{\mathscr W}$ 为完整返回稿中真实右环境的物理投影，并置
$Y=(u_{n+1},\ldots,u_{n+h})$。原 $Y$ 不必满足全部头旗，因此这里必须先保 $P_{\mathscr W}$。

同一顶部给
$P^{\rm lo}P_{\mathscr W}Y=P^{\rm lo}Y\in\mathcal Y_b$，
且 $-P^{\rm lo}Y$ 是源 $r_n^C$ 的裸候选。又 $Y\perp Z_f$，因为每个完整右零源都可作为支撑 $\le n+h+R<Q$ 的真核与原 $u_Q$ 配对。故
$$
e_Y=P_{\mathscr W}Y+J_b r_n^C\in\mathscr E_0,
$$
$$
\|e_Y\|^2
=\|P_{\mathscr W}Y\|^2-\alpha(r_n^C)^2
\le\|Y\|^2-\alpha(r_n^C)^2.
\tag{6.1}
$$
原完整 flat 配对和同源最小正交性准确给
$$
\boxed{
\mathcal R^*e_Y=(L+B)r_n^C.
}
\tag{6.2}
$$
因此 (5.2) 的同源配对误差不超过
$A_{\rm drv}\alpha(r_n^C)\|e_Y\|$。
仍需控制的就是
$$
\langle e_Y,q_h(-T_0)\mathcal Rr_n^C\rangle;
\tag{6.3}
$$
不能将 $e_Y$ 替换成一个独立选择的测试，或从 (6.1) 的小范数推 (6.3) 小而不保返回列。

## 7. 全局锚的准确含义

为区分新旧头，令 $M_0=m+R$，并用原全局后移 $B_{\rm glob}$ 定义
$$
C^g=\sum_{i<M_0}b_iN_i\quad(N\text{ 模型}),\qquad
C^g=\sum_{i<M_0}b_iN_i(I+N_i)^{-1}\quad(Y\text{ 模型}),
$$
其中 $N_i=B_{\rm glob}^{2^i}/d_i$。它与原 $T$ 交换，且是 $B_{\rm glob}$ 的零常数项有界函数。令 $D^g=T-C^g$。对 $w\in M=\ker T$，
$$
g=q_h(C^g)w=q_h(-D^g)w\in M.
$$
有限多项式的常数项给
$$
g-d_0w\in B_{\rm glob}M\subseteq N,\qquad
\langle w,g\rangle=d_0\|w\|^2\quad(w\in W).
\tag{7.1}
$$
这里只取一个有限多项式；不在全局后移上代入未收敛的无限逆级数。

还可准确记录低远孔运输。设
$\bar\delta=\max(\|D\|,\|D^g\|)<r_m$、
$\Delta=\|D-D^g\|$，并令
$$
Q_0=\sum_{k<h}|q_k|\bar\delta^k,\qquad
Q_1=\sum_{1\le k<h}k|q_k|\bar\delta^{k-1}.
$$
同一低输出方程、$n+h+R<Q$ 和原真实顶部误差给
$$
\boxed{
\|P_{\mathcal N_>\le n}q_h(C)u
  -P_{\mathcal N_>\le n}g\|
\le(2\eta_m Q_0+\Delta Q_1)\|w\|.
}
\tag{7.2}
$$
证明是在每个幂中先把 $C^ku_j$ 换成 $(-D)^ku_{j+k}$，再比较
$D^k$ 与 $(D^g)^k$；后者差至多
$k\bar\delta^{k-1}\Delta$。所有被读取的输入总孔均 $\le n+h-1+R<Q$，所以不出现环境 $\|q_h(C)\|$ 或未知的 $Q$ 外尾乘大常数。原 carry 估计可用于 $\Delta$，本式本身保其准确值。

(7.1)–(7.2) 是全局锚和低远孔运输；它们没有宣布 (3.6) 的有限末端属于一个已经付费的完整右链，也不估计将 $g-d_0w$ 反向除以 $B_{\rm glob}$ 的范数。真正普通封口、高返回主配对 (6.3) 和 $N=M$ 仍未完成。
