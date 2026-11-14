# R125. 实际范数一 Heegner 格的统一 Kolyvagin 指数界

日期：2026-11-12。状态：已证明。

完整证明见
[整增广比较与定量界](../notes/2026-11-12-integral-norm-one-kolyvagin-bound.md)。

固定 $E:y^2=x^3-17x$、$F=\mathbb Q(\sqrt{-15})$，令
$p\ge7$、$p\ne17$。令 $\ell$ 在 $F$ 与 $\mathbb Q(i)$
均惰性且 $v_p(\ell+1)=1$，$L/F$ 为环类域 $F[\ell]$ 中
的次数 $p$ 子扩张。设实际点
$$
Q=\operatorname{Tr}_{F[\ell]/L}P[\ell]
$$
非扭。写
$$
A=\ker(\operatorname{Res}_{L/F}E\xrightarrow{N}E),\qquad
\mathcal O=\mathbb Z_p[\zeta_p],\qquad\delta=\zeta_p-1.
$$
由 R119，$\Sha(A/F)$ 有限，且
$A(F)\otimes\mathbb Z_p=\mathcal O w$。令
$$
Q=\delta^a\varepsilon w,\qquad\varepsilon\in\mathcal O^\times.
$$
则存在有限 $\mathcal O$ 模 $M$ 使
$$
\boxed{\quad
\Sha(A/F)[p^\infty]\simeq M\oplus M,\qquad
\operatorname{length}_{\mathcal O}M\le a,\qquad
\operatorname{length}_{\mathcal O}\Sha(A/F)[p^\infty]\le2a.
\quad}
$$

本结论不要求 $p$ 在 $F$ 或 $\mathbb Q(i)$ 分裂，也不要求
$E$ 在 $p$ 普通。局部条件始终是实际 Bloch–Kato／Kummer 条件。

证明在整个整诱导模上构造原始 Heegner 导出类。其 augmentation
由 $N_\Gamma Y_n=0$ 对所有辅助标签严格为零。实际
$\operatorname{Res}_{L/F}E\to A$ 特化先给 leading $\delta Q$；
再利用全局 $H^0(F,A[\delta])=0$ 与多一层精度，唯一除去 $\delta$。
Cartesian 局部条件及辅助位有限、奇异群的实际注入保证除法合法。

有限–奇异比较只使用一个局部可逆矩阵
$\varphi_q\otimes1_{\mathbb Z_p[\Gamma]}$。它与所有精度商和
增广特化交换，无需将局部 Frobenius 误当成全局上同调自同态。
Howard 出版版 Lemma 1.6.4（印页 1454）的两个剩余 case
只需要边的局部消失等价；完整 stub 深度来自同页的低精度归纳
和 $2k-1\to k$ 自由秩一提升像。因此所得指数界是完整的
$\delta$ 长度界，而非仅模 $\delta$ 非零性。

未除增广因子时，同一方法只能给
$\operatorname{length}_{\mathcal O}M\le a+1$。本结果支付并去掉
这个额外的一层，但没有证明 $a=0$。即使与已证局部符号条件
联立，$a=2$ 及非零有限 $\delta$-初级 Sha 仍可能同时存在；
主问题的无穷素数原始性条件尚未由此闭合。

原始来源：Howard, *The Heegner point Kolyvagin system*,
Compositio Math. **140** (2004), 1439–1472，
[出版全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1BF8414258216C1575963BBDA814CB2F/S0010437X04000569a.pdf/the-heegner-point-kolyvagin-system.pdf)，
H.0–H.5、Lemmas 1.6.2–1.6.4、Proposition 1.7.4。
