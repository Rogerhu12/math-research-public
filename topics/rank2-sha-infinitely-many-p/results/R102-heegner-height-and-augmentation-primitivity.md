# R102. 原 Heegner 点的跨素数不可除性与实际导数缺口

沿用 R100 的固定 $E=E17$、虚二次域 $F$、模参数化 $\pi$ 和
无穷素数集合 $\mathcal P_F$。

## 原点有统一的双边高度界

对充分大的惰性辅助素数 $\ell$，准确有
\[
c_1\log\ell-C\le\widehat h(P[\ell])
\le c_2\log\ell+C,
\]
常数只依赖固定数据。
上界来自次数 $\ell$ 的 CM 同源和 Pazuki 的模高度比较；
下界来自 CM 阶的准确 Faltings 高度差
\[
h_F(\mathcal O_\ell)-h_F(\mathcal O_F)
=\left(\frac12-\frac1{\ell+1}\right)\log\ell.
\]
固定曲线 $X_0(N_E)$ 上 $j$ 与 $\pi$ 拉回的 ample 高度互相控制，
将这两边传到实际点 $P[\ell]$，没有将原点和迹混同。

## 对每个充分大的目标 p，原点可以取为不可除

Baker 对 $E(F^{\rm ab})$ 的定理给固定正常数 $c_{E,F}$，
使所有非扭点的典范高度至少为 $c_{E,F}$。
固定两个二次惰性条件并加入 $\ell\equiv-1\pmod p$，
CRT 与 Linnik 给
\[
4p-1\le\ell\le C_Fp^L.
\]
因此对每个充分大的 $p\in\mathcal P_F$，可选合法辅助 $\ell$，
使 $0<\widehat h(P[\ell])\ll\log p<c_{E,F}p^2$，从而
\[
\boxed{P[\ell]\notin pE(F[\ell]).}
\]
这是固定参数化的真实代数点结论，且同时适用于所有充分大的
输入 $p$；但 R100 需要的是导出点 $Y_\ell$。

## 为什么还不能移到导出点

令 $q=\ell+1$、$n=p^{M_\ell}\mid q$。
原整数导数给 $\widehat h(Y_\ell)\ll q^4\log\ell$。
将系数模 $n$ 化为平衡剩余，仍在同一域得到实际点 $Z$，
$Y_\ell-Z\in nE(F[\ell])$，但其可证上界仅为
\[
\widehat h(Z)\ll q^2n^2\log\ell.
\]
这些界达不到 Baker 判据所需的 $\widehat h(Z)<c_{E,F}n^2$。
它们的不足不构成实际导出点高度的下界。

更细的缺项在整格上可精确表示：在
$\mathcal O=\mathbb Z_p[\zeta_p]$、$u=\zeta_p-1$ 上，
$\sigma$ 乘 $\zeta_p$，则 $N_G=0$ 而 $D=p/u$。故
\[
Dx\notin p\mathcal O\iff x\notin u\mathcal O,
\]
强于 $x\notin p\mathcal O$；例如 $x=u$ 不可被 $p$ 整除，
但 $Dx=p$。这只检验逻辑缺口，不声称实际 Heegner 点取此值。
还须控制实际点在 $p$-Sylow 增广层的原始性，并保留类群和。
对有理向量 $Y_\ell/n$ 直接套用同一域的整点高度下界是不合法的。

[完整证明和原始来源](../notes/2026-11-12-heegner-height-and-augmentation-primitivity.md)
已由另一位研究者逐式独审，并经根端核对。
该结果尚未证明真实单素数导出点对无穷多个 $p$ 不可整除。
