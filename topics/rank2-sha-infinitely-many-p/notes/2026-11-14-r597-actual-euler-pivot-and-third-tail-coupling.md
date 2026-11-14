# R597 接续笔记 — 同一原 Euler 列支付第三尾，但第二块必须同改

日期：2026-11-14。**状态：以下整消元已证明；原指定余类非零仍未证明。**
本笔记不另占结果编号。

保 R597/R603 的同一 $r=1,\nu=2,c=3$ 结点、
$p=6s-1>101$、$\ell=2$，以及已经通过完整
$\mathcal D_\psi^+$ 的同一个 $R$。
采用 R597 §8.1 的真实同格规范
$\xi\in w^7$、$A\in w^5$。
这时原第二代表第三块准确为
$$
\Psi_2=a(z_0+z_1w),\qquad
z_j=[w^{s+j}]\bar Z^+ .
\tag{1}
$$
$n_0=s-13$ 及全部原 $M/J_A$ 区别保持。

## 1. 一条零新增预算的实际列

源端 $\mathcal E=Y\partial_Y$ 保每个
$Y^nq_n\mathcal O[t]_{\le e_{n+1}}$，
所以 $\mathcal EP$ 是原同一个 $\mathcal W_D$ 中的列组合；
无需任何新乘子、角或次数帽。

写
$$
B=(\mathcal E^2P)|_\psi=w^2b,\qquad
C=(\mathcal E^3P)|_\psi=c_1w+O(w^2).
$$
$c=3$ 给 $\bar c_1\ne0$。
因 $\bar\eta_0\in w^{s-2}$，
在原实际短长度 $n_0$ 内有
$$
(\mathcal EP)|_g=0,\qquad
(\mathcal E^2P)|_g=B,\qquad
\pi_2(\mathcal E^3P)|_g=c_1w .
$$
第一式仅在显示截断和模 $p$ 下使用，不作整恒等。

于是同一原第二次修正矩阵准确给
$$
\boxed{
\bar J_A(\mathcal EP)
=\left(0,\ a\pi_{n_0}B,\
 \frac{a^2c_1}{2}w\right).}
\tag{2}
$$
这里第三块长度为二。
这保留了 source degree 和全部原角；
在此步之前，两条十三行已由同一个 $R$ 支付。

## 2. 与已经付清的同 R gauge 联立

另假定接触准确为 $s-2$，所以
$\bar\beta_0\ne0$，
$\beta=\pi_2\mathscr S(B\eta_0)$。
已付的实际变换是
$$
R\longmapsto R+cP,\qquad
T\longmapsto T+cR.
\tag{3}
$$
它把整个 $P+pR+p^2T$ 乘以 $1+pc$ 模 $p^3$，
因此保持原完整可提升性。
第一修正仍通过同一个 $\mathcal D_\psi^+$。

按 R597 的 $Z^+$ 定义，(3) 给
$$
(z_0,z_1)\longmapsto
(z_0+c\beta_0,\ z_1+c\beta_1).
$$
取 $c=-z_0/\beta_0$，得到第三块
$$
a z_1^\circ w,\qquad
z_1^\circ=z_1-\frac{\beta_1}{\beta_0}z_0.
\tag{4}
$$
前两块必须一同使用变换后的 $R$ 重算；
不能只修改 (4)。

现在取真正第二次修正的一份
$$
\boxed{T_{\rm E}=-\frac{2z_1^\circ}{a c_1}\mathcal EP.}
\tag{5}
$$
由 (2)，$\Psi+\bar J_A(T_{\rm E})$ 的整个第三块为零，
而前两块准确为
$$
\boxed{
\left(\Psi_0,\ 
\Psi_1-\frac{2z_1^\circ}{c_1}\pi_{n_0}B\right).}
\tag{6}
$$
(6) 的 $\Psi_0,\Psi_1$ 是 (3) 后同一修正的完整代表，
不省 $U_1/p$、$Z^+$、普通高尾或原单位运输。

这确是一份全来源 Schur 消元：
在第三块常数为零的来源子空间内，(2) 的一次项为单位，
故它分裂出 $\mathcal EP$ 这一条实际补列。
余下来源准确是
$$
\mathcal H=
\{H\in\overline{\mathcal W}_D:
\pi_2(\mathcal E^2H)|_g=0\}.
\tag{7}
$$
所以旧截止内的剩余问题，是 (6) 是否属于同一个
$\mathcal H$ 的前两块像。
其普通低行继续用 R597 的实际整右逆消去。
不能把 (7) 换成任意两份 jet，也不能把 (6) 的 $B$ 项丢掉。

## 3. 准确边界

本笔记把第三尾化为一个明确的第二块 $B$ 倍数，
没有证明该倍数在剩余像中为零或非零。
$c$ 和 $T_{\rm E}$ 都由同一个 $R$ 决定。
因此不能分别消去 $z_0,z_1$ 后宣称原 $d_2$ 消失。

若 $\beta_0=0$，(3) 不能用于去掉 $z_0$；
若最低角重数 $c>3$，$c_1$ 不是单位，(5) 也不能调用。
这些边界均不从本笔记中省略。
R612 的两条更高单位行仍在旧目标之外，
并不代替 (6) 的实际像判定。
