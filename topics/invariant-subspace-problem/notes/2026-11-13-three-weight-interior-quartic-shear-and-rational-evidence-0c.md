# 两大权组加一异常位：内部四次式、交叉项符号及有限精确记录

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

状态：§§1–2 是完整代数归约和已证符号；§3 是有限有理核验，**一般全高度系数正性仍为猜想**。高度二的全参数结论由[完整二维稿](../results/R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md)另行证明。

## 1. 全部内部高度的真正四次式

沿完整二维稿，取 $2\le n\le h-2$。令 $a,b,c,d$ 为旧高出生阶相邻四个首一最小范数 $a_{n-1},a_n,a_{n+1},a_{n+2}$，令 $p,q,r,t$ 为旧低阶 $b_{n-2},b_{n-1},b_n,b_{n+1}$；它们全为正数。这里的 $q$ 仅为标量符号，不是短串长度。

记 $x=k_{n-1}-k_n,y=k_{n+1}-k_n$。同时剪切使 $k_n=0$，有
$$
A_-=a+wb,\quad A_0=b+wc,\quad A_+=c+wd,
$$
$$
B_-=\frac{wpq}{p+wq},\quad B_0=\frac{wqr}{q+wr},\quad
B_+=\frac{wrt}{r+wt}.
$$
令 $K=H_{n-1}-H_nH_{n+1}^{-1}H_n$，并置
$$
\Lambda=(ac-b^2)+w(ad-bc)+w^2(bd-c^2),
$$
$$
F=pq(qt-r^2)+wqr(pt-qr)+w^2rt(pr-q^2).
$$
完整块逆、再取行列式给准确恒等式
$$
\begin{aligned}
P(w)&:=\det K\frac{(p+wq)(q+wr)^2(c+wd)t}{w}\\
&=q\Lambda F-wpq^3r(c+wd)(r+wt)x^2\\
&\quad-wq^2r^2t(a+wb)(p+wq)y^2
-2wpq^2rt(b+wc)(q+wr)xy\\
&\quad-w^2pq^3r^2t x^2y^2.
\end{aligned}
\tag{1.1}
$$
所以问题只剩四次多项式的符号。两端系数已由旧两值严格比较支付：
$$
P_0=pq^2(ac-b^2)(qt-r^2)>0,
\qquad P_4=qrt(bd-c^2)(pr-q^2)>0.
$$
若记 $U_0=ac-b^2,U_1=ad-bc,U_2=bd-c^2$ 和 $V_0=qt-r^2,V_1=pt-qr,V_2=pr-q^2$，则一个明确的中间目标为
$$
P_1=q^2\{rU_0V_1+pU_1V_0
-pqr^2cx^2-pr^2tay^2-2pqrtbxy\},
$$
$$
\begin{aligned}
P_2={}&q(U_0rtV_2+U_1qrV_1+U_2pqV_0)\\
&-pq^3r(ct+dr)x^2-q^2r^2t(aq+bp)y^2\\
&-2pq^2rt(br+cq)xy-pq^3r^2tx^2y^2.
\end{aligned}
$$
标量差式全正尚不支付这些平方和四次费用。

## 2. shear 交叉乘积的符号是已知定理的实际应用

令 $S_i=s_\lambda(e^{\theta[i]},1^{[N-i]})$、$f_i=\log S_i$、$u_i=2f_i-f_{i-1}-f_{i+1}$。这里取完整二维稿的同一矩形 $\lambda=(t^{\delta+1})$、$N=h+1$，其准确源式给 $x=-u_n',y=u_{n+1}'$。

所需单调性属于 Suvrit Sra，*Monotonicity of Turán-ratios of symmetric polynomials* (2026), v1，Lemma 2.2 / Theorem 1.1，pp. 3–4；[作者页面](https://suvrit.github.io/papers/sym-turan/)及[原文](https://suvrit.github.io/papers/sym-turan/sym-turan-v1.pdf)。不把该定理登记为本仓库的新发现。为符合本课题的自足要求，下面从既有两值稿 §8 已完整重证的 Toda 身份给出所需短证。

写 $\kappa=(4\sinh^2(\theta/2))^{-1}$、$B_i=i(N-i)e^{-u_i}$、$v_i=u_i'$。微分 Toda 身份得到
$$
v_i''-\frac{\kappa'}\kappa v_i'
=\kappa(2B_iv_i-B_{i-1}v_{i-1}-B_{i+1}v_{i+1}),
\quad B_0v_0=B_Nv_N=0.
$$
负部之和 $W=\sum_i(-v_i)_+$ 在分布意义满足
$$
W''-(\kappa'/\kappa)W'\ge0.
$$
这是逐负指标相加后的符号：集合内 $B_iv_i<0$，集合外非负；过零的凸正部链式法则只增加非负项。

变量 $s=-\tfrac12\coth(\theta/2)$ 满足 $s'=\kappa$，故 $W$ 关于 $s$ 凸。对称齐次性给 $f_i'(0)=i|\lambda|/N$，所以 $v_i(0)=0$；半标准表的最大 $e^\theta$ 次数为 $\lambda_1+\cdots+\lambda_i$，故 $v_i(\infty)=\lambda_i-\lambda_{i+1}\ge0$。于是 $W$ 两端趋零，凸性迫 $W=0$。这证明 $u_i'\ge0$ 于 $\theta>0$；变量倒数与指标反射处理 $\theta<0$。

因此真实交叉源满足
$$
\boxed{xy\le0\qquad(z>0).}
$$
(1.1) 的 $xy$ 项因此非负；$x^2,y^2,x^2y^2$ 项仍须另外控制。

## 3. 有限有理核验及当前猜想

[完整可重算脚本](2026-11-13-three-weight-interior-quartic-rational-check-0c.py)直接对带强制根的正交多项式取完整矩最小值，然后生成 (1.1) 的五个系数。参数为：短串长度 $1\le q\le6$、$q\le L\le q+4$、所有合法二维出生、全部内部 $2\le n\le h-2$，以及 $z\in\{1/16,1/4,1,4,16\}$。

共 1840 组有理参数的五个系数全部严格正，未使用浮点容差。这只检查这一有限集合，不能证明全部重数或任意正实 $z$。由此提出继续目标：完整内部四次式的所有系数是否在任意两组重数、全部合法出生和 $z>0$ 下都非负？若成立，两端的严格正性便给所有 $w>0$ 的完整矩阵序；该一般命题目前仍开放。

[短串长度三、相对出生三的全高度稿](../results/R239-appendix-three-equal-short-weights-one-exceptional-saturated-two-dimensional-all-heights.md)已用完整整数多项式证书解决其中一个无限参数子族，包含其两个端点；它不覆盖这里的全部猜想。
