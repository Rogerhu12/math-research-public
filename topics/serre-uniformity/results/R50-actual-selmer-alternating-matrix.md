# R50：实际固定 CM 同余的 Selmer 群与交替矩阵

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的结构定理；主目标仍未解决。** 对固定参考曲线 $A:y^2=x^3-x$ 及每个 $p>37$、$p\equiv3\pmod4$，先无条件证明 $\operatorname{Sel}_p(A/\mathbb Q)=0$。若实际存在非 CM 同余 $E[p]\simeq A[p]$，令 $s$ 为新增**分裂乘法**素数的个数，则构造一个来自真实全局上同调的 $s\times s$ 交替矩阵 $M_E$，使
$$
\boxed{\operatorname{Sel}_p(E/\mathbb Q)\simeq\ker M_E,\qquad
M_E^{\mathsf T}=-M_E.}\tag{50.1}
$$
于是
$$
0\le\dim_{\mathbb F_p}\operatorname{Sel}_p(E)\le s,\qquad
\dim_{\mathbb F_p}\operatorname{Sel}_p(E)\equiv s\pmod2.\tag{50.2}
$$
特别地，$s=0$ 时群为零，$s=1$ 时维数恰为一。最后一种情形不能未经额外论证改写成 Mordell–Weil 秩一。

## 1. 参考曲线的 Selmer 群为零

### 1.1 中心值与周期

$A$ 的导子为 $32$。由模性和 $\dim S_2(\Gamma_0(32))=1$，其新形式为
$$f_{32}(\tau)=\eta(4\tau)^2\eta(8\tau)^2.$$
Li–Long–Tu (2018), §3、Lemma 3.1 完整证明了
$$L(A,1)=\frac18 B\left(\frac12,\frac14\right).\tag{50.3}$$
为固定归一化，可从该文微分恒等式 (3.1) 直接重作积分。沿虚轴取
$$x=\sqrt{\lambda(4\tau)},\qquad y=(1-x^2)^{1/4}>0.$$
该恒等式为
$$\frac{dx}{y^3}=8\pi i f_{32}(\tau)\,d\tau.$$
当 $\tau$ 从 $0$ 走向 $i\infty$ 时，$x$ 从 $1$ 降至 $0$，故 Mellin 公式给
$$
L(A,1)=\frac14\int_0^1(1-x^2)^{-3/4}\,dx
=\frac18B\left(\frac12,\frac14\right)>0.
$$

全局极小模型 $y^2=x^3-x$ 的 Néron 微分为 $dx/(2y)$。恒等实分量对应 $x\ge1$，沿上下两支积分得到最小正实周期
$$
\Omega_A^+=\int_1^\infty\frac{dx}{\sqrt{x^3-x}}
=\frac12 B\left(\frac14,\frac12\right).
$$
最后依次使用 $u=1/x$、$v=u^2$。所以
$$\boxed{L(A,1)/\Omega_A^+=1/4.}\tag{50.4}$$
若实周期约定为两个实分量上的总积分，所得比为 $1/8$；两种约定相差二，对奇素数赋值无影响。

### 1.2 已发表的 supersingular CM 定理

$p\equiv3\pmod4$ 在 $\mathbb Q(i)$ 中惰性，且 $A$ 在 $p$ 好超奇异。Pollack–Rubin (2004), Theorem 8.2 给
$$
A(\mathbb Q)\text{ 有限},\qquad
v_p(\#\Sha(A/\mathbb Q))=v_p(L(A,1)/\Omega_A).
$$
原文将可能的非 $p$ 因子记为 $r\in\mathbb Q^\times$，并证明 $v_p(r)=0$；此处没有假设完整 BSD。由 (50.4)，$\Sha(A)[p]=0$。

又 $A$ 在 $3$ 好约化且 $\#A(\mathbb F_3)=4$。素于 $3$ 的挠点约化单射排除 $A(\mathbb Q)[p]$；有限群 $A(\mathbb Q)$ 上乘 $p$ 因而可逆。Kummer 正合列
$$
0\longrightarrow A(\mathbb Q)/pA(\mathbb Q)
\longrightarrow\operatorname{Sel}_p(A)
\longrightarrow\Sha(A)[p]\longrightarrow0
$$
遂给 $\operatorname{Sel}_p(A)=0$。这对全部所述 $p$ 成立，无未计算的例外素数。

## 2. 局部条件的共同商

固定实际 Galois 同构 $\phi:E[p]\to A[p]$，把两边记为 $V$。令
$$
T=\{q:v_q(j(E))<0\},\qquad
S=\{q\in T:E/\mathbb Q_q\text{ 是分裂乘法约化}\},
\qquad s=|S|.
$$
**“分裂乘法”是约化类型，不是 $q$ 在 $\mathbb Q(i)$ 中的分解类型。**

记局部 Kummer 子空间为 $L_v^A,L_v^E\subset H^1(\mathbb Q_v,V)$。R17 证明了 $v\notin S$ 时两者相等，而 $q\in S$ 时
$$
\dim\frac{L_q^A}{L_q^A\cap L_q^E}
=\dim\frac{L_q^E}{L_q^A\cap L_q^E}=1.\tag{50.5}
$$

由 $A$ 的 Weil 配对定义
$$
B_v(x,y)=\operatorname{inv}_v(x\cup_{e_p}y)
\in\tfrac1p\mathbb Z/\mathbb Z\simeq\mathbb F_p.\tag{50.6}
$$
局部 Tate 对偶使它非退化，且每个 Kummer 子空间为自身的正交补。此形式是**对称**的：交换两个一次上同调类与交换 Weil 配对的两个因子各给一个负号，二者抵消。相关已发表局部对偶陈述见 Poonen–Rains 的极大各向同性命题。

即使 $\phi$ 不是辛同构，$L_v^E$ 仍对 $B_v$ 自对偶：二维空间的两个非退化交替配对相差一个非零标量；整体缩放不改变零配对及正交补。

置
$$
C_q=L_q^A\cap L_q^E,\qquad D_q=L_q^A+L_q^E=C_q^\perp.
$$
商 $W_q=D_q/C_q$ 有诱导的非退化对称形式，维数为二；两条不同各向同性直线为
$$\mathfrak a_q=L_q^A/C_q,\qquad \mathfrak e_q=L_q^E/C_q.$$
特别地，$q\equiv1\pmod p$ 时完整 $H^1$ 可以是四维、两 Kummer 空间各二维且相交一维；必须先作这个商，不能直接把完整 $H^1$ 当二维。

令
$$
W=\bigoplus_{q\in S}W_q,\qquad
\mathfrak A=\bigoplus_q\mathfrak a_q,\qquad
\mathfrak E=\bigoplus_q\mathfrak e_q.
$$
则
$$
W=\mathfrak A\oplus\mathfrak E,\qquad
\dim W=2s,\quad \dim\mathfrak A=\dim\mathfrak E=s,\tag{50.7}
$$
且 $\mathfrak A,\mathfrak E$ 互补、极大各向同性。

## 3. 真正的全局像

定义
$$
H^+=\{c\in H^1(\mathbb Q,V):
\operatorname{loc}_v c\in L_v^A\ (v\notin S),\
\operatorname{loc}_q c\in D_q\ (q\in S)\},
$$
并令 $H^-$ 为在全部 $q\in S$ 进一步落入 $C_q$ 的子空间。因为 $H^-\subset\operatorname{Sel}_p(A)=0$，局部化给单射
$$\iota:H^+\hookrightarrow W.\tag{50.8}$$

使用 Poitou–Tate 对偶的 Selmer 条件比较式：嵌套条件 $\mathcal F\subset\mathcal G$ 给相关正合部分
$$
0\longrightarrow H^1_{\mathcal F}(\mathbb Q,V)
\longrightarrow H^1_{\mathcal G}(\mathbb Q,V)
\longrightarrow\bigoplus_v\mathcal G_v/\mathcal F_v
\longrightarrow H^1_{\mathcal F^*}(\mathbb Q,V^*)^\vee.
\tag{50.9}
$$
最后的映射以局部 Tate 配对和局部化定义。此式是 Milne, Arithmetic Duality Theorems, I.4.10(c) 的标准有限条件比较；Poonen–Rains 所引的中间 Poitou–Tate 序列给同一正交湮灭子陈述。

取 $\mathcal F=(L_v^A)$，$\mathcal G_q=D_q$ 对 $q\in S$，其余不变。Weil 配对识别 $V^*=V$，且 $\mathcal F^*=\mathcal F$。(50.9) 两个端点都为零，故
$$
H^+\xrightarrow{\sim}\bigoplus_{q\in S}D_q/L_q^A
\simeq\mathfrak E.\tag{50.10}
$$
该映射是 (50.8) 后沿 $\mathfrak A$ 投影。于是
$$\dim H^+=s,\qquad \iota(H^+)\cap\mathfrak A=0.$$

令 $\Gamma=\iota(H^+)$。对 $c,d\in H^+$，全局 Brauer 互反给
$$\sum_v B_v(\operatorname{loc}_v c,\operatorname{loc}_v d)=0.$$
在 $v\notin S$ 两类落入同一 Kummer 子空间，配对为零；在 $S$ 内，配对下降到 $W_q$。因此 $\Gamma$ 各向同性，由维数又极大。

这一步没有假定任意局部数据能同时提升。(50.9) 与参考 Selmer 群为零恰好证明了 (50.10) 所需的提升与唯一性。

## 4. 交替矩阵与精确核

按固定顺序枚举 $S=\{q_1,\ldots,q_s\}$，选基
$$a_i\in\mathfrak a_{q_i},\qquad e_i\in\mathfrak e_{q_i},\qquad B(a_i,e_i)=1.$$
不同局部分量正交，故在这组坐标中
$$
B((a,e),(a',e'))=a^{\mathsf T}e'+e^{\mathsf T}a'.\tag{50.11}
$$
由 (50.10)，有唯一矩阵 $M_E$ 使
$$\Gamma=\{(M_Ex,x):x\in\mathbb F_p^s\}.\tag{50.12}$$
各向同性给
$$0=x^{\mathsf T}(M_E^{\mathsf T}+M_E)y\quad\text{对全部 }x,y,$$
故 $M_E^{\mathsf T}=-M_E$。因 $p$ 奇，其对角元全零。

一个全局类属于 $\operatorname{Sel}_p(E)$，当且仅当它在 $S$ 内落入 $L_q^E$；其余条件已相同。因而其像恰为
$$
\Gamma\cap\mathfrak E=\{(0,x):M_Ex=0\},
$$
证明 (50.1)。换基、重排素数或改变既定同构可改变矩阵，实际核的同构类型不变；条目不是由 $s$ 单独决定的常数。

## 5. 奇偶性、秩与小 s

交替矩阵的秩为偶数：若它非零，选一对配对非零的向量分出非退化二维块，在正交补归纳即可。所以
$$
\dim\operatorname{Sel}_p(E)=s-\operatorname{rank}M_E
\in\{s,s-2,s-4,\ldots\}.\tag{50.13}
$$

- $s=0$：$\operatorname{Sel}_p(E)=0$，故 $\operatorname{rank}E(\mathbb Q)=0$ 且 $\Sha(E)[p]=0$。
- $s=1$：$M_E=(0)$，故 $\dim\operatorname{Sel}_p(E)=1$。
- $s=2$：$M_E=\left(\begin{smallmatrix}0&m\\-m&0\end{smallmatrix}\right)$；$m\ne0$ 时维数零，$m=0$ 时维数二。
- 奇数 $s$：一定有非零 $p$-Selmer 类。

因 $E(\mathbb Q)[p]=A(\mathbb Q)[p]=0$，
$$
\dim\operatorname{Sel}_p(E)=\operatorname{rank}E(\mathbb Q)+\dim\Sha(E)[p].\tag{50.14}
$$
所以总有 $\operatorname{rank}E(\mathbb Q)\le s$。若另知 $\Sha(E)[p^\infty]$ 有限，奇数 $p$ 的 Cassels–Tate 配对才进一步使 $\dim\Sha(E)[p]$ 为偶数，并将 (50.13) 转为秩的同余。本文不假设所有实际 $E$ 的 $\Sha[p^\infty]$ 有限，也不把 $s=1$ 时唯一 Selmer 方向擅自提升成有理非挠点。

## 6. 从 R19 坐标确定 S

乘法素数 $q\ge5$ 处，整极小模型为分裂乘法型，当且仅当 $-c_6$ 模 $q$ 为平方；这也直接由结点的两条切线得到。

R19 族 I、II 有 $c_6=1728W=3W\cdot24^2$；族 III 有 $c_6=13824W=6W\cdot48^2$。原始性给 $q\nmid W$，因此
$$
S=\begin{cases}
\{q\mid Z:(-3W/q)=1\},&\text{族 I、II},\\
\{q\mid Z:(-6W/q)=1\},&\text{族 III}.
\end{cases}\tag{50.15}
$$
$(\,\cdot\,/q)$ 表示 Legendre 符号。它给出准确的输入素数集，没有计算全局矩阵的非对角条目。

## 7. 对下一步的准确限制

本篇补上了参考 Selmer 群为零的无条件证明，并把 R17 的上界加强为实际交替矩阵和奇偶性。它不排除非 CM 实际同余曲线：秩零、零 $p$-Selmer 与非 CM 性并不矛盾，非零 Selmer 类也可能属于 $\Sha[p]$。

仅用局部维数、互反和交替形式，无法产生对 $p$ 的矛盾：任意奇 $p$ 和任意 $s$ 都有零矩阵及各偶秩交替矩阵，给合法的抽象极大各向同性图。此句仅针对线性代数，不声称每个矩阵能由本题实际曲线实现。

R46 的 $B_a:y^2=x^3+a$、$D_a:y^2=x^3-27a$ 是另一对辅助曲线；实际 Frey 曲线 $E$ 与它们没有给出的有理同源。故 (50.1) 或 $s=0$ 时的零 Selmer 群，不推出辅助三同源 Selmer 群为零。继续此路需要控制实际矩阵条目，或建立新的算术联系。

## 8. 已核验来源

- R. Pollack and K. Rubin, **The main conjecture for CM elliptic curves at supersingular primes**, Annals of Mathematics **159** (2004), 447–464，Theorem 8.2、§5 的周期定义及式 (12)。[期刊页](https://annals.math.princeton.edu/2004/159-1/p11)，[期刊全文存档](https://arxiv.org/pdf/math/0509604)。仅对 CM 参考曲线应用，不对非 CM 的 $E$ 套用。
- W.-C. W. Li, L. Long and F.-T. Tu, **Computing Special L-Values of Certain Modular Forms with Complex Multiplication**, SIGMA **14** (2018), 090，§3、式 (3.1)、Lemma 3.1。[全文](https://arxiv.org/pdf/1803.06072)，[DOI](https://doi.org/10.3842/SIGMA.2018.090)。上文另算 $A$ 的实周期，避免混淆等同源模型。
- B. Poonen and E. Rains, **Random maximal isotropic subspaces and Selmer groups**, Journal of the American Mathematical Society **25** (2012), 245–269。[作者全文](https://math.mit.edu/~poonen/papers/quadratic.pdf)，该版本 Proposition 6.5、Theorem 6.8 及其引用的 Poitou–Tate 中间序列；Remark 2.4 给各向同性商。本文只用确定性对偶，不使用随机分布模型。
- J. S. Milne, **Arithmetic Duality Theorems**, 2nd ed. (2006)，Chapter I, Theorem 4.10(c)：Poitou–Tate 对偶；(50.9) 为嵌套有限 Selmer 条件的标准比较式。
- 仓库 [R17](R17-local-selmer-conditions-at-new-primes.md)、[R19](R19-converse-fermat-fixed-cm.md) 提供全部局部条件和精确整数模型。
