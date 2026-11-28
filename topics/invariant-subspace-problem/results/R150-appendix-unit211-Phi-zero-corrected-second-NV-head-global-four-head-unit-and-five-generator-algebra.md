# R150：正确 Phi 第二 NV 头的显示四阶头单位、完整同点五生成与原 t 二次延拓

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / literature_deddens。日期：2026-11-29（Asia/Taipei）。

**结论。** 在当前正确 Phi、物理 $D\ne0$ 的第二 NV 头
$$
B_2=\ell(3-2\lambda)+2T+2m\sigma=0
\tag{1}
$$
中，利用刚完成的[整个 $\ell=3/2$ 交集排除](R150-appendix-unit211-Phi-zero-corrected-second-NV-head-ell-three-halves-complete-original-exclusion.md)，两个完整原矩与完整原 $NV$ 的必要代数，在全部剩余权图上由
$$
\boxed{1,\ \lambda,\ \sigma,\ \lambda^2,\ \lambda\sigma}
\tag{2}
$$
五元生成。核心是四条真实原三次关系的头矩阵行列式
$$
\boxed{2P_{02}m\delta(3-2\ell),}
\tag{3}
$$
其每个因子在本图已付。加入此前全权原首一 $t^2$ 后，相应必要代数由 (2) 及其 $t$ 倍共十元生成。所有原条件、重数和同点相容继续保留；不假定这些生成元自由，也不宣整个第二头排空。

本稿是新的显示原身份及降次证明，没有脚本、Actions run、泛域 gcd、旧 cofactor 或已冻门的重放。新的 $\ell=3/2$ 排除只用于 (1)，不移到第一头或一般 Phi 权图。

## 1. 系数环与已付范围

记
$$
\begin{gathered}
s=u-1,\quad \delta=1-Q,\quad L=Q-2s(u-2),\quad
\ell=L/Q,\quad m=u-\ell,\\
K_w=Q+4s,\quad T_0=-K_w,\quad J=Q-4s^2,\quad
P_{02}=2sL,\quad M=\ell^2\delta-m^2 .
\end{gathered}
\tag{4}
$$
原权图中 $Q,\delta,s,K_w,L,M$ 都是原单位；$m$ 的支付来自已核真正 dual germ 乘法的[完整等权原排除](R150-appendix-unit211-equal-weights-complete-original-exclusion.md)，其修正后 Phi 适用静审为 blob **a69e073257e72633bdfb4c4bffbb3109cdae1327**。它只在当前正确 Phi、$D\ne0$ 图应用。

新交集排除进一步在 (1) 中支付 $3-2\ell$。以这些纯权单位作局部化，取
$$
A=\mathbb Q[u,Q]\!
 \left[Q^{-1},\delta^{-1},s^{-1},K_w^{-1},L^{-1},
 M^{-1},m^{-1},(3-2\ell)^{-1}\right].
\tag{5}
$$
这里的 $M,m,\ell$ 是 (4) 的有理函数，因 $Q$ 已逆，(5) 是明确的有限型纯权系数环。没有把几何 $D,t,f-u$ 加入此系数环的逆表。

从 (4) 直接有三个关键完整权身份：
$$
J-Q=-4s^2,\qquad J-T_0=2L,
$$
$$
\boxed{m^2-\delta(\ell-1)^2=s^2(3-2\ell).}
\tag{6}
$$
后一个等式只用 $(1-\ell)Q=2s(u-2)$；它不是由某个模因子或泛型点推出。

## 2. 第二头的同点恢复及完整原矩

设
$$
a=\lambda-\frac32,\qquad \theta=u-\ell Q,\qquad
h=\lambda-\frac12-\rho\sigma,\quad
k=\lambda-\frac12+\rho\sigma,\quad \rho^2=\delta .
\tag{7}
$$
于是 $h+k=2\lambda-1$，并有
$$
j=bh+ck=T+\ell=\ell\left(\lambda-\frac12\right)-m\sigma,
\qquad T=\ell a-m\sigma,\qquad w=\lambda-1-T.
\tag{8}
$$
$\rho$ 两个选择同时交换原 singleton 标签；下述所有式都落在 $A[\lambda,\sigma]$。

两个完整原矩为
$$
E_2=\ell a^2-2ma\sigma+\ell\delta\sigma^2-A_\lambda,
$$
$$
E_3=\ell a^3-3ma^2\sigma+3\ell\delta a\sigma^2-m\delta\sigma^3-B_\lambda,
\tag{9}
$$
其中 $A_\lambda=2\lambda^2-2\lambda+1$、
$B_\lambda=4\lambda^3-6\lambda^2+3\lambda-1$。

令 $E=A_1/2=f-V+bc\,t$。同一正确原 $P_1,N_0$ 恢复给
$$
\boxed{
E=\frac{P_{02}}{T_0}j,\qquad
f=\frac{P_{02}\lambda-QE+sT_0}{J-Q},\qquad
V=f+bc\,t-E .}
\tag{10}
$$
所以 $E,f$ 对 $(\lambda,\sigma)$ 都至多一次，且与 $t$ 无关。所有分母仅用 (5)；$J$ 本身没有被反演。原 $E_0$ 恢复为 $W_1=T_0/2+2uf$，随后从原两线性均值恢复 $X,Y$，仍只用 $M$ 等旧权单位。

## 3. 完整 NV 的新短原身份

本节从真 Gram 直接展开，说明三次来源是完整 $NV$，并保原矩误差。

记
$$
S=h+k=2\lambda-1,\quad P=hk,\quad
r=S+P,\quad R=1-S+P=(1-h)(1-k).
$$
在原 Gram 中
$$
d=(u,d_1,X,Y),\qquad d_1=2f-V-(1-\ell)u,\qquad F_2=2f.
$$
物理向量为 $\mathbf V=(1,w,h,k)$，满足
$$
\tau(\mathbf V)=\lambda,\qquad
\tau(\mathbf V^2)=2\lambda^2+E_2.
$$
因此原定义直接给
$$
NV+2fE_2
=2\tau\!\left(d(\mathbf V^2-2\lambda\mathbf V)\right)
 +\tau(\mathbf V D_K\mathbf V).
\tag{11}
$$
这里保留了全部误差 $2fE_2$。

真正 dual germ 乘法下，
$$
\mathbf V^2-2\lambda\mathbf V
=(-S,\ (1-S)w,\ -h-P,\ -k-P),
$$
而对完整 Gram，
$$
\tau(\mathbf V D_K\mathbf V)
=2E+2bhX+2ckY+2w(bph+cqk)+2bc(P-S)t .
\tag{12}
$$
把 (12) 代入 (11)，再用 $V=f+bc\,t-E$，所有 $t$ 项准确消掉，得到
$$
\boxed{
NV+2fE_2
=2\{-rf+RE+w[bp(1-k)+cq(1-h)]\}.}
\tag{13}
$$
这一步没有施加 $t=0$、没有丢弃 $E_0$ 误差，也没有把 singleton 的加权条件替代完整 $NV$。

由 (7)，
$$
r=\lambda^2+\lambda-\frac34-\delta\sigma^2,\qquad
R=a^2-\delta\sigma^2,
$$
$$
bp(1-k)+cq(1-h)=-ua-\theta\sigma .
$$
故定义
$$
\boxed{
N^\sharp=2\{-rf+RE-w(ua+\theta\sigma)\}\in A[\lambda,\sigma]}
\tag{14}
$$
后，准确有
$$
N^\sharp=NV+2fE_2,\qquad
(E_2,E_3,N^\sharp)=(E_2,E_3,NV).
\tag{15}
$$
$\deg_{\lambda,\sigma}N^\sharp\le3$。这条完整原身份与已刊[第二头幂等元极化小式](R150-appendix-unit211-Phi-zero-corrected-second-NV-head-idempotent-polarization-and-small-complete-cubic.md)相容；这里专门保留其对新头矩阵有用的形式。

## 4. 四个原三次头及其显示行列式

本节 $x,z$ 只表示 $(\lambda,\sigma)$ 的最高齐次符号。两个矩的真实最高部分是
$$
E_2^{[2]}=\mathcal E=(\ell-2)x^2-2mxz+\ell\delta z^2,
$$
$$
E_3^{[3]}=\mathcal F
=(\ell-4)x^3-3mx^2z+3\ell\delta xz^2-m\delta z^3.
\tag{16}
$$
由 (10)，
$$
E^{[1]}-f^{[1]}
=\frac{P_{02}}{T_0(J-Q)}
 \{(J\ell-T_0)x-Jmz\}.
$$
所以 (14) 的最高三次准确分解为
$$
(N^\sharp)^{[3]}=c\,\mathcal P,\qquad
c=\frac{2P_{02}}{T_0(J-Q)},
$$
$$
\mathcal P=(x^2-\delta z^2)\{(J\ell-T_0)x-Jmz\}.
\tag{17}
$$
原 $NV$ 的最高部是 $c\mathcal P-2f^{[1]}\mathcal E$。由于首两条关系正是 $x\mathcal E,z\mathcal E$，把 $N^\sharp$ 换回完整 $NV$ 只是头矩阵的一次列加法，行列式不变。

按基 $(x^3,x^2z,xz^2,z^3)$，四列
$x\mathcal E,z\mathcal E,\mathcal F,\mathcal P$ 的矩阵为
$$
H_0=
\begin{pmatrix}
\ell-2&0&\ell-4&J\ell-T_0\\
-2m&\ell-2&-3m&-Jm\\
\ell\delta&-2m&3\ell\delta&-\delta(J\ell-T_0)\\
0&\ell\delta&-m\delta&Jm\delta
\end{pmatrix}.
\tag{18}
$$
其完整行列式是
$$
\boxed{\det H_0=-4T_0m\delta\{m^2-\delta(\ell-1)^2\}.}
\tag{19}
$$

为显示 (19) 的短来源，在 $\mathcal E$ 的首一 $z^2$ 商中，把三次余式写为 $(x^3,x^2z)$ 两坐标。$\mathcal F$ 的两系数为
$$
F_0=-2(\ell-1)-\frac{2m^2(2-\ell)}{\ell^2\delta},\qquad
F_1=\frac{2m(2\ell-1)}{\ell}
       -\frac{4m^3}{\ell^2\delta}.
$$
直接代 $z^2=((2-\ell)x^2+2mxz)/(\ell\delta)$ 给
$$
\mathcal P+J\mathcal F
=-\frac{2T_0}{\ell}x^2\{(\ell-1)x-mz\}
\pmod{\mathcal E}.
\tag{20}
$$
并且
$$
\det
\begin{pmatrix}F_0&\ell-1\\F_1&-m\end{pmatrix}
=\frac{2m}{\ell\delta}\{m^2-\delta(\ell-1)^2\}.
$$
乘回消去两个最高 $z$ 项所用的 $(\ell\delta)^2$，就得 (19)。这里只使用已付 $\ell\delta$；没有反演 $J$、任一几何根或新的纯权主元。

现在将第四列乘 (17) 的 $c$，再换回原 $NV$。结合 (6)，四条完整原式
$$
\lambda E_2,\quad \sigma E_2,\quad E_3,\quad NV
\tag{21}
$$
的三次头矩阵 $H$ 满足
$$
\begin{aligned}
\det H
&=\frac{2P_{02}}{T_0(J-Q)}
 [-4T_0m\delta s^2(3-2\ell)]\\
&=\boxed{2P_{02}m\delta(3-2\ell)\in A^\times}.
\end{aligned}
\tag{22}
$$
(22) 同时覆盖 $J=0$ 及所有原 moment 头的各别零面；没有先把它们作为额外开图。

## 5. 完整原三次降到总次二，得到五生成

令 $\mathbf m_3=(\lambda^3,\lambda^2\sigma,\lambda\sigma^2,\sigma^3)^t$。
把 (21) 的四个完整多项式写为列向量 $\mathbf R$，则
$$
\mathbf R=H^t\mathbf m_3+\mathbf l_2,\qquad
\deg_{\lambda,\sigma}\mathbf l_2\le2.
$$
因为 (22) 是已付单位，
$$
\boxed{
\mathbf m_3=(H^t)^{-1}\mathbf R-(H^t)^{-1}\mathbf l_2.}
\tag{23}
$$
这是四条真实原多项式组合，且 $(H^t)^{-1}$ 可由同一个显示矩阵的 adjugate 和 (22) 定义。所有最终分母仍在 (5)；不存在瞬时未付主元。

因此在
$$
\mathcal C=A[\lambda,\sigma]/(E_2,E_3,NV)
\tag{24}
$$
中，四个三次单项式都降到总次至多二。对任意更高单项式，先选一个三次因子用 (23) 替换，总次数严格下降，故有限步终止。

最后使用完整 $E_2$：
$$
E_2=\mathcal E+(2-3\ell)\lambda+3m\sigma+\frac94\ell-1
$$
及其已付首项 $\ell\delta$，得到
$$
\sigma^2=
\frac{(2-\ell)\lambda^2+2m\lambda\sigma
 +(3\ell-2)\lambda-3m\sigma+1-\frac94\ell}{\ell\delta}.
\tag{25}
$$
只在总次已不超过二后使用 (25)，不会形成互相升次的循环。于是 (2) 生成整个 (24)。

这是全系数环 $A$ 上的生成定理，不是只在泛型 $\mathbb Q(u,Q)$ 上成立。任意固定合法权点上，(24) 的必要纤维长度至多五，且包含所有幂零结构。没有声称 (2) 线性独立或 $\mathcal C$ 为自由秩五。

## 6. 原动作与单首一 t² 的有限延拓

(23)、(25) 给明确的有限降次规则。对 (2) 各元分别乘 $\lambda$ 或 $\sigma$，依次按三次规则和最后的 (25) 归约，可定义两个 $5\times5$ 系数矩阵 $M_\lambda,M_\sigma$。若
$$
\pi:A^5\twoheadrightarrow\mathcal C
$$
是原生成映射，便有
$$
\pi M_\lambda=\lambda\pi,\qquad
\pi M_\sigma=\sigma\pi.
\tag{26}
$$
这里不要求两个裸矩阵自由表示一个结合代数；(26) 已足以给真实商上的动作。Cayley–Hamilton 经 $\pi$ 应用到 $1$，分别给原必要的首一 $\lambda^5$、首一 $\sigma^5$ 多项式。此处只提供由显示规则确定的来源，未声称其系数已另行展开或执行返回。

再用[全权正确原首一 t 二次](R150-appendix-unit211-Phi-zero-corrected-whole-monic-t-quadratic-exact-ten-columns-and-four-generator-NV-head.md)，将同一点的 (10) 代回三原均值，得到
$$
q_t=t^2+a_1(\lambda,\sigma)t+a_0(\lambda,\sigma)
$$
及其真实三均值组合，系数在 $\mathcal C$ 中。故未作几何 $D$ 局部化的必要代数
$$
\mathcal C[t]/q_t
\tag{27}
$$
由
$$
1,\lambda,\sigma,\lambda^2,\lambda\sigma,\quad
t,t\lambda,t\sigma,t\lambda^2,t\lambda\sigma
\tag{28}
$$
十元生成。它在固定权点的长度至多十，全部 $t$ 重数保留。其余原均值、$N_1$、完整 singleton $N/P$ 等仍须在同一个 (27) 中施加；本稿没有把 (24) 或 (27) 宣称为完整原系统的充分条件。

物理 $D\ne0$ 开集的纤维不会增加，但几何局部化后的全权模未必仍有限，所以有限模断言严格针对 (24)、(27)。本稿也不计算加入 $\rho$ 或独立 $U_0$ 尺度后的完整规范点数。

## 7. 来源边界与后继

本稿使用的新支付是第二头与 $\ell=3/2$ 的唯一首次原交集排除：run **46179464150**、job **141085521543**，正式稿 blob **cbd49c43a4c7d10d19ff1bb188403d601e2322b9**。其完整四次常数域和 16 维原值模型返回的是原均值组合 $1$；不靠旧 rank-one 假设。

新的内容是 (13) 的完整同点短式、(18)–(22) 的显示四阶原头单位以及 (23)–(28) 的全权降次。此前小三元商中的两个 scalar、旧二十列与奇部八列都没有重新计算。第一头已冻结的三 scalar gcd、两个 QQ[u] 幺模资源边界也保持冻结。

后续可直接在 (23)、(25) 所定义的真实五生成商及 (27) 中构造新的完整原值关系。仅有五生成或十生成不推出空性；所有尚未返回的原值条件继续保留。
