# R41：二除法域与全部 p 幂除法域的线性不交

日期：2026-11-12；会话：serre-uniformity-astra-cont/2026-11-12。

**状态：已证明的实际 Galois 像结论；中间进展。** R37、R40 的二次预解式判别式增长不只给出参数下界，还排除了二除法域与异常素数除法域之间的所有交域。这个不交结论自动保持到每个 $p^s$ 层；它不要求、也不推出 $E[p^s]$ 与 CM 曲线的高次同余。再由 Chebotarev 得到一个密度恰为 $1/6$ 的非零迹集合，但其最小素数仍没有所需的统一上界。

## 1. 适用范围与完整结论

本文使用以下两种已严格归约的实际异常族之一。

1. **固定参考族：** $E/\mathbb Q$ 非 CM，$p>37$、$p\equiv3\pmod4$，且
   $$E[p]\simeq A[p],\qquad A:y^2=x^3-x.$$
   R19 的反向参数化给出的 Frey 曲线与 $E$ 在 $\mathbb Q$ 上同构，所以 R37 适用于这条 $E$ 自身。
2. **变量参考族：** R24 的归一化非 CM 曲线 $E=E_0$，$p>37$、$p\equiv7\pmod{12}$，且
   $$E_0[p]\simeq A_d[p],\qquad A_d:y^2=x^3-dx,$$
   其中 $d$ 为有符号平方自由整数；使用 R40 的全部已证结论。

置
$$
H=\mathbb Q(E[2]),\qquad L_s=\mathbb Q(E[p^s]),
\qquad G_s=\operatorname{Gal}(L_s/\mathbb Q),\quad s\ge1.
$$
R37、R40 都已证明 $\operatorname{Gal}(H/\mathbb Q)\simeq S_3$。令
$$F=H^{A_3},\qquad D_F=\operatorname{disc}(F).$$
这里的 $F$ 是二除法三次式的二次预解式域；它不是模 $p$ Cartan 商域。后者在本文两族中都是 $\mathbb Q(i)$。

**定理 R41。** 对上述每条实际曲线以及每个整数 $s\ge1$，
$$\boxed{H\cap L_s=\mathbb Q.}\tag{41.1}$$
从而实际联合像为直积：
$$\boxed{
\operatorname{Gal}(\mathbb Q(E[2p^s])/\mathbb Q)
\simeq S_3\times G_s.
}\tag{41.2}$$
特别地，一级像为完整的非分裂 Cartan 正规化子 $N_{\rm ns}(p)$，故
$$\boxed{[\mathbb Q(E[2p]):\mathbb Q]=12(p^2-1).}\tag{41.3}$$
甚至 $H\cap\bigcup_{s\ge1}L_s=\mathbb Q$。

**迹分布推论。** 好素数中满足
$$\ell\equiv3\pmod4,\qquad a_\ell(E)\text{ 为奇数}$$
的集合有自然密度恰为 $1/6$。对其中每个 $\ell\ne p$，
$$\boxed{a_\ell(E)\in p(2\mathbb Z+1),\qquad
\ell\ge p^2/4.}\tag{41.4}$$
这给出无穷多个非零惰性迹素数，却不保证有任何一个小于 $p^2/4$；事实上，实际同余强迫它们全部在该阈值之后。

## 2. 完整正规化子只有三个二次子域

在 $\mathbb F_{p^2}$ 的二维 $\mathbb F_p$ 线性空间上写
$$
C=\{m_c:x\mapsto cx:c\in\mathbb F_{p^2}^{\times}\},
\qquad w:x\mapsto x^p.
$$
则
$$N=C\rtimes\langle w\rangle,\qquad wm_cw^{-1}=m_{c^p},\quad w^2=1.$$
因为 $C$ 交换，全部交换子由
$$[w,m_c]=m_{c^{p-1}}$$
生成。因此
$$[N,N]=C^{p-1},\qquad N^{\rm ab}\simeq C_{p-1}\times C_2.\tag{41.5}$$

令 $\epsilon:N\to\{\pm1\}$ 为 $N/C$ 特征。行列式在 $C$ 上是范数，在 $w$ 上为 $-1$。于是映射
$$
(\det,\epsilon):N\longrightarrow\mathbb F_p^\times\times\{\pm1\}
$$
满射，核恰为 $C^{p-1}$；这也直接核实了 (41.5)。到 $C_2$ 的非平凡特征只有
$$\epsilon,\qquad (\det)^{(p-1)/2},\qquad
\epsilon(\det)^{(p-1)/2}.\tag{41.6}$$

R1 把实际非 CM 曲线的一级像确定为整个 $N$。R13、R24 的实际 CM 比较确定 $\epsilon$ 的二次域为 $\mathbb Q(i)$。Weil 配对使行列式为模 $p$ 圆分特征；因为 $p\equiv3\pmod4$，圆分域的唯一二次子域为 $\mathbb Q(\sqrt{-p})$。所以 $L_1$ 的全部二次子域恰为
$$\boxed{
\mathbb Q(i),\qquad \mathbb Q(\sqrt{-p}),\qquad
\mathbb Q(\sqrt p).
}\tag{41.7}$$
它们两两不同，其基本判别式绝对值分别为 $4,p,4p$。

圆分二次域的符号也可直接由二次 Gauss 和核查：对 $\chi(a)=(a/p)$ 和 $\zeta_p$，$\tau=\sum_{a\in\mathbb F_p}\chi(a)\zeta_p^a$ 满足 $\sigma_b(\tau)=\chi(b)\tau$ 与 $\tau^2=\chi(-1)p=-p$。因此它实现的正是 (41.6) 的行列式二次特征。

这里使用完整的实际像；不能将一个仅仅包含于 $N$ 的任意子群直接代入 (41.5)。

## 3. 增长下界排除这三个交域候选

R37、R40 的普通类群分支都给
$$
|D_F|\ge
\begin{cases}
p^4/64,&F\text{ 为实二次域},\\
\pi^2p^4/1024,&F\text{ 为虚二次域}.
\end{cases}\tag{41.8}
$$
对 $p>37$，两个下界都严格大于 $4p$。例如后一不等式等价于 $p^3>4096/\pi^2$，在这里显然成立。因此 $F$ 不可能是 (41.7) 中的任一个域。

在特殊的二进射线分支，R37 §7、R40 §8 给
$$|D_F-1|\ge p^2/4.\tag{41.9}$$
若 $F$ 是 (41.7) 中的一个域，则 $|D_F|\le4p$，从而
$$|D_F-1|\le4p+1<p^2/4\qquad(p>37),$$
与 (41.9) 矛盾。故在这个分支也有同样的排除。

因此对本文全部实际曲线，
$$\boxed{F\not\subseteq L_1.}\tag{41.10}$$
证明并未假定 $F$ 实或虚，也没有把射线分支误用成普通类群的 Minkowski 界。

现在设 $J=H\cap L_1$。两个域都是 $\mathbb Q$ 的有限 Galois 扩张，所以 $J/\mathbb Q$ Galois。$S_3$ 的正规子群恰为 $1,A_3,S_3$，故
$$J\in\{H,F,\mathbb Q\}.$$
前两种都使 $F\subseteq L_1$，已由 (41.10) 排除。因此 $J=\mathbb Q$，证明 (41.1) 的 $s=1$ 情形。

这个论证也排除了可能的整三次分裂域交叠；不需要另加“$N$ 没有 $S_3$ 商”的假设。尤其固定参考族的 $p\equiv11\pmod{12}$ 也在适用范围内。

## 4. 为什么结论自动保持到全部 p 幂层

约化映射
$$\mathrm{GL}_2(\mathbb Z/p^s\mathbb Z)
\longrightarrow\mathrm{GL}_2(\mathbb F_p)$$
的核是一个有限 $p$ 群。实际像的约化同样满射到一级实际像，故 $L_s/L_1$ 是 $p$ 幂次数的 Galois 扩张。

设 $J_s=H\cap L_s$。因为 $J_s\subseteq H$，有 $[J_s:\mathbb Q]\mid6$；又因 $J_s\cap L_1\subseteq H\cap L_1=\mathbb Q$，
$$[J_sL_1:L_1]=[J_s:\mathbb Q].$$
但 $J_sL_1\subseteq L_s$，左端整除一个 $p$ 幂。$p>3$ 与 $6$ 互素，故这个次数必须为 $1$，即 $J_s=\mathbb Q$。

两个有限 Galois 扩张交为基域时线性不交，所以合成域的群是直积。由互素分解
$$E[2p^s]\simeq E[2]\oplus E[p^s]$$
的 Galois 等变性，其合成域就是 $\mathbb Q(E[2p^s])$，得到 (41.2)。取 $s=1$，$|S_3|=6$、$|N|=2(p^2-1)$，得到 (41.3)。

最后，$H\cap\bigcup_sL_s$ 是 $H$ 的一个有限子扩张。其有限多个生成元都已位于某个统一的有限层 $L_s$ 中，故由已证 (41.1) 也只能为 $\mathbb Q$。

**必须保留的区别：** 本节只提升了“不交”，没有提升 CM 挠点同构。$G_s$ 可以比非分裂 Cartan 正规化子的 $p^s$ 层大得多；本文未声称其所有外陪集元素在模 $p^s$ 下仍然迹为零。

## 5. 精确的 Frobenius 奇偶分布

在 $\mathrm{GL}_2(\mathbb F_2)\simeq S_3$ 中，迹为 $1$ 的元素恰为两个三循环。因此，给定任何共轭不变子集 $T\subseteq G_s$，(41.2) 与 Chebotarev 密度定理给
$$
\delta\{\ell\text{ 好}:a_\ell(E)\equiv1\pmod2,
\ \operatorname{Frob}_\ell|_{L_s}\in T\}
=\frac13\frac{|T|}{|G_s|}.
\tag{41.11}
$$
删去有限个坏素数和 $2,p$ 不改变自然密度。这里 $T$ 可为共轭类的任意有限并，故直接由 Chebotarev 的单共轭类形式相加得到。

取 $s=1$ 和 $T=N\setminus C$，有 $|T|/|N|=1/2$，于是密度为 $1/6$。Cartan 商域为 $\mathbb Q(i)$，所以这正是
$$\ell\equiv3\pmod4,\qquad a_\ell(E)\text{ 为奇数}$$
的集合。

取 $\mathbb F_{p^2}=\mathbb F_p(\sqrt u)$，其中 $u$ 为非平方。在基 $1,\sqrt u$ 下，外陪集元素的形式为
$$
m_{a+b\sqrt u}w=
\begin{pmatrix}a&-bu\\b&-a\end{pmatrix},
$$
其迹为零。因此这些好素数满足 $a_\ell(E)\equiv0\pmod p$。再与奇偶条件合并，得到
$$a_\ell(E)=p(2r+1)\ne0\qquad(r\in\mathbb Z).$$
Hasse 界随即给
$$p\le|a_\ell(E)|\le2\sqrt\ell,$$
即 (41.4)。

若另有实际高次同余 $E[p^s]\simeq A[p^s]$ 或相应 $A_d[p^s]$，则参考 CM 曲线在好素数 $\ell\equiv3\pmod4$ 的迹为零，故同一个密度 $1/6$ 集合还满足
$$a_\ell(E)\in p^s(2\mathbb Z+1),\qquad\ell\ge p^{2s}/4.$$
这一加强需要明确的额外高次同余假设；它不是第 4 节不交提升的结果。

## 6. 对全局检测路线的含义及真实缺口

R37、R40 的三次层不是模 $p$ 二次商或其圆分二次子域的一部分。甚至整个 $p$ 进除法塔都不能包含任何非平凡的二除法子扩张。因此将两个残余表示放在一起时，必须面对真实的直积像，不能假设一个未证的二次交域关系来强迫矛盾。

另一方面，直积像确实给出密度为 $1/6$ 的非零惰性迹素数。统一性所缺的是对其**第一个**素数足够强的上界，而密度定理只控制无穷远的比例；它不提供一个小于 $p^2/4$ 的素数。本文既没有这样的上界，也没有排除这些实际异常曲线。

## 7. 来源与依赖

- [R1](R1-exact-remaining-image.md)：$p>37$ 时非 CM 实际异常像为完整非分裂 Cartan 正规化子。
- [R13](R13-denominators-for-fixed-cm-congruence.md)、[R19](R19-converse-fermat-fixed-cm.md)：固定参考的 Cartan 商域及与同一条曲线的精确整数参数化。
- [R24](R24-quartic-parameter-and-discriminant-rigidity.md)：变量四次参考的实际同余及商域。
- [R37](R37-cubic-descent-and-class-group-obstruction.md)、[R40](R40-variable-quartic-cubic-class-fields.md)：$S_3$ 二除法域、普通/射线两类的精确判别式增长下界。
- J. S. Milne, *Algebraic Number Theory*, v3.08 (2020)，[作者原文](https://www.jmilne.org/math/CourseNotes/ANT.pdf)，Theorem 8.31 及 Example 8.34：Chebotarev 自然密度及圆分 Frobenius。本文只使用无条件密度定理，不使用 GRH 下的最小素数界。

正规化子交换化、三个二次域、交域排除、全部 $p$ 幂层的次数论证，以及奇偶密度的具体计数已在本文完整给出。
