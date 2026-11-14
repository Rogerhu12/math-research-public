# 原配点/平衡QR的磁盘存储：小型等价检查通过，未接生产

作者：root（GPT-6 Astra Pro，AI-assisted），2026-11-12。

完整强前缀同问题谱加密会增长每个节点的dense块。`root_disk_block_collocation.py`保留当前`root_block_collocation.py`的全部配点公式及原balanced orthogonal elimination，只把完整A/B/C和每个内部QR节点的qr/tau/top块按原float64字节写入匿名临时文件。逐径向batch写入原Jac；每次QR只读本地所需块。右端前后遍历直接继承原`BlockQRFactor.solve`，不改方程、线搜索、参数或验收门。

内存保留一个Jac batch、平衡递归的对数个coarse块及完整求解向量；磁盘量仍随nodes×state_dimension²增长。匿名文件在对象释放时关闭，不提交可重做的大型中间矩阵。仅支持原实float64。没有声称磁盘改变计算复杂度或已解决所有资源风险。

`root_disk_block_storage_check.py`的r2正式exit0：三组非线性实配点覆盖有/无参数、差分/解析状态导数以及两节点退化树；全部A/B/C、边界、matvec、单/多右端QR解均逐位相同。另与原稀疏矩阵直接LU比较，最大相对差2.01e−15，最大后向残差5.81e−15；文件描述符均释放。wall4.8615秒、峰62220KiB。

r1正式exit1的历史resource保留：原存储类在k=0且省略bc_jac时把SciPy返回的None当边界参数矩阵，触发原matvec错误。r2在同一两份实现中显式提供合法的空边界参数矩阵；没有修改正在运行的生产代码。实际课题k≥24，不属于该合成测试分支。

当前没有安装这个后端，也没有比较实际q095/q105的完整Jac。下一使用前应在真实同一保存态与原块结果核对，明确记录新增源哈希和后端；原全场RMS、physicalBC、真实tail/full audit全部保留。旧变分缓存、实际M24和强分支14476完全未改。
