# R271 附录：原同源位置发生器的二阶预算与完整返回测试运输

日期：2026-11-15（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本文把已付的位置加权一阶形式界提升为实际顶部和真实返回测试的完整算子范数界。全部估计保同一个 $f,V,K,u_f$ 及真实零源投影。特别，
$$
\|\mathcal G_{\rm pos}u_f\|\le40Q\|f-u_f\|,
$$
而返回、逆芽伴随和 Riordan 帽测试（包括其完整真正交旗）的二阶谱矩总量为 $O(\nu Q^2\|f-u_f\|^2)$。这里 $\nu$ 只是原未来段的实际重叠数。没有把投影说成与位置发生器或 MP 交换。

依赖：

- [实际固定测试的压后交换谐和方程](R271-appendix-actual-fixed-test-exchange-adjoint-harmonic-equations-and-full-generator-budget.md)；
- [同源位置形式、完整真旗和排斥 Hardy](R271-appendix-actual-position-weighted-exchange-full-flags-and-exclusion-hardy.md)；
- [返回逆芽伴随与位置全旗运输](R271-appendix-actual-return-germ-adjoint-test-and-position-weighted-full-flag-transport.md)。

本稿不从二阶正预算倒置任何返回列；原顺次 MP 和的两端 partial sums 仍须共同处理。

## 1. 同一个有限孔环境和实际来源

仍取原
$$
C=A_m+D_<,\quad C^h=0,\quad h=2^m+R,\quad x=m+R,\quad
D=\sum_{i\ge x}(i+1)^{-2}E_i .
$$
本稿使用 $1\le x\le Q$。原强联块合法右窗口满足此条件。把独立头张量及所需有限个右栈均纳入环境，但每个中间向量的远孔数都不超过 $Q$。

固定有限物理 $f$ 在第 $x$ 位以后为真空。令
$$
v=P_Vf,\quad k=P_Kf,\quad u_f=v-k,\quad e=f-v,\quad K\subset V,
$$
$$
\Delta_f^2=\|e\|^2+\|k\|^2=\|f-u_f\|^2,\qquad
\zeta_f=\|e\|+\|k\|\le\sqrt2\Delta_f .
\tag{1.1}
$$
原相邻交换及权为
$$
U_i^*=U_i,\quad U_i^2=I,\quad H_i=n_{i+1}-n_i,\quad
\theta_i=\log\frac{i+2}{i+1},\quad a_i=(i+1)(i+2),
$$
$$
V_i=e^{\theta_iH_i}U_ie^{-\theta_iH_i}
=e^{2\theta_iH_i}U_i .
\tag{1.2}
$$
每个 $V_i$ 保原 $V,K$ 及完整右栈中的 $E,Z_f,\widehat E$；它与真实 $D$ 交换，保持所有原方程、头旗和物理 cut。其伴随仍固定 $f$。

记
$$
\mathfrak e_{\rm pos}(z)=\sum_{i\ge x}a_i\|(I-U_i)z/2\|^2,
\qquad
G=\mathcal G_{\rm pos}=\sum_{i\ge x}a_i(I-U_i).
\tag{1.3}
$$
$G$ 是该自然闭非负形式对应的自伴算子，
$\|G^{1/2}z\|^2=2\mathfrak e_{\rm pos}(z)$。
先在远孔 $\le Q$ 的直和上讨论；这里 $\mathcal N\le QI$。
已付位置稿给有限位置支撑向量在自然形式域中稠密，且给
$$
\mathfrak e_{\rm pos}(z)\le2r_xQ\|z\|^2
\quad(z=e\text{ 或 }k),\qquad r_x=1+\frac1{x+1}\le\frac32,
\tag{1.4}
$$
$$
\mathfrak e_{\rm pos}(u_f)\le4r_xQ\Delta_f^2.
\tag{1.5}
$$
(1.4) 中的每个 $z$ 都是原来的实际缺陷；不是对任意向量的环境界。

## 2. 位置发生器的完整 skew 估计

在有限位置支撑核上定义
$$
L=\sum_{i\ge x}a_i(I-V_i),\qquad A=L-L^* .
$$
置 $n=i+1$。逐个两位矩阵给
$$
d_i=2a_i\sinh(2\theta_i)
=4n+2+\frac1n+\frac1{n+1},
$$
$$
c_i=a_i(\cosh(2\theta_i)-1)
=2+\frac1{2a_i}.
\tag{2.1}
$$
因此
$$
A=-\sum_{i\ge x}d_iH_iU_i,\qquad
L=G+J+\frac12A,\qquad
J=-\sum_{i\ge x}c_iU_iH_i^2 .
\tag{2.2}
$$
注意 $A$ 的位置系数增长，不能沿用无权发生器的环境 $O(x^{-1})$ 界。

由于 $n\ge2$，有 $d_i\le6n$、$d_i^2/a_i\le36$，并且
$0<d_i-d_{i-1}<4$。将 $A$ 准确分为
$$
Az=-\sum_i d_iH_i(U_i-I)z-\left(\sum_i d_iH_i\right)z.
\tag{2.3}
$$
在一个 $q$ 孔配置上，至多有 $2q$ 条相邻单占据边。先对该配置应用 Cauchy--Schwarz，再对所有配置求和：
$$
\left\|\sum_i d_iH_i(U_i-I)z\right\|^2
\le288q\,\mathfrak e_{\rm pos}(z).
\tag{2.4}
$$
这个计数同时适用于向量值头系数。随后在所有 $q\le Q$ 上合并，不增加孔层数。

另一项是真正的占据望远镜：
$$
\sum_{i\ge x}d_iH_i
=-d_xn_x+\sum_{j>x}(d_{j-1}-d_j)n_j.
\tag{2.5}
$$
其在 $\mathcal N\le Q$ 上的范数不超过
$6(x+1)+4Q\le16Q$。故
$$
\boxed{\|Az\|\le\sqrt{288Q\,\mathfrak e_{\rm pos}(z)}
+16Q\|z\|
=12\sqrt Q\,\|G^{1/2}z\|+16Q\|z\|.}
\tag{2.6}
$$
该式在完整位置形式域成立。

又 $c_i\le9/4$，每配置至多 $2Q$ 条活边，所以 Schur 行列和界给
$$
\boxed{\|J\|\le\frac92Q.}
\tag{2.7}
$$
$J$ 是有界自伴算子；这里没有把 (2.5) 的左端占据项删掉。

## 3. 闭算子、无限位置极限和真实谐和向量

为精确固定域，把 $A$ 依 (2.3)--(2.6) 延拓为从
$\operatorname{Dom}G^{1/2}$ 到环境的连续算子。有限位置形式核稠密给
$\langle Az,y\rangle=-\langle z,Ay\rangle$。
两个算子
$$
L_\pm=G+J\pm A/2,\qquad\operatorname{Dom}L_\pm=\operatorname{Dom}G
\tag{3.1}
$$
均闭，且 $L_+^*=L_-$。一个直接的域检验是
$$
\|(J\pm A/2)(G+\lambda)^{-1}\|
\le3\sqrt{Q/\lambda}+\frac{25Q}{2\lambda}<1
\quad(\lambda=100Q).
\tag{3.2}
$$
因此两边的平移均由同一 Neumann 分解满射；形式伴随包含关系遂为等号。等价地，闭形式
$$
\ell(z,y)=\langle G^{1/2}z,G^{1/2}y\rangle
+\langle Jz,y\rangle+\tfrac12\langle Az,y\rangle
$$
对应的算子正是 $L=L_+$，其伴随为 $L_-$。下文均用这个自然实现，不采用未指明边界条件的形式无限和。

可用有限边截断来核实际投影的域。选 $0\le\chi_M\le1$，在
$i+1\le M$ 为 $1$，在 $i+1\ge2M$ 为 $0$，且相邻差不超过 $1/M$。令
$$
L_M=\sum_i\chi_M(i)a_i(I-V_i),\qquad A_M=L_M-L_M^*.
$$
其每一项都保原 $V,K$，并连同伴随一起杀 $f$。
公式 (2.3) 仍成立，只需将 $d_i$ 换成 $\chi_M(i)d_i$；梯度部分受原形式尾控制，对角差的系数统一不超过 $16$，左端仍保 $d_xn_x$。所以
$$
A_Mz\longrightarrow Az
\quad(z\in\operatorname{Dom}G^{1/2}).
\tag{3.3}
$$
同时 $\ell_M(z,y)\to\ell(z,y)$ 对任意两个形式域向量成立。
这避免用陡峭截断产生未经控制的最外位置边界。

对 $z=P_Ef$，$E=V$ 或 $K$，每个有限 $M$ 有
$$
L_Mz=P_EA_Mz,\qquad
L_M^*z=-(I-P_E)A_Mz .
\tag{3.4}
$$
对 $z=e=f-P_Vf$ 同样成立，仍使用 $P_E=P_V$，因为
$L_Mf=L_M^*f=A_Mf=0$。由 (1.4)、(3.3) 和完整形式极限，(3.4) 证明这些向量实际属于 $\operatorname{Dom}G$，并给
$$
\boxed{Lz=P_EAz,\qquad L^*z=-(I-P_E)Az.}
\tag{3.5}
$$
这里两个输出正交。因此
$$
\|Lz\|^2+\|L^*z\|^2=\|Az\|^2,
\qquad
\left\|\frac{L+L^*}{2}z\right\|=\frac12\|Az\|.
\tag{3.6}
$$

结合 (1.4)、(2.6)--(2.7)，
$$
\|Az\|\le(24\sqrt{r_x}+16)Q\|z\|\le46Q\|z\|,
$$
$$
\boxed{\|Gz\|\le28Q\|z\|\qquad(z=e,k).}
\tag{3.7}
$$
故对原同一个 $u_f=f-e-k$，
$$
\boxed{
\|Gu_f\|\le40Q\Delta_f,\qquad
\bigl(\|Lu_f\|^2+\|L^*u_f\|^2\bigr)^{1/2}
\le66Q\Delta_f .
}
\tag{3.8}
$$
这是完整算子域和二阶谱矩的结论，不只是 (1.5) 的重述。它保同一个缺陷因子 $\Delta_f$，没有改成 $\|f\|$。

## 4. 真正不变源投影保持形式域，反馈准确可控

以下引理在同一 $\mathcal N\le Q$ 环境内成立。设闭空间 $E$ 被每个原 $V_i$ 保持，$P=P_E$。由于
$(I-P)V_iP=0$ 及其伴随，
$$
[U_i,P]=(I-P)(U_i-V_i)P-P(U_i-V_i^*)(I-P).
$$
右边的两个输出正交，而 $U_i-V_i$ 及 $U_i-V_i^*$ 都只作用于该对单占据扇区。因此
$$
\|[U_i,P]y\|^2\le(e^{2\theta_i}-1)^2
\bigl(\|H_iPy\|^2+\|H_i(I-P)y\|^2\bigr).
$$
原连续权准确满足
$$
a_i(e^{2\theta_i}-1)^2
=\left(1+\frac1{i+1}\right)
 \left(2+\frac1{i+1}\right)^2\le10 .
$$
使用 $\sum_iH_i^2\le2QI$ 得
$$
\boxed{\sum_i a_i\|[U_i,P]y\|^2\le20Q\|y\|^2,}
\tag{4.1}
$$
$$
\mathfrak e_{\rm pos}(Py)^{1/2}
\le\mathfrak e_{\rm pos}(y)^{1/2}+\sqrt{5Q}\|y\|.
\tag{4.2}
$$
所以真实 $P$ 保位置形式域。此证明不要求 $P$ 保逐孔层。

进一步，对 $y\in\operatorname{Dom}L^*=\operatorname{Dom}G$，
$$
\boxed{
L^*Py=P L^*y-(I-P)APy.
}
\tag{4.3}
$$
严格域证明：先对有限 $L_M$ 写该恒等式，在两边与任意形式域向量配对。由 (4.2) 可把 $P$ 放入这个测试；再用 (3.3) 和形式收敛通过极限。右边属于 Hilbert 空间，故 $Py$ 属于真实伴随域，得到 (4.3)。最后一项是原投影反馈，不能删掉。

## 5. 环境逆芽伴随、Riordan 逆伴随的真实对易

设环境有界 $B$ 满足
$$
BV_i^*=V_i^*B,\qquad\|B\|\le M ,
\tag{5.1}
$$
并保持所用的 $\le Q$ 物理右栈。则
$$
[U_i,B]=(U_i-V_i^*)B-B(U_i-V_i^*).
$$
同 (4.1) 得
$$
\sum_i a_i\|[U_i,B]z\|^2\le80QM^2\|z\|^2,
$$
$$
\mathfrak e_{\rm pos}(Bz)^{1/2}
\le M\mathfrak e_{\rm pos}(z)^{1/2}
+2\sqrt{5Q}M\|z\|.
\tag{5.2}
$$
$B^*$ 有相同形式域保持性质。有限 $L_M^*$ 与 $B$ 严格交换，故以 (5.2) 在形式极限中传递得
$$
\boxed{B\operatorname{Dom}L^*\subset\operatorname{Dom}L^*,
\qquad L^*Bz=BL^*z.}
\tag{5.3}
$$
这是真正环境算子之间的对易，不涉及任何 MP。

具体地，原
$$
B_q=q_h(-\mathbb T)^*,\qquad B_K=K_{\rm amb}^{-*}
$$
满足 (5.1)。$\mathbb T$ 每行是 $D$ 并只移一行，$K_{\rm amb}^{-1}$ 是输出行及 $\mathbb T$ 的原有限降行多项式；它们的伴随与所有 $V_i^*$ 交换。两者只在原第 $h$ 行截断，不产生栈外孔数。因此 (5.3) 可用于原全部中间测试。

仍保
$$
A_0=\sum_{j=0}^{h-1}|q_j|\delta^j<\frac32d_0,\qquad
d_0=e^{-20},\qquad \|K_{\rm amb}^{-*}\|\le\mathcal C_0,
$$
其中 $\mathcal C_0$ 是已付、与 $m,h,Q$ 无关的 Riordan 常数。
去常数 $q_h-d_0$ 的相同预算以 $A_1=\sum_{j\ge1}|q_j|\delta^j$ 代替 $A_0$。

## 6. 原返回测试的完整二阶矩

沿原合法切口集取
$$
Y_{f,n}=(u_{f,n+1},\ldots,u_{f,n+h}),\qquad
e_{f,n}=P_{E_n}Y_{f,n},
$$
$$
e^q_{f,n}=P_{E_n}B_qe_{f,n},\qquad
\widehat e^q_{f,n}=P_{\widehat E_n}B_Ke^q_{f,n}.
\tag{6.1}
$$
这些正是此前主配对中的真实返回代表；所有 $Z_f,\widehat Z_f$ 正交仍保留。普通帽测试为
$\widehat e_{f,n}=P_{\widehat E_n}B_Ke_{f,n}$。

令 $\nu$ 为一输出层被未来段读取的最大次数。已付
$$
\|\mathbf Y_f\|\le\sqrt\nu\Delta_f,\quad
\mathfrak e_{\rm pos}(\mathbf Y_f)\le4r_x\nu Q\Delta_f^2 .
$$
提取未来段与 $L,L^*,G$ 交换，故 (3.8) 给
$$
\|L^*\mathbf Y_f\|\le66Q\sqrt\nu\Delta_f,\qquad
\|G\mathbf Y_f\|\le40Q\sqrt\nu\Delta_f .
\tag{6.2}
$$

为保常数来源，假设一个实际测试 $\mathbf z$ 已有
$$
\|\mathbf z\|\le M_z\sqrt\nu\Delta_f,\quad
\mathfrak e_{\rm pos}(\mathbf z)\le C_z\nu Q\Delta_f^2,\quad
\|L^*\mathbf z\|\le D_zQ\sqrt\nu\Delta_f .
$$
对 $\mathbf w=P_EB\mathbf z$，用原已付位置界给其 $M_w,C_w$。
由 (4.3)、(5.3)、(2.6) 得新的完整范数递推
$$
\boxed{
D_w=M D_z+\sqrt{288C_w}+16M_w,\qquad
\|L^*\mathbf w\|\le D_wQ\sqrt\nu\Delta_f .
}
\tag{6.3}
$$
又 $G=L^*+A/2-J$，所以
$$
\boxed{
\|G\mathbf w\|
\le\bigl(D_w+\sqrt{72C_w}+\tfrac{25}{2}M_w\bigr)
Q\sqrt\nu\Delta_f .
}
\tag{6.4}
$$
每个中间测试都先由 (4.3)、(5.3) 放入准确算子域，因而 (6.4) 不是仅形式演算。

代入上篇已付的
$$
C_e=20r_x,\quad
C_q=(78+12r_x^2)r_x A_0^2,\quad
C_{\widehat q}=(252+48r_x^2)r_x\mathcal C_0^2A_0^2,
$$
及 $r_x\le3/2$，得到以下保守的绝对常数：
$$
\boxed{\begin{aligned}
\|G\mathbf e_f\|&\le240Q\sqrt\nu\Delta_f,\\
\|G\mathbf e_f^q\|&\le530A_0Q\sqrt\nu\Delta_f,\\
\|G\widehat{\mathbf e}_f\|&\le530\mathcal C_0Q\sqrt\nu\Delta_f,\\
\|G\widehat{\mathbf e}_f^q\|
&\le1040\mathcal C_0A_0Q\sqrt\nu\Delta_f .
\end{aligned}}
\tag{6.5}
$$
例如各步的 $L^*$ 常数可依次取
$176,406A_0,406\mathcal C_0,818\mathcal C_0A_0$。
所有平方范数已在原切口直和上相加；不能再逐切口或逐孔层乘 $Q$。
去常数版本的 (6.5) 将 $A_0$ 严格换成 $A_1$，包括
$\widehat{\mathbf e}_f^q-d_0\widehat{\mathbf e}_f$。

## 7. 全部真正正交旗的二阶矩也不乘旗高度

仍置
$$
\Pi_j=P_{\ker D^j},\qquad F_j=\Pi_j-\Pi_{j-1},\qquad \Pi_0=0.
$$
本节的 $F_j$ 始终是物理正交旗。它们不是顺次 MP 乘积。

每个 $\Pi_j$ 的像都被原 $V_i$ 保持。第 4 节也给另一方向的域公式
$$
LPy=P Ly-P A(I-P)y.
\tag{7.1}
$$
它与 (4.3) 一样先对有限边成立，再用形式域保持通过极限。因此
$\Pi_j,F_j$ 保 $\operatorname{Dom}G=\operatorname{Dom}L=\operatorname{Dom}L^*$。

每个 $V_i^*$ 只作用于两个物理位并保持这两位的总孔数，故
$$
\operatorname{ad}_D^3 V_i^*=0.
$$
直接证明时只需用该两位删除 $D_{\{i,i+1\}}$：
其三次幂为零，而
$D_{\{i,i+1\}}^2V_i^*D_{\{i,i+1\}}$ 和
$D_{\{i,i+1\}}V_i^*D_{\{i,i+1\}}^2$ 也因局部次数为零。
所以有限 $L_M^*$ 满足同一三重对易子恒等式，并把
$\ker D^j$ 送入 $\ker D^{j+2}$。另一方面 $L_M$ 保每个 $\ker D^j$。
借助 (7.1)、(4.3) 的形式域分块取极限，得到准确带宽
$$
F_aL^*F_b=0\quad\text{除非 }b\le a\le b+2,
\qquad
F_aLF_b=0\quad\text{除非 }b-2\le a\le b.
\tag{7.2}
$$
这里不把无界无限和的形式对易子直接当作有界算子恒等式。

对 $z\in\operatorname{Dom}G$，准确有 $F_aL^*F_b=-F_aAF_b$（$a>b$）；其余 $L^*$ 非对角块为零。
在 $[L^*,F_j]z$ 中，向上输出 $F_{j+1},F_{j+2}$ 与返回输出 $F_j$
正交；后者至多合并两个输入。对整个旗列求和遂得
$$
\boxed{
\sum_j\|[L^*,F_j]z\|^2
\le3\sum_j\|AF_jz\|^2.
}
\tag{7.3}
$$
这是完整正交列估计，不是对各个 $j$ 分别取范数后累加环境常数。

设某个已付实际测试族满足
$$
\|\mathbf z\|\le M\sqrt\nu\Delta_f,\quad
\|L^*\mathbf z\|\le D_0Q\sqrt\nu\Delta_f,\quad
\sum_{n,j}\mathfrak e_{\rm pos}(F_jz_n)
\le C_F\nu Q\Delta_f^2 .
$$
将 (2.6) 用于每个真实 $F_jz_n$ 后整体相加，得到
$$
\left(\sum_{n,j}\|AF_jz_n\|^2\right)^{1/2}
\le\sqrt{576C_F+512M^2}\,Q\sqrt\nu\Delta_f .
\tag{7.4}
$$
由 (7.3)、旗分析列等距以及 $G=L^*+A/2-J$，
$$
\boxed{
\left(\sum_{n,j}\|GF_jz_n\|^2\right)^{1/2}
\le
\left[
D_0+\left(\sqrt3+\frac12\right)
 \sqrt{576C_F+512M^2}+\frac92M
\right]Q\sqrt\nu\Delta_f .
}
\tag{7.5}
$$
全过程没有乘 $j$ 的总数、$h$ 或 $Q$ 的额外因子。

对第 6 节的每个返回／帽测试，可直接取已付
$$
C_F=2C_z+12r_x^{\,2\sqrt3-1}M^2,
$$
其中 $C_z,M$ 是该测试在上篇位置运输稿中的常数，
$D_0$ 则取 (6.3) 后的 $176,406A_0,406\mathcal C_0,
818\mathcal C_0A_0$。故整个正交旗的二阶矩也为
$O(\nu Q^2\Delta_f^2)$，常数仍不依赖 $m,h,Q$。

对原 $u_f$ 本身，不可把 $\|u_f\|$ 免费界成 $\Delta_f$。
应准确使用 $z_0=f-u_f=e+k$，它有 $\|z_0\|=\Delta_f$。
由于 $D f=0$，
$$
F_1f=f,\qquad F_{j>1}f=0,\qquad Gf=L^*f=0.
$$
因此 $GF_jz_0=-GF_ju_f$，且两者的全旗位置形式相同。
原位置稿给
$$
C_F=48r_x^{\,4\sqrt3-1},\qquad M=1,\qquad D_0=66,\quad \nu=1,
$$
代入 (7.5) 即得原 $u_f$ 的完整全旗二阶矩。
对未来段 $\mathbf Y_f$ 同样只乘实际重叠数 $\nu$。
这一步没有重新选择顶部或强迫源。

## 8. 新范围与未付接口

(6.5) 是真实测试的二阶谱矩，即
$$
\sum_n\int_0^\infty \lambda^2\,d\|P_\lambda w_n\|^2
\le C_w^{\prime\,2}\nu Q^2\Delta_f^2
$$
（$P_\lambda$ 为原自伴 $G$ 的谱分解，$C_w'$ 取 (6.5) 对应常数）。
例如对任何 $t>0$，
$$
\sum_n\|1_{[tQ,\infty)}(G)w_n\|^2
\le C_w^{\prime\,2}t^{-2}\nu\Delta_f^2.
\tag{8.1}
$$
同源固定测试逼近 $w\in W$ 时，原合法窗口已经给
$\limsup\Delta_f\le\|f-w\|$。因此归一二阶矩保固定逼近误差的平方，
不要求一个未知尾速率。

第 7 节另付同一真实正交旗之后的完整二阶矩，但没有从此推断真正返回列
$\mathcal R$、Feshbach 逆或顺次 MP 两端部分和相对受 $G$ 控制。
特别，$P_E$ 的 (4.3) 中压缩外项仍在，$B_q$ 的对易只在环境伴随上使用。
本稿新增的是原实际测试及全部必要环境／源投影之后的正则性预算，
后续必须继续在原同源混合配对中使用它。普通 $N=M$ 尚未完成。
