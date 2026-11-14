# R119 续篇：新外五盒的完整 generator、全频公共点与原层权

2026-11-14，visible-exact / tail_connector。

**状态：解析证明。** 本篇把新完整负分量
$o=(129,2)$ 的五个实际 compact 坐标接到其真正两根端口，
重新支付中心状态到端口的费用，并在同一个参数点选择全部非零
四重 Fourier 网络。新增有限外行的高截止按其实际强余项扩大，并在浅前缀取同一固定
平台，保持后续 Poisson 频率权的真实相邻比；无限深低尾仍是真实
允许线，不作有限截断。

下述公共点与 inverse 是径向的、使用真实径向外允许线的完整网络。
实际非径向余项、完整帽返回与原 source-to-label 两向识别仍需在
同一个表示中接合。本篇不把开放内部压缩认作已经闭合的全 PDE。

## 1. 同一个新对象和实际有限参数

使用已重建的新 fixed-stop 对象、完整简单根 A 篇、正型 DN P 篇、
完整外 principal O 篇，以及
[新外完整强散射和首相位](R119-supplement-new-outer-two-root-strong-scattering-and-complete-first-phase.md)
F 和
[新外联合两相位及高反馈](R119-supplement-new-outer-joint-two-phase-scalar-normal-form-and-high-feedback.md)
J。层量保持
$$
 \delta_j=(2/25)2^{-j},\qquad
 \eta_j=\delta_j^{3/2}/(4\sqrt2),\qquad J_j=j+5,
 \qquad \mathcal I_+=\{(j,k):j\ge129,\ k=1,2\}.
 \tag{C.1}
$$
新根、平台及长段只改变已明确的外部分量；原全部内层和两接缝
没有重编号。真实有限受影响集合是
$\mathcal J_o=\{(129,1),(129,2)\}$，不是由 cut128 的名字猜测。

每个窗仍使用
[浅前缀五盒](R119-supplement-shallow-five-cube-family-and-all-frequency-radial-selection.md)
(P.14) 的同一个低一维、紧三维、高一维盒：
$$
 \rho_\ell=2^{-1024}J^{-8},\quad
 r_\ell=2^{-1000}\Delta^2\rho_\ell^9,\qquad
 \rho_h=2^{-40}J^{-2},\quad r_h=2^{-1000}\rho_h^{13},
$$
$$
 K_*=2^{4000}J^{40},\quad L_*=1+K_*,\quad
 \rho_c=2^{-2240}J^{-2}\Delta^{-11}L_*^{-10},\quad
 R_c=2^{-2300}\Delta^{-5}L_*^{-5}\rho_c^{10}.
 \tag{C.2}
$$
坐标为 $\alpha_\ell=r_\ell\vartheta_\ell$、
$q_c=(R_c/3)\vartheta_c$、$\alpha_h=r_h\vartheta_h$，
$\vartheta_i\in[-1,1]^5$；复域为 $\|\vartheta_i\|_\infty<2$。
三组支集及各自的两个局部补偿不交，均在原
$J_x=(7/16,15/32)$，总 $C^4$ 小于 $2^{-79}$。
新外行使用原第129胞第二下降坡内的同一支集。

对外行仍有 $80<\Delta_o<3J_o$、
$\mathcal B_o=8\sqrt6\Delta_o\delta_{129}^{-3/2}>2^{190}$。
原 finite-$e$ 五函数逆、双真 null 除法和高区振荡核所需的
$0<e=\mathcal B_o^{-1}<2^{-190}$、$1/\Delta_o<1/80$
已经满足；从未要求 $e\ll\rho_c$。
上述三个局部曲线分别准确保持局部主光学长度和完整 strict
首积分。因此 J.6--J.9 说明它们保持新整段的
$(\omega_o,\beta_o^0)$，两根和所有原端 jets 不变。

这是一个真实 profile 子族。原非径向 $\Gamma^*$ 仍按 J.13
联合重解；$D_\vartheta\bar\Gamma=0$ 不表示
$D_\vartheta\Gamma^*(a,\vartheta)=0$。fixed stop 的
$\ell^0,\rho$ 固定，$D\ell^0=0$，不引入随参数重停的外线。

## 2. 从真正中心态到新两根端口的明确费用

先固定一个非零 $M=4|n|\ge4$。局部低、紧、高正型均以同一中心态
$$
 Z=\binom{\sqrt{k_M}\,u}{u_t/\sqrt{k_M}},\qquad
 u=\sqrt\mu\,h,\quad k_M=\sqrt{7M^2-16},\quad 2M<k_M<3M
 \tag{C.3}
$$
表示。它没有要求控制支集上的 $Q$ 等于7。

F.3--F.5 在新完整 strict 片及全部允许形状上给
$$
 2^{-7}<Q<2^{220},\qquad |Q_t|<2^{425},\qquad
 q=\sqrt Q>2^{-4}.
 \tag{C.4}
$$
取真实光学坐标 $dr=q\,dt$、$w=\sqrt q\,u$，
以及平衡光学态
$Z_{\rm opt}=(\sqrt M\,w,w_r/\sqrt M)$。准确有
$$
 Z_{\rm opt}=
 \begin{pmatrix}
  a&0\\ d&a^{-1}
 \end{pmatrix}Z,\qquad
 a=\sqrt{Mq/k_M},\qquad
 d={q_t\over2\sqrt{Mk_M}\,q^{3/2}}
   ={Q_t\over4\sqrt{Mk_M}\,q^{5/2}} .
 \tag{C.5}
$$
这是真 determinant-one 矩阵。由 (C.4) 和 $M\ge4$，
$a<2^{55}$、$a^{-1}<2^3$、$|d|<2^{433}$，
所以矩阵及逆的 Euclidean norm 均小于 $2^{440}<2^{512}$。
光学实两行与完整复 wave 的固定转换只再付2。
$\mu$ 已在 $u=\sqrt\mu h$ 中准确配对消去，不对裸物理高度
使用这个 norm1 断言。

F.8--F.25 的完整有序账给任意相应 root-to-strict 子段及逆
小于 $2^{32768}$；其 strict 能量证明本来覆盖每个闭子区间，
所以在三个控制中心切开该片不增加全区 Gronwall 次数。
这包括两端 root、真实 graph、normal shear、自由两行 frame
以及其正确低非mean费用。结合 (C.5)，可共同取
$$
                         K_o=2^{33792}
 \tag{C.6}
$$
作为任一控制中心 $Z$ 到两个实际端 wave 的正反向界。
同一门也覆盖原两个 $Q=7$ 固定截面：它们只是该真实片中的
内部截面。没有把旧的 $b^{1/2}$ free-frame 断言用于低非mean。

为说明完整 incoming 比较，把两端实际 wave 分量并列。
每端的 Cauchy norm 至多 $K_o|Z|$；总 incoming 的两个分量
是这四个真分量的坐标投影。于是
$|a_{\rm in}|^2\le8K_o^2|Z|^2$。
Green 参数恒等式将局部 crossing 精确送到
$-iS_M^*D S_M$，所以
$$
 \mathfrak L\ge d_{\rm loc}|Z|^2
 \quad\Longrightarrow\quad
 -iS_M^*DS_M\ge{d_{\rm loc}\over8K_o^2}I_2 .
 \tag{C.7}
$$
这个比较同时保两端，不假设任何一端的高度或单侧 incoming
有质量下界。源的仿射项在后面的完整 source 合同保留；
(C.7) 本身是齐次参数型。

## 3. 新外整个五盒中的三段 generator

对固定 $M$ 令 $\kappa=M^2/\mathcal B$。低、紧、高所取方向
$v_{i,M}$ 与原五盒 (Q.7) 完全相同，
$\|v_{i,M}\|_1\le1$，沿整条 cube 弦固定。
尤其紧三维方向只依赖 $\kappa$，不随当前核向量或盒点更新。

为避免把旧外行尚不存在时的结论直接转授，先列实际局部量。
低组的完整原单位型是
$$
 d_{\rm loc,\ell}
 =r_\ell\,2^{-780}\rho_\ell^8\Delta^3M^5\mathcal B^{-3}.
 \tag{C.8}
$$
紧组自然态恢复及半径给
$$
 d_{\rm loc,c}
 >{\Delta R_c\sigma_c\over48L_*\sqrt{\mathcal B}},
 \qquad
 \sigma_c=2^{-2110}\Delta^{-5}L_*^{-4}\rho_c^9 .
 \tag{C.9}
$$
高组的真实光学两态比较连同局部 Cauchy 后给
$2^{-1800}\rho_h^{20}\mathcal B K^{-2}M^{-3}$；
这里的 $K$ 必须取正在使用的完整端口常数。
(C.8)--(C.9) 分别是原低篇 L.21、紧篇 N.31--N.34；
高式是原振荡篇 O.38--O.40。
它们包括真实 $dt=(\Delta/\mathcal B)\,dx$、
两态条件数和所有局部补偿，不只是一条标量相位导数。

令 $D_{j,M}$ 为原明确的三段数值函数
$$
 D_{j,M}=
 \begin{cases}
 2^{-31400}J^{-160}\delta^{73/2}M^5,&\kappa\le1/4,\\
 2^{-861000}J^{-8300}\delta^{131/4},&1/4<\kappa<K_*,\\
 2^{-14800}J^{-64}\delta^{61/2}M^{-3},&\kappa\ge K_* .
 \end{cases}
 \tag{C.10}
$$
原推导把上述局部表达式除以
$K_{\rm alg}^2$，其中
$K_{\rm alg}=2^{6000}J^8\delta^{-16}$，得到严格大于
(C.10) 的数值。这里可以直接重做同一代入：
$$
 {K_o^2\over K_{\rm alg}^2}\le2^{55584}<2^{65536}.
 \tag{C.11}
$$
所以新的完整外行在整个同一五盒上准确满足
$$
 -iS_{o,M}^*D_{v_{o,M}}S_{o,M}>D^+_{o,M}I_2,\qquad
 D^+_{o,M}=2^{-65536}D_{129,M}.
 \tag{C.12}
$$
(C.11) 比较的是已列局部积分的代数乘数，不是假定旧外行
已经拥有一个完整 BVP。其余负窗本身未改变，取
$D^+_{i,M}=D_{j(i),M}$。
相邻 $(129,1)$ 的 positive cross 虽已在 J 中重付，
它的局部 negative 参数型仍来自其原同一个完整负窗。

(C.12) 对全部 $M\ge4$ 成立，不受所谓低 incoming 包限制。
低组的 flux mean 型和物理常高度 null 仍按原 L.22 保留，
但不把它们硬塞进非零模的严格 $2\times2$ 下界。

## 4. 真正 retained 集、固定接线与无限低尾

记原阈值与新的固定浅平台
$$
 A_j=2^{-40}\delta_j^{-1/8},\qquad
 T_j=2^{65664}J^2\delta_j^{-9},\qquad
 T_\bullet=2^{131072},\qquad T_j^+=\max(T_j,T_\bullet).
$$
令 $\mathcal I_M^{\rm old}$ 为浅前缀 P.16 的真实集合。
现在取准确并集
$$
 \mathcal I_M^+=\mathcal I_M^{\rm old}\ \cup\
       \{i\in\mathcal I_+:129\le j(i)\le8192,\ M\le T_\bullet\}.
 \tag{C.13}
$$
集合不重复计数。由于
$\log_2\delta_{129}^{-1}<133$、$\log_2(134)<8$，
原 $T_{129}<2^{67000}<T_\bullet$；而
$T_{8193}>2^{65664+9\cdot8193}>T_\bullet$，
故只改变有限浅前缀的辅助频率分割，所有深阈值不变。
每个未 retained 的有限前片仍使用完整真传递；
对 $\mathcal J_o$，删除时确实已处在 J.26 的强高范围。

这个平台不是额外物理参数。它避免只在两个外行骤增 cutoff
后，无依据地转授原高 Poisson 的频率权。
准确有 $1\le T_j^+/T_j<2^{65536}$，且
$1\le T_{j+1}^+/T_j^+<2^{10}$。
所以距离至多2的真实相邻块仍有
$\Omega_i/\Omega_k<2^{20}$，
$\Omega_i(m)=\max(1,\langle m\rangle/(1+T_i^+))$。
该门只用于径向右 Poisson 的内部低输入，
未覆盖外端口仍没有 $|m|<T_i^+$ 的权限。

当新两行和原 retained 链之间有有限个高窗时，准确串联消去
它们即可。每个真实 negative transmission 非零；实 positive
两端 DN cross 是非零 Wronskian 除以真实 Dirichlet 基解端值，
也非零。因此完整 lossless 两端口的各 reflection 满足
$|r|<1$，串联分母 $1-r_1r_2$ 从不为零。
接模长1的真实外允许线也合法。
这里不要求被消去的有限段先有一个给定边界的 inverse；
只用它的实际双端 transfer/scattering。

深于 retained 集的无限 low 尾仍由原强 Green 给非零实允许列
及完整 affine 位移。它只作为一个真实外 reflection 进入，
不再逐个计数无穷 low 窗。
根端或 $Q=7$ 单位均由各自完整 wave 转换定义，不混用它们的源。

这里把外侧那条固定线准确指定为**固定独立物理 $C_R$ 时的径向
未知高度列**，以便后继与 N 篇使用同一个问题。径向基点
$h=f_B=f_*=Z=0$，真实 (M.10)--(M.12) 给
$$
 (\delta C_R)_m=-\chi_R\sqrt{E_R}
       \bigl[(2h+h_t)_m-M^2h_m\bigr].
$$
令 $v=awh$，且长段 $(aw)_t=2aw$，则其齐次外线准确为
$$
 v_{m,t}(L)=M^2v_m(L)\quad(m\ne0),\qquad
 v_{0,t}(L)=0 .
 \tag{C.13a}
$$
mean 式来自真实 holonomy 小根在径向原点的一阶导数为零。
(C.13a) 是固定实 Robin 线；其全非mean反射正是
$\Phi_R$ 在原点对 $f_B$ 的完整导数，有限长反射没有删去。
这里不把 $q_m(R)$ 的帽内 regular 图替代 (C.13a)，也没有
把独立 $Z$ 及两条曲率 mean 方程宣告已解。

N 篇的简化径向参考是
$\mathcal N_{B,0}=\mu_0|D|\coth(L|D|)\Pi_\perp$。
把 N.1 取在 $a=0,Z=0,F=0$，准确得到 (C.13a) 的根返回
$\mathcal R_\circ$ 与该参考 $\mathcal R_0$ 的全部四阶角交换子
及 $|s|\le2$ 同空间差均小于 $2^{160}\epsilon$，
$\epsilon=e^{-7L/4}$。因此二者没有被默认为相同；
本篇的固定接线使用真实 $\mathcal R_\circ$。后继实际比较对
N 的两条差用三角不等式即可保留这个非零指数费用。
径向实线给 $\mathcal R_\circ$ 酉，但一般非径向固定 $Z$
返回仍只使用 P/N 已付的有界性。

固定 $M$ 后遂有真正有限的 radial unitary 网络
$$
 U_M^+=P_M^+\bigoplus_{i\in\mathcal I_M^+}S_{i,M},\qquad
                  (I-U_M^+)x_M=g_M .
 \tag{C.14}
$$
沿 $v_M=\bigoplus v_{i,M}$ 的整条弦，只有 retained 控制片改变。
端 jets、两 phase、固定 stop 与其余 profile 坐标均固定，
所以 $D_{v_M}P_M^+=0$。
$P_M^+$ 包含实际径向外允许线、正片、全部有限空隙及无限低尾。
它不是任意固定非径向背景下未经证明的完整 cap 图。

每个所选短控制片的相对传递仍满足原五盒 Q.10--Q.13 的
同一个无极点 local Cayley 图：低/紧片用自然态短区间，
高片用准确共同光学长度和完整振荡两行。
(C.5)--(C.6) 只改变原输入单位的定量下界，不改变这个局部图。

## 5. 同一个 cube 的谱流，不增加模式参数

写 $x=\log_2M\ge2$、
$n_M=|\mathcal I_M^+|$、$d_M=2n_M$。
浅层从头按最多16128个真实负窗计数，深层仍至多
$2(8x+321)$ 个；不是只给旧 retained 集加两个而漏掉平台中的窗。故
$$
 n_M<16772+16x,\qquad
 J_i<2^{14}(1+x),\qquad
 \delta_i^{-1}<2^{8196}M^8 .
 \tag{C.15}
$$
这些是不依赖任何有限截尾的真实计数；没有使用 $d_M<M$。

固定其余坐标及外参数 $t$。对任意目标圆点 $z$，把所有固定
两端口准确消去后，原 eigenvalue 方程化为局部 Cayley 图与
固定自伴 relation 的交。该 relation 允许有多值部分；
压到其真正 domain 后，导数由 (C.12) 严格正定。
原 Q.14--Q.18 的 min--max 证明逐字给整条弦的总交点重数
不超过 $d_M$。没有因新外线可竖直而除以其高度。

令
$$
 a_M=\min_{i\in\mathcal I_M^+}D^+_{i,M},\quad
 \varepsilon_M=(2^{16}n_Md_MM^{17/16})^{-1},\quad
 \xi_M=a_M\varepsilon_M,
$$
$$
 L_M=1+\log(8/\xi_M),\qquad
 \mathcal T_M=2^{16}n_Md_MM^{17/16}L_M .
 \tag{C.16}
$$
真实 eigenphase 速度满足
$\phi_k'\ge\langle w_k,D_M^+w_k\rangle\ge a_M$。
同一个谱变量换元、总交点重数和 cube 入流面因子
$\|v_M\|_1/2\le n_M/2$，准确给
$$
 \mathbb P\!\left\{
 \operatorname{dist}(1,\sigma U_M^+)<\xi_M\
 \text{或}\
 \|(D_M^+)^{1/2}(I-U_M^+)^{-1}(D_M^+)^{1/2}\|
                                  >\mathcal T_M
 \right\}<2^{-14}M^{-17/16}.
 \tag{C.17}
$$
这一概率估计没有 $K_o$ 在 logarithm 之外的损失；
其真实影响已经完整进入 $D^+_{o,M}$ 与 $a_M$。
也没有把各模式的不同固定方向相加成一个不存在的全频方向。

对 root-wave 网络和原 $Q=7$ 网络各取此事件，
再加同一个新 fixed-stop 对每个 profile 给出的外好参数
坏测度 $83/16384$。
由 $\sum_{M\in4\mathbb N}M^{-17/16}<5$，公共好集测度仍严格大于
$$
                         1-93/16384>0 .
 \tag{C.18}
$$
角目标和两个 radial phase 从头固定；
这个选择不会按非径向标签重新选择 phase 目标。
参数盒的产品连续性来自已重建完整尾图，新增外五坐标只有有限个。
闭间隙和闭 inverse 条件的可数交集给同一个非空紧好集。
因此可以一次指定一个真实公共 profile 与外参数，
而非声称枚举了无限数组的数值通过门。

## 6. 把新有限费用支付成每个窗口自己的权

先对 (C.10)--(C.13) 核一个统一下界。
原 retained 行仍有旧
$D_{i,M}>2^{-862000}J^{-8300}\delta^{115/2}$。
新外低、紧两段乘 $2^{-65536}$ 后更强于
$2^{-927536}J^{-8300}\delta^{115/2}$。
所有因固定平台新增的高段只需 $M\le2^{131072}$；
下面统一按外行最坏的 $2^{-65536}$ 费用宽放：
$$
 2^{-14800-65536}J^{-64}\delta^{61/2}M^{-3}
 \ge2^{-473552}J^{-64}\delta^{61/2}
 >2^{-927536}J^{-8300}\delta^{115/2}.
$$
除 $o$ 外的全部浅层并没有 $2^{-65536}$ 损失，更满足该门。故
$$
 D^+_{i,M}>2^{-927536}J_i^{-8300}\delta_i^{115/2},\qquad
 a_M^{-1}<2^{1565536}(1+x)^{8300}M^{460}.
 \tag{C.19}
$$
第二式的实际 bits 为
$927536+8196(115/2)+14(8300)=1515006<1565536$；
没有把新增的 $M$ 范围代入旧 $M\le T_{129}$。

对每个当前 retained 窗，仍满足原 $M\le T_j$ 的行有 $x<512J$；
其余新增平台行有 $x\le131072<1024(134)\le1024J$。
统一得
$$
 x<1024J,\qquad n_M<2^{15}J,\qquad d_M<2^{16}J .
$$
$\log(1+1024J)<J/8$ 在 $J\ge134$ 上成立。
将 (C.19) 代入 (C.16)，常数项至多 $8179J$，
$8300\log(1+x)<1038J$，
$(460+17/16)x\log2<330490J$；
其余 $\log(2^{19}n_Md_M)+1$ 在上述计数下小于 $2J$。
所以
$$
 L_M<2^{19}J,\qquad
 \mathcal T_M<2^{66}J^3M^{17/16}<2^{96}J^3M^{17/16}.
 \tag{C.20}
$$

定义新的实际逐窗权
$$
 (\mathcal W_M^+)_{i}^{\,2}
      =2^{-96}J_i^{-3}M^{-17/16}D^+_{i,M}.
 \tag{C.21}
$$
公共点上 (C.17)、(C.20) 逐对角消费，给全部 $M\ge4$ 的
$$
 \boxed{\quad
 \|\mathcal W_M^+(I-U_M^+)^{-1}\mathcal W_M^+\|\le1 .
 \quad}
 \tag{C.22}
$$
真正不同窗的 $D^+_{i,M}$ 仍保留，未先全换成最小值。

为后续实际差比较给一个统一较小包络：
$$
 \boxed{\quad
 (\mathcal W_M^+)_{i}^{-2}
       <2^{929600}J_i^{8330}\delta_i^{-1073/16},
 \qquad
 v_j^+=2^{-464800}J^{-4165}\delta_j^{1073/32}
                                      <(\mathcal W_M^+)_{i}.
 \quad}
 \tag{C.23}
$$
其原 $\delta$ 幂没有改变。
对仍满足 $M\le T_j$ 的旧行，这是原浅 P.24 增加16 bits。
对新外低行，inverse 的 bits 为 $97032$，$M^{-63/16}$ 只改善。
对紧行，使用准确 $\kappa<K_*$，
$M<2^{2004}J^{41/2}\delta^{-3/4}$，
得 bits 小于 $928762$、$J$ 幂小于8325、
$\delta$ 指数 $2147/64<1073/16$。
所有新增平台高行直接用 $M\le2^{131072}$，统一按最坏外行得
$$
 (\mathcal W_M^+)_{i}^{-2}
 \le2^{612912}J_i^{67}\delta_i^{-61/2},
$$
也严格落入 (C.23)。
这逐项支付了新外高截止，未将原 $T_j$ 错用于它。

与旧统一包络 $\underline v$ 的准确关系是
$v^+=2^{-32784}\underline v$。
因此只在**同一个已经证明的算子 block** 上重权，
双侧 inverse-weight norm 会增加 $2^{65568}$。
原层间相邻比不变。
这条换权恒等式不自动证明新外 Schur 与原开放 remainder 相同。

## 7. 原角宽与全频粗逆仍可保留

(C.19)--(C.20) 及
$(1+x)^{8300}\le8300!e^{1+x}<2^{116202}M^2$、
$J^3<2^{47}M^2$ 给
$$
                  \|(I-U_M^+)^{-1}\|<2^{1800000}M^{466}.
 \tag{C.24}
$$
这里仍没有用窗口数小于 $M$。
实际总 bits 小于
$1565536+116202+66+47=1681851<1800000$，
频率次方小于 $466$。

原 $h_j=8\delta_j^{1/256}$ 和角权
$W_{i,M}=\exp(2^{-800}Mh_i)$ 完全不变。
在 $M\ge M_*=A_{8193}>2^{984}$，
深层的原指数余量已大于 $2^{25}J$；
(C.19)--(C.23) 新 logarithm 只增加固定有限费用。
所有浅层包括新外行有 $h_j\ge h_{8192}$，
故 $2^{-800}Mh_j>2^{154}$，
直接超过该有限前缀的全部新 logarithm 费用。
因此高于 $M_*$ 仍有原角权界1。

若 $4\le M<M_*<2^{985}$，只有有限浅层。
(C.24) 给同一个安全常数 $2^{2400000}$。于是
$$
       \|W_M^{-1}(I-U_M^+)^{-1}W_M^{-1}\|
                                      <2^{2400000}
              \qquad(M\in4\mathbb N).
 \tag{C.25}
$$
这支付了新有限段的角费用，没有放宽原标签角宽。

## 8. 全部源、两个 mean 和真正剩下的联立

(C.22) 的精确 source 合同是
$$
 \|\mathcal W_M^+x_M\|
                 \le\|(\mathcal W_M^+)^{-1}g_M\|.
 \tag{C.26}
$$
这里 $g_M$ 包含全部负窗的两态 ordinary/weak particular、
正区完整 total-DN cross 与 affine 列、有限消去片的真实源、
实际径向外允许线的源和真正无限低尾的 affine 位移。
新外端按 F.38--F.39、新正型 P.27--P.32 和长段 N 的有序映射进入。
不能把任意 raw RHS 直接指定为一个免费 incoming 向量。

原材料坐标的两态源仍为
$$
 \binom{-\nu_m r^4F^t/(\sqrt{12}\mu_jp_*)}
       {r^4(g-imF^\theta+M^2F^t)/(12\mu_j)} ,
 \tag{C.27}
$$
ordinary 第二行仍是 $\mu_jp_*^2e/(12r^{10})$。
各局部自然态或光学态使用其完整真实矩阵作用这两个分量，
不把第一 weak 行删去，也不索取 $F^t_t$。
回到 bare flux 仍另保原 $F^t$ 的端荷；
径向原子使用 BV 解及单侧迹。

$M=0$ 没有被 (C.17) 的谱计数处理。
它保留唯一整体物理高度常数和完整通量积分，
$\pi_0' =g_0$；
非径向平均高度仍准确满足
$\partial_t\langle h\rangle
=\langle dh_\theta+\mu^{-1}\pi-\mu^{-1}F^t\rangle$。
新正 Robin 的 coercive mean 与物理常高度 null 也没有相互替代。
两 $\Gamma^*$、$\nu$、形状和外变量的材料导数全部进入同一源映射；
J.16 的 control derivative 包含真实径向 inverse 的显式参数导数。

本篇取得的是新对象上同一个五盒公共点、真实径向全部非零模
有限 retained inverse、正确无限低尾和原层权/角宽。
接下来的最小门是：在这些同一权与端口中比较完整实际剩余系统，
把新有限两行及其高反馈接入，并把独立 $C_R$ 与完整帽返回、
两个 mean 和原强标签域一起闭合。
谱流的 unitary 固定接线仅在这里已证明的径向问题使用；
它不单独授予任意固定非径向背景的全帽图。
