# R384：actual180 在同一准确 C 根族下完成 coast 修域

作者：ChatGPT（/root/amplitude），2026-11-15。

**实际结论：原准确九控制族的全部 419 个闭分片已在一个明确新参数点付清 $a>0$、$-1<a_s<1$ 的统一包围。**
按预先固定的共同 dyadic 缩放次序，β=1、1/2、1/4、1/8 各有严格速度反证；β=1/16 是首个完整域通过者。
只改变 coast 的三个系数 $p_3,\theta_3,\eta_3$，其余六系数、core、拼接窗口、cut、自然长度表达式和准确 C 根族不变。
九个选中有理系数均由原输出确认可被 binary64 逐字精确表示。

这是已经实际执行的准确域修正，不是以中心必要条件、数值采样或进程 success 代替完整域证明。
仍未运行新点的数值 BVP、native、full-DN，也没有非零场或闭曲面完成声明。
原 R323 准确族与旧有限 Gauss 十坐标实验的定义不同；本次不借后者的 FD 或接受记录支付新目标。

## 1. 独立运行与原件身份

- [actual180 run43753422569](https://github.com/Rogerhu12/math-research-public/actions/runs/43753422569)：
  source `636bbc30601cb577266219ed66bb2759d285badc`，
  2026-11-15 19:37:02 UTC 创建，19:38:02 UTC 已 complete/success。
- compute `132932188151`、report `132932432397` 均 success；
  原历史输入恢复、原 log 流读取、科学修域、必要原读回和 owned cleanup 均完成。
- science phase=`bounded-repair-finished`，process_exit_code=0，
  resource_partial=false，error=null，elapsed_seconds=`4.607932013999999`。
  恢复原日志的元数据阶段原耗时为 `23.970222845000002` s，不并入科学耗时。

| 实际对象 | bytes | SHA256 |
|---|---:|---|
| compute 原日志 | 186596 | `2411ea157637904bbb71ed5cd8be066cb8444f55e3ba55516f127a666c138e34` |
| report 原日志 | 132994 | `cc6ed5447996a677aade026d603657d86236c6b70f76b1f2dd726891e710e585` |
| 两 job 逐字相同的必要摘要，不含分隔 LF | 64284 | `503d2e7d86359c687842e5ce2d5161cac951c7a0b80c5d2b08f5bec3231dcafd` |
| 原 science summary，含 LF | 63192 | `1a0304969f9edd85b4e152cb7a3552295b387f24fa3a9873bd0a97df09a97108` |
| 原 science result.json | 63030 | `3b9bc1ba89e8961149d50edd4feca182d49fb6bf2ba47a5d20147395273cab78` |
| 原恢复回执 | 3048 | `f2f8662553a5bc7e5164243d4bf6acaaf216c37cfc04b4a03f32f9b882b4d412` |

两份已结束 job 日志各读取一次。只做运输前缀处理、原 JSON 字段读取、完整文字 SHA 与整数覆盖核对；
没有在本地计算任何 Bernstein 系数、区间、曲率、残差或新科学值。
本报告保研究结论所需的原界、完整候选状态与选中参数；不将 420 行成功叶或完整可重算定义搬入 Git。

## 2. 同一准确对象的恢复范围

原165实际 tuple 为 run `43736208020`、
source `1f2ec637430e5c6b27b1a93720e106539281a156`、
compute `132879253906`。
其官方原日志只在本次 Actions 内顺序扫描一次：
1,486,048,285 B，SHA256
`4ab8c6d688a27869353bb428288d467502c7aed6ad8cd96140a6cfaea508aea2`，
165009 物理行。708 个物理行首 BOM 只在解析视图中去除，原流字节 SHA 保留。
原165 run/job 的 failure 被如实保存；本次没有将它改成成功。

仅恢复三个实际成员：

| 原成员 | bytes | SHA256 |
|---|---:|---|
| complete-construction-summary | 27207 | `6ff7fb33455be8dbc4eef1eb819a8f7b90329c8575c442dc810c83db13117fb8` |
| complete-input-and-rebuilt-definition-binding | 62398 | `996593f3a615c3694596463c949990a4967cc5c5a1bf48b100fbc4e149e73e48` |
| complete-target-result | 105512 | `e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619` |

construction 的一个重复成员逐字相同；未完成组为空，construction frame incomplete=false。
没有重新计算原 C、原165大差额网格或旧严格反证。
原 core 是 2614352 B、SHA `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`；
config 是 2161 B、SHA `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。

恢复后用原 factory `0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e`
真实重建原表达式；30 个原 definition 字段逐项 exactly_same=true。
其原定义为 377789 B、
`9f4a9b0725d1db462d282c84de6be44832b3d8c7a46d638030b8f5ac0cbecb49`。
这项重建及字节比较约束实际输入来源，没有改变科学接受门。

原准确 C 身份仍为：

- model schema：`R286-original-stored-continuous-model-convention-C-v1`；
- deep definition：`original-exact-root-family`；
- source：`f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df`；
- `all_admissible_original_root_sequences_retained=true`。

原 E、E_r、E_rr 的完整 cut 包围随恢复输入消费；系数使用语义叶表达式，没有以包围中点定义准确 profile。
本次声明统一覆盖原继承 cut 盒，因此保留全部许可 C 根选择。
新运行的 provenance 或更窄盒不是准确函数的另一个定义；后续交接仍应按
[R383](R383-accurate-R323-target-identity-and-coast-control-necessary-band.md)
保准确函数身份与具体包围证据的区别。

## 3. 实际变化与完整域算法

准确九参数顺序是
$[p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3]$。
原 fixed recipe 的 $\kappa=1/2$，$d=1/524288$，
$\delta_A=\delta_B=1/1024$。
coast 是片416，support2；其自然坐标 $t=(s-S_1)/L_C$，闭区间为 $[0,1]$。

只对下列三个原准确有理词共同乘 β：

$$
(p_3,\theta_3,\eta_3)=
\left(
\frac{6173543729074581}{18014398509481984},
\frac{8445254225196179}{9007199254740992},
\frac{8453645258162737}{9007199254740992}
\right).
$$

原准确公式保留：

$$
a_\beta(t)=R_A+I_A-\kappa L_Ct+
 \beta L_C^2\bigl(p_3B_0(t)+\theta_3B_1(t)+\eta_3B_2(t)\bigr),
$$

$$
(a_\beta)_s=-\kappa+
 \beta L_C\bigl(p_3B'_0(t)+\theta_3B'_1(t)+\eta_3B'_2(t)\bigr),
\qquad
B_j(t)=64t^3(1-t)^3(2t-1)^j.
$$

其中公式内三系数指缩放前的原值。自然长度与支持位置不随这三系数变化。
未引入 support1 的 ξ，也没有把它误作能修复 coast 的自由度。
结构及充分小 β 的条件理由见
[R386](R386-accurate-coast-uniform-feasible-scaling-and-C2-bounds.md)；
本次选择实际仍由完整域 Bernstein 包围作出，不由一个充分界或中心点代替。

计划共有18档：
$1,1/2,\ldots,1/65536,0$，从大到小，选首个真正全域通过者。
β=0 是明列的基底候选，本次未访问。
其余418片完整重付一次；每个被试 β 只重付改变的完整 coast，
失败/未决/未访均保在原输出。
科学预算900 s、sqrt_bits256、最大深度28；
固定片最多65536 nodes/300 s，coast每档最多8192 nodes。
本次没有达到壁钟或节点预算。

## 4. 418 个不变闭片的实际证明

原表完整覆盖 indices 0…415、417、418，一共418行，不漏片也不重复。
原整数读回核：420 visited nodes、420 proved leaves、0 unresolved、
0 rigorously refuted、0 unvisited。
除 core-19 与 core-118 各有2个原初始闭子段，其余每片1个；没有据此新计算任何几何。
所有 closed_segments_visited=true，stop原文：

`all-planned-closed-pieces-visited`

全成功叶账仅临时文件身份：
340160 B、420行、
`c9cc25ca42dd47c3f41dfb0043b7473ba01b7c5f7ac0fed81db7519a10fdfd9a`。
本报告未取该完整叶账逐项重算，已读原418行覆盖表及下列原统一界。

以下区间均直接抄原必要摘要的**向外128位 dyadic展示界**；
科学原判断用准确 Q 包围，不是把展示界当作重算原件：

| 不变418片原量 | 展示包围 |
|---|---|
| minimum enclosed radius lower 本身的向外包围 | $2^{-128}[102084710076271635890282406154638436807,102084710076271635890282406154638436808]$ |
| 全不变片 enclosed speed hull | $2^{-128}[-339215103356001053969334373241858271062,140806544237904951098542503351755472896]$ |

## 5. 五个实际候选与全部未访范围

| index | β | 原status | nodes | proved leaves | unresolved leaves | refuted leaves | 未访闭区间 |
|---:|---|---|---:|---:|---:|---:|---:|
| 0 | 1 | rigorously-refuted | 48 | 16 | 2 | 1 | 11 |
| 1 | 1/2 | rigorously-refuted | 44 | 14 | 1 | 1 | 13 |
| 2 | 1/4 | rigorously-refuted | 45 | 15 | 1 | 1 | 12 |
| 3 | 1/8 | rigorously-refuted | 54 | 18 | 4 | 1 | 9 |
| 4 | 1/16 | whole-domain-proved | 5 | 3 | 0 | 0 | 0 |
| 5 | 1/32 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 6 | 1/64 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 7 | 1/128 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 8 | 1/256 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 9 | 1/512 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 10 | 1/1024 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 11 | 1/2048 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 12 | 1/4096 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 13 | 1/8192 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 14 | 1/16384 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 15 | 1/32768 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 16 | 1/65536 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |
| 17 | 0 | not-visited-after-first-proved-full-domain-candidate | — | — | — | — | — |

前四档 stop 原文均为
`stopped-after-one-sufficient-rigorous-coast-refutation`：
有一个严格反例已足够拒绝该 β，随后停止该档。
不能把该档其余未访区间叫已反证，也不能把深度28的未决叶误作通过或反证。
四个实际反证都是 speed，radius_refutation=false；实际原区间如下：

| β | coast闭坐标t | depth | 原 $a_s$ 展示包围 | 已证方向 |
|---|---|---:|---|---|
| 1 | $[89586355/268435456,22396589/67108864]$ | 28 | $2^{-128}[340282384072519165005071489401671256463,340282403002345407387557574578653527469]$ | 严格高于 +1 |
| 1/2 | $[29856301/67108864,14928151/33554432]$ | 26 | $2^{-128}[340282369764898630195947846989784559605,340282396040033582901831501688084320937]$ | 严格高于 +1 |
| 1/4 | $[47646067/67108864,11911517/16777216]$ | 26 | $2^{-128}[-340282424913980306210976424644867607217,-340282367051336633753292733500085691760]$ | 严格低于 −1 |
| 1/8 | $[207610735/268435456,12975671/16777216]$ | 28 | $2^{-128}[-340282381987660578122064458820436065995,-340282370229615572588504058231344231882]$ | 严格低于 −1 |

前四档还有如下原未决叶，均没有被当作反证：

- β=1：$[89586353/268435456,44793177/134217728]$（depth 28）、$[44793177/134217728,89586355/268435456]$（depth 28）。
- β=1/2：$[119425203/268435456,29856301/67108864]$（depth 28）。
- β=1/4：$[190584267/268435456,47646067/67108864]$（depth 28）。
- β=1/8：$[207610731/268435456,51902683/67108864]$（depth 28）、$[51902683/67108864,207610733/268435456]$（depth 28）、$[207610733/268435456,103805367/134217728]$（depth 28）、$[103805367/134217728,207610735/268435456]$（depth 28）。

这些档原未访闭区间分别为11、13、12、9段；
完整端点和每叶 $a,a_s,a_{ss}$ 在64284 B原必要摘要中已读取，
本刊稿保必要反证、未决范围和准确身份，不重新存整张可重算叶表。

中心公式 $(a_\beta)_s(1/2)=-\kappa+2L_C\beta\theta_3$ 只给必要信息。
原 β=1/4 和1/8 的中心速度包围处于开放带内，仍在完整 coast 的其他位置出现严格负速度反证。
因此仅修中心或读一个采样值不能代替本次完整域计算。
本次既不声称 β=1/16 为连续最大可行值，也不声称单独三个系数已优化 BVP 残差。

## 6. 被选 β=1/16 的完整 coast 包围

选中档 nodes5、proved leaves3、0 unresolved、0 refuted、0 unvisited；
all_closed_segments_visited=true、complete=true。
stop为 `all-planned-closed-pieces-visited`。
原完整 coast 成功叶账10816 B、3行、
`c2ca5fdce6ddb1e051fb49dc463f493384901c967dd85a6e9b4001b282c313bb`，
大叶表只身份，不将其伪装为已逐值运输。

| 选中coast原量 | 展示包围 |
|---|---|
| minimum enclosed radius lower 本身的向外包围 | $2^{-128}[102334057864186607078938387597628547281,102334057864186607078938387597628547282]$ |
| 完整coast enclosed speed hull | $2^{-128}[-279539009111056341476089538340155272055,-99197223211737688043168242290945161738]$ |

这与418不变片的实际完整证明一起给
`full_accurate_nine_domain_proved=true`。
本次没有将整个coast单个过宽Bernstein包围误认作实际最终 hull：
完整域证明实际作了5节点/3叶细分，展示的最终 hull 如上。

所有下界/上界均是统一区间陈述，保原cut根族不确定性。
本地没有把这些大整数换算成新的小数、再算裕量或重新判域。

## 7. 唯一选中九参数与下一实际输入

| 参数 | 准确有理词 | 原 binary64 数值 | 原 little-endian word |
|---|---|---|---|
| p1 | `1375945989099287/4503599627370496` | `0.3055213835477326` | `5c3ca48fa98dd33f` |
| p2 | `7798437871654891/36028797018963968` | `0.21645013203050154` | `eb97244fa3b4cb3f` |
| p3 | `6173543729074581/288230376151711744` | `0.021418782473590154` | `9511fa28ceee953f` |
| theta1 | `-569465276708805/9007199254740992` | `-0.06322334619266512` | `28be3dbc672fb0bf` |
| theta2 | `-5036686613378861/288230376151711744` | `-0.01747451701873286` | `2d776ffcd6e491bf` |
| theta3 | `8445254225196179/144115188075855872` | `0.05860072306016053` | `937421fae900ae3f` |
| eta1 | `4841957884391517/4503599627370496` | `1.0751306255033548` | `5d70b72bbc33f13f` |
| eta2 | `3101584203429797/4503599627370496` | `0.6886900390922872` | `4a6f5fb1bf09e63f` |
| eta3 | `8453645258162737/144115188075855872` | `0.058658947547659664` | `3182abaa8b08ae3f` |

原每个 `represented_exactly=true`，
`exact_projection_difference=Q(binary64)-accurate=0`，
`all_nine_exactly_representable=true`。
这些结论来自实际 Actions 生成值；没有为了数值 BVP 隐式换九参数点。
自然长度表达式不变，并不表示新数值 profile/J 或已有场随之自动相同。

| 实际新对象 | bytes | SHA256 |
|---|---:|---|
| selected-accurate-nine-recipe.json | 2136 | `cc87d9327c33a208ac36e7dadaa5608cc3597e8d9f9bc0bd615631a6681fc6fb` |
| selected-accurate-nine-definition.json | 377615 | `f568b81618f1f8b041327be55397293235ad5b3492310e03cb5b4ae75ab7b164` |

准确族schema仍 `R300-new-continuous-nine-target-family-v3-cut-v1`；
选择producer是33533 B /
`595bf01cd89690629ca167d5be9d674951d9959d7fd61717a296ecbd3fcd8c4c`，
factory仍0d89370d。
`source_identity_not_an_accepted_BVP_or_field=true`。

这两份临时输出不是伪造的原factory result：
本次确实形成新recipe/definition；未来原数值入口若要求原factory result，
须由真正factory调用生成并绑定相同准确参数与目标。
后继可按原165恢复输入和已公布源/参数重建这两件并核原SHA，不必再重复418/coast修域作为新增门。
具体新C包围、provenance与数值shadow仍如实记录，不能用旧run/SHA冒新输出。

## 8. 实际作用域与未完成责任

| 原顶层flag | 实际 |
|---|---|
| summary_complete | true |
| full_accurate_nine_domain_proved | true |
| actual_BVP_parameter_restart_available | true |
| all_declarations_are_uniform_over_inherited_semantic_cut_boxes | true |
| same_C_not_recomputed | true |
| actual_field_created | false |
| native_success | false |
| fullDN_success | false |
| new_BVP_acceptance_gate | false |
| resource_partial | false |

原 `continuous_tail_or_caps_closed_geometry_strong_C2_reach_held_not_paid=true`、
`relative_metric_transfer_to_old_field_not_supplied=true` 仍保留。
本次没有完成新参数点的 nonlinear native、完整场、full-DN、最终敏感度/审计；
没有证明新numeric参考与准确目标的误差，也没有把原旧场作新合法父场。
下一有依据的实际动作是按已选准确九词建立真实新profile，
保原全部BVP/native/最终门并实际求解，而不是再机械重复域诊断。

## 9. 来源、规则与清理

新恢复helper12957 B /
`630c288e45efa1f1f6649e9a9588f2dc7d01aea64e7fc9544107c83925f69ee2`；
request16925 B /
`3df438b87ecdd659b7796169d50f84d7daa9e0d02280d3ae5007fa45b212e954`；
workflow20757 B /
`ee7044e4ab7181d46c92b8cdb1a70b0c8c692e6c017ecff0e47667b8a02d4c66`。
原21 identity sources 加2新源，实际23源绑定步骤通过。
纯source/元数据前置不被冒作科学检验。

原3b8规则runner实际19:37:47–19:37:52 UTC，
science_returncode=wrapper_returncode=0，README_change=null，
periodic_sync_failures=[]、sync_rounds_started=1，
scientific_checkout_modified=false；原2700 s机制未变。
必要摘要读取没有新增科学评价，也没有重分类规则/科学错误。

清理原事件确认完整必要摘要先成功，原rules child已有真实wait记录且owner静止，
随后仅删除 `visible-accurate-coast-repair180` owned临时树。
没有新artifact、Release或raw Git上传。
本次结论由公开源码/参数/run和输出SHA可复现，不能声称临时raw在runner结束后仍可取得。
