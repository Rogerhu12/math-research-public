# R271 补录：实际四维 N 头的三孔费用消奇性、固定偶强段及固定中央新方向

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / r271_cost、root；AI-assisted，GPT-6 Astra Pro。

状态：下述有限头与固定参数渐近结论已证明；移动原大头费用仍开放。

## 0. 范围与沿用定义

本条只证明原纯远孔代表的一组有限头费用结论。它不证明普通 Hilbert 不变子空间问题，不证明所有移动头的实际费用可和性，也不把任意压缩的逆费用替代完整强头的 Moore–Penrose 费用。

沿用 [纯高度双塔代表](R271-appendix-dual-tower-kernel-only-error-pure-far-height-representatives-and-joint-reciprocal-budget.md) §1 的定义。给定完整有限强头 $C$、$0<S\le1$、$r=3$，记
$$
F=\ker C^3,\qquad
H=I+\frac{C^*C}{S}+\frac{(C^*)^2C^2}{2S^2},
$$
$$
a=(P_FH|_F)^{-1}P_Fe_1,\qquad
\xi=e_1-Ha,\qquad
q=((C^*)^3)^\dagger\xi.
\tag{0.1}
$$
这里 $P_FH|_F\ge I_F$，故 $a$ 唯一；Galerkin 正交性给出
$\xi\in F^\perp=\operatorname{Ran}(C^*)^3$，故最后一式是整个强头中的最小范数真解。原三孔代表的费用为
$$
\kappa_{m,3}^2=\sigma_{x,3}^2\|q\|^2,\qquad
\sigma_{x,3}^2=(3!)^2 e_3((b_i^2)_{i\ge x}),\qquad
S=S_x=\sum_{i\ge x}b_i^2.
\tag{0.2}
$$
以下每次使用 $F,H,q$ 都指完整空间；没有丢弃 primitive 链或仅在可达低列上做 Galerkin。

考察真实四维 N 头的一参数族
$$
A_t=
\begin{pmatrix}
0&1&1/4&0\\
0&0&t&1/4\\
0&0&0&1\\
0&0&0&0
\end{pmatrix},\qquad t>0.
\tag{0.3}
$$
原参数在 $m=2$ 时恰为
$$
t=\frac{d_1}{d_0^2}=e^{-1070},
\tag{0.4}
$$
因为原权重 $-\log d_0=20,\ -\log d_1=1110$。这是原 N 头；本条不将它称作 Y 头公式。

## 1. 原 $m=2,\ R=2$ 的完整有限矩阵结论

加入原强位 $2,3$，其权重为
$$
c_1=1/9,\qquad c_2=1/16.
$$
令 $E=c_1E_1+c_2E_2$ 为两位 Boolean 删除和，
$C_t=A_t\otimes I+I\otimes E$。
按 $u_{4i+j}=e_i\otimes e_j$ 编号，$e_1$ 的原源列为 $f=u_4$。

### 定理 1

当 $0<t\le10^{-2}$ 且 $0<S\le1$ 时，(0.1) 的完整真解满足
$$
\|\xi_t\|\le6.5\cdot10^6\,t^2S^{-6},
\qquad
\|q_t\|\le3.9\cdot10^8\,tS^{-6}.
\tag{1.1}
$$
特别地，取实际 $t=e^{-1070}, S=S_4$，有
$$
\kappa_{2,3}^2\le10^{18}t^2S_4^{-9}<e^{-2000}.
\tag{1.2}
$$

### 1.1 完整核旗与完整秩

设 $Z_t=Z_0+tZ_1$ 的十一列依次为
$$
u_0,u_1,u_2,u_3,u_4,u_5,u_6,u_8,\ 
u_9-8tu_7,\ 
u_{10}-\frac92tu_7,\ 
u_{12}-24tu_7.
\tag{1.3}
$$
直接作用 $C_t^3$ 可核对
$$
C_t^3u_7=\frac1{24}u_0,\quad
C_t^3u_9=\frac t3u_0,\quad
C_t^3u_{10}=\frac{3t}{16}u_0,\quad
C_t^3u_{12}=tu_0,
$$
其余八列为零，故 $\operatorname{Ran}Z_t\subset\ker C_t^3$。
这些列独立，且
$$
Z_0^*Z_0=I,\quad Z_0^*Z_1=0,\quad
\|Z_1\|^2=8^2+(9/2)^2+24^2=2641/4<26^2.
\tag{1.4}
$$

取 $X_t=C_t^3$ 的行集
$I=(0,1,2,4,8)$ 与列集 $J=(7,11,13,14,15)$，记
$B_t=(X_t)_{I,J}$。其行列式与逆为
$$
\det B_t=-t^3/6912,
$$
$$
B_t^{-1}=
\begin{pmatrix}
24&1/t&9/(16t)&-15/t&-3/(4t)\\
0&4/t&9/(4t)&-12/t&-15/t\\
0&1/(4t)&-27/(64t)&9/(4t)&9/(16t)\\
0&-4/(3t)&1/(4t)&4/t&1/t\\
0&0&0&0&24
\end{pmatrix}.
\tag{1.5}
$$
故 $t\ne0$ 时 $\operatorname{rank}X_t\ge5$。结合十一列核向量，
$$
\ker C_t^3=\operatorname{Ran}Z_t,\qquad \operatorname{rank}C_t^3=5.
\tag{1.6}
$$
(1.5) 的 Frobenius 范数直接给出
$$
\|B_t^{-1}\|\le60/t\qquad(0<t\le1).
\tag{1.7}
$$
这是完整秩与完整核的认证，不是只求一个低源压缩的逆。

### 1.2 残差的二阶消失

由 $Z_t^*f=e_4$（此 $e_4$ 为十一维系数向量），
$$
G_t=Z_t^*H_tZ_t\ge I,\qquad
v_t=G_t^{-1}e_4,\qquad a_t=Z_tv_t,\qquad \xi_t=f-H_ta_t.
\tag{1.8}
$$
按四个 Boolean 位的物理孔数分级为 $\mathcal H_j$。
在 $t=0$ 时 $C_0$ 是四位纯 Boolean 删除和，
$$
\operatorname{Ran}Z_0=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2.
$$
$H_0$ 保持孔数，$a_0=H_0^{-1}f\in\mathcal H_1$，故
$$
\xi_0=0.
\tag{1.9}
$$

设 $V=\partial_tC_t=|e_1\rangle\langle e_2|\otimes I$，它保持物理孔数。
$Z_1$ 只作用于二孔初始列，故 $Z_1v_0=0$，从而 $a'_0\in\operatorname{Ran}Z_0$。
又 $C_0^2a_0=0,\ VC_0a_0=0$，所以
$$
H'_0a_0=\frac{C_0^*Va_0}{S}
+\frac{(C_0^*)^2C_0Va_0}{2S^2}\in\mathcal H_2.
\tag{1.10}
$$
因此 $\xi'_0=-H'_0a_0-H_0a'_0\in\operatorname{Ran}Z_0$。
另一方面微分完整 Galerkin 条件 $Z_t^*\xi_t=0$，并用 $\xi_0=0$，得
$Z_0^*\xi'_0=0$。于是
$$
\xi'_0=0.
\tag{1.11}
$$

### 1.3 显式常数

对 $0\le t\le10^{-2},0<S\le1$，由 (0.3) 与实际两强位权重，
$$
\|C_t\|<1.5,\qquad
\|H_t\|\le6S^{-2},\quad
\|H'_t\|\le10S^{-2},\quad
\|H''_t\|\le11S^{-2}.
$$
这里 $V^2=0$，故 $(C_t^2)''=0$；以上亦可由
$\|(C_t^2)'\|\le3$ 直接核对。
由 (1.4)，可统一取
$$
\|Z_t\|<2,\quad\|Z'_t\|<26,\quad
\|G'_t\|\le700S^{-2},\quad
\|G''_t\|\le11000S^{-2}.
$$
因 $G_t^{-1}\le I$，微分 $G_tv_t=e_4$ 给出
$$
\|v_t\|\le1,\quad\|v'_t\|\le700S^{-2},\quad
\|v''_t\|\le10^6S^{-4}.
$$
进一步
$$
\|a_t\|\le2,\quad\|a'_t\|\le1500S^{-2},\quad
\|a''_t\|\le2.1\cdot10^6S^{-4},
$$
所以
$$
\|\xi''_t\|
\le\|H''_ta_t\|+2\|H'_ta'_t\|+\|H_ta''_t\|
\le1.3\cdot10^7S^{-6}.
$$
与 (1.9)、(1.11) 积分两次即得 (1.1) 第一式。

### 1.4 从选定满秩 minor 回到完整 MP 解

$\xi_t\in\operatorname{Ran}X_t^*$。构造只支撑于行集 $I$ 的向量
$$
\widetilde q_I=B_t^{-*}(\xi_t)_J,\qquad
\widetilde q_{I^c}=0.
$$
则 $X_t^*\widetilde q$ 与 $\xi_t$ 在 $J$ 上相等。
由于 $X_t$ 的 $J$ 列构成完整列空间的一组基，而且两向量均在
$\operatorname{Ran}X_t^*$，它们在所有坐标上相等。
故 $\widetilde q$ 是完整方程的真解，MP 最小性与 (1.7) 给出
$$
\|q_t\|\le\|\widetilde q\|
\le(60/t)\|\xi_t\|
\le3.9\cdot10^8tS^{-6}.
$$
最后 $e_3((b_i^2))\le S_4^3/3!$，故
$\sigma_{4,3}^2\le6S_4^3$。又
$S_4\ge\int_5^\infty u^{-4}du=1/375$，从而
$$
\kappa_{2,3}^2
\le10^{18}e^{-2140}375^9<e^{-2000}.
$$
定理 1 得证。

## 2. 任意固定偶强段：完整 MP 逆只损失一个 $t^{-1}$

现在令 $R=2k\ge2$ 固定，强位权重 $c_1,\ldots,c_R>0$ 固定，
$$
C_t=A_t\otimes I+I\otimes\sum_{\ell=1}^R c_\ell E_\ell,
$$
并固定 $0<S\le1$。仍按 (0.1) 在完整 $4\cdot2^R$ 维空间定义 $a_t,\xi_t,q_t$。

### 定理 2

当 $t\to0^+$ 时，
$$
\|\xi_t\|=O_{R,c,S}(t^2),\qquad
\|q_t\|=O_{R,c,S}(t).
\tag{2.1}
$$
这里 $O$ 的常数和有效邻域可依赖整个固定强段及 $S$。本条没有给出关于移动 $R$ 的统一常数，也不自动断言每一个固定大 $R$ 的实际 $e^{-1070}$ 已落入该邻域。

### 2.1 真核的解析极限与低孔包含

令 $N=R+2=2k+2$，按物理孔数分级为 $\mathcal H_j$，
$R_\lambda|_{\mathcal H_j}=\lambda^jI$。有
$$
C_t=tR_tC_1R_t^{-1},\qquad
C_t^3=t^3R_tC_1^3R_t^{-1}.
\tag{2.2}
$$
因此 $F_t=\ker C_t^3=R_tF_1$。

一个有限维子空间的此种对角退化有如下直接构造。按嵌套过滤
$F_1\cap\bigoplus_{j\ge a}\mathcal H_j$ 选取适配基；每个基向量
$v$ 的最低非零级为 $a$，且同一级初始向量独立。
对应列 $t^{-a}R_tv$ 是多项式，常数项在 $\mathcal H_a$，
其 $t^n$ 系数在 $\mathcal H_{a+n}$。
所得满列秩框架记为 $Z(t)$。$Z(0)$ 仍满列秩，所以真核投影在
$t=0$ 解析延拓，其极限 $F_0=\operatorname{Ran}Z(0)$ 是分级子空间。

写
$$
X_t=C_t^3=X_0+tX_1.
\tag{2.3}
$$
这是因为 $V^2=VC_0V=0$。$X_0=C_0^3$ 降三孔，$X_1$ 降两孔。
所有零孔、一孔向量对每个 $t$ 都在 $\ker X_t$ 中。
对 $u\in\mathcal H_2$，有 $X_tu=t\ell(u)\Omega$。
任选两个强位 $i\ne j$，置 $z=e_1\otimes e_{\{i,j\}}$；则
$$
X_tz=6c_ic_j\Omega
$$
与 $t$ 无关。于是
$u-t\ell(u)z/(6c_ic_j)\in F_t$，故
$$
\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\subset F_0.
\tag{2.4}
$$

用 $Z(t)$ 参数化完整 Galerkin 解，可知 $a_t,\xi_t$ 在零点解析。
$H_0$ 保持孔数，故 $a_0=H_0^{-1}f\in\mathcal H_1$，$\xi_0=0$。
可以把对全部 $t$ 已在核中的 $\mathcal H_{\le1}$ 选为框架的常数列，
故 $a'_0\in F_0$。微分完整 Galerkin 方程得到
$$
P_{F_0}(H_0a'_0+H'_0a_0)=0.
$$
(1.10) 仍成立，右端只在 $\mathcal H_2$；
压缩 $P_{F_0}H_0|_{F_0}$ 按孔数分块并严格正定，
所以 $a'_0\in F_0\cap\mathcal H_2=\mathcal H_2$。
于是 $\xi'_0\in\mathcal H_2\subset F_0$，再由 Galerkin 正交性得
$\xi'_0=0$。这证明 (2.1) 第一式。
注意这里没有假定 $H_0$ 保持 $F_0$ 中每个高孔子块；只用低两孔的完整包含。

### 2.2 所有 primitive 链的一阶开秩认证

强位对角相似可把 $\sum c_iE_i$ 化为未加权 Boolean 删除和；
再将其完整 Lefschetz 分解中的每一条链化为单位权 Jordan 链 $J_l$。
这些相似在固定 $R,c$ 下均与 $t$ 无关，但其条件数计入常数。
由于 $R$ 为偶数，每条链长 $l$ 为奇数。因而只需分析完整直和中的
$$
X_l(t)=(A_t\otimes I_l+I_4\otimes J_l)^3.
\tag{2.5}
$$

$t\ne0$ 时 $A_t$ 是单个四阶 Jordan 块；$t=0$ 时型为 $(3,1)$。
Jordan 张量和的链分解给出：
$$
\begin{array}{c|c|c}
l&\operatorname{rank}X_l(0)&\operatorname{rank}X_l(t),\ t\ne0\\ \hline
1&0&1\\
3&2&4\\
5&8&9\\
l\ge7\text{ 奇数}&4l-12&4l-12
\end{array}
\tag{2.6}
$$
该表也可由
$J_a\otimes I+I\otimes J_l$ 的链长
$a+l-1,a+l-3,\ldots,|a-l|+1$ 逐项取
$\max(\text{链长}-3,0)$ 核对。

为认证新增秩恰在一阶打开，以下给出可直接复核的 minor 数据。
坐标按旧头优先，编号 $li+j$，从零起。
选定零阶可逆基块 $B_0=(X_l(0))_{I,J}$ 后，
在其余坐标做 Schur 补。其一阶项为
$$
X_{1,22}-X_{1,21}B_0^{-1}X_{0,12}
-X_{0,21}B_0^{-1}X_{1,12}
+X_{0,21}B_0^{-1}X_{1,11}B_0^{-1}X_{0,12}.
\tag{2.7}
$$
所需数据为：

- $l=1$：基块空；新增行 $(0)$、列 $(3)$，一阶值 $1$。
- $l=3$：基行 $(0,1)$、基列 $(5,11)$；新增行 $(3,6)$、新增列 $(8,10)$，一阶 Schur 块为
$$
\begin{pmatrix}3/2&5/2\\-6&-2\end{pmatrix},
\qquad \det=12.
$$
- $l=5$：基行 $(0,1,2,3,5,6,10,11)$、基列
$(3,4,8,9,13,14,18,19)$；新增行 $(15)$、列 $(17)$，一阶 Schur 值 $10/3$。

各新增块尺寸恰等于 (2.6) 的秩差，故所有新增非零奇值均与 $t$ 同阶。
其余非零奇值在零点有正极限；$l\ge7$ 则秩恒定。
把有限多条 primitive 链全部合回，得到
$$
\|(C_t^3)^\dagger\|=O_{R,c}(t^{-1}).
\tag{2.8}
$$
结合 $\xi_t=O(t^2)$ 即得 $\|q_t\|=O(t)$，定理 2 得证。

## 3. 固定中央新方向的延迟泄漏

下述方向是零点固定的一阶 Schur 新方向，不是 $t\ne0$ 时某个未经比较的实际小奇值谱投影。

定义
$$
K_0=\ker X_0,\qquad
\mathcal E_1=P_{\ker X_0^*}X_1|_{\ker X_0},\qquad
E=\operatorname{Ran}\mathcal E_1.
\tag{3.1}
$$
由 (2.6)–(2.8) 的完整一阶开秩认证，
$$
\lim_{t\to0}\operatorname{Ran}X_t
=\operatorname{Ran}X_0\ \mathbin{\oplus^\perp}\ E.
\tag{3.2}
$$
这是标准有限维 Schur 消元的直接结论：在
$\ker X_0\oplus(\ker X_0)^\perp$ 与
$\operatorname{Ran}X_0\oplus\ker X_0^*$ 上消去可逆零阶块，
余块为 $t\mathcal E_1+O(t^2)$，且其秩已等于全部新增秩。

### 定理 3

若 $R=2k\ge2$，则
$$
E\subset\mathcal H_k,\qquad
P_Eq_t=O_{R,c,S}(t^k).
\tag{3.3}
$$
若 $R\ge4$，还得到完整真解的改进
$$
q_t=O_{R,c,S}(t^2),\qquad
\sigma_{x,3}^2\|q_t\|^2=O_{R,c,S}(t^4).
\tag{3.4}
$$
固定中央分量的平方费用为 $O(t^{2k})=O(t^R)$，但 (3.3)
没有把整个 $q_t$ 提升为 $O(t^k)$：完整真解可以从 $t^2$ 起
在低孔的普通范围方向上非零。

### 3.1 新方向只在中央级

$C_0$ 是 $N=2k+2$ 位加权 Boolean 删除和。
加权对角相似保持孔数，所以可用未加权 Boolean Lefschetz 秩：
$X_0=C_0^3$ 在 $\mathcal H_j$ 上对 $j\ge k+3$ 单射，
而对输出 $\mathcal H_\ell,\ell\le k-1$ 满射。
因此
$$
\ker X_0\subset\bigoplus_{j\le k+2}\mathcal H_j,\qquad
\ker X_0^*\subset\bigoplus_{\ell\ge k}\mathcal H_\ell.
$$
$X_1$ 恰降两孔，故 (3.1) 只可能由
$\ker X_0\cap\mathcal H_{k+2}$ 映入 $\mathcal H_k$。
这证明 $E\subset\mathcal H_k$，并且
$\mathcal E_1^*$ 在 $E$ 上单射。

### 3.2 Galerkin 系数的有限传播

把 §2.1 的解析核框架每列按其初始孔数赋级。
其 $t^a$ 系数从初始级 $j$ 映入物理级 $j+a$。
$H_t$ 的 $t^b$ 系数只改变孔数至多 $b$：因为
$C_t^j$ 中 $t^a$ 项降 $j-a$ 孔，而对应伴随项升同样孔数。

因此 $G(t)=Z(t)^*H_tZ(t)$ 的 $t^b$ 系数只连接相差至多 $b$
的初始级，且 $G(0)$ 按级严格正定。
$Z(t)^*f$ 的 $t^a$ 系数只在初始级 $1-a$。
逐阶解 $G(t)v(t)=Z(t)^*f$，再乘 $Z(t)$，得到
$$
a_t=\sum_{n\ge0}t^na_n,\quad
\xi_t=\sum_{n\ge0}t^n\xi_n,\qquad
a_n,\xi_n\in\bigoplus_{j\le1+n}\mathcal H_j.
\tag{3.5}
$$
这个结论使用完整 Galerkin 矩阵及其按级逆，并未删除高孔变量。

由 (2.8) 与 $\xi_t=O(t^2)$，MP 真解在穿孔邻域为亚纯且
$q_t=O(t)$，因而零点可去并可写
$$
q_t=\sum_{n\ge1}t^nq_n.
\tag{3.6}
$$
这里亚纯性可用恒秩区间上的任一固定满秩 minor 与最小范数投影的
有理公式直接得到。

### 3.3 归纳排除中央级之前的泄漏

由 (2.2)，$\operatorname{Ran}X_t=R_t\operatorname{Ran}X_1^{\rm fixed}$，
其中 $X_1^{\rm fixed}=C_1^3$；这处记号与 (2.3) 的一阶系数 $X_1$ 区分。
因此范围也有 §2.1 同型的解析分级框架 $U(t)$：
$U_a$ 将初始级 $j$ 送入 $\mathcal H_{j+a}$，且
$\operatorname{Ran}U_0=\operatorname{Ran}X_0\oplus E$。

归纳证明
$$
q_n\in\bigoplus_{j\le n-2}\mathcal H_j
\qquad(1\le n<k),
\tag{3.7}
$$
其中负上界表示零空间。
假设前面的系数已满足此式。写 $q_t=U(t)h(t)$，因 $U(0)$ 满列秩，
$h(t)$ 解析。按级递推可知先前 $h_j$ 的初始级也至多 $j-2$；
故
$$
q_n\in\operatorname{Ran}X_0+E+
\bigoplus_{j\le n-2}\mathcal H_j.
$$
当 $n<k$ 时最后一项已在 $\operatorname{Ran}X_0$ 中，因 $X_0$
对这些输出级满射。于是唯一正交分解
$q_n=b_n+e_n$，其中 $b_n\in\operatorname{Ran}X_0,e_n\in E$。

比较 $X_t^*q_t=\xi_t$ 的 $t^n$ 系数：
$$
X_0^*b_n+X_1^*q_{n-1}=\xi_n,\qquad q_0=0.
$$
$X_0^*$ 恰升三孔，在 $\operatorname{Ran}X_0$ 上单射；
结合 (3.5) 与归纳假设，右侧只在孔数 $\le n+1$，所以
$b_n$ 只在孔数 $\le n-2$。

再取 $t^{n+1}$ 系数并投影到 $\ker X_0$，得到
$$
\mathcal E_1^*e_n
=P_{\ker X_0}\xi_{n+1}
-P_{\ker X_0}X_1^*b_n.
$$
左侧在 $\mathcal H_{k+2}$，右侧孔数至多 $n+2<k+2$。
因此两侧为零；$\mathcal E_1^*|_E$ 单射给出 $e_n=0$，
归纳成立。这证明 $P_Eq_t=O(t^k)$。
若 $k\ge2$，取 $n=1$ 还得 $q_1=0$，即 (3.4)。

## 4. 可以与不可以带出的结论

1. 定理 1 是原 N 算子 $m=2,x=4,r=3$ 的真实纯三远孔列费用估计，
   包括完整核旗、完整 Galerkin 与完整 MP 最小解。
2. 该数值实例不满足旧联合预算使用的高度窗
$$
r\le1+\left\lfloor\frac{\sqrt{x+1}}{8(m+1)}\right\rfloor,
$$
   因为右端在 $m=2,x=4$ 为 $1$。它也不满足那些父结论的 $m\ge10$
   假设。不能据此直接调用移动头联合门；在 $x=4,p=2$ 下，
   粗双塔小误差判据本身也未由本条认证。
3. 定理 2、3 是每个固定偶 $R$、固定强权重、固定 $S$ 的解析渐近。
   物理相似的条件数与有效 $t$ 邻域均依赖 $R$；本条没有隐藏这些成本。
4. $E$ 是零点固定的一阶 Schur 新方向。没有证明
   $P_Eq_t$ 与 $t\ne0$ 时移动小奇值谱投影费用相等或同阶。
5. 本条尚未把原所有 $A_m$ 的多层 carry、允许高度窗内的可变 $r$、
   与移动 $R$ 的统一常数合并。普通 Hilbert ISP 与原 $\overline{BM}=M$
   的费用门均保持未闭。
