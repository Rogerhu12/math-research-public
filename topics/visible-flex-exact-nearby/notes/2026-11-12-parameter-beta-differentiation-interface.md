# 实际均值参数变化时 beta 的有向导数接口

状态：以下恒等式与误差转移已证明；**尚未给当前 KAM 参数盒的实际导数数值界**。
作用是把一个点的完整 beta 证书延伸到真实参数区间，避免把原点、D5 中心和 KAM 最终参数混为一谈。
它使用 R50/R52 的同一物理有限部与同一 R37 零阶口径，不引入新的返回图模型。

## 1. 假设与准确移动根

设 lambda 属于紧实区间 I。冻结各 scalar spline 的 knots，系数解析依赖 lambda；
仍显式保持 r 的正反射和四重角周期。在固定的公共样条段内，有唯一简单正根 t(lambda)，
完整无限目标曲率 K0 在该根为零。负核心与几何分母的所有实际条件在 I 上统一成立。
固定物理切口 b，令 eta(lambda)=t(lambda)-b，并假设

$$
0<\eta_-\le\eta(\lambda)\le\eta_+<R.
$$

根段中取 rho=t(lambda)-r。R52 的 regularized 密度 G(rho,theta;lambda)
在 rho 的 R 圆盘和统一复角条带上解析；其真实角均值写为 g(rho,lambda)。
bulk 中仍使用同一积分分部后的实际密度 J。

在本题的反射对称口径，准确相位系数为

$$
\beta(\lambda)=\frac12\left[
\int_0^b\langle J(r,\cdot;\lambda)\rangle\,dr+
\operatorname{FP}\int_0^{\eta(\lambda)}\rho^{-5/2}g(\rho,\lambda)\,d\rho
\right].
$$

因 t(lambda) 是完整无限方程的根，

$$
t'=-\frac{\partial_\lambda K_0}{\partial_rK_0}(t(\lambda),\lambda)
   =-\frac{\partial_\lambda C}{\partial_r C}(t(\lambda),\lambda),
\qquad C=a'E'-2a''E.
$$

第二式使用根上 C=0，分母为已在 root certificate 中出现的实际 C_r。
有限 DFT 的 C 在加上完整 E 与参数导数误差之前不能代入此式。

## 2. 移动上端的有限部导数

写 g(rho,lambda)=sum g_n(lambda)rho^n。所有指数 n-3/2 均非零，
因此有限部有一致收敛表示

$$
I(\lambda)=\sum_{n=0}^\infty
 \frac{g_n(\lambda)\eta(\lambda)^{n-3/2}}{n-3/2}.
$$

统一复域给 Cauchy 系数界，且 eta_+<R，故可逐项求参数导数。
前两个负幂只有有限项，不影响其余级数的一致收敛。于是

$$
I'=\operatorname{FP}\int_0^\eta\rho^{-5/2}\partial_\lambda g(\rho,\lambda)\,d\rho
 +t'\eta^{-5/2}g(\eta,\lambda).
$$

这里的偏导始终固定 rho，故它包含把实际几何评价于 t(lambda)-rho 时的根平移贡献。
又因 rho=eta 对应准确固定物理切口 r=b，端点项也可写成

$$
t'\langle J(b,\cdot;\lambda)\rangle.
$$

因此

$$
2\beta'=\int_0^b\partial_\lambda\langle J\rangle\,dr
 +t'\langle J(b,\cdot;\lambda)\rangle
 +\operatorname{FP}\int_0^\eta\rho^{-5/2}\partial_\lambda g\,d\rho.
$$

bulk 的准确 knot 分割不随 lambda 移动，所以没有隐藏的内部 knot 端点项。
每个分段内可按实际普通源的复域包络微分；有限个分段相加即可。
腰部的 Fz/r 可去性也要对参数导数统一支付，不能直接在含 r=0 的区间除以 Fz。

## 3. 完整 Taylor 与角求积误差

设整个参数区间、rho 圆盘和复角条带上有

$$
|G|\le M_0,\qquad |\partial_\lambda G|\le M_1,\qquad |t'|\le T_1.
$$

令 q=eta_+/R<1，取 N>=2。有限多项式及其准确导数是

$$
I_N=\sum_{n=0}^N\frac{g_n\eta^{n-3/2}}{n-3/2},
\qquad
I_N'=\sum_{n=0}^N\frac{g_n'\eta^{n-3/2}}{n-3/2}
 +t'\sum_{n=0}^Ng_n\eta^{n-5/2}.
$$

利用 |g_n|<=M0/R^n、|g_n'|<=M1/R^n，对 n>=N+1 的尾分别求和，得到

$$
|I'-I_N'|\le
\frac{M_1\eta_+^{N-1/2}}{(N-1/2)R^{N+1}(1-q)}
 +\frac{T_1M_0\eta_+^{N-3/2}}{R^{N+1}(1-q)}.
$$

第二项不可漏掉；它是 eta 变化时原 Taylor 余项的上端贡献。
有限多项式的正负大项应先在有向算术内相加，不应先逐项取绝对值而丢失实际消去。

若复角宽为 sigma，完整 A 点梯形均值误差为

$$
E_{A,k}=\frac{2M_k e^{-\sigma A}}{1-e^{-\sigma A}},\qquad k=0,1.
$$

Cauchy 给每个参数系数误差 |delta g_n|<=EA0/R^n、
|delta g_n'|<=EA1/R^n。因 |n-3/2|^{-1}<=2，有限部导数的额外角误差不超过

$$
\frac{2E_{A,1}\eta_-^{-3/2}}{1-q}
 +\frac{T_1E_{A,0}\eta_-^{-5/2}}{1-q}.
$$

这些费用加上普通 bulk 参数导数的径向/角向有向求积误差，便得到 beta' 的整个实参数区间包络。
这与固定一个参数点的数值差分不同：误差界必须覆盖 I 中所有 lambda。

## 4. 根 deflation 的参数导数无需除以 rho

同一根恒等式给

$$
\kappa_0^2(\rho,\lambda)=\int_0^1K_{0,r}(t(\lambda)-u\rho,\lambda)\,du.
$$

故准确双变量导数为

$$
\partial_\lambda\kappa_0^2=
\int_0^1(K_{0,r\lambda}+t'K_{0,rr})(t-u\rho,\lambda)\,du,
$$

$$
\partial_\rho\partial_\lambda\kappa_0^2=
-\int_0^1u(K_{0,rr\lambda}+t'K_{0,rrr})(t-u\rho,\lambda)\,du.
$$

因此连续复域包络可以沿用 R52 的真根积分 deflation，只新增实际混合 jets。
系数自动微分也可用双数在 native Arb radial series 上传播：一分量为值，一分量为真实参数导数。
每次根常数修正必须同时使用

$$
K_0(t(\lambda),\lambda)=0,
\qquad K_{0,\lambda}(t,\lambda)+t'K_{0,r}(t,\lambda)=0.
$$

两个常数分量均可准确置零；仅把值分量置零、却固定 t 后差分 K0，会引入不属于真实移动根的假奇性。

## 5. 接入实际 KAM 参数区间

若在 I 上证明 |beta'|<=B1，且已经取得 lambda0 的完整 beta 球 B0，那么

$$
\beta(I)\subset B_0+[-B_1d,B_1d],
\qquad d=\sup_{\lambda\in I}|\lambda-\lambda_0|.
$$

此时只要整个扩大球仍与 R34 的实际 norm 危险格分离，就可把同一 beta 条件授予
真实参数定理最终选择的 lambda。实际 B1、d、M1 和混合正则条件在当前候选尚未全部计算；
本文不把中心点诊断、有限差分斜率或另一个均值对象当成这个统一参数门。
