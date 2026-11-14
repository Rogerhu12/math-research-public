# M15 的首个真实有限尾 warm：s=.25 已收敛

状态：**启发式/数值结果，原有限 shooting 真收敛；完整 prefix 仍未匹配。** 2026-11-09，coupled_prefix。root 独立持有并观察了实际工具会话48634自然返回 exit 0。

成功响应为 `prefix-amplitude-recovery-s025-iter004-01_tail_0001.json.gz`，SHA256 `07db124d2da380171b99e6d577255b43d4f5496fbd6d982d5dea1a6df873c2e5`，273159 bytes。本节 notes 短名统一位于 `notes/2026-11-09-db6f-` 下。

## 1. 真正通过的条件

独立只读检查得到 `response.converged=True`，原 normalized residual

$$
1.5422380425305446\cdot10^{-10}<2\cdot10^{-9}.
$$

请求使用原 `jacobian=True,audit=False`；全部705个原 DN Jacobian 条目有限，实际 source audit 为空。恢复过程有13个 history base 态，最后 iteration12 的 minA 为 $.9039699504468596$，minD 为 $.9978542869609943$。这些是原 finite-N/RK 评价中的数值量，不是连续角或整个显式 XYZ 图的严格界。

response.request.height、checkpoint.cutHeight 和中断前目标逐值同，且逐值等于冻结 affine 目标的 $H_j(.25)=.25^{j+1}H_j(1)$（存储下标 $j=0,\ldots,14$）。整个物理/离散参数表除此前明确授权的六个恢复选项外相同：恢复初猜路径、剩余轮数、trace 路径、iteration 路径、trial 路径、失败 stage 路径。M15/N256/depth12/p8/steps32/floor.05、原度量与原容差均未改变。

原 worker 的实际退出码为0；完整 runner summary 无 error。root 的工具观察、UTC和八份已闭输出 hash 在 `root-amplitude-recovery-s025-observed-execution.json`。本文没有从进程消失推断退出码，先前 continuation01 的未知退出仍保留原中断记录。

## 2. 迭代与计数

原中断进程完成了0–3的四个接受更新，又评价了 iteration4。恢复从同一个 iteration4 状态出发，首个 base 的 residual/minA/minD 与保存态逐值同。

恢复 history 有13态、12个接受更新；其 iteration11 的残差约 $2.38510\cdot10^{-4}$，最后一次全步把真实 residual 降到上述 $1.54224\cdot10^{-10}$，随后的完整原 Jacobian 评价确认停止条件。

因此去掉重复恢复基点后，轨迹有17个不同的 base 态、16个接受更新。实际记录的全 Jacobian base 评价则为原5次加恢复13次，共18次。二者不同是恢复时重复评价了同一个 iteration4；不能将18次资源消耗写成17次。

恢复 runner wall time 为约2820.93秒。它使用原36轮预算中的剩余32轮；没有借重新起算扩大这一次请求的原接受更新预算。

## 3. resume02 的精确接续

`scripts/db6f-prefix-prepare-amplitude-resume02.py` 只读核验成功响应、原容差、真实 H、完整物理/离散参数、原 controller/client 及来源哈希，然后生成闭合结果 JSON 和 launch。它不启动 solver。

原 controller 不会自动从 `--resume-checkpoint` 的 history 选择下一步长。已记录轨迹长度超过7，所以 launch **显式**使用 `--initial-step .0625`，对应原 `.125` 首步按既定规则折半；`--resume-scale .25`，下一个请求为 `.3125`。继续使用原36轮 config、原 controller、原 guard/RK/tol，目标始终是同一个冻结 H(1)。

启动绑定在 `prefix-amplitude-resume02-launch.json`，SHA256 `b2e7371a89906a5f1048077eb2040fef8f2c0a58a136ef3812ab6cbc36b5310e`。root 已独立核66个绑定及原 H(.25) 并持有新的会话17869。本次 closed inventory 排除 resume02 的一切活动日志、进度、iteration和响应。

准备器最初曾因比较了包含恢复 I/O/预算字段的整个 parameters 字典而拒绝；这是纯元数据检查，未启动任何 solver。旧 source snapshot 和 `prefix-amplitude-resume02-setup-rejection.json` 已保留。修版只排除与原 runner 六个显式 overrides 完全相同的键，其余全部参数仍逐值比较。

## 4. 范围

成功只属于 $s=.25$ 的有限尾边值，尚未到完整目标 $s=1$，也没有重新求出实际 M15 prefix/tail 联解。这里没有新的 sourceFullD、actualXYZMetric、全图连续 metric/reach 或无限尾存在性结果。后续仍须成功接续到 $s=1$、执行原 audit、原实际 prefix 外层校正，并继续完成固定 g 加密门。
