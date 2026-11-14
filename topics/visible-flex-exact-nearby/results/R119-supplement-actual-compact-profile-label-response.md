# R119 续篇：compact 控制的实际全标签响应与完整 gauged 场的 rho5 传播

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本文把前篇的真实局部 forcing 传播到原完整标签
空间，不再停在一个尚未传播的 $\rho^5$ 积分上。
固定当前 $\Gamma$、原内部标签及其真实解 $X$。
若方向 $\psi$ 支持在第 $j\ge8193$ 层的真实下降坡
$x\in(7/16,15/32)$，满足前篇 (C.5)，则
$$
 \boxed{\quad
 \|D_\psi X\|_{\mathcal X_\beta}
 <2^{768} h_j^{-14}\delta_j^{-7/4}\rho^5
                                  \|X\|_{\mathcal X_\beta}.
 \quad}                                                     \tag{L.1}
$$
假设为 $\beta\ge224$、$\|X\|_{\mathcal X_\beta}\le2^{-262144}$；
真正 incoming 已在此球内。没有放宽原标签权，也没有加入一个未授予的
更宽标签输入。

本文还给整条实际尾上的 **gauged** 物理梯度变分，而不把局部
$\psi F_1$ 的 $\rho^4$ 项塞回该量：
$$
 \boxed{\quad
 \widehat n_i
 <2^{832}(N_i^c)^\#\|X\|_{\mathcal X_\beta}
           h_j^{-14}\delta_j^{-7/4}\rho^5 .
 \quad}                                                     \tag{L.2}
$$
这里 $\widehat n_i$ 含 $(\widehat p,\widehat k)$ 的前两个完整角导数，
按真实 $w$ 逐点归一，在固定物理角条带2上取 norm。
它正是前篇实际两射线 (C.23) 的响应列。独立高度、holonomy mean、
普通及 weak 源单位的参数项都在下文保留。

(L.1)–(L.2) 不是整个 $\mathcal F=0$ 的逆，也不把未付的物理
principal 端图当成恒等。下一消费者是完整两射线、fixed-label
kernel 以及同当前 $\Gamma$ 的散射导数。

## 1. 同一对象、空间及一个真正更好的 profile 上界

采用[控制后全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
和[实际 compact 通量规范](R119-supplement-actual-compact-profile-flux-gauge-and-principal-port-derivative.md)。
本篇所有 $p,k,w,J,D,f,F_1,\mathcal R$ 均按后一篇定义。
当前两个 bump 参数不随这个偏导变化；之后的
$D_\Omega\Gamma^*$ 两列另按其真实链式法则加入。

写 $\delta=\delta_j$、$h=h_j=8\delta^{1/256}$、
$\eta=\delta^{3/2}/(4\sqrt2)$、$\mathsf K=2^{128}$。
归一仍为
$$
 X_{m,j}=(-1)^j\zeta_j^{-1}e^{|m|\tau_j}V_{m,j},
 \qquad \tau_j-\tau_{j-1}=h .
 \tag{L.3}
$$
$\mathcal X_\beta$、$\mathcal F_\beta$ 始终先对每个 Fourier 模取径向
上确界，再求全部模的和。

在实际下降坡的 $J_x=[7/16,15/32]$，
$S=10x^3-15x^4+6x^5$ 满足 $S>3/8$。
第一下降坡的未扰 profile 是
$\mathsf K^{1-S}\alpha^{-S}\delta^{2S-1}$；
第二下降坡是 $C^S\delta^{S-1}$，$C=16\sqrt2<64$。
两个原 bump 支集离开 $J_x$；当前全部 compact 形状的
$C^0$ norm 小于 $2^{-20}$，指数因子小于2。
因此在本方向的整个真实支集，
$$
                 0<p_*<2^{129}\delta^{-5/8}.             \tag{L.4}
$$
这里不用全胞较粗的 $\mathsf K/\delta$。
任意既有实 slide 只平移同一坡坐标，不改变这个上界。
两个全局规范逆幂仍在原 $\zeta/\mu$ 中，未从 (L.4) 删除。

## 2. 任意截短子区间的真正全频局部图

本节说明以下传播没有引用一个未证明的 arbitrary-source Green。

对本胞元任意有向内部子区间，保留原 canonical 状态 $W$。
第53束 (C.12) 的内部真低窗界 $2^{140}M^4$ 适用；
截短只减少原有序 Gauss 面积，每个大剪切仍只出现一次。
第53束 (C.17) 的完整 nonlinear 积分界也只减少。
实际分段数至多9，原完整压缩 leading 逆、mean 小根和
Galerkin residual 恒等式都不改变。

把原角宽支出记为一般 $b>0$，取
$$
 J(b)=4\left\lceil4096(1+|\log\delta|)/b\right\rceil,\qquad
 R(b)=2^{-352}\mu_j\delta^2 b^5J(b)^{-5}.                 \tag{L.5}
$$
原有限 Picard、真实强修正及逐频输出 Cauchy 的证明于是直接在该
截短区间给
$$
 \Phi_{s,t}:B_{\mathcal A_{\sigma+b}}(R(b))
                         \longrightarrow\mathcal A_\sigma,
 \qquad
 \|\Phi_{s,t}(U)\|<2^{158}b^{-5}\|U\| .                  \tag{L.6}
$$
这是完整零 residual Cauchy 图；不是有限投影。
任意内部端点使用 $W$ 的准确 canonical 单位。
原全胞末端再乘 $\operatorname{diag}(1,C^{-1})$ 只减小 norm，
所以删掉该末端转换并未使 (L.6) 失效：其证明本来使用完整
$W$ 内部流界。

同一完整解的物理输出还满足第53束 (C.23) 的相对四态界
$2^{200}(\mu\delta^2)^{-1}b^{-5}\|U\|$。
所有 mean 已由 $M=1$ 的真实小根定义；整体平均高度常数不参与
$p,k$ 的 Cauchy 方程，最终仍独立积分。

只需 $b=h/2,h/4$。准确有
$J(h/4)\le4J(h)$、$R(h/4)\ge2^{-20}R(h)$；
这些新的截断也满足 $J(b)\le2^{-5}\delta^{-3/8}$。
例如 $J(h/4)<2^{17}(j+5)/h$，由
$\log_2(j+5)\le j/128$、$\delta>2^{-(j+4)}$，
在 $j=8193$ 已远小于该真实 cutoff，之后相对指数继续减小。
原 $J(b)b/4\ge4096(1+|\log\delta|)$ 始终准确保留。

## 3. 先支付实际背景落入每个内部 Cauchy 球

令 $X_*=\|X\|_{\mathcal X_\beta}$，$\sigma_o=\tau_{j-1}+\beta$。
原端点输入为 $\|U_j\|_{\mathcal A_{\sigma_o+h}}\le\zeta_jX_*$。
以 $b=h/2$ 重新构造本胞元完整图，得到在
$\sigma_m=\sigma_o+h/2$ 上的同一真实解；其与原较窄图的识别来自
实际 IVP 唯一性，未先假设原解已经增宽。
可安全取
$$
 n_m:=
 \sup_{\rm cell}\|(p,k,p_\theta,k_\theta)/w\|_{\mathcal A_{\sigma_m}}
 <2^{210}h^{-5}\frac{\zeta_j}{\mu_j\delta^2}X_* .
 \tag{L.7}
$$
额外5 bits 支付 $b=h/2$，再5 bits 支付各物理分量的求和。
所需输入球在下一段一并验证。

在任意内部时刻 $s$，从 $p,k$ 回到 $W$，取
$\sigma_1=\sigma_o+h/4$。真实第一行含
$\nu_m\partial_\theta^{-1}$，故使用
$|\nu_m/m|\le M^3/12$ 和这 $h/4$ 余宽。
第二行是 $p_*(k+p_\theta)/(\sqrt{12}r^3)$。
在全胞仍使用原 $p_*\le2^{128}\delta^{-1}$，得到
$$
 \|W(s)\|_{\mathcal A_{\sigma_1}}
   <2^{480}h^{-8}\delta^{-4}\zeta_jX_* .                \tag{L.8}
$$
这里没有用 (L.4) 去估计支集之外的背景。

原真实球账在首新层给 $\zeta_j/R(h)<2^{-19689}$。
由 $h^{-8}\delta^{-4}$ 的真实首层值及
$R(h/4)\ge2^{-20}R(h)$，(L.8) 给
$$
 \frac{\|W(s)\|_{\mathcal A_{\sigma_1}}}{R(h/4)}
                     <2^{14000}X_*<2^{-248144}<1/4.   \tag{L.9}
$$
这覆盖所有更深层：除固定全局因子外，相邻层
$h^{-8}\delta^{-4}\zeta/R(h)$ 的精确式正比于
$\delta^{249/2-4-13/256}J(h)^5$；
$J(h_{j+1})\le2J(h_j)$，其比小于
$2^{5-(249/2-4-13/256)}<1$。
首层的真实规范因子没有被重新定义。

同样 $\|U_j\|/R(h/2)\le2^{10}\zeta_jX_*/R(h)<1/4$，
所以 (L.7) 的较宽实际构造合法。
并且 (L.7) 的右端小于
$2^{-142}(\zeta_j/R(h))J(h)^{-5}X_*\ll1/64$；
全部所需 mean/leading 逆球在传播前已支付。

(L.6) 的完整全纯图在实际 $W(s)$ 周围取半径 $R(h/4)/2$ 的
方向圆盘，Cauchy 给真正线性化传播
$$
 \boxed{\quad
 \|D\Phi_{s,t}(W(s)):
       \mathcal A_{\sigma_1}\to\mathcal A_{\sigma_o}\|
                         <2^{170}h^{-5}.
 \quad}                                                     \tag{L.10}
$$
这是实际非零背景的全频导数，不是径向参考矩阵的替代。
同一 Cauchy 对物理相对四态输出给
$2^{212}(\mu\delta^2)^{-1}h^{-5}$。
所有费用与 $s,t$ 统一；对源积分时不反复支付新的角宽。

## 4. Canonical forcing 的真实两个分量与 mean 适配

前篇的物理修正是 $\widehat z=\dot z-\psi F_1$。
原 canonical 状态的 $p_*$ 微分也必须保留。
准确有
$$
 \widehat W=\dot W-\psi\mathcal B_W=\mathcal T\widehat z,
 \qquad
 \mathcal R_W=\mathcal T\mathcal R.                      \tag{L.11}
$$
第二式既可将前篇 (C.19) 展开，也可直接微分第一式得到。
它把抽象 bracket 化成完整可计算的两个源：
$$
 \boxed{\quad
 (\mathcal R_W)_1=\frac{\nu_m}{\sqrt{12}r^3}f_{\perp,m},
 \qquad
 (\mathcal R_W)_2=\frac{p_*}{\sqrt{12}r^3}
                       \Pi_\perp(\mathcal R_k+\partial_\theta\mathcal R_p).
 \quad}                                                     \tag{L.12}
$$
其中 $\mathcal R_p=f_\theta/\sqrt{12}$，
$\mathcal R_k$ 是前篇 (C.8) 的完整表达式。
特别第一行一般非零，不能按 ordinary second-row source 处理。

注入这个源并未删除 mean。把状态扩充为 $(p,k,w)$，
令 $\mathcal U=(V,0)$、$\mathcal B=(F_1,w)$。
前篇 (C.11) 给 $\mathcal BM=0$，(C.12) 给
$\mathcal UM=0$（完整周期积分后）。
而 $(\mathcal R,0)=D\mathcal U\,\mathcal B-D\mathcal B\,\mathcal U$，
所以
$$
                       D_zM[\mathcal R]=0.              \tag{L.13}
$$
因此每个真实 source impulse 都在同一个 $M=1$ 切空间。
由实际非mean $W$ 恢复其 mean 时，原 mean 小根的导数准确给
$\mathcal R_k$ 的 mean；没有先投掉它再任意补零。
另一条件 $\langle\mathcal R_p\rangle=0$ 来自 $f_\theta$。

## 5. 对真实非零背景支付完整源，而不重新制造方向导数

令 $g=\sigma_m-\sigma_1=h/4$。
在 $\sigma_m$ 上，前篇的实际代数给
$\|f\|\le8wn_m$、$\|k_\theta-p\|\le2wn_m$。
所有额外角导使用这个已经给定的 $g$。
由前篇完整 $\mathcal R_k$ 可取
$$
 \|\mathcal R_k\|_{\mathcal A_{\sigma_1}}
                     <32wn_m/g,\qquad
 \|\partial_\theta\mathcal R_p\|_{\mathcal A_{\sigma_1}}
                     <3wn_m/g^2 .
$$
第一式保留 $\mathcal R_k$ 的全部三项；用 $n_m\le1/64$、
$g\le1$ 即得到显示常数。
第一行 $\nu_m f$ 则以
$\sup M^4e^{-gM}\le(4/(eg))^4$ 付清。
两行一起给
$$
 \|\mathcal R_W\|_{\mathcal A_{\sigma_1}}
 <32wn_m(g^{-4}+p_*g^{-2})
 \le2^6\mu_j(2^{129}\delta^{-5/8})^2n_mg^{-4}.
$$
最后一步仅在真实 compact 支集使用 (L.4)。
代入 (L.7)，得到
$$
 \boxed{\quad
 \sup_{\operatorname{supp}\psi}
 \|\mathcal R_W\|_{\mathcal A_{\sigma_1}}
 <2^{490}\delta^{-13/4}h^{-9}\zeta_jX_* .
 \quad}                                                     \tag{L.14}
$$
实际 $dy=\eta\,dx$ 及 $\int|\psi|dx\le2\rho^5$ 随即给
$$
 \int\|\psi\mathcal R_W\|_{\mathcal A_{\sigma_1}}dy
 <2^{491}\eta\,\delta^{-13/4}h^{-9}\zeta_jX_*\rho^5.
 \tag{L.15}
$$
这里 $\psi_y$、$\psi_{yy}$ 都没有进入源 norm。
原当前 $p_*,w,\Gamma$ 及完整 angular convolution 均未冻结为常数。

## 6. 真实局部有源输出到原 $\mathcal F_\beta$、$\mathcal X_\beta$

取固定输入的局部 profile 变分，初值 $\widehat W=0$。
准确的参数常数变易为
$$
 \widehat W(t)=
 \int D\Phi_{s,t}(W(s))[\psi(s)\mathcal R_W(s)]\,ds .
 \tag{L.16}
$$
先对光滑角数据由原完整 variational 方程证明，
再由 (L.10)、(L.15) 的统一强界作 Bochner 极限。
源 (L.13) 始终属于同一真实 mean 图的切空间。
这条实际有源公式包括第一行 forcing，不是只保一个高度 particular。

端点 $\psi=0$，所以 $\widehat W=\dot W$。
由 (L.10)、(L.15)，局部完整输出小于
$2^{661}\eta\delta^{-13/4}h^{-14}\zeta_jX_*\rho^5$。
恢复原端口第二行 $C^{-1}$、符号和
$e^{M\tau_{j-1}}/\zeta_{j-1}$，它准确成为第 $j$ 行的 $g_\psi$。
因 $\zeta_j/\zeta_{j-1}<1$，$\eta<\delta^{3/2}/4$，
$$
 \boxed{\quad
 \|g_\psi\|_{\mathcal F_\beta}
 <2^{672}h^{-14}\delta^{-7/4}\rho^5X_* .
 \quad}                                                     \tag{L.17}
$$
同一输出 norm 仍包括全部 Fourier；没有对高模式删行或换序。
本方向只有这一行源，所以上式直接是原 $\mathcal F_\beta$ norm。

全图的准确变分方程是前篇 (C.21)。
原 $\|\mathcal G\|<2^{16}$ 和完整 nonlinear feedback
$\|\mathcal G D\mathscr N(X)\|<1/2$ 给
$$
 \|D_\psi X\|<2^{17}\|g_\psi\| ,
$$
从而证明 (L.1)，常数实际在 $2^{689}$ 内，统一放宽为 $2^{768}$。
该公式改变的是同一真解 $X$，并固定全部原内部标签，不只指定 cut128
低高度，也不改变真正 mean 条件。

有限或绝对可和的多方向可以线性相加：
每个方向用自己的 $j,\rho$ 和实际系数，累加 (L.17) 的右端。
本文不在未证明强卷积提升前把这个加和换成任意 $\ell^\infty$ 参数 norm。

## 7. 真正 gauged 物理场及完整高度 mean

令
$$
 P_j=h_j^{-14}\delta_j^{-7/4},\qquad
 N_i^c=2^{200}h_i^{-5}\zeta_i/(\mu_i\delta_i^2),\quad
 (N_i^c)^\#=N_i^c+\mathbf1_{i\ge130}N_{i-1}^c .
$$
对控制胞元之外的每个真实 cell，只有其端口输入 $D_\psi X$ 改变。
对完整物理输出应用同一真实 Cauchy，费用至多
$2^{12}(N_i^c)^\#\|D_\psi X\|$。
在控制 cell 内，另将 (L.15) 送入第3节完整物理导数列；
其费用可取
$$
 2^{512}N_j^cX_*\,h_j^{-9}\delta_j^{-7/4}\rho^5 .
$$
两项和由 (L.1) 支付，给统一 (L.2)。

这个场确实是 $\widehat z$：在任意内部时刻都使用
$\widehat W=\mathcal T\widehat z$，没有在输出端加回 $\psi F_1$。
完整物理解的 absolute 角宽大于224，故降到物理宽2时可额外支付
两个角导数而无需减少原标签权。上述常数已保留这一安全余量。
在本层表达式中，真实 $w$ 是逐点分母，不使用全胞
$w_{\max}/w_{\min}$。

若需要裸相对四态，则局部还必须加回
$$
 \dot{(p/w)}=\widehat p/w-\psi p/w,\qquad
 \dot{(k/w)}=\widehat k/w+\psi(f-k)/w                    \tag{L.18}
$$
及它们的完整角导数；其显式局部项小于
$2^6(N_j^c)^\#X_*\rho^4$。
两射线前篇 (C.23) 要用的是 (L.2)，不能把 (L.18) 的裸量替进去。

实际平均高度仍由
$$
 \dot v_0(r)=\dot\lambda+
        \int_1^r[\widehat k_0(s)+\psi(s)f_0(s)]\,ds     \tag{L.19}
$$
恢复。这里只有一个独立 $\dot\lambda$。
完整 holonomy 行是前篇 (C.11)，并未令 $\dot k_0=0$。
所有非控制 cell 的深端二 jet 包络仍是原 $\delta_i^{127}h_i^{-5}$
乘 (L.1) 的固定有限系数，故参数变分也真正 $C^2$ 接平盘。
新增局部 source 支持远离平端。

平均高度积分亦有显式有限界。用 $w<1$、每胞实际 $r$ 长小于1及
$\sum_i(N_i^c)^\#<2^{160017}$（保留原两个全局因子），
(L.2) 和 $\int|\psi|dy\le2\eta\rho^5$ 给安全值
$$
 \sup_r|\dot v_0(r)-\dot\lambda|
                  <2^{160900}P_j\rho^5X_* .            \tag{L.20}
$$
这仍是相对扰动高度 $v$。
实际参考轴对称高度也随 profile 改变，其准确参数项另为
$-\int w\psi\,da$，并保留原整体高度端值；
若外尺度/切口另动，仍加原 $w_e\dot a_e$。
不因 (L.20) 把该参考 mean 项删掉。

## 8. 普通/weak 单位及下一实际消费者

本篇首先估计 source-free nonlinear 背景对 profile 的真实响应；
任意 Jacobi ordinary/weak 数据并未被包括在 $X_*$ 内。
为在下一步微分完整 affine 列，保留新第53束的真 canonical 单位：
$$
 \mathcal J_1=-\nu_mr^4F^t/(\sqrt{12}\mu_jp_*),\qquad
 \mathcal J_2=r^4(f-imF^\theta+m^2F^t)/(12\mu_j).
$$
固定物理 $r,\mu_j$ 时，准确有
$$
 \dot{\mathcal J}_1=-\psi\mathcal J_1+
                   \mathcal J_1[\dot F^t],\qquad
 \dot{\mathcal J}_2=\mathcal J_2[\dot f,\dot F^\theta,\dot F^t].
 \tag{L.21}
$$
若固定的是 ordinary 几何源 $e$、$f=w^2e$，还要加
$\dot f=2\psi f$。若固定 raw $f$，不能加这项。
这些单位变化对 arbitrary $L^1$ 源只直接给 $\rho^4$ 乘法费用；
只有另给源密度的相应径向上界时，才可再消费支集长度得到 $\rho^5$。
没有把集中在支集内的任意源免费获得一个额外 $\rho$。

完整 mean 源行仍为
$$
 \dot\pi_{0,t}=\dot f_0,\qquad
 \dot H_{0,t}=(r/w)
       [\dot\pi_0-\dot F^t_0-\psi(\pi_0-F^t_0)] .        \tag{L.22}
$$
bare flux 的端点恢复仍需真实 $F^t_e,\dot F^t_e$；
本文没有引入 $F^t_t$ 的源 norm。
独立 Jacobi 高度/flux 两 mean 在 fixed-label Cauchy 与散射图里仍保留，
不能把本篇背景的 $M=1$ 切空间条件误读为删掉算子空间的两个 mean。

(L.1)、(L.2) 现在可直接代入前篇 (C.23) 的实际射线响应。
还要把真实 physical 端图与全部当前 $\Gamma$ 列接入完整 kernel
导数和 scattering/cluster；这些进一步的符号阶或小量没有由本篇
预先授予。全 $\mathcal F=0$ 与最终闭曲面族仍按原完成标准继续。

[准确预算程序](../scripts/fourfold_actual_compact_profile_label_response_20261114.js)
及[实际执行记录](../notes/2026-11-14-R119-actual-compact-profile-label-response-budget.json)
记录新的全部有理门、首层和全层单调费用。没有恢复旧 Python native。
