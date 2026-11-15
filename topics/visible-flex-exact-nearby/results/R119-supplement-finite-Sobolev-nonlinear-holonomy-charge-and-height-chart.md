# R119 续篇：有限角空间的非线性 holonomy、全 mean 源荷与真实高度图

2026-11-15，visible-exact / tail_connector。

**状态：已证明的有限 Sobolev mean 与高度图。** 本篇在同一个真实 controlled
profile、原 $\mu_j,\zeta_j$ 和 fixed-stop 对象上，给出不要求角解析性的
非线性 mean 消元。输入是有限 Sobolev 的完整非mean 两态和普通源；
输出是唯一 mean 斜率、真正 holonomy 荷、原平端高度及两个真实外端列。
它在新的有限角径向域上定义，不把输入冒称原 $\ell^1_{224}$ 标签。

这是背景变化时的一项真实新接口：既允许原零残差成员，也允许有
普通残差的近邻场。本文不由此宣布全部非mean mixed inverse、
相位选择或非线性迭代已经闭合。后继仍须支付那些算子在同一新域上的量词。

## 1. 原物理对象和不改动的尺度

采用 [原 controlled profile 全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
C.2、C.6--C.7，以及
[强深全标签规范](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
U.2 的同一尺度：
$$
 \delta_j=(2/25)2^{-j},\qquad
 \mu_j=\begin{cases}
 \varepsilon_s\delta_j^6,&j\le4096,\\
 \varepsilon_s\delta_{4096}^{3/2}\delta_j^{9/2},&j>4096,
 \end{cases}
$$
$$
 \zeta_j=\begin{cases}
 \varepsilon_s\delta_j^{39/4},&j\le8192,\\
 \varepsilon_s\delta_{8192}^{-485/4}\delta_j^{131},&j>8192.
 \end{cases}
 \tag{M.1}
$$
这里 $j\ge129$，$0<\varepsilon_s\le1$，原 $h_j$ 保持，
$$
 C_j=2^{200}h_j^{-5}{\zeta_j\over\mu_j\delta_j^2},\quad
 w={\mu_jp_*\over r^7},\quad t=\log r,\quad a_{\rm ph}=\rho r .
 \tag{M.2}
$$
所有实际接缝、两 bump、两 $\Gamma$、外端返回和帽内数据仍属于同一对象。
以下只固定其中一个真实 metric；最后单列给定 metric 方向的准确变分。

原输入逐胞给
$$
 1\le r\le2,\quad |I_j|_t<4\delta_j,\quad
 {\delta_j\over2}\le p_*\le{2^{128}\over\delta_j},\quad
 {\mu_j\delta_j\over256}\le w\le2^{129}\mu_j\delta_j^{-1}.
 \tag{M.3}
$$
实背景下 $q=w^2>0$；由 (M.1)--(M.3) 可统一用 $q<1/4$。
还可直接用
$$
 \sup_j C_j<2^{-12},\qquad
 \sigma_j={\zeta_j\over\mu_j}\delta_j^{15},\qquad
 \sup_j\sigma_j<2^{-2475}.
 \tag{M.4}
$$
第一式在首段由 $h^{-5}<2^{18}$、$\delta_{129}<2^{-132}$ 得到；
4097处的 $h^{-5}$ 跳小于 $2^{50}$，此前已有超过6000 bits余量。
后续逐段递减。第二个 supremum 在129取得：
$\sigma_{129}=\delta_{129}^{75/4}$。
所有后续规范接点保持连续，指数只增大。

角变量仍为原 $\theta$，Fourier 模为 $4\mathbb Z$，角平均归一化为1。
不使用随径向变化的角 pullback。

## 2. 新 mean 图的输入

令 $P$、$K_\perp$ 是给定的角零mean函数，置
$$
 U=P_\theta,\qquad V=(K_\perp)_\theta,\qquad K=K_\perp+\kappa(t).
$$
对任意有限整数 $s\ge2$ 定义
$$
 \mathfrak B_s=
 \sup_{j\ge129}C_j^{-1}
   \sup_{t\in I_j}
   \|(P,K_\perp,U,V)(t,\cdot)\|_{H^s}.
 \tag{M.5}
$$
只要求低 norm $\mathfrak B_2\le2^{-24}$；较高有限 norm可以另行给定。
本篇不把 (M.5) 解释成关于角变量的全纯性。

普通源采用已付 [canonical 强径向有限角域](R119-supplement-canonical-strong-radial-finite-Sobolev-domain-and-quadratic-sources.md)
的原单位
$$
 N_j={\mu_jp_*^2\over12r^{10}}e,\qquad
 \mathfrak N_s=
 \sup_j(\zeta_j\delta_j^{16})^{-1}
            \sup_{I_j}\|N_j\|_{H^s}.
 \tag{M.6}
$$
(M.6) 对任意给定有限 $s$ 只是本篇 mean 图的源 norm 定义；
它不扩大前篇 R 的逆到2114以外，也不扩大其非线性估计的0--64范围。
本节只需 $\mathfrak N_0\le1$。$e$ 是同一物理 ordinary 源，
不是裸的 weak 端荷；允许各胞的规范化 $N_j$ 按原单位变换。
物理源在真实接缝不含原子。若有原子，须另外输入它的真实 mean
荷跳量，不能从 (M.6) 凭空取得。后文的每个积分保实际方向和端点。

## 3. 消去 $q$ 的可去商及真正非线性小根

记
$$
 L=1+K,\quad E=1+q,\quad B=1-qP^2,\quad
 Z=2K+K^2+EP^2,\quad D=1-qZ,\quad {\cal J}=L+EU .
$$
原完整 angular holonomy 是
$$
 {\cal M}_q(P,K)=
 \left\langle\left(1+{qLU\over B}\right)D^{-1/2}\right\rangle .
 \tag{M.7}
$$
定义可去商
$$
 H_q(Z)={ (1-qZ)^{-1/2}-1\over q}
       ={Z\over2}\int_0^1(1-\tau qZ)^{-3/2}\,d\tau ,
$$
$$
 \Phi_q(P,K)=
 \left\langle H_q(Z)+{LU\over B\sqrt D}\right\rangle .
 \tag{M.8}
$$
于是 $\mathcal M_q=1+q\Phi_q$，包括 $q=0$ 的解析延拓；
(M.8) 不先作两个浮点大数的相减。
只要低 norm满足上述门，$B,D$ 和所用平方根支都有统一非零余量。

给定一个标量 $c$，mean 根由
$$
 \Phi_q(P,K_\perp+\kappa)=c .                              \tag{M.9}
$$
准确恒等式 $D+qL^2=EB$ 给
$$
 \partial_\kappa\Phi_q
    =\left\langle {\cal J}D^{-3/2}\right\rangle=: \langle A_0\rangle,
 \qquad |\langle A_0\rangle-1|<1/4 .                      \tag{M.10}
$$
这里 $A_0$ 不是原 $A=(\log w)_t$。

令 $n=\|(P,K_\perp,U,V)\|_{H^1}$。
由于 $\langle K_\perp\rangle=\langle U\rangle=0$，
直接展开 (M.8) 在 $\kappa=0$ 的线性项得到
$$
 |\Phi_q(P,K_\perp)|\le2^8n^2 .
$$
在 $|c|<2^{-32}$、$n<2^{-20}$ 上，
$\kappa\mapsto c-(\Phi_q-\kappa)$ 把
$|\kappa|\le2|c|+2^{10}n^2$ 映入自身，且导数小于 $1/4$。
所以唯一小根满足
$$
 |\kappa(P,K_\perp,c)|\le2|c|+2^{10}n^2.                  \tag{M.11}
$$
实输入给实根。也可在相同复 Banach 小球上使用这个收缩；
这只是有限 Sobolev 函数空间的解析映射，不提供角解析宽度。

固定 metric 时，分部积分给完整 Fréchet 微分
$$
 D\Phi_q[p,k]
   =\left\langle A_0(k-dp)\right\rangle,\qquad
 d={E(V-P)\over{\cal J}} .                               \tag{M.12}
$$
因此在给定非mean方向时
$$
 \dot\kappa=
 {\,\dot c-\langle A_0 k_\perp-E(V-P)D^{-3/2}p\rangle
       \over \langle A_0\rangle}.                       \tag{M.13}
$$
没有把 coefficient mean 与 bare Fourier mean互换。
因为 $p,k_\perp$ 的平均为零，
(M.13) 的非mean输入系数至少含一份当前背景；例如
$$
 |\dot\kappa|
 \le 2|\dot c|+
       2^{10}n\|(p,k_\perp,p_\theta,(k_\perp)_\theta)\|_{H^1}.
 \tag{M.14}
$$
二次微分也由同一个有界分母得到，不产生任何角导数损失。

## 4. 原方程给出的 nonlinear 荷恒等式

原完整非线性方程仍是
$$
 P_t=V-(A+1)P,\qquad
 K_t={\cal F}+e,\qquad A=(\log w)_t,
$$
$$
 {\cal F}={-A(2K+U+K^2+KU+qP^2)+E(V-P)^2\over{\cal J}} .
 \tag{M.15}
$$
只假定第一条运动学恒等式时，对任意 $K_t$ 已有
$$
 {d\over dt}{\cal M}_q(P,K)
   =q\left\langle A_0(K_t-{\cal F})\right\rangle .          \tag{M.16}
$$

为核对这一式并不借背景残差为零，令
$H=(1+qLU/B)D^{-1/2}$、$T=2K+U+K^2+KU+qP^2$。
对 $K$ 的变分有 $H_K=qA_0$，而
$H_P-\partial_\theta H_U=-qE(V-P)D^{-3/2}$。
此外对 $q$ 作偏导、固定 $P,K,U$，直接得到
$$
 2\partial_q H=(T-EP(V-P))D^{-3/2}
       +\partial_\theta\left({LP\over B\sqrt D}\right).
 \tag{M.17}
$$
代入 $q_t=2Aq$ 和第一条 (M.15)，角导数积分为零，
剩下的恰是 (M.16)。此证明保留全部 Fourier 模和 mean。

令真正 nonlinear 荷为
$$
 \chi={\cal M}_q-1,\qquad c=\chi/q .
$$
$\chi$ 是 nonlinear holonomy 缺陷；它的固定metric微分才是
当前真实 conormal 的平均：
$$
 D\chi[h]=\langle\pi_W[h]\rangle,\qquad
 \pi_W[h]={w{\cal J}D^{-3/2}\over\rho r}
                    (h_t-dh_\theta).
 \tag{M.18}
$$
不能在有限幅度下把 $\chi$ 直接替换成某一个冻结背景的线性通量。

## 5. 从平端到外端的完整 nonlinear Volterra 方程

给定 (M.5)--(M.6)，mean 荷必须满足
$$
 \chi(t)=\int_{t_f}^{t}
   12\mu_jr^{-4}
   \left\langle A_0(P,K_\perp+\kappa(\chi/q))N_j\right\rangle\,ds ,
 \qquad \chi(t_f)=0 .                                    \tag{M.19}
$$
积分中的 $j$ 是 $s$ 所在的实际胞元。
因 $q e=12\mu_jr^{-4}N_j$，所有 $p_*^2$ 恰好抵消，
而非将原源误作 unit Poisson 输入。

使用范数
$$
 \|c\|_\sigma=\sup_j\sigma_j^{-1}\sup_{I_j}|c(t)|.
$$
从 (M.1) 逐段看，$\mu_j\zeta_j\delta_j^{17}$ 的最小下降指数
是 $125/4>31$，规范接点不增大其连续因子。因此
$$
 \sum_{k\ge j}\mu_k\zeta_k\delta_k^{17}
          <2\mu_j\zeta_j\delta_j^{17}.                    \tag{M.20}
$$
由 $|A_0|<2$、(M.3) 及 $r^{-4}\le16$，完整当前半胞及未来胞元给
$$
 |\chi(t)|\le2^{12}\mu_j\zeta_j\delta_j^{17}\mathfrak N_0,
 \qquad
 |c(t)|\le2^{32}\sigma_j\mathfrak N_0 .                  \tag{M.21}
$$
没有截掉任何未来源。

在这个球中 (M.11) 全部适用。由 (M.10)--(M.13)，
$A_0$ 对 $c$ 的 Lipschitz 常数可取 $2^{12}$。
故 (M.19) 除以实际 $q(t)$ 后的映射，在 $\|\cdot\|_\sigma$ 中的
完整 Lipschitz 常数小于
$$
 2^{44}\mathfrak N_0\sup_j\sigma_j<2^{-2400}.              \tag{M.22}
$$
唯一固定点遂在整个无限尾上存在，按原有向积分定义。
先对完整有限尾源求解再取极限也得到同一解；(M.20)--(M.22)
的常数不依赖截断终点。$\chi$ 在真实接缝连续，
$K_0$ 由相同物理状态的小根得到，不按胞元重新选择。

真正外端 $\chi(t_{\rm out})$ 是 (M.19) 的输出；
它必须与帽、有限连接段和其他来源的真实 mean兼容等式联立，
不能因为给过平端条件而再把它设置为0。

## 6. 有限 Sobolev tame 性与非解背景的 residual 项

上述 mean 图记为
$$
 (P,K_\perp,N)\longmapsto(c,\kappa).
$$
它由统一的 pointwise 小根和真收缩组成。
所有需要的乘法与分部积分只用角 $H^1$ 代数；
因 (M.5) 已含 $P_\theta,(K_\perp)_\theta$，没有新增角导数损失。

可核的乘积工具是：对有限 $s\ge1$，
$$
 \|u^n\|_{H^s}
 \le n^s(2\|u\|_{H^1})^{n-1}\|u\|_{H^s}.
 \tag{M.23}
$$
它由 $\langle m_1+\cdots+m_n\rangle^s
\le n^{s-1}\sum_i\langle m_i\rangle^s$、
完整 Fourier 卷积和 $\ell^1\le2H^1$ 得到。
(M.8) 的可去商、平方根和两个 reciprocal 都在同一小球中
按绝对收敛幂级数应用 (M.23)。这同时证明有限 Sobolev 的连续性
与各阶 Fréchet 微分，不借 analytic-strip embedding。
对于 mean 输出本身，角 $H^s$ norm就是同一个 scalar绝对值；
(M.13) 的积分公式甚至不需要把高阶 norm灌入标量均值。

特别，令 $R=\mathfrak B_2$，完整 mean 斜率满足
$$
 |\kappa(t)|
 \le2^{10}C_j^2R^2+2^{33}\sigma_j\mathfrak N_0,\qquad
 \sup_j{|\kappa|\over C_j}
 \le2^{10}R^2+2^{-2400}\mathfrak N_0 .                    \tag{M.24}
$$
这里 $\sigma_j/C_j=2^{-200}h_j^5\delta_j^{17}$；
$h_j<1$ 和 $\delta_{129}<2^{-132}$ 支付了第二式。
两个不同来源的项仍独立保留，没有把荷项塞进背景平方。

一次变分可保如下明确局部门：
$$
 |\dot c(t)|
 \le2^{48}\sigma_j
       \{\mathfrak N_0(\dot N)+
                    \mathfrak N_0(N)\mathfrak B_2(\dot P,\dot K_\perp)\},
$$
$$
 |\dot\kappa(t)|
 \le2^{12}C_j^2 R\,\mathfrak B_2(\dot P,\dot K_\perp)
                   +2|\dot c(t)| .                      \tag{M.25}
$$
这是 (M.19) 的直接变分，唯一新反馈由 (M.22) 吸收。
再微分一次，(M.10) 的有界 inverse、(M.23) 的二次乘法及
$(1-2^{-2400})^{-1}<2$ 给统一的二次 Fréchet界；
在范数
$(\mathfrak B_2,\mathfrak N_0)\to
(\|c\|_\sigma,\sup|\kappa|/C_j)$ 中可取 $2^{256}$。
因此 (M.24)--(M.25) 是真实非线性图，不只是冻结零残差处的线性式。

对固定metric的有残差背景，准确微分 (M.19) 给
$$
 (\dot\chi)_t
 =12\mu_jr^{-4}
       \left\langle A_0\dot N+(D_WA_0[\dot W])N\right\rangle .
 \tag{M.26}
$$
第二项是确实存在的 residual-sensitive mean source。
它在这里由 (M.22)、(M.25) 支付；只在 $N=0$ 时才消失。
不能将 source-free Jacobi 的原 mean 行不加说明地转授给一般近邻场。

## 7. 这张图准确消去哪一条方程

若非mean数据同时满足
$$
 P_t=(K_\perp)_\theta-(A+1)P,\qquad
 P_\perp(K_t-{\cal F}-e)=0,                              \tag{M.27}
$$
其中 mean $K_0=\kappa$ 使用刚才的图，那么完整第二条 (M.15) 必然成立。
证明：令 $r_0(t)=K_t-{\cal F}-e$，(M.27) 说它是角常数。
由 (M.16) 与 (M.19)，
$$
 0=q\langle A_0\rangle r_0 .
$$
$q>0$ 且 $\langle A_0\rangle\ne0$，故 $r_0=0$。

反之，任何满足完整 (M.15)、平端 $\chi=0$ 且位于声明小球的解，
其 mean 必为本篇唯一图。这是一个双向等价，不凭输出维数删方程。

这里没有解掉 (M.27) 的非mean mixed 方程。
本篇取得的是在同一个有限 Sobolev 径向空间中可重复使用的
非线性 mean约束；它不授予变化背景上的完整 nonmean inverse。

## 8. 原高度的唯一恢复与两个外端输出

由 $\langle P\rangle=0$，非mean高度准确为
$$
 u_\perp=\rho rw\,I_\theta P .
$$
第一条 (M.27) 保证
$(u_\perp)_t=\rho rw K_\perp$，所以没有另加一个不相容的径向 primitive。
指定唯一平端高度 $\lambda$，mean高度是
$$
 u_0(t)=\lambda+\int_{t_f}^{t}\rho r(s)w(s)\kappa(s)\,ds .
 \tag{M.28}
$$
结合 (M.24) 和全部未来几何和可取
$$
 |u_0(t)-\lambda|
 \le\rho\,2^{256}
       \{\mu_jC_j^2R^2+\zeta_j\delta_j^{15}\mathfrak N_0\}.
 \tag{M.29}
$$
唯一可能使 $\mu C^2$ 几何和增大的4097规范跳小于 $2^{100}$；
逐段其余项均按至少9次幂下降。该跳和原 $2^{128}$ profile 高度
已完整计入256 bits。没有将每个胞元的 mean 高度重设为0。

若 (M.27) 成立且物理ordinary源连续，则使用完整第二行 (M.15)，
而非对未知粗场作两个径向微分，可得
$$
 \|u_0-\lambda\|_{C^2_r(I_j)}
 \le \rho\,2^{512}(j+5)
 \left\{\mu_jC_j^2\delta_j^{-5/2}R^2
               +\zeta_j\delta_j^{12}\mathfrak N_0\right\}.       \tag{M.30}
$$
具体地，$\langle U\rangle=0$，故
$|\langle\mathcal F\rangle-2Q\kappa|
 \le2^{12}(1+|Q|)n_{\rm full}^2$，
$Q=-A$，并保完整 $\langle e\rangle$；
再用 $|Q|<2^{12}(j+5)\delta^{-3/2}$、
$w<2^{129}\mu\delta^{-1}$ 和 $r\in[1,2]$。
由荷产生的 $\kappa^2$ 用 $\mathfrak N_0\le1$ 和 (M.4) 吸收到
显示的线性源项。荷项的最坏径向幂可粗收到 $\zeta\delta^{12}$，
没有漏 $A\kappa$。深段两个显示幂均严格为正，故 mean 高度有真实
平端 $C^2$ 延拓。完整物理 Cartesian转换仍使用原 $\rho$ 的费用。

外端同时取得
$$
 \chi_{\rm out},\qquad
 u_{0,\rm out}=\lambda+\int_{t_f}^{t_{\rm out}}\rho rw\kappa\,dt.
 \tag{M.31}
$$
一个是 holonomy荷，另一个是真高度跨度；二者不是同一个 gauge。
只有与原帽/长段的相应两条 mean 条件联立后，才得到全闭 mean 方程。

## 9. 两个真实 metric 方向及非解背景不可删的项

现在只取原两个径向 bump 的给定方向，固定材料截面、$\rho,\Omega$，
记 $\psi=\dot{\log p_*}=\dot{\log w}$。于是
$$
 \dot q=2q\psi,\quad \dot A=\psi_t,\quad
 \dot P=p-\psi P,\quad
 \dot K=k-\psi(1+K).
 \tag{M.32}
$$
$\dot U,\dot V$ 也由同一个角微分给出。
在 mean 图中必须使用
$$
 \dot c={\dot\chi\over q}-2\psi c,\qquad
 \dot\kappa=
 {\,\dot c-D_{(P,K_\perp)}\Phi_q[\dot P,\dot K_\perp]
                  -2q\psi\,\partial_q\Phi_q
       \over\langle A_0\rangle}.                         \tag{M.33}
$$
因此 profile变分既改变积分荷，也改变其真实 $q$ 归一化。

令 $\mathfrak r=K_t-\mathcal F$ 为当前 ordinary残差，
$\mathcal L_W h=k_t-D_W\mathcal F[p,k,p_\theta,k_\theta]$。
保持原 Q.17 的代数定义
$$
 e_\psi=(1+K+{\cal F}_A)\psi_t+
 \{{\cal F}-D{\cal F}[W+(0,1,0,0)]+2q{\cal F}_q\}\psi .
$$
即使 $\mathfrak r\ne0$，准确变分也可完全写出：
$$
 \dot{\mathfrak r}={\cal L}_Wh-e_\psi-\psi\mathfrak r .     \tag{M.34}
$$
这由 $\dot K_t=k_t-\psi_t(1+K)-\psi K_t$ 直接得到，
所以末项不能用“只是一次参数方向”删除。

更进一步，原归一化 residual 是
$N=c_{\rm ph}\mathfrak r$、
$c_{\rm ph}=\mu_jp_*^2/(12r^{10})$，其中 $r$ 始终为材料半径。
因为 $\dot c_{\rm ph}=2\psi c_{\rm ph}$，
$$
 \boxed{\quad
 \dot N=c_{\rm ph}({\cal L}_Wh-e_\psi)+\psi N .
 \quad}                                                  \tag{M.35}
$$
(M.34) 的 $-\psi\mathfrak r$ 与 (M.35) 的 $+\psi N$ 符号不同，
原因是 source单位本身也在变。两式不能混用。

原真实参考高度提升仍是
$$
 (h_\psi)_t=\rho rw\psi,\qquad h_\psi(t_f)=0,\qquad
 {\cal L}_Wh_\psi=\psi_t-{\cal F}_K\psi .
 \tag{M.36}
$$
令 $h=h_\psi+\widetilde h$，
$e_{\psi,\rm rem}=e_\psi-(\psi_t-{\cal F}_K\psi)$。
则完整更新式为
$$
 \dot N=c_{\rm ph}
       ({\cal L}_W\widetilde h-e_{\psi,\rm rem})+\psi N .
 \tag{M.37}
$$
新增 residual项有直接同域界
$\mathfrak N_s(\psi N)\le\sup_j\|\psi\|_{L^\infty(I_j)}
 \mathfrak N_s(N)$，因为 $\psi$ 真正径向。
它不需要2050阶或任何角解析费。

参考提升的跨胞高度积分、真实 total conormal端列和两条 $\Gamma$
都照原 Q.19--Q.27 保留；(M.37) 不把它们包进“小源”后丢掉。
本篇并未证明任意有限 Sobolev背景都有一个已选好的
$\Gamma^*(W)$。若使用原已证 $\Gamma^*(a,\Omega)$，
必须仍输入其真实强标签方向或另证新域中的选参定理。

## 10. 后继可消费的准确范围

本文已在同一 $\zeta_{131}$ 径向对象、任意给定有限角阶上构造：

- 完整 nonlinear holonomy 小根及 source charge 的唯一无限尾图；
- 不删 nonmean 到 mean 的反馈、同一个真外端荷和高度跨度；
- finite-Sobolev近邻中的无角导损失 mean tame映射；
- 有残差背景的 (M.26) 和两 metric 方向的 (M.34)--(M.37)；
- 当非mean方程解出时，完整 mean方程的双向等价及真实 mean $C^2$。

它没有把固定既知背景的2050阶逆改称 Banach收缩。
下一完整门仍是：新有限角域上的非mean背景族 inverse、
两个相位/两 $\Gamma$ 的同域选择，以及与真实帽和 $\nu$ 的联合解。
全部原角图、当前参数点和已经证明的解析强尾路线继续保留。
