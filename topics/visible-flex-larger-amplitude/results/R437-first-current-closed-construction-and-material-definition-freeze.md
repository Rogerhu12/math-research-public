# R437：首个真实闭构造的参数选择、材料定义冻结与同作业接线

作者：ChatGPT amplitude agent（AI）。日期：2026-11-16。

本结果是明确参数选择、条件恒等式及完整源码合同。没有执行新的 BVP、径向重放、FFT、区间覆盖、编译或数值检查；没有生成 accepted450、实际 H、marker、reach 或 held 结论。实际运算只在本库公开 Actions 中进行。本文与随附运行件不修改原 193、R438、R409 或任何既有科学门。

## 1. 本次解决的实际接口缺口

完整453接受后，冻结同十参数再真实重求的450才是后续原场输入。R409 径向重放只需要该 checkpoint、同作业原 geometry 和源闭包，并不需要帽高 H。相反，R413 原 cuff atlas 需要显式 W、H 和全部 marker。旧闭面构造的 H 从旧绝对高度表得到；当前 R409 使用本次完整径向重放的 background mean 与全部 Fourier node，不能只搬旧 H 或将尚无实值的 H 填零。

本次独立薄接线采用：

1. 真正完成原 R409 径向重放；
2. 按第3节声明的有限字面定义选择首次 H，以及原先声明的 W、四个 marker；
3. 形成真实第一份构造记录 A，再执行原 R413、R409 shared-field；
4. shared-field 完成后保存真正的材料/注册/归一化记录 B，解析声明的四个 held 见证地址；
5. 原 R426 metric、R435 完整块组织 reach 继续各自执行；独立 R425 held 使用同一实际 shared-field 与 witness plan。

第2、4项是定义构造和来源责任。它们不把任何 solver 失败改成通过，不证明原几何目标已达到。metric/reach 不以 held 见证成功为前提，held 也不以 metric/reach 成功为前提。缺失实际依赖、资源停止和数学未证分开记录。

## 2. 可选择的量与必须来自原场的量

| 量 | 本次来源及责任 |
|---|---|
| 准确 C、全部许可原根语义、cut/cuff、完整十参数 | 当前真正两阶段源与 checkpoint；不得由旧九族、另一 C 或数值影子替换 |
| 全部112 core 与完整338物理行 | 当前真正450；core 是该次解的未知数，不是仅由十标量参数定义的常数 |
| 全部576段、原步端、2048角与两 mean | 原 R409 径向重放；不缩模或借旧删 raw |
| W | 明确选择 `float("0.01")`，原构造允许的自由参数；原宽度条件仍实际检查 |
| marker 标量 k | 明确选择 `float(Fraction("1/160"))`；定义记录同时保存准确文本与实际 binary64 词 |
| H | 首场原径向数据按第3节计算一次，保存准确有限表达与最终 RN64 词；不是旧场 H |
| 全部 marker 中心/半径/幅值/所在帽 | 同一真实 cuff 词和第4节明确操作次序；全部词冻结 |
| SE2 registration、inlet normalization、mean/core gauge、phase rule | 当前 R409 真正形成后记录；不得用 source 名替代实际数据 |
| K、tau、eta、覆盖预算 | 随附小配方明确声明的实验常数与资源；不预付相应定理前提或 README 比例 |

旧 `exact_20261114_refined_closed_assembly.py` 与 `geometry_20261114_large_core_closed_assembly.py` 的完整配方已经有 W=.01、marker-k=1/160、四中心及幅值的选择。旧 plan 的额外 index/kappa 字段不是 R409 的 marker API。新列表每项恰为 `upper, center, radius, height`，保全部值并由 R413/R417 原验证处理，不假贴旧 binder/schema。

## 3. 首次 H 的完整有限定义

以下 Q(x) 表示一个实际有限 binary64 词的准确二进有理值。令当前112个 core 词为 c_m，当前完整前缀末节点的垂直物理行是 z_0,z_1,...,z_112。使用与 R409 `prepare` 相同的完整材料 mean：

$$
\mu=z_0+\frac12\sum_{m=1}^{112}(1-4m^2)Q(c_m)Q(z_m).
$$

式中 z_0 同样准确提升；没有省略零模或任何高列。R249 `normalize_inlet` 只改变首节点的原三个 jet 块，因而此末节点 mean 没有通过重新归一化偷换。

令 t_0 是本次 `CurrentRadialReadout.defining_node_coefficients(last)` 所返回垂直 DC 词的准确提升。该词来自原完整2048角 binary64 FFT；准确提升此词不证明它等于连续积分或精确 Fourier 系数。令 sigma=-1，并定义

$$
O=\mu-\sigma Q(t_0),\qquad
H_* = O-\sigma\bigl(Q(B_{\rm cut})-Q(B_{\rm inner})\bigr),
$$

其中 B_cut、B_inner 分别是本次径向完整 ledger 最后、最先节点的 `backgroundRKInnerAnchor` 原词。实际选用

$$
H=\operatorname{RN}_{64}(H_*).
$$

`Fraction` 加乘到最后 `float` 的次序明确。定义记录保存每个输入准确词、H_*、H 的完整LE64、Q(H)，以及 Q(H)-H_*。不增正数、不加几何容差、不在非有限或原域不合法时偷偷换另一高度。

**条件恒等式。** 原 R409 对每个真实径向节点的背景值恰按 O-sigma(B_cut-B_i) 形成；因此 H_* 是其首 native 内节点背景值的同一有限准确表达。新选 H 是该表达的一次 binary64 投影。原 cuff 节点仍为 `(H,0,0)`，原 native 首节点的值及 w/w_r 仍照原源保留；二者之间的 Hermite B 由原完整节点定义。

这条恒等式只说明本次帽 datum 的来源。native 内半径不是 cuff；本次没有声称 H 等于原准确连续 C 原函数在 cuff 的积分。R409 明确保有 `exact_RK_background_words_not_an_exact_continuous_C_primitive` 与 `target_metric_not_replaced_by_Bprime`。当前几何 B 不选取原 C 根族的某个成员，也不替换原目标 E。

## 4. 四个弱 marker 的准确身份和条件范围

设 c 是当前 C 的真实 `physical_parameters.rCuff` 词。按旧构造的 binary64 操作次序形成

$$
C_1=(c/2,0),\ C_2=(0,c/2),\ C_3=(-c/2,0),\ C_4=(0,0),
$$

$$
R_i=c/(8i),\qquad A_i=k\,c\,c/512,\qquad i=1,2,3,4.
$$

前三个放上帽，第四个放下帽。上述式子在代码中按明确 binary64 顺序求值，不能把舍入后的 A_i 宣称为未经舍入的准确 k c²/512。每个实得中心、半径、幅值以及 W/H 均另存LE64，负零不丢失；后续同作业 reuse 逐词使用第一份值。

固定帽始终是原 R409 的

$$
F_{\rm side}(x,y)=\bigl(x,y,\operatorname{side}(H+b_{\rm side}(x,y))\bigr),
$$

$$
b_{\rm side}(x,y)=\sum_{i\ {\rm on\ side}} A_i
\left(1-\frac{|(x,y)-C_i|^2}{R_i^2}\right)_+^4.
$$

高度、导数中的 side 与完整重叠求和都由原 R417 保留。R413 必须按当前 cuff 实际证明支撑与其平坦内环分离；这不是仅从本配方名称推出。

[R24](R24-weak-markers-with-explicit-reach-margin.md) 的弱标记结论有完整未标记曲面 reach、真空间支撑间距 d_0 和全法向弦前提。旧 k=1/160 是其中一个严格有理预算示例，不是本次已通过的 reach 证明。本次 work-choices 还明确选 K=1250/149、tau=1183/10000；准确代数给 K tau=1183/1192<1，只支付这一常数关系。完整全场曲率、AA/CC/AC 所有原点对、嵌入和 tau/D≥.03 仍须当前消费者真实支付。D≤1183/300 只是该比例要求的等价候选上界，本文没有给当前 D。

## 5. 首次材料定义必须一同保存

[R443](R443-common-material-angle-pullback-and-fixed-closed-target.md) 已明确：当前 R400 saved-prefix 读取的是当前 checkpoint 的 core，故同 C、同十标量参数不保证同 q 图中的目标系数相同。用这些完整准确词定义

$$
\Phi(\phi)=\phi+\sum_{m=1}^{112}
 \frac{(1-4m^2)Q(c_m)}{2m}\sin(2m\phi),\qquad \phi=2\pi q.
$$

R437 的 `material_definition` 保存112词、准确二进有理值、全部频率、准确 density 与 sine 系数，以及原675准确解释器/1c7 loader 身份。它没有用先经 binary64 乘法形成的 `saved.density` 代替准确系数，也不执行三角函数、材料逆或新的全圆正性检验。

第一份记录 A 在实际 radial 后保存：完整构造词、十参数、C/target 与 cuff 身份、首 checkpoint、完整112材料定义、原 fullDN member、H 形成式以及原截止钟。它明确说此时 registration/normalization 尚未形成。

第一份记录 B 只能在原 shared-field 真正完成后产生。它从同一七元组 `(paths,plan,assembly,target,saved,A,bindings)` 的真实文件读取并完整保存：

- `single_global_planar_registration`；
- `inlet_normalization`；
- `mean_gauge`、`core_and_hold_gauge`；
- `phase_rule`；
- 当前完整112材料定义、全部构造词、真实 source/field/checkpoint/deadline 身份。

完整记录仅留本作业临时树；必要结论只保身份、范围和少量实际比较标志。不会把归一化大树重新编码拆传。

## 6. 后继 reuse 的准确含义

`reuse-construction` 要求实际第一份 A 和 B 正文、bytes/SHA，而非只有旧摘要。它复用首场 W/H/全部 marker；不按新解再选 H、不重造四中心。完整同十词与当前目标来源仍由原 checkpoint 合同绑定。

它同时读当前真实 core，并记录首、当前 core 词是否相同。shared 后再次保存当前 registration/normalization/mean/phase，和第一份对应字段作元数据比较。比较包含来源记录时，字段不等不能自动解释为数学函数不等；比较结果也不作为新的 BVP、metric、reach 或 held 拒绝条件。

**本次明确未实现共同角拉回。** 当前 R409 仍用当前场自己的材料角。即使 A 的全部构造词相同，也不因此把当前 q 图称为首图上的同一完整 g。R443 的准确方向是

$$
\psi_j=\Theta_j^{-1}\circ\Theta_0,\qquad \Theta_j(q)=\Phi_j(2\pi q).
$$

真正的后继须消费第一份定义并按完整链式法则实施这个拉回，或使用 R443 条件下对全场 metric 证明的准确运输解释；还须保共同物理角 cuff 与帽笛卡尔图的拼接。R441/R442 的独立实现承担这项责任，R437 不预称它们已执行。

帽 H 是常数位置 datum，不进入帽的诱导 metric；它仍影响像集、全直径、reach 和 held。registration/normalization 对实际场的影响则仍由原 R249/R416/R418 全域责任处理。不能因 H 不进入帽 metric，就把所有构造来源一起省略。

## 7. 声明的四个 witness 只确定真实地址

本次固定计划是准确新场首个 `kind="prefix"`、`left=0`、`right>0` 的实际片；坐标 radial="0"，q依次"0","1/4","1/2","3/4"，lower=false。helper 在实际 R416 片表中找到唯一地址，不把旧 mesh 索引搬到新场，也不凭当前输出选择较好的见证点。

输出符合原 R425 `R425-current-accurate-active-quarter-turn-witness-plan-v1`，每项恰为 `piece_index,radial,q,lower`。helper 不算这四点的场包围、距离或 delta_E；原 R425 在同一 current field 上实际评价并作其原四分之一转中心及整像覆盖。

有限四点可能不给正的 held 下界；这不是驻点或不可能性证明。原反射范围、完整 D、全部帽、非平性、标记唯一性、全像覆盖和刚体/反射商责任都保留。未证项按原字段返回，不能由存在 witness plan 推出已完成。

## 8. 三种明确的来源分支

本源保留原 R438 的 `original193-frozen450` 与 `R431-refined450`，另显式增加 `joint203-frozen450`。joint 分支严格绑定 R444 的新 driver/launcher/schema/deadline，而不是把原193的provider名称改标签：

| 新来源 | SHA256 |
|---|---|
| joint driver | 5400aa4a724b0403e6a89db2ea056f489dc336e685fa85e2ef1ef0fc51569592 |
| joint launcher | cb05724bbedf71951524d187d242c1783d244bc729241ec91a91e0a9cf8f02d7 |

新 branch 将原 R438 `bind_original193` 的实际两阶段接受/quiet/checkpoint/C闭包正文完整放入独立函数视图，只变明确角色常数及函数名。原43f writer与完整450状态来源不变。R431 分支仍是其已发表的原193来源合同；本次不冒称它已支持未来 joint mesh/R441。

每个分支都先消费真453接受、同十词真450接受、原 native/fullDN/freshFD/finalaudit、原 owner 静止；没有 accepted450 就返回原未启动后缀。当前没有拿未来193或203结果填任何值。

## 9. 原钟、独立消费者与清理责任

选取的 deadline 必须与原 launcher 实际 `actual_job_deadline` 的 bytes/SHA一致，再核真实 run/source/recipe。仍是 namespace 建立后18900秒 science、2700秒 readback reserve。局部阶段 cap 只与真实剩余时间取小，不能在径向、参数动作、held 或 mesh 开始时重启总钟。

原五阶段 `radial_replay/original_cuff_atlas/shared_field/metric/reach` 的完整CLI、原 OwnedChild、stop/wait与原科学阈值不变。两个参数动作复用同一原 lifecycle 的独立行，保全失败/未访地址。它们耗时同样计入原钟。

若 first construction 未形成，依赖 H 的原 atlas/shared 后缀不能伪启动；若 witness 或材料记录动作失败，错误实际保存，metric/reach仍按其原独立前提执行。held 只在其真实前三依赖、实际 witness 和静止来源可用时开始，不检查 metric/reach success。

原 C 的四metadata及 `complete-source-radial-panels.jsonl`、`source-piece-index.json` 留到R426实际消费者结束。accepted450的完整 raw、径向节点、七元组、A/B记录及所有新结果留到所有声明消费者与必要读回完成，且所有属主静止。R437不执行删除；总workflow仍由root将此条件加到同一命名空间的末端清理。运行结束被销毁的临时场不能从SHA复原；未来重生必须重新实算。

## 10. 必要读回与证明范围

新 reader保留 R438 原五阶段全部必要语义，附两参数动作、实际 W/H/全部marker词、H形成值、四witness地址、材料来源身份与所有异常/未启动原因。大成功列、全场数组、归一化表与完整frontier仍只在Actions内消费，外部不重刊。独立held沿原完整必要selector。

每份结论仍硬限单ASCII90000B；超限如实70，不删字段后冒complete、不拆编码运输，也不将元数据70解释成科学反证。尚未有本源实际必要输出，所以没有字节余量或性能保证。协议允许读取一个真正完成的参数结果文件而其stdout必要摘要超限，依然记录运输超限；这不把缺失字段推成通过，最终总读回仍须诚实完成。

本次条件结论只支付明确的构造顺序、来源、上述有限H恒等式与冻结作用范围。全闭面正则/嵌入、全t metric、全原pair reach、README比例、全像held、含反射delta_E、同一g上的真实网格/角/谱精化仍须实际结果。source/API完整不等于这些结论已经付出。
