# M320 纯报告入口的最终完整源绑定修订

## 1. 独立版本与实际范围

本版本保留原完整 e244 纯 reader，不修改其历史字节。新的完整 reader 仍为 `read_frequency_refined_material_envelope_so3_report.py`，实际 SHA256 为 `bc0c2c64d4f512fe4a42711e1b0f91ef4496a03a7b1d969c27febd5476c3f2eb`，98804 bytes。相对已锁 e244b835b4550e427a6ccba6652cb2e211ef3b79b03effe073b53227a56c8c6f，唯一文本差别是顶层 DRIVER_SHA 从原 d43fe4c8ba89ada7067a360d75688fcb10f242b3b7b1e491b332f34b789a38ca 换成当前完整 driver：

`6a900861c01d0967dc585dd84797cc2428b62bd4a5969d594a68387c7a0175be`

该科学 driver 为 79,670 bytes，云端完整 blob `1c5eff9c52b705e20e889b5d02883f1d2cb969bb`。这不是只重标签旧报告：纯读取仍先验证实际整个 driver 文件、全部实际 SOURCE_PINS、报告 schema/source，以及原模型、目标、范数、参考、校准、18 个 Q 字、完整 permanent/typed 记忆和全部真实扫描、root snapshots。它不会接受旧 d43 报告冒充当前来源。

当前同型完整纯源派生器仍为 `derive_frequency_refined_reader.py`，11595 bytes，SHA256 `176fdb95374e03657516fd722bb00c41ec455170f9b686d5fe0080b412a59195`。相对 c87b8880fd3fb968ca022d506a60d46f8b5f65fcbe90e00fa95c2d0edc09e897 也只换同一个 DRIVER_SHA。它继续从完整 c0cc 父 reader 逐段生成全部新体，保原 AST 差异集合、重复键、完整文件长度和 verify-existing 检查；没有删旧校验来适配本次输入。

## 2. 当前 transfer 与 pure 交界的完整核对

本次定点静态审已读取新的完整 transfer：

`b8ac67ee7e2a9f972b4c8377dd49e925b9b178937f47049b17989dc7c767c2c2`，65,540 bytes，blob `3d931e4ecf2ba27ca28fbc0689a60036f168a6c1`。

对应独立 layout 为 `ce188ae4bdf1ccecfbf9549897284e8dc44f4722e04e974c7a0cd045c78a3a27`。这些来源均从新 driver 的真实完整 role 表读入，不让原 e244 内部暗钉旧 e6fb 或旧 0c0d。

核对到的接口事实如下：

1. `_input_identity` 仍要求原 reference bundle、实际 carrier、symbolic node report、scalar input 和完整 preparation report 为同一真实文件；完整 N/J、正权测度、谱损失、reach safety、五项幅度预算和旧 norm 定义均独立核验。实际 reach ratio 路径为 `final_geometry.source_binding.reach_ratio`；最终 transfer 已使用此嵌套路径，未沿先前候选错误顶层路径。
2. `_compatible_models` 逐字段核旧完整 M160 参考、新 M320 当前空间、原 fixed seed/chart/scalar/radial mesh/18Q/gamma/公共 normal partition。仅将已声明的来源与频率 layout 字段规范化后要求其余完整定义相等。新增坐标不是新冻结参考，旧 norm/浮点 field/连续证书不被继承。
3. `seed_from_complete_prior_final` 从真实完整 coarse report 与 NPZ 重新组装全部原 free core、三路 rotation、H；新模式归零但全部变自由。三路 161/161/160 个原 angular slots 分别落在新起点 0/321/642。原完整 core/H 字保留；父 final metadata 和 final geometry 的点摘要须与原重组坐标一致。
4. `validate_seed_metadata` 的接口仍是 `(value, *, report, model, transfer)`。第一次 M320 需要 `actual-complete-parent-zero-inclusion`、真实 coarse report/checkpoint、原 parent driver/model/norm、全数组摘要、当前完整点和 layout inclusion；它把新初场重读作为责任而不声称已完成。
5. `validate_metadata` 保留 uncapped typed 前缀、全部三角色地址 fingerprint、每个来源报告/ordinal、已知保护标签、未决并行责任和 actual parent families。新 memory source 是旧 complete envelope 或当前真实 restorer 变体时都必须与实际 report/source 对应，没有未知 typed 排序的伪造。
6. driver 写出的 `frequency_refinement`、`prior_envelope_final_variable_seed`、`initial_full_variable_point_sha256`、`actual_reference_initial_full_point_sha256`、`frequency_layout_source` 与 reader 完整调用相同。fresh 的 `new_zero_closure_seed_changes_physical_field` 是真实 `None`；它没有仅由零嵌入就推导所选隐式 branch 的浮点整场相等。same-source restart 为 `False` 并严格核自己原 source/model/norm/final。

在 pure 入口中，完整 source role 校验之后仍按原顺序执行 material envelope validator、transfer metadata/seed validator、独立 layout validator，然后继续全部模型/base/reference/scalar canonical 闭包。两个新增纯 validator 的真实代码文件均由完整 role SHA 核验；没有导入或执行科学 provider。

## 3. 检查与未做事项

本次执行环境不可用。已经实际完成的是云端完整源读取、唯一字面替换、全文替换可逆等号、完整文本 SHA256/UTF-8 bytes 核验，以及上述源接口静态核对。**本次没有执行 AST、compile、派生器、科学程序、F/J、root 或新的数值 fixture。** 原 e244 先前已实际通过的检查仅属于原版本，不改写成本次检查。

完整派生器的可执行检查仍保在新源里，供恢复后的纯 stdlib 源复现使用；它不是新场的科学前门。本条没有任何实际 M320 方向、精化收益、误差付款、连续 branch 唯一性或全题完成声明。真实来源报告若尚未返回，参数只能记录待消费路径，不能预填其最终 SHA 或 root/geometry 读数。
