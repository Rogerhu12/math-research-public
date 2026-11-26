# 实际 Haar 有界头图的底空间没有有界尾模补空间

作者：AI-assisted GPT-6 Astra Pro；会话 `Astra-ISP-8542378f-20261127`。日期：2026-11-27（Asia/Taipei）。

**状态：已证明的实际核/像约束。** 本稿保留同一个未知普通 $A$-不变空间及其真实有限头坐标像。若该坐标在 $M$ 上有下界，则其闭像 $L$ 不可能是原尾交换子中任何有界幂等算子的像，幂等算子不必正交。等价地，$L$ 没有对同一个尾算子不变的闭补空间。

本结论加强“底空间不是整个尾”及“无限余维”：后两者并不排除一个有界、非正交、对尾不变的补空间。仍没有排除一般不分裂的真闭底空间，也没有从原尾全空间字符推断限制空间的字符。

## 1. 有限重数中可分裂根限制的必要秩

用[原尾根重数定理](../results/R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md)的实际尾
$$
B_mf(z)=\alpha_{m+v_2(z)}f(z-1)
$$
及其完整交换子 $\mathscr C_m=\{B_m\}'$。前稿已逐尾证明每个 $\mathscr C_m$ 是含单位的交换 Banach 代数，并证明
$$
B_m=
\begin{pmatrix}0&B_{m+1}\\\alpha_mI&0\end{pmatrix},
\qquad
\chi(B_{m+1})=0
\tag{1.1}
$$
对 $\mathscr C_{m+1}$ 的每个字符成立。

固定 $k\ge1$，置 $\mathcal B=I_k\otimes B_m$，作用于 $K^{\oplus k}$。设 $L\ne0$ 是闭 $\mathcal B$-不变空间，且有有界 $T\in B(L)$ 满足
$$
T^q=\lambda\mathcal B|_L,\qquad \lambda\ne0,\qquad q\ge2.
\tag{1.2}
$$

**引理。** 若存在
$$
E\in B(K^{\oplus k}),\qquad
E^2=E,\quad E\mathcal B=\mathcal BE,\quad \operatorname{Ran}E=L,
\tag{1.3}
$$
则必有 $q\le k$。更准确地，每个下一尾字符下，$E$ 的有限非零像的维数为 $2r$，其中
$$
q\mid r,\qquad 1\le r\le k.
\tag{1.4}
$$
并且至少有一个这样的非零字符像。

**证明。** 定义整个 $K^{\oplus k}$ 上的有界算子
$$
Y=TE.
$$
因 $E|_L=I_L$，有
$$
EY=YE=Y,\qquad
Y^q=\lambda\mathcal B E.
\tag{1.5}
$$
$T$ 与其幂交换，所以 (1.2) 给 $T\mathcal Bx=\mathcal BTx$ 对 $x\in L$ 成立。结合 (1.3)，$Y$ 与整个 $\mathcal B$ 交换。因此 $E,Y$ 的 $k\times k$ 块均属于 $\mathscr C_m$。

再按每个尾的第一物理位分解。由于 $\mathscr C_m$ 元素与
$B_m^2=\alpha_m I_2\otimes B_{m+1}$ 交换，$E,Y$ 都成为
$M_{2k}(\mathscr C_{m+1})$ 中的矩阵。对任意字符 $\chi$ 逐块施加，记所得复矩阵为 $E_\chi,Y_\chi$。由 (1.1)、(1.5)，
$$
E_\chi^2=E_\chi,\qquad
E_\chi J=JE_\chi,\qquad
E_\chi Y_\chi=Y_\chi E_\chi=Y_\chi,
$$
$$
Y_\chi^q=\lambda J E_\chi,\qquad
J=I_k\otimes
\begin{pmatrix}0&0\\\alpha_m&0\end{pmatrix}.
\tag{1.6}
$$
这里 $J^2=0$ 且
$$
\ker J=\operatorname{Ran}J.
\tag{1.7}
$$

若 $V_\chi=\operatorname{Ran}E_\chi\ne0$，$J$ 保持这个空间，并且
$$
\ker(J|_{V_\chi})=\operatorname{Ran}(J|_{V_\chi}).
\tag{1.8}
$$
确切地，若 $v\in V_\chi\cap\ker J$，由 (1.7) 写 $v=Ju$；则
$v=E_\chi Ju=JE_\chi u$，所以 $v$ 属于 $J(V_\chi)$。反向包含由 $J^2=0$ 成立。

因此 $J|_{V_\chi}$ 的 Jordan 块全部为长度二，绝无长度一块；其维数为 $2r$，$1\le r\le k$。而 $Y_\chi$ 保持 $V_\chi$，在其上
$$
(Y_\chi|_{V_\chi})^q=\lambda J|_{V_\chi}.
$$
前稿的有限 Jordan 根秩论证给 $q\mid r$：根的块长度至多 $2q$，幂的秩恰为半维数，强迫每个根块长度都为 $2q$。这证明 (1.4)。

还必须排除所有字符像都是零的可能。若 $E_\chi=0$ 对全部 $\chi$ 成立，则在交换 Banach 代数 $\mathscr C_{m+1}$ 中，
$$
\chi\!\left(\det(I_{2k}-E)\right)=1
\quad\text{对每个字符 }\chi.
$$
交换含单位 Banach 代数中，一个元素非可逆当且仅当它属于某个极大理想，即被某个字符消去。所以 $\det(I_{2k}-E)$ 可逆；伴随矩阵公式给 $I_{2k}-E$ 在 $M_{2k}(\mathscr C_{m+1})$ 中可逆。但
$E(I-E)=0$，于是 $E=0$，与 $L\ne0$ 矛盾。因此至少有一个非零字符像，其 (1.4) 给 $q\le k$。$\square$

这一步只对整个尾交换子中的实际有界矩阵 $E,Y$ 取字符。没有对未知 $T|_L$ 单独取一个未经构造的全空间字符。

## 2. 应用于任意普通不变空间的真实有限头像

取
$$
H=\mathbb C^N\otimes K,\qquad N=2^m,\qquad
A^N=\beta_{N-1}I_N\otimes B_m.
\tag{2.1}
$$
令 $M\ne0$ 为闭 $A$-不变空间，$Q=Q_0\otimes I_K$，其中
$Q_0$ 秩为 $k$ 且 $0<k<N$。假设
$$
\|Qf\|\ge c\|f\|\quad(f\in M),\qquad c>0.
\tag{2.2}
$$
则 $L=QM\subset QH$ 闭，且
$$
F=Q|_M:M\longrightarrow L
$$
是有界同构；这里终点始终是实际像 $L$，没有改成整个 $QH$。

令
$$
T=F(A|_M)F^{-1}\in B(L).
$$
如前稿原幂计算所示，因为 $Q$ 与 $I_N\otimes B_m$ 交换，
$$
\boxed{T^N=\beta_{N-1}(I_k\otimes B_m)|_L.}
\tag{2.3}
$$
而 $L$ 对 $I_k\otimes B_m$ 不变。

将 §1 用于 $q=N>k$，得到
$$
\boxed{
\text{不存在有界 }E,\quad E^2=E,\quad
[E,I_k\otimes B_m]=0,\quad\operatorname{Ran}E=L.
}
\tag{2.4}
$$

等价地，不存在闭的 $(I_k\otimes B_m)$-不变空间 $L'$，使
$$
QH=L\dotplus L'
\tag{2.5}
$$
为拓扑直和。若有这样的直和，沿 $L'$ 投到 $L$ 的有界投影就满足 (2.4)；反过来，有界幂等算子的核是所需闭不变补空间。

特别，$L$ 不 reducing；但本结论更强，因为 (2.4) 连非正交交换投影也排除。它也不排除原正交投影 $P_L$ 的存在，只证明 $P_L$ 必须不与原尾算子交换。

## 3. R231 的原底空间与未付的返回

对 [R231](../results/R231-bounded-high-bit-graph-linear-root-cost-and-central-escape.md) 中任意已付删除下界的位 $j$，取完整头
$$
N=2^{j+1},\qquad k=2^j,
$$
并以该位的 Walsh 第二坐标为 $Q$。其闭底空间 $L_j$ 正是 §2 的实际 $L$。因此若原 Haar 核 $M\ne0$，
$$
\boxed{
L_j\text{ 在整个 }H^{\widehat j}
\text{ 中没有对 }I_{2^j}\otimes B_{j+1}
\text{ 不变的闭补空间。}
}
\tag{3.1}
$$
这与已付的无限余维相容，也保留全部低 $j$ 位放大。

后续若试图在这个未知底空间上构造一个与原尾交换的有界“投影式右逆”或尾模分裂，(2.4) 是必须满足的明确障碍。一般正交最小源和非交换右逆不在本排除范围内；它们的实际核、输出像、原图度量与费用仍需分别控制。本稿没有把此障碍当成不存在 $M$ 的证明。
