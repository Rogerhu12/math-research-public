# 高位近似伴随、有限秩正湮灭泛函与条件化逃逸

日期：2026-11-12（UTC）。作者：literature。

状态：完整的实际泛函接口，不编号。
本稿使用原 Haar 表示的强伴随边界，给出在整个交换子单位球上一致的估计，
并写清有限多位条件化的全部归一化预算。
它没有证明慢符号的普遍限制稠密像。

## 1. 设置与待解的正常性问题

记
$$
\mathfrak C=\{A\}',\qquad
N_j=A^{2^j}/d_j,\qquad E_j=e_{10}^{(j)}.
$$
本题的真实公式和范数界为
$$
\|N_j\|\le1,\qquad
N_j^2=\eta_jN_{j+1},\qquad
\|N_j-E_j\|\le\eta_j,\qquad\eta_j\longrightarrow0.
\tag{1.1}
$$
在原乘积真空表示中，
$$
N_j\rightharpoonup I/2,\qquad
\rho_j:=N_j+N_j^*-I\longrightarrow0
\quad\text{强收敛}.
\tag{1.2}
$$
后一式来自 $E_j+E_j^*$ 在每个固定有限柱向量上最终等于 $I$，
再用 (1.1)、有限柱稠密性及统一范数界推广。
所有内积对第一变量线性。

取非零的正有限秩正常泛函
$$
\phi(T)=\sum_{\nu=1}^d\langle Tx_\nu,x_\nu\rangle,
\qquad
M=\phi(I)=\sum_\nu\|x_\nu\|^2>0.
\tag{1.3}
$$
设它湮灭一个交换代数理想 $\mathcal J\subseteq\mathfrak C$：
$$
\phi(T)=0\qquad(T\in\mathcal J).
\tag{1.4}
$$
关注的情形是
$\mathcal J=S\mathfrak C$ 或其范数闭包，
其中 $S=S_N$ 或 $S_Y$。
若起初只知有限秩 $\phi$ 湮灭 $S\mathcal A$，
R88 的 SOT 多项式逼近与有限秩泛函的 SOT 连续性
会把它延为 (1.4) 对 $S\mathfrak C$ 成立。
这里不把一般无限秩正常泛函直接称为 SOT 连续。

定义泛函范数
$$
\|\ell\|_{\mathfrak C^*}
=\sup_{\substack{T\in\mathfrak C\\\|T\|\le1}}|\ell(T)|.
$$
以下逼近发生在这个受限对偶范数中，
不是整个 $B(H)^*$ 的范数。

## 2. 一位的准确恒等式

令
$$
\lambda_j(T)=\phi(TN_j),\qquad
\psi_j(T)=
\sum_\nu\langle T N_jx_\nu,N_jx_\nu\rangle.
\tag{2.1}
$$
$\lambda_j$ 是有限秩正常线性泛函，但没有假定其为正。
$\psi_j$ 是正有限秩正常泛函。

对 $T\in\mathfrak C$，由于 $TN_j=N_jT$，且
$N_jx=x-N_j^*x+\rho_jx$，逐项有
$$
\begin{aligned}
\langle TN_jx,N_jx\rangle
={}&\langle TN_jx,x\rangle
-\langle TN_jx,N_j^*x\rangle
+\langle TN_jx,\rho_jx\rangle\\
={}&\langle TN_jx,x\rangle
-\langle TN_j^2x,x\rangle
+\langle TN_jx,\rho_jx\rangle.
\end{aligned}
$$
所以
$$
\boxed{
\psi_j(T)-\lambda_j(T)
=-\phi(TN_j^2)
+\sum_\nu\langle TN_jx_\nu,\rho_jx_\nu\rangle.
}
\tag{2.2}
$$
这是实际算子等式，不删去进位项。

由 (1.1)，
$$
\boxed{
\|\psi_j-\lambda_j\|_{\mathfrak C^*}
\le
\eta_jM+
\sum_\nu\|x_\nu\|\,\|\rho_jx_\nu\|
=:\varepsilon_j
\longrightarrow0.
}
\tag{2.3}
$$
因此误差对全部 $\|T\|\le1$ 的交换子一致。
没有把强收敛作用于随 $j$ 变化的 $Tx_\nu$；
右侧只涉及原来的固定有限列向量。

由于 $\mathcal J$ 是理想，
$$
\lambda_j|_{\mathcal J}=0.
\tag{2.4}
$$
由 (2.3)，
$$
\sup_{\substack{T\in\mathcal J\\\|T\|\le1}}|\psi_j(T)|
\le\varepsilon_j.
\tag{2.5}
$$
准确湮灭的是 $\lambda_j$；
为正且正常的是 $\psi_j$。
本稿没有把这两种性质未经证明地合到同一个泛函上。

(1.2)、(2.2) 又给
$$
\psi_j(I)\longrightarrow M/2.
$$
正泛函在包含单位的 $\mathfrak C$ 上的限制范数仍等于其质量，
故
$$
\boxed{\|\lambda_j\|_{\mathfrak C^*}\longrightarrow M/2.}
\tag{2.6}
$$

## 3. 不能自动升级为趋近原泛函一半的对偶范数收敛

固定 $T\in\mathfrak C$ 时，(1.2) 给
$$
\lambda_j(T)\longrightarrow\phi(T)/2.
\tag{3.1}
$$
但正常性本身不能把 (3.1) 升为
$\|\lambda_j-\phi/2\|_{\mathfrak C^*}\to0$。

实际真空态已经给出反例。
取 $\phi_0(T)=\langle T1,1\rangle$，并使用移动测试算子 $T=N_j$。
由于 $\|N_j\|\le1$，
$$
\begin{aligned}
\|\lambda_j-\phi_0/2\|_{\mathfrak C^*}
&\ge
\left|\phi_0(N_j^2)-\frac12\phi_0(N_j)\right|\\
&\longrightarrow\frac14.
\end{aligned}
\tag{3.2}
$$
这里第一项由真实 $N_j^2=\eta_jN_{j+1}$ 趋于0，
第二项由 (1.2) 趋于 $1/4$。

这个真空态不被声称湮灭慢符号理想。
(3.2) 只排除“单凭正常性和高位伴随关系，就可对全部移动多项式取极限”的推理。
它不否定 (1.4) 加上尚未发现的额外信息可能产生更强估计。

## 4. 有限多位：统一的真实 carry 与正常向量预算

取高位有限集合 $F$，令
$$
r=|F|,\qquad
N_F=\prod_{j\in F}N_j,\qquad
E_F=\prod_{j\in F}E_j,\qquad
\epsilon_F=\sum_{j\in F}\eta_j.
\tag{4.1}
$$
所有实际 $N_j$ 交换，且各因子为收缩。
有限乘积望远镜给
$$
\|N_F-E_F\|\le\epsilon_F.
\tag{4.2}
$$

令 $P_m$ 为前 $m$ 位有限柱空间的正交投影。
假设 $F\subseteq[m,\infty)$，置
$$
v_\nu=P_mx_\nu,\qquad
\delta_m^2=\sum_\nu\|x_\nu-v_\nu\|^2,\qquad
M_m=\sum_\nu\|v_\nu\|^2=M-\delta_m^2.
\tag{4.3}
$$
有限列的正常性给 $\delta_m\to0$。
还记
$$
\Delta_m=
\sum_\nu\|x_\nu-v_\nu\|(\|x_\nu\|+\|v_\nu\|)
\le2\sqrt M\,\delta_m.
\tag{4.4}
$$

定义
$$
\lambda_F(T)=\phi(TN_F),\qquad
\psi_F(T)=
\sum_\nu\langle T N_Fx_\nu,N_Fx_\nu\rangle.
\tag{4.5}
$$
同样 $\lambda_F|_{\mathcal J}=0$，$\psi_F$ 为正有限秩正常泛函。

**命题4.1。**
$$
\boxed{
\|\psi_F-\lambda_F\|_{\mathfrak C^*}
\le4\sqrt M\,\delta_m+3r\epsilon_FM.
}
\tag{4.6}
$$

先对有限柱列 $(v_\nu)$ 证明。
按任意次序逐个加入 $j\in F$。
设已经加入的集合为 $G$，$j\notin G$。
纯算子
$$
\rho_j^0=E_j+E_j^*-I
$$
与 $E_G$ 交换，且 $\rho_j^0v_\nu=0$。
由 $\|\rho_j\|\le3$、$\|\rho_j-\rho_j^0\|\le2\eta_j$ 和 (4.2)，
$$
\|\rho_jN_Gv_\nu\|
\le(3\epsilon_G+2\eta_j)\|v_\nu\|.
\tag{4.7}
$$
将 (2.2) 用于移动向量 $N_Gv_\nu$ 时，
不是直接援引强收敛，而是明确支付 (4.7)。
该步相对于上一集合的误差不超过
$$
\bigl(\eta_j+3\epsilon_G+2\eta_j\bigr)M_m
=3\epsilon_{G\cup\{j\}}M_m.
$$
上一集合的泛函误差可作用于 $TN_j$，
因为 $TN_j\in\mathfrak C$ 且 $\|TN_j\|\le\|T\|$。
逐步相加给有限柱列的总误差
$3r\epsilon_FM_m$。

把 $v_\nu$ 换回 $x_\nu$ 时，
$\lambda_F$ 与 $\psi_F$ 的每一次改变都在受限对偶范数中至多为
$\Delta_m$，因为 $N_F$ 是收缩。
故总误差至多
$2\Delta_m+3r\epsilon_FM_m$，
由 (4.4) 得 (4.6)。

这给了任意指定有限 $r$ 的完整控制，
没有从单个位的强极限直接推出一个长度增长的乘积极限。

## 5. 质量估计及合法归一化

由于 $F$ 位于有限柱头之外，
$$
\|E_Fv_\nu\|^2=2^{-r}\|v_\nu\|^2.
\tag{5.1}
$$
用 (4.2) 比较 $N_Fv_\nu$ 与 $E_Fv_\nu$，
其平方范数差的总和至多 $2\epsilon_FM_m$。
再把 $v_\nu$ 换为 $x_\nu$，误差至多 $\Delta_m$。
结合 $M-M_m=\delta_m^2\le\Delta_m$，得到
$$
\boxed{
|\psi_F(I)-2^{-r}M|
\le4\sqrt M\,\delta_m+2\epsilon_FM.
}
\tag{5.2}
$$

特别对每个固定 $r$，
当 $\min F\to\infty$ 时，(4.6)、(5.2) 的误差一致趋于0，
从而
$$
\psi_F(I)\longrightarrow2^{-r}M,\qquad
\|\lambda_F\|_{\mathfrak C^*}\longrightarrow2^{-r}M.
\tag{5.3}
$$
但如果 $r$ 也增长，不能略去这个指数小质量。

给定 $r\ge1$ 和 $0<\varepsilon\le1/2$，
可先选择足够大的 $m$，使
$$
\delta_m\le\frac{\varepsilon2^{-r}\sqrt M}{16},
\qquad
r\sup_{j\ge m}\eta_j
\le\frac{\varepsilon2^{-r}}{12r}.
\tag{5.4}
$$
正常性及 $\eta_j\to0$ 保证选择存在，
没有给未知正常向量擅自指定收敛速率。
此后任意 $r$ 元集合 $F\subseteq[m,\infty)$ 都满足相应预算。
由 (4.6)、(5.2)，
$$
\|\psi_F-\lambda_F\|_{\mathfrak C^*}
\le\frac{\varepsilon}{2}2^{-r}M,
\qquad
|\psi_F(I)-2^{-r}M|
\le\frac{5\varepsilon}{12}2^{-r}M.
\tag{5.5}
$$
所以 $m_F:=\psi_F(I)>0$，且
$$
\boxed{
\left\|
\frac{\psi_F}{m_F}-\frac{\lambda_F}{m_F}
\right\|_{\mathfrak C^*}
\le\varepsilon.
}
\tag{5.6}
$$
$\psi_F/m_F$ 是正有限秩正常状态；
$\lambda_F/m_F$ 准确湮灭 $\mathcal J$。
结论仍只是受限对偶范数接近，
不是声称后者已有正正常延拓，
也不是声称前者准确湮灭 $\mathcal J$。

## 6. 长度增长时确实可能只产生非正常逃逸态

现在令 $r\to\infty$，取 $\varepsilon_r\downarrow0$，
按 (5.4) 选 $m_r\to\infty$，
再取任意 $r$ 元高位集合 $F_r\subseteq[m_r,\infty)$。
置
$$
\omega_r=\psi_{F_r}/\psi_{F_r}(I).
$$
它们都是原 Haar 表示中的正有限秩正常状态，
并且由 (5.6)，
$$
\sup_{\substack{T\in\mathcal J\\\|T\|\le1}}|\omega_r(T)|
\le\varepsilon_r\longrightarrow0.
\tag{6.1}
$$

然而，这些状态在每个紧算子上趋于0。
完整证明如下。固定有限柱投影 $P_k$。
当 $k\le m_r$ 时，纯乘积的真空分量给准确等式
$$
P_kE_{F_r}v_\nu=2^{-r}P_kv_\nu.
$$
由 (4.2)，用列向量的 Hilbert 范数估计，
$$
\left(\sum_\nu
\|P_kN_{F_r}x_\nu\|^2\right)^{1/2}
\le
2^{-r}\sqrt M+\delta_{m_r}+\epsilon_{F_r}\sqrt M.
\tag{6.2}
$$
把 (5.4) 及 (5.5) 的质量下界代入，
例如可得充分安全的常数界
$$
\boxed{\omega_r(P_k)\le8\,2^{-r}\longrightarrow0.}
\tag{6.3}
$$
对任意紧算子 $K$，先用 $P_kKP_k$ 在范数中逼近 $K$，
再用正性给
$$
|\omega_r(P_kKP_k)|\le\|K\|\,\omega_r(P_k),
$$
便得到 $\omega_r(K)\to0$。

因此任意 $B(H)^*$ 弱* 聚点状态都湮灭全部紧算子，
而其在 $I$ 上仍取1。
它是相对于原 Haar 表示的非正常状态。
由 (6.1)，该聚点同时湮灭 $\mathcal J$。
这里如有需要应取弱* 收敛子网，
不假设整个 $B(H)$ 上存在弱* 收敛子列。

所以，多位归一化没有自动改善原正常见证：
它能够把一个假设存在的正常湮灭者，
送成准确湮灭同一理想的非正常极限状态。
这与纯模型中的奇异正消去态并不冲突，
也不能反过来证明原正常湮灭者不存在。

## 7. 当前准确增量与未闭合处

本稿得到的是：

- 一位近似伴随关系产生整个 $\mathfrak C$ 单位球上一致的近正性式；
- 有限多位情形可用同一正常有限列及真实 carry 预算控制；
- 归一化必须显式支付质量 $2^{-r}$；
- 若让条件化位数增长，实际状态在紧算子上逃逸，
  不能把非正常聚点冒认为原 Haar-normal folium 中的新向量见证。

要排除慢 $S$ 的正有限秩正常湮灭者，
仍需一项额外事实，将准确湮灭与正正常性同时保留下来，
或控制与慢系数相关的移动多项式而不损失全部正常质量。
(2.3)、(4.6) 与 (5.6) 本身尚未提供这项事实。
完整 Hilbert 不变子空间问题未由这些估计解决。
