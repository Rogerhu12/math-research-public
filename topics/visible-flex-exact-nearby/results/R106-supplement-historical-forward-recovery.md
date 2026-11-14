# R106 续篇：原550段完整前向参考已按历史哈希重建

2026-11-13，visible-exact-astra-ac0d。

**状态：恢复任务已经实际完成，未改变历史参考对象。** 原始1032条角射线的 DOP853 计算真实运行，接受550段、10770次右端调用；随后重新生成原 ±516 Fourier 的全部 U/L 多项式和 retargeted Q 多项式。整个原生进程退出码0，总实时时长约1646.32秒。

`notes/2026-11-13-historical-forward-reference-cache-recovery.json` 保存完整70个文件的路径、大小和历史SHA，以及两个原manifest SHA。所有35份原始射线、23份 U/L、12份 Q 的字节SHA与历史记录逐一相等。根进程又独立逐文件重读并核实了该报告中的全部70个SHA，没有只读取成功标记。

两份完整manifest的SHA为：

- U/L：`43cbffb2e0b924b6d69608df54e0acf3cf8ecd66c030b7343e84864ad6eb81a0`。
- Q：`f1e7556a13aef2a4e5661fc00c1e9c4eda961335fb8685d26bcef550b7b147ce`。

运行未改动已经提交的 `scripts/fourfold_ci_forward_reference_bootstrap.py`；原生源码SHA为 `bcf9fe92ef39f2a2754dbe05c76818537b7931e5e8b8c0ae83dcb1971460b5b1`。环境准确版本为 Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0。可在本题目录重放：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_ci_forward_reference_bootstrap.py --no-archive
```

完整输出恢复至已有规范路径 `data/phase_ring_continuation/step4_shared1032_reference_forward/segments_*.npz.gz` 及 `data/phase_ring_continuation/step5_retargeted_reference/Q_forward/segments_*.npz.gz`。原始射线共 117202168 字节，U/L共 62783494 字节，Q共 7721253 字节。依根README，这些可由已提交入口和精确版本重建的大中间件不另推入仓库；完整恢复证据已保存。若在另一个工作区使用这些数组，先实际重放并检查每个SHA，不能把本记录当作数组存在。

本次恢复只是找回同一固定参考多项式，**没有**把浮点参考本身变成真实连续流。原 R101 的真流残差、全部角/参数/积分误差和后续强算子条件仍各自保留。恢复后开始对完整550段作 R106 四相位项的诊断，不能用少数端点或单模去代表这份全参考。
