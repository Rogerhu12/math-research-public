# R637 — 原短三块在平方根预算以上的整满射

日期：2026-11-15。**状态：以下原短三块的统一整满射范围已证明。** 在原 \(J=0\) canonical 来源内，显式条件
\[
\ell\le A_D,\qquad (d_D+3)^2>36(s-A_D)
\]
足以使整个实际相对 \(J\) 整满射，其中 \(d_D\sim41D/66\) 在正文准确给出。故低 \(\ell\) 时，除原固定坏集外，
\[
D>\left(\frac{396}{41\sqrt6}+o(1)\right)\sqrt p
\]
已经进入原 \(M\) 只有单位和 \(p\) 因子的范围。常数约为 \(3.943\)。这是旧短目标及同一原来源的结论，使用全部角帽和全部 \(g\) 高尾；不是完整 \(\mathcal C_p\) 的 Smith 结论向短目标的投影。

证明的几何输入是原 ODE 对同一低轴前 \(s\) 个自由无穷近点的曲线重数平方和界。随后在一条实际可提升异常链上应用有明确假设的对数消失定理。最后把所得平面多项式空间逐列放回原来源。临界 \(D\) 约为 \(0.413\sqrt p\) 的范围仍未覆盖，主课题未完成。

## 1. 原来源与精确充分条件

保持
\[
p=6s-1>101,\qquad
1\le\ell<s-13,\qquad
f_D=\lfloor9D/2\rfloor+4<p,
\]
以及原共同好素数和固定坏素数排除。记
\[
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad
C_n=\lfloor n/2\rfloor,
\]
\[
h_7=7+4t+16t^2,\quad d(t)=1+8t,\qquad
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n}.
\]
为避免与下文平面次数混淆，\(d(t)\) 始终带参数。整个实际来源是
\[
\mathcal W_D=\bigoplus_{n=0}^D
Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\qquad
e_{n+1}=f_n-3A_n-B_n+C_n.
\tag{1}
\]
其相对整矩阵 \(J\) 的三块长度仍为 \(s,s,\ell\)。模 \(p\) 后，在原 \(t\) 参数中通过已付整单位三角换参，读数等价于
\[
P\longmapsto
\left(
P(t,\rho)_{<s},\
\mathcal EP(t,\rho)_{<s},\
\mathcal E^2P(t,\rho)_{<\ell}
\right),
\quad \mathcal E=Y\partial_Y,
\tag{2}
\]
其中 \(\rho=(1+8t)\Theta^{17}\)，只读取原模 \(t^s\) 低轴。实际 Gaussian 行单位 \(a,a^2/2\) 暂剥去；它们最后原样恢复。

置
\[
A=A_D,\qquad B=B_D,\qquad N=s-A,
\]
并定义整数
\[
\boxed{
n_0=\max\left\{0,\
\left\lceil\frac{2(D+3A+B-4)}{11}\right\rceil
\right\},\qquad
d_D=D-n_0.
}
\tag{3}
\]
在下述范围 \(D\ge3\)，有 \(0\le n_0\le D\) 及 \(N>0\)。

**定理 1。** 若
\[
\boxed{\ell\le A,\qquad (d_D+3)^2>36N,}
\tag{4}
\]
则 (1) 的同一个实际 \(J:\mathcal W_D\to\Gamma_{2s+\ell}\) 整满射。

因此对完整原矩阵
\[
M^{\rm orig}=c_*U_0m_{13}J
\]
有准确 Smith 结构
\[
\boxed{
(2s+\ell-26)\text{ 个单位},\qquad
26\text{ 个 }p,\qquad
13\text{ 个目标自由方向}.
}
\tag{5}
\]
其中 \(P_{134}\)、整个 \(U_0\) 及两条十三行 carry 均保留。若来源还包含原固定 \(T^j\) 列，且确实包含 (1) 的 \(j=0\) 子格，则同一满射结论继续成立，不需使用那些额外列。

## 2. 原低轴上的完整重数平方和

先在代数闭剩余域中工作。取原光滑形式弧
\[
\mathfrak a:\quad Y=\rho_{<s}(t),\qquad P_0=(0,1).
\]
对任意 \(1\le M\le s\)，沿此弧依次吹起前 \(M\) 个点，所得
\[
\pi:X_M\to\mathbf P^2
\]
是一条自由无穷近点链。每个下一中心只在刚产生的异常曲线上，并避开以前异常曲线的交点；这是 \(t\) 沿原弧为正规参数的直接结果。只需原弧到 \(t^{M-1}\) 的有限 jet。

对平面几何不可约曲线 \(C\) 记其次数为 \(\delta\)，在这条链上的逐次重数为 \(m_1,\ldots,m_M\)，不经过后续中心时把相应重数记为零。

**引理 2。** 对全部这样的曲线，有
\[
\boxed{
\sum_{i=1}^M m_i^2\le4\delta^2,\qquad
\sum_{i=1}^M m_i\le2\sqrt M\,\delta.
}
\tag{6}
\]
该界包括 \(Y\)-次数达到或超过 \(p\) 的曲线，没有对不可分高次数曲线应用 tame 分支论证。

### 2.1 原 ODE 的平面 Bézout 改写

若 \(C\) 不过 \(P_0\)，结论显然。除直线 \(t=0\) 外，可在仿射平面写其不可约方程
\(F(t,Y)\)，并置
\[
b_F=\deg_YF,\qquad c_F=\operatorname{mult}_{Y=1}F(0,Y).
\]
先设 \(1\le b_F<p\)。

R467 的原径向方程为
\[
\mathscr D(Y)=A_0(YY''-(Y')^2)+B_0YY'-C_0Y^2,
\]
\[
A_0=6t(1-t)d(t)^2,\quad
B_0=(5-8t)d(t)^2,\quad
C_0=(154+160t+1792t^2)/3.
\tag{7}
\]
它在 \(\rho_{<s}\) 上的余项属于 \(t^{s-1}\)。同篇的真实隐式微分多项式是
\[
\begin{aligned}
K_F={}&A_0\{Y[-F_{tt}F_Y^2+2F_{tY}F_tF_Y-F_{YY}F_t^2]
                         -F_t^2F_Y\}\\
&-B_0YF_tF_Y^2-C_0Y^2F_Y^3.
\end{aligned}
\tag{8}
\]
原首共振和 tame 分支证明给 \(F\nmid K_F\)。具体而言，假如一个单位 tame 分支满足 \(\mathscr D(Y)=0\)，对其整数 \(t\) 次幂作 tame 平均会得到
\[
(6n+5)v_n=(6n+2)v_{n-1},\quad v_0=34/15,
\]
在 \(n=s-1\) 处产生 \(0=-3v_{s-2}\ne0\)。因为 \(b_F<p\)，所需局部根的 Galois 群阶整除 \(b_F!\)，故没有 wild 分支被漏掉。

本篇在 (8) 中使用的是**总次数**，而不是 R467 的矩形次数：
\[
\boxed{\deg K_F\le3\delta+1.}
\tag{9}
\]
例如首项的次数不超过
\(4+1+(\delta-2)+2(\delta-1)=3\delta+1\)，
其余项同样逐项满足此界。

令 \(\psi_1,\ldots,\psi_{c_F}\) 是经过 \(P_0\) 的单位 Puiseux 根，
\(h_j=\operatorname{ord}_t(\psi_j-\rho_{<s})\)。
原完整 Hensel 因子的判别式给
\[
I_{P_0}(F,K_F)
\ge\sum_j\min(h_j,s)+2c_F-3.
\tag{10}
\]
这是 R467 的局部乘积式；\(F_Y\) 非单位所造成的全部损失由同一个判别式支付，不逐支免费除掉它。

沿前 \(M\) 个自由中心的重数和准确为
\[
\sum_{i=1}^M m_i=\sum_j\min(h_j,M).
\tag{11}
\]
也可由 \(Y=\rho_{<M}(t)+t^MV\) 代入后关于 \(t\) 的一般系数赋值验证 (11)；它包括 ramified 分支及其投影重数。因 \(M\le s\)，由 (9)–(11) 及平面 Bézout 得
\[
\boxed{
\sum_{i=1}^M m_i
\le\delta(3\delta+1)-2c_F+3
\le3\delta^2+\delta+1.
}
\tag{12}
\]

### 2.2 曲线属公式和小次数

逐次吹起的算术属公式、以及严格变换仍是几何整曲线，给
\[
\sum_i m_i(m_i-1)\le(\delta-1)(\delta-2).
\tag{13}
\]
故对 \(\delta\ge2\)、\(b_F<p\)，由 (12) 有
\[
\sum_i m_i^2
\le(\delta-1)(\delta-2)+3\delta^2+\delta+1
=4\delta^2-2\delta+3\le4\delta^2.
\tag{14}
\]

直线不能只粗略并入 (12)。原低轴的前两项准确为
\[
\rho(t)=1+\frac{154}{15}t
+\frac{53278}{2475}t^2+O(t^3),
\]
\[
\boxed{
\frac{53278}{2475}
=\frac{2\cdot17(22^2+3\cdot19^2)}{2475}\in k^\times.
}
\tag{15}
\]
因为 \(p>101\) 惰性，\(-3\) 在 \(\mathbf F_p\) 中不是平方；
\(p\) 不能整除 \(22^2+3\cdot19^2\)，否则 \(19\ne0\) 会给
\((22/19)^2=-3\)。其余因子也都是单位。因此一条直线与原弧的接触最多为二；直线 \(t=0\) 的接触为一。直线在所经中心处的重数都是一，所以 (6) 对 \(\delta=1\) 也成立。

最后，若 \(b_F\ge p\)，则 \(\delta\ge p>M\)。不使用 (7)–(12)，只用每个 \(m_i\le\delta\) 及 (13)，便有
\[
\sum_i m_i^2
\le\delta^2-3\delta+2+M\delta
<2\delta^2.
\tag{16}
\]
这支付全部可能的高次数或不可分曲线。

(14)–(16) 给 (6) 的第一式，第二式是 Cauchy–Schwarz。所有论证只读取原低轴前 \(s\) 位，没有把 ODE 越过首共振继续使用。

## 3. 同一弧上两个法向 jet 的平面整值域

**引理 3。** 取 \(1\le M\le s\) 和整数 \(d\ge0\)。若
\[
\boxed{d+3>6\sqrt M,}
\tag{17}
\]
则原弧上的两 jet 评价
\[
k[t,Y]_{\deg_{\rm tot}\le d}
\longrightarrow
k[t]/(t^M)\oplus k[t]/(t^M),
\quad
P\longmapsto
\bigl(P(t,\rho),P_Y(t,\rho)\bigr)
\tag{18}
\]
满射。

这不是仅作维数估计。下面证明完整 \(H^1\) 消失，并核所用正特征定理的全部假设。

### 3.1 真实异常链上的充分正性

在 \(X_M\) 上用 \(H\) 表示平面直线类，\(E_i\) 表示每次异常曲线的**总变换**。则
\[
K_{X_M}=-3H+\sum_{i=1}^M E_i.
\]
置
\[
\mathcal L=dH-2\sum_iE_i,\qquad
A_{\rm adj}=\mathcal L-K_{X_M}
=(d+3)H-3\sum_iE_i.
\]
对任意非异常不可约曲线的严格变换 \(\widetilde C\)，引理 2 给
\[
A_{\rm adj}\cdot\widetilde C
=(d+3)\delta-3\sum_i m_i
\ge(d+3-6\sqrt M)\delta>0.
\tag{19}
\]
又
\[
A_{\rm adj}^2=(d+3)^2-9M>27M.
\tag{20}
\]
严格异常曲线为
\[
C_i=E_i-E_{i+1}\quad(i<M),\qquad C_M=E_M.
\]
在 \(C_i\)、\(i<M\) 上 \(A_{\rm adj}\) 的交数为零，在 \(C_M\) 上为三。

取一个足够小的正有理数 \(c\)，令
\[
\varepsilon_i=c\,i(M-i),\quad
\Delta=\sum_{i=1}^{M-1}\varepsilon_i C_i,
\]
使
\[
\varepsilon_{\max}
<\min\{1,(d+3-6\sqrt M)/2\}.
\tag{21}
\]
当 \(M=1\) 时取 \(\Delta=0\)。异常链是简单正规交叉，
\(0\le\varepsilon_i<1\)，所以 \((X_M,\Delta)\) 是 klt 对。

有
\[
(A_{\rm adj}-\Delta)\cdot C_i=2c>0\quad(i<M),
\qquad
(A_{\rm adj}-\Delta)\cdot C_M=3-\varepsilon_{M-1}>0.
\]
对非异常曲线，沿自由链的重数不增，故
\[
0\le\Delta\cdot\widetilde C
=\sum_{i<M}\varepsilon_i(m_i-m_{i+1})
\le\varepsilon_{\max}m_1
\le\varepsilon_{\max}\delta.
\]
结合 (19)、(21)，仍有严格正交数。
另外 \(A_{\rm adj}\cdot\Delta=0\)，且
\[
\Delta^2=-\sum_{i=1}^{M}(\varepsilon_i-\varepsilon_{i-1})^2>-M
\]
（\(\varepsilon_0=\varepsilon_M=0\)）。由 (20)，平方也为正。
曲面 Nakai–Moishezon 判别因此给
\[
\boxed{
\mathcal L-(K_{X_M}+\Delta)=A_{\rm adj}-\Delta
\text{ 为 ample 的有理除子}.
}
\tag{22}
\]

### 3.2 精确使用的正特征消失定理

使用以下已发表原文：

E. Arvidsson, F. Bernasconi, J. Lacini,
*On the Kawamata–Viehweg vanishing theorem for log del Pezzo surfaces in positive characteristic*,
Compositio Math. **158** (2022), 750–763,
**Lemma 2.10（印刷页 754）**，
[官方正文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/24893DF316D4A83FE7DAFFBF9873B6D3/S0010437X22007394a.pdf/on_the_kawamataviehweg_vanishing_theorem_for_log_del_pezzo_surfaces_in_positive_characteristic.pdf)。

该引理要求完美域、\(p>2\)、二维射影 klt 对、一个连同异常和边界支撑可提升到 \(W_2(k)\) 的 log resolution，以及所用整除子减去 \(K+\Delta\) 为 ample。它在这些假设下给高次上同调消失。这里不使用“所有有理曲面都自动满足消失”的概括，也不需要把 \(X_M\) 认作 del Pezzo 曲面。

所有假设逐项满足：

- 可先扩张到代数闭完美剩余域；最终有限矩阵的满秩按忠实平坦性下降。
- \(X_M\) 光滑射影，\(\Delta\) 为系数小于一的简单正规交叉异常链，故恒等映射就是所需 log resolution。
- \(\mathbf P^2\) 与该有限自由点链可直接提升到 \(W_2(k)\)：依次提升每个在最新异常曲线上、避开旧交点的中心，再吹起其截面。全部严格异常曲线及其交点一起保持简单正规交叉。也可逐次使用同篇 Proposition 2.9。原弧只涉及有限多个系数，不要求提升一个无限微分解。
- 整除子 \(\mathcal L\) 的 \(H,E_i\) 都在该提升中定义；ample 条件已由 (22) 完整证明。

因此
\[
\boxed{H^1(X_M,\mathcal O_{X_M}(\mathcal L))=0.}
\tag{23}
\]

### 3.3 从完整簇理想返回指定两 jet

在 \(P_0\) 的完成局部环中置
\(h=Y-\rho_{<M}(t)\)。这条自由点链上各重数为二的完整簇理想为
\[
\mathcal I_{\rm cl}
=(h^2,t^Mh,t^{2M}).
\tag{24}
\]
例如末次异常赋值为 \(v(t)=1,v(h)=M\)，条件
\(v(f)\ge2M\) 给 (24)，并自动满足之前各次的重数条件。
改变 \(\rho_{<M}\) 的未读尾只改变 \(h\) 一个 \(t^M\) 倍，保持 (24)。

有
\[
\pi_*\mathcal O_{X_M}(\mathcal L)
=\mathcal I_{\rm cl}(d).
\]
Leray 的低次正合列将
\(H^1(\mathbf P^2,\mathcal I_{\rm cl}(d))\)
嵌入 (23)，故这个 \(H^1\) 为零。于是全部总次数不超过 \(d\) 的平面多项式满射到 (24) 的长度 \(3M\) 商。

指定两 jet 的理想为
\[
\mathcal I_2=(h^2,t^M),
\]
且 \(\mathcal I_{\rm cl}\subset\mathcal I_2\)。
复合到其长度 \(2M\) 商即得 (18)。这一步使用一个明确较强的簇理想，不把原两 jet 误认成完整簇理想本身。因为 \(\rho\) 是单位，用 \(\mathcal EP\) 取代 \(P_Y\) 只是可逆目标乘法。

## 4. 所得平面空间逐列属于原十九角来源

现在取定理 1 的 \(A,B,n_0,d_D,N\)。定义真实公共因子
\[
q^*(t)=(th_7)^A(t-1)^B.
\tag{25}
\]
对于 \(n_0\le n\le D\)，准确有
\[
\frac{q^*}{q_n}
=t^{A-A_n}h_7^{A-A_n}(t-1)^{B-B_n}d(t)^{C_n}
\in\mathcal O[t].
\]
其次数为
\[
3(A-A_n)+(B-B_n)+C_n.
\tag{26}
\]
因此
\[
q^*Y^nt^k\in\mathcal W_D
\quad\text{只要}\quad
k\le f_n-3A-B.
\tag{27}
\]
这同时保留有限角和无穷远帽；不是先换成自由矩形再假定返回。

由 (3)，
\[
\lfloor11n_0/2\rfloor\ge D+3A+B-4
\]
（若右侧为负，\(n_0=0\) 的情形同样直接成立）。由于
\(f_{n_0}+n_0=\lfloor11n_0/2\rfloor+4\)，得到
\[
f_{n_0}-3A-B\ge D-n_0=d_D.
\]
\(f_n\) 随 \(n\) 增加。故有显示的实际包含
\[
\boxed{
q^*(t)Y^{n_0}\,
k[t,Y]_{\deg_{\rm tot}\le d_D}
\subset\mathcal W_D/p\mathcal W_D.
}
\tag{28}
\]
事实上同一包含在原整数环上成立。

在原点，(25) 是 \(t^A\) 乘一个单位；\(Y^{n_0}\) 在 \(Y=\rho(t)\) 处也是单位。因此在前两个原 jet 上，乘 \(q^*Y^{n_0}\) 等价于乘 \(t^A\) 后作一个完整可逆的二乘二三角单位变换。它保留所有实际系数，而不只保首项。因为 \(A\ge\ell\)，(28) 在原第三块中恒为零。

由 (4)，引理 3 可用 \(M=N=s-A,d=d_D\)。所以 (28) 的同一个实际像已包含前两块的全部 \(t^A\) 倍，即
\[
\bigl(t^Ak[t]/t^s,\ t^Ak[t]/t^s,\ 0\bigr).
\tag{29}
\]

## 5. 原低行的实际单位子式及整满射

剩下只需同时支付前两块次数 \(<A\) 及第三块次数 \(<\ell\)。
记
\[
b_n=A_n+e_{n+1},\qquad
\rho_{\rm ind}(r)=\min\{n:b_n\ge r\}.
\]
原 \(b_n\) 严格增加且 \(b_n\ge n\)，所以
\(\rho_{\rm ind}(r)\le r\)。

对每个 \(0\le r<A\)，若 \(r<\ell\) 取连续三个 charge
\[
n=\rho_{\rm ind}(r),\ n+1,\ n+2;
\]
否则取前两个。所用列准确为
\[
Y^{n+i}q_{n+i}(t)t^{r-A_{n+i}}.
\tag{30}
\]
它们全部实际存在：

- \(n+i\le r+2\le A+1\le D\)，因为 \(D\ge3\)；
- \(A_{n+i}\le\lfloor(r+3)/4\rfloor\le r\)，其中 \(r=0\) 也直接成立；
- \(b_{n+i}\ge b_n\ge r\)，故上帽同样满足。

每列在 \(t^r\) 处的首系数是 \(7^{A_{n+i}}(-1)^{B_{n+i}}\) 乘原单位。其两/三个 Euler 读数对应
\((1,n+i,(n+i)^2)\)。连续节点的 Vandermonde 行列式为一或二，连同真实 Gaussian 行因子 \(a,a^2/2\) 后仍为单位。

按 \(r\) 从小到大消去，(30) 因而给这些全部低行的实际单位右逆。低行消元可以产生任意实际高尾；它们没有被删除。所有剩余目标此时正落在 (29)，再由 (28) 一次补齐，且不会改变第三块或已支付的低行。

这证明同一完整 \(\bar J\) 满行秩。原来源与目标准确有限自由，所以某个实际方子式为 \(p\) 单位，从而 \(J\) 整满射。定理 1 的主体成立。

## 6. 完整原 M、两十三行及同一修正

仍使用原目标长度 \(2s+\ell+13\)，原
\(m_{13}\) 的两条十三行分别乘 \(p\)，而最初十三行是实际零行。
由于 \(J\) 已整满射，\(m_{13}J\) 的像恰为
\(m_{13}\Gamma_{2s+\ell}\)。恢复完整单位 \(c_*U_0\) 后给 (5)。

因此 R449 的真实相对 \(C_2(J)\) 为零，原 \(M\) 的 \(C_2\) 只有最初十三个自由方向；实际来源的第二障碍在这些方向本来为零。没有相对 \(p^2\) 缺陷，也没有原有限 \(p^2\) Smith 因子可供 Miller 修正配对。

这给的是整个有限来源的一个整右逆；需要修正时，全部块和两条十三行可在同一个来源向量中联立选择。它不声称任意预先固定的首次修正 \(R\) 的逐坐标代表已经为零：允许的首次修正变化和下一位修正仍按 R449 的同一个精确序列进行。不存在把第一块和第二块用不同 \(R\) 分别解掉的步骤。

## 7. 新范围的量级及仍留下的临界区

从 (3) 得
\[
A_D=\frac D4+O(1),\quad B_D=\frac D3+O(1),\quad
n_0=\frac{25}{66}D+O(1),\quad
d_D=\frac{41}{66}D+O(1).
\]
对固定低 \(\ell\)，\(A_D\ge\ell\) 最终自动成立。在
\(D=O(\sqrt p)\) 时，\(N=s-A_D=p/6+O(\sqrt p)\)。因此对任意固定 \(\varepsilon>0\)，充分大的共同好惰性 \(p\) 上，
\[
\boxed{
D\ge\left(\frac{396}{41\sqrt6}+\varepsilon\right)\sqrt p,
\qquad f_D<p
}
\tag{31}
\]
足以满足 (4)。这里
\[
\frac{396}{41\sqrt6}\approx3.943.
\]
精确使用时始终优先用整数条件 (3)、(4)，不以近似常数替代端点。

R629 的逐阶满射门为 \(b_D\ge s-13\)，主尺度是 \(D\ge p/25+O(1)\)。
(31) 对充分大 \(p\) 严格进入该门以下，故是原短目标的新范围，
并非重复其连续 charge 消元。

另一方面，低 \(\ell\) 的来源维数约为 \(47D^2/24\)，原短行数约为 \(p/3\)，所以维数平衡为
\[
D\sim\sqrt{\frac8{47}}\sqrt p\approx0.413\sqrt p.
\]
本篇的充分门没有覆盖这一区间。它把仍可能具有实际较深相对缺陷的预算限制到明确的较小范围，但没有判定该范围中 R651 的指定 forcing 或同一个 \(R\) 的第二余类。

原 \(S/T/U\) 完整中央基准没有被使用或扩大。整满射和有限余类消失均不是原中央非零、也不是跨素数 Sha 有限的证书；主目标继续开放。

## 依据

- R467：原 ODE、tame 各支的首共振、完整 Hensel 判别式及 (10) 的局部接触估计。
- R305/R434：原 \(\rho=(1+8t)\Theta^{17}\) 的精确低系数，给 (15)。
- Arvidsson–Bernasconi–Lacini (2022), Proposition 2.9、Lemma 2.10：只在本篇明确构造的可提升异常边界及 ample 差除子上使用。
- R412/R449：原 \(m_{13}\)、完整 \(U_0\)、两条 carry 带及同一修正的第二余核运输。

本篇是统一参数证明，没有新增目标素数扫描。
