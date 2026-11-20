# 实际 M8→M12 完整参考传递与真实高模端口

维护会话：Astra-held10-1b6d88ec-20261120。

## 实际返回

公开 Actions run44720589640 的同一个 runner 保留了旧物理 g 的 λ=.02 原场。
在未删改原域门的条件下，这次 M12 exporter 与完整 lift 传递实际 exit0，
状态为 `nodal_initial_guess_ready`。这只是原 BVP 的新维初猜；没有 M12
BVP、真实非线性 DN、metric 或闭面通过的含义。

原输入实际 raw SHA256 为
`2a6f97324986437e2f065bf29e98d55b48e43cf19a3bb9fc321fad7b27d197a4`，
旧场 N1024 的 relative operator 峰为2.1302182023390677e−5，仍不合格。
它的完整 Frenet R 以未知投影带外 ψ26—50 壳为主，见同日实际审计记录。
因此此步扩大未知空间，而不是再次改变审计节点来重评同一失败场。

真实 M12 linear port 用原 exporter 生成，angular quadrature 从128增至256，
满足引擎原条件 N>4M×spacing=144。第一次 N=128 exporter 的失败保留，
没有降低检查门。该 angular quadrature 是数值尾角求积设置，closing_recalibrated_tail 建背景时把底层 modes/steps/quadrature固定为1/1/16，
其积分另由 calibrationSteps、warpSteps与求积容差决定；故该256角设置不进入背景assemble。
完整固定 g 身份仍须依照原背景定义核对，不能只凭
短 port 的 cut 或部分参数推出所有精化都同 g。

完整参考差按 R48/R49 加入 `aχ(Inew−Iold)`，其系数是1。
材料核心 λ=.02 不乘在此补偿上。实际2048角×103径点检查如下：

| 完整 jet | 最大差 |
|---|---:|
| 位置 | 3.19264533430656e−16 |
| ψ | 3.3917531705969593e−16 |
| ψψ | 7.947987303456224e−16 |
| s | 2.3281675882275486e−16 |
| sψ | 7.351053198070336e−16 |
| ss | 3.999211501054847e−15 |
| ρ | 0 |

这些是同一公式的浮点接口检查，不是连续范围证书。入口投影改变
2.1505121850230283e−6，必须交由随后原边界方程校正，不把该初猜直接接受。

## 原始数据与复现命令

完整可再生数组只留 runner 的 WORK，不进入 Git 或 artifacts。

| 对象 | SHA256 |
|---|---|
| M12 initial.npz | `58546880d4d66e4ab0ddd8bc538e07eeb090cd4f5b70a234f14e061f5d9d057e` |
| 新真实 linear-port.json | `e59fd73d1ca019ff9891d72af9a31489cc90e64c5cb8a199eb2882ecd7ef3f38` |

其中 WORK=/home/runner/work/_temp/held10-live。输出目录
`material-lam002-m12-transfer-v2` 内同时含 tail-settings.json；本次 prefix
angular=384、modes=12。已实际执行命令为：

```bash
python -u topics/visible-flex-held-10pct/scripts/resume_m3/prepare_lifted_mode_restart.py \\
  --source-run "$WORK/material-lam002-linear/run.json" \\
  --modes 12 --tail-config "$WORK/inputs/q060-tail.json" \\
  --outdir "$WORK/material-lam002-m12-transfer-v2"
```

实际调度环境先清除子进程继承的 LD_PRELOAD、LD_LIBRARY_PATH，验证原 Python
仍可导入 NumPy2.3.5/SciPy1.17.0；原 native loader guard 保持。
单独的 M8 true-DN corrector 已进入 native_ready，登记本条时没有最终尾返回。
这个工程状态不判数学成功或失败。

随后使用本次 initial.npz 和新 linear-port.json 求 M12 原 linearDN；
λ、旧物理 profile 和所有最终门不改。若 δ 或支撑控制继续变化，则属于
设计延拓，不能登记为 README 要求的全部物理参数固定的误差精化。
紧凑实际返回见同名 JSON。

