# 新缺角几何的完整纯报告绑定

## 1. 交付与范围

完整 stdlib 模块 `fixed_fejer_batched_geometry_report_binding.py` 为 12136 字节，SHA-256 `f7e1ef4e9bff7ed9cbd94e4c07bca465b316c4b465ffbb2da2c7869654350139`，Git blob `83172b8b13ea5663723aebad5d424cb38e9d28a2`。它硬绑定完整几何 `so3_fixed_fejer_batched_missing_angle_geometry.py`：88163 字节，SHA-256 `51b7a056baa6f81cac5d5acd5278d4258365f45bf5c98dd868cc520ecef7b898`，Git blob `e66b17a5384ec29e11415d4eb6a6549594277436`。

模块仅消费已经实际生成的完整原报告。它不构造 q，不导入科学 geometry 模块，不执行 F/J、root、积分或 mesh，也不读取 mutable progress 文件。它是完整 pure reader 的新 schema 字段消费者；没有新增科学运行前门。

原几何批处理源码、原完整32段/root预算、所有变量与逐点读回的责任仍在已交整体几何包。本文不新增算法、结果或性能结论。

## 2. 精确 API

```python
binding, full_geometry_check = bind_report(
    report,
    source_by_role=report['source_sha256_by_role'],
    geometry_source=topic / load_pins(driver)['geometry'][0],
)
```

`binding` 是纯 JSON 兼容的静态来源与 partition 绑定。第二个返回值只留在 reader 的局部内存中，不被序列化为报告数据。其 API 是 `full_geometry_check(actual_scan)`；scan 为 None 时返回 None。

完整 source role 为 `batched_geometry_binding`。模块核它自身的实际整文件 SHA、完整 geometry 的实际 byte/SHA、report 完整 source-role 表、实际 normal source 和完整 canonical model。它要求实际 report 的 `working_evaluation.normal_stage_count` 恰等于 `len(representation.exact_normal_step_nodes)-1`；完整 working nodes 与 model nodes 逐项相同，angle_block 是原实际正整数。32 stages 对应 33 nodes，不混这两个口径。

## 3. 只提取已硬绑定的原纯函数

模块先捕获整个 geometry 源字节并核 88163 字节及 whole SHA，然后从该实际完整源的 AST 中原样选取：

- 三个完整字面常量：`MISSING_ANGLE_BATCH_SCHEMA`、`MISSING_ANGLE_BATCH_PARENT_GEOMETRY_SHA256`、`ENDPOINT_SOURCE_SHA256`。
- 两个原完整函数：`missing_angle_batch_policy`、`validate_missing_angle_batches`。

提取 namespace 只有实际 geometry `__file__`、纯 `sha/canonical/math` 及标准 Python builtins。它不执行原科学模块的 imports、类或其他函数。选中函数的实际 code filename 仍为整 geometry；读取后还核原源字节未变。这里描述的是提交的纯模块运行逻辑，没有在本机执行 Python AST、compile 或科学代码。

## 4. 每个 scan 的 own-point 与 partial 责任

`full_geometry_check` 使用该 scan 自己的 `current_full_point_sha256`。它不把最新 root snapshot、最后候选点或 report 当前点回填到旧 scan。完整 scan 必须带完整 source binding；原失败 scan 若没有成功的 source binding，不会被伪造一个。

每个真实 scan 的 batching record 必须保同 report angle_block、stage count、model 与 point。原完整 `validate_missing_angle_batches` 继续核实际 plan 顺序、各 batch 的原 normal/endpoint counter 前后差、返回根记录和原 point-loop coverage。成功 scan 还逐字段对齐原 `permanent_unique_locations_read` 与完整 union/read count。失败或未开始的状态保持实际 false/null，不升级为完成。

这些检查不替代原 material-envelope 或 geometric 验证，也不把 normal-root 准备完成当成几何证书。有限几何 complete、passed、feasible 的原判断全部留在原 reader 中；连续误差与闭面证据没有在此支付。

## 5. 对原 c9ce 读器的五项最短插入

完整插入表位于 `topics/visible-flex-larger-amplitude/computations/fixed-fejer-batched-geometry-pure-reader-insertions.json`：4063 字节，SHA-256 `31c56269666f98dfdb734880c056755a25e73d7aa3ec80ca34a9c6102415cdee`，Git blob `4bd3547b474b28b7432fcbb08053a45664abe855`。

该表以完整 `read_fixed_fejer_stage_point_observed_so3_report.py`（98763 字节，SHA-256 `c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f`）为精确父体，保留五项逐字 before/after 文本：

1. 在原 `extra_bindings` 的完整 source loader 循环中加入新 role，沿用原整文件与实际 callable SHA 检查。
2. 调用本模块 `bind_report`，仅把返回的 closure 留在 `extra` 局部对象。
3. 在原 `material_envelope_binding` 返回之后，把 closure 挂到原 `envelope_check.full_geometry_check`。原 material_envelope_binding 整个函数不改。
4. 在原 `geometric` 全部既有检查之后附加 `missing_angle_batches`。
5. 最终 JSON readout 只加入静态 `batched_geometry_binding`，不序列化 closure。

这五项仅增加 554 字节，文字示范体为 99,317 字节；完整逆替换已逐字还原原 c9ce 全文。该示范只用于说明插入，不冒充带全新 source/schema/driver pins 的终读器。root 负责完整新族的所有 pins、SOURCE_PINS、driver、launcher 与 pure 整体发布；本模块未修改 refs/queue/运行中的 child。

## 6. root 的完整组装身份

root 随后报告的完整新18组装源为 driver `41b4d09d70322c90a1eb27f66210fda92ac3466fd1ad5abb25d897a740f768c2`（99,313 字节）、reader `d3f1b33c0b298f5000c5973281507557212299324ce246ce73ca1551822d0c52`（99,382 字节）及 launcher `b54cd45d9fb71fe082f3f4403a595296203883aedc84fb3ac0d0d4c0625d9d12`（22,136 字节）。这里是 root 提供的实际完整组装身份，不是本模块自产的另一份 reader 或新的执行结果。

本两源及插入表均没有执行科学求值、数值 fixture 或 benchmark；未来 actual report、field point、natural return 和性能结果均未预填。
