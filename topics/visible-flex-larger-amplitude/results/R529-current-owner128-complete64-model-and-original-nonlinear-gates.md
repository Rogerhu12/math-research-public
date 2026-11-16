# R529：同次128最终解、完整64阶段模型与原非线性末门的分责

作者：ChatGPT /root（AI）。日期：2026-11-16 UTC。

**可信度：纸上证明与实际源码的数据依赖核对。** 本文证明完整阶段模型可以作为明确的近似线性模型，与同一当前H的原128值、残差、重放和物理审计分责；证明原affine内层在重新绑定当前非线性值后，其末端值检查不由旧模型误差代替。本文没有执行新科学程序，没有给出新native、FD、fullDN接受、耗时收益或闭曲面。拟用的完整64矩阵尚须真实来源组合、实际调用与原全部验收；不能把本文当成现有R501/R527已经改成此方法。

## 1. 具体缺口与现有入口

[R486实际215](R486-actual215-complete-necessary-readback-and-stage-audit-budget-partial.md)已返回同一当前H的persistent128末解和完整fresh replay，原norm从约1.22096e−4降到9.68582e−11；stage独立8000秒预算只完成478/576段，audit独立1800秒只完成574/576段。boundary与endpoint因stage前件不全没有开始。这说明该次实际未完成部分在末解之后；它不证明所有未来输入都以相同方式受限，也不许可抬原component cap。

本条针对其中完整stage线性模型的成本。取**这个实际当前H的完整最终128状态**，逐字一次RN64，再重新形成全部576段、每段全部224输入方向和226输出；让其成为明确声明的近似模型。实际非线性值和接受依据仍由这个H的128末解、fresh replay、128物理读出与独立audit承担。这里没有复用初始capture的旧J，也没有拿另一个H的J作当前J。

原完整fullDN实际源[geometry_20261114_full_dn_solve.py](../computations/geometry_20261114_full_dn_solve.py)，30017 B / c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162，在outer anchor、候选最终height和最终audit三处均真实调用jacobian=True。因此“给无J请求省掉末J”不触及本入口的这三个请求。当前方法必须真正完成并返回新的全338×112模型，不能只加noJ分支或把缺失矩阵伪装成可用response。

原FD围绕当前affine boundary检查实现的一致性；它不是独立测量原非线性DN导数的证书。这个事实在第7节直接证明，并不撤掉原FD门。

## 2. 四种对象必须分别绑定

固定一次真实call及其原输入。记M=112、K=224、d=576；H为原输入的112个完整binary64物理height字。下表每一行代表不同对象：

| 对象 | 全部范围 | 来源与角色 |
|---|---|---|
| X | (d+1)×K，即577×224个binary128字 | 当前H的实际owner最终状态；原128 residual与fresh replay的对象 |
| Xhat | 同形状577×224个binary64字 | 对X逐字一次RN-even投影；只作当前模型的取值点 |
| T_n | 每段226×224个binary64字 | 实际已加载同一DN各cell.engine在Xhat[n+1]的完整原切向程序输出 |
| A_n、C_n | 分别224×224及2×224 | 原port变换后的shape模型和原两mean响应 |
| G | 112×112个binary128字 | 在所有新A_n上完整far-to-cut QR形成的当前近似Pi/Q图 |
| V、J | 原338值及338×112模型 | V在X的实际cut节点用128物理程序求；J按原mixed读出规则以新G形成 |
| audit | 原576段及其全部query/advance/角行 | 从X各真实128节点独立重新开始，仍由原128程序执行 |

Xhat不是另一个已通过原128容差的解。投影后的64值程序可以有自己的残差，但该残差只作明确标记的diagnostic，不能覆盖owner的norm、below_original_tolerance、原fresh replay或response.converged。T_n也不因名为tangent就成为精确数学导数或原128阶段程序的逐字复制。

“同一次”至少包括原run/attempt/source、call number、当前H完整字节、capture snapshot/context/manifest、原packet与physical packet、实际owner source及final state、fresh replay、实际原deadline。只相同shape、同一个文件名或相同简写hash不够。[R493](R493-current-H-live128-response-projection-and-original-fullDN-interface.md)、[R501](R501-live128-original-full112-same-call-executable-composition.md)已有这些实际来源义务；新模型的不同精度不能取消它们。

## 3. 完整投影与精确升精度

对每个实际128字定义

$$
\widehat X_{nj}=\operatorname{RN}_{64}(X_{nj}),
\qquad 0\le n\le d,\quad 0\le j<K,
\tag{529.1}
$$

其中RN64是对整个准确dyadic值的一次nearest-ties-to-even，保signed zero。用已发表[整数投影库](../computations/exact_20261116_binary128_live_response_projection.py)，19902 B / b2336bcf56ba294efd1ba19e02b5d9acaedebb6eb669489fa1d869be7259626e，而非先转十进制文本或借原截断binary64中间状态。其streamed数组接口会检查真实同job路径、完整字节数、全字数和读完全文件后的SHA；不能只用调用前stat当完整内容绑定。

该库对非有限128输入报原错误；有限128溢出到64时产生真实infinity字后由finite requirement报错，不饱和截断。部分输出及已完成计数仍是partial，不可补成全577×224。库原接口docstring曾为可选predictor用途；本文提出的是新的显式用途，必须以新调用者和来源声明接入，不能声称旧predictor流程已经自动执行本文方法。

**引理529.1（有限binary64字的准确binary128嵌入）。** 每个有限binary64值可在binary128中准确表示。按完整二进制字实施的升精度不增加舍入误差，并可保两个零的符号。

**证明。** 非零binary64是至多53位significand的整数乘二次幂；normal和subnormal的所有指数范围都包含在binary128范围内，且53≤113。故其准确dyadic值属于binary128可表示集合。零另保原sign bit即可。没有从十进制近似值反推二进制的步骤。证毕。

这里“准确升精度”只说已经形成的64字，不说其与原128计算结果相等。一般地

$$
\operatorname{embed}_{128}(A_n^{64})
\ne A_n^{128}(X),
\tag{529.2}
$$

因为取值点、根求解、局部切向算法、每次乘加与port除法的精度均可能不同。没有误差估计就不能把式(529.2)中的差叫作机器epsilon量级。新模型必须以自己的method/schema/source明确保留这种差别。

## 4. 每段完整64模型的精确定义

固定实际已加载DN的第n个cell。它的engine、profiles、原stepsPerSegment、真实cusp integrationBreakpoints、mu、portRatio及全部原配置必须仍属于第2节的同一当前问题。初值为

$$
y_n=(\widehat X_{n+1,0},\ldots,\widehat X_{n+1,K-1},0,0),
\tag{529.3}
$$

由实际原cell.engine.flowStateWithJacobian在全部原profiles上返回完整state和tangent。这里两mean初值为零，不表示两mean的输出或224方向导数为零；必须保存全部226输出和两mean行。

原[78718-tail-tangent-core.mjs](../../visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs)的cellFlow先建立K+2状态、复制224输入，再调用本实际engine。它把返回前224状态的后112项除以cell.portRatio；全shape矩阵的对应112行也按相同原除法形成。令p_n为这个实际portRatio；用“按原binary64算式形成”的记号，

$$
A_n[i,j]=
\begin{cases}
T_n[i,j],&0\le i<M,\\
T_n[i,j]/p_n,&M\le i<K,
\end{cases}
\qquad
C_n[a,j]=T_n[K+a,j],\quad a=0,1.
\tag{529.4}
$$

每个j都取0至223，n都取0至575，不删列、模式、mean或stage。原port若不在实际合法/有限范围，按原失败责任记录，不能为了形成模型另行夹取p_n。原wrapper只保shape J和meanHeight之和；新完整模型库需要在真实full tangent返回处同时保before-port226×224、after-port224×224及两mean行，不能从被wrapper丢掉的行凭空恢复。

原product-flow的循环在每个原分段及cusp网格上执行完整四场RK，并分配226×224的tangent，初始前224行是identity、末两行为零。R523等已发表有限乘积实现若是实际已加载engine的一部分，其真实source与计数仍须绑定；不得为了使用本定理而把engine换回另一份较小或较便宜的算式。本文把T_n定义为**实际完整有限切向程序**的返回，不以符号D把尚未证明的IEEE roundmap导数写成前提已付。

**命题529.2（完整模型的来源与尺寸）。** 若第2节来源条件成立，式(529.1)的全部投影以及式(529.3)–(529.4)的全部实际cell调用完整返回，所有原finite/domain要求满足，则得到每段全224方向、226行的明确有限模型及其两个mean行；它只依赖这次X的投影和这次真实DN对象。完整升精度后的数组是这些实际64字的准确嵌入。

**证明。** 每段从原X的唯一对应n+1节点读全224字，两个新mean坐标按原约定起零；原完整engine返回所有方向，式(529.4)逐行沿实际port转换，不引用其他call或旧T。第3节的整个文件身份和真实cell来源将每个数组与同一call绑定。引理529.1逐字给出升精度结论。证毕。

本命题没有结论说Xhat满足原求解器容差、T_n等于128阶段导数、所有stage必然在原时间内完成，或不同矩阵带来相同接受序列。遇到原域/finite/resource停止，必须保正在处理的stage、原rawCell/rawSegment、返回范围及全部未访后缀；失败段不能当完整零矩阵。

## 5. 完整boundary传播可以使用什么矩阵

原[geometry_20261115_native_boundary128.cpp](../computations/geometry_20261115_native_boundary128.cpp)，12493 B / c218f12850e513cc58151e679c26de038f37b105dd187696e6f785ec4667fe96，执行完整far frame、逐段thin QR、cut square QR和向外系数回代；没有SVD截秩或normal equations。数值主体消费的是每段after-port全224×224矩阵及两mean行。对任意这类完整有限输入，代数问题都可明确写成

$$
z_n=A_n z_{n+1},\quad n=d-1,\ldots,0,
\qquad
z_d\in\operatorname{graph}(G_{\mathrm{far}}),
\qquad
Q_0=F_H.
\tag{529.5}
$$

F_H必须沿原physical packet声明的实际height局部延伸形成，不从舍入过的旧H/r^4重新猜；原远端全112模式也保留。原程序依次将far frame薄QR正交化，对每个A_n乘当前完整frame再薄QR，最终从cut Q块解全112列。返回的Pi/Q图G、全577×224×112 node响应、全129248×112原cut/stage/far残差读回及所有两mean响应，均是**这个新系数模型**的对象。

**命题529.3（模型级完整传播）。** 令各A_n、C_n是命题529.2形成后准确升精度的完整矩阵。若原QR算法在所需全部列上实际有限返回，且所有实际零pivot等原错误均未发生，则可沿原全部数值运算和原完整读回，形成该当前模型的完整boundary响应；不需把A_n证明为原128非线性阶段程序的导数才能定义这项线性计算。

**证明。** 原数值body只使用原far coefficients、实际cut forcing和每段完整A_n，按既定线性代数算式传播全112列。其每个stage residual是A_n z_{n+1}−z_n，far/cut residual也用本次实际参数重新形成。两mean的C_n同时乘相应全部node响应并按原段序累加。所有输入已是准确嵌入的有限128字，故这些算式是明确的有限算法；原shape、finite、零pivot和resource检查仍真实执行。完成时对该算法输入的责任完整，缺段则仍缺段。证毕。

这不是对式(529.5)准确实数可逆性或误差界的证明。原程序自己的numeric_readback_not_verified_error_bound、cut_chart_nonsingularity_proved_over_reals=false等范围仍成立；原readback不是新增验收门。也不能从这些完整QR结果推导新J优于旧J。

**现有消费者并未自动允许新来源。** c218头注释与原launcher明示禁止fixed64/R273替代原stage source，summary还有R273_or_fixed64_used=false；原R501 assembly也硬核当前128 stage的source、schema、全primal和full-column flags。本文只证明数值主体可用于新系数模型，绝不许可把这些来源检查短接或把上述false继续写在新结果里。

真正实施时需要独立明确的新boundary/assembly方法声明，保留原完整数学和所有原阈值，标明“当前owner投影点上重新计算的64阶段系数、准确升为128后完整传播”。旧R273固定矩阵和本次全新A_n是不同对象，不能靠一个含混的fixed64布尔混为一谈。原完整129248行、112列、两mean、全部factor/readback和原资源上限不减少；仅来源、精度与模型性质按真实事实更新。

## 6. 128端点值与新G的独立依赖

原[geometry_20261115_native_physical_final128.cpp](../computations/geometry_20261115_native_physical_final128.cpp)，18055 B / a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415，endpoint先读取完整128 final state，再取cut节点，同时读取完整G。随后：

- base=cut_readout(p,physical,node,policy,...)只消费原packet、physical packet、实际128 cut node和原policy；
- base.rows、原C-based Ldot和13个物理scalar均从这个base及同一geometry形成；
- 每个symmetric perturbation的Pi方向和finite-trace slope方向才依赖G；
- independent audit另从每个实际X[n+1]重起，读取全部原query/advance表，不读取G或新A_n。

现有endpoint入口在base之前就要求读取G文件，因此它**尚不是**一个可单独调用的noJ/base-only入口。以下命题讲函数的数据依赖；不把独立性误写成现有控制流已拆开。

**命题529.4（固定同次输入后的基值分责）。** 固定相同的实际X、packet、physical packet、原算术环境与policy；比较两个不同完整G。如果对应128 base和independent audit均沿原完整程序返回，那么base的338字、原13物理scalar及audit各原数值运算的输入不因G而改变。新G改变的是端点线性模型，不能代替这些128基值或审计。

**证明。** endpoint的base调用实参不含G；base.rows及13scalar的形成只使用该返回与固定geometry。audit初始化每段y的前224项来自X[n+1]，末两项为零；随后原capture_field、physical_jets、physical_metric及各advance仅依赖该段当前y、原packet/profile/query/policy。源码中这些路径无G或A_n的输入边。故在相同输入与执行环境下，模型系数没有影响这些数值对象的数据路径。证毕。

这是已完成路径的依赖命题，不是资源前沿等价：新的模型会改变前置walltime和剩余预算，线程调度也可能改变哪个audit段在截止前完成。partial audit的极值仍可含正在进行query的中间结果，不能把它们改称只在已完成query集合上取值。旧R486中stage/audit的partial范围不能因为本文未来可能省时而倒填complete。

原mixed端点算法完整保留。对每列c，使用**实际physical packet**中的difference_step和relative_step_floor，以及当前128 cut node计算原h_c：

$$
h_c=\mathrm{difference\_step}\,
\max\!\left(|Q_c|,\,
 \mathrm{relative\_step\_floor}\,
 \max(\mathrm{scale\_floor},\max_j|Q_j|)
\right).
\tag{529.6}
$$

这不是本文另造的二次幂步长。原symmetric部分在Q的第c列作±h_c、Pi作±h_c G_{:c}，调用原全部338物理读出，再除原2h_c r^4。随后原finite-trace RHS variation覆盖112个first-slope行和meanSlopeCorrection那一行；second、meanSecond及height行仍沿原symmetric方法。完整J仍338×112，没有缩到只给inner需要的112×112。

实际338行顺序是

$$
(\mathrm{slope}[112],\,\mathrm{second}[112],\,
\mathrm{meanSlopeCorrection},\,\mathrm{meanSecondCorrection},\,
\mathrm{height}[112]).
\tag{529.7}
$$

[R493组装源](../computations/geometry_20261116_live128_response_assembly.py)按此顺序解析，AffineTail取首112行。R527初稿和继承221的一个说明metadata曾误列另一顺序，已在R513发表时透明勘误；真实源从未使用该说明字段来索引。本条不改变冻结225的执行源。

由命题529.4可保持128基值的来源责任，但不能说替换G后J逐字不变，也不能把完整symmetric加finite-trace的mixed矩阵升级为全338解析导数。所有原finite/domain/原mixed方法限制继续有效。

## 7. 重新锚定的affine内层为何不把模型误差当末端值

令D(H)是该次真实非线性tail求解返回的112个slope值；此符号仅代表原完整有限求解程序的值，暂不指已证明的连续DN算子。令B为任何完整有限112×112矩阵。定义当前affine模型

$$
L_{H,B}(K)=D(H)+B(K-H).
\tag{529.8}
$$

**引理529.5（当前锚点值恒等）。** 对每个这种B，

$$
L_{H,B}(H)=D(H).
\tag{529.9}
$$

若另求得H'的真实值并重新设置

$$
L_{H',B'}(K)=D(H')+B'(K-H'),
\tag{529.10}
$$

则在H'求值同样返回D(H')，不含旧H或旧B的值误差项。

**证明。** 两式中的差向量在各自当前锚点为零，矩阵乘零向量为零。第二次设置直接替换原anchor、slope和矩阵，不沿旧线性外推继承D(H')。证毕。

原AffineTail.set复制当前H、response.jets.slope和完整heightJetJacobian首112行；__call__恰实施式(529.8)。真实height与右端boundary的H提取路径也已核对：[full_dn_solve](../computations/geometry_20261114_full_dn_solve.py)的true_height，以augmented endpoint中的core、物理state、控制参数，调用boundary.rhs与boundary.trace，再乘同一height_sign；[SeparatedBoundary](../computations/geometry_20261114_full_dn_augmented.py)以endpoint core建立proxy后交[FullDNBoundary](../computations/geometry_20261114_full_dn_boundary.py)，后者以相同core、物理height、该RHS和同一trace形成native_height。没有在末检查时切换为另一个材料角、core或物理height定义。

在有限字运算中，相同有限H字相减数值上为零，有限B乘零仍为数值零；signed zero的位型不作为整个BC逐字相等的结论。原BC还实际重算材料角、RHS和其他行，本文没有提供所有平台/舍入路径的严格实数误差包围。由源路径相同得到的“当前H”条件应继续真实绑定，不能用近似相同的height替代；任何实际域/finite错误仍由原代码处理。最终接受是原实际有限BC检查，未升级成连续边界的严格零。

**命题529.6（完整原末门的条件保持）。** 对一个采用本文新模型的实际调用链，假设完整原response由同一当前H的128 owner/replay、完整新J及所需物理audit真实形成，所有原来源/shape/finite检查均保留。若外层仍逐项执行下列原步骤，则其最终值验收不由旧anchor的affine预测替代：

1. 在当前H求真实response，设原affine内层；
2. 原solve_bvp真实执行全物理/常数core/控制行，原collocation RMS、inner BC、domain和原Newton门；
3. 从候选最终state提取H'，对H'重新求真实完整response并重设anchor；
4. 在同一候选state上重新实际计算原boundary，要求原1e−11阈值；
5. 再按候选endpoint的固定参数真实计算原frozen physical RMS，要求原1e−6阈值；
6. 在候选最终H'作原jacobian=True、audit=True的最终调用，再重设anchor并重算audited BC，仍要求原1e−11；
7. 继续原seam、物理输出与全部原消费者的责任。

**证明。** 步骤3与6分别用真实当前H'替换模型基值；在其当前锚点，式(529.9)–(529.10)说明B不产生旧H到H'的外推残差。其余BC行、domain、collocation和物理RMS都由原程序真实计算，不从矩阵或其shape推断。步骤6要求原最终audit和完整J真实返回，不因内部仅用slope行就省掉其余226行。故只有原实际计算与原门已经返回通过时才会走向原有限fullDN成功分支。证毕。

该命题不是“任何B都能收敛”，也不是放弃J完整性或任意伪造矩阵的许可。本方案的B必须来自第2–6节明示的完整当前模型，保持来源与实际输出；引理中对任意有限B的代数恒等只用于分清末端值验收的逻辑。

**原FD的适用范围。** 对固定H和B，式(529.8)的数学导数正是B。FullDNBoundary的解析Jacobian把同一个B与材料角/物理链式导数组合，原directional_check又在这个同一affine边界上作差分。因此测试可以发现实现/链式组合错误，但不能独立证明B=D'(H)。例如纸上取D(s)=s^2，H=a，任取b≠2a；L(s)=a^2+b(s−a)在其自身上差分与导数b一致，而b仍不等于真实D'(a)。这不是新增数值fixture或已执行例子。

原FD的两组完整方向、原三step/两Richardson、5e−5及全部适用contraction仍须实际完成。不能因其不能证明整个DN导数而删掉该已有门；也不能反向把全DN导数严格证明增设为本课题额外前门。

## 8. 尚无误差与收敛速度结论

一次准确RN64只解决“给哪个64字”的问题，不能单独控制新矩阵偏离原128矩阵的大小。即使Xhat−X很小，原有限根分支、局部scale、cut图条件数或矩阵连乘也可能放大差别。完整mean和port行必须保留，恰因这些耦合不能由状态投影误差代替。

如果另有一个明确光滑分支，在同一邻域定义了128模型T(X)，且其Lipschitz常数L已知，同时已知同点64模型与128模型的差不超过epsilon，则纯三角不等式给出

$$
\|T^{64}(\widehat X)-T^{128}(X)\|
\le \epsilon+L\|\widehat X-X\|.
\tag{529.11}
$$

这里第一项必须包括真实有限算术/模型差，不能直接赋成机器epsilon。G的进一步误差还涉及全部boundary传播与cut图的条件数。当前未付这些常数、邻域、分支稳定或同点误差，式(529.11)只说明所缺的具体数学对象，不声称已有误差证书，也不把它增加为新科学运行前门。

近似Newton的方向可能更好也可能更差；原line search、domain、每模型fresh W/J、merit及实际非线性末门照常决定。这一新模型不从R486一次owner收敛外推未来H，不继承原215或204的component完成标志。原原始trace derivative和mixed物理J的已声明局部限制仍然存在。

## 9. 真实接线仍需完成的工作

本文不是完整新request。当前R501/221与R527/225都保原全128 stage来源，不因本条发表而改变。新入口应显式接以下数据流，来源/所有权条件属于已有同次责任；不是增加独立审查、fixture或benchmark门。

**先完成原owner与fresh replay。** 原same-call owner的实际execute目前同步包含post-owner components，不是得到末state就已经返回给外层。若只在其整个返回后追加新64模型，仍会先耗原128 stage预算，且可能已经进入失败范围。因此需要以完整来源计划把原owner/replay及其precleanup handoff真实分成可消费的阶段；原final state、residual、fresh replay不改来源、不提前删。不能把现有wrapper误称已经支持该拆分。

**在实际持有DN的调用者中形成完整模型。** 第4节要求真实已加载DN的cell.engine/profiles。它不是仅把source basename写进receipt就成立；当前Node/Python的同步调用边必须显式调整，使那个真实DN对象在owner最终状态投影返回后实际执行全576段。另起一个进程重新加载另一套对象时，需要给出真实构造来源/参数与完整对象对应，不能假称跨进程仍是同一个内存对象。

**分清四类数组。** 原128 final state、full residual和fresh replay继续是原非线性事实；新64 state/primal只作模型点/诊断；全64 tangent/port/mean是新的完整模型；准确lift后的128 arrays只记录前一类64字的嵌入。新schema要保这四类来源，不沿旧stage.complete_576_stage_primal假报128阶段重新完成，也不把新64 diagnostic写回原norm。

**真实完成原全boundary、endpoint与audit。** 完整A_n/C_n作为新来源喂原全部QR；原physical cut forcing/远端不换；endpoint在X本身作原全338×112 mixed读出；audit从X原128节点作完整独立原schedule。原assembly需要接新来源tuple和正确声明，保原全部response字段、两mean、hex scalar/数组的正常一次RN64、原finite/shape/residual门。原c218禁止fixed64的注释/flag和原128 component schema必须诚实更新为新方法，不能旁路检查。

**共享原实际时钟。** 输入恢复后的原19200秒、最末120秒保留、原owner6000/replay1200/stage8000/boundary600/endpoint600/audit1800及其总剩余裁剪仍保。投影、新stage及所有真实启动、等待、读写、编译成本都计在同一实际deadline中；component最多只用自身原cap与当前总剩余的最小值。不能把每一个phase或子进程重新设成完整19200，也不能因旧215还有总余量就偷偷抬stage/audit cap。

**读回与清理。** 对新增source、projection、stage、lift及完整模型consumer保实际输入bytes/SHA、真实执行/返回、原错误、已完成和全部未访范围；source prepared不冒compiled，compiled不冒component complete。必要scope仍原单90000 B、超限70，无分包、科学树编码或raw上传；主科学scope不因新增来源而被拆成多份。真实owner pid/startticks/group/session及所有新增子进程必须按原合同登记/静止；未完整读回或quiet未知时不清理。大state/J/原账只在同一Actions临时空间，Git只存源、配方、run/source身份和紧凑结论。

以上是新方法能进入原消费者的真实实现义务。它不要求先对整个新方案作独立数值对拍，也不许可依赖未完成的步骤来报告原末门成功。

## 10. 核对过的主要原源

以下是本文直接读取并按完整文本核对的数据依赖。源码和相应既有正文是证据；本文未在本地导入、AST、编译或运行任何科学代码。

| 来源 | B | SHA256 |
|---|---:|---|
| computations/geometry_20261114_full_dn_solve.py | 30017 | c6a1f4d8025508ee49fe9324b3401440a2de88329d0b78ef0d0814860c2d3162 |
| computations/geometry_20261114_full_dn_boundary.py | 10619 | 4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2 |
| computations/geometry_20261114_full_dn_augmented.py | 11311 | f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e |
| computations/geometry_20261115_native_boundary128.cpp | 12493 | c218f12850e513cc58151e679c26de038f37b105dd187696e6f785ec4667fe96 |
| computations/geometry_20261115_native_physical_final128.cpp | 18055 | a0904ea0ea632da9e9c58f7b75b5ce2440a89e7b54916f44bfc84a27905b8415 |
| computations/geometry_20261116_live128_response_assembly.py | 28584 | 08d48b55934e5306258d70a26aa8f8f57c89f71b45f6175b777ab46405cd43eb |
| computations/geometry_20261116_live128_call_pipeline.py | 19240 | 137cc95996dca1d876640fb81e4fd3290d41e32e9b23027cb29d103b5cb0eda8 |
| computations/exact_20261116_binary128_live_response_projection.py | 19902 | b2336bcf56ba294efd1ba19e02b5d9acaedebb6eb669489fa1d869be7259626e |
| 原恢复源78718-tail-tangent-core.mjs | 17250 | ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3 |
| 原恢复源78718-tail-fourier-product-flow.mjs | 2400 | 717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f |
| computations/tail_resumable_engine.mjs | 4193 | 1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8 |
| computations/numerical-tail-slope-jacobian.mjs | 8131 | 206d82d3b41e6b9ce24b26447a2026c19c1c7126765107c23d58e55da25639e2 |

原恢复source的实际路径来自已绑定的公开repro树；新运行必须继续绑定真实restore root，不按表中basename从任意磁盘目录寻找另一文件。R523等具体完整engine若用于新入口，应另列其真实已发表tuple，不能只引用上表祖先就声称实际新engine已付。

## 11. 本结论的已付与未付

已付的是：完整当前X→一次RN64→全部226×224 stage/两mean→准确升精度后的新系数模型的明确构造；全boundary数值算法消费这种模型的条件范围；原128 endpoint基值与audit对G的数据独立性；重新锚定的affine内层不以旧模型外推代替当前非线性值检查；原FD只在自身模型上的解释。

未付的是：新实际caller阶段拆分、完整来源注册、真实模型/128升精度/全部consumer执行、实际native/FD/fullDN通过、资源改善、J误差或收敛速度，以及README的连通闭同g、全t几何比例和固定参数精化。只有原完整事实返回后才能给各项实际结论；本条完成即发表，随后继续真实接线，不等待独审或额外机械门。
