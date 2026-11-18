# n4：生产 floor 0.05 的独立 native 源与 batch 身份计划

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 已准备的唯一源码改动

在 [capsule 0.1／生产 0.05 的入口发现](2026-11-18-n4-capsule-and-production-floor-binding.md) 后，本条准备独立源码 `native_extended/frozen_flow_production.cpp`。它的 SHA256 是 `e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf`。

与已执行且保持冻结的 `frozen_flow.cpp`（`916d0a…`）相比，**只有一处字面替换**：

```cpp
c.floor!=.1||
```

变为

```cpp
!(c.floor==.1||c.floor==.05)||
```

新文件其余内容逐字相同；仍使用原 header。`Engine` 的实际 D/S/A 比较依然读取传入的 `c.floor`，没有固定成某个隐含默认值。生产入口需明确提供原 DN 的 0.05；0.1 仅保留给已有胶囊接口对照。

这没有改变根方程、原 Newton 矩阵、30 次上限、20 个减半因子、停止／fallback 常数、原 RK、字面隐式 Jacobian、静态系数定义、数学函数、输出转换或 binary wire 布局。旧 C++、旧 `.so`、旧 batch 可执行文件及全部已执行源码保持不动。

## 当前只有准备，没有编译或新数学执行

`prepare_native_production_floor.py` 已真实完成源生成、AST 检查和来源哈希核对，保存计划
`n4_work/native-production-floor-v1/plan.json`，SHA256 `6d3aa2a9deaea97a73e2a6d4a227c6f7ae0e775edbbd94c4982c748721d41a4e`。

紧凑入口为 `scripts/resume_n4_tail/native_production_floor_entry.json`。准备过程没有调用编译器、加载共享库、执行流、Jacobian 或 batch。后续两个阶段的命令已经写入计划，尚未执行：

| 阶段 | 冻结操作 | 必须保存的结果 |
|---|---|---|
| 编译 | 原 compiler／flags 分别生成新的 `.so` 和 CLI | 两次真实 returncode、stdout/stderr、源／二进制／命令 hash |
| fixture batch | floor 0.1、floor 0.05 各一次 CLI；每次仅原 stage 43、38、175，均完整 Jacobian | 两个 binary input/output、真实 returncode、全部 42／1680 输出及同态结果 |

`compile_native_production_floor.py` 在编译前重新验证“新源除该唯一表达式外与旧源相同”，保存实际编译结果，但不加载或执行结果。新输出目录独立，遇到已有部分或完成产物即拒绝覆盖。

## 两个 floor 的精确接口门

`probe_native_batch_floor_binding.py` 只复用原冻结 harness 的 fieldwise payload encoder 和 output parser。原三段 state、trig、几何系数、完整 cusp/RK 网格保持现有胶囊值；不重新计算原非线性流来造参考。

两个输入文件除了 **64 字节 payload token** 和 **8 字节 floor** 必须逐字相同。其 wire offset 分别是 `[44,108)` 和 `[108,116)`；token 只绑定 payload，源／编译器／二进制身份另由 manifest 校验。生产的 0.05 还必须与原完整 CP 的 `parameters.projectionFloor` 相同。

每个 stage 的全部 42 项 binary64 state、全部 $42\times40$ binary64 tangent，以及可取得的原根聚合必须逐位等于既有 [LD full-Jac 终态](2026-11-18-n4-native-longdouble-pair-terminal.md)。总计核对 252 个 state 值、10080 个 tangent 值。时间不是身份比较项；不通过时保存原输出和错误并终止，没有换变体或自动重试。

这一步针对新 binary／配置／wire 接口，不能把两个不同域门宣称为全局等价。三段原保存轨迹都远高于 0.1，因而适合检查参数传播，但尚未检查任意未来 Newton 试步的域判断。

## 已定位的生产调用边界

原 worker `950f-tail-stage-port-v3.mjs` 构造 split DN；`950f-tail-stage-core.mjs` 的 `solve` 调用内部词法闭包 `evaluate`。只给导出的 `dn.tail.evaluate` 重新赋值不会替换这个内部调用。因此未来 owned 版本需在这个词法入口加入一次完整 batch，随后保留原逐段 residual、scales、左端 target、far Robin、稀疏校正、线搜索和原 $2\times10^{-9}$ 门。

原 stage 输入是 $K+2$ 维零数组，其中前 $K=40$ 项直接复制 `states[n+1]`，两 mean 初值为零；没有输入 portRatio 乘法。原输出只对 $\pi$ 行除 `c.portRatio`。batch 要保全 42 项和 $42\times40$ tangent；原生产稀疏校正及 cut graph 只消费 tangent 的 **前 40 行**，并同样只对输出 $\pi$ 行除 ratio。meanHeight 是两 mean 状态的和。

`cutJets`、`heightJetJacobian` 的有限差分和原 audit／RK32 继续使用原 engine 对象；这条射击 evaluate 接口不自动把它们升级成 LD。原 same-mu engine cache 和对象身份也保留。静态几何／state trig／实际 cusp 网格可在固定 DN 下首次 evaluate 后缓存；本自包含 CLI 协议没有跨进程的 native 系数缓存。

**本条没有实现或安装生产 Node hook。** 这里只定位接入边界，并准备上述独立 floor 源及有限三段协议检查；完整 worker 接入仍需后续实际源码和审查。

## 协议字节成本的有限口径

现有 ABI 在 $M=20,N_q=128$ 时，输入固定头为 42284 字节，每个 stage 为

$$344+256p+36s\quad\text{字节},$$

其中 $p$ 是实际去重后的 coefficient point 数，$s$ 是实际 RK 子步数。若仅作“无额外 cusp、每段 $s=16,p=33$”的字节预算，2304 段输入为 21626156 字节；state-only 输出为 940120 字节，完整 Jacobian 输出为 31905880 字节。

这些是按 wire 字段数得到的预算，不是已经观测全部物理 cusp 网格。真正打包时必须记录总 $p,s$ 和精确输入长度。完整 evaluate 计划只启动一个 batch 进程；CLI 按 stage 读取和计算。原稀疏系统的独立 Python 调用仍是原流程的一部分。

当前没有完整尾性能测量、生产 DN／audit 成功或新闭合构造结论。独立 MP90 全 Jacobian 比较属于另一份已保存数据对照，也不能代替这里生产 floor 和协议绑定的实际执行。
