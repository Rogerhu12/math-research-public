# 原 LocalNormalSystem 的无损分片检查点

## 目的和实现范围

当前完整 normal 装配已经可能在后续 QP 前因进程退出而丢失。本入口只保存和恢复已存在的原 `LocalNormalSystem`，使装配、QP 和实际 Armijo 评估能够在同一个输入、同一个有限目标上分进程继续。它没有改变 R159 消元、求和、缩放、阻尼或方向求解公式，也没有装配任何新的 F/J/normal。

新源为 `scripts/fd2d_gc_normal_checkpoint.py`，SHA256：

`330fad074fcfc021279802c9b8f11e0f0f84dc6acb96e48d165360eb82dec66d`。

它绑定未修改的 `fd2d_gc_local_normal_system.py`，SHA256：

`2773a28192620749bb227b33e7ebdbb42deacca9370b34c392ba9d3edfa95bcf`。

这是存储接口，不新增 R 号，不作为新数学门，也不认定此前进程 −9 的原因。

## API

```python
from fd2d_gc_normal_checkpoint import (
    save_normal_checkpoint, load_normal_checkpoint,
)

manifest = save_normal_checkpoint(normal, prefix, binding=binding)
# manifest is Path(prefix) / "manifest.json".
# prefix must be a new directory and is never overwritten.

restored = load_normal_checkpoint(
    problem, manifest, expected_binding=binding,
)
# restored is the unchanged source's LocalNormalSystem(problem).
```

`binding` 是调用者给出的明确 JSON 对象。接口不猜测实际 input、source 或有限目标。调用方当前约定应包含实际输入 NPZ 的内容 SHA/bytes、当前完整 vector 的 dtype/shape/内容身份、candidate 与实际数学源 SHA、完整有限目标设置及 field-definition SHA。阻尼、cache 计数、路径和计时不属于此数学绑定。阻尼变化时只要有限 normal 相同，可以重用此检查点。

绑定以排序 JSON 对象的规范文本核对；数组顺序、整数与浮点数类型、负零等均不被悄悄改写。不接受 NumPy scalar 或 tuple 冒充已经定义的 JSON binding。调用方可以按自己的准确定义先构成 JSON 值，再传入。

## 保存内容和精确身份

normal 的数值数据包括逐节点 `diagonal`、逐邻接节点 `upper`，以及相应自由列区间的 `Hfp`、`gf`、`field_norm_squared`。每个节点分片最多 4 个节点。全局 `Hpp`、`gp`、`parameter_norm_squared` 单独放在一个小包中；空宽度节点也按原 shape/dtype 保留。

每个 NPZ 实际文件严格小于 1000000 bytes，保存原数组 dtype、shape 和 C 顺序逻辑字节的 SHA256；没有量化、转 dtype 或 pickle。本次范围的 K31、q95、P54 已在此上限内。若未来一个单独节点块已大到超过这个声明的包上限，入口明确拒绝写成完成状态，不能把超限文件静默保存；这不是本次数值问题的障碍或解存在性条件。

mapping 的 `central_nodes`、`extra`、`pairs`、`fixed`、`free`、`widths`、`offsets` 保存实际必要数组。还对每个节点的 `node_free`、`field_maps`、`parameter_maps` 保存独立 shape/dtype/字节 SHA，包括中央精确消元进入参数列的实际矩阵。仅验证 fixed/free 列表而漏掉中央映射是不充分的，此实现没有这样省略。

`residual_squared`、`rows`、`blocks`、`row_groups`、`info` 通过有类型的 JSON metadata 保存。Python 浮点用实际 64 位字节编码，NumPy scalar 与小诊断数组保留实际 dtype 和字节；list、tuple、dict 的值和类型均保持。这里保存的是诊断值，不承诺不同 Python 对象之间的内存 alias 关系。意外的大数组若塞进 `info` 会被明确拒绝，不能用 metadata 绕过分片大小约定。

## 恢复为何不需要重算 normal

load 先验证完成 schema、调用方 binding、原 normal 源和检查点源身份，然后调用原构造器 `LocalNormalSystem(problem)` 重建 mapping。只有此新 mapping 的全部数组、每个节点两种线性映射和标量尺寸都与保存身份一致，才读入数据。

每个分片读取时同时验证文件 SHA/bytes、完整 key 集、每个数组 shape/dtype/字节 SHA。恢复严格覆盖从第 0 到最后节点的连续不重叠范围；遗漏、重复或超过 4 节点的块都会拒绝。所有数值直接赋回原构造器分配的数组，没有矩阵乘法或求和。metadata 再作逐类型往返核对。因此，成功返回时，原已装配 normal 的全部逻辑数值字节和诊断值保持不变；源公式、映射不匹配或不完整分片不会作为一个“近似可用”的 normal 返回。

原 finite normal 的正确性仍来自装配过程自身。本接口只证明和核实 transport，不能从一个成功读取的文件推断几何或有限残差已经合格。

## 写入完成与恢复状态

save 使用目标的唯一同层临时目录。各 NPZ 先写临时文件、flush/fsync，再改名；manifest 最后写入。只有全部文件完成，整个目录才原子改名为调用方给出的全新 `prefix`。已有目标不覆盖。load 还核对 manifest 声明的最终目录名，因此未完成临时目录不能冒充已提交检查点。

真实昂贵的中间 normal 可留在当前工作区或 `/tmp` 供阶段恢复；它不是每轮都应提交的研究成果。发布必要源、绑定定义、SHA 和最后 accepted 状态即可。若某个未接受 normal 成为唯一昂贵可恢复进度，可由主代理单独保留最新闭实体；本次没有为每次 normal 创建仓库副本。

## 本次唯一小核

`scripts/fd2d-normal-checkpoint-check.py` 使用原 `LocalNormalSystem`，只建 9 个抽象节点，采用当前 K31 的 q95/P54 宽度，包含零宽度中央/末节点、一个 coast 冗余帽和一个 trace gauge 节点。数组填入明确标为 synthetic 的测试数据，不把它们称为实际23b4 normal，也没有求一个残差或 Jacobian。

一次 save/load 往返结果：

| 项目 | 结果 |
| --- | --- |
| normal 数值存储 | 866904 bytes |
| 最大 NPZ 分片 | 577446 bytes |
| 所有 normal 数组和 typed metadata | 逐字节/逐类型一致 |
| 重建 mapping 全部值 | 逐字节一致 |
| 错误 binding | 拒绝 |
| 中央映射仅改 1 ulp | 拒绝 |
| 分片仅破坏 1 byte | 拒绝；随后恢复测试文件原字节 |

这些拒绝检查只使用同一个小 transport fixture，没有再次装配 normal。实际进程 session83425，初始 chunk3ab9c0、末 chunk1f2da6，自然 exit0；0.3413010709991795 秒，峰值 RSS 65152 KiB。原始报告、实际回执、源和完整 fixture manifest 定义在本组 closed manifest 中；临时 fixture 数值包不另加入 git。

最终主线是否从某个真实完整 normal 继续，须由 driver 提供该真实输入与完整有限目标的 binding。此处没有产生新的方向、accepted 状态、BVP 或闭曲面结论。
