# R153：快逼近分式场在全部不变子商上的真实闭实现

日期：2026-11-12（UTC）。独占作者：critical_kernel。主会话预留 R153。
状态：以下全部子商单射性、最大闭分式、原分母图核心、闭包运算及循环空间精确保持均已完整证明，并通过主会话与 l2_moments 独立审读。
本稿不把原空间共轭直接下放到未知子商。

## 1. 基础类与子商记号

使用 R151 的交换子代数 $\mathcal G\subseteq\mathcal A$。
其元素具有真解析范数逼近，且误差的实际四次型趋无穷。
R151 已证明：

1. $\mathcal G$ 是含真解析演算、对 gauge 稳定的交换整环；
2. 每个非零 $E\in\mathcal G$ 在原空间及所有闭不变限制上单射稠密；
3. 在每个有限放大 $A^{(d)}$ 的每个闭不变空间 $\mathcal M$ 上，

$$
\overline{E^{(d)}\mathcal M}=\mathcal M;
\tag{1.1}
$$

4. 因此

$$
I\in\overline{E\,\mathbb C[A]}^{\mathrm{SOT}};
\tag{1.2}
$$

5. 在任意非零不变 Hilbert 子商上，非零 $E$ 的诱导算子不为零，并保留精确四次型 $100\,\operatorname{ord}(E)^4/15$。

设 $N\subseteq M\subseteq H$ 为闭 $A$ 不变空间，记 Hilbert 子商为

$$
Q=M/N,
$$

并用 $M\ominus N$ 表示其范数。$A_Q,E_Q$ 表示诱导算子。
R88 保证所有 $\mathcal A$ 元素保持 $M,N$；诱导映射为收缩代数同态。

## 2. 非零快分母在全部子商上单射

R151 的“$E_Q\ne0$”可加强成真正单射。

**定理2.1。** 对每个非零 $E\in\mathcal G$ 和每个不变子商 $Q$，

$$
\boxed{\ker E_Q=0,\qquad
\overline{\operatorname{Ran}E_Q}=Q.}
\tag{2.1}
$$

**单射证明。** 若 $x\in M$ 且 $Ex\in N$，由 (1.2)，存在 $E p_\alpha(A)$ 在有限测试向量意义下强趋恒等。于是

$$
p_\alpha(A)Ex\in N,\qquad
p_\alpha(A)Ex\longrightarrow x.
$$

$N$ 闭，故 $x\in N$。
这里也可只为这个固定 $x$ 选择逐次误差趋零的多项式；不需要有界强逼近序列。

**稠密像证明。** $\overline{EM}=M$，投影到 $M/N$ 后得到结论。证毕。

因此 $E$ 对每个闭 $A$ 不变 $N$ 都有饱和性

$$
\boxed{Ex\in N\quad\Longrightarrow\quad x\in N.}
\tag{2.2}
$$

### 2.1 子商中的有限放大性质来自真实 lift

设 $\mathcal L\subseteq Q^{\oplus d}$ 为闭 $A_Q^{(d)}$ 不变空间。
取商映射 $\pi:M^{\oplus d}\to Q^{\oplus d}$，令

$$
\widetilde{\mathcal L}=\pi^{-1}(\mathcal L).
$$

它是 $H^{\oplus d}$ 中闭、$A^{(d)}$ 不变的子空间，且含 $N^{\oplus d}$。
由 (1.1)，

$$
\overline{E^{(d)}\widetilde{\mathcal L}}
=\widetilde{\mathcal L}.
$$

投影后得到

$$
\boxed{\overline{E_Q^{(d)}\mathcal L}=\mathcal L.}
\tag{2.3}
$$

若再取 $\mathcal L$ 的不变子商，它同样可提升成原放大空间的两个嵌套不变子空间；(2.1) 的单射证明也适用。

这一步没有假设任意正交压缩保乘法，也没有在子商中引入一个未经证明存在的共轭。

## 3. 每个抽象分式的最大闭实现

令

$$
\mathbb K=\operatorname{Frac}(\mathcal G).
$$

$\mathcal G$ 是整环，因为它包含于 R32 的无零因子代数 $\mathcal A$。

对 $a,e\in\mathcal G$，$e\ne0$，在每个 $Q$ 上定义

$$
\boxed{
T_{a/e,Q}=e_Q^{-1}a_Q,\qquad
\operatorname{Dom}T_{a/e,Q}
=\{x\in Q:a_Qx\in\operatorname{Ran}e_Q\}.
}
\tag{3.1}
$$

由于 $e_Q$ 单射，值唯一。
它闭：若 $x_n\to x,T x_n\to y$，则 $e_Qy=a_Qx$，故 $x$ 在最大域中且 $Tx=y$。
交换性给

$$
\operatorname{Ran}e_Q\subseteq\operatorname{Dom}T_{a/e,Q},\qquad
T_{a/e,Q}e_Q=a_Q.
\tag{3.2}
$$

因此定义域稠密。

若 $a\ne0$，由 (2.1)，$a_Q$ 也单射稠密。所以

$$
\boxed{T_{a/e,Q}\text{ 单射且值域稠密}.}
\tag{3.3}
$$

像稠密可直接由 (3.2) 的 $\operatorname{Ran}a_Q\subseteq\operatorname{Ran}T$ 得到。
$a=0$ 时 (3.1) 的域是整个 $Q$，它是真正的全域零算子。

### 3.1 同一个分式给同一个最大闭算子

若 $a/e=b/f$，即 $af=be$，则 (3.1) 的两个域和作用完全相同。
例如 $a_Qx=e_Qy$ 时，

$$
e_Q(b_Qx-f_Qy)
=b_Qe_Qx-f_Qe_Qy
=f_Qa_Qx-f_Qe_Qy=0.
$$

由 $e_Q$ 单射得 $b_Qx=f_Qy$。反向用 $f_Q$ 单射即可。
因此实现只依赖抽象分式，不依赖表示。

非零分式的实现不会变成零算子，因为其分子在非零 $Q$ 上单射。
从而在每个非零 $Q$ 上得到忠实的分式表示。

## 4. 原分母的图核心与域交换

### 4.1 原分母图核心

令 $T=T_{a/e,Q}$。
其图 $\mathcal G_T\subseteq Q\oplus Q$ 闭且为 $A_Q\oplus A_Q$ 不变，因为 $a_Q,e_Q$ 与 $A_Q$ 交换。
对这张图应用 (2.3)，得到

$$
\overline{e_Q^{(2)}\mathcal G_T}=\mathcal G_T.
$$

且

$$
e_Q^{(2)}(x,Tx)=(e_Qx,e_QTx)=(e_Qx,a_Qx).
$$

于是

$$
e_Q^{(2)}\mathcal G_T
\subseteq\{(e_Qy,a_Qy):y\in Q\}
\subseteq\mathcal G_T.
$$

故

$$
\boxed{\operatorname{Ran}e_Q\text{ 是 }T_{a/e,Q}\text{ 的图核心}.}
\tag{4.1}
$$

这用的是原分母，而不需要先约分或更换一个较方便的分母。

### 4.2 全有界交换子域交换

若 $R\in\{A_Q\}'$，则 $R$ 与 $a_Q,e_Q$ 交换，因为它们属于 $A_Q$ 的范数代数。
若 $a_Qx=e_QTx$，便有

$$
a_QRx=e_QRTx.
$$

由最大域定义，

$$
\boxed{
R\operatorname{Dom}T\subseteq\operatorname{Dom}T,\qquad
TRx=RTx.
}
\tag{4.2}
$$

此处甚至允许子商上新出现的有界交换子，并不要求它们来自原空间的某个交换子。

## 5. 闭包意义的分式场运算

令 $T=T_{a/e,Q}$、$U=T_{b/f,Q}$。

### 5.1 加法

在自然共同域 $\operatorname{Dom}T\cap\operatorname{Dom}U$ 上，

$$
e_Qf_Q(T+U)x=(a_Qf_Q+b_Qe_Q)x.
$$

所以自然和包含于最大闭商

$$
V=T_{(af+be)/(ef),Q}.
$$

反之 $\operatorname{Ran}(e_Qf_Q)$ 包含在自然共同域，且自然和在该域上的图恰为 $((ef)_Qy,(af+be)_Qy)$。
$ef\in\mathcal G\setminus\{0\}$，(4.1) 说明这个域是 $V$ 的图核心。因此

$$
\boxed{\overline{T+U}=T_{(af+be)/(ef),Q}.}
\tag{5.1}
$$

若分子为零，右边为全域零算子；没有把自然共同域上的零作用提前当成全域零算子。

### 5.2 乘法

自然复合 $TU$ 的域包含 $\operatorname{Ran}(e_Qf_Q)$：在该域上

$$
U(e_Qf_Qy)=e_Qb_Qy,\qquad
TU(e_Qf_Qy)=a_Qb_Qy.
$$

对其任意自然域向量，也有 $(ef)_Q TUx=(ab)_Qx$，故自然复合包含于相应最大闭商。
再用原分母图核心，

$$
\boxed{\overline{TU}=T_{ab/(ef),Q}=\overline{UT}.}
\tag{5.2}
$$

### 5.3 逆与常数

若 $a\ne0$，(3.1) 直接给包含真实域的逆等式

$$
\boxed{T_{a/e,Q}^{-1}=T_{e/a,Q}.}
\tag{5.3}
$$

标量分式 $\lambda$ 实现成全域 $\lambda I_Q$。
以上闭包运算因抽象分式场中的运算而满足结合律与分配律；
本稿不声称任意自然无界乘积在取闭包之前就处处有定义或已经闭。

## 6. 对限制及再次取商的兼容性

令 $L\subseteq Q$ 为闭 $A_Q$ 不变空间。

若 $x\in L\cap\operatorname{Dom}T$，则 $a_Qx=e_QTx\in L$。
$e$ 在 $Q/L$ 上单射，故 (2.2) 的子商版本给 $Tx\in L$。因此

$$
T(L\cap\operatorname{Dom}T)\subseteq L.
\tag{6.1}
$$

其域包含 $e_QL$，所以在 $L$ 中稠密。
最大定义域直接给

$$
\boxed{
T_{a/e,Q}|_{L\cap\operatorname{Dom}T}
=T_{a/e,L}.
}
\tag{6.2}
$$

并且 $e_QL$ 是该限制的图核心。这里是真正的限制等式。

### 6.1 再次取商时只主张图闭包等式

对 $L_0\subseteq L_1\subseteq Q$ 的两个闭不变空间，先把 $T$ 限制到 $L_1$，再对 $L_0$ 作自然诱导图。
因 (6.1)，该图是单值且定义良好的；它包含于最大分式 $T_{a/e,L_1/L_0}$。

原诱导图还包含

$$
\bigl(e_{L_1/L_0}x,\ a_{L_1/L_0}x\bigr)
\quad(x\in L_1/L_0),
$$

由原分母图核心，遂有

$$
\boxed{
\overline{\text{自然诱导图}}
=\mathcal G_{T_{a/e,L_1/L_0}}.
}
\tag{6.3}
$$

没有声称自然商域必等于最大商域；
从最大域中的模 $L_0$ 等式求精确提升可能需要额外的范围结论。

## 7. 每个定义域向量的循环空间精确保留

设 $a\ne0$，$u\in\operatorname{Dom}T_{a/e,Q}$，记 $v=Tu$，并令

$$
L=\overline{\mathbb C[A_Q]u}.
$$

(6.1) 先给 $v\in L$，所以 $\overline{\mathbb C[A_Q]v}\subseteq L$。
另一方面，

$$
a_Qu=e_Qv.
$$

$a$ 在 $L$ 上有稠密像，因此

$$
\overline{\mathbb C[A_Q](a_Qu)}
=\overline{a_QL}=L.
$$

$e_Q$ 是 $A_Q$ 的范数多项式极限，所以 $e_Qv$ 属于 $v$ 的闭循环空间。
由此得到反向包含，故

$$
\boxed{
\overline{\mathbb C[A_Q]\,T_{a/e,Q}u}
=
\overline{\mathbb C[A_Q]u}
\quad(u\in\operatorname{Dom}T_{a/e,Q},\ a\ne0).
}
\tag{7.1}
$$

这对每个子商成立，也不要求 $u$ 原先对整个 $Q$ 循环。

还可得到图范数加强。
取 $e_Q$ 的范数多项式逼近，便知 $(e_Qu,a_Qu)=(e_Qu,e_Qv)$ 属于
$\{(p(A_Q)u,p(A_Q)v)\}$ 的图闭包。
再利用 $u$ 对 $L$ 的循环性及 $a_Q,e_Q$ 的有界性，该闭包包含所有 $(e_Qx,a_Qx)$、$x\in L$。
由 $e_QL$ 是图核心，得到

$$
\boxed{
\{p(A_Q)u:p\in\mathbb C[z]\}
\text{ 是 }T_{a/e,L}\text{ 的图核心}.
}
\tag{7.2}
$$

特别地，定义域内的循环向量被非零分式送成循环向量，而且这是循环空间相等，不只是一个方向的传递。

## 8. 共轭、谱参数和有界性的准确界线

### 8.1 只在原空间使用 $C$ 自伴

在 $Q=H$ 上，$a,e$ 对同一个 $C$ 对称。
令 $T_0$ 为原分母域上的限制 $T_0(ex)=ax$。
伴随定义给

$$
T_0^*=(e^*)^{-1}a^*=CT_{a/e,H}C.
$$

由 (4.1) 的图核心，

$$
\boxed{T_{a/e,H}^*=CT_{a/e,H}C.}
\tag{8.1}
$$

一般 $Q=M/N$ 不被原 $C$ 保持；本稿没有在 $Q$ 上宣称 (8.1)。

### 8.2 非常数分式没有点谱或不稠密值域参数

对任意 $\lambda$，最大域直接给

$$
T_{a/e,Q}-\lambda I
=T_{(a-\lambda e)/e,Q},
\tag{8.2}
$$

包括定义域相等。
如果抽象分式 $a/e$ 非常数，则 $a-\lambda e\ne0$ 对所有 $\lambda$ 成立。
所以在每个非零 $Q$ 上，

$$
\boxed{
\ker(T_{a/e,Q}-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(T_{a/e,Q}-\lambda I)}=Q
\quad(\lambda\in\mathbb C).
}
\tag{8.3}
$$

这没有判定哪些参数属于预解集。空谱与连续谱的区别仍取决于逆分式是否有界。

### 8.3 有界性就是实际算子因式

最大闭商在某个非零 $Q$ 上有界，当且仅当存在 $R\in B(Q)$ 满足

$$
\boxed{a_Q=e_QR.}
\tag{8.4}
$$

此时最大域为整个 $Q$，$T=R$；
由 $e_Q$ 单射及与 $A_Q$ 的交换关系，$R$ 自动属于 $\{A_Q\}'$。
若只是先知道闭商在其稠密域上有一个范数界，闭性也会迫使其域为整个 $Q$，因此与上面等价。

不能把 (8.4) 替换成仅形式除法。

### 8.4 负形式阶在任何非零子商上都无界

设非零分子、分母的首阶为

$$
p=\operatorname{ord}a,\qquad e_0=\operatorname{ord}e.
$$

如果 $T_{a/e,Q}$ 在某个非零 $Q$ 上有界，则 $a_Q=e_QT$，所有因子交换，故

$$
\|a_Q^n\|\le\|e_Q^n\|\,\|T\|^n.
$$

R151 的精确子商型给

$$
\frac{100}{15}p^4
=\tau_4(a_Q)
\ge\tau_4(e_Q)
=\frac{100}{15}e_0^4.
$$

于是

$$
\boxed{
p<e_0\quad\Longrightarrow\quad
T_{a/e,Q}\text{ 在每个非零子商上无界}.
}
\tag{8.5}
$$

没有从 $p\ge e_0$ 反推有界性，也没有从负形式阶推出空谱。
(8.5) 是必要条件，预解集仍由实际有界因式 (8.4) 决定。

## 9. 当前用途与未覆盖范围

本稿给出 $\operatorname{Frac}\mathcal G$ 在全部不变子商上的真实闭实现：
非零分式单射稠密、原分母图核心、有限放大兼容、自然运算的闭包以及每个域向量的循环空间相等。

它与 R152 的一慢方向解析芽及全空间解析闭商互补。
这里不把一般 $\mathcal G[S]$ 分母自动当成在所有未知限制上稠密；
R152 的超越分支若只得到全空间 quasiaffinity，不能未经另外证明传到本稿的全部子商结论。

对于普通慢第一行或一般二阶分子，是否属于这些受控分式域仍须实际证明。
完整不变子空间问题保持开放。
