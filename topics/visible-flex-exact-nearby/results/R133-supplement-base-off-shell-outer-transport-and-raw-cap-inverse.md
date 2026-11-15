# R133：基点非解外残差的完整运输项与 raw 帽逆

2026-11-15，visible-exact-astra-0df9。

**已证明的补充接口。** 原 S、O、T、X、Q 的帽逆使用固定物理角
中的 nonlinear regular residual 的导数。若改用随帽背景改变的
pulled 非mean输出，必须补其真实 residual transport。
本篇在同一个已知实族 $Q_\delta$、同一个已知 long 高度背景处付清
该项：相对于原完整基点 lift，新增反馈小于 $1/16$。
原主体及外行的 $3/8$ 加该项仍小于 $7/16$。
新的 raw 基逆在原 $-3/2\le s\le8212$ 窗口继续有完整源增益
$2^{4194304}$。

本篇不回写旧 $\mathcal G_\delta^{\rm true}$ 已经包含此项；
新逆明确记为 $\mathcal G_{\delta,\mathrm{raw}}$。
没有重算旧 target、long 解、帽核、有限矩阵或 Actions 数值。
它也不从这一局部帽逆推出原内体、未知 high 返回或非线性全局存在。

## 1. 两个确实不同的边界微分

对象固定为原连续中心定义
$440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47$，
完整方向定义
$6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04$，
物理 $\eta_0$ 与实 $|\delta|\le10^{-8}$。
同一已知 long 高度背景为
[T](R133-supplement-full-delta-fixed-angle-regular-graph-analytic-translation.md)
所构造的 $y_{B,\delta}$，不能在本篇换成任意未知高度，也不擅自置零。

令 $\varphi$ 为原 moving 角，$\theta=\Theta_\delta(\varphi)$ 为
$Q_\delta$ 的物理角，$x=\theta_0$ 为固定基点物理角。
在真实外端 $R=25/8$，
$$
 \tau_\delta=\Theta_\delta\circ\Phi_0,\qquad
 j_\delta=(\tau_\delta)_x,\qquad
 m_\delta=\langle v_\delta\rangle_\varphi<0 .
 \tag{R.1}
$$
$\Gamma_\delta$ 表示原完整 nonlinear long graph：输入真实
nonmean $C_\delta(R)$ 和同一个 $f_{B,\delta}$，先求完整 long 解、
holonomy 小根及真正 $C_R$ inverse，再输出全 $B$、$C_0$ 和 $B_0$。
定义其实际 B 残差
$$
 R_{B,\delta}=B_\delta-\Gamma_{\delta,B},\qquad
 R_{B,\delta}^{\flat}=R_{B,\delta}\circ\tau_\delta .
 \tag{R.2}
$$
这里不假定 $R_{B,\delta}=0$，也不假定帽的 $C_0$ 已经等于 long 输出。

原
[S.23](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md)
的 $f,g$ 是固定 physical $\theta$ 的 $\delta B,\delta C$；
[O.9–O.10](R133-supplement-true-full-delta-outer-rows-in-fixed-base-cap-inverse.md)
经准确 $D\Psi_\delta$ 及完整 onto chart 得到它的原 moving 行
$\mathfrak b_\delta$。这正是 fixed-physical-output residual 的导数，
并不需要候选本身已经满足 PDE 或外匹配。

另一张 nonlinear map 取输出
$$
 \big(P_{\perp,x}R_{B,Q}^{\flat},
      M_jR_{B,Q}^{\flat},
      M_jC_Q^\flat-\Gamma_{j,C_0}\big),\qquad
 M_jf=\langle jf\rangle_x .
 \tag{R.3}
$$
所有外 source 坐标只在基点固定转换，不对一个当前变化的
normalization factor 乘残差后遗漏其导数。
原实际反射类的 $B_0$ 精确为零；为完整 signed Fourier 延拓，
这里先保留该 weighted mean 行。

由
[完整 good tangent](R133-supplement-exact-unknown-outer-angle-good-tangent-and-full-means.md)
的 $\delta M_jf=M_j(\delta f-b_Hf_x)$，
(R.3) 的非mean raw 微分比原 good 行多
$$
 P_{\perp,x}\{b_H(R_{B,\delta}^{\flat})_x\},
 \qquad b_H=\eta_H/j_\delta .
 \tag{R.4}
$$
两个真实 curvature mean 的微分仍是原 good mean 行，不能给它们
重复加入同一 transport。独立高度、相容性荷及原角常相位荷仍分别保留。

## 2. 真实端点与完整 residual 的小量

本节的实际 small input 来自已经成功的 public run
$43615531666/1$，而非新计算。原小摘要为

- 路径：notes/full_delta_positive_ci/run-43615531666-1-full-real-delta-positive/evidence/full-delta-complete-regular-Hs-outer-summary.json；
- 23649 bytes，Git blob $0c43c92a618579401b8681dca67ba3a0e1554399$；
- SHA256 $769204e822787216c5aebd2cde30e73759fcf66d3bb1d6d1d76d2381bad6cae6$；
- 原 native SHA256 $5ab1d1b85cb71556b051fd53f5579cb30260ebdda6a844df9a4b377508e057fc$。

其完整字段直接给
$$
 \begin{aligned}
 |m_\delta|&>5.8446114523299999999991>5.8,\\
 |m_\delta|&<7.000000000000000000001,\\
 \|v_\delta-m_\delta\|_{A_{1/8}}&<9.615692\,10^{-9},\\
 \|u_\delta\|_{A_{1/8}}&<1.645272\,10^{-9}<2^{-28}.
 \end{aligned}
 \tag{R.5}
$$
因此 $\|v_\delta\|_{A_{1/8}}<8$。
这是把真实 mean 上界与 nonmean 上界相加得到的门；
不是从 T 中较松的 $|m_\delta|<8$ 再免费推 $|v_\delta|<8$。

T.3–T.6、T.16 已在固定 $x$ 的宽 $1/512$ 共同域给
$$
 \|j_\delta^{-1}\|<33/32,\quad
 \|\widehat u_\delta\|<2^{-25},\quad
 \|\widehat v_\delta-m_\delta\|<2^{-25},\quad
 \|y_\delta\|_{\mathcal Y_A}<r:=30F<2^{-24},
 \quad F=111/10^{11}.
 \tag{R.6}
$$
已知固定 $\Phi_0$ 的复合仍落在原 endpoint $1/8$ 域。
由 $|m_\delta|>5.8$ 和同宽 Neumann 级数，
$\|\widehat v_\delta^{-1}\|<1/4$，从而
$$
 \|B_\delta^\flat\|_{A_{1/512}}<2^{-27}.
 \tag{R.7}
$$

真 long 的 T.11、T.20 给
$$
 \Gamma_{\delta,B}^{\flat}
 =\chi_R(V-P)D^{-1/2},\qquad
 \chi_R<1/5,\quad \|V\|\le2r,\quad \|P\|\le r/3 .
$$
同一原小球有 $\|D^{-1/2}\|<2$；完整 mean 与 holonomy 小根都在
这个 binomial 级数中。因此
$$
 \|\Gamma_{\delta,B}^{\flat}\|_{A_{1/512}}
       <\frac{14}{15}r<2^{-24},\qquad
 \|R_{B,\delta}^{\flat}\|_{A_{1/512}}
       <\frac98\,2^{-24}.
 \tag{R.8}
$$
这里只用 T 实际已付的 $F=111/10^{11}$，没有将允许的独立高度
背景半径 $10^{-11}$ 偷换成较小的 $2^{-60}$ 半径。

完整 Fourier Cauchy 界与 $\partial_\theta=j_\delta^{-1}\partial_x$
于是给
$$
 \|R_{B,\delta,\theta}\|_\infty
 <\frac{33}{32}\,512\,\frac98\,2^{-24}
 =\frac{297}{256}\,2^{-15}<2^{-14}.
 \tag{R.9}
$$
这是整个原实 $\delta$ 区间和整个真正 nonlinear long graph 的界。
既没有按采样点估计，也没有把 residual 的上界称为实际误差下界。

## 3. 准确 B-only lift 与 source/load 方向

先固定原角常相位荷。由原归一化角定义，
$$
 \eta_H
 =I_\varphi\left(\frac{h_2}{m_\delta}
       -\frac{v_\delta\langle h_2\rangle_\varphi}{m_\delta^2}\right),
 \qquad \langle\eta_H\rangle_\varphi=0 .
 \tag{R.10}
$$
$m_\delta$ 的负号在恒等式中不变。用完整 $I_\varphi$ 的 $1/4$ 核及
(R.5)，
$$
 \|\eta_H\|_2
 \le\frac14\left(\frac1{5.8}+\frac8{5.8^2}\right)\|h_2\|_2
 =\frac{345}{3364}\|h_2\|_2<\frac18\|h_2\|_2 .
 \tag{R.11}
$$
$h_2$ 的 mean 没有删除；恰是 (R.10) 第二项。

在 $\varphi$ 表示中令
$$
 g=(R_{B,\delta,\theta}\circ\Theta_\delta)\eta_H,\qquad
 g_0=g-\langle g\rangle_\theta,\qquad
 h^*=(v_\delta g_0,0).
 \tag{R.12}
$$
这里 $\langle g\rangle_\theta=
\langle(v_\delta/m_\delta)g\rangle_\varphi$。
实际反射类中 $g$ 为奇函数，$g_0=g$；一般四重方向使用显示的
weighted 投影。减去常数不改变 (R.4) 的 ordinary 非mean 输出，
且使真实 B mean source 为零。

为明确全模 $L^2_\varphi$ 费用，写
$j_\varphi=v_\delta/m_\delta$，$\langle j_\varphi\rangle=1$。
在 ordinary 常数与非mean的正交分解中，
$I-1\otimes j_\varphi$ 的 norm 为
$\sqrt{1+\|j_\varphi-1\|_2^2}=\|j_\varphi\|_2<33/32$。
故
$$
 \|h^*_1\|_2
 <8\frac{33}{32}\frac{345}{3364}
       \|R_{B,\delta,\theta}\|_\infty\|h_2\|_2
 =\frac{11385}{13456}
       \|R_{B,\delta,\theta}\|_\infty\|h_2\|_2
 <2^{-14}\|h\|_{\mathrm{pair},2}.
 \tag{R.13}
$$

由于 $h^*_2=0$，其 mean、角变化和 physical C 变化准确为零。
完整 $D\Psi_\delta$ 因而直接给
$$
 (D\Psi_\delta h^*)_B=g_0\circ\Phi_\delta,\qquad
 (D\Psi_\delta h^*)_C=0,\qquad
 \langle h^*_1\rangle_\varphi
       =m_\delta\langle g_0\rangle_\theta=0.
 \tag{R.14}
$$
这里两次换测度均准确保留：
$d\theta=(v_\delta/m_\delta)d\varphi$、
$d\varphi=\omega_0dx$，且
$d\theta=j_\delta dx=(v_\delta/m_\delta)\omega_0dx$。
因此
$$
 g\circ\Phi_0=b_H(R_{B,\delta}^\flat)_x,\qquad
 P_{\perp,x}(g_0\circ\Phi_0)
       =P_{\perp,x}(g\circ\Phi_0),\qquad
 \langle g_0\circ\Phi_\delta\rangle_\theta
       =\langle(v_\delta/m_\delta)g_0\rangle_\varphi=0 .
 \tag{R.14a}
$$
(R.11)–(R.13) 的所有未知方向 $L^2$ norm 都在同一个归一化
$\varphi$ 测度中；没有将 $\theta$ 或 $x$ 的未知 $L^2$ norm
无偿等同于它。只有已知 coefficient 的 supremum 在实双射间取值，
故 (R.9) 可直接乘原 $\varphi$ norm。

这一步只用准确 reciprocal/angle differential，不需要背景解方程。
physical B mean 亦为零。原 long 导数作用在 zero C、zero height
输入上为零，故不会凭空添加 mean 或 nonlinear graph 项。

将 (R.14) 用 O 的基点固定 affine source chart 换回原 moving
行，得到 transport 的准确 load
$$
 \mathfrak t_\delta h=(-J_\varphi h^*_1,0),
 \qquad
 \|\mathfrak t_\delta h\|_{L^2\oplus\mathbb C}
                          <2^{-14}\|h\|_{\mathrm{pair},2}.
 \tag{R.15}
$$
若保完整 $B_0$ 端荷，第三个分量准确为零。
这里用的是 $J_\varphi$ 在完整非mean空间的等距性。
它不是把一个 forward cap 图转置成 adjoint，亦没有以有限97
矩阵代替未知完整输入。

在 (R.3) 规定的固定输出 source 坐标中，
$$
 \mathfrak b_{\delta,\mathrm{raw}}h
              =\mathfrak b_\delta h+\mathfrak t_\delta h .
 \tag{R.16}
$$
任何当前 normalization factor 的导数均不在这个固定转换中；
若另选一个会变化的输出因子，须重新加入其 factor-derivative
times residual。

独立角常相位若作为 affine source 允许变化，
(R.10) 应另加该常数 $\alpha$，并保留
$\alpha R_{B,\delta,\theta}$ 对应的 B-only source 列。
其大小由 (R.9)、(R.12) 同样支付；不把它认成径向 $\Gamma^*$，
也不把它删成零。实际反射任务的此常相位按原规范固定。

## 4. 以原完整基点 lift 同时付三项反馈

沿用 O.12–O.13 的原固定物理状态 $x=D\Psi_0h$：
$$
 \|G_{\partial,0}(r,s)\|_{\mathfrak M_0}
       <24(\|r\|_2+|s|),\qquad
 \|h(R)\|_{\mathrm{pair},2}<41\|x\|_{\mathfrak M_0}.
 \tag{R.17}
$$
这些是已证明的真实 boundary lift 与 endpoint 读出，
不是从 $L^2_r$ norm 猜测一个 trace。
$G_{\partial,0}$ 的原 residual Hessian、真实 outer graph、独立
mean 及非反射时完整 $B_0$ closure 继续保留。

当新数据指定 $\mathfrak b_{\delta,\mathrm{raw}}h=d_\partial$，
原 good 行满足 $\mathfrak b_\delta h=d_\partial-\mathfrak t_\delta h$。
因此完整固定方程准确为
$$
 x=x_{\mathrm{data}}
      +K_{\mathrm{body},\delta}x+K_{\mathrm{out},\delta}x
      -G_{\partial,0}\mathfrak t_\delta\mathcal H_0x,
 \qquad \mathcal H_0=(D\Psi_0)^{-1}.
 \tag{R.18}
$$
source/load 的负号由实际 boundary equation 得到；
范数预算只在该式之后取三角上界。

由 (R.15)–(R.17)，
$$
 \|K_{\mathrm{transport},\delta}\|
       <24\cdot41\,2^{-14}=984\,2^{-14}<\frac1{16}.
 \tag{R.19}
$$
最后比较是 $16\cdot984=15744<16384$。
原 V/O/X 的真实 $1/4+1/8<3/8$ 与该项**相加**，故
$$
 \|K_{\mathrm{raw},\delta}\|<\frac7{16}<\frac12,\qquad
 \|(I-K_{\mathrm{raw},\delta})^{-1}\|<\frac{16}{9}<2 .
 \tag{R.20}
$$
新因子不是旧 $8/5$；也没有把两个已经求逆的因子重复相乘。
全部 compatible source block 进入同一个方程，mean 与高度荷
从未被 projection 改成任意可解数据。

## 5. 新已知解析列与原高阶共同权

新增列仅含已知系数、weighted mean、固定 primitive 和
Hilbert 共轭，不对未知场作裸复角复合。
在固定 $x$ 的宽 $1/1024$ 上，(R.8) 的余宽与 T.3 给
$$
 \|R_{B,\delta,\theta}\circ\tau_\delta\|_{A_{1/1024}}<1.
 \tag{R.21}
$$
原 W.11 给 $\|\mathcal H_0\|<2^{13}$、
$\|I_{\varphi,0}\|<2^8$、$\|\Pi_{\varphi,0}\|<8$。
结合 $|m|^{-1}<1/3$、$\|\widehat v\|<8$，
(R.10) 的括号费小于8，所以 $\|\eta_H\|<2^{11}\|\widehat h\|$。
weighted 投影在复模块中可粗取3；固定 $J_\varphi$ 的真实核族
由 T 第6节可取16。于是 raw transport 行预合 $\mathcal H_0$ 后
有统一界小于 $2^{33}$。

在窄条带 $\sigma_*=2^{-128}$ 内，W.7 的完整物理 boundary
lift 族小于 $2^{16}$，O 的固定端口 source 换算可再付 $2^{16}$。
因此新增反馈的准确 coefficient-translation family 满足
$$
 \sup_{|\Im z|\le\sigma_*}
       \|K_{\mathrm{transport},\delta,z}\|<2^{65}<2^{80}.
 \tag{R.22}
$$
原完整 $\Gamma$、Cauchy derivative 与小根来自 T 的已知解析背景；
这里只有已知对象被平移。若包括上述独立角相位源，其新增 column
也被同一个安全 $2^{80}$ 支配。

将此项加入 X/Q 原族，可统一取
$$
 \sup\|K_{\mathrm{raw},\delta,z}\|<2^{130},\qquad
 \sup\|L_{\mathrm{raw},\delta,z}\|<2^{129}.
 \tag{R.23}
$$
第二式给原全部 ordinary/divergence、many-jump、端荷、mean、
height 与可选独立角相位 source 列；没有改变它们的原单位。
这两个粗界不用作实轴 Neumann 小量。

保持 Q 的同一辅助权
$$
 M=2^{416},\qquad W_{s,M}(n)=(1+n^2/M^2)^{s/2},\qquad
 -3/2\le s\le8212,\qquad \tau_s=|s|/(2M)<2^{-403}.
$$
原完整 signed-lag lemma 直接给
$$
 \|W_{s,M}K_{\mathrm{raw},\delta}W_{s,M}^{-1}
                 -K_{\mathrm{raw},\delta}\|
 <8\,2^{130}2^{-403}2^{256}=2^{-14}.
 \tag{R.24}
$$
(R.20) 加此数仍小于 $1/2$；完整 shifted inverse 仍小于2。
原 source lag 和以全部整数宽放，有
$$
 \|W_{s,M}L_{\mathrm{raw},\delta}W_{s,M}^{-1}\|<2^{260}.
$$
回通常 Sobolev 权只付一次 $M^{|s|}$；
原真实物理高度 $H^{s+2}$ 与其 pulled chart 的 Q.15 费用仍为
$2^{524288}$。于是
$$
 \boxed{\ 
 \|\mathcal G_{\delta,\mathrm{raw}}:
      \mathfrak D_s\longrightarrow\mathfrak M_s\|
 <2^{416\cdot8212+261+524288}<2^{4194304},
 \quad -3/2\le s\le8212 .
 \ }
 \tag{R.25}
$$
负阶仍先在有限 Fourier 输入上定义并完成，完整零阶唯一性识别
重叠定义。mean 频率的权为1，没有隐藏截止或未知高频清零。

## 6. 后续使用边界

R.25 是原显式族、同一已知 long 高度背景上的**新 raw 基逆**。
它为 B.25 的条件提供同一 source 坐标下的基点输入；
与有限高正则附近外行差组合时仍须实际加入独立高度背景差、
body 差、全部 mean、相容性与剩余强尾条件。
B 的方向窗口最高8192，不因 R.25 的8212自动扩大。

旧有限193 Green/Poisson/same97 数值链的算子身份保持原样；
本篇没有修改那些实际矩阵，也不能以一个全频局部帽上界代替
其尚未完成的方向合成或整个内体 high 反馈。

最后，原 $Q_\delta$ 仍不是已经匹配的 nonlinear PDE 解。
R.25 和附近极小球不证明 actual residual 已进入该球。
真正中心、可用低阶后验或延续、完整参数 Schur、所有两迹/mean
matching 以及最终几何条件仍须继续完成。
