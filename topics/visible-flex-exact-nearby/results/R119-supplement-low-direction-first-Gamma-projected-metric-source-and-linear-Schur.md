# R119 续篇：第一 Γ 的低阶切向、投影 metric 源与完整线性 Schur

2026-11-15，visible-exact / tail_connector。

**状态：解析证明已逐段独立核对。** 本篇继续已经构造的 fixed-stop
simple-root 对象，保持原 $\zeta_j$、公共五盒、两个真实根、
全部 mean、原单位 source 和外 $C_R$ 行。第二参数固定为原已知
成员的 $\gamma_2^\flat$，第一参数取 P 的实际非线性选择。

本篇证明两件互相关联的事。第一，虽然第一参数的值图定义在
高阶物理背景域，它在一个固定高背景处的准确切向 functional
只需低阶方向；这个 functional 由真实 ODE 和正权平均直接定义。
第二，这一方向经真实 metric、mean 与参考高度变化所产生的
compatible ordinary 源，仍有背景的高阶角正则。因此它与刚付的
2050阶损失逆复合后，在低阶方向空间中是一个真正的小算子。
这里的 Schur 只消去第一参数反馈，不把整个 residual-sensitive
Jacobi 差或后续 nonlinear 迭代冒称同域收缩。

## 1. 固定背景、低方向和全部实际指标

使用下列全文及其原单位：

* [第一 principal 参数](R119-supplement-finite-Sobolev-principal-KAM-and-true-first-metric-counterterm.md)，记 P；
* [nonlinear mean 与高度图](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md)，记 M；
* [准确 metric ordinary 源](R119-supplement-exact-nonlinear-ordinary-sources-and-Gamma-reference-height-lifts.md)，记 Q；
* [受控 residual 背景](R119-supplement-off-shell-controlled-radial-jets-and-exact-holonomy-retraction.md)，记 C；
* [附近全尾 proxy 逆](R119-supplement-nearby-finite-Sobolev-full-tail-proxy-inverse-and-complete-sources.md)，记 I。

固定 I.1 的一个真实 holonomy-one 背景，记其大小为
$$
 R=\mathscr R\le2^{-8192000}.
 \tag{G.1}
$$
这个背景可以有非零 ordinary residual
$N=c_{\rm ph}(K_t-F)$，但由 M.16 和 $\chi=0$ 准确有
$\langle A_0N\rangle=0$，其中
$$
 A_0=JD^{-3/2},\qquad
 c_{\rm ph}(t)=\frac{\mu_jp_*(t)^2}{12r(t)^{10}} .
$$
背景仍有 P 的8196角阶和 C 的4420角阶/三阶 residual 径向输入。
第二参数及形状控制在下文切向中先固定。

对物理非mean高度方向 $v_\perp$，在当前 metric 中定义
$$
 p=\frac{(v_\perp)_\theta}{a_{\rm ph}w},\quad
 k_\perp=\frac{(v_\perp)_t}{a_{\rm ph}w},\quad
 u=p_\theta,\quad v=(k_\perp)_\theta .
$$
为免与背景的 $R$ 混淆，方向 norm 写成
$$
 {\cal D}_8(v_\perp)=
 \max\left\{\sup_{j\ge129}C_j^{-1}
       \sup_{I_j}\|(p,k_\perp,u,v)\|_{H^8},
 \quad
 2^{440}\sup_{\mathrm{cut128}\to e_0}
              \|(p,k_\perp,u,v)\|_{H^8}\right\}.
 \tag{G.2}
$$
这是固定当前物理 $t,\theta$ 的 norm，保真实一阶径向迹与运动学。
其零 mean 斜率由 M.13 的准确 holonomy 切向补回。
独立常高度和独立荷不由 (G.2) 计量；后文仍保它们的实际列。

记 $C_j^{\rm P}=C_j+\mathbf1_{j\ge130}C_{j-1}$，
而 $C_j^\#$ 仍为 C 篇定义的完整六邻胞和。
这两个量不换名字。P.13 的邻胞比较已经包含
$\mathcal N_{i|j}\le2^{132}C_j^{\rm P}$。
以下低阶 ODE 常数吸收这132 bits，而最后 source 继续用完整
$C_j^\#$。

## 2. 不降背景正则性的低方向 ODE

在一个固定高背景处，P.10 的两条真实 principal ODE 可以直接
对 (G.2) 的方向作一次变分。这只需要当前系数及方向的一阶角导，
并不需要先把方向送入 $H^{8196}$。
背景的 $H^{20}$ 已足够支付这一低阶计算；高背景域不改变。

定义
$$
 E_i^\ell=2^{4096}J_jC_j^{\rm P}\quad(i\ne o),\qquad
 E_o^\ell=2^{4096},\qquad J_j=j+5,\quad o=(129,2).
 \tag{G.3}
$$
以 $\dot f_i[v_\perp]$ 记真实 return 的线性 ODE 输出。
按照 P.13 的同一个实参数、有序正支/反向负支积分证明，有
$$
 \|f_i\|_{H^{16}}\le E_i^\ell R,\qquad
 \|\dot f_i[v_\perp]\|_{C^1}\le E_i^\ell{\cal D}_8(v_\perp),
$$
$$
 \|\dot f_i[v_\perp]-\dot f_i|_{u_\perp=0}[v_\perp]\|_{C^0}
       \le(E_i^\ell)^2R{\cal D}_8(v_\perp),\qquad
 \|D_pf_i[\dot p]\|_{C^0}
       \le E_i^\ell R\|\dot p\|_{\cal P}.
 \tag{G.4}
$$
第三式沿 $\lambda u_\perp$ 积分的是一次背景变分和一次低方向变分；
它不主张任意两个 $H^8$ 输入的整个 return 都有 $H^{16}$ 正则。

为列明4096的实际余量：P.14 的完整 reciprocal、平方根及 mean
分母在 $s=16$ 时至多收 $2^{32(16+8)}=2^{768}$；
实际 $C^1$ 方向变分用至多背景第三角导和方向第二角导。
P 的实 flow composition 账在 $k=16$ 为
$2^{18k+50}=2^{338}$，双线性项另收 $2^{16}$。
完整径向积分仍为内部 $32(j+4)$ 和外行 $2^9$；
六邻胞132 bits、四倍角、两次反向图和两个 mean 由余下固定
费用支付。总量严格小于 $2^{4096}$，二次项由其平方支付。
积分方程的 Lipschitz 常数先用 (G.1) 取得小于 $1/8$，
不假设未经证明的低阶 return inverse。

P.16 的真实小除数仍给
$$
 B_\ell:=\sup_i\frac{E_i^\ell}{(\gamma_i^{\rm D})^2}
                         <2^{4416},
 \qquad \gamma_i^{\rm D}=\kappa_i/4096 .                  \tag{G.5}
$$
内部可读为 $4096+24+55+202<4416$；
外行为 $4096+24+263<4416$。$j+4$ 换成 $j+5$ 的一次因子
已包含在202中。这里没有增加一个随深层发散的 supremum。

## 3. 直接定义低方向 functional，而非假设稠密延拓

对当前实际 $f_i$，分别以 P.22 的 $s=16$ 和原高阶定理构造共轭。
二者是同一个真 return、同一个 irrational 目标和同一 mean
归一化，故由 P.27 的唯一性准确一致。
所以 P.28 的正权公式可以直接消费 (G.4)：
$$
 {\cal T}'_{u,i}[v_\perp]
 =-\frac{\left\langle
       \dot f_i[v_\perp](h_i(x))/h_i'(x+\omega_i)\right\rangle}
       {\left\langle1/h_i'(x+\omega_i)\right\rangle}.
 \tag{G.6}
$$
它定义在整个 (G.2) 方向空间，且有界、线性。
并未断言参数值 map 定义在一个仅有 $\mathcal D_8$ 正则的开球；
也未使用 Fourier 截断在 uniform 全层 norm 中必稠密这种不成立的
假设。对于原高阶方向，(G.6) 就是已经证明的真正 Fréchet 导数。

P.36 在径向点给
$\langle\dot f_i|_0[v_\perp]\rangle=0$，其中 holonomy mean 已补全。
用 P.31 的 $s=16$ 正权误差和 (G.4)，得到
$$
 |{\cal T}'_{u,i}[v_\perp]|
 \le2^{80}(\gamma_i^{\rm D})^{-1}
                  (E_i^\ell)^2R{\cal D}_8(v_\perp).
 \tag{G.7}
$$
这是同一个物理方向的低阶预算，不是沿各 Fourier 坐标分别取最大值。

完整参数矩阵 $D_p\mathfrak T$ 仍为 P.34 的真实无限矩阵。
定义
$$
 \dot p=(I-D_p\mathfrak T)^{-1}{\cal T}'_u[v_\perp].
 \tag{G.8}
$$
原 inverse norm 小于2，所有 cross 参数行保留。
先在原 $\mathcal P$ norm 取完整 supremum，再代回逐行方程，可取
$$
 \|\dot p\|_{\cal P}
    \le2^{8960}R{\cal D}_8(v_\perp),\qquad
 |\dot p_i|\le2^{4512}E_i^\ell R{\cal D}_8(v_\perp).
 \tag{G.9}
$$
第一式用 $2^{80}B_\ell^2$ 及 P.2 的
$\kappa_i=4096\gamma_i^{\rm D}$，包括 inverse 因子2仍小于8960 bits。
逐行的首项至多 $2^{80+4416}E_i^\ell R{\cal D}_8$；
反馈项 $E_i^\ell R\|\dot p\|_{\cal P}$ 因 (G.1) 更小。
因此4512留有真实余量。

最后乘真正 metric 曲线导数，而非把 $p_i$ 当作 $\gamma_{1,i}$：
$$
 \begin{split}
 |D^\ell\gamma_{1,i}[v_\perp]|
 &\le2^{8960}J_j^2\delta_j^{-1}C_j^\#
                     R{\cal D}_8(v_\perp),\quad i\ne o,\\
 |D^\ell\gamma_{1,o}[v_\perp]|
 &\le2^{8960}R{\cal D}_8(v_\perp).
 \end{split}                                             \tag{G.10}
$$
使用的是 P.3 的 $2^{-18}\kappa_i^{-1}$，
内部 $\kappa_i^{-1}<2^{28}J_j\delta_j^{-1}$ 和外部 $<2^{132}$。
两行最大指数分别为8618、8722，小于8960。
(G.10) 与高阶背景图的真实 $D\gamma_1^*$ 在其共同域上相同。

## 4. 两个真实 mean 与参数引起的总高度

置
$$
 \psi=\sum_i\psi_{1,i}D^\ell\gamma_{1,i}[v_\perp].
 \tag{G.11}
$$
这里仅消去第一参数；给定第二参数、形状、$\nu$ 方向以后必须
另加其原真实列。

固定物理 $u_\perp$ 作 metric 变分时
$\dot P=-\psi P,\ \dot K_\perp=-\psi K_\perp,\ \dot q=2q\psi$。
由于当前背景 holonomy 为1，M.33 给
$$
 \dot\kappa=
 \frac{\psi D_{(P,K_\perp)}\Phi_q[P,K_\perp]
                      -2q\psi\,\partial_q\Phi_q}
      {\langle A_0\rangle}.
 \tag{G.12}
$$
所有 $\partial_q$ 均固定 $P,K_\perp,U$，不与 M.8 的函数名混淆。
M.8 的可去商展开表明
$\partial_q\Phi_q=O(n^2)$；
M.12 中方向 $P,K_\perp$ 的 Fourier mean 为0，
故 $D\Phi_q[P,K_\perp]=O(n^2)$。
连同 $\kappa=O(n^2)$，对
$n=\|(P,K_\perp,U,V)\|_{H^2}$ 可安全取
$$
 |\dot\kappa|+|\psi\kappa+\dot\kappa|
                         \le2^{16}n^2|\psi| .
 \tag{G.13}
$$
此界使用真实 mean 分母 $|\langle A_0\rangle|>3/4$，
没有除以趋零的 $q=w^2$。

参数造成的总物理高度 $H_p$ 与原参考 lift $h_\psi$ 分别为
$$
 (H_p)_t=a_{\rm ph}w\{\psi(1+\kappa)+\dot\kappa\},
 \quad (h_\psi)_t=a_{\rm ph}w\psi,\quad
 H_p(t_f)=h_\psi(t_f)=0 .
$$
令
$$
 b_p=H_p-h_\psi,\qquad
 \ell=\frac{(b_p)_t}{a_{\rm ph}w}=\psi\kappa+\dot\kappa .
 \tag{G.14}
$$
这是角常数斜率，不是将两个独立 mean 方程删去。
完整 parameter height 仍是有向积分；在每个胞元不能重置它。

## 5. 消去的是径向常数源，保留的是实际 residual 与高度

对同一背景定义 compatible 投影
$$
 \Pi_A f=f-\frac{\langle A_0f\rangle}{\langle A_0\rangle}.
 \tag{G.15}
$$
它减去一个角常数，$\Pi_A1=0$，
$\langle A_0\Pi_Af\rangle=0$。
它不同于外 DN 的 density 投影 $P_\mu$。
在全部需要的 $H^q$ 上 $\|\Pi_A\|<4$；
此处 mean functional 只需 $A_0$ 的低 norm，不再收一次高阶乘法。

M.37 用完整 $H_p$ 变分时准确给
$$
 \delta_pN=c_{\rm ph}\{\ell_t-F_K\ell-e_{\psi,\rm rem}\}+\psi N ,
$$
其中 Q.20 的真实 ordinary scalar 是
$$
 e_{\psi,\rm rem}
   =(K+F_A)\psi_t+\{F-DF[W]+2qF_q\}\psi .                 \tag{G.16}
$$
$c_{\rm ph}\ell_t$ 和 $2c_{\rm ph}Q\ell$ 都是径向常数。
因此实际 projected metric column 准确为
$$
 \boxed{\quad
 {\cal B}_p[v_\perp]:=-\Pi_A\delta_pN
   =\Pi_A\{c_{\rm ph}e_{\psi,\rm rem}
              +c_{\rm ph}(F_K-2Q)\ell-\psi N\}.
 \quad}                                                  \tag{G.17}
$$
(G.17) 不需要估计 $\ell_t$ 的高角 norm，也不丢掉
$+\psi N$ 在原 $\delta N$ 中的准确符号。
它只把一个实际径向常数从 compatible 源坐标中消去。
$(H_p)_t$、$H_p$ 的两个端点以及原 mean 约束全部仍在 (G.12)--(G.14)。

## 6. 高阶源来自固定高背景，方向只进入径向标量

对 $0\le q\le2114$，背景的4420阶输入足够支付 (G.16)--(G.17)
所有角乘积。完整 rational 分母按 C.9a 的绝对收敛代数级数处理。
以 $n_q=\|(P,K,U,V)\|_{H^{q+2}}$ 记局部背景大小，有
$$
 \|e_{\psi,\rm rem}\|_{H^q}
 \le2^{131104}\{n_q|\psi_t|+(1+|Q|)n_2n_q|\psi|\},
$$
$$
 \|F_K-2Q\|_{H^q}\le2^{131104}(1+|Q|)n_q .
 \tag{G.18}
$$
这是 Q.20 的完整商式在有限 $H^q$ 代数中重新收费，
不沿用其 analytic 宽度2/4。
线性部分 $F=-A(2K+U)+O(W^2)$ 直接给
$F_K-2Q=O((1+|Q|)W)$；$F-DF[W]+2qF_q$ 从二次开始。
C.9a 的131072、两次 Fréchet 乘法及投影的费用被131104覆盖。
若把所有小 mean/全乘积一次宽放，下面统一使用 $2^{196608}$；
这不是给每个 factor 另乘该常数。

内部实际同胞参数和满足
$$
 g_j\le2^{9216}J_j^2\delta_j^{-1}C_j^\#
                         R{\cal D}_8(v_\perp).
 \tag{G.19}
$$
Q.22 保持 $|\psi|\le g_j$、
$|\psi_t|<2^{13}\delta_j^{-3/2}g_j$。
(G.13) 的 $\ell$ 项比显示二次项更小；
$(1+|Q|)n_2$ 乘当前球后也可保守吸入这个统一账。

原 $o=(129,2)$ 的 bump 支集仍在第129胞元的第二下降坡，
这正是新对象说明第8节的原支集；它不在新 finite connector 或
新根内。该唯一浅端例外使用 (G.10) 第二行单独付，不把其
无 profile 上界强行改成内部 (G.19)。
其余实际邻胞和/重编号已经保在 $C_j^\#$ 中。

现在核最坏无限层幂。原 $p_*^2\le2^{256}\delta_j^{-2}$ 给第一项。
这里必须付完整六邻胞，而非只付 $C_j+C_{j-1}$：
Q.24c 的真实和为 $C_{j+1}+2C_j+2C_{j-1}+C_{j-2}$，
原后向一步比 $<2^{127}$、前向比 $<2^{64}$，
故对本篇的六邻胞 $C_j^\#$ 使用
$C_j^\#<2^{256}C_j$。因此
$$
 \frac{c_{\rm ph}(C_j^\#)^2}{\zeta_j\delta_j^{16}}
 \le2^{1168}h_j^{-10}\frac{\zeta_j}{\mu_j}\delta_j^{-22}.
 \tag{G.20}
$$
与 $\psi_t$ 和 (G.19) 相乘后，剩下的 profile 正是
$$
 J_j^2h_j^{-10}\frac{\zeta_j}{\mu_j}\delta_j^{-49/2}.
 \tag{G.21}
$$
它的完整三段 supremum 小于 $2^{200000}$，可逐段直接核：

* $j\le4096$ 时为 $J^2h^{-10}\delta^{-83/4}$；
  $h^{-10}<2^{40}$、$J^2<2^{26}$、
  $\log_2\delta_j^{-1}<4100$，总量小于 $2^{86000}$。
* $4097\le j\le8192$ 时为
  $2^{-30}J^2\delta_{4096}^{-3/2}
                 \delta_j^{-77/4-10/256}$，
  $\log_2\delta_j^{-1}<8196$，总量小于 $2^{165000}$。
* 深段是
  $2^{-30}J^2\delta_{4096}^{-3/2}
     \delta_{8192}^{-485/4}\delta_j^{102-10/256}$。
  它在规范接点连续，随后真实幂 $102-10/256>101$
  压过 $J^2$，故同样小于 $2^{165000}$。

这样 (G.17) 的第一项所需 bits 至多
$$
 196608+1168+9216+13+200000=407005<524288 .
$$
$\ell$ 项的额外 $n_2$ 和一个 $J$ 由实际
$JC_j^\#R<1$ 吸收。最后 $\psi N$ 不用假设 $N=0$：
原 $\sup J^2\delta^{-1}C_j^\#<2^{160144}$
使它在同一窄源 norm 中至多 $2^{170000}R^2{\cal D}_8$。

浅端外行例外也有完整费用：
$c_{\rm ph}C_j^\#/(\zeta_j\delta_j^{16})
 \le2^{712}h_j^{-5}\delta_j^{-20}$，
在129及实际相邻有限几项上连 $\delta^{-3/2}$、
(G.10) 和上述角费仍小于 $2^{212992}$。
这不是把深层幂用于一个有限外行。

因此得到真正的同一 ordinary 源域估计
$$
 \boxed{\quad
 \mathfrak N_q({\cal B}_p[v_\perp])
      \le2^{524288}R^2{\cal D}_8(v_\perp),
                       \qquad 0\le q\le2114 .
 \quad}                                                  \tag{G.22}
$$
所有 mean 已由 (G.15) 精确处理，而非把 unknown mean 丢弃。
源在原固定 $t$ 给定；bump 的0、1、2阶端 jet 为0，
不产生新的值跳或 Dirac。独立 weak/原子源仍只按原合同输入。

(G.22) 的高角正则来自当前已知背景系数。
方向 $v_\perp$ 仅通过每个真实径向标量 $D^\ell\gamma_{1,i}$ 进入；
没有对 $H^8$ 方向偷偷收2114角导。
本篇也不从 (G.22) 免费推出三个径向 residual 导数的增量界。

## 7. 全 proxy 逆的低方向读出，包括有限外段

令 $\mathcal K_W$ 是 I 的 compatible 全 proxy inverse，
固定同一个真实外线性行及唯一常高度 gauge。
记 $h=\mathcal K_Wg$；对任意 height，下面的 $\mathcal D_8(h)$
只读其非mean高度部分。

I.34 直接支付内部 $\mathcal D_8$。
有限 negative connector 仍需一条实际读出，不把内部 $\mu_j$ 公式
移用到那里。由 I.24--I.28 的全源及其两真实端口，
在129附近 $(v^\#)^{-1}<2^{1240000}$。
原 Y 的有限 frame/共同表示转换费小于 $2^{1238200}$。
新的有限 word 用 $\lambda_o=2^{2048}$，
其完整 Cauchy 子乘积为
$2^{8192}\lambda_o^{12}=2^{32768}$；该门来自 I.15 的
先径向 Picard 后 scattering 顺序，非椭圆区任意 Cauchy 演化。
root 端的两个 half-order 和恢复相对四态只用额外4角导。

物理比例也明确保留：有限 negative connector 中
$a_{\rm ph}\ge\rho$、$\omega<2^{362}$、
$w=a_{\rm ph}/(4\omega)$，且新对象 S.17 给
$\varepsilon_s/\rho<2^{440}$。所以从
$h=\rho\varepsilon_s\bar H$ 读回
$h_\theta/(a_{\rm ph}w)$、$h_t/(a_{\rm ph}w)$
至多增加 $2^{804}$；
(G.2) 的 $2^{440}$ 及全部有限 source/mean 单位
可连同上述余项收到 $2^{65536}$。
这些数与 I.28 的3145732 bits相加，严格小于7600000。
正侧若有独立源，仍通过原真实 Poisson 端口进入，
不在正片使用高频 Cauchy 传播。

故可使用统一低方向门
$$
 {\cal D}_8(\mathcal K_Wg)
 \le2^{7600000}\mathfrak N_{2058}(g)
       +2^{4400000}\mathfrak B_{2056}^{W,\rm ext}.
 \tag{G.23}
$$
外源项指 I.25 完整有序范数，含 root、ordinary/weak、
两 mean、真实 $C_R/B_0$、$\nu$、两 $\Gamma$ 和原子。
此处为参数反馈只消费 $\mathfrak B^{W,\rm ext}=0$ 的新内部列；
对任意已给外源仍保其完整独立读出。

## 8. 一个真正同域的第一参数 Schur

将 $\mathcal B_p$ 视为固定背景处 (G.17) 定义的线性列。
它的值逐 $t$ 满足 $\langle A_0\mathcal B_pv\rangle=0$；
且其两端没有新增 total flux 荷。
因而它合法进入 I 的 compatible body inverse，无须先加
一个未知的 $\sigma_\circ$ 荷来掩盖不相容。

(G.22)--(G.23) 直接给
$$
 \|P_\perp\mathcal K_W\mathcal B_p:
                     {\cal D}_8\to{\cal D}_8\|
 \le2^{8124288}R^2<2^{-8000000}.
 \tag{G.24}
$$
这是同一完备低方向空间上的有界算子。
2050导损失仍存在于一般输入上，但这里高阶源依赖的只是
固定背景和低方向标量，故 (G.24) 没有跨源/状态域形式相乘。

对原 compatible $g$ 及任何已付 affine 外源，先取其完整解 $h_0$。
准确解
$$
 v=P_\perp h_0+P_\perp\mathcal K_W\mathcal B_pv,\qquad
 h=h_0+\mathcal K_W\mathcal B_pv,\qquad
 \dot\gamma_1=D^\ell\gamma_1[v].
 \tag{G.25}
$$
同域 Neumann 级数收敛，且 $v=P_\perp h$。
它等价于
$$
             c_{\rm ph}\mathcal J_Wh-\mathcal B_p(P_\perp h)=g
 \tag{G.26}
$$
及原全部外线性行、gauge、荷条件。
原给定外部荷不被新 compatible feedback 改变；
若另要求完整 holonomy-one 切向，则保原相应荷为0的真实条件，
不能从 (G.25) 自动把所有外部荷清零。

这里还须区分参数方向的身份：对于一般带独立 affine flux 荷的数据，
(G.25)--(G.27) 证明的是显示的 projected-feedback 算子的代数逆。
此时 $h$ 的 mean 还含真实 $\chi/w^2$ 项，
$D^\ell\gamma_1[P_\perp h]$ 不自动等于该 charged 方向的完整
principal 参数微分。本篇只在 (G.30) 所指定的 holonomy-one
切向上认同真正的 nonlinear reduced derivative。
若要对给定非零荷作该认同，还须将它引起的真实 principal
一次变分保为另一独立 affine 参数列；本篇未把 $\Gamma$ 值图
延伸到 $\chi\ne0$ 的背景。

I 的更高读出仍可以消费同一个新源。
例如 $0\le s\le64$，宽放后有
$$
 \mathfrak Y_s^W(h)
 \le2^{7600010}\mathfrak N_{\max(s,8)+2050}(g)
     +2^{4500010}
                   \mathfrak B_{\max(s,8)+2048}^{W,\rm ext}.
 \tag{G.27}
$$
这里 $\max(s,8)$ 只是为了同时支付定义 (G.25) 的低方向 norm；
没有新增背景正则性结论。
源最高仍为2114，外有序窗最高2112。
独立常高度仍按原单独 gauge 输出。

## 9. 真高度、mean 与原方程 derivative 的最后身份

实际重选 metric 后的总高度切向是 $h+H_p$，不是仅 $h$。
其相对态同时减去 $\psi(P,1+K,U,V)$；
特别参考斜率 $\psi$ 与总高度中的 $h_\psi$ 正好按 M.32 抵消。
不应把 $h_\psi$ 的完整 mean 斜率强行放入原固定 metric 的
$C_j^{-1}$ 状态 norm 再称其有界。
它是已经显式给出的参考几何列。

(G.14) 的积分绝对收敛并给实际平端 $C^2$。
例如无限内部部分可从 Q.22、M.3 和 (G.10) 保守读出
$$
 \|H_p\|_{C^2_r(I_j)}
 \le \rho\,2^{12000}J_j^4 h_j^{-5}\zeta_j\delta_j^{-13/2}
                         R{\cal D}_8(v),                 \tag{G.28}
$$
并另保唯一129浅端外行的有限支集费用。
为核 $t$ 二 jet，用 $(aw)_t=(1+A)aw$、
$|Q|<2^{13}J\delta^{-3/2}$、(G.13) 的直接一次实 $t$ 导数，
其 $n_t$ 由原 $K_t=F+\mathfrak r$ 和 C.7 支付。
所有含 $n^2$ 的附项在 (G.1) 下小于同一主账。
接点几何和与 $t\leftrightarrow r$ 转换计入12000 bits。
深处真实幂为 $131-13/2-10/512>124$；
故两个径向导数确实趋0，而不是只给某个 Sobolev 标签。

在 bump 支集外 $(H_p)_t=0$，但 $H_p$ 一般为非零常数。
必须输出
$$
 H_p(t_{\rm left}),\quad H_p(t_{\rm right}),\qquad
 \pi_{H_p}=w^2A_0\{\psi(1+\kappa)+\dot\kappa\}.
 \tag{G.29}
$$
完整 finite connector 和 new root 在这些 $\Gamma$ 方向上固定，
所以其常高度列只经真实原 matching 传递；
它不被宣称为一个零边界条件。
相应物理 Cartesian 读出仍收原
$2^8\max(1,\rho^{-2})$，不抹去 $\rho$。

最后，把真正 off-shell Jacobi 差保在正确位置：
$$
 c_{\rm ph}\mathcal L_Wh
     =c_{\rm ph}\mathcal J_Wh-\mathcal E_N[h],\qquad
 \mathcal E_N[h]=\alpha Nk-\beta N_\theta p-\gamma Np .
$$
在 holonomy-one chart 的真正切向上，
$$
 \boxed{\quad
 \Pi_A D N_{\rm reduced}[v]
 =c_{\rm ph}\mathcal J_Wh-\mathcal B_pv
                          -\Pi_A\mathcal E_N[h].
 \quad}                                                  \tag{G.30}
$$
参数列已经由完整 $\delta_pN$ 构造，不能在它之外再重复收一次
$\mathcal E_N[H_p]$。式中的 $+\psi N$ 已在 (G.17) 内，
并未假设当前背景是解。

(G.25)--(G.27) 只消去 (G.30) 的第一参数反馈。
剩下的 $\mathcal E_N[h]$ 对一般方向仍有真实导数损失；
没有据 (G.24) 对它再作同域 Neumann。
第二参数、形状和 $\nu$ 的真实方向仍是原独立列；
第一参数的 low functional 也不等于一个新的 low-regularity
非线性参数值图。

后续 smoothing/tame 构造必须另外给出足够宽的有限阶尺度、
其径向 residual 增量、以及真实 cap/height/荷的全部联立。
本篇的作用是准确关闭其中第一 $\Gamma$ 的线性反馈：
全无限层、真实外行、当前 mean、非零 residual、原单位 source
及参考高度端点均在同一个已给背景上保留。
