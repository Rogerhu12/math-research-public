# R119 续篇：实际径向完整返回的首相位、双根两迹与全源

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对强尾的每个完整内部负型分量，在同一个真实
正型双端 DN、两个真实根和实际严格区中，完整径向返回的首相位现已
识别，包含原密度、两个 Airy 次首项和正确的 Maslov 号。对物理频率
$M=|m|=4n$，$n>0$，可选定一支返回行使其标量主式准确为

$$
 1+\exp\{i(n\omega+\beta/n)\},\qquad
 \omega=-8S=4\Theta,\quad
 S=\int_{I}\sqrt Q\,dt,\quad \beta=-b/2.
 \tag{N.1}
$$

另一实共轭支取此式的复共轭。这里 $Q=-A$，且真实首系数为

$$
 \boxed{\quad
 b=\frac12\int_{I_*}V_w\sqrt Q\,dt
 +\sum_{e=\pm}a_e\left[
     \frac12\int_0^H\frac{V_e(\xi)}{\sqrt\xi}\,d\xi
                         -\frac5{48H^{3/2}}\right],
 \qquad H=1/64.
 \quad}                                                     \tag{N.2}
$$

$I_*$ 是删去两个准确 $\xi_e\in[0,H]$ collar 后的全部严格区。
本篇给完整两行 Cauchy 和返回行的有界 $4/3$ 阶余项，而不是单列渐近。
正型 off-diagonal、所有源和 mean 仍作为实际网络的输入/输出保留。
全网络分母的逆及非径向更新仍需另付。

由[第43束](R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md)，
保持真实 $\omega$ 不变时，可以把本篇**完整 PDE 系数** $\beta$ 改动任意
$|\Delta\beta|\le1$，所需第二参数和第一参数的改动均小于 $2^{-86}$。
这不再是仅严格内部相位的条件性解释。

## 1. 完整对象与实际统一常数

使用已安装强尾及第43束的两实际负区 bump 盒
$|\gamma_1|\le2^{-18}$、$|\gamma_2|\le2^{-30}$。每个完整负分量跨至多
两个胞元，含一个下降段；根和所有正段完全不变。记 $J=j+5$、
$\delta=\delta_j$。下列粗包络在全部实际分量同时成立：

$$
 |I|<4\delta,\quad Q_{\max}<2^{12}J\delta^{-3/2},\quad
 |Q_t|<2^{18}J\delta^{-3},\quad
 |Q_{tt}|<2^{26}J\delta^{-9/2},\quad
 a_*<2^{16}\sqrt J\,\delta^{-9/4}.
 \tag{N.3}
$$

它们是[参考全频证明](R119-supplement-uniform-frequency-reference-Airy-Cauchy.md)
的实际门。新增 bump 对所需前三阶 log jets 的费由
$2^{-18}+4^k2^{-30}<2^{-16}$ 支付；它在自己支集上的 $Q_x>0$ 已由
整区间验证，所以单峰性保持。第四阶也有相同严格不等式。由
$|S^{(4)}|\le360$、$\|[64z^3(1-z)^3]^{(4)}\|_\infty\le4608$，
真实每个光滑片还满足

$$
 |Q_{ttt}|<2^{40}J\delta^{-6}.
 \tag{N.4}
$$

两个胞元原五平台/四过渡的至多18片，加两个内部 bump 的四个断点，
总数小于32。$Q,Q_t$ 连续，$Q_{tt}$ 的真实跳变保留；它们的总跳幅
不超过 $64\sup|Q_{tt}|$。没有把 $C^2$ 的 log profile 误当作全局解析。

在严格区 $Q>1/128$。由真实公式

$$
 V_w=\frac{Q_t}{2Q}-\frac{(1+Q)^2}{4Q}
                 +\frac{5Q_t^2}{16Q^3}-\frac{Q_{tt}}{4Q^2},
 \tag{N.5}
$$

前篇已给 $I_1:=\int_{I_*}|V_w|\sqrt Q\,dt<2^{60}J^2\delta^{-5}$。
再直接微分各光滑片：

$$
 (V_w)_t=\frac{Q_{tt}}{2Q}-\frac{Q_t^2}{2Q^2}
 -\frac14(1-Q^{-2})Q_t+\frac98\frac{Q_tQ_{tt}}{Q^3}
 -\frac{15}{16}\frac{Q_t^3}{Q^4}-\frac{Q_{ttt}}{4Q^2}.
 \tag{N.6}
$$

加上刚才的实际跳变，得到

$$
 \|V_w\|_\infty<2^{64}J^2\delta^{-6},\qquad
 \operatorname{Var}_{I_*}V_w<2^{96}J^3\delta^{-8}.
 \tag{N.7}
$$

变换 $ds=\sqrt Q\,dt$ 严格单调，所以总变差不变。真实有限分片和
全部跳幅是 (N.7) 的组成部分。

## 2. 两个真实负根的完整首 Dyson 系数

根变量和物理 height 使用
$U_e=\sqrt{a_eg_e\mu}\,h$、$\xi_e$ 向负区为正。准确方程为

$$
 U_{\xi\xi}+[\kappa_e^2\xi+V_e(\xi)]U=0,
 \qquad\kappa_e=M/a_e.
 \tag{N.8}
$$

完整复盘 $|\xi|\le1/4$ 上 $|V_e|<16$，故在真实 $[0,H]$ 上
$|V'_e|<16/(1/4-H)<128$。这些都是整盘界，不是有限根 jets 的外推。

在原 R39 两行 Airy 基 $F_*$ 中写 $z'=Kz$。若 $\kappa\ge2^{12}$，
完整实轴 Airy 界给

$$
 \int_0^H\|K\|_2d\xi<128\kappa^{-2/3}\le1/2.
 \tag{N.9}
$$

真实第一 Dyson 积分的同支项为

$$
 \operatorname{diag}\left(
 \frac{i}{2\kappa}\int_0^H\frac V{\sqrt\xi},
 -\frac{i}{2\kappa}\int_0^H\frac V{\sqrt\xi}\right).
 \tag{N.10}
$$

[R43 的完整积分证明](R43-first-airy-phase-and-four-thirds-remainder.md)
在这里仅消费实际标量 $|V|<16,|V'|<128$：根层切在 $\kappa^{-2/3}$，
同支替换费至多 $(50\pi+2)16\kappa^{-4/3}$，跨支积分费至多
$(50\pi+5)144\kappa^{-4/3}$。这是同一 $2\times2$ 矩阵的两个输入列。
二次及以上 Dyson 项由 (N.9) 给小于 $2^{14}\kappa^{-4/3}$；把纯虚
对角一次项改写成指数也有同阶界。因此准确 root amplitude 传播满足

$$
 C_e(H,0)=\operatorname{diag}(e^{i b_{V,e}/\kappa_e},
                              e^{-i b_{V,e}/\kappa_e})+R_e,
 \quad b_{V,e}=\frac12\int_0^H\frac{V_e}{\sqrt\xi},
 \quad\|R_e\|_2<2^{18}\kappa_e^{-4/3}.
 \tag{N.11}
$$

这里 $|b_{V,e}|<16\sqrt H=2$。两行、跨支和实际 potential 全部保留。

## 3. 原 Airy 根到实际严格 wave 两迹

令 $u=Q^{1/4}\sqrt\mu h$。在 $\xi_e=H$，准确有

$$
 u=\xi^{1/4}U_e/\sqrt{a_e},\qquad
 u_s=\varepsilon_e\sqrt{a_e}\xi^{-1/4}
                       (U_{e,\xi}+U_e/(4\xi)),
 \tag{N.12}
$$

其中 $s$ 总沿物理 $t$ 增加，$\varepsilon_-=1$、$\varepsilon_+=-1$。
所以原密度、根斜率、完整 shear 和右根方向均准确进入两行。

用统一的 wave 振幅

$$
 u=\frac c{\sqrt\pi}M^{-1/2}(w_++w_-),\qquad
 u_s=\frac {ic}{\sqrt\pi}M^{1/2}(w_+-w_-).
 \tag{N.13}
$$

注意 (N.12) 的 $a_e^{-1/2}$ 与 Airy 首项的
$\kappa_e^{-1/2}$ 恰好给 $M^{-1/2}$，两端没有未付的振幅比例。
原 R46 §8 的终端 Volterra 证明同时给高度和导数：若
$\eta=2\kappa\xi^{3/2}/3$，$A_*=5/72$，则归一的自由 Airy 两行
与 $e^{\pm i(\eta+\pi/4)}(1\mp iA_*/\eta)$ 的误差各小于
$1/(4\eta^2)$。在 (N.13) 的完整差/和两行中重组，并把一次项指数化，
在固定 $H$ 上有矩阵误差小于 $2^{21}\kappa^{-2}$。

因此根处到严格 cut 的真 map 是

$$
 L_e=\operatorname{diag}(e^{i\phi_e},e^{-i\phi_e})
                      +\widetilde R_e,
 \qquad
 \phi_e=\frac M{a_e}\frac23H^{3/2}+\frac\pi4
    +\frac{a_e}{M}\left[b_{V,e}-\frac5{48H^{3/2}}\right],
$$
$$
 \|\widetilde R_e\|_2<2^{24}(a_e/M)^{4/3}
 \tag{N.14}
$$

在后面的实际高频分界上成立。右根转到物理 wave 时还乘准确交换矩阵
$P=(0,1;1,0)$。这同时固定了 $-5/48$ 的号和两个 $\pi/4$；不能只取
height 的渐近式再猜 slope 或 Maslov 因子。

## 4. 整个严格区，及实际高频分界

在同一 $s$ 中准确有 $u_{ss}+(M^2+V_w)u=0$。去掉自由旋转后，
完整 wave generator 的对角为 $\pm iV_w/(2M)$，跨支为同系数乘
$e^{\pm2iMs}$。令

$$
 M_0=2^{72}J^2\delta^{-5}.
 \tag{N.15}
$$

当 $M\ge M_0$，$I_1/M<2^{-12}$，且两个根均有
$\kappa_e>2^{56}$。完整 strict propagator 和根 map 的正逆都小于2。
跨支积分作一次真实 BV 分部积分，费用为
$(2\|V_w\|_\infty+\operatorname{Var}V_w)/(4M^2)$；二次 Volterra 和
对角指数化的总费小于 $2I_1^2/M^2$。由 (N.7)，

$$
 W_* =\operatorname{diag}(e^{i\phi_*},e^{-i\phi_*})+R_*,
 \quad\phi_*=M\int_{I_*}\sqrt Q\,dt
                         +\frac1{2M}\int_{I_*}V_w\sqrt Q\,dt,
 \quad\|R_*\|_2<2^{128}J^4\delta^{-10}M^{-2}.
 \tag{N.16}
$$

不穿过仅 $C^2$ 接缝去使用一个虚构的解析径向估计。

由准确关系 $P L_+z_+=W_*L_-z_-$，根到根 Cauchy 矩阵为
$L_+^{-1}PW_*L_-$。结合 (N.14)--(N.16)，得到

$$
 z_+=\left[
  \begin{pmatrix}e^{-i\Phi}&0\\0&e^{i\Phi}\end{pmatrix}P
                   +E_{-,m}\right]z_-,
 \qquad \Phi=MS+\pi/2+b/M,
$$
$$
 \|E_{-,m}\|_2<2^{160}J^4\delta^{-10}M^{-4/3},
                           \qquad M\ge M_0.
 \tag{N.17}
$$

式 (N.2) 正是这个准确两行拼接的系数，不是发散积分的形式有限部。
由 $|b_{V,e}|<2$ 和已有 $a_e$ 界，直接有

$$
 |b|<2^{61}J^2\delta^{-5},\qquad |\beta|<2^{60}J^2\delta^{-5}.
 \tag{N.18}
$$

若改变合法 root cut，(N.12) 的自由 Airy 次首项与严格区新增的
$5/(16\xi^2)$ 密度项准确抵消；potential 积分补上其余部分。因此 (N.2)
也给同一个实际 Hadamard 有限部，而不依赖本篇选 $H=1/64$ 的便利。

## 5. 所有低模真实保留，并给统一强余项

对 $4\le M<M_0$，使用同一真实参考的全频两态界
$K_j=2^{5000}J^5\delta^{-10}$。根上从原梯度两态
$X=\sqrt\mu\operatorname{diag}(\sqrt\varpi,\varpi^{-1/2})(im h,h_t)$
到原 Airy 两振幅及其逆，完整 height/flux 公式给

$$
 \|T_e\|_2,\ \|T_e^{-1}\|_2
       <2^{12}a_*\rho_j M,
 \quad\rho_j=32J/\delta,
 \quad\varpi=\rho_j(1+M)^{-1/3}.
 \tag{N.19}
$$

例如两独立主系数是
$a^{1/6}M^{-2/3}\varpi^{-1/2}$、
$a^{-1/6}M^{-1/3}\varpi^{1/2}$；normal shear 还真实产生
$(\ell_\xi/2)a^{5/6}M^{-4/3}\varpi^{-1/2}$，其中
$|\ell_\xi|<1/32$。反向变换同样包含此 shear。原 Airy 根值矩阵的
固定常数由 $A_0,A_1,c$ 支付，(N.19) 为宽裕共同上界。

所以低频真实 Cauchy norm 加1，乘 $M_0^{4/3}$ 后小于
$2^{5400}J^{15}\delta^{-34}$。结合高频 (N.17)，所有非zero模统一有

$$
 \boxed{\quad
 \|E_{-,m}\|_2<2^{5600}J^{16}\delta^{-36}M^{-4/3}.
 \quad}                                                     \tag{N.20}
$$

这是一条真实全频界，没有扫描有限模后外推。

mean 不代入 $b/M$。它在 raw 高度/flux 中准确为
$p_0(t)=p_0(t_-)$、$h_0(t)=h_0(t_-)+p_0(t_-)\int_{t_-}^t\mu^{-1}$；
两端再用 (N.8)、原 R39 mean frame 作准确换元。由于
$\mu_{\max}/\mu_{\min}<2^{272}\delta^{-2}$，该 mean 矩阵的 norm
小于 $2^{290}a_*\delta^{-1}$，并可由同一更大的 (N.20) 常数携带。
真实外高度常数 $\lambda$ 和 mean flux 始终是两条独立状态。

## 6. 完整返回行的符号、跨分量项与首系数横截

用根幅度的上标 $+$、$-$ 区分两支。忽略余项只为显示已经识别的
主式时，(N.17) 是

$$
 z_R^+=e^{-i\Phi}z_L^-,\qquad
 z_R^-=e^{i\Phi}z_L^+.
$$

[真实正型双根证明](R119-supplement-actual-positive-two-root-Airy-defect-and-full-sources.md)
给 $z_e^-=-z_e^++e_e$；这里 $e_e$ **完整包含**相邻正分量两个根的
$(R_++I)$ 作用和该正分量的 affine source，不令它为0。代入两条
准确 Cauchy 行后，在左端得到的标量主系数是

$$
 1-e^{-2i\Phi}=1+e^{-i(2MS+2b/M)}.
 \tag{N.21}
$$

这就证明 (N.1) 的符号与因子。$z_L^-$ 的替换也必须应用于完整
$E_{-,m}$；它同 $e_L$ 的乘积仍保留。每条返回行只连接相邻有限多个
根端口。将真实所有这些项归入 $\mathcal E_m$，由 (N.20) 和正型
全矩阵强界得到一条宽裕的实际局部行预算

$$
 \|\mathcal E_m\|<2^{5800}J^{16}\delta^{-36}M^{-4/3}.
 \tag{N.22}
$$

在高频使用真实 Cauchy norm 小于8来估计其与正型 defect 的乘积；
低频使用 (N.19) 的真实矩阵和 $\|R_+\|=1$，再乘 $M_0^{4/3}$。
所以没有未经证明地把两个巨大强常数相乘后称为同一个常数。
两端相邻胞元的 $\delta$ 比例至多2，其 $2^{36}$ 和有限行度数已包含
在 (N.22) 的余量中。无限指标的实际权和全网 inverse 仍需另行支付。

两个新 bump 支集外的原密度、根、严格片和正段都准确不变。因此
沿第43束的准确保持 $\Theta$ 曲线，

$$
 \frac{d\beta}{d\gamma_2}
     =-\frac12\frac{d\mathfrak b}{d\gamma_2},\qquad
 \left|\frac{d\beta}{d\gamma_2}\right|>2^{-9}\sqrt B.
 \tag{N.23}
$$

那条曲线在 $|\gamma_2|\le2^{-31}$ 的两侧相位范围均大于 $2^{55}$。
所以任意 $|\Delta\beta|\le1$ 准确可达，且
$|\Delta\gamma_2|,|\Delta\gamma_1|<2^9/\sqrt B<2^{-86}$。
这是完整 PDE 首相位的横截；未知固定根偏移不曾被设为0。

## 7. 完整普通/弱 source 与 mean 仍使用实际传播

在每个负 collar，令 $T=\sqrt{a_eg\mu}$、
$\sigma_e=\operatorname{sign}(dt/d\xi)$、$r_\xi=(\log T)_\xi$。
对物理约定 $\operatorname{div}(G_0\nabla h)=s-\operatorname{div}F$，
准确有

$$
 F^\xi=\sigma_e F^t/T,\quad
 F_c^\theta=F^\theta/(a_egT),\quad
 s_c=s/(a_egT)-r_\xi F^\xi,
$$
$$
 U_{\xi\xi}-\frac{\xi}{a_e^2}U_{\theta\theta}+V_eU
       =s_c-\partial_\xi F^\xi-\partial_\theta F_c^\theta.
 \tag{N.24}
$$

定义 total canonical flux $P=U_\xi+F^\xi$，其真实两行源为

$$
 \partial_\xi\binom UP
 =\begin{pmatrix}0&1\\-(\kappa_e^2\xi+V_e)&0\end{pmatrix}\binom UP
                  +\binom{-F^\xi}{s_c-imF_c^\theta}.
 \tag{N.25}
$$

没有 $F^\xi_\xi$ 的额外正则性要求，但第一 source 分量与
$-r_\xi F^\xi$ 不能删除。bare 两迹由 $U_\xi=P-F^\xi$ 恢复，需要
真实端点迹时仍另给其范数。

整个负区的 ordinary/weak particular 使用准确两态 Duhamel，再按
(N.12)、(N.19) 逐端变换。不能用首相位指数代替真实 sourced propagator。
第41--42束的总 flux、归一 $W(q,v)=-1$ 和完整两列 Green 公式继续
成立。mean 在物理坐标中为
$p_0(t)=p_0(t_-)+\int s_0$、
$h_0(t)=\lambda+\int(p_0-F_0^t)/\mu$；它及两个正区 mean contact
完整进入剩余网络。

本篇已识别完整第一相位并支付其真实余项。尚未完成的是新相位目标的
全频算术选择、同一实际无限网络的分母/低块逆，以及非径向变化下的
全相位参数行。它们不能由 (N.22) 的阶数单独宣称小量吸收。

[完整代数与有向预算程序](../scripts/fourfold_actual_complete_radial_phase_20261113.py)
及[报告](../notes/2026-11-13-R119-complete-radial-phase-budget.json)
记录所有显示常数和两行/相位/source 的准确归一。
