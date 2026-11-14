# R236 附录：纯等权整个高阶交换子像的真空衰减及高池弱极限

日期：2026-11-13（UTC）。作者：central_review。
独立复核：normal_complex 已核有限 $\mathfrak{sl}_2$ 分解、全部常数及尾和；
主会话已全文复核分解、旋转符号、精确模块质量及所有域。
状态：完整有限维估计及原 Haar 高池弱极限。
本稿仅处理纯等权 creation 和，不将其直接外推到异权主行或真实 Bell 算子。

## 1. 结论及与已有提升带障碍的区别

在
$$
H_N=(\mathbb C^2)^{\otimes N},\qquad
\Omega_N=\left(\frac{e_0+e_1}{\sqrt2}\right)^{\otimes N},
$$
令
$$
E_j=|1\rangle\langle0|^{(j)},\qquad
C_N=\sum_{j=1}^NE_j,\qquad
\delta_N(U)=[C_N,U].
$$
$C_N$ 的方向始终是 $e_0\mapsto e_1$。
允许任意有限维矩阵 $U$，不要求它是纯 lowering 单项或多项式。

**定理。** 设 $k\ge1$，
$$
Q=\delta_N^k(U),\qquad L=\lceil k/2\rceil.
$$
若 $L\le N$，则
$$
\boxed{
|\langle Q\Omega_N,\Omega_N\rangle|
\le
\sqrt{N+1}\,\|Q\|
\left[
\frac{(N!)^2}{(N-L)!(N+L)!}
\right]^{1/2}
\le
\sqrt{N+1}\,\|Q\|
\exp\!\left[-\frac{L^2}{2(N+L)}\right].
}
\tag{1.1}
$$
若 $k>2N$，则 $Q=0$。

特别，当 $\sup_N\|Q_N\|<\infty$ 且
$$
\frac{k_N}{\sqrt{N\log(N+1)}}\longrightarrow\infty,
\tag{1.2}
$$
真空配对趋于零。
固定比例 $k_N\asymp N$ 包含在该范围内。

[R236 已有提升带附录](R236-appendix-high-degree-raising-band-obstruction-and-range-projections.md)
控制纯高提升度输出，包括外坐标算子系数。
这里新增的限制是输出属于整个
$\operatorname{Ran}\delta_N^k$；
它可以含 lowering、对角项和混合项，不要求具有纯提升度。
本稿的明确阈值是 (1.2)，没有把它加强为仅 $k_N/\sqrt N\to\infty$。

## 2. 对称块压缩：只付 $N+1$ 维

令 $V_N\subset H_N$ 为完全对称张量空间，其维数为 $N+1$。
用 $v_j$ 表示恰好 $j$ 个物理 $1$ 的归一化对称向量，$0\le j\le N$。
则
$$
C_Nv_j=\sqrt{(j+1)(N-j)}\,v_{j+1},
\qquad
C_N^*v_j=\sqrt{j(N-j+1)}\,v_{j-1}.
\tag{2.1}
$$
超出指标范围时按零解释。
$V_N$ 同时约化 $C_N,C_N^*$，且 $\Omega_N\in V_N$。

记 $P_N^{\rm sym}$ 为其正交投影。
若
$$
U_{\rm sym}=P_N^{\rm sym}U|_{V_N},\qquad
Q_{\rm sym}=P_N^{\rm sym}Q|_{V_N},
$$
则准确有
$$
Q_{\rm sym}=\operatorname{ad}_{C_N|_{V_N}}^k(U_{\rm sym}),
\qquad
\|Q_{\rm sym}\|\le\|Q\|.
\tag{2.2}
$$
所以只需在 $\operatorname{End}(V_N)$ 中证明估计。
这一压缩是等权模型的实质；
对任意不同权的 creation 和，它一般不成立。

以下简写 $C=C_N|_{V_N}$，并在 $\operatorname{End}(V_N)$
使用 Hilbert--Schmidt 内积，约定对第一变量线性。

## 3. 全部交换子模块的自含正交分解

令
$$
H_0v_j=(j-N/2)v_j,\qquad
\mathscr E=\operatorname{ad}_C,\quad
\mathscr F=\operatorname{ad}_{C^*},\quad
\mathscr H=\operatorname{ad}_{H_0}.
$$
由 (2.1) 直接得到
$$
[C,C^*]=2H_0,\qquad [H_0,C]=C.
$$
因此
$$
[\mathscr E,\mathscr F]=2\mathscr H,\qquad
[\mathscr H,\mathscr E]=\mathscr E,\qquad
[\mathscr H,\mathscr F]=-\mathscr F,
\tag{3.1}
$$
且
$$
\mathscr E^*=\mathscr F,\qquad \mathscr H^*=\mathscr H
$$
（此处伴随取 Hilbert--Schmidt 度量）。

对每个 $0\le\ell\le N$，$C^\ell\ne0$，并满足
$$
\mathscr E(C^\ell)=0,\qquad
\mathscr H(C^\ell)=\ell C^\ell.
$$
逐次使用 (3.1)，有
$$
\mathscr E\mathscr F^j(C^\ell)
=j(2\ell-j+1)\mathscr F^{j-1}(C^\ell).
\tag{3.2}
$$
于是
$$
\|\mathscr F^j(C^\ell)\|_{\rm HS}^2
=
j!\frac{(2\ell)!}{(2\ell-j)!}\,
\|C^\ell\|_{\rm HS}^2
\quad(0\le j\le2\ell),
\tag{3.3}
$$
而 $\mathscr F^{2\ell+1}(C^\ell)=0$。
这些向量的 $\mathscr H$ 特征值是
$\ell,\ell-1,\ldots,-\ell$，所以彼此正交。

置
$$
\mathcal W_\ell
=\operatorname{span}\{\mathscr F^j(C^\ell):0\le j\le2\ell\}.
$$
其维数为 $2\ell+1$，并被 $\mathscr E,\mathscr F,\mathscr H$ 保持。
算子
$$
\mathscr K=\mathscr H^2+
\frac{\mathscr E\mathscr F+\mathscr F\mathscr E}{2}
$$
自伴；由 (3.1) 可逐项检查它与三者交换，
且在 $\mathcal W_\ell$ 上等于标量 $\ell(\ell+1)$。
这些标量彼此不同，故不同 $\mathcal W_\ell$ 正交。

最后
$$
\sum_{\ell=0}^N(2\ell+1)=(N+1)^2,
$$
正好是整个矩阵空间的维数。因此
$$
\boxed{
\operatorname{End}(V_N)
=\bigoplus_{\ell=0}^N\mathcal W_\ell
}
\tag{3.4}
$$
是完整正交分解。
在 $\mathcal W_\ell$ 上，$\mathscr E^{2\ell+1}=0$。
所以
$$
\operatorname{Ran}\mathscr E^k
\subseteq\bigoplus_{\ell\ge L}\mathcal W_\ell,
\qquad L=\lceil k/2\rceil.
\tag{3.5}
$$
没有假定不同物理权仍有同一个正交分解。

## 4. 真空秩一矩阵的精确模块质量

记
$$
\rho_N=|\Omega_N\rangle\langle\Omega_N|,
\qquad
\rho_{\rm top}=|v_N\rangle\langle v_N|.
$$
有限酉旋转
$$
R=\exp[-\pi(C-C^*)/4]
$$
把 $v_N=e_1^{\otimes N}$ 送到 $\Omega_N$。
它在原 $N$ 位上就是同一个单个位旋转的张量积。
由于每个 $\mathcal W_\ell$ 都被
$\mathscr E-\mathscr F$ 保持，酉共轭 $B\mapsto RBR^*$
保持每个 $\mathcal W_\ell$，并保持 Hilbert--Schmidt 范数。
故 $\rho_N$ 与 $\rho_{\rm top}$ 在各模块上的投影质量相同。

$\rho_{\rm top}$ 与 $H_0$ 交换，故它只与每个模块中的零权向量配对。
该零权方向恰为 $\mathscr F^\ell(C^\ell)$。
下面完整计算其系数。

首先，由 (2.1)，
$$
\begin{aligned}
\|C^\ell\|_{\rm HS}^2
&=(\ell!)^2
 \sum_{j=0}^{N-\ell}
 \binom{j+\ell}{\ell}\binom{N-j}{\ell}\\
&=(\ell!)^2\binom{N+\ell+1}{2\ell+1}.
\end{aligned}
\tag{4.1}
$$
最后一步是有限 Vandermonde 求和；
也可把两个生成式
$(1-z)^{-\ell-1}$ 相乘，比较 $z^{N-\ell}$ 系数得到。

在完整 Leibniz 展开
$$
\mathscr F^\ell(C^\ell)
=\sum_{j=0}^\ell(-1)^j\binom\ell j
(C^*)^{\ell-j}C^\ell(C^*)^j
$$
中，作用于 $v_N$ 后，只有 $j=\ell$ 能对顶对角贡献非零。
因此
$$
\langle\mathscr F^\ell(C^\ell)v_N,v_N\rangle
=(-1)^\ell\ell!\frac{N!}{(N-\ell)!}.
\tag{4.2}
$$
另一方面，(3.3) 在 $j=\ell$ 时给
$$
\|\mathscr F^\ell(C^\ell)\|_{\rm HS}^2
=(2\ell)!\,\|C^\ell\|_{\rm HS}^2.
\tag{4.3}
$$
将 (4.1)--(4.3) 合并，得到准确投影质量
$$
\boxed{
w_\ell
:=\|\operatorname{Proj}_{\mathcal W_\ell}\rho_N\|_{\rm HS}^2
=\frac{(2\ell+1)(N!)^2}
{(N-\ell)!(N+\ell+1)!}.
}
\tag{4.4}
$$

令
$$
R_L=\frac{(N!)^2}{(N-L)!(N+L)!}\quad(0\le L\le N),
\qquad R_{N+1}=0.
$$
直接相减有 $R_\ell-R_{\ell+1}=w_\ell$。
所以
$$
\boxed{
\sum_{\ell=L}^Nw_\ell=R_L.
}
\tag{4.5}
$$
特别 $R_0=1$，与 $\|\rho_N\|_{\rm HS}=1$ 一致。

又
$$
R_L=\prod_{j=0}^{L-1}\frac{N-j}{N+j+1}.
$$
使用 $\log(1-x)\le-x$，逐项得到
$$
\log R_L
\le-\sum_{j=0}^{L-1}\frac{2j+1}{N+j+1}
\le-\frac{L^2}{N+L}.
\tag{4.6}
$$

## 5. 输出范数估计及阈值

由 (2.2)、(3.5)、(4.5)，
$$
\begin{aligned}
|\langle Q\Omega_N,\Omega_N\rangle|
&=|\langle Q_{\rm sym},\rho_N\rangle_{\rm HS}|\\
&\le\|Q_{\rm sym}\|_{\rm HS}\sqrt{R_L}\\
&\le\sqrt{N+1}\,\|Q\|\sqrt{R_L}.
\end{aligned}
$$
这里最后一个维数损失是 $\sqrt{N+1}$，
不是整个 $2^N$ 维空间的 $2^{N/2}$。
再用 (4.6)，即得 (1.1)。

若 $k_N\le2N$，则 $L\asymp k_N$、$N+L\le2N$。
因而 (1.2) 使 (1.1) 右侧趋于零。
若某些 $k_N>2N$，相应交换子本来就是零，不造成例外。

因此，固定 $0<\eta<2$ 且 $k_N\ge\eta N$ 时，
任意统一有界的输出 $\delta_N^{k_N}U_N$
都不能在真空上趋向恒等。
$U_N$ 的范数允许任意增长；
本结论只约束已经形成的纯模型输出。

把 $C_N$ 乘任意非零共同标量不改变这一像空间，
因为 $\operatorname{ad}_{\gamma C_N}^k(U)
=\operatorname{ad}_{C_N}^k(\gamma^k U)$。

## 6. 外坐标算子系数及高池弱极限

允许任意 Hilbert 空间 $\mathcal K$，并令
$$
Q=\operatorname{ad}_{C_N\otimes I_\mathcal K}^k(U)
\in B(H_N\otimes\mathcal K).
$$
对任意 $x,y\in\mathcal K$，取外坐标矩阵元。
由于导子只作用 $H_N$，所得有限矩阵仍属于
$\operatorname{Ran}\delta_N^k$，而其范数至多
$\|Q\|\|x\|\|y\|$。
所以 (1.1) 升为
$$
\boxed{
\left\|
(\langle\Omega_N|\otimes I)Q
(|\Omega_N\rangle\otimes I)
\right\|
\le
\sqrt{N+1}\,\|Q\|\sqrt{R_L}.
}
\tag{6.1}
$$

在原 Haar 无限张量中，取任意 $N$ 个不同物理位为池，
要求 $N\to\infty$、池的最小物理位趋于无穷，
并满足 (1.2)。
若原输出 $Q_N$ 一致有界，则 (6.1) 先使全部固定有限柱交叉矩趋于零，
再由稠密性得到
$$
Q_N\rightharpoonup0\quad\text{弱算子收敛}.
\tag{6.2}
$$
最大物理位及池的跨度不进入常数。
这里只把纯有限池作为原 Haar 中的已知矩阵使用，
不宣称它属于实际 $A'$。

## 7. 对原 Bell 端项的准确限制

原全域双导子方案是
$$
[\operatorname{ad}_T^{2r}U_N]\,V_N\longrightarrow I
\quad\text{强收敛},
$$
其中右因子 $V_N$ 是纯提升和的 Moore--Penrose 逆。
展开整个乘积的导子时，必须保留 $V_N$ 的全部导子，
这正是尚未支付的短端项。

本稿说明一个更窄、但完整的事实：
在纯等权线性模型 $T=C_N$ 中，
当 $2r\asymp N$ 时，
不可能找到任意另一个输入 $\widetilde U_N$，
使 $\operatorname{ad}_{C_N}^{2r}\widetilde U_N$
既一致有界又强趋于恒等。
因此，在这个模型中不能仅把右伪逆吸收进新输入，
同时保留高阶整体导子和强单位输出。

该结论没有处理：

- 不同物理权 $a_j$ 的导子；
- 非线性 Bell 算子及核内关系；
- 仅在未知核上受控、而不在全空间一致有界的输出；
- 不经过整个高阶导子像的双边配对；
- 只知道真实 carry 模型输出有界的情形。

特别，异权与等权之间的对角相似通常有巨大条件数，
不能用 (2.2) 的等权正交压缩免费运输。
对真实 $N_j$，若要从纯模型传递结论，
必须另外支付实际输出与纯输出之差；
单凭实际输出的算子范数界并不够。

本稿不把一种端点改写机制的失败当作非零实际核的存在，
也不排除原 Bell 短端项仍能由真实无限结构关闭。
