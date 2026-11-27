# 碰撞剩余 E 曲线：固定 u QQ 结式的首次超时

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

新源 [2026-11-28-unit211-collision-remaining-E-fixed-u-original-QQ-projection-8542.py](2026-11-28-unit211-collision-remaining-E-fixed-u-original-QQ-projection-8542.py) 的唯一实际运行是 46056479321 / job 140700095041。源 blob 612cb5b34d68c081be461abfb0f747366c07c6df，SHA256 ba42a1359c72f65434457327001761cef9a91ba62d1fd5b1fd6d84df757e63bb。

实际内层 180.068846732 秒，峰值 104532 KiB，退出码 −14（SIGALRM）。预算是 180 秒 / 4 GiB，没有抬限或换进程重试。外层 job 失败，不能记为投影完成、结式为零或数学反例。

已完成的前段只有两份已保存原 E 因子的准确加载与 primitive 整系数乘回：

- E177/18：3338 项，整数分母和 content 均为 1，0.023199731 秒。
- E182/19：3621 项，整数分母和 content 均为 1，0.048478825 秒。
- 0.048565597 秒进入固定原 u 次数 18、19 的 37 阶 QQ Sylvester 结式。

此后没有结果式返回标记，没有任何真实 lambda 因子剥除，没有平方自由 lambda 覆盖，也没有新参数载荷。源码中这些后续步骤没有执行到，不能依据它们的预备代码填补结论。

源提交 350aa64980e7bb55bddd5e60b06f615c7d3dd360；2026-11-27 19:24:45.820647 UTC 的实际 pull 前进到 6af8dabc213ae32d6ef023f9b2b2fffffd8bd27d，两 README blob 无变化。stdout 1008 字节，SHA256 a1deb2b22274706c097b8afc26812e44d0bf92294ac8a7fe3712aa349f3e05f9。

[完整小回执](2026-11-28-unit211-collision-E-fixed-u-first-timeout-receipt-8542.json) 保存全部三条真实数学记录与执行身份。此门冻结，不延时、不改算法重跑同一结果式。此前两 E 交点与首一 Q 六次给出的有限五坐标环境维数不超过 235170，保持原证明；所有完整原方程仍须继续。

下一不同原输入转到两 E 的原 u 首项、lambda 无穷远主部及它们各自的整有限头纤维；只使用已有完整系数，不能把未取得的完整 lambda 投影当作输入。
