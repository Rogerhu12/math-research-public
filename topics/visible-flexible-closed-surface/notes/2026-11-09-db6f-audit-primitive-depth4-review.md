# 深度4背景原函数包的全量独立重放

2026-11-09，independent_geometry。**PASS。**

使用已经审查的 stable primitive 方法、相同实际 checkpoint、有限 calibration 表、紧 alpha、A0、inner A、B0–15 输入，独立重跑 depth4、order8、density10⁻¹⁰ 到 `2026-11-09-db6f-audit-primitive-stable-depth4.json.gz`。

作者文件 `2026-11-09-db6f-tail-background-primitive-stable-depth4.json.gz` 的 SHA256 为 `28577da04035f91bcd5dc310094d5844347cbeb78d6213dcba0232b62acf56e9`。

比较完整 JSON：raw0–3 的36个 profile 及其全部叶逐字段、逐值相同；所有 inputs、sources、parameters、alpha、状态与 scope 也相同。差异仅为 settings.out 和耗时。先前已审的 raw0/1 方法没有改变；新包把同一已审算法的覆盖扩展到 raw2/3。

本次没有以相同输出单独推导算法正确性：解析叶/范围叶、强锚与部分原函数余项仍采用已有方法独审；此记录补充实际36个 profile 的完整独立运行证据。它提供后续局部 w 包的源输入，不证明任何有限扰动的 metric 或实际曲率。

完整机器比较与作者/重跑哈希见 `2026-11-09-db6f-audit-primitive-depth4-review.json`。
