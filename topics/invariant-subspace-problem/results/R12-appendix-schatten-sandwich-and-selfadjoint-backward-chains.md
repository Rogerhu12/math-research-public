# R12 后续附录：Schatten 夹积极限与完整自伴回传链的排除

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf；全部极分解、理想范数与有限秩逆像域已核查。
状态：已证明，完整证明。沿用 [紧夹积与回传成本附录](R12-appendix-compact-sandwich-limit-and-backward-orbit-cost.md) 的实际有限放大旗子商，不增加任何未知限制上的归一化假设。自伴链的范数一致有界由极分解推出，不作为额外前提。

## 1. 任意有限 Schatten 指数的准确夹积极限

在一个实际有限放大旗子商 Q 上令
$
 T=P_QA^{(r)}|_Q,\qquad T_j=T^{2^j}/d_j.
$
前稿已证
$
 \|T_j\|\le1,\quad \|T_j^2\|\le\eta_j,\quad
 T_j^*T_j,\ T_jT_j^*\xrightarrow{\rm WOT}\tfrac12I_Q,
$
其中
$
 \eta_j=\exp(-1400\,16^j+630\,8^j-300\,2^j).
$
对 $1\le p<\infty$，记 $\mathcal S_p(Q)$ 为 Schatten 理想。

**定理 1.1。** 对任意 $K\in\mathcal S_p(Q)$，
$
 \boxed{\lim_{j\to\infty}\|T_jKT_j\|_p=\tfrac12\|K\|_p.} \tag{1.1}
$

若 K 有有限秩 s，取 $K=U\Sigma V^*$，U、V 为 $\mathbb C^s\to Q$ 的等距嵌入，$\Sigma$ 为奇异值对角阵。置
$A_j=T_jU,\ B_j=T_j^*V$，则有限维 Gram 矩阵满足
$
 A_j^*A_j\to\tfrac12I_s,\qquad B_j^*B_j\to\tfrac12I_s
$
于矩阵范数。充分大的 j 可以取两侧极分解；$T_jKT_j=A_j\Sigma B_j^*$ 的全部非零奇异值准确等于矩阵
$
 (A_j^*A_j)^{1/2}\Sigma(B_j^*B_j)^{1/2}
$
的奇异值。该矩阵以范数趋于 $\Sigma/2$，故其每个奇异值趋于对应原奇异值的一半。这证明有限秩的 (1.1)，而非只证明最大奇异值。

一般 K 取有限秩 $K_\nu\to K$ 于 $\mathcal S_p$。理想不等式及 $\|T_j\|\le1$ 给
$
 \|T_j(K-K_\nu)T_j\|_p\le\|K-K_\nu\|_p.
$
先取 j 的上下极限，再令 $\nu\to\infty$，即得 (1.1)。

相应回传缺陷也有完全同样的理想范数版本。若 $X_j\in\mathcal S_p(Q)$，令
$
 \delta_{j,p}=\|KT_j-T_jX_j\|_p,\qquad
 \delta'_{j,p}=\|T_jK-X_jT_j\|_p.
$
逐项乘法恒等式与理想范数给
$
 \boxed{\tfrac12\|K\|_p
   \le\liminf_j(\delta_{j,p}+\eta_j\|X_j\|_p),\qquad
 \tfrac12\|K\|_p
   \le\liminf_j(\delta'_{j,p}+\eta_j\|X_j\|_p).} \tag{1.2}
$
两式独立，不要求两个方向同时成立。

特别，若完整链的各项 $J_n\in\mathcal S_p(Q)$，且满足
$
 J_{n-1}T=TJ_n\quad(n\ge1)
 \quad\hbox{或}\quad
 TJ_{n-1}=J_nT\quad(n\ge1),
$
则
$
 \boxed{\liminf_j\eta_j\|J_{2^j}\|_p
       \ge\tfrac12\|J_0\|_p.} \tag{1.3}
$
当 $J_0\ge0$ 为非零迹类且 p=1 时，右端为
$\operatorname{Tr}J_0/2$。这里只在各相应项确属 $\mathcal S_p$ 时使用理想范数；不把逐项有界自动改成逐项迹类。

## 2. 任何全自伴完整链自动等范数，故紧起点必为零

[R23](R23-strong-star-polynomials-and-tail-block-projections.md)的实际多项式强单位使每个非零实际旗子商的 T 单射且稠密像。以下先给一般有界算子的极分解事实。

**引理 2.1。** 若 T 单射、稠密像，且有界自伴 J、L 满足
$
 JT=TL,
$
则 T 的极分解 $T=U|T|$ 中 U 为酉算子，并且
$
 [L,|T|]=0,\qquad J=ULU^*. \tag{2.1}
$

证明：T 单射且稠密像给 U 的初、终空间均为整个 Q。
对原等式取伴随，得 $T^*J=LT^*$。因此
$
 T^*JT=T^*TL=LT^*T.
$
L 与正算子 $|T|^2$ 交换，连续函数演算给它与 $|T|$ 交换。于是
$
 JU|T|=U|T|L=UL|T|.
$
$|T|$ 的像稠密，两个有界算子可在此稠密像上消去，得 $JU=UL$，即 (2.1)。没有取一个未经证明有界的 $|T|^{-1}$。证毕。

现在设每个 $J_n$ 都有界自伴，满足任一上述完整链。
对第一个方向，引理逐步给
$J_{n-1}=UJ_nU^*$；第二方向交换 J、L 的位置，同样给相邻项酉等价。故无需额外一致界，已经有
$
 \|J_n\|=\|J_0\|\qquad(n\ge0). \tag{2.2}
$
若 $J_0$ 紧，则每个 $J_n$ 也紧。前稿的算子范数下界
$\liminf_j\eta_j\|J_{2^j}\|\ge\|J_0\|/2$
与 (2.2)、$\eta_j\to0$ 矛盾，除非 $J_0=0$。

因此
$
 \boxed{\text{实际有限放大旗子商上，非零紧起点没有全自伴完整回传链。}} \tag{2.3}
$
全正完整链是其特例。这个结论不需要迹类、迹保持或预先假定一致有界；紧起点与每层自伴性才是所用条件。非紧常值链 $J_n=I$ 不被排除。

## 3. 有限秩自然共轭链：合法但迹不控制核范数

设 K 为有限秩，并且
$
 \operatorname{Ran}K\subseteq\bigcap_{n\ge1}\operatorname{Ran}T^n.
$
T 单射保证每个逆像唯一。取有限表示
$
 K=\sum_{\ell=1}^s u_\ell\otimes v_\ell
$
并让各 $u_\ell$ 位于 $\operatorname{Ran}K$。定义
$
 J_n=T^{-n}KT^n
     :=\sum_{\ell=1}^s T^{-n}u_\ell\otimes(T^*)^nv_\ell. \tag{3.1}
$
这是整个 Q 上真正的有限秩有界算子：只在有限多个已付域的向量上使用 $T^{-n}$。定义与有限表示无关，因为它就是先作用 $KT^n$，再在其有限维值域上取唯一逆像。

直接逐项计算得
$
 J_{n-1}T=TJ_n.
$
而有限和的迹公式合法给
$
 \operatorname{Tr}J_n
 =\sum_\ell\langle T^{-n}u_\ell,(T^*)^nv_\ell\rangle
 =\sum_\ell\langle u_\ell,v_\ell\rangle
 =\operatorname{Tr}K. \tag{3.2}
$
中间一式先将 $T^n$ 作用到已存在的 $T^{-n}u_\ell$；未循环交换无界算子与无穷迹。

尽管 (3.2) 恒定，(1.3) 给
$
 \liminf_j\eta_j\|J_{2^j}\|_1\ge\tfrac12\|K\|_1.
$
若 K 正且非零，右端为 $\operatorname{Tr}K/2$，核范数必爆炸。
所以迹恒定既不给一致核范数界，也不给每层正性。事实上 §2 已排除该完整链始终自伴。

任意迹类 K 的同类公式则仍须另付 $T^{-n}K$ 的全域及理想范数条件，不能从本节有限和推到未验证的无穷迹循环。本稿也没有从真正慢理想见证构造出一条全自伴链，或一条成本低于 (1.3) 的紧链。
