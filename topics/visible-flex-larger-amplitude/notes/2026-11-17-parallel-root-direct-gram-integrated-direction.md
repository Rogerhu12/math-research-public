# R647：全 Gram–T 的唯一真实满步方向

本条消费85c准备/b1c报告/70c尺度，执行且仅执行一个完整LSMR方向和一个alpha=1试点。它是新完整Gram目标的实际结果，不能改写旧Pr预算的收敛门。原1662同g、M160/N2048、602节点、全部1158250行及580328未知/964边界保留。

## 实际固定调用

可逆T保留所有C/U/D。联合边界投影包括原482位置条件和482个U0=ez条件；所有初始列矩直接复用70c，不重算。固定mu=1、atol=btol=1e−8、conlim=1e6、maxiter256，LSMR实际256步、istop=7，256次matvec及257次rmatvec，96.711296秒。返回的条件估计约9.51015不是整体精确条件数。全程序103.119984秒，最大RSS446964KiB。

**这是固定迭代额返回，不是线性收敛。** 显式正则normal残差L2为1.8866726814522458e−8，相对值5.470492532467464e−5。

| 完整Gram量 | 实际数值 |
|---|---:|
| 初始全行SSE | 1.4951624510753042e−9 |
| 线性模型SSE | 6.191012874365848e−10 |
| 满步真实SSE | 6.191013184119097e−10 |
| 预测下降 | 8.760611636387194e−10 |
| 真实/预测下降比 | .9999999646425087 |
| 满步节点系数最大 | 1.9566420834815216e−6 |
| 满步中点系数最大 | 1.7204323484087522e−6 |
| 原位置BC最大 | 5.551115123125783e−17 |
| U0残差 | 字面准确0 |
| max deltaY / max deltaU | 1.4428569546212544e−8 / 7.461689338565369e−7 |

本目标的精确二次射线余项为q=(deltaV·deltad/a, |deltad|²/a²−deltarho², |deltaV|²)，边界余项0。特别是第二项保留共享核心的负deltarho²，不能借用旧Pr的q。实际全q平方和1.0551277318834953e−22；真实满步减r+Jdelta+q的最大差约4.45746e−12，发生于短胞中点，节点约1.29683e−15。不是把浮点差报为准确零。

## 完整物理样点及仍有的失败

同一满步Y/U进行了唯一完整8192角、602节点和601个实际cubic中点检查。rho、Q、W、H及正分支法速度在全部这些样点均正：最小rho=.16601843095975743，Q=.027562119418339526，W=.00021883032194409225，H=.00021208491223043653，法速度=.01456220042749131。

实际共同cubic相对Gram最大 **4.980386907216856e−6**，最坏在节点600、s=1.0299174816448637、phi=1.4603497100671303。原始不变几何的已付初值为7.5050072699644945e−6；本次没有重审原初值。下降后仍超过1e−6，且峰值就在节点；任何仅保Y/U重选共同加速度A的方案都不能修复该节点。故不启动此类无效A-only试验。

原物理读取器附带的Pr点残差第二组可达.01589104625306703。它们属于另一个微分目标，不参与本次Gram目标的接受判定，也不能被低Gram SSE隐去。满步通过原始merit、联合BC和样点分支条件；`accepted_parent=false` 保持。

浮点位置投影产生160个非零核心Z槽，最大2.4645024459428988e−32；U0字面为ez。此数组仍不能声称核心镜像位置严格为零。当前只有C¹分段cubic，未定义共同C²加速度；更没有连续域度量/曲率、闭合、reach或固定g实际精化。

## 原始身份与可复现入口

算法 [parallel_20261117_direct_gram_integrated_direction.py](../scripts/parallel_20261117_direct_gram_integrated_direction.py)，SHA `513aa782ee2da6bc61acb3c7e5df2c2585e4f3e917b76836946284394253306d`。

本次原始证据均保留仓外：

- 完整报告 `parallel-root-direct-gram-integrated-direction-once.json`，SHA `81c8d13152a5b31229395c148d8d115ab3d071b421b92cf1e31f8acd04b884b4`。
- 完整方向NPZ，SHA `11550c74cc98c95864625b499d90aa136b56961452f266f314672cf3dea51447`。
- 实际candidate NPZ，SHA `0bf58beddf796479af2baed4dc8039fc6da97d6168834e12c151dfc552ae8608`。
- candidate Y/U二进制SHA `3ddd76ccc283aab650277fb0799e0d94b0a430708047402d761f145c393aae0a`。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python parallel-root-direct-gram-integrated-direction.py \
 --topic math-research-public/topics/visible-flex-larger-amplitude \
 --problem-source parallel-model-implicit-frenet-newton.py \
 --warm parallel-hold-m160-short-bvp-warm.json.gz \
 --polynomial-source parallel-root-implicit-frenet-probe.py \
 --matrix-source parallel-root-implicit-matrix-free.py \
 --gram-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_direct_gram_matrix_free.py \
 --coordinate-source parallel-root-integrated-coordinate-preparation.py \
 --preparation-source parallel-root-direct-gram-integrated-preparation.py \
 --prepared parallel-root-direct-gram-integrated-preparation.prepared.npz \
 --preparation-report parallel-root-direct-gram-integrated-preparation.json \
 --out parallel-root-direct-gram-integrated-direction-once.json
```

报告身份含本次路径/时间，仅标识此次实际证据；冷重建的新身份须真实记录。本次方向/physical可作为独立新Gram固定预算的方向0完整复用，不重付；其新终门和最多24方向/20接受须另行明确，不因复用而暗改原Pr任务。
