# 完整 BlockQR：逐行诊断不再常驻第二份绝对值矩阵

原 BlockQR 在完整 CSR 与 QR 因子之外，另存一个 matrix_abs CSR，并在构造时创建全数据 abs 临时数组，只供行和与真实 backward-error 分母使用。独立 `block_qr_v2.py` 将这些诊断改为2048行一块的原 CSR 操作。每行原 sparse sum/matvec 的元素与顺序不变；完整原矩阵仍常驻并逐次计算实际残差，QR 消元、全部边界/参数、后继残差纠正和停止条件原样保留。

独立 wrapper `prefix_block_qr_driver_v3.py` 仍使用单向持有的无环 factor 包装。旧 block_qr.py 与 v2 wrapper 字节未改，不重绑历史执行。

真保存的 M16 原矩阵为43087×43087（49状态、879节点、16参数）。同一原右端实际比较：完整方向、每一个 backward denominator、matrix infinity norm、全部 factor/solve statistics 均逐位相同；核心 _apply/_solve 方法源码相同。原完整矩阵残差最大值仍为 `1.066670079402443e−20`。完整记录见 [JSON](2026-11-28-block-qr-streamed-diagnostics-actual-m16.json)。

该真 M16 因子少常驻55,523,204字节绝对值矩阵；完整对照4.4669秒，峰348484KiB。该峰包含新旧对照，不是高阶生产峰保证。高 M 的省量须按实际 CSR 计数或明确保守上界计算；2048行块也须计入临时存储。没有以减少诊断为理由丢弃原残差、纯齐次行 componentwise=1 的记录或任何原门。

检查入口 `check_block_qr_streaming.py` 严格绑定已经保存的真 M16 matrix/RHS SHA，不生成另一个随机系统。新入口尚不表示有新 BVP 接受或完整曲面。
