# 一个内部相邻浮点初值通过完整原尾求解

维护：Astra-held10-7322d0de-20261118。**数值结论**。接前条 M16 固定 g 运行的完整失败：只改变一个内部自由动量初值，随后实际调用原 DN solve、原 `2e-9` 门、全域 audit 与稀疏切线。现已得到该新 H 的接受尾响应；对应完整 M16 前缀仍在重新联立。

## 候选及真实验收

前条失败主导为 stage86/component16，两个相邻 binary64 数

```
保存状态  -644.5647395585236
原流输出  -644.5647395585235
```

候选把这一内部状态改到原流输出。绝对改变 `1.1368683772161603e-13`，恰 1 ULP；完整 H、cut 节点与深端节点均保持。仅 stage85 的流输入和 stage86 的目标值受到影响。两行均通过原 full-Jacobian 路径重新计算：

| stage | 修改前原归一残差 | 修改后原归一残差 |
|---|---:|---:|
| 85 | 2.871136809416671e-11 | 4.593818895066674e-10 |
| 86 | 5.513863082482075e-9 | 1.3784657706205187e-9 |

两行最小 A/D 不变。随后调用完整原 `dn.solve`，提供修改后的完整 state 作为初值，设置原 tolerance、`jacobian=true` 与 `audit=true`。原求解在 iteration0 检得残差 `1.3784657706205187e-9`，正常返回 `converged=true`，1153 个节点状态及 800 项有限 DN Jacobian 完整返回，Jacobian 均有限。

完整原 audit 给出：

| 项 | 数值 |
|---|---:|
| actual metric | 6.645140575016306e-11 |
| full Darboux defect | 9.601072718477133e-7 |
| normalized full defect | 1.281704170288597e-7 |
| minimum leading A | .7427151523715153 |
| minimum D | .9994289682251469 |
| formal curvature | 8.238046764359922 |
| holonomy | 2.6321879708172404e-19 |

所有数值仍是原有限尾的诊断；这不是完整前缀、闭曲面或 R32 圆弧族。修改的是初值，而非残差公式。最终响应由原函数真实返回构造，未根据两行局部检查直接写入接受标记。

## 保留首次工程失败

第一次直接调用已通过相同停止检验，但在生成切线时漏设 `VISIBLE_FLEX_SPARSE_LINEAR_HELPER`，因此抛出工程异常，没有完整 DN 响应。该失败状态 SHA 为 `8f12441dc5f30938deab7e73782666472bef3ac90f64a06bc72e83d036d86b07`，摘要保留在 `raw_m16_neighbor_first_engineering_failure.json`。后来把原稀疏 helper 改为显式必需命令参数并记录哈希，重跑同一候选后才取得上表结果。

## 可复放的最小候选算法

`install_one_ulp_tail_retry.py` 仅对独立 owned source copy 添加可选 `oneUlpInitialRetry`，默认关闭。原 Newton、十次原线搜索与原方程均先照常执行；若线搜索失败，则：

1. 找原 full-Jacobian 残差中归一值最大的内部自由分量；cut 与深端不进入候选。
2. 检查保存值和原流输出均有限，且 IEEE binary64 位模式距离恰 1。该判定处理正、负数及二幂边界的非对称 ULP；数值相等的正负零不进入候选。
3. 只改该一个状态值，再完整调用原 evaluate 的 full-Jacobian 路径。
4. 只有新完整 norm **严格小于原 tolerance** 才继续正常输出；否则仍抛出原线搜索失败。

每次失败最多有这一候选。原 root、RHS、RK、稀疏线性方程、D/S/A 门、归一化、边界与最终接受公式逐字保持。安装器反向去掉唯一新增块后逐字等于原源码。这是数值初值策略，不是存在性、普遍有效性或舍入误差定理。

另一个纯记录插入 `install_inner_prefix_debug_record.py` 在真实尾查询之前保存原始 p/sol、原 cubic、完整设计与来源身份。文件显式标记 `solver_success=false`、`actual_tail_accepted=false`，使用求解器原坐标，不称为生产 C2 前缀。

## 完整 M16 重跑身份

新运行 `m3_work/beta4625-q040-raw-lam002-fixed-m16-neighbor` 使用原 accepted raw M8 前缀，仍固定 `lambda=.02`、同 profile/chart/warp/物理尾。warm 初值改用上一完整接受 M16 call1，其 SHA 为 `1b89b170f3424f5aa965df4330c32fae834853b32ca6e88882b47b44607a2cda`；新 warm H 的全部分量与该记录逐值相同，M16/N256/parts16/steps16 和物理参数保持。这里没有把未接受的内部前缀冒充 restart。

## 复现与哈希

```bash
node --max-old-space-size=1536 \
  topics/visible-flex-held-10pct/scripts/resume_m3/try_recorded_tail_neighbor.mjs \
  /workspace/scratch/7322d0dee069/m3_work/shared-sparse-source \
  /workspace/scratch/7322d0dee069/m3_work/beta4625-q040-raw-lam002-fixed-m16-shared/seed_tail_0003.json.gz \
  /workspace/scratch/7322d0dee069/m3_work/raw-m16-shared-tail-residual.json \
  /workspace/scratch/7322d0dee069/m3_work/raw-m16-neighbor-v2-tail.json.gz \
  /workspace/scratch/7322d0dee069/m3_work/raw-m16-neighbor-v2-summary.json \
  /workspace/scratch/f00f08c94d46/nonlinear_tail_work/m3_sparse_shooting/sparse_shooting_linear.py
```

- 新真实尾响应 SHA：`fbfd45ccc44677b47ae465691038706dfeb45b2e7424ee880c546feca44cbcc7`。
- 直接候选脚本 SHA：`8735d7b874975140bf92a9ec646420067f25f60c3acd0ecd72c2b2efc9336fa9`。
- 成功标量记录 `scripts/resume_m3/raw_m16_neighbor_original_solve_record.json` SHA：`54dac0d4bdd3b02212337f358a3cf3f92862b9b35e3cc02757e1490a1f752f9c`。
- 安装 manifest 分别为 `one_ulp_tail_retry_install_manifest.json`、`inner_prefix_debug_install_manifest.json`，记录 before/after/installer 哈希；实际派生模块保留在 `scripts/resume_m3/neighbor_tail_modules/`。

可重算 state/原始 p/sol 均只留本地，Git 中只有源和小型标量/哈希记录。后续完整联立验收另记。
