# R273 完整 native 阻尼平方根链：独立备用入口

类型：备用计算源码与接口；作者：exact_refinement；日期：2026-11-14。

## 1. 状态与用途

源码为 `computations/exact_20261114_native_damped_chain_qr.py`。本次只完成源码和 Python AST 检查，没有导入科学模块、没有本地数值、没有派发 Actions，也没有选定 eta。request54 的新矩阵计算仍由其原完整均衡流程执行；这份备用源的存在不表示该计算已经数学失败。

数学依据是 [R273](../results/R273-complete-native-damped-square-root-chain.md)。入口给原完整 finite block system 选择一个阻尼最小二乘方向；它保持原目标 H、far 图、所有 sigma、所有非零模式和原最终 nonlinear 规则。严格二范数模型下降不能推出原无穷范数下降；最终仍须单独执行原十个试步。

## 2. 输入与唯一目标

组件硬锁当前 `exact_20261114_rawcell0_direct_ld_system.py`，SHA 为 `b64b6ed8b387834b5cc9332675127a1dcbb15a317c3400f5b768d18cdbdf5a8e`。该 adapter 完整绑定 actual28、actual41 和本次真实 direct-LD capture result SHA，给出唯一的原坐标 binary64 新 1372 矩阵。输入合同与 [完整 1372 接口](2026-11-14-direct-LD-complete1372-system-interface.md) 相同。

它保留 1372 stage、1373 节点、每节点 224 个 Q/Pi 变量和原 112 个非零模式；868 个新形状块与 504 个旧块均完整使用。全部 r、base、cut、far、原 sigma、原 577 节点映射由原 adapter 复用。这里没有新的 RHS、root、ODE、局部 J 或 whole-tail J 调用。

唯一新增数值参数是显式给定的正有限 `--eta`。它记录原 CLI 文本和实际解析的 binary64 bits，不提供默认 eta，也不把 eta 当作原接受 tolerance。方向坐标固定为

$$
\delta_n=\sigma_n z_n.
$$

模型是原全部行的 sigma 加权最小二乘加 $\eta^2\|z\|_2^2/2$。每个节点的 $\eta I$ 恰加入一次。cut、stage、far 权重与 R273 的表逐项相同。

## 3. 两次局部 Householder QR 与完整常数项

每段 front 的列是当前 224 个变量、下一节点 224 个变量及一列 affine 值。完整输入包含 carry、当前节点的 $\eta I$、以及原 stage 的全部 224 行。

第一轮 Householder QR 消去当前变量，保存上三角 $R_n$、next 块 $S_n$ 和 affine 向量 $a_n$。剩余 next 行再做一轮 Householder QR，保留新的 carry 和所有纯常数残差 $d_n$。carry 可秩亏；程序不逆 carry、不截秩、不添加另一层 ridge。

最后节点加入唯一的末节点正则项和全部 far 112 行，再完成最后 QR。源码检查恰有 1373 个节点正则块、1373 个 retained factor、307552 个纯常数残差分量，并核实际 factor/constant 字节总量与完整尺寸公式一致。这些是完整性检查，不是几何或 native 容差。

每个非末节点的保存数组是 `[R_n, S_n, a_n]`，末节点是 `[R_D, a_D]`；数学上 $R$ 的下三角显式置零，不把 LAPACK reflector 内存误当三角矩阵。每个 $d_n$ 独立保存。所有数组均为 artifact 的完整 `<f8` 原字节及 SHA。常数能量从这些 $d_n$ 的平方累计，不用两个大数相减来定义。

完整方向按 R273 回代得到 z，再执行一次实际 binary64 `sigma*z` 得到全部原坐标 delta。若乘法产生有符号零，逐项保留并报告操作数/结果例子；不阈值化、不剪切、不删模。原 577 节点限制是该全方向的原字节抽取。

## 4. 形成舍入与两种读回分别记账

原实数组模型中的 stage right block 为 $J_n\sigma_{n+1}/\sigma_n$，affine 项为 $r_n/\sigma_n$。实现明确使用实际 `longdouble` 的乘除，然后一次 cast 成 binary64 front。当前模型的左块 $-I$、cut 的 `[I,0]` 和 far 的 `[-G,I]` 通过同一原 sigma 的实恒等式精确约消，不重付端口。

这不宣称形成是 exact rational RN。运行会记录 longdouble 实际有效位数、范围、每段形成后的完整 V/rho SHA、cast-to-zero 数量和原 sigma bits。形成后的 stage V 不再复制一份巨型阵列到 artifact；它由原 J/sigma 和明确算术路径给定，模型读回时第二次形成并逐段要求相同 raw SHA，保证同一次求解的目标没有漂移。这不是第二次 J 或 RHS 计算。

两种读回的范围分开。

1. **形成后模型读回。** 对同一 formed binary64 V/rho 和 eta，用 longdouble 累计完整 A、A-transpose 行动及 gradient，记录完整模型值、梯度、三角残差、常数能量、factor energy 与 formed energy 的差。它作用于恢复之前的 z，属于数值诊断，不是精确后验界，也不是原 native 接受。
2. **原坐标精确行读回。** 对最终实际 binary64 delta，使用冻结 `0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f` 整数 kernel，完整形成每行 $r+J\delta_{n+1}-\delta_n$，之后精确除以原 sigma。cut/far 同样完整保留。它使用新主矩阵的原未缩放 J/r，完全不使用 formed front，不包含 eta 行。

第二种读回没有形成误差修正 RHS：阻尼方向不需要该 RHS，故不让一次不必要的 float RHS 溢出抹掉本来可保存的 exact residual。全部 307552 行的精确 dyadic 账、逐块最大值、全局最大值、原基态最大值、最坏行完整操作数 bits 和行序均保存。有限数组的 exact residual 仍不声称是精确 nonlinear 导数误差。

无论精确线性缺陷大小，程序都不将它作为原试步的新准入门。它不运行原 native trial，也不声称任一方向 accepted。

## 5. CLI：尚未选参数，尚未运行

所有科学入口要求 `GITHUB_ACTIONS=true` 和本公开仓库。未来如有实际依据决定运行，CLI 为：

```bash
python "$C/exact_20261114_native_damped_chain_qr.py" \
  --capture-directory "$CAP28/native-correction-capture" \
  --step-directory "$CAP41/native-rawcell0-step-capture" \
  --step-result-sha256 6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf \
  --direct-directory "$VISIBLE_OUT/native-rawcell0-direct-ld" \
  --direct-result-sha256 "$ACTUAL_DIRECT_RESULT_SHA" \
  --eta "$EXPLICITLY_CHOSEN_ETA" \
  --max-factor-bytes 2147483648 --exact-workers 2 \
  --out "$VISIBLE_OUT/native-damped-chain-qr"
```

`ACTUAL_DIRECT_RESULT_SHA` 必须取实际已完成 capture 原件；`EXPLICITLY_CHOSEN_ETA` 尚未设置，示例不是可偷偷采用的默认值。可另显式给 `--factor-budget-seconds`；不指定时没有内部 factor 时间截止。资源预算只约束是否能保存完整因子，不允许丢方程或缩短链。

deadline 只在启动下一完整 front 前检查。若 factor 不完整，完整方向不会被宣称已形成；已完成的 factor、formed-stage inventory 和错误仍保留。若完整方向已经形成，原 exact 行账和必要保全不因 factor deadline 被丢弃。

## 6. 输出合同

- `result.json.gz`：完整 schema `complete-native-direct-LD-J1372-damped-square-root-direction-v1`。
- `summary.json`：小于 100KB 的原已存读数与完整结果描述器；超出显示预算只收缩摘要，不否决已完成科学结果。
- `input-binding.json.gz`：完整当前主矩阵身份，原28/41/新capture/source链不变。
- `factor-index.json.gz`、`factor-report.json.gz`：全部 factor/constant 描述器、形成模型身份、节点正则计数、QR 次数、存储与实际时空读数；失败时保留 `partial-factor-index.json.gz`。
- `formed-stage-inventory.json.gz`：每段原 J SHA、两个 sigma bits 和 formed V/rho SHA；失败时保留完整已形成的部分清单。
- `exact-original-readback.json.gz`、`exact-original-worst-witness.json` 和 `large-arrays/damped-direction-all-exact-rows.jsonl.gz`：同一恢复后方向的完整 exact 原行账。
- `output-array-manifest.json.gz`：所有完整数组描述器；大阵均 artifact-only。

顶层方向键保持 `step_delta`、`step_direction_checkpoint`、`restricted_old_node_delta`、`restricted_direction_checkpoint`。但 producer 和 schema 明确独立：full checkpoint 为 `complete-native-damped-chain-direction-v1`，577限制为 `complete-original-node-restriction-of-damped-chain-direction-v1`；不能冒作之前 LU/Newton producer。

`linear_direction_computed=True` 只表示完整 finite 方向已经产生，`diagnostic_completed=True` 表示规定的读回完成；二者都不表示 native accepted。最终原试步仍要在原 577 基态上用原 target/far/全部 guards、原十个 alpha、原 infinity norm 和原 strict 降低规则运行。

## 7. 资源及当前限制

该算法没有完整 normal matrix，也没有完整 dense 全系统矩阵。front 最多 `[672,449]`，保留的完整 R/S/affine 和纯常数 raw 总量约 1.10GB，逐块流写。源码按实际尺寸计算精确字节预算，默认单套 factor 保存上限 2GiB；因子不会整体常驻 RAM。完整原数据绑定、exact worker 整数和 LAPACK workspace 仍另占空间，必须读实际 RSS，不把 factor 磁盘量冒内存量。

各 factor 在反序回代和模型读回前重新核 raw SHA。一次完全 factorization 有 $2D+1$ 次局部 QR；回代有 $D+1$ 次三角解。完整 original-row exact 读回使用一个或多个显式 worker，不重 ODE/J。实际运行时间、factor 残差和原 trial 结果均未产生。

本入口目前只作备用源码交付。它不预言哪一个 eta 会有效，不预言 request54 失败，不把 R273 的精确正则秩下界冒为实际浮点精度，也不改本课题任何完成标准。

## 续接状态（20:18 UTC）

实际54完整capture/均衡方向已存，原trial因旧28文件名错尚无数学结果；55已复用其保存方向进入原试探。root已全文读此42340B源码及接口，只核AST/原源SHA，没有本地科学。若55全拒，首次后继拟明确取eta=1，理由和数值边界见[同尺度单位阻尼合同](2026-11-14-native-damped-eta-one-trial-contract.md)；此刻没有调度R273数值或伪造结果SHA。此追加不改冻结source。
