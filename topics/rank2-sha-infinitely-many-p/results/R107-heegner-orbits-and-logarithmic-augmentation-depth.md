# R107. 实际 Heegner 轨道的跨素数增广长度

固定 $F=\mathbb Q(\sqrt{-15})$ 与 $E:y^2=x^3-17x$。
取 R105 的真实类群和 $X_\ell=\Phi(z_\ell)$，其中
$\Phi:X_0(3N_E)\to E$ 固定且有限；每个充分大的输入 $p$ 可选
$v_p(\ell+1)=1$、$\ell\ll p^C$，使
$0<\widehat h(X_\ell)\ll\log p$。

## 精确挠点与固定纤维

有
\[
E(F^{\rm ab})_{\rm tors}=E[2].
\]
两个固定好素数 $53,61$ 均在 $F$ 与 $\mathbb Q(i)$ 分裂。
直接点数给 CM Frobenius $-7\pm2i$、$-6\pm5i$。
它们与交换 CM 两条线的 $g\in G_F$ 在阿贝尔点上交换，
故 prime-to-$53$、prime-to-$61$ 挠点分别被 $4$、$10$ 杀。
交叉处理这两个 primary 例外后即得二挠上界；全部二挠点确在
$F(\sqrt{17})$ 中。

令 $\sigma_p$ 为环类 Galois 群中的任意阶 $p$ 元，
$\Delta_p=\sigma_p-1$。若 $\Delta_pX_\ell$ 挠，则
$[2]X_\ell$ 为 $\sigma_p$ 不变，迫使 $p$ 个不同 CM 源点落在
固定 $[2]\Phi$ 的同一纤维中。
因此 $p>4\deg\Phi$ 时，$\Delta_pX_\ell$ 非挠。
有限阶作用的特征零半单性进一步给所有 $k\ge1$ 的
$\Delta_p^kX_\ell$ 都非挠。

## 真实模 p Jordan 长度随 p 增长

由 Galois 不变的二次高度，
\[
\widehat h(\Delta_p^kX_\ell)\le4^k\widehat h(X_\ell)
\ll4^k\log p.
\]
配合 R102 的 Baker 固定正高度下界，存在常数 $C_0$，使
\[
K_p=\left\lfloor\log_2p-\tfrac12\log_2\log p-C_0\right\rfloor
\quad\Longrightarrow\quad
\Delta_p^kX_\ell\notin pE(F[\ell])\quad(0\le k\le K_p).
\]
所以实际 $X_\ell$ 模 $p$ 的循环子模有至少 $K_p+1$ 的 Jordan 长度。
这并未达到单素数 Kolyvagin 导数所需的最底增广原始性。

## 额外做完一次实际 prime-to-p 迹

另一个分歧理想
\[
\mathfrak r_{5,\ell}=(5,(5+\ell\sqrt{-15})/2)
\]
满足 $\mathfrak r_{5,\ell}^2=(5)$。
它的 Artin 元 $\tau_{5,\ell}$ 与 R105 的 $\tau_{3,\ell}$ 之积，
恰是 $G_\ell$ 的唯一阶二元 $\epsilon_\ell$。
实际点
\[
Z_\ell=(1+\epsilon_\ell)X_\ell
=(1+\tau_{3,\ell})(1+\tau_{5,\ell})P[\ell]
\]
来自固定 $\Psi:X_0(15N_E)\to E$，其微分为
\[
c\bigl(f(q)+3f(q^3)+5f(q^5)+15f(q^{15})\bigr)dq/q.
\]
非零首项使 $\Psi$ 有限，故同样得到 $\widehat h(Z_\ell)\asymp\log\ell$
及上述约对数长度的所有不可除性。

若 $U\subset G_\ell$ 阶为 $u=(\ell+1)/p$，则 R104 的实际迹点
现在为
\[
Q_{\ell,p}=\operatorname{Tr}_{U/\langle\epsilon_\ell\rangle}Z_\ell.
\]
剩余次数 $u/2$ 仍为偶数。
正文还证明：固定理想在无穷多个环类群中有统一有界阶时，只能来自
$3,5$ 的分歧理想；一个真实阶四相对理想类的 prime-to-$\ell$
整代表范数至少为 $\ell/2$。
这个限制只针对这些 CM 同源分支，不排除别的全局迹恒等式。

[完整证明](../notes/2026-11-12-heegner-orbits-and-logarithmic-augmentation-depth.md)
与[两素数整数证书](../scripts/check-minus15-abelian-torsion.py)。
尚待控制剩余实际迹和最底增广层；无穷多个 $p$ 的 Sha 有限性仍未证明。
