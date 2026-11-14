# 固定分母范数消去了目标的奇字符；正确加权对象仍需 p-torsion

**可信度：以下范数、字符及辅助理想比较均已证明。** 日期：2026-11-12。本文继续 R31 和 norm-one/high-jet 笔记，定位固定单位接口中实际丢失的信息，并把辅助理想 $(67)$ 的正确 $\chi$-加权式写出。

## 1. 固定域与 p-除法域线性无交

设
$$
L_p=K(E[\mathfrak p]),\qquad
\Delta_p=\operatorname{Gal}(L_p/K),\qquad
p\ge13,\quad p\equiv1\pmod4,\quad p\ne17.
$$
局部 Lubin–Tate 理论给出 $[L_p:K]=p-1$，且 $\mathfrak p$ 在这个扩张中完全分歧。也可先观察全局 Galois 作用嵌入
$(\mathcal O_K/\mathfrak p)^\times$，再用局部完全分歧的 $p-1$ 阶惯性作用证明其像恰为全群。

R18 的固定 $F=K(E[\mathfrak f])$，从而 $M\subset F$，在 $\mathfrak p$ 处不分歧。因此
$$
F\cap L_p=K,\qquad M\cap L_p=K.
\tag{1}
$$
确实，交域同时是 $L_p/K$ 的完全分歧子扩张和一个不分歧扩张，只能平凡。于是可在复合域中让 $\Delta_p$ 固定 $F$，而在所有非零 $\mathfrak p$-torsion 点上作通常的乘法作用。

取 $P_\pi$ 为一个非零 $\mathfrak p$-torsion 点，令
$$
\rho=t(P_\pi),\qquad t=-1/X,
$$
并令 $\widetilde\chi:\Delta_p\to\mu_{p-1}\subset\mathbb Z_p^\times$ 为 R16/R21 的 Teichmüller 提升。特别地
$\widetilde\chi(-1)=-1$。

## 2. D_p(alpha) 正好是一个普通范数

R31 的 $D_p(X)$ 在 $X$ 线上有 $p-1$ 个不同的根，正是
$X(Q)$，$0\ne Q\in E[\mathfrak p]$。同一个 $X$ 值的两个点由
$P\mapsto T-P$ 配对；该映射把 $\mathfrak p$-核送到核的 $T$ 平移，故在非零核内部不会合并两个不同点。$D_p(0)=1$ 因而给出准确乘积式
$$
\boxed{\quad
D_p(X)=\prod_{0\ne Q\in E[\mathfrak p]}
\left(1-\frac{X}{X(Q)}\right).
\quad}
\tag{2}
$$
因为 $t(Q)=-1/X(Q)$，在固定 $\alpha$ 处，
$$
\boxed{\quad
D_p(\alpha)=
\mathrm N_{M L_p/M}(1+\alpha\rho).
\quad}
\tag{3}
$$
因此 R31 的固定单位 $w$，以及去掉有理分量后的固定 norm-one 单位 $u$，控制的是这个普通范数的值。

核点按 $Q,-Q$ 配对，所以 $D_p(-X)=D_p(X)$。于是
$$
\varepsilon_{\alpha,p}
=\frac{1+\alpha\rho}{1-\alpha\rho}
$$
满足
$$
\boxed{\quad
\mathrm N_{M L_p/M}\varepsilon_{\alpha,p}
=\frac{D_p(\alpha)}{D_p(-\alpha)}=1.
\quad}
\tag{4}
$$
而原来的固定函数给出
$$
\Phi(P_\pi)=\mathrm N_{M L_p/L_p}\varepsilon_{\alpha,p}.
\tag{5}
$$
式 (4) 是准确恒等式；它不是因目标单位为零或微小而成立的估值条件。

## 3. 被消去的正是 p-tame 的非平凡字符

在 $p$-进完成的单位群中用加法记号，普通范数算子为
$$
\sum_{\sigma\in\Delta_p}\sigma=(p-1)e_{\mathbf1}.
$$
它只保留平凡字符。在任意非平凡字符块上为零，特别包括目标的奇字符 $\widetilde\chi$。

此外 $u,w,D_p(\alpha)$ 都在固定域 $M$ 中，$\Delta_p$ 固定它们，所以
$$
e_\chi\log_pu=e_\chi\log_pw
=e_\chi\log_pD_p(\alpha)=0
$$
在复合局部域中成立。固定域内的 Galois 共轭、普通迹和对数都与 $\Delta_p$ 作用交换，不能仅靠这些操作把已消去的 $\chi$ 分量恢复出来。

这不是对任何可能比较公式的“不存在定理”：原同源和原单位之间仍可能存在额外的算术关系。但是 R31 的范数恒等式本身没有包含目标奇字符。尤其不能由固定 $u$ 的一个浅 Fermat quotient，未经额外比较就推出原 $\Phi(P_\pi)$ 的 $\chi$ 深度小。

## 4. 正确的加权 resolvent

必须保留的对象可以准确写成一个 $\chi$-加权对数。令
$$
\mathcal R_{p,\chi}(\alpha)
=e_\chi\log_p(1+\alpha\rho)
=\frac1{p-1}\sum_{\sigma\in\Delta_p}
\widetilde\chi(\sigma)^{-1}
\log_p(1+\alpha\,\sigma\rho).
\tag{6}
$$
$\alpha$ 在目标素位为单位，而 $\rho$ 有正赋值，所以这些对数收敛。取 R21 的
$$
\rho_\chi=e_\chi\rho,
$$
它是非零的 $\chi$ 本征向量，局部均匀化赋值为一。由于 $-1$ 把 $\rho$ 送到 $-\rho$，奇性给
$$
e_\chi\log_p(1-\alpha\rho)
=-e_\chi\log_p(1+\alpha\rho).
$$
因此 R21 的目标标量准确为
$$
\boxed{\quad
\mathcal Q_p
=\frac{e_\chi\log_p\Phi(P_\pi)}{\rho_\chi}
=2\operatorname{Tr}_{M/K}
\left(\frac{\mathcal R_{p,\chi}(\alpha)}{\rho_\chi}\right).
\quad}
\tag{7}
$$
与 (3) 相比，(6) 保留了全部 Teichmüller 权，而不是把它们全部改成一。它至少需要一个 $\mathfrak p$-torsion 本征方向（这里用 $P_\pi$ 与 $\rho_\chi$ 明确选出）；这个方向不位于固定、不分歧的 $M$ 中。

式 (7) 没有把困难换成一个“已知固定数”：$\mathcal R_{p,\chi}$ 正是普通范数丢掉的那一块。在本方法中，若希望把它进一步改成固定数域数据，必须额外构造保持这个 $\chi$ 权的比较，而不能仅援引 (3)。

## 5. 辅助67在正确字符块上的准确结果

令
$$
\mathfrak a=(67),\quad a=-67,\quad A=4489,
\qquad P=P_f+P_\pi.
$$
R31 的准确函数恒等式为
$$
\frac{\Theta_{\mathfrak a}([\pi]P)}
{\Theta_{\mathfrak a}(P)^p}
=
\frac{\Theta_{(\pi)}([a]P)}
{\Theta_{(\pi)}(P)^A}.
\tag{8}
$$
在这里
$$
[\pi]P=\sigma_{\mathfrak p}P_f,\qquad
[a]P=P_f+[a]P_\pi,
$$
因为 $[a]P_f=P_f$。$\Theta_{\mathfrak a}(\sigma_{\mathfrak p}P_f)$ 属于固定 $F$，故其 $\chi$ 投影准确为零。对 (8) 取局部对数及 $e_\chi$，得到
$$
\boxed{\quad
-p\,e_\chi\log_p\Theta_{\mathfrak a}(P_f+P_\pi)
=
\bigl(\widetilde\chi(a)-A\bigr)
e_\chi\log_p\Theta_{(\pi)}(P_f+P_\pi).
\quad}
\tag{9}
$$
其中
$$
\widetilde\chi(a)-A\equiv-4556=-4\cdot17\cdot67\pmod p
$$
在全部目标素数处为单位。

所有对数均合法。$\Theta_{\mathfrak a}$ 的混合 torsion 值有复合导子 $\mathfrak f\mathfrak p$，是全局单位。对于 $\Theta_{(\pi)}(P_f+P_\pi)$，可直接由 R31 的定义核对局部单位性：非零核点 $Q$ 满足
$v_p(x(Q))=-2/(p-1)$，而 $P_f+P_\pi$ 约化为非零的 $P_f$，$x$ 值整。乘积中每个差的赋值因此为 $-2/(p-1)$；$p-1$ 个因子及指数 $-6$ 共给赋值 $12$，恰好抵消前面的 $\pi^{-12}$。其余判别式因子为单位。

式 (9) 表明：正确取 $\chi$ 权以后，原先固定的 $\Theta_{\mathfrak a}(\sigma P_f)$ 项消失，留下的是两个仍在混合导子场中的单位。辅助恒等式没有把该字符分量送回固定域。

## 6. 再取 f-orbit 迹恰好返回原来的未知量

定义
$$
\Lambda_{\mathfrak b}(R)
=\prod_{\sigma\in\operatorname{Gal}(F/K)}
\Theta_{\mathfrak b}(R+P_f^\sigma).
$$
将 (9) 对 $F/K$ 求和，得到
$$
e_\chi\log_p\Lambda_{(\pi)}(P_\pi)
=-\frac{p}{\widetilde\chi(a)-A}
e_\chi\log_p\Lambda_{\mathfrak a}(P_\pi).
\tag{10}
$$

R19 的除子证明适用于这个固定辅助理想：$[a]$ 置换（此处甚至固定）两个导子 orbit，并且在 $O$ 处两边的比值为一。所以
$$
\frac{\Lambda_{\mathfrak a}(R)}
{\Lambda_{\mathfrak a}(-R)}
=
\left(\frac{\Phi([a]R)}{\Phi(R)^A}\right)^{12}.
$$
取奇字符分量后，
$$
e_\chi\log_p\Lambda_{\mathfrak a}(P_\pi)
=6(\widetilde\chi(a)-A)
e_\chi\log_p\Phi(P_\pi).
\tag{11}
$$
代入 (10) 得
$$
\boxed{\quad
e_\chi\log_p\Lambda_{(\pi)}(P_\pi)
=-6p\,e_\chi\log_p\Phi(P_\pi).
\quad}
\tag{12}
$$
也可直接用相同除子恒等式的辅助理想 $(\pi)$ 版本：因为 $[\pi]P_\pi=O$、$\Phi(O)=1$，其右侧成为
$\Phi(P_\pi)^{-12p}$，奇字符投影正好给 (12)。

因此，保留正确字符以后，辅助67路线准确回到原 $\Phi$ 的同一个未知分量，只增加一个可见的 $p$ 因子。这个等式是一条确切的比较，但不是新的非零来源；它没有用固定 $u$ 的普通范数数据替代原问题。

## 7. 这条路线的当前边界

目前得到的两类对象应区分：

- 固定 $u\in M^\times$ 的 Frobenius quotient，准确控制 $D_p(\alpha)$ 的普通范数部分；其未加权 trace 已在前篇化为底数 $2$，norm-one 部分的普通 trace 为零。
- 保留 $\widetilde\chi$ 权的 resolvent (6)，准确给出原目标的标量 (7)；通过辅助67及导子 orbit 求和，只得到 (12)，没有得到固定域中的新非零量。

若下一步要继续这条方向，真正需增加的是保持 $\chi$ 的额外比较或非零信息，例如一个带该本征方向的 Gauss resolvent、相应的导出单位或所需高 jet 配对。当前没有证明它们能由固定有限个数域单位的值重建，也没有证明目标对无穷多个 $p$ 成功。

## 依赖

- R16、R21：局部 Lubin–Tate 塔、目标字符与 $\rho_\chi$。
- R18：固定域在目标素位不分歧。
- R19、R31：固定 $\Phi$、Theta 的准确辅助交换式及除子规范。
- R29 与 Padé 桥：$D_p$ 的次数、根和规范化。
- 本文已给出范数的精确识别、奇字符消去及正确加权辅助式的完整推导。
