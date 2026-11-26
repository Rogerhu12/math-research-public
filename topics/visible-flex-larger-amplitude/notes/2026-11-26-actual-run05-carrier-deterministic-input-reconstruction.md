# run05 完整 observation carrier 的真实叶数再生与地址身份

## 1. 目的与当前事实

本说明给出一个独立的公开 Actions 输入再生入口：由原完整标量参数、同一真实 warm、原准确节点公式及旧05**实际返回的2397个积分叶**恢复旧 observation carrier 候选，并且只在候选的**整个 NPZ SHA256 和字节数都等于原实际文件**时承认其为旧地址输入。

它不重跑 seed19，不重放优化方向，不猜旧六个 Gauss 字，不把当前 carrier 的同一命令当作旧字节证据。这个必要输入步骤没有 F、J、端点根、几何筛或非线性优化；完整历史有限包络的新消费者仍另行承担每个新场的真实约束和明确的工作集政策。

旧05真实小记录：

- `notes/2026-11-26-public-actions-45870334713-1-part-001.md`，53029B，SHA256 `6eca69a388330b3e539aac4e2c793ce8256c724d52abf11adc8c8e85d49d08b3`。
- 该卷第2步 `independent-axisymmetric-R690-reference-prepare-v2-first-20261126-05` 完成，returncode 0。
- 原完整准备报告29795B，SHA256 `9a97bb6a615618c0be5e5e87f2cc059e292e548451ca23ccc4889a8b9cb3f846`。
- 原 observation carrier **227202B**，SHA256 **`dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0`**。
- 原 reference NPZ SHA256 `59027f3a144f8f0feb59e378b058178c781856803e6e704db8a6ff689b45d90f`。
- 原 source 为完整4e，source commit `be84fce832419adb10f0b714633a254943f88ade`。

07实际小记录：

- `notes/2026-11-26-public-actions-45909290354-1-part-001.md`，22619B，SHA256 `94ba3a5dac8397466e6b328683bb7739754e25c4c70347aef2502e99adcdab15`。
- 第2步 `independent-axisymmetric-R690-reference-prepare-v2-first-20261126-07` 完成，returncode 0。
- 当前完整准备报告29792B，SHA256 `78411d9a91633816fd514b927d288ad17922b67eca0f5bd4fd400ec3a06b1821`。
- 当前 observation carrier227211B，SHA256 `7c8b3cbffd66a360b01341db8e1179f211da3c264de85812020a5e48ad5637c3`。
- 当前 reference NPZ SHA256 `e435343954ed3c9fd2617e36185a1e0a71213cc6b432eb94578066954930c5db`。

两完整 carrier 不同。这既不证明其 cells/u 不同，也不证明相同。本入口实际解决这个缺口；没有把公开的 mesh/core 摘要错误拆解为六个 Gauss 字。

## 2. 完整源与逐数组依赖

新完整源：

`scripts/resume_20261126/restore_actual_run05_observation_carrier.py`

完整锁源26612B，SHA256 `ef67425800ae9de626a7f8f48fd89deb125fbf0e4d6af72cf79741d1e254664e`。这是尚未科学执行的新完整输入重建源。

新源严格核下列原完整源，没有修改这些文件或放宽原读取器：

| 作用 | 原完整源 SHA256 |
|---|---|
| 4e reference producer/context | `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3` |
| 26f observation plan | `26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d` |
| e091 accurate deep tail | `e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2` |
| bee5 complete warm/node recipe | `bee5ae587bd519189b0b27c249987d80d82ab66822cd4f1ea4746a769f7fb3c3` |
| FullHold scalar | `a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670` |
| integer scalar oracle | `babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0` |
| original Hold provenance | `ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1` |
| original history source, preserved dependency | `4d9dd319052d4e503e881c1a9f404501c0bb2f26dfb859cd836210f2a624bf60` |

4e的 `np.savez_compressed(observations.npz,...)` 完整成员只包括：

1. 原26f `plan.arrays()` 的所有14成员，含全部 cells/u/times/Hermite三jet权、正积分权、完整legacy权、piece/cell/index、六Gauss节点/权、order与lift断点。
2. 完整 mesh、`a_stages`、全部7377个 `a_observations`、各自绝对误差、时间carrier绝对误差。
3. radius、width、前三固定core字，以及原完整准确 scalar profile identity 字串。

它**不含**参考H、原mean/normal的工作根、whole-law四jet缓存、实际时长、文件路径或新准备报告正文。因此不需要重复完整参考高度、14753个unit-meridian标量查询、任何场或方向。再生器逐字保原保存关键字顺序、dtype构造及14个plan成员；容器格式是否相同仍由最终整文件SHA检验，不能靠 NumPy 版本保证。

## 3. 当前文件与历史来源不可混标

这两次 warm NPZ 真正相同：

`3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c`。

但是旧05 scalar 文件为 `0ee422aef7efcf8f307a3bd4c58f7f1bffd9bb581d889b1ce509167253d7a535`，当前07实际文件为 `931565a140891ecd6dedf579b778f3c95ab5172b1deeeddc892c1f1552c7d159`。旧node报告为 `2ec37435284048be6fbcde71c03d462692bfc708103ef553a35c570d51b3ee3c`，当前为 `1820f7c37d54e615c678c688da44c2f5aa0c1d7f4b0ebc00d3bad681dab59aa0`。

新源不会创建一个假旧scalar/node文件，也不会把当前文件记录改标成旧SHA。它分别保存当前实际四输入的路径、SHA、字节数，以及旧公开记录中的原输入身份。

完整 FullHold 源逐项只读取 scalar payload 的：

- `analytic_extension_origin`；
- `fixed_scalar_profile.geometry`，包括全部原 scalar knots、完整 initial_law 及其全部成员。

4e的 `scalar_parameters` 正好给出这个完整投影。05和07已经实际公开同一 canonical SHA：

`e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`。

再生器以当前实际文件重新计算这个完整投影摘要并硬核。FullHold 源、integer/hold 源、固定128 panels 全同，因此构造的准确参数和相同整数运算完全确定；输入中的其他provenance不会进入这些数学运算。

旧 carrier 的 profile-ID 是旧完整 definition 的身份，其中原 `original_input.scalar_input` 确实记录旧0ee。新源把它作为**原真实 definition 的来源参数**从公开旧记录读取，以原三source摘要与原e091完整definition公式重新构造并核原 profile SHA：

`e71b374557c5efa07ce2b5795c73f3e5b3a50d10d125b40c1f1682af37742350`。

报告显式记录 `original_scalar_file_recreated=False`、`original_node_report_recreated=False`、`current_files_relabelled_as_historical=False`。这是依完整数学参数等号恢复原definition，**不是声称当前9315文件具有旧0ee摘要**。它也不赋予新场任何旧几何证书。

## 4. 准确923节点的独立完整恢复

bee5保留原819个literal节点，并在其后按固定五段追加4、8、64、12、16个准确 affine-in-S 节点。前819节点逐字写入warm的前819个mesh位置；其余公式只依固定FullHold参数及literal lift width `float(.05)`。

新源从同一完整3df warm读取前819字，以 bee5 的完整五段公式重建全部923个有理对，不通过浮点mesh反解未知 affine节点。随后与当前真实node报告全部 `true_scalar_nodes` 逐项比较，并核唯一 `(1,-width)` 准确断点。

旧bee5真实输出已绑定同3df warm；其准确 FullHold 参数完全相同。故旧05使用的节点公式也由这些完全相同输入唯一确定。当前node的路径/原始payload不同不参与该公式。新源不复制或假造旧node报告，只恢复其已知数学节点输入。

## 5. 真实2397叶唯一确定原 e091 整数表

旧实际4e参数完整为：angles2048、seed_integration_order8、panels128、scalar_integral_tolerance `1e-18`、tail_cutoff `1/8`、时钟准入300秒。它实际报告 accuracy false、完整infinite tail true、live leaves2397。

e091以固定 `epsilon=1/8` 开始。有限部分初始仅一叶 $[1/8,1/4]$，无限尾 $[0,1/8]$ 完整另付。每轮：

1. 每叶两分量的误差宽度是准确整数。heap键为其负宽度与单调递增序号。
2. 弹出唯一确定的最优先叶；相同宽度也由序号唯一决定。
3. 准确有理中点一分为二，先左后右，序号与整数累加顺序不变。
4. 从总端点和中准确移除旧叶两端，再追加两新叶，live叶数净增1。

所有叶的 `_beta_jets`、integer三角/指数、Simpson区间和range交集均为原e091完整方法；leaf priority不读当前时间。因而归纳地，开始后的第 $n-1$ 次完整细分产生唯一的 $n$ 叶表。原300秒只决定在哪次已完成细分后的循环入口停止，不改变已完成表的任何叶或其值。

新 `ReconstructedTail` 只覆写这个表的**准入控制**：保原准确度停止，换时钟条件为 `len(live)>=2397`。它保留原所有数学方法、原完整准确definition和模型source；新控制器自身另有完整source身份。若原准确度条件在2397前已经满足，将报告不匹配，不绕过它。

不能只以叶数宣称再生成功：新源还核原真实的完整有理uncertainty：

`16969065832368305227111929060904651270139202719716738824077699765133823557287/28823037615171174400000000000000000000000000000000000000000000000000000000000000000000000`，

核 accuracy 仍false、完整原profile-ID、原radius字 `0x1.2124d67c6a7adp-1` 与原radius误差2.363596792320704e-13。以上全部取自旧05实际小卷，不是本地科学计算。

然后原 `target_a_box`、`point_definition`、`midpoint_and_error`、`upper_float` 在全部7377个原plan地址上依原次序构造a/ae/te。没有裁掉尾、换精度或只存低阶近似。

## 6. Gauss与完整容器身份的最终条件

26f重新生成当前平台上的6阶Gauss候选字。这里不预言它们与旧runner相同。压缩库/NumPy写NPZ的格式也不被猜作相同。

再生步骤的唯一身份接受是：

$$
\operatorname{SHA256}(\text{完整候选 observations.npz})
=\texttt{dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0},
$$

并且字节数等于227202。匹配时，完整NPZ成员就是旧实际文件的成员；随后从真实匹配文件读取cells/u与六Gauss字，再同07实际carrier逐成员比较。允许“旧文件已复原但新地址不同”的诚实返回，此时消费者应读两套真实地址并取并集，不因不同而丢旧集合。

不匹配时，完整report保候选SHA、各实际绑定及明确failure，但不给出可消费的 `material-envelope-carrier-binding.json`，不宣称旧六字、不认旧G已覆盖。不会自动试若干邻近叶数、改旧SHA、强塞Gauss字或放松整文件条件。没有把“输入再生失败”解释为课题不存在。

## 7. 可消费输出与完整责任

只有上述身份成功时，fresh output目录有：

- `run05-observations-restored.npz`：runner scratch完整原carrier，227202B，不提交Git。
- `report.json`：完整来源/数学投影/准入控制/真实比较，小报告。
- `material-envelope-carrier-binding.json`：小控制对象，schema `material-envelope-carrier-path-binding-v1`。

binding提供 `origin_carrier` 与 `current_carrier` 的真实路径、SHA、字节数，以及新producer source/commit/scope。它不自引用本report的未来SHA；后继独立消费者必须重hash两个NPZ并真正读取完整cells/u/Gauss成员，不能只信自报true。

完整report保所有14个plan成员的新旧dtype/shape/SHA及byte-equality，必要六个旧/新Gauss word作为小输入参数单列。公开summary只取标量、SHA、必要6字，不发布生成数组。根可将报告、参数和真实结论按原规则刊小摘要；旧NPZ仍只在runner临时目录。

准确目标/域、固定材料chart与角公式仍必须由后继完整输入绑定。完整未知历史包络的 nonlinear类别、可能protected的明确政策、全部当前场真筛、32段normal、原变量/原C与连续费用责任，都没有由这个小地址输入再生自动支付。旧场读数与证书不会转移。

## 8. 执行与静态验证

必要单步完整参数见 `restore-actual-run05-carrier-run07-ready.json`。它使用07当前真正存在的warm、scalar、node、reference report和carrier，两个已公开小volume；没有依赖未知seed19报告或虚构原raw。公开Actions上实际执行前，未来候选SHA/比较值均未预填。

本地仅完成完整源阅读、逐数组依赖与确定性控制证明、stdlib AST/compile、重复literal-key与尾空白检查。另以完整 AST 比较确认新旧 `_build_integral_table` 在仅规范化模块限定名、准入条件和末尾真叶数核后完全相同；没有改叶数学或优先级。未导入NumPy/e091、未执行任何科学数组或标量运算。实际重建与完整SHA接受尚待07真实返回。

这不是新增科学前置fixture，而是为履行未知同目标历史地址责任所需的原输入恢复；它不阻断其他已经授权且来源完整的独立科学分支。

