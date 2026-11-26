# v5 真实 metric-only 场续入与稀疏 LU 资源尝试

日期：2026-11-26。会话：Astra-held10-06bbeb39-20261126。

**实际观察与执行改动，不是新的数学接受。** [第三次实际返回](2026-11-26-v5-third-actual-solver-return.json)已给 λ=.003/M24 完整 raw/physical 场，原 solver/RMS/物理 BC 通过，metric=8.468987358775224e−6 未门。接受锚仍为 λ=.002 的已核同图重表达；不能将该未接受场改称接受解。

[同 VM 已存异常栈](2026-11-26-v5-m32-saved-exception.json)真实定位此前 .004/M32 的 MemoryError 于原 solve_newton 调 SciPy splu。栈不说明第几次 LU 刷新，也不说明旧 factor 当时是否存在。径向分批不减少最终单个稀疏 LU 的内存。本次仅使用仓库现有 streamed_release_prefix_driver.py，在原刷新位置先释放不再使用的旧 factor，并按8个径向点分批评价原 RHS/Jacobian。原方程、完整矩阵、未知量、网格/角频率、物理参数、RMS/BC/metric 门均不变；不承诺逐位相同或资源异常已经解决。

## 直接续入合同

新增 controller 可选参数 --resume-metric-summary 先核真正接受锚，再独立核旧 summary 最后一个真实 solver return：v5 KIND、SOLVER_RETURN、solver_invoked、原全部非metric门、有限超门metric、raw/physical SHA、完整 baseline/provider/scale、除 λ 外的固定设计输入。旧 summary 的末 stage、最后接受锚和 λ、首 pending target 都须与实际字段一致。这里只恢复已有数据责任，没有增加数学接受门。

此处实际未接受 seed 为 attempt-002/run.json（908a480127f769124731af36bcf64196b7507de9b49a85ecbd78194ad7cdbd40），首 pending=.003、M24；直接进入下一声明档 M32，调用原完整 lift 和真实 phase embedding 检查，然后运行原 BVP。不重求 zero/M24。若新 BVP 失败，仍回真正接受锚进行原二分；失败 seed 不成为下端。

--streamed-rhs-block 8 显式保存真实 wrapper argv、wrapper SHA、其实际 radial-batching.json SHA、block 与原 driver SHA。wrapper 内部实际保存的 portable argv 必须吻合；不会伪改 run.command。旧 summary 的旧 controller SHA 与新 controller SHA 分列。entry/factory 均不改。

## 同 VM 实际请求

```sh
python @REPO@/topics/visible-flex-held-10pct/scripts/resume_20261126/warm_delta_phase_continue_v5.py \
  --repo @REPO@ --work @WORK@ \
  --source-run @WORK@/fresh-v5/v5-material-design/zero-control/run.json \
  --resume-metric-summary @WORK@/fresh-v5/v5-material-design/summary.json \
  --streamed-rhs-block 8 --max-attempts 3 \
  --outdir @WORK@/v5-resume-m32-stream8
```

复用 run45822332434/job139917497866；新 id 为 held10-v5-metric-resume-m32-stream8-20261126-01。本记录登记请求，不冒充 worker 已启动或 solver 已返回。每段返回后继续真正接受/未接受状态，三次段预算不是课题结束。

controller SHA256：626e11c9522df6367cac8724d8ea6a47b11e932469a922685c0c2cb8247356b1。断线前该版本 py_compile 已实际通过；CLI help 在仅 setdefault 失败记录健壮性调整前已实际通过。源码差异已读，原实际 driver 命令记录语义已核。fresh recovery harness 仅同步此 controller 的声明 SHA，原6801-byte q/M24恢复块及所有数值门不改；本次续入不经过恢复 harness。

当前只补真实输入断点和资源执行路径。full-H、固定完整 g 精化、共同 Cartesian 两jet、λ1 与完整闭族均未由此支付。
