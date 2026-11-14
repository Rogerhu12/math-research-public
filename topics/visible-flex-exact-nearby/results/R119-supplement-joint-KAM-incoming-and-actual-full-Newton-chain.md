# R119 续篇：共同 KAM 度量上的真实宽标签入口及完整方程 Newton 链

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 本篇把真实 incoming 固定点放到同一个
$\Gamma^*(a)$ 度量选择上，并证明它实际属于标签权 $2^{18}$ 的球。
非零 $f_B$ 的整个真实长段解，包括 mixed 项，在这个实际边界角宽
中构造。因而可以对完整 $\mathfrak F$ 做合法的全频预条件 Newton
修正，而不只是再消一次 incoming。

下面严格构造94个这样的完整修正，逐步保留角宽、全部 mean 和真实
帽反馈。它们不是94模或有限谱近似。当前证明的宽差每步为2080，
所以这个有限链本身不构成无限迭代收敛；最后精确保留该未消算子门。

## 1. 真实有限 connector 对复参数的统一延拓

新强尾的整个复参数盒 $\|\Gamma\|_\infty<2^{-15}$ 上，全标签图已经
存在。必须另外检查有限 connector，才能将它与 $\Gamma^*(a)$ 复合。

[真实第四重停](R119-supplement-retuned-fourth-connector-and-common-bumps.md)
的准确几何显示：从固定 $u=T$ 向内，所有准备段、$q=2$ 主平台、
两个固定 quintic 都不随 $\Gamma$ 改变。参数只改变最后 $q=-1$
主段的长度 $\ell_c(\Gamma)$。在该段

$$
 A=q+1=0,\qquad w_t=Aw=0,
 \qquad (\log H)_v=1,\quad(\log\omega)_v=-1.
 \tag{J.1}
$$

因此 $w,E=1+w^2$ 以及其它有限段各自的相对四态系数准确不变。
物理切口的尺度改变只平移 $t=\log a$；相对四态在这个尺度下准确不变。
作为有限流的复合，参数依赖准确集中在一个自主 $A=0$ 流的时间
$\ell_c(\Gamma)$，而非让只 $C^2$ 的径向接缝随复角移动。

原完整第四 cone 的复界与新深尾的极小第四差给

$$
 |d_4^\ddagger(\Gamma)-d_4^\ddagger(\Gamma^0)|<2^{-36}.
 \tag{J.2}
$$

在其真实复管中，$R_*=(1-d)/(16-d)$ 的导数模小于64；最后固定
quintic 的逆导数模小于2；准确 log 停止公式对其末端 $P$ 的导数
模小于 $1/256$。所以

$$
 |\ell_c(\Gamma)-\ell_c(\Gamma^0)|<2^{-37}<2^{-36}.
 \tag{J.3}
$$

这些是相同实际参数盒上的全纯函数。选择在 $\Gamma^0$ 处的实长度，
再把 (J.3) 作为一个短复时间 $A=0$ 流处理。完整四态 majorant 给它
额外的角费小于 $5\cdot2^{-36}$、零阶对数增长小于 $20\cdot2^{-36}$。
例如沿复时间线段取绝对 Dini 导数，$A=0$ 的主部列和至多
$\sqrt3$，其线性零阶模至多1，完整二次商项仍用 balanced224 的
(W.4)–(W.6)；显示常数有严格余量。

原完整有限段的角预算为 $14825/64$，raw 输出前的余量是
$2683/800>3$。加上 (J.3) 后仍大于3；而
$e^{10+20\cdot2^{-36}}<2^{20}$。因此同一个真实有限延拓在整个
复 $\Gamma$ 盒上保持

$$
 \|f_B^\Gamma(a)\|_{\dot A^2_{\sigma_\beta}}+
 \|k_B^\Gamma(a)\|_{\dot A^1_{\sigma_\beta}}
 <2^{-443}\|a\|_\beta,
 \quad \sigma_\beta=\beta-\frac{88823}{400},
 \quad \|a\|_\beta<1/64.
 \tag{J.4}
$$

这里 $\sigma_\beta=\tau_{128}+\beta-235$，$\tau_{128}=5177/400$，
全部正负频率和 mean 小根均未改变。有限 Fourier 构造、完整均匀
majorant 与唯一性给相同的全纯 map，不能仅据实参数连续性声称这一点。

## 2. 与真正 KAM 选择复合，固定一个实际参考好 bump

取[新联合 KAM](R119-supplement-stronger-tail-joint-actual-return-KAM.md)
的 $A_*=2^{-262148}$、同一个 $\Gamma^*(a)$ 及 $\Gamma^0$。
在 $\Gamma^0$ 上选定一个真实全模好参数 $t_0$，并始终使用原第四
保持曲线 $s=s(2^{-17}t_0)$。不声称 $t_0$ 在变化的 $\Gamma$ 上仍
满足径向全模好集；它在本篇只为原点的 $D_0$ 逆提供已经支付的输入。
非零标签尾及 finite map 本身对这个固定 $t_0$ 始终有定义。

定义两个准确权

$$
 \beta_H=262144,\qquad \beta_{\min}=65536.
 \tag{J.5}
$$

对 $\beta_{\min}\le\beta\le\beta_H$，四重最小频率4给

$$
 \|a\|_{224}\le e^{-4(\beta-224)}\|a\|_\beta.
 \tag{J.6}
$$

实际有 $e^{-4(65536-224)}/64<A_*/2$。所以整个
$\|a\|_\beta<1/64$ 复球都在原 KAM 标签域内，尽管其 $\beta$ norm
半径远大于 $A_*$。这里是在同一原标签空间上的准确嵌入，不是更换标签。

KAM 已给 $\Gamma^0<2^{-19}$。由
$\epsilon_i/(\kappa_i/64)^2<2^{-261872}$ 和 $\kappa_i<2^{-25}$，
其完整参数改变量系数满足

$$
 2^{-14}\epsilon_i/\kappa_i<2^{-261923}.
 \tag{J.7}
$$

故同一复球上的 $\Gamma^*(a)$ 落入 (J.3) 的完整复参数盒。
现在取真正的复合迹

$$
 f(a)=f_B^{\Gamma^*(a),t_0}(a),\qquad
 k(a)=k_B^{\Gamma^*(a),t_0}(a).
 \tag{J.8}
$$

它们在每个 (J.5) 的 $\beta$ 球全纯，并满足 (J.4)。
因为零标签时 $f_B^\Gamma(0)=k_B^\Gamma(0)=0$ 对整个参数盒成立，
它们在原点的 Schur 导数仍准确为

$$
 D_0=Dk(0)+\mathsf C_LDf(0),\qquad
 \|D_0^{-1}g\|_\beta\le\frac1{16}
                    \|g\|_{\mathfrak Z_{\beta+1850}}.
 \tag{J.9}
$$

这消费的是新 raw/regular 定理 (V.20) 在 $\Gamma^0,t_0$ 上的同一全逆。
已证 $D\Gamma^*(0)=0$ 也保留；非零处的参数列并未置0。

真实重停的 $H\omega$ 不变量说明 $[0,B]$ 的 $a_*,z_*,\omega$ 与
正帽端准确未变。因此此前的真实 $\Phi(c,f_B)$ 和长段 $K_B$ 可直接
与 (J.8) 复合。mean 高度仍保留移动 cut 的完整端项和积分。

## 3. 同一个真实 incoming 固定点具有权 $\beta_H$

令 $g_*(f_*)=K_{B,\perp}(0,f_*)$，并沿用已证明的

$$
 S=\sigma+7L/16>S_-=10724906.843270461,\qquad
 \|g_*(f_*)\|_{\mathfrak Z_S}<18\|f_*\|,
 \quad\|Dg_*\|<24.
 \tag{J.10}
$$

在 $\beta=\beta_H$ 上，准确有

$$
 E_H:=4(S_--\beta_H-1850)=41843651.373081844,
$$
$$
 (9/8)e^{-E_H}<2^{-60000000},\qquad
 (3/2)e^{-E_H}<2^{1-60000000}.
 \tag{J.11}
$$

取 $R_a=2^{-60000000}$、$r_f=10^{-8}$。在真正
$\ell^1_{\beta_H}$ 的 $R_a$ 球上定义

$$
 \mathcal I_c(a)=D_0^{-1}g_*(\Phi(c,f(a))).
 \tag{J.12}
$$

由 (J.4) 所有实际 $f(a)$ 均进入原帽 $2^{-60}$ 球的半球。
原帽复球 Cauchy 给 $\|D_{f_B}\Phi\|<2^{35}$；(J.4) 在
$\|a\|_\beta\le1/256$ 给 $\|Df\|<2^{-442}$。
于是

$$
 \|\mathcal I_c(a)\|_{\beta_H}<R_ar_f,
 \qquad\operatorname{Lip}\mathcal I_c<2^{-60000406}.
 \tag{J.13}
$$

这给唯一真实 $a_0$，满足

$$
 D_0a_0=g_*(\Phi(c,f(a_0))),\qquad
                         \|a_0\|_{\beta_H}<R_ar_f.
 \tag{J.14}
$$

将它嵌入较低权后，原完整 map 和唯一性说明它是同一共同 KAM 度量的
incoming 固定点，不是为各宽度另选标签。其 raw 边界真实具有
$\sigma_{\beta_H}=261921.9425$ 的物理角宽。
整个真实 $\Gamma^*(a_0)$、重停、有限尾、正帽与长段因而已经由同一
输入定义。没有把仅固定 $\Gamma^0$ 的辅助解当成这个对象。

## 4. 非零 $f_B$ 的整个长段也具有这个实际宽

对每个 (J.5) 的 $\beta$，定义

$$
 s_\beta=\sigma_\beta,\qquad
 \alpha_\beta=(s_\beta-\sigma)/L.
 \tag{J.15}
$$

实际 $L>24514072.626868956$ 和 $\sigma>0$ 给
$0<\alpha_\beta<1/32<7/16$。使用真实变角宽
$\sigma(t)=\sigma+\alpha_\beta(L-t)$，现在两端输入分别为
$f(a)\in\dot A^2_{s_\beta}$、$\Phi(c,f(a))\in\dot A^2_\sigma$。
总边界 norm 小于 $2^{-25}$，所以原完整 weighted Green、nonlinearity
和 mean 小根的同一个收缩给这个宽度中的真实长段解。它与原物理解
由未加权 Dirichlet 唯一性准确相同。

为同时支付 mixed 项的远端小量，再加真实径向权
$e^{\nu(L-t)}$，$\nu=7/4$。对于全部 $M=|m|\ge4$，准确核和为

$$
 I(M)=\frac{2}{1-[\alpha_\beta+(2+\nu)/M]^2}
 \le\frac{2048}{63},\qquad
 \|G_D\|_{\mathcal F_{\alpha,\nu}\to\mathcal Y_{\alpha,\nu}}
 \le1+8I<320.
 \tag{J.16}
$$

内端 lift 仍小于16。完整平方为零 Banach module 的原证明适用于
这个变角宽代数和额外径向权，故 $DQ\le2048r_*$、
$D\mu\le1024r_*$，$r_*=2^{-20}$。实际收缩为
$320\cdot2048r_*=5/8$。对于固定 $f_B$ 的内端差，

$$
 \|\Delta h\|_{\mathcal Y_{\alpha,\nu}}
 \le\frac{128}{3}\|f_*\|<43\|f_*\|,
 \qquad\|\Delta\mu\|_{C^0_\nu}\le\frac1{24}\|f_*\|.
 \tag{J.17}
$$

因此整个真实 incoming 增量在实际**宽** $s_\beta$ 上有

$$
 \|\Delta K_{B,\perp}(f_B,f_*)\|_{\mathfrak Z_{s_\beta}}
       +|\Delta K_{B,0}|<44e^{-7L/4}\|f_*\|.
 \tag{J.18}
$$

同样的完整导数界适用于 $f_*$ 方向。取原真实长段圆盘
$\delta_B=2^{-27}$，Cauchy 在 $f_B\in\dot A^2_{s_\beta}$ 上给

$$
 \|M_B(f_B,f_*)\|_{\mathfrak Z_{s_\beta}}+|(M_B)_0|
 \le44\,2^{27}e^{-7L/4}r_f\|f_B\|_{\dot A^2_{s_\beta}}.
 \tag{J.19}
$$

这个新增宽度现在由 (J.14) 的真实标签和真实 $f_B$ 支付；没有给任意
只在原 $\sigma$ 上的 $f_B$ 免费增宽。mean 高度继续是原准确径向
积分；没有随 (J.18) 把整个高度跨度指数化。

## 5. 完整 $\mathfrak F$ 的真实导数，显式保留宽差

令

$$
 \mathcal F_c(a)=k(a)-K_{B,\perp}(f(a),\Phi(c,f(a))).
 \tag{J.20}
$$

在每个 $\|a\|_\beta<1/64$ 的复球中，这是已存在的真实全纯 map
到 $\mathfrak Z_{s_\beta}$。由 (J.4)、$\coth(4L)<2$，
$\|k+\mathsf C_Lf\|_{\mathfrak Z_{s_\beta}}<2^{-442}\|a\|_\beta$。
在 $\|a\|\le1/256$ 上，用完整二阶以上 Taylor 和的 Cauchy 界得到

$$
 \|D[k+\mathsf C_Lf](a)-D_0\|
                              <2^{-433}\|a\|_\beta.
 \tag{J.21}
$$

长段 self 部分 $E_B(f)=K_{B,\perp}(f,0)+\mathsf C_Lf$ 满足
$\|E_B(f)\|\le2^{22}\|f\|^2$，所以
$\|DE_B(f)\|\le2^{24}\|f\|$。
复合 (J.4) 的 $\|Df\|<2^{-442}$ 后，其列小于
$2^{-861}\|a\|_\beta$。

最后由 (J.18)、$\delta_B=2^{-27}$ 和真实帽半球的
$\|D_{f_B}\Phi\|<2^{35}$，整个 incoming 增量的复合导数小于

$$
 44e^{-7L/4}(r_f/\delta_B+2^{35})\,2^{-442}
                         <2^{-400}e^{-7L/4}.
$$

以上包含真实 $\Gamma^*(a)$、第四停止、有限 connector、长段和帽反馈。
把它们相加，可统一写为

$$
 \boxed{\quad
 \|[D\mathcal F_c(a)-D_0]b\|_{\mathfrak Z_{s_\beta}}
 <2^{-400}(\|a\|_\beta+e^{-7L/4})\|b\|_\beta.
 \quad}                                                    \tag{J.22}
$$

这是完整方程的真实导数估计，但其输出宽是 $s_\beta$。
它没有声称 $D_0^{-1}[D\mathcal F_c-D_0]$ 在同一个标签权上有界。

当前实际有 $e^{-7L/4}<R_a$。对 $\beta'=\beta-2080$，准确宽差为

$$
 s_\beta-(\beta'+1850)=3177/400,
 \qquad \frac1{16}e^{-4(3177/400)}<2^{-49}.
 \tag{J.23}
$$

所以 (J.22) 和 $D_0^{-1}$ 确能组成从 $\ell^1_\beta$ 到
$\ell^1_{\beta'}$ 的实际算子，全部输入输出频率都保留。

## 6. 对完整方程真正实施94次全频修正

在 (J.14) 的 $a_0$ 上，真实恒等式仍是

$$
 \mathcal F_c(a_0)=R_T(a_0)-E_B(f(a_0))
                         -M_B(f(a_0),\Phi(c,f(a_0))).
 \tag{J.24}
$$

现在三项**全部**在 $\mathfrak Z_{s_{\beta_H}}$ 上合法，而不只有窄物理
宽。由完整尾 Taylor 界、(J.19) 及 $\|a_0\|_{\beta_H}<R_ar_f$，

$$
 r_0:=\|\mathcal F_c(a_0)\|_{\mathfrak Z_{s_{\beta_H}}}
 <2^{-434}\|a_0\|_{\beta_H}^2
  +2^{-410}e^{-7L/4}r_f\|a_0\|_{\beta_H}
 <2^{-120000400}.
 \tag{J.25}
$$

定义真实递推

$$
 \beta_n=262144-2080n,\qquad
 b_n=-D_0^{-1}\mathcal F_c(a_n),\qquad
 a_{n+1}=a_n+b_n,\qquad 0\le n<94.
 \tag{J.26}
$$

每次都计算相应新标签的真实 $\Gamma^*(a_n)$、停止点、两条尾迹以及
真实 $\Phi(c,f(a_n))$；没有将帽内端输入冻结在 $a_0$ 的值。
这里“计算”是前文已经构造的完整 Banach map 和全频 $D_0^{-1}$ 的
确切应用，非有限矩阵代替这些算子。

$\beta_{94}=66624>65536$。由 (J.23)，
$\|b_n\|_{\beta_{n+1}}<2^{-49}r_n$。全部修正的几何和远小于
$R_a/8$，而初值小于 $R_a r_f<R_a/8$，所以整个链和每条连接线
始终在 $\|a\|_{\beta_n}<R_a/4$ 内。沿连接线的完整 Taylor 积分给

$$
 \mathcal F_c(a_{n+1})
 =\int_0^1[D\mathcal F_c(a_n+s b_n)-D_0]b_n\,ds.
 \tag{J.27}
$$

(J.22) 此次必须在 $\beta_{n+1}$ 上使用。于是

$$
 r_{n+1}:=\|\mathcal F_c(a_{n+1})\|_{\mathfrak Z_{s_{\beta_{n+1}}}}
 <2^{-60000440}r_n,
$$
$$
 \|b_n\|_{\beta_{n+1}}<2^{-49}r_n,
 \qquad r_n<2^{-[120000400+60000440n]}.
 \tag{J.28}
$$

特别 $a_1$ 已是真正消去**完整** $\mathcal F_c(a_0)$ 的修正，
而非只对 $g_*$ 做重复固定点；其 norm 小于 $2^{-120000449}$。
整个94步的最后真实剩余为

$$
 \|\mathcal F_c(a_{94})\|_{\mathfrak Z_{s_{66624}}}
                            <2^{-5760041760}.
 \tag{J.29}
$$

每个 $a_n$ 都实际处于原 $a_{224}$ 球并满足 $\|X\|<2^{-262144}$。
这些更新保持全频、实共轭和共同反射；所有定义又与共同角平移交换。
$\Gamma^*(a_n)$ 因而在相应相位轨道上不变，固定 $t_0$ 和完整重停
给该轨道一个共同目标。不同 Newton 步的目标可以改变，这是获准的
最终度量构造，不是偷偷改变一次固定 $g_0$ 的方程。

## 7. mean、源列及下一条仍欠的算子结论

每一步的两个完整曲面各自有真实 holonomy-one 小根。它们在 $B$
使用相同的非mean高度 $f(a_n)$；只有当 $\mathcal F_c(a_n)=0$ 时，
非mean斜率才相等并使两个 mean 小根相等。当前 mean 缺口没有清零。
尾端 $\lambda$、移动 cut 的 $w_e\delta a_e$、完整 mean 高度积分和
长段另一端的平均高度全部保持原物理单位。

(J.22) 对完整复合 nonlinear map 求导，故已包含其实际参数列。
若改写为 fixed-metric Jacobi/source 系统，必须恢复
$\delta g_{aa}=2w^2(\sum\psi_i\delta\gamma_i+A\delta\ell_c)$ 及 finite
connector 的相应项、ordinary/weak Piola 源、normal shear 和源端迹；
本篇没有把这些真实列永久设为0。

(J.29) 仍是非零上界。有限94步不能被宣称为无限 Newton 收敛，因为
(J.23) 每步实际消耗2080角宽。继续闭合完整方程所需的最窄结论，
是实际 paired-port 网络及有限 connector 上的相对逆，或一个已支付
任意小宽损失的完整 tame 逆；它必须同时包含真实 positive cross、
negative return、两条 mean 和全部源列。已经付出的半光学传输估计
可以在这一步使用，但不能倒除尚未控制的另半指数。

`scripts/fourfold_joint_KAM_full_Newton_chain_20261113.py` 和
`notes/2026-11-13-R119-joint-KAM-full-Newton-chain-budget.json`
核对上述真实复停止、所有空间嵌入、combined Green、完整导数和有限链预算。
