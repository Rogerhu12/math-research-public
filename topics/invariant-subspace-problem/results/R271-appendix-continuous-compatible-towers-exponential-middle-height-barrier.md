# R271 附录：原连续尾公共相容塔的中段相干相对费用必有指数增长

日期：2026-11-16（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿加强[相容塔边际门槛](R271-appendix-continuous-compatible-vacuum-tower-marginals-and-linear-deep-return-barrier.md)：对原无限连续尾 $b_i=(i+1)^{-2}$，任何允许复系数、全部 primitive 修正的公共真空塔，只要相容到高度 $x$，便满足
$$
\boxed{
\max\left\{
\sigma_{\lfloor x/48\rfloor}^2\|v_{\lfloor x/48\rfloor}\|^2,\
\sigma_x^2\|v_x\|^2
\right\}
\ge\frac14 e^{x/12800}\qquad(x\ge64).
}
\tag{0.1}
$$
两个高度都在 $j\le x$ 的真实中段，未落入[原强头四次幂已付高段](R271-appendix-true-strong-head-powers-and-complete-deep-return-high-tail.md)。

因此，任何固定多项式的公共塔相干相对上界都不可能成立。这不否定实际完整源 $a=H_C(s)^{-1}g$ 的特殊加权能量，也不否定依赖头源、保全部 primitive/零源的最小化。证明只用原固定大小乘积测度在全部有限条件化下的 pair 负相关；不需要额外的实根或 Poisson-binomial 表示。

## 1. 全部 Hilbert 与有符号边际

在原 Boolean 尾孔层中取
$$
D=D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad
z_i=(i+1)^{-4},\qquad S_x=\sum_{i\ge x}z_i,
$$
$$
\omega_j=(D^*)^j\Omega,\qquad
\sigma_j^2=(j!)^2e_j(z).
$$
令 $L\ge x$，考虑任意
$$
v_j\in\mathcal H_j,\qquad v_0=\Omega,\qquad Dv_j=v_{j-1}
\quad(1\le j\le L).
\tag{1.1}
$$
允许复坐标，没有第一列最小性或非负性假设。

定义
$$
\mu_j(I)=\frac{z_I}{e_j(z)},\qquad
f_j(I)=\frac{j!e_j(z)}{b_I}(v_j)_I,\qquad
\nu_j(I)=\mu_j(I)f_j(I)=j!b_I(v_j)_I.
$$
直接 Cauchy--Schwarz 给
$$
\|\nu_j\|_{\rm TV}\le\sigma_j\|v_j\|<\infty,
$$
而 $D^jv_j=\Omega$ 给
$$
\mathbb E_{\mu_j}f_j=1,\qquad
\mathcal M_j:=\mathbb E_{\mu_j}|f_j|^2=\sigma_j^2\|v_j\|^2.
\tag{1.2}
$$
各 $\nu_j$ 是质量 $1$ 的有限复测度。

逐坐标相容性等价于
$$
\sum_{i\notin I}\nu_j(I\cup\{i\})=j\nu_{j-1}(I).
$$
因此，对任意 $k<j$ 及任意 $k$ 子集事件 $\mathcal A$，
$$
\boxed{
\nu_k(\mathcal A)
=\sum_{|I|=j}\nu_j(I)
\frac{\#\{J\subset I:\ |J|=k,\ J\in\mathcal A\}}{\binom jk}.
}
\tag{1.3}
$$
这是同一个均匀删除 Markov 核作用于复测度，所有求和绝对收敛。没有把 $\nu_j$ 当作概率使用。

## 2. 原 pair 负相关给全部 hole cylinder 与低尾 Chernoff

对 $\mu_j$ 的不同位置 $i,\ell$，删两位后的初等对称和给
$$
\begin{aligned}
&\mathbb E_{\mu_j}n_i\,\mathbb E_{\mu_j}n_\ell
-\mathbb E_{\mu_j}(n_i n_\ell)\\
&\qquad=
\frac{z_i z_\ell}{e_j(z)^2}
\big[(e_{j-1}^{i\ell})^2-e_{j-2}^{i\ell}e_j^{i\ell}\big]\ge0.
\end{aligned}
\tag{2.1}
$$
这里所需的非归一 Newton/log-concavity 已在前稿 §2 由逐因子乘 $1+zt$ 的三项展开自足证明。对有限位置头取极限合法，因为每个固定次数的 $e_r(z)$ 在 $\sum z_i<\infty$ 下绝对收敛。

条件某些有限位置全部占据或全部不占据以后，剩余测度仍是删去这些位置后的同类固定大小乘积测度。因此 (2.1) 对每个非零概率的条件测度继续成立；补指标 $h_i=1-n_i$ 有同一 covariance。逐次条件全 $h_i=1$ 时，另一 $h_\ell$ 的条件概率不会增加。归纳得
$$
\boxed{
\mathbb P_{\mu_j}(h_i=1\ \forall i\in B)
\le\prod_{i\in B}(1-p_i),\qquad
p_i=\mathbb E_{\mu_j}n_i,
}
\tag{2.2}
$$
对每个有限 $B$ 成立。零概率事件直接按零处理。这里没有由 pair 负相关免费调用一般负关联；使用的是条件化后仍属同一族这一额外事实。

对有限 $A$，令 $X=N_A=\sum_{i\in A}n_i$、$\mu=\mathbb EX$。将指数展开成 hole cylinder 的非负系数和，(2.2) 给全部 $t\ge0$ 的准确 MGF 上界
$$
\begin{aligned}
\mathbb E e^{-tX}
&=e^{-t|A|}
\mathbb E\prod_{i\in A}[1+(e^t-1)h_i]\\
&\le\prod_{i\in A}(1-p_i+p_i e^{-t})\\
&\le\exp[-\mu(1-e^{-t})].
\end{aligned}
\tag{2.3}
$$
所以对 $0<a<\mu$，取 $e^{-t}=a/\mu$，有
$$
\boxed{
\mathbb P(X\le a)
\le \exp\{-\mu+a+a\log(\mu/a)\}
\le\exp\left[-\frac{(\mu-a)^2}{2\mu}\right].
}
\tag{2.4}
$$
最后一个初等不等式由
$1-r+r\log r\ge(1-r)^2/2$（$0\le r\le1$）得到。
(2.2)--(2.4) 在无限尾上只涉及有限 $A$，已由上述条件化与系数极限全部支付。它们只作用于正概率 $\mu_j$，从未作用于复 $\nu_j$。

## 3. 两个真实中层的占据分离

设整数 $x\ge64$，置
$$
A=\{x,\ldots,x+\lfloor x/4\rfloor-1\},\qquad
k=\lfloor x/48\rfloor,\qquad j=x.
\tag{3.1}
$$
特别 $k\ge x/96$ 且 $k\ge1$，并有 $j\le L$。

记 $S_A=\sum_{i\in A}z_i$。原连续尾积分界给
$$
\frac1{3(x+1)^3}\le S_x\le\frac1{3x^3}.
$$
由 $|A|\ge x/4-1$，以及
$$
\left(\frac{x+1}{5x/4-1}\right)^3
\le\left(\frac{65}{79}\right)^3<\frac9{16},
$$
得到
$$
\frac{S_A}{S_x}
=1-\frac{S_{x+|A|}}{S_x}\ge\frac7{16},
\qquad
\frac{z_{\max}}{S_x}\le\frac3{x+1}.
\tag{3.2}
$$

原逐次删位计数恒等式为
$$
\frac{\mathbb E_{\mu_k}N_A}{k}
=
\frac{\mathbb E_{\mu_{k-1}}\sum_{i\in A\setminus I}z_i}
{\mathbb E_{\mu_{k-1}}\sum_{i\notin I}z_i}.
$$
分母不超过 $S_x$，分子至少 $S_A-(k-1)z_{\max}$。因此
$$
\boxed{
\mu:=\mathbb E_{\mu_k}N_A\ge\frac38 k,
}
\tag{3.3}
$$
因为 $7/16-3/48=3/8$。

令 $k$ 子集事件
$$
\mathcal A=\{N_A>3k/10\}.
$$
函数 $(\mu-a)^2/(2\mu)$ 在 $\mu\ge a$ 上递增。将
$\mu\ge3k/8$、$a=3k/10$ 代入 (2.4)，得到
$$
\boxed{
\mu_k(\mathcal A^c)
\le\exp\left(-\frac3{400}k\right).
}
\tag{3.4}
$$
准确算术为 $(3/8-3/10)^2/[2(3/8)]=3/400$。非整数阈值无需另取整。

## 4. 从任意 $x$ 子集均匀删到 $k$ 的相反偏差

固定任意 $|I|=x$。因 $|I\cap A|\le|A|\le x/4$，从 $I$ 均匀选取 $k$ 子集时，$N_A$ 是成功比例不超过 $1/4$ 的超几何计数。记该正概率 Markov 核为 $K(I,\cdot)$。

对 $t>0$，
$$
\mathbb E_{K(I,\cdot)}e^{tN_A}
=\frac{e_k(e^t\text{ 重复 }|I\cap A|\text{ 次},\
1\text{ 重复其余次数})}{\binom{x}{k}}.
$$
在非负变量总和固定时，把任意两个变量替为其均值不会减小 $e_k$：将 $e_k$ 分成不含、只含及同时含这两个变量的三项，唯一变化项是二者乘积，且系数非负。逐次均值化遂给
$$
\mathbb E_{K(I,\cdot)}e^{tN_A}
\le(1-\rho+\rho e^t)^k,\qquad \rho\le1/4.
$$
单个 Bernoulli 中心化对数矩母函数的二阶导数至多 $1/4$，故它不超过 $t^2/8$。Chernoff 选参于是给
$$
\boxed{
K(I,\mathcal A)
\le\exp[-2k(3/10-1/4)^2]
=\exp(-k/200).
}
\tag{4.1}
$$
该界对所有 $x$ 子集 $I$ 一致，不需要它是 $\mu_x$ 的典型子集。

## 5. 复密度 Cauchy 与指数下界

由 $\nu_k$ 总质量为 $1$、(1.2)、(3.4)，
$$
\begin{aligned}
|\nu_k(\mathcal A)-1|
&=|\nu_k(\mathcal A^c)|\\
&\le\sqrt{\mathcal M_k\,\mu_k(\mathcal A^c)}
\le\sqrt{\mathcal M_k}\,e^{-3k/800}.
\end{aligned}
\tag{5.1}
$$
另一方面，真实相容性 (1.3)、(4.1) 及
$\|\nu_x\|_{\rm TV}\le\sqrt{\mathcal M_x}$ 给
$$
\boxed{
|\nu_k(\mathcal A)|\le\sqrt{\mathcal M_x}\,e^{-k/200}.
}
\tag{5.2}
$$
两式合并，
$$
1\le\sqrt{\mathcal M_k}\,e^{-3k/800}
+\sqrt{\mathcal M_x}\,e^{-k/200}.
$$
令 $\mathcal M=\max(\mathcal M_k,\mathcal M_x)$。因为 $1/200>3/800$，
$$
\mathcal M\ge\frac14e^{3k/400}
\ge\boxed{\frac14e^{x/12800}},
$$
最后使用 $k\ge x/96$。这证明 (0.1)。整个论证保留全部复相位，不需要任何一层的正性或 MP 最小性。

## 6. 原实际窗口与未付量的准确区分

原 $R=d=2^m$、$x=m+d$、$h=2d$ 在 $m\ge10$ 时满足 $h-1\ge x$。所以对 canonical 全塔及任何其他公共相容塔，本稿的两层都确实出现在原合法 $Q\ge4d$ 真核候选中。两层 $k=\lfloor x/48\rfloor$、$x$ 又都低于已付四次幂高段阈值
$$
J_*(x)=\lceil x+2\sqrt{x}(\log x)^{1/4}\rceil.
$$
因此本稿不是对已经由真实幂压掉的高层重复给坏系数。

若 $R=0$、$m=x\ge64$，原头高度 $2^m$ 同样覆盖这两层；结论亦非依赖强位数量人为过多的现象。

另一方面，实际修复误差始终是同一个完整源的加权和。例如 canonical 完整列满足
$$
\|F_s-z\|^2=
\sum_j
\left[
s^jj!\|v_j\|^2-2+\frac{\sigma_j^2}{s^jj!}
\right]\frac{\|C^ja\|^2}{s^jj!}.
$$
(0.1) 只说明其中某个公共塔系数必须很大，并未给那个高度上的真实 $C^ja$ 下界；大系数与实际源能量不能互换量词。因此它不构成 actual-$u$ 或 $W$ 的反例。

准确后继仍可以是：证明实际源在危险层的更强衰减；使用依赖完整头源的 lift；或者保留所有 primitive、零源及中间 Schur，得到更小的真实距离。不能再仅以一个尚未证明、且已被 (0.1) 排除的公共塔 $O(j)$ 预算，连接 log-variance 的一阶能量选择。
