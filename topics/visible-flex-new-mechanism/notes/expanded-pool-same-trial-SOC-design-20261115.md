# 扩池后对同一失败试点作一次 SOC：最小准确合同

日期：2026-11-15。提出者：tail_cost。状态：纸面/源码合同，尚无新人工或科学执行。
本稿接 [norm-memory 首实际](norm-memory-first-actual-result-20261115.md) 及
[十一模型诊断](norm-memory-eleven-model-diagnostics-and-next-SOC-interface-20261115.md)。

## 1. 唯一拟改变的分支

已有公开运行43741276060/source c30e7ea00a9ae06356409d5fdae289dfecf2210d中，模型1、5、10的试点已完成原两网普通值，但发现新增原行后立即返回最后已接受点，因此0次SOC。模型5、10的新增行仅soft，而失败曲率行已在原primary中；其真实曲率残差并未由完整metric范数模型消除。

新方法只替换这个分支：

> 同一个未接受的 full primary 试点 \(y\) 学到新行后，冻结 \(y\) 的实际两网数据；回到同一已接受中心 \(x\)，按扩大后的原行池重建完整模型。若原预算、正预测下降和所有绑定条件仍满足，对同一 \(y\) 作一次原SOC。

正常 primary、没有扩池的原SOC、真实值、原14门、原物理盒、原半径尺度和controller公式保持。未通过新绑定或预算条件时，仍执行原“扩池后返回”行为。本轮不并加near-active硬行/邻点预覆盖，不改曲率floor，不改12LP/40共享值/120秒active限额。

## 2. 固定物理输入与延续来源

下次只能从已完成run43741276060的 future_direct_checkpoint恢复，不重复其优化：

- 完整reference163的binary64精确数；
- final159及其对应final163精确物理数；
- 共同exact null-height映射和原九高度参考；
- 两个完整原行池及其原网格ID；
- 终态B=1/16000及success_streak=1；
- 同一完整 \(g,b_0\)、163物理盒、Pi定义和两网节点。

当前norm-memory报告未直接保存bank内部entries，但已找到完整事件重放接口：祖run43728280256的19个原seed，加本次模型8唯一新cut轮的2个 directional_oracle_attainer，共21条有序输入。不能再把 complete_model 镜像中的同一cut算第二遍。后两条保持原 lp.model.binding_sha256 来源。

在runner中沿原unit函数重放，首次primary_observable_model消费pending输入后、求LP前，必须核bank最终9条及原state SHA
07a1f00af0acc950a7db91c698d824b3ce47324921272f45b2e2b1b1eca18f81。
只有实际hash吻合才能称精确恢复；不吻合立即停止，不能退为未声明的新bank。
恢复不调用旧优化器或旧人工。源/原日志/事件路径/hash均绑定，重新可算payload不进入仓库。

此直接输入消费与新科学分账；新科学只运行一次。原source、旧已通过开发和已完成优化都不重跑。root拥有transfer/audit/workflow/ref/Actions。

## 3. 两个绑定上下文，不能覆盖或混用

设原outer模型为 \(C_0\)，包括：

\[
(x,\mathcal I_c^0,\mathcal I_f^0,v^0,J_x^0,g^0,\tau^0,
 B,\;M,\;D_{\rm phys},\;\mathrm{primary}_0,\mathcal A_0).
\]

其中 \(\mathcal A_0\) 为完整两网affine-e/f谱范数模型，\(M\)是159到163物理映射，
\(D_{\rm phys}\)为原物理盒宽度。原LP输出、原步、原试点记录和原误差分解永久归属于 \(C_0\)。

试点学习后池为
\(\mathcal I_c^1\supseteq\mathcal I_c^0,\mathcal I_f^1\supseteq\mathcal I_f^0\)。
新上下文 \(C_1\) 必须在同一 \(x\) 上按完整新池重新构造：

\[
C_1=(x,\mathcal I_c^1,\mathcal I_f^1,v^1,J_x^1,g^1,\tau^1,
 B,M,D_{\rm phys},\mathrm{primary}_1,\mathcal A_1).
\]

不得只是给旧矩阵尾部添一行、改旧版本号，或把当前 \(y\) 的导数当成 \(x\) 的导数。

### 3.1 必须原样相同的对象

- \(x,y\) 的159实际数组和163规范物理身份；
- 原独立坐标定义、runtime field/H/九高度参考和固定 \(g,b_0\)；
- 全部原物理上下盒、物理宽度、159→163映射；
- 原coarse/fine有理径向节点、完整均匀角网格及group/branch语义；
- 原B及body/tail/height尺度 \(B,B/8,4B\)；
- \(\epsilon\)、metric target、old metric预算、strip/curvature floors及所有真实门容差。

### 3.2 必须重新生成并记录的对象

新池版本、完整IDs及顺序、\(v^1,J_x^1,g^1,\tau^1\)、selected-model签名、
完整observable/方向oracle binding、scalar/full预测及SOC上下文。

对所有旧IDs的行值/J可另存同中心差异诊断；不能只靠shape相等或旧签名相等授新绑定。

## 4. 固定失败试点及其实际总位移

第一版仅适用于第一个full primary：

- kind为primary-metric-short-step，alpha_exact=1；
- \(y\) 未被接受；
- 原两网普通值均已经完成且regularity通过；
- 此模型还没有调用SOC，没有进入parabolic分支；
- 本次扩池完整成功，没有容量超限；
- 原LP、value和active预算仍允许一次SOC及其真实验值。

保存原名义proposal \(p\)，同时形成实际binary64位移

\[
d=y-x.
\]

新SOC使用 \(d\)，并先严格核
\(\mathrm{apply}(x,d)=y\) 的数组逐字节相同及规范物理SHA相同。
若浮点往返不相同，保留原失败事实并返回，不默换 \(y\)、不把 \(p\) 与 \(d\) 当成同一数组。记录两者的hash和差异，保证所有后续“同一试点”陈述有实际依据。

在切换缓存回 \(x\) 前，冻结原完整 \(y\) 的两个 FullGridValues、网格定义、共同高度 \(b_y\)、全部rows及状态身份。这里读取已计算数组；不得先切到 \(x\)，再调用 full_views 并把它们命名为 \(y\)。

冻结对象须只读，必要时复制；后续池学习或缓存复用不得改变它们的值。SOC只需真实两网rows/共同高度/网格和身份，不要求为 \(y\) 重做普通geometry或全Jacobian。

## 5. 原入口重建 \(C_1\)

1. 保留原failed trial及实际新增行明细；先读出新池的全部IDs/version。
2. 恢复同一已接受 \(x\) 的ordinary缓存。若原缓存能复用则复用；不能复用的普通值调用照常计入40共享预算，不能称免费。
3. 用原 objective.linear_rows 得到完整新池在 \(x\) 的base/J/groups/tolerances。所有新增或必要重建J费用进入当前active clock；不重启clock。
4. 用原 selected_model 在同一 \(x,B,M,D_{\rm phys}\) 下建立 primary1，不求解第二个主LP。
5. 由相同冻结factory建立 \(\mathcal A_1\)，完整原两网方向计算仍保全部角后再取点。selected与complete factory均会扩展primary签名，因此必须等二者完成后生成最终model_binding；factory前的scalar签名只可另字段留存。
6. 记录最终新model_binding及两网IDs/hash，核actual-y视图与新primary的网格、共同高度规则兼容。rebound不求primary LP，在首次slack前调用原oracle.set_post_primary_phase()，将其费用准确记为actual-total-step-prediction。
7. 新context存在后，旧layout guard仍有效：只接受新context声明的当前版本；不能改成跳过guard。

已有 selected_model 的原检查会逐项核
selected values=base、groups和tolerances完全相同。build_primary同时重算原耦合物理盒、cap invariant、outside限制以及原步尺度。这些原式检查继续使用，不用另造弱替代。

## 6. 原scalar预算与完整affine预算分开

令新selected scalar模型的基准和同一 \(d\) 预测为

\[
\rho_{0,S}=\max(0,\rho_{\rm out},\max_{i\in S}-v_i^1),\qquad
\rho_{1,S}=\max(0,\rho_{\rm out},
 \max_{i\in S}-(v_i^1+J_{x,i}^1d)).
\]

完整两网affine-e/f模型另给
\(\rho_{0,F}=\mathcal A_1(0)\)、\(\rho_{1,F}=\mathcal A_1(d)\)。
四个数都按新绑定计算和报告；旧primary返回的LP辅助量没有参与替代。

先要求所有这些量有限，原scalar gain
\(\rho_{0,S}-\rho_{1,S}\) 大于原improvement_floor；
完整gain \(\rho_{0,F}-\rho_{1,F}\) 也必须大于该floor。
任何一个不满足均不求SOC，保持最后接受点。

本次SOC仍用原build_correction的预算

\[
\beta_S=\rho_{0,S}-\vartheta(\rho_{0,S}-\rho_{1,S}),
\qquad
\vartheta=\mathrm{SOC\_predicted\_descent\_retention}=1/2.
\]

同时可报告
\(\beta_F=\rho_{0,F}-\vartheta(\rho_{0,F}-\rho_{1,F})\)，但不替换原RHS。
不先断言 \(\beta_S\leq\beta_F\)：两种基准不同，应记录实际差值及比较布尔值。尤其不能把某次LP返回的非最小rho当成 \(\rho_{1,S}\)。

新complete模型不需要用memory再次求主LP。相同冻结的方向bank可保留，所有norm数值支撑仍只在其声明的当前中心建立。

## 7. 原SOC数组、物理尺度与真实 \(y\)

记新selected IDs上的实际试点残差为 \(c_y\)。SOC求159独立修正 \(w\)，仍使用 \(J_x^1\)，而非 \(J_y\)。

hard行：

\[
c_{y,i}+J_{x,i}^1w\ge
\max\{\gamma\max(v_i^1,0),\text{原适用strip/curvature floor}\},
\quad\gamma=1/4.
\]

soft行：

\[
c_{y,i}+J_{x,i}^1w\ge-\beta_S.
\]

式中各row、group和floor均由原build_correction生成，不手动改号或用未scaled残差替换。Outside常值预算、constant cap、共同高度、固定物理槽和exact null积分仍按原模块处理。

修正body半径仍为
\(\frac12\|d\|_{\rm common\,body}\)，tail为其1/8，height为其4倍。
原163耦合物理盒施于 \(y+w\)，保物理宽度和原159 pivot缩放。
目标仍是原163物理归一化修正的L1；不是159坐标L1。
原正缩放及解后original-unit residual检查全部保留。

应在调用前核原build_correction以
\(\mathrm{apply}(x,d)\) 计算的 \(y\) 与第4节冻结视图确为同一试点。
这正是不能只把新增行嫁接到旧primary上的原因：new IDs、base/J、
predicted budget、row scale和盒center必须共同更新。

## 8. 预算账与异常

本方法不另开预算：

- 任一新primary inner LP与本次SOC共用12个LP；
- 新J、方向JVP、绑定、LP和优化内checkpoint费用共用原120秒active；
- 普通coarse/fine值共用原40次；独立末尾两次复验仍按原driver分账；
- 每个primary最多一次SOC；本新增分支不额外放宽原maximum_SOC_LPs_per_primary_model。

实现必须在实际进入solver之前记一次started LP。可用显式新薄适配层把原build/scale/solve数学原样保留，仅插入启动账本回调；不能只在linprog成功返回后计数。若构造阶段发现无正gain而未调用solver，则started LP为0；若solver抛异常，则已开始的调用仍计入，保原最后接受点和原异常。

不要重复调用旧solve_correction再由报告猜是否已经执行。一个SOC算法调用必须只有一个linprog入口。各原solver tolerance、time_limit取当前剩余active时间的规则不变。

容量超限、预算不足、非有限值、绑定失败均显式记录，回原安全退出/返回分支；不删除旧行、不重置半径、streak或预算来继续。

## 9. 修正试点与结束条件

得到通过原LP residual检查的 \(w\) 后，在同一runtime field构造
\(z=\mathrm{apply}(y,w)\)。照常执行：

- exact163物理盒及固定高度槽/null积分；
- 原coarse/fine完整ordinary值与全部硬门；
- 旧metric预算与原真实两网 \(\eta\) 下降门；
- 原行学习及capacity规则；
- 完整affine模型对实际 \(z-x\) 的预测和两网误差分解。

对修正trial的曲率诊断，应明确采用
\(c_y+J_x^1(z-y)\)；对接受质量/总步诊断，应明确采用 \(C_1\) 在
实际 \(z-x\) 的预测。两个参照不能混为“同一个预测”。

如果 \(z\) 原门通过且下降达标，按原顺序可接受；
如果它又发现新行，则仍保真实新增记录，并依原规则处理。
第一版**不对同一 \(z\) 再建立第三个context或第二次修正**。
未接受则返回 \(x\)；已接受但学习了行时，下个模型从该已接受点与更新池开始，不能把该合法接受倒称“无新增行”。

没有可用SOC时，本新增分支返回最后已接受点，不新开backtracking循环。原没有扩池的SOC/backtracking路径保持其冻结行为。

## 10. Controller保留、不可洗掉新增行

原failed trial的 new_coarse_rows、new_fine_rows、omitted_hard、
actual gate flags和scale_feedback永久保留。

因此本新增分支的任一成功SOC仍不满足旧SOC-hold条件

    all_new_coarse_and_fine_rows_including_soft_zero

；有新hard的模型1类还不满足primary-only-curvature条件。
不把“新context现在包含这些行”当成“原trial没有学新行”。
新rebound成功仅增加一个原门认可的接受点，不能自动取得持径或增长资格。

调用原 next_soc_hold_trust 时，原controller和所有trial仍用真实历史。
新binding的总步诊断单列于rebound记录，原proposal binding不覆盖；
如为原hold格式另生成引用，必须保持学习事实，不能使全部17条件人为变真。
后继输入恢复应回放同一真实controller，无半径reset。

## 11. 报告与缓存：防止zip错位

当前 attach_complete_model_reports 用outer models与
objective.complete_models按位置zip。若rebound factory额外append一个完整模型，
之后普通模型的报告会错配。

新实现必须选择明确方法：

- 主proposal模型仍一对一存入原complete_models；
- rebound factory可复用原科学装配，成功后将刚追加的complete model立即移入独立rebound_models登记；原complete_oracles保留全部主/rebound oracle，另存明确oracle index；
- rebound登记按outer model number、revision、新binding SHA精确关联；失败构造的部分oracle也保费用/错误，不冒完成模型；
- 所有rebound oracle费用仍进入snapshot和最终stdout，不因分表丢计数；
- 原linear_program报告永远附其 \(C_0\)；新correction和其预测只附 \(C_1\)；
- 不通过修改旧模型下标或覆盖旧dict掩盖多出的模型。

原attach函数还会给每条correction写入所配主model的 selected/full rho0 元数据。
新报告适配在调用原attach后，必须对rebound correction按其精确登记显式覆盖这两项及source binding，保原主proposal的报告不变；不能只pop模型后忘记correction仍引用旧rho0。

可复用原factory的科学装配代码，但对追加账本的操作必须显式且异常安全。
只读数组、同state+pool-version缓存合同和初始pending directions的一次消费保持；
rebound不能再次消费初始norm seed或回放旧科学。

## 12. 建议实现分工及新增接口

tail_cost只新增三个独占文件，不改旧科学源：

- scripts/frame_metric_expanded_pool_soc.py：独立context、冻结真实trial视图、
  同中心扩池后model重绑、预算启动钩子及准确report关联；
- scripts/frame_metric_expanded_pool_soc_recovery.py：从当前norm-memory outer明确派生，
  只增加本合同的单次rebound分支、按context的trial诊断和独立费用/状态报告；
- scripts/frame_metric_expanded_pool_soc_development.py：developer_check()，仅下节新增接口人工。

root负责新的direct transfer、audit、request、workflow与发布。
新transfer从本次完整future checkpoint恢复，并提供上节21条可追溯原事件及 expected_initial_bank_state_sha256、expected_initial_bank_entries=9。新objective只在首次primary安装后做严格hash/entry核验并记录，不在rebound重复seed。

正式类名ExpandedPoolSOCObjective，新增显式关键字expanded_pool_policy必须为same159-expanded-pool-rebound-SOC-v1；恢复入口run_expanded_pool_soc_recovery。**原source configuration逐项不变**：factorizer把digest(cfg)纳入其定义，而方向bank的context包含该factorizer定义哈希。故不得在cfg添加新policy或transfer注释字段；算法声明仅写request和objective.evaluation_definition。原floor/fraction/weight/retention从旧cfg显式读出并在rebound核同，不用两个缺失的primary.information字段相等冒作核验。

root的transfer/audit文件分别为frame_metric_expanded_pool_soc_transfer.py与frame_metric_expanded_pool_soc_audit.py；tail_cost只交未挂UTF8 blobs，不写ref或触发Actions。

科学装配仍调用现有selected-row factorization、selected_model、
CompleteGridAffineModel、build_correction/scale_mapped_correction及原真实验收。
不改ordinary geometry、Pi、完整 \(g,b_0\)、真实height映射、row解析或原gate公式。

## 13. 只覆盖新增接口的人工计划

公开Actions首验才执行。无需重复已付norm方向、163/159地图、原开发套件或原14门科学。新developer_check()只含十项接口检查，按四组组织：

1. **bank与实际步**：完整SHA/9条entry严格相同；错误hash/size拒绝。实际y−x必须以原apply逐字节复原y，不用名义proposal代替。
2. **真实新context数组接口**：只借旧artificial_arrays的固定数据，不调用其developer_check。实际走capture、冻结y、恢复x、linear_rows、selected_model/build_primary、new rebuild及build_correction；核所有新IDs、same x/y、新J和真实y数组。完整observable factory使用明确标号stub并模拟其两次签名更新，以检最终binding生成次序；不把该stub称真实JVP或科学值。检查版本/ID顺序变化拒绝、失败视图不被live cache覆盖及失败部分oracle仍保留。
3. **预算与报告**：started callback成功和抛异常都在调用前扣共享slot；无余量不调用。模拟主模型1、rebound归属于模型2的明确映射，核原attach错误rho0被正确替换、普通correction未变及全部oracle费用保留。这里只测试新边界，未执行真实LP。
4. **当前日志parser**：直接调用root新transfer.parse_records。timestamp与BOM前缀、十一条有序MODEL及唯一COMPLETE均用小标号JSON；原COMPLETE JSON+LF精确保留。缺模型、重复模型、重复COMPLETE均拒绝。没有网络读或旧checkpoint恢复。

以上人工passed只证明所列接口。显式outer的真实accept、original hold/no-recursion及全部真实门仍须由公开科学实际如实消费；不能凭人工数组宣本轮SOC成功。一次实际运行须完整消费同试点身份、新base/J签名、新旧rho、SOC原residual、两网全部gate、真实接受/controller、预算与费用；若无rebound触发，也应如实报告未观察到该新分支的科学效果。

## 14. 可判定结论与限制

新方法若成功，只证明本次已算family/网格/容差下，通过准确扩池重绑定后，
一个原本因新行而提前返回的试点有可验的修正。它不证明SOClocal一定收敛、
更大半径普遍可行、0.26已付，或连续几何/第四阶joint已解决。

若失败，准确分清无预测下降、LP不可行、原residual失败、真实门失败、
再次扩池或预算耗尽；不能合称“完整norm模型失败”。
无论结果如何，既有第一次运行及其三次提前返回事实保留，不重新计算或改写。
