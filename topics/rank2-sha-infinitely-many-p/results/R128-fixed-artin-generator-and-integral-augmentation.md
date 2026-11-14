# R128：固定 61 Artin 生成元与完整整数增广像

日期：2026-11-12。**状态：已证明；主目标仍未完成。**

固定
$$
 F=\mathbf Q(\sqrt{-15}),\qquad
 \beta=1+2\sqrt{-15},\qquad \mathfrak b=(\beta),\qquad N\mathfrak b=61.
$$
在 R123/R124 的相对密度一辅助素数选择，以及 R126 不限制
$p$ 约化型的无穷选择中，都可以同时要求
$$
 \operatorname{Gal}(L_{p,\ell}/F)
       =\langle\operatorname{Art}_{L_{p,\ell}/F}(\mathfrak b)\rangle.
 \tag{1}
$$
这保留既有完整 Heegner 迹、两个局部符号及高度结论。

## 坏候选的固定整数证书

写 $\ell+1=pu$、$p\nmid u$。环类核
$\mathbf F_{\ell^2}^{\times}/\mathbf F_\ell^\times$ 经
$x\mapsto x/x^\ell$ 识别为阶 $pu$ 的范数一群；固定主理想
$\mathfrak b$ 的像为 $\beta/\bar\beta$，至多因 Artin 约定倒置。
因此其 $p$ 次商像平凡当且仅当
$\beta^u-\bar\beta^u\equiv0\pmod\ell$。

令 $U_0=0,U_1=1,U_{n+2}=2U_{n+1}-61U_n$，则
$$
 D_n=N(\beta^n-\bar\beta^n)=240U_n^2>0,\qquad D_n\le4\cdot61^n,
 \qquad \log\prod_{n\le V}D_n=O(V^2).
 \tag{2}
$$
所有 $u\le V$ 的坏 $\ell$ 整除这个固定非零整数乘积。
在 R123 中新增损失是 $O(X^{2\theta-2}/\log X)$ 个辅助素数，
只使 $O(X^{\theta-1})=o(X/\log X)$ 个输入可能失败。
在 R126 中新增损失是
$O(Y^{666/1000}/\log Y)=o(Y/\log Y)$。
都可与原坏集合同时删除。任意固定有限组同类主理想也可同时处理。

## 完整整数群上的自同构

对 $A=\ker(N:\operatorname{Res}_{L/F}E\to E)$，
$\Phi_p(\tau)=0$，故 $\mathbf Z[\zeta_p]$ 整作用于 $A$。
若 (1) 中的 Artin 元为 $\tau^k$，$1\le k<p$，则
$$
 u_k(\tau)=1+\tau+\cdots+\tau^{k-1}
$$
为实际 $F$-自同构：取 $kl\equiv1\pmod p$，
其逆为 $\sum_{j=0}^{l-1}\tau^{kj}$，因为乘积模
$\Phi_p(\tau)$ 恰为 $1$。
对平衡算子 $\delta=\tau^{(p-1)/2}(\tau-1)$，于是
$$
 \boxed{(\operatorname{Art}(\mathfrak b)-1)^nA(F)=\delta^nA(F)
                      \quad(n\ge0).}
 \tag{3}
$$
这不是仅在 $p$ 进张量后的结论，并包括挠点。
特别地，原点的 $\delta^2$ 可除性等价于同一个固定 $61$
Artin 差分的平方可除性。

进一步，$[p]=\epsilon\delta^{p-1}$ 中 $\epsilon$ 是整自同构，
故 $A(F)/\delta^nA(F)$ 是有限 $p$ 群，其到 $p$ 进完成商的
映射为同构。因此对实际 $Q=\delta^avw$，
$$
 a\ge n\quad\Longleftrightarrow\quad
 Q\in\delta^nA(F)\quad\Longleftrightarrow\quad
 Q\in(\operatorname{Art}(\mathfrak b)-1)^nA(F).
 \tag{4}
$$

尚未证明原 Heegner 点不在该整数像中；(3) 没有排除 $a=2$，
也不把首局部 jet 或固定素位非零变成全局增广原始性。

完整证明、精确计数与环类映射：
[固定 Artin 生成元笔记](../notes/2026-11-12-fixed-artin-generator-and-integral-augmentation.md)。
