# R99：真实根的完整 Cauchy 变换及 canonical v1 的全 Wiener 界

2026-11-12。本文的两个输入估计已完成；完整反馈逆与非线性零解仍在推进。

对象始终是 R97 的准确仿射族
$$
\delta_5=-7789843107295549/4611686018427387904,\qquad
|\delta-\delta_5|\le10^{-9}.
$$
所有真根、无限原函数和角图都随这个同一实参数变化。本文给出真实物理
Cauchy 变换的全部乘子与误差，并对实际 canonical 势
$b=(v_1\circ H^{-1})/3$ 证明六档截止、五档权、两档矩的完整 Wiener 界。
没有把准确有限参照多项式重新定义为几何，也没有据此宣称全反馈可逆。

本次本地执行器失联后的结果是在 CI 中从原始已保存输入重新计算的。
新报告 SHA 与丢失的本地报告不同，全部数值引用下面的新实际报告；
不能用旧摘要的末位替换新报告。

## 1. 精确的 Cauchy 变量变换

沿用 [R83](R83-actual-canonical-root-jets-and-physical-frame.md)：
$Y=F_z/|F|$ 是球面高度，$Y_0'$ 是根角导数，二者不同。
设
$$
u=\log\kappa+4\log F_z+2\log W-4\log H_{\rm geom},
\quad
v=\log\kappa+2\log W-2\log D,\quad
\mathscr D=-\partial_r+(M/D)\partial_\theta,
$$
并定义
$$
t_0=e^{-u/4},\quad Y_0'=e^{-v/2},\quad
\alpha=e^{(u-v)/2},\quad
\mu=\frac{\mathscr Du-\mathscr Dv/5+2\partial_\theta(M/D)/5}{4}.
\tag{99.1}
$$
由 R83 的 $c=2h_1/5$ 和 $L_1=(s_1-c)/2$，(99.1) 正好给
$\mu=L_1/2$，不是仅径向微分的替代量。物理 $r$ 方向动量为
$$
\pi_Y=-\alpha\,\mathscr DY/Y^2.
$$
R83 的准确关系
$$
w=Yt_0U,\qquad
\pi_g=-(Y\pi_w-w\pi_Y),\qquad
U_\xi=(t_0/Y_0')\pi_g+\mu U
$$
给
$$
\boxed{
\begin{pmatrix}w\\ \pi_w\end{pmatrix}
=
\begin{pmatrix}h&0\\s&-c\end{pmatrix}
\begin{pmatrix}U\\U_\xi\end{pmatrix},\quad
h=Yt_0,\quad c=Y_0'/h,\quad s=t_0\pi_Y+c\mu .
}
\tag{99.2}
$$
行列式准确为 $-Y_0'$。这里保持物理 $r$ 动量方向；换外法向时必须同步
改变该端动量符号。这个矩阵本身不是普通 $L^2$ 的酉矩阵。

grounded 的物理 $r$ 动量为 $Y\pi_w-w\pi_Y$，所以其变换是
$$
\begin{pmatrix}t_0&0\\c_g\mu&-c_g\end{pmatrix},
\qquad c_g=Y_0'/t_0.
\tag{99.3}
$$
根上物理密度源到 canonical 源的因子是 $h/Y_0'=1/c$，grounded
flux 因子是 $t_0/Y_0'=1/c_g$。这些恒等式不自动控制根外的体源。

## 2. 全参数、全角的真实有限系数和无限尾

源为以下三个已提交文件：

- scripts/fourfold_phase_root_cauchy_frame_ci_v1.py；
- scripts/fourfold_phase_root_cauchy_frame_ci_grid_cover.py；
- scripts/fourfold_phase_root_frame_fourier_ci_v1.py。

原准确 scalar germs、真无限 primitive 的全部 Cauchy 费用和移动根证书
与 R97 相同。三次区间 Newton 仅在原 family-root 包围内求交。新程序从
原足阶 jet 精确截到径向/角向三阶，保留各已知系数上的完整无限误差；
未知高系数没有补零。所有角导数仍由真正几何 ODE 递推。

在物理带 $|\operatorname{Im}\theta|\le S=1/256$ 上，64 个连续复矩形
覆盖半 quarter 的上半带；每格验证
$\operatorname{Re}F_z,\operatorname{Re}W,\operatorname{Re}D,
\operatorname{Re}H_{\rm geom},\operatorname{Re}\kappa,
\operatorname{Re}(F\cdot F)>0$。
因此倒数、对数、根号均在实轴相容分支。R83 的准确 D4 反射和 Schwarz
共轭补齐整个带。该复报告 complete/proved 为真、failed/pending 为空，
并给每个实际场的完整带上模界 $M_f$；没有用节点最大值代替复带界。

实角在准确 $\theta_j=\pi j/(2N)$、$N=4096$ 上计算 2049 个点，准确偶反射
给全部 $N$ 点。各点包含整个参数盒。对其中点作 Arb DFT，再把导出的
binary64 中点视为准确 dyadic，定义
$$
P_f=c_0+2\sum_{n=1}^{K-1}c_n\cos(4n\theta)+c_K\cos(4K\theta),
\quad K=N/2.
\tag{99.4}
$$
Nyquist 项只有一倍，不能当作两个完整系数。令 $e_2,e_\infty$ 为真实
nodal ball 对这些点中点的离散 RMS 和最大误差，$r=e^{-4S}$。以
$$
\|f\|_{A_s}=\sum_{n\in\mathbb Z}(1+4|n|)^s|\widehat f_n|,
\qquad s\in\{0,1/3,1/2,1\}
$$
计，nodal 插值误差至多
$(1+4K)^s\sqrt N\,e_2$。这是有限离散 Parseval 加 Cauchy--Schwarz，
并保留 Nyquist 半权。Arb DFT ball 变准确 dyadic 的完整加权 $\ell^1$
误差另付。

对所有遗漏系数、所有折回 alias 和 Nyquist，统一费用是
$$
E_{{\rm tail},s}\le
4M_fr^K\left[
\frac{(1+4K)^s}{1-r}+
\frac{4s(1+4K)^{s-1}r}{(1-r)^2}
\right].
\tag{99.5}
$$
证明使用 $|\widehat f_n|\le M_fr^{|n|}$；有限折回权不大于原高频权。
对于 $0\le s\le1$，凹函数的切线给
$(1+4(K+j))^s\le(1+4K)^s+4sj(1+4K)^{s-1}$，
再对几何级数准确求和，包含所有 $j\ge0$。两份高频尾由因子 4 支配。

因此真实 $A_s$ 范数是准确有限范数加上述三笔误差。每个请求的截断尾
也用有限剩余系数加同一完整误差，而不是由截断图形推断。
实 $L^2$ 误差为 $e_2+E_{{\rm tail},0}+e_{{\rm DFT},2}$。
用 R97 已证 Lebesgue 上界
$\Lambda_N\le1+(4/\pi)(1+\tfrac12\log(N-1))$，
实一致误差为 $\Lambda_Ne_\infty+E_{{\rm tail},0}+e_{{\rm DFT},1}$。

新完整报告包含 16 个 frame 场及 $v_1$，共 17 场。以下数字均向外放宽：

| 实际物理乘子 | $A_0$ | $A_{1/3}$ | $A_1$ | 真值减有限参照的 $L^2$ |
|---|---:|---:|---:|---:|
| $h$ | .346731 | .375796 | .584091 | $6.680\,10^{-11}$ |
| $c$ | .882631 | 1.890907 | 17.463166 | $1.438\,10^{-10}$ |
| $s$ | 25.469277 | 54.601077 | 504.373963 | $1.229\,10^{-8}$ |
| $1/h$ | 3.475994 | 3.747835 | 5.680984 | $6.860\,10^{-10}$ |
| $1/c$ | 8.109083 | 16.509203 | 152.204779 | $1.828\,10^{-9}$ |
| $t_0$ | 1.477443 | 1.629008 | 2.666851 | $2.536\,10^{-10}$ |
| $c_g$ | .207803 | .444708 | 4.120836 | $3.301\,10^{-11}$ |
| $c_g\mu$ | 5.132365 | 10.987889 | 101.971751 | $2.610\,10^{-9}$ |

完整表另含 $1/t_0,1/c_g,Y,\pi_Y,\mu,Y_0'$、两个源/flux 因子、
$s=1/2$ 范数和 11 档真尾。均值以及所有非零 Fourier lag 都在。
对物理 $v_1$，得到
$$
\|v_1-P_{v_1}\|_2<.007192175369,\qquad
\|v_1-P_{v_1}\|_\infty<.080749994709,\qquad
M_{v_1}=2380464.990234375.
\tag{99.6}
$$
一个带上最大模可小于其 Wiener 范数，这不是矛盾。

## 3. 准确名义角图的逐节点逆

使用 R97 已付的准确 dyadic $q_0$ 与完整有限 $P_Y$，定义
$$
H_0(\theta)=\theta+q_0I(P_Y)(\theta),\qquad
H_0'=1+q_0(P_Y-c_{Y0}),\qquad
\nu_0=P_{v_1}\circ H_0^{-1}.
\tag{99.7}
$$
$I$ 是零均值原函数；$H_0(0)=0$ 且其 quarter 周期归一准确成立。
其 $H_0'>m_0>0$ 的完整实圆证书来自同一 R97 名义图报告。

在物理 $G=16384$ 节点上，对 $H_0-\theta,H'_0,P_{v_1}$ 同时构造
$J=16$ 阶归一 Taylor 系数。半宽
$R=\pi(1+2^{-24})/(4G)$；各有限 Fourier 系数 $a_n$ 的完整余项为
$$
\sum_n|a_n|e^{4|n|R}\frac{(4|n|R)^{J+1}}{(J+1)!}.
\tag{99.8}
$$
导数系数和逆 FFT 由逐运算向外舍入的 DirectedFFT 包围，根单位本身由
Arb 包围。每次 Horner 前都以真正 Arb $\pi$ 验证相对于最近物理节点
的准确偏移满足 $|\Delta/R|\le1$。

对 canonical $\psi_j=\pi j/(2Q)$，$Q=16384$，浮点 Newton 仅产生候选
准确 dyadic $\theta_j$。最后重新计算整个真实有限多项式的球，得
$$
|H_0^{-1}(\psi_j)-\theta_j|
\le |H_0(\theta_j)-\psi_j|/m_0.
\tag{99.9}
$$
由于实圆 lift 全局严格递增且 onto，此式给真正唯一逆点；并不依赖
浮点 Newton 曾否收敛或某个 libm 精度假设。将 (99.9) 乘
$L_P=\sum_n4|n||a_n|$ 加入 $P_{v_1}(\theta_j)$ 得全部准确逆节点球。

$H_0$ 的完整复带正实导数给其逆带
$u_0=(7/8)S\inf\operatorname{Re}H'_0$。
与 R97 的单叶/边界虚部论证相同，像包含这个严格子带。
名义势复模由整个有限和
$M_{\nu_0}\le\sum_n|a_n|\cosh(4|n|S)$ 支付。
保留 canonical $|n|\le M=4096<Q/2$ 时，每个节点 DFT 系数的全部 alias 是
$$
M_{\nu_0}
\frac{e^{-4u_0(Q-n)}+e^{-4u_0(Q+n)}}{1-e^{-4u_0Q}},
\qquad n\ge0.
\tag{99.10}
$$
离散 nodal RMS、全部有限 DFT 舍入的 $\ell^2$ 和 (99.10) 的完整 $\ell^2$
都加入投影误差。准确偶性使 Fourier 系数实；程序验证 DFT 虚球含零。
这里的 $M<Q/2$，没有把 canonical 投影端点误当 Nyquist。

## 4. 从名义势回到整个真实参数盒

真实 $H=qY_0$ 和 (99.7) 满足 R97 的
$$
\|H-H_0\|_\infty<E_H=1.573761\,10^{-10},\quad
\inf H'>m=.54445389965,\quad \sup H'<M_H=2.80066819210.
$$
先将 $v_1-P_{v_1}$ 用真正 $H^{-1}$ 拉回，变量替换
$d\psi=H'(\theta)d\theta$ 给 $L^2$ 费
$\sqrt{M_H}\|v_1-P_{v_1}\|_2$。
再以 $H^{-1}$ 的 Lipschitz 界比较两个逆图，第二项至多 $L_PE_H/m$。
所以
$$
\|\nu-\nu_0\|_2
\le\sqrt{M_H}\|v_1-P_{v_1}\|_2+L_PE_H/m
<.012340284309,\quad \nu=v_1\circ H^{-1}.
\tag{99.11}
$$
加上 §3 的有限投影误差，准确 dyadic 系数 $c_n$ 满足
$$
\left(\sum_{|n|\le4096}|\widehat\nu_n-c_n|^2\right)^{1/2}
<E=.012340300647.
\tag{99.12}
$$
新报告的未放宽上界为
$.01234030064681631632736870274854222677429\ldots$。
丢失的本地运行给过不同末位，本文使用这次实际重算的较大上界。

真实逆图的带宽由同一真实 $H$ 的正实导数给
$$
u_*>\ .0018609264148396234,\qquad
|\widehat\nu_n|\le M_{v_1}e^{-4u_*|n|}.
\tag{99.13}
$$
不能把名义逆带 $u_0$ 与真实带 $u_*$ 混用。

## 5. 全 scaled Wiener 界及正根度量

对 $K\in\{52,64,96,128,192,256\}$、$a=0,\ldots,4$、
$j\in\{0,1\}$ 定义
$$
B_{K,a,j}
=\sum_{n\in\mathbb Z}|n|^j
 \left(1+\frac{|n|}{K+1}\right)^a|\widehat b_n|,
\qquad b=\nu/3.
\tag{99.14}
$$
$j=0$ 包含完整均值，采用 $0^0=1$；$j=1$ 的均值因子为零。
对任意实际选择的整数 $L\le4096$，(99.12)--(99.13) 严格给
$$
B_{K,a,j}\le\frac13\left[
\sum_{|n|\le L}w_n|c_n|+
 E\left(\sum_{|n|\le L}w_n^2\right)^{1/2}
+2M_{v_1}\sum_{n>L}w_ne^{-4u_*n}
\right],
\quad w_n=|n|^j(1+|n|/(K+1))^a .
\tag{99.15}
$$
中间项是整个低系数误差的 Cauchy--Schwarz 界，不是逐项将 L² 误差
直接当作无需累积的误差。最后一项包括 $4096$ 之外的所有真模。

所有多项式几何尾以准确二项式系数及
$$
\sum_{n\ge0}n^pr^n
=\sum_{\ell=0}^p
 \left\{\begin{matrix}p\\\ell\end{matrix}\right\}
 \frac{\ell!\,r^\ell}{(1-r)^{\ell+1}}
$$
支付，最大 $p=a+j=5$。有限个 $L$ 中选择任一已付上界都有效；
程序记录最终所选 $L$ 和有限参照、低系数费、完整真尾三项。
共 60 行，未对某个权使用未支付的导数。

例如 $K=64$ 的向外放宽结果是：

| $a$ | $B_{64,a,0}$ | $B_{64,a,1}$ |
|---:|---:|---:|
| 0 | 692327 | 143113 |
| 1 | 694529 | 232885 |
| 2 | 698111 | 1389968 |
| 3 | 719491 | 48192638 |
| 4 | 1460805 | 2157953223 |

$K=256$ 时另有 $B_{256,3,1}<1136112$ 和
$B_{256,4,1}<11589197$。大矩常数如实保留，不能用浮点观察替换。

令 $P_{>K}$ 为 canonical 四重指标 $|n|>K$ 的准确投影，
$\Gamma_n=4q|n|$，并定义
$$
D_K=P_{>K}\Gamma^{-1}M_b\Gamma^{-1}P_{>K}.
\tag{99.16}
$$
若 $|n|,|m|>K$，则
$\max(|n|/|m|,|m|/|n|)\le1+|n-m|/(K+1)$。
在高空间的 $\Gamma$ Sobolev 范数中，Young 卷积不等式因此给
$$
\|D_K\|_{H^s\to H^s}
\le \frac{B_{K,a,0}}{[4q_-(K+1)]^2},\qquad |s|\le a.
\tag{99.17}
$$
物理 Fourier 归一的非齐次范数也可用同一比值上界。
$D_K$ 实自伴，所以 $W_K=I+D_K$ 正性直接由 $s=0$ 的界给出。

| $K$ | $\|D_K\|_{L^2\to L^2}$ 上界 | $|s|\le4$ 上界 |
|---:|---:|---:|
| 52 | .163013 | .562317 |
| 64 | .108380 | .228680 |
| 96 | .048667 | .060448 |
| 128 | .027517 | .029866 |
| 192 | .012293 | .012564 |
| 256 | .006933 | .007000 |

特别是 $W_{52}\ge.836987I$；在低空间把 $D_K$ 延为零时 $W_K=I$，
低空间和物理均值被保留，没有从原问题删除。平方根、共轭与 Airy
函数的交换费用由后续完整算子论证支付，不能仅从正性免费得到。

## 6. 实际执行、原字节与重放

两个独立 CI 数学作业实际完成：

- canonical：run 43299719198，数学计算成功、artifact 保存成功；
  最后的 Git 发布因工作目录权限失败。run 43300446121 仅恢复该实际
  artifact，逐原文件 SHA 检查后终端 Git 推送，未用摘要重造数据。
  普通 PR81 已合 main，merge 1c104b2cc48bb7586df7fcf8cf98455a38f632a6。
- Cauchy frame：run 43301136757，复格、真节点、完整 Fourier 三步均成功，
  原生 artifact 13980433875；终端 Git 推送
  0329befbdc6426b3a7e750b2ba1408d087cd0766。报告含全部依赖、输入和 runtime。

关键 SHA256：

| 文件 | SHA256 |
|---|---|
| notes/2026-11-12-ci-physical-v1.json | 7364affd39b7b5a73f45988f0e697c93c73720f32b655b65940375d0b6dbc01d |
| notes/2026-11-12-ci-canonical-v1-scaled-Wiener.json | c736ccff24d8cacc607d5a8f016f66b72a2565112e989ea01e4078c5dc9e1ae6 |
| notes/2026-11-12-ci-canonical-v1-scaled-Wiener.npz | 5c0653d5844e5de2259e2e856ef5efeed0577b2d84b355cb18078fef2dfe8615 |
| data/root_finite_grid/ci_cauchy_frame_grid4096_h1e9/manifest.json | d0f263f4f48e24fd88b8cd39e63d51cdd0206d50d3d314796ff41a6c0d1d9f98 |
| notes/2026-11-12-ci-actual-root-Cauchy-frame-complex.json.gz | b872d49b788f54c0ad8f854b16c1097d6a7ef04162b883b9d0b675ab57db7d05 |
| notes/2026-11-12-ci-actual-root-Cauchy-frame-Fourier.json.gz | d6f74fae93df5db08f5ac26b2ba196112ce73812643ad125278c42a8ca345439 |
| notes/2026-11-12-ci-actual-root-Cauchy-frame-Fourier.npz | d459eebbc6b7520b51507828506bb1f084dc879af547fa822ef7993ec60e8607 |

完整原生数据由终端 Git 保存；工具接口只传小于 100 KB 的文本。
两个小 summary 是完整实际报告的逐字段抽取；它们不是替代原报告的新证书。
ci-root-r99-manifest 和 ci-root-frame-r99-manifest 记录全部文件 SHA；
后者明确 actual_fresh_computation=true、original_local_bytes_recovered=false。

重放入口，工作目录为本课题目录：

~~~bash
python scripts/fourfold_phase_physical_v1_fourier.py --out notes/2026-11-12-ci-physical-v1.json
python scripts/fourfold_phase_canonical_v1_wiener_ci_v1.py --out notes/2026-11-12-ci-canonical-v1-scaled-Wiener.json
python scripts/fourfold_phase_root_cauchy_frame_ci_v1.py --mode strip --out notes/2026-11-12-ci-actual-root-Cauchy-frame-complex.json.gz
python scripts/fourfold_phase_root_cauchy_frame_ci_grid_cover.py --grid 4096 --chunk 256 --directory data/root_finite_grid/ci_cauchy_frame_grid4096_h1e9
python scripts/fourfold_phase_root_frame_fourier_ci_v1.py --out notes/2026-11-12-ci-actual-root-Cauchy-frame-Fourier.json.gz
~~~

已有实际成功证据不要求机械再跑才能使用。本条完成了根上的乘子、完整误差和
$W_K$ 正性输入；其后继续同一全两通道反馈、有限低块/高模 Schur、
全源右逆及保持固定开帽的非线性 C² 零解。
