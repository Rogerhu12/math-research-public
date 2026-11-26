# 2026-11-26 当前完整 SO3 八列 PCG：五件完整接线与未运行候选

## 1. 本条的范围

本条发布完整的新 driver、launcher、cache、deriver、reader，把当前 SO3 完整 A/A* 的八列 SPD 预条件器接入 metric QP。全变量、原 residual、C/b、mu、母范数、完整 Phase I、后退锚全行 SOC、全部永久地点与真实非线性接受保持。它不是八维场 ansatz，不复用旧父 Gram，也不把均值行投掉。

实际 run04 的46/47、48/49在原892f下返回了有限真筛通过的 SOC 推进，64 advances仍是 iteration_limit。这支持检查全空间线性求解器，但没有给出本新入口的实际速度、驻点或精度结果。这里没有本地科学运算，没有新 fixture，**没有声明加速或研究完成**。

SPD 和活动面代数沿用 R681/R685；八列构造、原白化逆映射及完整 A/A* 费用见 [ac03完整组件](../scripts/resume_20261126/so3_current_eight_column_preconditioner.py)。本条付的是完整原科学入口的闭合接线、来源、缓存继承与纯归因，不重复给既有代数编号。

## 2. 完整新源身份

五件文件均在 scripts/resume_20261126；每件完整源小于100KB。

| 文件 | Bytes | SHA256 |
|---|---:|---|
| so3_frozen_parent_cache_for_current_pcg.py | 26825 | 78f7924f89ee874d14ea9dd9b78630910ed6c0b5e53c9ed4771d910015fcdfb7 |
| fullclosed_so3_cached_current_pcg_soc.py | 79214 | a0e27f36692d565d333b1ef5a207afa425ec0fc9a120164a0df3a3057f3dc743 |
| launch_so3_cached_current_pcg_soc.py | 11877 | 333ea5c5f9c06b434c4f16fcb8e93ec202d7f40decf819c152e26ddcef3257e2 |
| derive_so3_cached_current_pcg_soc.py | 21766 | 6420bb73edad599da723001fff95c4ab9c64ccecff6e2459cf1fc85a20209d3e |
| read_so3_cached_current_pcg_soc_report.py | 71779 | 0d659ab94bff7fe12337cc8f1eb18263ae1623f8fb8bcbb40108e7e03ad3856f |

新科学 schema 为 complete-normalized-parent-cached-current-eight-column-PCG-SOC-v1；纯读 schema 为 actual-complete-normalized-parent-current-eight-column-PCG-SOC-readout-v1。原892f、6c59、50a9、009e不改，不把旧报告重标签。

新组件准确绑定为 ac03c43dba4c24016a79012e322d66a53b0ed155a1e5e00065e476846cc8ec33，原 face-PCG v5 为76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8。原 fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4 继续负责 StreamedRows、全部 Phase I 和可选准备失败后的原 QP。

原物理234ac、parent provider d3f25、29e2正谱桥、e837谱目标、e716同父全行 SOC 与 a2c6全部半空间投影均保准确原字节。整个33-role来源表保留原物理/目标/norm/几何/地址/投影，只有 cache role 改为明确新完整实现，并另保原 cache/driver/deriver 来源。完整SHA表可从新 driver literal SOURCE_PINS逐项复核，不以简称替代实际源检查。

## 3. 当前完整 A、母坐标与八列

每个 metric phase 固定当前完整自由点 x，调用原 NativeLinearization(q,x,stage_weights,parameters)。外缩放保留原字面公式

$$
\mathrm{factor}=\sqrt{\frac{k}{\mathrm{scale}^2\,\mathrm{normalizer}}}.
$$

helper返回的 A/rhs直接用于QP；driver独立核 factor.hex 与原式实际字相等，A形状等于完整观测/变量维度，enabled标志对应实际 B是否存在。每次 A/A*运算仍经原完整 J/J*及原母范数 lift/transpose；core逆图、parent归一化、闭合升降和全部Gram分量都在原链内。

八列为H、首个原自由core系数、三个最低旋转谐波槽各两条完整径向三jet。径向多项式是 $p_0(t)=t(1-t)^2$、$p_1(t)=t^2(1-t)^2$。在当前完整实际mesh/S取value/slope/acceleration后，通过本场原node-jet或integral白化的准确逆映射进入母坐标。原端点mask、角权、全core/H和未入粗框架的其余变量全部继续存在。

每列真实调用完整 A 与 A*；成功准备明确付 **8次A和8次A***。逐列释放完整quarter-orbit输出，不存full-n-by-8或full-rows-by-8大阵。完整全角逻辑rows和实际quarter bridge行数分开记；单列字节不是总峰值，原桥/场算子的临时数组另计。

小阵为

$$
K=\operatorname{sym}(W^TA^TAW)+\mu^2W^TW.
$$

使用实际 literal $W^TW$，不假装浮点QR准确正交。**原完整QP仍是$\mu^2I$阻尼**，没有改变A、rhs、C、b或目标单位。实际data Gram非对称缺陷、SHA、完整小阵及成功Cholesky被记录；代码不剪裁负特征、不加ridge/jitter、不删粗列来伪造原K。

成功后使用R681平方补式

$$
B=\beta(I-WW^T)^2+WK^{-1}W^T,\qquad\beta>0,
$$

并由原v5在原Euclidean活动行基Q上采用R685面逆。这一代数不要求把工作W声称成精确正交；实际W与小阵仍需数值误差责任。一次Cholesky成功不是浮点全算子精确SPD或连续可行性的证书。

## 4. 分派、失败与Phase I

这次准备得到的一个B.apply固定用于整个QP；下一外方向必须从真正当前x、目标、norm和实际mu重新组装。不得把之前父、之前mu或之前Phi的Gram拿来冒当前H。

完整来源、布局、当前点或norm不匹配明确抛错。可选数值准备阶段的非有限、线性代数失败或MemoryError如实返回B=None和optional_numeric_preparation_unavailable；v5 wrapper在**任何PCG chain之前**完整委托原v3，A/rhs/C/b/mu不变。partial A/A*尝试数和成功列数分开保存，已付费用不归零。

已经进入PCG后，B应用或数值下降性失败按原76b真实truncated status返回；不会在原chain中静默改identity。活动面Schur准备失败的整面PBP回退仍是原v5的显式分支，次数及成本保留。纯读取分别归因setup→v3、面准备回退、chain应用失败。

Phase I继续原v3、原公共slack、正interior搜索margin、全部C以及真实违反量下降接受。它不调用八列prepare；slack不是物理可行性。源码中的qp仍是fb4e，供原行运算和Phase I；qp_v5是独立metric求解模块。

## 5. 原后退锚SOC与完整缓存

从原alpha=1开始到main末尾的整个ray/SOC/候选选择/最新永久点重读/唯一接受/保存/最后统计后缀，deriver逐字核同892f。所有原top-level科学接口及所有main-local统计、几何、memory、cache函数AST不变。实际改变仅metric准备和求解分派、新来源/报告以及明确新旧schema续接。

最近被拒但真Phi下降的ray仍在原ray找到真可行fallback之后选定。整个同父x、原QP方向、固定锚、原C prefix与新增行全部保留。每个SOC重新读完整A*z、同Phi、域、全grid和所有永久点；候选按已有同Phi排序后，在最新memory全重读。两候选都失效则继续原剩余ray，原fallback未被先行偷偷接受。

78f cache完整复制50a9，仅增真实892f旧producer和新self。原完成报告、每role源码、234ac/d3f25/9ca、same-run、完整inputs/model/target/norm、literal query、manifest、每文件checksum和hardlink检查保持。旧50a9完成manifest只在全部同immutable numerical input成立时采用；新consumer在自己的manifest记新producer。更早legacy从未承诺的checksum仍明确披露，未反写虚构证据。

从892f父续接会核相同SOC policy与helper/projection；完整同norm/model/四输入/target及真实final checkpoint通过后，原q.load_checkpoint载入完整x。**启用PCG不重置到q.initial。**

## 6. 完整纯读与公开数据边界

新reader保留009e全部source、目标、norm、cache、row prefix、后退锚、全SOC、真接受、最新memory和finalbundle验证，另核当前prepare的source/x/g/norm/mu/factor字与完整维度、完整成功/部分列计数、同次v5保存metadata逐值相等、固定B/活动面分支和Phase I未误接。

原8×8 Gram/H/factor及大报告只留runner。纯读在runner内选择已有对角、SHA、skew、计数、耗时和失败记录，不重算Gram、特征值、分解或科学数组。**对角摘录也只留runner，包括把数组编码成JSON字符串的形式。** 公开队列summary仅保source/SHA、skew、实际计数/耗时和正因子等标量，不公刊矩阵、对角数组或其字符串。原v5 fallback_faces是整数，reader不误当list计数；partial setup满足completed≤ATcalls≤Acalls≤completed+1，不能从未完成列推断零费用。

必须把setup、QP与完整真筛一起计价。压缩SPD、iteration_limit、有限投影或工作网格通过都不是原QP驻点或连续几何证明。当前性能和最终效果尚待真实Actions。

## 7. 实际父上的完整候选

computations/resume-20261126-current-eight-column-PCG-SOC-after48-ready.json为 **17,581B**，SHA256为a715ab7d3531e996b404692ac9368690af395d10181a0d9bbddae8d8dd66b17c，明确prepared_not_admitted。它不改已排原892f单准入pair。

此候选具体使用实际run04 stage48完整父a801cf94cea863374b4453046c09bfb95a24903a8e6bb0e0a7ccbf6915de4b37，完整report bf64118bed66e05a24f80741e02b0a5ad45d521d6da25985809a75b1a96450df，同c4b2范数、2612目标、实际mu=.01。全部110科学argv保原1×64 metric、4×64 restoration、15ray、8SOC及原接受门；原locations与实际39/40/44/46/48六个显式history完整保留。

如真正执行前已有更新同目标父或新地址，必须新建明确父/全history请求；不可把这份准备中的旧父候选冒作最新。任何新runner需完整合法输入再生和真实新返回身份，不能从SHA合成raw或搬科学缓存进Git、release、artifact。原892f续算不等待本组件性能试验。

## 8. 已实做的静态检查与未完成责任

五件全源均通过实际AST/compile、重复literal字典key、尾空白检查。完整launcher科学CLI AST等同。四组完整diff可审。deriver先调用原4243完整复现174b→892f及原launcher→6c59，再以唯一literal edits复现全部新driver/launcher/cache；所有33 role实际SHA逐项核。

完整--verify-existing已经在scratch候选和公开依赖上真实通过，没有导入科学模块或调用F/J。原ray/SOC后缀逐字、全部物理接口及main-local函数AST已核。geometry另独立静态核当前A/rhs/B/None/v3分派、原Phase I、计数分离及reader对应ac03/76b真实字段，没有设置额外数值门。

初次纯验证曾因旧launcher文件名误写成不存在的restore_qp.py报FileNotFoundError；最终6420源已改为真实launch_so3_cached_interior_restore_actions.py，并整条重验通过。该失误只在未刊纯源码派生检查阶段，未运行科学或冒成功。

尚无新PCG方向、数值fixture、F/J、粗列产品或速度比较。待付责任是实际公开Actions返回、同父Phi/几何/全部成本归因，以及题README的连续metric、全t几何、reach/幅度/闭合/嵌入和固定g精化。本套源码闭合不是研究完成。
