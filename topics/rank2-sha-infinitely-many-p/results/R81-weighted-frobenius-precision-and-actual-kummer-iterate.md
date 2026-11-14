# R81：加权 Frobenius 精度与实际 Kummer 迭代格

日期：2026-11-12。状态：加权估计、完整测试的加强输入及实际补偿均已证明。
完整证明见[二次 Frobenius 与 Kummer 迭代](../notes/2026-11-12-weighted-two-step-frobenius-and-kummer-iteration.md)。

固定惰性 $p\ge7$，$\rho=p^{-1/(p+1)}$，沿用 R77 的真实有理整 $G_p$。

## 1. 迭代次数不增加加权输入精度损失

置 $A_j=-G_p(t^{p^{2j}})/p$，准确有

$$
\|A_0\|_\rho=\rho^{-1},\qquad \|A_j\|_\rho=1\quad(j\ge1).
$$

第一因子的 $t^p$ 系数确有分母 $p$，故这不是系数格的免费整换基。
若 $G_p(0)=-pI$ 固定准确、其他系数误差模 $p^N$，则任意长度的乘积 $Q_a$ 满足

$$
\|\widetilde Q_a-Q_a\|_\rho\le p^{-(N-1)}\rho.
$$

恢复 $(Q_a)_{22}$ 与 $-(Q_a)_{12}/t$ 后，误差均至多 $p^{-(N-1)}$。
后续因子的误差被 $t\mapsto t^{p^{2j}}$ 推到高次，每项至多遇到一个非整首因子。

所以 R77 的完整测试 $S_{p,n}\bmod p^{4n+4}$，现在只需
$G_p$ 到 $D-3$、精度 $p^{4n+4}$，以及 $M_1$ 到 $D$、精度 $p^{4n+3}$；
$D=\min\{(p+1)p^n,2(p+1)(4n+3)+4\}$。
这一加强不改变完整判据，也没有给跨素数命中率。

## 2. 两次 Kummer 迭代的第一真实分母

选合法形式 lift $\phi(t)=t^p,\phi(Z)=Z^p$，完整系数作用记 $\Phi$。
实际两半线按奇偶交换；$\epsilon_j=e/o$、$\eta_j=c_e/c_{\epsilon_j}^{\sigma^j}$ 给

$$
\mathcal D_{e,h}
=\frac{\eta_h\Phi^h(h_{\epsilon_h})-p^hh_e}{p^h}
=\sum_{j=0}^{h-1}p^{-j}\eta_j\Phi^j(B_{\epsilon_j}).
$$

完整整性只有 $p^{h-1}\mathcal D_{e,h}$ 整。
对所有 $h\ge2$，

$$
[Z^p]\mathcal D_{e,h}=[Z^p]B_e-\frac{\eta_1}{p}M_o(t^p).
$$

总次数小于 $2p$ 的系数整，而 $t^pZ^p$ 的赋值准确为 $-1$。
该垂直行的 $\rho$ 范数恰为 $\rho^{-1}$，与首个归一 GM 因子的代价一致。
在二变量半径 $(\rho,p^{-1/(2p)})$ 上，所有 $\mathcal D_{e,h}$ 范数仍统一不超过一。
这是明确加权格中的有界性，不是原系数整性。

## 3. 指定投影的整化没有留下独立单位

真实 $\mathcal P_p(M_o(t^p))=-p$ 给

$$
\mathcal P_p([Z^p]\mathcal D_{e,h})
=\mathcal P_p([Z^p]B_e)+\eta_1\in\mathcal O.
$$

R78 已证明右侧未知投影内含准确 $-\eta_1$，故已知单位自动相消。
剩下的是带全部 GM 权重的固定代数对数导数及准确初值修正。
不能把这次指定行整化当作全层比较或新的非零证据。

**剩余任务：** 在这套实际格中联立完整 Hecke、isogeny 或高 Witt 关系，
对完整中央导数证明独立约束。
