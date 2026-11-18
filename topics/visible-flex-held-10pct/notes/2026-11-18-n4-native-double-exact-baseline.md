# n4：native double 移植的完整字节基线通过

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 真实结论

按已冻结且独立审查的 [native 入口](2026-11-18-n4-native-compile-and-double-entry.md)，原 stage 43、38、175 的 native **double** 计算真实完成：包括两个 mean 的全部 **126 个输出 double 字节**、原记录中的全部 **116608 条事件及其操作数/判断**，均与原参考逐位相同。没有使用误差容忍放行。

这验证的是原 formed-moment 根、普通 RK 和冻结系数在 native 源中的移植身份。当前没有执行 long double 分支、字面隐式 Jacobian、完整 native batch 或 DN；不是新的实际尾接受，也不是扩展精度准确性或性能结论。

## 执行和逐位结果

执行保持 C++ 源 `916d0a948a15100f9bb68b255c2192460efe249c08a3559ea9fb800fbb59ac3f`、harness `42893f210b6d31c59abd04cdfec415a2408a543f726f87d808fc99cf8fad45db`、build 记录 `6a3bccea3aafe115cb28071ca23986e14e27c9074c67f8f91b094bfb87db0bf8`。唯一运行命令来自原计划 `67ee96a3323e457fefedc3b727180e321fdcd722232518e3a8bfdbf7fd8661f8`，模式为 `float-baseline`。

原 `root_rows` 向量标量回调和 SPD `sqrt` 回调仍由既有 V8 bridge 提供；没有将其他数学函数实现混入 double 身份核对。

| stage | 完整输出 | 逐位相同事件数 | 返回根数 | Newton 更新总数 | fallback 数 |
|---:|---:|---:|---:|---:|---:|
| 43 | 42/42 | 44928 | 64 | 128 | 0 |
| 38 | 42/42 | 44928 | 64 | 128 | 0 |
| 175 | 42/42 | 26752 | 64 | 64 | 0 |

逐位核对覆盖原完整 state、两 mean、target/L、点根求值、D/S/A 域比较顺序、Cholesky 枢轴、原停止/减半/fallback 判断及 RK field 身份。三个最终输出 SHA256 仍为原来的：

- stage 43：`16c51ec0c3fea016923f23d7ab866d85d9b9011be3f8b8ed8ef35d0dd1799343`；
- stage 38：`adb4f35c8dfcf45052ee3878ea3cf97868942a13a023249263fff5493b5acef4`；
- stage 175：`ac9b59fd3a38ed4bbd8b81c9fbf272052bfdbbe049ca9cbc1a346167383c4786`。

固定 target 的原归一残差也保持 $7.4292894202\times10^{-9}$、$6.4195450047\times10^{-9}$、$9.5074111752\times10^{-10}$。这些旧固定节点没有因移植身份通过而成为 accepted 尾状态。

## 运行环境和计时口径

observer session 93415 记录真实 child exit 0，终态为 2026-11-18 02:19:21 UTC，约 6.018 秒。目录为 `n4_work/native-float-baseline-v1`；summary SHA256 `8bc4adafbd655fe5fa5de7b7fbda542a3c4edda5b7505deb579d9ec40a503078`，raw SHA256 `50776b349d13d1239e0de925e3f9954bd51352a6e740f8b26e86016d2827ec4a`。

实际加载时 C ABI 和 ctypes 的 config/step/stage/callback/diagnostics 大小分别为 88/40/32/32/80 字节，全部匹配；读取的舍入模式为 nearest，x87 control word 为 895，即 `0x037f`。这仍不是已经运行 long double 数学函数的证据。

三个 `kernel_seconds` 约为 0.4850、0.4079、0.2197 秒，包含 V8 标量和完整 trace 回调；observer 时间还包含解析、比对和保存。它们不能用于冒充无 trace 的 native long double 全 2304 段性能。

## 可复核记录和剩余门

`scripts/resume_n4_tail/record_native_float_baseline.py` 只读完成文件，重新核对完整 126 字节输出、全部 116608 事件、原根诊断、执行命令和所有来源后生成 `native_float_baseline_record.json`。它没有再次调用任何流或共享库。记录只含来源、哈希和标量，完整字段/trace 留在 scratch。

这一步付清了 native double 移植身份。long double 的 state-only/full-Jac 同态、全部 42 输出对 MP90 的精度、40 列独立变分参照、真实数学库身份、无 trace 性能、完整 batch/原边界 norm/原 DN 和最终审计仍分别待做；没有把基线通过扩大成这些结论。
