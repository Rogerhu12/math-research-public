# 同一抛物线系数模式的全部二次多项式矩分离

日期：2026-11-12。会话：Astra-ISP-0c017065，子任务 l2_moments。

**状态：主定理已证明。** 对任意平方可和复数列 $t_j$，令

$$
X=\sum_jt_j\chi_j,\qquad Z=\sum_jt_j^2\chi_j.
$$

任意两个非零、标量系数、总次数至多二的多项式 $P(X,Z)$、$Q(X,Z)$，不可能对实际算子 $A$ 的复双线性形式 $B$ 全部矩消失。允许 $t\notin\ell^1$，尤其覆盖此前有限方向和平方根可和横向误差定理均未覆盖的 $(t_j,t_j^2)=(j^{-1},j^{-2})$。

本稿逐项处理 $Z^2$、$XZ$、纯 $X^2$ 及全部退化系数情形，不使用未经证明的普遍曲率独立性。最后使用的是实际 $B$-对称性和循环向量 $1$ 的矩分离性。任意有限前缀函数作为多项式系数的推广，尚不包含在本定理内。

依赖：R9/R12 的高位矩阵单位近似；R11 的 $1$ 及有限柱循环性；R24 的复双线性对称性；R40 的连续对矩分离。逐位有限翻译恒等式亦已在 R46 和 R63 给出，本稿重写所需精确形式。

## 1. 定理与内积范围

设

$$
B(u,v)=\int u(y)v(-1-y)\,d\mu(y),\qquad
\chi_j(y)=(-1)^{b_j(y)}.
$$

固定任意 $t=(t_j)\in\ell^2(\mathbb C)$，并定义

$$
X=\sum_{j\ge0}t_j\chi_j,\qquad
Z=\sum_{j\ge0}t_j^2\chi_j.
\tag{1.1}
$$

$X$ 在每个有限 $L^p$ 中存在，$Z$ 绝对一致收敛。故任意二次多项式的代入都属于 $L^2$。可加任意常数于 $X,Z$，因为这些常数可吸收进多项式。

**定理 1.1。** 若 $P,Q\in\mathbb C[x,z]$ 的总次数均至多二，则

$$
B(A^nP(X,Z),Q(X,Z))=0\quad(n\ge0)
\quad\Longrightarrow\quad
P(X,Z)=0\ \text{或}\ Q(X,Z)=0.
\tag{1.2}
$$

若 $t_j$ 全为实数，则该类对反射共轭

$$
Ch(y)=\overline{h(-1-y)}
$$

保持不变，因为 $CX=-X$、$CZ=-Z$。因此实数列 $t$ 的同一模式还满足通常内积版本：

$$
\langle A^nP(X,Z),Q(X,Z)\rangle=0\quad(n\ge0)
\quad\Longrightarrow\quad
P(X,Z)=0\ \text{或}\ Q(X,Z)=0.
\tag{1.3}
$$

更一般地，$t_j=e^{i\theta}s_j$、$s_j\in\mathbb R$ 时也保持同一多项式代数，所以 (1.3) 仍成立。对任意复数列 $t$，(1.2) 始终成立；通常内积的直接对应版本把第二端的模式改为 $\overline X,\overline Z$。本稿不把一般复数列的两个同一模式未经证明地视为对 $C$ 保持不变。

## 2. 两个实际模型事实及代入单射性

以下记

$$
M_n(u,v)=B(A^nu,v),\qquad
\mathfrak m_n(h)=M_n(1,h).
\tag{2.1}
$$

R24 和 $B$ 本身的对称性给

$$
M_n(u,v)=M_n(v,u).
\tag{2.2}
$$

R11 中 $1$ 的循环性给

$$
\mathfrak m_n(h)=0\ \text{对全部 }n
\quad\Longrightarrow\quad h=0.
\tag{2.3}
$$

因此，下文写出一个向量 $h$ 的全部 $\mathfrak m_n(h)$ 为零时，可以得出实际 $L^2$ 向量恒等式 $h=0$。这不是任意抽象双线性矩映射都具有的性质。

若 $t$ 只有有限支撑，则 $P(X,Z),Q(X,Z)$ 都是有限柱函数，定理由 R11 立即成立。故只需考虑无限支撑情形。由于 $t_j\to0$，非零 $t_j$ 中存在无限多个不同值。

**引理 2.1。** 当 $t$ 有无限支撑时，二次多项式代入 $\mathbb C[x,z]_{\le2}\to L^2$、$P\mapsto P(X,Z)$ 单射。

**证明。** 设

$$
\alpha X^2+\beta XZ+\gamma Z^2+\delta X+\varepsilon Z+\kappa=0.
\tag{2.4}
$$

对任意不同的 $i,j$ 且 $t_it_j\ne0$，取 Walsh 系数 $\chi_i\chi_j$，得

$$
2\alpha+\beta(t_i+t_j)+2\gamma t_it_j=0.
\tag{2.5}
$$

固定一个非零 $t_i$。其他非零 $t_j$ 仍有无限多个不同值，所以以 $t_j$ 为变量的一次多项式 (2.5) 恒为零，即

$$
\beta+2\gamma t_i=0,\qquad 2\alpha+\beta t_i=0.
$$

再取两个不同的非零 $t_i$，得 $\alpha=\beta=\gamma=0$。此后 (2.4) 的一次 Walsh 系数给

$$
\delta+\varepsilon t_i=0
$$

对无限多个不同的 $t_i$ 成立，故 $\delta=\varepsilon=0$，最后 $\kappa=0$。二次 Walsh 系数的计算可先对有限和进行，再用有限阶 Rademacher 矩界在 $L^2$ 中取极限。证毕。

特别地，$1,X,Z$ 线性无关，$X$ 非常数，非零形式二次多项式不会代入成零向量。

## 3. 沿抛物线的精确有限残差

反设 $f=P(X,Z)$、$g=Q(X,Z)$ 非零且全部 $M_n(f,g)=0$。形式求导只作用于多项式变量；记

$$
U_T=T\partial_x+T^2\partial_z
$$

作用于第一个多项式，$V_T$ 为第二个多项式上的相同形式。两者作用于不同张量因子，彼此交换。

在二次多项式的导数空间中，$U_T^3=V_T^3=0$。于是精确矩阵恒等式为

$$
e^{U_T+V_T}\bigl(\cosh(U_T-V_T)\bigr)^{-1}
=I+U_T+V_T+2U_TV_T
+U_T^2V_T+U_TV_T^2+2U_T^2V_T^2.
\tag{3.1}
$$

这里等号右边在第一行之后仍连续相加。可直接将 $e^{U+V}$ 与 $1-\tfrac12(U-V)^2+\tfrac5{24}(U-V)^4$ 相乘，并去掉 $U^3=V^3=0$ 的项核实。

对固定 $n$，定义标量多项式

$$
\begin{split}
\mathcal R_n(T)={}&
M_n(U_Tf,g)+M_n(f,V_Tg)+2M_n(U_Tf,V_Tg)\\
&+M_n(U_T^2f,V_Tg)+M_n(U_Tf,V_T^2g)
+2M_n(U_T^2f,V_T^2g).
\end{split}
\tag{3.2}
$$

其次数至多八，且常数项为零。式中的 $U_Tf$ 指 $(U_TP)(X,Z)$，其余同理。

**引理 3.1。** 存在与高位 $j$ 无关的 $C_n$，使

$$
|\mathcal R_n(t_j)|\le C_n a_j^{\mathrm{op}}
\tag{3.3}
$$

对全部充分大 $j$ 成立，其中 $a_j^{\mathrm{op}}=e^{-L_j}$ 是实际算子的第 $j$ 层权。

**证明。** 令 $A_j$ 为切断第 $j$ 位以上进位的低 $j$ 位有限链，$E_j=e_{10}$ 作用于第 $j$ 位。$A_j^n$ 不作用这一位。把该位从 $X,Z$ 中去掉，剩余的双线性积分记为 $\Lambda$。由于 $B$ 的第二变量反射时该位取补，

$$
M_{A_j^n}=\Lambda\cosh(U_{t_j}-V_{t_j}),\qquad
2B(E_jA_j^nf,g)=\Lambda e^{U_{t_j}+V_{t_j}}.
\tag{3.4}
$$

有限导数空间上的双曲余弦为 $I$ 加幂零矩阵，可逆。由 (3.4) 消去 $\Lambda$，再用 (3.1)，得到精确逐位公式。

另一方面，

$$
\|A^n-A_j^n\|\le n a_j^{\mathrm{op}},\qquad
\|N_j-E_j\|=\eta_j,\qquad
N_j=\frac{A^{2^j}}{W_{2^j}},\qquad
\eta_j=o(a_j^{\mathrm{op}}).
\tag{3.5}
$$

零矩假设给 $B(N_jA^nf,g)=0$。所以 (3.4) 左端在替换为真实矩之后为 $O_n(a_j^{\mathrm{op}})$。右端全部导数向量落在固定有限维空间内；$t_j\to0$，故相应有限矩阵系数一致有界，把 $A_j^n$ 换回 $A^n$ 的误差同样为 $O_n(a_j^{\mathrm{op}})$。去掉已为零的零阶矩，即得 (3.3)。证毕。

**引理 3.2。** 反设下每个 $\mathcal R_n(T)$ 都恒为零。

**证明。** 若某个非零 $\mathcal R_n$ 在原点的消失阶为 $\nu$，则 $1\le\nu\le8$。因而存在 $c,\rho>0$，使

$$
|\mathcal R_n(T)|\ge c|T|^\nu\qquad(|T|\le\rho).
$$

结合 (3.3) 及 $t_j\to0$，得

$$
|t_j|=O\bigl((a_j^{\mathrm{op}})^{1/\nu}\bigr).
\tag{3.6}
$$

实际权满足对任意 $s>0$ 都有 $\sum_j(a_j^{\mathrm{op}})^s<\infty$。所以 $t\in\ell^1$，从而 $X,Z,f,g$ 均有连续代表。R40 的连续对矩分离与非零零矩反设矛盾。证毕。

关键区别是：这里先把实际高位方向限制在同一条已知参数曲线 $(T,T^2)$，得到一个一变量的精确有限多项式；没有从多变量残差的非零性推断原点是孤立公共零点。

## 4. 全部系数表

为方便核查，写

$$
a=f_x,\quad b=f_z,\quad c=f_{xx},\quad d=f_{xz},\quad e=f_{zz},
$$

$$
\widetilde a=g_x,\quad \widetilde b=g_z,\quad
\widetilde c=g_{xx},\quad \widetilde d=g_{xz},\quad
\widetilde e=g_{zz}.
\tag{4.1}
$$

其中 $a,b,\widetilde a,\widetilde b$ 为至多一次的实际向量；全部二阶导数 $c,d,e,\widetilde c,\widetilde d,\widetilde e$ 是标量。由 (3.2) 直接展开，

$$
\begin{array}{c|l}
\text{次数}&[T^r]\mathcal R_n(T)\\ \hline
1&M_n(a,g)+M_n(f,\widetilde a)\\
2&M_n(b,g)+M_n(f,\widetilde b)+2M_n(a,\widetilde a)\\
3&2M_n(a,\widetilde b)+2M_n(b,\widetilde a)
+\mathfrak m_n(c\widetilde a+\widetilde c a)\\
4&2M_n(b,\widetilde b)
+\mathfrak m_n(c\widetilde b+2d\widetilde a+\widetilde c b
+2\widetilde d a+2c\widetilde c)\\
5&\mathfrak m_n(2d\widetilde b+e\widetilde a
+2\widetilde d b+\widetilde e a+4c\widetilde d+4d\widetilde c)\\
6&\mathfrak m_n(e\widetilde b+\widetilde e b
+2c\widetilde e+8d\widetilde d+2e\widetilde c)\\
7&4(d\widetilde e+e\widetilde d)\mathfrak m_n(1)\\
8&2e\widetilde e\,\mathfrak m_n(1).
\end{array}
\tag{4.2}
$$

表中标量出现在 $\mathfrak m_n$ 内时表示相应常数函数。引理 3.2 说明表的每一行对所有 $n$ 都为零。

## 5. 排除两端的 $Z^2$ 项

先假设 $e=f_{zz}\ne0$。第八次项及 $\mathfrak m_0(1)=1$ 给 $\widetilde e=0$；第七次项随即给 $\widetilde d=0$。

因此 $g_z=\widetilde b$ 是标量，而 $g_x=\widetilde cX+k$。第六次项及 (2.3) 给

$$
\widetilde b+2\widetilde c=0.
\tag{5.1}
$$

第五次项再化为

$$
\mathfrak m_n\bigl(e\widetilde a+
2d(\widetilde b+2\widetilde c)\bigr)
=\mathfrak m_n(e\widetilde a)=0.
$$

所以 $\widetilde a=g_x=0$。由引理 2.1，$\widetilde c=k=0$，再由 (5.1) 得 $\widetilde b=0$。于是 $g$ 是常数。

非零常数不能与非零 $f$ 全部矩消失，因为 (2.2)–(2.3) 将其归结为 $f=0$。矛盾。故 $e=0$。交换两端同样得 $\widetilde e=0$。

此论证也覆盖一端二次项退化、另一端已经线性或常数的情况；没有假设两端的二次齐次部分非零。

## 6. 排除两端的 $XZ$ 项

已知 $e=\widetilde e=0$。假设 $d=f_{xz}\ne0$。第六次项给

$$
8d\widetilde d=0,
$$

故 $\widetilde d=0$。此时 $g_z=\widetilde b$ 为标量，第五次项给

$$
\widetilde b+2\widetilde c=0.
\tag{6.1}
$$

把 (6.1) 代入第四次项，并用 (2.2) 把常数端移到第一位置，得到

$$
\mathfrak m_n(2d\widetilde a-3\widetilde c\,b)=0
\quad\text{对全部 }n.
\tag{6.2}
$$

这里

$$
b=dX+m,\qquad \widetilde a=\widetilde cX+k.
$$

所以由 (2.3)，

$$
-d\widetilde cX+2dk-3\widetilde c m=0.
\tag{6.3}
$$

$X$ 非常数且 $d\ne0$，故 $\widetilde c=0$，再得 $k=0$，由 (6.1) 得 $\widetilde b=0$。于是 $g$ 又是常数，矛盾。故 $d=0$，交换两端得 $\widetilde d=0$。

至此，所有反设配对必可写为

$$
f=AX^2+lX+mZ+c_0,\qquad
g=BX^2+kX+nZ+d_0.
\tag{6.4}
$$

这里 $A,B,l,k,m,n,c_0,d_0$ 都为复标量，允许任意退化。

## 7. 纯 $X^2$ 情形及全部退化分支

在 (6.4) 中，

$$
f_x=2AX+l,\qquad g_x=2BX+k,\qquad f_z=m,\qquad g_z=n.
$$

残差只剩以下四个系数恒等式：

$$
M_r(f_x,g)+M_r(f,g_x)=0,
\tag{7.1}
$$

$$
\mathfrak m_r(mg+nf)+2M_r(f_x,g_x)=0,
\tag{7.2}
$$

$$
\mathfrak m_r\bigl((n+B)f_x+(m+A)g_x\bigr)=0,
\tag{7.3}
$$

$$
mn+An+Bm+4AB=0.
\tag{7.4}
$$

这里把矩指标改成 $r$，避免与 $g$ 的 $Z$ 系数 $n$ 混淆。式 (7.3) 已除去非零数 $2$；式 (7.4) 用 $r=0$ 得到。

若任一端是常数，则已由 (2.3) 排除。下面均假设两端非零且非常数。

### 7.1 $A=B=0$：两端均至多一次

由 (7.1) 和 (2.3)，

$$
lg+kf=0.
\tag{7.5}
$$

其 $X$ 系数为 $2lk$，故 $lk=0$。若 $l\ne0$，则 $k=0$，(7.5) 给 $g=0$，矛盾；若 $k\ne0$，则同样给 $f=0$。所以 $l=k=0$。

两端非常数迫使 $m,n\ne0$。此时 (7.2) 给

$$
mg+nf=0.
$$

左端 $Z$ 系数为 $2mn\ne0$，与引理 2.1 矛盾。

### 7.2 $A=0,\ B\ne0$：一次与二次

式 (7.3) 及 (2.3) 给

$$
(n+B)l+m(2BX+k)=0.
\tag{7.6}
$$

$X$ 系数为 $2Bm$，所以 $m=0$。由于 $f=lX+c_0$ 非常数，$l\ne0$，(7.6) 再给 $n=-B$。

将这些代入 (7.2)，得

$$
\mathfrak m_r\bigl(3BlX+2lk-Bc_0\bigr)=0.
\tag{7.7}
$$

故括号内向量为零，但其 $X$ 系数 $3Bl\ne0$，矛盾。

### 7.3 $A\ne0,\ B=0$

交换两端即归于 §7.2，故同样不可能。

因此，至此已经独立证明：本定理类中，任意一个至多一次非零向量，与任意一个至多二次非零向量，不可能全部矩消失。该子结论没有援引 R41 的第一 chaos 与有限秩二阶条件；$X^2-Z$ 的二阶 Walsh 矩阵通常并不符合可随意省略对角条件的有限秩表述。

### 7.4 $AB\ne0$：最后的二次与二次

由 (7.3) 的 $X$ 项和常数项，

$$
An+Bm+2AB=0,
\tag{7.8}
$$

$$
(n+B)l+(m+A)k=0.
\tag{7.9}
$$

将 (7.8) 代入 (7.4)，得

$$
mn+2AB=0.
\tag{7.10}
$$

令 $u=m/A$、$v=n/B$。由 (7.8)、(7.10)，

$$
u+v=-2,\qquad uv=-2.
\tag{7.11}
$$

所以 $u,v$ 是 $-1+\sqrt3$、$-1-\sqrt3$，顺序任意。特别地，

$$
u+1\ne0,\qquad v+1=-(u+1).
$$

式 (7.9) 因而化为

$$
\frac{k}{B}=\frac{l}{A}=:h.
\tag{7.12}
$$

最后，用实际对称性 (2.2) 将 (7.1) 的两项合并：

$$
0=AB\,M_r\left(
2X+h,\ 
2X^2+2hX-2Z+\frac{c_0}{A}+\frac{d_0}{B}
\right)
\quad(r\ge0).
\tag{7.13}
$$

第一端是非零一次向量；第二端由引理 2.1 是非零二次向量，因为其 $X^2$ 系数为 $2$。式 (7.13) 与 §7.1–§7.3 已证明的一次与二次分离矛盾。

全部分支均已排除，定理 1.1 得证。

## 8. 相对此前失败路线增加了什么

同目录的 multivariate-curvature-obstructions 工作笔记保留了两种已核实障碍：

1. 实际有限前缀例子中，某个非零混合二阶矩序列确实会落在全部一阶矩序列张成的空间内；该例本身不满足零阶全部矩消失。
2. 仅用抽象有限维双线性矩映射和通过原点的代数曲线，曲线张成空间未必含可供低次数归纳使用的另一个非零纯张量；该抽象映射没有实现为本题实际 $A$ 的全部矩。

本定理并未否定这些障碍，而是使用它们没有包含的实际条件：

- 参数严格落在共同曲线 $(T,T^2)$，使所有高位测试成为有限的一变量残差；一旦某个残差非零，即强制系数绝对可和。
- 在全部残差恒零的剩余分支，二阶导数是标量。由 $B$-对称性，许多系数可化成同一个循环向量 $1$ 的矩。
- 循环性将这些矩等式升级为实际多项式向量等式，依次去掉 $Z^2$、$XZ$；最后 (7.13) 把剩余二次配对化为已完整处理的一次与二次配对。

因此这是 $(j^{-1},j^{-2})$ 最小非有限方向例的实际闭合，而不是又一次固定方向紧性论证。它仍未处理任意两个完全不同的有限模式、一般三次多项式、任意有限前缀多项式系数或全部有限 Walsh chaos。
