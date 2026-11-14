# R269 — 实际 theta 权、五条原 companion 与三曲线完整中央返回

日期：2026-11-13。**状态：R268 的 de Rham 分解已经乘回原相邻 theta 来源；全部 apparent poles、原点质量、五条具体列、三阶 Mellin 转置及原三条曲线的真实返回均已证明。尚未从三条中央零推出裸 de Rham/Cartier 类消失。**

本篇接续 [R265](R265-nonbeta-full-transport-cm-boundaries-and-complete-connection.md)
的全十九坐标图与 [R268](R268-normtwo-de-rham-dual-cartier-and-unipotent-connection.md)
的实际余核。它与 R266 的普通 theta–Cartier 公式不同：本篇的惰性 frame
使用 R166 的真实 $[p]$ 除法式和 R247 的共同整参考，不移用普通 $\mu_p$ 或 étale CM 公式。

## 1. 将原微分准确乘回原相邻 theta 截面

固定既有规范
$$
E_0:y^2=x^3-x,\quad dz=\frac{dx}{2y},\quad U=x^2,
\quad D=U^8(U-1)^8,
$$
$$
F=S_8^{17}=WD,\quad S_8=-y\vartheta\sigma^3,\quad
W=-y\vartheta\sigma^{67},\quad \nabla_F=\partial_z-F'/F.
$$
对 $\deg Q\le16$，实际相邻来源是
$$
C_Q=\frac WxQ(U).
$$
R268 给出的微分及原函数为
$$
\eta_Q=\frac{4P_8(U)(U-1)Q(U)}{xU^8}\,dz
=d\mathcal R_Q+\lambda\ell(Q)x\,dz,
\tag{1}
$$
其中 $\mathcal R_Q=yR_Q(x)$，$R_Q$ 是已明确列出的奇 Laurent 多项式，
$$
\lambda=\frac{17179869184}{644658718275},
$$
$P_8$ 和本原整数泛函 $\ell$ 均为 R264 的原对象。

所需的实际 theta 权并非任意 $G$，而是
$$
\boxed{a(z)=\frac1{4P_8(U)(U-1)^9},\qquad
Fa\,\eta_Q=C_Q\,dz.}
\tag{2}
$$
式 (2) 直接由 $F=WD$ 约分得到。若要得到正权 $WQ\,dz$，须再乘一个 $x$；
本篇始终保相邻权，因而不加该因子。

定义三个真实 companion
$$
B_Q=Fa\mathcal R_Q,\qquad
E_Q=-Fa'\mathcal R_Q,\qquad H_0=Fax.
\tag{3}
$$
因为 $\nabla_F(Fg)=Fg'$，(1)、(2) 给出完整源恒等式
$$
\boxed{C_Q=\nabla_FB_Q+E_Q+\lambda\ell(Q)H_0.}
\tag{4}
$$
所以
$$
\boxed{\nabla_F^2C_Q
=\nabla_F^3B_Q+\nabla_F^2E_Q
 +\lambda\ell(Q)\nabla_F^2H_0.}
\tag{5}
$$
$E_Q$ 就是把 de Rham 原函数乘回真实 theta 权时留下的原连接项。
即使 $\ell(Q)=0$，它也仍在 (4)、(5) 中。

## 2. 同一原参数中的有限多项式恒等式

取原参数
$$
u=x^{-1/2}=z+O(z^5),\qquad s=u^4,\qquad
t=\sqrt{1-s},\qquad F=\vartheta^{68}t^{17},
$$
平方根恒取原点值一。令
$$
P(s)=s^8P_8(1/s),\qquad q(s)=s^{16}Q(1/s).
$$
R268 的 $R_Q$ 只含 $-17\le k\le31$ 的奇次幂，故可唯一写成
$$
\mathcal R_Q=yx^{-17}A_Q(U),\quad\deg A_Q\le24,
\qquad J_Q(s)=s^{24}A_Q(1/s).
$$
在这些原坐标中，(3) 准确成为
$$
\boxed{\begin{aligned}
B_Q&=\vartheta^{68}u^3b_Q(s),
&b_Q&=-\frac{J_Q}{4P},\\
E_Q&=\vartheta^{68}u^2t\,e_Q(s),
&e_Q&=\frac{J_Q\{(17-8s)P-s(1-s)P'\}}{P^2(1-s)},\\
H_0&=\vartheta^{68}u^2t\,h(s),
&h&=\frac{s^{16}}{4P(1-s)}.
\end{aligned}}
\tag{6}
$$
这里 $P',J_Q'$ 是 $s$ 导数。
利用 $u'=t$，可直接算出
$$
\frac{\nabla_FB_Q}{\vartheta^{68}u^2t}
=3b_Q+4sb_Q'+\frac{34s}{1-s}b_Q.
$$
所以 (4) 等价于一个完全有限的多项式恒等式：
$$
\boxed{4P(1-s)q
=-4s(1-s)J_Q'+(65-63s)J_Q+\lambda\ell(Q)s^{16}.}
\tag{7}
$$
随文证书对 $Q=1,U,\ldots,U^{16}$ 的全部十七列逐系数核实 (7)，
并保存 $Q\mapsto J_Q$ 的完整 $25\times17$ 矩阵。该矩阵的秩为十七。
因此本篇使用的是五条指定原 companion 的真实原函数，未用自由选择的局部原函数代替。

### 2.1 全部极点和原点质量

$P_8$ 的根均简单，且不为 $0,1$。在这些根上，$B_Q,H_0$ 至多有一阶极，
$E_Q$ 至多有二阶极；(5) 的三项至多出现四阶极。
式 (7) 先证明 (4) 整组没有这些极，再求两次真实协变导数，证明 (5)
在同一除子上的全部极准确抵消。没有将任何单项称作全局全纯 theta 截面。

在 $T_\pm$，$B_Q$ 正则，$E_Q,H_0$ 至多有一阶极。
求导后仍按 (5) 整组相消，最后只留下 R265 已付的
$$
-1190Q(0)\frac WU+1088Q(1)\frac W{U-1}.
\tag{8}
$$
因此结果确实回到原“十七个全纯坐标加两个实际极坐标”，没有新增未记账的极层。

在原点，准确有
$$
\boxed{B_Q= -\frac{Q_{16}}{65}z^3+O(z^7),\qquad
E_Q=\frac{68Q_{16}}{65}z^2+O(z^6),\qquad H_0=O(z^{66}).}
\tag{9}
$$
例如 $Q=U^{16}$ 时，(5) 的质量为
$$
6\left(-\frac1{65}\right)+2\left(\frac{68}{65}\right)=2,
\tag{10}
$$
恰为 $\nabla_F^2C_Q$ 的原质量。
连接项不是可忽略的小量：仅保留原函数项会把这个质量算错。

原 dyadic 返回的自然分支原点都是 R246/R250 的实际奇八挠点。
证书用原 $\psi_8/y$ 除法多项式核实
$$
\gcd(P_8,\psi_8/y)=1.
\tag{11}
$$
它们也不属于 $T_\pm$。因此 (3) 在全部实际分支原点有合法 germ。
后续除去 (11) 非零固定 resultant 及已有固定代数分母的有限坏素位，
即可在原正式盘内同时使用这些分支。其 resultant 完整保存，不以若干浮点 torsion 值替代。

## 3. 原两列、原两伴随和无对数列的明确坐标

令 $H_j^{\rm new}$ 是 R254 原相邻十七维中的四个八次来源，均以 $z^2$ 系数一归一，
$\delta_j$ 是其已付的原正向 dyadic 系数。用 R235 的原 $a_j,b_j$ 定义
$$
Q_A=\sum_j a_j\delta_jH_j^{\rm new},\qquad
Q_{B^+}=\sum_j b_j\delta_jH_j^{\rm new}.
\tag{12}
$$
本式将 $H_j^{\rm new}$ 视为其升幂多项式。
R254 的全部十七坐标核对给
$$
\mathcal V(C_{Q_A}(2z))=C_A(2z),
$$
$$
\kappa_4^{-1}Q_{+,0}\mathcal V(C_{Q_{B^+}}(2z))=C_B^+(2z).
\tag{13}
$$
第二式之后仍须使用 R235 的原 $\operatorname{Reg}$ 和三个 CM 修正，才是完整 $C_B$。
本篇没有把这个有限恢复算子无证延长到 (3) 的各个单独 meromorphic 分量。

另三列取自 R245/R251：$Q_*$、$Q_2$ 是 $C_*,C_2$ 的原有理部分，
$$
C_*=C_{Q_*}-\frac{\gamma_*}{8}FL,\qquad
C_2=C_{Q_2}-\frac{\gamma_2}{8}FL,
\quad L=\log\frac{x-1}{x+1},
$$
$$
\gamma_* =\frac{402182437912192}{106525601325},\qquad
\gamma_2=-\frac{471121690512128}{645609705},\qquad
\tau=\frac{\gamma_2}{\gamma_*}=-\frac{607305304175790}{3142050296189}.
\tag{14}
$$
令 $Q_\circ=Q_2-\tau Q_*$。下面均为直接在原整数余核 $\ell$ 上计算的准确值：

| 原列 | $\ell(Q)$ | $[U^{16}]Q$ |
|---|---:|---:|
| $Q_A$ | $171893911321984i/28875$ | $-2873i/92400$ |
| $Q_{B^+}$ | $-2121752694058327i/273000$ | $12250247i/3748659200$ |
| $Q_*$ | $-10517471000491721768192/369111208591125$ | $-100545609478048/106525601325$ |
| $Q_2$ | $210114934005359983616/19119979725$ | $235561490865769/1291219410$ |
| $Q_\circ$ | $11638033428105690498006936064/2123004833877502575$ | $1/2$ |

原两列的实际边界是
$$
\begin{array}{c|cc}
 &Q(0)&Q(1)\\ \hline
Q_A&199i/924000&1850368i/9625\\
Q_{B^+}&3415177i/56229888000&9733111i/92400.
\end{array}
\tag{15}
$$
而 $Q_*,Q_2,Q_\circ$ 在 $0,1$ 均为零。
因此前两列在 (5) 中的 (8) 必须保留；后三列确实全局正则。
加回 (14) 的原 log 后，$C_*$ 的 $z^2$ 系数为零，$C_2$ 为 $1/2$，与 R245/R251 相同。

五列全部的 $Q,J_Q$、两条 CM 边界系数、完整十九坐标和
R265 真正 $T_-^{-1}$ 的原像均已保存。
准确回乘 $T_-T_-^{-1}Q=Q$，证明这些列确在同一非 beta 载体图中，
没有用函数域维数来代替原坐标返回。

### 3.1 四个不同条件没有未记录的共同消去

对四列 $(Q_A,Q_{B^+},Q_*,Q_2)$，依次取边界 $Q(0),Q(1)$、
de Rham 系数 $\ell(Q)$ 和原 log 系数 $\gamma$，得到准确矩阵
$$
\mathcal B=\begin{pmatrix}
 Q_A(0)&Q_{B^+}(0)&0&0\\
 Q_A(1)&Q_{B^+}(1)&0&0\\
 \ell(Q_A)&\ell(Q_{B^+})&\ell(Q_*)&\ell(Q_2)\\
 0&0&\gamma_*&\gamma_2
\end{pmatrix}.
$$
其两个关键行列式为
$$
\boxed{\det\mathcal B_{\rm boundary}
=-\frac{9399989227}{853776000000},\qquad
\det\mathcal B
=\frac{13674673605957421212332682996609722816}
{60011686317469517490234375}\ne0.}
\tag{16}
$$
因此没有非零固定代数组合能同时清掉这四种实际条件。
第五列只有已付关系 $Q_\circ=Q_2-\tau Q_*$，不会再添一条独立消去。
(16) 的用途是核实具体列之间的相容性；它不是一个原中央泛函矩阵，
也没有替代下面的完整 theta 连接项。

## 4. 惰性 theta frame 的实际 Frobenius 与共同整参考

R166 已证明原整数除法式
$$
\vartheta(pz)=H_p(s)\vartheta(z)^{p^2},\qquad
\Phi_p(s)=s(pz)=s(D_p/H_p)^4,
$$
$$
H_p\equiv1,\qquad D_p\equiv-s^{(p^2-1)/4},\qquad
\Phi_p\equiv s^{p^2}\pmod p.
\tag{17}
$$
因此本篇实际 $F=\vartheta^{68}(1-s)^{17/2}$ 满足
$$
\boxed{
\frac{F(pz)}{F(z)^{p^2}}
=H_p(s)^{68}
\left(\frac{1-\Phi_p(s)}{(1-s)^{p^2}}\right)^{17/2}
\in1+ps\mathcal O_p[[s]].}
\tag{18}
$$
平方根分支由原点值一固定。对于 (6) 的固定角函数，先保留其原点单项式和
固定首系数，再将剩下的单位归一到一；其 Frobenius 商还须准确乘
$v(\Phi_p)/v^{p^2}$。在固定坏素位外这仍是 $1+ps\mathcal O_p[[s]]$。
物理零阶 $u^3,u^2,s^{16}$ 从未被作为单位删除。
完整 ghost 展开使用 R166 的原 $\Phi_p$；实际 theta 次数仍从 $68$ 变为 $68p^2$。

对前三中央权，(6) 可以更明确地放进 R247 同一整参考。
写 $p=4r-1$，并用 $\mathsf F(s)$ 表示原椭圆对数因子，以区别本篇的 theta frame $F$：
$$
z=u\mathsf F(s),\qquad
\mathsf G=\mathsf F+4s\mathsf F'=(1-s)^{-1/2}.
$$
令 $\widetilde\Gamma$ 是 R247 的共同整参考。对 $n=1,2,3$，(6) 的实际整行为
$$
\boxed{\begin{aligned}
\mathcal D_{n,k}^{B_Q}
 &=[s^{nr}]\widetilde\Gamma\,
       \frac{b_Q\mathsf G}{\mathsf F^{n+4}}(\log\mathsf F)^k,\\
\mathcal D_{n,k}^{E_Q}
 &=[s^{nr}]\widetilde\Gamma\,
       \frac{e_Q}{\mathsf F^{n+3}}(\log\mathsf F)^k,\\
\mathcal D_{n,k}^{H_0}
 &=[s^{nr}]\widetilde\Gamma\,
       \frac{s^{16}}{4P(1-s)\mathsf F^{n+3}}(\log\mathsf F)^k.
\end{aligned}}
\tag{19}
$$
分别对应 $B_Q/z^3,E_Q/z^2,H_0/z^2$。
后两行的原平方根只在实际 Lagrange 核中相消。
全部角分母在所取正式盘内为单位，且所读 $s$ 次数小于 $3r<p$，
所以 R247 的整性、真实下一位和第三权几何 carry 原样适用。

这些单位角函数没有改变共同 theta 首 carry
$$
p[s^r]\log\vartheta^{68}\equiv68\kappa\pmod p,
\qquad \kappa=\frac{\binom{2r-2}{r-1}}{4^{r-1}}\ne0.
\tag{20}
$$
因此裸 $\mathcal C(\eta_Q)$ 只读 $\ell(Q)$，并不意味着实际原行只读它。
(19) 显示真实 theta 权、原椭圆对数因子及全部移动 log 项均继续存在。
本节没有把三个有限权逐个置零，也没有将普通 Cartier 的 étale 公式用于惰性处。

## 5. 完整一阶、二阶、三阶 Mellin 算子

固定 $d=p+1,c=68c_0$，置
$$
W_F=zF'/F,\quad W_0=W_F-dcz^d,\quad\mathcal E=z\partial_z.
$$
对一个从 $z^j$ 起的聚合 companion $Y$，记 $v=Y/z^j$，并定义
$$
f_0=\mathcal J_c(v),\quad f_1=\mathcal J_c(W_0v),\quad
f_2=\mathcal J_c((W_0^2+\mathcal EW_0)v),
$$
$$
f_3=\mathcal J_c((W_0^3+3W_0\mathcal EW_0+\mathcal E^2W_0)v).
\tag{21}
$$
所有函数保留全变量 $u$。令 $t=du$。
一阶和二阶的准确全体 $u$ 式是
$$
\boxed{\mathfrak D_1(Y;u)=(t+1)f_0(u)-f_1(u)-duf_0(u-1),}
\tag{22}
$$
$$
\boxed{\begin{aligned}
\mathfrak D_2(Y;u)={}&(t+1)(t+2)f_0(u)-(2t+3)f_1(u)+f_2(u)\\
&+du\{(d-2t-3)f_0(u-1)+2f_1(u-1)\}\\
&+d^2u(u-1)f_0(u-2).
\end{aligned}}
\tag{23}
$$
它们分别等于 $\mathcal J_c(\nabla_FY)$ 和 $\mathcal J_c(\nabla_F^2Y)$。

三阶令 $A(t)=3t^2+12t+11$、$B(t)=3t+6$，则
$$
\boxed{\begin{aligned}
\mathfrak D_3(Y;u)={}&(t+1)(t+2)(t+3)f_0(u)-A(t)f_1(u)
 +B(t)f_2(u)-f_3(u)\\
&+du\{[-A(t)+dB(t)-d^2]f_0(u-1)\\
&\hspace{36mm}+[2B(t)-3d]f_1(u-1)-3f_2(u-1)\}\\
&+d^2u(u-1)\{[B(t)-3d]f_0(u-2)-3f_1(u-2)\}\\
&-d^3u(u-1)(u-2)f_0(u-3).
\end{aligned}}
\tag{24}
$$
这准确等于 $\mathcal J_c(\nabla_F^3Y;u)$。
证明是将 $(\mathcal E-W_F+1)(\mathcal E-W_F+2)(\mathcal E-W_F+3)$
完全左正规排序，再用原 $\mathcal J_c(\mathcal EA)=du\mathcal J_c(A)$
和 $\mathcal J_c(cz^dA)=u\mathcal J_c(A;u-1)$。
证书逐项核实三阶的四个移权多项式。

例如求 (24) 的中央导数时，必须保留 $11df_0(0)$，以及
$$
d\{(-11+6d-d^2)f_0(-1)+(12-3d)f_1(-1)-3f_2(-1)\},
$$
$$
-d^2\{(6-3d)f_0(-2)-3f_1(-2)\}-2d^3f_0(-3),
\tag{25}
$$
同时保留 $6f_0'(0)-11f_1'(0)+6f_2'(0)-f_3'(0)$
和 $-12df_1(0)+3df_2(0)$。所以这里没有把三阶式缩成一个未移权导数。

由 (5)，原相邻列的完整中央函数现在准确为
$$
\boxed{\mathcal J_c(\nabla_F^2C_Q;u)
=\mathfrak D_3(B_Q;u)+\mathfrak D_2(E_Q;u)
 +\lambda\ell(Q)\mathfrak D_2(H_0;u).}
\tag{26}
$$
含原 log 的 $C_*,C_2$ 还须减去 $\gamma_*/8$、$\gamma_2/8$ 乘
$\mathfrak D_2(FL;u)$；R245 的完整 log 尾仍在该项中。

## 6. 全部分支先聚合，再作原点除阶

原三曲线返回仅使用 R246/R250 已付的实际 $\mathcal V$ 与 $Q_{+,v}$。
写其中任一个为 $\mathcal O=\sum_\nu b_\nu T_\nu$。
这些 dyadic 分支斜率为一，所有 Mumford/Gaussian 因子都在 $T_\nu$ 内。
作共同 $[2]$，令 $F_2=F(2z)$，在原目标采用
$\Theta_2=\vartheta(4z)^{17}$、$\nabla_0=\partial-\Theta_2'/\Theta_2$，并置
$$
a_\nu=\partial\log\frac{T_\nu F_2}{\Theta_2}.
$$
准确链式法则为
$$
T_\nu\nabla_{F_2}^j=(\nabla_0-a_\nu)^jT_\nu.
\tag{27}
$$
以下将 $Y_B=T_\nu B_Q(2z)$、$Y_E=T_\nu E_Q(2z)$、
$Y_H=T_\nu H_0(2z)$、$Y_L=T_\nu(FL)(2z)$。
对原 log 系数 $\gamma$，定义四个完整聚合来源
$$
\begin{aligned}
Z_3={}&\sum_\nu b_\nu Y_B/8,\\
Z_2={}&\sum_\nu b_\nu\{-3a_\nu Y_B/8+Y_E/4
             +\lambda\ell(Q)Y_H/4-\gamma Y_L/32\},\\
Z_1={}&\sum_\nu b_\nu\{3(a_\nu^2+a_\nu')Y_B/8
             -a_\nu Y_E/2-\lambda\ell(Q)a_\nu Y_H/2
             +\gamma a_\nu Y_L/16\},\\
Z_0={}&\sum_\nu b_\nu\{-(a_\nu^3+3a_\nu a_\nu'+a_\nu'')Y_B/8\\
 &\hspace{25mm}+(a_\nu^2+a_\nu')Y_E/4
             +\lambda\ell(Q)(a_\nu^2+a_\nu')Y_H/4
             -\gamma(a_\nu^2+a_\nu')Y_L/32\}.
\end{aligned}
\tag{28}
$$
这里的 $1/8,1/4$ 是真实 $[2]$ 的三阶、二阶缩放；原 log 项同时保留其 $1/8$ 系数。
把 (27) 左正规排序，准确得到
$$
\boxed{\mathcal O\left(
 [\nabla_F^2(C_Q-\gamma FL/8)](2z)\right)
=\nabla_0^3Z_3+\nabla_0^2Z_2+\nabla_0Z_1+Z_0.}
\tag{29}
$$
所有 $a_\nu'$、$a_\nu''$ 都在 (28) 中；没有省去 frame 交换差。

原算子与 $i$ 相容，分支在 $i$ 作用下完整置换。
于是聚合后的 $Z_j$ 具有真实特征 $i^j$。
由 §2.1 的分支正则性，$Z_j=O(z^j)$，$j=1,2,3$。
**只在这一步聚合之后**，才将它们分别除以 $z^3,z^2,z$。
单个 $Y_B$ 通常不从 $z^3$ 起，不能对单分支作该除法。

因此在 $4c=272c_0$ 的原目标 gauge 上，(29) 的完整转置是
$$
\boxed{\mathcal E_{\mathcal O}(Q,\gamma;u)
=\mathfrak D_3^{\Theta_2}(Z_3;u)
 +\mathfrak D_2^{\Theta_2}(Z_2;u)
 +\mathfrak D_1^{\Theta_2}(Z_1;u)
 +\mathcal J_{4c}(Z_0;u).}
\tag{30}
$$
上标表示 (21)–(24) 采用该真实目标 frame 和 $4c$。
(28) 的原点质量及 (30) 的全部移权均保留。
固定有理角分母和 prime-to-$p$ 平移的 Gauss 成本按 R245/R254 支付，
故 (26)、(30) 使用完整收敛尾，不是有限权替代。

## 7. 原三条 rank-two 曲线的准确全体中央行

以下只用原三个合法来源
$$
A=A_{17}(2z)/16,\qquad B=A_{34}(z),\qquad H=A_{136}(z).
$$
令
$$
K_I=\frac{S_8(\bar\beta z)-S_8(\beta z)}{2i},\quad
\beta=4-i,\quad\bar\beta=4+i,
$$
$$
a_*^{\rm CM}=-\frac{14548243}{4370281080},\qquad
a_2=\frac{8235327}{3310819}.
$$
这里 $a_*^{\rm CM}$ 是 R245 原 CM 系数，不是 R264 的 de Rham 周期 $a_*$。
原完整恒等式为
$$
\nabla_F^2C_*=H-a_*^{\rm CM}K_I,\qquad
\nabla_F^2C_2=S_{2312}-a_2K_I.
\tag{31}
$$

定义未经 dyadic 运输的实际函数
$$
\begin{aligned}
\mathcal N(Q,\gamma;u)={}&\mathfrak D_3(B_Q;u)
 +\mathfrak D_2(E_Q;u)+\lambda\ell(Q)\mathfrak D_2(H_0;u)\\
&-\gamma\mathfrak D_2(FL;u)/8.
\end{aligned}
$$
取 $q_2=2^{p-1}$、$q_4=4^{p-1}$、$\kappa_4=2^{-1/4}$。
R246/R250 的真实原返回是
$$
\mathcal V(H(2z))=\frac{8i}{11}A(2z),\qquad
Q_{+,v}(S_{2312}(2z))=-640i\kappa_4B(2z).
\tag{32}
$$
因此三条完整中央函数准确写成
$$
\boxed{\begin{aligned}
J_H(u)&=\mathcal N(Q_*,\gamma_*;u)
                 +a_*^{\rm CM}\mathcal J_c(K_I;u),\\
\frac{8i}{11}q_2^uJ_A(u)
 &=\mathcal E_{\mathcal V}(Q_*,\gamma_*;u)
                 +a_*^{\rm CM}\mathcal J_{4c}(\mathcal V K_I(2z);u),\\
-640i\kappa_4q_2^uJ_B(u)
 &=\mathcal E_{Q_{+,v}}(Q_2,\gamma_2;u)
                 +a_2\mathcal J_{4c}(Q_{+,v}K_I(2z);u).
\end{aligned}}
\tag{33}
$$
这里的 $J_A,J_B,J_H$ 就是原三来源在同一自然 $c=68c_0$ 上的完整变换。
所以本篇没有只把新函数送到某个同维空间，而是送回原三条中央问题。

### 7.1 原 CM 参考的相位、质量和全部单位

令 $F_0=(x^2-1)\sigma^4$，并记其原完整参考为 $J_0$，
$S_8$、$\vartheta$ 的参考分别为 $J_8,J_\vartheta$，三者中心值均一。
设
$$
U_{\beta,p}=\frac{\beta^{p+1}}{17},\qquad
U_{\bar\beta,p}=\frac{\bar\beta^{p+1}}{17}.
$$
原规范给出
$$
\boxed{\begin{aligned}
\mathcal J_c(K_I;u)
 &=\frac{U_{\bar\beta,p}^u-U_{\beta,p}^u}{2i}J_8(u),\\
\mathcal J_{4c}(\mathcal V K_I(2z);u)
 &=\frac{q_4^u}{2i}
       (U_{\bar\beta,p}^u+U_{\beta,p}^u)J_\vartheta(u),\\
\mathcal J_{4c}(Q_{+,v}K_I(2z);u)
 &=-i\kappa_4q_2^u
       (U_{\bar\beta,p}^u+U_{\beta,p}^u)J_0(u).
\end{aligned}}
\tag{34}
$$
第二、三行的质量分别为 $-i$、$-2i\kappa_4$。
它们在 (33) 中由实际连接块的质量准确补偿；不能因三个曲线来源质量零
就将这些内部参考质量也当零。
求导时保留 $J_\vartheta'(0),J_0'(0)$、全部 $\log_pq_2,\log_pq_4$
及 $\log_pU_{\beta,p},\log_pU_{\bar\beta,p}$。
只有第一行的差准确消去共同参考导数，得到原 norm-one-$17$ 对数。

若原三个中央导数都为零，(33) 使三条右侧的**完整聚合**同时为零。
它没有使 (28) 的任一个 $Z_j$、(19) 的任一有限权或裸 $\ell(Q)$ 分别为零。
这一区别在本篇由实际 theta 权和全部移权公式明确给出。

## 8. 已付图与可用范围

(7) 支付了原 de Rham 原函数乘 theta frame 后的全部极；
(12)–(16) 指定同一原 $C_A,C_B^+,C_*,C_2,C_\circ$ 的具体列；
(17)–(20) 保留惰性实际 Frobenius、共同 gauge 和首 carry；
(28)–(34) 将全部三阶连接返回原三条曲线。
这四步各有不同用途，不能把 (16) 的有限行列式当作 (33) 的中央行列式。

另外，R264 的水平来源 $S_*=Fh_*=WU^8P_8(U)$ 不能免费改称一个已知 CM 参考。
在 R248 的原 CM5 矩阵中，$S_*$ 与 $NS_*$ 的拼接秩为二，
其五块投影外的十二角色余项非零。证书保存全部五个系数和余项。
所以该水平核与 (34) 的三条已知参考仍是不同的实际来源。

目前尚未证明三条完整中央零会迫 (33) 的连接聚合消失为某个单独 de Rham 条件，
也未证明它们在 R265 整个十七维运输图下闭合。
本篇给出了这一步必须比较的原固定五列、原点质量、全部连接块和真实参考单位。

## 精确证书

- [脚本](../scripts/check-actual-companion-theta-derham-frame.py) 与
  [完整输出](../scripts/check-actual-companion-theta-derham-frame.json)
  的 $139$ 项精确检查全部通过。输出给出全部十七条实际原函数、五列具体坐标、
  十九坐标返回、CM 边界、完整三阶正规排序、四个聚合分支块和八挠极回避证书。
- 全体计算在固定精确数域中完成，没有扫描目标素数或按数值样本识别函数。
- 原有限 dyadic 相位与三来源身份依赖 R239/R246/R250；
  原 companion 与完整 log 依赖 R245/R251；实际 de Rham 依赖 R264/R268；
  惰性 frame 和完整低权整参考分别依赖 R166/R247。
