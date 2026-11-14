# 原始两行共同核的相反范数壳约束

日期：2026-11-13。接 R177、R182 及 primitive-cartan-common-kernel 检查点。

**状态：以下正规化子作用和支撑分离已证明；没有据此排除共同核。**
全部运算固定同一个加性角色、同一个实际频率和同一个剩余嵌入。
这是线性 Weil 作用，不是移动圆分 Galois 共轭或重新选择实际尖点。

## 1. 一个保持同一系数嵌入的线性正规化子

沿用 R177 的相空间 $V=\mathbb F_{p^2}$、$\tau^2=z$ 非平方及

$$
\Omega(u,v)=-\operatorname{Tr}(\tau u\bar v)/a,\qquad a\in\mathbb F_p^\times.
$$
取任意 $b\in V^\times$ 满足 $N(b)=-1$，置

$$
\iota_b(v)=b\bar v.
$$
范数映射满射，故这样的 $b$ 存在。共轭改变 $\Omega$ 的符号，乘 $b$ 又乘范数 $-1$，所以 $\iota_b$ 是辛变换；它满足 $\iota_b^2=-I$。

在 R177 的 Schrödinger 模型中，可取一个可逆线性算子 $J_b$，满足

$$
J_bD_vJ_b^{-1}=D_{b\bar v}.
\tag{1}
$$
它可由有限 Fourier 矩阵、对角二次相位矩阵和置换矩阵的 Bruhat 分解构造；所有矩阵及其逆都整于 $\mathbb Z[\zeta_p,1/p]$。这里只使用其共轭作用，任选的总体标量没有影响。因此 (1) 在任何 $\ell\ne p$ 的固定剩余嵌入下仍可用，无需引入一个会改变 $\zeta_p$ 的半线性作用。

R177 的准确公式

$$
K_t=-\frac1p\sum_{v\in V}\psi(tN(v)/a)D_v,\qquad K_\infty=I
$$
直接给

$$
\boxed{J_bK_tJ_b^{-1}=K_{-t}.}
\tag{2}
$$
因为换元 $w=b\bar v$ 时 $N(w)=-N(v)$。$t\mapsto-t$ 正是 $C$ 中取逆，故

$$
J_bP_HJ_b^{-1}=P_H.
\tag{3}
$$
它交换 $P_H$ 的两条三次特征线。

## 2. 两个范数壳的准确共同核

将 R182 的符号显式添上位移参数：

$$
Q_s(u)=\frac1s\sum_{\kappa\in\mu_{6s}}D_{u\kappa},\qquad
\mathcal R_m(u)=\sum_{s\mid m}\mu(s)Q_s(u).
$$
相空间的辛形式仍使用上面固定的 $a$；这里改变 $u$ 不改变该形式，也不重选加性角色。
由 (1) 和每个 $\mu_{6s}$ 在共轭下稳定，得

$$
\boxed{J_b\mathcal R_m(u)J_b^{-1}=\mathcal R_m(b\bar u).}
\tag{4}
$$
特别地，对原来的 $u=a\in\mathbb F_p^\times$，

$$
\mathcal R_m(a)P_H=0
\quad\Longrightarrow\quad
\mathcal R_m(ab)P_H=0.
\tag{5}
$$
右边的支撑范数为 $-a^2$；不是原来范数为 $a^2$ 的圆上另选一个角度。
$\mathcal R_m$ 的对称性把 R182 的左行条件 $P_H\mathcal R_m(a)=0$ 变成此处的右核条件。

精确地，令

$$
U_u=\bigcap_{c\in C}\ker(K_c\mathcal R_m(u)K_c^{-1}),\qquad
V_{a,b}=U_a\cap U_{ab}.
\tag{6}
$$
$U_u$ 是 $C$ 稳定的。对一条 $C$ 特征线 $L$，有
$\mathcal R_m(u)L=0\iff L\subset U_u$。
又由 (4)，

$$
J_bU_a=U_{ab},\qquad J_bU_{ab}=U_{-a}=U_a.
$$
最后一个等号使用 $-1\in\mu_6$，故 $\mathcal R_m(-a)=\mathcal R_m(a)$。
因此 $V_{a,b}$ 对 $C$ 和 $J_b$ 都稳定。

记两条三次线为 $L_+,L_-$，则有准确等价式

$$
\boxed{
\mathcal R_m(a)(L_+\oplus L_-)=0
\iff L_+\subset V_{a,b}
\iff L_-\subset V_{a,b}.}
\tag{7}
$$
前向用 (5)；反向利用 $J_b$ 交换两线。
换成 (6) 的矩阵元图，就是同时取两个范数壳的边；目标是证明该联合图中的指定三次顶点不孤立。

## 3. $m=2^r$ 时两个十二点支撑没有和碰撞

现在设 $m=2^r$、$p=6m-1>37$ 为素数。因此 $r\ge3$ 且 $p\equiv23\pmod{24}$。
令 $\nu$ 为 $\mu_{12}$ 的生成元，并使用 R182 未除二的算子

$$
R(u)=\sum_{j=0}^{11}(-1)^jD_{u\nu^j}=2\mathcal R_m(u).
$$
置 $A=a\mu_{12}$、$B=ab\mu_{12}$，于是 $N(A)=a^2$、$N(B)=-a^2$。

**命题。** 有

$$
(A-A)\cap(B-B)=\{0\}.
\tag{8}
$$
所以加法映射 $A\times B\to V$、$(u,v)\mapsto u+v$ 为单射，其像准确有 $144$ 点。

**证明。** 因为 $p\equiv23\pmod{24}$，$2,3$ 是平方而 $-1$ 非平方。
取 $s^2=3$。两个不同十二次单位根之差的范数，除去一个平方因子，恰在

$$
\{1,2,3,4,2+s,2-s\}
$$
中。最后两个数满足

$$
2\pm s=(s\pm1)^2/2,
$$
所以列出的六个非零数全部是 $\mathbb F_p$ 的平方。
因此 $A-A$ 的每个非零元素有平方范数，$B-B$ 的每个非零元素有非平方范数。
这证明 (8)；若 $u+v=u'+v'$，则 $u-u'=v'-v$，由 (8) 两边都为零。证毕。

此外，任意 $u\in A,v\in B$ 都有

$$
\Omega(u,v)\ne0.
\tag{9}
$$
否则二维辛空间中两向量共线，$v=tu$、$t\in\mathbb F_p^\times$，便有 $-1=N(v)/N(u)=t^2$，矛盾。

## 4. 乘积和交换子中的系数确实都是单位

设 $\epsilon(u)=(-1)^j$ 对 $u=a\nu^j$，$\epsilon(v)=(-1)^k$ 对 $v=ab\nu^k$。
由 (8)，每个 $w\in A+B$ 有唯一的表示 $w=u+v$。Weyl 乘法因而给

$$
[R(a),R(ab)]
=\sum_{u\in A,v\in B}
\epsilon(u)\epsilon(v)
\bigl(\psi(\Omega(u,v))-\psi(-\Omega(u,v))\bigr)D_{u+v}.
\tag{10}
$$
由 (9)，括号是一个 $p$ 次单位根乘 $1-\zeta_p^k$，其中 $k\not\equiv0\pmod p$。
它在 $\mathbb Z[\zeta_p,1/p]$ 中为单位。
因此 (10) 有准确 $144$ 个非零单位系数，在任何 $\ell\ne p$ 下都无支撑内的抵消。
乘积 $R(a)R(ab)$ 同样有 $144$ 个单位系数。

这不能直接推出乘积或交换子可逆。Weyl 符号有许多非零单位系数并不控制矩阵的整个核；例如一个秩一坐标投影已有 $p$ 个非零单位 Weyl 系数。
若 (7) 发生，则这两个算子及其交换子都杀两维 $P_H$；(10) 尚未给矛盾。
真正需要的是利用两个范数壳的联合条件消去指定 $C$ 特征线，而不是把“无系数抵消”误认成“无共同核”。

## 5. 当前剩余接口

(4)–(10) 是比单个 R182 方块更强的实际约束，且不依赖残余 Frobenius 是否交换三次方向。下一步可尝试用这些互不碰撞的支撑和完整 Cartan 乘法建立整左理想的 Bézout 关系。
目前没有证明该左理想包含 $P_H$，没有证明两个 cubic 方块行列式的共同理想为单位，也没有得到一般 $p$ 的原始两行非消失。
旧 Steinberg 行及所有实际中心值/秩零商前提继续与 R169–R181 完全一致；本笔记不消去任何该类前提。
