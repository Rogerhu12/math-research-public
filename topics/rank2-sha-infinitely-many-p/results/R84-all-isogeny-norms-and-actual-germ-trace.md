# R84：全部同源范数、准确常数与实际全 germ 迹

日期：2026-11-12。状态：全部除子、常数、复合及微分公式已根端独审。
完整证明见[所有同源邻点的 Kummer 范数](../notes/2026-11-12-all-isogeny-neighbors-kummer-norms.md)。

固定 $N=68$，使用原归一单位
$r_P(R)=\Psi_N(P+R)/(d_PZ(R))$、$d_P=D\Psi_N(P)$。
所有同源都运输原来的 $N$ 级及二挠点标签。

## 1. 常数不能在取范数时省略

对奇次数 $n$、$(n,N)=1$ 的同源 $\varphi$，准确有

$$
\operatorname{Norm}_\varphi r_P
=\kappa_{\varphi,P}r'_{\varphi P},\qquad
\kappa_{\varphi,P}=\prod_{Q\in\ker\varphi}r_P(Q)
=\frac{K_{\varphi,N}}{\Psi_\varphi(P)^{N^2}}.
$$

$K_{\varphi,N}=\prod_R\Psi_\varphi(R)^{D_N(R)}$ 保留完整公共除子
$D_N$，包括两个二挠点处的重数二。
所有阶 $p$ 子群的非零点分拆给
$\prod_G\kappa_{\varphi_G,P}=\kappa_{[p],P}$。

令 $\mathfrak D=\prod_Rd_R^{D_N(R)}$、$w_P=d_P^{N^2}/\mathfrak D$。
除法函数的复合式在 $P$ 处展开一次项给

$$
d_{pP}\Psi_p(P)^{N^2}=N^{1-p^2}d_P^{p^2},\qquad
\kappa_{[p],P}^{N^2}=\frac{w_{pP}}{w_P^{p^2}}.
$$

第一式两边的 $p$ 已准确相消。原轨道满足 $p\mathcal S=\epsilon_p\mathcal S$，
$\epsilon_p=(-1/p)$，且 $d_{-P}=d_P$，故
$\kappa_{[p],\mathcal S}^{N^2}=w_{\mathcal S}^{1-p^2}$。
在原 CM 纤维上旋转轨道的 $w$ 相同，真实偶投影的常数对数为

$$
\mathcal L_{\kappa,e}
=\frac{c_e(1-i)(p^2-1)}{2N^4}\log w_{\mathcal S}.
$$

这是准确常数公式；其正次数纤维导数全为零，继续作模参数导数也不改变这一点。
因此即使另证这个固定对数非零，也不能直接传到目标行。

## 2. 全部邻点的真实微分权重

整个归一 germ 满足

$$
\prod_G r^{E/G}_{\varphi_GP}(\varphi_GR)
=r_P(R)^p r_{pP}([p]R).
$$

取原偶投影并令 $\varphi_G^*\omega_G=c_G\omega$，得到

$$
\sum_G h_{e,G}(\varphi_GR)=p h_e(R)+h_e(\epsilon_p[p]R),
$$
$$
\sum_Gc_G^kD_G^kh_{e,G}(O)
=(p+\epsilon_p^kp^k)D^kh_e(O).
$$

惰性 $k=1$ 时右端为零，高阶不能误用同一个零结论。
以上在加法参数中是完整导数公式；换原形式参数须保留完整同源级数。

## 3. Frobenius 比较的交换子

对共同代数闭包选定一个一致的系数 $\sigma$ 延拓，
$B_\Phi(u)=p^{-1}(\log u^\sigma\Phi-p\log u)$ 的完整迹式成立。
把源 lift 改成每个邻点自己的 lift 时，必须保留

$$
\frac1p\log
\frac{(r'_G)^\sigma\varphi_G^\sigma\Phi_E}
     {(r'_G)^\sigma\Phi_G\varphi_G}.
$$

分歧邻点上并未指定一个典范 Witt Frobenius，也未声称这些交换子整。
本结果提供完整同源关系，尚未证明其指定 GM 中央投影对无穷多个 $p$ 非零。
