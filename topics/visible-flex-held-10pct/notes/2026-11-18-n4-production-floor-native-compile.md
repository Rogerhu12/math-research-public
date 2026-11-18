# n4：生产 floor 独立 native 版本真实编译完成

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

按 [已冻结源码及两阶段计划](2026-11-18-n4-production-floor-native-source-plan.md)，只执行编译阶段。新共享库和新 CLI 的两次编译均真实 returncode 0，stdout/stderr 均为空；没有加载库或运行数学内核。

源 `frozen_flow_production.cpp` 的 SHA256 仍为 `e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf`。相对旧源只扩展配置检查，允许明确的生产 floor 0.05 并保留胶囊 0.1；其余源码逐字相同。旧 C++、旧 `.so`、旧 CLI 及已执行程序保持不变。

## 编译身份与真实终态

使用原 `/usr/bin/x86_64-linux-gnu-g++-14`，基础 flags 完全沿用原 build：

```text
-std=c++17 -O2 -fno-fast-math -ffp-contract=off
-fexcess-precision=standard -frounding-math
```

共享库额外使用 `-fPIC -shared`；CLI 使用 `-DVF_BUILD_MAIN`；两者均链接 `-lm`。编译器文件 hash、完整真实 argv 和两次输出文件均保存在 build 及紧凑记录中。

| 产物 | 编译 returncode | 编译墙钟秒 | SHA256 |
|---|---:|---:|---|
| `libfrozen_flow_production.so` | 0 | 3.624432 | `d6ee1b5a19bad636f012a02f02d7e99379249431df96bb970113a85dbff79bef` |
| `frozen_flow_production_batch` | 0 | 3.433770 | `1b47ed47e70e35a08f11173b1f17a5d1c2ee046f59f54f235ee5fa56de07af94` |

产物目录为 `n4_work/native-production-floor-v1`。observer session 83860 记录真实 child exit 0，时间为 2026-11-18 02:58:24 UTC，观察总时长约 8.009846 秒。

`build.json` 的 SHA256 为 `069165b977b12576586a94ffd60a17f24f9c292b30827bf6e874c7b0c9daa2d3`；`compile-resource.json` 为 `aa15034a21cc248ebcc81c0d510fbab72ccdd69084cfb5e18e392896cf0cdda2`。

## 记录与边界

只读 collector `scripts/resume_n4_tail/record_native_production_compile.py` 检查原计划、唯一源码替换、所有来源、真实编译 argv、返回码、产物和原观察器日志，生成 `native_production_floor_compile.json`。collector 没有加载或执行产物。

编译成功只说明这个独立版本已生成；不证明两个 floor 的完整数值输出相同。已冻结的两次 CLI 三段 full-Jac 接口检查尚未执行。生产 Node 的词法 evaluate hook、完整 tail residual／原 $2\times10^{-9}$ 门、原 audit 和 coupled prefix 也都未运行，不能从本条推出新 actual-tail 接受或闭合几何结果。
