# n4 固定全部物理参数的场校正接口及尾兼容债

维护会话：Astra-held10-1b6d88ec-20261120。

**状态：新增代数推导与可接入源码；源码尚未执行。** 本文没有重跑旧 n4 联立 96568，也不推断失联 18524、2919 的终态。现有 M20、核心同伦 .02 的真实有限尾与 metric 结果仍按原登记范围使用。本条给出在同一完整物理设计上进行后验精化的实际接口，不把一次矩形残差下降写成 README 第 5 条已经完成。

## 1. 先把原 fixed=True 的物理语义说清

原 `refine_fixed_raw_n4.py`、`refine_fixed_large_radius.py` 与 `couple_raw_actual_tail.py` 的 `fixed=True` 固定已解出的子午轮廓，包括 delta、vd 和真正物理分段；它们仍把

$$
p_0=\log(q_{\rm actual}/q_g),\qquad
c_j=s_jp_{j+1},\quad j=0,\ldots,M-2
$$

作为未知量。这里 q_g 是表示的固定 gauge，s_j 是已声明的物理控制尺度。原 M20 联立所以仍有 **q 与 19 个 c 的 20 个自由参数**。如果这些量改变，不能将新结果称为固定全部参数的后验精化。

design-only 对象的 p0 可以表示 delta 位移，p1 也可能表示 vd 位移，语义不同。必须先从实际解和原解释函数确定物理 profile、q、全部 c、核心设置、材料角图及真实切口，再在 fixed-profile 对象中重新编码。不能把旧 design 向量按同一数组长度直接当作 log(q) 向量。

本条的新接口 `FrozenPhysicalField` 接受已经完成这一步的 fixed-profile 对象。它复制 p，设为只读；所有场评价都使用这个同一 p。核心参数导数列不参与求解，也不为构造场 Jacobian 临时扰动 q/c。原 `Flow.fun_jac` 的场导数足够。

共同固定的对象为：完整 g 的定义轮廓和材料图、q_actual、完整物理 c、q_g、核心同伦与窗口/anchor 设置、切口与尾的物理定义、核心高度原点及最终 t 范围。参数化或网格的数值评价精度可以提高，但不能借此重新选择这些物理量。最终全 t 闭曲面的收敛仍须另外支付；当前带边前缀不能满足它。

## 2. 完整 lift 的系数不能与核心同伦 .02 混淆

[R47](../results/R47-fixed-slot-nested-circle-homotopy.md) 提供固定控制定义下的补零嵌套；[R48](../results/R48-exact-reference-compensation-for-mode-extension.md) 提供完整参考补偿；[R49](../results/R49-frenet-mean-invariance-under-exact-reference-transfer.md) 支付共同完整场下的 Frenet 正根和均值原函数身份。此处直接使用它们，不重新证明已经登记的结论。

n4 现用 [exact_core_lift.py](../scripts/even_circle/double_prefix_first/exact_core_lift.py) 在完整场中加入

$$
h(s)\bigl(\Gamma-b-q_g\mathcal B_M I_M\bigr),\qquad h=a\chi .
$$

源码没有在此再乘核心同伦参数。故 R48 的 **reference-lift 系数在这个入口为 1**。核心的 $\lambda_{\rm core}=.02$ 仅参与固定 $\Gamma$ 的定义；不能把它乘到转移补偿中。升至 N 模的正确连续初值是

$$
Z_N=E_{N\leftarrow M}Z_M+a\chi\,
 (I_N-E_{N\leftarrow M}I_M). \tag{1}
$$

其一、二阶物理 s 导数同时使用 $(a\chi)'$、$(a\chi)''$。按实际 $[R_0,R_1,\ldots,R_M,T_1,\ldots,T_M,Z_1,\ldots,Z_M]$ 三块嵌入，不能在整条状态数组后简单补零。原实际有限投影 I_M、I_N 均保留，不假设它们是精确 Fourier 积分。

固定旧 raw anchor J，原控制逐列保留，新增物理 c 严格设为零并保持零。R50 的控制空间稠密性允许逼近函数空间；它不授权在“固定这一核”的测试里重新优化新增控制。

式 (1) 是连续初值身份。节点取样、生成新的 cubic/quintic 后并不自动保持整个旧物理图。若原入口本来有有限边界残差，随后把入口节点设为新 I_N 是一次明确的场校正，应报告其大小；不能继续声称校正后的整图仍与旧图严格相同。

同理，R49 只对转移前后的相同完整场保持同原点的 mean primitive。场校正之后必须按新完整场重新运行原 `height_integral`，保持同一个入口高度常数。不能把 mean 当作新增自由参数来调平接缝。

## 3. 真实冻结后的变量和全部方程

设 K 为径向节点数，n=3M+1。原联立离散有

$$
n(K-1)\text{ 条 collocation},\quad
n\text{ 条完整入口},\quad
M\text{ 条真实非线性 DN}.
$$

未知为 nK 个场值与 M 个核心参数，因此原平方系统确实闭合。冻结所有 p 后，将入口直接消元：

$$
Y(:,0)=I_M(p_*).
$$

仅余 n(K-1) 个场未知，而保留 n(K-1)+M 个原方程。这 M 条多出的条件是固定核对真实尾的兼容要求，不能删除，也不能把新 c 当作无物理意义的“精化变量”。

“两高度定支”有两种明确的声明：

- H4、H8 仅用于先前寻找分支，而完整物理核已经冻结：H 是场的派生输出。此时不额外冻结 H，但必须用它的实际当前全向量求真实尾。
- 若 H4、H8 本身也被声明为固定的分支坐标，则永久设
  $Y_{z,j}(1)=H_j^*/(\sigma q_g)$，再消去这两个场坐标。**所有 M 条 DN 仍保留**，方程盈余为 M+2。

不能用两条 H 条件替换两条真实 DN，然后把结果称为原完整尾问题已经接受。新接口支持第二种明确选择；不传 `fixed_heights` 则为第一种。

升模式数会同时增加场方程、场未知和对应尾条件；不是凭空获得可调的物理边界自由度。因此加密能否收敛是要实际测量的数学问题，不能由维数变化预先宣告。

## 4. 可直接实施的矩形场校正

新源码：

- [frozen_physical_field_refinement.py](../scripts/resume_n4/frozen_physical_field_refinement.py)

给定固定对象及当前场，它按原 SciPy collocation 规则组装原残差，并保留完整参考 lift、正根分支、节点/中点和原 RMS 两个额外 Lobatto 点的域条件。它只取 Jacobian 的场列，丢弃恒为零的物理 p 列；入口已恒等满足，所以把恒零入口行消去。

真实 DN 值与场导数逐式采用原 `db6f-prefix-coupled.py::TailMixin`：

$$
H=\sigma q_gY_z(1),\qquad
T(Y)=\frac{q_g f_z(Y)-{\rm slope}(H)/\sqrt{E_{\rm cut}}}
                {{\rm bcweights}},
$$

$$
T_Y=\frac{q_g f_{z,Y}
 -(\sigma q_g/\sqrt{E_{\rm cut}})\,
 D_H{\rm slope}\,P_z}{{\rm bcweights}}. \tag{2}
$$

其中 H 包括全部 M 个实际分量。源码要求真实尾返回 converged 且原 residual 不超过 2e-9；原临时 AffineTailForInnerBVP 缺少这些真实接受字段，因此不能被冒充成这里的永久尾响应。

一步校正求

$$
\min_{\Delta Y_{\rm free}}
 \|W(r+J_Y\Delta Y_{\rm free})\|_2,
\tag{3}
$$

使用稀疏 LSMR 和显式列尺度，然后进行原域内回溯。行权重在这一轮回溯中固定；对 collocation 用
$\sqrt{\Delta x}/[\Delta x(1+|f_{\rm mid}|)\,\tau_{\rm ode}]$，避免仅因区间变短而把同一个 ODE 缺陷误判成收敛。真实 DN 使用声明的原 bc 容差归一。权重只选数值校正方向，不改变最后任何原门。

每个候选只改自由场节点；入口和可选两 H 在每次评价前直接恢复其定义值。没有附加 ODE forcing、没有可调 mean 常数、没有增加核自由参数。回溯允许拒绝原 Frenet 域失败或真实尾失败的候选。其他程序错误仍应由调用者记录为运行错误，不得当作物理结论。

返回的 `accepted_step` 仅表示这一次原域内加权残差下降。它不表示 BVP 已解出，也不表示全 metric 或 README 通过。LSMR 迭代到限和原残差都逐项报告，不能把线性求解的停止码替代几何验收。

### 接入已有真正原尾对象

以下代码应放在实际 runner 已构造 obj、par、x、y，且 obj.tail 是原真实 WeightedTailPort 之后。它不重新运行旧计算，也不依赖已失联数组。

```python
from types import SimpleNamespace
from frozen_physical_field_refinement import FrozenPhysicalField

frozen = FrozenPhysicalField(
    obj, par,
    # 若这两高度是本次物理分支的固定参数才传入：
    # fixed_heights={0: H4_fixed, 1: H8_fixed},
)
candidate = frozen.correct_once(
    x, y, ode_tolerance=1e-8, bc_tolerance=1e-8,
    lsmr_maxiter=120, max_backtracks=4,
)

# 此处仍只是一个场候选。保持同一 p，生成原物理 C2 表示。
s, ds = obj.chart(candidate.x, candidate.p[0])
physical = SimpleNamespace(x=s, y=candidate.y, p=candidate.p)
flow = obj.flow(candidate.p[0])
physical.sol = flow.c2_interpolant(physical)

# 对刚生成的实际表示重新跑原完整审计。
prefix_audit = adaptive.audit(obj, physical, 512)
tail_seam = obj.seam_audit(physical)
```

这里的物理 quintic 与校正过程的 normalized cubic 是不同有限对象。实际导出的 quintic 必须接受它自己的全角 metric、原 mean-height 积分和两 jet 审计；不能把 cubic 的 RMS 当作 quintic 的误差界。

这是一轮函数接口，不是新的自动“成功” runner。调用者可在实际下降且全部原域仍成立时继续场校正或按同一物理图增加节点/频率。每层须分别记录原 full metric、真实 DN、尾残差、mean/nonmean 两 jet；仅当完整误差随加密实际下降，才积累 README#5 证据。

**资源范围：** 上例最多一次场 collocation Jacobian、120 次 LSMR 迭代，以及基点值/Jacobian的两次真实尾请求和最多五次回溯尾请求；客户端相同 H 缓存可减少实际工作。当前尚未执行；实际运行时分别记录请求数与返回，使用独立工作目录。全场数组仅暂存运行目录，不进入 Git 或 CI artifact。

## 5. 精确线性兼容公式，比“少了 M 个未知”多一步

先暂不消去可选末端 H 坐标，只消去固定入口。记 E 为全部 collocation 残差，T 为全部真实 DN；若两 H 固定，把它们的实际残差也加在 T 后。对当前场：

$$
A=E_Y,\qquad C=T_Y,\qquad r_E=E(Y),\quad r_T=T(Y).
$$

若方形 A 可逆，为一阶消除全部内部缺陷所需的唯一场修正为

$$
\Delta Y=-A^{-1}r_E.
$$

其剩余尾兼容债恰为

$$
\boxed{\eta=r_T-C A^{-1}r_E.} \tag{4}
$$

因此同一冻结物理设计的一阶全方程能够同时置零，当且仅当 $\eta=0$。原始尾残差小不代表这个条件：内部场缺陷对尾的反馈 $C A^{-1}r_E$ 仍可能主导。这里既没有允许 q/c 变化，也没有把 Schur 公式的核心参数块误搬成自由度。

更明确地，令 $L=[-CA^{-1},I]$。有 $L[A;C]=0$，故任何场线性校正后 $L(r+J\Delta Y)=\eta$ 不变。对已选定的有量纲一致的行尺度，这给

$$
\|r+J\Delta Y\|_2\ge \|\eta\|_2/\|L\|_2. \tag{5}
$$

若记 $D=CA^{-1}$，无权线性最小二乘的最小平方残差为

$$
\eta^{\mathsf T}(I+DD^{\mathsf T})^{-1}\eta. \tag{6}
$$

证明可令 $e_E=r_E+A\Delta Y$，则 $e_T=\eta+De_E$，最小化
$\|e_E\|^2+\|\eta+De_E\|^2$ 即得。带权情形先同时对 E、T 与其 Jacobian 应用相应固定权重，再用同一公式。

这些是精确线性代数恒等式。它们不说有限非线性问题没有解，也不保证 A 有良好数值逆。高频初值推进可能使 A 极病态；源码的可选 `compatibility_debt` 只做一遍 sparse LU 并同时报告真实线性求解残差，不把浮点 eta 当作严格下界。A 不可逆或解失稳时，应报告这个互补选择失效，不能给出固定设计不存在结论。

对于可选两 H，C 的额外行就是固定 endpoint 高度的真实场导数 $\sigma q_g P_{z,j}$。它们不是新可调列。因此式 (4) 也直接检测“消掉内部缺陷会不会迫使已固定的两高度移动”。

## 6. 加密之后怎样判断下一步

在一个已经满足原全部有限门的候选上，先冻结本条列出的完整设计，然后从式 (1) 的连续参考转移开始：

1. 增加径向分辨率，记录实际物理 quintic 与原完整 metric。若误差仍主要来自径向表示，这个场校正接口应能降低它，而 p 始终相同。
2. 增加角向状态频率和评价/求积精度。原物理核由旧控制加零保持；新增状态允许表示新的场修正，其原方程和新实际尾分量同步加入。
3. 原真实尾按同一物理尾的数值定义加密步数、射击分段与角频率。若改变了实际切口、轮廓或物理尾定义，就不是这一固定设计的后验加密；若改变数值截断深度，须明确它对应同一个预先定义的连续尾，而不是换了物理目标。
4. 两 H 若固定，始终保留相同定义值；不固定时记录其随数值精化的输出变化，不反过来用它调 q/c。
5. 如果场残差、原 full metric 或兼容债出现稳定误差底，则这个具体候选尚未取得 README#5 的收敛证据。可以返回设计阶段寻找新的候选，但新设计应另起序列，不能把换参数后的下降接在旧序列上。

有限 c 向量解出某一离散 BVP，并不自动等于一个完整无限维可闭合核。已登记 M20 的 metric 通过是有限候选的事实；本方法不会从该事实额外推导固定全参数精确解存在。也不能由一个前缀的收敛推出全曲面、全 t、闭合、reach、握持比例或 Euclidean 除刚体变化量。

## 7. 已核的源码依据与执行边界

本条使用现有 `refine_fixed_raw_n4.py` / `refine_fixed_large_radius.py` 的 p 解码，`exact_core_lift.py` 的完整 h=aχ lift，`analytic_adaptive_core_jac.py` / 原 Flow 的场 Jacobian，以及 `db6f-prefix-coupled.py::TailMixin` 的真实尾公式。R47–50 是此前已登记结论，本条只接上它们没有提供的冻结参数残差校正接口。

`frozen_physical_field_refinement.py` 在执行环境失联期间写成，尚无 Python 导入、实物 Jacobian、BVP 或几何测试结果；函数调用示例是下一实际入口，不是已发生的命令。原未知作业状态不变。源代码和本文可提交；任何再次求得的全场、矩阵和尾 stage 数据继续只用于临时运行，按根 README 第 15 条处理。
