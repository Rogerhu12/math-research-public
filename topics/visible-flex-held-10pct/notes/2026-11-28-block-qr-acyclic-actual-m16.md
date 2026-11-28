# 完整 QR 包装器的因子即时释放：真实 M16 矩阵核验

原 `prefix_block_qr_driver.py` 把捕获 `result` 的 `apply` 写回 `result.solve`，形成 `result → apply → result` 引用环。原资源入口在刷新前执行 `factor=None`，但这个环使旧因子要等循环垃圾回收才能释放。原 source 保持原字节；新独立 `prefix_block_qr_driver_v2.py` 返回只持有 `solve` 闭包的 `SimpleNamespace`，不再写回 factor。引用变为单向 wrapper → factor。完整 BlockQR 数值核心、原矩阵、所有非线性门与日志统计均未改变。

真实核验复用 `held10-linear-work/actual-m16-check` 已保存的完整原 collocation J 与 residual。矩阵为 43087×43087；未重新生成小模型或删行。先调用同一 factor 的原 solve，再调用新 `wrap_factor`；两个完整方向逐位相同，原矩阵残差最大为 1.066670079402443e−20。保持 wrapper 时 factor 的 weakref 有效；禁用 cyclic GC 后先删除裸 factor、再删除 wrapper，weakref 立即变空。实际 wall 2.938712194 s，maxRSS348416 KiB。

数值与对象寿命检查的完整参数、输入/源 SHA 和原 solve 统计在[实际记录](2026-11-28-block-qr-acyclic-actual-m16.json)。再生原完整矩阵使用已登记 `check_block_qr_cached.py` 的 M16 命令；包装检查的核心为：

```python
factor = BlockQR(matrix, n, nodes, k)
baseline = factor.solve(rhs)
wrapper = wrap_factor(factor, event, 1)
assert np.array_equal(wrapper.solve(rhs), baseline)
reference = weakref.ref(factor)
gc.disable()
del factor
assert reference() is not None
del wrapper
assert reference() is None
```

这是具体内存滞留结构的修复及真实线性方向检查，不证明此前 exit137/−9 的终止原因，也不是新 BVP 接受或几何结果。后继 V5 设计入口可显式选择该 v2；当前仍活跃的旧入口不被改写。
