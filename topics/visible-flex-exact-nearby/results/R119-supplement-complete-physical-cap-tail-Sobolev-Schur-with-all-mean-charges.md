# R119/R133：同一物理帽与完整尾逆的 Sobolev Schur，保留全部 mean 荷

2026-11-15，visible-exact / tail_connector。

**已证明下述物理空间中的完整线性 Schur。** 本篇在同一个新 fixed-stop simple-root 尾、
同一个已选全网参数及原 final ac1 物理帽线性化上，真正消去此前独立的
$Z=(C_R-C_{\rm ref})_\perp$。关键是以
$H^{-3/2}$ 作为这条曲率接口的空间：帽的二阶高度列与 long 的一阶
平滑源列恰好相接。全部无限 high、deep-low、有限浅前缀和真实平均通量
继续参与同一个逆。

所得反馈严格小于 $2^{-32000000}$。其中物理因子 $a_Bw_B$ 在往返中
准确抵消；没有把这个极小正数、长段反射或帽内高频设为零。
本篇也重新支付从 $B$ 源到根的一阶源窗，未把已付 $L^2$ contact
擅自用于 high inverse。

范围必须精确：帽系数是
[实际全模物理帽](R133-supplement-actual-final-all-mode-physical-cap-Green.md)
(C.1)--(C.28) 的完整 ac1 中心、原 $|\eta|\le10^{-9}$ 区间。
帽内不要求该有限候选已经满足 Codazzi；其真实缺陷作为 affine source
保留。第9节使用已经完成的同物理角完整转授，将同一结论推广到定义
SHA256 为 440866a3… 的连续修补中心，明确限于固定 $\eta_0,\delta=0$
的物理 Codazzi 线性化。全 $\delta$ moving 族及其
$H^{-3/2}$ residual-sensitive 共轭仍是另外的转授门；本文不将
已付的 $L^2$ Hessian 门升为该负阶门。

## 1. 完整联立式及三种不同的 mean

记 $R=25/8$，帽内侧仍为原 $L_c=9/10$，$B$ 是 long 另一端的
真实物理切口，令
$$
 s_B=a_Bw_B>0,\qquad
 \epsilon_L=e^{-7L/4}<2^{-33554432}.
 \tag{L.1}
$$
在一个固定背景处，所有未显示的 affine 数据暂固定为零。令

* $\mathcal C_f$ 为完整物理帽加真实 regular 边界图的线性解算子
  $f_B\mapsto Z$，内侧非mean $C(L_c)$ 固定；
* $\mathcal Q_Z$ 为 long 的独立 $Z$ 列到 $B$ 的物理 total 通量源；
* $\mathcal T_B$ 为已闭合 fixed-$C_R$ 尾的 $B$ 通量源到
  $\Pi_\perp h_B/s_B$，整体物理高度 gauge 取零。

$f_B$ 是原归一化非mean高度，不是物理高度 $h_B$。
$\mathcal C_f$ 内已解掉所有 $D_Zd,D_Zc_0,D_Zb_0$；
$\mathcal T_B$ 内已解掉真实 $D_f\Phi_R$。
这两处是原同一二变量 $\Phi_R(Z,f_B)$ 的两个不同导数列，均只计一次。

在加入原实际源后，准确联立式是
$$
 Z=Z^{\rm cap}+\mathcal C_f f_B,\qquad
 f_B=f_B^{\rm tail}+\mathcal T_B\mathcal Q_Z Z .
 \tag{L.2}
$$
这里 $Z^{\rm cap}$ 和 $f_B^{\rm tail}$ 是各自原完整 Green/source map
的真实输出。它们不是一个新定义的“普通 $L^2$ 源”替身。

本篇始终区分三个量：

1. Darboux/Jacobi 的物理 mean total 通量及其一个常高度 gauge；
2. Codazzi 曲率的 $B_0,C_0$，包括真实 long 输出 $b_0(Z,f_B)$；
3. canonical root-wave 的 Fourier mean 槽。

它们之间只用已付的准确两行变换，不互相代称。
曲率的平均 $B$ 条件不能靠高度通量兼容自动删去。

## 2. 同一 ac1 帽在完整复角平移族中的逆

采用原物理角，归一圆周测度。
[实际帽](R133-supplement-actual-final-all-mode-physical-cap-Green.md)
(C.4)--(C.11) 的完整乘法列满足
$$
 \|Q_B\|_{\mathfrak A_{1/64}}<.04,\qquad
 \|Q_c\|_{\mathfrak A_{1/64}}<.052 .
 \tag{L.3}
$$
这里 $\mathfrak A$ 是逐 Fourier 系数先取径向 supremum 后求和，
包含全部真 inverse-angle 产生的无限模。特别 (L.3) 并不是 moving
多项式未换角时的系数范数。

原全正核有
$$
 K_G<16,\qquad H_D<10,\qquad H_C<3 ,
 \tag{L.4}
$$
来自原 (C.18)--(C.20)。两条 mean 的未闭右端 lift 都不超过1。
这些是整个 $[L_c,R]$ 的核，不是只在外端成立的数。

下面给出外边界图所需的共同复背景球，避免把实角逆直接延拓。
[实际 regular 图的 Hs 证明](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md)
(S.7) 给
$$
 \|Z\|_{A^0}<2.533\cdot10^{-13},\quad
 |Z_{4j}|\le {4|j|P\over5.8}e^{-4|j|d},\quad
 P=1.480385\cdot10^{-11},\quad d>.124999999985 .
$$
在 $|\operatorname{Im}z|\le1/128$ 平移背景时，$|j|\le32$ 的贡献
不超过 $3\|Z\|_{A^0}$。其余模可用
$q=e^{-4(d-1/128)}<2/3$ 及
$$
 \sum_{j\ge33}jq^j
 \le105(2/3)^{33}<105\,2^{-18}
$$
直接加总；$3^{16}>2^{25}$ 即给所用最后一个有理门。
所以整个平移背景仍满足
$$
 \|C_zZ\|_{A^0}<10^{-12}<\bar z=10^{-10},\qquad
 \|C_zf_B\|_{\dot A^2}<2^{-60}<\bar b=10^{-11}.
 \tag{L.5}
$$
后式使用原背景的真实宽 $1/16$；它不限制未知 Sobolev 方向。

在原 Hs 篇 (S.10)--(S.11) 取
$$
 r_f=10(\bar z+\bar b),\quad
 F=r_f+\bar b={111\over10^{11}},\quad
 \kappa=36\,2^{12}F<1/4096 .
$$
原平方零 Banach module、完整 long Green、holonomy 小根和准确
$C_R$ 反演给以下同宽列；完整 Wiener 方向和原 $L^2$ module
方向均适用：
$$
 \begin{array}{c|cc}
 &Z\text{ 列}& f_B|D|^{-2}\text{ 列}\\ \hline
 d(R)&1/1024&1/8192\\
 c_0(R)&1/8192&1/65536 .
 \end{array}
 \tag{L.6}
$$
例如 $J_f=9/(1-\kappa)<10$，
$T=2^{-512}+4\,2^{14}FJ_f<1/1024$；
其余三项直接代入同一原公式。所有 scalar mean functional 仍在表中。

[真实 B 均值接口](R133-supplement-complete-fourfold-periodic-cap-long-graph-with-true-B-mean.md)
(B.9)--(B.18) 再给完整 $b_0$ 两列，均可安全取 $2^{-48}$。
该结论在平方零 $L^2$ module 中另已证明；不是把 Wiener
导数范数直接改名为 Hilbert 范数。此处较小的 $F$ 仍在该原球内。

由 (L.3)--(L.6)，同一复杂平移族中的完整帽反馈小于
$$
 16(.052)+10/1024+1/8192+2^{-48}<.85<.9 .
 \tag{L.7}
$$
$Q_B$、$Q_c$ 通过原 pair 范数取最大值，不能再漏掉一条 mean。
因此全帽逆 norm 小于10。
$f_B$ 的完整未闭右端荷则小于
$10/8192+1/65536+2^{-48}<1/512$ 倍 $\|f_B\|_{\dot H^2}$。
故
$$
 \|\mathcal C_f:\dot H^2_\perp\to L^2_\perp\|<1/32 ,
 \qquad
 \|\mathcal C_f:\dot A^2_\perp\to A^0_\perp\|<1 .
 \tag{L.8}
$$
同一证明也控制完整两曲率输出；这里只在最后取 $Z$ 的非mean投影。
没有利用反射子空间的逆来猜全 $4\mathbb Z$ 逆。

所有 shifted 算子均由同一个原物理角的准确方程定义。
先在有限 Fourier 数据上，由唯一性有
$\mathcal C_{f,z}=C_z\mathcal C_fC_{-z}$；
然后按已付 norm 完成闭包。原实中心的反射只是一种背景性质，
未知方向并不被要求具有同一反射。

## 3. 帽的二阶列与 long 的一阶列在同一 Sobolev 空间相接

记 $\Lambda=(1-\partial_\theta^2)^{1/2}$，物理频率为 $4\mathbb Z$。
对输入单模 $n\ne0$，(L.8) 在 $z=\pm i/256$ 给
$$
 |(\mathcal C_f)_{mn}|\le |n|^2e^{-|m-n|/256}.
 \tag{L.9}
$$
输出 $m=0$ 的完整曲率行也满足同式；取 $Z$ 后才删除它。
乘输入 $H^{1/2}$、输出 $H^{-3/2}$ 权，
$$
 {\ |n|^2\over\langle n\rangle^{1/2}\langle m\rangle^{3/2}}
 \le(1+|m-n|)^{3/2}.
$$
两侧 signed-lag Schur 和同时有限。用
$1-e^{-1/64}>1/128$ 及完整 $\sum_{\ell\ge1}\ell^2q^\ell$
公式，含两分量和 mean 的安全界是
$$
 \boxed{\ 
 \|\mathcal C_f:H^{1/2}_\perp\to H^{-3/2}_\perp\|<2^{40}.
 \ }
 \tag{L.10}
$$
这里没有先将输入截成有限 head。

另一方面，
[真实 long 的完整 DN 与独立帽列](R119-supplement-actual-long-screening-complete-Sobolev-DN-and-cap-facing-port.md)
(N.23)--(N.23a) 先给 long 自己的物理源列，其同宽
$A^0\to A^1\oplus\mathbb C$ 费为 $2^{10}s_B\epsilon_L$。
进入 tail 的真源还须经过 (N.24) 的有序
$\mathcal P_{\mu_T}M_{r_\mu}$。原 (R.19)--(R.20) 在同一余宽中
给这两个乘法/mean 读取在 $A^0,A^1$ 的合计费用小于 $2^8$；
例如每个非constant系数的 $A^1$ norm 小于2，
mean 分母大于原正参考的一半。没有用 $P_\perp$ 替代
$\mathcal P_{\mu_T}$。把这项、原余宽和有限求和放入 $2^{20}$，
完整源的真实平移族给
$$
 |(\mathcal Q_Z)_{mn}|
 \le {2^{20}s_B\epsilon_L\over\max(1,|m|)}
                 e^{-|m-n|/128}.
 \tag{L.11}
$$
这次输入权 $H^{-3/2}$、输出权 $H^{-1/2}$ 的商不超过
$2(1+|m-n|)^{3/2}$。因此同一个全 signed-lag 论证给
$$
 \boxed{\ 
 \|\mathcal Q_Z:H^{-3/2}_\perp\to H^{-1/2}\|
             <2^{64}s_B\epsilon_L .
 \ }
 \tag{L.12}
$$
它是原列的准确改权，不是新宣称任意外源都享有相同平滑。

(L.11)--(L.12) 计算时保留完整输出 mean。
原真实 long mean 商 (R.5)--(R.6) 证明，holonomy-one 的线性化
对两端所有非mean Dirichlet 方向使用同一个自然 mean 通量条件。
随后在未匹配 $B$ 口，未知 $Z$ 变化不改变独立的 $q_T$；
准确 $\mathcal P_{\mu_T}$ 令这条 tail affine 列的 mean 通量为零。
因此其实际输出属于
$$
 \mathcal B_0=\{b\in H^{-1/2}:\langle b\rangle=0\}.
 \tag{L.13}
$$
该恒等式由真正 total 通量及有序接口求平均得到，不是对 (L.11) 矩阵
任意删一行。其 raw mean 斜率修正 $c_B$ 仍按 (N.24) 输出；
背景未匹配时不能同时宣称它为零。一般 long particular、metric source 或 weak
法向端荷仍可能有非零 charge，后文另保。

## 4. 远端源的一阶根窗必须重新支付

记 $\mathcal P_B$ 为新完整正区的 homogeneous root incoming
到真实 $B$ 高度的映射。它含 actual fixed-$C_R$ long 图、
未匹配界面和全部 mean。以下证明
$$
 \|\mathcal P_B:L^2\to H^{1/2}\|<2^{256},\qquad
 \|\mathcal P_B\Lambda^{4/3}:L^2\to H^{1/2}\|<2^{6100}.
 \tag{L.14}
$$
相同门对真实伴随正型成立。这里并没有要求整个负尾 inverse
具有 $H^1$ 状态界。

完整依据是
[新正区](R119-supplement-new-simple-root-complete-positive-DN-Airy-return-and-sources.md)
(P.13)--(P.32)，连同上述 long 篇 (N.26)--(N.28) 的真实小型差。
根初值准确为
$u_0=D_+(0)z_++D_-(0)\mathcal R_a z_+$。
原 $D_\pm(0)=\chi B_0^{-1/2}E_\pm$、
$2^{28}<b<2^{29}$ 和 $\|\mathcal R_a\|<2$ 给
$$
 \|u_0\|_{H^{1/3}_\kappa}<2^{14}\|z_+\|_2 .
$$
(P.31) 的全域 Poisson 有根数据能量范数小于32，
$B$ 非mean迹由真实 long 正型控制，完整 mean 高度则由
$\sup_t\|H_f(t)\|_2<2^{194}\|u_0\|_{H^{1/3}_\kappa}$ 控制。
固定-$C_R$ 相对型差小于 $1/64$，正逆及伴随的额外因子小于2。
两端角图费用均已包含；这些式子给 (L.14) 第一门。

还需一个 source-to-$B$ 辅助门。对零 root Dirichlet、
$B$ 荷 $\beta\in H^{-1/2}$，(P.31) 给能量范数
$<2^{191}\|\beta\|_{H^{-1/2}}$，包括其 mean。
(P.16) 的零 root trace 版本再给其 collar 高度的
$L^2_yH^{2/3}_\kappa$ norm $<2^{196}\|\beta\|$。
取真实伴随和 Green 配对，得到
$$
 \|w_B\|_{H^{1/2}}<2^{196}
       \|f\|_{L^2_yH^{-2/3}_\kappa}
 \tag{L.15}
$$
对完整零 root Dirichlet collar ordinary 源成立。
根以外的所有响应仍通过同一个全域 inverse，未设置第二个 collar 边界。

现在使用 (P.23)--(P.25) 的高输入 trial，
$P_H=\mathbf1_{\{|m|\ge L_*\}}$、$L_*=2^{4200}b$。
trial 在 $B$ 准确为零，其真实校正给
$$
 \mathcal P_B(I+E_A)P_H=(w_{\rm corr})_B P_H .
 \tag{L.16}
$$
这里每一式均在右侧保留 $P_H$，低 trial 列为零。
原完整 residual 和 incoming contact 已付
$$
 \|f_{\rm tr}P_H\Lambda^{4/3}\|<2^{30}b^{4/3},\qquad
 \|E_AP_H\Lambda^{4/3}\|_{2\to2}<2^{50}b^{5/3}.
$$
代入 (L.15)、(L.14) 第一门，按
$\mathcal P_BP_H=(w_{\rm corr})_BP_H-\mathcal P_BE_AP_H$
支付，得到高输入右强窗。这里没有反演 $I+E_A$。

低输入按真实 $\mathcal P_BP_L$ 付
$2^{256}\langle L_*\rangle^{4/3}<2^{5900}$；
$2^{28}<b<2^{29}$ 已计入。
高低相加严格落在 (L.14) 第二门。
这一步保留低非mean、mean、远 lag 和两条 source 行。

## 5. 实际 B 源到完整 Airy affine 列的 H1 窗

令 $b_e$ 是给定 $B$ 端物理通量荷 $\beta$ 时，根 incoming 为零的
真实 Airy affine 输出。全根 Wronskian 对每个非mean和 mean
均为同一个 $2i\chi^2$，$\chi=c/\sqrt\pi$。
对任意伴随 incoming $z$ 作完整 Green 配对，给
$$
 2\chi^2|\langle b_e,\mathcal R_{\rm adj}z\rangle|
     =|\langle\beta,\mathcal P_{B,\rm adj}z\rangle|.
 \tag{L.17}
$$
真实方向只改变配对的一个单位符号，故不影响这个绝对值恒等式。
没有把伴随返回写成 $\mathcal R_a^*$：
准确式仍为 $\mathcal R_{\rm adj}=\mathcal R_a^{-*}$。

由 (L.14)，
$\mathcal P_{B,\rm adj}^*:H^{-1/2}\to H^{4/3}$
的 norm 小于 $2^{6100}$。
从 (P.1) 的 $s=1$ 门及 $b<2^{29}$，
$\|\mathcal R_a:H^1\to H^1\|<2^{6040}$。
又 $(2\chi^2)^{-1}<4$。因此 (L.17) 严格给
$$
 \boxed{\quad
 \|b_e\|_{H^1}<2^{14000}\|\beta\|_{H^{-1/2}} .
 \quad}
 \tag{L.18}
$$
这正是全 high inverse 所需的一阶 source 窗。
只使用 (P.32) 的 $L^2$ affine 门，无法推出 (L.18)。

同一个 source lift 的 $B$ 高度也有安全门
$2^{15000}\|\beta\|_{H^{-1/2}}$。
可先取 (P.31) 的零 root Dirichlet 解，再用其完整 incoming
contact 和 (L.14) 第一门消掉 incoming；全部 mean 仍包含在内。

## 6. 用实际全网权抽取有限 e0 响应

采用已出版
[真实 mixed weighted Schur](R119-supplement-new-outer-complete-mixed-weighted-Schur-and-closed-nonmean-inverse.md)
(Y.17)--(Y.28) 及
[完整 mean 商](R119-supplement-new-closed-mean-compatibility-gauge-and-complete-fixed-CR-inverse.md)
(Z.18)--(Z.28) 的同一个参数、表示和源域。记
$$
 v_j=2^{-464800}(j+5)^{-4165}\delta_j^{1073/32},
 \qquad F_j=2^{4096}(j+5)^4\delta_j^{-5}.
$$
在新增外分量及其相邻有限行 $129\le j\le131$ 上，
$$
             v_j^{-1}<2^{503000},\qquad F_j<2^{5000}.
 \tag{L.19}
$$
这是直接使用 $j+5<2^8$、$\delta_j^{-1}<2^{135}$ 的有理幂比较。
不是用一个浅层频率 cutoff 代替源的真实 $H^1$ norm。

设输入是仅支持在这些有限根上的原 Airy $H^1$ 源，norm 为 $G$。
共同 $H_a^*$ 在 $H^1$ 的费用小于 $2^{66}$，
见原 high-exterior (H.6)--(H.9) 与新增同一个模型共轭。
令 $D=2^{503066}G$。
完整高消元给
$$
 \|v^{-1}k_{\rm rem}^{(H)}\|<2D,\qquad
 \|v^{-1}F k_D\|<2^{-4000}D .
$$
第二式使用 $g_D=0$ 和真正 $F_H$ 在权 $v^{-1}F$ 下的
$2^{-9000}$ 门。有限源的 $F_j$ 费由 (L.19) 支付；
没有假定高消元后的源仍有限邻接。

再用完整 $F_D$ 费用 $2^{130}$，有
$\|v^{-1}k\|<4D$。
对物理 charge 相容的源，(Z.18)--(Z.27) 在零高度 gauge 给
$$
 \|vx_{\rm rem}\|<8D,\qquad
 \|vF^{-1}x_D\|<2^{134}D .
 \tag{L.20}
$$
后式含真实 $R_Dk_D$，使用
$\|vF k_D\|\le\|v^{-1}F k_D\|$，没有删掉 particular。
在权 $vF^{-1}$ 下继续用 $E_H,R_H$ 得
$$
 \|vF^{-1}x_H\|<2^{15}D .
 \tag{L.21}
$$
$R_H$ 在这里确实消费原输入的 $H^1$ norm，合法性由 (L.18) 保证。

最后从 (L.20)--(L.21) 抽取有限外根，用 (L.19) 支付
$F_j/v_j$。实际负片散射与共同 $H_a$ 在 $L^2$ 真酉，
该分量只有两个实际根；所以送入新正片的真正 incoming 满足
$$
                  \|z_{+,e_0}\|_2<2^{1100000}G .
 \tag{L.22}
$$
未粗化的指数在 $1011100$ 以下；显示门留有明确余量。
这项推导没有要求整个全网状态在未加权 $\ell^2$，
也没有把 weighted strong source 与 weak state 域混同。

对 $\beta\in\mathcal B_0$，其正片 source 的全网兼容荷正是
$\pm\langle\beta\rangle=0$，由原完整 Piola/Green 接线而得。
把 (L.18)、(L.22)、(L.14) 和 source particular 合并，
恢复原归一化 $f_B=\Pi_\perp h_B/s_B$，得到
$$
 \boxed{\quad
 \|\mathcal T_B:\mathcal B_0\to H^{1/2}_\perp\|
                        <{2^{1200000}\over s_B}.
 \quad}
 \tag{L.23}
$$
$s_B$ 没有被丢弃。这个门也不把 $H^{1/2}$ 端迹升成原
$\mathcal X_{224}$ 的全层强标签。

## 7. 同一个实际 Schur 已经严格收缩

由 (L.10)、(L.12)、(L.23)，在同一个
$\mathcal Z=H^{-3/2}_\perp$ 中，
$$
 \mathcal K=\mathcal C_f\mathcal T_B\mathcal Q_Z,\qquad
 \|\mathcal K\|
 <2^{1200104}\epsilon_L<2^{-32000000}.
 \tag{L.24}
$$
这里 $s_B^{-1}s_B=1$ 是原物理单位的准确抵消，
不是对两个极端浮点数的数值约分。

所以 (L.2) 的真实唯一解为
$$
 Z=(I-\mathcal K)^{-1}
       (Z^{\rm cap}+\mathcal C_f f_B^{\rm tail}),\qquad
 \|(I-\mathcal K)^{-1}\|<2 .
 \tag{L.25}
$$
恢复 $f_B$、帽两曲率以及全尾的 high/deep/remaining 时，
每一块都使用其原完整 Poisson 和同一 source map。
不能只把 (L.25) 的低边界逆称作帽 high 已消失。

如果需要将各个独立数据显示成矩阵形式，准确的是
$$
 \binom{f_B}{Z}
 =
 \begin{pmatrix}I&-\mathcal T_B\mathcal Q_Z\\
                 -\mathcal C_f&I\end{pmatrix}^{-1}
 \binom{f_B^{\rm tail}}{Z^{\rm cap}},
 \tag{L.26}
$$
其中第一行 norm 按 $s_BH^{1/2}$、第二行按 $H^{-3/2}$ 读取。
没有把非对称 block 矩阵误作正定或酉矩阵。

## 8. 所有原源、曲率 mean 和物理荷继续保留

原帽 ordinary pair 源使用 C.22 的真实 $L^2_rL^2_\theta$ 输入；
角散度源使用其原 Hilbert-module 范数，
物理 jumps 和两端曲率数据按 C.24--C.25。
加入真实 $b_0$ 列后仍按本文完整逆处理。
这些数据先形成 $Z^{\rm cap}$；
若只付到另一个原源域，就保留该 Green 输出的真实
$H^{-3/2}$ norm，不改名为任意 $L^2$ 方向。

尾的 ordinary、两 weak、BV 原子、独立 long particular、
裸法向端荷、两条 $D\Gamma^*$、$\nu$ 和其它材料列，
先按 A/P/N/Y/Z 的有序 map 形成 $f_B^{\rm tail}$。
它们必须满足该 map 的原 source 窗。
本篇 (L.18) 只替特定远端 $H^{-1/2}$ 荷支付额外根窗；
不替任意体源自动增加角导。
一般 $L^2$ 体源也不自动拥有裸 $F^t$ 的端点迹。

若独立源的真实兼容荷为 $\mathcal L_a g\ne0$，
先用 Z.19 的增广解保留
$\tau=\mathcal L_ag/(\mathcal L_a\sigma_\circ)$。
由于 (L.13)，改变未知 $Z$ 的闭环不改变这条真实 charge。
因此 (L.25) 不会偷偷消去 $\tau$；真正方程仍须满足
$\mathcal L_ag=0$。一个整体物理常高度依然是唯一 gauge，
而且在 (L.2) 的两条非mean曲率/高度列上准确不起作用。

帽内平均曲率仍满足
$$
 (a^2B_0)'=a^2(F_B)_0,\qquad
 [a^2B_0]_{L_c}^{R}
   =\int_{L_c}^{R}a^2(F_B)_0\,dr
      +\sum_i a_i^2[j_B]_0 .
 \tag{L.27}
$$
外端 $B_0(R)=D b_0(Z,f_B)+b_0^{\rm src}$、
$C_0(R)-C_{\rm ref}=D c_0(Z,f_B)+c_0^{\rm src}$
都是原完整输出。内端的平均 $B$ 若须与 waist 或主体接合，
(L.27) 是仍需消费的真实 scalar 行；不能用 (L.13) 替代它。

未匹配 $B$ 口的 raw mean 斜率 $c_B$ 继续按 (N.24) 的准确式
回传；它也不由曲率 $B_0$ 或 (L.13) 替代。
long 的 mean 高度跨度仍是
$\int_0^L aw\,D\mu(h)\delta h\,dt$，按原 $aw(R)/165$ 门收费，
没有附加 $\epsilon_L$。
参数微分保留
$\delta s_B,\delta\mu_0,\delta\Phi_R$、
真实 root/source 坐标及 $\dot H_a^*g$；
stop 和尺度只在原已经证明固定的方向上取零导数。
在真正参数盘内仍支付 $q!r_p^{-q}$，不改变选参测度。

## 9. 已付连续修补物理中心的推论，以及尚余强问题

上述 ac1 结论可以真正转授到已有的连续修补物理中心；
这里使用原证书的完整解析条带，不能只使用其 $L^2$ 结论。
[连续修补物理帽及准确残差共轭](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)
第1节固定的修补定义 SHA256 是

```
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
```

该原文 (C.8)--(C.9) 已明确证明，在修补后的**同一物理角**
及完整联合 Wiener 范数中，
$$
 \|Q_B\|_{\mathfrak A_{1/64}}<.039196064,\qquad
 \|Q_C\|_{\mathfrak A_{1/64}}<.051432066,\qquad
 \|\Delta C(R)\|_{\mathfrak A_{1/64}}<4.970\,10^{-19},\qquad
 |\Delta C_0(R)|<7.898\,10^{-23}.
 \tag{L.28}
$$
其原实际 background-v2 native 的六门全部成功。
第7节明确该报告证明的是背景及物理 Green 转授，未将
`full_residual_sensitive_bridge_proved=false` 改成 true。
本篇复用这些已付不等式，没有重跑其原目标或把数值摘要作为新对象。

原 intrinsic target 与 rotational comparison Green 完全相同，
所以 (L.4) 的原核逐项保留；(L.28) 直接给 (L.3)。
对同一 $|\operatorname{Im}z|\le1/128$ 平移，
$\|C_z\Delta C(R)\|_{A^0}\le4.970\,10^{-19}$。
前述 (L.5) 的原端点计算实际小于 $7.7\,10^{-13}$，
加上这个真修补差仍小于 $10^{-12}$。
$C_0$ 的改变按 (L.28) 留在原 uniform exterior 图中。
因此 (L.5)--(L.8) 及完整 signed-lag 推导逐项成立，
所有 mean 列保留，未知方向仍取全 $4\mathbb Z$。

新尾的 positive/long/fixed-$C_R$ 结果本来就在这一共同
$Z$ 及 $f_B$ 背景球上均匀成立。故在固定
$\eta=\eta_0,\delta=0$ 时，(L.2)、(L.10)--(L.27)
也给**连续修补中心的物理 Codazzi 帽与同一新尾的完整 Schur**，
同样有 $\|\mathcal K\|<2^{-32000000}$。
修补中心真实物理残差、独立 mean、$\nu$ 入端响应和所有界面源
作为其自己的 affine 输入保留；没有以旧 ac1 源替换它们。

这条推论的未知空间是物理曲率空间。它不借助原文
(C.11)--(C.13) 依反射固定角积分常数的 moving 反演，
也不将其自动延拓到任意全 $4\mathbb Z$ moving 方向。
已有 $L^2$ Hessian 反馈小于 $.003840162$ 的完整帽证书，
仍不能单独推出本文所需的 $H^{-3/2}$ 同空间逆。
若要用于全 $\delta$ 或 moving 中心，尚须另付：

* 同一物理角的 (L.3) 与端点复平移球 (L.5)--(L.6)，以及
  全部 real/complex 参数范围；若常数改变，重新代入 (L.7)；
* moving-to-physical 的完整 residual-sensitive operator/source
  差在所用负阶空间中的界，含角规范、两条 mean、参数列及界面迹，
  不能只转换 homogeneous principal 两行。

原 $\nu$ bump 在 $r>.18$ 为零，仅说明 intrinsic cap 不直接变化；
它不证明非径向中心的两个物理乘法列不变。
原方向是有限 Fourier 多项式，也不使真 physical-angle 系数有限带。

在上述两个明确物理中心的范围内，未知 $C_R$ 已由 (L.25)
真正解掉，所有曲率 mean 与 source row 都完整回传。
仍需完成原强 ordinary/weak source 和 $\ell^1_{224}$ 标签两向映射、
原主体/waist 的 mean 与 $\nu$ 联立、最终 nonlinear matching；
不能从本篇 Sobolev Schur 或 Y/Z 的弱根逆直接宣称这些强结论。
