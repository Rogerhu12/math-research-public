# 任意普通不变空间均无任何整幂的不变闭补空间

作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。日期：2026-11-27（台北）。

**状态：完整证明的原算子结构结论。** 若 $M$ 是原 $A$ 的非零真闭不变子空间，则对每个正整数 $p$，都不存在闭 $A^p$-不变空间 $N$ 使 $H=M\dotplus N$。结论允许非正交补空间。它不预设 $M$ 是某种有限头图，也不排除没有这种补空间的普通不变子空间。

## 1. 已有准确输入

沿用原尾 $B_m$ 及 $\mathscr C_m=\{B_m\}'$。以下三条已经逐尾支付：

1. [有界根正文](R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md)证明每个 $\mathscr C_m$ 是交换的含单位 Banach 代数，$B_m$ 拟幂零，且有准确有限头尾分解。
2. [奇幂恢复](R12-appendix-odd-power-strong-recovery-all-power-commutants-and-actual-subquotients.md)给：若 $p=ds$、$d=2^{v_2(p)}$、$s$ 奇数，$c=\beta^{(0)}_{d-1}>0$，则
   $$
   A^p=c^s I_d\otimes B_{v_2(p)}^{\,s},
   \qquad
   \{A^p\}'=M_d(\mathscr C_{v_2(p)}).
   \tag{1.1}
   $$
3. [全部原尾强不可约](R12-appendix-all-original-tails-strongly-irreducible-and-ordinary-invariant-complements.md)证明每个 $\mathscr C_m$ 只有 $0,I$ 两个幂等，因而其中每个元素的算子谱连通。

最后一条可直接用于该 Banach 代数中的谱：完整交换子逆封闭。若 $Z\in\mathscr C_m$ 在 $B(K)$ 中可逆，由 $ZB_m=B_mZ$ 乘两侧逆得 $Z^{-1}B_m=B_mZ^{-1}$，所以 $Z^{-1}\in\mathscr C_m$。因此它的代数谱与算子谱相同。

## 2. 所有幂的不变补空间排除

**定理 2.1。** 设 $M\in\operatorname{Lat}A$，$p\ge1$。若存在有界幂等 $E$，满足
$$
E^2=E,\qquad EA^p=A^pE,\qquad \operatorname{Ran}E=M,
\tag{2.1}
$$
则 $E=0$ 或 $E=I$，故 $M=0$ 或 $M=H$。

**证明。** 由 $M$ 的 $A$-不变性，
$$
EAE=AE.
$$
置 $Y=AE$。准确有
$$
EY=YE=Y,\qquad
Y^p=A^pE.
\tag{2.2}
$$
而且 $E,Y$ 都与 $A^p$ 交换。将 $p=ds$、$d=2^v$、$s$ 奇数，使用 (1.1) 得
$$
E,Y\in M_d(\mathscr C_v),\qquad
Y^p=c^s(I_d\otimes B_v^{\,s})E.
\tag{2.3}
$$
这是后来字符像与完整 $J$ 交换的来源；只知道它与 $J^s$ 交换是不够的。

选深度 $\ell$ 使 $D=2^\ell\ge2s$。将每个 $\mathscr C_v$ 条目再分成 $D$ 位头和真尾。原身份
$$
B_v^D=\beta^{(v)}_{D-1}I_D\otimes B_{v+\ell}
$$
保证这些深尾条目属于交换 Banach 代数 $\mathscr C_{v+\ell}$。取其任意字符 $\chi$；它杀掉拟幂零的 $B_{v+\ell}$。逐条目施 $\chi$，记所得复矩阵为 $E_\chi,Y_\chi$，并记
$$
J=I_d\otimes J_{v,\ell},
$$
其中 $J_{v,\ell}$ 是长度 $D$ 的非退化加权 Jordan 块。由 (2.3) 的完整交换子范围和原首尾分解，
$$
E_\chi J=JE_\chi,\qquad
E_\chi^2=E_\chi,\qquad
E_\chi Y_\chi=Y_\chi E_\chi=Y_\chi,
\tag{2.4}
$$
$$
Y_\chi^p=c^sJ^sE_\chi.
\tag{2.5}
$$

令 $V=\operatorname{Ran}E_\chi$。因为 $E_\chi$ 与 $J$ 交换，$V$ 与 $\ker E_\chi$ 都被 $J$ 保持，且二者给整个有限维空间的直和。原 $J$ 的所有 Jordan 块长度恰为 $D$，准确有
$$
\ker J=\operatorname{Ran}J^{D-1}.
$$
这个身份下降到 $V$：
$$
\boxed{
\ker(J|_V)=\operatorname{Ran}(J|_V)^{D-1}.
}
\tag{2.6}
$$
确切地，若 $x\in V$ 且 $Jx=0$，先写 $x=J^{D-1}z$，再用 $E_\chi x=x$ 和交换性得到
$x=J^{D-1}E_\chi z$。反向显然。

$J|_V$ 的 nilpotent 块长度至多 $D$。一个短于 $D$ 的块会在左边的核贡献一维，在右边的 $(D-1)$ 次幂像贡献零维；一个长度 $D$ 的块在两边各贡献一维。所以 (2.6) 排除了全部短块。于是存在 $0\le r\le d$，使 $J|_V$ 恰由 $r$ 个长度 $D$ 的块组成。

若 $r>0$，由 $D\ge2s$，$J^s|_V$ 恰有 $rs$ 个 Jordan 块，而且每个长度至少二。式 (2.4) 保证 $Y_\chi$ 把 $V$ 保持，(2.5) 在 $V$ 上给一个 $p$ 次根。由[一般根稿的有限 Jordan 引理](R12-appendix-all-integer-power-root-multiplicity-and-closed-root-domains.md)，
$$
p\mid rs.
$$
因为 $p=ds$，这就是 $d\mid r$。结合 $0\le r\le d$，必有
$$
r=0\quad\text{或}\quad r=d.
$$
所以对每个字符 $\chi$，
$$
E_\chi=0\quad\text{或}\quad E_\chi=I_{dD}.
\tag{2.7}
$$

现在将深头矩阵 $E$ 的有限矩阵迹看成一个实际标量尾算子
$$
t=\operatorname{tr}_{dD}(E)\in\mathscr C_{v+\ell}.
$$
式 (2.7) 给
$$
\chi(t)\in\{0,dD\}\qquad\text{对每个字符 }\chi.
$$
交换含单位 Banach 代数中元素的谱等于其全部字符值的集合；故
$$
\sigma_{\mathscr C_{v+\ell}}(t)\subseteq\{0,dD\}.
$$
由第 1 节的逆封闭及已证谱连通，该非空谱只能是其中一个单点。因此，要么所有 $E_\chi=0$，要么所有 $E_\chi=I_{dD}$。

第一种情形中
$$
\chi(\det(I-E))=1
$$
对所有字符成立，故 $\det(I-E)$ 在 $\mathscr C_{v+\ell}$ 中可逆。矩阵伴随公式使 $I-E$ 有界可逆。再由 $E(I-E)=0$ 得 $E=0$。

第二种情形同理使 $\det E$ 可逆，从而 $E$ 可逆；$E^2=E$ 迫 $E=I$。证毕。

## 3. 任意普通不变 M 的结论

若 $M$ 与某闭 $A^p$-不变空间 $N$ 满足
$$
H=M\dotplus N,
$$
则 $M$ 本身也 $A^p$-不变。沿 $N$ 投影到 $M$ 的幂等有界，并与 $A^p$ 交换。因此定理 2.1 给
$$
\boxed{
0\ne M\ne H,\ M\in\operatorname{Lat}A
\quad\Longrightarrow\quad
M\text{ 没有任何 }A^p\text{-不变闭补空间 }(p\ge1).
}
\tag{3.1}
$$
这严格保留“闭”的要求。若两个闭不变空间的代数和只稠密而不闭，沿其中一个投影的算子可能无界，定理不能对它施用有限矩阵字符。

同样证明从任意 $B_m$ 开始成立。对任意正整数 $k$ 的整个放大 $I_k\otimes B_m$，则不能照搬结论：例如它的各副本本来就有闭不变补空间。本文只处理原重数一的实际尾及其原有限头整幂。
