# R133 补篇：由已成径向权重得到完整帽误差的二次与四次积分包络

2026-11-15，visible-exact / newton_source。

**本篇证明新的解析消费规则，尚未执行新的数值消费者。** 对同一个实际物理帽解与同一个连续修补中心，六个已成径向加权解界给出全帽逐点包络。该包络的二次、四次积分可用闭式计算，分别支付原 formal residual 与完整二次非线性接收项。原 7908 个 Gram、97 维已知 signed 模型、RW 的权重和后验解界均只读；没有重新计算原积分、改未知中心或宣布新的 trace 门。

## 1. 同一个实际未知量与原参数域

固定 SA/SC 的连续修补中心 ac1/440866、原真实物理角、反射类和帽区间
$$
 I=[L,R]=[9/10,25/8],\qquad \ell=R-L=89/40 .
 \tag{CEB.1}
$$
角测度始终是归一化完整圆周测度。令
$$
 y(r,\theta)=W_*(\gamma,f)(r,\theta)-\widehat W(r,\theta),
 \qquad W=(B,C).
 \tag{CEB.2}
$$
这是物理 pair 的差；它不是 raw moving $Q$ 的差。原已知 physical conversion、真实 $\alpha$ 和 continuous repair 已经包含在 $\widehat W$ 与原 RW 对象中，不再乘入任何转换因子。

原 SA.1–3/M product 给出
$$
 \|\gamma\|_{A^0_\theta}<10^{-9},\qquad
 \|f\|_{\dot A^2_\theta}<2^{-60},\qquad
 \|y\|_{X_0}\le\rho=3\,10^{-6},\qquad
 \|P_\perp y_C(R)\|_{A^0_\theta}\le\zeta=9.9\,10^{-10}.
 \tag{CEB.3}
$$
这里 $X_0$ 是逐 signed Fourier 系数先取径向 supremum、再对频率及两个物理分量求和的原 joint Wiener norm。完整 $C$ mean 留在其中。$B$ mean 为零仅使用当前实际反射类的原身份，不推广至一般 parity。

后文分别使用两个已经定义的输入范围
$$
 \Gamma_{\rm full}=10^{-9},\qquad
 \Gamma_{\rm tail}=(128\,10^9)^{-1}.
 \tag{CEB.4}
$$
每个结论均以前置条件 $\|\gamma\|_{A^0}\le\Gamma$ 为准。在 selected affine 应用中，还必须满足 SA/SC 的真实 matching 条件
$\gamma=P_\perp(\Psi(Q_\delta(L))-\widehat W(L))_C$。
不能以待证的 trace 大小反推 tail 域资格。

原 selected 参数范围仍是 $|\delta|\le d=10^{-10}$。它改变已知左读出 $S_\delta$ 及已知左差；未知 body 始终是 (CEB.2)。原 intrinsic bump 不交本帽，不能由此改换 $\widehat W$ 或删去任何端点项。

## 2. 已成功小原件与完整权重

本篇直接消费以下不可变文本。所有路径均相对于当前 topic。

| 角色 | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| RW 完整实际科学结论 | a4d46696df6125524d7491cd1d4efde156794aee | 57702 | ec6e088f2d361b35c938eb94bfe78d284507376b4d859c7eadc44c2635316ca9 |
| RW 完整 process | df608c6a12fb193106fba64fb23fd7afad37de29 | 16350 | daabac142b01e886d7bf3e3f9f53820cb6fb7c053e44a78972d4313ac4bb66e6 |
| 原 RW scientific source | a44357cfc1e8b5034a1daa587aff9bcaaf7d93ab | 31066 | f8d97a14aa7c2ebac746a9732e7b9fd00bf939db95b2b610edcd47f22f9388bb |
| SC3 完整实际科学结论 | a05d881b0b160299d39cb522ee88304a45b20af0 | 23672 | f0838341d4f661714328da407c9a45f7ef137c43e8ab1ca7f4adfc2b12e7893c |
| SC3 完整 execution | 34050b25b7197fb27d886b40c8f3366726e34f08 | 43738 | 9ce9955fade952563c6d2dc2ca7650b43a3752d3b10e9051a798ffd73fe2c5e9 |
| 原 SC3 scientific source | a3e2150166472fd5c08b5508cd30dda12be7836f | 44167 | 41b8f50cd7faafc438f37f3f4514caa24142af63d9921044d91ead67d6fcd1dd |

RW 前缀为
`notes/radial_weighted_cap_receivers_ci/run-43729429382-1-radial-weighted-cap-receivers/`，
科学原件名为 `actual-radial-weighted-cap-receivers.json`，过程为 `process.json`。
该次 child0、15 个完整门和六组后验门的成功保持冻结。

SC3 前缀为
`notes/signed_cap_affine_functional_ci/run-43754452928-1/`，
科学原件名为 `actual-scientific-conclusion.json`，过程为 `execution.json`。
该次 child0、20 门、7908 ordinary rows、32 slices、4 pilots、完整 97 维参数模型的成功保持冻结。
其实际说明为 blob
`09a8cf5fdb69d07b4592601b7389e8b053df830b`，
24004 B，SHA256
`3302361eb50e9345be6fce4f1374b4e304b4b4a1741d756281e92b113d7c0ae6`。

数学入口为：
[SA](R133-supplement-signed-physical-cap-affine-and-complete-adjoint-receivers.md)
SA.1–3、13、16、20–25，
[SC](R133-supplement-exact-radial-subtraction-and-complete-known-cap-affine-moments.md)
SC.22–25，
以及
[RW actual](R133-supplement-actual-radial-weighted-cap-and-complete-left-receivers.md)
RA.3–4。SA 的完整身份是
`f7db2f18230e62d216f8a901b990bfd9e6d703c0` / 23561 B /
`85e07aba2d895c160be6c307da9ff0740fb817bbad6f3813d0acf3242e0f35d1`；
SC 为
`0e2fcd353d8c6c2274633d7e052f645f0d9bf534` / 20669 B /
`927c3ba2ada01e1a571ce4d180c7d1e41ac25b1dda273cc6aef90511d40b9583`。

对每一个已通过的
$$
 \kappa\in\{1/16,1/8,1/4,3/8,1/2,3/4\},
$$
原权重在整个 $I$ 上准确为
$$
 w_\kappa(r)=\exp\!\left(-\int_L^r\lambda_\kappa(s)\,ds\right),
 \quad w_\kappa(L)=1,\quad
 0\le\lambda_\kappa(r)\le a_\kappa .
 \tag{CEB.5}
$$
$a_\kappa$ 读取
`new_weighted_candidates[kappa].complete_kernel_bounds.lambda_max`。
原 producer 的 `weighted_kernel` 将它定义为全 949 reference rows 的
`exact(max(profile))`；不是局部右输出段的速率。

同一完整 row 的后验结论给
$$
 X_{w_\kappa}(y)\le X_\kappa(\Gamma)
 :=x_{\kappa,0}+x_{\kappa,\gamma}\Gamma ,
 \tag{CEB.6}
$$
其中两个原系数分别读取 `posterior_bounds.Xw_affine`、
`posterior_bounds.Xw_gamma_gain`。完整 $w_\kappa(R)$ 读取
`new_source_and_output_integrals.weight_R`。必须保留同一 row 的
`complete_weighted_posterior_applies=true`、
`candidate_failure=null`、两 mean 分母与 physical nonmean curvature 输入身份。

这里使用的是已成实际解的 joint Wiener 后验界。没有把原 Wiener
$\ell^1$ operator norm 免费提升成 Hilbert pair-sum operator norm。
原数据中的 `right_body_inverse_weight_square_integral` 仅属于
$[9/10,19/20]$，不用于本篇的 whole-cap 积分，也不按区间比例扩张。

## 3. 全帽逐点包络

由 normalized Fourier 展开与 (CEB.6)，对每个 $r,\theta$，
$$
 \begin{split}
 |y(r,\theta)|_{\mathbb R^2}
 &\le |y_B(r,\theta)|+|y_C(r,\theta)|\\
 &\le \sum_j|\widehat y_{B,j}(r)|
       +\sum_j|\widehat y_{C,j}(r)|
 \le {X_\kappa(\Gamma)\over w_\kappa(r)} .
 \end{split}
 \tag{CEB.7}
$$
原 $X_0$ 存在球同时给 $|y(r,\theta)|_{\mathbb R^2}\le\rho$。
而 (CEB.5) 给
$$
 w_\kappa(L+t)\ge e^{-a_\kappa t},
 \qquad 0\le t\le\ell .
 \tag{CEB.8}
$$
故整个真实帽上有同一个 scalar 包络
$$
 |y(L+t,\theta)|_{\mathbb R^2}\le
 m_\kappa(t):=\min\{\rho,X_\kappa(\Gamma)e^{a_\kappa t}\}.
 \tag{CEB.9}
$$
特别，$\|y(L+t,\cdot)\|_{L^2_\theta(\mathbb R^2)}\le m_\kappa(t)$。
这些不等式含所有 signed 频率与实际 mean，不需要 $\sqrt2$、
$\sqrt{97}$、角长度或新的 moving-to-physical 转换费用。

式 (CEB.9) 仅用 whole-cap 速率上界与已成同态解界。
它没有求解新 PDE、重建未知解、改写旧权重，或声称真实未知解在
旧存在球之外仍满足 rational nonlinear 公式。

## 4. 二次、四次普通径向积分的准确闭式

对任意 $p>0$ 定义
$$
 J_p(\rho,X,a;\ell)=
       \int_0^\ell \min\{\rho,Xe^{at}\}^{\,p}\,dt ,
 \qquad \rho,X,a,\ell\ge0 .
 \tag{CEB.10}
$$
这里只需 $p=2,4$。积分是普通真实 $dr=dt$，没有重新归一化径长。

边界情形准确为
$$
 \begin{array}{ll}
 J_p=0,&\rho=0\ \hbox{或}\ X=0\ \hbox{或}\ \ell=0,\\[2mm]
 J_p=\ell\min(\rho,X)^p,&a=0,\\[2mm]
 J_p=\ell\rho^p,&X\ge\rho .
 \end{array}
 \tag{CEB.11}
$$
剩下的 $a>0$、$0<X<\rho$ 情形，令
$$
 t_*={\log(\rho/X)\over a},\qquad
 h=\min(\ell,t_*) .
 \tag{CEB.12}
$$
由于 $Xe^{at}$ 单调，
$$
 \boxed{\displaystyle
 J_p=X^p\,{\exp(pah)-1\over pa}+\rho^p(\ell-h).}
 \tag{CEB.13}
$$
证明是将积分在 $h$ 处分成指数段和常数段。若 $h=\ell$，
第二项为零；若 $h=t_*$，首项也准确等于
$$
                 {\rho^p-X^p\over pa}.                 \tag{CEB.14}
$$
两种式子在 $t_*=\ell$ 处相同。$a=0$ 及 $X=0$ 用 (CEB.11)，
没有除零或取 $\log0$。也可从积分本身取这些连续极限。

从 (CEB.10) 立即得到
$$
 0\le J_2\le\rho^2\ell,\qquad
 0\le J_4\le\rho^2J_2\le\rho^4\ell .
 \tag{CEB.15}
$$
$J_p$ 对 $\rho,X,a,\ell$ 均单调不减；故在未来向外算术中，
对同一对象使用各参数的合法非负上界仍给合法上界。

令
$$
 Y_{2,\kappa}=\sqrt{J_2(\rho,X_\kappa,a_\kappa;\ell)},\qquad
 Y_{{\rm quad},\kappa}=
                 \sqrt{J_4(\rho,X_\kappa,a_\kappa;\ell)} .
 \tag{CEB.16}
$$
$Y_{\rm quad}$ 是“四次积分的平方根”，不是通常的 $L^4$ norm。
由 (CEB.9) 和归一角测度，
$$
 \|y\|_{L^2(I\times\mathbb T;\mathbb R^2)}
       \le Y_{2,\kappa},\qquad
 \big\||y|_{\mathbb R^2}^{\,2}\big\|_{L^2(I\times\mathbb T)}
       \le Y_{{\rm quad},\kappa}
       \le\rho Y_{2,\kappa}.
 \tag{CEB.17}
$$
这是对同一完整未知函数的两个相关范数界；不把它们当作独立随机误差平方相加。

## 5. 直接消费原 formal 与完整 nonlinear 接收范数

对每个原 97 维单位测试输入 $\xi$，SA.13、16 的准确 body 项为
$$
 {\cal E}_{\xi,{\rm body}}(y)
 =\int_I\langle r_{\xi,0}^*,y\rangle_\theta\,dr
       -\int_I\langle q_\xi^*,{\cal R}_Q(y)\rangle_\theta\,dr,
 \qquad
 q_\xi^*=-\gamma_{\rm rad}z_{\xi,B,\theta}+\beta z_{\xi,C}.
 \tag{CEB.18}
$$
这里 $q_\xi^*$ 的第二项保留完整 $C$ mean。
SC3 已成小结论直接提供
$$
 \sup_{\|\xi\|_{97}\le1}\|r_{\xi,0}^*\|_{L^2}\le D,\qquad
 \sup_{\|\xi\|_{97}\le1}\|q_\xi^*\|_{L^2}\le Q .
 \tag{CEB.19}
$$
它们分别是
`unchanged_unknown_operator_bounds.unweighted_formal_ordinary_norm`
与 `complete_q_star_norm`。这些字段已经是完整 norm，
不再次取平方根、不补一个旧 Hessian Gram，也不从整体 Gram
按新的径长比例截取部分。

原 SA.22 的点态 rational 余项完整满足
$$
        |{\cal R}_Q(y)(r,\theta)|
                    \le13|y(r,\theta)|_{\mathbb R^2}^2,
                    \qquad |y|\le\rho .
 \tag{CEB.20}
$$
该定理使用原 $|v^\flat|<6$、$|u^\flat|<1/50$、
$|K(v^\flat)^2+(u^\flat)^2|<2$ 以及原 $\rho$；
本篇不重新计算该 rational 导数。
由 (CEB.17)，
$$
 \|{\cal R}_Q(y)\|_{L^2}\le13Y_{{\rm quad},\kappa}.
 \tag{CEB.21}
$$
在 (CEB.18) 对同一个 $\xi$ 分别用 Cauchy–Schwarz，再取输入
Euclidean 单位球上的 supremum，得到新的完整 97 维 body 费用
$$
 \boxed{\displaystyle
 E_{{\rm body},\kappa}
       =D Y_{2,\kappa}+13QY_{{\rm quad},\kappa}.}
 \tag{CEB.22}
$$
同时
$$
 E_{{\rm body},\kappa}
 \le(D+13\rho Q)Y_{2,\kappa}
 \le(D+13\rho Q)\rho\sqrt\ell .
 \tag{CEB.23}
$$
因此这是原存在球 body 费用的合法完整替代。它不以 known signed
模型的大小代替未知 body 项，也不假设完整误差为零。
原 SC3 posterior 的 body 正是 $(D+13\rho Q)Y$；本篇没有额外
$E_0$、没有改变其中心，也没有新增未知 Hessian 假设。

## 6. 左端、外端、known 模型与完整候选

仍取同一 $\kappa$、同一 $\Gamma$ 的完整 $X_\kappa$ 和
$w_\kappa(R)$。由 $w_\kappa(L)=1$ 和原存在球，左端本来有
$$
 Y_{L,\kappa}=\min\{\rho,X_\kappa\}.
$$
在 SC3 selected 左读出中使用的完整费用仍是
$$
 Y_{L,\kappa}^{\delta}=Y_{L,\kappa}+10d,\qquad
 Z_{R,\kappa}=\min\{\zeta,X_\kappa/w_\kappa(R)\}.
 \tag{CEB.24}
$$
$10d$ 是原已知物理左差费用，保留在左端。它不加入 body 包络，
不被当作未知 body 的重新定心，也不从 (CEB.16) 的积分界反推端点值。

直接复制 SC3 原 complete
$E_{L,\delta},E_R,Z_B,Z_m$，以及原实际 outer Lipschitz
$L_D=.006,L_m=.00075$。原 Hermite 试件的所有 internal value jump
已经准确为零；若改试件或改接缝，就必须恢复 SA.22 的全部 jump 项。
对当前同一试件，完整未知费用为
$$
 E_\kappa(\Gamma)=
 D Y_{2,\kappa}+13QY_{{\rm quad},\kappa}
 +E_{L,\delta}Y_{L,\kappa}^{\delta}
 +(E_R+L_DZ_B+L_mZ_m)Z_{R,\kappa}.
 \tag{CEB.25}
$$
令 $B_{\rm known}$ 是 SC3 已成完整 selected signed 参数模型的
uniform norm，含原数值误差、三阶参数余项和已实际算入的 known 项，
但不含下一句另列的外端缺项。原字段为
`complete_error_accounting.uniform_known_parameter_model_norm`。
令 $B_{\rm out,known}$ 直接读取
`complete_outer_omission_norm`。它已经包含修补中心 A.15 的
$r_{D,+}=1.3\,10^{-15}$ 和 $r_{m,+}=2.05\,10^{-19}$，
以及完整外端 $B/C$ mean readout；不改用未修补中心的更小值，
也不把这份外端缺项重复加进模型。

于是每个完整 weight 都给
$$
 \|b_\delta^f\|_{97}
 \le A_\kappa(\Gamma):=
           B_{\rm known}+B_{\rm out,known}+E_\kappa(\Gamma).
 \tag{CEB.26}
$$
$b_\delta^f$ 始终是 SA.25/SR 的完整 inner $B$ 加 $C$ mean 的
同一个 affine source。原 height 球、实际 $\gamma$ trace 条件与
selected $S_\delta$ 均未改变；已对整个原 $f$ 球统一的 outer 缺项
不再次加同一个 height 变化。

可对完整候选取
$$
 A_{\rm new}(\Gamma)=
 \min\{A_{\rm SC3,old}(\Gamma),
                  A_\kappa(\Gamma):\kappa\hbox{ 为六个已通过权重}\}.
 \tag{CEB.27}
$$
$A_{\rm SC3,old}$ 是该域原 SC3 的完整已成 posterior 行，逐字复制。
选择比较的是同一个真实 $b_\delta^f$ 的整行上界。
不能从不同 weight 逐项选择未闭合的 $\chi$、kernel 或
feedback 分母，再拼成新解界。本篇每个候选都先完成同一 weight
的全式 (CEB.25)，然后才应用 (CEB.27)。

原 SC3 两域的 selected prior 都是 weight $3/4$，其中 body
仍使用 $\rho\sqrt\ell$ 的存在球分支；其 known 模型约为
$3.8444\,10^{-13}$，而旧完整 posterior 约为 $1.6173\,10^{-7}$。
这只是说明当前可改进的项在何处，数字均来自已成原记录；
本篇没有计算或宣称新的 $A_{\rm new}$ 值。
式 (CEB.27) 保留旧完整行，所以新的向外数值宽化也不会迫使消费者
输出比旧已成上界更差的结论。

## 7. 最小新消费者的输入与输出合同

下表限定未来唯一新目标；本篇没有执行它。

| 输入 | 已存字段及用途 |
|---|---|
| RW science / process | 同候选 ac1/440866、原 full physical product、child0/15 门、六个通过 row 的完整身份 |
| 每个 RW row | 两个 $X_\kappa$ affine 系数、whole-cap `lambda_max`、完整 `weight_R`、原 mean/type flags |
| SC3 science / execution | child0/20 门、完整 7908/32/4 与 97 模型身份、旧结果和原 source/helper/reader/manifest identities |
| 原 body 常数 | $D,Q$ 已经是 norm；所有完整 $C$ mean 及 formal/Hessian 区分 |
| 原 endpoint 常数 | $E_{L,\delta},E_R,Z_B,Z_m$、$10d$、outer 域和全部 mean |
| 原 known 结论 | $B_{\rm known},B_{\rm out,known}$ 与每个 $\Gamma$ 的旧完整 posterior 行，直接复制 |

仅以下算术是新目标：必要时把同一已存 affine 系数代入两种
$\Gamma$；按 (CEB.11–16) 计算每个 weight 的两个完整积分；
再计算 (CEB.25–27) 的整行费用。它们是新的有限标量组合，
不是重新生成原 RW 系数、权重积分、旧 Gamma 后验或 signed 97 模型。

未来输出至少完整保存两域各六个 weight 的
$X_\kappa,a_\kappa,w_\kappa(R)$、采用的闭式分支、
$J_2,J_4,Y_2,Y_{\rm quad}$、三类未知费用、
完整 $A_\kappa$、旧整行及最终整行选择。
若旧小结论已经保存同域完整 $X_\kappa$，应直接读该原球；
否则明确标记本次仅由原两系数作新的 affine scalar evaluation。
不将原已丢的临时 comparison audit 冒称已恢复或已读取。

有向实现必须先锁定合法非负参数上界，再评价完整闭式。
若球不能决定 crossing 分支，应使用覆盖两个分支的区间计算、
等价的安全积分上界，或回到完整 $\rho^p\ell$；
不得以 midpoint 选择分支。除法须用完整球或严格正下端，
不能把 upper 分母直接当作上界除数。
零输入按 (CEB.11) 单独处理；所有平方和的非负性与有限性在开方前
明确核验，取上端后再开方。失败保留完整诊断和此前已成新小标量，
不能因为展示或包装失败重算一个已经成功的科学目标。

所需旧数学资料均为上述小文本；不恢复原 36 个 archives、
候选 NPZ、7908 行数组或失去的 transient 权重 profile。
原实际 complete source、Grams、Hessian、repair、mean、
flow、Riccati、Green 和 successful scalar consumers 的重算次数为零。

## 8. 结论范围

(CEB.22) 是同态物理未知量的一个新完整 body 接收界，
(CEB.26–27) 是同 97 维 affine source 的完整 posterior 候选。
归一角测度、普通全径长、完整 mean、真实 endpoint、
原 selected-left 变化和 outer height 域均保留。

这些公式不证明新的 core 解、low trace 自映像、完整 incoming
逆、finite border、waist 或 high body/cut 门；也不把尚未计算的
新候选值记录成已成功的小结论。所有这些独立输入继续按原
SA/SC/SR/VR 的完整同态合同消费。
