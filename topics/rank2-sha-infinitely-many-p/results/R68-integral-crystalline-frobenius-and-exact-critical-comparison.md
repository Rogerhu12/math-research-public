# R68. 实际整 crystalline Frobenius 与临界行的完全精度比较

日期：2026-11-12。**状态：整 Frobenius 代表、准确比较及首次分母改善已证明；指定行的跨素数非零仍开。**

## 1. 整基、全形式盘整除和矩阵方向

使用 R66 的 Legendre 族、$s=1-4t^2$，在 $R=\mathbb Z_p[[t]]$ 上取
$$
\omega=dx/(2y),\quad\xi=x\omega,\quad
\eta=\nabla_{\partial_t}\omega
 =\frac{\omega}{2(1-\lambda)}-\frac{\xi}{2\lambda(1-\lambda)}.
$$
$\omega,\xi$ 的整 Čech 代表与单位 cup pairing 给整基；上式的变换行列式也是单位。
故 $e=(\omega,\eta)^t$ 是整个形式盘的整 de Rham 基，连接矩阵为
$$
A=\begin{pmatrix}0&1\\s^{-1}&8ts^{-1}\end{pmatrix}.
$$

对 $\phi(t)=t^p$ 的实际 crystalline Frobenius 使用行约定
$$
\Phi(e^\phi)=\mathcal F_p(t)e.
$$
光滑 proper 的整比较给 $\mathcal F_p\in M_2(R)$。
模 $p$ 的相对 Frobenius 杀掉相对一形式，因此在整个形式盘都有
$\mathcal F_{11},\mathcal F_{12}\in pR$，不只是 CM 纤维的整除。

设 $Y=\begin{pmatrix}K&L\\K'&L'\end{pmatrix}$，$Y(0)=I$，$\det Y=s^{-1}$。
水平性与初值准确给
$$
\boxed{\mathcal F_p(t)=Y(t^p)\mathcal F_p(0)Y(t)^{-1}.}
\tag{1}
$$
CM 自同构在 $e(0)$ 上为 $\operatorname{diag}(i,-i)$。
保留系数 Frobenius 对 $i$ 的作用及行列式 $p$，得到
$$
\mathcal F_p(0)=
\begin{cases}
\begin{pmatrix}0&pa_p\\b_p&0\end{pmatrix},&p\equiv3\pmod4,\quad a_pb_p=-1,\\
\operatorname{diag}(pa_p,b_p),&p\equiv1\pmod4,\quad a_pb_p=1,
\end{cases}
\tag{2}
$$
$a_p,b_p\in\mathbb Z_p^\times$。本篇的 $a_p$ 不是 Frobenius trace。

## 2. 两种真实整周期替代

惰性处定义
$$
U_p=\frac{\mathcal F_{12}}{pa_ps}
 =K(t^p)K-\frac{b_p}{pa_p}L(t^p)L,
$$
$$
V_p=-\frac{\mathcal F_{22}}{b_ps}
 =L'(t^p)L-\frac{pa_p}{b_p}K'(t^p)K.
\tag{3}
$$
普通处定义
$$
U_p=\frac{\mathcal F_{22}}{b_ps}
 =L'(t^p)K-\frac{pa_p}{b_p}K'(t^p)L,
$$
$$
V_p=-\frac{\mathcal F_{12}}{pa_ps}
 =K(t^p)L-\frac{b_p}{pa_p}L(t^p)K.
\tag{4}
$$
这些是真实整 Frobenius 的条目，故 $U_p,V_p\in R$，初值分别为 $1,t$。
导数撇号表示先求导再代入 $t^p$。
两种情形都准确有
$$
U_p-K=O(t^{p+1}),\qquad V_p-L=O(t^p).
\tag{5}
$$
首差的赋值惰性为 $-1,+1$，普通为 $+1,-1$。
它们分别消去原 $K$ 或 $J=L/t$ 的首次分母。

置 $H_p=V_p/t$、$B_p=U_p/H_p$，以及
$$
W_{i,p}=\frac{M_1U_p}{sH_p^2},\qquad
W_{o,p}=\frac{M_1}{sU_p}.
$$
R66 已证明 $M_1$ 对所有 $p\notin\{2,3,5,17\}$ 整，所以这些都是完整整级数。
由于 $M_1$ 从四次开始，(5) 的差在目标临界次数尚未出现。于是
$$
\boxed{C_{p+1}=[t^{p+1}]W_{i,p}B_p^p,\qquad
C_{p-1}=[t^{p-1}]W_{o,p}B_p^p.}
\tag{6}
$$
这两式均为特征零的完全相等，而非只保留模平方的近似。

## 3. 真正全级数除法差与准确临界行

完整整性允许定义
$$
\Delta_p(B_p)=\frac{B_p(t)^p-B_p(t^p)}p\in R.
$$
$B_p(t^p)-1$ 从 $2p$ 次开始。因此惰性处得到完全保精度的式子
$$
\boxed{\frac{C_{p+1}}p
 =\frac{[t^{p+1}]W_{i,p}}p
  +[t^{p+1}]W_{i,p}\Delta_p(B_p).}
\tag{7}
$$
第一项的整性由实际 $C_{p+1}\in p\mathbb Z_p$ 推出，不能预先删掉它。
普通处把 R66 的三项第二除 $p$ 行以 $U_p,H_p$ 替代即可，仍需完整相加，
其临界系数模 $p$ 等于 $C_{p-1}/p^2$。

## 4. 首次非目标分母统一推迟至 $2p+4$

两种情形都有 $B_p=1-t^2+O(t^4)$，且 $W_{i,p},W_{o,p}=t^4+O(t^6)$。
由完整整性，$\log B_p$ 首坏项准确为 $t^{2p}$，且该系数乘 $p$ 后为 $-1$。

定义
$$
\widetilde{\mathcal G}_{i,p}=(t\partial_t-1)^{-1}W_{i,p}+W_{i,p}\log B_p,
$$
$$
\widetilde{\mathcal G}_{o,p}=(t\partial_t+1)^{-2}W_{o,p}
 +(t\partial_t+1)^{-1}(W_{o,p}\log B_p)
 +\tfrac12W_{o,p}(\log B_p)^2.
$$
在次数 $2p+4$ 之前，Euler 逆唯一可能出现的偶次 $p$ 分母正是临界 $p\pm1$，
已由实际 $C$ 的整除消去。于是二者首坏次数都准确为 $2p+4$，并有
$$
\boxed{p[t^{2p+4}]\widetilde{\mathcal G}_{i,p}\equiv-1,
\qquad p[t^{2p+4}]\widetilde{\mathcal G}_{o,p}\equiv-1/5\pmod p.}
\tag{8}
$$
这是真实 Frobenius 整规范对原固定标量行 $p+5$、$p+3$ 首坏次数的改善。
但新代表依赖于 $p$；不能将其无代价视为一个固定 adelic germ。
同样，(7) 仍是非线性 $p$ 次幂差加上移动阶 jet，尚未被识别为固定有限秩
线性相对 cohomology 的已知非零 Frobenius 条目。

完整证明、整比较的一手来源和矩阵约定见
[整 GM Frobenius 与临界行](../notes/2026-11-12-integral-gm-frobenius-critical-row.md)。
后续须同时保留 R66 的实际 Kummer 切向代表、Hodge 源格修改及全微分项。
