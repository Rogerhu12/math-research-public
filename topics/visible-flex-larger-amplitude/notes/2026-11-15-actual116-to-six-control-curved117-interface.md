# Actual116 → 六控制完整三共振实验117

分类：算法、源码及执行接口；尚无117数值结果。  
作者：exact_refinement；日期：2026-11-15。  
本文件交付独立源码、真实短参数recipe与工作流。全部新科学运算仅在公开Actions；本地仅读取原116字面结果、源码/JSON/SHA和静态语法。旧115/116两个数学源保持原字节。

## 1. 实际依据与本次选择

原116为run `43690052251`，source `4f4dbf700ee0732f6e7bd245f35808592ac82607`。其短报告77,038B，SHA256 `d24aa292cc9729fdb03bd7b692d87e29d1a4862575dcc1510abc7baa2dbf7b19`；原临时status 1,603,983B，SHA256 `5e5b634c42c5faba1ea70e35aa232d43d49cbb5c155ea55d97a674ea9d3f5a95`。短报告来自[实际116](https://github.com/Rogerhu12/math-research-public/actions/runs/43690052251)，不把已删除raw重构为一个伪parent status。

全部8个方向均有真实接受，27个外试探无评价异常；接受alpha依次为`[1/16,1/8,1/8,1/4,1/4,1/4,1/4,1/2]`。原未加权目标从`1236.0078724708571`降至`1234.283357373182`。每次接受均触发原半径减半规则，初末半径为`.1`与`.000390625`；首末保存方向斜率分别为`−31.830303481764954`与`−.00817762310168303`，最后实际接受下降仍为`.002040385409600276`。

初末完整3×4数值最小奇异值为`6.4079507884103455`与`.19378008756935441`；前三列相应为`5.331001438692232`与`.16017404141989777`。末原unit三式仍为`[-49.684657180215,-.03944148553951741,-9.621600240219177e-6]`；unit停止标志、full112候选标志及非零场/native责任均未通过。这些是原浮点报告，不是导数误差界、严格奇异值界、局部极小、无根或浮点极限证明。

本次据此增加另外两段独立odd形状，作一次有界六控制实验。没有把四控制预算悄改为64，也没有实现四控制八批编排。116仍有实际下降；本次选择不声称原四维族已无有效路径。

## 2. 精确参数顺序、来源和新族

六控制顺序固定为

$$
z=(p_1,p_2,p_3,\theta_1,\theta_2,\theta_3).
$$

116旧四控制是$(p_1,p_2,p_3,\theta_2)$，对应新列 **`[0,1,2,4]`**，绝不是新矩阵的前四列。新列为`[3,5]`。初值逐字取原116的四个binary64参数，在这两个新坐标明确补零：

```json
[0.43234616540612814,0.1783653778144092,0.5751222087274236,0.0,0.016140885548593657,0.0]
```

这里两个零是本实验的初始化选择，不是116曾输出的参数。短recipe同时保存真实run/source/status SHA/短报告SHA与原四数学输入SHA；只复用参数值，不复用父W/J/传播数组、区间证书或接受场身份。新入口也明确支持将来自己的六参数短recipe，但未实现或派发任何后续循环。

保留原三段prefix支撑、原stored left/right/width及原偶形

$$
b_i(s)=w_i^2P(x_i),\quad P(x)=64x^3(1-x)^3,\quad x_i=(s-\ell_i)/w_i.
$$

现在每段均有奇形$o_i=b_i(2x_i-1)$。原115/116已有第二段$o_2$；117只新增$o_1,o_3$。在每个原支撑内

$$
\begin{aligned}
o_i&=w_i^2P(x_i)(2x_i-1),\\
o_i'&=w_i\{P'(x_i)(2x_i-1)+2P(x_i)\},\\
o_i''&=P''(x_i)(2x_i-1)+4P'(x_i).
\end{aligned}
$$

支撑外与端点取零；因$P$含端点三重因子，新增控制具有零0/1/2阶jet。`OddBump`原构造与jet源码AST不变，只实例化三段。精确声明的支撑使用$\ell_i+w_i$，原binary64 right另存，不能无声认定两者相等；也不假定三个stored width逐位相同。

在原分离支撑上，若六形状线性组合为零，逐段除以内部正的$b_i$得$a_i+c_i(2x_i-1)=0$，故各$a_i,c_i$均零。这证明标量函数独立，**不能证明三条响应对六列满行秩**；六个响应向量位于三维空间，更不可能宣称六列线性独立。

新完整标量为$a_0+\sum p_i b_i+\sum\theta_i o_i$。它是一族新$g$。固定最终全部六系数才得到一个确定标量身份，搜索中的不同点不冒同一个fixed $g$。

## 3. 退化读回与完整响应

新family保存相同的原三偶控制组装，再按`theta2,theta1,theta3`顺序添加非零odd项。此顺序保留旧theta2路径；但实际有限数组是否逐位相同仍由读回报告，不作为源级假定或运行门。

`zero_added_odd_reduction_readback`在`theta1=theta3=0`处，调用真正冻结的旧FourControlProfile/CircleReference，并用旧参数`p[[0,1,2,4]]`比较全部25个原状态/传播数组。输出`zero_added_odd_reduction`、各数组bytes/SHA/byte-identical与完整scope。它不取父status，也不把theta2置零。数值相等或不相等都不改变原候选接受条件。

完整CircleReference仍使用原mesh、原circle半径递推、全部低三L/R块、全部原112×112真实零高尾J及完整112右行。新节点/中点标量组装之后，旧circle/传播/右行实现逐字相同。没有用旧profile斜率替代原native J，没有将高109残差为零当成高块可逆证明。

参数Jacobian用原`1e-25` complex-step完成全部六列，包含circle半径和全链传播响应，输出`three_by_six_parameter_jacobian`。初末都以原三个实差分尺度`2e-5,1e-5,5e-6`尝试六列；某列发生原域/线性求解异常时，该列记录失败且仍尝试余列，不能默默跳过。实FD公式、每列误差定义不变，FD/SVD不形成新门。

初末报告保完整3×6 SVD、前三列SVD、明确`old_four_column_indices=[0,1,2,4]`的子矩阵SVD、三odd响应及新增列`[3,5]`。这些都只是当次浮点诊断。

在精确同一光滑模型、同一嵌入点与同一坐标单位下，旧四列确实嵌入新J，因而

$$
J_6J_6^T=J_4J_4^T+b_1b_1^T+b_3b_3^T.
$$

所以同点精确最小行奇异值不会因仅增列而下降；不保证严格增加、条件数改善或非线性进展。本次实际浮点J、所选正阻尼、域、曲率和回溯不由该恒等式保证，更不把尚未形成的新J称为已改善。

## 4. 完整9×6方向、两normal及四tangent

方向仍解原形式

$$
\min_\zeta\ \|JS\zeta+r\|_2^2+\mu^2\|\zeta\|_2^2,
\qquad v=S\zeta,\quad S_j=\max(1,|z_j|),\quad\|\zeta\|_2\le\Delta.
$$

这里$\mu>0$，增广矩阵是完整9×6，使用带列主元Householder QR和完整6×6三角解；不形成normal matrix，不用`lstsq/rcond`或截断弱奇异值。原正机器尺度下限、64次上界搜索、64次几何细化仅在同一线性模型中选阻尼，不额外试探非线性点。初半径明确为`.1`，不继承116的`.000390625`，也不把半径当物理参数。

取$c=(r_2,r_3)$，$C=J[1:,:]$。对行平衡后的$(CS)^T$完整QR得到$Q\in\mathbb R^{6\times6}$；前两列为$N\in\mathbb R^{6\times2}$，后四列为$T\in\mathbb R^{6\times4}$。没有删除任何参数列。每个外试探仍为

$$
q(\alpha,w)=z+\alpha v+SNw,\qquad
c(q)=c(z)+\alpha(Cv),\qquad w\text{初值}=0.
$$

在光滑模型且$CSN$可逆时，$\alpha=0,w=0$是原点；对上式微分得$CSNw'(0)=0$，故$q'(0)=v$。原full3目标的起点斜率保持$r^TJv$。这只是局部光滑模型关系；程序另外保留有限形成的起点导数、原J作用、normal残差与实际参数位移。

`full_column_qr_solve`仍是完整原2×2 QR；`curved_candidate`整个函数只将保存当前J字段名从`fresh_current_full_three_by_four_J`改为`fresh_current_full_three_by_six_J`。校正仍最多12次，每次最多20档。`1e-8`仅为内层target计算停止阈值；未达该阈值的最后实际有限点仍进入原full3外门。原直接seed先失域就结束该alpha，本次没有实现沿曲线分段绕过非法seed。

## 5. 原接受规则、预算与停止含义

原外门完整保留：实际有限域、$r^TJv<0$，对实际返回点计算原未加权$W=\frac12\|r\|_2^2$，并要求

$$
W(q)\le W(z)+0.2\alpha r^TJv.
$$

保留全部三条实际残差，不把target误差或重置后的$d_2,d_3$当原残差。alpha仍`2^-j,j=0..19`。每次接受后的原半径更新函数AST完全一致；20档全拒才缩半径为四分之一，点/state/J不变，下一方向重新求完整阻尼方向。拒绝方向也计入8个方向总预算。

仍最多160个外试探，38,560次seed/normal-backtrack实评价、1,920次normal fresh-J调用；这些原源码预算上界不含复步和初末检查，每个新完整J现在有六列。科学步骤75分钟、compute job90分钟、report job10分钟保持。资源超时/异常诚实保部分状态并输出已有信息，不冒原数学无根、全拒或接受。

原unit停止阈值`max|equation|<=1e-8`与最终完整112行候选标志`max|full_right|<=1e-8`分别保留，不能互换。原scalar域、circle物理域和full FFT检查仍执行。任何这些候选读数都不是非零场、原native/fullDN或最终几何完成。

## 6. 全三odd冻结的平方物理视图

`OddCoefficientsFrozenProfile`固定实际$(\theta_1,\theta_2,\theta_3)$，但其base_jet、完整标量profile及新声明式包含三项；只保原$p_1,p_2,p_3$为active。新AugmentedFlow和原PhysicalTestBoundary仍为338物理分量+112core+3参数，即453维；$K=3,T=M=112$，原全部物理行和边界行保留，不向旧平方BVP塞六个active参数。

`complete_reference_check`重新生成同一当前数学标量下的circle状态、原FFT/node/mid/RMS/BC读回和原九个低模切向检查。`frozen_three_odd_square_check`记录完整六参数、实际固定odd向量、scalar路径读回与同一数学函数声明。它不宣称不同浮点求和路径逐位相同。

新`scalar_spec`、descriptor和`ScalarExpression`都包含三odd的完整left/right/stored width、全部六系数和对应来源。Arb仍160位、最大深度14，重新对全部声明实表达式$a>0,|a'|<1$付域检查，不沿用115/116旧证书。保持原范围限制：这里并未给binary64求值舍入包络、原有限Gauss的$a$与独立返回$a'$兼容证明、原全局C²接口证书，或circle/fullFrenet连续域证明。

全3×6若数值满行秩，也不等于冻结odd后的前三列足以作非零分支坐标。未来可基于真实非零3×3 minor另选三个active并冻结其余三个，但必须另立准确parameter/profile/order/scalar身份，不能悄改本次冻结视图。当前高109非共振、完整非零lambda BVP、真实非零H原native/finalJ/audit和全闭场责任仍未付。

## 7. 输入、来源闭包和复算CLI

四个原数学输入与116相同，均逐完整bytes/SHA核对；若main已清理原数据，仅从真实历史commit `8bd267107cc8710d371f3b62c02986655ac965b0`恢复。原78个公开数值文件仍经原prepare_public_source恢复一次，并设置`VISIBLE_SOURCE_TOPIC`。输入路径、bytes、完整SHA均在request中，不靠本文缩写重建。

原116 producer闭包为22项；当前新producer为这22项加新family/search，共24项。原family922239与search3ca1保留；旧search只作来源，旧family仅供明确的退化比较。其余旧solver main不执行。request完整81项primary pins保留旧79全部再加新两源；workflow支持为原rules runner及新reader两项。未把22项父闭包冒当前24项，也未声称本地重新取读全部81旧payload；Actions起步逐件验证。

科学入口：

```text
geometry_20261115_small_core_six_control_curved_recipe.py
  --accepted <原M96 actual.json.gz>
  --prepared <原prepared.json.gz>
  --tail-anchor <真实zero T112 anchor>
  --tail-config <原T112-config.json>
  --parameter-recipe actual116-explicit-six-control-parameter-recipe.json
  --parameter-recipe-sha256 4f40206d6b08ff6e232c7239677e90730496ffbc230e19d671e145c50b497e67
  --initial-relative-radius 0.1 --candidate-steps 8 --backtracks 20
  --normal-iterations 12 --normal-backtracks 20 --normal-target-tolerance 1e-8
  --candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14
  --out <fresh>/small-core-six-control-curved
```

runtime仍Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0、全部BLAS线程1。真实Actions触发后才有117run/source/status/结果SHA；本交付不预造。

## 8. 输出合同、保全与发布

|对象|实际schema/字段|
|---|---|
|recipe|`R259-explicit-six-control-odd-shape-recipe-v1`|
|完整临时status|`six-control-curved-status.json`；`R259-six-control-full-three-two-normal-curved-trust-recipe-v1`|
|新scalar|`complete-prefix-three-even-plus-three-odd-controls-v1`|
|声明式|`complete-six-control-scalar-real-expression-v1`|
|circle|`R259-six-control-circle-full-three-resonance-family-v1`|
|域报告|`R259-six-control-complete-declared-scalar-domain-enclosure-v1`|
|短reader|`request117-original-six-control-full3-curved-trust-scalar-readback-no-raw-retention-v1`|

完整status保每个实际方向、完整9×6QR、列主元/尺度/阻尼搜索、6×2和6×4基、真实normal每次试探、full3原门及完整原112残差。各外trial另逐行stdout输出实际参数/三残差、target/error/内层tol状态、原W/Armijo界、异常和来源，不因短报告超限改变科学。

新reader只拷贝已有原值和hash，不做科学算术。它保初末3×6/旧四子矩阵/前三列SVD、完整六列FD、全三odd冻结报告、退化读回、原17列外trial表及所有原布尔scope。90,000B上限和诚实fallback沿旧协议：如需省略可重算辅助字段，保原bytes/SHA和明确省略标志；更大时明确报告超限，不伪造完整读数。

独立report job经`GITHUB_OUTPUT`接短JSON，以`BEGIN_VISIBLE117_SCALAR_SUMMARY`和`END_VISIBLE117_SCALAR_SUMMARY`打印，并记录排除日志分隔LF的bytes/SHA。reader中的`new_scientific_computation=false`仅指这个纯读出阶段；compute执行的是本文件明确的新六控制科学计算。

遵当前规则15，不上传artifact/Release，不向Git保存可重算raw/status/大审计。短读出之后删除本次临时科学输出；原脚本、完整参数recipe、run/source/输出SHA与紧凑结论足以说明和复算。原rules runner `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde`保启动及2700秒真实pull/rebase/规则变动停止；双README为当前已读`74c08a36...`/`bff8aea2...`，H唯一规则行、≤10000B、`merge.stat false`、固定science checkout均沿原接线。

## 9. 冻结交付

所有文件当前位于`/tmp/visible-small-core-six117/`。除workflow放`.github/workflows/`外，前五件放课题`computations/`；本接口放`notes/`。不得修改旧115/116文件。

|文件|bytes|SHA256|
|---|---:|---|
|`geometry_20261115_small_core_six_control_family.py`|39524|`79464f9c6af8863d3c65254701a858f067881b22ca80dba24bacf2bfea484acf`|
|`geometry_20261115_small_core_six_control_curved_recipe.py`|53497|`e154afe28c588ce0c2ae936d4304b67ec84e2b46c96b03e48ce4113e2401a761`|
|`root_20261115_small_core_six_control_curved_scalar_readout.py`|19347|`3e2c0515ee9759162e3736915674c86ca9a56441f2a7561df9dc09d37fea4d45`|
|`actual116-explicit-six-control-parameter-recipe.json`|1869|`4f40206d6b08ff6e232c7239677e90730496ffbc230e19d671e145c50b497e67`|
|`public-small-core-six-control-request.json`|34000|`7147dbdaf544370ab37d458f81103342930679e0514936e8975f28218244eeb5`|
|`visible-larger-public-small-core-six-control.yml`|16905|`f3e7a17eb49854598f694ff5d4edf2487935a7caadb3897f670916d078da6297`|

数学源及request/workflow完整相对diff、reader相对115diff、8个bash步骤和5个inline Python的静态回执已实际形成。新三Python只作AST/compile；未导入科学模块或运行fixture，未本地算响应/范数/ODE，也未修改Git、dispatch或上传。diff和静态回执是临时可重算证据，不另设审核或科学门。
