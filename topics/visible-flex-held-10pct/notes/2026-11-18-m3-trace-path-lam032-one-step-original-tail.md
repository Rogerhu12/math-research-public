# λ=.32：两格与一格残差，各走一邻数后原尾接受

**状态：数值证据；原求解器的完整停止门真实通过。**

针对 [λ=.32 的实际新 H 原尾失败](2026-11-18-m3-trace-path-lam032-inner-accepted-tail-failed.md)，一次完整失败行重放发现了与前两步不同的情况：一个超门分量距离保存 flow 两个相邻数，另一个距离一个相邻数。没有套用旧脚本的“每项一步恰到 flow”前提；只让完整超门集合的每项各朝 flow 走一个相邻数，执行一次组合候选。

原 fresh 受影响全行给出的有限上界过门后，唯一原 worker 在 iteration 0 真实接受：

$$
\mathrm{residual}=1.8339186209756414\times10^{-9}<2\times10^{-9}.
$$

全部 208 个有限 Jacobian 元素和完整 finite audit 返回，最终 $1153\times16$ 状态与候选逐位一致。原 H/配置/方程/停止门不改，已经接受的原内解没有重跑。

## 实际完整行与唯一变化

原 full-Jac 路径逐位重放原失败 norm=$3.667837241951283\times10^{-9}$。完整超门集合只有 stage/node 86 的下列两项：

| 分量 | 类型 | 原 state | 保存 flow | 唯一新 state |
|---|---|---:|---:|---:|
| 9 | mode 6 momentum | 313.2630705193686 | 313.26307051936874 | 313.2630705193687 |
| 11 | mode 12 momentum | 636.0290738585496 | 636.0290738585495 | 636.0290738585495 |

第 9 分量只向正方向走一格，**仍留一个 ULP**，绝对残差为 $5.684341886080802\times10^{-14}$；没有将它写成零，也没有再走第二格。第 11 分量向负方向一格，恰到其保存 flow。Python `math.nextafter` 独立核对两个实际步长及完整状态差集。

所有其余分量最大为 $1.8339186209756414\times10^{-9}$；cut 为 0，deep 为约 $2.55324\times10^{-14}$。唯一组合初值只改这两个自由内部标量，随后新求原 stage 85、86 的全部 16 个分量：

- stage 85 全行 norm：$3.0558212588986265\times10^{-10}$；
- stage 86 全行 norm：$1.8339186209756414\times10^{-9}$；
- 加上已保存未改变行/两端的整体上界：$1.8339186209756414\times10^{-9}$。

该组合量是有限局部依赖给出的上界，不声称又做了一遍全候选 replay。原 native 随后独立完整检验全部行与原域/Jac/audit，真实接受同一数值。

## 最小规则派生

[候选源](../scripts/resume_m3/propose_complete_row_one_step.mjs) 从旧 `65d1dd…` 独立派生，只将“每个超门成员必须恰一邻数到保存 flow”改成“每个成员朝其保存 flow 各走一邻数，且旧输入 flow 差严格缩小”。受影响及上游完整行集合、原 full-Jac flow、未改变行界和严格门不变。

[原请求入口](../scripts/resume_m3/solve_complete_row_one_step_original_tail.py) 对应改用新候选源 SHA，并独立核对 `adjacentTowardFlow`、`math.nextafter` 和剩余差；之后仍只有一次原 worker 请求。没有新增坐标轮流试探、候选扫描、第二步、H 扫描或 gate 调整。旧两源保持原字节。

两个新源 SHA 分别为 `2c0fddb9d6f0932d41ccf2d5cfaace3d734f28c946a2dc29f05d0debb2bdfd42`、`b3bf456201f7319439e86f9ec1bc354b2f86a53dfe38c99c5e17e4f6ee97b3b2`。完整 3+3 处字面派生保存在 SHA `e680128f843076409c498916d288f7a24b14c80f7bbe7a645edfe739e6f387ec` 的 scratch manifest 中。语法核没有执行额外数学。

## 真实运行与接续

| 阶段 | session / 终态块 | 终态 UTC | child/observer |
|---|---|---|---|
| 原完整失败行 | 33004 / `09c0a0` | 2026-11-18 04:42:08 | 0/0 |
| 唯一各一步候选 | 44597 / `bb9547` | 2026-11-18 04:44:27 | 0/0 |
| 原 native DN/Jac/audit | 43436 / `816188` | 2026-11-18 04:46:54 | 0/0 |

原 native worker 也真实 exit 0；重新加载 ratio=1、边界修补为零。接受文件 `m3_work/trace-path-lam032-native-one-step-v1/seed_tail_0001.json.gz` 的 SHA 为：

`5e1634539b56ed8bca2a9f7d505f28b9cfe2351da748589c658cd5870bc2e33d`。

完整旧失败、全行、候选、真接受、源、参数及实际命令见 [紧凑执行记录](../scripts/resume_m3/trace_path_lam032_one_step_execution.json)。它已交通用 pending 恢复器接原内解 `71a9f0…` 的 post-tail 流程；本条不预认后续 full metric 或接缝成功，也不从这个有限邻数案例推出一般机器误差下界。
