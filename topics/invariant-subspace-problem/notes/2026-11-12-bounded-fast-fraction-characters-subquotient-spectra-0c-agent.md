# R168：有界快分式在不变子商上的形式字符与真实谱约束

日期：2026-11-12（UTC）。作者：critical_kernel。根代理预留 R168。

状态：完整证明。本稿仅处理已经由 R153 实现的快分式场，以及其中在指定非零子商上实际有界的元素。没有把形式非负阶当作有界性的充分条件，也没有把所得到的一个字符称为唯一字符。

## 1. 记号、范围与已证输入

令 $\mathcal G\subseteq\mathcal A$ 为 R151 的快解析逼近代数，令

$$
\mathbb K=\operatorname{Frac}(\mathcal G).
$$

固定非零 Hilbert 不变子商 $Q=M/N$。以下也适用于 R153 的有限放大及再次取子商版本：所需的稠密性和图核心均经真实不变图的 lift 获得，不在子商上假设一个共轭。

对 $P,E\in\mathcal G$、$E\ne0$，使用 R153 的最大闭实现

$$
T_{P/E,Q}=E_Q^{-1}P_Q,\qquad
\operatorname{Dom}T_{P/E,Q}
=\{x\in Q:P_Qx\in\operatorname{Ran}E_Q\}.
\tag{1.1}
$$

本稿使用 [R153](../results/R153-fast-fraction-field-on-all-invariant-subquotients.md) 已完整证明的以下事实：

1. 每个非零 $E_Q$ 单射且值域稠密；实现 (1.1) 闭、稠密定义，且只依赖抽象分式。
2. 非零分式在每个非零 $Q$ 上单射、值域稠密，实现忠实。
3. 原分母 $\operatorname{Ran}E_Q$ 是 (1.1) 的图核心，且

$$
T_{P/E,Q}E_Q=P_Q.
\tag{1.2}
$$

4. 自然和、自然复合的闭包是相应分式的最大闭实现；非零分式的真实逆为反分式：

$$
\overline{T_r+T_s}=T_{r+s},\qquad
\overline{T_rT_s}=T_{rs},\qquad
T_r^{-1}=T_{1/r}.
\tag{1.3}
$$

最后一个等式包含准确的定义域，逆的域是原算子的值域。

5. 若 $r=P/E\ne0$，则

$$
\operatorname{ord}r
=\operatorname{ord}P-\operatorname{ord}E<0
\quad\Longrightarrow\quad
T_{r,Q}\text{ 在每个非零 }Q\text{ 上无界}.
\tag{1.4}
$$

其依据是实际因式 $P_Q=E_QT_{r,Q}$ 和 R151 的精确子商四次型，不是形式除法。

$\iota:\mathbb K\to\mathbb C((z))$ 表示原形式嵌入的分式延拓。它单射。对非零分式使用通常整数阶 $\operatorname{ord}$，对零分式约定阶为 $+\infty$。

## 2. 有界实现组成真正的交换代数

定义

$$
\mathfrak B_Q
=\{T_{r,Q}:r\in\mathbb K,\ T_{r,Q}\in B(Q)\}.
\tag{2.1}
$$

此处“有界”指最大闭算子实际为全域有界算子；若只先得到它在原稠密域上的一个范数界，闭性已会迫使定义域等于 $Q$。

**命题2.1。** $\mathfrak B_Q$ 是 $B(Q)$ 中含单位的交换代数。它在 $B(Q)$ 中对可逆元取逆封闭，且

$$
T_{r,Q}=T_{s,Q}\quad\Longleftrightarrow\quad r=s.
\tag{2.2}
$$

**证明。** 若 $T_r,T_s$ 全域有界，它们的和、积也全域有界且闭。因此 (1.3) 中的闭包不再增加定义域，给

$$
T_r+T_s=T_{r+s},\qquad T_rT_s=T_{rs}=T_sT_r.
$$

标量分式给 $\lambda I_Q$。忠实性给 (2.2)。

若 $T_r$ 是 $Q$ 上有界可逆算子，则 $r\ne0$。由 (1.3) 的准确逆等式，$T_{1/r}$ 就是这个有界全域逆，故仍属于 $\mathfrak B_Q$。证毕。

特别，不能把 $\mathfrak B_Q$ 误写成全部 $\mathbb K$；是否进入 (2.1)，仍须验证实际有界因式。

## 3. 逆分式与有界预解的定义域核对

后文的谱反证需要排除一个可能的定义域误用。这里把该步骤单独写清。

固定 $r=P/E$ 及 $\lambda\in\mathbb C$，设

$$
F=P-\lambda E\ne0.
$$

由最大域的定义，

$$
T_{r,Q}-\lambda I=T_{F/E,Q},
\tag{3.1}
$$

且两侧的定义域相同。其原分母核心上的图为

$$
\{(E_Qx,F_Qx):x\in Q\}.
\tag{3.2}
$$

反分式 $T_{E/F,Q}$ 的原分母图核心为

$$
\{(F_Qx,E_Qx):x\in Q\}.
\tag{3.3}
$$

(3.3) 正是 (3.2) 的翻转；取图闭包仍保持翻转。因此 R153 的原分母图核心给

$$
\boxed{(T_{r,Q}-\lambda I)^{-1}=T_{E/F,Q}}
\tag{3.4}
$$

作为真实闭算子等式，而不仅是符号恒等式。

如果 $\lambda$ 是 $T_{r,Q}$ 的预解参数，左侧是全域有界算子，故右侧也必须全域有界。也可以逐向量直接核对：令 $R_\lambda$ 为该有界逆。由

$$
F_QR_\lambda y=E_Qy\qquad(y\in Q)
$$

知每个 $y$ 都在最大反分式域中；$F_Q$ 单射保证其唯一值为 $R_\lambda y$。这里没有在未知定义域上消去一个无界逆。

## 4. 形式常数必属于实际谱

对 $T_{r,Q}\in\mathfrak B_Q$，由 (1.4) 有

$$
\operatorname{ord}r\ge0
\tag{4.1}
$$

（$r=0$ 时按约定理解）。所以 $\iota(r)$ 是真正的形式幂级数，而不是含负幂的 Laurent 级数。定义其形式常数为

$$
c(r)=[z^0]\iota(r).
\tag{4.2}
$$

正阶分式的形式常数为0。

**定理4.1。** 对每个非零子商 $Q$ 和每个在该子商上实际有界的快分式，

$$
\boxed{
\operatorname{ord}r\ge0,\qquad
c(r)\in\sigma_{B(Q)}(T_{r,Q}).
}
\tag{4.3}
$$

**证明。** 非负阶已由 (1.4) 得到。

若 $r=c(r)$ 是标量分式，则 $T_{r,Q}=c(r)I_Q$；因 $Q\ne0$，结论直接成立。

以下设 $r-c(r)\ne0$。形式常数相消给

$$
\operatorname{ord}(r-c(r))\ge1.
\tag{4.4}
$$

若 $c(r)\notin\sigma(T_{r,Q})$，则 $T_{r,Q}-c(r)I$ 有界可逆。§3 将其逆准确识别为

$$
T_{1/(r-c(r)),Q}.
$$

但

$$
\operatorname{ord}\frac1{r-c(r)}
=-\operatorname{ord}(r-c(r))<0,
$$

这与 (1.4) 的每个非零子商无界性矛盾。证毕。

写成分子、分母时，若 $c=c(r)$，上述非标量分支就是

$$
F=P-cE\ne0,\qquad
\operatorname{ord}F>\operatorname{ord}E,
$$

而假想有界逆为 $T_{E/F,Q}$。因此反证确实用了阶数严格较小的分子，没有把一次形式抵消当成有界除法。

### 4.1 一个直接的受限因式判据

若 $P_Q=E_QY$，其中 $Y\in B(Q)$，则最大商就是 $Y$。于是

$$
\boxed{[z^0]\iota(P/E)\in\sigma(Y).}
\tag{4.5}
$$

特别，若另有独立论证给 $\sigma(Y)=\{\lambda_0\}$，必须有

$$
[z^0]\iota(P/E)=\lambda_0.
\tag{4.6}
$$

这可用于检查某个未知核上声称成立的有界分式关系。但分子、分母必须已被证明属于 $\mathcal G$；一般慢第一行或慢 Bell 项不因此进入该类。

## 5. 一个收缩字符及其范数闭包

由 (2.2)，可以在实际算子代数 $\mathfrak B_Q$ 上无歧义地定义

$$
\varepsilon_Q(T_{r,Q})=c(r).
\tag{5.1}
$$

所有有关形式级数都没有负幂，所以常数项在和、积下满足

$$
c(r+s)=c(r)+c(s),\qquad c(rs)=c(r)c(s),\qquad c(1)=1.
\tag{5.2}
$$

由定理4.1及有界算子的谱半径界，

$$
\boxed{
|\varepsilon_Q(T)|\le r(T)\le\|T\|
\qquad(T\in\mathfrak B_Q).
}
\tag{5.3}
$$

因此 $\varepsilon_Q$ 是一个范数恰为1的连续字符：上界由 (5.3)，下界由 $\varepsilon_Q(I_Q)=1$ 和 $\|I_Q\|=1$。

令

$$
\overline{\mathfrak B_Q}^{\,\|\cdot\|}
\subseteq B(Q)
$$

为其算子范数闭包。它是含单位的交换 Banach 代数。$\varepsilon_Q$ 唯一连续延拓到这个闭包，并继续满足

$$
\varepsilon_Q(ST)=\varepsilon_Q(S)\varepsilon_Q(T),
\qquad
\|\varepsilon_Q\|=1.
\tag{5.4}
$$

唯一性这里只指给定字符的连续延拓唯一，不声称该 Banach 代数只有这一个字符。

### 5.1 闭包仍在 $B(Q)$ 中对逆封闭

若 $T\in\overline{\mathfrak B_Q}$ 在 $B(Q)$ 中可逆，取 $T_n\in\mathfrak B_Q$、$T_n\to T$。有界可逆集合开，故充分大 $n$ 时 $T_n$ 也可逆。命题2.1给

$$
T_n^{-1}\in\mathfrak B_Q.
$$

而逆映射在有界可逆集合上范数连续，所以

$$
T_n^{-1}\longrightarrow T^{-1}
$$

按范数成立。于是 $T^{-1}\in\overline{\mathfrak B_Q}$。

因此

$$
\boxed{
\sigma_{\overline{\mathfrak B_Q}}(T)
=\sigma_{B(Q)}(T)
\qquad(T\in\overline{\mathfrak B_Q}).
}
\tag{5.5}
$$

特别，延拓字符的值仍落在实际 Hilbert 空间谱中：

$$
\boxed{
\varepsilon_Q(T)\in\sigma_{B(Q)}(T)
\qquad(T\in\overline{\mathfrak B_Q}).
}
\tag{5.6}
$$

也可由 (4.3) 取范数极限直接验证 (5.6)：若极限点在预解集，充分接近的 $T_n-\varepsilon_Q(T_n)I$ 都会可逆，矛盾。

闭包元素一般没有在本稿中指定的抽象分式表示；(5.4) 给它的连续字符值，并不额外定义完整形式级数。

## 6. 非常数有界分式的谱全为连续谱

设 $r\in\mathbb K$ 非常数，且 $T=T_{r,Q}\in B(Q)$。对每个 $\lambda\in\mathbb C$，$r-\lambda\ne0$，R153 给

$$
\ker(T-\lambda I)=\{0\},\qquad
\overline{\operatorname{Ran}(T-\lambda I)}=Q.
\tag{6.1}
$$

若 $\lambda\in\sigma(T)$，其像不可能等于 $Q$，否则有界逆定理将使该参数处于预解集。因此

$$
\boxed{
\sigma(T)=\sigma_c(T),
}
\tag{6.2}
$$

其中连续谱指单射、稠密而非满射的谱点。该谱是非空紧集，并至少含 $c(r)$。本稿没有证明它是单点集。

作为直接推论，每个谱点都有单位弱零近似特征向量。确实，单射、稠密而非满射使 $T-\lambda I$ 不可能有一个正的下界；可取 $\|x_n\|=1$ 及 $(T-\lambda I)x_n\to0$。其任意弱聚点都在零核中，故为0；在 Hilbert 空间中可取这样的弱零序列。因此所有谱点也属于 Fredholm 本质谱。

这些单射、稠密值域及连续谱结论只对实际分式成立。本稿没有把它们无条件传给 $\overline{\mathfrak B_Q}$ 中任意范数极限；循环或单射类的稠密性不允许这种推断。

## 7. 对未必有界分式的一个补充

设 $r\in\mathbb K$ 非零、$\operatorname{ord}r\ge0$，此处不预设 $T_{r,Q}$ 有界。仍令 $c=[z^0]\iota(r)$。

若 $r=c$，它就是标量算子。若 $r\ne c$ 且 $c$ 是其预解参数，§3仍将有界预解算子识别为负形式阶分式 $T_{1/(r-c),Q}$，与 (1.4) 矛盾。因此

$$
\boxed{
\operatorname{ord}r\ge0
\quad\Longrightarrow\quad
[z^0]\iota(r)\in\sigma(T_{r,Q}),
}
\tag{7.1}
$$

即使这个最大闭实现实际无界也成立。

特别，在本快分式场内，

$$
\sigma(T_{r,Q})=\varnothing
\quad\Longrightarrow\quad
\operatorname{ord}r<0.
\tag{7.2}
$$

这只是必要条件。负形式阶本身不被用来断言空谱。

例如 $A_Q^{-1}$ 是负阶分式，其每个 $\lambda$ 的有界全域逆为

$$
(A_Q^{-1}-\lambda I)^{-1}
=A_Q(I-\lambda A_Q)^{-1}.
$$

右侧的像在 $\operatorname{Ran}A_Q$ 中，且 $A_Q$ 拟幂零，所以这个例子的空谱可直接核验。与之相比，R167 的零形式阶闭分式无界而具有全平面连续谱；其形式常数仍位于该谱，完全符合 (7.1)。

## 8. 当前适用边界

本稿新增的是：

- 指定非零子商上有界快分式的非负阶及形式常数谱约束；
- 实际有界分式代数上的范数1字符；
- 其范数闭包的同一字符及对真实有界逆封闭；
- 非常数有界分式的全部谱点都是连续谱；
- 任意非负阶最大闭快分式的形式常数不能是预解参数。

它不把普通慢共振关系中的任意分子、分母变成 $\mathcal G$ 元素，也不声称未知核上的每个有界乘子都属于这个分式域。

一般慢平方共振、一般二阶核及完整 Hilbert 不变子空间问题仍未解决。
