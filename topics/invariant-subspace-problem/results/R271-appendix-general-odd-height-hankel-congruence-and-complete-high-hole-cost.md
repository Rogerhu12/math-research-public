# R271 补录：任意允许奇高度的解析 Hankel 合同、全真幂旗高孔门与完整最高极点费用

作者：Astra-ISP-b2a9acde-20261120（root 与 r271_cost）；AI-assisted GPT-6 Astra Pro。日期：2026-11-20 UTC。状态：本条明确范围已证明。

## 0. 范围

本条把已证三孔长链和高孔补空间推进到一般奇高度 $r$。
核心是一个显式标量 Hankel 正交化：
它只含 $A$ 的非负幂，保留原旧头的全部真实幂核旗。
不需要把逐个高度的消元数组登记为结果。

父结论为[完整奇高度简单极点](R271-appendix-odd-height-highest-carry-full-mp-simple-pole.md)、[完整 Galerkin 极点最小范数](R271-appendix-complete-galerkin-highest-carry-pole-and-cancellation-criterion.md)、[三孔一般长链](R271-appendix-general-head-long-bad-chain-analytic-schur-and-three-true-power-flags.md)、[一般头高孔源门](R271-appendix-general-head-high-hole-schur-complement-and-complete-residue-cost.md)，以及[强尾中位归一化](R271-appendix-median-strong-tail-scaling-four-power-condition-and-full-odd-height-cost.md)。
普通 Hilbert ISP 与实际完整源费用仍未闭。

## 1. 参数与精确核参数化

取原 N 型，令
$$
m\ge5,\quad n=2^{m-1},\quad d=2n,\quad
R\ge d\ \text{为偶数},
$$
并取任意奇数
$$
\boxed{r\ge1.}
\tag{1.1}
$$
后面会按实际存在的短链、长链分别取最低孔门；不预设小 $r$ 限制。
先固定全部旧基准 carry 为正。在最高 carry 参数 $t$ 下，
$$
H_t=\begin{pmatrix}A&bI+tV\\0&A\end{pmatrix},
\qquad b=b_{m-1},
$$
其中 $A$ 为原旧 $n$ 维循环头，$H_0$ 的 Jordan 型为
$(n+1,n-1)$，故 $H_0^{n+1}=0$。

在单位奇尾链 $J_l$ 上，若
$$
l\ge n+r,
\tag{1.2}
$$
令 $C_t=H_t+J_l$、$X_t=C_t^r=X_0+tX_1$，并定义
$$
\Phi_p(u)=\sum_{j=0}^{n}(-1)^j
\binom{p+j-1}{j}H_0^ju\otimes e_{p-1+j},
\qquad1\le p\le r.
\tag{1.3}
$$
逐项相消给 $C_0\Phi_p=\Phi_{p-1}$，$\Phi_0=0$。
前 $r$ 个尾级的参数矩阵为单位三角，所以这些 $rd$ 列独立。
另一方面，$H_0$ 的各块与 $J_l$ 张量相加后的最短链至少为 $l-n\ge r$，
因此完整 $r$ 次幂核维数为 $rd$。
所以 $\Phi=(\Phi_1,\ldots,\Phi_r)$ 参数化整个 $\ker X_0$。

## 2. 完整 Schur 型的生成式

记 $\mathcal J_h$ 为逆序翻转。
真实二进制头满足 $\mathcal J_dH_t=H_t^*\mathcal J_d$。
令
$$
\mathcal J=\mathcal J_d\otimes\mathcal J_l.
$$
标量截断生成向量
$$
v_p(z)=\sum_{j=0}^{l-p}(-1)^j
\binom{p+j-1}{j}z^je_{p-1+j}
$$
满足
$$
(z+J_l)v_p=v_{p-1}
+(-1)^{l-p}\binom l{p-1}z^{l-p+1}e_{l-1}.
$$
又对 $0\le h\le r-1$，
$$
v_q(z)^T\mathcal J_l(z+J_l)^he_{l-1}
=\mathbf1_{\{h=q-1\}}.
$$
迭代 $r$ 次得到
$$
v_q^T\mathcal J_l(z+J_l)^rv_p
=c_{pq}\,z^{l+r+1-p-q},
$$
$$
c_{pq}=
\begin{cases}
0,&p+q\le r,\\
(-1)^{l+r-p-q}\binom l{p+q-r-1},&p+q\ge r+1.
\end{cases}
\tag{2.1}
$$
代入 $H_t$ 并在 $t=0$ 微分；
$\Phi$ 的导数项与 $X_0\Phi=0$ 相消，故
$$
\Phi_q^*\mathcal JX_1\Phi_p
=c_{pq}\mathcal J_d
\left.\partial_tH_t^{\,l+r+1-p-q}\right|_0.
\tag{2.2}
$$

沿用真实旧函数 $F$、旧 weighted shift $B$、
$\rho=d_{m-2}^2$、$g(z)=F(z)/z$，置
$$
U=\rho g(B)^n,\qquad G=\mathcal J_nU.
$$
$G$ 自伴可逆，$GA=A^*G$，且对 $k\ge n$
$$
\left.\partial_tH_t^k\right|_0
=\begin{pmatrix}0&UA^{k-n}\\0&0\end{pmatrix}.
\tag{2.3}
$$
由 (1.2)，(2.2) 所需的最小 $k=l-r+1\ge n+1$，所以 (2.3) 全部适用。

每个参数的最高位为 $0$ 的部分在根空间中。
对最高位为 $1$ 的参数，反序编号
$$
i=r-p,\qquad j=r-q,\qquad0\le i,j\le r-1.
$$
令
$$
e=l-n-r+1,\qquad
\mu_k=(-1)^k\binom l{r-1-k},
$$
负下标二项式按零解释。
完整剩余 Schur 型为
$$
\boxed{\mathcal B_{ij}=\mu_{i+j}GA^{e+i+j}.}
\tag{2.4}
$$

## 3. 显式 Hankel 正交化

设 $u=r-1$，令标量矩阵
$$
C_{ij}=\mu_{i+j}\quad(0\le i,j\le u).
$$
定义单位下三角矩阵 $M$：
$$
\boxed{
M_{ji}=
\binom ji
\frac{(u-i)!\,(l-u+j+i-1)!}
{(u-j)!\,(l-u+2j-1)!},
\qquad0\le i\le j\le u.
}
\tag{3.1}
$$
所有分母阶乘均非负。

### 引理 3.1

$$
\boxed{
MCM^T=\operatorname{diag}(\delta_1,\ldots,\delta_r),
}
\tag{3.2}
$$
其中
$$
\boxed{
\delta_k=(-1)^{k-1}
\frac{(l+k-1)!\,(k-1)!\,(l-r+k-1)!}
{(r-k)!\,(l-r+2k-1)!\,(l-r+2k-2)!}.
}
\tag{3.3}
$$
每个 $\delta_k\ne0$。

**证明。** 以形式矩定义双线性型
$\langle z^i,z^j\rangle=\mu_{i+j}$。
令
$$
p_j(z)=\sum_{i=0}^jM_{ji}z^i.
$$
它首一。对 $0\le a<j$，将 (3.1) 与 $\mu_{i+a}$ 相乘后，
除去与 $i$ 无关的因子，所剩求和为
$$
\sum_{i=0}^j(-1)^i\binom ji
(u-i)_{\downarrow a}\,
(l-u+i+a+1)_{\uparrow(j-a-1)}.
\tag{3.4}
$$
这是一个 $j-1$ 次多项式的 $j$ 阶有限差分，所以为零。
二项式项越界时第一下降乘积自动为零，故没有边界缺项。
因此 $p_j$ 与所有较低次数多项式正交，(3.2) 为对角。

为求其对角，令 $\Delta_k$ 为 $C$ 的前 $k$ 阶主子式。
反序行后得到 binomial Toeplitz 行列式，故
$$
\Delta_k=(-1)^{k(k-1)/2}
\prod_{i=0}^{k-1}
\frac{(l+i)!\,i!}
{(r-k+i)!\,(l-r+k+i)!}.
\tag{3.5}
$$
这里的 Toeplitz 乘积式可自足验证：
若
$D_k(l,a)=\det[\binom l{a+i-j}]_{0\le i,j<k}$，
候选乘积
$$
\prod_{i=0}^{k-1}\frac{(l+i)!\,i!}{(a+i)!(l-a+i)!}
$$
在 $k=1$ 及边界 $a=0,l$ 正确。
Desnanot–Jacobi 恒等式给
$$
D_k(l,a)D_{k-2}(l,a)
=D_{k-1}(l,a)^2
-D_{k-1}(l,a-1)D_{k-1}(l,a+1).
$$
候选式的右侧比率为
$$
1-\frac{a(l-a)}{(a+k-1)(l-a+k-1)}
=\frac{(k-1)(l+k-1)}
{(a+k-1)(l-a+k-1)},
$$
恰等于左侧所需比率，归纳即证。
在本条 $a=r-k\ge0$ 的范围各主子式非零。
最后 $\delta_k=\Delta_k/\Delta_{k-1}$，化简得到 (3.3)。证毕。

这给理论闭式与完整证明，不是输出消元数组。

## 4. 不用 $A^{-1}$ 的真实幂旗合同

定义单位上三角算子矩阵
$$
Q_{ij}=
\begin{cases}
M_{ji}A^{j-i},&i\le j,\\
0,&i>j.
\end{cases}
\tag{4.1}
$$
它及逆矩阵只含 $A$ 的非负幂。
由 $GA=A^*G$ 和 (3.2)，直接相乘给
$$
\boxed{
Q^*\mathcal BQ
=\bigoplus_{i=0}^{r-1}\delta_{i+1}GA^{e+2i}.
}
\tag{4.2}
$$
换回 $p=r-i$，真实幂指数为
$$
\boxed{e_p=l-n+r+1-2p,\qquad1\le p\le r.}
\tag{4.3}
$$
因 $A$ 为原循环上三角头，
$$
\ker A^k=\operatorname{span}(e_0,\ldots,e_{k-1}).
$$
$GA^k$ 自伴，故在后面的真实坐标旗上非退化。
没有更换旧真核旗，也没有用奇异的 $A^{-1}$ 完成平方。

## 5. 一般奇高度的完整高孔补空间

完整强尾每条 primitive 链长
$$
l=R-2j_0+1,\qquad1\le l\le R+1.
$$
只有奇 $l\le d+r-2$ 会产生最高新增约束；
更长的链在 $t=0$ 不掉秩。

定义
$$
A_s=\max\!\left(0,\frac{R-n-r+3}{2}\right),\qquad
A_l=m+\frac{R-d+r+1}{2},
$$
$$
\boxed{A_0=\min(A_s,A_l).}
\tag{5.1}
$$
全部量均为整数，且 $A_l>0$。
本节证明完整 $K/F_0$ 有一个非退化 Schur 补空间，
全部支撑在物理总孔级至少 $A_0$。

短坏链满足
$$
1\le l\le\min(R+1,n+r-2),
$$
所以最低 primitive 级恰至少 $A_s$。
这整条链都够高，可取完整局部 Schur 型的物理正交非根补空间。

长坏链只在
$$
n+r\le l\le\min(R+1,d+r-2)
\tag{5.2}
$$
时存在。若该段为空，必有 $r\ge R-n+3$，于是 $A_s=0$，
(5.1) 只使用实际短链的零级门，不虚构长链约束。

对 (5.2) 中的长链，置
$$
h=\frac{d+r-2-l}{2}.
$$
(4.3) 的第 $p$ 个真实非根旗中的新头坐标可写成
$$
e_{d-1-z},\qquad0\le z\le2\bigl(h-(r-p)\bigr).
$$
因为 $z\le2v\Rightarrow\operatorname{popcount}(z)\le v$，
该头孔数至少 $m-h+r-p$。

合同参数还原 (4.1) 每次从参数 $p$ 移到 $p+a$，
恰附带 $A^a$。
N 型每一步至多删一个孔；再用 (1.3)，
头的孔减少与尾级增加逐项抵消。
所以每列最低局部孔为
$$
m-h+r-p+(p-1)=m+r-1-h.
$$
加上 primitive 起始级后，
$$
j_0+m+r-1-h
=m+\frac{R-d+r+1}{2}=A_l.
$$
三个步骤都保完整真幂旗；将所有坏链直和得到全新增约束的补空间。
短链处没有遗漏零源或横向方向。
Schur 型为零的块不需要补空间；如所有块均为零，则极点本来为零。

当
$$
r\le n/2-m+1
\tag{5.3}
$$
时，$A_l\le A_s$，恢复先前较高的长链门 $A_0=A_l$。
超过这个范围后使用真实短链门，不把 (5.3) 人为变成母窗限制。

## 6. 完整实际源、候选与两个加权界

采用统一旧 carry 缩放
$$
d_i(s)=s^{2^i-1}\bar d_i,\qquad
d_{m-1}(s,t)=t\,d_{m-2}(s)^2.
$$
令 $C(s,t)$ 为原头加整个强段，$N=m+R$，
$$
H_r(s,t)=\sum_{j=0}^{r-1}
\frac{(C(s,t)^*)^jC(s,t)^j}{j!S^j},\qquad S>0.
$$
在完整最高真核极限 $F_0(s)$ 中解原物理 Galerkin，
得到 $a_0(s)$ 与
$$
\xi_0(s)=f_1-H_r(s,0)a_0(s).
$$
完整核过滤框架给
$$
\xi_0(s)=\sum_{\nu\ge0}s^\nu\xi_\nu,\qquad
\xi_\nu\in\bigoplus_{g\le1+\nu}\mathcal H_g
\tag{6.1}
$$
（固定所有参数）。
这里始终是完整 $P_{F_0}$，没有把 primitive 分块当物理正交 Galerkin。

物理孔缩放 $\mathcal R_s|_{\mathcal H_g}=s^gI$ 满足
$$
X_1(s)=s^{r-1}\mathcal R_sX_1(1)\mathcal R_s^{-1}.
$$
标准直和中的翻转 $\mathcal J$ 将 $g$ 翻为 $N-g$。
若 $Y$ 是 §5 的高孔补空间，则完整候选为
$$
\widetilde q(s)=
s^{-N-r+1}\mathcal J\mathcal R_sY
(Y^*\mathcal JX_1(1)Y)^{-1}
Y^*\mathcal R_s\xi_0(s).
\tag{6.2}
$$
它满足整个退化核的最高极点方程；
真 $q_{-1}(s)$ 在该完整解集中物理范数最小。

对任意 $0<\gamma\le1$，定义原完整物理加权源
$$
\mathcal Z_\gamma(s)=
\left\|\sum_{g\ge A_0}\gamma^{1-g}P_g\xi_0(s)\right\|.
\tag{6.3}
$$
从 (6.2) 的两侧各取一次 $\mathcal R_s$，得
$$
\|\widetilde q(s)\|
\le C_{\rm loc}\,
s^{2A_0-N-r+1}\gamma^{A_0-1}\mathcal Z_\gamma(s).
$$
其中精确的 $s$ 指数是
$$
\boxed{\beta=2A_0-N-r+1.}
\tag{6.4}
$$
当长链门主导时，
$$
\beta=m+2-d.
$$
当正的短链门主导时，
$$
\boxed{\beta=-n-m-2r+4.}
\tag{6.5}
$$
若 $A_0=0$，则直接使用 $\beta=-N-r+1$，不套正短链公式。

取 $\gamma=s$，形式消失阶为
$$
\boxed{\nu=3A_0-N-r.}
\tag{6.6}
$$
因此固定参数下
$$
q_{-1}(s)=O(s^\nu).
\tag{6.7}
$$
具体地，长链门主导时
$$
\nu=(R-3d+r+3)/2+2m;
$$
正短链门主导时
$$
\nu=(R-3n-5r+9)/2-m.
$$
这仍是最高 $t^{-1}$ 系数，不是整个原 $q(s,t)$。

## 7. 明确有限头常数与全部 $R,r$ 成本

令 $a=16^{m-2}$，并使用真实旧头/参考头界
$$
\|A\|<6,\quad
\kappa(V_{\rm old})\le e^{221a},\quad
\kappa(\widehat V)\le e^{441a}.
$$
原最大低 carry 重标度的有效性由三孔高孔稿的逆芽/输入权单调性证明保持。

### 7.1 短坏链

单位 $J_l$ 上的标准 sl2 成本及 $r!$ 幂增益给
$$
C_{\rm short}=
e^{883a}(1+rb)^2\,8^{2r-2}
\frac{((n-1)!)^2(d-1)!((n+r-3)!)^3}{(r!)^3}.
\tag{7.1}
$$
这是完整局部 Schur MP 的上界。
此式对一般 $r$ 仍有效：
先以 $l-1\le n+r-3$ 统一全部短链。
最大阶乘因子
$e^{221a}(n-1)!(n+r-3)!/r!\ge1$，
所以先取统一上界后再处理剪切中的 $1+\cdots$；
不需要对每条短链假设其个别 MP 上界大于 $1$。
若某条 $D^r=0$，相应剪切项本来为零，该统一上界也仍成立。
取该局部非根空间的物理正交基，基范数为 $1$。

### 7.2 长坏链

由 (1.3)，可以取
$$
\|\Phi\|\le
\sqrt{r(n+1)}\binom{n+r-1}{n}7^n.
$$
从 (3.1)
$$
M_{ji}\le\binom ji
\left(\frac{r-1}{l-r+1}\right)^{j-i},
$$
故按列和及 Frobenius 范数，
$$
\|Q\|\le\sqrt r\exp(6r^2/n).
$$
(3.3) 的倒数中先约去共同因子 $l-r+2k-1$；剩下的上升乘积至多有 $k-1$ 项，每项不超过 $l+r$，其余分母至少为一，阶乘比不超过 $(r-1)!$。因此
$$
|\delta_k|^{-1}\le(r-1)!(l+r)^{r-1}
\le(r-1)!(d+2r)^{r-1}.
$$
再用真实
$\|(GA^e)^\dagger\|\le e^{662a}$，可取
$$
C_{\rm long}=
r^2(n+1)\binom{n+r-1}{n}^{\!2}49^n
e^{12r^2/n}
(r-1)!(d+2r)^{r-1}e^{662a}.
\tag{7.2}
$$
置 $C_{m,r}=C_{\rm short}+C_{\rm long}$。
完整标准直和中的候选按块平方相加，统一常数取 $C_{m,r}$，
不再乘 primitive 重数。
对一般 $r$，可从 (7.1)–(7.2) 直接读出粗界
$$
\log C_{m,r}\le883a+
O\!\left((d+r)\log(d+r)+r^2/n\right).
\tag{7.2a}
$$
明确公式 (7.1)–(7.2) 保留所有常数；本条不把增长 $r$ 藏入固定参数记号。

### 7.3 强尾物理还原

令 $y=m+R/2,c=y^{-2}$。
中位强尾成本不超过 $4^R$；
只需将坏链 $l\le d+r-2$ 从 $cL_l$ 化为单位链，
实际坏链还满足 $l\le R+1$，所以额外条件数不超过
$$
y^{2\min(R,d+r-3)}\le y^{2(d+r-3)}.
$$
因为 $l\le R+1$ 且 $R\ge d$，所用 $cl/2\le1$ 对全部实际链成立，
无需在这里假设 $r$ 小。

源以 $\mathcal S^*\xi$ 进入，候选以
$\mathcal S^{-*}\widetilde q$ 还原，二者只合计一个真实相似条件数。
于是对全部 $0<s,\gamma\le1$，
$$
\boxed{
\|q_{-1}(s)\|
\le C_{m,r}\,4^R\,y^{2(d+r-3)}
s^{2A_0-N-r+1}\gamma^{A_0-1}\mathcal Z_\gamma(s).
}
\tag{7.3}
$$
取 $\gamma=s$ 得同样明确的原 $s$ 权源界。
所有 $R,r$ 成本、完整真核域与物理还原均保留。

## 8. 与原允许高度窗、母窗的确切相容性

原 $m\ge20$、偶 $R\ge d$、$x=m+R$ 时，
所有允许奇高度
$$
1\le r\le
1+\left\lfloor\frac{\sqrt{x+1}}{8(m+1)}\right\rfloor
\tag{8.1}
$$
均满足 $r\le R-n+1$。
所以实际长链段存在，$A_s\ge1$，
不需要使用 §6 的退化零级情形。

当 $R=d$ 时，(8.1) 还远小于
$n/2-m+1=d/4-m+1$，故恢复 $A_0=A_l$。
取原 $Q=4d$，仍有 $R+r\le Q$，并在原同 $w$ 母窗内。
这覆盖此前分离高度带中取出的全部奇高度，
没有将不在允许窗的小头特例冒充移动头结果。

若需要把 $R$ 增大到支付 $d^4$ 头费用，
(8.1) 中的 $r$ 可能超过 (5.3)；
此时正短链门给
$$
A_0=(R-n-r+3)/2,\qquad
\beta=-n-m-2r+4.
$$
因此 $s$ 的负指数仍只有 $O(d+r)$，
而 $\gamma^{A_0-1}$ 的指数为 $R/2-O(d+r)$。
原 (8.1) 还给
$$
r^2/n=O\!\left(R/(m^2d)+1\right),
$$
所以显式合同的新增 $\exp(12r^2/n)$ 只占一个可见的小线性 $R$ 项。
只要所选 $Q\ge R+r$ 仍在原母窗内，这里没有额外的小 $r$ 阻断。
例如任何固定次数多项式 $R(d)$，可先取 $Q=4R$ 并逐项核原母窗；
该几何选择不代替实际源费用。

(7.3) 仍需要原 $\mathcal Z_\gamma(s_*)$ 的实际可支付上界。
其中 $\gamma<1/16$ 可以在几何上压过 $4^R$，
但本文没有无证地给 $\mathcal Z_\gamma$ 一个统一常数。
完整正则部分可另用[全实参数线性图定理](R271-appendix-complete-highest-carry-linear-graphs-and-full-interval-regular-cost.md)估计；
该粗上界是否够小仍是独立费用问题。
