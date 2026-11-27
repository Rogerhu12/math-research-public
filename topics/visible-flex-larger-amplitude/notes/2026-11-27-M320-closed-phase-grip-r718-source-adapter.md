# M320 同一实际场的完整闭面、全相位、握持与 R718 来源适配

日期：2026-11-27。本文只登记独立完整后处理源与其实际输入责任。新的科学优化变量、方程、取样、根、求积和优化预算均不在本次改动内。所有科学或准确场消费仍只在本公开仓库的 GitHub Actions 执行。

## 1. 本次所完成的入口

本入口完整派生于已刊的 `fixed_fejer_stage_observed_closed_phase_grip_evidence.py`，父源 83,826 B，SHA256 `eddc1fb7d10cc6a24f8245920b93babbf71886e550ceb1b0293b892323548aa9`，Git blob `33261dc5dff1eb2514c3497aca597f52abb09b68`，发表提交 `be3d3935ea1c4ac8f09c5f1da02d47222794b2a3`。本次把该完整闭面/R718消费算法接到已刊的实际 M320 来源族与其完整准确费用流。父 source、所有父参数与父结论保持历史原字。

新的运行源名为 `fixed_fejer_M320_closed_phase_grip_evidence.py`，schema 为 `actual-fixed-fejer-M320-complete-closed-phase-grip-evidence-v1`。输入完整几何报告路径为：

```
{work}/fixed-fejer-M320-continuous-gram-curvature-support-v1/report.json
```

输出完整主报告路径为：

```
{work}/fixed-fejer-M320-complete-closed-phase-grip-v1/report.json
```

本源码不接受 N4096、J1845、原 M160 或 run16 观测族冒充 M320。共用的完整准确数学核原字保留；本层在已经完整重绑的费用输入上再明确选取唯一 M320 分支。实际完整场未返回时，future point、snapshot、科学报告 SHA、准确几何报告 SHA 和闭面数值结果均为 null。输入准备完成或 mutable progress 不是完整场。

运行源完整包含原全部闭面逻辑：全上片准确叶、下片反射、两完整固定 p4 帽、全相位、混合点对共同支撑、全像 Hausdorff 盒距离、原八项 beta 证据、独立无标记外管、原 R718 可选下界，以及最终全输入输出复读和晚失败清空。没有仅供展示的占位函数。

## 2. 固定参考与当前空间的精确区别

| 对象 | 本入口实际定义 |
|---|---|
| 固定参考 Fourier 核心 | M160，原七个 RN-even64 Fejer 系数和其余零词；完整 160 词从实际固定参考绑定读取 |
| 当前完整核心 | M320；前三个固定实际词与参考相等，后 317 个系数是所选完整当前点的自由坐标 |
| 当前旋转通道 | 962；x odd-sine 321 槽、y odd-cosine 321 槽、z even-sine 320 槽 |
| 当前径向布局 | J923、三阶节点 jet，排除完整径向行 0、2766、2767，保留 2766 行 |
| 当前总自由坐标 | 317 + 2766 × 962 + 1 = 2,661,210 |
| 最后一个坐标 | 当前完整 H 原字，不由参考 H 或旧父 H 替代 |
| 当前完整观察 | N2048；固定参考也为 N2048，本适配不合并 N4096 |
| 准确径向域 | 全部 922 原单元及完整尾；准确 s=alpha*S+beta，端点/支撑/原切片全部保留 |
| 准确角域 | phi/pi 属于 [0,2]；全部 1024 个闭角胞及原 literal 关联 |
| normal 链 | 全部 32 段、六控制、完整 angular jet/root/相邻关联与周期 glue |

真实 M base 的 `_core_and_cap` 分别使用 `reference_freq` 读取固定 $\Theta_0,\rho_0,\rho'_0$，使用 `freq` 与全部当前 core 读取当前逆图和 $\Gamma_c$。真实 M normal 的 `_chart` 只读 `reference_freq` 与固定 `parent_core`；其 `_core_and_cap` 使用全部当前 320 系数。所选场的当前核心不能截为 160，也不能把初始零扩张关系当作后来全部点或准确根的等号。

参考图、scalar 函数、固定 seed、18Q/原支持、积分规则、准确目标、normal 32 分段和原隐式分支没有因 M 精化被重定义。本层也没有重新定义它们。当前完整 coordinate norm 与 frequency-refinement 模式由原完整 M reader/source binding 读取，不从 M160 的范数或旧 Phi 迁移。

## 3. 完整且严格的来源族

M 科学/纯读者来源：

| 角色 | 完整文件 | SHA256 |
|---|---|---|
| 科学 driver | fullclosed_fixed_fejer_frequency_so3_qp.py | fff956cc086c8f69c7de87c2d9117792b6b1d5e1de853e59a992fb67e04b4e51 |
| 纯 reader | read_fixed_fejer_frequency_so3_report.py | b79c352d11b41de5384016f103c07db7abc2a41bf438ef92fe20b8a9b43e75bb |
| 当前 normal | fixed_fejer_frequency_normal_lift.py | 60769d4999af17f6dc904400e414e3f34ec1000bd84529ad168dca67f6889b5f |
| 当前 base | fixed_fejer_frequency_meridian_operator.py | f7058f9c9d3f02292b738b360b116062b60bcf07907286acb42346eb431bdf9a |
| 当前 source binding | fixed_fejer_frequency_source_binding.py | caf16fbc87ef618ddae5ba42616d9bbe136beac6d32487224073ac6958c4d3c0 |
| 当前布局 | fixed_fejer_frequency_layout.py | 67c5503e8df036aa1468a3df2f395f5a33c91c4309520fbb8862b39c2495a251 |
| 当前 immutable packet | fixed_fejer_frequency_root_packets.py | 767be252b02b0f92ee1a7229881cfa693a2d4e73f48f6a703fe0c21340c59b78 |
| 固定参考 | fixed_fejer_axisymmetric_reference.py | e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb |

完整 M 运行源/参数表为 `computations/fixed-fejer-frequency-M320-complete-delivery.json`，83,648 B，SHA256 `882ef34f535f0e6a83a262cede79f5857dadafa28c8b039ac84d911cd7e15e17`，blob `33b9fb7d2119f5c3911e62351b7758037a422b1d`。其后五个元数据修订没有改任何运行源或完整 science/pure step 对象。本入口使用该完整表的全部 128 角色；原 Fejer 110 个 path/SHA 对也全部保留。完整科学 SOURCE_PINS 的 canonical identity 为 `a25ffd18c4a8286c904ca186d820e8939f71337dd4fe41c365d6202bf291f608`。

准确费用七体已经独立完整刊于 ae8d223e3ed43c4efb33a07b4619328d1808d734，其 M 分支运行体未随后来 N 修复改变：

| 角色 | 完整文件 | SHA256 |
|---|---|---|
| 两个明确完整族的严格 binder | fixed_fejer_refinement_fee_source_binding.py | 9d2d2fafd9a89569615b8af0e0137f1a5f44b0df9656d877d4e63b9a79f5f03e |
| 实际完整 point/packet input | fixed_fejer_refined_normal_packet_accurate_field_input.py | 6df6761df76fad96a85024627b3b07cab666504368a20f4ab56ddc006bcab35d |
| 准确 reference/control radial | fixed_fejer_refined_accurate_reference_control_radial_boxes.py | 2650bae91fb92d2c45ac829ec45ead2398a11c8c1a289b1ccf0ee05e60a42ed9 |
| 完整 normal root/physical sixjet | fixed_fejer_refined_complete_normal_root_and_sixjet_fees.py | 85dace5827a57d72c4dbff497a5b3bf3e468d817a8c19a77568e67e1e1e97c51 |
| 完整叶读者 | fixed_fejer_refined_complete_physical_leaf_binding.py | 361af2d352075a310950926049f13b9fcf271ab5e9b4e155cabe726b6b8bce5e |
| 连续 Gram/曲率/支撑 | fixed_fejer_refined_continuous_gram_curvature_support.py | db2a08431e8bd4ab484bc8e4e93b46450e0b6341781ea02303fe5e80e7c8d52b |
| 完整 beta bridge | fixed_fejer_refined_complete_geometry_support_beta_bridge.py | e4c4e99b24de17e3ec6a1ec3eb7e9d752557ba2d8060cd273a7541723bfff797 |

所有文件均在 `scripts/resume_20261126/`。完整七体表为 `computations/fixed-fejer-N4096-M320-complete-continuous-fee-delivery.json`，38,028 B，Git blob `8313cd61969d162d3a6b3a2cd8a8f49917a51e31`。该 binder 本身不接受任意 schema；只有两份完整固定的源表。新的闭面层进一步要求 `family=="M320"`，因此不能消费它的 N 分支。

## 4. 读取顺序与实际全点闭合

第一步仍是原 `bridge.load_geometry`。它完整读取 source-bound geometry report、其 complete binding、原准确 normal report、immutable 科学报告、完整 point/snapshot、六个当前真实输入和所有 normal/physical/geometry journal。原 M reader 被实际调用；其 `frequency_refinement_binding` 与纯读结果逐对象相等，包括独立初点、真实完整父13成员迁移或相同来源 restart 的原合同。这个后处理不杜撰父 final，也不把 independent 重新分类成有父场。

`m320_source_layout` 是本次新增的完整纯元数据函数。它重新钉完整叶、输入和 family source 文件，调用该完整 family 的 `family_from_actual`，选择其原 M320 整对象。它要求：

- context 与 actual 的完整 source pins、完整 family binding 精确相等；
- 所有 M320/refM160/J923/N2048、317、962、2,661,210、三不等长 omega blocks 和三固定零行精确匹配；
- 原 family binding 的全部128角色、完整 SOURCE_PINS identity、原110对保留、完整父13成员验证和 typed/未知历史责任均仍在；
- 当前 full model/base/reference canonical identities 和实际 sources/schema 一一对应；
- 当前 base 与固定 reference 的完整 mesh、chart、前三词、scalar identity 和 scalar definition 对象保持原相等关系；
- current normal/base/packet/source-binding/layout 五个真实角色不能用历史 alias 代替。

这不是仅凭 self-reported family label 的准入。上游原完整 binder/reader刚已从真文件重算整个结构，此处再作唯一 M 来源的精确专属选择；所有消费文件保原路径并末次重读。整个 base 或 reference 对象没有被剥除后比较。

随后 `current_core` 再完整读取 `current_point_arrays_file`，要求 NPZ 成员集合恰为 `{"x"}`，全部 x 为有限 float64，shape 恰为2,661,210，并按原完整 array-SHA 算法核 same point。三个固定 hex 词从当前 base 读取，317 个自由词从 x 的完整前缀读取。重建的320词另计算完整 dtype/shape/payload array SHA，必须等于准确 input 的 `original_current_core_sha256`。H取 x 最后一词，须等于准确几何中的同一 singleton H。没有抽取少量系数或把参考核心充作当前核心。

## 5. M320 端口与完整物理六jet

新 `exact_ports` 只改变 source/layout读取位置和明确的当前维数。它从已完整绑定的 `context.actual_input_source_pins` 读取当前 normal/base/reference SHA，原参考仍是 e717 的 M160 准确图。其余端口、支撑、标记、拓扑和相位数学保留原完整函数体。

在同一实际完整根分支、全部32段、全圆关联及周期glue已付时，原 R715 raw lift 为

$$
U=(1-h)P+h\Gamma+\int_0^sT-(1-h)\int_0^ST,
\qquad h=1-10(s/S)^3+15(s/S)^4-6(s/S)^5.
$$

真实 source 的三固定 omega 行仍为0、2766、2767；各控制/seed支持完整位于(0,S)；原 h端点的一二导数为零。故保持原核心端口 $U=\Gamma_c$、$U_s=e_z$、$U_{ss}$水平、$U_{s\phi}=0$，以及完整 cap端口 $U=R e_r(\Theta_0)+He_z$、$U_s=-e_r(\Theta_0)$、$U_{ss}=0$。完整 $\phi$与混合jet均不删减，raw closure defect并未被强制设零。

当前 $\Gamma_c$ 的全部320系数进入当前逆图；固定 $\rho_0,\rho'_0,\Theta_0$ 只来自完整参考160图。因此当前/core与固定/chart正性是两项分别完整的责任，不能从来源相同或离散domain采样推出。既有准确 radial/leaf producer的 `current_rho_proof` 必须使用全部320当前系数，其完整正下界和固定参考正下界都被复读。

下片保持有符号参数 $u\leq0$ 的 $J_zU(-u,\phi)$，六jet依次为
$J_zU,-J_zU_s,J_zU_\phi,J_zU_{ss},-J_zU_{s\phi},J_zU_{\phi\phi}$。
上下片共享完整核心C2端口；帽用Cartesian盘图和原固定p4图，不以极坐标退化冒浸入。只有严格帽collar和真实全部上片法向正下界已付，才输出闭C2参数球与连续全局定向法向。这里不先假设嵌入或外向。

## 6. 完整全相位与混合点对

本入口保留 R248 的准确相位
$$
\alpha=\pi t/2,\quad
\zeta=\Theta_0^{-1}(\Theta_0(\phi)-\alpha),\quad
F_t^+=R_\alpha U(s,\zeta).
$$
下片为 $J_zR_\alpha U(s,\zeta)$，固定Cartesian帽材料点不动。完整 $\zeta_\phi,\zeta_{\phi\phi}$ 原公式保留，强C2时间连续性的前提与cap/core接缝责任保持。当前M320不改变物理相位定义或目标 $g=ds^2+a_{\rm deep}^2d\Theta_0^2$。

所有准确whole support rows经过原预扫和完整第二遍重读。原两个beta区间、全部正负零系数、闭可行/严格正支撑的区别、p4帽分子符号和801/800范数界都不改。一个共同 $A_\beta=\operatorname{diag}(1,1,\beta)$ 必须同时覆盖全部旋转/反射活动片和全部固定帽，因而包含上/下/帽之间的混合点对责任。只有这套完整支撑与曲率假设付齐后才调用已刊R650的全闭面嵌入、外向及reach结论。普通旋转不使整个带固定帽表面的reach自动不变。

原八个 beta evidence roles、单独lower-reflection扩展、完整support chunks、原 e0b44 `read_input/consume` 和完整bridge逐row/source复核均保留。证书中的准确sixjet error scope只指准确场全域外包所需全部误差；`working_field_word_error_bound_produced` 保持false。whole root/normal/积分/精确scalar/舍入界不能被有限工作点或进度代替。

## 7. 真实全像盒距离与全部320模式的R718增强

原完整盒法逐一读取每个上片位置盒、每个对应下反射盒和两完整固定标记帽。四个真实 t=1 核心像见证与整个目标像作 min，再在见证间取 max。它使用全三维距离，包括z分量；不变为同材料点位移。所有目标盒都在；宽盒只能令下界不足，不能删去。

定义全部当前支持系数为 $c_1,\dots,c_{320}$，则本程序准确有理地计算

$$
X=1+\sum_{j=1}^{320}c_j,\qquad
Y=1+\sum_{j=1}^{320}(-1)^j c_j.
$$

当前核心是support-function曲线，X/Y不是对radial graph的采样拟合。真实 source 的 $\Gamma_c$ 位于z=0；R248全相位包含t=1半四分之一转。已经付齐完整marked closed/outward/common support和八项证据后，才调用父源完整R718算法，以实际r=max(X/Y,Y/X)、m=min(1,beta)、共同marked sigma产生

$$
d_H(S_1,S_0)\ \geq\ \frac{\sigma}{m}(r^m-1).
$$

实施保留原32项正log级数、32项正exp级数、2^-96向下有理舍入；m=1使用准确r。常数项1准确保留，最终向下封口。全部参数和有理方向都原字保留。仅MemoryError可以放弃可选增强；来源、same-point或绑定错误不被吞掉。最后输出原完整盒下界和已付R718下界的最大值。

R719适用于任意有限M≥3，包括320；但本程序仍逐个用全部实际系数形成r。只有实际前三RN词满足既定式、完整当前连续rho正性已付时，才记录7/3一致性结论。已刊 [R720](../results/R720-three-moment-current-axis-ratio-and-gap.md)（完整SHA256 `cda0763b31d7f54e3cc93126f09be5b03d114e37ae59283658cee764bcfa1fc8`）的8/3强化可作为数学背景，本次运行没有引入新常数来替换实际r，也没有为了它再求值任何场。未知sigma或未付闭面假设不能产生数值比例。

R717同叶三维norm直径和完整cap norm仍通过当前geometry流进入原D取最小算法；不会用独立坐标极值的较弱界覆盖它。原0.05D与更强0.2D握持目标分别记录。固定H握持按原题不作刚体对齐；四仿射独立固定点是保留的几何事实，不新增δhold前提。

## 8. 独立无标记管与R716晚失败接口

`unmarked_body_interpretation` 全函数逐字保留。它从全部真实活动支撑重新加入平帽支持beta*H和零cap曲率，独立计算无标记全闭面reach；不拿marked嵌入倒推这一步。真实mark height=1/1000必须严格小于该无标记reach，才能由R716§6支付全外管和固定四p4柱体的加法解释。半转或质心消失没有被假设；全十二通道积分、正V和非零中心矩仍独立未付。

副件名仍为 `R716-unmarked-outward-tube.json`，schema为本主schema加 `-R716-unmarked-outward-tube`。下游必须：

1. 先读最终完整主report，核其本source SHA、`complete is True`、`status=="complete-same-field-consumption"`、`all_bound_input_and_generated_evidence_bytes_rechecked is True`；
2. 在主report的 `R716_outward_tube_evidence` 取精确原path/bytes/SHA，并要求它也逐对象列于 `generated_evidence_records`；
3. 复读该真正原路径全部字节，核副件 `required_final_report_path` 等主实际路径、final-complete标签与所有same-point/model/snapshot/target/input/normal/geometry身份；
4. 全部原source/input/output records复读，不能仅凭当前checkout有一份同名文件替代原记录；
5. 只有对应外向、strict tube、体加法解释均true时，才升级相应R716责任。

本主程序所有latefailure清空顶层已付结果，complete/recheck保持false。此前可能已经写出的任何副件单独不具证明资格。M320来源不会改变这个合同。实际当前core记录含完整320词及其point/layout/source身份，供后继严格重算；未知结果不补旧来源值。

## 9. 已真实返回的run14输入与未返回的场

实际run14为46028184571/1，head05c45d48a8013955e70be41401b26181f6bc7326。已真实完整输入小卷为
`notes/2026-11-27-public-actions-46028184571-1-part-001.md`：
16,602 B，SHA256 `98eb4446b33c6a75d35b962381101c09dbdd8b253046c170e6fd733f5640d4ab`，blob `be5daabc639905ebc87078d67f9ea38b882cffe2`。其两个完整实际record都返回0；只据该小卷记录以下输入身份，不读取大raw：

- maker来源89cc、实际sourcecommit80649973c546ec5f7c9930313617ae2e903980d6；
- reference来源e717、实际sourcecommite1f3eae778b24a03a30cbcec395f21fbb3156169；
- 数学recipe957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9；
- complete target identity50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319；
- 真实reference model ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac；
- 实际chart af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103；
- 真完整binding文件92a1bd95d5934efd666f6f01925a40c38fbc37b6546f78e1e764680553f5d422/35,712B；
- 真preparation43a727cfa6ee7f9760cadfb4b0758709cde5823fa794eb2762c44b16acf0e969/84,966B；
- 完整当前scalar table为2218叶，accuracy_reached=false，whole tail保留；2397只属于更早历史carrier责任。

全部六输入的原path/wholeSHA/bytes、全部side inputs和完整target/binding记录在本完整ready中保存。实际当前/准确wholefield、rootpacket、normal费用、geometry或closed结果不从这些准备记录推出。18:09的小索引仍仅返回1–2；M工作点更新也不代表接受或自然完成。运行入口在真正complete-required-angle同一全point immutable snapshot和完整报告可读后消费；不用等待假想父final，也不拿仅部分缓存冒完整packet。

## 10. 完整参数与来源构造

新完整ready保持父所有8个argv词和66个scalar selectors；唯一两参数路径替换为M geometry输入和M新输出命名空间。完整原step的outputs、scope、fresh-output规则和所有selector保留，新增的M布局绑定不删任何科学责任。`--support-chunk-rows 4096` 保持；全1024角胞、全922+tail径向叶、32normal段、全部physical六jet、全t、全帽与所有support rows保持。原源码没有新增或缩短运行预算；上游normal/geometry的完整900s参数不改，当前closed仍按原完整消费，不设置新科学门。

完整再生器 `reproduce_fixed_fejer_M320_closed_phase_grip_r718.py` 读取父whole源码和父whole ready，核固定SHA/bytes，在内存应用六项完整文本替换并核结果whole身份。它同时按明确顶层字段替换生成完整新ready。反向使用全部旧文本和旧参数值可逐字恢复完整父source与完整父ready。这个程序是source/parameter构造器，不生成科学结果或证明所需数据。

完整源文本比较范围为27个原top-level完整函数逐字不变；修改5个完整函数：`current_core`、`exact_ports`、`flow_image_distance`、`complete_sources`、`field_and_cover`；新增1个完整纯元数据函数 `m320_source_layout`。其中physical端口、流距离和field evidence的数学只保留原公式并换精确当前身份/维数；原main、partial/latefailure、全部support/cap/box/phase/grip/tube消费、全部β写入以及原有理幂算法完整原字不变。

本次实际只做V8全源文本/JSON/字节SHA/正逆对应工作，没有Python AST/compile、scientific imports、本机数值、fixture或实际准确消费。所有运行源、完整ready、完整再生器、本文及完整manifest都各小于100,000B，并以真实远端blob保护。root是唯一refs/队列写者；本文不是额外审核或科学准入门。

## 11. 原结论与本新来源之间的责任

本文把已刊端口/R248/R650/R715/R716/R717/R718/R719的条件结论实例化到严格当前M320来源。它不重复证明已登记定理，也不宣称已付实际Gram、reach/D、δhold/D或δE。旧M160、旧run09/run10、N4096、run16或未返peer结果都不能借公式相同迁移为本场证书。完整typed历史和未知并行来源继续由实际原reader/transfer保存。

未来若拓展到另一source、M/N/J组合、另一point、另一chart或另一个物理相位，需要明确对应完整来源与输入，不能通过放宽schema或删除sourceguard使用此包。若whole leaf、连续rho、浸入、共同support、帽collar、同point绑定或最终完整复读尚未付，输出继续保null/未付，科学运行本身照原完整参数进行。
