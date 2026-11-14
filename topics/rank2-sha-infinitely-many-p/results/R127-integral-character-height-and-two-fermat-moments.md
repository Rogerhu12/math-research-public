# R127. 整角色高度与两个实际全局 Fermat 商矩

日期：2026-11-12。状态：已证明；无穷非零性仍开。

完整证明、所有地方的 norm 及正规化见
[整角色高度与 Fermat 测试](../notes/2026-11-12-cyclotomic-height-integral-character-and-fermat-test.md)。

本结果只用于 R120 的子族：$p\ge13$ 在
$F=\mathbb Q(\sqrt{-15})$ 与 $\mathbb Q(i)$ 均分裂。
另排除固定有限多个整除 $\#\Sha(E^{(-15)}/\mathbb Q)$ 的素数。
R123 为这个子族提供相对密度一的合法实际输入；下面的矩
非零仍待证明。无需假设 R126 的无穷素数落入这个子族。
取实际范数一 Heegner 点 $Q$，写
$$
A(F)\widehat\otimes\mathbb Z_p=\mathcal O w,
\quad \mathcal O=\mathbb Z_p[\zeta_p],
\quad Q=\delta^a\varepsilon w,
\quad\delta=\zeta_p^{(p-1)/2}(\zeta_p-1).
$$

## 1. 准确的整高度对象

以 raw $\log_p$、再除 $[L:\mathbb Q]=2p$ 的二次高度
$H$ 定义 $h(P,Q)=\tfrac12(H(P+Q)-H(P)-H(Q))$。
Mazur–Stein–Tate 的全部地方公式给 $h(W,W)\subset\mathbb Z_p$。
令
$$
b_j=h(Q,\tau^jQ),\qquad
\mathcal R_Q=\frac{\sum_{j=0}^{p-1}b_j\zeta_p^j}{\delta^2}.
$$
则
$$
\mathcal R_Q\in\mathcal O^+,
\qquad v_\delta\mathcal R_Q=2a+v_\delta\mathcal R_w.
$$
若 $h(xQ,yQ)=\operatorname{Tr}(c_Qx\bar y)$，则
$\sum b_j\zeta_p^j=pc_Q$。different 指数为 $p-2$，
$c_w$ 的共轭不变性使 $v_\delta c_w\ge-(p-3)$，
所以准确 regulator 赋值为
$$
v_p\operatorname{Reg}_h(W)=1+v_\delta\mathcal R_w.
$$
高度非退化只给 $\mathcal R_w\ne0$。

原辅助位 $\ell$ 的首 jet 给
$v_\ell t_E(2Q)=1/p$。所有 $\Gamma$ 共轭以及任意两个
共轭之和具有相同局部参数赋值；因此对全局高度作极化后，
$\ell$ 处的局部矩阵是常数矩阵。它在每个非平凡角色的
Fourier 系数**准确为零**。单独的
$\log_p\ell/p$ 单位项不是目标高度的单位证书。

## 2. 两个有限全局测试

令 $d=(p-1)/2$。Chebyshev 整多项式展开给
$$
v_\delta\mathcal R_Q<4
\quad\Longleftrightarrow\quad
\left(\sum_{j=1}^{d}j^2b_j,
      \sum_{j=1}^{d}j^4b_j\right)\ne(0,0)\pmod p.
$$
它强迫 $a\le1$，这已经足以给
$\Sha(E/\mathbb Q)[p^\infty]=0$，无需 $a$ 为偶数或
$r_-=1$。具体地，令 $d_p=\dim\Sha(E/\mathbb Q)[p]$。
R125 给 $\operatorname{length}_{\mathcal O}S\le2a$。
$a=0$ 时 $S=0$，R122 立即给 $d_p=0$。
$a=1$ 时其负号公式迫使 $r_-=0$ 且
$\dim S[\delta]^-=1$，正号公式给
$\dim S[\delta]^+\ge1+d_p$；故
$2+d_p\le\dim S[\delta]\le\operatorname{length}S\le2$，
仍给 $d_p=0$。此分支允许非零的有限 $S$，并未消去它。

上述 $a\le1$ 的充分推论只用 R122、R125，故删去同一固定
有限集后对任意充分大的好素数成立。ordinary／在 $F$ 分裂
只限制本篇的高度测试。由 R128，完整整数条件
$Q\notin(\sigma_{\mathfrak b}-1)^2A(F)$ 因而已经充分；
不必先排除一次差分像。

这些高度矩可以完全换成实际有理范数的 Fermat 商。
令 $s\in\Gamma$ 为一个 $p$ 上素位的算术 Frobenius，并取
$$
D=(s^2-a_ps+p)(s^{-2}-a_ps^{-1}+p),\qquad R=12DQ.
$$
有限域 Frobenius 特征多项式使 $R$ 在所有 $p$ 处
formal；$12$ 清掉坏位组件，且 $12D\in\mathcal O^\times$。
故 $R$ 保持实际指数 $a$。

对这样的点 $P$，令
$$
\nu(P)=\frac{N_{L/\mathbb Q}(-x(P)/y(P))}
                    {N_{L/\mathbb Q}\mathfrak d(P)},
\qquad z_j=\frac{\nu(R+\tau^jR)}{\nu(R)^2}.
$$
这些是非零有理 $p$-单位；$\mathfrak d(P)$ 是 $x(P)$
分母理想的平方根。ordinary sigma 的奇整性以及全部
$p$ 处 norm 给
$$
h(R,\tau^jR)\equiv-\frac14q_p(z_j)\pmod p,
\qquad q_p(z)=\frac{z^{p-1}-1}{p}\pmod p.
$$
所以，下面是一个纯有限精度、包含全部地方的充分证书；
它不再需要知道实际 $a$ 的奇偶：
$$
\boxed{\quad
\left(\sum_{j=1}^{d}j^2q_p(z_j),
      \sum_{j=1}^{d}j^4q_p(z_j)\right)\ne(0,0)
\quad\Longrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]=0.
\quad}
$$

本结果没有证明这两个和在无穷 $p$ 中非零。固定 $61$
进 Mellin 非零性不能直接代替它：对 $p\ne61$，
$N(\zeta_p-1)=p$ 是 $61$-单位，故 $\delta$ 在
$\mathbb Z_{61}[\zeta_p]$ 中可逆，实际指数 $a$ 在这个
局部整格中不可见。新的全局比较仍须另证。

一手规范来源：Mazur–Stein–Tate（2006），
*Computation of p-Adic Heights and Log Convergence*，
Theorem 1.3、§§2.3–2.8，印页 592–595，
[作者全文](https://wstein.org/papers/pheight/pheight.pdf)。
