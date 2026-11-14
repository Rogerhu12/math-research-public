# R109 — 真实高度格与 Gauss 算子把增广长度提高到 (p+3)/2

状态：已证明，独立复核通过；主目标仍未完成。

## 准确结论

固定 $E:y^2=x^3-17x$、$F=\mathbb Q(\sqrt{-15})$。
对每个充分大的目标 $p$，选 R105 的实际辅助素数 $\ell$ 和点
$X_\ell$。对任意阶 $p$ 元 $\sigma\in\operatorname{Gal}(F[\ell]/F)$，
令 $\Delta=\sigma-1$。则
\[
 \Delta^kX_\ell\notin pE(F[\ell])
 \quad(0\le k\le(p+1)/2)
\]
对所有充分大的目标 $p$ 成立。
这是实际点模 $p$ 的 Jordan 长度至少 $(p+3)/2$，
加强了 R107 的约 $\log_2p$ 下界。
同一个结论适用于已完成真实阶二子迹的 $Z_\ell$。

## 证明接口

1. R107 已证 $x=\Delta X_\ell$ 非挠，且全部阿贝尔挠点为 $E[2]$。
   在 $G=E(F[\ell])/\mathrm{tors}$ 中，$V=\mathbb Q[\sigma]x$
   恰为一份 $\mathbb Q(\zeta_p)$，维数 $r=p-1$。
2. $W=G\cap V$ 是饱和格，$L=\mathbb Z[\sigma]x$ 的 $r$ 个共轭基
   各有高度至多 $H_p=4C\log p$。Baker 的统一下界对 $W$ 的全部
   非零点仍有效。Hadamard 与 Minkowski 球界给
   \[
   [W:L]\le\left(\frac{2rH_p}{\pi c}\right)^{r/2},
   \quad a_p=v_p[W:L]
   \le\frac r2\left(1+\frac{\log\log p+O(1)}{\log p}\right).
   \]
3. $W\otimes\mathbb Z_p$ 是 $\mathbb Z_p[\zeta_p]$ 自由秩一格，
   $x$ 的局部赋值恰为 $a_p$；$W/pW$ 注入实际 $G/pG$。
   故对大 $p$，$\bar x$ 的 Jordan 长度为 $p-1-a_p$，
   $\bar X_\ell$ 的长度恰为 $p-a_p$，先得约一半的长度。
4. 实际整数 Gauss 算子 $\mathcal G=\sum_{j=1}^{p-1}(j/p)\sigma^j$
   满足 $\mathcal G^\dagger\mathcal G=p-N$、
   $\mathcal G^2=(-1/p)(p-N)$。
   在范数零格中，$v_{\zeta_p-1}(\mathcal G)=(p-1)/2$，
   且 $\widehat h(\mathcal Gx)=p\widehat h(x)$。
   若 $a_p\ge(p-1)/2$，则 $\mathcal Gx/p$ 确为 $W$ 中非零整点，
   高度为 $\widehat h(x)/p=O(\log p/p)$，与 Baker 下界矛盾。
   因而 $a_p\le(p-3)/2$，得到所列精确半层加强。

## 尚未付清

仍须控制 $Q_{\ell,p}=\operatorname{Tr}_U X_\ell$ 的实际迹，
并达到范数零点所需的最大 $p-1$ 层。
模 $p$，$D_p=-\sigma\Delta^{p-2}$，所以约一半的非零层仍不推出
单素数 Kolyvagin 类非零。没有假设 Heegner 格自由、Sha 有限或完整调节子界。

## 完整证明

[高度格、Gauss 算子与线性增广深度](../notes/2026-11-12-height-lattice-and-linear-augmentation-depth.md)。
两位研究者已分别独立审计饱和性、体积界、局部指数和实际 Gauss 商点。
