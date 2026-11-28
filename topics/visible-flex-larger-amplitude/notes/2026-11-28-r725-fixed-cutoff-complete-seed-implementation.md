# R725 固定 epsilon=1/8 端层 cutoff：完整 seed 实现与必要接线

2026-11-28（UTC）。本包交付一个完整独立 seed 源、一个完整原文再生器，以及实际下游修改清单。它实现已登记 R725 的三片端层函数，保留原 paired-halfwave 中央机制。**仅该 seed 已构造；新上层科学入口和新准确费用还没有在本包中构造或执行。** 不把新源码准备或符号系数当作 reach、位移或均值根已经改善。

后续首个科学比较的参数按根指令是原完整半波 $b/S=1/2$、$\delta=1/32$、同一固定 $g$ 与同一初始 $H$，其余参数、全部变量和32 normal阶段保留。epsilon 固定为 $1/8$，无需增加科学 CLI 词。run25 的缓存/观察新上层由其他工作负责；本包没有复制尚未锁定的上层来源，也没有改动任何活运行、refs 或队列。

## 1. 完整原件与新件

完整父 seed：

- 路径 scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_reference.py；
- 43697 B，SHA256 cec7f1a297851c43bb5db4174d3a15d7d1a40eb1683b145d1f845aff732d10f0；
- Git blob cc877246e546b8294826ad38d33b3eb2f7434f25。

新完整 seed：

- 路径 [fixed_fejer_paired_halfwave_flat_cutoff_meridian_reference.py](../scripts/resume_20261126/fixed_fejer_paired_halfwave_flat_cutoff_meridian_reference.py)；
- 51540 B，SHA256 1533deac6485f4b7fc065d4e40ed23ef0220ebb1800e868a518fd27ec623616f；
- Git blob b37f930874dd9b874d58120a2d9fe86031146ccb；
- schema 为 complete-fixed-fejer-paired-halfwave-flat-cutoff-meridian-seed-reference-v1。

完整再生器：

- 路径 [reproduce_fixed_fejer_paired_halfwave_flat_cutoff_seed.py](../scripts/resume_20261126/reproduce_fixed_fejer_paired_halfwave_flat_cutoff_seed.py)；
- 16949 B，SHA256 4a2f0b313decbc8cf8ee997fbb598254e83c2a93cbdb1a3b21430b83a0bdf4b7；
- Git blob 21980d71c0985429d6d226475dbcbee5aae195d9。

对应证明为
[R725-fixed-width-boundary-cutoff-and-curvature-decomposition.md](../results/R725-fixed-width-boundary-cutoff-and-curvature-decomposition.md)。
准备时完整稿30079 B，SHA256 f40eb810c7c5c15583155335756a2ef3aa2c60155f319b6943725906e6171bc3，blob872fda9c48d04db1e3b45bd855b041f5226ab002；运行源没有把某个公开论文路径当作科学输入。

## 2. 明确的准确定义与工作求值

新常量 BOUNDARY_CUTOFF_EPSILON="1/8"。完整定义 schema 是
complete-fixed-width-three-piece-C3-boundary-cutoff-v1。

保持 R725 全式：

$$
G(u)=\frac52u^4-3u^5+u^6,\quad
C_\epsilon(t)=
\begin{cases}
\epsilon G(t/\epsilon)/(1-\epsilon),&0\le t\le\epsilon,\\
(t-\epsilon/2)/(1-\epsilon),&\epsilon\le t\le1-\epsilon,\\
1-\epsilon G((1-t)/\epsilon)/(1-\epsilon),&1-\epsilon\le t\le1.
\end{cases}
$$

外部常延拓为0和1。四个 API 的职责如下。

| API | 实际职责 |
|---|---|
| _flat_cutoff_polynomial_jets(t,epsilon) | 一个完整三片代数体，使用整数常数；Fraction 输入得到精确 Fraction，float 输入进行工作浮点运算 |
| boundary_cutoff_exact_jets(t) | 只接受 canonical rational string 或 Fraction；epsilon 固定1/8；返回值及归一化坐标前三导数 |
| boundary_cutoff_working_jets(t) | 对完整 finite t∈[0,1] 求同一三片的四个工作值，保有限性/范围检查 |
| boundary_cutoff_definition(support,central) | 重建全部准确系数、0/epsilon/1-epsilon/1端点jets、四层方向、12物理boundary片和8个新内cut |

R725 中的准确函数系数是有理数；除法中的 $8/7$ 等不因工作 float 求值而成为新的 dyadic 准确定义。工作舍入仍明确未包围。分支点本身两侧值和前三导数一致；新代码以中片处理两个内部等号，端点常延拓处理0、1。

右端层仍使用 $C_\epsilon(1-t)$。其物理奇数阶导数带负号、偶数阶带正号。新的 definition 保存 odd_material_derivative_orientation；实际 seed evaluate 需要的 $\chi_s$ 在右层使用负号。全端口jet表同时保存准确0–3阶，不声称四阶连续。

原 _S5、_S5_prime、_profile 和 paired_halfwave_definition 函数完整原字保留。中央仍使用原 h_delta(t/2)、正负两段、六片每段和原链因子1/2；本包没有全局替换任何 bubble、gamma 或 lift 的 smoothstep。

## 3. 参数与物理模型身份

SeedParameters 最后增加 boundary_cutoff_epsilon，默认固定 "1/8"。definitions 对其作 canonical rational 读取并严格要求等于1/8；原八项返回 tuple 和原所有参数约束不变。因此现有使用关键字的完整构造器不需增加 CLI 参数，也不能静默选择另一个 epsilon。

新 model 顶层增加：

- exact_boundary_cutoff_epsilon；
- boundary_cutoff_definition。

working_definition 增加完整同一 definition、准确 epsilon、旧边界 quadrature/root/cache 不继承声明和外层 whole-cell规则独立声明；schema 改成 paired-halfwave-flat-cutoff-reference-working-definition-v1。模型 canonical identity 因真实新来源和物理定义而变化。没有仅凭旧点向量的同一 SHA 声称场相同。

原 dataclass 的历史 width/profile 默认值没有顺带改动。后续完整科学 argv 必须像原半波 bhalf ready 一样显式传入 --seed-boundary-total-length 1/2 和 --seed-profile-delta 1/32。此处不删除任何原157词、数值预算或仍需继承的历史责任。

固定原 reference source e717、scalar/a、Fejer参考图、M160/N2048/J923、mean source f848、原 support、所有外层 core/三通道 omega/H 自由坐标的接口保留。本 seed 的原 constructor 全输入/source/模型/完整core/H字等号没有放宽。

## 4. 切点进入真实 mean 计划

_prepare_plan 原先已有全部 context.nodes、support/boundary边缘以及中央半波六片切点。现在对每个 support 再加入

$$
a+\epsilon\Delta,\quad a+(1-\epsilon)\Delta
$$

的两个左层内部切点，以及右层的对应两个切点。两 support 共八个新内cut，全部为准确 Fraction affine 地址。集合与原所有切点取真正并集后，仍用原 _compare、原 original_cell 检查和完整正宽度规则。没有通过近似 u 或近似距离合并地址。

每个实际 boundary piece 记录：

- boundary_cutoff_piece_index（0、1、2）；
- boundary_cutoff_branch（按材料发现次序的准确三片名称）；
- odd_material_derivative_orientation。

逐piece还检查其左右准确地址位于相应 cutoff 分片内，跨越真实内cut就失败。中央仍记录原 node_count=0，因为原辅助 A_delta 负责其完整均值；外部和每个 boundary 子片都使用原 radial_quadrature_order 的全部正权 Gauss，所有真实节点和权重进入 boundary_values/boundary_weights/boundary_chi。

**分片后工作 boundary 节点/权重及调用次序可以改变。** 保留的是原完整每片规则与域，不伪称旧 Gauss 点数组、旧均值根、旧当次闭合词仍相同。原补集和准确 K 的定义不变，但本包也没有以纸面同式代替工作字节结果。

新计划 schema 为 complete-paired-halfwave-flat-cutoff-seed-radial-plan-v1。它保存完整 boundary definition、epsilon、8个内cut和12物理boundary片的声明，并保原全部 arrays/pieces/nodes 的真实身份、source/model绑定和原失败语义。

## 5. 准确 B、根与两角 jet 的实际调用

_means 全函数原字保留：它将本次完整 plan 的 boundary_chi、全部 boundary_values/weights、原 K0/K1/K2、原中央总长和原迭代/回溯/tolerance/scalar预算传给 f848.solve_mean_jets。新对象初始化为空的实际 mean/radial cache；没有从旧provider导入根。

evaluate 全函数原字保留：端层的
Y=(1-chi)T0+chi*d，
Y_s=(1-chi)T0_s+chi_s(d-T0)
和完整两角归一化公式都沿原执行。唯一实际差异由 _cutoff_and_profile 的左右边界两处返回值引入。中央半波与所有补集值的公式原样。

f848 的完整三向量 Newton/角jet与原十二片 A/A'/A'' 规则仍可共享原字，因为其 API 接收实际 cutoff 值，不要求它们只能来自 S5。新 B 变了，实际 r/d/lambda 及其两角导数仍需真实重算；原 R709 粗条件、R722 posterior 或连续几何未被填 true。

## 6. 准确费用必须修改的真实位置

这不是“只换 pins”的适配。以下位置已经按当前已锁半波完整源读清。

### 6.1 完整输入与 R722 source scope

当前 input：
fixed_fejer_paired_halfwave_normal_packet_accurate_field_input.py，
39751 B / e71ad557ce20cdb147cb259b3fe66aa5b8ccb144fe57cb0586a3822c705d98de，
blob9b25e54fbd4b504494638766b14d899934f4aa3c。

当前 posterior：
fixed_fejer_paired_halfwave_R722_posterior_mean_jets.py，
57884 B /1048f2d0457721664a04c9d4cd0ececa538accbc85d48a6dbe24c468c86f9a2a，
blob4df602ed5f17b74a7d1d8eaea98e13749465034b。

两者的 paired_halfwave_seed_scope 当前严格绑定旧 seed/schema 和 paired-halfwave-reference-working-definition-v1。新完整体须明确接新 seed/source/schema，并重建、逐字段核对整个 boundary definition；仍保 seed 与 base/normal 完整对象及其 canonical identity 全等。原函数返回的中央 physical definition 可以保其原职责，另外增加独立 boundary-definition identity，不能把12个boundary片混称原12个中央片。

complete_paired_profile_moment_enclosures 的物理来源 guard 也需接新完整 seed；其原辅助 A 数学正文可保。validate_root_domain_attribution 必须对新几何 identity、新完整分片与新 B 残差进行原严格重算。不得把旧 R709 bool 写 true，不可用工作保存的 d 代替准确归一化候选。

纯源提取若需要重建本包的 cutoff definition，完整依赖为 BOUNDARY_CUTOFF_EPSILON、BOUNDARY_CUTOFF_SCHEMA、_flat_cutoff_polynomial_jets、boundary_cutoff_exact_jets、boundary_cutoff_definition、exact_fraction，以及原 Fraction 别名 F。它们只作准确代数/定义；不调用工作 field/mean/root。

### 6.2 WholeMean 中仍有真实 S5 专属函数

当前准确 radial：
fixed_fejer_paired_halfwave_R722_accurate_reference_control_radial_boxes.py，
50745 B /2baef8e83025dee6e0b74f8084e0d055a7cd15a091599cf5b343ff97b4f2963f，
blob5f92e643f7b331c88c3d5af068429ba8bb597af0。

reference_mean_adapter 内部的 WholeMean 继承 ae67.ActualMeanBatch。原 parent.cutoff(left,right,kind,index) 直接以 S5 的端点值生成准确 cutoff 盒；因此只增加种子 cuts 或只改新 source pin，仍会积分错误的 B。

独立新 WholeMean 必须覆写这一个准确 cutoff：根据完整同源 epsilon/三片定义，对准确归一化区间给 C_epsilon 的完整有理单调端点包围；其 make_plan 同时加入全部八个内cut并保原context节点/支持/中央/完整尾。原 leaf、assemble_sums、三分量0/1/2角积分可以继续委托原完整数学体，不能跳过新模型或完整域绑定。

原 ae67 literal CLI 及其 strict 来源职责保留，不在原件上偷偷允许新来源。

### 6.3 Physical radial 与纯读流的切点义务

新 AccurateFieldGeometry.make_plan 必须增加八个准确内cut、完整boundary branch归属及同定义identity。AccurateFieldGeometry.cutoff 的值和材料一阶导数须改成完整三片有理外包，再按实际右层方向与 delta*S 缩放。

不能全局替换当前 _s5：bubble_piece 和 lift_piece 也使用它，必须保原字。reference_piece 的完整归一化、两角jet与 Ts 公式可保，AccurateAngleOracle 的所有32阶段/旋转/积分/物理六jet公式可保，但接收的新边界值必须真实。

当前 leaf 的 validate_paired_physical_plan 只逐一核原中央六片。后继须另核四boundary的8内cut确实在原完整plan边缘、所有boundary leaf都归属其准确片且不跨cut，同时保原中央检查。geometry identity、input identity、normal journal/source records及最终全字 recheck必须包含新boundary definition。不能用“所有cuts已列出”的单一bool代替逐流检查。

原 1024整圆角胞、全部径向/尾段、全部32 normal stage/root包含/周期glue、物理6jet、原R717同leaf三维Dnorm、R723全闭相位/帽/mixed和R716主副件晚失败合同都保；本包没有声称已完成这些后继源。

## 7. 科学来源级联的最小范围

待run25最终缓存/观察族全锁后，新上层可以按真实依赖接入本seed，不先复制中间driver家族。真正的来源范围是：

1. 新 seed 的 source/schema/model；
2. base 对 seed 类/source/schema的严格绑定，以及Q定义、reference calibration 的相应完整模型/source依赖；
3. 依赖base、calibration和normal完整来源的各下层guard、packet/source binder；
4. 最终driver/reader/launcher与完整source registry，保持原所有source pair和原typed/history；
5. 上节明确有数学变化的准确 mean/radial/input/leaf，再递归normal/G/closed/moment/mesh必要源。

哪些新run25纯缓存体可以原字共享，必须以其真实终锁依赖表判断；这里不预填还未读取的schema/pin。对原字共享的数学核，不为换名字另造字节副本；对真实source guard需变的体，则完整派生，不删守卫。

## 8. 外层 working Gauss 的准确边界

本 seed 的新 mean 计划已经真实含新cuts。原外层base integration_query/_integrate、每whole-cell Gauss及partial Lagrange没有在本包修改。它们不会因为 seed metadata 多了cut而自动采用同一细分；旧工作字或积分误差也不因此变为精确。

如果后续科学沿用原预算和外层规则，说明和准确消费者应如实保这个事实，由完整新准确物理积分支付误差。若后续明确改变外层积分分片，则须另有完整实际源码/参数/预算定义；不能把这个额外变化藏在本次“只改cutoff”里。

## 9. 完整再生方法与实做范围

标准库再生器的完整参数是：

~~~text
python3 scripts/resume_20261126/reproduce_fixed_fejer_paired_halfwave_flat_cutoff_seed.py \
  --parent-source scripts/resume_20261126/fixed_fejer_paired_halfwave_meridian_reference.py \
  --output-directory generated-r725-seed
~~~

它读取完整43697字节父源并核whole SHA，应用16个完整精确文本patch，核完整51540字节目标SHA，反向逐patch还原全部父字节后写独立basename。不会import科学源、AST/compile或运行数值fixture，也不是新增科学准入步骤。

本次已在V8源文本构造中实际应用这16个patch并反向逐字恢复父全文；没有执行再生器Python、没有AST/编译或科学。完整PATCHES正文在16949字节再生器内，不以简略diff代替新51540字节运行体。原源留原路径，所有新件由独立Git blob保护。

本包不填新的run ID、模型/点/mean/packet/final/费用结果。当前已有半波的有限统计和曲率缺口只是选择此构造方向的背景，不能被写成新cutoff已经成功的证据。
