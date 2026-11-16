# R271 附录：同一物理低孔测试的直接 Chebyshev 核逼近与全部中间 Gram

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本文直接比较原有限头模型的 $V_{m,Q}$、$K_{m,Q}$ 和同一个实际 $u_f=(P_{V_{m,Q}}-P_{K_{m,Q}})f$。不引入强前缀或额外远池，不把完整 inverse 换成其低源压缩，也不要求某个 MP 与头相似交换。

固定头相似到齐次后，两个真实子空间在低 total grade 完全一致。全部高低源反馈保留在 $V$ 上的完整正 Gram 中。其有限带宽给出一个已经属于原 $K_{m,Q}$ 的多项式候选，并有无额外条件数前因子的相对能量界：
$$
\|(P_{V_{m,Q}}-P_{K_{m,Q}})f\|
\le
\frac{2\rho_m^\nu}{1+\rho_m^{2\nu}}\,
\|P_{V_{m,Q}}f\|,
\qquad
\nu=\left\lfloor\frac{Q-s}{d-1}\right\rfloor,
$$
其中 $f$ 的原尾孔数不超过 $s$，$\rho_m=(\kappa_m-1)/(\kappa_m+1)$，$\kappa_m$ 是实际头相似条件数。

该结论对同一个 $m$ 的所有尾权和所有低孔 forcing 同时成立。代入已付原头相似，可把直接模型窗口的 $\log Q$ 主项取为 $35d^4/6$，无需相干塔方案中的 $\log x=12d^4$。原 $T$ 的真实 carry 修复及同 $w$ 导数仍未由此付清，见 §6。

已付依据与本稿区别：

- [真实头 Jordan 相似及纯分级形式像](R239-appendix-true-head-jordan-cost-and-pure-graded-formal-range.md)，提供原 N/Y 头及齐次化范围；
- [固定头条件数与全部源普通右旗窗口收敛](R271-appendix-fixed-head-condition-and-uniform-window-convergence.md)，已对 $\lambda_h/\lambda_\infty$ 证明带状完整 Gram 与 Chebyshev 证书；本稿复用该方法，新增对象是原 $V_Q/K_Q$ 差对固定低孔测试的直接界；
- [缩放真实头与同源 Chebyshev 能量](R271-appendix-scaled-head-similarity-chebyshev-source-energy-and-moving-model-window.md)，§§1--2 给出本稿采用的明确物理条件数，§6 保原母提升全部双侧头幂。

## 1. 原算子、cut 与完整物理相似

先在一般有限头加纯尾模型上证明。头空间 $\mathfrak h$ 维数为 $d\ge2$，设 $A$ 与一个按头 grade $0,\ldots,d-1$ 恰降一阶的带权 Jordan 头 $J$ 相似：
$$
A S=S J,\qquad S:\mathfrak h\longrightarrow\mathfrak h
\quad\hbox{有界可逆}.
$$
尾空间按原孔数正交分解
$$
\mathcal H_{\rm tail}=\bigoplus_{p\ge0}\mathcal H_p,\qquad
D\mathcal H_p\subset\mathcal H_{p-1},
$$
并设 $D$ 有界。原连续尾 $D_m=\sum_{i\ge m}(i+1)^{-2}E_i$ 满足此条件。定义
$$
L=A+D,\qquad L^0=J+D,\qquad
\mathcal S=S\otimes I,\qquad L\mathcal S=\mathcal S L^0.
\tag{1.1}
$$
$\mathcal S$ 与每个原尾孔数投影交换。全部算子和方程在原 Hilbert 空间中有界；本稿没有无界 MP 域的省略。

对整数 $Q\ge0$，令 $\Pi_{\le Q}$、$\Pi_{<Q}$ 为尾孔数 cut，准确使用
$$
V_Q=\{v:\Pi_{\le Q}v=v,\ \Pi_{<Q}Lv=0\},
\qquad
K_Q=\{v:\Pi_{\le Q}v=v,\ Lv=0\}.
\tag{1.2}
$$
两者均闭，且 $K_Q\subset V_Q$。这是原左可行空间和同一 cut 的完整真核；$K_Q$ 包含所有真零源，并非只取一个相干或 primitive 子族。

记
$$
V_Q^0=\mathcal S^{-1}V_Q,\qquad K_Q^0=\mathcal S^{-1}K_Q.
$$
由 (1.1) 及 $\mathcal S$ 与 cut 交换，二者正是把 (1.2) 的 $L$ 换为 $L^0$ 所得的原式。

令
$$
\kappa=\|S\|\|S^{-1}\|\ge1,\qquad w=d-1.
$$
把 $S$ 乘正标量，使最小奇异值为 $1$。于是
$$
I\preceq \mathcal G=\mathcal S^*\mathcal S\preceq\kappa^2I.
\tag{1.3}
$$
这一步只归一整个相似的标量；没有将非酉物理度量删掉。

## 2. 两个真实空间在低 total grade 一致

给相似后的头基向量 $e_i$ 赋 grade $i$。令 $\mathcal P_\ell$ 为
$$
\ell=\text{头 grade}+\text{原尾孔数}
$$
的正交投影。$L^0$ 恰降 total grade 一阶，而原尾 cut 与所有 $\mathcal P_\ell$ 交换。因此 $V_Q^0$ 和 $K_Q^0$ 都是这个 total grade 的约化子空间，其正交投影也保每个 grade。

准确有
$$
\boxed{
V_Q^0\cap\operatorname{Ran}\mathcal P_{\le Q}
=
K_Q^0\cap\operatorname{Ran}\mathcal P_{\le Q}.
}
\tag{2.1}
$$
证明：若 $v$ 的 total grade 不超过 $Q$，则它的尾孔数也不超过 $Q$；$L^0v$ 的 total grade 不超过 $Q-1$，从而所有输出尾孔数都小于 $Q$。故 $\Pi_{<Q}L^0v=0$ 已经是完整的 $L^0v=0$。反向包含由 $K_Q^0\subset V_Q^0$ 得到。

此外，$\mathcal G$ 只改头 grade，所以在 total grade 上的带宽不超过 $w$。记 $P_E$ 为 $E=V_Q^0$ 的正交投影，在整个闭空间 $E$ 上定义
$$
G_E=P_E\mathcal G|_E.
\tag{2.2}
$$
则
$$
\boxed{
I_E\preceq G_E\preceq\kappa^2I_E,\qquad
G_E\text{ 的 total-grade 带宽不超过 }w.
}
\tag{2.3}
$$
因为 $P_E$ 严格保 grade，压缩没有增加带宽。全部 $V_Q^0$ 的高层、低层和中间 nuisance 都在 (2.2) 中；没有先压到 forcing 的支持上再取 inverse。

## 3. 完整 Riesz 最小者与有限传播候选

设原物理 forcing 满足
$$
\Pi_{\le s}f=f,\qquad 0\le s\le Q-w.
\tag{3.1}
$$
头部可以是全部 $d$ 维的任意向量；尾位置支撑也可以无限。记
$$
v=P_{V_Q}f,\qquad u=(P_{V_Q}-P_{K_Q})f.
$$
相似后的真正完整 Riesz 方程为
$$
b=P_E\mathcal S^*f,\qquad
a=G_E^{-1}b,\qquad v=\mathcal Sa.
\tag{3.2}
$$
因 $\mathcal S^*$ 只改头，$\mathcal S^*f$ 的 total grade 不超过 $s+w$；$P_E$ 保 grade，因此
$$
\mathcal P_{\le s+w}b=b.
\tag{3.3}
$$
并且
$$
\|v\|^2=\langle G_E^{-1}b,b\rangle.
\tag{3.4}
$$

先设 $\kappa>1$，置
$$
\rho=\frac{\kappa-1}{\kappa+1},\qquad
a_\nu=\frac{2\rho^\nu}{1+\rho^{2\nu}},\qquad
\nu=\left\lfloor\frac{Q-s}{w}\right\rfloor\ge1.
\tag{3.5}
$$
令 $\mathsf T_\nu$ 为 Chebyshev 多项式，定义
$$
r_\nu(t)=
\frac{\mathsf T_\nu((\kappa^2+1-2t)/(\kappa^2-1))}
{\mathsf T_\nu((\kappa^2+1)/(\kappa^2-1))},
\qquad
p_{\nu-1}(t)=\frac{1-r_\nu(t)}t.
\tag{3.6}
$$
$r_\nu(0)=1$，所以 $p_{\nu-1}$ 是次数至多 $\nu-1$ 的真正多项式。准确 Chebyshev 恒等给
$$
\sup_{1\le t\le\kappa^2}|r_\nu(t)|\le a_\nu.
\tag{3.7}
$$

取
$$
a_{\rm pol}=p_{\nu-1}(G_E)b,\qquad
k_{\rm pol}=\mathcal S a_{\rm pol}.
\tag{3.8}
$$
由 (3.3) 和 (2.3)，$a_{\rm pol}$ 的 total grade 不超过
$$
s+w+(\nu-1)w=s+\nu w\le Q.
$$
它属于 $E=V_Q^0$，故由 (2.1)，$a_{\rm pol}\in K_Q^0$。因此
$$
\boxed{k_{\rm pol}\in K_Q.}
\tag{3.9}
$$
这一步得到的是原完整核向量。没有将小残量当成到核的距离，也没有更换 cut 或源。

## 4. 同 actual-$u$ 的无额外条件数前因子界

由 (3.2)、(3.6)，
$$
a-a_{\rm pol}=r_\nu(G_E)G_E^{-1}b.
$$
在整个 $E$ 上保留物理能量，则
$$
\begin{aligned}
\|v-k_{\rm pol}\|^2
&=\langle G_E(a-a_{\rm pol}),a-a_{\rm pol}\rangle\\
&=\|r_\nu(G_E)G_E^{-1/2}b\|^2\\
&\le a_\nu^2\,\|G_E^{-1/2}b\|^2\\
&=a_\nu^2\|v\|^2.
\end{aligned}
\tag{4.1}
$$
$K_Q\subset V_Q$ 给 $P_{K_Q}f=P_{K_Q}v$。其最小性和 (3.9) 遂给
$$
\boxed{
\|u\|^2
=\operatorname{dist}(v,K_Q)^2
\le a_\nu^2\|v\|^2
\le a_\nu^2\|f\|^2.
}
\tag{4.2}
$$
这同时证明候选本身的实际原范数误差 (4.1)，并非只比较两个 Gram 的标量值。

当 $\kappa=1$ 时，$\mathcal G=I$、$G_E=I$，故 $a=b$ 已有 total grade $\le s+w\le Q$；(2.1) 直接给 $v\in K_Q$，即 $u=0$。$d=1$ 亦直接齐次，按相同论证有 $u=0$。

所有带宽、逆和谱定理均作用于有限个 grade 的闭 Hilbert 直和；每个 grade 内可以无限维。因此 (4.2) 对原无限连续尾直接成立，无需先截有限位置后交换极限。

## 5. 原 N/Y 模型的直接 moving-head 窗口

对原 $m\ge10$、$d=2^m$，采用缩放真实头稿 §2 的 $S_m$。定义其已付上界
$$
\begin{aligned}
\Psi_m={}&
\frac{35}{6}d^4+\frac52d^3
-(150m-275)d-\frac{850}{3}\\
&+2\log d+2(d-1)\log2,
\qquad \overline\kappa_m=e^{\Psi_m}.
\end{aligned}
\tag{5.1}
$$
原 N/Y 物理条件数满足 $\kappa_m\le\overline\kappa_m$。固定原 forcing 的尾孔上界 $s$，取
$$
\nu_m=\lceil m\,\overline\kappa_m\rceil,\qquad
Q_m=s+(d-1)\nu_m.
\tag{5.2}
$$
由
$$
-\log\rho_m
=\log\frac{\kappa_m+1}{\kappa_m-1}
\ge\frac2{\kappa_m}
\ge\frac2{\overline\kappa_m},
$$
得到
$$
\boxed{
\sup_{\substack{\Pi_{\le s}f=f\\\|f\|\le1}}
\|(P_{V_{m,Q_m}}-P_{K_{m,Q_m}})f\|
\le2e^{-2m}\longrightarrow0.
}
\tag{5.3}
$$
若实际 $\kappa_m=1$，左侧为零。

这个窗口准确有
$$
\log Q_m=\frac{35}{6}d^4+O(d^3+md),
\tag{5.4}
$$
其中固定 $s$ 不改变主项。它不需要先取额外 $x_m$，也不需要 $Q_m\ge x_m-m+L_m$。全部原头向量以及所列低尾孔 forcing 统一受控；没有仅对一个外选真空塔重选来源。

## 6. 与原 carry / same-$w$ 门的准确关系

(4.2) 是原有限头模型的真实物理投影结论，已经保住完整中间 Schur。它对所有有界齐次尾 $D$ 成立，因此没有从连续尾的特殊 MP 低层预算偷渡高层结论。

但 (5.2) 尚不在旧 c26 的原全局运输窗口内。原 c26 一步修复准确含
$$
\mathcal R_0
\sum_{j,\ell<z}
\frac{\mathcal R_0^{j+\ell}}{(j+1)!\ell!}
\|A_p^jK_pA_p^\ell\|,
\qquad
\mathcal R_0\le512(Q+5z)^2.
\tag{6.1}
$$
所以不能把该式称作只出现一次 $Q^2$。当 $p=m$、$\log Q$ 为 (5.4) 的量级时，完整跨块 $2z-1$ 仍会带来 $O(d^5)$ 的正指数成本，旧 $e^{-c d^4}$ carry 不足以通过这一既有环境估计。因此本文没有证明 (5.3) 能与原 $W$ 的锚、同一 $w$ 导数和母提升同时使用。

它较此前“远池相容塔加完整头 Chebyshev”的模型应用减少了一个真正的限制：原 actual-$u$ 可以直接在 $Q$ 上获得 (4.2)，不用为来源恒等式支付一个更大的远池位置 $x$。下一步仍需利用当前特定 $k_{\rm pol}$ 或固定物理 forcing 的结构，证明原 (6.1) 的实际共同 carry 费用，或改善完整 $G_E$ 在该 forcing 上的谱测度；不能把全头 $\kappa_m$ 删除，也不把模型结论等同 $N=M$。
