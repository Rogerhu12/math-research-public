# 原尾 M≤64 边界的只读审查

本条只读检查当前 E 链实际载入的 native/chord 源，以及仓内 native ABI/包装器。未改运行中的 kernel、源树、manifest 或请求，未执行 M80 尾。结论是：**64 是若干明确的构造器/协议守卫；所读原 native ABI 及 Fourier 状态并没有固定长度 64 的模数组。** 仅放宽 C++ 一处不足以进入完整高 M。

## 活跃链必须一致处理的边界

| 位置 | 真实限制 | 要求 |
| --- | --- | --- |
| `frozen_flow_production.cpp` 的 `validate` 与 CLI header | 两处 `1<=M<=64` | 新独立候选同时采用声明的有限上界；保 N>4M·spacing 等所有其他门。 |
| `parallel_native_batch.py:split_wire` | `1<=modes<=64` | 与候选 CLI 一致，否则进程前就拒绝高 M。输出长度本来按 M 动态计算。 |
| 实际 `scripts/periodic-quadrature/general_root_tail_momentum.mjs` | `M<=64` | stage-core 与 split/fast 工厂均经此构造器。 |
| `general_exact_tail_cauchy.mjs` | `M<=64` | 上述 momentum 工厂仍创建完整 `createRawTailEngine`，它立即创建 relative engine；独立旧诊断也必须保留完整 M。 |
| `mild_mode_tail_continue.py` | 默认模序列止于 64 | 新 continuation 需显式包含实际源 M；不能截到 64。自适应 full-H 入口本身没有新的 64 限制。 |

`repro/source-root/.../general_root_tail_momentum.mjs` 也有 64 守卫，但当前物理背景工厂明确以 `modes:1` 构造旧几何源；完整 shooting 使用上表的 periodic 版本。`78718-tail-fourier-root-momentum.mjs` 的 64 守卫属于另一个未选中的工厂。不能把搜索到的每一个 64 都改掉：原几何 R64、SHA 的 64 个 ASCII 字节、x87 的 64 位有效数字、原 root 的 20 个二分数及 2/3 维自动微分数组均与模数上限无关。

## 不破坏字面几何来源的最小独立扩展

旧 `closing_tail_sources.mjs` 在导入任何几何源前逐个验证九个 Git blob，包含 `general_exact_tail_cauchy*.mjs`。因此不能在 verified cache 内改 relative 守卫，再保留旧 blob 声明。可在全新 owned runtime 的 periodic 目录复制完整 raw/relative 两模块，只改变 relative 的有限 M 上界并把 periodic momentum 的 raw 导入指向这份独立副本；原 verified geometry cache 及其九个 blob 保持字面不变。全部复制源、导入重定向与原来源哈希进入新的 runtime manifest。

native 侧在另一独立候选路径复制原 C++/header/wire wrapper，只改上述三处有限维度守卫。`prepare_recovered_native.py` 现在会把自身目录下的原 C++/wrapper 哈希写入 manifest，所以不能把新二进制塞给它后谎称仍是旧 C++；需独立扩维 installer 明确绑定候选 C++、原 header、候选 wrapper 和新二进制。ABI1 的字段布局本身无需改动；固定 scope 仍绑定每次实际 M/N/spacing，不能用宽上界替代 scope 检查。

最小下一维度若是 M80，可先声明候选上界 80；若要预备 M96/M128，审查范围应明确写为 `1<=M<=128`，逐次运行仍只用其真实完整 M。这里没有证明任何高 M 数学实例可收敛。spacing=3 时保原严格 N>12M，并保 audit 的 2 幂 N；现 controller 的 `next_power_of_two(16M)` 对 M80/96/128 均给 N2048。

## 动态布局与真实资源边界

`VFConfig.M` 是 int32；header 中 `VFStage.initial42` 是旧字段名的指针，实际读写长度严格为 2M+2。C++ 用动态 vector 存 state、J=M+1 根、(2M+2)×2M 变分矩阵及每点 M+12 个系数。固定 `std::array<R,2/3>` 只用于标量偏导。JS 的对应 Fourier、root、physical jets、cut jets 和 height-J 都按 M 动态分配；没有发现要求把 M>64 分块丢模的 ABI 结构。

对当前 1152 段，成功 full-J wire 的精确大小为

`88 + 1152 * (8 + 8*(2M+2)*(1+2M) + 64)` 字节。

| M | N（上述 2 幂规则） | 完整 shooting 未知数 | 原 full-J wire | 仅所存 2M×2M stage-J |
| ---: | ---: | ---: | ---: | ---: |
| 24 | 512 | 55344 | 22662232 B | 21233664 B |
| 64 | 1024 | 147584 | 154635352 B | 150994944 B |
| 80 | 2048 | 184480 | 240454744 B | 235929600 B |
| 96 | 2048 | 221376 | 345148504 B | 339738624 B |
| 128 | 2048 | 295168 | 611159128 B | 603979776 B |

这只是 wire/数组大小，不是峰值 RAM。现 JS 还持有输入、输出、解析后的 flows，再把全部 J 序列化给原 sparse helper；Python 同时持有 JSON/CSR/LU。native adapter 的 `maxBuffer=16MiB` 只管子进程 stdout/stderr，二进制另从文件读；sparse helper 的 `maxBuffer=128MiB` 是其返回流限制，并不是完整输入 J 可免费驻留的保证。客户端另有压缩响应小于 5,000,000 B 的既有记录门；尚未对 M80 实际响应测量，不能假设一定通过，更不能不记录就丢 state。

后继的候选资格验证应先只核完整尺寸/源身份及所需方向与原允许模数的真实重叠实例，再在实际高 M 场上付全部原域、残差、full-J、height-J 与 audit。该审查没有改变当前 M24/full-H 生产链，也没有获得高 M 接受或闭图结论。
