# Request197：完整 Prüfer 行族保留后的联合名义数字行与原完整453入口

## 1. 实际问题、唯一改动与未付责任

实际187（source `6a272aae6a3a0ac864bb2c5769bcf78a6a2312c8`，run `43759238493`，compute `132950069367`，report `132986874120`）已完成全部112个频率的 physical-far 传播、完整不确定根族以及原 Q/Pi 取向单位行族。其后原 `momentum_rows` 对两最终系数盒分别取中点并转换 binary64，实际抛出：

```text
ArithmeticError: Both explicit unit-row representatives rounded to zero; no numeric boundary fabricated
```

原必要摘要没有保存具体失败 mode、两个准确中点或完整转换过程。因此不能从这次记录断言准确中点为零、非零中点下溢、真物理列为零或真实共振；也不能把后置数字行失败回填成112模式传播失败。实际187没有进入 native、当前 H 求解、338×112响应、FD、453 full-DN 或 final audit。

197 是独立的完整重新计算。它继续实际180所选九参数，重新生成当前 C、cut、deep112、真正 factory、数值标量和全部 far 行族；旧187没有任何 C 值、角、系数盒、行、H 或 J 被当作当前输入。正端点 Prüfer 核 `c2f515aa…` 和正端点 helper `91dd207b…` 逐字不改。唯一科学表示改动在完整行族形成之后：从一个真实已提交候选保存的完整参数盒内构造一个联合名义 Q/Pi 数字行，并对**全部原真实行族**保留到该实际数字行的误差包。

这个名义盒点不保证属于任一准确 root 分支，更不保证所有112个数字行、577网格或后续场点同时来自同一个全局准确 C。197 明确记录这些限制。原完整112/224/226和两个 mean、338响应、453方程、所有 $\sigma$、当前 H/FD/full-DN/最终审计责任都没有减少；没有加入“名义误差足够小”等新的原求解接受门。新源是否能完成数字表示、后续完整采样或 BVP，只由本次真实 Actions 给出。

## 2. 科学源、协议和完整闭包

九个新增源均在 `topics/visible-flex-larger-amplitude/computations/`。下列是完整文件身份；blob 只存源码，不是科学结果。

| 文件 | bytes | SHA256 | Git blob |
|---|---:|---|---|
| geometry_20261115_pruefer_joint_row_representative.py | 9205 | `24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97` | `257be53e43a1c933712ee84211c8a2feae76bf89` |
| geometry_20261115_current_C_pruefer_joint_radial_sampling.py | 69702 | `32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4` | `decad25aac951886e0544e35de66f42f0e49ffa9` |
| geometry_20261115_current_C_pruefer_joint_native_worker.mjs | 18377 | `d015a52c126b26a749ed1dfd60d613fdf09c54826a9465c7e38824d41bda6e4a` | `4fa34b7e6afd271d7cdaf624403bd7575f476a07` |
| geometry_20261115_current_C_pruefer_joint_tail_client.py | 23164 | `02e1645248ef01ffff10a50c2198194fafd40709254816408e1b9944e1cd0ae1` | `c013eee5dbaf12460fa57778bdd1144bbbeafab2` |
| geometry_20261115_current_C_pruefer_joint_full453_physical_dn.py | 64245 | `c71d616936cf33e43965906c7cc99face01d06a12433420474b688b8d76b946d` | `466d751bf3ad3ab73f80a434e46f41b132126a74` |
| geometry_20261115_current_C_pruefer_joint_full453_launch.py | 19263 | `d655e62d6a746cdd5c98338959537b3d65c93b105818dd5a39c46343a70771ec` | `b169389dd234af975c05ead090ba040b445f4c0f` |
| geometry_20261115_selected_coast_joint_owned_process.py | 14001 | `440987bb74d2f3a17e36a6e893a076693db0486d9471e1e4a9d6704f45ec6e9b` | `97805a38157d8f1454b4821513636f73cb05dc9b` |
| root_20261115_current_C_pruefer_joint_full453_necessary_readout.py | 55181 | `19878e48ed25dec8bdcbd36c3d7ea7168796a08fb60675ad7455dbb296a0918c` | `fbb96d8f034b9eb0758a193bc05dea605cfd7100` |
| geometry_20261115_selected_coast_joint_current_C_pipeline.py | 42631 | `7628a0be12c235e6e30088668755d20ebbdd14bc7f060fe43f15f42f721ded0d` | `ea041b61f167d74ed4f6631f561be504024334af` |

新 sampler schema 为：

```text
current-C-pruefer-joint-nominal-row-physical-radial-samples-and-general-far-v1
```

新 BVP recipe/driver 保原 R300-v3、三个 active 和完整453责任，但改用独立的 `current-C-pruefer-joint-nominal-R300` 协议身份。请求文件为：

```text
public-selected-coast-joint-current-C-full453-request.json
```

其 74777 B / SHA256 `f64705668b7ae4189f530473feb8154435fe582129d4153f198d75c3d0afcf0e`，blob `d3719d1af54e1693c3cda4e97af155cb77d27966`。工作流为：

```text
.github/workflows/visible-larger-public-selected-coast-joint-current-C-full453.yml
```

其 81174 B / SHA256 `f0128cbd83344fe65f83a43cbc41f0771f2d0152a23fcc40a98aa23dff487d02`，blob `8324db367b27db61d7949675c5099733225a974b`。独立 trigger 路径、concurrency 和临时 namespace 均为197；不会修改或取消187等已有 run。

请求保留原187的84个 source pins 全部原值，新增这9件，共93件。原84件不是当前结果；其中已被新独立 source 替代的旧入口只作数学/协议来源。当前 driver 实际 PINS 为56，native configuration 实际 source closure为30。worker 的 helper依赖加在原 required-source 列表末尾，原前五个索引和 original worker/client/native核心引用位置没有移动。

当前 driver 的完整闭包中，原187 sampler/worker/client三项换成新三项，加入新 joint helper；原正端点 kernel/helper、原 general-Robin native、同步完整 QR、原 matched variational engine及其原 runtime 均未改。原 driver入口自身有独立 source identity。原源没有在同 basename 下静默改写。

数值 row 的定义与误差责任详见 [R419](../results/R419-correlated-nominal-Robin-row-formation-with-complete-family-errors.md)：10693 B / SHA256 `da5969fda0b4e5545b4988090fe0135c44542af4b5514cddaea13d5b6e290dbb`。R380、R357、R383、原完整 native/full-DN责任仍分别保留，不以 R419 的文件存在代替任何实际计算。

## 3. 实际180点与来源恢复

唯一初始准确点仍是 actual180 的首个全域证明候选 $\beta=1/16$，参数顺序

$$
[p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3].
$$

原准确有理字为：

```text
1375945989099287/4503599627370496
7798437871654891/36028797018963968
6173543729074581/288230376151711744
-569465276708805/9007199254740992
-5036686613378861/288230376151711744
8445254225196179/144115188075855872
4841957884391517/4503599627370496
3101584203429797/4503599627370496
8453645258162737/144115188075855872
```

actual180 source `636bbc30601cb577266219ed66bb2759d285badc`，run `43753422569`，compute `132932188151`，report `132932432397`。原必要摘要64284 B / `503d2e7d86359c687842e5ce2d5161cac951c7a0b80c5d2b08f5bec3231dcafd`，口径不含帧分隔 LF；原 report HTTP log132994 B / `cc6ed5447996a677aade026d603657d86236c6b70f76b1f2dd726891e710e585`。

197沿原187方式在 Actions 内一次读取该小 report，逐全文件 bytes/SHA核回。原 `630c288e…` 只恢复 actual165 已存在的准确 definition/input字段；原 `ba8fb7f3…` 以原180实际 run/provenance作为输入值，确定性重建真实 selected recipe2136 B / `cc87d9327c33a208ac36e7dadaa5608cc3597e8d9f9bc0bd615631a6681fc6fb` 与 definition377615 B / `f568b81618f1f8b041327be55397293235ad5b3492310e03cb5b4ae75ab7b164`。两原件逐完整原bytes核回；不改当前环境冒原run，不伪造原 factory.result，不重做180候选选择。

原完整三尾输入以及完整 prefix seed / accepted 来源共五件仍从原历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复并逐原字节验证。它们的完整 descriptors 保在请求中，和187逐对象相同。新 C 和原 `0d89370d…` factory必须实际运行；原 `e5ab2a8c…` semantic adapter严格核同一准确 C/root族、core/cut/windows/DAG/支撑及九有理点，而不要求不同run或区间盒字节相等。

旧全419片域证明只传到这个相同准确初始点。新的浮点 shadow、J、FD、metric以及后续 active参数都不能借用旧全域结论。原 factory本次两次300秒域遍历和所有未决地址仍如实读回；未另把同一域证明重做完整加成 BVP 前门。

## 4. 一个真实提交候选的名义种子

原 physical-far 所有 possible inverse leaves、源面板、全空间 tube、完整 angle lift、正幅度和取向单位行传播全部保留。每个 mode 的 `point_column` 只多保留**首个实际已提交**的完整候选 seed：

- physical frequency、原 source-panel/piece、possible-inverse-leaf、transaction/coefficient行；
- 原闭 step区间和原闭 leaf交集；
- 完整不折返的角包围、完整正 $w$ 包围、实际二幂 frame指数 $b$；
- 原 $Q_F=1$ 正幅度/取向声明和原 normalization记录的canonical SHA。

该 seed不会替换当前传播状态，不减少后续 candidate，也不把某个 coarse片点当作真 C成员。直到所有112模式的完整单位行族都形成以后，才运行新的 `momentum_rows`。其输入仍包括当前实际 far半径word与本job真实采样得到的 $\mu$ word，并逐词核对；$\mu$ 不来自静态配置猜值。

原 standalone complete-cut main不在此请求调用。当前责任是完整 physical-far接口；不把 far完成冒称所有 cut-DN图已经通过非零高度除法。

## 5. 联合形成与同角坐标关系

对保存的完整角/w参数盒，helper直接从原记录提取准确端点，不先重装成另一个可能扩宽的 Arb球再取中点。定义准确有理名义值

$$
\phi_0=(\phi_-+\phi_+)/2,\qquad
w_0=(w_-+w_+)/2>0.
$$

$r>0$、$\mu>0$用本job实际 binary64 word所代表的准确有理数；$b$ 为该真实候选的原 frame指数，$m$为完整偶频率。共同名义表达是

$$
A=m^2r^3,\qquad B_c=2^b r^4/w_0,\qquad
C=\sqrt{12}\,\mu/(r^4w_0),
$$

$$
\widehat R(\phi_0,w_0)=
\begin{pmatrix}
A\cos\phi_0-B_c\sin\phi_0\\
C\cos\phi_0
\end{pmatrix}.
$$

这里 $\widehat R$ 只是盒松弛的准确名义表达；Arb给它的数值包围，不能反过来称它等于某一真实参数族成员。对应 row变换为

$$
\begin{pmatrix}A&-B_c\\C&0\end{pmatrix},
\qquad \det=B_cC>0.
$$

它与 R380 的物理 column/frame变换是不同的映射。197保留原187对真实行族的正范数/全候选取向论证；没有用名义点重新证明或缩小原行族。

每次局部精度下，helper对两个名义系数包围取准确有理中心 $(z_Q,z_\Pi)$，先作**同一个准确正比例** $s=\max(|z_Q|,|z_\Pi|)$。只有 $s>0$ 才形成

$$
(y_Q,y_\Pi)=(z_Q/s,z_\Pi/s),
$$

再分别转binary64，作实际 `math.hypot` 和实际除法。至少一个准确 $y_j=\pm1$，所以共同 max缩放后的两词不会一起下溢成零。整个方向不经过两个独立完整 family系数盒中心的相互不相关选择，也没有把幅度 $\rho$ 物化后引入巨大/微小比例。

实际两词的范数并不声明准确等于1，也不声明数字向量落在真相关 family中。实际 finite/nonzero word检查属于数字表示是否已形成的定义范围，不替换原 native残差门。

## 6. 精度预算、错误包与原科学门

原传播精度仍256 bits。名义点局部初始精度不低于原传播精度，也不低于所用准确dyadic输入的实际有效位数。必要时局部倍增，明确上限4096 bits；source parser可描述到8192，但本次请求固定4096。没有改旧 propagation精度或其他积分、Taylor、closed-domain参数。

局部精度只在 helper的 `try/finally` 中改变；成功或错误都恢复原 `B.ctx.prec`。它调用原 sampling预算检查，仍在原 point phase时间内，不开额外科学墙钟。若准确输入所需有效位超限，或上限处两个名义中心尚无法形成非零向量，记录 `nominal-representation-precision-resource-partial` 并以原 `WorkStop` 退出该表示；这不是 native拒绝、准确向量零或无根反证。没有保证这个有限精度预算必定成功。

最关键的不变量是对每个实际输出word $\bar r_j$ 保留

$$
E_j=H_j-\operatorname{exact}(\bar r_j),
$$

其中 $H_j$ 是**全部真实候选取向单位行族的原包围**。只要 $R_j\in H_j$，便有 $R_j-\operatorname{exact}(\bar r_j)\in E_j$；该包含不要求名义点属于真实 family，不要求名义点误差小，不要求所有mode共享一个实际准确 C。197原样保留全部 $H_j$、所有 candidate和这个差额。算法没有对 $E_j$ 增设小阈值，也不把存在一个有限数字行当作原物理模型的严格完成证书。

原 $\sigma$、非除式112×224 far行布局、原零初态/当前 H调用、完整224 state与226含mean RK、32×10 native、严格残差下降及 $2\times10^{-9}$ 保留。原 BVP $\lambda=.001$、338物理+112core+3active=453、两个原控制族、8×17外层、RMS $10^{-6}$、BC $10^{-11}$、三方向多层 FD $5\times10^{-5}$、独立 final J/audit全部不变。

## 7. 可执行同job完整顺序

实际工作流按下列依赖运行，原科学失败/未开始范围分别保留：

1. 创建独立 `visible-selected-coast-joint-current-C-full453197` namespace和真实起始deadline；固定checkout、93源、完整原请求/输入与协议身份。
2. 用原规则runner包裹 actual180小摘要与原165必要字段恢复，确定性恢复 selected两原件。token只在process环境中；HTTP重定向不转发认证。
3. 用原 `f12f7470…` 重算连续 C，全160×9、六primitive、原全部深根族与两query，3600秒。
4. 原cut twojet必要读回；真正运行原factory得到当前definition/numeric，以 `e5ab…` 同语义绑定 actual180初始点；当前 selected recipe和original179模板分别保留，不重标旧文件。
5. 原deep-port159、完整112行族生产器。
6. 新far sampler调用原正端点R380 kernel，完整112 far传播，随后全部名义行形成；只有真实成功后继续577节点和全部原field点采样、原误差与arrays输出。
7. 当前197独立 provider recipe显式换三native source并加入四个明确依赖；原179模板仍是immutable来源。保护九准确点/parameter origin/所有原控制和执行资源值不变。
8. 原同owner current H→full J→原FD→完整453 full-DN→final J/audit，在真实同job geometry上运行，前置缺失则明确未起，不捏造失败或接受锚。
9. 六个必要范围 C、cut、deep、construction、BVP/sampler、rules各自按原值读回；实际 quiet后、完整readback marker齐全才删owned临时raw。失败读回或未知存活进程保留至runner销毁，不并发读删。

sampler CLI沿原全部参数，仅新增：

```text
--representative-max-precision-bits 4096
```

其余原完整参数明确为 `precision256 / linear14400s / point1800s / maxpanels25000000 / depth32 / defect12 / norm1/4 / Taylor24 / cache65536 / inverse-depth24 / point-max-nodes1000000 / sample-value-bits32 / steps12`。R380 proof由原 `--proof`，R357由原 `--unit-row-proof` 实际传入。原 parser全部参数逐个按请求生成，无借旧sampler schema省略字段。

## 8. 总预算与同owner控制

job仍360分钟，namespace从实际开始计18900秒科学计划、2700秒读回/结束保留。该计划并不冒称给所有上游一个外部硬kill：原C、恢复、factory、sampling各有自己的受控阶段。原完整BVP launcher从开始时执行真实绝对deadline裁切，仍保持7200秒原进程预算的上限。

采样启动前，在实际规则同步耗时之后，以当时剩余量预留原 BVP7200秒，对 linear14400和point1800按同一比例裁切。线性和点采样仍各自原phase时钟；bind/setup不冒计入其中，但已进入namespace实际耗时。新增名义形成从point预算扣除，不凭未测速度承诺整job完成。原2GiB运行空闲保留、初始32GiB检查、原QR1800秒子预算及2 jac workers不变。

原owned过程协议逐pid/start-time/session/pgid核来源，处理TERM/INT及child close；规则runner每2700秒真实读取/同步规则，原基线 root `21bd547f…` / topic `bff8aea2…`。规则变化、资源partial、异常读回和数学未过门各自保留。compute明确保 `contents:write` 和 `actions:read`，以便官方实际180/165恢复；token不写文件、不进入科学child、不打印。

## 9. 完整必要读回与失败定位

新增 `numeric-far-row-selection.jsonl` 在每个真实mode形成之后写原记录；若形成失败，先保存该mode、来源候选地址、精度尝试、实际错误及剩余数字mode后缀，再退出。这个后缀与已经完成的112传播后缀是不同责任，reader不混淆。

helper同时记录旧独立final-box中点的准确零/非零舍零分类，只为本次读回，**不作为另一个数值对拍门**。它不反推187未知中点或未知mode。全大名义区间、正映射包、每次Arb精度的详细系数和每行完整误差见证只留Actions临时原件。

必要BVP摘要每mode仅保下列透明小表字段：

```text
m, complete_numeric_row, source_panel, source_piece, inverse_leaf,
precision_bits, precision_attempts,
old_Q_center_exact_zero, old_Pi_center_exact_zero,
old_Q_nonzero_center_rounded_zero, old_Pi_nonzero_center_rounded_zero,
old_pair_both_zero, Q_numeric_value, Q_f64le,
Pi_numeric_value, Pi_f64le, actual_error
```

精度字段是最后实际精度及真实尝试次数；完整尝试原件只保身份。失败另保准确候选地址、输入所需有效位/资源cap及所有未开始mode。全112传播模式表、candidate/leaf计数、未付地址、当前point/field完成数与完整源输入身份保留。

reader在Actions内完整读取全112 general-row原JSON，核实际输出word与原selection journal相同、误差字段仍存在；不重算interval、norm或科学值。摘要只返回完整文件bytes/SHA、行覆盖/计数和必要实际数字词，不把全部 dyadic误差树换编码搬出。完整stream byte身份不冒独立科学审计。原 BVP/FD/native trial必要读回逻辑不变。

每个原来独立的C/cut/deep/construction/BVP/rules范围仍只有自己的必要摘要；BVP单份上限90000 bytes，不把完整科学树拆包。若真实必要范围超过该上限，明确 exit70/读回未完，不输出清理marker，也不以截断摘要假称完整。原运行中大日志不为人工反复搬运或增加前门。

## 10. 静态交付与实际未运行状态

此包只做源码文本、准确替换次数、JSON字段与bytes/SHA核对。192项纯metadata核对确认原84pins逐项保、九新增source身份、原输入/参数/whole-object不变、driver56/native30及workflow必要权限；它们不是新科学gate。不曾在本地import科学模块、AST解析、编译、执行Arb/矩阵/方向或造fixture。实际source语法/运行由原公开Actions步骤承担。

七薄源相对实际187完整差异46398 B / `8972e09db14807c43fdb0027cc516bd98f3cb69d4e98dedad9f1cfbb05234d87`，blob `e6236baf5eeadf66684844d6fc17a0b61de1dc78`；far完整差异18978 B / `7cce0bc113516715e8cbbe3343b8794d88ceecc8f6f9e7b37bd63883a0fcc0ce`，blob `27f875848b68ca2f577bd3adbbba54f30fb44570`。新增helper全文就是其完整diff。request/workflow相对真正187完整差异与publication清单另付；原187和正在运行的191/195没有修改。

当前没有197 run、接受场或结果数字。R420预留给实际197必要终态。若新表示成功而后续点采样、native、FD或full453失败，应逐层原样记录；若全finite责任成功，也不能据此自动宣布真实全局C、same-g450闭场、continuous metric、embeddedness或reach完成。
