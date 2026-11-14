# R119 续篇：KAM 后的固定径向参考、真实端角和二阶度量选择

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在
[新尾实际联立 KAM](R119-supplement-stronger-tail-joint-actual-return-KAM.md)
的同一标签球内，严格段的完整密度 Cauchy 比较可以从随标签变化的
径向参考 $\Gamma^*(a)$，改为 KAM 之前已经固定的 $\Gamma^0$。
仍有
$$
 \sum_i\eta_i<2^{192000}\|X\|\le2^{-70144}.                  \tag{F.1}
$$
这里比较的是全频、两个独立 mean 的完整演化。两个真实端角可以
同时把两条实际 principal 流与这个固定参考的两条流准确对齐。
此外 $\Gamma^*(a)-\Gamma^0$ 从标签二阶开始，因而此度量选择
不改变零标签处的固定度量 Jacobi 方向。

本篇不把上述事实称作整个正负混合网络的逆；真实正型 DN、根
框架和完整普通/度量源仍须按各自合同接入。

## 1. 一个固定参考和清楚的物理尺度

采用前篇
$$
 A_*=2^{-262148},\quad \|a\|_{224}<A_*,\quad
 \bar a=\|a\|/A_*,\quad \|X\|<16\|a\|,\quad
 \varepsilon_i=2^{24}(j+4)N_j^\#A_*.
$$
标签函数是实际 (U.13) 的一行，$\|E^{-1}\|<2$，所以也有
$$
                         \|a\|_{224}\le2\|X\|_{\mathcal X_{224}}.
 \tag{F.2}
$$
这不是任意状态的假逆界，而是对同一个满足 $\ell(X)=a$ 的
真实全标签解直接读取的界。

KAM 之前固定
$\Theta_i(\Gamma_i^0)=\omega_i/4$，其后
$\Gamma_i^*(a)$ 满足实际非径向 return 的同一目标相位。
两者的实际 log-profile 参数差满足
$$
 |\Delta\gamma_i|:=|\Gamma_i^*(a)-\Gamma_i^0|
 <2^{-14}{\varepsilon_i\over\kappa_i}\bar a
 <2^{39}(j+4)\sqrt j\,\delta_j^{-3/4}N_j^\#\|X\|.
 \tag{F.3}
$$
这里使用 $\kappa_i^{-1}<2^{28}\sqrt j\,\delta_j^{-3/4}$ 和 (F.2)。
它在每个真实负分量只改变其自己一个下降 bump。

比较参考的 $A_0,w_0$ 取固定 $\Gamma^0$。在每个实际解上，
参考物理半径采用同一个 $a_{\rm phys}=\rho(\Gamma^*)e^t$。
这个明确的整体相似尺度不改变 $\kappa_0$、参考角相位或以下
任何归一化 Cauchy 常数；在原两迹恢复中它仍被完整保留。
因为 bump 在根邻域为0，参考 $w_0,A_0$ 在两端与
$w_{\Gamma^*},A_{\Gamma^*}$ 准确一致。没有同时混用两个不同
$\rho$ 的 raw flux 单位。

## 2. 真实 bump 支集上重新估完整径向势

写本分量下降段的实际落差为 $\Delta=\Delta_{j,k}$，
$\eta=\eta_j$。在支集上
$$
 Q_\gamma=-A_\gamma
 =7+{\sqrt{12}\Delta\over\eta}S'(x)-\gamma\psi_t,\quad
 dt={\eta\over\sqrt{12}}dx,\quad 1/4\le x\le3/8.
 \tag{F.4}
$$
此前已核 $j/2<\Delta<3j$、
$135/128\le S'\le3375/2048$、$|S''|\le6$、
$|S'''|\le60$、$|\psi_x|\le96$、
$|\psi_{xx}|\le6144$、$|\psi_{xxx}|<2^{24}$。
整个实参数盒给下列实际包络；以下差分取连接
$\Gamma_i^0,\Gamma_i^*$ 的实线段，故全部平方根取正实支：
$$
 {\Delta\over\eta}<Q_\gamma<12{\Delta\over\eta},\quad Q_\gamma>1,\quad
 |Q_{\gamma,t}|<2^7{\Delta\over\eta^2},\quad
 |Q_{\gamma,tt}|<2^{15}{\Delta\over\eta^3},
$$
$$
 |\partial_\gamma Q|<2^9\eta^{-1},\quad
 |\partial_\gamma Q_t|<2^{17}\eta^{-2},\quad
 |\partial_\gamma Q_{tt}|<2^{30}\eta^{-3}.
 \tag{F.5}
$$
三阶 bump 导数在两支集端点按分片函数理解；其前二阶连续且
端二 jet 为0，所以 $Q_t$ 连续，没有差分造成的 delta 源。

完整径向密度势是
$$
 \kappa_0(\gamma)
 ={Q_t\over2\sqrt Q}-{(1+Q)^2\over4\sqrt Q}
              +{5Q_t^2\over16Q^{5/2}}-{Q_{tt}\over4Q^{3/2}}.
 \tag{F.6}
$$
由 (F.5) 逐项微分，四项的绝对导数可以分别取
$$
 2^{17}\Delta^{-1/2}\eta^{-3/2},\quad
 2^{11}\Delta^{1/2}\eta^{-3/2},\quad
 2^{27}\Delta^{-3/2}\eta^{-3/2},\quad
 2^{30}\Delta^{-3/2}\eta^{-3/2}.
$$
例如第一项完整导数为
$Q_{\gamma,t}/(2\sqrt Q)-Q_tQ_\gamma/(4Q^{3/2})$；
第三、四项同样保留其分母导数。由于 $\Delta>1$，安全地有
$$
 |\partial_\gamma\kappa_0|
 <2^{32}\sqrt\Delta\,\eta^{-3/2}.
$$
支集长小于 $\eta$，$\sqrt\Delta<2\sqrt j$，
$\eta^{-1/2}<3\delta_j^{-3/4}$，所以
$$
 \boxed{\quad
 \int_I|\kappa_0(\Gamma_i^*)-\kappa_0(\Gamma_i^0)|dt
 <2^{35}\sqrt j\,\delta_j^{-3/4}|\Delta\gamma_i|
 <2^{74}(j+4)^2\delta_j^{-3/2}N_j^\#\|X\|.
 \quad}                                                     \tag{F.7}
$$
这一次费用使用实际大 $Q\asymp\Delta/\eta$ 支集，不用根切口
的小下界 $Q>1/128$ 去估内部 bump。没有由参数很小就推断
整个势或高频相位的算子差很小。

## 3. 所有部分参考角流，及完整同空间 generator

两个径向参考流都是实际平移。任意部分区间上的相位差由
$$
 |q_{\Gamma^*}-q_{\Gamma^0}|
 ={|\Delta\gamma_i\psi_t|\over q_{\Gamma^*}+q_{\Gamma^0}}
$$
及 $\int|\psi_t|dt=2$ 控制，故
$$
 \sup_{t\in I}\left|
    \int_{t_L}^t(q_{\Gamma^*}-q_{\Gamma^0})d\tau\right|
 <2\sqrt{\eta_j/\Delta_i}\,|\Delta\gamma_i|
 =2^{26}\kappa_i|\Delta\gamma_i|
 <2^{37}(j+4)N_j^\#\|X\|.
 \tag{F.8}
$$
因 bump 在两个根 collar 之外，这个估计同时适用于完整分量
和两个固定原径向严格切口间的部分区间。相位窗 $\kappa_i$
与 (F.3) 中的逆相位窗在这里准确相消。

保留
[严格段全密度证明](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
的实际状态
$Y=(c,\alpha,Z_+,Z_-)\in\mathcal F_\upsilon$、
$-9/2\le\upsilon\le7/2$，以及两条真实 $H_\sigma,S_\sigma$。
只把参考 $H_\sigma^0$ 改为固定 $\Gamma^0$ 的平移。
此前实际流与 $\Gamma^*$ 参考流的 $C^8$ 差小于
$2^{34}(j+4)N_j^\#\|X\|$；(F.8) 的另一个差是常平移，
没有额外角导。故可统一取
$$
 \widehat r_i=2^{40}(j+4)N_j^\#\|X\|<2^{-32}.
 \tag{F.9}
$$
以同一个有序 $L_HB_HR_H$ 分解估计，仍有
$$
 \|\mathcal A_H-\mathcal A_{0,\Gamma^0}\|
 <2^{96}\big(\|\kappa-\kappa_{0,\Gamma^0}\|_{\mathcal A_1}
                       +\widehat r_i|\kappa_{0,\Gamma^0}|\big).
 \tag{F.10}
$$
这里真正小差是
$(C_S-C_{S^0})D_\theta^{-1}$ 或从 $H^{\upsilon+1}$ 到
$H^\upsilon$ 的 density pullback 差；裸同阶 pullback 差未使用。

原 (S.13) 给
$\int\|\kappa-\kappa_{0,\Gamma^*}\|_{\mathcal A_1}
 <2^{130}(j+4)^2\delta_j^{-5}N_j^\#\|X\|$。
加 (F.7)，在同一个角空间中得到
$$
 \int\|\kappa-\kappa_{0,\Gamma^0}\|_{\mathcal A_1}
 <2^{131}(j+4)^2\delta_j^{-5}N_j^\#\|X\|.
$$
固定参考也有 $\int|\kappa_{0,\Gamma^0}|<2^{60}(j+4)^2\delta_j^{-5}$。
于是完整预算仍满足原来的较宽门
$$
 \int_I\|\mathcal A_H-\mathcal A_{0,\Gamma^0}\|dt
 <2^{256}(j+4)^3\delta_j^{-5}N_j^\#\|X\|.
 \tag{F.11}
$$
两个独立 mean 通过同一 $L_H,R_H$ 包含在内；并非只估高频
Volterra 部分。固定参考的完整双向
$K_j^{\rm st}=2^{512}(j+4)^5\delta_j^{-10}$ 已在整个参数盒一致
证明。因此其 interaction picture 和完整前缀/深尾和与原
(S.29)--(S.31) 相同，证明 (F.1)。

实际 ordinary/weak 源继续使用该篇 (S.32)--(S.40) 的全部真实
密度、两个 mean 行、法向端点负荷。改变齐次参考并没有改变
真实 source 的单位，也没有授予未支付的裸弱源端迹。

## 4. 两端一张共同角图同时准确对齐两条真实射线

在完整负分量上记
$$
 S_i^0=\int_{I_i}q_{\Gamma^0}\,dt=-\omega_i/8,\qquad
 K_{i,-}(\theta)=h_i(4\theta)/4 .
$$
这里取已固定的真实 lift，故不是只模一个周长的等式。
令 $F_\pm$ 是 (K.13) 的实际两条从左到右的流，准确定义
$$
                      K_{i,+}=F_+\circ K_{i,-}\circ T_{S_i^0}.
 \tag{F.12}
$$
由 $F_-^{-1}F_+\circ K_{i,-}
 =K_{i,-}\circ T_{-2S_i^0}$，直接得到
$$
 \boxed{\qquad
 F_+\circ K_{i,-}=K_{i,+}\circ T_{-S_i^0},\qquad
 F_-\circ K_{i,-}=K_{i,+}\circ T_{+S_i^0}.
 \qquad}                                                    \tag{F.13}
$$
两端各是一张共同的 degree-one 图，没有分别替两条支选两个
不一致的物理端角。用 $H_\sigma^0$ 的同一密度规则，
完整 principal 的两行都与固定径向参考对齐，而非只对齐一个
瞬时速度或一个平均角。

逐行 KAM 修正和给
$$
 \|K_{i,-}-\mathrm{id}\|_{\mathcal A_{3/8}}
 +\|K_{i,-}'-1\|_{\mathcal A_{3/8}}
 <2^{19}{\varepsilon_i\over\gamma_i^{\rm D}}\bar a.
$$
因为全部实际 flow 相对于参考平移的完整位移和导数已付，
再用 (F.8)，其像仍在宽 $3/8$ 内部。宽 $1/4$ 上两端统一可取
$$
 \boxed{\quad
 \|K_{i,e}-\mathrm{id}\|_{\mathcal A_{1/4}}
 +\|K_{i,e}'-1\|_{\mathcal A_{1/4}}
 <k_i,\qquad
 k_i=2^{24}{\varepsilon_i\over\gamma_i^{\rm D}}\bar a .
 \quad}                                                     \tag{F.14}
$$
具体地，(K.24) 的和给每个标准圆位移及其一阶导小于
$2^{18}\varepsilon_i(\gamma_i^{\rm D})^{-1}\bar a$；
从宽 $3/2$ 标准圆换回物理角，位移只改善。右端用已付两流
复合，所有因子乘起来小于16；显示常数仍留余量。
两个端图都从已存在的实际 KAM 输出定义，不另外选择相位。

端高度和 raw conormal 通量必须准确使用
$$
 h_e^{\rm new}=h_e\circ K_{i,e},\qquad
 p_e^{\rm new}=K_{i,e}'\,p_e\circ K_{i,e}.
 \tag{F.15}
$$
对偶 pairing 及通量 mean 保持；高度 mean 按新角实际积分。
如果还微分 $K_{i,e}$，必须保留位移导数乘 $h_\theta$ 和密度
Jacobian 导数，不能因 (F.14) 很小就删去这些整行。

## 5. 实际度量反调从标签二阶开始

这一点由完整 mean，而非由一条旋转数的形式假设得到。
在 $a=0,\Gamma=\Gamma^0$ 处线性化全标签解，写其第一变化为
$(P_1,K_1,U_1,V_1)$。准确 $P=h_\theta/(aw_{\rm ref})$、
$U=P_\theta,V=K_\theta$ 给
$\langle P_1\rangle=\langle U_1\rangle=\langle V_1\rangle=0$。
同一 holonomy-one 小根给 $\langle K_1\rangle=0$，因为其完整
被积式的一阶平均为 $w_{\rm ref}^2\langle K_1+U_1\rangle$。
于是
$$
 d_1=E(V_1-P_1),\qquad v_1=-E(K_1+U_1),\qquad
                    \langle d_1\rangle=\langle v_1\rangle=0 .
 \tag{F.16}
$$
两条参考流是实平移，故每一条真实流的第一变化都是
$-d_1-\sigma q_0v_1$ 沿该平移积分，其圆周平均为0。
逆流和两流复合的第一变化只增加平移，仍保持平均0。因此
$$
                         \langle D_af_i(p=0,a=0)[b]\rangle=0
                         \quad\text{对每个完整标签方向 }b .
$$
零标签时 $f_i(p,0)=0$ 对整个参数盘恒成立，故
$D_pf_i(p,0)=0$。对联立 KAM 方程一次微分并取平均，准确得到
$(D_ap_i^*)(0)=0$，进而
$$
                              D_a\Gamma^*(0)=0.            \tag{F.17}
$$
没有把非径向瞬时波速的非mean一阶部分删掉；它在 cohomological
解的角图中完整保留，只是不会产生一阶标量参数修正。

参数 map 全纯。沿任意标签的复直线应用二阶 Schwarz 引理，
利用前篇完整行界，得到有真实单位的二阶强化
$$
 |\Gamma_i^*(a)-\Gamma_i^0|
 <2^{-14}{\varepsilon_i\over\kappa_i}\bar a^2 .
 \tag{F.18}
$$
若 $\|a\|<A_*/2$，对以 $a$ 为中心、半径 $\|a\|$ 的复方向盘
再作一次 Cauchy，亦可取
$$
 |D_a\Gamma_i^*(a)[b]|
 \le8\left(2^{-14}{\varepsilon_i\over\kappa_i}\right)
                         {\|a\|\,\|b\|\over A_*^2}.
 \tag{F.19}
$$
这是明确分级的系数导数，不是粗 Sobolev 裸 pullback 的无损耗
算子解析性结论。整个最终目标的第一变化在零标签处为0；
固定初始度量的 Jacobi 方向因此准确保留。

## 6. 接口仍保留的真实问题

(F.13) 给相邻正型分量可直接消费的真实两端角。每个正型 DN
应同时在其左右端采用这两张已确定图，保留完整非对角耦合、
mean 高度差和通量负荷。此坐标对齐不会自动证明真实高度/flux
振幅的整个网络反馈可逆；那仍要把完整根 Airy 和正型双端
散射算子接到同一个归一化空间。

对最终 nonlinear regular 方程，如果让 $\Gamma=\Gamma^*(a)$
随构造变量变化，其导数仍产生真实 metric-source。
(F.17)--(F.19) 说明其零阶消失和准确大小，不允许把该源永久
设为0。有限 connector 的实际第四方向、停止点、物理尺度和
外帽全部边界行仍按所选最终度量处理。

[实际参数势和全部端相位预算程序](../scripts/fourfold_KAM_fixed_reference_20261113.py)
及[完整报告](../notes/2026-11-13-R119-KAM-fixed-reference-budget.json)
给出 (F.5)--(F.11) 的全系数和全空间费用；没有沿用未经改变
profile 核对的旧参数数值。
