# R150 / S0 / Lt0：同一 eta 的四单项式生成及全部二次重叠

状态：**已证明的原必要系统与带来源的有限生成归约**。本条没有判空一般 Lt0，没有声称四个生成元线性独立，也没有声称下面六式生成整个原临界理想。

作者：AI-assisted GPT-6 Astra Pro；会话 `Astra-ISP-8542378f-20261127`。日期：2026-11-27（Asia/Taipei）。

## 1. 原坐标、已付单位与精确范围

沿用[原低不变量系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-low-invariant-original-system.md)与[原 Cramer 系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-original-Cramer-minor-system.md)。令

$$e=u-1,\qquad k=Q/e,\qquad j=k+2-2e,\qquad x=k+4,\qquad v=4kbc\,t,$$

$$D_3=4e^3-3e^2k-4e^2+ek^2+4ek+4e-k-4.$$

原恒等式给 $bc=D_3/[4k(ek-1)]$，$ℓ=j/k$。本条只局部化在已经支付的

$$e\,k\,(e+1)(e-1)(4e-k-4)j\,x\,D_3(ek-1)\ne0.$$

其中 $e-1$ 来自整个零基点权重分支的排除，$4e-k-4$ 来自整个半权分支；$j$ 的单位性来自 S0 原 $P_{02}$ 恒等式，而非借用 L0 的权重结论。所有初始 Gram 坐标分母仍逐项验证为 $Q,1-Q,bc$ 的乘积。源从原 Frobenius Gram 重建均值与 $N/P$；双点乘法始终含

$$ (d^2)_1=2d_0d_1. $$

以下 $eta$ 始终是同一个带符号变量。记

$$s=2\lambda-3,\quad A=2\lambda^2-2\lambda+1,\quad C=-4\lambda^2+5\lambda-2,$$

$$T=x^2-2j^2-2\lambda jx-4xf,\quad Z=sT-2jkA,\quad Z_d=2j^2,$$

$$D=s^2Z_d-4Z,\quad B=T-j^2s,\quad U=ek+2e-2.$$

三个指定原 S0 关系为

$$M_a=UD-2j\eta B,\qquad M_n=\eta^2Z_d-(1-ek)D,$$

$$M_N=2k^2x((3-4\lambda)Z_d-Z)f-2ek(2j^2+T)Z-xW Y,$$

其中

$$W=(\lambda-1)(2jk)-T,\qquad Y=j(j+k(e+1))s-T-j^2\eta.$$

源保留从同一原 S0 的矩、配对、范数、$P_1$ 与 $N(V)$ 到这些关系的全部有理恒等式，逐项乘回；尤其 $M_N$ 保留同一个 $eta$，没有从范数方程另选一个嵌入。

令 $E_1,E_{B,+},E_{B,-}$ 为三个已登记的原均值必要式，取六个**指定**原生成元

$$\mathcal O=(E_1,E_{B,+},E_{B,-},M_a,M_N,M_n).$$

本条证明的是这些六式在上述已付局部化中的精确改写及其原必要后果。完整原系统的其他方程仍保持为另外的必要约束。

## 2. 两个可逆矩阵及六条改写

前三个均值对 $(\lambda^2,\lambda f,f^2)$ 的系数矩阵 $C_0$ 满足

$$\det C_0=-512e(e+1)(4e-k-4)k^2(-j)^3D_3^3.$$

源核出全部九个伴随矩阵恒等式。因此三个平方单项式可改写为 $1,\lambda,f$ 的线性组合，其系数是 $v$ 的次数至多二的多项式，分母只来自该行列式。

先用这三条改写约化 $M_a,M_N$。它们对 $(\eta\lambda,\eta f)$ 的系数矩阵为

$$C_\eta=\begin{pmatrix}4j^2(x+j)&8jx\\4xj^3(k+2)&4x^2j^2\end{pmatrix},$$

$$\det C_\eta=32x^2j^4(1-e).$$

这四个系数及行列式是在原多项式上逐项核出的；四个逆矩阵乘积恒等式也逐项通过。新增因子只有已付的 $x,e-1$。因此 $\eta\lambda,\eta f$ 可以改写为 $1,\lambda,f,\eta$ 的线性组合，系数的 $v$ 次数至多三。

同样约化 $M_n$ 后，$\eta^2$ 的首项系数恰为 $2j^2$。除去这个已付单位即得第六条改写，其 $v$ 次数至多二。总计六个左端为

$$\lambda^2,\quad\lambda f,\quad f^2,\quad\eta\lambda,\quad\eta f,\quad\eta^2.$$

每个右端对 $\lambda,f,\eta$ 的总次数至多一。按此总次数递降，任意多项式均返回

$$a_0(e,k,v)+a_1(e,k,v)\lambda+a_2(e,k,v)f+a_3(e,k,v)\eta.$$

这是四个单项式的**生成性**。额外一致性行可能令它们相关，故不从此推出自由模、独立基底或维数恰为四。

源对每条改写关系 $R_i$ 显式建立并核验

$$R_i=\sum_{q=1}^{6} T_{iq}\mathcal O_q.$$

随后反向约化每个 $\mathcal O_q$ 至零，核验

$$\mathcal O_q=\sum_{i=1}^{6} S_{qi}R_i.$$

所以六条改写与六个指定原生成元的局部化理想确实相同。每次进一步约化还同时保存两种来源：

$$p-\operatorname{NF}(p)=\sum_i Q_iR_i=\sum_q\widetilde Q_q\mathcal O_q.$$

这里的 NF 是固定顺序的、带来源的递降返回；没有在尚未支付一致性之前宣称它是唯一的商环标准形。

## 3. 完整重叠与原 N/P 返回

六个二次左端的十五对重叠全部处理。九对的最小公倍单项式为三次，分别构造两条改写所得差，再按上述递降返回。每一行均核回六个指定原式的显式组合。其余六对左端互素，用精确的乘积恒等式核回，不添加未经证明的新关系。

以 $R_i=m_i-r_i$ 记六条改写，对一对左端 $m_i,m_j$ 及最小公倍式 $m$，源先核

$$\frac m{m_i}r_i-\frac m{m_j}r_j
=\frac m{m_j}R_j-\frac m{m_i}R_i.$$

互素时还核

$$m_jr_i-m_ir_j=r_iR_j-r_jR_i.$$

非互素时返回的三次重叠差作为原必要行保留；并不把非零余行忽略或当成已满足。

同一算法返回六个额外原必要式：双点 $N_1$、原 U 矩、两个分别的 $N_B$ 共轭分量和两个分别的 $P_B$ 共轭分量。$N/P$ 中使用的 $\eta$ 和上述六式相同；原三次幂与范数约化三次幂之差是原 $M_n$ 的显式倍数，源也核回这一点。原 $N_1$ 返回仅 205 项，次数 $(e,k,v)=(8,7,2)$；原 U 矩返回 880 项，次数 $(14,13,3)$。所有十六个非零必要行的完整系数可由源即时重建，仓库不保存可重算系数表。

一个较小的新后果完全不需要除以 $B$。定义

$$Q_a=U^2D-2(1-ek)B^2.$$

直接展开有

$$D Q_a=M_a(UD+2j\eta B)+2B^2M_n.$$

原三值互异图的 $D=2j^2\Delta_U$、$\Delta_U=(h-k)^2=(2\lambda-3)^2-4z$ 是已付单位（整个 $h=k$ 已关闭），故 $Q_a=0$ 为原必要式。它返回一个不含 $\eta$、对 $\lambda,f$ 线性的 451 项式，次数 $(e,k,v)=(12,10,2)$；以上恒等式避免了独立取范数或除以可能为零的 $B$。

## 4. 真实执行与准确边界

[自含源](../notes/2026-11-27-unit211-S0-Lt0-same-eta-four-monomial-original-return-8542.py)。

- 源 SHA-256：`cc6de2e33abfa5e8356919205e38ade41678df35be2f1c873332c71ab452f9cb`。
- 参数：无；Python 3.12.14、python-flint 0.9.0；120 秒 alarm、4 GiB 地址空间上限。没有调用 Singular，也没有把 build 当作排空。
- 实际返回码 0，外层运行 7.896800 秒；源内 7.610593 秒，最大 RSS 43,084 KiB。
- 共核 1,325 个返回/来源系数分母，均由指定已付单位组成。
- 十五对重叠全部覆盖：九条三次原来源返回、六条互素乘积恒等式；十六个非零原必要行全部核回。
- stdout 15,163 字节，SHA-256 `de491f0713732d188259bc4957722a28db03e8990ac395d014b394f7577b99e4`。
- [小回执](../notes/2026-11-27-unit211-S0-Lt0-same-eta-four-monomial-execution-8542.json)。首次额外 scratch JSON 导出在全部数学检查通过后因未把 flint 指数转成 Python int 而退出 1；回执保留其准确失败范围与 SHA。修正只涉及该外部导出器，以上源字节未改。

本条支付的是新的低次原必要输入与完整改写来源。一般 S0/Lt0 的公共零点排除、全原临界理想来源和普通 Hilbert ISP 仍未完成；它们没有被本条的四单项式生成性替代。
