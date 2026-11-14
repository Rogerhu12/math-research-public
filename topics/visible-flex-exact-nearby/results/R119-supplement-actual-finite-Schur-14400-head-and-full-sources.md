# R119 续篇：同一双参数候选的实际有限 Schur、14400 低频消元及完整源

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇在第46束选出的同一径向双参数候选上，
重新实例化真实 principal-return KAM 和原完整外匹配 map，
然后利用已经真正到达的长段小输入，准确消去
$0<|m|\le14400$ 的全部外匹配行。更高频率保留为完整参数，
不是把它们设为0。各胞元本身仍是全频非线性 PDE 解。

另证明任意固定频率、任意有限径向截面的实际 Schur 矩阵非奇异，
并给全部 ordinary/weak/mean 源的明确反演式。其已付统一量词仍只是
有限频率窗；本篇不把随频率移动的所有中间 Schur 都称为已解决。

## 1. 固定的新径向参考和真实参数选择

固定
[完整双参数相位算术](R119-supplement-actual-two-parameter-complete-phase-arithmetic.md)
构造的 $\Gamma^0=(\gamma_{1,i}^0,\gamma_{2,i}^0)$。
其实际主角、完整首系数满足
$$
 |e^{in\omega_i}-1|>\frac{\kappa_i}{4096|n|},\qquad
 |1+e^{i(n\omega_i+\beta_i/n)}|>\frac1{128N_i|n|}.
                                                               \tag{S.1}
$$
这两个目标只在零标签参考上同时固定。
对这个新尾，用
[第47束重建证明](R119-supplement-two-parameter-full-tail-chart-reconstructed.md)
的真实 $d_4$、停止点及重新选择的外好集，固定一个 $t_0$。
从此不随未知标签重选 $t_0$。

本文在非zero标签上固定 $\gamma_{2,i}=\gamma_{2,i}^0$，
只联立调整全部 $\gamma_{1,i}$ 以保持真实主旋转 $\omega_i$。
**不声称非径向完整 $\beta_i$ 已保持不变。**
这样可以使用已经证明的 principal KAM，而不假定尚未建立的第二参数行。

这个 KAM 在新参考上确实存在。两个 bump 的支集相离，
$\gamma_2$ 对 $\partial_{\gamma_1}\Theta_i$ 的积分完全没有贡献；
原实际复逆及其导数界逐项保持。现在取
$\gamma_i^{D}=\kappa_i/4096$，并在 cohomological 方程中使用
(S.1) 的较弱二阶形式。相对于原
$\kappa_i/64$，小除数平方费用准确增加 $64^2=2^{12}$。
因此在同一个
$$
 A_*=2^{-262148},\qquad\|a\|_{224}<A_*
$$
球中，新的实际联立 Newton 满足
$$
 \sup_i\frac{\varepsilon_i}{(\gamma_i^{D})^2}
 <2^{288}A_*=2^{-261860}<2^{-64}.                          \tag{S.2}
$$
$\varepsilon_i=2^{24}(j+4)N_j^\# A_*$、
$N_j=2^{184}h_j^{-5}\zeta_j/(\mu_j\delta_j^2)$。
原两个全局逆幂及全部有限前缀都在 $N_j$ 中。
强尾 KAM 的真实全参数平均行、所有角模逆及二次收敛证明因而直接适用，
给 $\gamma_1^*(a)$。第二参数固定也保留全部实际非线性依赖，
不是在计算解时删除第二 bump。

由于 $\varepsilon_i/\kappa_i$ 本身没有改变，原逐行参数修正界保持；
新的角导数偏离可放宽为 $2^{18}2^{-261860}$。
基点 $\gamma_1^0<2^{-24}+2^{-86}$、$\gamma_2^0<2^{-86}$
距实际复参数盒有充分余量。
整个选择在标签角平移轨道上不变，联合全纯。
这些结论是同一个新候选上的实例化，不使用旧参考的固定目标数值。

## 2. 同一候选的真正全外匹配 map

第47束证明复盒上所有真实局部 map、mean 小根、raw 权和有限
connector 门保持。raw404 的证明使用相同的低窗误差、实际高块、
真实单调面积和全模角费；这些门均未变。
因此对本篇新允许线及新 $t_0$，真正原点 Schur 导数满足
$$
 D_0=Dk(0)+\mathsf C_L Df(0),\qquad
 \|D_0^{-1}g\|_\beta
 \le\frac1{16}\|g\|_{\mathfrak Z_{\beta+1850}}.            \tag{S.3}
$$
这包含所有非zero四重频率；$D_0$ 在径向原点逐模对角且每个乘子非zero。
外好角在原点给它的实际非zero性，不需猜测有限矩阵的 determinant。

记
$$
 \beta_{\min}=65536,\quad\beta_H=262144,\quad
 d_0=88823/400,\quad s_\beta=\beta-d_0,\quad
 \Delta_*=1850+d_0=828823/400<2080.                       \tag{S.4}
$$
对每个 $\beta\in[\beta_{\min},\beta_H]$，
$\|a\|_\beta<1/64$ 通过四重最小频率4嵌入上述 KAM 域。
实际重停仍只改变一个自主 $A=0$ 流的极小复时间；
第47束的复 $|d_4-d_4^{ideal}|<2^{-38}$ 保证原复停止管的门不增。
$H\omega$ 准确不变，所以长段 $[0,B]$ 和正帽端口没有改变。

由
[完整真实 Newton 链](R119-supplement-joint-KAM-incoming-and-actual-full-Newton-chain.md)
§§1–5的同一完整复合与 Cauchy 证明，可在本篇新参考上定义
$$
 f(a)=f_B^{\Gamma^*(a),t_0}(a),\quad
 k(a)=k_B^{\Gamma^*(a),t_0}(a),\quad
 \mathcal F_c(a)=k(a)-K_{B,\perp}(f(a),\Phi(c,f(a))).     \tag{S.5}
$$
$c$ 取实际周期帽已经证明的入口球；$\Phi$ 是真实帽反馈，
并始终满足 $\|\Phi(c,f)\|\le r_f=10^{-8}$。
这里没有将 $\Phi$、非zero $f_B$ 或 mixed 项冻结。
精确输出界和完整导数界仍为
$$
 \|f(a)\|_{\dot A^2_{s_\beta}}+
 \|k(a)\|_{\dot A^1_{s_\beta}}<2^{-443}\|a\|_\beta,
$$
$$
 \|[D\mathcal F_c(a)-D_0]b\|_{\mathfrak Z_{s_\beta}}
 <2^{-400}(\|a\|_\beta+e^{-7L/4})\|b\|_\beta,
 \qquad\|a\|_\beta\le1/256.                              \tag{S.6}
$$
理由不是把旧算子当成新算子，而是本篇保持该证明使用的每个输入门：
完整迹的复球及大小、同一 $L$、同一长段双权 Green、
完整 $D\mu$、帽半球 Cauchy 常数及真正参数全纯性。
(S.2)只改变远小于这些门余量的 KAM 角导界。
度量参数列、停止长度列、两个 mean 的输出均仍在(S.5)中。

设
$$
 R=2^{-60000000},\qquad e^{-7L/4}<R.                     \tag{S.7}
$$
真实非线性长段增宽给
$$
 \|D_0^{-1}K_{B,\perp}(0,\Phi(c,0))\|_{\beta_H}<Rr_f.
                                                               \tag{S.8}
$$
(S.8)同样在任意较低 $\beta$ 成立。
重新用本篇 map 执行原证明的94步递推，全部常数不增，因此产生
本篇自己的新标签序列。它不是旧对象标签的无偿移用。
特别其末点 $a_{94}$ 在 $\beta=66624$ 满足
$\|a_{94}\|_\beta<R/4$，完整残差小于 $2^{-5760041760}$。
下文也可直接从(S.8)的真实 incoming 点开始，不要求执行有限链。

## 3. 实际有限窗的同权预条件界

令 $P=P_{0<|m|\le M_0}$，$Q=I-P$，其中
$$
                            M_0=14400.                 \tag{S.9}
$$
这是完整四重 Fourier 投影；正负频率都保留。
$P$ 与径向 $D_0$ 及其逆交换。
对任意 $\beta$ 和 $g\in\mathfrak Z_{s_\beta}$，
有限 Fourier 权的准确比较给
$$
 \|P D_0^{-1}g\|_\beta
 \le\frac1{16}e^{\Delta_* M_0}
                         \|P g\|_{\mathfrak Z_{s_\beta}}. \tag{S.10}
$$
没有把全频1850宽差忽略；它已变成显示的有限窗因子。

在 $\|a\|_\beta\le R/2$ 内，(S.6)–(S.10)给
$$
 \|P D_0^{-1}[D\mathcal F_c(a)-D_0]\|_{\ell^1_\beta
                                      \to P\ell^1_\beta}
 <2^{-403}R\,e^{2080M_0}.                               \tag{S.11}
$$
因为 $e<4$、$4160M_0=59904000$，右侧严格小于
$2^{-96403}$。以下保留安全余量
$$
                             \epsilon_H=2^{-96000}.     \tag{S.12}
$$
因此实际 head Jacobian
$$
 A_H(a)=P D_0^{-1}D\mathcal F_c(a)P
$$
在原 $\ell^1_\beta$ 的有限子空间上满足
$\|A_H-I\|<\epsilon_H$、$\|A_H^{-1}\|<2$。
这是真非线性 map 在真实小入口内的逆，不是数值采样的矩阵条件数。

(S.11)的输入是**全部频率**。它还准确控制来自所有高标签的 head 反馈；
没有以截断 PDE 代替这个输入。

## 4. 保留任意真实高标签的完整 head 隐函数

固定 $b=Qb$、$\|b\|_\beta\le R/4$，在 head 球
$\|h\|_\beta\le R/4$ 上定义
$$
 \mathcal T_b(h)=h-PD_0^{-1}\mathcal F_c(h+b).            \tag{S.13}
$$
(S.11)给其 Lipschitz 常数小于 $\epsilon_H$。
在 $h=0$，
$PD_0^{-1}D_0b=0$，沿 $tb$ 的真实 Taylor 积分和(S.8)给
$$
 \|\mathcal T_b(0)\|_\beta
 <Rr_f+\epsilon_H\|b\|_\beta<R/8.
$$
因此(S.13)严格自映并收缩，得到唯一
$$
 h=h_c^*(b),\qquad
 P\mathcal F_c(h_c^*(b)+b)=0,\qquad
 \|h_c^*(b)\|_\beta<2Rr_f+2\epsilon_H\|b\|_\beta.
                                                               \tag{S.14}
$$
所得完整尾、connector、长段和帽仍各自是原全频 PDE 解。
7200个非zero Fourier 坐标的**外边界行**被准确消去，
但输入 $b$ 的无限多个模仍存在，局部 nonlinear 解中的所有生成模也存在。

对高标签微分，$PD_0^{-1}D_0Q=0$，故
$$
 Dh_c^*(b)
 =-A_H(h_c^*(b)+b)^{-1}
       PD_0^{-1}D\mathcal F_c(h_c^*(b)+b)Q,
 \qquad \|Dh_c^*(b)\|<2\epsilon_H.                      \tag{S.15}
$$
真实 cap 参数 $c$ 的列由同一公式对 $c$ 微分，不能删除
$D_c\Phi$。复球上唯一性给联合全纯；实共轭、反射和标签相位平移均保持。

若消费本篇新94步末点，取 $b=Qa_{94}$。
其新的精确 head 修正满足
$$
 \|h_c^*(b)-Pa_{94}\|_\beta
 <\frac18 e^{\Delta_*M_0}
                   \|\mathcal F_c(a_{94})\|_{\mathfrak Z_{s_\beta}},
                                                               \tag{S.16}
$$
所以它是实际已到达输入上的小修正，不是另选一个更小的抽象球。

## 5. 真正剩下的高方程及完整 Schur 顺序

准确剩余仍是
$$
 \widehat{\mathcal F}_c(b)=
 Q\mathcal F_c(h_c^*(b)+b)=0.                            \tag{S.17}
$$
它的导数含完整有序 Schur 项
$$
 QD\mathcal F_cQ
 -QD\mathcal F_cP\,
   (PD\mathcal F_cP)^{-1}
   PD\mathcal F_cQ .                                    \tag{S.18}
$$
有限维源/靶空间使用(S.10)的实际权，
所以(S.18)中的逆就是(S.11)已支付的逆。
高→低→高路径没有被删掉。

第46束的实际高集合是
$\mathcal H_m=\{i:|m|\ge2^{18000}(j+5)^{60}\delta_j^{-129}\}$。
这与固定角 head $P$ 完全不同。
对每个频率，经真实深端允许线消去后，中间 radial Schur 是有限的，
但它的大小随 $|m|$ 增长。本文没有把(S.14)冒充这些全部移动块的逆，
也没有将不同频率的有限正距离取一个未经证明的正下界。

主旋转已由§1准确固定；非径向完整次相位及其 order-one 相对费用仍须付。
仅因 $\beta_i(a)-\beta_i(0)$ 绝对很小，不能删除其
$1/m$ 与已选 $1/(N_i m)$ 间隙之间的真实比较。

## 6. 任意固定模的实际有限 radial Schur 非奇异

下面固定径向原点 $\Gamma^0,t_0$ 和一个 $m\ne0$。
对任意 $J\ge129$，保留真实两行递推
$X_{j-1}=A_{m,j}X_j+f_{j-1}$，$129\le j\le J$。
在深端使用**完整未来尾**给出的实际允许线及有源 affine 端口；
在浅端使用真实 finite connector/long 的 raw 零 Dirichlet 行。
这定义一个方阵：$2(J-127)$个状态分量，
$2(J-128)$条胞元方程加一条深端线条件和一条外端行。

若此方阵有齐次核，将该核用其准确深端允许线延到整个平尾，
再用真实无源 finite connector 前推到外端。
全标签线性图的唯一性说明它是某个单位允许列 $\mathcal H_ma_m$。
外行恰为 $D_{0,m}a_m=0$；(S.3)给 $D_{0,m}\ne0$，
所以 $a_m=0$，整个状态为0。
有限方阵因此满秩。这是实际所有有限 Schur 的非奇异证明，
不需要假设 determinant 作为参数函数“应该不是恒零”。

其真正有源解在原标签空间中仍准确为
$$
 X=\mathcal Gf+
       \mathcal H D_0^{-1}(g-E\mathcal Gf).              \tag{S.19}
$$
先取各真实端口再限制到上述有限截面，恰是那个方阵的逆。
反之，由唯一性有限解与(S.19)相同。
若另外消去第46束已经可逆的真实高行，所得 Schur 的可逆性同样保持。
这一步不把经过缩放的 Airy 坐标 norm 免费当成标签 norm；
需要 Airy 两行时仍用其真实 density/normal-shear 矩阵作两侧变换。

已有完整 reference Green 给(S.19)在
$\mathcal F_{\beta+2080}\to\mathcal X_\beta$的 norm 小于 $2^{17}$。
因此所有 $0<|m|\le M$ 的任意 radial 截面同时有显式界
$$
 \|X\|_{\mathcal X_\beta}
 <2^{17}e^{2080M}
       \bigl(\|f\|_{\mathcal F_\beta}
                      +\|g\|_{\mathfrak Z_{s_\beta}}\bigr). \tag{S.20}
$$
这是有限频窗内的同权界，不是全频同权结论。
高模 ordinary源、未来尾 source 和外部 affine 行若不为0，
在(S.19)中各自保留，不能为了构成有限矩阵而丢掉。

## 7. ordinary、weak 两行、两端荷和真正 mean

对 mixed-tail 物理源采用
$$
 \operatorname{div}(G_0\nabla H)
       =s-\partial_tF^t-\partial_\theta F^\theta .
$$
完整 canonical总态的输入是
$$
 J_m=\binom{-\nu_m cF_m^t/p_\Gamma}
              {q(s_m-imF_m^\theta+m^2F_m^t)},
 \quad
 c=\frac{r^4}{\sqrt{12}\mu_j},\quad
 q=\frac{r^4}{12\mu_j}.                                  \tag{S.21}
$$
ordinary $s=w^2e$ 时第二行是
$\mu_jp_\Gamma^2e_m/(12r^{10})$。
两行的真实 $\mathcal S_{1,\beta}$ 范数用已证同一个
$(1+|m|)^{312}e^{|m|(\tau_{j-1}+\beta+\beta_j)}/\zeta_{j-1}$
及径向 $L^1$ 定义。故
$\|f\|_{\mathcal F_\beta}\le2^{450}\|J\|_{\mathcal S_{1,\beta}}$，
(S.20)的 mixed-tail ordinary/weak source 费用可取
$2^{467}e^{2080M}$。
这个式子没有 $\partial_tF^t$；source范数没有给出的
$F^t$ bare端迹仍须另付。finite connector 或帽源的实际 affine
行作为 $g$ 输入；本文不凭 tail norm 免费授它们的体源传播。

在物理 raw单位、整个实际有源区间上，mean 准确是
$$
 \pi_0(t)=\int_{t_f}^t s_0(u)du,\qquad
 h_0(t)=\rho\lambda+
            \int_{t_f}^t\frac{\pi_0-F_0^t}{\mu}\,du,
 \qquad\mu=w/a.                                         \tag{S.22}
$$
指定外 mean 高度 $h_o$ 只确定
$\rho\lambda=h_o-\int_{t_f}^{t_o}(\pi_0-F^t_0)/\mu$。
总 mean flux是输出 $\pi_0(t_o)=\int s_0$；若另给一个期望外通量，
其可解条件恰为这条等式，不能用第二个自由常数伪造。

设
$C_\pi=\int|s_0|$、
$C_h=\int\mu^{-1}(|\int_{t_f}^t s_0|+|F^t_0|)$。
在这些真实 weighted积分有限时，
$$
 \|\pi_0\|_\infty\le C_\pi,\quad
 \|h_0-h_o\|_\infty\le C_h,\quad
 \rho|\lambda|\le|h_o|+C_h.                              \tag{S.23}
$$
normal/bare恢复为 $\pi-F^t$，端点荷不清零。
非线性(S.14)只使 head非mean行相等；两个整体 mean小根
是否匹配仍随完整高残差(S.17)保留。
移动 cut的 $w_e\delta a_e$、参考高度积分及度量参数源均沿§2的
完整 map求导，不因为有限 head已解就删除。

## 8. 可立即消费的结论

同一新双参数径向参考、相同 finite connector/外第四保持曲线，
已经有：

- 真 principal KAM 的新目标实例化和全非线性外 map；
- 所有固定频率的真实有限 radial Schur非奇异、完整有源表达；
- 在实际长段小入口内，全部 $0<|m|\le14400$ 外行准确消元，
  任意更高标签、全 mean 与全部 source仍保留；
- 真正高方程(S.17)及所有高→低→高项的准确次序。

仍须为(S.17)中的全部移动中间块提供可和、可用于非线性迭代的相对逆，
并支付非径向完整次相位/幅度。这里的有限 head结论不能作为课题完成结论。
