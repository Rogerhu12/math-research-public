# Actual61：当前 576 段完整循环的三次试步接受与第 4 轮下降失败

作者：ChatGPT（geometry 子会话）。日期：2026-11-14 UTC。

分类：公开 Actions 的实际数值结果与来源核对；没有新增数学定理，没有本地运行科学计算。本记录先核公开的小文本原件；全部 snapshot、Jacobian、因子、方向及精确行账的字节审计另由对应 reader 完成，不能把本记录称为大数组全审。

## 1. 实际结果与范围

[实际 run 43645948199](https://github.com/Rogerhu12/math-research-public/actions/runs/43645948199) 使用 source `cf6b51193255dfc713610d2919598451ccdd49e2`，job `132603626663`。原科学 step 在 2026-11-14 22:02:57 开始，23:23:40 以失败结束；完整产物保存及普通 rebase 出版两个 step 均成功。job 于 23:25:37 结束。这里的失败不是 Actions 超时、文件传输错误或同步桥异常。

唯一 native 请求保留 actual17 的全部 112 个非零高度系数，并从 actual59 真正接受的一步后的完整 577×224 状态启动，初始状态 raw SHA 为 `384de298d6274ef7a6f5bdbc4e6cf6ef9dee5fb9bffd020b7b60001463940e03`，恢复负零 8 个。它没有把 actual28 旧雅可比或旧残差冒充当前评估。

实际完成 **4 次当前状态 fresh with-J 评估与 4 次 R273、eta=1 的完整 576 段 QR 校正**。四个 Python 子进程均返回 0，`bridge_failure=null`。原循环共执行 17 个 no-J 试步：3 个按原严格范数下降接受，14 个因残差不降而拒绝。全部已记录拒绝都属于 `residual-not-decreasing`；没有一个被记为 D/S/A、根求解或其他域守卫拒绝。

第 4 次校正后的原十个步长全部被拒，原 native 抛出：

> Error: multiple-shooting line search failed at 0.00007952539043101878

最后当前 with-J 范数为 `7.952539043101878e-5`，原容差仍为 `2e-9`。`native_accepted=false`，`complete_tail_matching=false`，没有完成真实的 endpoint 全 Jacobian 或最终 audit。请求包含 `jacobian=true,audit=true` 只表示它们被请求，不能当成它们已经执行并返回。原最大 32 轮没有改动，本次是在 iteration 3 的原线搜索失败处提前终止。

## 2. 当前评估与原试步必须分列

下表全部数值来自原 `native_trace.jsonl`、`native_trials.jsonl` 及桥的原摘要，不是本地重新算范数。迭代编号从 0 起。

| 原 iteration | 当前 fresh with-J 的原范数 | 原 no-J 试步结局 | 接受步长 | 接受时原 no-J 范数 |
|---|---:|---|---:|---:|
| 0 | 0.00018359565445185818 | 第 0 个试步接受 | 1 | 0.00016781299431962708 |
| 1 | 0.00016781299431962708 | 第 0 个试步接受 | 1 | 0.00008541616009257574 |
| 2 | 0.00010439752900203701 | 前 4 个拒绝，第 4 个接受 | 0.0625 | 0.000103579366549043 |
| 3 | 0.00007952539043101878 | 原十个全部拒绝 | 无 | 无 |

特别是 actual59 的原 no-J 接受范数 `0.0001289424025918576`，与本次对同一 raw 状态第一次 fresh with-J 返回的 `0.00018359565445185818` 不相同。本轮也出现同样现象：iteration 1 接受的 no-J 范数，与下一轮 fresh with-J 范数不同；iteration 2 接受的 no-J 范数，与最后一轮 fresh with-J 范数也不同。

这些已报数值明确要求区分两个实际计算路径。它们不证明是 Jacobian 数组求解误差、eta 选择、非线性截断、状态舍入或某个模式造成了唯一原因。原始 no-J 与 with-J 分支在源码中本来就是分别实现的路径；仅凭连续方程相同，不能把两次 binary64 返回的范数当成逐位相同。当前证据也没有完整保存每个 no-J 试步的全残差数组，不能在这里虚构最坏行位置或逐段误差分布。

## 3. 最后一轮全部十个实际试步

原 iteration 3 的 baseNorm 恒为 `0.00007952539043101878`。以下十行均实际调用原 no-J evaluate 并返回完整 trialNorm，然后由原严格下降条件拒绝。

| trial | 原步长 | 实际 trialNorm | 原分类 |
|---|---:|---:|---|
| 0 | 1 | 0.00014334206176455237 | residual-not-decreasing |
| 1 | 0.5 | 0.00024610326586060134 | residual-not-decreasing |
| 2 | 0.25 | 0.00015302135233630825 | residual-not-decreasing |
| 3 | 0.125 | 0.00014538746789703744 | residual-not-decreasing |
| 4 | 0.0625 | 0.0000959704557361986 | residual-not-decreasing |
| 5 | 0.03125 | 0.0001043157127567376 | residual-not-decreasing |
| 6 | 0.015625 | 0.0001043157127567376 | residual-not-decreasing |
| 7 | 0.0078125 | 0.000103579366549043 | residual-not-decreasing |
| 8 | 0.00390625 | 0.000103579366549043 | residual-not-decreasing |
| 9 | 0.001953125 | 0.000103579366549043 | residual-not-decreasing |

最后三个 no-J trialNorm 与上轮已接受 no-J 范数相同，是实际浮点读数事实；不能仅凭标量相等断言三个完整试步状态相同、方向为零，或定位发生了哪一项舍入。最后当前 with-J 返回 `minA=0.9999999999759498,minD=0.9999999999999858`；这些是守卫读数，不是求解器条件数或残差精度界。

## 4. 四个真正当前状态的身份

| iteration | 当前状态 raw SHA256 | snapshot result SHA256 |
|---|---|---|
| 0 | `384de298d6274ef7a6f5bdbc4e6cf6ef9dee5fb9bffd020b7b60001463940e03` | `8414a098f9bbd87b373b50e9579c04d9c1af11f9c31a5c613c7db29452ed86d2` |
| 1 | `78bd3880951910c473fa42b03bd87165b123e0339d4ced343f11e3ffb153caee` | `b49f483cf0e392850b220a93f843240ff5a7ace2a7b55910f2d7bea70bc350db` |
| 2 | `ad7963646d2d3351690b9c9945ef26caf0baf4cf12c92ac12c8bd716dc9a6fec` | `bd6834d59183ede5ed4d9bfede15e8d90b4e04251c491ac1642f6c452bed875c` |
| 3 | `b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013` | `5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286` |

本表是生产者已经写出的身份；本文件没有本地恢复方向、计算 base+alpha*delta 或重新执行完整 RHS。每轮保存的当前状态、原 J/r/cut/far/target/sigma 和实际方向仍是下一步可直接消费的独立原件。

## 5. 小文本原件保全与可核范围

以下原件来自已公开目录 [public-actions-43645948199-1-current576native](public-actions-43645948199-1-current576native/)。本地只将公开 UTF-8 原文逐字保存、核字节数及 SHA；没有通过连接器传二进制。

| 相对文件 | 字节数 | SHA256 |
|---|---:|---|
| `native-current576-damped/result.json` | 6891 | `b8754cc3c6f9635bd2f37da56d39811c2c8ef5442aa7947df89078cb416715ef` |
| `native-current576-damped/current-correction-summary.json` | 12691 | `f75e96707b7af6f191777145108c646c9aa863082b882dbdfc5b15e316bceeed` |
| `native-current576-damped/native_trace.jsonl` | 6292 | `864da1a02ced69724b4363fa40b04f7e6aa5d40539236733583d8a0a77259b41` |
| `native-current576-damped/native_trials.jsonl` | 3072 | `f0dfe82db212c9645c69b424995bb309aba6ee09c1b34db9a354ca604220aec6` |
| `native-current576-damped.log` | 837 | `c8820262f1c103656fb76a5e9993dd210ca6429a094b42a9d348311976db0490` |

summary、trace、trials 的 SHA 与 producer result 中对应收据逐字一致。[小文本字节与记录审计](2026-11-14-actual61-native-small-text-byte-audit.json) 保存了这些身份、全部 17 个原试步记录及四个 snapshot 收据，不冒全数组审计。原 launcher 是 `06b8c44c115fcf754e963aeeb3adc04a26500cade3817018bae50e2e50aebc3b`，hook 是 `0933ee819ce56be648f17e2e876372e943059f19c79fed701bda60ec11cf66dc`。当前系统 adapter 是 `695c2a564ada2bfc3cac251dfb5bd46bf99f6d16b696c64b75d9f90703a6ed90`，当前 QR entry 是 `ac04842bb9c42b9f29c8209d0d5f523c83744aa548e5615267521d8bf2c3141f`，借用原完整 R273 engine 是 `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33`。

运行还实际完成了两次规则同步，22:03:00 记录读取 `c383317e2c959e7af26e401b240d97ff8d13cf29` 并发布 `e88ab369d338f09f278a8a40c68fcba79ecbdd7c`，22:48:08 读取 `291303c473ba4e28dc6327734c8c93951424295e` 并发布 `e93d2290be74ec34df536524d86720ed6dae0760`。这些是同步日志事实；它们不改变本次冻结的科学源身份。

## 6. 后继所依据的具体缺口

本次已经推进到完整原非线性循环，得到三个真接受试步；没有得到可供后继 live full-DN 作为“已完成非零尾锚”的成功响应。既有 live full-DN、闭面与同 g 精化组件仍保持参数化，不能拿失败 native_0001 或最后 checkpoint 冒成功锚。

后继首先应消费本次真实 iteration 3 的状态与完整 with-J 原件，并明确同状态原 no-J 返回的全残差、原尺度及最坏行，定位两个实际路径的差异。必要的一次原 no-J 回放只补这份缺失证据，不需要再算同一份 J，也不改 g、H、远端图、scale、原容差或原十步逻辑。当前还不能据标量读数单独选择新 eta、重定义验收范数或称原方向已经有效。[R266](../results/R266-native-block-Newton-defect-and-original-scaled-descent.md)、[R272](../results/R272-native-RK-reference-and-propagation-error-split.md) 与 [R273](../results/R273-complete-native-damped-square-root-chain.md) 中不同误差对象的区分继续适用。
