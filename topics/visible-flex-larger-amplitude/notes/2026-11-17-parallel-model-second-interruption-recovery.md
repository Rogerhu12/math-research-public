# 两固定几何批在19:49附近中断后的仅缺项续接

2026-11-17，parallel-model。**运行状态与完整复用账，不是全域科学终态。** 所有 raw、manifest、日志均在仓库外。

## 1. 已观察的中断

19:52:54 UTC，旧曲率 session58085 和支持 session34099 均返回 Unknown process id；两套进度已停约249–252秒，均没有 result.json，当前可见进程表未见匹配旧 worker。因此没有把消失的句柄当成完成。

曲率完整报告有686/818胞，0失败，最后中断在 G685；其 λ685 已完整落盘，必须复用。支持完整报告有249/819片，含原五代表与244次后续调用，0失败；中断调用为245。完整报告逐一按既定 source/input/参数/准确片范围及所用 λ SHA 核对后保留；未完整写出的当次调用如实记为中断，只在新目录再次执行。后续未访问项按原计划各一次，未改变任何科学预算。

## 2. 曲率第二续接

新胶水源 `parallel-model-curvature-second-recovery.py`，6091 B，SHA `20c03e7f957bd122c520a2e0ba03c12a966a8d91ad46c35b1408ca0ba8fcc3f1`。它只把已完成第一续接报告覆盖到原 manifest，再调用**未修改的 e024.execute**。所以科学执行报告中的 source_sha256 仍是 e024；新胶水身份额外写入 manifest 与终态 overlay-execution-binding，不把二者混作同一来源。

原执行源 `parallel-model-fixed-certificates-resume.py` SHA `e024c7aa3d011090d79d00f8db97f931520e0b0abbacf9e24a7487cb71964627`；原818胞计划 SHA `df745a9b3c204aaea2f1fee568282be24a13b1db7245095a743b52690fbf6602`。

新 manifest `parallel-pulse-curvature-second-recovery.manifest.json` SHA `dc74a04ae6d916e486a1c96e61c08369783faefffa3159573658218eab6dbc4a`：686 个完整 G 复用，**仅131个新 λ 调用与132个 G 调用**。G685 使用已成 λ685；全部818胞、Q4096/径向8sub、817既付Q8192/8sub、准确scalar分片均不变。源和完整旧证据变动会停止，不加密、不替换候选。

从仓库根实际使用：

```sh
W=/workspace/scratch/16f63c8bce6b
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
 "$W/parallel-model-curvature-second-recovery.py" \
 --engine "$W/parallel-model-fixed-certificates-resume.py" \
 --topic topics/visible-flex-larger-amplitude --work "$W" \
 --prior "$W/parallel-pulse-curvature-fixed-recovery" \
 --manifest "$W/parallel-pulse-curvature-second-recovery.manifest.json" \
 --outdir "$W/parallel-pulse-curvature-second-recovery" --execute \
 > "$W/parallel-pulse-curvature-second-recovery.log" 2>&1
```

删掉 --execute 可在新manifest路径只做准备。本次准备中一次绝对 topic 路径被原计划的字面路径身份门拒绝，没有科学调用；改回原计划的上述相对路径后准备退出0。实际续接 session80092，首G685使用旧λ后成功；19:56:52累计已704/818、0失败。输出目录同上。

## 3. 支持量续接

新胶水源 `parallel-model-weighted-support-recovery.py`，11285 B，SHA `187c3990b414ebe40a8f8f232720cf943de7e9e3d117f02f922b7930457b6d61`。只调用未修改 f115 reader 的 certify；原97a707源只提供同一元数据/原子写盘函数。全部819准确片、Q8192/4sub、β=1/4及每片既付R648 λ/λs界不变。

新 manifest `parallel-pulse-weighted-support-recovery.manifest.json` SHA `447150d49573f80b9db282f68fc585c21b4ecd224e33c02467c897e3e13cc814`：249完整报告复用，含原五代表；仅570未完整片调用，新 λ 计算为0。已完成失败或异常也会保留而不重试；本次旧报告恰无失败。

原819计划 SHA `a2acf3719692e360f8e5a4d0dce1777882494a05286700ae82c5ff7a5561899b`；原五代表聚合 SHA `48d5d0523e0fb3d0d850ccc543cdc25d74feab387c002354fbf85a99f0b03e52`。

```sh
W=/workspace/scratch/16f63c8bce6b
T="$W/math-research-public/topics/visible-flex-larger-amplitude"
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -u \
 "$W/parallel-model-weighted-support-recovery.py" \
 --batch-source "$W/parallel-model-weighted-support-fixed-batch.py" \
 --reader "$W/parallel-geometry-weighted-support-interval.py" \
 --input "$W/parallel-pulse-a5-complete-base.json.gz" \
 --interval-source "$T/scripts/parallel_20261117_arclength_interval_positive.py" \
 --gram-index "$W/parallel-pulse-gram-fixed-recovery/result.json" \
 --component-source "$T/notes/2026-11-17-parallel-root-pulse-curvature-component-box.py" \
 --plan "$W/parallel-model-weighted-support-fixed-plan.json" \
 --representatives "$W/parallel-geometry-weighted-support-representatives.json" \
 --prior "$W/parallel-pulse-weighted-support-fixed-20261117" \
 --manifest "$W/parallel-pulse-weighted-support-recovery.manifest.json" \
 --outdir "$W/parallel-pulse-weighted-support-recovery" --execute \
 > "$W/parallel-pulse-weighted-support-recovery.log" 2>&1
```

实际唯一续接 session18950，第一调用245已经成功；19:56:52累计253/819、0失败。没有重算五代表，也没有用不同 β 或粗细网格替代任何失败项。后续全覆盖结论必须消费真实终态、全部报告与最终资源，另行登记；上述中断恢复本身不证明闭合、reach或README第5项。
