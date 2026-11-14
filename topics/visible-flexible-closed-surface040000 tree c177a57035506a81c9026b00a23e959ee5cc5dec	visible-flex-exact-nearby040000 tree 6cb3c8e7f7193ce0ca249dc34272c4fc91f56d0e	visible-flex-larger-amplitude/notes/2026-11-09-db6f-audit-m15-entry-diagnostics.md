# M15 首 RK 失败与正 floor 探针的独立审查

审查者：`/root/independent_geometry`。状态：**只读诊断方法、数据语义与独立完整复跑 PASS**。未参与候选优化；没有产生 root、stage 或 joint 解，也没有非存在性结论。

## 1. 冻结对象

全文核查了：

- `scripts/db6f-tail-diagnose-failed-stage.mjs`，SHA256 `d46112eb867814128862b276a2775524840dd13ab6692bd6c593279d779fd8a2`；
- `scripts/db6f-tail-moment-positive-floor-probe.mjs`，SHA256 `0daac9cb19aa312c55a1817adabab13f06338a6b4a8e9d306da4a000c0bb8670`；
- 两份说明 `db6f-tail-m15-first-rk-failures.md`、`db6f-tail-m15-positive-floor-probe.md`（在 `notes/`，均带日期前缀）。

同时读取冻结原源的 momentum engine、fast momentum、fast split engine、split RHS、cusp wrapper，以及本题 shooting subdivision、trial core 的阶段输入语义。没有更改这些文件或当前活动 worker。

## 2. 原方程及记录方法

`createFastMomentumTailEngine` 保留原 `createMomentumTailEngine` 的 root、geometry 和 evaluateL；快速部分改变的是变分计算。fast split 也保留这个 root，并使用已审的 split RHS。因此 companion 用原 momentum engine 重放局部 root 与失败入口的原 root 相同，不是换了一套隐含方程。

诊断脚本从冻结源原样抽取 `solveSPD`、`root` 与 split `rk4`。独立 Python 审查器按相同唯一标记重新切片，SHA 与诊断输出的抽取片段完全相同。注入的 evaluateL 记录层最终调用原函数，Newton 步、Cholesky、20 次回溯和原停止条件均不变。提前得到 root 后以 `knownRoot` 传入原 RHS，没有重新写 RHS 或添加接受规则。

独立记录器的 $P,P_\theta,L,D,S,A$ 用原代码相同的项次和算式计算；所有成功 evaluateL 的最小值必须逐值相同。原 guard 失败时，记录器额外遍历所有角点给出的最小值仍只是有限样本诊断，不能视为连续角域的区间界。

subdivision 的阶段以 `states[n+1]` 作为输入，积分局部坐标从 0 开始，恰与原 trial core 相同。原 profile 坐标由 `rawLeft+(rawRight-rawLeft)*x` 得到。五个实际段都无内部 cusp breakpoint，因此首错误位置确为第 0 普通 RK 步的 k1，而不是未保存的更深 RK 内点。

## 3. 替代种子与较低正 floor 的范围

第一份诊断始终使用原 floor=.05。$L=-w^2P_\theta$ 的种子在实数公式中使 $A=1$，但脚本仍重新执行原 D/S/A 全部采样 guard，没有把 $A=1$ 误当成其它正性也自动成立。

只调整均值的种子使用

$$
D=ES-w^2(1+L-P_\theta)^2
$$

及 $A>\mathrm{floor}$ 的线性约束构造候选区间。由于这里只是数值初猜，脚本不把浮点求出的区间称作严格可行域；候选仍再次通过原 guard 才调用原 root。替代种子没有送回 RK 或 shooting。

companion 按 root 已明确授权的单点诊断，把正 floor 分别设为 .05、.025、.01、.001。固定的状态、moment target、背景和方程均不变；改变的是这个诊断调用的正性接受阈值。原函数与记录函数在每个配置中都重跑，并要求成功/错误一致；成功时还必须有 L 系数的逐字节一致性。

全部 8 个局部调用仍失败，因而 N512、N1024 与更密角检查的后继列表正确地保持为空。不能把这些未发生的工作填成通过。

## 4. 实际独立重放

使用作者给出的同一 config、五个保存的 trial stage 输入和原 base iteration checkpoint，另行输出：

- `notes/2026-11-09-db6f-audit-m15-failed-stage-replay.json.gz`，163021 字节，SHA256 `1aee13edf8b9a3be009930d35f86c2be92d034c535ee29919024d1887814f5f5`；
- `notes/2026-11-09-db6f-audit-m15-positive-floor-replay.json`，27257 字节，SHA256 `a8cd4b7dedc94a1d6c564495289195e4ad014e7053b42cd00eae3bc2cf93f56e`。

两次 Node 进程均实际退出 0，分别耗时约 3.76 秒与 3.21 秒。第一份原 JSON 立即以确定性 `mtime=0` gzip 保存，没有把大数组输出到对话。

完整 JSON 的所有字段（只除顶层运行时间 `seconds`）与作者原报告逐值相同。输出 hash 的差别来自运行时间，不是数学数据差别。输入、所有源文件、原样抽取片段的 hash 也已重新核验。

独立后处理脚本为 `scripts/db6f-audit-failed-stage-replays.py`，SHA256
`775565d3766eff2dd2af5ef0fd1a609244cc4990a9efe3930e57f32730a9f750`；报告
`notes/2026-11-09-db6f-audit-m15-entry-diagnostics.json`，SHA256
`18719428b3c5e299339cedeca395aa7ebb0b04e7b8f0e7aa092467a64fcbe720`。

```bash
python scripts/db6f-audit-failed-stage-replays.py \
  --stage-replay notes/2026-11-09-db6f-audit-m15-failed-stage-replay.json.gz \
  --floor-replay notes/2026-11-09-db6f-audit-m15-positive-floor-replay.json \
  --out notes/2026-11-09-db6f-audit-m15-entry-diagnostics.json
```

该命令实际退出 0。它确认五个失败 trial 的成功完整 RK 步数都是 0；单独的成功 base 控制例才有一整个 RK 步与原实现逐字节相同。成功控制输入与失败 trial 输入明确不同，不能把前者偷换成后者的恢复结果。

另按 config 重建实际 source 参数并与保存入口比较，共有 55 个共有键。仅 `depth` 和 `linearMethod` 的数值标签不同：前者在 factory 中是 raw depth，在保存 shooting 记录中是分段后的 stage 数，而 `physicalDepth` 保留同一 raw depth；后者是派生 shooting 方法名。所有其它共有键逐值相同，见 `db6f-audit-m15-stage-source-identity.json`。首次直接要求这两种数值标签也相同的检查安全拒绝，明确区分其定义后重查通过；未修改源函数或参数。

## 5. 通过的结论

五个保存 trial 都在实际 stage 入口失败。前四案默认初猜直接触发 A guard，最后一案先通过初始 guard，随后在原 Newton 回溯中失败。D 与 S 没有接近当前正 floor。可行种子以及授权的较低正 floor 没有得到该入口的成功 root。

这些事实可以排除对**这些已保存调用**的错误位置解释。它们没有证明 guard 域内无根，没有证明 $A>0$ 的有限 moment 方程无解，更没有证明固定 $g$ 的完整精确族不存在。说明稿对这一范围的限制正确，无需数学修订。
