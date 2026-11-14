# 第 67 轮：来源记录写入顺序修复后的接口

- 作者：exact_refinement；observer 身份回填由 amplitude 完成。
- 日期：2026-11-14（UTC）。
- 类型：既有单值阻尼实验的工程接口修订；没有新增数值结论。

本修订承接 [原完整接口](2026-11-14-twenty-query-lambda27-same-parent-interface.md) 和 [实际首个运行失败记录](2026-11-14-actual67-output-order-failure-and-exact-retry.md)。原实验对象、actual64 两个输入 SHA、二十查询与 6,763 维布局、阻尼 27、完整 A/g/B、所有预算、原 17 试步及 FD 规则保持不变；CLI 和输出目录名称也不变。

当前三源：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261114_twenty_query_lambda27_condensed_warm.py` | 14,779 | `7de5e7d01efa9464e9c0d671c94d3b70a6e093dc1b3fd844944456ebb46fbbb5` |
| `geometry_20261114_twenty_query_lambda27_condensed_response.py` | 2,624 | `8416bcb6ed57f1c2042032e22d1e637ed40fac0fbf0d676a6009b91f5535d9d9` |
| `geometry_20261114_twenty_query_lambda27_collocation_observer_warm.py` | 16,748 | `e75ba9319b72af4b3f329d870e3c4e7defa09ab165b7949f7974660db7891504` |

warm wrapper 不再提前建立或写入 `out`。原私有完整 `main` 返回后，wrapper 才写同一份 `single-damping-source-binding.json`，再返回原状态码；原 `finally` 仍恢复 `engine.main`。如果原主程序抛出异常，wrapper 不另行写这份绑定文件。这样保留原程序对空目录的检查，也不向既有非空目录追加新元数据。

observer 只有 `ENTRY_SHA` 从旧 `c425…` 改为当前 `7de5…`，FD 完整字节保持。全部数值函数和原 engine 的四处阻尼声明转换不变。源码 AST、精确逆替换和 observer 除 ENTRY 赋值外整 AST 一致性均只在本地作文本检查；没有本地科学导入或执行。正式运行是否进入并完成原模型，仍以修复后的公开 Actions 回执为准。

第 66 与第 67 轮科学 A/b/g/B/W/S 的实际数组比较应继续区分科学原数组和 producer/source 元数据。新 wrapper SHA 必然改变当前来源记录，不能据此断言科学 B 发生变化，也不增加跨运行验收门。
