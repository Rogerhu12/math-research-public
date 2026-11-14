# R144 — E389 实际诱导族原始性与准确范数一 Sha 长度

**状态：已证明。日期：2026-11-12。**

## 结论

在 R136、R139、R140 的实际输入下，取充分大的 good ordinary
$p$，$E=389\mathrm a1$，$F=\mathbb Q(\sqrt{-7})$，
$\ell+1=pu$，$p\nmid u a_\ell$。令
$Q=\operatorname{Tr}_{F[\ell]/L}P[\ell]$ 是原非扭完整迹，
$L/F$ 为次数 $p$ 的环类子扩张，$A=\ker\operatorname{Norm}
\operatorname{Res}_{L/F}E$。写
$$
 A(F)\otimes\mathbb Z_p=\mathcal O w,\quad
 Q=\delta^a\varepsilon w,\quad
 \mathcal O=\mathbb Z_p[\zeta_p].
$$
则 R139 的同一个原始有限诱导族模 $\delta$ 非零，并且
$$
 \Sha(A/F)[p^\infty]\simeq M\oplus M,\qquad
                   \operatorname{length}_{\mathcal O}M=a+1.
$$
不要求 $p$ 在 $F$ 分裂。原族最小的模 $\delta$ 非零辅助
数目准确为
$$
 \nu_p=\operatorname{rank}E(\mathbb Q)
           +\dim_{\mathbb F_p}\Sha(E/\mathbb Q)[p]-1.
$$
此处是模 $p$ 的维数；全 $p^\infty$ 版本应改用 Sha 余秩。

## 完整证明所在及核心步骤

[完整证明](../notes/2026-11-12-noncm-primitive-induced-system-and-exact-length.md)。

1. Zhang（2014）Theorem 1.1 的全部条件在 E389 上成立：
   $N=389$ 是 Heegner 平方自由导子，$I_1$ 的最小判别式
   估值为一支付剩余分歧；其结论不要求 $p$ split $F$。
2. R139 的实际 Kummer 图给逐节点准确式
   $\overline c_n^A=-a_\ell\overline c_n^{E,\mathrm{raw}}$。
   因 $a_\ell$ 为单位，原曲线的非零模 $p$ 分量传入同一个
   诱导族。辅助 $q$ inert $F$ 自动在二面体 $L/F$ 分裂。
3. 完整证明 §4 不假定 $A$ 有全局 correction。它从 Howard
   已证 Selmer 四角图，证明任意 stub 平移的局部零性等价；
   至多四个剩余类的高精度 Chebotarev 使 core 图连通。
   实际局部自同构 $-q\varphi_q^{-1}$ 保持所有 $\delta$ 深度，
   从而非 core 归纳给
   $\mathcal O c_n^{(k)}=\delta^d\mathcal S_k(n)$，其中 $d$
   独立于节点、精度。剩余非零迫 $d=0$。
4. 首项是 $(\tau-1)Q$，其真实自由格指数为 $a+1$。
   在任意大的精度应用上一步得准确长度等式。
5. Zhang Lemma 8.4 的原族三角化和上述逐节点比较给 $\nu_p$
   公式。故整族原始性没有支付原 $Q$ 的两步原始性。

## 对主问题的范围

R139 的 $a\le1$ 充分条件保持有效，仍能推出
$\operatorname{rank}E(\mathbb Q)=2$ 及 $\Sha(E/\mathbb Q)[p^\infty]=0$。
本结论将此前 $2(a+1)$ 上界提升为同一原族的准确值；没有
证明无穷多个 $p$ 有 $a\le1$。不能整体再除 $\delta$，因为
原族已经有已证明非零的剩余分量。

## 文献

- W. Zhang, *Selmer groups and the indivisibility of Heegner points*,
  Cambridge J. Math. 2 (2014), Theorem 1.1、Lemma 8.4、Theorem 11.2；
  [正式全文](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2014/0002/0002/CJM-2014-0002-0002-a002.pdf)。
- B. Howard, *The Heegner point Kolyvagin system*, Compositio Math.
  140 (2004), §1.5–1.7；
  [正式全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1BF8414258216C1575963BBDA814CB2F/S0010437X04000569a.pdf/the-heegner-point-kolyvagin-system.pdf)。
- A. Burungale–F. Castella–G. Grossi–C. Skinner,
  *Non-vanishing of Kolyvagin systems and Iwasawa theory*（2026），
  Lemma 2.2.4 的严格族参照；本文弱族证明另已完整给出。
