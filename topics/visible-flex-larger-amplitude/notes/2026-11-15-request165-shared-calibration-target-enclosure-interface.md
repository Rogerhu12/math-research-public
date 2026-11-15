# Request165：R352 共享校准表达式与完整 Bernstein 公共坐标包围

日期：2026-11-15。状态：独立源码、参数、公开 Actions 工作流已冻结，尚无本请求实际数值。原151源码及其实际结果不修改；本请求以同一准确目标、同一字面数值参考和同一组九参数重建当前现场。

## 1. 要支付的具体责任

原151已经完整覆盖419个数值查找闭片，但在65535个节点后因两子事务剩余额度不足停止。R349的字节读回给出32977个当前cover叶、10468个未决叶、0个严格域反证以及global_delta_upper=null。该读回没有逐值提供未决叶的d0/d1/a/as，不能据计数确定唯一瓶颈。本请求不把这些原ledger的hash当可恢复数值，也不另取旧大日志重新计算。

[R352](../results/R352-shared-calibration-normal-forms-and-complete-Bernstein-target-enclosures.md)给出了可直接消去的准确共享量：L=S3+d、两端速度过渡的同一校准、以及每支撑三项控制的同一局部变量。新consumer使用这些恒等式和完整向外Bernstein包围；仍与[R330](../results/R330-centred-common-coordinate-difference-and-target-coefficient-bounds.md)的中心差和直接差求交。上游C的真实区间宽度并未凭恒等式消失，本请求不预许严格成功、显著速度提升或更小的全局δ。

数学对象仍为完整公共u∈[0,1]上的准确目标diag(L²,a(Lu)²)，与原实际numeric compilation的准确实字面word分片参考diag(ell²,N(u)²)比较。后者不是IEEE程序逐次舍入映射，也不把真实准确L换成ell。当前没有同一目标的非零场、当前C尾J、native/fullDN或几何完成证书。

## 2. 冻结文件、身份与直接基线

|目标文件|字节|SHA-256|
|---|---:|---|
|computations/root_20261115_continuous_nine_shared_target_enclosures.py|94125|61b98b3e853b31535ac31b66d4cf4513f1271d9852acfb09b948990a30acb205|
|computations/public-continuous-nine-shared-target-enclosures-request.json|16401|6beff06bb6ffdd9604b936016635b3cf47adbf45181b266f7b0a85743a60f7c3|
|.github/workflows/visible-larger-public-continuous-nine-shared-target-enclosures.yml|53762|10b6e44a44ba019a930acf6321f54dd17e3e2861727434cee9ea6dc36e4ac915|

computations与本note均在topics/visible-flex-larger-amplitude之下。每个新文本都小于100KB。

直接基线是commit618a9369d2bd45210767e294726cec10be1cd2df：

- 原consumer root_20261115_continuous_nine_target_enclosures.py：69431B / 6dfb79be9b77e85ffff496e4349b9c6b01c1ab74f28d0a64bf76d4dc8cadb768。
- 原request public-continuous-nine-target-enclosures-request.json：13405B / a4894d6bc0388121c07e6b4b47d019d1004a14f5a44878415ba9f1f7e9cfffe3。
- 原workflow visible-larger-public-continuous-nine-target-enclosures.yml：50748B / 3995b487f98f3c61cf28cc0418f666c9cb1ae6748156930718fb889f4ed5a9e9。

新source schema是request165-shared-calibration-complete-nine-target-enclosures-v1；新request schema是public-continuous-nine-shared-target-enclosures-request-v1。触发路径和concurrency group均独立，cancel-in-progress=false。旧151不被重标，也不执行为第二遍consumer。

完整21源闭包为原151的20项原SHA全部保留，再新增本consumer。原151源只承担来源身份；实际新consumer包含原绑定、区间操作、完整cover与读回正文，并新增R352表示层。原19个147科学源码未更改。request逐项列出完整21 pins；没有隐式未标注的模块替换。

R352的准确已发表身份为17736B / 58cdfeb61adb46378ca4f6c070b8b8e7d7c0ff3f9cf1b853e44a1c52316f5a85，commit34fd5a7f241406a2bb48a6d8ed6f6ec1a4e69188。原R326、R330仍各自逐字核对；R300/R323及原连续C证明仍沿原147闭包。

## 3. 同job完整重建，不能以旧输出SHA代输入

先执行冻结原147子程序请求public-continuous-nine-v3-construction-request.json，17398B / 4b6f78bb25e0d87354e2ad786637fc9e4db5c7c34774d3cad4716638552ba707。其request147/schema保持原文。新165明确沿151的实际C预算3600秒；原147记载的1800秒只作来源，不冒本次实际预算。f12f完整C公式/对象、原两域各300秒、cut完整两jet、R323选择、core/recipe/definition/numeric均重生于本次同job。

原factory：geometry_20261115_continuous_nine_scalar_factory_v3.py，0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e。原construction：geometry_20261115_continuous_nine_v3_actual_construction.py，738dd352cf62fbd47eb80e867ac441b7d0c179074cbee93fb8dd6528ba0d4cb0。原numeric：geometry_20261115_continuous_nine_scalar_numeric_v3.py，7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60。

新consumer仍用实际core、实际recipe、当前完整C/cut重新调用build_expression。全部definition字段逐canonical字节比较，并核原definition文件包括末LF。它不只相信producer自报的一个hash。全部DAG literal words、所有piece coefficient words、三支撑的left/stored width/rounded-right、完整查找partition、九个parameter words与真实length root都继续逐项绑定。rounded-right仅作原元数据保留，数学支撑右端一律准确left+stored width。

九参数保持原R320同一组实际末literal值，顺序[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]：

[0.3055213835477326, 0.21645013203050154, 0.34270051957744246, -0.06322334619266512, -0.01747451701873286, 0.9376115689625685, 1.0751306255033548, 0.6886900390922872, 0.9385431607625546]。

这些是原系数来源，不是新准确目标的预付域证书；不自动置零，不把旧目标搜索状态作为新场。原M96 accepted只提供原core几何，T112配置只提供完整原配置，不能据它们声称新目标场已存在。原历史输入恢复仍来自8bd267107cc8710d371f3b62c02986655ac965b0，真实当前输出均须有本次run/source。

## 4. 区间表示与共享L

所有原Tree.evaluate仍使用256bit平方根包围，逐节点准确Q区间先外包到320bit整数格。Interval的每次非准确加减乘除及有理转格都朝外取整；新多项式只在这一格上操作。没有先取原C、L或derived coefficients的中点。

令κ,d,d_A,d_B和原core端RA,VA,BA为准确常数，S1=core_end+d_A，IA=d_A(VA−κ)/2+d_A²BA/12。新consumer仅从原rational节点取这些常数，不能从一个语义cut叶假取常量。根据R352：

$$
L=C_0+C_vv+C_bb+C_qq,
$$

$$
C_0=S_1+\frac{d_B}{2}+d+\frac{R_A-R+I_A}{\kappa},\qquad
C_v=\frac{d+d_B/2}{\kappa},
$$

$$
C_b=-\frac{d^2/2+d_Bd/2+d_B^2/12}{\kappa},\qquad
C_q=\frac{d^3/6+d_Bd^2/4+d_B^2d/12}{\kappa}.
$$

新长度盒是此展开的向外结果与原DAG长度盒的交，不覆盖原输入。coast width再用原LC盒与L−S1−d_B−d求交；其正性沿原准确构造严格前提。若两个已宣称同对象包围出现空交，记录consumer/enclosure错误，不能称物理域反证。

result.shared_calibration_and_literal_defect_binding保留原L、展开L、相交L、准确常数系数、coast宽盒、完整三支撑九项合并系数和numeric collar缺陷。原v/b/q的上游依赖仍由原盒包围，本次不声称已消除所有E0/E1/E2相关性。

## 5. 四类准确piece与全部支撑

完整原core片及其实际local_interval不改。普通piece仍从原系数在共同u变量上形成a/as/ass多项式；三个特殊后段使用同一准确函数的代数形式。

collar使用z=L(u−1)：

$$
a=R+vz+\frac12bz^2+\frac16qz^3,\qquad
a_s=v+bz+\frac12qz^2,\qquad a_{ss}=b+qz.
$$

coast使用a=RA+IA−κ(Lu−S1)，a_s=−κ，a_ss=0，再完整加第三支撑的三项控制。不得因为基底线性而删除这三项。

last transition使用r=(-L(u−1)−d)/d_B。记

$$
H_2=-3(\kappa+V_B)+2d_BB_B,\qquad
H_3=2(\kappa+V_B)-d_BB_B.
$$

其三个物理jet按R352右锚形式分别构成四、三、二次多项式。原RB/VB/BB盒还与由同一R/v/b/q推得的盒求交。新u变量的转化没有把物理s导数误当u导数；最终u导数仍为L a_s和L² a_ss。

所有准确piece都先保原可行性条件T=((L U−A)/W)∩actual local_interval；还用包含全部可能物理位置的public-u外盒筛选。筛掉的只有由这些外包已能排除的piece，不选单一“最可能”片。每个保留branch继续覆盖其全部可能参数与u。

对第i个支撑，将原三项准确合并为：

$$
\Psi_i(x)=64x^3(1-x)^3\{p_i+p_{3+i}(2x-1)+p_{6+i}(2x-1)^2\},
\qquad i=0,1,2.
$$

完整次数不超过8。物理三jet分别为w_i²Ψ_i、w_iΨ_i′、Ψ_i″，原九参数无遗漏。

准确支撑的逻辑由已绑定factory定义支付：支撑0严格在core内部，支撑1恰为first transition，支撑2恰为coast；last transition和collar不含非零控制。core每片继续枚举支撑0之前、内部、之后的全部可能闭分支。first/coast完整加入相应三项；共享端点其他支撑的0/1/2 jet准确为零。因此不会把宽区间造成的“同点可能属于两片”误当可删掉某一侧，也不把区间重叠本身当真实支撑重叠或不重叠证明。

## 6. 字面numeric参考保持独立

numeric的所有anchor、stored width、系数均直接使用原编译word的准确dyadic值。原419个lookup闭片完整保留；local t不clip到[0,1]或准确piece的local_interval。

在每个当前u闭片内，再按三支撑的准确word边界left/ell及(left+stored width)/ell分闭段。某段内部真实存在的全部numeric支撑都累加，绝不假设数值支撑仍两两不交。两侧端点都保；在支撑切换端点，所有bump的0/1/2 jet准确为零。

准确L=S3+d不施加给numeric word。代码另外形成literal collar缺陷epsilon=ell−hatS3−hatd，保留：

$$
\widehat t=1+\frac{\ell(u-1)+\epsilon}{\widehat d}.
$$

实际numeric collar仍按其原存储系数和一般local坐标计算。它不会被R/v/b/q替换；numeric coast斜率也不会被强制写成−κ。新加法合并只改变准确实参考表达式的求值包围，明确不主张IEEE有限求值路径逐word相同。

## 7. 同一个u多项式相减，再作完整Bernstein包围

对每个query，统一X使u=u0+(u1−u0)X。accurate与numeric的所有可能branch都使用这一共同变量；只在二者闭分支window相交时组成候选pair。每个pair保accurate piece、控制支撑、literal支撑、完整u外窗、两个差多项式次数及包围。

每个多项式以向外区间系数完整形成。restrict到子窗后，对实际次数n计算全部n+1个Bernstein系数：

$$
b_j=\sum_{k=0}^{j}\frac{\binom jk}{\binom nk}c_k,\qquad 0\le j\le n.
$$

以所有下界最小值、所有上界最大值包围范围。没有只取端点、取部分系数或角点采样。点窗则为同一完整多项式的点区间包围。每组九项合并之前的所有准确参数已进入系数；省略的是准确为零的高次系数，不是科学列。

新的radius差是同一pair中的N(X)−A(X)系数先减，再取Bernstein范围。新的public-u导数差是ell N_s(X)−L A_s(X)系数先减。全部pair取hull，保不确定piece与支撑的完整并集。

原R330还在：d0=N(m)−A(m)照实际中点完整包围；d1为整个u盒的导数差。新导数差与原R330导数盒求交，再形成d0+(U−m)d1；新radius差与原直接差、原中心差以及收窄中心差求交。result同时保R330_before_shared_coefficient_difference、R330_before_shared_derivative_difference以及新的R352包围，不能仅把“变窄”写为无证结论。

准确域仍分别证明a_lower>0和−1<as_lower≤as_upper<1。只有整盒a_upper≤0，或整盒as_lower≥1/as_upper≤−1，才给严格域反证。其余过宽或暂不可分都保持unresolved。

在准确半径严格正时，以原形式rho=maxabs(D)/a_min、d_beta=2rho+rho²，与abs(ell²/L²−1)取共同上界。工作目标δ≤1/10000000仅决定当前cover细分是否满足目标，不改任何native、fullDN、物理场或最终几何接受阈值。

## 8. 原完整cover和失败保全

原先419片全部coarse、之后两子原子替换的代码保持，只将当前调用的区间表示换成上述新类。两子都完成才删父；中断时父仍在cover，已完成但未提交的子另记。每个可能未访问片、待细分节点、深度上限、错误或中断的闭u范围都完整保存。

每叶仍输出a/as/ass、u导数、准确与literal两目标系数、d0/d1、中心差/直接差/相交差、rho、两相对误差、共同δ、域与工作目标flags及reasons。新增全部可能branch-pair的piece/support/window、完整Bernstein差与导数差，并保原比较盒。完整当前cover、全部pending/frontier及所有事务记录在清理前逐字段输出；不是只保计数和hash。

原科学exit与传输结果分离：正常完整、严格域反证、资源未决、源/区间错误有原独立状态；summary超过90KB时保完整result分段输出并明确exit70/transport_complete=false，不能删字段后冒完整成功。各段12000字符，ASCII JSON无损；hash口径包括canonical末LF。

原readback-only仅重放已经记录的字面节点、区间端点和事务，不重新做新多项式或区间运算。尚无primary summary时，依真实临时日志恢复完整cover与未访问范围；缺原definition/plan则明确不补造。原粗cover若因实际预算未全部完成，也不声称全u完成。

## 9. 明确资源与运行顺序

本次未增加原151节点预算：C3600秒；原两域各300秒；新target900秒，最多65536 evaluated nodes、depth32、整数格320bit、原Tree sqrt256bit、419原lookup片。新target科学时钟包含绑定、DAG重建和新区间表示初始化；不能把这部分计时挪掉。

workflow job150分钟，C step75分钟，原construction20分钟，target20分钟，target只读步骤10分钟；后置完整元数据输出不当作继续细分的科学预算。新方法的单节点成本不同，尚无实际耗时或完成保证。尤其900秒可能先于节点预算停止，必须按真实partial读回。

全流程为：历史原输入与78源恢复→当前完整C→当前完整cut两jet→原147真实构造/R323/definition/numeric→独立165公共u包围→always原元数据读回→按实际读回状态决定是否清理新165命名空间。C/head/cut若未支付，后续不得用旧147/151hash冒其当前输入。

清理步骤虽为always，但只有cut_twojet、construction_readback、target_readback、scalar四个实际step outcome逐项均为success才调用rmtree。任一failure、cancelled、skipped或缺失状态都跳过删除，输出四项原outcome、原E/construction/target科学outcome及相应未读或尚未确认完整的范围，保留RUNNER_TEMP现场直至runner销毁。此保留不上传raw，不承诺job结束后还能恢复；runner销毁也不代表科学成功。这个条件只保护错误与未读记录，不改变原科学exit、域/误差工作目标或native门。若已确认读回后删除本身失败，仍独立输出cleanup_error和原outcomes。

原3b8规则runner分别外包实际C、construction与target；按真实已读21bd根README/bff课题README建立BASELINES，2700秒真实pull/rebase/差异停止保留。fixed科学checkout不改成规则镜像HEAD。Git merge.stat=false，凭据只在规则parent环境；科学child移除GH_TOKEN/GITHUB_TOKEN/MR_TOKEN。无force、无artifact、无Release、无raw入Git。

## 10. CLI、来源与验证范围

唯一新增科学入口接受与原151相同的显式路径参数：

~~~text
python -u root_20261115_continuous_nine_shared_target_enclosures.py
 --request <computations>/public-continuous-nine-shared-target-enclosures-request.json
 --original-request <computations>/public-continuous-nine-v3-construction-request.json
 --inputs-directory <same-job inputs>
 --tail-cover-directory <same-job actual C>
 --cut-twojet-readout <same-job actual complete cut JSON>
 --construction-directory <same-job actual147 atomic construction>
 --code-directory <pinned computations>
 --repository-directory <fixed scientific checkout>
 --out <fresh RUNNER_TEMP/visible-continuous-nine-165/target-enclosures>
~~~

同source的--readback-only --out用于原值重放。报告job使用BEGIN_REQUEST165_COMMON_U_TARGET_SUMMARY/END_REQUEST165_COMMON_U_TARGET_SUMMARY，SHA针对ASCII canonical bytes包括末LF；原147 C/cut/construction报告保原schema与marker，因为它们确实是原子子程序的实际输出。

已做完整源码字符串与SHA、基线差异、全部旧20 pins保留、三个新文件身份和数学责任逐段源级核对。终端不可用；没有本地Python导入、AST/CPP编译、数值fixture或科学计算。工作流的普通Actions语法解析先行，然后直接做已授权科学；没有新增待审批或成功前置门。

源码、参数与当前run/source身份、紧凑结论、完整scope与输出SHA是持久记录。全部可重算原输入副本、大节点/cover/frontier数据只在本job临时目录；四个实际读回步骤均成功后才清理，读回失败时明确保留未读范围而不声称完整log。完整差异可从上述151基线和本次新源码重得，不必另外入库可重算raw。

本请求能支付的是同一准确目标与其字面参考的严格有限区间责任。它既不把R352的表示恒等式当数值成功，也不把字面参考误差界当真实IEEE误差或已接受场的同metric证书。后续选择仍以实际165完整结果和真实未决范围为准。
