# 完整 full-Phi 的当前粗空间 PCG 与父行 SOC：显式复合派生及真实父续算入口

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

## 范围

本条把已经分别完成的 [R681 当前线性化粗空间预条件](../results/R681-current-J-coarse-frame-preconditioning.md)、[R680 真实几何步的二阶修正](../results/R680-true-geometric-step-second-order-correction.md)、完整父行 SOC helper 和原模型 / R671 两个完整 driver 接成同一可执行入口。它新增的是完整源码身份、实际父报告和执行接线，没有新增数学完成结论。

这里未执行新科学计算。原完整变量、同一个固定目标度量、原全部观察与正权、谱目标参数、物理母范数、永久几何位置和真实回溯均保留。PCG 用固定 SPD 作用改变当前凸二次问题的迭代方法；SOC 在指定条件下额外评价一个原母范数中的修正方向。二者都不构成连续 metric、全域曲率、reach 或完成标准的证书。

## 1. 冻结依赖和两份新增源

| 角色 | 文件 | SHA256 |
|---|---|---|
| 新完整复合 driver 派生及未来父绑定 | [derive_full_phi_coarse_pcg_soc.py](../scripts/resume_20261120/derive_full_phi_coarse_pcg_soc.py) | `40e8c42b8c66424d06ff08af8dff8d1505eff2b4f48ba905c9ae405000d2357e` |
| 新实际父复合续算入口 | [launch_full_phi_coarse_pcg_soc.py](../scripts/resume_20261120/launch_full_phi_coarse_pcg_soc.py) | `3f1516c0997cc0bd2eeafbe1f9b9e1646380904ac2c055440c6e668129383e36` |
| 原完整 driver | `fullclosed_gauss_inequality_qp.py` | `5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a` |
| R671 完整 driver | `fullclosed_gauss_exact_tail_inequality_qp.py` | `b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8` |
| 精确 binary 位置派生 | `launch_fixed_g_refinement_qp.py` | `100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622` |
| 已刊独立 SOC 派生 | `derive_full_phi_parent_row_soc.py` | `805823e49970246bf532b65a0caefd88244b414ee52f8f555ff28b745d2fd30a` |
| 已刊 SOC 数值 helper | `full_phi_parent_row_soc.py` | `5bc50d6b18223685da8ea355d179191234ad83b5e92fd6313f4070b7e02127c7` |
| 已刊独立 SOC 续算入口 | `launch_full_phi_parent_row_soc.py` | `9b7d50fd7d1a0332fc493f848688b792dff39fd2a1af4914349d048abe080d0a` |
| 当前粗空间 PCG 源增强器 | `augment_full_phi_coarse_pcg.py` | `f96cb48933d1356b97b5a687d25cc05cd33188b08c14cd0b439f170b027fce18` |
| 原增广坐标的粗空间 frame | `full_phi_coarse_frame.py` | `324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da` |
| 当前完整谱 Hessian 的粗矩 | `full_phi_coarse_moments.py` | `da083ae9b20674a29121c25d5b57ef867fba442559a50791b7fc0b43d4db5719` |
| 固定 SPD 的活动集 PCG v4 | `fullspace_feasible_active_pcg_v4.py` | `dd59510599334843cf79159cafe5d2548818ab8b7fdf6813f164ee811247ad3b` |
| 显式 None 的原 v3 后备 | `fullspace_feasible_active_cg_v3.py` | `fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4` |

以上文件的公开目录统一为 `scripts/resume_20261120/`。本次没有修改任何上述已刊冻结源。新增 deriver 为 11,710 bytes；新增 launcher 为 12,055 bytes；两者仅使用 Python 标准库进行源码准备、元数据读取和子进程组织。

实际父与末端阻尼仍复用已刊 history `4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60`；原完整父 planner 为 `18ba10e5a37f5032b37388a7bfcdede97d11dc680685d73520732f9a278697f7`，R671 同模型父 planner 为 `425fd1d1254450afac26b2ca29ca4ffbb6fb93d59588163bef726e34999e4703`。

## 2. 完整 driver 派生，不凭注释头继承规则

新 deriver 依次进行以下操作。

1. 验证冻结的原完整 / R671 完整 driver 及 `100e` 精确位置源。
2. 调用冻结 `805` 的 `build_ast`，得到已经完整包含 `100e` 改动和 12 个 SOC 修改点的 AST。没有重新手写 SOC 科学逻辑。
3. 将该完整 AST 的规范 Python 文本传给冻结 `f96`。核其输入 / 输出文本 SHA、增强器 SHA 和四个数值组件 SHA。其 6 个准确修改点各只发生一次。
4. 在唯一 run report 中增加 `pcg_soc_derivation`，并用明确的复合 schema；全体物理、目标、范数、SOC 回溯代码保持该前序 AST。

运行报告 schema 为：

- 原表示：`fullclosed-gauss-original-coarse-PCG-parent-row-SOC-v1`。
- R671 表示：`fullclosed-gauss-R671-coarse-PCG-parent-row-SOC-v1`。

报告同时保留 `soc_derivation`、`coarse_preconditioner_derivation` 和新的 `pcg_soc_derivation`。最后一项写完整派生顺序、两种变换的源 SHA、实际输入 / 输出文本身份、全部数值组件 SHA，以及完整 AST 的必要修改点计数。

`bind_soc_parent` 是给已刊 SOC launcher 的兼容接口，但显式区分两类新父：纯 `805` SOC 父委派原完整 binder；含 `pcg_soc_derivation` 的父则从冻结 base 重新执行整个 `100e → 805 → f96 → 复合身份` 派生，比较实际提供源的完整 AST、实际源 SHA 和完整报告 lineage。它还核实际 `soc`、`coarse_frame`、`coarse_moments`、`qp`、`coarse_qp_v3` role SHA，并要求本入口声明的 PCG enabled 分支。它不会仅凭 SOC 注释头接受一个后来加入未知 body 的源。

该绑定只说明来源、模型和代码一致。`enabled=True` 不表示每方向预条件器构造成功，更不表示 PCG 已收敛。

## 3. 当前方向内的 PCG / SOC 生命周期

每方向先按原完整场和永久位置建立原不等式 $Cz\leq b$、原完整目标线性化算子 $A$、虚拟右端和原增广坐标。当前谱目标采用已刊精确残差 Hessian 桥；它的虚拟残差平方和并非实际谱目标，这一点原记录继续保留。

PCG 增强器随后用这一次当前的 `bridge`、`coordinates`、`height_map`、`basis`、`coarse_diagonal`、`coarse_chol` 构造 R681 固定 SPD 作用。背景逆尺度明确为

$$
\beta=\frac{1}{\mu^2},
$$

其中 $\mu$ 是当前方向实际阻尼，不是旧父报告中的某个历史初始值。粗矩阶段块固定为 8。这个构造不修改 $A$、$C$、$b$、完整母范数或阻尼更新规则，也不新增完整 `Jv` / `J^T` 调用；解析粗矩的实际构造时间和元数据单独记录。

构造出现已定义的 `SmallSPDUnavailable` 或受限数值资源失败时，实际报告保原因，并在这一次求解开始前显式传 `None`，由 v4 委派准确冻结 v3。模型、来源、维数或布局错误不会被这种后备吞掉。预条件作用在迭代期间失败时，v4 返回其真实失败状态和最终线性诊断，不自动再开一个未登记的 v3 求解。合法截断方向仍由完整实际回溯评价；它不被标成 PCG 收敛。

QP 返回后释放 PCG frame / factor 的引用，避免 SOC 额外保留这些工作数组。SOC 所需的 $A$、原虚拟右端、原返回方向 $d$ 和完整 $C,b$ 延续到该方向回溯完成。新的完整增广空间、坐标提升 $T$ 和其转置均沿原源，不建立另一个窄空间求解器。

只在第一满步 $\alpha=1$ 已通过定义域与真实 Phi 下降、但因真实已知点几何失败时，调用一次冻结 SOC helper。它固定父行的曲率位置、主曲率 branch、半径伙伴和父行规范化，不在试点重选行的最大半径。其选中行的真实规范化残差和右端为

$$
c_i(d)=\frac{0.03\,D_i(x+Td)\,|\kappa_i(x+Td)|-0.992}{n_i(x)},\qquad
h_i=c_i(d)+\tau\|d\|^3.
$$

只在 $c_i(d)>0$ 的所选行构造原增广范数最小修正。rank-aware 正交行分解取 $C_I=RQ$，其中 $R$ 为下三角，故

$$
e=-Q^T R^{-1}h.
$$

秩丢失会放弃这一次提案，不删行冒充解。完整原 $C$ 的 $Cd$、$Ce$、$C(d+e)$、所有 slack 和规范化前的物理线性产品仍逐行记录。新点为 $x+T(d+e)$。真实读取它的完整残差、Phi、定义域、全部永久几何点；本次发现的新曲率 / 半径位置即使修正被拒也永久保留。

修正的预测使用新的 $A(d+e)$，不是把旧 $Ad$ 的预测配给修正场：

$$
s_{\rm corr}=r_{\rm virtual}^T A(d+e),\qquad
\widehat\Phi_{\rm corr}=\Phi(x)+2s_{\rm corr}+\|A(d+e)\|^2.
$$

其真实下降比、Armijo 条件和阻尼更新均用这同一个修正方向。额外完整算子成本至少包括实际发生的一次修正模型 matvec，并分别记录新残差 / 全已知点读取是否发生；任何未发生的步骤不会写成已经完成。修正未接受则继续原始 $d$ 的原回溯，不尝试第二次 SOC。

## 4. $\tau=0$ 的首实际选择和未付责任

本入口要求 `--soc-tau` 显式传值。首批拟用 $\tau=0$，即不加入尚未标定的三阶 buffer，只作当前违反父行的最小二阶修正。它是具体算法参数，不是已经验证 R680 的局部 Lipschitz 常数或三阶充分阈值。

因此不能从提案存在、QR 满秩或完整原线性 slack 通过推出真实几何可行。接受仍由修正场的真实完整 Phi 与全部永久点筛查决定。新的未记录峰、未选行、半径伙伴改变或二阶以上误差都可能使它被拒；原回溯保留。有限点筛查成功也不等于连续全域几何证书。

## 5. 从真实自然完成父报告接续

外层新 launcher 从冻结 `9b` 独立 SOC launcher 派生一份完整的 stdlib 副本，仅增加 7 个准确源码修改点：复合 deriver 的 SHA 和默认路径、两项 PCG 源参数、四个固定数值组件绑定、driver 的启用参数、显式复合计划身份以及真实返回状态记录。它没有编辑原 `9b` 文件或父报告。

初次旧父仍由原 `18ba` / `425f` 在 `--print-command` 模式下核真实完整报告、实际 final bundle SHA、原 carrier、全部物理 / 范数依赖、末端阻尼以及 R671 canonical 模型。新入口显式选择 v4，原 planner 会单列这次 QP 模块改变。对于未来纯 SOC / 复合父，新入口先用第 2 节完整 binder；再生成仅改父源绑定调用的 preparation-only planner。该副本不允许运行科学，原其他父身份检查保持。

末端 $\mu$ 从真实记录重放：接受满步且实际下降比大于 $0.75$ 才取 $\max(10^{-8},\mu/2)$；接受其余步保持；整方向不接受乘 $4$；无方向使用实际初始阻尼。SOC 父额外核显式 `final_damping` / 各方向 `damping_after_direction`。被接受修正的顶层方向模型必须准确对应其 `soc.trial`，然后才按这同一规则继续。

全部调用者旧 manifest 和父报告的全部历史位置取精确 binary tuple 并集。父报告 trial 中的新永久点、SOC 提案和修正 trial 中 tagged 父伙伴、最终 memory / protected 点均沿已刊 history extractor 读取。grid 索引在 Actions 用实际旧 carrier 与实际旧 N 转为位置，不沿用 round13；不继承那些点的旧几何数值。

本次已返回的实际 R671 v3 父为 `exact-tail-full-phi-v3-continuation/report.json`，报告 SHA `8b1935fd34e6bb3b30415302506043e61f61827d62a42a1a991e3dd6efb5a1f7`，final bundle SHA `7fd352757ca69554b367f08c6a76f343729aef795f68f218e202e2cacd933c21`。按该实际报告，本轮接受 $\alpha=0.5$，实际末端阻尼仍为 `0.0007539530259341321`，Phi 约 `8.52075845e-8`；满步 Phi 约 `7.82023445e-8`，但已知点产品约 `1.001267636`，故被拒。QP 的 256 次上限和 `iteration_limit` 保留为真实状态，不能解释为 KKT 已解或已证某个 restart 是主因。

新入口不把这些历史数字硬编码成下一父身份；实际运行必须读取调用者给的报告 / bundle，并逐项绑定。原 R671 planner 保同 $\lambda=1$、同准确 $\eta$（该父起点索引 885）、同 scalar / nodes / M / N / carrier / 母范数，采取 keep-q。新的 full-Phi 方向默认 1 次、256 次内部推进、atol 为 0；不会因此声明优化成功。

公开后典型调用结构如下，路径均须指向本次真实 runner 文件；重复 `--manifest` 可保全部调用者位置源：

```bash
python scripts/resume_20261120/launch_full_phi_coarse_pcg_soc.py \
  --repo REPO --work WORK \
  --model R671 \
  --parent-report ACTUAL_COMPLETE_REPORT \
  --parent-source ACTUAL_PARENT_DRIVER \
  --bundle ACTUAL_FINAL_BUNDLE \
  --carrier ACTUAL_OBSERVATION_CARRIER \
  --node-report ACTUAL_NODE_REPORT \
  --scalar-input SAME_SCALAR_INPUT \
  --manifest ALL_KNOWN_LOCATION_MANIFEST \
  --outdir NEW_OUTPUT_DIRECTORY \
  --directions 1 --maxiter 256 --qp-atol 0 --soc-tau 0
```

源码目录实际位于 topic 下；命令中的 `scripts/...` 是该 topic 内的相对写法。`--print-command` 只做完整元数据准备，不读取科学数组。`--prepare-source-only` 仅输出 launcher 的源码派生记录。实际求解仍由已刊 Actions guard 约束。

## 6. 报告消费和归因

计划 schema 为 `actual-full-Phi-parent-to-current-coarse-PCG-and-SOC-v1`；计划记录父准备 argv、完整科学 argv、实际末端阻尼、组件身份、canonical 模型、全部位置 union、显式 $\tau$、$\beta$ 规则和真实执行状态。

完整求解报告沿冻结 `f96` 保留顶层 `coarse_preconditioner_setup` 和每方向 `coarse_preconditioner`。每方向 `qp` 永远指原未修正的主 QP 返回方向；其 `status`、投影梯度、原约束诊断和实际算子计数不得被 SOC 接受标签覆盖。

若 SOC 接受，则顶层方向模型描述实际被接受的修正方向，`accepted_update_kind='parent_row_soc'`，`accepted_direction_is_main_QP_solution=False`，`main_QP_diagnostics_remain_uncorrected=True`。原回溯 ray 的模型保存在 `uncorrected_direction_model`，其 `trials` 仍是原 ray；修正试点及其真实预测读取在 `soc.trial`。消费者必须按这两类配对，不能把修正后的顶层 slope 配给原 ray 的历史 trial。

返回后新入口再次完整重建所用 driver，核自然 complete、actual final bundle SHA、QP 模块 SHA、carrier 和 R671 最终 canonical 定义，再重放实际末端 $\mu$。它同步 PCG 构造 / 应用状态、实际方向数、SOC 尝试与接受数、最终已知点筛查等。不将 source preparation、PCG enabled、数值截断解或有限筛查提升为 README 完成。

## 7. 本条实际完成的源码检查

本地仅执行标准库源码派生、AST / compile 与文本 roundtrip。两种冻结完整 driver 的精确位置、12 个 SOC、6 个 PCG、唯一复合报告身份均在声明位置发生；launcher 的 7 个准确修改点也各发生一次。没有导入 NumPy / SciPy 数值模块，没有构造科学数组，没有执行 driver，没有造 fixture。

本次源码生成样本为：原完整组合 driver 64,419 bytes，SHA `de2cf83ba292323255c6e90a51a9695fcccce75e12c171de6a94a24810df32f2`；R671 组合 driver 70,119 bytes，SHA `a2e47b098912178b8192b1552f1fac9b58ff4858de7a3e36a378cb67f5b8f930`；派生 launcher 21,681 bytes，SHA `2a3526e8c841e4928c1f428b18d26baa031ab972bba8ea2937daaca3a7308dfa`。它们只是本次源码展开，不是实际 Actions 运行证据；runner 仍记录其真实生成源码 SHA。

后续直接运行当前新父的一次完整方向即可得到算法证据；本条没有新增独立科学检查流程或先验成功标签。

## 8. 本次明确排入的实际预算

本次已向同一run44758209061的后续队列追加 `actual-R671-current-coarse-PCG-parent-row-SOC-02`，从真实7fd完整终父启动一次256推进方向、atol=0、rtol=1e-6、192工作行、stage block64、tau=0。完整argv及输出路径见[队列](../computations/resume-20261120-followups-02.json)；输出前缀为 `exact-tail-full-phi-PCG-SOC-first`。当前已有入场计算自然结束后执行；本条发布时只是已排，不是已启动或已成功。

全部父报告历史位置与原完整compact manifest准确并集，旧父源路径明确指向其真实 `derived-R671-full-phi-exact-positions.py`。主QP数组和SOC行QR工作缓存只在runner，子进程自然返回后可删除它此次新生成的行缓存；完整report、方向、final及输入不删除，也不进Git/Release/artifact。真实结果将单独刊，不以源码准备替代。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
