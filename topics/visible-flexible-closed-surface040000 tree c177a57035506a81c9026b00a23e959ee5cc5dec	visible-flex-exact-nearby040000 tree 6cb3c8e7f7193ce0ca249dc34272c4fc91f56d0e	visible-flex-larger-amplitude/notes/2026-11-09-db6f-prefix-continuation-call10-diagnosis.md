# continuation02：call 10 的真实失败与 call 8／9 对照

作者：`/root/coupled_prefix`，2026-11-09。**状态：已关闭运行记录的元数据核查与数值诊断；不是无解结论。** 主求解器、物理目标、原方程、guard 和容差均未改变。本轮没有新 root、flow、RK、Jacobian、BVP 或连续几何计算；没有中止、重启或接管 root 持有的进程。

## 1. 真实关闭状态及退出码范围

call 10 请求 $s=7/8=0.875$，原十档线搜索在 iteration 3 全部被拒，关闭 trace 的 failure 时间为 **2026-11-09 14:03:29.877 UTC**。原原子响应

`prefix-flat-v17v18-m15-amplitude-continuation-02_tail_0010.json.gz`

SHA 为 `2f6d0b4ba5ac9adf4a0a4c182b4587d7f230a0d57e103a69dbbf543174d37995`，其 `response` 的键集合严格是

```text
failed, lastIteration, checkpoint
```

原失败文字是 `Error: multiple-shooting line search failed at 4892.887571107566`。它**没有** `converged`、`residual`、`history` 或 `audit` 字段。本稿和小报告没有修改这个原响应，也没有给它补造成功协议字段。控制器自己的已闭 attempt 行另有 `converged=false`、`residual=null`；这是原控制器对失败协议的记录，两层 schema 不能混同。

`lastIteration` 实际记录 iteration 3、norm `4892.887571107566`、minA `0.05038380907076433`、minD `0.992549099744137`。保留的 865×30 shape state 及 13 个 raw 节点全部有限，rawStates 与对应 states 逐值一致，但它是 **FAILED 初猜／诊断状态**，不是已解 DN。

这次保存的是一次有限请求返回失败，**不能记成 worker 已退出**。14:08:15 UTC 的控制器观察没有 `worker_exit_code` 键；本稿保留“未报告”，不从响应文件存在推断退出码。metadata 核查脚本本身真实退出 0，不能把它的退出码移用给主 worker。

## 2. 大初始残差不是新现象；线搜行为才改变

三次均使用 M15、N256、physicalDepth12、p8、每 stage 32 步、原 solveTolerance $2\cdot10^{-9}$、maxIterations36。projectionFloor 由原省略键的默认值0.05和保存 CP 参数双核；本轮没有降低它。

| call／s | 第一次完整残差 | 第一次 minA | 原请求结果 | 最后 minA |
|---|---:|---:|---|---:|
| 8／.75 | 8871.20324137 | .4603433652 | 真成功，$7.20944321877\cdot10^{-10}$；5 基点 | .4521271055 |
| 9／.8125 | 9427.83057519 | .3889009364 | 真成功，$3.79627825854\cdot10^{-10}$；6 基点 | .3874099708 |
| 10／.875 | 9818.05219825 | .3158778749 | 原线搜索失败；4 基点 | .0503838091 |

call 8 的原残差链为

$$
8871.20324\to117.772287\to1.929242\to0.001871865
\to7.2094432\cdot10^{-10},
$$

call 9 为

$$
9427.83058\to123.014920\to6.838724\to0.2252365
\to1.5439811\cdot10^{-5}\to3.7962783\cdot10^{-10}.
$$

这两次每个被接受的 Newton 步都是全步，没有 guard／root 拒绝。call 10 的初值只略大于这两个前例，所以单凭初 norm 9818 不能诊断失稳；其后出现的强阻尼则是新的具体事实。

## 3. call 10 的拒绝类型与位置

| iteration | 基点 norm | 基点 minA | 被拒 trial | 接受步长／下个 norm |
|---:|---:|---:|---|---|
| 0 | 9818.05219825 | .3158778749 | 1 次 moment root 线搜拒绝 | $1/2$ → 4921.66987676 |
| 1 | 4921.66987676 | .0864570158 | 2 次 D/S/A guard、6 次 root 线搜拒绝 | $1/256$ → 4902.46237772 |
| 2 | 4902.46237772 | .0547447093 | 2 次 D/S/A guard、7 次 root 线搜拒绝 | $1/512$ → 4892.88757111 |
| 3 | 4892.88757111 | .0503838091 | 1 次 D/S/A guard、9 次 root 线搜拒绝 | 十档全拒，返回 failed |

共 **28 次拒绝**：23 次 `momentum-root-solver-rejection`、5 次 `momentum-guard-rejection`；没有一次被记录为“真实有限残差算出但不下降”。全部记录的位置都在 **rawCell0／rawSegment4，stage32–38**。28 份失败 stage 输入的 SHA／字节、call 对应目标和维数均重新核过。

这些 stage 标签不能自动细化成“第一个 RK 子点 x=0”，本轮没有重新执行内部 root，也不能把旧 M15 其它失败输入的子点定位搬到这里。D/S/A 组合错误文字没有说明究竟是哪一项失败，不能将全部五例改标成 A 单项失败。已接受基点的 minA 的确逐渐贴近0.05；minD 则维持约0.99255。两者支持“当前 Newton 路径受到原 root／guard 可行性约束”的诊断，不支持“同一边值下不存在正分支”。这些 minA/minD 也是有限 source 路径诊断，不是全连续曲面的几何证书。

call 10 因线搜索失败而结束，**没有耗尽36轮预算**。不能把它写成超时或 maxIterations 到限。

## 4. 初猜规则没有在这一步切换

controller 使用物理高度 $h_j(s)=s^j h_j^*$，$j=1,\ldots,15$。worker 虽设置 `harmonicAmplitudePredictor=true`，其谐波分支还要求新请求所有高于首模的高度严格为零；这三次真实请求的高模均非零，始终执行同一规则：

$$
y_n^{\rm guess}=\widehat\rho y_n^{\rm old}
  +\mathcal L_n\left(h^{\rm new}/c^4-\widehat\rho Q_0^{\rm old}\right),
\qquad
\widehat\rho=h^{\rm new}_1/\mathrm{last.jets.height}_1.
$$

$\mathcal L_n$ 是原 `tail.initial` 的有限线性响应；它同时修正 Q 和 Pi。此处没有额外 momentum gauge 或重 remesh。完整公式及实数／保存浮点的区别已由 [独立 warm 源码核查](2026-11-09-db6f-tail-continuation-warm-scaling-static.md) 给出（SHA `0c31f54b321358119bdab570537c3759dd91e67f6aba08d0474a122eacc721a9`）；本稿另核实际关闭输入的标量。

| 转向 call | 实际统一比例 | 按前后请求高度计算的 cut 修正量最大绝对值 | 最大修正所在模 |
|---|---:|---:|---:|
| 8 | 1.0909090909090908 | $4.05448953\cdot10^{-7}$ | 2 |
| 9 | 1.0833333333333333 | $4.39236366\cdot10^{-7}$ | 2 |
| 10 | 1.076923076923077 | $4.73023779\cdot10^{-7}$ | 2 |

表项使用 $h^{\rm new}-\widehat\rho h^{\rm old}$；原 worker 实际按上式的保存 $Q_0^{\rm old}$ 与 $c^4$ 执行除法和加法。另一次只读标量核查确认三个旧 CP 的 $Q_0^{\rm old}$ 均与保存 $h^{\rm old}/c^4$ 浮点逐值相等，但这里不把乘除末位舍入宣称为逐位相同。

这是边界输入层的平滑变化，没有观察到新代码分支或错误 H 标签。相邻三步第15模目标倍率依次约3.6883、3.3222、3.0393，反而递减；不能把最后一个倍率本身作为失败原因。上表没有重建或评价完整 warm flow，不能单独证明实际残差来自某一个高模。

call 10 的第一次完整评价已经通过原 root／guard，minA约0.31588。贴近0.05发生于后续接受方向，故也不能描述为“初猜立即不在可行域”。

## 5. 控制器按原规则回退；下一请求仍未被本文验收

worker 只有 `sol.converged` 时更新 `last`；call 10 的 failed 状态未覆盖 call 9。原控制器随后把本次步长减半：

$$
s_{\rm last}=13/16,\qquad
\Delta s=1/32,\qquad
s_{\rm next}=27/32=0.84375.
$$

14:08:15 UTC 的只读 progress 观察实际给出 current_attempt10、current_requested_scale0.84375、current_step0.03125、last_converged_scale0.8125。观察单列于 JSON，不把活动 progress 文件哈希绑定成不可变的完成证据。本文没有读取或判断下一请求的迭代结果。

最小后续方案就是保留原控制器这次回退和减半，让新请求按原方程、原 guard、原 tol 自然验收。较小步的第15模理想目标倍率降至约1.76139，但这仍只说明输入距离变小，不保证收敛。不从本次失败态冒充 last-success，不降 guard，不改 PDE，不以有限次拒绝证明无解。若以后更小步仍反复受限，再单独评估已成功 CP 的另一种**仅初猜**延拓；本稿没有实施该替代。

## 6. 冻结与复核

小脚本 `scripts/db6f-prefix-continuation-call10-diagnosis.py` 真实退出0。它重新核了 launch 的66项绑定、每份响应的8项实际源码、原配置除5类 I/O 键外不变、物理目标逐项相同、三次物理 H 与原 NumPy 幂路径逐值相同、CP／rawStates，以及所有关闭日志与失败 stage 输入。日志可能含早期 call 的行，汇总严格按实际 call 号筛选，没有跨调用重复计数。

输出同名 JSON（SHA `9590a68b5aff0b916801830a0e964df85a4e2a2bd7c1446fc8066bac02b271b8`）包含66项 launch 绑定、43项其它闭输入、三次各基点／trial 分类、原 closed attempt 行以及明确标为 mutable observation 的控制器状态。它不含完整 shooting 数组，不修改原响应 schema。

复跑仅核元数据，不调用任何原数学 engine：

```sh
cd /workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface
python scripts/db6f-prefix-continuation-call10-diagnosis.py \
  --out notes/2026-11-09-db6f-prefix-continuation-call10-diagnosis-independent.json
```

复跑的闭输入和数学诊断应相同；活动控制器观察及观察时间会随实际状态变化，不要求该部分或整个输出逐字节相同。原调用、来源和报告均不冒充未参与优化者的独立求解重跑。本稿不支付最终 M15 联解、实际 XYZ metric 或 G5。
