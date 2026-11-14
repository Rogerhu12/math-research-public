# R18. 最低层有理化与固定代数数的 Frobenius–Fermat quotient

**状态：已证明。** 日期：2026-11-12。会话：Astra-rank2-Sha / cm_iwasawa_routes。

本结果继续 [R17](R17-cm-prime-diagonal-four-layer-reduction.md)，证明其最低层 $R(t)$ 实际上是固定有理函数，并将 $b_0(p)/p$ 精确写成一个固定代数数的 Frobenius–Fermat quotient 的 trace。其余三层仍未因此消失，故没有完成无穷素数目标。

## 1. 固定域与结论

沿用 R6、R17 的
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
f=34(1+i),\quad P_f=(u,v),\quad F=K(E_f)=K(u).
$$
令
$$
\alpha=\frac vu,
\qquad M=K(\alpha).
$$
则 $[F:M]=2$，且在已知 $[F:K]=256$ 的记号下 $[M:K]=128$。有
$$
\operatorname{Tr}_{M/K}\alpha=0,
\tag{1}
$$
以及 R17 中的精确函数等式
$$
\boxed{\quad
R(t)=\operatorname{Tr}_{M/K}
\left(\frac{\alpha}{1-\alpha^2t^2}\right)\in K(t).
\quad}
\tag{2}
$$
因此对每个奇素数 $p$，
$$
\boxed{\quad b_0(p)=\operatorname{Tr}_{M/K}(\alpha^p).\quad}
\tag{3}
$$
域 $M/K$ 在 $2,17$ 外不分歧，$\alpha$ 在这些素数以外的每个素位都是单位。对 good split $p$，选择 $\mathfrak p\mid p$，令 $\sigma_{\mathfrak p}\in\operatorname{Gal}(M/K)$ 为算术 Frobenius。则
$$
\mathcal F_{\mathfrak p}(\alpha)
=\frac{\alpha^p-\sigma_{\mathfrak p}(\alpha)}p
\tag{4}
$$
在 $M$ 的每个 $\mathfrak p$-上方素位都 integral，并且
$$
\boxed{\quad
\frac{b_0(p)}p
=\operatorname{Tr}_{M/K}\mathcal F_{\mathfrak p}(\alpha).
\quad}
\tag{5}
$$
这是一个固定域、固定代数数上的准确等式。它只处理四层中的第一层。

## 2. Galois involution 是 $P\mapsto T-P$

令 $T=(0,0)$。在复均匀化中，$T$ 对应 $\Omega_\infty/(1+i)$，所以
$$
T=[34]P_f.
\tag{6}
$$
对于 $\ell=3,11$，曲线有 good reduction，且 $\ell\equiv3\pmod4$。将有限域求和中的 $x$ 与 $-x$ 配对，可见 $a_\ell(E)=0$。因此 $\mathbb F_\ell$-Frobenius 的平方为 $[-\ell]$；$K$ 中素理想 $(\ell)$ 的 Frobenius 在 prime-to-$\ell$ torsion 上作用为 $[-\ell]$。两者相乘，得到 $\operatorname{Gal}(F/K)$ 中作用为 $[33]$ 的元素 $\tau$。

由式 (6)，
$$
\tau P_f=[33]P_f=T-P_f.
$$
其平方是恒等作用，因为 $33^2-1=1088$ 可被 $f$ 整除；它非恒等，因为 $32$ 不可被 $f$ 整除。加法公式给出
$$
u^\tau=-\frac{17}{u},\qquad
v^\tau=-\frac{17v}{u^2},\qquad
\alpha^\tau=\alpha.
\tag{7}
$$
又因
$$
u^2-\alpha^2u-17=0,\qquad v=\alpha u,
$$
可知 $[F:M]\le2$。$\tau$ 非平凡且固定 $\alpha$，故恰有 $[F:M]=2$，$M=F^{\langle\tau\rangle}$。

域 $F/K$ 是阿贝尔扩张：Galois 作用与定义在 $K$ 上的 $\mathbb Z[i]$-作用交换，而 $E[f]$ 是秩一的 $\mathbb Z[i]/f$-模。因此 $M/K$ 也是阿贝尔扩张，各个 $\tau$-pair 正好由 $\operatorname{Gal}(M/K)$ 标记。

## 3. CLS 的 $n=1$ trace 公式给出零 trace

记 $E_1^*(z,\Lambda)$ 为奇的、双周期的 Eisenstein–Kronecker 一阶函数。它由 Weierstrass $\zeta$ 函数减去相应实线性的准周期修正得到，因此仍满足加法公式
$$
E_1^*(z+w)=E_1^*(z)+E_1^*(w)
+\frac{\wp'(z)-\wp'(w)}{2(\wp(z)-\wp(w))}.
\tag{8}
$$
在非零 $2$-torsion 点 $T$，奇性与周期性给出 $E_1^*(T)=0$。取 $z=P_f,w=T$，式 (8) 变成
$$
E_1^*(P_f+T)=E_1^*(P_f)+\alpha.
$$
由于 $P_f+T=-\tau P_f$，再用奇性可得
$$
E_1^*(P_f)+E_1^*(\tau P_f)=-\alpha.
\tag{9}
$$

这里的 torsion 值与 Galois 作用相容。为明确这一点，可取任意整数 $N$ 杀掉 $P_f$，如 $N=2312$，并取标准 $N$-division 函数 $\Psi_N$。其非零 $N$-torsion 零点都是单零点，而
$$
N\zeta(Nz)-N^2\zeta(z)=\frac{d}{dz}\log\Psi_N(z).
$$
此恒等式也可直接比较两边的极点、留数和奇性得到。在 $z=z_0$、$Nz_0=\lambda\in\Lambda$ 处比较常数项，得到
$$
E_1^*(z_0)
=-\frac{1}{2N^2}
\frac{\delta^2\Psi_N(P)}{\delta\Psi_N(P)},
\qquad P=(\wp(z_0),\wp'(z_0)/2).
\tag{10}
$$
分母非零，因为 $\Psi_N$ 在 $P$ 为单零点。右侧是定义在 $K$ 上的有理表达式，且 $\delta x=2y,\delta y=3x^2-17$ 也定义在 $K$ 上，所以 $E_1^*(\tau P_f)=\tau E_1^*(P_f)$。

现在使用准确的外部输入：Coates–Liang–Sujatha，*The Tate–Shafarevich group for elliptic curves with complex multiplication*（2009），Theorem 2.3、式 (24) 在 $n=1$ 的情形；单位数因子按 CLS II（2010）§4 的勘误删除。其公式为
$$
\operatorname{Tr}_{F/K}E_1^*(P_f)
=\frac{f}{\Omega_\infty}L_{\mathfrak f}(\overline\psi_E,1).
\tag{11}
$$
来源：[2009 原文](https://arxiv.org/abs/0901.3832)、[2010 勘误所在原文](https://arxiv.org/abs/1005.4206)。这里只用右侧为零，故旧文本的单位数误因子也不会改变这个零性结论。

R4 已证明 $E(\mathbb Q)$ 的秩为 $2$。若 $L(E,1)\ne0$，解析秩零定理将给出代数秩零，与 R4 矛盾；故 $L(E,1)=0$。本曲线的 Hecke $L$ 函数与 $L(E,s)$ 相同，$\psi_E$ 与 $\overline\psi_E$ 的 $L$ 函数也相同，而 $\mathfrak f$ 就是其导子，所以式 (11) 的右侧为零。

对式 (9) 取 trace 得
$$
\operatorname{Tr}_{F/K}\alpha
=-2\operatorname{Tr}_{F/K}E_1^*(P_f)=0.
$$
因 $[F:M]=2$，得到式 (1)。这一步使用的是已证明的解析秩零蕴含代数秩零，没有假设秩 $2$ 的 BSD 或 Sha 有限性。

## 4. 配对后平方根项恰好消失

R17 的定义是
$$
R(t)=\frac1{s(t)}\operatorname{Tr}_{F/K}\frac{v}{x(t)-u},
\quad s^2=1+68t^4,
\quad x(t)=\frac{1+s}{2t^2}.
$$
对每一对 $(u,v),(u^\tau,v^\tau)$，代入式 (7) 并化简，得到
$$
\frac1s\left(
\frac{v}{x-u}+\frac{v^\tau}{x-u^\tau}
\right)
=\frac{\alpha}{1-\alpha^2t^2}-\frac{\alpha}{s}.
\tag{12}
$$
计算中只用到
$$
u+u^\tau=u-17/u=\alpha^2,
\qquad v/u=v^\tau/u^\tau=\alpha.
$$
将式 (12) 对 $\operatorname{Gal}(M/K)$ 求和：
$$
R(t)=\operatorname{Tr}_{M/K}\frac{\alpha}{1-\alpha^2t^2}
-\frac{\operatorname{Tr}_{M/K}\alpha}{s(t)}.
$$
第二项由式 (1) 消失，得到式 (2)。展开几何级数，
$$
R(t)=\sum_{m\ge0}\operatorname{Tr}_{M/K}(\alpha^{2m+1})t^{2m},
$$
取 $2m=p-1$ 即得式 (3)。这里有理化的是 R17 的辅助最低层，并非 R13 所排除的整条 $a_n$ 序列。

## 5. $\alpha$ 不引入新的坏素数

取任意有理素数 $p\nmid34$ 及 $F$ 的一个 $p$-上方素位。曲线在该处有 good reduction，且 $p\nmid\mathrm N(f)$。因此 $f$-torsion 的约化映射单射，且该 torsion 扩张不分歧。

点 $P_f$ 不约化到无穷远点，否则单射性会迫使 $P_f=O$。故 $u,v$ 均在该处 integral。若 $u$ 的约化为 $0$，点的约化就是 $(0,0)$；若 $v$ 的约化为 $0$，约化点也是 $2$-torsion。这两种情形都使 $[2]P_f$ 约化为 $O$，再用 prime-to-$p$ torsion 约化的单射性，得到 $[2]P_f=O$，矛盾。因此 $u,v$ 均为单位，$\alpha=v/u$ 亦为单位。

这对每个 $p\nmid34$ 及每个上方素位成立，所以
$$
\alpha\in\mathcal O_M[1/34]^\times.
\tag{13}
$$
特别地，$\mathrm N_{M/K}(\alpha)$ 的非零赋值只能位于 $2,17$ 上方，不会给目标的 good split 素数增加额外排除。上述有限 étale torsion 论证也说明 $F/K$，从而 $M/K$，在这些素数以外不分歧。

## 6. Frobenius quotient 的 trace

现取 $p\equiv1\pmod4$、$p\ne17$ 和 $\mathfrak p\mid p$。因为 $M/K$ 阿贝尔且在 $\mathfrak p$ 不分歧，同一个算术 Frobenius $\sigma_{\mathfrak p}$ 在每个上方素位都诱导 $p$ 次幂映射。由式 (13)，
$$
\alpha^p\equiv\sigma_{\mathfrak p}(\alpha)\pmod{\mathfrak P}
\quad(\mathfrak P\mid\mathfrak p).
$$
这些扩张不分歧，且 $p$ 在 $K_{\mathfrak p}$ 的赋值为 $1$，因此式 (4) 的商在所有这些素位 integral。利用 trace 的 Galois 不变性及式 (1)，
$$
\operatorname{Tr}_{M/K}\mathcal F_{\mathfrak p}(\alpha)
=\frac{\operatorname{Tr}_{M/K}\alpha^p
-\operatorname{Tr}_{M/K}\sigma_{\mathfrak p}\alpha}{p}
=\frac{b_0(p)}p.
$$
这证明式 (5)，也独立解释了 R17 最低层的 $\mathfrak p$ 整除性。

特别地，可限于在固定域 $M$ 的一个固定 Galois 闭包中完全分裂的有理素数。Chebotarev 定理给出无穷多个这样的素数，且它们在 $K$ 中也分裂。在此固定素数集合上，$\sigma_{\mathfrak p}=1$，所以
$$
\frac{b_0(p)}p
=\operatorname{Tr}_{M/K}
\left(\alpha\frac{\alpha^{p-1}-1}{p}\right).
\tag{14}
$$
这才是通常的固定代数底数 Fermat quotient；没有把随 $p$ 变化的 Frobenius 生成元当成固定底数。

## 7. 三个高层与秩 $2$ 条件仍然保留

若 $p=4r+1$，记
$$
T_{p,j}(X)=\sum_{k=0}^{r-1}[t^{4k}]L(t)^j\,X^{4k}.
$$
由式 (2) 和 $L\in t^4\mathbb Q[[t^4]]$，可精确写成
$$
b_j(p)=\operatorname{Tr}_{M/K}
\left(\alpha^p T_{p,j}(\alpha^{-1})\right),
\qquad j=0,1,2,3.
\tag{15}
$$
本来可能出现的 $k=r$ 项乘上 $\operatorname{Tr}\alpha=0$，所以已删除；保留下来的分母均为 $p$-adic 单位。对 $j=0$，$T_{p,0}=1$，与式 (3) 一致。

式 (15) 是有限截断求值，不能擅自换成 $L(\alpha^{-1})^j$。由式 (13)，$\alpha^{-1}$ 在所有目标素位都是单位，不在形式对数的自动收敛圆盘 $p\mathcal O$ 中。更不能将椭圆曲线上 torsion 点的全局 $p$-adic 对数为零，直接解释成这些截断级数求值为零。

R17 的秩 $2$ 整除性现在表示为
$$
\operatorname{Tr}_{M/K}\mathcal F_{\mathfrak p}(\alpha)
\equiv b_1(p)\pmod{\mathfrak p}.
\tag{16}
$$
这确实把最低两层的一阶相消写成了固定底数 Frobenius quotient 与一个椭圆对数截断的比较。但所需的剩余条件仍是
$$
\frac{b_0(p)-p b_1(p)}{p^2}
+\frac{b_2(p)}2-\frac{p b_3(p)}6
\not\equiv0\pmod{\mathfrak p^2}
$$
对无穷多个 $p$ 成立。Chebotarev 只在式 (14) 中固定了 Frobenius 置换；它没有证明这个由后三层参与的同余式非零，也没有排除 Fermat quotient trace 的相消。
