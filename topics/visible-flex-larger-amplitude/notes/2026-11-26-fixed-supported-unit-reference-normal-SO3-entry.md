# 固定支撑单位子午线参考场接完整 normal-lift 求解入口

日期：2026-11-26。状态：完整源码、参数和静态来源核验已齐；本说明所列新入口尚未进行科学执行。本文是 R708、R709、R703 和 R707 的实施记录，不增加已证明范围，不把工作求根或有限点几何筛变成连续证书。

## 1. 本次改变和固定对象

旧轴对称单位切向量提供完整固定标量目标的参考场，但旧初点的受支持端点校正求根没有走到原闭合方程。本入口改用 R708 的支撑单位子午线构造，先从实际完整 4e 参考输入的原核心、原高度和准确标量场定义一个固定参考切向量 $T_*(s,\phi)$，随后仍令全部原外层变量作用为
$$
T_y(s,\phi)=\exp([\omega(s,\phi)]_\times)\,T_*(s,\phi).
$$
完整 gamma 六控制、共同固定分段的 normal-lift、全角 Gram 行、原母范数、几何和握持筛继续作用于这个新场。$T_*$ 不读取当前外层 $\omega$、自由核心或高度，因而没有用中段 seed 覆盖当前自由变量，也没有把很多原自由槽变成失效变量。

准确目标仍由同一个实际参考上下文给出：
$$
g=ds^2+a_{\rm deep}(s)^2\,d\theta_0^2.
$$
准确符号域、全部深尾、原 $R$、固定材料角图 $\theta_0$、标量定义和正权观测均保留。固定 seed 是新的表示输入，不宣称它和原有限 Fourier/quintic 场族双射；也不因为 runner 的原始文件摘要改变就宣称数学 $g$ 改变或清除既有永久地点。

seed 的原核心和 $H$ 仅用于定义固定参考场。当前外层核心和 $H$ 仍全部自由，并在当前核心端点、帽端点、隐式逆图、闭合方程、全 Gram 以及几何导数中使用。固定 seed 对当前这些变量的导数为零是定义的一部分；当前端点和完整 normal 校正的导数没有因此消失。

## 2. 完整准确构造和本次参数

沿用两段支撑，所有位置都是相对于准确 $S$ 的 Fraction 参数：
$$
U_0=[S/32,15S/32],\qquad
U_1=[17S/32,31S/32].
$$
首个可执行参数采用总端层长度 $b=S/16$，四个端层各宽 $S/64$，中央五段剖面的 $\epsilon=1/10$。这些是明确输入选择，不是已经验证的统一可行性界，也不是新增完成标准。R709 已去掉收缩常数 $q<1$ 的要求；源码没有保留这个数值门。

设原固定单位子午切向量为 $T_0$，支撑补集积分为 $I_{\rm out}$，原帽点为 $P$，原核心点为 $\Gamma$，两段中央总长度为 $L_c$。对每个固定材料角图地址，求
$$
L_c v+B(d)=K,\qquad d=\frac{v}{|v|},\qquad
K=P-\Gamma-I_{\rm out},
$$
其中
$$
B(d)=\int_{\text{四个端层}}
 N\big((1-\chi)T_0+\chi d\big)\,ds,\qquad
N(Y)=Y/|Y|.
$$
再求五段正权余弦矩
$$
a_\epsilon(\lambda)=|v|,
$$
并令
$$
w=\frac{e_r(\theta_0)-(e_r(\theta_0)\cdot d)d}
 {|e_r(\theta_0)-(e_r(\theta_0)\cdot d)d|}.
$$
支撑外保留 $T_0$；端层取上式归一化插值；每段中央取
$$
T_*=\cos(\lambda h_\epsilon)d+\sin(\lambda h_\epsilon)w.
$$
完整奇对称剖面的正弦矩准确为零。两个中央区间各用同一完整五段剖面，不截断常值平台或过渡段。准确闭合、端点接合、全角选择与正则性依赖 R708/R709 所列前提；本实现不会从一次工作根自动宣布这些统一前提已付。

R708 的保守收缩 recipe 不是后继输入的永久限制。若实际完整输入不能满足某个保守充分条件，应使用 R709 的更宽层条件或另外完整证明的界，不能悄悄放宽最终几何、握持或度量验收。

## 3. 全域径向计划和准确输入责任

provider 保留原全部准确仿射节点，并插入支撑首末和四个端层的准确仿射边界。它用原完整 $S$ 包围来排序不同节点；只有完全相同的 Fraction 对才合并。如果当前包围不足以判定顺序，返回完整失败，不能以两个相近浮点数当同一个准确地点。

每个新 piece 位于一个原胞内，并保留其原胞与局部准确端点。支撑补集和四个端层均完整纳入正权 Gauss 工作计划，补集包括原无限标量尾。中央段另由全部五段剖面定义其余弦矩。首参数使用每 piece 8 个径向 Gauss 点、每剖面段 16 个点；它们都是工作求积，而非准确积分的替代定义。

原胞已有点复用真实原参考载体；新增准确点通过原完整标量 law 求值。Hold 和深尾保持稳定的相位 sin/cos 表达，没有用接近帽端的 $1-a_s^2$ 消减来猜垂直分量。数值切向量用实际 $b,c$ 归一化，并保留
$$
n=(b^2+c^2)^{1/2},\quad B=b/n,\quad C=c/n,\quad
n_s=Bb_s+Cc_s,
$$
$$
B_s=(b_s-Bn_s)/n,\qquad C_s=(c_s-Cn_s)/n.
$$
这些工作值的归一化、Hermite/符号节点载体、trig、求和和求积误差尚未包围。原标量盒只支付其自身范围，不能自动支付上述新费用。

计划完整写入 runner 的 supported-unit-reference-radial-plan.npz/json，报告保文件摘要、全域 scope、原胞数、补集/端层点数和未付费用。原始数组和批次文件不入 Git。

## 4. 固定图、核心和均值两角导数

原固定核心定义
$$
\theta_0(\phi)=\phi+\sum_\nu\frac{1-\nu^2}{\nu}c_\nu\sin(\nu\phi),
\quad \rho_0=\theta_0',\quad \rho_0'=\theta_0''.
$$
令 $e_0=e_r(\theta_0)$，则
$$
e_1=\rho_0e_t(\theta_0),\qquad
e_2=\rho_0'e_t(\theta_0)-\rho_0^2e_r(\theta_0).
$$
原核心的支撑表示为 $\Gamma=p e_r(\phi)+p'e_t(\phi)$，故
$$
\Gamma_\phi=\rho_0e_t(\phi),\qquad
\Gamma_{\phi\phi}=\rho_0'e_t(\phi)-\rho_0e_r(\phi).
$$
这里最后一项是 $\rho_0$，不是材料角旋转架的 $\rho_0^2$。两种表达在源码和纯读取器中没有混用。

补集积分写为 $A_{\rm out}e_0+C_{\rm out}e_z$，于是实际均值目标的三套工作 jet 为
$$
K_0=(R-A_{\rm out})e_0+(H-C_{\rm out})e_z-\Gamma,
$$
$$
K_1=(R-A_{\rm out})e_1-\Gamma_\phi,\qquad
K_2=(R-A_{\rm out})e_2-\Gamma_{\phi\phi}.
$$
完整尾、核心常数和全部 $H$ 项都保留。provider 固定原核心和高度，故求这套参考角 jet 时不把当前外层变化混进来。

均值核从同一个完整根解 $v,v_\phi,v_{\phi\phi}$。设 $M=B_d$，则
$$
J_v=L_c I+M\,DN(v).
$$
$M$ 对称半正定不意味着乘积 $M DN(v)$ 在通常坐标中对称；实现使用完整矩阵，未把它错误交给对称正定求解器。隐式一、二角导数保留边层归一化的全部 $DN,D^2N$ 和目标 $K_1,K_2$，随后完整传播到 $d,w,\lambda$ 三套 jet。

## 5. 工作均值求解和失败记录

均值核 bd9c 对完整三分量方程做真实残差回溯 Newton，首预算 128 个 Newton 外步、每步 24 次回溯、Armijo 常数 $10^{-4}$。所有待求角都保留；每个候选重新读取其实际 $B$ 和残差，归一化域不合法或非有限的候选标明 unavailable 后继续原回溯。源码不声称这个实际算法全局收敛。

失败记录区分最后已算 Jacobian 所在点、最后候选点、实际步长、候选是否可读和各自残差；不拿接受后状态冒最后失败矩阵。profile 幅度根用实际五段正权矩进行最多 64 次二分，不把工作 $a_\epsilon(0)$ 强行写成 1，也不重新归一化权。

完整返回不仅检查两个分步残差，还单独读取组合物理闭合：
$$
B+L_c\,a_\epsilon(\lambda)d-K.
$$
它必须满足本次原工作容差 $2\cdot10^{-12}$。不能把两个分别小于此容差的残差直接相加后仍称组合已通过。角 jet 的实际线性方程残差另报；没有把工作根提升为准确根或准确误差盒。

provider 将固定参考角根按 literal binary64 phi.hex 地址缓存，每个完整批次保存全部角、均值元数据和实际数组。它不因当前外层 x 改变而重新定义 seed。缓存写入中断可能造成缓存中已有数值而完整批记录尚未追加；纯读取器分别报告二者真实数量，不把缺少记录补成成功，也不把这类中断改写成方程不可解。

## 6. 新参考场四套 world jet

端层令 $Y=(1-\chi)T_0+\chi d$，则
$$
Y_\phi=(1-\chi)T_{0,\phi}+\chi d_\phi,\qquad
Y_{\phi\phi}=(1-\chi)T_{0,\phi\phi}+\chi d_{\phi\phi},
$$
$$
Y_s=(1-\chi)T_{0,s}+\chi_s(d-T_0).
$$
源码对归一化使用完整一、二阶链，返回 $T_*,T_{*,s},T_{*,\phi},T_{*,\phi\phi}$，不是只旋转零阶向量。

中央记 $\alpha=\lambda h_\epsilon$，有
$$
T_*=\cos\alpha\,d+\sin\alpha\,w,
$$
$$
T_{*,\phi}=\cos\alpha\,d_\phi+\sin\alpha\,w_\phi
+\alpha_\phi(-\sin\alpha\,d+\cos\alpha\,w),
$$
$$
T_{*,\phi\phi}=\cos\alpha\,d_{\phi\phi}+\sin\alpha\,w_{\phi\phi}
+2\alpha_\phi(-\sin\alpha\,d_\phi+\cos\alpha\,w_\phi)
+\alpha_{\phi\phi}(-\sin\alpha\,d+\cos\alpha\,w)-\alpha_\phi^2T_*,
$$
$$
T_{*,s}=\lambda h_{\epsilon,s}(-\sin\alpha\,d+\cos\alpha\,w).
$$
原支撑外四套完整 jet 原样保留。端层和中央接口使用其实际准确边界定义；$S_5$ 首两端导数和中央剖面端口保证所列准确接合。一般原 $T_0$ 的径向正则性没有被虚构提高，场的 $C^2$ 范围仍按 R708 的明确假设。

## 7. 外层全部自由变量和完整 normal 链

新 base 除构造器与 metadata 外，原 7f 的全部物理方法逐个 AST 相同。完整当前核心隐式图、Rodrigues、全域/partial 积分、六 jet、残差、J/J*、point VJP、保存/续接和 H² 坐标都继续执行。旋转规范冗余没有删除，自由核心和最后高度槽没有冻结。

新 normal 除构造器外，原 42ea 的全部类方法 AST 相同。共同准确分段为 $\tau_i=i/32$，所有角和当前外层点使用同一分段；没有逐角自适应选择另一个模型。每段三增量根保留之前六控制、之前法向 frame 和原零控制目标的完整参数/角链。度量读数使用完整 $6m$ 隐式系统，六 jet 与其 J/J* 使用完整 $9m$ 系统。旧角根升级为二角 jet 时保留同一已选前向分支。

准确 seed 在原零外层点满足闭合时，原零控制是准确 normal 方程的一个解；实际 seed 求积与外层全域求积不同，工作初根仍必须真实重读并求解。尤其 R709 的均值 Jacobian $J_v$ 可逆不证明 normal 控制 Jacobian $C_u$、每段 $A_iA_{i-1}^T$ 或其全角同支条件。源码和读取器显式记录这条不继承关系。

首个输入保持原 $M=160,J=923,P=7377,N=2048$，按完整布局预计原自由变量数 1,333,370、全角三分量度量行 45,324,288；实际报告仍须从真正对象给出这些计数。没有去掉均值或 mixed Gram 行。选用原明确 jet-sum 母范数及 $\mu=0.01$，不把它冒准确积分 H²；径向长度 .05、角转折 24 和全部缩放沿原源。

## 8. 原完整几何、幅度、Phase I 和永久地址

新 geometry 只改构造器的真实来源/模型绑定。从 _set_x 到文件末尾的整个物理后缀逐字保留，SHA256 为 50d6f1414807ea91710ecf3a0e3e52d9530a04f299763d2a05f30c372f27bf7e。完整 world 六 jet 扫描、原 192 行 selector、幅度两支 $\pm p$、帽/高度行、全部 free core 的 $dp$、point VJP、原母范数转置和永久地点并集都保留。

driver 从 save_report 定义到文件末尾逐字保留原完整 normal driver，后缀 SHA256 为 9b05f8e00c483491ffd9259b2d675af940c6f0b8a8104d6bfcd70ffb0e31b4ee。全变量 QP、共同松弛 Phase I、全部已知点和全网格真实非线性筛、拒绝后新地点记忆、末父复读均未缩小。

首参数保原 reach safety .992、目标比例 .03、marked diameter budget 4.2、见证长度 .9、高度底线 1.01。它们是该分支算法约束，有限必要筛不等于连续 reach 或全相位证书。显式新输入和新参考缓存都不能抹去旧 $g$ 的永久地址责任；旧物理角字作为当前固定图地址的已登记语义保持，不声称跨表示是同一个空间点。

## 9. 完整新来源闭包

全部新源以独立 schema 和完整文件 SHA 绑定，未把旧 7f/42ea 标签贴到新物理输入上。

| 文件 | 字节 | SHA256 |
|---|---:|---|
| supported_unit_seed_mean_jets.py | 32767 | bd9c0761e101679b10ff52d50f27a3dfb964687130c59878d756389b304ee771 |
| supported_unit_meridian_reference.py | 39826 | 30ea80ec0673f3bdff3e59b97dfb5f7166a296aeb4b989fbca18b2feb5e9544c |
| so3_supported_unit_meridian_operator.py | 40705 | e1bb7303540b1e807176ca5e71dcb2798b3f1e4e34909cd207cea300a9d4ebc0 |
| supported_unit_literal_zero_moment_input.py | 30373 | 9fecbe018442be23d0c36d139ebb6ba3574b550aed76ef89cdcadd279770b0d6 |
| so3_supported_unit_normal_lift_operator.py | 91472 | 5297192216356970140585eb9e56c521d9f35453211fb5a76086b713350eaa67 |
| so3_supported_unit_normal_lift_geometry.py | 55752 | d84b540d21622d4d609efa5ea85fef432a2dcebb51bea0f3c7c24376294918f4 |
| fullclosed_supported_unit_normal_lift_so3_qp.py | 67642 | e482428ee68aefa23da5b3b5c0a6b3363f047b0457f67a9193044ef151caec35 |
| launch_supported_unit_normal_lift_so3_actions.py | 17149 | fa468e7bbe58daa8aba0b6403b81468c7e8ed399028c19b1a2c71d47be87919b |
| read_supported_unit_normal_lift_so3_report.py | 56534 | d788f4f07559b9375247874abbd57ec7d493a1cb4f543b8ab9f31f8dab3d128b |

新 Q binder 继续读取原已刊十八个 literal Q 字，但它们是明确固定参数，其旧 trace 仅为来源，不是本 seed 当前真矩逆。新 definition 的完整十二字段同时绑定本次原参考、固定标量、完整 base、原初自由点、固定图和完整 seed model/identity。固定 seed 的支持首末与两 wide bubble 首末逐项核对。

新 base 模型明确收完整 seed 定义、其工作定义、provider/kernel SHA。normal、geometry、driver 和纯 reader 逐级核同一对象。actual 原始参考文件摘要来自本次真实报告，不硬填旧 03b 的原始 SHA，也不凭来源同名假定字节相同。

## 10. 报告、失败和纯读取

provider 的完整实际工作记录位于 latest_operator_metadata.base_complete_metadata.fixed_supported_unit_seed。它包括全径向计划、实际计数、完成角数、全部完整均值批记录、最大原标量费用和本次失败。base_complete_metadata 是真实接口名称，不能误选不存在的 base_metadata。

driver 在首次 F/root 之前保存原输入/模型/初点报告。provider 的实际失败作为 RuntimeError 派生类由原初场失败路径记录，不要求 normal 根曾先成功。纯 reader 将固定 seed 工作完成度与当前 normal 根可用性分列，保所有三十四个原 normal snapshot 字段及当前点摘要；不存在的值保 null，不从另一点 metadata 回填。

纯 reader 全文保留原十个核心读取函数，新增完整 seed binding 和 provider 实际 metadata 核验。可公开的标量包括 seed identity、completed_literal_angle_count、mean_successful_batch_count、complete_radial_plan_available、完整批记录与缓存数量是否吻合、最后 seed 失败阶段/原因。不能把完整计数对象或批次数组直接送进 scalar-only controller 摘要。

## 11. 可执行参数和九个真实历史来源

完整参数文件为 supported-unit-fixed-reference-normal-full-history-run05-ready.json。科学输出目录 supported-unit-fixed-normal-lift-first；纯读输出 postprocess/supported-unit-fixed-normal-lift-first-readout.json。两步的准入 parent 都使用本次真实 reference.npz，以便科学初场失败而没有 final.npz 时，纯读取仍能完整运行。

九个显式历史输入依次为：

1. axisymmetric-R690-reference-v2-first/locations.json。
2. axisymmetric-so3-complete-v2-first/report.json。
3. axisymmetric-so3-prior-separation-SOC-first/report.json。
4. angular-unit-complete-first/report.json。
5. axisymmetric-so3-integral-norm-first/report.json。
6. axisymmetric-so3-integral-norm-second/report.json。
7. zero-closure-added-gamma-KKT-explicit-H-first/report.json。
8. zero-closure-fixed-normal-lift-first/report.json。
9. zero-closure-fixed-normal-lift-explicit-H-first/report.json。

最后 normal-H 的实际报告已返回，九个路径均有本次真实前驱。ready 不借旧 run 的 raw SHA 假装本次输入。若准入前另有必须继承的新地点报告，应显式追加；setup 缺报告不能冒充空集合。

首科学预算保 1 条完整 metric 方向、每条 16 次 QP 迭代、最多 4 条恢复方向各 64 次、15 次原 ray 回溯。normal 为 32 个共同阶段，每根最多 24 次 Newton、18 次回溯、控制球半径 2、原物理闭合容差 $2\cdot10^{-12}$。这些只是这次自然完整方向预算，不是能力极限或完成判断。未知实际成本通过原完整计数、耗时和峰值内存返回。

只清理新 QP 行缓存；固定 seed 的径向计划、均值批次和参考 cache 保留在 runner 供同场归因。科学原始数组、完整大报告及 cache 不经集成上传或入 Git。所有科学函数有公开 Actions 仓库环境守卫；本地只做纯源码操作。

## 12. 已实际完成的静态检查和未付责任

全部上述源已实际做 stdlib AST/compile 和重复字面 key/keyword、尾空白检查。没有导入科学模块或执行数值 fixture。pure launcher 的 --print-command 已实际解析完整 148 参数和九 manifest，不读取科学输入。

独立比对确认：新 base 33 个类方法中 31 个 AST 同原，只有构造器和 metadata 改；新 normal 51 个类方法中 50 个 AST 同原，只有构造器改；新 geometry 30 个类方法中 29 个 AST 同原，只有构造器改。driver 全部 literal source role 消费落在其完整声明集合中，launcher parser 与 driver parser 逐树一致。这里报告的是实际静态检查，不是执行成功。

仍未返回本入口真实参考根、首完整场、全 QP 方向或连续证书。新 seed 根、两角导数、trig/归一化、所有求积和工作算术费用必须另付；当前全场准确/数值差、完整固定 $g$ 三 Gram、全局嵌入、整像握持幅度、含反射的 Euclidean 商、全相位 reach 与真正固定问题精化均未由本说明完成。原失败没有被解释为不可达、端点秩亏或 KKT 曲率奇性。

本次实施的实际用途是把有完整准确构造依据的闭合单位 seed 作为固定参考输入，同时保留全外层求解能力和所有原约束。下一步应读取这个完整入口的真实返回，按已付或未付的具体项继续研究。

## 依据

- [R708 支撑单位子午线 seed](../results/R708-supported-unit-meridian-seed-contraction.md)。
- [R709 不需收缩的全局凸均值闭合](../results/R709-global-convex-mean-closure-without-contraction.md)。
- [R703 固定分段 normal 端点提升及完整角 jet](../results/R703-normal-endpoint-lifting-and-fixed-partition-jets.md)。
- [R707 完整有限 normal 链的根与 jet 误差传播](../results/R707-fixed-normal-chain-root-jet-error-propagation.md)。
