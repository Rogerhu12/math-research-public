# 首次新输入：全 W 可逆斜率权坐标中的六个同 f 原 NS/PS 余子式

- 会话：Astra-ISP-8542378f-20261127。
- 日期：2026-11-28（UTC）。
- 状态：未执行。没有预记新多项式非零、几何次数下降、权次数改善、有限性或排空。
- 源：2026-11-28-unit211-W-inverse-weight-six-small-same-f-NP-original-cofactors-8542.py。
- Git blob：cf6d6f1e31c6c324ac9eea2a5ec179fe70530df0。
- SHA256：758d461e6ce8869e3ff08fc395403f98cce27a1322329e793b21b1bdfb80e131。
- 15990 字节；自含、零依赖；唯一首次 180 秒、4 GiB。

## 1. 原范围和真正的新目标

本输入在整个当前已刊 W 权图中工作，保原 singleton 值互异和物理 $D\ne0$ 的原范围。这里 $T$ 是自由几何变量，**没有施加 $b_0=0$，也不倒置 $\nu+2$ 或 $A_*$**。

新目标是：对真正原 weighted NS/PS 各构造三个同 $f$ 的标量余子式，完整返回全部六个原源；结合已经证明的六标量 $I_4$ 呈示，得到同一个完整 $I_6$ 的另一套纯 $(\lambda,T)$ 输入。原 $I_{11}$ 的其余条件仍保留。

本次不重建原 $g$ 的显式大系数，不跑旧 b1 六标量门、全 c0 十一式门、五个 adjugate 三次门、整 b0 的六个固定结式或已冻结的 primitive PRS。只有原真 Gram、首一 $q_f$、三个原一次余式的必要定义前缀；新计算对象是六个尚未执行过的 NS/PS 同点 cofactor。

## 2. 权坐标覆盖整个当前 W

令 $u=e+1$、$V_b=uk+2$、$s=2u-1$，使用

$$
\nu=\frac{\beta}{u}=\frac{s(k+2)}{V_b},\qquad
\beta=2u-\frac JQ,
$$

以及

$$
d=u\nu-s,\quad r=s-\nu,\quad H_\nu=\nu^2-(u+1)\nu+s.
$$

完整正反身份为

$$
\begin{aligned}
d&=\frac{2s(u-1)}{V_b},&
r&=\frac{s(u-1)k}{V_b},&
k&=\frac{2r}{d},\\
Q&=\frac{2(u-1)r}{d},&
\ell&=\frac{uH_\nu}{r},&
m&=\frac{u\nu(u-\nu)}r,\\
\delta&=\frac{\nu(3u-2)-s^2}{d},&
\Phi&=-2(u-1)(\nu-1),&
J-Q&=-2(u-1)r,\\
T_0&=-\frac{2u(u-1)\nu(\nu-1)}d,&
\beta&=u\nu.&
\end{aligned}
\tag{1}
$$

这些是[新整 b0 输入中第 2 节的全 W 坐标部分](../results/R150-appendix-unit211-W-b0-inverse-slope-five-original-quadrics-six-weight-conditions.md)。该节的正反式本来不使用 $b_0=0$；只有它随后用 $\kappa=\ell/(\nu+2)$ 恢复 $T$ 的步骤限于 b0。本源不做该步骤。

$s$ 由既有 $J-Q$ 全支排除支付；$e,k,k+2,V_b$ 等沿当前 W 已付。因此 $d,r,\nu,\nu-1$ 都是原单位。源将 (1) 与旧 $\ell=u((k+2)^2-2ek)/(kV_b)$ 全部相互返回，不把任何新增权零面删掉。

另设新的小系数定义

$$
P_\nu=(3u-2)\nu^2-(2u^2+3u-3)\nu+(2u-1)^2.
$$

直接由 (1) 得

$$
P_{02}=\frac{2u(u-1)P_\nu}{d};
\tag{2}
$$

源同时核对其等于原 $(2-3u)V_2-Qu+2u^3$。式 (2) 只作更小参数定义，不新增单位或单独计算门。

实际检查分母时只准剥：原 $u,u-1,2u-1,d,r,\nu,\nu-1,\delta,M,\ell,m,P_{02},2\ell-1$ 的多项式分子支持。其中 $2\ell-1$ 明确引用[完整 Lhalf 排除](../results/R150-appendix-unit211-W-entire-Lhalf-complete-original-exclusion.md)，不能用先行的 F101 覆盖代替。任何不在这个列表中且不能由其准确整除剥尽的实际分母都会立即阻止对应结论。

另外，新的六个 cofactor 可合法使用[整个 G36 排除](../results/R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md)支付的旧纯权支撑。这里没有把未经支付的 raw $\det B$ 当单位。源只复制旧 36 项数学定义：

- 旧来源：2026-11-27-unit211-W-G36-whole-Q-six-original-thirty-six-column-return-8542.py。
- Git blob：c489948be8e967575417a1e21de51cd5a915dc80。
- 旧完整源 SHA256：3ec9b206da1dbde4103ebf7633e725e4cf5b8518055ac8f0945d7ba6a1e24a22。
- 36 项在五指数规范中的定义 SHA256：994fe0821fb8c70e7f82edf8aea19a17ee1ffa99fd5fd4b5b3c065daea84ad78。

本次先对旧定义核这个 SHA，再令

$$
\widetilde G(u,\nu)=G_{36}\!\left(u-1,\frac{2r}{d}\right).
$$

因旧 $k$ 次数最大为 8，完整原拉回身份为

$$
d^8\widetilde G
=\sum_{i,j}c_{ij}(u-1)^i(2r)^j d^{8-j}.
\tag{2a}
$$

源对 (2a) 直接乘回。$d$ 已由 (1) 支付，所以约消后的 $\widetilde G$ 分子确为同一旧原单位，可以加到新六式的剥除列表。没有重跑旧 G36 原曲线排除、因式或泛型矩阵，也不改已冻结 10ab 的支撑表。

完整 $I_4$ 的 $f+g$ 定理同样沿用这个旧 G36 单位；本次只用其已成纯权组合存在式，不展开 $g$。

## 3. 同点真 Gram 与 monic f 环境

保持 $T$ 自由，用原关系

$$
\begin{aligned}
G&=\lambda P_{02}-(1-u)T_0,\\
P_c&=QP_{02}(\ell+T)-GT_0,\\
t&=-\frac{P_ff+P_c}{bcQ\Phi},\\
V&=\frac{Jf-G+bcQt}{Q},\qquad W_1=T_0/2+2uf,\\
x&=\frac{(u-\ell Q)V-mW_1}{M},\qquad
y=\frac{\ell W_1-uV}{M}.
\end{aligned}
\tag{3}
$$

源在 $\rho^2=\delta$ 的整个二次代数中构建 $b,c,X,Y,r,s$ 与四维原 Gram；这里不倒置二次范数，权 $b,c$ 的实际组合通过已付 $bc=M/(4\delta)$ 表示。

真 dual 乘法严格是

$$
(vz)_1=v_0z_1+v_1z_0.
$$

独立 $E_1$ 用 $-2(d^2)_1=-4d_0d_1$，singleton 行另核含 $2pr$ 的完整表达式。新源不使用错误 compact E1，不偷用 $E_1=E_W$。

原四行记为

$$
F=(E_1,E_{B,e},E_{B,o},N_1).
$$

它们对 $(\lambda,T,f)$ 总次数至多二。原均值给

$$
q_f=c_f\left(E_{B,e}+\frac{\ell\delta}{m}E_{B,o}\right)
=f^2+q_1f+q_0,\qquad
c_f=\frac{bc}{2u(u-\beta)}.
\tag{4}
$$

$u-\beta=u(1-\nu)$ 已付。对 $j=1,3,4$ 的三个原式，减掉其纯权 $f^2$ 系数倍的 $q_f$，得

$$
r_i=A_i+B_if,\qquad
\deg_{\lambda,T}A_i\le2,\quad
\deg_{\lambda,T}B_i\le1.
\tag{5}
$$

实际四源向量为 $r_i=F_j-[f^2]F_jq_f$。由于 (4) 的 $E_{B,e}$ 系数为单位，$I_4=(q_f,r_1,r_2,r_3)$ 的双向来源沿已刊证明成立。

## 4. 原 NS/PS 只作一次短除

以同一 Gram 直接构造原 $N_4$ 与 $P_2$，并先核两个 singleton 的共轭身份。随后形成

$$
\begin{aligned}
NS&=bN_4(B)+cN_4(C)-2\lambda P_{02}(\ell+2T+A_\lambda),\\
PS&=bP_2(B)+cP_2(C)-P_{02}(\ell+3T+3A_\lambda+B_\lambda).
\end{aligned}
\tag{6}
$$

整个 $\rho$ 奇部必须实际为零，原几何总次数均至多三。对每个 $F\in\{NS,PS\}$，只用首一 (4) 作短除：

$$
F=Q_Fq_f+A_F+B_Ff,\qquad
\deg_{\lambda,T}A_F\le3,\quad
\deg_{\lambda,T}B_F\le2.
\tag{7}
$$

每一步短除均回乘，所有新分母逐个支付；没有原 $g$ 的高次代入，也不需要 $B_i$、$\Delta_B$、$A_*$ 等新头的逆。

新目标为每个 F 的三式

$$
H_{Fi}=A_FB_i-A_iB_F
=B_i(F-Q_Fq_f)-B_Fr_i.
\tag{8}
$$

它们对 $(\lambda,T)$ 的总次数至多四，且具有显示的完整六源向量。程序分别核整个原组合和每个 $f$ 系数，保证最终确实不含 $f$。本次不先假定 (8) 非零、没有共同因子，或实际只有三次。

## 5. 共同乘子取消保整零面

对每条 (8)，先取六个真实原乘子分母的 LCM；该 LCM 必须只由旧已付权单位组成。随后只除这六个乘子多项式共同的因子，再重新计算

$$
\widetilde H=\sum_{a=1}^6\widetilde\gamma_a F_a,
\qquad F_a=(E_1,E_{B,e},E_{B,o},N_1,NS,PS).
\tag{9}
$$

若共同因子为 $c$、清分母为 $d$，实际核

$$
c\widetilde H=dH.
\tag{10}
$$

因此即使 $c$ 在某个权或几何点为零，新 $\widetilde H$ 仍由 (9) 直接属于原理想；不是把原方程除以未知因子。之后只允许剥已付纯权支持，所有实际乘子再次完整返回。

若某原组合恰为零，准确记录零式，不把它解释为空。若出现未付分母或实际次数超过已证边界，则保留精确失败身份；不删检查、延时或重跑。

## 6. 六个新 cofactor 与原 I6 的精确关系

[三 pair、三同 f norm 的完整原 I4 呈示](../results/R150-appendix-unit211-W-three-pairs-three-same-f-norms-complete-original-I4-presentation.md)已从纯权四源的 $R=f+g$ 证明存在纯权 $v_i$，满足

$$
\sum_i v_iB_i=1,\qquad g=\sum_i v_iA_i.
\tag{11}
$$

该原恒等式可以沿 (1) 可逆换坐标，不需本次再计算 $g$。写 $P_i=A_i-B_ig$，以及

$$
P_F=A_F-gB_F.
$$

则完整恒等式为

$$
\sum_i v_iH_{Fi}=P_F,\qquad
H_{Fi}=B_iP_F-B_FP_i.
\tag{12}
$$

所以在既有完整 $I_4$ 理想上，加三个 $H_{Fi}$ 与加原 F 完全等价。对 NS、PS 同时应用，得到

$$
I_6=I_4+(H_{NS,1},H_{NS,2},H_{NS,3},
          H_{PS,1},H_{PS,2},H_{PS,3}).
\tag{13}
$$

源若按第 5 节得到 primitive 新核，(9) 给它们属于原 $I_6$；(10) 及只剥旧单位给原 $H_{Fi}$ 属于这些新核生成的理想。故 (13) 也适用于此次实际得到的 primitive 核。没有把三线性方程的 pair 相容性单独当成充分条件：旧三同 f norm 全部保留。

最终纯 $(\lambda,T)$ 模型仍使用已刊 $R=f+g$ 恢复同一个 $f$。此结构不要求任意六元或二元环境自由，也不删除 $B_i=0$ 的纤维。

## 7. 唯一首次的边界

源只预定执行上述六个新原 cofactor、其实际共同乘子取消与分母检查，输出参数定义、次数、字节数、SHA 和实际 checkpoint。不作任何新结式、因式、rank、模采样或 pure-u PRS。

在实际返回之前，权次数是否降低、六核是否非零及是否具有新的共同因子均未知。即使六核全部完成，也只登记原接口及其精确理想关系；原 $I_{11}$ 仍保留，不能直接宣称整个 W 已空或新增有限点数界。
