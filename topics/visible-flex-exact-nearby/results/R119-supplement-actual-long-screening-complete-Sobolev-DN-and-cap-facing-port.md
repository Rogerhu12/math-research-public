# R119 续篇：真实 long 屏蔽到完整 Sobolev DN、独立帽端口及新外返回的小差

2026-11-14，visible-exact / tail_connector。

**同一新简单根对象上的完整算子估计。** 本篇接
[新完整正区](R119-supplement-new-simple-root-complete-positive-DN-Airy-return-and-sources.md)，
把原真正 nonlinear long 屏蔽转成所有角频和 mean 同时成立的
$H^{1/2}\to H^{-1/2}$ DN 差。帽侧实际非mean物理曲率
$Z=(C_R-C_r)_\perp$ 保持独立；准确 $C_R\to f_*$ 反馈
$f_*=\Phi_R(Z,f_B)$ 包含在导数中。长段的粗 $N_L<2^{-18}$
只给存在；本篇取得的小差使用准确指数 $e^{-7L/4}$，不乘长 $L$。

记 $X=\|X\|_{\mathcal X_{224}}$、
$n_0=2^{-447}X$、$\epsilon=e^{-7L/4}$、
$F=\|f_B\|_{\dot A^2_{1/16}}\le n_0$。
同一角表示中，固定实际 $Z$、包含上述真实反馈的新外返回与新径向参考满足
$$
 \max_{0\le q\le4}
 \|\operatorname{ad}_{D_\phi}^{\,q}
       (\mathcal R_{a,Z}-\mathcal R_0)\|_{L^2\to L^2}
 <2^{160}(n_0+F+\epsilon).
 \tag{N.1}
$$
相同右端也可作为 $H^s\to H^s$ 的上界，$|s|\le2$。
因此在当前真实球 $X\le2^{-8388608}$，
$$
 \|\mathcal R_{a,Z}-\mathcal R_0\|_{H^s\to H^s}
 <2^{-280}X+2^{160}\epsilon<2^{-8388864}.
 \tag{N.2}
$$
这不是完整闭网络逆：新外负分量的相位选择、全源的原标签权与最终
闭合仍须接续。本篇的返回和 DN 均不是有限角截断。

## 1. 同一个 long、真正帽图与独立 mean

新对象只改变远端 finite connector；$a_*,\omega,L$ 和实际帽图保持
[新对象](../notes/2026-11-14-R119-simple-root-fixed-stop-new-object-and-transfer-gates.md)
的已付身份。原长段
$$
 t\in[0,L],\quad a=a_Be^t,\quad w=a/(4\omega),\quad
 L=\omega(2^{24}-25/8)>2^{24},\quad 7/5<\omega<3/2
 \tag{N.3}
$$
没有重解或换成半线。真实高度为
$$
 v=awh+v_0,\qquad
 v_0(t)=\lambda+\int_0^t aw\,\mu_s(h)\,ds ,
 \qquad \langle h\rangle=0 .
 \tag{N.4}
$$
两端非mean输入是 $h(0)=f_B,h(L)=f_*$。
$\mu_s(h)$ 是原 holonomy-one 小根；一个整体高度平移 $\lambda$
仍独立，两端 mean 高度不能再分别任意指定。

记完整归一化斜率
$$
 \mathcal K_B(f_B,f_*)=
 [\,2f_B+h_t(0)\,]+\mu_0(h),\qquad
 \mathsf C_L=|D_\theta|\coth(L|D_\theta|)\Pi_\perp .
 \tag{N.5}
$$
方括号是非mean部分，后项是 mean。输出空间取
$\dot A^1_\sigma\oplus\mathbb C$，范数是两部分之和。
原 long Dirichlet 定理的代数和 Green 已明确在全部
$4\mathbb Z$ Fourier 空间成立；几何偶反射不是以下算子证明的
有限维或半谱限制。

当前 ac1 输入的真实解析宽取 $\sigma_0=1/16$。
帽侧保实际非mean物理曲率 $Z=(C_R-C_r)_\perp$，
$\|Z\|_{A^0_{\sigma_0}}\le z_a=3.3\cdot10^{-10}$。
[同 fixed-stop 完整源](R133-supplement-fixed-stop-D0-complete-sources-and-incoming.md)
(D.31a)--(D.31b) 已用无限物理 Fourier 包络和同一个
$C_R\to f_*$ 收缩证明这个输入域。其准确方程是
[长段曲率接口](R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md)
(M.17)；完整余项由 (M.10)--(M.13) 给出。
所有乘法、非mean投影和 holonomy 小根在整个 $4\mathbb Z$ 代数
有相同绝对界，所以该收缩在不加偶反射条件时仍成立：
$$
 f_*=\Phi_R(Z,f_B),\quad
 \|\Phi_R\|_{\dot A^2_{\sigma_0}}\le r_f=10^{-8},\quad
 \|D_{f_B}\Phi_R\|<2^{35},\quad
 \|D_Z\Phi_R:A^0_{\sigma_0}\to\dot A^2_{\sigma_0}\|<10 .
 \tag{N.6}
$$
最后一个门由 $9/(1-1/512)<10$；前一个由
$f_B$ 球半径 $r_B=2^{-60}$、输出 $r_f$ 的 Cauchy 半球给出。
所有实际 $f_B$ 严格在该半球内。准确有理的球像和收缩门
$9z_a+2^{-512}r_B+9\,2^{12}(r_f+r_B)^2<r_f$、
$36\,2^{12}(r_f+r_B)<1/512$ 已在原 (D.31b) 支付。

这里没有把旧共同偶反射的整帽图
$c_{\ne0}(1)\mapsto C_R$ 自动延拓为任意固定背景的全 Fourier 图。
本篇直接在完整代数中反演真实 $C_R$，保留实际 mean $B_R$、
mean $C_R$ 及非mean Robin 另一迹为输出；见第5节。
固定 $Z$ 的任意角扰动因此都是所证明域中的真实导数，
而所有帽内 head、高模和其它源仍通过独立 $Z$ 及这些输出联立。
## 2. 先在完整 Wiener 空间付真正导数

在 $f_*=0$，原16 lift和完整收缩给
$\|h(f,0)\|_{\mathcal Y_\sigma}<17\|f\|_{\dot A^2_\sigma}$。
原 long (D.27) 的两端非mean余项与 (D.8) 的 mean 小根合计给
$$
 \mathcal E(f):=\mathcal K_B(f,0)+\mathsf C_L f,\qquad
 \|\mathcal E(f)\|_{\dot A^1_\sigma\oplus\mathbb C}
 <2^{23}\|f\|_{\dot A^2_\sigma}^{\,2}.
 \tag{N.7}
$$
线性 mean 为零只是径向参考的准确一阶事实；
非线性 mean 已在 (N.7) 中付费。

在 $\|f\|\le F$ 周围取半径 $F$ 的真正复方向圆盘，所有输入仍满足
$2F<2^{-25}$。Cauchy 给
$$
 \|D\mathcal E(f)\|<
 2^{25}F .
 \tag{N.8}
$$
$F=0$ 时由二次零点直接给 $D\mathcal E(0)=0$，不使用零半径圆盘。

令
$\Delta\mathcal K_B(f,f_*)=\mathcal K_B(f,f_*)-\mathcal K_B(f,0)$。
[真实 nonlinear 屏蔽](R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md)
(S.15)--(S.19) 是在完整径向加权 module 中证明的，含 mean。
它给
$$
 \|\Delta\mathcal K_B(f,f_*)\|<25\epsilon\|f_*\|,\qquad
 \|D_{f_*}\mathcal K_B(f,f_*)\|<25\epsilon .
 \tag{N.9}
$$
第二式由同一个加权线性化 Green 和 $5/16$ 收缩率得到，
不是从无权导数猜径向屏蔽。

原 (S.28) 允许只针对 long 方程在 $f$ 周围取
$\delta_B=2^{-27}$ 的圆盘；不要求把帽图扩到这个大球。
故
$$
 \|D_f\Delta\mathcal K_B(f,f_*)\|
 \le25\epsilon r_f/\delta_B<2^6\epsilon .
 \tag{N.10}
$$
固定 $Z$，定义
$$
 \mathscr K_Z(f)=\mathcal K_B(f,\Phi_R(Z,f)).
$$
把 (N.6)、(N.8)--(N.10) 按准确 chain rule 相加，得到
$$
 T_Z:=D_f\mathscr K_Z(f)+\mathsf C_L,\qquad
 \boxed{\quad
 \|T_Z:\dot A^2_\sigma\to
               \dot A^1_\sigma\oplus\mathbb C\|
 <2^{25}F+2^{41}\epsilon .
 \quad}
 \tag{N.11}
$$
真实 $C_R$ 逆的所有高频反馈及 holonomy mean 都仍在
$D_{f_*}\mathcal K_B\,D_f\Phi_R$ 中；帽内未知 $Z$ 的响应仍是
独立端口，不能在这里删掉。若固定 $f_*$ 而不闭 $C_R$ 反馈，
(N.11) 的 $2^{41}$ 可改为 $2^6$；下文统一使用较宽前者。

## 3. 解析平移给全矩阵 Schur，不按有限窗口计数

以下给出本篇使用的完整算子引理。令 $T$ 的输入零 mean，输出允许
mean，并满足
$$
 \|T_z:\dot A^2_{\sigma_i}\to
             \dot A^1_{\sigma_i}\oplus\mathbb C\|\le B,\qquad
 T_z=C_zTC_{-z},\quad C_z=e^{z\partial_\theta}.
 \tag{N.12}
$$
在每个 $|\operatorname{Im}z_0|<1/256$ 周围允许再平移
$|\operatorname{Im}(z-z_0)|\le h=1/64$，
并取 $\sigma_i=1/256$。
这些数的总和小于 $1/16$。
因此对当前数据，(N.12) 来自原同宽完整全纯解和唯一性；
仅用有限 Fourier 多项式核平移身份，然后完成闭包。
不把一个在固定背景下的 Wiener 界直接当作 Sobolev 界。

写 $a_m=\max(1,|m|)$。对输入单模 $n\ne0$，
输出单模 $m\in4\mathbb Z$，在平移的两个边上择一得到
$$
 |(T_{z_0})_{mn}|
 \le B\,\frac{|n|^2}{a_m}\,
       e^{\sigma_i(|n|-|m|)}e^{-h|m-n|}
 \le B\,\frac{|n|^2}{a_m}e^{-|m-n|/128}.
 \tag{N.13}
$$
这里 $m=0$ 正是原输出 mean 行，未将它设零。
$T_{m0}=0$ 则是“输入为非mean高度”后的准确零延拓。

把 $H^{1/2}$ 输入及 $H^{-1/2}$ 输出的权写进矩阵，利用
$|n|\le a_m(1+|m-n|)$，每个元素不超过
$$
 2B(1+|m-n|)^{3/2}e^{-|m-n|/128}.
 \tag{N.14}
$$
完整 signed-lag 行和、列和同时有界。例如
$q=e^{-1/32}$、$1-q>1/64$ 给
$$
 \sum_{k\in4\mathbb Z}(1+|k|)^2e^{-|k|/128}
 \le1+50\sum_{\ell\ge1}\ell^2q^\ell
 <1+\frac{100}{(1-q)^3}<2^{25}.
$$
故 Schur 引理给安全全空间门
$$
 \boxed{\quad
 \|T:H^{1/2}_\perp\to H^{-1/2}\|<2^{28}B .
 \quad}
 \tag{N.15}
$$
不需要有限角窗数，不删 mean-to-high、high-to-mean 或相反频率锥。
(N.12) 对 $\Phi_R$ 使用的是其真实联合平移
$Z\mapsto C_zZ,\ f\mapsto C_zf$；没有把固定 $Z$ 的任意变化误作
角协变性。范数在该整个平移族内统一。

## 4. 真物理 DN：归一化、mean 和 $C_R$ 反馈同时还原

令 $g$ 为 $B$ 端真实 Jacobi 高度。固定度量参数、固定 $Z$ 时，
$$
 \delta f_B=\Pi_\perp g/(a_Bw_B),\qquad
 (\delta v)_t(B)=D_f\mathscr K_Z(f)\,\Pi_\perp g .
 \tag{N.16}
$$
第二式中 $a_Bw_B$ 准确抵消；$D_f\mathscr K_Z$ 的输出仍含
holonomy mean 斜率。整体常高度对应 $\delta f_B=0$，
另保 (N.4) 的一个平移。

使用实际 raw 系数
$\mu=\mu_0JD^{-3/2}$、
$d=E(V-P)/J$、$\mu_0=1/(4\omega)\in(1/6,1/4)$，
在 long 左端的 outward 通量为
$$
 \mathcal N_{B,Z}g
 =-\mu\{D_f\mathscr K_Z(f)\Pi_\perp g-d\,g_\theta\}.
 \tag{N.17}
$$
这是原物理 total 通量；齐次时没有 weak source 项。
径向参考
$\mathcal N_{B,0}=\mu_0\mathsf C_L$。
因此完整差准确分成
$$
 \mathcal N_{B,Z}-\mathcal N_{B,0}
 =(\mu-\mu_0)\mathsf C_L
   -\mu T_Z\Pi_\perp+\mu d\,\partial_\theta .
 \tag{N.18}
$$
若先删 $T_Z$ 的 mean 行，(N.17)--(N.18) 不再是正确公式。

在 $B$ 端，$P=f_\theta,U=f_{\theta\theta}$，
而 $K,V$ 用 $17F$ pure-incoming 解和 (N.9) 比较。
逐项有
$$
 N_B^{\rm coeff}:=\|P\|+\|U\|+\|K\|+\|V\|
 <2^8F+2^6\epsilon r_f .
 \tag{N.19}
$$
全部范数为原完整 $A^0_{\sigma_0}$。
代入 $J=1+K+EU$ 和
$D=1-w^2(2K+K^2+EP^2)$，
$E\le2,w<1$ 给
$$
 \|\mu/\mu_0-1\|_{A^0_{\sigma_0}}
       +\|d\|_{A^0_{\sigma_0}}
 <2^{16}(F+\epsilon r_f).
 \tag{N.20}
$$
剩余真实角宽使这些乘法在 $H^{\pm1/2}$ 的费用小于
$2^8$ 倍该 Wiener 上界；
可直接用 $(1+|k|)e^{-|k|/64}<2^8$ 的完整 Fourier 和证明。
$\mathsf C_L:H^{1/2}\to H^{-1/2}$ 的范数小于2。
(N.11)、(N.15)、(N.18) 最后给
$$
 \boxed{\quad
 \|\mathcal N_{B,Z}-\mathcal N_{B,0}:
                     H^{1/2}\to H^{-1/2}\|
 <2^{80}(F+\epsilon).
 \quad}
 \tag{N.21}
$$
该门在 $|\operatorname{Im}z|<1/256$ 的整个实际角平移族统一。

常数输入列准确为零。输出 mean 也为零，但证明方式是对完整
(N.17) 使用原 $M=1$ 的线性化：无源 mean 总通量恒为零。
等价地，先保 $D\mu(h)$，再取 (N.17) 的真实乘积 mean 才得零。
(N.21) 从未用“投掉输出 mean”获得。
独立有源 mean 荷不满足这个齐次零式，下一节保留。

## 5. 实际 $C_R$ 源列、全部曲率输出及 mean 高度的原单位

若帽侧实际 $Z$ 或其它独立源改变，精确写
$$
 \delta f_*=
 D_f\Phi_R\,\frac{\Pi_\perp g}{a_Bw_B}
 +D_Z\Phi_R\,\delta Z+f_*^{\,\rm src}.
 \tag{N.22}
$$
于是帽侧对 $B$ 的独立通量列是
$$
 -\mu a_Bw_B\,D_{f_*}\mathcal K_B
       (D_Z\Phi_R\,\delta Z+f_*^{\,\rm src}) .
 \tag{N.23}
$$
它保留全部 head、高模、mean 斜率和原物理 $a_Bw_B$。
由 (N.6)、(N.9)，其 $\delta Z$ 列在真实窄角域有
$A^0\to A^1\oplus\mathbb C$ 的费 $2^{10}a_Bw_B\epsilon$。
重复 (N.13)--(N.15)，这次矩阵权是
$\langle m\rangle^{1/2}\langle n\rangle^{1/2}/a_m
 \le2(1+|m-n|)^{1/2}$，故完整物理源列有
$$
 \|\mathcal B_Z:H^{-1/2}_\perp\to H^{1/2}\|
 <2^{48}a_Bw_B\epsilon .
 \tag{N.23a}
$$
所有 mean 输出仍先计入矩阵。其它 $f_*^{\,\rm src}$ 使用原实际
$\dot A^2_\sigma$ 范数，不从 (N.23a) 免费授予粗源相同单位。

另三条曲率输出保持原 (M.10)、(M.21) 的真实公式：
$$
 B_R=\chi_R\frac{V_R-P_R}{\sqrt{D_R}},\qquad
 C_R=-\chi_R\frac{J_R}{\sqrt{E_R}\sqrt{D_R}},\qquad
 d_m(R)=i\operatorname{sgn}(m)(B_R)_m+q_m(R)Z_m .
 \tag{N.23b}
$$
其中 $(B_R)_0$ 和 $(C_R)_0-C_r$ 均是独立实际输出。
共同偶反射基点的 $(B_R)_0=0$ 不可用于删掉任意非对称扰动的
$D(B_R)_0$。$q_m(R)$ 是原准确 regular 比值，有限长反射未改。
本篇没有解掉这些行与帽内图的联立，也不把 $Z$ 当已知零荷。

原 long 体源、两端 mean 总荷、weak 法向迹及未匹配 connector
仍按前篇 (P.27)--(P.32) 的完整式进入：
$$
 q_L=q_A-\int g_0,\qquad
 \pi_{\rm tmp}=r_\mu\pi_L+b_\mu H_\theta+\mu_Tb_\perp
                    +F_T^t-r_\mu F_L^t,
$$
$$
 \pi_T=P_\mu\pi_{\rm tmp}
             +\frac{\mu_T}{\langle\mu_T\rangle}q_T,\qquad
 c_B=\frac{q_T-\langle\pi_{\rm tmp}\rangle}
           {\langle\mu_T\rangle}.
 \tag{N.24}
$$
$c_B$ 是实际 mean 斜率输出，不能在两背景尚未匹配时置零。
把 (N.23) 加入该式是仿射源的有序代入，未改变原两 mean 条件。

平均高度跨度也不能因 (N.9) 的屏蔽而删除。准确式仍为
$$
 \delta[v_0(L)-v_0(0)]
       =\int_0^L aw\,D\mu_t(h)\,\delta h\,dt .
 \tag{N.25}
$$
原屏蔽定理 (S.21) 对远端变化给其真实
$aw(L)/165$ 费用；不是给它额外乘 $\epsilon$。
所有 $\Gamma^*$ 列和 $\nu$ 列必须微分 (N.16)、(N.22)--(N.25)
以及其度量系数，包含 $\delta(a_Bw_B)$、$\delta\mu_0$、
$\delta\mathsf C_L$ 和 $\Phi_R$ 的显式参数列。
(N.21) 是固定度量的未知高度列，不以它取代这些有源列。

## 6. 从完整 $B$ 差到新根返回的同空间小差

用前篇的新正区完整型，与新径向 connector 及
$\mathcal N_{B,0}$ 比较。因为
$\mathcal N_{B,0}\ge(1/6)|D_\theta|\Pi_\perp$，
而 (N.21) 的输入常数列、输出 mean 行均为零，
其 $B$ 边界型相对误差小于
$$
 2^{85}(F+\epsilon).
 \tag{N.26}
$$
这里非mean $H^{1/2}$ 与 $\dot H^{1/2}$ 的两侧转换已支付；
没有用未知 mean 高度的 trace 去控制这项。

原未匹配 $E_B$ 不能省略。真实
$\mathfrak r=\|K_{T,\perp}-K_{L,\perp}\|_{\dot A^1}$
满足
$$
 \mathfrak r<2^5(n_0+F)+25\epsilon r_f .
$$
前篇 (P.8) 的 $2^{48}\mathfrak r$ 相对费完整保留。
再加同一短 connector 的 $2^{60}n_0$ 混合坐标费，
整个固定边界型相对误差可取
$\delta_{\rm form}=2^{86}(n_0+F+\epsilon)$。

为明确消元不会再带长 $L$，令 $H_f^0$ 是 reference Poisson。
实际零边界修正满足
$$
 w_f=-(A_{00}^0+E_{00})^{-1}E H_f^0,\qquad
 \|w_f\|_{\mathfrak a_0}
 \le\frac{\delta_{\rm form}}{1-\delta_{\rm form}}
                      \|H_f^0\|_{\mathfrak a_0}.
$$
其完整 DN 差是该有界型的 Schur 补，故相对 $P_0$ 的费不超过
$\delta_{\rm form}/(1-\delta_{\rm form})$。
这也对非自伴的实际 $C_R$ 反馈成立；没有用其 unitarity 或正性。

根密度的真共轭和正 mean shear 仍按前篇 (P.17) 付
$2^{80}n_0$。因此相对于新径向完整 $R_0+A_0$，可取
$$
 \epsilon_R^{\rm sharp}
       =2^{96}(n_0+F+\epsilon)<1/64 .
 \tag{N.27}
$$
前篇 (P.19) 的准确有序 Cayley 式和其双向 resolvent 恒等式给
$$
 \|\mathcal R_{a,Z}(z)-\mathcal R_0\|_{L^2\to L^2}
 <2^{112}(n_0+F+\epsilon),
 \qquad |\operatorname{Im}z|<1/256 .
 \tag{N.28}
$$
两端完整 mean 阻抗是 $i/\pi$，已在同一个 Cayley 中；
$\mathcal R_0$ 是径向 Fourier 乘子，不改变这一 mean 块。

在真实角条带内取半径 $1/512$ 的 Cauchy 圆，至多四阶的费用
$q!512^q<2^{41}$。完整平移协变性把它准确识别为
$\operatorname{ad}_{D_\phi}^q$。
再付有限个整数 Sobolev 乘积、对偶和 $|s|\le2$ 的插值，
$2^{160}$ 有余量，得到 (N.1)。
$F\le n_0$ 给 (N.2) 的第一不等式。
由 $L>2^{24}$ 和 $\log2<7/8$，
$\epsilon=e^{-7L/4}<2^{-33554432}$；
于是第二不等式在全实际 $X$ 球统一成立，未把极小正数下溢为零。

## 7. 保留的量词

本篇证明了新根正区固定 $C_R$ 时的完整 $B$ 消元、真实
$C_R\to f_*$ 反馈及其到根的同空间小差，所有 $4\mathbb Z$
频率、两个 height/flux mean、实际未匹配界面及外侧独立源身份
同时保留。固定几何参数、固定实际 $Z$ 的全高低未知高度列已经付清。
帽侧曲率 mean $B_R$、mean $C_R$ 与非mean Robin 残差另按
(N.23b) 保持；它们不等于高度 DN 的齐次 mean 总通量条件。

几何参数的导数仍在各自已付复盘内取真正
$q!r_p^{-q}$；强标签只按原标签域消费。
实际帽内 $Z$ 响应和 (N.23b) 的全行仍须联立。
新外负分量尚须用其真实两根、strict 段及两个 $\Gamma$ 支集
建立相位/五盒条件，并与原内部开口网络联立。
正区同空间小差本身不替代该谱选择或全部原源的 strong-label 逆。
