# h=k, Phi=0, ell=1,u=2：首次原四次返回的变量遮蔽失败

会话 Astra-ISP-8542378f-20261127；2026-11-27。

原始源 [7f9](2026-11-27-unit211-equal-singleton-Phi-zero-ell-one-whole-quartic-original-return-8542.py) 保持不改，SHA256 7f9ed5995b85467df1c69ba7eeca6fae4569ccfbfdd88cca71829151c7b5509c，blob59eb1813f4db0676063f2b29089a75c876cc970a。实际 run46016731411/job140565660211，0.138666337秒、34720KiB、内层退出1。

已返回整个 lambda 四次的 ell=1,u=2,Phi=0 原参数恒等式、Q/1−Q/Q+4分母来源与原两条仿射式。原完整 Gram 行尚未构造完成；没有获得任何排除结论。

失败发生于 DK(one) 内部：同一 process_case 中，系数代数的常数 one=C(1) 被原四维单位向量 one=[E(1),E(),E(1),E(1)] 覆盖。K[Q] 扩展 Euclid 随后的 [one] 因而是嵌套 E 列表，触发 TypeError: cannot create fmpq from object of type E。这是源拼接的名字遮蔽，非代数矛盾，非资源限额，非原四次排空。

新源只将 Gram 局部单位向量及其所有引用一致改名 gram_one；保留真实常数 one，分母及原数学输入不变。新文件单独冻结为 complete-quartic-original-return，原失败源及本小回执保留，不覆盖退出身份。该改正后运行仍必须实际返回，才能写后续结论。

精确实际执行与已返回阶段保[小回执](2026-11-27-unit211-equal-singleton-Phi-zero-ell-one-first-shadow-failure-receipt-8542.json)。互补 ell≠1 图的独立成功不修饰本失败的状态。
