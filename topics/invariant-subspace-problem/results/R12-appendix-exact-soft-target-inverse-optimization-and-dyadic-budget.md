# 原球内软目标的准确逆像最优化及 dyadic 四次预算

作者：OpenAI ChatGPT，`/root/literature_deddens`；会话 `Astra-ISP-8542378f-20261127`。日期：2026-11-27（Asia/Taipei）。

**状态：已证明的中间结论。** 本稿在原 $L^2$ 球内准确求出具有最小 $A^{-n}$ 范数的软目标，并在 $n=2^j$ 时给含常数的渐近式。它没有默认逐个最优目标可以由同一条 Deddens 递推连接；该连接仍须支付实际插值成本。

## 1. 问题及原逆像

固定原 Haar 算子
$$
(Af)(y)=w(y)f(y-1),\qquad
W_n(y)=\prod_{a=0}^{n-1}w(y-a),\qquad A^n=M_{W_n}U^n.
$$
权、测度和 $\beta_n=\|A^n\|$ 均沿用 [R9](R9-radial-odometer-and-nilpotent-approximants.md)。$W_n$ 连续、有界、几乎处处严格正，且只有有限零点。原逆像满足
$$
g\in\operatorname{Ran}A^n\quad\Longleftrightarrow\quad
g/W_n\in L^2,
\qquad
\|A^{-n}g\|=\|g/W_n\|_2.
\tag{1.1}
$$

对固定 $0<r<1$，定义实际球内最优值
$$
\mathfrak m_n(r)=\inf\{\|A^{-n}g\|:
g\in\operatorname{Ran}A^n,
\ \|g-\mathbf1\|_2\le r\}.
\tag{1.2}
$$
这既保留原目标球，也保留完整原逆像；不只删除少数坏格来估算普通范数误差。

## 2. 唯一最优软目标

**定理 2.1。** 存在唯一的 $\lambda=\lambda_n(r)>0$ 使
$$
\int\left(\frac{\lambda}{W_n(y)^2+\lambda}\right)^2d\mu(y)=r^2.
\tag{2.1}
$$
问题 (1.2) 的唯一最优向量是
$$
\boxed{g_{n,r}(y)=\frac{W_n(y)^2}{W_n(y)^2+\lambda_n(r)},}
\tag{2.2}
$$
并且
$$
\boxed{\mathfrak m_n(r)^2
=\int\frac{W_n(y)^2}{(W_n(y)^2+\lambda_n(r))^2}\,d\mu(y).}
\tag{2.3}
$$

**证明。** (2.1) 左侧关于 $\lambda>0$ 连续且严格增加；由支配收敛，端点极限分别为 $0$ 和 $1$。严格性使用 $W_n>0$ 几乎处处。故唯一参数存在。

写 $W=W_n$、$g_\lambda=W^2/(W^2+\lambda)$。有
$g_\lambda/W=W/(W^2+\lambda)$，其模不超过 $1/(2\sqrt\lambda)$，所以 $g_\lambda\in\operatorname{Ran}A^n$。对任意同值域的 $g$，逐点配方后积分得
$$
\|g/W\|^2+\lambda^{-1}\|g-\mathbf1\|^2
=\|g_\lambda/W\|^2+\lambda^{-1}\|g_\lambda-\mathbf1\|^2
+\int(W^{-2}+\lambda^{-1})|g-g_\lambda|^2\,d\mu.
\tag{2.4}
$$
若 $g$ 可行，则 $\|g-\mathbf1\|^2\le r^2=\|g_\lambda-\mathbf1\|^2$，移项可见 $\|g/W\|\ge\|g_\lambda/W\|$。等号迫最后非负积分为零，故 $g=g_\lambda$。证毕。

同样证明对一般给定球心 $f$ 和 $0<r<\|f\|$ 有 $g_\lambda=W_n^2f/(W_n^2+\lambda)$；下面的准确层分布和渐近常数专门针对球心 $\mathbf1$，不把它未经证明地推广到未知向量。

## 3. Dyadic 幂的准确原权分布

令 $n=N=2^j$，写 $y=a+Nz$，$0\le a<N$。乘积 $W_N(y)$ 所含的 $N$ 个连续整数位置中，恰有一个是 $Nz$，其余位置的模 $N$ 类遍历 $1,\ldots,N-1$。因此
$$
\boxed{W_N(a+Nz)=\beta_{N-1}w(Nz).}
\tag{3.1}
$$
对 $k\ge0$，置
$$
E_{j,k}=\{a+Nz:v_2(z)=k\},\quad
p_k=2^{-k-1},\quad b_{j,k}=\beta_{N-1}\alpha_{j+k}.
$$
除有限零点外，这些层分割整个空间，且
$$
\mu(E_{j,k})=p_k,\qquad W_N|_{E_{j,k}}=b_{j,k}.
\tag{3.2}
$$
所以 (2.1)–(2.3) 在原模型上准确成为
$$
\sum_{k\ge0}p_k
\left(\frac{\lambda}{b_{j,k}^2+\lambda}\right)^2=r^2,
\tag{3.3}
$$
$$
\mathfrak m_N(r)^2
=\sum_{k\ge0}p_k
\frac{b_{j,k}^2}{(b_{j,k}^2+\lambda)^2}.
\tag{3.4}
$$
未使用任何替代权或有限 nilpotent 模型。

## 4. 含 dyadic 边界的精确渐近式

给定固定 $0<r<1$，令 $q\ge0$ 为唯一满足
$$
2^{-q-1}\le r^2<2^{-q}
\tag{4.1}
$$
的整数，并置
$$
t_r=1-\sqrt{2^{q+1}r^2-1},\qquad
c_r=2^{-(q+1)/2}t_r>0.
\tag{4.2}
$$
注意下端点包括在内：$r^2=2^{-q-1}$ 时 $t_r=1$。上端点属于前一个区间，不在本区间中令 $t_r=0$。

**定理 4.1。** 当 $N=2^j\to\infty$ 时，
$$
\boxed{\mathfrak m_N(r)
\sim\frac{c_r}{\beta_{N-1}\alpha_{j+q}}.}
\tag{4.3}
$$

**证明上界。** 在原层上取可行测试
$$
g_j^{\rm test}=
\sum_{k<q}\mathbf1_{E_{j,k}}+t_r\mathbf1_{E_{j,q}}.
$$
更深层全部置零。因为 $\sum_{k>q}p_k=p_q$，有
$$
\|g_j^{\rm test}-\mathbf1\|^2
=p_q(1-t_r)^2+p_q=r^2.
$$
其支持上的权至少为 $b_{j,q}>0$，故确在 $\operatorname{Ran}A^N$。于是
$$
b_{j,q}^2\mathfrak m_N(r)^2
\le\sum_{k<q}p_k\left(\frac{b_{j,q}}{b_{j,k}}\right)^2+p_qt_r^2
\longrightarrow p_qt_r^2=c_r^2.
\tag{4.4}
$$
极限使用固定 $k<q$ 时 $\alpha_{j+q}/\alpha_{j+k}\to0$。

**证明下界。** 取定理 2.1 的实际最优向量 $g_j$。上界已给 $b_{j,q}\|A^{-N}g_j\|$ 一致有界。在较深层 $F_j=\bigcup_{k>q}E_{j,k}$ 上，$W_N\le b_{j,q+1}$，故
$$
\|g_j\mathbf1_{F_j}\|
\le b_{j,q+1}\|A^{-N}g_j\|
\longrightarrow0,
$$
因为 $b_{j,q+1}/b_{j,q}=\alpha_{j+q+1}/\alpha_{j+q}\to0$。又 $\mu(F_j)=p_q$，所以
$$
\|(g_j-\mathbf1)\mathbf1_{F_j}\|^2\longrightarrow p_q.
$$
整个球误差至多 $r^2$，因此
$$
\limsup_j\|(g_j-\mathbf1)\mathbf1_{E_{j,q}}\|
\le\sqrt{r^2-p_q}.
$$
反向三角不等式给
$$
\liminf_j\|g_j\mathbf1_{E_{j,q}}\|
\ge\sqrt{p_q}-\sqrt{r^2-p_q}
=c_r.
$$
而 $b_{j,q}\|A^{-N}g_j\|\ge\|g_j\mathbf1_{E_{j,q}}\|$，故与 (4.4) 的上界吻合。这也完整覆盖 $r^2=p_q$ 的边界，没有在边界处假定 $\lambda/b_{j,q}^2$ 趋于某个正数。证毕。

## 5. 原四次预算的准确常数

记 $S_n=-\log\beta_n$。对 $N=2^j$，直接按 $v_2$ 计数给
$$
S_{N-1}=\sum_{k=0}^{j-1}2^{j-k-1}L_k
=\frac{20}{3}N^4-15N^3+(150j-275)N+\frac{850}{3}.
\tag{5.1}
$$
代入原 $L_{j+q}$，得到准确恒等式
$$
S_{N-1}+L_{j+q}
=\frac{20+280\,16^q}{3}N^4
-(15+90\,8^q)N^3
+(150j-275+300\,2^q)N.
\tag{5.2}
$$
由 (4.3)，
$$
\boxed{\log\mathfrak m_N(r)
=S_{N-1}+L_{j+q}+\log c_r+o(1),}
\tag{5.3}
$$
特别
$$
\boxed{\lim_{j\to\infty}
\frac{\log\mathfrak m_{2^j}(r)}{(2^j)^4}
=\frac{20+280\,16^q}{3}.}
\tag{5.4}
$$
例如，$1/2\le r^2<1$ 时常数为 $100$；$1/4\le r^2<1/2$ 时为 $1500$；$1/8\le r^2<1/4$ 时为 $23900$。这些变化来自原 Haar 层的质量与极快权衰减，不是把半径随 $n$ 调整。

## 6. 对实际递推能合法推出什么

若从 $f_0=\mathbf1$ 出发，已有一条实际递推
$$
f_n=R_nAf_{n-1},\qquad R_n\in\mathcal D_A,
\qquad\|f_n-\mathbf1\|\le r,
$$
则 [负幂域与共轭](R12-appendix-deddens-negative-domains-and-isometric-conjugation.md) 保证
$$
f_n\in\operatorname{Ran}A^n,\qquad
\|A^{-n}f_n\|\le\prod_{i=1}^nc_A(R_i).
$$
因此
$$
\boxed{\prod_{i=1}^nc_A(R_i)\ge\mathfrak m_n(r).}
\tag{6.1}
$$
沿 dyadic 子列，(5.3)–(5.4) 给全部实际递推必须支付的准确最有利逆像预算。它只使用真实目标所在球，不要求目标采用硬截断、复制或运输形式。

反方向并未自动成立。定理 2.1 给每个 $n$ 单独的最优目标，并没有证明存在统一普通范数有界的 $R_n$ 将 $Ag_{n-1,r}$ 映到 $g_{n,r}$，更没有证明其全 Deddens 费用可由相邻最优逆像范数之比控制。下一步若要连接这些目标，应把它们代入 [实际同源运输证书](R12-appendix-same-source-transport-interpolation-and-sustainable-actual-recursion.md) 的全部前缀及加权列约束，而不能以标量最优化替代实际算子插值。

本稿不声称 Deddens 算子保持未知 $A$-不变子空间，也未由 (6.1) 得到普通不变子空间。
