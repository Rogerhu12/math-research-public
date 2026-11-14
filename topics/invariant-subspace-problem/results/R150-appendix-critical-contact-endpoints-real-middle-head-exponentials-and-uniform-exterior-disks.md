# R150 附录：临界端点的真实中头指数界与统一外盘排核

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。

状态：已证明。

本稿处理[对数权齐次稿 §10](R150-appendix-logarithmic-weighted-homogeneous-resonances-below-degree-two.md)中中心曲线消失重数判据的严格端点 $D=2m$。
旧根界需要尾根成本趋零；端点只留下一个固定成本。
这里把有限头再次分为短低头与中头，对真实 $N_j$ 的中头直接建立指数生成界，
再用有限标量逆多项式构造未知核上的测试。
所得结论是一个统一外盘：半径依赖原有限模式与原多项式，
不依赖点态幂次或复指数权。盘内、尤其零参数，仍不由本稿排除。

## 1. 原函数与端点结论

固定有限个正实权 $\alpha_1,\ldots,\alpha_q$。
沿用对数幂中心稿中的原正行
$$
a_j^{(\rho)}=\frac{\rho(\log(j+2))^{\rho-1}}{j+2},\qquad \rho>0,
$$
以及固定常数 $\kappa_\rho$ 和原函数
$$
u_\rho=-\kappa_\rho+\sum_ja_j^{(\rho)}\chi_j.
$$
令 $u_\nu=u_{\alpha_\nu}$、$X_\nu=X_{u_\nu}$。
对 $S=S_n=\log(n+2)$，实际前缀中心满足
$$
s_{\nu n}=S^{\alpha_\nu}+O(n^{-1}S^{\alpha_\nu-1}),
\qquad p_{\nu n}=s_{\nu n}/S^{\alpha_\nu}
=1+O((nS)^{-1}).
\tag{1.1}
$$

设非零标量多项式 $G$ 对原权 $\alpha$ 齐次，
$G(\mathbf1)=0$，并记其在 $\mathbf1$ 的普通消失重数为
$$
m=\min\{|\beta|:(\partial^\beta G)(\mathbf1)\ne0\}\ge1.
$$
本稿假设准确端点
$$
\boxed{D=2m,}
\tag{1.2}
$$
其中 $D$ 为 $G$ 的权次数。记 $d_0=\deg G$ 为普通总次数。

**定理 1。** 存在有限常数 $R_G>0$，仅依赖固定的原权族与 $G$，使：
若非零标量多项式 $Q$ 的全部零点满足 $|\lambda|>R_G$，则对任意原复
$\ell^2$ 第一阶指数 $w$，
$$
\boxed{Q(G(u_1,\ldots,u_q))e^w\text{ 对实际 }A\text{ 循环}.}
\tag{1.3}
$$
特别，同一个半径同时给
$$
\boxed{
[G(u)-\lambda]^r e^w\text{ 循环},
\quad |\lambda|>R_G,\quad r\ge1,\quad w\text{ 任意}.
}
\tag{1.4}
$$
常数多项式 $Q\ne0$ 按原指数循环性解释。
半径一致不表示后文截断指标或收敛速度对全部 $r,w$ 一致。

## 2. 端点的实际线性变量与有限极限多项式

只在原共同深词域上定义
$$
V_n=\frac{X_1-s_{1n}}{\alpha_1S^{\alpha_1-1}},
$$
$$
U_{\nu n}
=S^2\left[
\frac{X_\nu-s_{\nu n}}{S^{\alpha_\nu}}
-\frac{\alpha_\nu}{\alpha_1}
\frac{X_1-s_{1n}}{S^{\alpha_1}}
\right],\qquad 2\le\nu\le q.
\tag{2.1}
$$
这是有限线性变换，不应用任何无界分数幂或非线性解析换元。

为说明原有限多项式的系数，置
$$
\mathfrak G(t,v)
=G(1+\alpha_1t,1+\alpha_2t+v_2,\ldots,
1+\alpha_qt+v_q).
$$
中心曲线消失重数引理给
$$
[t^jv^\beta]\mathfrak G\ne0
\ \Longrightarrow\ j+2|\beta|\ge2m=D.
\tag{2.2}
$$
其标量证明简述如下：在零点附近取
$\rho(t)=(1+\alpha_1t)^{1/\alpha_1}$，
$\psi_\nu(t)=\rho(t)^{\alpha_\nu}-1-\alpha_\nu t=O(t^2)$。
加权齐次性使所有低于 $m$ 阶的原导数在整条 $\rho(t)^\alpha$ 曲线上消失。
因此沿横向展开只含至少 $m$ 个 $(v_\nu-\psi_\nu(t))$ 因子，
得到 (2.2)。这些局部解析函数只证明有限标量系数恒等式，不代入实际算子。

写
$$
\mathfrak G(t,v)=\sum c_{j\beta}t^jv^\beta,\qquad
\Phi(V,U)=\sum_{j+2|\beta|=D}c_{j\beta}V^jU^\beta.
\tag{2.3}
$$
这是固定有限多项式，且 $\Phi(0)=0$。
其次数不超过 $d_0$。

实际线性逆式为
$$
X_1=s_{1n}+\alpha_1S^{\alpha_1-1}V_n,
$$
$$
X_\nu=s_{\nu n}+\alpha_\nu S^{\alpha_\nu-1}V_n
+S^{\alpha_\nu-2}U_{\nu n}.
\tag{2.4}
$$
把它代入原 $G$。由 (2.2)，形式中心的每个系数带
$S^{D-j-2|\beta|}$，均有界并逐系数趋于 (2.3)。
(1.1) 的实际中心误差使每个额外系数最多为
$CS^{D-1}/n\to0$。
所以原有限多项式在这些实际字母中满足
$$
\boxed{G(X)\longrightarrow\Phi(V,U)\quad\text{逐系数}.}
\tag{2.5}
$$
(2.5) 是变化字母中的系数陈述，不是声称无界算子范数收敛。

## 3. 三段物理分解与真实尾预算

以后对每个固定 $Q,w$ 选择一个足够大的固定实数 $L$，
并令
$$
J_n=\lceil S^L\rceil.
$$
最终 $J_n<\sqrt n$，且 $J_n^4/n\to0$。
每个 (2.1) 的字母拆为：

- 位 $0\le j<J_n$ 的低头；
- 位 $J_n\le j<n$ 的中头；
- 位 $j\ge n$ 的实际补集 first。

原中心已经在 (2.1) 中扣除，所以有限头均由 $(V_j-I)$ 组成，没有额外条件收敛的尾部标量和。

令 $\theta_j=\log(j+2)/S$。切向字母 $V_n$ 的行系数准确为
$$
c_{0,nj}=\frac{\theta_j^{\alpha_1-1}}{j+2},
$$
横向字母 $U_{\nu n}$ 的行系数为
$$
c_{\nu,nj}
=\frac{\alpha_\nu S}{j+2}
\left[\theta_j^{\alpha_\nu-1}-\theta_j^{\alpha_1-1}\right].
\tag{3.1}
$$
对 $j\ge n$，令 $x=\log((j+2)/(n+2))$，则 $\theta_j=1+x/S$。
两项差的常数准确相消，故
$$
|c_{0,nj}|\le\frac{C(1+x)^B}{j+2},\qquad
|c_{\nu,nj}|\le\frac{Cx(1+x)^B}{j+2},
$$
其中 $B$ 固定。
指数分组的真实全远尾估计
$$
\sum_{j\ge n}\frac{(1+\log((j+2)/(n+2)))^B}{(j+2)^2}
\le C_B/n
$$
因此给这个有限补集族
$$
\boxed{\varepsilon_n\le C_\alpha n^{-1/2}.}
\tag{3.2}
$$
没有将 $j/n$ 限制在一个固定区间。

令 $\mathsf Q_n$ 为前 $n$ 位的整个柱投影。
[R251 §§2—3](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md)的同一补集次数尺度给所有混合伴随自然词的实际域。
若总尾长度为 $a\le n$，则
$$
\boxed{
\|\text{尾词}\,\mathsf Q_n\|
\le(C\varepsilon_n\sqrt a)^a
\le B_\alpha^a
}
\tag{3.3}
$$
，其中可取固定 $B_\alpha\ge1$，只依赖原有限权族。
此处仅需一个固定成本，不再声称它趋零。

## 4. 真实中头的指数生成界

记 $H_{\ell n}$ 为 (2.1) 各字母的中头，字母个数为固定的 $q$。
由
$$
V_j-I=-2N_j(I+N_j)^{-1},\qquad
\|(I+N_j)^{-1}\|\le3,
$$
每个中头都是真实有限和，全部因子交换。

### 4.1 包含进位修正的单因子界

若 $B$ 与 $N_j$ 交换、$\|B\|\le b$，则
$$
(N_jB)^{2h}\text{ 的范数}\le(\eta_jb^2)^h,\qquad
(N_jB)^{2h+1}\text{ 的范数}\le b(\eta_jb^2)^h,
$$
因为 $N_j^2=\eta_jN_{j+1}$、$\|N_j\|\le1$。
故
$$
\boxed{
\|\exp(N_jB)\|
\le \cosh(b\sqrt{\eta_j})
+\frac{\sinh(b\sqrt{\eta_j})}{\sqrt{\eta_j}}
\le(1+b)e^{b\sqrt{\eta_j}}.
}
\tag{4.1}
$$
这使用真实 $N_j$，不以平方为零的纯块代替它。

对 $|z_\ell|\le n$，有
$$
\sum_\ell z_\ell H_{\ell n}
=\sum_{J_n\le j<n}N_jB_j(z),\qquad
\|B_j(z)\|\le
6n\sum_\ell|c_{\ell,nj}|=:b_{nj}.
$$
实际有界交换性使指数准确分解，(4.1) 给
$$
\left\|\exp\left(\sum_\ell z_\ell H_{\ell n}\right)\right\|
\le
\prod_{J_n\le j<n}(1+b_{nj})
\exp\left(\sum_{J_n\le j<n}b_{nj}\sqrt{\eta_j}\right).
\tag{4.2}
$$

### 4.2 统一的整段中头费用

在 $J_n\le j<\sqrt n$ 上，(3.1) 粗略给
$$
\sum_\ell|c_{\ell,nj}|\le CS^2/(j+2).
$$
因此这一段对 $\sum\log(1+b_{nj})$ 的贡献最多为
$C\sqrt n\,S=o(n)$。

在 $\sqrt n\le j<n$ 上，$\theta_j$ 落在一个固定的正闭区间内。
对 (3.1) 的差作普通均值估计，得到
$$
\sum_\ell|c_{\ell,nj}|
\le\frac{C[1+\log((n+2)/(j+2))]}{j+2}.
\tag{4.3}
$$
令 $r=(n+2)/(j+2)\ge1$。
由 $1+\log r\le r$，
$$
\log(1+b_{nj})\le \log(1+C)+2\log r.
$$
而 $\sum_{j<n}\log((n+2)/(j+2))\le n+1$。
故整段对数费用为 $O(n)$。

进位修正另由真实 $\eta_j\le e^{-770\,16^j}$ 支付：
$$
\sum_{J_n\le j<n}b_{nj}\sqrt{\eta_j}
\le CnS^3 e^{-c16^{J_n}}\longrightarrow0.
\tag{4.4}
$$
于是存在只依赖原权族的常数 $K_\alpha>0$，使充分大 $n$ 时
$$
\boxed{
\sup_{|z_\ell|\le n}
\left\|\exp\left(\sum_\ell z_\ell H_{\ell n}\right)\right\|
\le e^{K_\alpha n}.
}
\tag{4.5}
$$
常数不依赖 $L$、$Q$ 或 $w$；这些参数只影响充分大指标的起点。

### 4.3 总次数不超过 n 的真实中头词

多变量 Cauchy 估计给
$$
\left\|\prod_\ell H_{\ell n}^{h_\ell}\right\|
\le
\left(\prod_\ell h_\ell!\right)n^{-h}e^{K_\alpha n},
\qquad h=\sum_\ell h_\ell.
$$
当 $h\le n$ 时，$\prod h_\ell!\le h!\le n^h$，所以
$$
\boxed{\|\text{任意长度}\le n\text{ 的中头词}\|
\le e^{K_\alpha n}.}
\tag{4.6}
$$
伴随词满足同一界。
这取代了端点上过粗的 $A_n^h$ 估计。

## 5. 完整 Bell 系数只放入短低头与小误差

固定非恒定外层 $Q$，记 $r=\deg Q$、$K=Q\circ G$。
所有系数仍对原 $X_\nu$ 和原指数 $w$ 定义：
$$
P_K(X)=\sum_\beta\frac{C_\beta^w}{\beta!}
(\partial^\beta K)(X),\qquad C_0^w=I.
\tag{5.1}
$$
[R145](R145-multimode-bell-mixed-domains-cyclicity.md) 的额外 $w$ 模式与 [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md) 给
$$
K(u)e^w=B_wP_K(X)\xi_w,\qquad \xi_w=B_w^{-1}e^w,
\tag{5.2}
$$
并支付原指数图核心与完整 $C$ 自伴规范最大图。

原对数累积量满足
$$
\kappa_\gamma
=\sum_j\left(\prod_\nu(a_j^{(\alpha_\nu)})^{\gamma_\nu}\right)
L_j^{(|\gamma|)}(w_j).
$$
[R154 §3](R154-supercubic-modes-all-polynomials-exponential-weights.md)的真实商及[完全居中幂稿 §§4—5](R150-appendix-centered-critical-powers-gradient-tail-cancellation-and-nonzero-parameters.md)的一阶加强给
$$
L_j^{(h)}(w_j)=N_jU_{hj},\quad \sup_j\|U_{hj}\|<\infty,
$$
$$
L_j'(w_j)=w_jN_jW_j,\quad \sup_j\|W_j\|<\infty.
\tag{5.3}
$$
这些是实际商，不是零字符的形式除法。
不可和原行的对数范数收敛由
$O(|w_j||\xi|+|\xi|^2)$ 与 $\ell^2$ 配对支付。

取固定整数 $M>rD$，再取固定 $L>2M+2$。
把所有所需有限个累积量准确拆在较短的 $J_n=\lceil S^L\rceil$：
$$
\boxed{S^M\kappa_\gamma=H_{\gamma n}+E_{\gamma n}.}
\tag{5.4}
$$
其中
$$
H_{\gamma n}=\sum_{j<J_n}N_jB_{\gamma j,n},\qquad
\sum_{\gamma,j<J_n}\|B_{\gamma j,n}\|\le C_wS^M.
\tag{5.5}
$$
对某个固定 $B$，原绝对系数尾与一阶 Cauchy–Schwarz 界给
$$
\begin{aligned}
\|E_{\gamma n}\|
&\le CS^M(\log(J_n+2))^B
\left[J_n^{-1}+J_n^{-1/2}\|w_{\ge J_n}\|_2\right]\\
&\longrightarrow0.
\end{aligned}
\tag{5.6}
$$
固定对数幂只产生 $(\log S)^B$，严格 $L>2M$ 足够；
无需指数权的额外尾速度。

把 (2.4) 代入原各偏导时，系数最多为 $CS^{rD}$。
每个非基础 $C_\beta^w$ 的单项式至少含一个累积量，
代入 (5.4) 后，以 $S^{rD-Mh}\le1$ 支付含 $h\ge1$ 个累积量的项。
所以整个 (5.1) 成为固定有限多项式，全部数值系数一致有界。
它的基础部分准确为 $Q(G(X))$；
每个其余项至少含一个实际低头 $H_{\gamma n}$ 或小误差 $E_{\gamma n}$。

把 (2.1) 的低头与 (5.5) 合并。
其全部显式 $N_j$ 因子均在 $j<J_n$，可取统一预算
$$
A_n\ge1,\qquad A_n\le C_wS^M.
\tag{5.7}
$$
$M>rD\ge2$ 也覆盖线性变量的 $O(S^2)$ 低头。

## 6. 低头的趋零字母权与有限次数系数范数

R251 的真实进位估计及带交换有界因子版本给：任意长度 $h$ 的低头词至多为 $A_n^h$，
而当 $h\ge2J_n$ 时至多为 $A_n^he^{-\gamma h^4}$，
$\gamma=770/16^4$。

置
$$
\delta_n=A_ne^{-\gamma(2J_n)^3}\to0,\qquad
\mathcal C_n=e^{\gamma(2J_n)^4}.
$$
对全部整数 $h\ge0$，统一得到
$$
\boxed{\|\text{低头词}\|\le\mathcal C_n\delta_n^h.}
\tag{6.1}
$$
当 $h<2J_n$ 时，用
$(A_n/\delta_n)^h\le(A_n/\delta_n)^{2J_n}=\mathcal C_n$；
当 $h\ge2J_n$ 时直接用真实进位界。
并且
$$
\boxed{\log\mathcal C_n=O(J_n^4)=o(n).}
\tag{6.2}
$$
这允许把每个低头字母赋予趋零权，而只支付一个对 $n$ 次迭代可忽略的共同前因子。

给实际有限多项式表达式的字母赋权：

- 每个低头字母的权为 $\delta_n$；
- 每个中头字母的权为1；
- 每个无界补集字母的权为 $B_\alpha$。

有界交换系数使用其算子范数；小 $E_{\gamma n}$ 可以吸收在这些系数中。
先按相同的交换单项式合并系数，再取其范数，保留基础多项式的准确有限抵消。记所得系数绝对和为 $\nu_n(P)$。
这是一个有限多项式的次乘性系数范数：
$$
\nu_n(P_1P_2)\le\nu_n(P_1)\nu_n(P_2).
$$
只是有限表达式的估计，不把实际无界算子族当作一个全域 Banach 代数。

对总字母数不超过 $n$ 的一个词，
将全部低头和中头有界因子移到实际尾词左侧。
(3.3)、(4.6)、(6.1) 给
$$
\|\text{该词}\,\mathsf Q_n\|
\le\mathcal C_n e^{K_\alpha n}
\delta_n^{h_{\rm low}} B_\alpha^{h_{\rm tail}}.
$$
所有移序只在原共同自然词域中进行；不要求这些有界因子保持补集加权范数。

故对固定次数至多 $d\ge1$ 的测试多项式 $\mathscr T_n$，
取
$$
p_n=\lfloor n/d\rfloor,
$$
便有
$$
\boxed{
\|\mathscr T_n^{p_n}\mathsf Q_n\|
\le\mathcal C_n e^{K_\alpha n}\nu_n(\mathscr T_n)^{p_n}.
}
\tag{6.3}
$$
从而
$$
\boxed{
\limsup_n
\|\mathscr T_n^{p_n}\mathsf Q_n\|^{1/p_n}
\le e^{K_\alpha d}\limsup_n\nu_n(\mathscr T_n).
}
\tag{6.4}
$$
同样适用于伴随表达式。

## 7. 只依原 G 的有限半径

令 $b_\alpha=1+B_\alpha$。
对标量多项式 $P(V,U)$，记
$$
\|P\|_{b_\alpha}
=\sum_\beta|\operatorname{coeff}_\beta(P)|\,b_\alpha^{|\beta|}.
$$
取
$$
R_0=\max(1,\|\Phi\|_{b_\alpha}),\qquad
\boxed{R_G=R_0\exp(K_\alpha d_0+1).}
\tag{7.1}
$$
这些量只依原权族与 $G$。

各原变化变量是“低头＋中头＋补集”。
低头权趋零，其余两段的总权为 $1+B_\alpha=b_\alpha$。
因此对每个固定标量多项式 $E$，由 (2.5) 的有限系数收敛，
$$
\limsup_n\nu_n(E(G(X)))\le\|E(\Phi)\|_{b_\alpha}
\le\|E\|_{R_0}.
\tag{7.2}
$$
其中对单变量 $E(z)=\sum_j e_jz^j$，$\|E\|_{R_0}=\sum_j|e_j|R_0^j$。
最后一式是有限多项式乘法的次乘性。
同时，§5 的每个非基础 Bell 项至少含一个趋零低头权或小 $E_{\gamma n}$，
所以其系数范数趋零。
这一步只用于固定有限表达式，不交换无穷次极限。

## 8. 有限逆多项式同时支付任意外层 Q

设非恒定 $Q$ 的全部零点模长大于 $R_G$。
取标量圆半径
$$
R_0e^{K_\alpha d_0}<\rho<
\min\{|\lambda|:Q(\lambda)=0\}.
\tag{8.1}
$$
标量函数 $1/Q(\zeta)$ 在该闭圆盘邻域解析。
写其 Taylor 系数为 $a_j$，并取有限多项式
$$
q_N(\zeta)=\sum_{j=0}^{N}a_j\zeta^j.
$$
Cauchy 界给 $|a_j|\le M_\rho\rho^{-j}$，其中
$M_\rho=\max_{|\zeta|=\rho}|1/Q(\zeta)|<\infty$。
因此有限误差多项式
$$
E_N(\zeta)=1-Q(\zeta)q_N(\zeta)
$$
满足
$$
\boxed{
\|E_N\|_{R_0}
\le
\frac{M_\rho\|Q\|_{R_0}}{1-R_0/\rho}
(R_0/\rho)^{N+1}.
}
\tag{8.2}
$$
此处只用标量 Taylor 级数选择一个有限 $q_N$。
后面绝不将无限逆级数代入无界 $G(X)$。

令 $\dagger$ 表示在原共同深域上的有限形式伴随：
每个有界系数取伴随、每个原 first 取伴随，并按实际词域运算。
定义
$$
\boxed{
\mathscr T_n
=I-P_K^\dagger\,q_N(G(X))^\dagger,
\qquad K=Q\circ G.
}
\tag{8.3}
$$
算子表达式本身与 $n$ 无关；下标标记其三段物理展开。
$q_N(G(X))^\dagger$ 是一个有限原词多项式，未被声称全域有界。

由于完整 Bell 的基础部分为 $Q(G(X))$，
§§5、7 给
$$
\limsup_n\nu_n(\mathscr T_n)
\le\|E_N(\Phi)\|_{b_\alpha}
\le\|E_N\|_{R_0}.
\tag{8.4}
$$
所有非基础项仍至少含一个低头或小误差；
与固定有限 $q_N(G(X))$ 相乘不改变这一点。

若 $r=\deg Q$，测试 (8.3) 的展开次数至多
$$
d_N=d_0(N+r).
\tag{8.5}
$$
理由是原 $K$ 的普通次数不超过 $rd_0$；
一个 Bell 项中累积量字母的个数不超过原偏导阶数，
而偏导已经减少同样多的普通次数。
线性变化和三段分解不增加总次数。
再乘 $q_N(G(X))$ 至多增加 $Nd_0$。

取 $p_n=\lfloor n/d_N\rfloor$。
(6.4)、(8.2)、(8.4) 给
$$
\begin{aligned}
\limsup_n\|\mathscr T_n^{p_n}\mathsf Q_n\|^{1/p_n}
&\le e^{K_\alpha d_0(N+r)}
C_{Q,\rho}(R_0/\rho)^{N+1}.
\end{aligned}
\tag{8.6}
$$
由 (8.1)，右侧随 $N\to\infty$ 几何趋零。
先选择一个固定有限 $N$ 使右侧小于 $1/2$，再让 $n\to\infty$。
于是
$$
\boxed{\|\mathscr T_n^{p_n}\mathsf Q_n\|\to0.}
\tag{8.7}
$$
有限 $N$ 可依赖 $Q$，但 (7.1) 的半径不依赖 $Q$、$r$ 或 $w$。

## 9. 未知核上的实际迭代

令 $\mathcal P_K$ 为 (5.1) 的原规范最大闭实现。
若其核投影 $\Pi\ne0$，R186 的实际共同伴随域给
$$
\Pi P_K^\dagger=0.
$$
整个 $\mathsf Q_nH$ 属于原 first 的全部有限混合伴随词域。
有限多项式 $q_N(G(X))^\dagger$ 将这共同深域送回自身；
原全部有界 Bell 系数也保持它。
因此准确有
$$
\Pi\mathscr T_n=\Pi,\qquad
\Pi\mathsf Q_n=\Pi\mathscr T_n^{p_n}\mathsf Q_n.
\tag{9.1}
$$
未知投影始终在左侧。
没有要求它与 $q_N$、变化字母或任何 $n$ 依赖系数交换，
也没有把无界 $q_N$ 的定义域扩大到全空间。

由 (8.7) 与 $\mathsf Q_n\to I$ 强，得到 $\Pi=0$，矛盾。
所以 $\mathcal P_K$ 无核。
其完整 $C$ 自伴性、原指数图核心及 (5.2) 的 $B_w$ 单位
给目标向量循环，完成定理1。

## 10. 两个端点例与范围

### 10.1 严格临界 Newton 的二模式端点

取原权 $(1,1/k)$，完全去中心的
$u=u_1$、$z=u_{1/k}$，以及
$$
G(x,y)=y^k(y^k-x).
$$
它的权次数为2，在 $(1,1)$ 的普通消失重数为1，故准确满足 $D=2m$。
这里 $d_0=2k$。
在 (2.1) 的切向、横向坐标中，
$$
\Phi(V,U)=kU+\frac{k-1}{2k}V^2.
$$
因此存在只依 $k$ 的有限 $R_k$，使
$$
\boxed{
[z^k(z^k-u)-\lambda]^r e^w
\text{ 对全部 }|\lambda|>R_k,\ r\ge1,\ w\text{ 循环}.
}
\tag{10.1}
$$
更一般可在这个共振量外复合任意零点全在该盘外的标量多项式。

临界 Newton 稿已经覆盖 $y^L(y^k-x)^a-\lambda$ 的 $L<ka$、
全部 $\lambda\ne0$。
本稿只新增端点 $L=ka$（$a\ge1$ 为整数）的外盘：
此时 $y^{ka}(y^k-x)^a=[y^k(y^k-x)]^a$，
故由完整外层多项式结论，
$[z^{ka}(z^k-u)^a-\lambda]^re^w$ 在
$|\lambda|>R_k^a$ 时循环。
这同样是整体 Bell 证明，不是循环向量相乘。

### 10.2 高消失重数的真实三模式端点

取原权 $(1,1/2,3/4)$，令
$$
G(x)=x_1\left[(x_1-x_2^2)^3+(x_3^2-x_2^3)^2\right].
$$
权次数为4，在 $\mathbf1$ 的普通消失重数为2，
因为乘子 $x_1$ 在该点非零，而最低项为
$(2h_3-3h_2)^2$。
所以仍有一个不依幂次或指数权的有限外盘结论。

本稿不声称盘内无核，也没有把 $\lambda=0$ 并入。
$D>2m$ 的一般共振、任意向量循环性、真正常见证的源上界
及普通复 Hilbert ISP 仍开放。

## 11. 完整有限 jet 的临界单位判据与端点全参数族

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。
状态：已证明；root 与 kernel 全文独立核查。

本节承接[有限 jet 稿](R150-appendix-finite-logarithmic-jets-vandermonde-tail-cancellation-and-polynomial-cyclicity.md)的同一固定原函数、数值矩阵和 jet 权。它处理缩放等号 $\delta=1$，不重计该稿已付的严格 $\delta<1$ 范围。新的输入是本稿真实中头指数界，以及在有限个变化变量中选取的有限逆多项式。

### 11.1. 原有限 jet 在临界缩放下的真实行

先合并重复原权，取两两不同的正实数
$\alpha_1,\ldots,\alpha_\ell$。
保持原 $u_{\alpha_\nu}$、$X_\nu$、$S=\log(n+2)$、
$s_{\nu n}$、$p_{\nu n}=s_{\nu n}/S^{\alpha_\nu}$。
固定可逆数值矩阵为
$$
M_{\nu r}=\alpha_\nu\binom{\alpha_\nu-1}{r-1},
\qquad 1\le\nu,r\le\ell.
$$
在原共同深域中定义
$$
Z_{\nu n}=\frac{X_\nu-s_{\nu n}}{S^{\alpha_\nu}},\qquad
\boxed{V_{rn}=S^r(M^{-1}Z_n)_r.}
\tag{J.1}
$$
这是完全线性的实际坐标变化，不使用未知部分上的逆。

令
$$
f_r(y)=\sum_\nu(M^{-1})_{r\nu}
\alpha_\nu(1+y)^{\alpha_\nu-1}.
$$
有限 jet 稿已从 $M^{-1}M=I$ 精确证明
$$
[y^h]f_r(y)=\delta_{r,h+1},\qquad 0\le h<\ell.
\tag{J.2}
$$
所以 $f_r$ 在零点至少消失到 $r-1$ 阶。
第 $r$ 个 (J.1) 的原行系数为
$$
\boxed{
c_{r,nj}=
\frac{S^{r-1}}{j+2}
f_r\!\left(\frac{\log((j+2)/(n+2))}{S}\right).
}
\tag{J.3}
$$
有限头仍由这些系数乘 $(V_j-I)$ 组成，原固定常数已被实际中心扣除。

对于 $j\ge n$，(J.2) 的真实积分余项和全远尾分组估计给
$$
|c_{r,nj}|
\le
\frac{C x^{r-1}(1+x)^B}{j+2},
\qquad x=\log((j+2)/(n+2)),
$$
故全部有限补集行共同满足
$$
\boxed{\varepsilon_n\le C_\alpha n^{-1/2}.}
\tag{J.4}
$$
当 $r=1$ 时 $x^0=1$。每个原线性 jet 的有限头绝对费用最多为
$CS^r$，合并后至多 $CS^\ell$。

### 11.2. 任意阶 jet 的真实中头指数预算

取短低头截止 $J_n=\lceil S^L\rceil$，其中固定 $L$ 稍后支付所有 Bell 项。
仍按低头 $j<J_n$、中头 $J_n\le j<n$、无界补集 $j\ge n$ 分解。

在 $\sqrt n\le j<n$ 上，(J.3) 的标量自变量落在固定区间
$[-1/2+o(1),0]$。
(J.2) 与该区间上的有界导数给
$$
\boxed{
\sum_{r=1}^{\ell}|c_{r,nj}|
\le
\frac{C[1+\log((n+2)/(j+2))]^{\ell-1}}{j+2}.
}
\tag{J.5}
$$
这是实际负自变量上的余项估计，不是把正远尾公式未经核查地延伸过去。
在 $J_n\le j<\sqrt n$ 上，粗界为
$$
\sum_r|c_{r,nj}|\le CS^\ell/(j+2).
\tag{J.6}
$$
因为 $\theta=\log(j+2)/S\ge1/S$，
每个 $\theta^{\alpha_\nu-1}$ 至多为固定常数乘 $S$。

对中头 $H_{rn}$ 及 $|z_r|\le n$，本稿 (4.1) 的真实因子界
$$
\|\exp(N_jB)\|\le(1+\|B\|)e^{\|B\|\sqrt{\eta_j}}
$$
完全适用。
(J.6) 的早中段对数费用为 $O(\sqrt n\,S)=o(n)$。
在 (J.5) 的其余中段，令 $t=(n+2)/(j+2)\ge1$，由
$t(1+\log t)^{\ell-1}\le t^\ell$ 得
$$
\log\left(1+6n\sum_r|c_{r,nj}|\right)
\le C+\ell\log t.
$$
求和是 $O(n)$。
真实进位误差另由
$$
CnS^{\ell+1}e^{-c16^{J_n}}\to0
$$
支付。因此存在只依原固定权族的 $K_\alpha>0$，使
$$
\boxed{
\sup_{|z_r|\le n}
\left\|\exp\left(\sum_rz_rH_{rn}\right)\right\|
\le e^{K_\alpha n}.
}
\tag{J.7}
$$
Cauchy 给所有总长度不超过 $n$ 的中头词同一界。
(J.4) 和 R251 则给所有长度 $a\le n$ 的补集词至多 $B_\alpha^a$，
其中 $B_\alpha\ge1$ 同样只依原权族。

### 11.3. 原完整 Bell 与通用有限系数单位准则

固定任意原标量多项式 $K$，并假设存在实数 $b\ge0$，使把实际有限变化
$$
x_\nu=S^{\alpha_\nu}
\left[p_{\nu n}+\sum_{r=1}^{\ell}M_{\nu r}S^{-r}v_r\right]
\tag{J.8}
$$
代入后有逐系数极限
$$
\boxed{S^{-b}K(x(v,n))\longrightarrow P_\infty(v).}
\tag{J.9}
$$
这些都是固定有限多项式的系数，不是无界算子范数极限。

设 $W$ 为 $K$ 的原最大权次数。
(J.8) 中各 $x_\nu$ 的系数均为 $O(S^{\alpha_\nu})$，
所以全部原偏导代入、再乘 $S^{-b}$ 后，系数至多为 $CS^W$。
取整数 $M_0>\max(\ell,W)$，再取 $L>2M_0+2$。
原完整 Bell 的全部所需累积量准确拆为
$$
S^{M_0}\kappa_\gamma=H_{\gamma n}+E_{\gamma n},
\qquad
H_{\gamma n}=\sum_{j<J_n}N_jB_{\gamma j,n},
$$
$$
\sum_{\gamma,j<J_n}\|B_{\gamma j,n}\|\le C_wS^{M_0},
$$
$$
\|E_{\gamma n}\|
\le CS^{M_0}(\log(J_n+2))^B
\left[J_n^{-1}+J_n^{-1/2}\|w_{\ge J_n}\|_2\right]\to0.
\tag{J.10}
$$
这里保留一阶 $L_j'(w_j)=w_jN_jW_j$ 及全部混合高阶项，
正是本稿 §5 的原实际分解。

每个非基础 Bell 项至少含一个累积量，故其数值系数由
$S^{W-M_0h}\le1$ 支付。
所有这类项进入短低头或小有界系数。
把原线性变量的低头一并加入，低头预算
$A_n=\max(1,\text{全部低头绝对费用})\le C_wS^{M_0}$。
本稿 §6 给全部低头词
$$
\|\text{低头词}\|
\le\mathcal C_n\delta_n^h,\qquad
\delta_n\to0,\qquad \log\mathcal C_n=O(J_n^4)=o(n).
$$

沿用权为 $\delta_n$、1、$B_\alpha$ 的低头、中头、补集系数范数
$\nu_n$，并在每个实际有限单项式先合并系数再取范数。
对任何固定次数至多 $d$ 的测试多项式，仍准确有
$$
\boxed{
\limsup_n
\|\mathscr T_n^{\lfloor n/d\rfloor}\mathsf Q_n\|^{1/\lfloor n/d\rfloor}
\le e^{K_\alpha d}\limsup_n\nu_n(\mathscr T_n).
}
\tag{J.11}
$$
所有非基础 Bell 项在此系数范数中趋零。
每个实际变化变量的剩余中头加补集总权为
$$
b_\alpha=1+B_\alpha.
$$

取只依原权族的固定半径
$$
\boxed{R_\alpha=b_\alpha e^{K_\alpha+1}.}
\tag{J.12}
$$

**临界单位准则。** 如果 (J.9) 成立，且
$$
\boxed{
P_\infty(v)\ne0
\quad\text{对所有 } |v_1|,\ldots,|v_\ell|\le R_\alpha,
}
\tag{J.13}
$$
则对全部原复 $\ell^2$ 指数权 $w$，
$$
\boxed{K(u_{\alpha_1},\ldots,u_{\alpha_\ell})e^w
\text{ 对实际 }A\text{ 循环}.}
\tag{J.14}
$$
(J.13) 是一个有限标量多项式的真实紧集非零条件；
没有把一般 $A'$ 当作一个局部代数。

### 11.4. 多变量有限逆的完整证明

由 (J.13)，$1/P_\infty$ 在该闭复多圆盘邻域解析。
写 Taylor 系数为 $a_\beta$，则多变量 Cauchy 给
$$
|a_\beta|\le C R_\alpha^{-|\beta|}.
$$
取总次数不超过 $N$ 的有限多项式
$$
q_N(v)=\sum_{|\beta|\le N}a_\beta v^\beta,\qquad
E_N(v)=1-P_\infty(v)q_N(v).
$$
记 $\|\cdot\|_{b_\alpha}$ 为普通有限多项式的
$b_\alpha^{|\beta|}$ 加权系数绝对和。
因为次数 $h$ 的单项式数为 $\binom{h+\ell-1}{\ell-1}$，
几何尾和给
$$
\boxed{
\|E_N\|_{b_\alpha}
\le C(N+1)^{\ell-1}
(b_\alpha/R_\alpha)^{N+1}.
}
\tag{J.15}
$$
常数可依赖 $P_\infty$，但不依赖 $N$。

令 $P_K$ 为原完整 Bell 多项式，$\dagger$ 仍表示共同深域上的有限形式伴随。
构造
$$
\boxed{
\mathscr T_n
=I-S^{-b}P_K^\dagger\,q_N(V_{1n},\ldots,V_{\ell n})^\dagger.
}
\tag{J.16}
$$
这里 $q_N$ 固定有限；
每个 $V_{rn}$ 是 (J.1) 的原有限线性词。
没有把无限逆 Taylor 级数代入无界算子，也未声称 $q_N(V_n)$ 全域有界。

由 (J.9)—(J.10)，基础部分逐系数趋于
$1-P_\infty q_N=E_N$，
其余项都有一个趋零低头权或小误差。
所以
$$
\limsup_n\nu_n(\mathscr T_n)\le\|E_N\|_{b_\alpha}.
$$
若 $d_K=\deg K$，测试 (J.16) 的字母次数至多 $d_K+N$；
完整 Bell 的累积量字母个数不超过偏导已经减掉的普通次数。
由 (J.11)，
$$
\limsup_n
\|\mathscr T_n^{\lfloor n/(d_K+N)\rfloor}\mathsf Q_n\|^{1/\lfloor n/(d_K+N)\rfloor}
\le
e^{K_\alpha(d_K+N)}
C(N+1)^{\ell-1}
(b_\alpha/R_\alpha)^{N+1}.
\tag{J.17}
$$
(J.12) 使右侧随 $N\to\infty$ 几何趋零。
先选固定有限 $N\ge1$ 使其小于 $1/2$，再令 $n\to\infty$。

若 $\Pi$ 是原规范 $\mathcal P_K$ 的非零核投影，
原共同伴随深域给 $\Pi P_K^\dagger=0$。
每个有限的 $q_N(V_n)^\dagger$ 保持该全部自然词域，
整个 $\mathsf Q_nH$ 也在其中。
因此
$$
\Pi\mathsf Q_n=
\Pi\mathscr T_n^{\lfloor n/(d_K+N)\rfloor}\mathsf Q_n.
$$
未知投影始终在左侧；所有 $n$ 依赖系数和无界有限词都没有穿过它。
(J.17) 使右侧范数趋零，故 $\Pi=0$。
原 $C$ 自伴性、原指数图核心及 $B_w$ 单位随后给 (J.14)。

### 11.5. 有限 jet 的弱不等式端点

保持有限 jet 稿的分解
$$
F=\sum_DG_D,\qquad
\mathcal J_D(t)=G_D(\mathbf1+Mt),\qquad
\omega(\beta)=\sum_{r=1}^{\ell}r\beta_r,
$$
及 $\nu_D$ 的最低 jet 权。

若存在非零曲线分量，令
$$
d_0=\max\{D:G_D(\mathbf1)\ne0\},\qquad
c_0=G_{d_0}(\mathbf1)\ne0.
$$
把原严格条件放宽为
$$
\boxed{D>d_0\ \Longrightarrow\ D-d_0\le\nu_D.}
\tag{J.18}
$$
有限系数逐项代入 (J.8) 即得
$$
S^{-d_0}F(x(v,n))\longrightarrow\Phi_F(v),
$$
$$
\boxed{
\Phi_F(v)=
\sum_{\substack{D,\beta\\D-d_0=\omega(\beta)}}
[t^\beta]\mathcal J_D(t)\,v^\beta.
}
\tag{J.19}
$$
真实中心误差仍由有限对数幂乘 $n^{-1}$ 支付。
$\Phi_F(0)=c_0$，其非恒定部分只来自原等号分量。

如果 $d_0>0$ 且 $\Phi_F$ 在 (J.13) 的闭多圆盘上无零，
则对任意非零外层多项式 $Q$，
$$
\boxed{Q(F(u))e^w\text{ 循环}.}
\tag{J.20}
$$
证明是对整个原 $K=Q\circ F$ 应用单位准则：
令 $q=\deg Q$，其归一极限为
$\operatorname{lc}(Q)\Phi_F^q$，尺度为 $S^{qd_0}$。
若 $d_0=0$，则只需 $Q(\Phi_F(v))$ 在该闭多圆盘上无零，
直接以 $b=0$ 使用同一准则。
这些仍是完整原 Bell 的证明，不是循环向量的乘法规则。

若每个 $G_D(\mathbf1)=0$，而所有 $D\le\nu_D$，
则同理有 $F(x(v,n))\to\Phi_F(v)$，
其中 (J.19) 取 $d_0=0$。
只要 $Q(\Phi_F)$ 在该闭多圆盘无零，仍有 (J.20)。
特别存在一个不依幂次及指数权的有限外盘，
覆盖全部 $[F(u)-\lambda]^re^w$。
当所有不等式严格时 $\Phi_F=0$，准确退回原 $Q(0)\ne0$ 范围。

一个便于有限系数检验的充分条件是
$$
|c_0|>
\sum_{\beta\ne0}
|\operatorname{coeff}_\beta(\Phi_F)|R_\alpha^{|\beta|}.
\tag{J.21}
$$
它直接使 $\Phi_F$ 在整个闭多圆盘上离零，而不需要寻找未知算子谱。

### 11.6. 同一小系数覆盖全部 L 的端点全参数族

回到二模式原权 $(1,1/k)$，$k\ge2$，令 $u=u_1,z=u_{1/k}$。
此时
$$
M=
\begin{pmatrix}
1&0\\
1/k&-(k-1)/k^2
\end{pmatrix}.
$$
对 $g(x,y)=y^k-x$，其最低 jet 权为2，准确的二阶 jet 是
$$
\boxed{
\Psi_k(v_1,v_2)
=\frac{k-1}{2k}(v_1^2-2v_2).
}
\tag{J.22}
$$
取任意整数 $L\ge1$，定义原多项式
$$
F_{L,\varepsilon}(x,y)
=y^L+\varepsilon y^{L+k}(y^k-x).
\tag{J.23}
$$
较低曲线分量权为 $d_0=L/k>0$、字符为1；
较高分量权为 $d_0+2$、jet 阶恰为2（$\varepsilon\ne0$ 时）。
所以它准确落在 (J.18) 的等号端点，原严格 Newton 条件不覆盖。

实际归一极限为
$$
\boxed{\Phi_{L,\varepsilon}=1+\varepsilon\Psi_k,}
\tag{J.24}
$$
与 $L$ 无关。
令 $R_\alpha$ 为此二模式的 (J.12) 半径，并取
$$
\boxed{
\varepsilon_k=
\frac{k}{(k-1)(R_\alpha^2+2R_\alpha)}>0.
}
\tag{J.25}
$$
对任意复数 $|\varepsilon|\le\varepsilon_k$，
$$
|\varepsilon\Psi_k(v)|
\le\frac12
\qquad (|v_1|,|v_2|\le R_\alpha).
$$
故 (J.24) 在整个闭多圆盘离零至少 $1/2$。
由 (J.20)，同一个 $\varepsilon_k$ 同时给全部 $L\ge1$：
$$
\boxed{
Q\!\left(z^L+\varepsilon z^{L+k}(z^k-u)\right)e^w
\text{ 对任意非零 }Q\text{ 循环}.
}
\tag{J.26}
$$
特别全部谱参数 $\lambda\in\mathbb C$、整数 $r\ge1$、原指数 $w$ 的
$$
\left[z^L+\varepsilon z^{L+k}(z^k-u)-\lambda\right]^re^w
$$
均循环。
这是对一个原端点多项式的整体证明；既未把两个循环因子相乘，也未借用尾原子的循环性。

### 11.7. 普通简单零点而任意高临界 jet 的外盘

有限 jet 稿构造
$$
G_{R,D}(x)=\sum_{p=1}^R c_px_p^p,\qquad
\alpha_p=D/p,\qquad
c_p=\left[\prod_{q\ne p}(1/p-1/q)\right]^{-1}.
$$
它的普通消失阶为1，最低 jet 权准确为 $R$。
原稿已经覆盖 $D<R$ 的全部非零参数。
现在取准确端点 $D=R$，则 (J.19) 的极限是一个固定非零有限多项式，
其 $v_R$ 系数为 $R^R/(R-1)!$。
本节因此给一个有限外盘，半径不依幂次或指数权。
这包含 $R>2$ 时普通消失阶判据 $D=2m$ 本身不包含的端点。

例如
$$
G(x)=x_1-4x_2^2+3x_3^3,\qquad
\alpha=(3,3/2,1),
$$
的临界极限准确为
$$
\Phi_G(v)=\frac92v_3-9v_1v_2+3v_1^3.
$$
所以存在有限 $R_*>0$，使
$$
[u_3-4u_{3/2}^2+3u_1^3-\lambda]^re^w
$$
对全部 $|\lambda|>R_*$、$r\ge1$、$w$ 循环。
三项的原混合 Bell 系数全部由前述短低头与小尾支付。

### 11.8. 剩余范围

(J.13) 是实际支付过的有限系数单位条件。
原弱不等式本身不保证它成立；
本节不把有零的极限多项式、盘内共振或零参数自动纳入。
$D-d_0>\nu_D$ 的一般分量、无这些预算的任意慢行、
真正常见证源上界、任意向量循环性及普通复 Hilbert ISP 继续开放。

## 后续：合并矩方法与已解除的参数限制

[复对数合并矩池](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)以不同的正则化/矩阵提升方法，现已证明任意两个不同复对数模式的全部非零普通多项式，以及本系列 G_R 高阶共振族在所有 Re𝔇>0 下的全部参数、点态幂和指数权，包含零参数。原函数及固定中心不变；本稿已证的柱预算、单位条件和较多模式的其他范围仍保持各自准确假设。一般目标的最高合并矩系数全部为零时，不由新定理自动处理。
