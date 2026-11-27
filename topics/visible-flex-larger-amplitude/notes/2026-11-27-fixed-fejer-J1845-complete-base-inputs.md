# 固定 Fejér 目标的完整 J1845 径向基础：准确地址、全 scalar、原参考及全 Q

本轮完成五份独立完整基础运行源及完整可逆文本再生器；这是旧 J1845 已登记数学与现行固定 Fejér 输入的实际接线。没有运行新的 J1845 科学求解，没有父场、末点、根、数值收敛或几何证书。完整 lower/upper、三个独立/终态/末点参数计划另行接续；本说明不把基础源码准备写成完整研究结果。

## 1. 当前目标与来源

现行目标由 `fixed_fejer_r690_reference_inputs.py`（whole SHA `89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60`）预先定义；材料图采用 R717 的七个预定 RN-even binary64 系数作为准确 dyadic，完整160槽保留。原 R690 全尾法则不截断。当前参考源码为 `fixed_fejer_axisymmetric_reference.py` / `e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb`，支持 seed 为 `ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a`。

公开 run12 `46011377225/1` 两个输入步骤已返回。数学 recipe identity `957cf0fc1ee59835f499b21a2300094ecb8c8a39fe14a1ebd987cef11305faa9`、完整 fixed target identity `50df37b6b832dcdd53d05c54138e62e43df6b14df68d946a7b8a7b8227f58319`、reference model identity `ea64e2fe5e272648195128d53521705cc266d82f7d2636bd7201b90fcf172fac` 分别绑定。这些是实际输入记录，不是一个已返回的完整场。

标量原参数投影 identity 是 `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa`；实际固定 scalar definition identity 是 `d492e4ad97245a8474f1a73a8787aac2fc5691b1f928d0b8ea72224cabd55160`。二者不得混用。其当前完整积分表有2218叶，原 accuracy_reached=false 保持。2397旧表仍只承担此前登记的历史/地址职责。

原 [J1845完整说明](2026-11-27-run10-J1845-complete-radial-continuation.md)、原全源及参数总表 `run10-radial-J1845-complete-source-delivery.json` 保留。旧 source/target 的完整算法结构可用，旧 e711 / 081 / optimized chart 或未知末点不成为本目标数据。

## 2. 五份完整运行体

| 角色 | 文件 | 字节 | SHA256 | Git blob |
|---|---|---:|---|---|
| layout | `fixed_fejer_radial_bisection_layout.py` | 18929 | `a31d80a953722cc3644f793e4a28a372d980f6d0af7c8d98402f5f4739e3b5cf` | `7374adfdd1cfef17d15aae80d7dd88295d518440` |
| affine | `fixed_fejer_exact_affine_supported_reference.py` | 23452 | `622e50feab2dcd65b0191a880375a6fb064be2382a8fd576f09e08a69ac6fd95` | `0ef1acf9c39f41ee932baebd76b8feb68db2e8a7` |
| observations | `fixed_fejer_complete_dyadic_radial_observations.py` | 28203 | `a89cb4f660f56ccc49e6f59191730aacc414cb36714ec64c2061784d3215f07d` | `54a8322239c739dd9ea38bfa91827f765c7fd789` |
| base | `fixed_fejer_radial_refined_meridian_operator.py` | 45823 | `78ded2682f5a42bc44a1939e9d814eec17254d1385dfe08a545d6aee109892ef` | `f924383de380d1117c48633855687055c13b3fa6` |
| Q | `fixed_fejer_radial_literal_zero_moment_input.py` | 36238 | `2e0c056652b10b4158bc74ec1fd2cdae54e05fb439154a462d6f1e4eb717428c` | `def2762a906f138ae05a01d76a9a2124e5c0736a` |

文件都位于 `scripts/resume_20261126/`，完整运行体合计152645字节；每件小于100000字节。全部公开 Actions 限定、原输入检查、完整数学函数和失败范围保留。每件是完整新源，不在运行时给旧源打补丁。

### layout 与 affine 查询

layout 完整保留准确 affine 节点定义、旧节点到偶数槽的逐词复制、完整三通道 Hermite 系数限制/包含和地址映射。参考网格仍 J923；当前网格 J1845。两个网格各有自己的完整 identity，不能用 current mesh 覆盖 frozen reference。

原准确节点写作 `A*S+B`。新子胞元 `(2*i+j,u)` 的旧胞元准确局部坐标为 `(j+Fraction(u))/2`，而不是先舍入旧局部坐标再称同点。只有准确 affine 等式与 binary64 可表示性都成立时才用原快速地址；其余调用完整原 scalar/seed 法则。所有旧节点及原482个角通道完整保留，新增中点与全部自由 jet 不删除。

affine adapter 保持原完整 provider 方法、完整 mean kernel `f8487dfe917e76dae12e3ba5667f66423ada305c077160d606d6f6aea6dc3917` 和完整 seed 对象。只变明确 source/schema 对应，未改变任何 scalar、normal 或场计算公式。

### 原完整 scalar 与 observation union

observer 保留全部原7377行，另保新网格原完整 node/midpoint/six-Gauss 原生14753行，形成完整正权并集。Gauss 规则不假称嵌套；每个行的准确地址、scalar word/error 与原 parent stage map 全部保留。当前 outer 场的八 Gauss 积分规则与观察 six-Gauss 是不同合同，不互换。

`_restore_actual_scalar` 完整保留原实现：整源核 `e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2`，读完整当前 preparation 的 `true_scalar`、准确原 input definition、实际叶数/叶求值数、epsilon、要求宽度及原 admission 字段。重建后只允许 elapsed_seconds 不同，所有其余 metadata 字段必须逐项相等；完整 scalar definition 与 identity、accuracy status 都再核。

该 observer 的整个 `counted_tail_class` 工厂逐字取自实际 e717 参考，完整函数片段 SHA256 为 `0b5b91706b1df8806bae649d367a55defdefbf13d348ced430eb0b11d9dddcc4`。它返回 `ReconstructedTail`；原准确整数 leaf 操作、heap tie 顺序、全尾与要求精度停止均保。叶数是当前实际表的重建参数，绝不代替全部 metadata 或准确度。预定叶数/不由时钟选择的说明属于原外层 `deterministic_scalar_work`，不是虚构的 scalar 子类属性。

### base 与完整 Q

新 base 保持完整 SO(3) meridian 的 field、全部 J/J*、范数、domain、径向和角导数、全部 current core/omega/H 自由量。它显式分开 reference_J=923 与 current_J=1845，完整绑定三个新径向模块以及真实 e717/ad52。材料图描述明确改为预定 Fejér 图；没有旧 optimized warm chart 定义目标。

新的 Q 以当前 Fejér `ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3` 完整体为父。完整旧 J 的 `_radial_source_module` 与 `_radial_binding` 加入后，保留当前原 recipe canonical、predeclared chart、warm_or_BVP_core_consumed=false、same_previous_target_claimed=false 及 `fixed_input_bundle_sha256` 等全部检查。不是把旧 radial Q 换标签并丢新目标规则。

原 base/reference mesh 相等改成明确双网格完整关系：layout 的 complete original reference、原 mesh、新 mesh、准确 affine definition、全部 union arrays、parent map、正权规则及所有 shapes/dtypes 各自严格核对。固定 chart、scalar、seed、原18个 Q words、两 bubble triples及原 provenance 全保。base current_J=1845；reference 始终 J923。source/schema 改变并不等于数学 g 改变，也不构成新工作场的逐字相等断言。

## 3. 全部完整父与精确改动

| 角色 | 完整父文件 | 字节 | SHA256 | Git blob |
|---|---|---:|---|---|
| layout | `radial_bisection_layout.py` | 18923 | `cf5bb90fa59ea1e1662095a317260f68d2568e33f941e0d6750e9c490053b744` | `50304523b343957632dc25de61de403b8ca3bad4` |
| affine | `exact_affine_supported_reference.py` | 23435 | `2d1f02119c019b298caf8f7877ab3c9ba9cd0feff85155d095e00bce7394d117` | `1c7f9ddde0b94692b792cca40cf466046e30ed5b` |
| observations | `complete_dyadic_radial_observations.py` | 28167 | `2e2031901477dad98db1e97d5d5fcf9fd0815e537cf1dba01ad0d18e95d67b74` | `e7ab1d8f3a52720e484fc4531156d8e233d592ab` |
| base | `so3_radial_refined_public_reference_meridian_operator.py` | 45749 | `130ee3c53389fced6b01c211782756c2501e1a96c60db428c233faa5574ae7e0` | `9851a696fea6d07690d61dbe23452c185fc4485d` |
| Q | `fixed_fejer_literal_zero_moment_input.py` | 31409 | `ca4fef4066bfb6d6fedbdf9b65349f7f0ba8480376858c84faa8ee3d4d4b97b3` | `172d2b82eca6496058d2c73560de86bada50f12d` |

layout/affine/observations/base/Q 分别有3/5/4/8/8项明确纯文本事务；完整事务在下面再生器中，不以本说明的缩写替代。Q 的 radial helper 来源另是完整旧 `radial_refined_public_reference_literal_zero_moment_input.py`（35736字节，SHA `59033328b5cdfd3de96026cd860bcab71d598dee4fce774c08f9c299eea2b652`，blob `3322530f8cf16214cb3e6c11ca368d56b9af44d9`）。工厂来源是完整60335字节 e717 参考；这些来源完整保在仓库。

全源再生器为 `reproduce_fixed_fejer_J1845_base_sources.mjs`，23129字节，SHA `5d6c57b87bdbf28892fbd52782b9b9050303a087fe00706a257aee849dedff17`，blob `b817aa98c7a62a818f460474d0eabf9a897ca944`。它读取五完整父的实际全字节/whole SHA，按明确事务生成五完整体，再逆全部事务恢复每个原父全文，输出前核每件完整大小及 SHA。使用方式：

~~~text
node scripts/resume_20261126/reproduce_fixed_fejer_J1845_base_sources.mjs \
  --source-directory <complete-original-script-directory> \
  --output-directory <fresh-independent-directory>
~~~

本轮已在 V8 纯文本上实际完成所有正向/逆向全体等式及远端 Git blob identity 核对。未运行 Python AST、compile、NumPy/Torch import、F/J/root、scalar 积分或数值 fixture。再生器仅保存来源能力，不是新科学准入门。

## 4. 后继完整求解及未付范围

后继将保当前 immutable-point 59048字节 closure 家族与1aa完整 normal32实现，不退回旧每key全点拷贝的 detached 路径。原完整 J1845 地址/历史/共同父 functional、所有旧/新自由量、双 mean、全尾、当前 Jacobian/范数及原 metric/restoration/line-search预算持续保留；这些不由五基础源码代替。

合法独立模式不需要不存在的12 final；它从完整冻结参考初点出发，保所有已知和未知历史来源。terminal 只能读真实完整父 report/history，final 另需真实477499/274d父及其全部13成员、全部原字与点摘要。进度不是父，未返 typed 不补空。

准确 Hermite 包含与新积分读取不自动证明浮点工作场相同、normal全角同支、误差下降、连续 Gram、reach、整像 amplitude 或闭面存在。共同原7377 functional须在真实新点重新评价。固定 g、完整参数/t下的真正 mesh/M/t精化、准确 sixjet/闭帽/全phase费用和全部README标准均未完成，继续实际工作。
