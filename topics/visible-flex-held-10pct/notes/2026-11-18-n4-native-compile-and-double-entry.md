# n4：native 原有限流源码、编译与 double 基线入口

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 已完成的事

[native 扩展精度方案](2026-11-18-n4-native-extended-precision-plan.md)已落实为一个 C++ 标量内核、C ABI、三段 Python harness 和同内核的二进制 batch CLI。共享库和 CLI 两条 GCC/G++ 14.2.0 编译命令均真实 exit 0。四件源码均小于 30 KB，没有新增外部库依赖。

**截至本条，尚未加载共享库，尚未执行任何新的 flow、Jacobian 或 native batch。** 编译成功只说明这个入口可以构建，不说明移植字节身份、扩展精度误差、完整尾或 DN 已通过。下一份冻结计划只允许原 stage 43、38、175 的 **double 精确基线**；long double 和全部 40 列变分是之后的独立步骤。

## 冻结源码和实际构建

源码目录为 `scripts/resume_n4_tail/native_extended/`：

| 文件 | 内容 | SHA256 |
|---|---|---|
| `frozen_flow.cpp` | 原 formed-moment 根、普通 RK、字面隐式 Jac、同内核 batch CLI | `916d0a948a15100f9bb68b255c2192460efe249c08a3559ea9fb800fbb59ac3f` |
| `frozen_flow.h` | C ABI、回调和标量编码接口 | `88d7b9bc6c92a3d73ca33b2152e8bac078b6c9b3f90167f5e0a3409dd01f8356` |
| `probe_native_frozen_flow.py` | 原 V8 回调、完整 trace 重建、精确基线门和批协议编解码 | `42893f210b6d31c59abd04cdfec415a2408a543f726f87d808fc99cf8fad45db` |
| `build_native_extended.py` | 仅编译共享库和 CLI，不加载或运行它们 | `20437402d90d4bf1a7aa9488d9651dbc5387a2cbaffb85667ebb4e093ccbc6c3` |

编译保留 `-O2 -fno-fast-math -ffp-contract=off -fexcess-precision=standard -frounding-math`，不使用 FMA 合并或快速数学重排。编译记录为 `n4_work/native-extended-build-v1/build.json`，SHA256 `6a3bccea3aafe115cb28071ca23986e14e27c9074c67f8f91b094bfb87db0bf8`；包含实际命令、返回码、编译器/源码/产物身份和每条 stdout/stderr 哈希。

builder 的 Python 3.12 解析曾因一个相邻的数字/生成式关键字产生空格 `SyntaxWarning`；两条 C++ 编译均成功。这不是数学执行或数学失败，记录不将其描述为完全无警告的启动。编译二进制留在 scratch，不进入 Git。

## 源码保持的数学范围

C++ 状态核按既有冻结 evaluator 使用原 `moments - target` 根残差、原 Newton 矩阵、原 30 次迭代及 20 次减半、原停止/fallback 阈值和普通 RK 四项求和。没有移根 A/B、Kahan 或 Neumaier 改写。所有原 double 系数和 state trig 精确提升，原 double 的 $x,h$ 仍用于固定采样点查表。

完整 $42\times40$ 字面 Jacobian 源也已实现，但本条没有运行。它从 $q(L_v,P,P_t)$ 的三个局部导数另组 $B^{\rm exact},C_Q$，求全部 40 个隐式方向，再对原 split RHS 和变分 RK 求导。$B^{\rm exact}$ 独立检查正且有限的分解枢轴，不从原 Newton 矩阵或 D/S/A 域门借用 SPD 结论；不约简独立冻结的 $E,w^2$ 或 $\mathrm{pref}\,\mathrm{TF}$，两个 mean 行完整保留。

这仍是返回近似根处的方程隐式导数，不是停止分支算法的导数，也不是连续误差证书。root、closed_geometry 和 m3 的只读源审已核这一区分、链式、mean 索引、C ABI 和普通 RK 路径；源审不能替代未来数值门。

## 下一项唯一冻结执行

`n4_work/native-float-baseline-plan-v1.json` 的 SHA256 为 `67ee96a3323e457fefedc3b727180e321fdcd722232518e3a8bfdbf7fd8661f8`。该计划只运行 `--mode float-baseline`，不执行 literal Jacobian。

double 模式使用已有 V8 `root_rows` 向量回调和 `sqrt` 回调，避免把 glibc 的不同标量实现混入移植核对。harness 重建全部 12 类原 trace 事件；门是完整 **126 个输出 double 的字节**和 **116608 条事件的每个已记录操作数/判断**与原参考完全一致。任意不一致会先保存失败记录并停止，不用数值容忍放行。

旧根参考对应每段 64 个 RK field。未来利用 MP90 trajectory 计算变分参考时，必须按 `profile/step/label` 和原事件顺序对应根；同一 $x$ 的 b/c 是不同输入状态，不能合并。当前未实现或执行该独立 MP 变分参考。

## 接口和未付门

批处理协议按字段写入 little-endian 数据，避免直接复制 `Step` 结构体填充。它是一次完整 evaluate 的自包含系数/状态请求，native 不重新构造 profile；当前没有跨进程常驻系数缓存，也没有 Node 生产适配。token 绑定请求 payload，源码身份由外层 build manifest 另验，不能只凭 token 称源码已核。

native 状态和 tangent 在每段末尾转换为 binary64，原物理 portRatio、`out - node`、scales、左 target 和远端边界 norm 都应留在原调用层。内部高精度残差不能直接替代原 $2\times10^{-9}$ 门。

源码的 `diagnostics.kernel_seconds` 计时覆盖 `e.flow` 内的 trace 回调，因此带 trace 的值是包含回调的 stage 墙钟，不能称为纯 native 算术时间。longdouble trace 还会触发 Python/MP140 解码与十进制序列化。未来性能 probe 应在同库明确使用 null trace；本次计划的 double 基线仍须保留全部 116608 事件，不能为计时删掉身份门。

仍未完成的事项包括：native double 精确基线；long double 的状态精度和真实数学库/运行环境身份；state-only 与 full-Jac 的状态一致性；全部 40 列的独立 MP 变分比较；真实内核性能；完整 2304 段 batch、原边界 norm、原 DN 和最终 audit。当前 harness 的 longdouble 模式固定计算全 Jac，不意味着 state-only 对照已经完成。

紧凑入口记录为 `scripts/resume_n4_tail/native_extended_entry.json`，由 `record_native_extended_entry.py` 只读核对构建、冻结计划、全部来源及原参考计数后生成。没有新增场、节点或矩阵表进入 Git。
