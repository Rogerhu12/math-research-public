# 同一 HoldProfile 到 1.03 的完整 BVP 原预算失败与实际定位

本条是已登记 1.03 准备之后的**唯一一次完整求解**及只读诊断。保持全部 M160/N2048、482 ODE、325 左行、157 冻结右 Schur 行及其非零参考目标，前三 core、标量 g、全部原门不变；`tol=1e-8, bc_tol=1e-11, max_nodes=1800`。不读取 1.04 失败场作父，不启动替代 solver。

## 原预算终态

运行 2023.02 秒，完成 11 个完整 QR。602 节点首轮的 8 个内部步后，原 RMS 为 `3.60e-3`，原规则加 1117 节点至 1719。第二轮接受两个小步，第三个 fresh-J 的全部 17 次试步无下降，保留旧点；再拟加 3269 节点，所需总数 4988 超过 1800，故正常返回 `status=1, success=false`。未装配第 12 个 Jacobian；不是 singular-Jacobian 终态。

终 RMS=`0.0433480621660537`，边界最大误差 `4.85722573273506e-17`。最后一个完整线性系统的绝对残差 `1.05572746590e-14`，除完整 collocation+BC RHS 最大值 `4.25269495821e-7` 为 `2.48249045904e-8`；此比值不是 PDE 误差。峰值 RSS 为 1814000 KiB。

下表由冻结 `feasible_newton` 与原 `separated_qr_solve` 日志逐步核出：每个 finite trial 必调用一次线性 solve，扣除各 fresh-J 的初始线性解即可计数。没有虚构未记录的每次坏点/角度。

| 网格 | 内部步 | 接受 α | finite trials | nonfinite trials |
|---:|---:|---:|---:|---:|
|602|0|1/1024|5|6|
|602|1|1/512|1|9|
|602|2|1/256|2|7|
|602|3|1/16|1|4|
|602|4|1/8|2|2|
|602|5|1/64|1|6|
|602|6|1/16|1|4|
|602|7|1/256|2|7|
|1719|0|1/4096|4|9|
|1719|1|1/8192|4|10|
|1719|2|未接受|4|13|

最后 17 次试步含 13 次非有限残差与 4 次 finite merit 未过；最小实际试 α 为 `1/65536`。合计 104 个 trial、10 个内部接受，不等于 BVP 接受。

## 缺陷实际集中在哪里

诊断固定保存值及实际 RHS 所定义的原 SciPy cubic，不改变场；重新调用原 Lobatto RMS 规则，全部 1718 胞有限，**保存/复算 RMS 最大差为 0**。

最坏胞为 1642，区间 `[1.0261263240374572,1.0262652808411958]`。其 midpoint `s=1.0261958024393265` 的完整 ODE 系数缺陷最大 `0.00459066577936`（Z 第6模），相对向量 L2 为 `0.0547237531653`。这里属于 rise、仍早于真类型界面 `1.0283496328972757`；参考曲率约 `−0.800276`，不是旧桥、固定负曲率 hold 内的 1.0066 点或末二 jet 外推区。

| 原参考区间标签 | 最坏 RMS |
|---|---:|
|旧 prefix|3.85633e-5|
|原 warm 桥区|3.67471e-5|
|余下 curvature fall|1.53731e-4|
|negative-curvature hold|1.93294e-4|
|rise 至真 κ=0 界面|4.3348062e-2|
|界面后的显式参考区|6.27065e-4|

这些标签只定位空间区间，未把全局 Newton 后的场冒作仍等于原桥或二次参考。

原 N2048 的节点、中点、两个 RMS 点全部通过 Q/W/H 采样门。N8192 节点也通过，最紧 H=`1.30343935895e-8` 在上述胞右端。但 N8192 对同一 cubic 的中点、左右 RMS 点各发现一个坏点，均属胞1642：中点 H=`−3.57138e-7`；左 RMS 点 `s=1.0261503181485079, φ=0.26231071472844464` 有 H=`−5.97992865971e-7`、H/W=`−0.0720107`；右 RMS 点 H=`−1.89391e-7`。这是指定加密采样结果，非连续区间证明。

因此，本次实际失败同时包含未消除的完整 ODE/RMS 缺陷、角网格之间的域退出及有限节点预算。不能仅归因于末端二 jet 参考过长，也不由此推出同 g 无解、所有边界失效或新隐式表示必成功。失败输出不作父，不生成其几何通过或固定 g 收敛声明。

## 冻结身份与复现

已刊 solver 生成器 `parallel_20261117_hold_short_bvp_run_generate.py` SHA `d46cd5fb136ae92f3d93138ea7a95099915e41254cc2ff359b438005f799d53a`；其固定原完整 solver 为 `f93d74382ac83bee08079759ca17cace95b3e99cb765e706e6d1ef67c7861d81`，实际生成源为 `af0e5ab2d198c1a475b51a35b57f4a6ced171595b96a8e4d905377adfb404c9c`。新只读源 `parallel_20261117_hold_short_bvp_diagnose.py` SHA `f12c444f5f192b9262018bbd09eca16862d2734447267c9c13ffb34365b2b7fa`。

固定 warm=`1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057`，冻结 arrays=`2d3c4133959e662b87289fb26fd1aa2c73d2a1ddd278e8f0e1d23fbc1b9d6f7e`，HoldProfile=`ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`。用已刊 1.03 准备配方再生输入，令 T 为课题目录、S 为仓库外目录：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$T/scripts" \
python "$T/scripts/parallel_20261117_hold_short_bvp_run_generate.py" \
 --base-source "$T/scripts/parallel_20261117_hold_full_bvp_once.py" \
 --generated-source "$S/parallel-hold-short-bvp-run-source.py" --topic "$T" \
 --warm "$S/parallel-hold-m160-short-bvp-warm.json.gz" \
 --arrays "$S/parallel-hold-m160-short-bvp-arrays.npz" \
 --hold-source "$T/scripts/parallel_20261117_negative_hold_profile_ivp.py" \
 --out "$S/parallel-hold-m160-short-bvp-once.json.gz" \
 > "$S/parallel-hold-m160-short-bvp-once.log" 2>&1
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$T/scripts" \
python "$T/scripts/parallel_20261117_hold_short_bvp_diagnose.py" \
 --input "$S/parallel-hold-m160-short-bvp-once.json.gz" \
 --log "$S/parallel-hold-m160-short-bvp-once.log" \
 --hold-source "$T/scripts/parallel_20261117_negative_hold_profile_ivp.py" \
 --audit-angles 8192 --out "$S/parallel-hold-m160-short-bvp-diagnosis.json"
```

实际仓库外输出 SHA256：

| 文件 | SHA256 |
|---|---|
| `parallel-hold-m160-short-bvp-once.json.gz` | `e313da8db55cb1729c142f877324b352334ff030b350d9dc7f618b3753f410b5` |
| `parallel-hold-m160-short-bvp-once.json.report.json` | `bdcb6250a161691f694c468804fbb483fa99a102189a0332959dfb5ac29fdc61` |
| `parallel-hold-m160-short-bvp-once.log` | `aad042eeda8d10257a6ccb8a1c46ef0ab9dd2d45950fc4779ad996b6cfdfdd54` |
| `parallel-hold-m160-short-bvp-diagnosis.json` | `222138e8e30039cd609522a718b2e125f1ca5b3fa6bff109a06c7fc575b5d4ab` |

报告含计时/路径，跨环境不要求其字节相同；原真实输入、源码与数学字段须核。所有 raw、log、expanded source 和报告留仓库外。
