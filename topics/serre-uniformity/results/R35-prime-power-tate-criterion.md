# R35：素数幂层的精确 Tate 判据与固定 CM 分母界

日期：2026-11-12；会话：serre-uniformity-astra-cont。

**状态：已证明。** 将 R2 的完整局部等价判据推广到每个 $p^n$ 层，并将 R13 的固定 CM 分裂分母下界提高为 $4p^{2n}+1$。高次层的正规化子阶可被 $p$ 整除，不能重复一级证明中“群阶与 $p$ 互素”的论证；这里直接使用非分裂二次代数对自由直线的作用。

这是带有实际高次像或高次挠点同构假设的必要条件。它不把模 $p$ 异常自动提升为任意 $p^n$ 的异常，也不提供统一高度上界。

## 1. 有限局部环上的正规化子与自由直线

固定奇素数 $p$、整数 $n\ge1$，写
$$R_n=\mathbb Z/p^n\mathbb Z,\qquad S_n=R_n[\alpha],\qquad\alpha^2=\epsilon,$$
其中 $\epsilon$ 模 $p$ 为非平方。$S_n/R_n$ 是非分裂的二次 étale 代数；其剩余域为 $\mathbb F_{p^2}$。记 $\sigma(\alpha)=-\alpha$。在基 $(1,\alpha)$ 下定义
$$C_n=S_n^\times\subset\operatorname{GL}_2(R_n),\qquad
N_n=C_n\rtimes\langle\sigma\rangle.$$

这确为 $C_n$ 的完整正规化子：$C_n$ 的 $R_n$ 线性张成包含 $1,\alpha$，故为整个代数 $S_n$；正规化 $C_n$ 的矩阵也正规化该代数。$S_n$ 的 $R_n$ 代数自同构只有恒等与 $\sigma$，而其中心化子的可逆元恰为 $S_n^\times$。

**引理 35.1。**

1. 若 $c\in C_n$ 保持 $R_n^2$ 中的一条自由直和子模 $L$，其秩为一，则 $c$ 是标量。
2. $N_n\setminus C_n$ 的所有元素迹为零。

**证明。** 将 $R_n^2$ 识别为 $S_n$。$L$ 有一个本原生成元 $v$，即 $v$ 模 $p$ 非零。因 $S_n$ 为局部环，$v$ 是 $S_n$ 中的单位。若 $cv=av$、$a\in R_n$，乘以 $v^{-1}$ 得 $c=a$；由于 $c$ 可逆，$a\in R_n^\times$。这证明第 1 点，且没有把 $R_n$ 错当成域。

若 $c=a+b\alpha$，则 $c\sigma$ 的矩阵为
$$\begin{pmatrix}a&-b\epsilon\\ b&-a\end{pmatrix},$$
其迹为零，证明第 2 点。证毕。

## 2. 局部等价定理

设 $p\ge5$，$q$ 为任意有理素数，$E/\mathbb Q_q$ 满足 $v_q(j(E))<0$。设 $t\in\mathbb Q_q$ 为相同 $j$ 的 Tate 参数，故
$$v_q(t)=-v_q(j(E))>0.$$

**定理 35.2。** 下列条件等价：

1. $\rho_{E,p^n}(G_{\mathbb Q_q})$ 包含于 $\operatorname{GL}_2(R_n)$ 中某个非分裂 Cartan 正规化子；
2. $q\ne p$、$q\equiv\pm1\pmod{p^n}$，且
   $$\boxed{\quad t\in\mathbb Q_q^{\times p^n}.\quad}\tag{35.1}$$

此时，除去可能的二次扭曲后，Tate 曲线的整个模 $p^n$ 局部像至多有两个元素。若保留原曲线的二次扭曲，像至多有四个元素。

**证明。** Tate 均匀化给出 $E$ 是 $T_t$ 的至多二次扭曲。扭曲只乘 $\{\pm I\}\subset C_n$，不改变条件 1，故可先令 $E=T_t$。其挠点表示具有形状
$$\rho(g)=\begin{pmatrix}\chi_{p^n}(g)&c_t(g)\\0&1\end{pmatrix},\tag{35.2}$$
并有标准的 Galois 正合列
$$0\longrightarrow\mu_{p^n}\longrightarrow T_t[p^n]
\longrightarrow\mathbb Z/p^n\mathbb Z\longrightarrow0.\tag{35.3}$$
其中扩张类是 $t$ 在
$$H^1(\mathbb Q_q,\mu_{p^n})
\simeq\mathbb Q_q^\times/\mathbb Q_q^{\times p^n}$$
中的 Kummer 类。

假设条件 1，在相应的 $N_n$ 中考虑像群 $G$。它保持 (35.3) 的自由直和子模 $\mu_{p^n}$。若 $g\in G\cap C_n$，引理 35.1 使 $g$ 为标量；它在 (35.3) 的商上恒为 $1$，故该标量只能为 $1$。所以
$$G\cap C_n=\{I\}.$$
正规化子的商阶为二，因而 $|G|\le2$。对任何外陪集元素，迹为零；比较 (35.2) 得
$$\chi_{p^n}(g)+1=0.$$
因此整个圆分像包含于 $\{1,-1\}$。

若 $q=p$，局部圆分特征满射到 $R_n^\times$，其阶 $p^{n-1}(p-1)>2$，矛盾。故 $q\ne p$。此时 $p$ 幂根单位给非分歧扩张，Frobenius 的圆分值为 $q\bmod p^n$，所以 $q\equiv\pm1\pmod{p^n}$。

最后，由 $|G|\le2$ 且 $2$ 在 $R_n$ 中可逆，(35.3) 有一个 $G$-等变截面。具体地，将任意 $R_n$ 线性截面对 $G$ 平均即可；(35.2) 的整个作用经过这个有限群，所以得到 $G_{\mathbb Q_q}$-等变截面。因此其 Kummer 扩张类为零，即 (35.1)。这里用平均的是实际的至多二阶像群，而不是可能含 $p$ 阶元素的整个 $N_n$。

反之，若条件 2 成立，可以在 $\mathbb Q_q$ 内选择 $t^{1/p^n}$，故
$$T_t[p^n]\simeq\mu_{p^n}\oplus R_n.$$
圆分特征的像由 $q\bmod p^n$ 生成。若 $q\equiv1$，表示平凡；若 $q\equiv-1$，像由 $\operatorname{diag}(-1,1)$ 生成，它就是上述基下的 $-\sigma\in N_n$。再乘二次标量仍在 $N_n$ 中。定理得证。

## 3. 单位条件及商二次特征

记 $e=-v_q(j(E))=v_q(t)$。因 $q\ne p$，$p^n$ 次幂映射在 $1+q\mathbb Z_q$ 上为同构。于是定理 35.2 的条件又可写成：

- $q\equiv-1\pmod{p^n}$ 时，恰需 $p^n\mid e$；
- $q\equiv1\pmod{p^n}$ 时，恰需 $p^n\mid e$ 且 $q^{-e}t\bmod q\in(\mathbb F_q^\times)^{p^n}$。

其他 $q$ 均不可能。第一行因为 $p\nmid q-1$，剩余单位群的 $p^n$ 次幂映射也可逆；第二行不能省去剩余单位条件。

若全局表示包含于一个固定 $N_n$，记其商特征为
$$\varepsilon_n:G_{\mathbb Q}\longrightarrow N_n/C_n=\{\pm1\}.$$
每个负 $j$ 赋值素数满足
$$\varepsilon_n|_{I_q}=1,\qquad
\varepsilon_n(\operatorname{Frob}_q)=
\begin{cases}+1,&q\equiv1\pmod{p^n},\\-1,&q\equiv-1\pmod{p^n}.
\end{cases}\tag{35.4}$$
惯性在 Tate 表示上平凡，原曲线可能的二次扭曲仍只是 Cartan 内的标量。Frobenius 在第一种情形为标量；在第二种情形不可能在 Cartan 内，因为它保持自由直线且具有两个不同的特征值。由引理 35.1 得到 (35.4)。这个商与降模 $p$ 后的商相同，因为 $N_n/C_n\to N_1/C_1$ 为同构。

## 4. 任意全局曲线的素数幂分母

设 $E/\mathbb Q$ 的模 $p^n$ 像包含于 $N_n$ 的一个共轭。将 $j(E)$ 约分，则有
$$j(E)=\frac{a}{B^{p^n}},\qquad a\in\mathbb Z,\quad B\in\mathbb Z_{>0},\quad\gcd(a,B)=1.\tag{35.5}$$
每个 $q\mid B$ 满足 $q\equiv\pm1\pmod{p^n}$；若为正号，还须
$$a\bmod q\in(\mathbb F_q^\times)^{p^n}.\tag{35.6}$$

式 (35.5) 来自全部负赋值都被 $p^n$ 整除。对 (35.6)，使用 R2 已核对的 Tate 反演
$$t=j^{-1}(1+O_q(j^{-1})).$$
括号内的主单位为 $p^n$ 次幂，分母的单位部分本来也是 $p^n$ 次幂；余下恰是 $a$ 的逆的剩余类条件，与 (35.6) 等价。

若 $B>1$，则 $q\mid B$ 都为奇素数，$q\pm1$ 是 $p^n$ 的正偶数倍，所以
$$q\ge2p^n-1,\qquad
\boxed{\quad h(j(E))\ge p^n\log(2p^n-1).\quad}\tag{35.7}$$
这仍然只有高度下界。只有另行取得适用于相同实际全局曲线的上界，才可用来限制 $p$ 或 $n$。

## 5. 固定 CM 曲线的高次同余

现在固定
$$A:y^2=x^3-x,\qquad p>37,\quad p\equiv3\pmod4,$$
并假设有实际 $G_{\mathbb Q}$ 同构
$$E[p^n]\simeq A[p^n].\tag{35.8}$$

**定理 35.3。** 令 $T=\{q:v_q(j(E))<0\}$。则 (35.5) 成立，且：

1. $N_E=32\prod_{q\in T}q$，同 R13；
2. 每个 $q\in T$ 满足
   $$q\equiv\chi_{-4}(q)\pmod{p^n},\qquad
   q\equiv\pm1\pmod{4p^n};\tag{35.9}$$
3. 若 $q\in T$ 在 $\mathbb Q(i)$ 分裂，则
   $$\boxed{\quad q\ge4p^{2n}+1.\quad}\tag{35.10}$$

若 $E$ 无 CM，$B>1$，因此
$$h(j(E))\ge p^n\log(4p^n-1);\tag{35.11}$$
若还有一个分裂分母素数，则
$$h(j(E))\ge p^n\log(4p^{2n}+1).\tag{35.12}$$

**证明。** CM 自同态 $i$ 在 $A[p^n]$ 上的作用记为 $J$。由于 $p\equiv3\pmod4$，$R_n[J]\simeq R_n[i]$ 正是上述非分裂二次代数，$A[p^n]$ 是其秩一自由模。最后一个事实也可从 $A(\mathbb C)=\mathbb C/\Lambda$ 看出：$\Lambda$ 是 $\mathbb Z[i]$ 理想，局部化到 $p$ 后自由，故 $\Lambda/p^n\Lambda$ 为所需自由模。

对每个 $g\in G_{\mathbb Q}$，
$$\rho_{A,p^n}(g)J\rho_{A,p^n}(g)^{-1}=\chi_{-4}(g)J.$$
所以全局像包含于 $N_n$，且其二次商恰是 $\chi_{-4}$：若符号为正，矩阵在 $J$ 的中心化子；若为负，因为 $2J$ 可逆，它不可能同时在中心化子。由 (35.8) 可对 $E$ 应用定理 35.2 和 (35.4)，得到 (35.5) 与 (35.9)。导子以及非 CM 时 $B>1$ 已由降模 $p$ 后的 R13、R11 得到。

设 $q\in T$ 分裂于 $\mathbb Q(i)$。R13 保证 $q\ne2,p$，$A$ 在 $q$ 好约化而 $E$ 乘法约化，其 Tate 二次特征不分歧。由 (35.9)，$q\equiv1\pmod{p^n}$，故 $E[p^n]$ 的 Frobenius 矩阵为
$$s_q I,\qquad s_q\in\{\pm1\}.$$
同构 (35.8) 因此给出 $A[p^n]$ 上的**同一个标量矩阵**；这里比仅知道 Frobenius 的迹与行列式更强。

在 $A/\mathbb F_q$ 上，Frobenius 与 $i$ 交换，故如 R13 的论证，它是
$$\pi_q=u+vi\in\mathbb Z[i],\qquad u^2+v^2=q.$$
$A[p^n]$ 对 $\mathbb Z[i]/p^n$ 的作用忠实，所以标量等式强迫
$$\pi_q\equiv s_q\pmod{p^n\mathbb Z[i]},\qquad
u\equiv s_q\pmod{p^n},\quad p^n\mid v.\tag{35.13}$$
若只使用 $u^2+v^2\equiv1\pmod{p^n}$，不能推出这里的 $p^n\mid v$；(35.13) 使用的正是完整的高次挠点同构。

曲线 $A$ 在每个奇 $q$ 处都有全有理 $2$ 挠点，因此 $q+1-2u\equiv0\pmod4$。$q\equiv1\pmod4$ 使 $u$ 为奇数，$v$ 为偶数。又 $q$ 为素数，所以 $v\ne0$，且 $u\ne0$。由 $p^n\mid v$ 得 $|v|\ge2p^n$、$|u|\ge1$，即 (35.10)。高度结论按约分分母直接推出。证毕。

## 6. 来源、用途与没有推出的结论

Tate 均匀化、正合列 (35.3) 和其 Kummer 类是经典工具，见 J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves* (1994), Chapter V, §3，[出版页](https://doi.org/10.1007/978-1-4612-0851-8)。R2 已给一级形式的原始文献定位；R13 已处理固定 CM 曲线、导子及 Frobenius 整环计算。本文新写出有限局部环引理、完整高次局部等价以及标量 Frobenius 给出的高次分母界。

M. Bisatt, L. Furio, D. Lombardo, *Explicit p-adic Hodge theory for elliptic curves and non-split Cartan images*, [arXiv:2603.04021v2](https://arxiv.org/abs/2603.04021)（2026-06-08），研究相同背景下的高次 $p$ 进像。本文只将其作为进一步研究的文献定位；没有引用尚未公认的像分类或 Hodge 理论论证来证明本结果。

若只知道模 $p$ 像异常，目前只能无条件应用上面的 $n=1$ 情形。高次结论要求模 $p^n$ 像仍包含于非分裂正规化子，或者确有 (35.8)。不能令 $n$ 任意增大后以分母无限可除得到假矛盾。实际满足这些更强假设的曲线仍缺统一高度上界；本文未完成 Serre 一致性。
