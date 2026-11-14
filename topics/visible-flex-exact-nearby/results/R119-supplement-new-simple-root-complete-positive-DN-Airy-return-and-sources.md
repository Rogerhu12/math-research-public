# R119 续篇：新简单根到真实长段的完整正区 DN、Airy 返回及全源

2026-11-14，visible-exact / tail_connector。

**新固定 stop 对象上的完整外正区定理。** 使用
[新对象](../notes/2026-11-14-R119-simple-root-fixed-stop-new-object-and-transfer-gates.md)
及[新根的完整解析图](R119-supplement-new-fixed-stop-simple-root-full-analytic-chart-and-sources.md)，
把新根 $e_0$ 一直到原切口 $B$ 的整个非负 connector 与真实长段相接。
原准备段的零曲率平台、全部正平台、两个真实 mean、长段自然 mean 条件、
未匹配背景的真实修正及帽侧全部仿射列都保留。本篇不在根 collar 的外端添加边界。

下文构造的完整 Airy 返回记为 $\mathcal R_a$，约定根处
$z_-=\mathcal R_a z_+$。它包含全部 $4\mathbb Z$ 模及 mean。
真实、匹配总通量的比较问题给 onto unitary $\mathcal R_s$；
实际未匹配问题有
$$
 \|\mathcal R_a\|_{L^2},\quad
 \|\mathcal R_a^{-1}\|_{L^2}<2,
 \qquad
 \|\mathcal R_a+I:H^s\to H^{s+4/3}\|
 <2^{6000}b^{4/3},\quad |s|\le1 .
 \tag{P.1}
$$
这里 $2^{28}<b<2^{29}$ 是新根的真实斜率。强余项的两个方向、
全部低输入、mean 输出及远 angular lag 都已包含。

本篇给的是该新对象的完整外正区算子及源合同。它尚不把新外负分量
自动加入已选内部相位，也不把 $\mathcal R_a$ 的存在称作整个闭网络
已经可逆。尤其长段背景的粗 $2^{-18}$ 门只在本篇用于正型存在和
有界性，不被称作 $O(X)$ 的实际尾扰动。

## 1. 同一个实际外区间及保留的长段

从 $e_0$ 向外到 $B$ 取原物理 $t=\log a$。新对象的真实参数给
$$
 0\le A(t)\le3,\qquad 1<\ell<132,\qquad
 2^{-363}<\mu_0=w/a<5/18 .
 \tag{P.2}
$$
在两 bumps 上仍有 $7/8<A<9/8$，主放大平台 $A=3$；
准备段允许 $A=0$。新根附近 $A$ 从零以一阶增加。
这些是全真实区间的界，不把其中零平台换成严格椭圆区。

实际 connector 背景满足
$N_b< n_0=2^{-447}\|X\|_{\mathcal X_{224}}$，且有超过三单位的
额外角宽。原真实 long 解保持原 $a_*,\omega_*,L$，其完整背景
$N_L<2^{-18}$，角宽至少 $1/16$。
其 Jacobi 问题的外端指定非mean高度，**mean 使用自然总通量条件**；
平均高度只保留一个整体平移。因而在原物理 $B$ 口，
[真实 long mean 商](R119-supplement-actual-long-mean-quotient-and-unmatched-exterior-return.md)
(R.8)--(R.10) 给非负自伴算子
$$
 \mathcal N_B1=0,\qquad
 \frac1{16}\|f_\perp\|_{\dot H^{1/2}}^2
 \le\langle\mathcal N_Bf,f\rangle
 \le\|f_\perp\|_{\dot H^{1/2}}^2 .
 \tag{P.3}
$$
$\mathcal N_B$ 是真实完整 long 消元，已含另一端反射和独立 mean。
它不是半线 DN，也不是只保留一个首模的 Robin 常数。
帽侧非mean高度、long 体源、两端总 mean 荷及 weak 法向迹仍是独立
仿射输入，见第9节。

令 $K_T,K_L$ 是 $B$ 两侧的实际背景斜率，定义
$\mathfrak r=\|K_{T,\perp}-K_{L,\perp}\|_{\dot A^1_\sigma}$，
其中 $\sigma\ge1/16$。本篇用安全门
$$
 \mathfrak r<2^{-64}.
 \tag{P.4}
$$
它对当前新对象不是一个额外待验假设。真实 balanced 输出
$f_B,k_B$ 的范数和小于 $n_0$；原 long 解在 $f_*=0$ 时
$\|h(f_B,0)\|_{\mathcal Y}<17\|f_B\|$，而已证真正远端筛选给
$25e^{-7L/4}\|f_*\|$。故
$$
 \mathfrak r<2^{-440}\|X\|+25e^{-7L/4}10^{-8}<2^{-64}.
$$
使用的当前 $\|X\|\le2^{-8388608}$ 和原真实 $L>2^{24}$ 足够；
没有把一个上界下溢为零。mean 差仍由同一个 holonomy 小根恢复，
不能从此非mean定义中删除。

## 2. 短段漂移、整个闭型及实际界面差

原 raw 高度的完整散度矩阵为
$$
 G=\mu\begin{pmatrix}1&-d\\-d&d^2+A\upsilon^2\end{pmatrix},
 \quad
 \mu=\mu_0JD^{-3/2},\quad
 d=E(V-P)/J,\quad \upsilon=\sqrt D/J .
$$
只在长度小于132的 connector 上解真实 drift
$\Phi_t=-d(t,\Phi)$，$\Phi(e_0)=\mathrm{id}$。
其 Jacobian $j=\Phi_\eta$ 满足
$1/2<j<2$、$|j_\eta|<1/4$；正逆 pullback 在 $H^1$ 的范数小于2。
这些门由 $n_0$ 和真实长度直接给出，不把长段长度乘以其粗背景界。

置 $H=h\circ\Phi$。短段完整能量准确为
$$
 \mathfrak a_C(H,V)
 =\int\langle aH_t,\overline{V_t}\rangle
           +\langle b_\theta H_\eta,\overline{V_\eta}\rangle\,dt,
$$
$$
 a=(\mu\circ\Phi)j,\qquad
 b_\theta=A(\mu\upsilon^2\circ\Phi)/j,\qquad
 2^{-365}<a<2,\quad0\le b_\theta<24 .
 \tag{P.5}
$$
其中 $b_\theta$ 是本节的能量系数，不是根斜率 $b$。
整个 long DN 按同一 $B$ 端 pullback 及其对偶变换接入：
$$
 \mathfrak a_s(H,V)
 =\mathfrak a_C(H,V)
 +\langle\mathcal N_B(H_B\circ\Phi_B^{-1}),
                       V_B\circ\Phi_B^{-1}\rangle .
 \tag{P.6}
$$
因此常高度是唯一共同零方向，$B$ 的非mean迹由该型控制；
root 零迹的空间没有常数核。

对未匹配背景，保留真实
$$
 r_\mu=\mu_T/\mu_L,\quad b_\mu=\mu_T(d_L-d_T),\quad
 \mathcal P_{\mu_T}z=z-\frac{\mu_T}{\langle\mu_T\rangle}\langle z\rangle .
$$
原 (R.21)--(R.25) 的准确差仍是
$$
 \mathcal E_BH
 =\mathcal P_{\mu_T}
   [-(r_\mu-1)\mathcal N_B\Pi_\perp H+b_\mu H_\theta],
 \quad
 \mathcal E_B1=0,\quad\langle\mathcal E_BH\rangle=0 .
 \tag{P.7}
$$
实际型为 $\mathfrak a_a=\mathfrak a_s-\langle\mathcal E_BH_B,V_B\rangle$
（两端仍按 (P.6) 的真 pullback）。保守取
$$
 |\langle\mathcal E_BH_B,V_B\rangle|
 <\eta_B\|H\|_{\mathfrak a_s}\|V\|_{\mathfrak a_s},
 \qquad \eta_B=2^{48}\mathfrak r<2^{-16}.
 \tag{P.8}
$$
原实角费用 $2^{36}\mathfrak r$ 已足；这里多付12位，覆盖
$|\operatorname{Im}z|<1/256$ 平移后余宽改为 $1/32$ 的乘法、
两侧端角及对偶费用。没有用旧三阶根的平滑或端口常数。

在原零 root 迹能量空间，(P.8) 给真实 Neumann/Lax--Milgram 反演。
所得算子保留 $\mathcal E_B$，不是给一个并不存在的已匹配背景强加
正 Robin 条件。其伴随型有相同门。

## 3. 新根的严格正剪切及整个 root DN

新根的 $s_0\in(3/8,2/5)$ 满足
$S''(s_0)\ge72/25$、$S'(s_0)<15/8$。由新根 (A.8)，
$$
 \ell_{0,\xi}(0)=\frac1b+\frac25
              \frac{S''(s_0)}{20S'(s_0)^2}
 >\frac1{64},\qquad
 \ell_{0,\xi}(0)<\frac1{16}.
 \tag{P.9}
$$
非径向差在原完整复域中的一阶 Cauchy 费小于 $2^{27}n_0$。
所以实际实根上
$$
 1/128<\ell_\xi(0,\phi)<1/8 .
 \tag{P.10}
$$
这是本新对象的严格符号；不来自旧 quartic 根。

用新根 canonical 正变量 $y=-\xi$，$0\le y\le H=1/64$。
真实能量密度为
$\alpha\,\operatorname{diag}(1,y/b^2)$，且
$$
 |V|<17,\qquad
 |\nabla\log\alpha^{-1/2}|_{\operatorname{diag}(1,y/b^2)}<5 .
 \tag{P.11}
$$
它是 (P.6) 中真实 collar 的限制。
canonical 高度为 $u=\sqrt\alpha\,h$。
把 raw DN 共轭到该高度，令
$$
 P_s=M_{\alpha_e^{-1/2}}\mathcal N_{e_0,s}
                   M_{\alpha_e^{-1/2}},\qquad
 R_s=P_s+\tfrac12M_{\ell_\xi(0)} .
 \tag{P.12}
$$
$P_s$ 非负自伴，$R_s$ 严格正；共同物理常高度仍是 $P_s$ 的核。
(P.12) 的剪切只是原准确两行恢复，并没有给原 mean 新加边界条件。
实际未匹配 $R_a$ 以 $\mathfrak a_a$ 同样定义，包含其全部非自伴小差。

下面给出根 trace 的真实空间和足够的双向型界。令
$$
 \kappa_m=|m|/b,\qquad
 W_m=(1+\kappa_m^{4/3})^{1/4},\quad m\in4\mathbb Z .
$$
$W_0=1$。则
$$
 2^{-16}\|Wu_0\|_2^2
 \le\langle R_su_0,u_0\rangle
 \le2^{11}\|Wu_0\|_2^2 .
 \tag{P.13}
$$
完整型域是 $H^{1/3}_\kappa$，与 $\|Wu_0\|_2$ 等价。
它含 mean，并非先商去两个 mean 后补一个形式零槽。

## 4. (P.13) 与完整 Poisson 的局部能量证明

给定根数据 $u_0$，取
$a_\kappa=H^{-1}+\kappa^{2/3}$，在实际 canonical collar 使用
$$
 v_\kappa(y)=
 \frac{e^{-a_\kappa y}-e^{-a_\kappa H}}
      {1-e^{-a_\kappa H}}(u_0)_m ,
 \qquad 0\le y\le H ,
 \tag{P.14}
$$
其外零延拓作为能量 lift。分母大于 $1/2$。
对平坦 collar 能量
$E_{\rm fl}=\int(|v_y|^2+\kappa^2y|v|^2)$，逐模有
$$
 E_{\rm fl}\le(2a_\kappa+\kappa^2/a_\kappa^2)|(u_0)_m|^2,
 \qquad \int|v|^2\le2a_\kappa^{-1}|(u_0)_m|^2 .
$$
(P.11) 把真实能量控制在 $2E_{\rm fl}+50\int|v|^2$ 内；
故完整 lift 能量小于 $2^{10}\|Wu_0\|_2^2$。
它在 $B$ 为零，所以不漏掉 long DN 项。
全域能量最小化给真正 Poisson 解及同一个能量上界。

为付清 local $L^2H^{2/3}_\kappa$，对任意 collar 函数先证明
$$
 \int_0^H(1+\kappa^{4/3})|u|^2
 \le256|u(0)|^2+18E_{\rm fl}.
 \tag{P.15}
$$
若 $\kappa\ge H^{-3/2}=512$，置 $d=\kappa^{-2/3}\le H$。
对 $0\le y\le d$，把
$|u(y)|^2\le2|u(s)|^2+2d\int_0^d|u'|^2$
在 $s\in[d/2,d]$ 上平均；再在 $y\ge d/2$ 用
$\kappa^2y\ge\kappa^2d/2$。得到
$\kappa^{4/3}\int|u|^2\le2\int|u'|^2+9\int\kappa^2y|u|^2$。
低 $\kappa$ 则直接使用
$\int|u|^2\le2H|u(0)|^2+H^2\int|u'|^2$。
两者即给 (P.15)，全 Fourier 和用 Parseval。

同一最后一个不等式和 (P.11) 给
$E_{\rm fl}\le3E_{\rm collar}+2|u(0)|^2$，
故
$$
 \|u\|_{L^2_yH^{2/3}_\kappa}^2
 \le512\|u_0\|_2^2+64E_{\rm collar}.
 \tag{P.16}
$$
这证明完整 Poisson 的实角界小于 $2^{10}$。
这里没有给未知解在 $y=H$ 添加 Dirichlet 或 outgoing 条件。

同样，平均积分还给高区的 trace 界
$\kappa^{2/3}|u(0)|^2\le20E_{\rm fl}$。
用 $\kappa^{2/3}\ge64$ 吸收右侧的 $40|u(0)|^2$，得
$\kappa^{2/3}|u(0)|^2<256E_{\rm collar}$。
低区 $W^2\le65$ 则由 (P.10) 的 $R_s\ge1/256$ 控制。
结合 lift 上界即证 (P.13)。特别 mean 的下界由真实 density shear
支付，不是假定其 Dirichlet 能量为正。

## 5. 真复角族、全 mean Cayley 与 onto 性

先以径向 reference 的整个 connector 加原径向 long DN 作共同型。
短 drift 的相对误差由长度132及 $n_0$ 控制；long 只用其已付
$N_L<2^{-18}$ 的**相对正型差**，不乘长 $L$。
在 $|\operatorname{Im}z|<1/256$ 内，完整相对型误差可取
$2^{-10}$；加 (P.8) 后仍小于 $2^{-9}$。
证明 long 项可直接把 $B$ 的角图在整个 long 中保持为同一个
$t$ 无关 pullback。原 mean 自然边界在该 pullback 下不变，
其真实非mean数据用对偶角图转换；不需让 drift 流穿过长 $L$。

为在同一个**固定 canonical collar**证明复 Poisson，
把新根的真实 inverse chart $\Psi_c=(t_c,\theta_c)$ 在
$0\le y\le H$ 原样使用。记
$t_0(y)=t_e-x_0(-y)/b$、
$\Psi_d(y,\phi)=(t_0(y),\Phi(t_0(y),\phi))$。
在 $H\le y\le2H$ 取固定 quintic cutoff $\chi$，内端为1、外端为0，
$\|\chi'\|<2^8,\|\chi''\|<2^{17}$，并定义
$\Psi_b=\Psi_d+\chi(\Psi_c-\Psi_d)$；外侧继续真实 drift 图。
这里 $2^{28}<b<2^{29}$，且参考
$A(t_0)=y g_0^2>1/128$、$1/2<g_0<2$。

以下把这次换图的相对型费单独展开。新根 (A.15)--(A.16)
及其 $2\times2$ inverse Jacobian 公式给
$$
 b|t_c-t_0|<2^{15}n_0,\quad
 b|\theta_c-\phi|<2^{11}n_0,\quad
 b|\partial_y(t_c-t_0)|+
 b|\partial_\phi(t_c-t_0)|<2^{24}n_0,
$$
$$
 b|\partial_y(\theta_c-\phi)|+
 b|\partial_\phi(\theta_c-\phi)|<2^{24}n_0.
$$
例如 inverse 的分母是
$\xi_x\phi_\theta-\xi_\theta\phi_x$，距 $g_0$ 小于
$2^{19}n_0$；代入 (A.15) 后即得这些宽门。
在该 buffer 上 $t_0-t_e<1/(8b)$；
$|d|<2^8n_0$ 及其窄一单位角宽的一阶 Cauchy 界给
$\Psi_d-(t_0,\phi)$ 的上述三类 $b$ 倍费用均小于 $2^{12}n_0$。
乘回 $\chi,\chi'$ 后，若 $\Psi_b=(t,\theta)$，便有
$$
 b|t-t_0|<2^{16}n_0,\qquad
 b\bigl(|t_y-t_0'|+|t_\phi|+
        |\theta_y|+|\theta_\phi-1|\bigr)<2^{27}n_0.
$$
这一步没有让无量纲角位移丢掉原 $b^{-1}$。

置 $J_0=\operatorname{diag}(t_0',1)$、
$J=D\Psi_b$、$E=J_0^{-1}J-I$，
$S=\operatorname{diag}(1,\sqrt y/b)$。
因 $1/(2b)<t_0'<2/b$、$y^{-1/2}\le8$，逐项有
$$
 |E_{11}|<2^{28}n_0,\quad |E_{12}|<2^{28}n_0,\quad
 |E_{21}|+|E_{22}|<2^{27}n_0/b,
$$
$$
 \|S^{-1}ES\|<2^{32}n_0,\qquad
 |\det J/t_0'-1|<2^{30}n_0 .
$$
其中下左项准确乘 $b/\sqrt y$、上右项乘 $\sqrt y/b$；
所以这些门对整个 $2^{28}<b<2^{29}$ 统一成立。
同时 $|A_t|<4b$、$|(\log\mu_0)_t|\le4$ 给
$|A(t)/A(t_0)-1|<2^{25}n_0$。
原 $|d|,|\upsilon-1|<2^8n_0$、$\mu/\mu_0-1$ 的同阶门，
在 $A>1/128$ 下把准确物理矩阵
$\mu\left(\begin{smallmatrix}1&-d\\-d&d^2+A\upsilon^2\end{smallmatrix}\right)$
变成规范矩阵时，完整系数差小于 $2^{30}n_0$。

最后使用准确 pullback
$\widetilde G=(\det J)J^{-1}GJ^{-T}$。
相对于 $\widetilde G_0=\alpha_0S^2$，它是
$\det J/t_0'$、$(I+S^{-1}ES)^{-1}$、上述系数矩阵
及该 inverse 的 transpose 的有序乘积。
由 $\|(I+S^{-1}ES)^{-1}\|\le(1-2^{32}n_0)^{-1}$，
其与 $I$ 的差小于 $2^{37}n_0<2^{60}n_0$。
在 $y\le H$ 使用准确对角图，不除以 $\sqrt y$；
在 $y\ge2H$ 使用已经支付的 drift 图。
这支付整个复域的混合换图，而没有把实能量结论直接延拓成复域界。

根上的实际 $\alpha_e$ 与参考 $\alpha_{0,e}$ 的乘法变化也不能
因共同常数核而漏掉。用 (P.13) 的 $2^{-16}$ trace 下界、
$2^{11}$ 上界和新根的角解析乘法界，完整根共轭及剪切差在
$R_0$ 的型 norm 中小于 $2^{80}n_0$。
因此可共同取
$$
 |\langle(R_a(z)-R_0)f,g\rangle|
 \le\epsilon_R\,
 \langle R_0f,f\rangle^{1/2}
 \langle R_0g,g\rangle^{1/2},\qquad \epsilon_R<1/64 .
 \tag{P.17}
$$
$R_0$ 是径向新对象的完整 root Robin，含其正 mean shear。
上述参数均在本新对象已付门内；没有把旧根的零 mean 框架转授。

用同一原 Airy 常数
$c_A=-\operatorname{Ai}'(0)/\operatorname{Ai}(0)>0$、
$c=c_A^{-1/2}$，在根处保两列
$$
 D_\pm(0,m)=c\kappa^{-1/3}[\operatorname{Bi}(0)\pm i\operatorname{Ai}(0)],
$$
$$
 D_\pm'(0,m)=-c\kappa^{1/3}
       [\operatorname{Bi}'(0)\pm i\operatorname{Ai}'(0)],
 \qquad m\ne0 .
$$
mean 仍是 $c$ 和 $\pm ic/\pi$。
$\operatorname{Bi}(0)=\sqrt3\operatorname{Ai}(0)$、
$\operatorname{Bi}'(0)=-\sqrt3\operatorname{Ai}'(0)$ 及 Wronskian
给准确 diagonal impedances
$$
 Z_\pm=-A_0\pm iB_0,\quad
 (A_0)_m=\tfrac12c_A\kappa^{2/3},\quad
 (B_0)_m=\tfrac{\sqrt3}{2}c_A\kappa^{2/3}\quad(m\ne0),
$$
$$
 (A_0)_0=0,\qquad (B_0)_0=1/\pi .
 \tag{P.18}
$$
本节 $A_0,B_0$ 是这些 Fourier 乘子，不是根多项式 $B_0(x)$。
令 $\chi=c/\sqrt\pi$，$E_+$ 在非mean上为 $e^{i\pi/6}$、mean上为1。
完整初值高度系数准确为
$D_\pm(0)=\chi B_0^{-1/2}E_\pm$，$E_-=E_+^*$。
于是
$$
 S_a=B_0^{-1/2}(R_a+A_0)B_0^{-1/2},\qquad
 \boxed{\quad
 \mathcal R_a=-E_+(S_a+i)^{-1}(S_a-i)E_+ .
 \quad}
 \tag{P.19}
$$
这是全部 mean 与非mean同时成立的算子式，不先把 mean 单独解完再
忽略混频行。对于真实对称问题，$S_s\ge0$ 自伴，故 (P.19)
真正 onto unitary。

对复族和实际未匹配型，(P.17) 仍是相对于正型
$R_0+A_0$ 的同一误差。写
$S_a=S_0+S_0^{1/2}ES_0^{1/2}$，$\|E\|<1/64$。
由
$\|S_0^{1/2}(S_0\pm i)^{-1}\|\le1/\sqrt2$、
$\|S_0^{1/2}(S_0\pm i)^{-1}S_0^{1/2}\|\le1$，
实际 resolvent 的 Neumann 级数给两 Cayley 与参考之差
小于 $\epsilon_R/(1-\epsilon_R)<1/63$。
所以 (P.1) 的两个同阶 $L^2$ 门成立，正逆皆为全纯有界族。
这不是由 J-unitarity 猜一个正定 $L^2$ norm。

## 6. 完整 collar contact，包括复族和伴随

(P.14)--(P.16) 的 lift、全域型 inverse，以及第5节的真复域
比较共同给
$$
 \|\mathcal P_{e_0}:H^{1/3}_\kappa
            \longrightarrow L^2_yH^{2/3}_\kappa\|<2^{16}.
 \tag{P.20}
$$
这是足够宽的统一常数：实角门小于 $2^{10}$，标准 Bessel 权
与 $W$ 的比较小于2，复型 inverse、根乘法及伴随各用不到2倍，
全部仍在显示的64倍余量中。
同一证明适用于实际非自伴小差的伴随型。

零 root Dirichlet 的 canonical ordinary collar 源 $f$，
其完整 outward contact 是对应 Poisson 的负 adjoint；
因而
$$
 \|K_cf\|_{H^{-1/3}_\kappa}
 <2^{16}\|f\|_{L^2_yH^{-2/3}_\kappa}.
 \tag{P.21}
$$
它是包含真正 $B$ 外响应的全域 contact。
根 collar 外的解及两端背景差没有被删去。

contact 到任一原 Airy 波的非mean因子准确为
$(\pi\operatorname{Ai}(0)/c)\kappa^{-1/3}$，mean因子为
$\pi/(2c)$。因此在 (P.21) 的标准权下，
$$
 N_m<4\quad(\kappa\ge1),\qquad
 N_m<4b^{1/3}\quad(m\ne0),\qquad N_0<2 .
 \tag{P.22}
$$
这里依照原完整 Airy 初值，不把低非mean因子错误地换成
mean 的费用。

## 7. 全高输入强 $4/3$ 余项，低输入仍是真列

令 $\mathcal D=\langle D_\phi\rangle$，
$L_*=2^{4200}b$，$P_H=\mathbf1_{\{|m|\ge L_*\}}$。
对这些高输入，使用原完整 trial
$$
 U_{\rm tr}=2ic\kappa^{-1/3}\operatorname{Ai}(y\kappa^{2/3})\chi_H(y),
$$
其中 $\chi_H=1$ 于 $[0,H/2]$、在 $y=H$ 连同前两 jets 为零；
$\|\chi_H'\|<2^8$、$\|\chi_H''\|<2^{17}$。
在全部低输入列取零 trial，包括 mean。其完整 residual 是
$$
 f_{\rm tr}=-V\chi_HU_0-2\chi_H'U_0'-\chi_H''U_0 .
 \tag{P.23}
$$
trial 零延拓到真实其余正区，故不产生任何隐藏界面原子。
用全域零 root Dirichlet inverse 校正 (P.23)。

[完整正片斜率余项证明](R119-supplement-positive-full-Airy-remainder-in-root-slope-units.md)
(P.10)--(P.15) 的三项计算只用本篇重新付清的 (P.11)、
同一 collar 和同一原 Airy 波；不要求第二个根或特定全正区长度。
逐项重用其 Parseval、完整乘法及 cutoff 衰减得到
$$
 \|f_{\rm tr}P_H\mathcal D^{4/3}:
          L^2\to L^2_yH^{-2/3}_\kappa\|
 <2^{30}b^{4/3}.
 \tag{P.24}
$$
完整 potential、mean 输出及所有 angular lag 均在该式内。

$E_A,E_B$ 只记高输入校正残差列，并在低输入上零延拓，
所以 $E_A=E_AP_H,E_B=E_BP_H$。校正后的真正高输入列是
$A_{\rm in}=(I+E_A)P_H,\ A_{\rm out}=(-I+E_B)P_H$。
(P.21)--(P.24) 给全输出安全费
$2^{50}b^{5/3}$；输出 $|m|\ge L_*/2$ 时改为
$2^{50}b^{4/3}$。余下低输出使用真实角平移族：
在输入两个 Fourier 锥分别沿相反方向多移 $i/512$，
连同基点 $|\operatorname{Im}z|<1/1024$ 仍在 $1/256$ 内。
它给准确隔带因子 $e^{-L_*/1024}$，所以低输出中的额外
$b^{1/3}$ 被付清。该论证是整个算子的带间估计，非逐列高度界。

准确 graph 恒等式为
$$
 \mathcal R_a(I+E_A)P_H=(-I+E_B)P_H,\qquad
 (\mathcal R_a+I)P_H=(E_B-\mathcal R_aE_A)P_H .
 \tag{P.25}
$$
没有反演一个可能不可逆的 trial incoming 矩阵。
低输入仍由真正的 $(\mathcal R_a+I)P_L$ 给出，
其右乘 $\mathcal D^{4/3}$ 费用小于
$3\langle L_*\rangle^{4/3}<2^{5605}b^{4/3}$。
合并高输入和全 $L^2$ graph 门，先得到右强窗。

为了付另一侧，必须注意实际未匹配 $\mathcal R_a$ 不必 unitary。
真实伴随型给
$$
 \mathcal R_{\rm adj}=\mathcal R_a^{-*},
 \qquad
 \mathcal R_a^*+I=\mathcal R_a^*(\mathcal R_{\rm adj}+I).
 \tag{P.26}
$$
第一式直接对 (P.19) 取 adjoint，保 $E_\pm$ 次序。
伴随型有同一个 root 局部算子、contact 和复域门，
所以其右强窗已由上述同一证明取得。
第二式于是给 $\mathcal R_a^*+I$ 的右强窗，取 adjoint 即为
$\mathcal R_a+I$ 的左强窗；没有借未成立的 unitarity。

最后在余下的真复角条带上取至多四阶 Cauchy 交换子，再用整数
Sobolev 乘积、对偶和插值。每一轮的四阶费用小于 $2^{80}$；
两强窗、伴随变换和矩阵合并最多再收两轮。
由 $5605+160+20<6000$ 得到 (P.1)，$|s|\le1$。
这也明确覆盖全部低列和 mean-to-high 输出。
所用 $2^{6000}b^{4/3}$ 是新完整对象的费用，不是旧正片结论的
未核转授。

## 8. 原 mean、未匹配径向行与真正的 affine 外口

原 raw $B$ 接口仍准确为
$$
 \pi_{\rm tmp}=r_\mu\pi_L+b_\mu H_\theta+\mu_Tb_\perp
                      +F_T^t-r_\mu F_L^t,
$$
$$
 \pi_T=\mathcal P_{\mu_T}\pi_{\rm tmp}
             +\frac{\mu_T}{\langle\mu_T\rangle}q_T,\qquad
 c_B=\frac{q_T-\langle\pi_{\rm tmp}\rangle}{\langle\mu_T\rangle}.
 \tag{P.27}
$$
$c_B$ 是真实 mean 径向斜率差，归一化 $K$ 单位须除
$a_Bw_B$。它仍是输出；只在原 nonlinear 非mean matching 真正为零
后，同一 holonomy 小根才使该差为零。
$\lambda$ 仍是唯一整体高度平移。

完整外仿射项是
$$
 b_B=\mathcal P_{\mu_T}
 [r_\mu(-\mathcal N_{BA}f_*-\ell_B+q_L)
                  +\mu_Tb_\perp+F_T^t-r_\mu F_L^t]
       +\frac{\mu_T}{\langle\mu_T\rangle}q_T .
 \tag{P.28}
$$
其中 $q_L=q_A-\int g_0$，$f_*$ 用原真实物理高度单位。
帽侧的全部 high/low cross、long 两端反射、两条 mean 与
ordinary/weak 体源都在此式内。若另有高度跳，按原 (R.21)--(R.23)
先改 $H_T=H_L+u$ 并加入 $-\mu_Td_Tu_\theta$。
这些项不因本篇的齐次图已经存在而变成零。

## 9. 原物理 ordinary、weak 与原子源的充分合同

在真实短段保
$\operatorname{div}(G\nabla h)=g-\operatorname{div}\mathbf F$，
令
$$
 \mathscr P=\|g\|_{\mathcal M_tL^2_\theta}
       +\|F^t\|_{\mathcal M_tH^1_\theta}
       +\|F^\theta\|_{\mathcal M_tH^1_\theta},
 \qquad \mathscr B=\|b_B\|_{H^{-1/2}_\theta}.
 \tag{P.29}
$$
端点原子另作为 boundary 荷给出。此合同包含原径向 $L^1$ 源，
不要求 weak 源有径向导数。长段源通过原完整 long 合同形成
(P.28)，其物理尺度和长度费用原样保留。

短段的真实 fixed-$t$ Piola 变换是
$$
 \widetilde g=j(g\circ\Phi),\quad
 \widetilde F^t=j(F^t\circ\Phi),\quad
 \widetilde F^\eta=(F^\theta+dF^t)\circ\Phi .
$$
令
$$
 K(t)=-\int_{[e_0,t)}a^{-1}\,d\widetilde F^t,\qquad H=K+V .
 \tag{P.30}
$$
这里须付 $a^{-1}$ 的角导。原 $n_0$ 角解析余量和
$\mu=\mu_0JD^{-3/2}$ 给
$|\mu_\theta/\mu|<2^{10}n_0$、$|d_{\theta\theta}|<2^{10}n_0$。
由 $j_t=-d_\theta(t,\Phi)j$，有
$$
 \left|\frac{j_\eta}{j}\right|
 =\left|\int_{e_0}^t d_{\theta\theta}(s,\Phi)j\,ds\right|
 <2^{19}n_0,\qquad
 \left|\frac{a_\eta}{a}\right|
 =\left|(\mu_\theta/\mu)\circ\Phi\;j+j_\eta/j\right|
 <2^{20}n_0<1 .
$$
结合 $a>2^{-365}$，乘以 $a^{-1}$ 在真实 $H^1$ 上的范数小于
$2^{366}$。上述 Piola 法向列在 $H^1$ 的费用小于8，
所以 Bochner 测度积分 (P.30) 确给
$\sup_t\|K(t)\|_{H^1}<2^{370}\mathscr P$。
零 root 迹空间的径向 Poincare 门仍为
$\sup\|V(t)\|_2<2^{187}\|V\|_{\mathfrak a_s}$、
$\|V\|_{L^2}<2^{190}\|V\|_{\mathfrak a_s}$；
这些只用真实短长度和 $a>2^{-365}$，与旧零平台 lift 无关。

准确新源是
$\widetilde g-\partial_\eta\widetilde F^\eta
       -\partial_\eta(b_\theta K_\eta)$，
另有真实 $B$ 边界荷
$-(\mathcal N_B-\mathcal E_B)K(B)$ 及 $b_B$。
它们的零 root 能量对偶 norm 小于
$$
 2^{380}\mathscr P+2^{190}\mathscr B .
 \tag{P.31}
$$
这里 $\sqrt{\int b_\theta}<64$，完整 $B$ 非mean迹由 (P.3)
控制，而其 mean 由上述径向 Poincare 控制。
特别没有在零曲率平台除以 $b_\theta^{1/2}$。

(P.14) 的根 lift 与径向 Poincare 给
$\sup\|H_f(t)\|_2<2^{194}\|u_0\|_{H^{1/3}_\kappa}$；
能量范数小于 $32\|u_0\|_{H^{1/3}_\kappa}$。
这里实角 (P.14) 的更细平方界小于 $2^9\|Wu_0\|^2$，
而实际小型差 $\eta_B<2^{-16}$ 的修正仍留在该32门内。
因此 Green 配对保留全部 source contact 后，canonical 根端荷的
$H^{-1/3}_\kappa$ norm 小于
$2^{410}\mathscr P+2^{210}\mathscr B$。
(P.22) 和完整 $\|\mathcal R_a\|<2$ 最后给原 Airy affine 列
$$
 \boxed{\quad
 \|b_{e_0}^{\rm Airy}\|_2
 <2^{512}(\mathscr P+\mathscr B).
 \quad}
 \tag{P.32}
$$
包括 independent mean source。相同构造保守地给实际短段
$(h,\pi)$ 的 $L^2$ 范数小于
$2^{640}(\|z_+\|_2+\mathscr P+\mathscr B)$。
对测度源这是 BV/单侧迹解，不冒称每处连续。

高度/总通量跳 $(a_s,b_s)$ 准确编码为
$F^t=-\mu a_s\delta_{t_s}$、
$F^\theta=d\mu a_s\delta_{t_s}$、
$g=b_s\delta_{t_s}$；每原子的费用为
$\|b_s\|_2+4\|a_s\|_{H^1}$。原两 $\Gamma^*$ 列分别通过
(P.28)、(P.30) 和 (P.32)，不得因固定 stop 的 compact metric
在此无体源而丢掉它们的端迹。
$\nu$ 及其它 metric 方向仍从自己的真实源和帽侧输入进入。

所有图一直用 total 通量。恢复 bare 端口必须另给原 $F^t$
端点迹；径向 $L^1$ 或测度范数不自行授予该迹。原物理
normal/grounded 及水平重建仍使用新对象自己的尺度和准确两行，
不由 (P.32) 免收费。

## 10. 本结论与下一项

新简单根现在已有整个真实外正区的完整 DN/Poisson，
实际未匹配 mean 商、原 Airy 返回、双侧强 $4/3$ 余项及完整
ordinary/weak/原子/外端源列。long 的未知高模始终保留在
$\mathcal N_B,\mathcal N_{BA}$ 中，未用给定 head 的帽高图替代。

接下来要把新完整负分量的两 $\Gamma$、第五形状盒、固定相位和
这个实际外返回并入全网络。全部构造对本新对象原复参数盒统一全纯；
参数微分按真实圆盘半径收取 $q!r_p^{-q}$，不重新扩大控制盒。对径向参考与实际 long 的小差，还应
使用其真正远端筛选和完整 Frechet 列进一步付同空间 norm；
本篇粗 $N_L<2^{-18}$ 只证明全域有界性，绝不冒作当前极小 $X$
的同阶量。闭网络 inverse、原强标签权与最终 nonlinear matching
继续保留为下一项。
