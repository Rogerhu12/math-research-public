# 完整物理点采样未决范围：独立必要 reader 接口

作者：ChatGPT（AI，exact_refinement）；2026-11-16。  
本件由 geometry 统筹 R476/R477/request212 使用。只修必要元数据选择和真实 reader 来源，不改变任何已发布入口或科学算法。本地仅文本读取、精确替换、diff与字节身份；未执行、导入、AST、编译、测试或重算科学。

## 1. 已确认的原写入与丢失路径

真实采样器 `geometry_20261115_current_C_pruefer_joint_radial_sampling.py`，SHA256 `32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4`，在 `InverseSampler.sample` 的异常分支真实保存：

`kind="actual-current-C-physical-point-inverse"`，以及下列八项：

| 原键 | 原语义及本次保留方式 |
|---|---|
| point_index | 原实际待返采样点序号，直接保留 |
| radius_word | 原真实半径字对象，直接保留，不重算十进制或逆像 |
| role | 原调用用途字符串，直接保留 |
| actual_error_type | 原异常类型名，直接保留 |
| actual_error | 原完整异常字符串，直接保留 |
| all_pending_closed_fragments | 原全部待处理闭片对象，保持顺序、全部端点、source panel/piece和depth |
| retained_original_leaf_rows | 原已写叶账的first/stop，直接保留，不冒整点完成 |
| complete_point_not_returned | 原布尔值，不由计数推断 |

原代码会先把尚未提交的 `in_flight` 放回stack，再按 `reversed(stack)` 保存全部pending；每个地址对象含 `original_source_panel_row`、`source_piece`、`closed_parameter_interval` 和 `depth`。原first/stop对应当时叶账行区间；它不表示该点已完成，正由 `complete_point_not_returned` 明确区分。

旧必要base为：

`root_20261115_current_C_pruefer_joint_full453_necessary_readout.py`，55,181字节 / `19878e48ed25dec8bdcbd36c3d7ea7168796a08fb60675ad7455dbb296a0918c`。

它的 `unpaid_view` 白名单没有八项，所以即使原 `complete-unpaid-scope` JSONL完整读取且hash核对成功，这八项也不会进入 `complete_necessary_unpaid`。旧摘要把stream身份保住，不代表必要失败定位已全部输出。

原205双阶段reader：

`root_20261116_actual202_accurate_ten_two_phase_necessary_readout.py`，29,882字节 / `80c26207dea0d393a102dabba9f1e5ed9580460cc40876d2668975ae9499af1f`。

其 `sampler_view` 调旧base的 `sampler_readback`，随后仅 `dict(full)` 并去掉成功general-row大表；没有再丢这八项，但上游已经没把它们返回。因此这是确定的选择遗漏，不是原采样器没写、不是真实逆像已消失，也不是数学域反证。

## 2. 两个最终新源

| 角色 | 新basename | bytes | SHA256 |
|---|---|---:|---|
| 原采样/native必要API | `root_20261116_current_C_sampling_scope_necessary_readout.py` | 55606 | `47d7ec771331f417dffb783a79e02d1ae9720e9ad0a699a72c37cf3031718cb2` |
| 原205同候选双阶段必要入口 | `root_20261116_actual202_sampling_scope_two_phase_necessary_readout.py` | 30114 | `6e40dc6365246113d8abc07110582a030b4930195070a71ba08e9872a11bb1e7` |

本地目录：

`/workspace/visible-larger-working/current-C-sampling-scope-readback-R477/`。

两个运行源各有 `.complete.diff`，相对上述真正已发布19878和80c2基线。它们不是对正在运行205/207/209的原位修改。

新base仅做这些改变：

- 新basename、独立schema和独立输出帧/事件；
- 在原 `unpaid_view.keep` 中增加八项；
- 直接复制八项的原值；不经过 `small()` 的列表16项限制或字符串前缀缩写；
- 注释明确全部pending地址和原leaf span必须保留。

原所有mode/native/trace/trial/FD/far单位行选择、输入身份、原float字词校验、原错误处理及90KB界不改。其他成功大矩阵/原科学数组仍只返回原身份；没有借此输出大科学树。

新outer实际把 `BASE` 与 `BASE_SHA` 指向新base，经原 `load_reader` 真正导入该metadata模块。它的PINS仍保留旧19878作为明确祖先，原八项来源均未删除；加上新base成为九项。没有执行旧base后猴补其全局函数，也没有在回执中只改来源名称。

以下原科学来源原样保留：

- driver `geometry_20261116_actual202_accurate_ten_full453_frozen450.py` / `56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615`；
- launcher `geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py` / `227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7`；
- candidate `geometry_20261116_actual202_accurate_ten_candidate.py` / `ee3675ce3465930f2ce32283a468f5fad464639ca6ccda6352f027f00f0c6c38`；
- 原5400 joint双阶段层、62010 hooks、3bc profile与43f checkpoint。

## 3. Schema、帧和实际调用

### 3.1 新base

Schema：

`current-C-complete-physical-point-sampling-scope-full453-necessary-readback-v1`。

独立调用CLI仍为：

`--launch-directory --sampler-directory [--sampler-result-sha256] --computations --out`。

新base的独立输出帧：

`BEGIN_CURRENT_C_COMPLETE_SAMPLING_SCOPE_BVP_NECESSARY_SUMMARY`

`END_CURRENT_C_COMPLETE_SAMPLING_SCOPE_BVP_NECESSARY_SUMMARY`。

双阶段outer调用其函数，不调用这个base的main；因此212正常双阶段回执只有下一节outer帧，不重复打印base帧。

### 3.2 新outer

Schema：

`actual202-complete-sampling-scope-ten-two-phase-necessary-readback-v1`。

CLI逐项不变：

```text
--launch-directory ACTUAL_BVP_LAUNCH
--sampler-directory ACTUAL_CURRENT_GEOMETRY
--sampler-result-sha256 ACTUAL_RESULT_SHA
--candidate-binding ACTUAL_R449_ADAPTER_RESULT
--computations ACTUAL_COMPUTATIONS
--out FRESH_SIBLING_READBACK_DIRECTORY
```

采样result缺失时原optional SHA参数可不传；原缺失范围逻辑不补造成功。所有路径仍受原RUNNER_TEMP所有权和同run/source身份约束。

新outer帧准确为：

`BEGIN_ACTUAL202_COMPLETE_SAMPLING_SCOPE_TEN_TWO_PHASE_NECESSARY`

`END_ACTUAL202_COMPLETE_SAMPLING_SCOPE_TEN_TWO_PHASE_NECESSARY`。

事件名 `actual202_complete_sampling_scope_necessary_summary_identity`。它们没有旧REQUEST205标签，也没有伪造实际新run编号。GitHub outputs仍是原三键：

- `bvp_summary`；
- `bvp_summary_bytes`；
- `bvp_summary_sha256`。

文件仍为 `scalar-summary.json`、`necessary-readback-index.json`、成功时的 `readback-complete.json`；marker schema仍准确等于本新schema加 `-complete-marker`。

212编排需要真实替换 `current_BVP_readout` 的basename/bytes/SHA、保旧原pin并新增两新pin、更新读回后schema断言、report两帧及任何直接核旧schema的清理消费者。科学driver/launcher/candidate/原预算不动。仅替文件而忘记schema或marker消费者不是完整接线。

## 4. 205 / 207 / 209 全链的已核范围

| 真实路径 | 是否存在相同八项遗漏 | 源码依据 |
|---|---|---|
| 205首个current-C采样→80c2双阶段reader | 是 | 80c2实际load19878；其unpaid_view白名单遗漏 |
| 207首个205子合同采样 | 是 | workflow读取真实dispatch-request.current_BVP_readout，仍为80c2；首链科学块沿冻结205 |
| 209首个205子合同采样 | 是 | 同一冻结205读回合同；后置union没有替代首采样 |
| 207/209后置R456真同far新网格 | 此处不丢这八项 | R456 reader `same_far_sampling_view` 对complete-unpaid-scope整原行json.loads并放入complete_unpaid_records |
| 207后置R457完整M采样 | 存在独立同型遗漏 | R442 M API `22923f449d363543169446eb970c78f0aaa7410648df4ebc02cd7fd6fafc96c1` 的unpaid_view仍是旧白名单；R442 phase和R457保留该返回 |
| 209后置R462/R464 union采样 | 该整行路径不丢八项 | R462 readback对complete-unpaid-scope使用selected=None，全部原行进入complete_unpaid_records；R464实际返回complete_original_necessary_scope；209未对其内部pending再选白名单 |

207与209最外层 `solve_view` 对R456的 `original.complete_unpaid_records` 是原对象直传。对完整M API返回的不含 `original` 的sample，它直接保留sample；这不会恢复M API已经丢掉的八项。209 union返回也不含同名 `original` 分支，完整原necessary scope被保留。

这张表仅是明确源码路线结论，不据源码把未实测的分支写成已发生的失败，也不替任何运行补字段。当前两新源针对212原205首链；不会自动修已冻结207的独立M API。若后继需要完整M同型修补，必须给M API及真正phase/owner reader依赖新的显式来源闭包；不能把112 API换名冒动态M来源。此次不改这些既有源。

## 5. 90KB、未完成与清理

新增的pending项是原必要地址：panel、piece、闭区间端点、depth和原已写叶span；不是成功区间矩阵、逐角数组或完整科学树编码。

它们全部保留后仍执行唯一90,000字节检查。没有上调预算、没有分页、分片、编码或截断后返回成功。若必要摘要超限，原outer保：

- `complete_necessary_readback_without_recorded_error=false`；
- 原完整summary的bytes/SHA；
- 原temporary index身份；
- `cleanup_marker_not_written=true`；
- `owned_raw_retained_until_runner_destruction=true`；
- 返回70。

如果存在读回错误，原返回2和未写完整marker范围保持。科学是否接受只由原solver门决定；传输未完不变成数学拒绝，也不能被外层当清理授权。

## 6. 来源界限与交付

两源码生成只用了两份精确冻结基线和明确字面替换；完整diff与最终实际文件字节一起交root/geometry。原写入者和各callee只读，不改其source/schema。本文没有运行新reader、没有制造point错误fixture、没有从旧run日志恢复未输出的pending列表，也没有预填下一run的point index或半径。

这次修补的责任是可执行的字段保全：未来真正同job原采样器写出这些八项时，新outer会通过新base将它们全部带到同一必要摘要；原完整science、原所有门、原资源与原quiet后清理合同不变。
