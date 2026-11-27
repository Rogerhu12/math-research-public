# Run18：完整 R716 十二矩与重心补偿来源适配

日期：2026-11-27。状态：完整源码与全部参数已准备，尚无本包的科学执行结果。

## 1. 本次交付与真实执行边界

本次从已公开的完整 run16 stage-observed 两个运行源派生独立的 run18 meridian-batched 版本。只更新确切来源、文件名和 schema；完整积分、全域覆盖、分支关联、反射和平帽、四个固定标记、重心补偿、三相位比较以及闭面证据消费保留。旧源、旧参数文件和正在执行的 15、16、17 不修改。

当前独立执行来源是 driver `41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2`、pure reader `d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52`、normal `388c756a81d76c92ef146838a081cfee298e43ba44fee8d936f88341ebdf3ed4` 和 packet `910f131c9f7024cdd7866f913f3211247327098bdae2735442619f397d3a9e15`。整个实际科学角色表为 137 项，保留原 120 项完整路径与 SHA 来源责任。完整科学交付表是 `computations/fixed-fejer-meridian-batched-complete-delivery.json`，78671 B / `18c451846439d93e5ba69c9773b3d35253765fbd3bae769076e35cde80669e41`，blob `7c64de07241a312dcdc7244345998f5c9a217a00`。

根已记录 run `46062343475/1` 的两项必要输入均真实返回 0；首个科学入口约 8.147 秒返回 1，缺少科学 report，仅产生 command 文件。后续真实诊断已定位为新 normal 构造器进入 analytic-frame 时，旧完整方法守卫拒绝新的 `_meridian_data` 方法；这是实际来源绑定异常，不是已运行物理场的收敛结论。根给出的固定诊断小卷为 42,893 B / blob `b4c479790c2d90184be6f42d77322affca66af5b`。本说明只登记根实际读回的边界，不编造原异常全文、完整点、末点、typed 历史或费用结果。

因此本包是这个确切来源版本的完整 prepared 交付。本包没有可用的新场报告、packet、矩积分、闭面体积或 delta_E 结果。科学源若随后修复，需要另作明确的新来源适配，不能更换本包已有 SHA 或把旧准备状态当成新版本已经执行。

## 2. 完整文件身份

| 角色 | 完整文件名 | 字节数 | SHA-256 |
|---|---|---:|---|
| 十二矩 producer | `fixed_fejer_meridian_batched_complete_closed_surface_moment_integrals.py` | 61092 | `c1ae47c429a3ffed9646d8c90cc3671519668505c171ce006a8c1d9813960d97` |
| R716 consumer | `fixed_fejer_meridian_batched_r716_centred_volume_moment.py` | 46798 | `daff2a1b8ebaa67fe00fc78ceb9c59bb939c63a235394f97bc52fb483d56343a` |
| 全部两步参数 | `fixed-fejer-meridian-batched-complete-R716-closed-flux-centred-moments-ready.json` | 45251 | `91461ab60ec090a3313f90837dbec041eea5d7a670b28935d558b1335240b7ff` |
| 完整文本再生器 | `reproduce_fixed_fejer_meridian_batched_R716_moment_sources.py` | 61704 | `e052e1f579249a1b06569744c10f297df9611356d10c52c3008c639c49c77846` |

上表均置于本主题；运行源与再生器在 `scripts/resume_20261126/`，完整 ready 在 `computations/`。所有单个完整文件均小于 100,000 B，没有按函数切碎运行体。

数学核原样复用 `r716_closed_surface_moment_arithmetic.py`，17,397 B / `f79c69edc4686148ca0a1418a498ce0154492a842561542c6bbdb8d810563e9a` / blob `e265b5b25932ac97dc173071e00c60a568e80cc5`。本次没有重新证明 R625/R716，也没有改变其系数、矩通道、相位或标记配方。

直接完整父源为：

- `fixed_fejer_stage_observed_complete_closed_surface_moment_integrals.py`，61,079 B / `a5d17ca2ad21aea7d3dc714875c40098f2aa4a281352a3192d4645057c7608a7` / blob `bcf872d81c53f930200397327a85d5e2fcd95e23`。
- `fixed_fejer_stage_observed_r716_centred_volume_moment.py`，46,786 B / `a6979c102e8620e31422f14c6368044b796767dbd69f2819ed8bae7a8d1fd992` / blob `33de6985fe7dee75f0e97fbc68d166e08aa2b26d`。
- 父完整 ready 31,162 B / `bca7946c9b37096ac65c2236f0792830ef85edf1a313f7f4d998773213f9e027` / blob `67881a6498db2504dad50935044cee310d17c673`；父总表 46,921 B / `a1ceeffb21e6c800e57406eced56553db2664f077652649cee0981681f2e17af` / blob `2744530cdfa75c7a9cc8a82e81e41cb859fe1719`。

## 3. 新准确场来源闭包

准确费用六源与全部参数的完整交付表为 `computations/fixed-fejer-meridian-batched-complete-accurate-fees-delivery.json`，60,812 B / `25d8288c8a812a8b87dec89df9e59ef120982ccc7e6a166c04712311c6630fdd` / blob `8129866071548651514aa5a09461ec8314a89725`。本包实际绑定以下完整新体：

| 作用 | 完整来源 | SHA-256 |
|---|---|---|
| input | `fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py` | `d9cbf733957e3577cfc6175a1d69024a2874468e1cde7141f5d81b984676430b` |
| radial | `fixed_fejer_meridian_batched_accurate_reference_control_radial_boxes.py` | `a978609f6ec973c5c495e7cdb2a2da36eb2e786f48bd948e5ed1ce488934a1fb` |
| normal | `fixed_fejer_meridian_batched_complete_normal_root_and_sixjet_fees.py` | `242fc2f403db2495ea70e27437823031a84b26da717190b5f7e7ea252f9c0e2e` |
| leaf | `fixed_fejer_meridian_batched_complete_physical_leaf_binding.py` | `897fceaa340fd042db03b3ea0f9b72b3e2c1a5c235d7104ead2c4b0104c07fc6` |
| geometry | `fixed_fejer_meridian_batched_continuous_gram_curvature_support.py` | `d0d0f45332ece0a63192b4e80c7c318635ba1068208bad45bec2a136781934a5` |
| bridge | `fixed_fejer_meridian_batched_complete_geometry_support_beta_bridge.py` | `d0b72820b7a7f8f872d2cb460e6f2fba3a685804e200ac4f35f7f12bf33cb0e7` |

完整输入仍由新准确 input 的 `ActualNormalPacketPoint` 读取实际科学 report、完整 pure 验证、真实 immutable snapshot、全部当前变量和原已记录 packet。没有构造 working normal，没有调用新 F/J/root，也没有把 detached cache、batching、时间计数或 mutable progress 当作准确盒。

新完整 field binder 是 `fixed_fejer_meridian_source_binding.py`，41,894 B / `15cd8e201db8aeef7139baf0e82d9d18fcf190194cd33dc8b112bebe05a7dffc`。原 `fixed_fejer_reference_input_binding.py` 的完整 `3da43e82722dfb4548ff4e8b454d47ec2626ece76084c7801c0be5b8c989670f` 身份保留。producer 重新调用实际新 binder，完整比较报告里的输入 binding、真实 binding 文件、完整参考模型、固定目标对象、纯数学配方和全部六个当前文件；并重读四个 side-input records。它不以两个未经校验的摘要相等代替实际输入。

本包保留原固定布局 M160、J923、N2048、全 1,333,370 个自由词。完整点必须来自同一准确输入里的单成员 `x` immutable NPZ，dtype、shape、finite、完整数组 SHA、末字 H 和整个模型身份均核。自由 core、三条旋转槽、core 的一二阶和 cap 的二阶自由量仍保留；没有只读部分变量或借参考 H。

纯数学 target 配方仍为源定义的 `957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`，固定 chart 定义为 `af8ab672f847163fe02999df70a031cd5e4a495ed89c788ad0dffc8786651103`。这些预先确定的定义与本次 actual target 文件、完整参考模型和实际点的身份分开。新 ready 没有把原16的 ea64 模型、50df 目标文件对象或其六文件 records 冒作当前18；这些原证据完整保存在固定父 ready 中。当前18的 report、snapshot、point、实际参考模型和费用结果留 null。配置的完整参考构造为2218叶；历史2397只属于旧05/10地址来源，不提供本场的准确参考值。

原 P0/全 G/typed 和未返回平行历史责任未被删去。本包只消费一份实际完整 required-angle snapshot 上的同一个场，不声称覆盖所有历史优化点，更不从未知历史补出空列表。

## 4. 整个参数域和十二通道

原积分域保持 `phi/pi in [0,2]`，上游完整参数计划为1024个闭角胞。全部922个原径向单元、完整标量尾和实际支持/剖面/Q/gamma 分割仍在同一准确计划中。径向仿射约定严格是 `s = alpha*S + beta`，不是把 alpha/beta 颠倒。每个有效叶要有准确正宽度，原单元集合必须完整等于0至921，邻接叶不能有空隙或重叠；后来真实细分的全部叶也完整消费。

这不是对有限节点做积分拟合。每个完整角胞内，程序读取整径向叶乘整角区间的六 jet 盒，以准确区间测度包围整个叶的通量。所有32段 normal 根和完整33节点分区、周期与相邻/literal 分支关联、每个完成的 physical stream header/footer 和最终字节复核责任保留。缺一个域块就保留其原 id，不把缺块当零。

十二通道原样为：

`V, mx, my, mz, Qxx, Qxy, Qxz, Qyy, Qyz, Qzz, A2_real, A2_imag`。

候选上片法向面积向量使用原 `N = F_phi cross F_s`。对多项式 p，原核使用 div(X p)=(3+deg p)p，因此 V、一次矩和二次矩的通量系数分别为1/3、1/4、1/5；复矩 A2 是二次矩的组合。当前完整 F、Fs、Fphi 以及原 raw closure lift 的 h、h'、h'' 项都来自同一上游准确场。原完整下反射贡献、两张平帽和固定 p4 标记的体积、全部一次矩、全部混合二次矩原样加入。

每个角胞是原子完成单位。程序可以读回已有且整个绑定相同的完整块；预算耗尽只在整块之间停止。任何未完成角胞、未付完整同支关联或缺最终全字节复核，都使全域矩保持 null；已有部分贡献有明确 partial 标签。完整形式通量本身仍不等于已经证明存在嵌入、外向的有界实体。

## 5. 三物理相位与重心补偿

一般分支始终保留 t=0、1/2、1，物理角 alpha=pi*t/2。旋转对未标记实体的一次矩和二次矩分别作用为 U m 和 U Q U^T；固定 Cartesian 帽标记保原位置，再对总量计算完整重心补偿 C=Q−m m^T/V。xz、yz、z 方向和全部混合项不因期待半转而被删除。正总体积须由实际完整区间严格离开0，Frobenius 不变量及其分离量也由实际全矩盒产生。

完整相位几何仍须消费准确 R248 的固定材料图逆映射：`F_alpha(s,phi)=R_alpha U(s,Theta0^{-1}(Theta0(phi)-alpha))`。本包没有把简单移动旧 phi 网格当作闭面接缝证明。数学核的旋转矩只在后续真实同场闭面/相位条件付清时，才解释为这些完整实体的矩。

较简的 B_eff 公式仍需要额外的实际 all32-stage signed half-turn 根盒包含。一般十二矩/三相位公式不需要先假设这个半转性质；验证失败或未付时保留一般公式。R718 的 held-distance 结论不是体积、重心矩或 E(3) 商距离证据，R722 新均值存在路线也没有被加入本版本。

## 6. 闭面主件与 sidecar 的真实消费

唯一接受的新完整闭面运行源是 `fixed_fejer_meridian_batched_closed_phase_grip_evidence.py`，84067 B / `cbd01222938bd0f82ca54188eab5b5b187469985727bf94406de84de4070d549` / blob `570f0d318f1c84d68c2ccbf314fef2986006f91b`。其主 schema 为 `actual-fixed-fejer-meridian-batched-complete-closed-phase-grip-evidence-v1`。源适配证明是 `notes/2026-11-27-meridian-batched-closed-phase-grip-r718-source-adapter.md`，21,998 B / `4eb8967fbb7e5ad5a6220825320b943fca306db124c4c5225f2e4de6c3561f21`；完整闭面包表为36,036 B / `8a4b1a1d7dab735f204f45622bfd3ddfd945aecbbdb8cff4cb91b994040fbf9c` / blob `3ffd7eac134052c8a574f507a1dc1934e430c6ec`。

consumer 先读最终主报告。只有它真实 complete=True、status=`complete-same-field-consumption`、且 `all_bound_input_and_generated_evidence_bytes_rechecked=True`，才读取主报告唯一准确记录的 `R716_outward_tube_evidence`。sidecar 为同目录的 `R716-unmarked-outward-tube.json`；它必须声明这个实际主报告绝对路径及最终完整主报告责任。晚失败残留的 provisional sidecar 不能独立付费。

之后仍执行原完整消费：

1. 所有原输入和所有生成证据整文件复核，同一完整 point/model/snapshot/target、normal binding 和 geometry binding 逐对象相等。
2. 原科学 report 的 immutable copy 必须与原报告整字相等；原路径仍读。只有完整 source/proof 副本允许通过整 SHA 和字节数相同建立新 checkout 关系，不能替换原记录。
3. 完整 geometry、current core、精确端口、整个相位接缝与每一支持域叶重新消费；共同正 A-support 的外向证明没有循环假设。
4. 原全部八个 beta 证据角色、下反射/活动接缝扩展、e0b44 原消费者和完整生成文件逐项重读；不使用摘要 flag 自证。
5. 单独重新计算未标记实体的 reach/tube 条件，严格检查标记高度1/1000小于其下界，才给 p4 外侧/互不交和全部十二矩加性的实体解释。

缺主报告或它不完整时，仍可以诚实输出已有条件式积分/代数；未标记管、外向嵌入、完整正总体积和分离不变量均不假填。只有实际全部条件付清后，原 R625/R716 商距离下界分支才可能给正 delta_E。当前没有这种数值结果。

## 7. 两个完整实际步骤

完整 ready保留原10与8个argv元素、34与60个标量 selector。所有 selector 名和表达式逐项不变，所有数值参数原样；只更换已声明的来源、运行标识、上游/输出路径及 honest scope。

Producer：

```text
--repo {repo}
--normal-fee-report {work}/fixed-fejer-meridian-batched-normal-root-and-sixjet-fees-v1/report.json
--outdir {work}/fixed-fejer-meridian-batched-r716-complete-moment-integrals
--seconds 600
--maximum-angle-blocks 0
```

Consumer：

```text
--repo {repo}
--moment-report {work}/fixed-fejer-meridian-batched-r716-complete-moment-integrals/report.json
--output {work}/fixed-fejer-meridian-batched-r716-complete-centred-moments/report.json
--closed-phase-report {work}/fixed-fejer-meridian-batched-complete-closed-phase-grip-v1/report.json
```

两步 parent_bundle 仍为 `fixed-fejer-reference/reference.npz`。600秒只调度完整积分块，maximum-angle-blocks=0保留全部计划，不能解释成只做零块，也没有另设小角度/小径向 fixture。所有 raw arrays、根盒、matrices、physical streams、完整块和矩报告仅在 runner。Git保存完整源码、全参数、来源恢复和实际紧凑记录；本次没有写 refs、queue 或改变运行中 job。

## 8. 全源再生与已做的源级工作

两个运行体通过完整文本替换构造。producer共16处明确来源/schema替换，consumer共10处；逐项逆替换恢复两个完整父源的每个字节。producer的29个顶层函数中，28个全文不变，唯一变化的 `_verify_source_roles` 只是三个全源名称/SHA；其余类/科学循环均由完整逆像保留。consumer全部13个顶层函数全文不变。数学核未变。

完整再生器读取两个whole父源和完整父ready，包含全部逐字 patch、完整参数替换/删除记录、18个实际全文件依赖和每个输出的完整预期SHA。参数逆过程恢复完整父对象；原参数文件自身始终只读并保其whole SHA。生成后的两运行体和ready都有完整长度/SHA断言。再生器不用导入科学源，也不运行AST或科学求解；它不是 solver 的新增前置步骤。

```text
python topics/visible-flex-larger-amplitude/scripts/resume_20261126/reproduce_fixed_fejer_meridian_batched_R716_moment_sources.py --repo <repo> --output-directory <fresh-source-directory>
```

本次实际做的是完整远端源读取、JavaScript字符串构造、完整源码正逆字节比较、137角色表相等、全部argv/selector保持和完整JSON数据字面回读。没有本地 Python、AST、compile、NumPy/Torch、Fraction算例、F/J/root、准确积分、数值fixture或benchmark。不存在速度收益或科学通过声明。

## 9. 留待实际结果的事项

当前源绑定异常的科学修复属于另一个真实版本。本包与原缓存/分批方案不宣工作浮点字等于旧版本，也不把访问计数当误差证据。新费用必须取得同一真实 immutable 点和完整 packet，付完相应 whole-angle、whole-radial、32段根与分支责任，再进行本文完整积分。任何源修复、不同N/M/J或不同seed版本必须明确绑定完整新来源，不能重贴本包身份。

原目标问题、连续全域度量/reach、工作字误差、外参数费用、网格和t精化及未知平行历史责任均不因本包准备而消失。当前可确认的是完整源码与全参数已经保全，尚无这里所需的实际场或最终证书。
