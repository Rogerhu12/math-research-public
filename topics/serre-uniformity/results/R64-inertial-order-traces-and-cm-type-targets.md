# R64. 惯性字符阶的精确部分迹与由 CM 点实现的类型靶集

日期：2026-11-12。会话：serre-uniformity-astra-resume2；qc_global。

**状态：已证明。** 设 $p>37$，$X=X_{\rm ns}^+(p)$，$J=\operatorname{Jac}(X)$。本文细化 R59 的 supercuspidal 部分，计算完整 $J$ 上按惯性字符阶选出的全局 Hecke 幂等元在每个 Drinfeld 分量的准确部分迹。由此得到一个实际坏高度子空间的精确秩，并把它的全部坏处靶值接到明确的有理 CM 点。

这里始终区分完整 $J$ 与 R45 的真实 Heegner 商 $A$。字符阶幂等元在完整 $J$ 上的迹可精确求出；投影到任意 $A$ 后，不能把这些迹原样保留。对真实 QC 方程，本文只使用实际包含于 $A$ 的类型方向。

## 1. 记号及惯性字符阶幂等元

置
$$M=p+1,\qquad
\mathcal D_p=\{d:d\mid M,\ v_2(d)=v_2(M),\ d>2\}.
\tag{1.1}$$
下文的 $d$ 表示惯性字符阶；全部尖点除子的度数另记为 $\delta=(p-1)/2$，避免混淆。

R59 给完整有理 Hecke 代数的分解
$$\mathbb T_{\mathbb Q}
=\mathbb T_{\rm ps}\oplus\mathbb T_{\rm sc}\oplus\mathbb T_{\rm tor},
\qquad e_{\rm ps}+e_{\rm sc}+e_{\rm tor}=1.
$$
对一个 supercuspidal 新形式 $f$，其二维 Weil–Deligne 表示的有限惯性字符为 $\theta,\theta^{-1}$，二者阶相同，且该阶整除 $M$。对每个阶 $d$，令 $e_d$ 为所有此阶因子的完整全局 Galois 轨道之和。

这确实给定义于 $\mathbb Q$ 的 Hecke 幂等元：系数域自同构把有限阶惯性字符变成互素次幂，保持其阶；R59 §1 的局部全局相容性保证该划分是全局新形式因子的划分。不同 $e_d$ 正交。定理 1 将证明只有 (1.1) 中的阶出现，且
$$e_{\rm sc}=\sum_{d\in\mathcal D_p}e_d.
\tag{1.2}$$

设 $\mathcal S_p$ 为全部几何超奇异 $j$ 标号。记
$$n_{\rm gen}=|\mathcal S_p\setminus\{0,1728\}|,\qquad
\epsilon_0=\begin{cases}1,&p\equiv2\pmod3,\\0,&p\equiv1\pmod3.\end{cases}
$$
惯性字符用一个辅助上同调素数 $r\ne p$ 计算，必要时扩张 $\mathbb Q_r$ 以包含相关根单位。这不改变最后的有理迹与维数。

## 2. 每个一般 Drinfeld 分量上的字符，逐个计数

Edixhoven–Parent (2021), Theorem 3.5，pp.249–251，给一般标号对应的光滑射影曲线
$$D:Y^2=X(X^{M/2}+a),\qquad a\ne0.
\tag{2.1}$$
该文 §2.2.4 与 (23) 中的坐标变换给有限惯性作用
$$X\longmapsto u^{2(p-1)}X,\qquad
Y\longmapsto u^{p-1}Y,
\quad u\in\mathbb F_{p^2}^{\times}.
$$
因为 $u^{p-1}$ 遍历 $\mu_M$，可用生成元 $\zeta\in\mu_M$ 写作
$$\sigma(X,Y)=(\zeta^2X,\zeta Y).
\tag{2.2}$$
这里是完整有限惯性经过 $\mu_M$ 的作用；不是把 (2.2) 再限制到 R59 的范数一子群后误少算一个二因子。

### 引理 1：一般分量的全部 $H^1$ 字符

在 $H^1(D)$ 中，每个以下列出的字符都恰出现一次：

- 若 $p\equiv1\pmod4$，字符为 $\zeta\mapsto\zeta^k$，其中 $k$ 遍历模 $M$ 的全部奇数，唯独去掉 $k=M/2$。
- 若 $p\equiv3\pmod4$，字符为模 $M$ 的全部奇指数字符。

等价地，对于每个 $d\in\mathcal D_p$，所有阶恰为 $d$ 的 $\varphi(d)$ 个字符各出现一次；此外没有字符。

**证明。** 写 $m=M/2$。曲线 (2.1) 的全纯微分基为
$$\omega_i=X^i\frac{dX}{Y},\qquad 0\le i<g(D),$$
且由 (2.2)，
$$\sigma^*\omega_i=\zeta^{2i+1}\omega_i.
\tag{2.3}$$

上述微分计算可严格用于 étale $H^1$ 的特征标：将 $a$ 及 $M$ 次根单位提升到不分歧特征零离散赋值环。因 $p\nmid2M$ 且 $a$ 为单位，分支多项式在特殊纤维无重根，曲线有光滑射影提升，作用 (2.2) 也提升。光滑真基变换使 $H^1_{\rm et}$ 的有限群特征标不变。在特征零，经比较同构，$H^1$ 的字符为全纯微分的字符及其逆字符。也可从 $H^1_{\rm dR}$ 的 Hodge 短正合列和 Serre 对偶得到同一结论。

若 $m$ 奇，即 $p\equiv1\pmod4$，则 $g(D)=(m-1)/2$。式 (2.3) 给
$$1,3,\ldots,m-2,$$
其负数模 $2m$ 给其余大于 $m$ 的奇数，恰漏掉二次字符指数 $m$。

若 $m$ 偶，即 $p\equiv3\pmod4$，则 $g(D)=m/2$。式 (2.3) 给
$$1,3,\ldots,m-1,$$
与其负数合起来恰为模 $2m$ 的全部奇数。此时二次字符指数 $m$ 本来是偶数。

一个模 $M$ 的字符 $k$ 具有阶 $d=M/\gcd(k,M)$。$k$ 为奇数恰等价于 $v_2(d)=v_2(M)$。去掉二次字符又恰为要求 $d>2$。每个给定阶有 $\varphi(d)$ 个本原字符，故得到最后的等价描述。证毕。

特别要区分两种数：$H^1$ 中阶 $d$ 的字符数是 $\varphi(d)$；相应阿贝尔维数才需要再除以 $2$。不能先把 $\theta,\theta^{-1}$ 合成一对，再把该对数误写成 $H^1$ 的迹。

## 3. 两个特殊标号及全局块维数

### 引理 2：$j=0$ 的三次商恰保留 $d\mid M/3$

当 $0\in\mathcal S_p$ 时，完整一般方程上的额外自同构为
$$X\longmapsto\eta^2X,\qquad Y\longmapsto\eta Y,
\qquad \eta^3=1.
\tag{3.1}$$
因此 $D_0$ 的 $H^1$ 恰保留引理 1 中阶 $d$ 满足 $d\mid M/3$ 的字符，每个仍一次。$D_{1728}$ 的 $H^1$ 为零。

**证明。** EP Theorem 3.5 的证明，p.251，明确计算几何自同构 $[\zeta_6]$ 为 $X\mapsto\zeta_6^4X$、$Y\mapsto\zeta_6^2Y$。置 $\eta=\zeta_6^2$ 即为 (3.1)。它正是 (2.2) 的 $\mu_3$ 子群，并且商曲线的坐标可取 $X^3,XY$；方程为
$$Y_0^2=X_0(X_0^{M/6}+a).$$
商的次数为 $3$，素于 $p$，所以商曲线的 $H^1$ 等于原曲线 $H^1$ 的 $\mu_3$ 不变量。

指数 $k$ 的字符在 $\mu_3$ 上平凡当且仅当 $3\mid k$。若其阶为 $d$，写 $k=(M/d)b$、$\gcd(b,d)=1$。若 $3\mid M/d$，所有这类 $k$ 都为 $3$ 的倍数。若 $3\nmid M/d$，则 $3\mid d$ 且 $3\nmid b$，所有这类 $k$ 都不是 $3$ 的倍数。因此精确条件为 $d\mid M/3$。

同一页计算额外 $[i]$ 为超椭圆对合，其商 $D_{1728}$ 是 $\mathbb P^1$。于是该处 $H^1=0$。证毕。

令 $P_{D_j}$ 为单值中间分次到分量 $H^1(D_j)$ 的规范投影，按 R59 定义
$$\tau_j(G)=\operatorname{Tr}(P_{D_j}G\mid\operatorname{gr}_1^M H^1).$$

### 定理 1：准确的字符阶部分迹及块维数

对于完整 $J$ 上的 $e_d$，
$$\boxed{\quad
\tau_j(e_d)=\varphi(d)\varepsilon_j(d),\qquad
\varepsilon_j(d)=
\begin{cases}
1,&j\ne0,1728,\\
\mathbf1_{d\mid M/3},&j=0,\\
0,&j=1728.
\end{cases}
\quad}\tag{3.2}$$
进而
$$\boxed{\quad
a_d:=\dim(e_dJ)
=\frac{\varphi(d)}2
\left(n_{\rm gen}+\epsilon_0\mathbf1_{d\mid M/3}\right).
\quad}\tag{3.3}$$
式中只在 $\epsilon_0=1$ 时解释 $d\mid M/3$ 的项。只有 $d\in\mathcal D_p$ 出现，且每个这样的块非零。

**证明。** R59 定理 3 已严格证明 supercuspidal 全部 $H^1$ 贡献恰为各 Drinfeld 分量 $H^1$ 的直和。全局 $e_d$ 在有限惯性阶 $d$ 的全部子空间上为恒等，在其他阶上为零。因此它在中间分次上就是由惯性作用确定的精确阶投影；特别地，这些特定投影保持各 $H^1(D_j)$。引理 1、2 给 (3.2)。

把 (3.2) 对全部 $j$ 求和得到 $H^1(e_dJ)$ 的维数；它等于 $2\dim(e_dJ)$，故得 (3.3)。没有其他字符阶可出现，因此得到 (1.2)。当 $p>37$，一般超奇异标号的数目为正，故 (3.3) 对每个 $d\in\mathcal D_p$ 都为正。证毕。

作为因子二的具体核对，$p=41$ 时 $M=42$，容许阶为 $6,14,42$，一般标号数为 $3$，并有 $j=0$。于是
$$a_6=\frac{2\cdot3}{2}=3,\qquad
a_{14}=\frac{6\cdot4}{2}=12,\qquad
a_{42}=\frac{12\cdot3}{2}=18.$$
三者和为 $33$，与 R59 的 $\dim J_{\rm sc}=33$ 一致。

## 4. 完整类型维数和可用的迹补偿

记 $a_{\rm ps}=\dim J_{\rm ps}$、$a_{\rm sc}=\dim J_{\rm sc}$、$t=\dim J_{\rm tor}$。有

| $p\bmod12$ | $a_{\rm ps}$ | $a_{\rm sc}$ | $t$ |
|---|---:|---:|---:|
| $1$ | $(p-9)(p-13)/48$ | $(p-1)^2/48$ | $(p-13)/12$ |
| $5$ | $(p-5)(p-17)/48$ | $(p-5)(p+3)/48$ | $(p-5)/12$ |
| $7$ | $(p-7)^2/48$ | $(p-7)(p+1)/48$ | $0$ |
| $11$ | $(p-3)(p-11)/48$ | $(p-7)(p+1)/48$ | $0$ |

**证明。** 总亏格为
$$g(X)=\frac{p^2-10p+23+6(\frac{-1}{p})+4(\frac{-3}{p})}{24};
\tag{4.1}$$
可核对 Rouse–Sutherland–Zureick-Brown (2022), Lemma 12.8，p.37，其中列出非分裂正规化子群的这一亏格公式。EP Theorem 3.5 给表中的 $t$。

几何超奇异标号数在四个剩余类依次为
$$\frac{p-1}{12},\quad\frac{p+7}{12},\quad
\frac{p+5}{12},\quad\frac{p+13}{12}.$$
其中特殊标号分别为无、仅 $0$、仅 $1728$、二者都有。一般 Drinfeld 亏格在 $p\equiv1\pmod4$ 时为 $(p-1)/4$，在 $p\equiv3\pmod4$ 时为 $(p+1)/4$。$j=0$ 的亏格由引理 2 的商方程依次为 $(p-5)/12$（剩余类 $5$）及 $(p+1)/12$（剩余类 $11$）；$j=1728$ 为零。

逐项相加给 $a_{\rm sc}=\sum_jg(D_j)$，再由 R59 的分解用 $a_{\rm ps}=g-a_{\rm sc}-t$，即得到全表。此推导也可直接由 (3.3) 对 $d$ 求和完成。证毕。

特别地，所有 $p>37$ 都有
$$a_{\rm ps}>0.
\tag{4.2}$$
所以完整 $J$ 中的任意有限个类型标量方向，都可用 $e_{\rm ps}$ 补偿其总迹；R59 已证明这一补偿不改变 Drinfeld 部分迹和图项。式 (4.2) 不声称实际 $A$ 的 principal-series 部分一定非零。

## 5. 类型内为标量的方向：坏高度映射的精确秩

定义完整 $J$ 中的有理子空间
$$Z^{\rm type}
=\mathbb Qe_{\rm ps}\oplus\mathbb Qe_{\rm tor}
\oplus\bigoplus_{d\in\mathcal D_p}\mathbb Qe_d,
\qquad
W^{\rm type}=Z^{\rm type}\cap\ker\operatorname{Tr}.
\tag{5.1}$$
若 $e_{\rm tor}=0$，省略该零项。这里不是把整个 Hecke 代数称为一个小“中心”；整个代数本来就是交换的。式 (5.1) 只是要求在每个完整惯性类型块上为有理标量。

沿用 R59 的
$$a_j=1\ (j\ne0,1728),\qquad a_0=3,\qquad a_{1728}=2,$$
以及实际线性泛函
$$\Xi_j(G)=a_j\tau_j(G)+\frac{p^2-1}{2}Q_j(G).
$$
对总迹为零的方向，R59 给
$$k_j(G)-k_i(G)
=-\frac{p-1}{p+1}\bigl(\Xi_j(G)-\Xi_i(G)\bigr).
\tag{5.2}$$
这里的 $k$ 已经来自一次 $G\mapsto2G$ 的实际线丛，边长使用 $v_p(p)=1$。本文没有再乘 $2$ 或 $\delta^2$。

### 引理 3：环面单位的图项模常数为 $a_j$

当 $p\equiv1\pmod4$ 时，在 $\mathbb Q^{\mathcal S_p}/\mathbb Q\mathbf1$ 中有
$$[(\Xi_j(e_{\rm tor}))_j]=[(a_j)_j].
\tag{5.3}$$

**证明。** R57 §4 的两 Igusa 图中，每条半边长为
$$L_j=\frac{4a_j}{p^2-1}.$$
环面单位在 $H_1(\Gamma)$ 上为恒等，在中间分次上为零。置
$$q_j=\frac{1/L_j}{\sum_i1/L_i}.$$
R57 引理 2 的实际正交投影计算给
$$Q_j(e_{\rm tor})=\frac{L_j}{2}(1-q_j).$$
所以
$$\Xi_j(e_{\rm tor})=a_j(1-q_j)
=a_j-\frac1{\sum_i1/a_i}.$$
最后一项与 $j$ 无关，得到 (5.3)。这只用了实际图上恒等作用，不把任何抽象 Hecke 模同构当成具体路径基的识别。证毕。

由 R59 和定理 1，对
$$G=c_{\rm ps}e_{\rm ps}+c_{\rm tor}e_{\rm tor}
+\sum_dc_de_d\in W^{\rm type}$$
有完整公式
$$\boxed{\quad
[(\Xi_j(G))_j]
=\left[\left(a_jc_{\rm tor}
+a_j\sum_{d\in\mathcal D_p}c_d\varphi(d)\varepsilon_j(d)\right)_j\right].
\quad}\tag{5.4}$$
$p\equiv3\pmod4$ 时令 $c_{\rm tor}=0$。总迹条件准确为
$$a_{\rm ps}c_{\rm ps}+tc_{\rm tor}+\sum_da_dc_d=0.
\tag{5.5}$$

### 定理 2：完整几何及真正可达分量上的精确秩

实际坏高度差值映射限制到 $W^{\rm type}$ 后，其秩为
$$\boxed{\quad
r_{\rm type}=
\begin{cases}
0,&p\equiv1\pmod{12},\\
1,&p\equiv5,7\pmod{12},\\
2,&p\equiv11\pmod{12}.
\end{cases}\quad}\tag{5.6}$$
这个秩对全部几何标号成立；只保留 R55 中真正 $\mathbb Q_p$ 可达的标号 $\mathcal S_p\cap\mathbb F_p$ 后仍完全相同。

**证明。** 由 (4.2)，给定任意 $c_{\rm tor},c_d$，都能唯一选择 $c_{\rm ps}$ 满足 (5.5)，且不改变 (5.4)。因此秩恰为 (5.4) 中各列模常数的秩。

若 $p\equiv1\pmod{12}$，所有标号一般，$a_j=1$、$\varepsilon_j(d)=1$。全部列为常数，秩为零。

若 $p\equiv5\pmod{12}$，只有一般类及 $j=0$ 两种。所有列在各类上常数，所以秩至多一。$t>0$，而 $e_{\rm tor}$ 给两类的值 $(1,3)$ 模常数，故秩恰为一。

若 $p\equiv7\pmod{12}$，只有一般类及 $j=1728$ 两种。任一 $e_d$ 给值 $(\varphi(d),0)$，所以秩为一。

若 $p\equiv11\pmod{12}$，三类为一般、$0$、$1728$，所以秩至多二。阶 $d=M$ 属于 $\mathcal D_p$ 且不整除 $M/3$，给列
$$\varphi(M)(1,0,0).$$
阶 $d'=M/3$ 同样属于 $\mathcal D_p$，且 $d'>2$，给列
$$\varphi(M/3)(1,3,0).$$
这两列模常数独立：若其线性组合为常数，第三坐标使常数为零，第二坐标再使第二系数为零，第一坐标使第一系数为零。因此秩恰为二。

为证明限制到真正可达标号不降秩，只须确认上述每种类中都有一个 $\mathbb F_p$ 标号。特殊 $0,1728$ 本来属于 $\mathbb F_p$。一般类可用下一节的 CM 模型直接给出：剩余类 $5,11$ 用 $j=54000$，剩余类 $7$ 用 $j=287496$。它们在相应 $p$ 下好超奇异约化，且模 $p$ 不等于 $0$ 或 $1728$。R55 证明这些 $\mathbb F_p$ 超奇异标号恰为可达标号，故同一非零列及独立性仍成立。剩余类 $1$ 的秩本来为零。证毕。

式 (5.6) 计算的是 (5.1) 这个具体子空间，不是整个 $\Phi_A$ 或整个 $\Phi_J$ 的秩。一般 Hecke 元在同一类型块内部仍可给不同分量的不同部分迹。

## 6. 类型靶值由明确的有理 CM 点全部实现

对 $p\not\equiv1\pmod{12}$，定义一组 $X(\mathbb Q)$ 中的 CM 点 $\mathcal C_p$，用其 $j$ 值列为

| $p\bmod12$ | $\mathcal C_p$ 的 $j$ 值 | 覆盖的坏标号类别 |
|---|---|---|
| $5$ | $0,54000$ | $0$、一般 |
| $7$ | $1728,287496$ | $1728$、一般 |
| $11$ | $0,1728,54000$ | $0$、$1728$、一般 |

### 引理 4：表中每点存在，而且其坏类别准确如表

**证明。** 使用 R9 中的四条明确模型：

| $j$ | 方程 | CM 判别式 | 方程判别式 |
|---|---|---:|---:|
| $0$ | $y^2=x^3+1$ | $-3$ | $-2^4 3^3$ |
| $1728$ | $y^2=x^3-x$ | $-4$ | $2^6$ |
| $54000$ | $y^2=x^3-15x+22$ | $-12$ | $2^8 3^3$ |
| $287496$ | $y^2=x^3-11x+14$ | $-16$ | $2^9$ |

这些特定模型在所有 $p>37$ 都有好约化；无需把 R9 为十三个模型一起选的 $p>163$ 下界搬过来。前、第三条的 CM 域为 $\mathbb Q(\sqrt{-3})$，在 $p\equiv2\pmod3$ 时惰性；另两条的 CM 域为 $\mathbb Q(i)$，在 $p\equiv3\pmod4$ 时惰性。因此每一行用于表中相应剩余类时，CM 环模 $p$ 是 $\mathbb F_{p^2}$。

Galois 正规化完整 CM 环，所以其在 $E[p]$ 中的像给一个 Galois 不变的非分裂 Cartan 结构，从而给 $X(\mathbb Q)$ 的点。这里不需要完整模 $p$ 像等于正规化子，只需这个实际 Cartan 结构；特殊自同构在粗模空间取轨道后仍给同一个有理点。R9 §§2–3 的证明在上述四个模型及 $p>37$ 下逐字适用：$p$ 不整除相应 CM 判别式，且 $(p+1)/3>2$，所以这个有理 CM 结构也是唯一的。

好约化且 CM 域在 $p$ 惰性使约化超奇异。可直接使用 R9 §2 的证明：惯性中央化 $\mathbb F_{p^2}$，与普通惯性中的非标量分裂元素矛盾。于是 R55 的实际末端标号就是该模型的 $j\bmod p$。

最后，恒等式
$$\begin{aligned}
54000&=2^4 3^3 5^3,&54000-1728&=2^4 3^3 11^2,\\
287496&=2^3 3^3 11^3,&287496-1728&=2^3 3^6 7^2
\end{aligned}$$
说明在 $p>37$ 时后两者的约化均不是特殊标号。因此它们确实代表一般类别。证毕。

### 定理 3：CM 点给出全部类型坏靶集

令 $V\subseteq W^{\rm type}$ 为任意有理子空间，固定统一参考标号 $j_*$，置
$$b_j(F)=k_j(F)-k_{j_*}(F)\quad(F\in V).$$
当 $p\not\equiv1\pmod{12}$ 时，在 $V^\vee$ 中有精确集合等式
$$\boxed{\quad
\{b_j|_V:j\in\mathcal S_p\cap\mathbb F_p\}
=\{b_{\operatorname{sp}_p(c)}|_V:c\in\mathcal C_p\}.
\quad}\tag{6.1}$$
若 $V=W^{\rm type}$，这组靶的不同值个数依次恰为 $2,2,3$。限制到更小的 $V$ 时，某些值可以重合。

**证明。** 由 (5.2)、(5.4)，$b_j|_V$ 只取决于 $j$ 属于一般、$0$ 或 $1728$ 哪一类。引理 4 给每一类一个实际有理 CM 点，因此两边集合相等。定理 2 证明完整类型空间区分各类：二类时有非恒定列；三类时用其证明中的两个独立列同时区分三点。这给最后的个数。证毕。

因此本结果不仅给一个靶空间维数界，还把该子空间的所有允许局部靶值由确定的全球有理点实现。

## 7. 接到真实辅助 QC 函数：准确的 CM 基准等式

令 $A$ 为 R45 的实际 Heegner 商，并把 $T_A=e_A\mathbb T_{\mathbb Q}$ 视作在互补因子上为零的子代数。正确的类型方向空间是
$$V_A^{\rm type}=W_A\cap Z^{\rm type},
\qquad W_A=\ker(\operatorname{Tr}_A:T_A\to\mathbb Q).
\tag{7.1}$$
这里使用交集，不擅自改成 $e_AZ^{\rm type}\cap W_A$。若某一惯性阶块只有部分全局因子属于 $A$，$e_Ae_d$ 就不再是全部该阶惯性子空间上的恒等；其 Drinfeld 部分迹不由 (3.2) 给出。只有整个类型块包含于 $A$ 时，其完整 $e_d$ 才属于 (7.1)。

对 $F\in V_A^{\rm type}$，令 $\mathcal Q_F$ 为 R54 (2.3) 的**真实完整**辅助函数；它使用固定的全局截面归一化、实际秩一 Mordell–Weil 高度项、规范平移及完整辅助局部高度。对方向只作一次 $G=2F$。

### 定理 4：有理点必须落在 CM 点的共同函数值纤维中

设 $p\equiv5,7,11\pmod{12}$，$\ell\ne p$。则
$$\boxed{\quad
X(\mathbb Q)\subseteq
\bigcup_{c\in\mathcal C_p}
\left\{x\in X(\mathbb Q_\ell):
\mathcal Q_F(x)=\mathcal Q_F(c)
\text{ 对全部 }F\in V_A^{\rm type}\right\}.
\quad}\tag{7.2}$$
右侧的有限函数值靶集恰等于实际可达坏靶集在 $(V_A^{\rm type})^\vee$ 上的限制乘以 $-\log_\ell(p)$。

**证明。** 若 $x\in X(\mathbb Q)$，R54 给
$$\mathcal Q_F(x)=-\log_\ell(p)b_j(F),\qquad
j=\operatorname{sp}_p(x),$$
同一个 $j$ 对所有方向同时适用。由 (6.1)，存在同一个 $c\in\mathcal C_p$，使 $b_j(F)=b_{\operatorname{sp}_p(c)}(F)$ 对全部 $F\in V_A^{\rm type}$ 成立。再对这个真实有理 CM 点使用 R54 的同一全局高度恒等式，得到
$$\mathcal Q_F(c)=-\log_\ell(p)b_{\operatorname{sp}_p(c)}(F),$$
故得 (7.2)。反过来，每个 $c$ 确实给一个可达坏分量，因此其函数值确实在原靶集中。这证明所述的集合相等。证毕。

式 (7.2) 可避免另算这些类型方向的坏靶常数：对确定的 CM 点取真实函数值，就得到全部联合靶值。它不允许把每个方向的值独立选择，也不把全局项或平移项删去。

若某水平已无条件证明 $A=J$，则 $V_A^{\rm type}=W^{\rm type}$，可直接使用全部公式。例如 R57 已核对 Dogra–Le Fourn §5.3 的已发表输入给 $p=41$ 时 $A=J$；此时有 $e_{\rm ps},e_{\rm tor},e_6,e_{14},e_{42}$ 五个块，故 $W^{\rm type}$ 四维，坏映射秩一，全部类型靶由 $j=0,54000$ 的两点实现。本文不把有限层的 $A=J$ 扩张为一般层断言。

## 8. 对共同根问题已推进的部分与精确边界

已得到的算术信息是：在所述真实类型方向中，所有有限靶都已由明确 CM 点识别，不再只是未知有理向量。对每个 $c\in\mathcal C_p$，可直接研究完整函数组
$$\mathcal R_{F,c}(x)=\mathcal Q_F(x)-\mathcal Q_F(c).
\tag{8.1}$$
它们确实在 $c$ 消失，并保持 R49 的独立性。R48 的饱和与圆盘证书适用于这些真实函数组。

但式 (7.2) 还不是 CM 根唯一性。惯性类型是坏 $p$ 处的分类；它本身没有给出辅助 $\ell$ 处 (8.1) 的导数、零点位置或高阶系数。R49 还说明：对任意独立非零方向，完整 QC 函数与全纯积分在每盘代数独立；因此不能从这些类型标签再假定一个额外的恒零解析关系，把剩下的共同根自动消去。

一般 $A$ 中是否包含足够的完整类型块也仍是实际输入问题。要用所有 $A$ 方向继续推进，需要计算 $e_A$ 在每个惯性阶内的真实分量投影，而非只使用本结果的整块维数。本文不证明 (7.2) 右侧只有 CM 点，不证明无 CM 圆盘无根，也不证明 Serre 一致性。

## 9. 原始来源与依赖

- B. Edixhoven and P. Parent, **Semistable reduction of modular curves associated with maximal subgroups in prime level**, *Documenta Mathematica* **26** (2021), 231–269，DOI [10.4171/DM/814](https://doi.org/10.4171/DM/814)，[作者全文](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)。§2.2.4，pp.243–244，给有限惯性；(23)，p.248，给正规化子商坐标；Theorem 3.5 及证明，pp.249–251，给曲线方程、特殊自同构、图与环面秩；Remark 3.8，pp.251–252，直接核对剩余类 $5$ 的维数。
- J. Rouse, A. V. Sutherland and D. Zureick-Brown, **$\ell$-adic images of Galois for elliptic curves over $\mathbb Q$ (and an appendix with John Voight)**, *Forum of Mathematics, Sigma* **10** (2022), e62，DOI [10.1017/fms.2022.38](https://doi.org/10.1017/fms.2022.38)。Lemma 12.8，p.37，列出 (4.1) 的非分裂正规化子亏格公式；§12.1 的 CM 正规化子解释与引理 4 使用的定义性构造相符。
- 本仓库 [R9](R9-cm-reduction-separation.md) 给四个 CM 模型、唯一 Cartan 结构和超奇异约化证明；[R55](R55-rational-bad-components-and-larger-qc-kernel.md) 给真正可达标号；[R57](R57-new-hecke-spectrum-does-not-kill-bad-height.md) 给实际图项及尺度比较；[R59](R59-local-types-toric-twist-and-height-kernel.md) 给全局类型分解及差值公式；[R54](R54-hecke-spectral-defect-and-finite-target.md) 给共同归一化下的完整有限靶方程；[R48](R48-analytic-saturation-and-root-certificates.md)、[R49](R49-independent-qc-functions-and-saturated-degree.md) 给真实函数的饱和与独立性。
