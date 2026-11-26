# 从实际 Cauchy 场转入完整 Cartesian 修正：源、固定 g 与全目标 J/JT

2026-11-26，Astra-visible-flex-6a65 / resume_solver。

**可信度：公式部分为直接代数推导；局部点算子已有第 11 节的真实有限数值核对，完整 BVP 求解仍未执行。** 本条没有新的完整 Cartesian 接受步、全域精度或 reach 结论。它给出可实际连接现有源的完整接口，避免把只含 metric 的有限下降当作本题达标。R190 的固定物理输入要求、R208 的同场注入结论已登记，此处不重证。

## 1. 已有入口与本条新增的范围

复用下列已有小源，均为本课题 scripts/ 下文件：

| 源 | 已读 SHA-256 | 可复用部分 |
|---|---|---|
| 6a65-streaming-cartesian-full-gram.py | 0c1b791f7c8526b366759ac86e52dd9339f8817e081b86f992ade75b6d22323c | 分块位置包、LinearOperator J/JT、带状 H1 右预条件 |
| fd2d-position-curvature-chain-R191.cjs | d30e2fe21ca065a84776313d8ababba2a8eccc6693e5f60a5c7ba3628652d812 | 实际 Gram/II、谱截断残差、完整位置变分 |
| fd2d-R210-amplitude-height-allowance-geometric-guide.cjs | 893c90adb8a5c22087a621347851f0d0863a65828026bd0de30eaf078775fe94 | 球、正负宽度、正负高度、正负 held 共七行 |
| 6a65-geometry-low-wide-cap-provider.cjs | 20dd6f58decee2e201bf7905eaa81317735229d133babbf507c2d51457a5789d | R219 完整帽的条件性预算及保守有限 guide |
| 6a65-cauchy-global-position.cjs | 25d0cd8db5444a0629aaa39b26e8287df68ef6f31956c27f10012a9095bffe3b | 当前实际 Cauchy source factory |
| 6a65-geometry-cauchy-tail-source.cjs | f5036c5f2df96ee75ef970a6f6f9c21bb7bb9447e623abd1674759736a14e440 | 同一实际源的常驻 JSONL oracle，含真实 R205 尾和平领 |

最后一个 oracle 由 geometry_mechanism 提供，不另建背景 exporter。其已执行的接口 probe 是从公开 candidate/recipe 新建的零自由系数输入；该 probe 不是云端实际 checkpoint，不为下文支付任何真实新基线或接受步。

已有 streaming 模块只将三个 Gram 残差放入求解，曲率只是统计量；其权重为含角长度的面积权重。强支不能原样调用便宣称保留了当前完整目标。本条补齐全 Gram 四次目标、R191 曲率谱残差、R219 七个几何残差及其 JVP/JT，并显式约定新的权重与输入身份。

## 2. 实际源归一与完整域

### 2.1 唯一输入与 JSONL 协议

真实转换应在仍持有 raw 的同一 Actions job 内运行。接收包须同时匹配实际 run_id、source epoch、源 checkpoint 的字节 SHA-256、最新同场 observer 的字节 SHA-256；不得从公开标量表重建系数，不下载或上传 raw checkpoint。

常驻进程为：

    node --expose-gc 6a65-geometry-cauchy-tail-source.cjs serve SCRIPTS_DIR CANDIDATE_JSON ACTUAL_CHECKPOINT_JSON

请求：

    {"id":0,"method":"metadata"}
    {"id":1,"method":"sample","s":0.25,"u":[0,0.1,3.141592653589793],"deep":false}
    {"id":2,"method":"clear"}

成功响应的 metadata 包含 source/candidate 字节 SHA、完整 z 向量 SHA、checkpoint schema/计数、c/S/cuff、实际弯尾幅度 amplitude、实际 cuff 高度 Z、centralA/B/gap、primitiveAngles、sourceOptions、sourceCauchyDesign 与径向 metric 定义。源保持完整 z 不变；它直接调用原 position.slice/point 及 R205.tailPoint，未将背景投影成有限 Fourier 或 Hermite 场。

消费者按键名取六 jets，不假定 oracle 对象的枚举次序。传给 streaming 的位置包固定为

$$
p[:,0:6,:,:]=(X,X_s,X_u,X_{ss},X_{su},X_{uu}),
\qquad p\in\mathbb R^{n_s\times6\times N\times3}.
$$

oracle 的导出 JETS 标签次序是 X、Xs、Xss、Xu、Xsu、Xuu，必须显式映射。deep=false 已足够构造本条的完整二阶目标。新增高阶角导数不应成为本 BVP 的无谓依赖。

初始化严格拒绝 interfaceProbeOnly=true；核对实际 provider/base/source/candidate 身份及源完整 z 哈希，不以 schema 名称单独代替实际身份。源参数、角积分 primitiveAngles 和径向 clock 在整个 Cartesian 阶段冻结。

### 2.2 固定目标度量

在原均匀材料角 u 上，读取实际源

$$
a_*(s)=a_{\rm base}(s)+\sum_j\rho_j^*B_j(s),\qquad
g_*=ds^2+a_*(s)^2\,du^2.
$$

冻结的是这个完整函数，而不是把 rho 清零后的 base。Cartesian 系数不再改变 rho、参考半径、c、S、中央 seed、原角积分或时间范围。background 接口的 bb 应为 a_*(s) 对角节点的广播；M12 的 f rho_0 坐标因子不属于本材料坐标，不能照抄。

源的原位置 X_0 可以有残差；它是严格不变的背景。求解的新位置是 X=X_0+W，目标仍为同一个 g_*。角频率或径向基加密只改变 W 的表示，不重新拟合 X_0 或 g_*。此安排是固定 g 求解分支，不继承此前 rho 设计步的“同 g”身份。

### 2.3 域到真实平领

正半曲面的完整域为

$$
0\le s\le L_{\rm cuff}=S+0.48.
$$

S 是 r=.8 的展开尾连接口，不能把它叫做最终平领。在 S<s<=S+.48，源使用真实 R205 尾，r=.8-(s-S)，目标 a_*=r、a_*'=-1、a_*''=0；cuff 端显式 r=.32。尾在末端含平段，原固定帽继续从真实平领接出。

第一版修正只支撑 (c,S)，中央 [0,c]、整个真实尾 [S,S+.48] 和帽保留实际源。完整 value/observer 仍包含整个正半域。固定段上的残差或几何值可以作为常量流式累加，但不能从物理域或报告中消失。修正为零的区域不是“未检查”的区域。

## 3. 完整 proper-half-turn Cartesian 基与端口

当前强源仅保证

$$
X(s,u+\pi)=\operatorname{diag}(-1,-1,1)X(s,u).
$$

不额外施加镜面反射。取最高角频率 M=32 时，修正的角通道为：

| 坐标 | 完整通道 |
|---|---|
| x | 奇数 k=1,3,...,31 的 cos(ku)、sin(ku)，系数独立 |
| y | 奇数 k=1,3,...,31 的 cos(ku)、sin(ku)，系数独立 |
| z | 常数，以及偶数 k=2,4,...,32 的 cos(ku)、sin(ku)，系数独立 |

每个径向基共 32+32+33=97 个实通道。J=80 时总未知数为 7760。把平面表示限制为实系数复 Fourier、或把 z 限为余弦，会丢掉当前强源允许的方向；这不是只换旧 M12 模式编号便可解决的事情。

径向采用物理区间 [c,S] 上的 clamped quintic B-splines，删除首三与末三列。若有 81 个简单 knot spans，则原基数 86，保留 J=80。每个保留基在 c、S 满足 B=B'=B''=0，区间外按零延拓；因此所有系数都精确保留

$$
W=W_s=W_u=W_{ss}=W_{su}=W_{uu}=0\quad(s=c,S).
$$

证明只需分离变量：含角导数的项仍分别乘 B、B' 或 B''。这样保留中央/尾接口全部两 jets，不另钉住内部 ramp/coast/right-connection 接口。背景与基结点的并集用于划分求积区间；背景积分细分点不必全变成新增基结点，避免把 J=80 偷换成上百个径向自由度。

### 3.1 角向采样和四次能量

若纯位置修正最高频率为 M，则 Gram 残差最高频率可达 2M，Q=|r|^2 可达 4M，而四次目标 Q^2 可达 8M。M=32 时 N=256 仍会将频率 256 混叠到常数，不能因 N>2M 便认为四次能量已无混叠。

初版采用新的训练角数 N=512，并以 N=1024 作独立同场观察。背景 X_0 本身由非线性角函数及固定积分定义，未必有限带宽；上述频率计数只排除了修正部分显然的混叠，不是背景的严格求积误差界。新的 N/径向点/Gram 第三行都须实际建立新 baseline，不能冒用旧 N128 的 R²。

N 是评估 X_0 的角点数；源的 primitiveAngles 仍保持实际 checkpoint 的值，例如 128。绝不为求值加密而修改源位置本身。

## 4. 三组完整残差与权重

所有残差都在固定点集上拼接；一个外层 LM 内保持点集、权重、guide、tau 和基不变。每个 trial 重算完整非线性值、实际 immersion 及全部几何约束。

第一版明确保留当前源配置里的 metricTau、curvatureTau、curvature guide/weight/nodeShare、R219 geometry weight/nodeShare；这些值从实际源读出，不从旧已丢失本地数据推断。当前公开 Cauchy recipe 为 metricTau=.05、curvatureTau=10^6、curvature guide=9.5、weight=.01、nodeShare=.5，geometry weight=10、nodeShare=.5。

各组径向积分采用已声明物理 ds/S 归一，角向采用周期平均 1/N；尾上的常量贡献也按同一明确规则计入。曲率与几何继续保留结点/单元 Gauss 的混合规则。不默默沿用旧 streaming 的 sqrt(w_s*a/N) 面积权重。若以后有意改权重，须列为新目标并重评 baseline。

可在完整 2pi 周期保存全部角行。原半周期端点梯形规则与完整周期规则的总能量，在相同点集、proper-half-turn 及全部正负几何行保留时一致；不能据此删去 width_minus 或 held_minus。

### 4.1 Full Gram 四次目标

记 U=X_s、V=X_u、a=a_*(s)，

$$
e=U\cdot U-1,\qquad f=U\cdot V/a,\qquad g=V\cdot V/a^2-1,
\qquad r=(e,\sqrt2f,g).
$$

Cartesian 修正不自动保 G=a^2，必须保留第三行。令 Q=r\cdot r、

$$
h=\sqrt{1+Q/\tau_m^2},\qquad R_m=\sqrt{w_m}\,h r.
$$

于是 |R_m|^2=w_m(Q+Q^2/tau_m^2)。这里用 r 包含全部相对 Gram 分量，不能使用旧 unit-tangent 模型中 g 恒零的二行公式。

### 4.2 曲率完整谱残差

从实际 X 的 Gram/II 算二维对称形算子 S_actual。复用 R191 的

$$
Q_\kappa=S_{\rm actual}
 -\operatorname{clip}(S_{\rm actual},[-\kappa_0,\kappa_0]),
\qquad r_\kappa=(Q_{11},\sqrt2Q_{12},Q_{22}).
$$

继续使用实际 source 声明的正 tau 放大

$$
R_\kappa=\sqrt{w_\kappa}\,
 r_\kappa\sqrt{1+|r_\kappa|^2/\tau_\kappa^2}.
$$

曲率必须使用实际诱导 Gram 的正交化，不能在尚未等距时直接把目标 g 用来升指标。

### 4.3 R219 七行几何

冻结源的真实 cuff 高度 Z_*、中央支持半长轴 A_q=centralA。A_q 不是弯尾参数 amplitude，也不是预算中仅作下界的 1.4。令 r_cyl=sqrt(X_x^2+X_y^2)，H(r_cyl) 为原 R210 quintic allowance。七个有符号约束为

$$
\begin{split}
c_1&=|X|-1.59,\\
c_2&=X_y-.885,\quad c_3=-X_y-.885,\\
c_4&=X_z-Z_*-H(r_{\rm cyl}),\quad
c_5=-X_z-Z_*-H(r_{\rm cyl}),\\
c_6&=.65-|X-A_q e_y|,\quad
c_7=.65-|X+A_q e_y|.
\end{split}
$$

残差 R_g=sqrt(w_g)(c_k)_+。H 的最大值 .0195，过渡区 [.52,.54]，实际 cuff 窗 [.41,.52] 沿用 R219。所有七行及各自的见证点都保留。

## 5. 六 jets 的矩阵自由合成与转置

设 B_d 是径向 d 阶导数矩阵，A_d 是角 d 阶导数到 Cartesian 值的映射。对系数方向 dC，

$$
\begin{array}{lll}
dX=A_0B_0dC,&dX_s=A_0B_1dC,&dX_u=A_1B_0dC,\\
dX_{ss}=A_0B_2dC,&dX_{su}=A_1B_1dC,&dX_{uu}=A_2B_0dC.
\end{array}
$$

若点目标反向给出六个 Cartesian cotangents T_X、T_s、T_u、T_ss、T_su、T_uu，则完整系数梯度为

$$
\begin{split}
B_0^T(A_0^*T_X+A_1^*T_u+A_2^*T_{uu})\\
{}+B_1^T(A_0^*T_s+A_1^*T_{su})+B_2^TA_0^*T_{ss}.
\end{split}
$$

各点集按此累加，最后仅一次施加右预条件器的转置。不能在每一残差组又重复施加预条件。

三角函数导数为 k^d cos(ku+d*pi/2) 和 k^d sin(ku+d*pi/2)。角转置是离散内积求和，不内置额外 1/N；1/N 已进入残差的 sqrt(weight)。用未归一化 FFT 时，0 阶 cos/sin 转置分别为 Re F_k、-Im F_k；1 阶分别为 k Im F_k、k Re F_k；2 阶分别为 -k^2 Re F_k、k^2 Im F_k。不同 Cartesian 坐标分别取相应分量，重复 |k| 的通道可以共用预条件因子。

## 6. Full Gram 的点 JVP 与 JT

固定 g 下 da=0，

$$
dr=\left(2U\cdot dU,\
\sqrt2(V\cdot dU+U\cdot dV)/a,\
2V\cdot dV/a^2\right).
$$

放大的局部导数

$$
D_m=hI+\frac{rr^T}{\tau_m^2h}
$$

对称，因此点 JVP 为 sqrt(w_m) D_m dr。给定已加权行 cotangent y，先令 t=D_m(sqrt(w_m)y)，再累加

$$
\overline U=2t_1U+\sqrt2t_2 V/a,\qquad
\overline V=\sqrt2t_2 U/a+2t_3V/a^2.
$$

其余四个 jet cotangents 为零。这是完整三行的精确转置，不使用残差截断或只看最大峰的替代目标。

## 7. R191 曲率的显式点反向链

### 7.1 前向量

记

$$
\begin{gathered}
U=X_s,\quad V=X_u,\quad B=X_{ss},\quad C=X_{su},\quad D=X_{uu},\\
W=U\times V,\quad w=|W|,\quad n=W/w,\quad E=U\cdot U,\quad F=U\cdot V,\\
L=n\cdot B,\quad M_2=n\cdot C,\quad N_2=n\cdot D,\quad
r_0=F/E,\quad P=w^2/E,\\
s_{11}=L/E,\quad s_{12}=(M_2-r_0L)/w,\quad
s_{22}=(N_2-2r_0M_2+r_0^2L)/P .
\end{gathered}
$$

这些量逐项等同 R191 的 actual curvature。需要 E>0、w>0 且全值有限，失败为实际域拒绝。

### 7.2 谱残差转置

复用 R191/显式 tau wrapper 的 hinge.apply(H)，其输入 H=(d s11,d s12,d s22)，输出已含 sqrt(2) 的三个谱残差导数。以三次 apply(e_j) 组成局部 3x3 矩阵 J_h，不是“每个全局参数列调用一次”。

对曲率残差行 cotangent y，令

$$
(\alpha,\beta,\gamma)=J_h^T(\sqrt{w_\kappa}\,y).
$$

这一步避免把对称矩阵的 Frobenius 坐标与未加权 s12 混用。R191 在恰好 +/-guide 时采用 inactive slope zero 的广义导数；照原约定保留，不声称该处通常可微。若 Python 重写局部谱公式，应逐分支对应原 R191，不调用带未知重复特征值导数约定的通用自动微分。

### 7.3 Gram/II 反向式

先建立标量 cotangents：

$$
\begin{aligned}
\bar L&=\alpha/E-\beta r_0/w+\gamma r_0^2/P,\\
\bar M_2&=\beta/w-2\gamma r_0/P,\qquad \bar N_2=\gamma/P,\\
\bar r_0&=-\beta L/w+\gamma(-2M_2+2r_0L)/P,\\
\bar P&=-\gamma s_{22}/P,\qquad
\bar w=-\beta s_{12}/w,\qquad
\bar E=-\alpha s_{11}/E .
\end{aligned}
$$

按顺序继续：

$$
\begin{aligned}
\bar F&=\bar r_0/E,&
\bar E&\mathrel{+}=-\bar r_0r_0/E,\\
\bar w&\mathrel{+}=2w\bar P/E,&
\bar E&\mathrel{+}=-P\bar P/E,\\
\bar n&=\bar L B+\bar M_2 C+\bar N_2 D,\\
\bar W&=\frac{\bar n-n(n\cdot\bar n)}{w}+\bar w n .
\end{aligned}
$$

最后五个非零位置导数 cotangents 为

$$
\begin{aligned}
\bar U&=2\bar E U+\bar F V+V\times\bar W,\\
\bar V&=\bar F U+\bar W\times U,\\
\bar B&=\bar L n,\qquad \bar C=\bar M_2 n,\qquad \bar D=\bar N_2 n .
\end{aligned}
$$

位置本身的 cotangent 为零。叉乘符号来自

$$
\bar W\cdot(dU\times V+U\times dV)
=dU\cdot(V\times\bar W)+dV\cdot(\bar W\times U).
$$

以上每个点只需固定数量的标量与三维向量，不存 n_parameter 个曲率导数。它是已有 R191 variation 的反向链，实际代码接入后应以该前向式的点积恒等式核对，不借此条公式宣称已经执行完整 BVP。

## 8. R219 几何 JVP 与 JT

令 active_k=(c_k>0)。恰好 c_k=0 时保持原 zero slope 约定。七个对 X 的梯度依次为

$$
\begin{gathered}
X/|X|,\quad e_y,\quad -e_y,\\
e_z-H'(r_{\rm cyl})(X_x,X_y,0)/r_{\rm cyl},\\
-e_z-H'(r_{\rm cyl})(X_x,X_y,0)/r_{\rm cyl},\\
-(X-A_qe_y)/|X-A_qe_y|,\quad
-(X+A_qe_y)/|X+A_qe_y|.
\end{gathered}
$$

H'=0 的分支直接给零径向项，避免在 r_cyl=0 做 0/0。球心和 held 中心处的实际距离微分域沿用旧 provider 的显式检查。

JVP 为 sqrt(w_g) active_k grad(c_k)·dX；JT 只向位置 cotangent 增加

$$
\bar X=\sum_k\sqrt{w_g}\,y_k\,active_k\,\nabla c_k .
$$

因为本阶段固定了 A_q 与实际 Z_*，没有遗漏的 dZ 全局列；若以后开放尾口高度或幅度，那是另一个显式 BVP，必须增加真实尾/帽联动及相应完整列，不能只解开上述七行的一项。

## 9. 分块存储、预条件与实际求解回执

source adapter 可将固定背景采样按径向 block 缓存在 runner scratch/memmap。每个块显式检查身份、六 jets 的有限性、a_*>0，并清理 oracle slice reuse。背景不会在每次 LSMR matvec 重新构造；变动的 W 由有限基在同点求值。

残差和少量第一导数缓存为 O(n_points)，系数为 O(JM)，B-spline 带矩阵为 O(J)。不建立 7760x7760 法矩阵。已知维数并不能代替实际 RSS/退出监控；这里只说明算法存储结构。

现有 H1 预条件可以直接接入，但活动曲率行含二阶导数。需要时采用显式正定带状 Sobolev 预条件

$$
P_k=\beta_1K_1+(\beta_0+\beta_1 k^2)M_0
 +\beta_2(K_2+2k^2K_1+k^4M_0),
$$

其中 M_0=B0^T W B0、K1=B1^T W B1、K2=B2^T W B2，beta0,beta1>0、beta2>=0。quintic 基局部重叠给半带宽 5；程序必须检查带外非零而不是按“小”丢弃。重复 |k| 的通道共用 Cholesky 因子，所有反向运算使用精确转置三角求解。

这是求解的预条件器，不是新增物理残差。选择 beta 与 damping 的规则在每次外层线性化前冻结。若采用 P=LL^T、dC=L^{-T}y，则 LSMR 求

$$
\min_y\ |J L^{-T}y+R|^2+\lambda|y|^2 .
$$

这里 damping 的坐标已明确；不能声称与旧 R206 的所有 damping 方向逐位相同。完整实际 Armijo 使用三组原物理残差总值，而不使用预条件器能量替代。若需物理系数空间的 damping，增广算子应改为 sqrt(lambda)L^{-T}，另行声明。

每个实际接受态至少记录：输入/source/observer SHA、固定 g 定义 SHA、basis/节点/权重 SHA、完整列/行数、LSMR 实际状态与残差、damping/alpha、完整 baseline→end、三组分量、full-Gram 峰与位置、实际 kappa 峰、最小 immersion、七个几何违反及见证、两个端口两 jets 的一致性、真实 OS exit。只产生了 value 或线性方向的运行不能增加接受数。

## 10. 尚须实际支付的数学输入

这一分支让 1788 列模型之外的全部允许 Cartesian 方向可用，并可把 g 真正冻结；它没有证明固定端口 BVP 必有解。若在充分丰富的空间仍有系统性残差，应读取真实固定 g 线性余核或调整新的物理输入，不能通过把 g 再次设计而冒充同 g 加密。

即使完整有限目标改善，还须同一场更密观察、连续域误差控制、全闭曲面嵌入和非局部 reach、同一 g 的整个时间族及握持/形状变化。R219 的帽预算仍以完整核心条件为前提。曲率半径通过并不排除不同曲面部分接近；本条没有把局部 curvature guide 当作 reach 证书。

当前 actual Cauchy CI 的第一次完整接受已经显示：总目标下降时，最大曲率可以变坏。因此本接口坚持同时输出并保留 metric、曲率与全部几何；后续求解不能只消费 metric-only streaming 模块的下降作为本题结果。

## 11. 已执行的完整局部点算子

新增两个可复算小源：

| 源 | SHA-256 |
|---|---|
| 6a65-cartesian-complete-point-operator.py | cf475476fb2b5e3a91d4438dd9dd67e54652bfd9594cc577b038ee2fd5e6f08f |
| 6a65-cartesian-point-operator-fixture.py | e7255389d9edd407561171211ca52299b4f6d87c56a2fc02008cff42c0ad708a |

点模块接收任意 batch 的 (...,6,3) 六 jets、固定实际目标半径 a_*、显式三个点权重和 PointConfig；返回全部十三行 residual、jvp、vjp 及 full-Gram/curvature/七项几何统计。权重已包括外部径向、角向与 guide 系数，模块内不添加面积因子或二次归一。bind_source_metadata 要求实际 oracle 身份与 runner 独立预期值逐项匹配，并拒绝 interfaceProbeOnly；这个字段验证不能代替初始化器实际读取源文件。

真实命令为：

    python /tmp/visible-flex-6a65e705/solver-work/recovered-sources/6a65-cartesian-point-operator-fixture.py \
      /tmp/visible-flex-6a65e705/math-research-public/topics/visible-flexible-closed-surface/scripts \
      /tmp/visible-flex-6a65e705/solver-work/cartesian-point-fixture01-report.json

文件发布到 scripts/ 后，只需把第一个路径改成本课题脚本路径，报告仍写 runner/tmp 中新的路径。实际外部 OS exit=0，外部等待 .121376533 秒，脚本内部 .10928246800904162 秒；NumPy 2.3.5。原 JavaScript 对照子进程同样真实 exit=0。报告 SHA-256：

    67059eb9a33cc9f0d90d1609510d25abec8e68a783598402b645d99967a994df

输入由固定种子 20261126 和显式 16 个二维形算子生成，不含任何实际 Cauchy checkpoint。16 点覆盖正/负/混合谱分支、重复特征值、恰好阈值、非正交 U/V 和带非零切向部分的二阶 jets；七个几何约束均含实际活动行。分别取 curvature tau=2、10^6，metric tau=.05。

程序直接调用原 R191 的 curvature/variation、原显式 tau wrapper 的 hinge/apply、原 R210 的 constraints 于完全相同的点输入，与新 Python 局部算子比较，并验证每组和逐点的双线性伴随恒等。没有调用任何表面 position.slice 或求解完整法方程。

| 实际检查 | 结果 |
|---|---|
| 1412 个同输入标量比较 | 最大 abs(error)/(1+abs(reference)) = 1.6976792853374324e-15 |
| metric、curvature、geometry、全十三行的双线性伴随 | 最大归一缺陷 2.696262079667182e-16 |
| 恰好曲率阈值约定 | 6 个阈值点，与原 R191 一致 |
| 标量点与 2x8 batch | residual/JVP 逐值相等 |
| 光滑活动分支上的完整非线性中央差分 | 两个 tau 均用 7 点；步长 1e-5 时最大相对差 4.983420773444934e-11 |
| interface-only source | 明确拒绝，未消费为实际输入 |

差分步长 1e-6、1e-7 时实际相对差分别为 5.560848082182702e-10、7.887415469725833e-9，符合本次浮点差分的舍入放大；不把更小步长自动称为更精确。阈值处只验证已有广义导数约定，不作不成立的光滑差分测试。

可重生点输入 SHA-256 为 b42f5da7cc91aa2685a5abb46099f90d72c981572fd5651b7302d9d20d07932f；原 Node stdout SHA-256 为 1c2fb5435d3c046efda419b26fef243ffe70e5b12d3fa76b57e8dc0635d52515。只提交脚本、参数、这些哈希和本记录，不提交可重算点数组或 JSON 报告。

这项已执行检查支付的是局部完整残差链及其转置。真正源上的归一、全域基/角伴随、实际完整 LM、同场加密与 reach 仍分别需要后续实际输入；本次接受表面步数为零。
