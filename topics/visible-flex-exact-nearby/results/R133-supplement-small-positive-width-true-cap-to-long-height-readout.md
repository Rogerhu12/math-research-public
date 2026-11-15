# R133 续篇：小正角宽中的真实帽曲率到长段高度读出

2026-11-15，visible-exact / tail_connector。

**已证明并独立核对的实际局部结论。** 本文先在同一物理角中重新实例化完整
\(C_R\) 到 Dirichlet 数据的非线性逆，再将它接到新加权帽球。
它不把帽的曲率 norm 当作高度 norm，也不把小正角宽提高成标签宽。
公开43695160055/1已通过完整加权门；[实际帽存在性](R133-supplement-actual-all-mode-positive-cap-existence-at-repaired-M32-centre.md)
已把该门接到完整E定理，因此本文的帽解应用现已满足条件。
独立 \(C_R\) 逆是下面明确域上的解析定理。

原对象固定 \(\eta=\eta_0,\delta=0\)，帽内区间
\([9/10,25/8]\)，原 ac1 的连续修补定义为 440866a3…。
长段采用同一个真实 \(a_*,w_*,\omega,\mathcal L\)；
新 fixed-stop simple-root 修改在长段之外，
未改变这些参数。本文只用原真正的径向长段方程和曲率公式，
不消费另一个候选的非线性解。

## 1. 输入变量、真实角与三个独立均值

令 \(R=25/8\)，取
$$
 \sigma_0=\frac1{8192},\qquad
 r_Z=10^{-9},\qquad r_B=2^{-60},\qquad r_*=10^{-8}.
 \tag{H.1}
$$
物理 Fourier 频率为 \(m\in4\mathbb Z\)，归一圆周测度。定义
$$
 \|Z\|_{A^0_\sigma}=\sum_{m\ne0}e^{\sigma|m|}|Z_m|,
 \qquad
 \|f\|_{\dot A^2_\sigma}
       =\sum_{m\ne0}e^{\sigma|m|}|m|^2|f_m|.
 \tag{H.2}
$$
这里 \(\sigma\) 是角宽，不是导数阶。输入为
$$
 Z=P_{\perp,\theta}(C_R-C_{\rm ref}),\qquad
 \|Z\|_{A^0_{\sigma_0}}<r_Z,\qquad
 \|f_B\|_{\dot A^2_{\sigma_0}}<r_B .
 \tag{H.3}
$$
\(Z\) 与 \(f_B\) 都在原物理角 \(\theta\) 中。
\(f_B\) 是长段 \(t=0\) 端的归一化非mean高度；
它不是 moving 曲率、return-angle 标签或裸 flux。
长段 \(t=\mathcal L\) 对应物理 \(r=R\)，其另一 Dirichlet 数据记为
\(f_*\)，同样是非mean归一化高度。

三个均值始终分开：曲率的 \(B_0,C_0\)，Darboux 高度的
holonomy mean \(\kappa(t)\)，以及整体高度常数 \(\lambda\)。
(H.3) 未指定任意的 \(C_0\)，也未设置第二个 mean Dirichlet 条件。
先在共同反射类 \(f_B,Z\) 偶对称中证明，允许所有复偶四重 Fourier
系数；不能把复化误读为复共轭。随后同时平移整个数据与背景的轴，
得到相应轴的同一个结论。

## 2. 小正角宽中的完整长段 BVP

原[真实周期接合](R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md)
M.5--M.9 及[真实长段](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
给逐模 Dirichlet Green。对 \(M=|m|\ge4\)，两个准确 lift 是
$$
 A_M(t)=e^{-2t}\frac{\sinh(M(\mathcal L-t))}{\sinh(M\mathcal L)},\qquad
 B_M(t)=e^{2(\mathcal L-t)}
                    \frac{\sinh(Mt)}{\sinh(M\mathcal L)}.
 \tag{H.4}
$$
在原完整强 norm \(\mathcal Y_\sigma\) 中，每个 Fourier 系数先取
径向 supremum，再求带指数权的全和。原逐模常数给
$$
 \|h_D\|_{\mathcal Y_\sigma}
 \le5\|f_B\|_{\dot A^2_\sigma}+3\|f_*\|_{\dot A^2_\sigma}
 \le5F,\qquad
 F=\|f_B\|_{\dot A^2_\sigma}+\|f_*\|_{\dot A^2_\sigma}.
 \tag{H.5}
$$
零 Dirichlet Green 的完整 norm 小于32，非线性源满足
\(\|\mathcal Q(h)\|\le512\|h\|_{\mathcal Y_\sigma}^2\)。
holonomy mean由原准确小根求出，满足
\(|\kappa(t)|\le256\|h\|_{\mathcal Y_\sigma}^2\)；
它的全部反馈已经在这个非线性源中。

这些论证不使用 M.4 的特定端宽数值：Green 和 lift 逐频对角，
指数权满足 \(e^{\sigma|m+n|}\le e^{\sigma|m|}e^{\sigma|n|}\)，
primitive 保留同一个非mean除数及独立mean。
因此对每一个固定 \(\sigma\ge0\)，在同样的边界 norm 球中，
同一收缩证明给同一个完整周期解。特别可重新取
\(\sigma=\sigma_0\)，无需把任何未知函数作复角 pullback。

只要 \(2F<2^{-25}\)，原解在半径 \(2^{-20}\) 内，且
$$
 H:=\|h\|_{\mathcal Y_{\sigma_0}}
 \le5F+2^{14}H^2\le5F+H/64,
 \qquad H<6F .
 \tag{H.6}
$$
原 M.9 的真 \(R\) 端导数核亦逐模不变：
$$
 \|\partial_\theta(h-h_D)_t(\mathcal L)\|_{A^0_{\sigma_0}}
                 \le1024H^2,\qquad
 \|(h-h_D)_t(\mathcal L)\|_{A^0_{\sigma_0}}\le256H^2 .
 \tag{H.7}
$$
所有模、两端和真实 \(\mathrm dt\) 均保留；
没有借短 collar 或单向能量门代替这两个端口。

## 3. 精确非线性曲率式与完整 \(C_R\) 逆

在 \(R\) 端仍用 M.10 的同一真实公式：
$$
 P=(f_*)_\theta,\quad U=(f_*)_{\theta\theta},\quad
 K=\kappa(\mathcal L)+2f_*+h_t(\mathcal L),\quad V=K_\theta,
$$
$$
 D=1-w_R^2(2K+K^2+E_RP^2),\quad J=1+K+E_RU,
$$
$$
 B_R=\chi_R\frac{V-P}{\sqrt D},\qquad
 C_R=-\chi_R\frac{J}{\sqrt{E_R}\sqrt D},\qquad
 \chi_R=w_R/a_R .
 \tag{H.8}
$$
所以 \(C_{\rm ref}=-\chi_R/\sqrt{E_R}\)。
这里保留 \(\kappa(\mathcal L)\)，不能先令 \(K_0=0\)。
同一参数满足 \(w_R<1/800000\)、
\(\chi_R\sqrt{E_R}<1/5\)，原完整状态和 \(N<4H\)。
完整 Binomial 级数在 Banach 代数中给
$$
 \|JD^{-1/2}-1-E_R(K+U)\|\le8w_R^2N^2 .
 \tag{H.9}
$$
这支付所有 mean--nonmean 乘积。

令 \(c_M=M\coth(M\mathcal L)\)、
\(s_M=Me^{-2\mathcal L}\operatorname{csch}(M\mathcal L)\)。
(H.4)、(H.7)--(H.9) 给准确非mean行
$$
 Z=\mathcal L_C f_*+\chi_R\sqrt{E_R}\,\mathcal S f_B
                              +\mathcal R_C(f_B,f_*),
 \quad
 (\mathcal L_C)_m=\chi_R\sqrt{E_R}(M^2-c_M),\
 \mathcal S_m=s_M .
 \tag{H.10}
$$
原 M.13、M.16 的逐模/代数证明在当前 \(\sigma_0\) 给
$$
 \|\mathcal R_C\|_{A^0_{\sigma_0}}\le2^{12}F^2,\qquad
 \|\mathcal L_C^{-1}:A^0_{\sigma_0}\to\dot A^2_{\sigma_0}\|<9,
$$
$$
 \|\mathcal L_C^{-1}\chi_R\sqrt{E_R}\mathcal S\|
                                      <2e^{-6\mathcal L}.
 \tag{H.11}
$$
特别第二式控制全部 \(M\ge4\)；不是有限矩阵逆。

定义
$$
 f_*=\mathcal L_C^{-1}
 \{Z-\chi_R\sqrt{E_R}\mathcal S f_B-\mathcal R_C(f_B,f_*)\}.
 \tag{H.12}
$$
取 \(F_*=10^{-8}+2^{-60}\)。与原 M.17--M.19 相同的准确标量
预算是
$$
 2F_*<2^{-25},\quad 6F_*<2^{-20},
$$
$$
 9r_Z+2e^{-6\mathcal L}r_B+9\,2^{12}F_*^2
          <9.003686401\,10^{-9}<r_*,
 \qquad 36\,2^{12}F_*<.001474561 .
 \tag{H.13}
$$
这里复用的是不依赖角宽的原有理不等式；
不重新运行目标、旧 Fourier 数据或旧长段积分。
完整两变量 Cauchy 估计
\(\|D\mathcal R_C\|\le4\,2^{12}F_*\)
在原 \(2F_*\) 边界盘内成立，故 (H.12) 是严格压缩。

因此得到唯一的全模全纯 map
$$
 \mathcal H_\sigma:(Z,f_B)\longmapsto f_*,
 \qquad
 \|\mathcal H_{\sigma_0}(Z,f_B)\|_{\dot A^2_{\sigma_0}}<10^{-8},
 \qquad
 \|D_Z\mathcal H_{\sigma_0}\|<9.013290638 .
 \tag{H.14}
$$
本文的上标/下标 \(\mathcal H\) 仅表示这条真实高度读出，不表示
全尾 inverse。由于所有宽度的收缩都满足同一个原实圈方程，
两个可用宽度在公共域上的解由零宽唯一性相同；
没有为较小宽度改变几何或所解分支。

## 4. 全部曲率 mean、真实高度与轴

(H.8) 的完整输出满足原 M.14--M.15：
$$
 B_R=\mathcal T Z+\mathcal S_B f_B+\mathcal R_D,\quad
 \|\mathcal R_D\|_{A^0_{\sigma_0}}<2^{14}F_*^2,\qquad
 |(C_R)_0-C_{\rm ref}|<2^{11}F_*^2 .
 \tag{H.15}
$$
\(\mathcal T,\mathcal S_B\) 保留完整有限长反射和真实 regular 误差；
它们没有被设成径向无限长极限。共同反射给
\((B_R)_0=0\) 准确成立，而 \((C_R)_0\) 是 (H.8) 的真实输出。
本篇没有把 (H.12) 的独立输入扩大成任意指定的 \(C_0\)。

物理高度/径向迹仍按原 M.26--M.27：
$$
 v_\perp(R)=a_Rw_Rf_*,\qquad
 v_a(R)=w_R\{\kappa(\mathcal L)+2f_*+h_t(\mathcal L)\},
$$
$$
 v_0(\mathcal L)-v_0(0)
          =\int_0^{\mathcal L}a(t)w(t)\kappa(t)\,\mathrm dt .
 \tag{H.16}
$$
符号沿原几何 \(Z_{\rm height}=Z_{\rm ref}-v\)。
第二式不是无权的 \(f_*\) 端值；第一式中的 \(a_Rw_R\) 不取为1。
由 \(\int_0^{\mathcal L}aw\,\mathrm dt\le a_Rw_R/2\)，还可保留
$$
 |v_0(\mathcal L)-v_0(0)|
                  \le128a_Rw_R(6F_*)^2 .
 \tag{H.17}
$$
这个 mean高度跨度没有远端筛选因子。
整体 \(\lambda\) 依旧独立，不能分别在帽两端归零。
内端帽的 \(B(L_c),C_0(L_c)\)、mean高度与相位继续是其真实输出，
不是通过 (H.14) 新增的约束。

所有 (H.8)--(H.17) 在同一个物理 \(\theta\) 中解释。
若帽原来由 moving 多项式给出，必须先使用它已经证明的真实
\(\Theta_Q\) 生成物理 \(B,C\)；本文不再对未知 \(Z\) 或 \(f_*\)
施加一个未付的 moving/return pullback。
同时平移整个物理数据、背景和轴时，径向长段方程、mean小根与
(H.12) 唯一性给相同平移协变。只平移未知函数而固定非径向帽背景，
不是此协变的含义。

## 5. 接到新加权帽球的准确实际推论

使用[加权 Q 端点不变球](R133-supplement-weighted-Q-endpoint-invariance-and-small-analytic-cap-ball.md)
(E.1)--(E.23) 的同一数据、同一 \(\sigma_0\)、同一修补中心。
该篇原来唯一新的局部数值门是
$$
 q_w<10^{-5}.
 \tag{H.18}
$$
实际43695160055/1 child0/21门给 \(q_w<3.561348304031\,10^{-6}\)，
因此 (H.18) 已成立；完整证据见[实际加权报告](R133-supplement-actual-cached-weighted-cap-Q-and-endpoint-margins.md)。
[实际存在性 X.1--X.16](R133-supplement-actual-all-mode-positive-cap-existence-at-repaired-M32-centre.md)
已在相同反射复偶域登记该帽解。

取给定内端非mean曲率
\(\|\gamma\|_{A^0_{\sigma_0}}<10^{-9}\)，
以及 \(\|f_B\|_{\dot A^2_{\sigma_0}}<2^{-60}\)。
E 篇在同一完整复参数球中给唯一帽解
\(W(\gamma,f_B)\)，满足全部真实外曲率行。
它的右端
$$
 Z(\gamma,f_B)
       =P_{\perp,\theta}(C(R;\gamma,f_B)-C_{\rm ref})
$$
由其特殊端点保持式满足
\(\|Z\|_{A^0_{\sigma_0}}<3\,10^{-13}+9.9\,10^{-10}<r_Z\)；
不是从较大的主体半径 \(3\,10^{-6}\) 直接推出这个界。
由此定义实际复合
$$
 \Phi_\gamma(f_B)
       =\mathcal H_{\sigma_0}(Z(\gamma,f_B),f_B).
 \tag{H.19}
$$
它是同一个帽--long 接口的真实非mean归一高度，
有完整强值域
$$
 \|\Phi_\gamma(f_B)\|_{\dot A^2_{\sigma_0}}<10^{-8}<2^{-26}.
 \tag{H.20}
$$
真 \(C_0\) 和 \(B_0\) 分别按 E 的右端行与 (H.15) 一致。
由原完整物理 frame 唯一输运，可在 \(R\) 选择同一点/frame接合；
本文不因此宣称更内侧 body/waist 与这些输出已经接合。

E 的完整复球压缩与 (H.12) 的均匀压缩均全纯。
对固定允许的 \(\gamma\)，在
\(\|f_B\|_{\dot A^2_{\sigma_0}}\le2^{-61}\) 上作同一个 Banach
值域的 Cauchy 估计，得到
$$
 \|D_{f_B}\Phi_\gamma\|_{\dot A^2_{\sigma_0}\to\dot A^2_{\sigma_0}}
 \le 2^{61}\,10^{-8}<2^{35}.
 \tag{H.21}
$$
这已经包含 \(D Z(\gamma,f_B)\) 的完整帽反馈；不能再把其一列重复相加。
它不是由仅有 \(L^2\) 的 Jacobian 猜出的导数界。
对固定 \(f_B\)、\(\|\gamma\|\le(1/2)10^{-9}\)，同样得到
\(\|D_\gamma\Phi\|<20\)，单位仍是实际内端物理曲率。
任何独立 mean、内端相位或物理高度输入没有因这个值域估计被删除。

## 6. 与新尾标签和有限预处理链的边界

新固定stop对象保持同一 \(R,a_*,w_*,\omega,\mathcal L\)，其真 finite
尾迹 \(f_B(a),k_B(a)\) 必须先在相同物理角和归一单位中输出，
才能将 \(f_B(a)\) 代入 (H.19)。
实际需要解的另一端方程仍完整为
$$
 k_B(a)+C_L f_B(a)-S_L\Phi_\gamma(f_B(a))
       -E_D(f_B(a),\Phi_\gamma(f_B(a)))=0 .
 \tag{H.22}
$$
这是原最终端口证书 F.21 / 原周期接合 M.29 的准确同类行，
不是帽存在性的推论。真实两侧 holonomy mean须以同一个
非mean Cauchy 数据重建；未满足 (H.22) 时不把两个 mean差设为0。
mean高度则继续用 (H.16)，每条链只保一个整体高度规范。

(H.20) 只在小宽 \(\sigma_0\) 给值；它不授
\(\dot A^1_{s_\beta}\)、\(\mathcal X_{224}\) 或任何任意大的输出角宽。
若后续使用
\(g_*(f_*)=K_{B,\perp}(0,f_*)\)
在 \(S=\sigma_0+7\mathcal L/16\) 的筛选，须另消费完整长段 Green
及有序两端 Dirichlet 构造；
对于非zero \(f_B\) 的 mixed项，还须单独支付该实际 \(f_B\) 的宽度。
本文不将这些待消费的门藏入 \(\Phi\)。

因此此处新闭合的是：同一物理角、全部Fourier模与mean保持的小正角
\(C_R\) 逆，以及由已成 (H.18) 得到的实际帽到 \(f_*\) 强值域和
完整 Cauchy 导数。旧94步输出不能据此改名为新对象；
在新对象上重新作有限链、界面 lifting、普通三径源单位、
全部 height/flux 与 \(\nu\) 联立，仍按各自准确合同继续。
