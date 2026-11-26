# 支持内单位 seed 的完整工作均值与角 jet 小核

日期：2026-11-26。完整源码：supported_unit_seed_mean_jets.py。
SHA256：bd9c0761e101679b10ff52d50f27a3dfb964687130c59878d756389b304ee771。
字节数：32767。
schema：complete-supported-unit-seed-working-newton-mean-and-angular-jets-v1。

本源消费固定参考的完整角 jet，产生工作三均值根、中央幅度根及它们的两阶角导数。它是候选生成的一个数值小核，不是完整物理场、全变量优化器、连续证书或新的求解前置 fixture。固定 scalar/reference、真正径向/角坐标、所有积分载体和最后有限表示/完整自由点的绑定由独立 provider 负责。它没有导入旧物理模型以假冒同一候选，也不改变调用者数组。

## 1. 输入和返回合同

唯一公开科学函数为：

    solve_mean_jets(
        K0, K1, K2, T0, T1, T2, chi, weights,
        central_length, e0, e1, e2,
        *,
        epsilon,
        profile_quadrature_order=16,
        maxiter=128,
        tolerance=2e-12,
        scalar_iterations=64,
        mean_backtracks=24,
        mean_armijo=1e-4,
    )

- $K_j$ 和 $e_j$ 形状均为 $(A,3)$，$A>0$。前者是完整支持所需积分 $K$ 的零、一、二阶材料角 jet；后者是固定 world 径向向量 $e_r(\theta_0)$ 的相同三套 jet。
- $T_j$ 形状均为 $(P_b,A,3)$，$P_b>0$，必须覆盖全部端层和所有当前角。这里是未作端层插值的真实参考 meridian 的工作角 jet。
- cutoff chi 和实际物理积分权 weights 形状为 $(P_b,)$。工作 cutoff 保留在 $[0,1]$，权必须为正，源不对它们重新归一化。
- central_length 是准确 $L_c$ 的有限正工作载体。epsilon 可传准确 Fraction/分数字符串；若传普通 float，则数学参数在本核记录中明确按该 binary 字的准确有理值解释，不能把它另称某个未传入的分数。
- maxiter 限制 Newton 更新次数；每次更新前及最后都重读全部角的当前完整均值。mean_backtracks 限制每个仍未接受的角的真实试点次数。所有参数和真实使用次数均记录。

十二个稳定主返回键为：

    v, v_phi, v_phiphi
    d, d_phi, d_phiphi
    w, w_phi, w_phiphi
    lambda, lambda_phi, lambda_phiphi

前九个数组形状为 $(A,3)$，后三个为 $(A,)$。额外保留实际同点 mean_jacobian、中央 $a,a',a''$、端层均值三 jet、组合闭合三 jet 和 metadata。所有返回数组只读。metadata 是普通 JSON 可序列化对象；控制器若只允许标量摘要，应从中选择实际标量叶子，不能把整个字典作为 summary 值。

角索引是**当前输入批的实际行索引**。provider 必须把它绑定到自己的真实角数组/地址。端层归一化失败另保留 $(\text{boundary node},\text{angle})$ 全部坏索引，不把其 flatten 后的整数误称角地址。

## 2. 完整均值方程与真实 Newton

在每个角定义
$$
d=N(v)=v/|v|,\qquad
Y_p=(1-\chi_p)T_{0,p}+\chi_p d,\qquad
B=\sum_p w_pN(Y_p).
$$
完整三分量工作方程为
$$
R(v)=L_c v+B-K_0.
$$
从同一个 $v^{(0)}=K_0/L_c$ 开始，当前点的完整 Jacobian 为
$$
M=\sum_p w_p\chi_p DN(Y_p),\qquad
J_v=L_cI+M DN(v).
$$
在准确算术中 $M$ 对称半正定，但 $J_v$ 一般不对称；源码没有把乘积次序交换，也没有用对称近似替代它。

对当前残差尚超过原 tolerance 的每个角，解同点
$J_v s=R$，再实际计算 $R(v-\alpha s)$。
只有试点可用、真实欧氏残差严格降低，并满足
$$
|R(v-\alpha s)|
\le(1-\text{mean_armijo}\,\alpha)|R(v)|
$$
才接受。非有限或归一化零范数试点只是该角的不可用试点，继续按同一策略回溯；不能补有限向量、剪切方向或丢弃该角。已接受的角在当前回溯批中保留，下一次全角读取仍会独立核其实际残差。

源不计算或要求 $q<1$，也不把 R708 的保守薄层选择公式设为数值门。R709 的凸性/单调性说明了可以使用更宽端层的数学理由；源码仍不宣称有限次 Newton 回溯在任何输入上必成功。耗尽实际预算就返回完整失败。

科学调用必须同时满足 GITHUB_ACTIONS=true 和
GITHUB_REPOSITORY=Rogerhu12/math-research-public。
本地仅做过 AST/compile/重复字典键与尾空白检查，没有导入、科学求值或合成 fixture。

## 3. 两阶完整角导数

所有角 jet 都在最终同一个已读取的工作 $v$、同一端层规则上计算。
对单位 $n=N(y)$、$r=|y|$，
$$
DN(y)h=\frac{(I-nn^T)h}{r},
$$
$$
D^2N(y)[h,h]
=-2\frac{n\cdot h}{r}DN(y)h-|DN(y)h|^2n.
$$
该完整二阶式用于参考均值、方向和最终投影，没有漏掉法向分量。

第一角导数使用
$$
J_vv_\phi
=K_1-\sum_p w_pDN(Y_p)(1-\chi_p)T_{1,p},
\qquad
d_\phi=DN(v)v_\phi.
$$
令
$$
Y_{1,p}=(1-\chi_p)T_{1,p}+\chi_p d_\phi,
$$
$$
d_{2,\mathrm{known}}=D^2N(v)[v_\phi,v_\phi],
\quad
Y_{2,\mathrm{known},p}
=(1-\chi_p)T_{2,p}+\chi_p d_{2,\mathrm{known}}.
$$
则同一个 $J_v$ 给
$$
J_vv_{\phi\phi}
=K_2-\sum_p w_p\{
DN(Y_p)Y_{2,\mathrm{known},p}
+D^2N(Y_p)[Y_{1,p},Y_{1,p}]
\},
$$
并返回
$$
d_{\phi\phi}=DN(v)v_{\phi\phi}+d_{2,\mathrm{known}}.
$$
源实际重读这些一、二阶工作方程的完整残差，但没有把残差读数当作全角诱导算子上界或准确导数证书。

这里是固定参考的角导数，不是对当前全部外参数的反向传播模块。
数值迭代图没有被微分。若后继将此层变成每次当前外参数都变化的表示，必须另外实现完整输入依赖和 J/J*，不能只导入本函数就宣称已完成该链。

## 4. 五个完整中央分段与组合闭合

epsilon 的准确定义、五个准确端点、实际端点字、节点/权/形状数组摘要均记录。
五段分别是上升段、正平台、中央反向段、负平台和下降段。
每段使用完整指定阶数的正 Gauss 规则；没有略去短段、合并不同工作端点或把权和强制设为一。

以同一工作规则计算
$$
a(\lambda)=\sum_j w_j\cos(\lambda h_j),\quad
a'(\lambda)=-\sum_jw_jh_j\sin(\lambda h_j),\quad
a''(\lambda)=-\sum_jw_jh_j^2\cos(\lambda h_j).
$$
实际 $a(0)$ 是该规则的权和，源码没有假设它逐字等于一。
只有同一实际规则在 $(0,\pi/2)$ 给出原开区间 bracket，才在该分支二分。
每个角满足完整验收后冻结其实际值，其余角继续；
原预算未达不作为成功。

除了读取 $|a(\lambda)-|v||$，最终还必须实际满足
$$
\left|B+L_c a(\lambda)d-K_0\right|\le\text{tolerance}.
$$
不能由均值残差和幅度残差分别小于 tolerance，直接推断相加后的物理闭合也小于 tolerance。
本源使用全部三个物理分量的欧氏范数。二分会在原预算内继续，直到幅度和组合物理条件同时成立；否则如实失败。

中央横向积分按准确反对称 profile 的定义结构上为零。
因此本处组合工作读数是“实际 cosine moment 加结构零横向均值”的规则，
不自动等于另一条用工作节点逐向量读取完整中央 $T$ 的 Gauss 求和。
非 dyadic 边界与浮点映射可以破坏逐字反对称性。
metadata 明确区分这两种工作路径；真实后继物理场和 normal endpoint 仍须用它们自己的完整规则重新读取，所有准确积分与载体差都未在本核包围。

幅度角 jet 使用
$$
r_\phi=d\cdot v_\phi,\qquad
r_{\phi\phi}
=d\cdot v_{\phi\phi}
+\frac{|v_\phi|^2-r_\phi^2}{r},
$$
$$
\lambda_\phi=r_\phi/a',\qquad
\lambda_{\phi\phi}=(r_{\phi\phi}-a''\lambda_\phi^2)/a'.
$$
实际分支和负的有限 $a'$ 均读取；没有用预期理论值补成一个可除的分母。

## 5. 正确径向投影的完整三 jet

给定固定 world 径向向量的三 jet $e_0,e_1,e_2$，定义
$$
c=e_0\cdot d,\qquad q=e_0-cd,\qquad w=N(q).
$$
源码完整计算
$$
c_\phi=e_1\cdot d+e_0\cdot d_\phi,\quad
c_{\phi\phi}=e_2\cdot d+2e_1\cdot d_\phi+e_0\cdot d_{\phi\phi},
$$
$$
q_\phi=e_1-c_\phi d-cd_\phi,\quad
q_{\phi\phi}=e_2-c_{\phi\phi}d-2c_\phi d_\phi-cd_{\phi\phi},
$$
再用同一个 $DN,D^2N$ 得 $w_\phi,w_{\phi\phi}$。
它不在各角另挑特征向量符号，也不把 $e_r$ 换成反射下多一个取向号的 $e_\theta$。

工作域只读取实际有限/正归一化分母；本核未认证整个角圈的半球正隙、周期同支或投影分母统一下界。那些属于完整准确输入及其连续包围的责任。

## 6. 真实失败、来源和未付责任

SeedMeanFailure 的 record 保存实际 phase、坏角、计数、最后已计算的工作载体及其数组摘要。Newton 失败时，Jacobian 明确属于回溯前的同一点；最后试点、其实际 scale/可用性/残差另列，不把旧矩阵冒充最后拒绝点的矩阵。未计算量保留明确的 unavailable/nonfinite 表示，不填零，不生成完整场或成功声明。

原始控制和小矩阵只供 runner 原始输出恢复，不能直接当公开 compact summary；公开记录应保源码/参数/运行身份、实际成功或失败、完整角覆盖和必要标量。provider 还须绑定准确 scalar、参考输入、完整 K 定义、真实端层节点/权、中央参数与实际有限表示。跨输入的旧几何、旧闭合或旧 Phi 均不继承。

该源没有提供：

- 准确 $K,B,a$ 与工作积分之间的连续误差；
- 全角根包围、同支、参数导数或余量验证；
- 精确种子到有限 Fourier/共享 quintic 空间的误差；
- 原全部 Gram、幅度、embedding、reach 或物理全相位证书。

实际完整 provider 和原全部变量求解负责继续这些事项。源允许真正的新候选生成；任一失败仅描述这次实际数值路径，不能据此宣布准确构造不存在。

## 7. 静态复核范围

初体 efd1 的完整 $DN/D^2N$、两阶均值 jet、幅度与投影链由 construction 与 solver 独立文字核对；无所见漏项。
最终 bd9c 只更换均值数值策略和真实失败/计数记录，并明确结构奇零的工作规则范围。
construction 已完整核对相对初体的 diff，包括非对称矩阵乘序、角索引映射、真实 Armijo、不可用试点处理和同点矩阵归因，无所见阻断。

本地已实际通过 AST、compile、重复字典键和尾空白检查。
没有运行任何科学数值、方向检查或额外 fixture。
