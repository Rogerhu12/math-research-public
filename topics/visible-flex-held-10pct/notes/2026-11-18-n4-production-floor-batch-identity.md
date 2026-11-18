# n4：新 CLI 的两 floor／三 stage 完整输出身份通过

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 真实结果

在 [独立版本编译完成](2026-11-18-n4-production-floor-native-compile.md) 后，按原冻结计划只执行两个 fixture batch：floor 0.1 和生产原值 0.05，每个 batch 都是原 stage 43、38、175，完整 40 列 Jacobian。

两次 CLI 真实 returncode 均为 0。**全部 252 个状态值、10080 个 tangent 值及六组可取得的根诊断聚合，均逐位相同于已保存的原 LD full-Jac 输出。** 两个 mean 行包含在完整状态和 $42\times40$ tangent 中，未省略。

这付清了该新 CLI、配置参数和二进制协议在所选三段上的身份检查。0.05 和 0.1 仍是两个不同的域门；三段同态不证明任意新状态或完整尾的门等价，也不是原 $2\times10^{-9}$ DN 接受。

## 输入字段与输出字节的独立复核

两个输入都为 70388 字节，输出都为 41632 字节。只读 collector 独立按字段解码，不 import 原 encoder/parser 或 native library。它逐项核对：

- ABI、维度、原根参数和 20 个减半因子；
- 原 state trig、全部 42 维初值和静态几何系数的 binary64 字节；
- 每个实际 RK 子步的 profile、step、三个 coefficient index、$x,h$；
- 完整输出 42 项、1680 项 tangent、原根聚合和 EOF。

这三个具体 fixture 实际各有 16 个子步、33 个去重后的 coefficient point。该观察只针对三段，不推广为全 2304 段的 cusp 网格统计。

两个输入文件共有 **59 字节实际不同**：58 字节位于 payload token 区间 `[44,108)`，1 字节位于 floor 区间 `[108,116)`；其他所有字节完全相同。允许变化区间共 72 字节，不是说 72 字节都改变。token 按输入头与 body 计算并在输出中原样回显；源、compiler 和 binary 身份仍由外部 manifest 独立绑定。

生产 0.05 与原完整 CP 的 `parameters.projectionFloor` 一致。每个 stage 的根数均为 64，按 43、38、175 的更新总数为 128、128、64，无 fallback；这些是可取得的聚合，没有把它们写成新的逐根 trace。

## 执行身份

保持新 C++ `e5a7d3b0…`、冻结 plan `6d3aa2a9…` 和 probe `994e7546…` 不变。执行的是新 CLI `frozen_flow_production_batch`，SHA256 `1b47ed47e70e35a08f11173b1f17a5d1c2ee046f59f54f235ee5fa56de07af94`。新 `.so` 在这一阶段没有被加载。

observer session 20894 记录真实 child exit 0，终态时间 2026-11-18 03:01:51 UTC，观察总时长约 2.002496 秒。两个 CLI 墙钟分别约 0.516666 秒和 0.650464 秒，stdout/stderr 均为空。没有重复运行来取更好的数值或时间，不把两次时间之差归因于 floor 参数。

目录为 `n4_work/native-production-floor-v1`，summary SHA256 `53c90c199ece0e11cb9e556a0c93a363a2113f79392915f81914e5cb20e83a21`。两个原 input/output、完整 raw、逐 case checkpoint、stdout/stderr 和 observer 终态全部保留。只读 `record_native_production_batch.py` 生成紧凑 `native_production_floor_batch_terminal.json`，没有再次调用流或 Jacobian。

## 后续生产边界

本轮没有安装 Node hook，没有构造新的完整物理尾、执行全部 stage 的 evaluate、Newton、DN、cut jets 或 audit。未来接口仍须在原 `evaluate` 词法闭包中一次调用全 stage batch，保留原 residual/scales/左端/Robin/稀疏校正/线搜索与验收门。

原生产只消费完整 $42\times40$ tangent 的前 40 行，输出 $\pi$ 行除该 stage 的 portRatio；原 stage 输入列不另缩放，两 mean 的末态求和仍供 `meanHeightToCut`。当前三段协议身份不替代实际 Node 参数传播、真实全 cusp 网格、原 audit 和最终 coupled prefix 的后续验收。
