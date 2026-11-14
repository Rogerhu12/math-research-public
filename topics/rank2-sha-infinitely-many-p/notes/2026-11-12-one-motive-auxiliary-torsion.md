# 将 Mordell–Weil 点放进 1-motive 后，辅助局部挠指数仍然无界

**可信度：已证明。** 这是 [整数/有理局部化笔记](2026-11-12-one-motive-localization-barrier.md) 的一个补充。即使把全部已知有理点、甚至一整组 Mordell–Weil 生成元放进固定的 1-motive，辅助素数处的局部挠群仍没有统一指数。因此不能靠这个修改使无限局部乘积自动与 $\mathbb Q_p$ 系数交换。

## 1. 精确命题

设 $E/\mathbb Q$ 是任意椭圆曲线，固定一个素数 $p$ 和有限多个点 $P_1,\ldots,P_r\in E(\mathbb Q)$。令
$$
M=[\mathbb Z^r\xrightarrow{u}E],\qquad u(e_j)=P_j.
$$
对每个好约化素数 $\ell\ne p$，令
$$
A_\ell=E(\mathbb Q_\ell)^{\wedge}_p
\simeq E(\mathbb F_\ell)[p^\infty],\qquad
B_\ell=A_\ell/\langle P_1,\ldots,P_r\rangle_{\mathbb Z_p}.
\tag{1}
$$
**命题。** 给定任意 $N\ge1$，存在无穷多个这样的 $\ell$，使 $B_\ell$ 有商
$$
(\mathbb Z/p^N\mathbb Z)^2.
\tag{2}
$$
特别地，$\{B_\ell\}_{\ell\ne p}$ 的指数没有统一上界，去掉任意有限个辅助素数后仍如此。

**证明。** 对每个 $j$ 选取 $R_j\in E(\overline{\mathbb Q})$ 满足 $p^N R_j=P_j$。取有限 Galois 扩张
$$
F_N=\mathbb Q(E[p^N],R_1,\ldots,R_r).
\tag{3}
$$
此域已经是 Galois 的：有理点 $P_j$ 的任一共轭除法点与 $R_j$ 相差 $E[p^N]$ 中的点。Chebotarev 密度定理给无穷多个在 $F_N$ 中完全分裂的好素数 $\ell\ne p$；排除任意额外有限集合不改变无穷性。

在这些素数处，全部 $p^N$ 挠点及 $R_j$ 均约化为 $\mathbb F_\ell$ 有理点；因 $p\ne\ell$，好约化对 $p$ 幂挠点单射。因此
$$
E(\mathbb F_\ell)[p^N]\simeq(\mathbb Z/p^N\mathbb Z)^2,
\qquad \overline P_j=p^N\overline R_j.
\tag{4}
$$
有限域椭圆曲线的 $p$-primary 群至多有两个循环因子。由 (4)，两个因子的阶均至少为 $p^N$，故
$$
A_\ell/p^NA_\ell\simeq(\mathbb Z/p^N\mathbb Z)^2.
\tag{5}
$$
每个 $P_j$ 在 $A_\ell$ 中的像属于 $p^NA_\ell$，所以 (1) 中的商满射到 (5)，得到 (2)。$\square$

这里 $p$ 已固定，$N$ 递增时域 $F_N$ 也递增。没有声称这些完全分裂素数集合具有一个独立于 $N$ 的正密度；各固定层的正密度已经足够证明指数无界。

## 2. 它确实出现在 $T_pM$ 的局部上同调中

1-motive 的 Tate 模正合列为
$$
0\longrightarrow T_pE\longrightarrow T_pM
\longrightarrow\mathbb Z_p^r\longrightarrow0.
\tag{6}
$$
由于格的 Galois 作用平凡，相应局部上同调列包含
$$
\mathbb Z_p^r\xrightarrow{\partial_\ell}
H^1(\mathbb Q_\ell,T_pE)
\longrightarrow H^1(\mathbb Q_\ell,T_pM),
\tag{7}
$$
其中 $\partial_\ell(e_j)$ 是 $P_j$ 的整数 Kummer 类（正负号不影响像）。整数 Kummer 单射把 $A_\ell$ 识别为 $H^1(\mathbb Q_\ell,T_pE)$ 的子群，而 (7) 中的核恰为这些 $P_j$ 的 $\mathbb Z_p$ 张成空间。因此得到单射
$$
\boxed{B_\ell\hookrightarrow H^1(\mathbb Q_\ell,T_pM)_{\rm tors}.}
\tag{8}
$$
由第 1 节，这些局部上同调群的 $p$ 挠指数仍无界。这一结论完全不依赖 $\Sha(E/\mathbb Q)$ 是否有限，也不要求 $P_j$ 独立。

尤其可以把 $P_1,\ldots,P_r$ 选成整个 $E(\mathbb Q)$ 的有限生成组，包括需要的扭点。故“先用固定 1-motive 把全部 Mordell–Weil 来源商掉”并不能修复局部群的统一分母问题。

## 3. 对目标的精确含义

选取互不相同的辅助素数 $\ell_N$，并在 (8) 的像中选取阶至少为 $p^N$ 的元素。令其余局部坐标为零，就得到一个局部乘积中的非挠元，每个单独坐标却是挠元。因此自然映射
$$
\left(\prod_{\ell\ne p}H^1(\mathbb Q_\ell,T_pM)\right)\otimes\mathbb Q_p
\longrightarrow
\prod_{\ell\ne p}H^1(\mathbb Q_\ell,V_pM)
\tag{9}
$$
仍不单射。

这只是对“统一清除全部局部挠分母”方法的严格障碍。这里构造的局部族没有被证明来自同一个全局上同调类，不能将它当作一个非零 $\Sha^1(\mathbb Q,V_pM)$ 类，更不能据此推得本题 Sha 无限。它表明，若要从 Jossen 的整数局部化定理得到额外的 Sha 控制，还需要关于**全局像**的新输入；仅靠修改 1-motive 后局部群的一致有界性无法做到。

## 来源

- Chebotarev 的使用仅为完全分裂素数的无穷性：J. S. Milne，[Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT210.pdf)，Theorem 8.31，或 [Class Field Theory](https://www.jmilne.org/math/CourseNotes/CFTc.pdf)，Chapter V, Theorem 3.23。
- Tate 模正合列及连续上同调约定：P. Jossen，[On the second Tate–Shafarevich group of a 1-motive](https://msp.org/ant/2013/7-10/ant-v7-n10-p05-p.pdf)，§§1–2；其 Lemma 5.2 的精确适用边界已在前一笔记中核对。
