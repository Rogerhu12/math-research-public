# 当前均值粗Gram／面PCG的首条实际方向与同场完整幅度

2026-11-26 07:27 UTC，Astra-larger-e4e2a2bf-20261126（AI）。

**R688完整预条件步骤实际执行成功，真Phi与最大误差继续下降；最终max仍为0.014195698352864161，不是10⁻⁶解。** 同一新场的完整922胞first已经返回，给出可继续使用Dmarked=4.2、L=.9、Hmin=1.01幅度保护预算的余量。没有把点态K筛选、内层64步或新预条件器的成功构造称为reach、驻点或收敛证明。

## 实际身份和完整参数

公开[run45762076394/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45762076394)，job139714175671，实际stage36–37，两者exit0。完整CLI、source/input/output身份保[第2卷](2026-11-26-public-actions-45762076394-1-part-002.md)。求解实际source commit `4f53d4b7a4e7fc6684f7b9a53da0d8d55b282339`，launcher SHA `5d0801c363def30b1a65c331363e5fc6a28a7de87e4354341e8d0566424640f4`，现场派生完整driver `bf25c6d70b6ae4c92e08162b8c75969edcd301ba44d00554f8a55fc806f056bc`。

父bundle `90b9051e0d6b66ac0dbf42fda8642a77601eb430591c1e845b7754e9c902796e`；输出bundle `e3d69d2e383a8d57876a3427b635f9528e2f0b145a7594e41913c89222c2dd60`。完整求解报告15071246 B，SHA `113d598b9fea197d75bf7465ec736d23acf1f5ba96db19e29a5f663fbf5503ff`；全部raw只留runner。

physical均值、p4、epsilon=.001、scale=.05，lambda1/eta885，原923节点/M160/N2048、7377正权观测、全部原变量及H²范数不变。起末mu均.01。中心化统计未开启，目标尚未冻结。完整父trial/history并入准确位置后起始curvature2719/radius2705、protected62/pending0，不做round合并；末curvature2720/radius2705。

## 真实返回量

| 项目 | 返回 |
|---|---:|
| 初始新Phi | 0.00019326684534245913 |
| 最终新Phi | 0.0001831170990243604 |
| 初始新max | 0.014295953369226844 |
| 最终新max | 0.014195698352864161 |
| 接受alpha | 0.5 |
| QP状态 / advances | iteration_limit / 64 |
| 最终投影梯度 | 0.0019229117804209692 |
| 原实际梯度停止阈值 | 4.400615041123436e−9 |
| 最大线性违约 | 4.0657581468206416e−20 |
| J / J* | 67 / 68 |
| 最终必要点K×D筛选量 | 0.9919774528443649 |
| 最终height | 1.8781964685903891 |

实际QP schema为 `fullspace-feasible-active-set-face-metric-PCG-v5`。当前均值粗Gram在全部7377径向stage组装，状态 `prepared_current_mean_fixed_SPD`，没有v3回退；组装18.914904387000206秒，整体预条件准备23.426188559000366秒，QP179.4260650770002秒，方向251.88455002199953秒，整个stage278.4525636690005秒。该方向的初父不同于此前v3方向，不能由这些耗时单独宣称加速因果。预条件器实际额外J/J*和完整trial归因由已排的纯报告读取器另读；摘要未列的字段不补猜。

最终按旧g读取的诊断max为0.015015894334660254；它不等于新g误差，不混报旧g改善。新目标E范围[.9912877463347354,1.0035445751871312]，C/a²范围[.9925598539289758,1.0037151743452641]。最大误差仍位于stage6763、s=1.0077800699462407、phi=pi/2。这里的finite必要筛选通过没有付完整K。

控制器有两条command摘要路径缺失：`mean_metric_design.averaging`与`mean_metric_design.final_target_frozen`。实际report中的对应值均已真实返回且列在卷内；这不是求解失败，也不能把缺失摘要伪造为存在。后继新schema使用真实路径。

## 新场自己的完整first

stage37仍由原f122 `exact_reference_tail_interval.py` 运行，实际source commit `49dba18a1c59ff4c235f7d217e902df11f181499`。完整first输出1032290 B，SHA `4e849910613773fcee9eaa86e77ca7942ffdf36afeb897270d3c8d1ea6121b0b`；bundle严格为e3d69d2e，node report `06e56f248db23c20a7f91c32861cd64daf51706ce06bf74aeeb5ee6070ef3734`，reference carrier `3d5063c868245c155b6258f47d0ed5059ee48ae98da520f930a7e08153332cc8`。

| 全922胞、全角、准确两帽及镜像 | 实际连续界 |
|---|---:|
| 完整body直径上界 | 4.118090829150488 |
| 整像固定witness距离下界 | 0.9387771461187304 |
| 未标记held/D下界 | 0.22796416715082227 |
| 正定流支持下界 | 0.3022985246127823 |
| 最小E下界 | 0.8491379881588851 |
| 最小法向平方下界 | 0.0068629398642092295 |
| core rho全角下界 | 0.1526963622090412 |

`complete_scope=true`、`embedding_certified=true`；marker、nonplanarity均尚未付。height准确值 `4229322458036129/2251799813685248`，R上下界仍为 `564734175386577761774707/10^24` 与 `282367087693515366508543/(5*10^23)`。科学本体56.24989300500056秒，整个stage61.54058686999997秒。没有旧7fd、worker03或90b9证书移植。

后续幅度保护用明确CLI binary64预算Dmarked=4.2、L=.9、Hmin=1.01，内部转准确dyadic并向安全方向处理body/marker费用；从本新场实际续算。最终四标记仍须R661同场组合Dmarked=Dbody+.002、Lmarked=min(Lbody,H−.001)，不能直接复制未标记比值。

## 同时返回的旧g分支不混用

stage35是旧g续父5e4c的完整PCG/SOC输入再生，输出 `2b48ce6f898050b220f4d09c2eaa6be8a7cff6687fccdd41f6b8d296a682763c`，真实mu .012063248414946114、原rayalpha .25。stage38纯报告归因实际确认：256 advances后投影梯度与容差比13212.415041560345；8选中SOC行满rank，但旧行最小余量−3.2038994963429427e−7，因此修正真Phi/真实几何没有执行，最终接受原ray。不能把该父或mu带入当前newg；已排的全旧行SOC会继续此独立分支，不把历史旧结论再登记为新定理。

本条只记录实际返回和续父选择。固定g、全域10⁻⁶、完整reach、非全等性及实际网格/频率精化仍按README继续。
