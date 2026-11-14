# 原 M28 几何参考的直接恢复（2026-11-13）

状态：恢复检查已执行；完整物理后处理仍在运行。这里没有新增曲面或闭合声明。

旧 `r2-tail-ready.json` 没有归档，本执行器也没有旧临时目录。所需 M28 几何参考其实已在原成功求解的 `2026-11-12-strong-q096-sameg-m28-local-recovery6-r1-actual28-tail-response_adapter.json` 的 `stored_metric` 字段中完整保存。它的 `physicalParameters.modes=28`，前后七分点 profile 指纹相同，并包含 160 层原校准、全 warp 和原完整物理参数。原 60 件文件的大小与 SHA256 本次全部通过。

本次仅把这个已存字段原样放入 `storedMetricAdapter` 键，另附提取来源；没有伪造遗失的 ready 事件、路径、内存值或旧 SHA。新参考文件是 `2026-11-13-strong-m28-recovered-original-reference.json`。原 `root_actual_staged_tail.py` 会再次由真实 M28 工厂构造新 ready，检查全部原物理参数、全 profile 指纹和 warp 后才发送完整 28H/J/audit 请求。

此恢复保留原 M28 成功 raw、全部五组数组和原 28H，prefix Newton 调用为零；所用 91 份固定物理源码取自原提交 `869436630c99aa5a68afb55bd8877c826034d117`，总计 866846 字节，逐项对照原 manifest。旧 MJS 和原数学程序不改。

原 `strong_sameg_m28_cache_snapshot.py` 固定要求遗失旧 ready 的精确 SHA，不能用于这个新生成的参考包装。当前机器可直接运行原完整 J/audit，因此先运行原 `strong_sameg_m28_staged_audit.py`，不以缓存诊断代替实际计算。

复现入口：

```sh
python computations/strong_m28_saved_reference.py --out notes/2026-11-13-strong-m28-recovered-original-reference.json
```

该入口已实际运行，完整原存适配器 SHA256 为 `d948afb8049924291354e360d72530e45af0f604470fb6ff0533f36f886a1cba`，本恢复参考 SHA256 为 `ae86e3a7036b3e1b7eb4e07677dc209cd5d092e778c1872c4581f435750ee5a5`。绝对来源路径改变时包装的 SHA 会改变，原 `storedMetricAdapter` 数学内容不变。
