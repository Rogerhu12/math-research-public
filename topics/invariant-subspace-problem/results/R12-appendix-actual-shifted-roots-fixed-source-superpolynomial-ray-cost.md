# 原 Haar 移位解析根在每条完整射线上的同源费用

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127  
作者：stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：完整证明。** 对每个原 Haar 尾及任意非零实际闭不变旗子商，每个非零固定向量的移位解析 $q$ 次根费用，在任一完整射线上都不是任何有限负幂的 $O$。因而任何固定非零有界左、右正则器都不能使此族有多项式范数界。结论使用同一个原算子及真实向量，不使用负整数边界。

这里的发散是逐射线的 $\limsup$，不是断言整个极限必为无穷。稀疏参数子列、随动向量和其他非局部闭根仍未排除。

## 1. 原尾及实际子商的四次幂界

按[原尾根重数正文](R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md) §1，记原 Haar 尾为 $A^{(m)}$，原权满足
$$
\alpha_j=e^{-L_j},\qquad L_j\ge20\,16^j,\qquad
\|(A^{(m)})^n\|=\prod_{a=1}^n\alpha_{m+v_2(a)}.
\tag{1}
$$
所有权均不超过一。取 $j=\lfloor\log_2 n\rfloor$，
乘积中包含 $a=2^j$ 的因子，故对 $n\ge1$，
$$
\|(A^{(m)})^n\|
\le\alpha_{m+j}
\le e^{-20\,16^{m+j}}
\le e^{-c_m n^4},
\qquad c_m=\frac54\,16^m.
\tag{2}
$$

现令 $K_-\subset K_+$ 是任意真实闭 $A^{(m)}$ 不变旗，
$Q=K_+/K_-\ne0$，并令
$$
C=(A^{(m)})_Q.
$$
原强多项式单位逐旗下降，已付 $C$ 单射、值域稠密；
参见 [R140](R140-invariant-subquotient-type-and-fixed-first-regularization.md)
及[原幂恢复与实际子商](R12-appendix-odd-power-strong-recovery-all-power-commutants-and-actual-subquotients.md)。
同时
$$
\|C^n\|\le e^{-c_m n^4}.
\tag{3}
$$
下面也适用于全原尾，即 $K_-=0,K_+=H_m$，以及任意固定有限放大。
$C^*$ 同样单射且满足 (3)，因为 $C$ 已有真实稠密值域。

## 2. 同一原算子上的整函数根

固定整数 $q\ge2$，置
$$
b_n=\binom{1/q}{n},\qquad
F_q(w)=\sum_{n=0}^{\infty}b_n w^n C^n.
\tag{4}
$$
$b_n\ne0$ 对所有 $n$ 成立，而且 $|b_n|\le1$。
由 (3)，级数在每个紧集按算子范数绝对收敛，故为整函数。
在原点邻域的普通二项式身份，再由整函数唯一性，给
$$
F_q(w)^q=I+wC\qquad(w\in\mathbb C).
\tag{5}
$$

这里还有必须保留的全圆周增长界。
令 $L=\log^+|w|$、$c=c_m$。
对 $n\ge0$，
$$
nL-cn^4
\le-\frac c2n^4+
\frac{3}{4(2c)^{1/3}}L^{4/3}.
$$
于是
$$
\boxed{
\|F_q(w)\|
\le K_c\exp\!\left[
\frac{3}{4(2c)^{1/3}}(\log^+|w|)^{4/3}
\right],
\qquad
K_c=\sum_{n=0}^{\infty}e^{-cn^4/2}<\infty.
}
\tag{6}
$$
特别这是零阶整函数增长；后面的单射线论证使用的是 (6)，
不只是谱半径为零。

固定射线角 $\phi$，取 $\epsilon=re^{i\phi}$、$r>0$。
在这条射线上固定任意一个 $q$ 次根相位，定义
$$
R_{\epsilon,q}=\epsilon^{1/q}F_q(\epsilon^{-1}).
\tag{7}
$$
它就是原点处解析芽 $(\epsilon+z)^{1/q}$ 在 $C$ 上的真实有界全纯演算。
每个固定 $\epsilon\ne0$ 有
$$
R_{\epsilon,q}^{\,q}=C+\epsilon I.
\tag{8}
$$
本文没有将 $\epsilon=0$ 代入这个公式以制造闭根。

## 3. 单射线多项式界的完整整函数引理

**引理。** 设 Banach 空间值整函数 $F$ 满足
$$
\|F(z)\|\le K\exp[K(\log^+|z|)^{4/3}].
\tag{9}
$$
若存在 $\theta\in\mathbb R$、$a\ge0$，使
$$
\|F(te^{i\theta})\|=O(t^a)\qquad(t\to\infty),
\tag{10}
$$
则 $F$ 是次数不超过 $\lfloor a\rfloor$ 的向量多项式。

**证明。** 旋转变量后令该射线为正实轴。
选
$$
a<b<\lfloor a\rfloor+1,\qquad 0<\rho<\frac12.
$$
在切开的外圆域 $\{z:|z|>R,\ 0<\arg z<2\pi\}$ 上，
选同一分支 $z^b,z^\rho$，并令
$$
H_\eta(z)=z^{-b}F(z)
\exp[-\eta e^{-i\pi\rho}z^\rho],
\qquad\eta>0.
$$
对整个角区间，
$$
\operatorname{Re}(e^{-i\pi\rho}z^\rho)
=|z|^\rho\cos(\rho(\arg z-\pi))
\ge |z|^\rho\cos(\pi\rho)>0.
\tag{11}
$$
两侧射线边界由 (10) 和 $b>a$ 一致有界。
内圆边界也有与 $\eta$ 无关的界，因为指数因子的模不超过一。
在外圆 $|z|=R'$ 上，(9)、(11) 给
$$
\|H_\eta(z)\|
\le K(R')^{-b}
\exp[K(\log R')^{4/3}-\eta\cos(\pi\rho)(R')^\rho]
\longrightarrow0.
$$
逐个连续线性泛函使用最大模原理，并取其单位球上确界，
得到 $\|H_\eta(z)\|\le M$，其中 $M$ 可不依赖 $\eta$。
先令 $R'\to\infty$，再对固定 $z$ 令 $\eta\downarrow0$，
得全外圆域上的 $\|F(z)\|\le M|z|^b$。
加上被切射线及内圆，得到全平面的同一多项式增长界。

Cauchy 系数估计使所有整数 $n>b$ 的系数为零。
因 $b<\lfloor a\rfloor+1$，剩余次数至多 $\lfloor a\rfloor$。证毕。

证明保留了完整 $2\pi$ 开角；$\rho<1/2$ 是压低两个边界之间整个角域所需的条件。
没有从一条射线上的界直接跳到全圆周界。

## 4. 每个固定非零来源都超出任意多项式费用

**定理。** 对上述任何实际 $C$、任何整数 $q\ge2$、
任何 $x\in Q\setminus\{0\}$、任何 $\phi\in\mathbb R$ 和任何 $M\ge0$，
$$
\boxed{
\limsup_{r\downarrow0}
r^M\|R_{re^{i\phi},q}x\|=\infty.
}
\tag{12}
$$

**证明。** 若该 $\limsup$ 有限，则
$\|R_{re^{i\phi},q}x\|=O(r^{-M})$。
令 $t=r^{-1}$，由 (7) 得
$$
\|F_q(te^{-i\phi})x\|=O(t^{M+1/q}).
$$
应用 §3 于同一向量值整函数 $F_q(w)x$，
它只能是有限次数的向量多项式。
而 (4) 的第 $n$ 个系数是 $b_n C^n x$，
每个 $b_n$ 非零。于是对某个整数 $n\ge1$ 有 $C^n x=0$。
$C$ 单射迫 $x=0$，矛盾。证毕。

特别，对每个非零 $x$，这族根在任何完整射线上都不是有界的。
这比“算子范数无界”严格更强：来源 $x$ 在全部参数中是固定的。

## 5. 任意固定有界左、右正则器都不能支付

设 $P$ 是相应 Hilbert 空间上的任意非零有界算子，
不要求它与 $C$ 交换、不要求它单射或满像。
选 $u$ 使 $Pu\ne0$，定理直接给
$$
\boxed{
\limsup_{r\downarrow0}r^M\|R_{re^{i\phi},q}P\|=\infty
\qquad(M\ge0).
}
\tag{13}
$$
右侧若有任何多项式范数界，作用在这个固定 $u$ 上就与 (12) 矛盾。
特别，$R_{re^{i\phi},q}P$ 不可能沿整条射线强收敛；
否则一致有界原理会给一个最终的统一范数界。

将同一结论用于 $C^*$ 和 $P^*\ne0$。
实二项式系数给
$$
R_{re^{i\phi},q}(C)^*
=R_{re^{-i\phi},q}(C^*)
$$
至多相差一个模为一的固定分支标量，因此也有
$$
\boxed{
\limsup_{r\downarrow0}r^M\|P R_{re^{i\phi},q}\|=\infty.
}
\tag{14}
$$
左正则器族同样不能沿完整射线强收敛。

所以即便选取已刊平坦理想中的非零算子，
或 [R267 全部幂共同倍数](R267-appendix-common-multiples-of-all-a-powers-and-non-uhf-strong-units.md)，
也不能靠一个固定左右正则器使移位解析根的整射线极限成立。
这里排除不依赖形式喷射忠实性，且覆盖任意固定有界 $P$。

## 6. 原接口的边界

本文只处理 (7) 的同一原解析移位根族。
对稀疏 $r_n\downarrow0$，(12) 没有断言该子列也发散；
它也不控制随动 $x_n\to x$ 时
$R_{r_ne^{i\phi},q}x_n$ 的图极限。
若采用随动源，仍须支付同一个非零极限向量、输出强收敛及自然平方域。

一般稳定闭根 $S^q=C|_{\operatorname{Dom}S}$ 不必由 (7) 得到，
本稿不排除这种根，更不把未知实际旗子商换成整个原尾。
它关闭的是本次新尝试的固定来源、固定正则器、完整射线解析极限输入；
原 Haar 普通不变格和 README 的完成目标仍未解决。
