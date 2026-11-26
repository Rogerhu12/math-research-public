# R150 附录：rankH3 约化退化 Gram 的本质六维支只余非零 F 的双约化零 Hp 型

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明的必要归约。** 假设原完整临界点 $\operatorname{rank}H=3,\operatorname{rank}V=2$、$\dim\operatorname{ess}(T_3)=6$，且 H 的唯一物理长度三支撑为三个不同点、它的原 Gram 退化。则 V 必为两个不同点，且 $F\ne0,Hp=0$；H Gram 必为秩二、恰有一条零边。本文完整排除了 $F=0$、V 的二重 jet、以及 $F\ne0,Hp\ne0$ 三个范围，不声称最后零 Hp 型为空。

## 1. 原方程、满空间独立性与 H 的全部退化 Gram

原定义为
$$
p=Ky,\quad F=\tfrac12y^{\mathsf T}Ky,\quad
b_0=p^{\mathsf T}Hp,\quad\tau_2=\operatorname{tr}((KH)^2),
$$
$$
T_3=y^3-6yH+4V.
$$
仍保[原完整三阶矩公式](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)的
$$
\Gamma=(F^2-2b_0+2\tau_2)y-4FHp+8HKHp
+4V(p,p,\cdot)-8V:(KHK),
\tag{1.1}
$$
$$
N=Fyy^{\mathsf T}-2FH-2\{y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\}
+4HKH+4V_p.
\tag{1.2}
$$
完整临界性给 $\Gamma=0$、全部原物理极线恒等式 $k_x^{\mathsf T}Nk_x=0$，以及最高式
$$
P(x)^3-6P(x)G_H(x)+4V(k_x,k_x,k_x)=0,
\quad k_x=Ku(x),\quad P(x)=p^{\mathsf T}u(x).
\tag{1.3}
$$

H 的三个非零原子权可吸收到平方根，准确写为
$$
H=\tfrac12(z_1^2+z_2^2+z_3^2).
\tag{1.4}
$$
三个 $z_i$ 都是真实物理点的非零代表，允许无穷远。其 Gram 零对角，行列式是三个非对角配对乘积的两倍。退化性遂允许重编号使
$$
B=(z_i^{\mathsf T}Kz_j)=
\begin{pmatrix}0&g&h\\g&0&0\\h&0&0\end{pmatrix},
\qquad \sigma=g^2+h^2.
\tag{1.5}
$$
$g,h$ 可零，且 $\sigma$ 可零；这些边界均保留。

令 $a_i=p^{\mathsf T}z_i$、$a=(a_1,a_2,a_3)^{\mathsf T}$。由于
$$
T_3\text{ 支持于 }\mathbb Cy+\operatorname{Ran}H+\operatorname{Ran}V
$$
且假设本质维数六，$(y,z_1,z_2,z_3,u,v)$ 必构成整个原六维空间的一组基，其中 $u,v$ 是 V 的两个值或两个 jet 列。这是反设推出的独立性，不是新增共支撑假设。原 K 在该基中的 Gram 必可逆。

在完整 mean 向量中，Gaussian 部分与 V 部分分别属于独立的四空间、二空间。所以 Gaussian 系数给
$$
\boxed{Ba=Fa,\qquad a^{\mathsf T}a=F^2+\sigma.}
\tag{1.6}
$$
这里 $B^3=\sigma B$，故 $B^3$ 的对角线全零。完整 N 在每个实际 H 物理点评价，准确给
$$
\boxed{4V_p(Kz_i,Kz_i)=F\{a_i^2+(B^2)_{ii}\}.}
\tag{1.7}
$$
证明是把 (1.2) 的该评价写成
$Fa_i^2-F(B^2)_{ii}-2a_i(Ba)_i+(B^3)_{ii}+4V_p(Kz_i,Kz_i)$，
再用 (1.6)。没有只取受限 H 参数梯度。

## 2. V 两种类型的全部原 mean / 最高后果

若 V 约化，可准确规范为
$$
V=\tfrac12(u^3+v^3),\qquad e=uKv.
$$
记 $c_i=z_iKu,d_i=z_iKv$，写 $c,d$ 为两个三列。独立的 V mean 系数及最高式在 V 值处评价给
$$
p(u)^2=c^{\mathsf T}c,\quad p(v)^2=d^{\mathsf T}d,\quad
p(u)^3=p(v)^3=e^3.
\tag{2.1}
$$
若 $e=0$，便有 $p(u)=p(v)=0,V_p=0$。若 $e\ne0$，用保 $V$ 的三次单位根尺度可使
$$
p(u)=p(v)=e,\quad c^{\mathsf T}c=d^{\mathsf T}d=e^2,\quad
V_p=\tfrac e2(u^2+v^2).
\tag{2.2}
$$
(1.7) 求和给
$$
\boxed{4e^3=F(F^2+3\sigma).}
\tag{2.3}
$$
该式在 $e=0$ 时也成立。

若 V 非约化，保全部 value 权写
$$
V=\alpha u^3+\beta\operatorname{Sym}_{\Sigma}(u^2v),\qquad\beta\ne0.
$$
物理关系为 $uKu=uKv=0$，而 $vKv$ 可非零。原两个 V mean 系数与最高式在 u 处的评价给
$$
\boxed{
p(u)=0,\quad c^{\mathsf T}c=0,\quad c^{\mathsf T}d=0,\quad
V_p=\beta t\,u^2,\quad t=p(v).
}
\tag{2.4}
$$
其推导与前[rankH2 全类型稿](R150-appendix-rank-two-second-and-third-cumulants-with-a-tangent-support-have-essential-dimension-at-most-four.md) §2 相同，只把 $G_H(u)=\tfrac12c^{\mathsf T}c$ 保为三列。用 (1.7) 求和，得到
$$
\boxed{F(F^2+3\sigma)=0.}
\tag{2.5}
$$

若此时 $F\ne0$，(1.6) 有两种且仅两种情形：$a=0$ 时 $\sigma=-F^2$；$a\ne0$ 时，$Ba=Fa$ 与 $B^3=\sigma B$ 给 $\sigma=F^2$。两者都与 (2.5) 矛盾。所以非约化 V 必落 $F=0$。下一节将把所有 $F=0$ 一并排除。

## 3. $F=0$ 先把 V 收缩完全消去

若 V 约化，(2.3) 给 $e=0$，于是 $p(u)=p(v)=0,V_p=0$。

若 V 非约化，(1.7) 给 $\beta t c_i^2=0$ 对三个 i 全成立。假设 $t\ne0$，则 $c=0$，所以 u 正交于全部 $z_i$；(2.4) 又给 u 正交于 y、u、v。六列是一组基，K 可逆，故 u=0，矛盾。因此仍有
$$
\boxed{p(u)=p(v)=0,\qquad V_p=0.}
\tag{3.1}
$$

### 3.1 $B=0$

此时 $HKH=0$，完整 N 只余 $-2\operatorname{Sym}_{\Sigma}(y\otimes Hp)$。其原极线式是 $P\,k_{Hp}=0$。因 $P\ne0$、多项式整环无零因子、K 可逆，得到 $Hp=0$，即 $a=0$。结合 (3.1)、$F=0$，y 正交于六列基中的每一列，矛盾。

### 3.2 $B\ne0,\sigma=0$

此时 $g,h$ 都非零。令
$$
L=gz_2+hz_3.
$$
$Ba=0$ 的核由 $(0,g,h)$ 张成，故 $a=\lambda(0,g,h)$。于是
$$
Hp=\tfrac{\lambda}{2}L,\qquad
4HKH=z_1\otimes L+L\otimes z_1.
$$
用 (3.1)，完整 N 成为
$$
N=(z_1-\lambda y)\otimes L+L\otimes(z_1-\lambda y).
$$
其原极线恒等式给 $k_L(k_{z_1}-\lambda P)=0$。L 非零，所以 K 可逆迫 $z_1=\lambda y$；$\lambda=0$ 会使 $z_1=0$，而 $\lambda\ne0$ 会使两列相关。均矛盾。

### 3.3 $\sigma\ne0$

由 (1.6)，$a=\varepsilon(0,h,-g)$，$\varepsilon=\pm1$。置
$$
Z=z_1,\quad L=gz_2+hz_3,\quad R=hz_2-gz_3,\quad
E_4=\operatorname{span}(Z,L,R,y).
$$
因 $\sigma\ne0$，四列独立，原配对只有
$$
K(Z,L)=\sigma,\qquad K(y,R)=\varepsilon\sigma
$$
及其对称项非零。因此 $E_4$ 非退化，$M=E_4^{\perp_K}$ 为非退化二维空间。u、v 在 M 的投影必须线性无关，否则六列不能张成六维。

用下标表示配对，例如 $c_Z=K(Z,u),c_L=K(L,u)$，并同样写 $d_Z,d_L$。因为 (3.1)，u、v 在 $E_4$ 的投影满足
$$
K(u_{E_4},u_{E_4})=\frac{2c_Zc_L}{\sigma},\qquad
K(u_{E_4},v_{E_4})=\frac{c_Zd_L+d_Zc_L}{\sigma}.
\tag{3.2}
$$
N 在物理值 u 的评价是 $c^{\mathsf T}Bc=2c_Zc_L=0$，所以 $u_M$ 等向。

若 V 非约化，原 H 极线的一阶导数亦给 $N(u,v)=0$。因 (3.1)，这正是 $c_Zd_L+d_Zc_L=0$，故由 (3.2) 和 $uKv=0$ 得 $u_MKv_M=0$。

若 V 约化，v 也是物理值，故 $d_Zd_L=0$。最高式在 H 点 Z 的评价，因 $a_1=0$，给 $c_Z^3+d_Z^3=0$。因此 $c_Z,d_Z$ 或者都为零，或者都非零。前者显然使 (3.2) 的交叉分子为零；后者由两个 N 值迫 $c_L=d_L=0$，仍使其为零。又 $uKv=e=0$，所以依旧 $u_MKv_M=0$。

非退化二维复型中，非零等向向量的正交补就是其自身那条线。故 $u_M,v_M$ 不能线性无关；$u_M=0$ 时更立即不可能。矛盾。

三个小节穷尽 $F=0$，所以全部 $F=0$ 被排除，连同 §2 的全部非约化 V 一起排除。

## 4. $F\ne0,Hp\ne0$ 的约化 V：有限四行规范

现在 V 约化、$F\ne0$。假设 $Hp\ne0$，即 $a\ne0$。则 (1.6) 给 $\sigma=F^2$，而 (2.3) 给 $e^3=F^3$。特别 $e\ne0$。

给 $z_1$ 取适当正负号并作原整体加权尺度，可规范为
$$
F=1,\qquad g^2+h^2=1,\qquad a=(1,g,h),\qquad e=\omega,\quad\omega^3=1.
\tag{4.1}
$$
这种整体尺度把 y、每个 z、u、v 同乘一个非零数，对 H、V 正是二次、三次权，故保完整临界性。

(1.7) 和最高式在 H 点逐条给
$$
c_i^2+d_i^2=\omega^2a_i^2,\qquad c_i^3+d_i^3=a_i^3.
\tag{4.2}
$$
若 $g=0$，第二行便使 $c_2=d_2=0$：两平方和、两立方和同时为零只允许两数皆零。此时 $z_2$ 是原 B 的根向量，且与 y、u、v 也正交，违反完整六维 K 非退化。$h=0$ 同理。因此 $gh\ne0$。

令
$$
q=g^2\notin\{0,1\},\qquad
c_i=\omega a_i r_i,\quad d_i=\omega a_i s_i.
$$
每一行准确满足
$$
r_i^2+s_i^2=1,\qquad r_i^3+s_i^3=1.
$$
令 $b=r_i+s_i$，则 $(b-1)^2(b+2)=0$。所以每行只可能是
$$
(1,0),\quad(0,1),\quad(r_*,s_*),\quad(s_*,r_*),
\tag{4.3}
$$
其中
$$
r_*+s_*=-2,\quad r_*s_*=\tfrac32,\quad
\{r_*,s_*\}=\{-1+\tfrac{\sqrt{-2}}2,-1-\tfrac{\sqrt{-2}}2\}.
$$
所有系数都在二次域 $L=\mathbb Q(\sqrt{-2})$ 内；并未假定 q 或 $\omega$ 属于这个域。

置
$$
\bar r=qr_2+(1-q)r_3,\qquad
\bar s=qs_2+(1-q)s_3.
$$
两个 V mean 系数保
$$
r_1^2+qr_2^2+(1-q)r_3^2=1,\qquad
s_1^2+qs_2^2+(1-q)s_3^2=1.
\tag{4.4}
$$
下一节保完整 N 的两个 V 值，不能只停在有限四行列表。

## 5. 原 N 的两个 V 值排空全部四行数据

沿用
$$
Z=z_1,\quad L_0=gz_2+hz_3,\quad R=hz_2-gz_3,\quad
\eta=y-Z-L_0.
$$
由 (4.1)，$\eta$ 与 H 三空间正交且自身等向。完整 N 准确为
$$
N=\eta^2-2(Z^2+L_0^2)-R^2+2\omega(u^2+v^2).
\tag{5.1}
$$
在实际物理值 u、v 评价，用 (4.4) 消去
$q(1-q)(r_2-r_3)^2=1-r_1^2-\bar r^2$ 及其 s 版本，得到
$$
\boxed{(r_1-1)(\bar r-1)=1-\omega,\qquad
(s_1-1)(\bar s-1)=1-\omega.}
\tag{5.2}
$$
例如 u 的原值除以 $\omega^2$ 是
$[1-r_1-\bar r]^2-2(r_1^2+\bar r^2)
-q(1-q)(r_2-r_3)^2+2\omega$，准确等于 (5.2) 第一式的两倍零多项式。

若第一行是 $(1,0)$，(5.2) 给 $\omega=1,\bar s=1$。(4.4) 给
$$
q(1-q)(s_2-s_3)^2=0,
$$
所以 $s_2=s_3=1$，第二、三行都为 $(0,1)$。因此 R 与 u、v 都正交；它本已与 H 三空间及 y 正交，成为原六维 K 的非零根向量，矛盾。第一行为 $(0,1)$ 由交换 u、v 同理排除。

只余第一行为一个非单位行 $(r,s)$。其两个数均非一，且 $(r-1)(s-1)=9/2$。由 (5.2)
$$
\bar r+\bar s=\frac{10+8\omega}{9}.
\tag{5.3}
$$
若第二、三行同为单位行，其和均为一，便使 $\omega=-1/8$；若同为非单位行，其和均为负二，便使 $\omega=-7/2$。均不满足 $\omega^3=1$。因此二、三行恰有一个单位行。交换它们，再必要时交换 u、v，可设第二行为 $(1,0)$、第三行为非单位行 $(r_3,s_3)$。式 (5.3) 给
$$
q=\frac{28+8\omega}{27}.
$$
再把 (5.2) 第二式写成
$$
-\frac{(1+8\omega)s_3}{27}=\frac{s-\omega}{s-1}.
$$
这是一条关于 $\omega$ 的 L 系数一次式：
$$
[-s_3(s-1)-27s]+\omega[-8s_3(s-1)+27]=0.
\tag{5.4}
$$
两个系数不能同时为零：否则 $s_3(s-1)=27/8$ 并且 $s=-1/8$，后者不是 $X^2+2X+3/2$ 的根。因此 (5.4) 要么已矛盾，要么迫 $\omega\in L$。

L 不含非平凡三次单位根。直接证明：若 $(2\omega+1)^2=-3$ 在 L 中成立，写 $2\omega+1=a+b\sqrt{-2}$、$a,b\in\mathbb Q$，则 $ab=0$，继而要么 $a^2=-3$，要么 $b^2=3/2$；两者都无有理数解。因此 $\omega=1$。于是 $q=4/3$、$\bar s=1$，而 $\bar s=(1-q)s_3=-s_3/3$，迫 $s_3=-3$，再次不是上述二次式的根。最后一型也被排除。

故 $F\ne0,Hp\ne0$ 的整个约化 V 分支为空。

## 6. 准确保留的零 Hp 分支

前五节已证明：本质六维反设下只能有约化 V、$F\ne0,Hp=0$。此时 (1.6)、(2.3) 保
$$
\boxed{
a=0,\qquad g^2+h^2=-F^2\ne0,\qquad 2e^3=-F^3,\qquad e\ne0.
}
\tag{6.1}
$$
若 g 或 h 为零，(1.7) 与最高式在相应孤立 H 物理点又给该行 $c_i^2+d_i^2=c_i^3+d_i^3=0$，所以两交叉数皆零；那个物理点将正交六列基，矛盾。故
$$
\boxed{gh\ne0.}
$$
H 的实际 Gram 因此准确秩二，非零边恰为两条。这里的零 Hp、非零 F 层还没有在本稿排除，仍须继续保其全部逐点原 N 条件及全部极线多项式，不能把 (6.1) 的抽象 Gram 当成实际临界解。

本稿只用了显示的完整原梯度、原物理值/一次 jet、有限维非退化型及明确的四行代数；没有新的计算源或数值推断。它不覆盖 H 非约化的长度三支撑，也不排除 H 三点 Gram 非退化的本质六维情形。本质四、五维、全局匹配 Bell 自然幂和普通 ISP 完成标准亦保持原缺口。
