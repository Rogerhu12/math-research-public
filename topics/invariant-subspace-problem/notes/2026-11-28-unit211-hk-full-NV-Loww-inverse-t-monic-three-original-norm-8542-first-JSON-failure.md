# HK 完整 NV–Loww：首次 JSON 类型错误与同输入工程修复

日期：2026-11-28。会话：Astra-ISP-8542378f-20261127。

唯一首次 run46159596374 / job141023709190 的真实内层为 **exit 1**，2.457205909 秒，峰值 61528 KiB。它不是资源触界，也没有发生数学断言失败。

源 e9bd30f0ceb6c2b123a0c4a2528b99b73a6f3ac2 的 SHA256 为
25d3ea3e3726b88a6cf5c831aa0228923226fab6c01d12d2e3a4fb0c2b97b8c2。
source commit 与实际 pull 后均为 2c12a08a06949ed99cb68ac4560efa6008145743；
pull UTC 2026-11-28T15:23:26.074454+00:00，两份规则未变。

明确输出的唯一数学 checkpoint 在 0.095850844 秒：完整原 NV 对同 t 的一次式、完整 Loww 三次式、已付常数项和
$$
tv-1=-Loww/c_0
$$
均已返回。

程序随后在 line183 调用第一个 Norm profile；pp 的 line81 把 FLINT 的 fmpz 指数直接放进 JSON，报
“Object of type fmpz is not JSON serializable”。只从 traceback 所处位置可知，源码此前的三列乘法、三个伴随坐标和完整多项式 lift 断言已经越过；它们没有单独输出的新 checkpoint 或系数摘要。这里不猜范数次数、因式或后续权支持。

完整两原式回代、清分母、实际乘子共同因子取消和最终权支持尾段尚未执行返回。stdout 为 2114 字节，SHA256
ed623f8e621142ed75f985e9f45190c9ae41ae8bd96b663da62d9b6d3f749e39。

根已核实际日志并授权修复同一未完成输入。修订仅为 pp 中两处显式 Python int 转换：

- 规范指数序列改为 [int(e) for e in m]；
- profile 的次数序列改为 [int(e) for e in p.degrees()]。

数学定义、所有断言、唯一必要前缀、180 秒/4 GiB 及外层 195 秒预算完全保留。这不是另一个数学目标，也不是重开旧 dc888 投影门。旧源与本次失败身份不改写。

修订源 SHA256：039f4dd37cbe91d03c12465c62b637f177fee7bf227b39e9335833ddd3f52fda；UTF-8：10014 字节。源 basename 仍为
2026-11-28-unit211-hk-full-NV-Loww-inverse-t-monic-three-original-norm-8542.py。

本记录不记修订源成功，不给新权曲线、有限性或排空结论。
