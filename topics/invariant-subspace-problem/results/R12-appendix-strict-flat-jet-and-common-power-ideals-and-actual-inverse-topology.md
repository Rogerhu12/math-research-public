# R12 后续：全喷射平坦理想严格大于实际全部幂共同理想

日期：2026-11-28（台北）。作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。

本稿补充原两个平坦对象的严格差别及其实际除法拓扑；没有把任一平坦条件提升为原平方根分子的存在。

## 1. 原对象

固定原 Haar 尾 $C=A^{(m)}$，记 $\mathscr C=\{C\}'$。
沿用[完整兼容喷射](R12-appendix-full-commutant-compatible-formal-jets-and-flat-root-denominators.md)：
$$
\mathfrak I=\bigcap_\chi\ker j_\chi,\qquad
\mathfrak F=\bigcap_{n\ge1}C^n\mathscr C.
\tag{1}
$$
原文已证明 $\mathfrak I$ 是非零范数闭理想，$\mathfrak F\subset\mathfrak I$；
R267 的[实际全部幂共同倍数](R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)给 $\mathfrak F\ne0$。
$C$ 单射、拟幂零，且
$$
\beta_n=\|C^n\|,\qquad \beta_n^{1/n}\longrightarrow0.
\tag{2}
$$
这些均是同一个原尾上的结论。

## 2. 在闭平坦理想上的真正除法

由 $j_\chi(C)=z$，有准确的饱和等式
$$
\boxed{\mathfrak I\cap C^n\mathscr C=C^n\mathfrak I\quad(n\ge1).}
\tag{3}
$$
确实，若 $X=C^nY\in\mathfrak I$，则
$z^n j_\chi(Y)=0$；形式级数环无零因子，故 $j_\chi(Y)=0$ 对全部 $\chi$ 成立，即 $Y\in\mathfrak I$。反向包含由理想性成立。这里不能把 (3) 改成 $\mathfrak I\subset C^n\mathscr C$。

对任意 $n\ge1$，乘法
$$
M_{C^n}:\mathfrak I\longrightarrow\mathfrak I,\quad X\longmapsto C^nX
$$
是单射有界算子，其值域不闭。反设值域闭；闭图逆定理给常数 $b>0$ 使
$\|C^nX\|\ge b\|X\|$。对固定 $0\ne X\in\mathfrak I$ 迭代，得到
$$
b^k\|X\|\le\|C^{nk}X\|\le\beta_{nk}\|X\|.
\tag{4}
$$
取 $k$ 次根与 (2) 矛盾。因此
$$
\boxed{C^n\mathfrak I\text{ 严格包含于 }\mathfrak I
\text{，且不是范数闭子空间}.}
\tag{5}
$$
由单射消去 $C^n$，还得到整个严格下降链
$$
\mathfrak I\supsetneq C\mathfrak I
 \supsetneq C^2\mathfrak I\supsetneq\cdots.
\tag{6}
$$

结合 (3)、(5)，存在实际非零 $P_0\in\mathfrak I$ 满足
$$
P_0\notin C\mathscr C.
\tag{7}
$$
特别 $P_0H$ 不包含于 $\operatorname{Ran}C$：
若全域包含成立，$C^{-1}P_0$ 的最大自然实现处处定义且闭，因而有界；
由 $C$ 单射及 $P_0C=CP_0$，该有界除商属于 $\mathscr C$，与 (7) 矛盾。
不把这种 $P_0$ 宣称为单射、稠密像或任何已给闭根的分母。

因为 $\mathfrak F\subset C\mathscr C$，(7) 证明此前未比较的包含严格：
$$
\boxed{\mathfrak F\subsetneq\mathfrak I.}
\tag{8}
$$

## 3. 共同全部幂理想的范数闭包

实际共同幂理想满足
$$
\boxed{C\mathfrak F=\mathfrak F.}
\tag{9}
$$
给定 $X\in\mathfrak F$，先写 $X=CY$。对每个 $n$，另有
$X=C^{n+1}Z_n$；取消单射 $C$ 得 $Y=C^nZ_n$，所以 $Y\in\mathfrak F$。
反向包含显然。

若 $\mathfrak F$ 范数闭，则它是非零 Banach 空间，(9) 使乘 $C$ 成为有界双射，逆也有界；于是又与 (4) 的原拟幂零界矛盾。因此
$$
\boxed{\mathfrak F\text{ 不是范数闭理想}.}
\tag{10}
$$

记 $\mathfrak J=\overline{\mathfrak F}^{\|\cdot\|}$。这是非零范数闭理想，且
$$
\mathfrak F\subsetneq\mathfrak J\subseteq\mathfrak I,\qquad
\overline{C^n\mathfrak J}^{\|\cdot\|}=\mathfrak J\quad(n\ge1).
\tag{11}
$$
密度来自 $C^n\mathfrak F=\mathfrak F$。同时每个 $C^n\mathfrak J$ 非闭且严格小于 $\mathfrak J$，仍由 (4) 证明。
没有证明 $\mathfrak J=\mathfrak I$，也没有由 (11) 把闭包范围换成实际范围。

## 4. 可以合法使用的共同逆拓扑

对 $X\in\mathfrak F$，用唯一实际有界除商定义
$$
p_n(X)=\|C^{-n}X\|,\qquad
q_n(X)=\max_{0\le r\le n}p_r(X).
\tag{12}
$$
这是一个完整、局部乘法凸的 Fréchet 代数拓扑。完整性可直接把 $X$ 识别成序列 $(X_r)_{r\ge0}$：
$$
X_0=X,\qquad CX_{r+1}=X_r,\qquad X_r\in\mathscr C.
\tag{13}
$$
这些关系定义了 $\prod_{r\ge0}\mathscr C$ 的闭子空间；反向 (13) 给 $X_0\in\mathfrak F$。
又
$$
p_r(XY)\le p_r(X)\|Y\|,
\qquad q_n(XY)\le q_n(X)q_n(Y).
\tag{14}
$$
在这个拓扑中乘 $C$ 与其逆都连续：
$p_n(C^{-1}X)=p_{n+1}(X)$。

该完整拓扑不能由一个范数产生。若能，设该范数为 $\|\cdot\|_*$。
存在某个 $n$ 与常数 $K,K'$，使
$\|X\|_*\le Kq_n(X)\le KK'\|X\|_*$。
原同源估计
$$
q_n(C^kX)\le\beta_k q_n(X)
$$
使乘 $C$ 在这个 Banach 范数下仍拟幂零；但其逆连续，因此有界，与可逆 Banach 算子的谱非零矛盾。

(12)--(14) 允许以后逐一记录全部实际整数逆费用，不能用空的形式喷射替代它们，也不能据连续的整数除法自动定义半次幂。原同分母方程 $V^2=CP^2$ 的有界 $V$ 仍未构造。
