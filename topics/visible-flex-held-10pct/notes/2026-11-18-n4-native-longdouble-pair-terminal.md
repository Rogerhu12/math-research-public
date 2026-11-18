# n4：同库 long double 六调用真实完成，完整状态同态通过

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 真实结论与范围

按已发布的 [六调用入口](2026-11-18-n4-native-longdouble-pair-plan.md)，stage 43、38、175 各一次 state-only、一次完整 40 列 Jacobian，全部真实完成。三段两模式之间的 **42 个原生 x87 编码、42 个 binary64 输出和原根诊断聚合均逐位相同**；两个 mean 没有省略。

原生状态对既有 MP90 的误差明显小于原 binary64 路径，最终 binary64 边界转换后的误差也更小。此结论不表示每个分量都逐点改善，或所有输出都与 MP90 的就近舍入逐位相同。固定的旧节点仍未达到原 $2\times10^{-9}$ DN 门；没有新的 actual-tail 接受。

本轮只用了同一已编译 C++ 内核，源 `916d0a…`、共享库 `d31cd86…`、build `6a3bccea…` 不变。执行源 `4d6b143b…`，计划 `b30bdac3…`；没有 traced 追加调用、变体重试、重新编译、原公式改写或阈值变动。

## 状态对 MP90 的有限算术误差

以下归一误差是完整物理 40 行的最大值，输出 $\pi$ 行依原 portRatio 除法，再除原段的归一尺度。MP90 是已保存的冻结 binary64 系数、原 RK 和原 point-root 停止规则读数，不是真连续 ODE 误差证书。

| stage | 原 binary64 对 MP90 | 原生 long double 对 MP90 | 转回 binary64 后对 MP90 | 旧固定 target 残差 |
|---:|---:|---:|---:|---:|
| 43 | $3.3719781\times10^{-9}$ | $2.5583335\times10^{-12}$ | $2.0297027\times10^{-10}$ | $4.1273830\times10^{-9}$ |
| 38 | $9.5921018\times10^{-9}$ | $7.8293990\times10^{-12}$ | $1.7922483\times10^{-10}$ | $4.8146588\times10^{-9}$ |
| 175 | $1.3520220\times10^{-8}$ | $5.5579300\times10^{-12}$ | $1.6916379\times10^{-9}$ | $1.5211858\times10^{-8}$ |

原生全部 42 项的最大绝对误差分别约为 $1.4093620\times10^{-15}$、$4.4369480\times10^{-15}$、$3.2451220\times10^{-19}$；两个 mean 的最大绝对误差分别约为 $2.2058150\times10^{-24}$、$2.2058150\times10^{-24}$、$7.0586079\times10^{-23}$。转回 binary64 后，两 mean 的最大误差分别为 $2.4705128\times10^{-21}$、$6.6350914\times10^{-21}$、$4.9692600\times10^{-20}$。

最终 42 个 binary64 分量中，与保存 MP90 值的就近舍入逐位相同的数量分别是 37、40、12；没有以误差较小替代“全部字节相同”的要求。这里要求全部逐位相同的是 **同一 LD 内核的 state-only 与 full-Jac 两模式**，该门在全部三段通过。

stage 175 对旧固定 target 的残差比原 binary64 路径更大，但对 MP90 更接近。这再次区分了旧节点一致性与流值的有限算术准确性；不能用较小 target 残差单独选择求值路径。

## 原根和完整切向量

每次调用返回 64 个原根；按 stage 43、38、175，每种模式的 Newton 更新总数分别为 128、128、64，fallback 均为零。null callback 下没有保存逐根迭代／减半轨迹，记录只给内核实际提供的聚合。

最大相对停止残差分别为 $8.7170971\times10^{-20}$、$8.4958480\times10^{-20}$、$1.2789347\times10^{-15}$。完整 Jacobian 模式独立分解 $B^{exact}$ 的最小观测枢轴分别约为 0.9999038914、0.9998236156、0.9999999997；这是有限分解读数，不是严格下界或条件数。

三个完整 $42\times40$ Jacobian 的 **5040 个原生值及其 5040 个 binary64 转换**全部保存。只读 collector 使用独立 `Fraction` 解码每个 10 字节 x87 值，并逐项核对原生值到 binary64 的转换；它同样核对了六次调用的 252 个状态输出转换，以及所有逐段 checkpoint 与最终 raw 的一致性。没有再次调用 flow、根、Jacobian 或共享库。

完整切向量的数学准确性仍等待 [独立 MP90 保存轨迹变分](2026-11-18-n4-saved-mp90-variational-reference-plan.md) 的全部 40 列对照。即使随后对照很接近，也仍是近似根处隐式导数和固定有限轨迹的数值证据，不是对 Newton 停止算法的微分或连续流证书。

## 无 trace 的真实计时与运行环境

observer session 95607 的真实 child exit 为 0，终态时间 2026-11-18 02:35:34 UTC，总计约 4.0068 秒。探针内部从加载阶段至 raw 保存后约 0.9901 秒；observer 还包含输入解析、哈希、导入和观察周期。

| stage | state-only native flow 秒 | full-Jac native flow 秒 | full-Jac FFI 秒 | full-Jac Python 解码／比较秒 |
|---:|---:|---:|---:|---:|
| 43 | 0.072172 | 0.201980 | 0.202038 | 0.004491 |
| 38 | 0.064883 | 0.178017 | 0.178079 | 0.004344 |
| 175 | 0.043079 | 0.161655 | 0.161714 | 0.004812 |

native flow 计时覆盖无 callback 的 `e.flow`，包括其临时分配；FFI 还包括 Engine 构造和 native 输出编码；Python 字节解读、哈希、MP90 比较另计。没有把三个 stage 直接称为全部 2304 段的 benchmark，也没有与带 V8／trace callback 的原 double 基线混比。

所有调用前后实际读到 FE nearest、x87 control word 895（`0x037f`）、64 位有效精度和 16 字节存储，ABI 大小与原 ctypes 一致。实际映射的数学库为 `/usr/lib/x86_64-linux-gnu/libm.so.6`，SHA256 `6d567d53e895273ca14a1f9dc164fc6c8d39aed2f60aa46a733c2784228915f3`；`sqrtl`、`log1pl`、`expm1l` 的 provider 均解析到它。符号别名与完整 maps 另有记录；这只绑定实际装载身份，不宣称观察到每次数学函数调用或编译器是否内联。

sampled namespace tree RSS 与 `RUSAGE_CHILDREN` maxrss 分别记录为 197976 KiB 和 251900 KiB；这两个口径不同，均不冒称全宿主机全部进程峰值。

## 完成文件与下一接口边界

执行目录为 `n4_work/native-longdouble-pair-v1`。summary SHA256 为 `94f774a4ebac0c1dcad8f6de8e3796f4e6ab23475694e09acefb9fb7e4c86908`，完整 raw 为 `9853dc0ae370b775f2bf1441510884632a9afe2b1428b88f2f223d6947ca0b43`，真实 resource 为 `7c8b285074fad00270bc77cc1fb8c04cef7a4ddcf56da341bb340edf99f4ca0a`。

`scripts/resume_n4_tail/record_native_longdouble_pair.py` 只读这些原输出，独立解码、重新计算全部状态误差标量、核对六次命令日志及所有来源，生成紧凑 `native_longdouble_pair_terminal.json`。完整 state、tangent、maps 和逐调用 checkpoint 均留在 scratch。

原 Node 的完整 evaluate → 同库 batch、原边界行缩放与 norm、原 DN、audit 和 coupled prefix 均未运行。下一接口须保留原 stage 输入、只对输出 $\pi$ 行按 portRatio 转换、原 $2\times10^{-9}$ 门与最终审计，并另核实际使用的 Jacobian 行。当前不能将三个有限 stage 的精度进展扩大为 full tail 或 10% 闭合构造。
