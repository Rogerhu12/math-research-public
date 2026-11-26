# 共同固定法向分段的完整 SO(3) 求解入口

状态：完整源与可执行接口已形成；还没有本入口的实际科学结果。数学依据是已刊 [有限法向选枝方案](2026-11-26-normal-endpoint-lifting-without-stationary-control-selection.md)。这里登记实际全体代码、输入、参数链、缓存、完整求解和读数合同，不把之前 gamma KKT 的数值失败解释成已经证明的 KKT 奇异，也不把本入口预告为可达性或等距存在证明。

## 1. 同一六控制族，明确不同的有限选枝

固定原实际 base、完整 scalar g、材料图、十八个字面 Q、旧两 bubble、独立 gamma，以及全部原外层自由点 x。令 $u=(z/S,v)\in\mathbb R^6$、$f(x,\phi,u)=C(x,\phi,u)/S$。本次取消控制驻点的 KKT 选择，采用共同固定准确分段
$$
0=\tau_0<\tau_1<\cdots<\tau_m=1.
$$
初值 $u_0=0$，每段定义
$$
A_{i-1}=f_u(x,\phi,u_{i-1}),\qquad
u_i=u_{i-1}+A_{i-1}^{T}\eta_i,\qquad
f(x,\phi,u_i)=(1-\tau_i)f(x,\phi,0).
$$
每个 $\eta_i$ 有三个分量。所有角与所有候选使用同一个完整分段，分段本身进入新 model identity。driver 的首接口用 `--normal-stages m` 构造全部 `Fraction(i,m)`；默认 m=32。operator API 也接受完整准确节点 tuple，严格要求首0末1与递增。

这是同一六控制可容许族的一种不同选枝，未扩大这个已声明的可容许族。它不是 min-norm KKT 的换标签，也不是精确连续 horizontal ODE 解；有限分段变动会改变选定场定义。重新选择 m 必须建立新模型并真读 baseline；同一 g 不等于同一选定场或同一根。

当前段矩阵是 $A_iA_{i-1}^{T}$，一般并不对称，也不因两个 A 都行满秩便自动可逆。代码不作这种假设。全局根存在、每段逆、共同周期/反射分支及连续误差仍按数学稿的条件范围处理。

## 2. 完整输入和全部原自由量

新 operator 从完整 b712 源派生，保留原 base 7f26 的所有外层 core / omega / H 自由量与原打包。内部六控制和每段三个增量是隐式解，不作为额外自由字段加进 QP，也没有冻结已有自由方向。

原两种 Q 模式保持独立，完整 validator 文本未变：

- 原 strict same-reference 模式仍绑定原参考、base、profile、初点和旧 trace 来源，不更名通过 guard。
- 新-reference 模式仍由完整 ea94 binder 对当前真实 reference / base / profile / 初点 / chart 全部绑定，十八字仅作为采用的常量，不称当前矩逆，不以新 raw 字节身份删除同 g 历史位置。

完整 source SHA、数学 definition、当前真实初始参考、全部 observation / node / scalar 身份仍由原入口与新 constructor 逐项验证。新的根选枝、准确分段与原数值 carrier 的边界全部写入 model。constructor 明确验证每个浮点分段载体仍严格递增；不在工作值中折叠相邻准确节点。

## 3. 实际有限根算法

每一段从字面 $\eta_i=0$ 开始 Newton / Armijo，保上一段已经实际返回的完整 $u_{i-1}$ 和 $A_{i-1}$。数值迭代只有当前平面的三个未知量。原归一式的完整残差用于下降判据，实际 $|u_i|<2$ 是首版显式六控制域；没有暗加或继承旧三根球，也没有把 $\eta_i$ 称为 Lagrange 乘子。

默认每段最多24个 Newton 更新、每次最多18个回溯，Armijo系数 $10^{-4}$。内部归一容差为实际 `endpoint_tolerance / S`；默认物理 endpoint tolerance 为 $2\cdot10^{-12}$。最终再读原物理 C，不把某个中段的 shifted residual 当成闭合。

任何一角在一段失败，候选就没有返回完整的闭合场。代码保存实际失败阶段、原当前点、局部角索引、真实控制和增量、残差、回溯，以及已经算过的3×3当前平面矩阵及其自身状态；不为诊断额外计算 F / J / SVD。失败不能用零根补齐，也不跳过该角。

各完成段以及完整终段都再次读原等式。最终原物理 C 的实际容差、控制域和 finite 条件分别检查。导数 jet 的残差完整记录，但不把工作数值残差当作连续误差上界。实际矩阵奇异值没有另计算；metadata 对此明确为 false。

数值求根迭代轨迹与所选准确隐式方程分开。共同固定节点不是逐角 adaptive continuation：即使某一个角困难，也不能在该角插一段后仍称同一个模型。改变共同分段需要新的明确输入和新 baseline。

## 4. 全角 jet 与全部参数 J/J*

记 $g_j$ 为 $f(\phi,u(\phi))$ 的总角 j-jet，把 $u_0,u_1,u_2$ 当作独立 jet 槽，则
$$
A^{[j]}=\frac{\partial g_j}{\partial u_0}.
$$
源码 `_normal_frame_jets` 按此对每个完整 closure 分量求偏导，`create_graph=True` 保留当前外参数和前段控制图；仅在数值计算需要而原张量没有图时，建立独立局部 control leaf。已有 active previous 或 data 图不 detach。

新控制的各角 jet 是
$$
u_i^{[j]}=u_{i-1}^{[j]}+
 \sum_{k=0}^{j}\binom jk\left(A_{i-1}^{[j-k]}\right)^T\eta_i^{[k]},
 \qquad j=0,1,2.
$$
每段完整三个方程及其一二阶总角导数进入当前段6×6或9×9系统。全链相应为 $6m$ 或 $9m$ 下三角系统；并不是在末端三个 closure 方程上单独求六控制的导数。

数值根计算可 detach。但 active 场的 `_implicit_jet_value` 顺次重新建立每一段：

1. 从全部当前 data 及上游控制图构造当前 A 的全角 jet；
2. 保留右端零控制 $f(x,\phi,0)$ 的全部当前参数及角导数；
3. 使用当前完整段的6×6/9×9矩阵，对 `residual-residual.detach()` 作隐式 solve；
4. 由同一个 binomial 控制式构造下一段控制；
5. 只对前向值作缓存字锚定，保全部一阶参数导数，再进入后段。

因此前段的 A、u、零控制目标与所有 outer core/omega/H 都作用到后段。J* 是同一完整图的转置，未使用有限差分，也未删除某个乘法链。末段方程不承担它无法独自确定的六控制导数。

这里是完整一阶外参数隐式线性化；没有承诺这些 value-preserving surrogate 提供二阶外参数 Hessian。A 的二阶角导数再作一阶参数微分仍可能用到 f 的混合四阶导数，因此没有把“取消驻点 Hessian”误写成只剩低阶成本。原 7f26 Rodrigues 小分支 degree12 多项式及其完整保图导数保持来源，不以原零阶运行替代本次高阶责任；截断、接缝与工作舍入误差仍未包围。

## 5. 同支缓存与 order 1 → 2

缓存按同一完整当前 x 和每一个 literal phi hex 绑定。当前 x 改变时清空根、残差、失败及 last normal batch；不把另一点的成功摘要放进当前点。

从 metric 的 order1 升级到完整六jet的 order2 时，代码逐段保留已选：

- $\eta_0,\eta_1$；
- $u_0,u_1$；
- 原 $A_0,A_1$；
- 已算的零阶3×3矩阵。

只沿这同一支补新 $A_2,\eta_2,u_2$，再组新的9×9矩阵。它不重新求零阶根来暗中换支，逐字复用被显式检查。升级后用实际现 data 再读各段原等式与终端物理 C；如果旧值不能满足这些实际检查，诚实拒绝该候选，不改写旧 baseline。

active 图中的 frame、原零控制 target 与各段控制前向值锚定到实际所选缓存字，导数保同公式的完整链。这使 grad / no-grad / 批形带来的普通工作舍入差异不会在调用 J 时改掉已经选择的前向控制。它不是 root 或求积误差证明；这些费用仍按同实际场另付。

缓存的 complete grid availability 只是数值缓存陈述。metadata 另外区分全 grid 零阶根与全 grid 二阶 jet，不把一阶缓存存在当作二阶已读。

## 6. 完整外层求解与新报告合同

新完整 driver 从 5134 派生；从 `def save_report():` 至 EOF 与父源逐字相同。全场初读、完整正权 Gram、原 H² 坐标、原全 QP、192选择器及附加幅度约束、共同松弛 Phase I、所有真实回溯与全永久位置复读、拒绝点记忆、最终独立真读均保留。

新 adapter 从 0c488 派生，只更换完整真实 source / model / 分段维数 guard。从 `_set_x` 至 EOF 的全部物理 scan / 世界坐标 covector / row / 幅度 / 记忆主体逐字相同。它不改预算，也不把有限必要筛升级成 reach 或 whole-image 连续证书。

原外层基函数与范数不变，但所选隐式场不同，必须重新读取 baseline、实际Phi、全几何与对应J。新入口保全部最初 core 固定槽的原定义，其余原自由量全部保留；没有靠删 mean/cross 行换取下降。

driver / reader 使用新的34字段 snapshot，逐个字段存在于本 operator metadata；旧 KKT counters、stationarity、乘子范数、KKT_dimension 都不作为本源数据。新 reader 严核：

- 真实 whole-source / fixed scalar / 完整 model / dual input；
- 全准确共同节点、实际载体、m、6/3/每段9与全6m/9m；
- 每个当前点 snapshot 的自身 source、model、原 root policy 和同一分段；
- latest whole metadata 和各点 snapshot 分开，没有缺值回填；
- 初次失败仍是未接受候选，失败后的空值保持 null；
- 目标、测度与规范参数相同才比较当前入口自己的初末 Phi。

所有失败、矩阵和各段原始数据只留 runner。公开元数据读取器仅选择明确的小标量键；大科学原数组不进入Git。初次数值入口或实现失败不会被换标签成科学结论。

## 7. 完整来源和静态范围

| 完整文件 | 字节 | SHA256 |
|---|---:|---|
| so3_zero_normal_lift_operator.py | 89757 | 42ea8ec5920e3815b99c83c41448efb38ee37860f4d9362ddea6bce2418d39fe |
| so3_zero_normal_lift_geometry.py | 52950 | 255760e188d13f22ffef86c029f35f5d1629384411d2e32f03f75df60f4ab71c |
| fullclosed_zero_normal_lift_so3_qp.py | 64080 | 68a6e483a4916d72411d08647622a1e539b26f9eca3c1449b4e7399bec17dd38 |
| launch_zero_normal_lift_so3_actions.py | 14803 | c5f139bac6ecb50aa4b31de0aa8f5da4f2feafc2b26bc821826fc31a0c6f5c46 |
| read_zero_normal_lift_so3_report.py | 42129 | 8381cd9e034fda5917cae5f221f0c3f5420953cab6ca8dd809c82f3de0f7e1e8 |

父 operator 是完整 b712，原初角/端口/物理六jet/所有 residual / J / J* / pointVJP / save / load 等30个类方法文本逐字相同；10个方法有明确变化，新增9个固定法向链方法，删除10个驻点 KKT / adaptive continuation 方法。此比较是完整函数文本（仅忽略末尾空行），不是尚未执行的 AST 检查。

driver 科学 suffix SHA为 `9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee`；geometry 物理 suffix SHA为 `50d6f1414807ea91710ecf3a0e3e52d9530a04f299763d2a05f30c372f27bf7e`。launcher 的 parser 去除自身 install / print 两flag后与 driver 完全一致。

完整 source/byte/metadata 静态审已做。当前本地环境不可用，尚未执行这些新文件的 AST / compile / 科学；没有构造科学 fixture 或用小维替代验证。m=32 的完整图内存和实际调用成本未知。首实际完整预算记录真实费用；不通过删变量、行或上游图隐藏成本。

## 8. 首实际请求的范围

首请求继续 N=2048、M=160、J=923、P=7377 的完整真实输入和正权观测，完整原自由量及H²坐标；初始 H 默认是当前已验证 reference 的原 H。不同高度可作为后续明确独立初点选择，本版不会默默采用旧运行的另一高度。

root 的完整科学队列决定首次使用的方向预算。ready保持一条 metric 方向最多16步、最多四条 restoration 每条64步、15次 ray、mu=.01、p=4、epsilon=.001、scale=.05，原reach/diameter/witness预算不变；m32和根24×18为明确本次选枝预算。它们不成为README验收阈值，也不是方向能力的极限结论。

所有当前真实同g永久位置必须保留。run05准备位置与3/17/21/26/30的完整真实再生报告是已明确闭包；若其后的 gamma+H 或其他真实场发现位置，也显式加入。新模型/source/raw身份不抵消该责任。所有引用的runner报告必须实际存在，不用旧SHA替代本运行输入。


## 有限法向选枝的端口与物理全相位消费

本实现的共同分段参数 $\tau_i$ 只用于在给定完整自由点上选择一个零闭合基场。它不是课题 README 的物理时间 $t$。固定全部 $\tau_i$、旧两个 bubble、独立 $\gamma$、材料图和字面 $Q$，在每个角上依次解同一组三维方程；任何一段失败都没有生成新的可接受闭面。

### 全部参数和角导数

设 $f=C/S$、$A_{i-1}=f_u(\phi,u_{i-1})$。每段使用
$$
u_i=u_{i-1}+A_{i-1}^{T}\eta_i,\qquad
f(\phi,u_i)=(1-\tau_i)f(\phi,0).
$$
末段的三个闭合等式本身不足以唯一决定六个控制的变化；全部先前选枝等式共同决定导数。因而 $A_{i-1}$ 的所有当前 core、原 $\omega$、H 和前段根导数，以及右端 $f(\phi,0)$ 的这些导数，都保留。每段的三个根及两阶总角 jet 组成九维下三角系统；全链是 $9m$ 维，按逐段三角消元/反向转置计算，不把前段值从参数图中 detach。数值 Newton 迭代轨迹不被微分，实际根载体与其隐式线性化分开。

在同一分支上，只要每段实际数学 Jacobian $A_iA_{i-1}^{T}$ 可逆，通常 IFT 逐段给参数及角的局部光滑性。共同分割本身不证明这些逆存在，也不证明全圈选择了同一周期/反射分支。反射轴的奇偶与一二阶迹必须属于相应的同一协变分支；每角分别得到一个孤立根不能替代此责任。order 1 到 order 2 的数值升级沿原已选根补第二 jet，不换零阶根。取消驻点 Hessian不意味着取消所有高阶导数：$A_{i-1}$ 的二阶角 jet 再求一阶外参数仍可能使用 $f$ 的混合四阶导数。

### 中圈、径向接缝与帽

最终六控制 $u(\phi)$ 是整条 meridian 的同一个根，不随 s 重解。两 bubble 和 $\gamma$ 的支撑严格处于 $(0,S)$，故新增旋转在 core 和帽附近恒等。最终准确闭合等式给
$$
F(s,\phi)=P(\phi)+\int_S^sT(v,\phi)\,dv,\qquad F(0,\phi)=\Gamma_c(\phi).
$$
其两阶角导数给 $F_\phi(0)=\Gamma_{c,\phi}$ 和 $F_{\phi\phi}(0)=\Gamma_{c,\phi\phi}$，不是由小数残差直接冒出的等式。

原 core 端 $\omega(0)=0$ 和单位参考给 $T(0,\phi)=e_z$。单位长度恒等式又给 $T_{s,z}(0,\phi)=0$，且 $T_\phi(0,\phi)=0$。因此反射拼接所需的 $F_z(0)=0$、$F_{s,xy}(0)=0$、$F_{ss,z}(0)=0$ 原样成立，并保全部混合两阶迹。当前 core 的逆材料角和全部原自由系数导数仍在 $\Gamma_c$ 中。

帽端原约束 $\omega(S)=\omega_s(S)=0$ 给
$$
F(S,\phi)=R e_r(\theta_0)+H e_z,\quad
F_s(S,\phi)=-e_r(\theta_0),\quad F_{ss}(S,\phi)=0.
$$
以 $r=R+S-s$ 和真正材料角 $\theta_0$ 表达，这些正是平帽的完整 Cartesian 两阶迹。帽极点使用 Cartesian 圆盘图，不把非线性 $\phi\leftrightarrow\theta_0$ 图硬延伸到极点。共享径向 jets 保证 $T,T_s$ 及所需角 jets 连续，已经足够 F 的 $C^2$ 接合，不另加 $F_{sss}$ 条件。以上均为准确隐式场的接口；工作 root、求积、逆图和 carrier 误差仍须据实际同场支付。

### 物理 t、reach 和固定标记

得到一个合格基场后，物理族仍使用已有 R248 的准确公式：活动面作空间相位旋转与逆材料角平移的复合，固定帽及标记不动。它保持活动区同一旋转不变 g，并把完整基场的相对 Gram 算子误差、主曲率和 $C^2$ 正则性准确传到全部物理相位。此处不使用有限 t 网格插值，也不把辅助 $\tau$ 的轨迹当作该族。

全 t 嵌入/reach 继续由 R650 消费新同场的完整闭浸入、同一个轴对称正定 $A_\beta$ 和轴上中心、全域正支撑下界与主曲率上界，再加固定帽/标记自身的同预算。$A_\beta$ 与全部绕轴旋转交换，所以活动输入能统一覆盖全部相位；带标记整像的 reach 不具有无条件的刚性旋转恒等式。有限 GeometryScreen 的全部网格和永久地址仍必读，但它的通过本身不是上述连续证书。旧场的 reach、diameter、held、metric 和 R661 逐胞非平面见证都不迁移到新隐式场；包含反射的 $\delta_E>0$ 及 README 其它条件仍须同候选完整消费。

