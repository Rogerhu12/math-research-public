# R618 当前固定 E 到 R579 宏观核心的实际接口

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。

**状态：已核源码事实与下面的核心变量恒等式；尚无新的科学运行或宏观连接解。**
本条消费已证[R579](../results/R579-smooth-thick-rounded-core-with-exact-perimeter-and-macro-budget.md)，不重证其支撑、周长或 reach。
正在运行的 actual397 分拆范围保持冻结；以下后继必须先消费它的真实自然终态。

## 1. 当前锁定什么，τ改变什么

来源是[完整模型](2026-11-27-r618-complete-growing-post-fixed-metric-model.md)、
[actual397范围](2026-11-27-r618-actual397-first-fixed-E-response-scope.md)及
`scripts/r618_growing_post_fixed_metric_height_20261127.py` 的构造器、
`_core_linear_directions/core_trace/height_jets/_complete_radial_data`。

固定目标 SHA 是
`86da8c603f3d7ed9eb928481f0afe492f10bb209c94bf0ccaf8070c1aa1cd6c5`。
原1130q、$H=q_0=.5188903877153482$、$\varepsilon=10^{-5}$、
$R=17/20$、$r_c=11/50$、中央半高 $1/25$ 和完整 $E_*(r)$ 均属于该身份。
后来普通优化的 q/H 不能回写它；H控制原 $W_*$ gain项。

实际高度仍允许同 $E_*$ 下的均值响应：$p_0=-W_*+s$，
$h_0-h_{0,*}=\int_{r_c}^r s(t)dt$。上帽锚固定，中央柱和反射中心按完整积分同移；
冻结参考 H 不等于把当前核心高度或整个均值函数冻结。

记原核心缺口 $\Delta_*=T(P_{0,*})-P_{1,*}$。源码准确采用

$$P_1=T(P_0)-(1-\tau)\Delta_*,\qquad 0\le\tau\le1.$$

τ只消除这个核心缺口；τ1不是放大幅度。当前硬τ1输入的其余1472响应为零。
更关键的是 `core_free_modes=4,6,...,J`，旧1129响应也从原 q 的索引1开始；
`_core_linear_directions` 没有任何原 j2 核心自由列。因此整个当前响应空间严格保持

$$P_{0,2}=-3\varepsilon/R=-3/85000.$$

新增 tail/compact 虽有 j2，但在核心邻域消失，不能改变此数。
现有高频核心列可以变大；这不等于已能指定 R579 的完整核心谱。
直接改构造参数 amp 会改冻结参考，不能称同 $E_*$ 放大。

## 2. 已有匹配尺度的宏观目标及其核心变量

R579 已给一个固定 $C^\infty$ 严格凸中心对称曲线 $\Gamma$：
周长准确 $2\pi R$，支撑 $A=1,B=.37$，核心 reach $>.075$，
中央高度 $|z|\le.04$ 的核心在球半径1.05内。
其完整闭面条件预算为 ball1.05、strip.37、reach.063、固定帽半径.22；
若连接和全部点对另付，即给 $\delta_{\rm hold}/D\ge.3$、
握持直径比 $\ge22/105$、reach比 $\ge.03$。
条件不移交当前 body。

令 $\phi$ 是 R579 外法线角、$\rho(\phi)>0$ 是其式(7)曲率半径，定义

$$
\theta(\phi)=R^{-1}\int_0^\phi\rho(v)dv,\qquad
u_\Gamma(\theta)=\rho(\phi(\theta))/R,
$$
$$
e_\Gamma=\langle u_\Gamma^2\rangle_\theta,\qquad
P_\Gamma=(u_\Gamma^2-e_\Gamma)/2.                 \tag{1}
$$

这里所有均值为连续均值。$P_\Gamma$ 零均值，且换元直接给
$\langle1/u_\Gamma\rangle_\theta=1$，所以 R618 同一个核心根满足
$e(P_\Gamma)=e_\Gamma$。核心 $q=f_\theta\to0$、$N\to1$，因而
$\psi_\theta=1/u_\Gamma$、$Y_\theta=R(\cos\psi,\sin\psi)$。
取 $\psi=\phi+\pi/2$ 即与 $\Gamma_\phi=\rho e_\perp$ 完全吻合。
固定中心和平面方向后，(1)给同一条 R579 曲线，未改变 $R$ 或核心周长。
反射对称给正偶余弦展开。

这里的方向已由现有 canonical 规范固定，并未引入一个可调积分常数。
已发 `r618_fixed_metric_numerical_chain_20261127.py:position_state` 使用
$\psi=\theta+\pi/2+\Pi(a-1)$、$Y=\Pi(bT)$；其核心极限为 $a=1/u_\Gamma,b=R$。
R579 的 $\rho$ 是偶函数且为 $\pi$ 周期，故从 $(A,0)$ 即 $\phi=0$ 开始的
$\theta(\phi)$ 为奇映射，并有 $\theta(\phi+\pi)=\theta(\phi)+\pi$。
于是 $g(\theta)=\phi(\theta)-\theta$ 是奇、$\pi$ 周期、零均值函数，且
$g'=1/u_\Gamma-1$。唯一的连续零均值 primitive $\Pi_0$ 因而满足
$\Pi_0(1/u_\Gamma-1)=g$，上述源码规范准确给 $\psi=\phi+\pi/2$。
又 $\Gamma(\theta+\pi)=-\Gamma(\theta)$，所以其材料均值也为零，
从而 $Y_{\rm canon}=\Pi_0(RT)=\Gamma$，无需另作平面旋转或平移；
支撑点 $(A,0)$、条带 $|y|\le B$ 与圆帽材料角处于同一方向约定。
这是连续 $\Pi_0$ 的恒等式，有限矩阵 $\Pi$ 的零模、Nyquist及其余 alias 误差仍须支付，
不把离散 primitive 的数值输出当作该连续核心或全连接的认证。

任意其他周长 $2\pi a_0$ 的目标须先缩放 $R/a_0$ 才能这样接入；
R565 原尺寸不能直接借用；R579 不需缩放。
但它的完整 $P_\Gamma$ 不是当前有限 J 的已付系数表；角反函数、完整谱与截断误差
必须按同一固定函数评价、加密。R579 的小圆滑参数 .001 也不保证 $u_\Gamma$ 或
$e_\Gamma$ 接近1，不能从 amp 很小推得宏观目标仍在旧数值小盒内。

## 3. 最小新控制与硬总 trace 的区别

在真实τ1解 $z_*$ 得到后，一个最小同目标后继是追加

$$\varepsilon c_2\chi_c(r)A_c(r)\cos2\theta,
\qquad A_c(r)=-\int_r^R W_*^{-1}(t)dt.$$

其核心增量为 $\delta P_{0,2}=\varepsilon c_2$、bare $\delta P_1=0$；
完整从属 correction、隐式 $\zeta,\zeta'$ 和所有2J项照 R618 共同更新。
$c_2=0$ 必须准确嵌回真实 $z_*$。例如硬定 $c_2=-3/R$ 给首谐波加倍的明确下一输入，
τ仍硬1、所有旧响应保留。它是有限设计延续步，不是宏观成功保证。
不能让新增 c2 无约束消掉非圆项，再把回到圆面的低残差称放大成功。

若指定整个 $P_\Gamma$，则必须约束**总** $P_0$：原 q 的 j≥4 与新增 lift 都改变它。
仅给新增坐标填一次目标值，随后自由优化旧 q，会把核心目标改掉。
应对完整 `dpc` 线性关系消元，或令 lift 等于指定 trace 减 bare trace并完整微分；
不能漏旧参数的核心导数。有限谱目标向 (1) 加密时，完整2J从属项仍全部保留。

这需要新的 source/model 身份及实际消费链：当前 solver 硬检查1473维、只消元末τ；
组合方向、`height_direction/coefficient_fields/embed_response`、tail producer和缓存身份
均须明确接新维度与硬 trace。旧已发模块不就地改常数冒相同模型。

## 4. 同 E 继续分支，不能永久锁在参考中心小盒

当前 `r618_split_reference_model_20261127.py` 的 trial 盒以原 x=0为中心，
半宽不超过.2；原 `function_step_limit` 还使用 `width-abs(x)`。
但核心准确要求 $\zeta_R=(e(P_0)-e_{*,R})/2$。
宏观后不能假定这个值、或 body 的 $\lambda=s/W_*$，仍在原小盒。

真正后继应从已接受的分拆根中心建立重叠同支盒，保同一个参考 $E_*$，
在新盒重新支付完整正域和同符号均值导数。位置与 $s_r$ 必须消费同根；
不能仅增大根预算、重置 E 或忽略盒失败。失去正域或 $c_0\ne0$ 的分支条件时，
仍记真实未解，不能把数值小盒失败当宏观不可能。

## 5. 可选的准确局部零消费与未付工作

当前首硬τ1输入只有 $\tau K_c\Delta_*$ 非零，原 $K_c$ cutoff 在 $r\le.65$
准确为零。因此该前缀的高度六 jets与参考按定义相同，真实 $s=s_r=0$。
如果自然终态显示重复 trial 根是成本瓶颈，可在**参数结构与准确 cutoff**证明此恒等时，
消费本次已求参考目标的 `literal_reference_state`；位置仍照当前完整链评价。
不得以浮点 jets 恰相等、尾 underflow或旧 fine 合格代替这个触发条件。
非零 tail/body 响应后除非另有同样准确结构恒等，否则继续完整求根。
当前运行未使用此优化，全部已付费用保留。

首τ1成功、增加核心控制或得到离散 S 下降，都不自动支付原七类源误差、
全角/全径向 metric、真实高度定位、C²拼接、连接/帽/镜射跨片 reach和全域支持预算。
同固定 E、参数和范围的精化仍须真实下降。最终静态候选完整过门后，
才按已证 R33 相位构造把它的空间几何传到全时间；设计 trace 的变化不是该时间族。
