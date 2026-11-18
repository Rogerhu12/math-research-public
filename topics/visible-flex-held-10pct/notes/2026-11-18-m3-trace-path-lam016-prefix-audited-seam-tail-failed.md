# λ=.16：原内解与真尾接受，完整前缀审计保存，接缝尾失败

## 已完成与未完成的部分

[唯一 λ=.16 续接](2026-11-18-m3-trace-path-lam016-coupled-entry.md) 这次无需外部邻数初值就完成了原内解和原新 H 实际尾。原 outer BC 也通过，完整物理前缀、mean-height 积分和 prefix audit 已即时保存。随后物理 quintic 端点提出略有舍入差异的新 H，原接缝尾在停止门失败；本轮不能记为完整联立终态。

| 阶段 | 真实结果 |
|---|---|
| 原 `solve_bvp` | success；494 节点、2 次 mesh 迭代，RMS=$9.880114855350935\times10^{-7}$ |
| 原 Newton 参数/状态迭代 | 5 次接受步，全部 α=1；域和 merit 拒绝均为 0 |
| 原节点 H 的实际尾 call 1 | 6 次原 Newton 修正后接受，residual=$1.83393059818419\times10^{-9}$；完整 208 个有限 Jac 元素及 audit 返回 |
| 原 outer 0 BC | $4.410472343803251\times10^{-11}$，通过 |
| 物理前缀完整有限 metric | $1.3837763095648974\times10^{-4}$，已保存，仍未达到最终 $10^{-6}$ 目标 |
| Cartesian Darboux 读数 | $.11186743320536596$，已保存 |
| 原物理端点 H 的接缝尾 call 2 | 迭代 0 原 line search 失败，norm=$3.66786119636838\times10^{-9}$ |

原尾 call 1 从 norm 约 62.1126 逐步下降；最后原线搜索取 α=1/512 后通过原严格 $2\times10^{-9}$ 门。这不是额外邻数算法的成功，也没有改原门。call 2 没有返回接受 audit。

## 已保存的真实恢复材料

执行目录：`m3_work/trace-path-lam016-coupled-v1`。

- 原完整内解 `inner-00-returned.json.gz`：`62e1c1e1567bf8827fb4d21bd4a5ec11284920d172c14e853503db1dc5fd4ebf`。
- 对应 DN 锚侧文件：`69ba65416c53b91e6e87ee6491ba63a9bc3ea01f65dd8ef93712799814f60a3b`。
- 原节点 H 真接受尾 `seed_tail_0001.json.gz`：`c807ab79ef1ca6d6a4b7954c9632d1defdee6e29bb1cf3380b737ffb7387c406`。
- 接缝新 H 原失败尾 `seed_tail_0002.json.gz`：`69e2d545dad75affedcde4872fcdf2fc86bb0e42234489c21887b58f81eed5bd`。
- 已保存完整 prefix audit 的物理 CP `seed.json.gz`：`f60de678f4a99595e0caba4ecd8c9379fb8b607522956d7bb9769559282cb797`。其中原内解成功及 prefix summary 都是真实已有数据，但 `tail_seam` 未完成。

原全部 8 参数、7 个物理控制、normalized 节点/状态、原 cubic 和 RMS 都保存；没有从物理 quintic 反造原 cubic。新同伦的 source、qseed/gauge、base profile 与完整 `p0` 语义仍沿入口，不是固定 g 精化。

## 接缝差异与接续边界

这里原 raw 节点 H 和物理 quintic 端点 H 只有分量 0、3 不同。它们都是真正求值所得，不能相互冒充逐位相同。实际首幅值比为 `1.0000000000000002`；比较已存原接受和原接缝失败状态，原 warm predictor/边界处理后共有 18106 个状态标量不同。这是下一次明确保留已接受内部/深端状态、只重新编码新 cut Dirichlet 初值的具体依据。

下一接口不需要重复内解、前缀 mean-height 积分或已经保存的完整 prefix audit。若新接缝 H 得到真实原尾接受响应，只须恢复这张实际物理图并完成原 seam audit。新初值本身不算接受；仍由原 worker 的全残差/Jacobian/audit 门决定。本条保留原失败，不预认后续修复结果。

## 实际运行记录

session **49902**，启动块 `9a2486`，真实终态块 `8d9e0f`。observer 于 **2026-11-18 04:31:37 UTC** 记录 child=0，worker=0；原 main 如实记录数学异常及 `solver_success=false`。进程 exit 0 不等于完整数学成功。

[只读紧凑终态记录](../scripts/resume_m3/trace_path_lam016_coupled_terminal.json) 给出全部来源、命令、状态 hash、两次真实 H 请求、参数及已有审计标量；沿用已提交 collector，不构造模型或重算任何数学。完整 metric 高于最终目标的短缺仍保持，不因中间 continuation 接受而放宽本题完成标准。
