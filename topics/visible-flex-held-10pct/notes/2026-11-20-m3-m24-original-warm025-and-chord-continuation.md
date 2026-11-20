# m3：新 g、M24 原首 warm 通过及实际 chord 接续

维护会话：Astra-held10-1b6d88ec-20261120。

本条接 M24 原 linear-DN 合格前缀与独立 bounded-chord 入口。
原 baseline 的首个 `.25 H` 实际 nonlinear shooting 已通过原门并保存
完整状态；这不是 full H 或整个 prefix/trueDN 已通过。随后按已授权计划
中断原 baseline，从它的真实完整 checkpoint 接显式 chord3 算法，
没有重做已完成的 `.25 H`。

## 1. 原路径真实结果

原输出 `WORK/newg-wide-lambda0p002-m24-actual` 的
`tail_0001.json.gz` 在 2026-11-20 13:23:58 UTC 前已完整写出。
2026-11-20 13:24:12 UTC 实际读取并检查了原 converged、原 residual、
完整 states、cutHeight 和物理参数一致性。

- 原 response converged=true，residual=1.8946163107633334e-10，
  低于原 shooting gate 2e-9；无 failed。
- M24、spacing3、physicalDepth8、shootingParts16；1153×48 个实际
  shooting states 全部可读且有限，cutHeight 与 request 完全一致。
- 原 request 为 jacobian=false、audit=true；没有生成 cut DN 导数，
  也没有在 response 中序列化阶段 Jacobian。五次完整 native Jacobian
  仍确实供原 Newton/终态判断实际算过。
- 实际物理 H 的前三项为 -4.042855928697207e-5、
  2.9287203862202366e-7、1.0318183846968562e-8。这是完整 H 的第 j 模
  乘 `.25**j` 的原 warm 目标。

| 原迭代 | shooting norm | 原线搜步长 |
|---|---:|---:|
| 0 | 5271.857359290682 | 1 |
| 1 | 36.07282114693708 | 1 |
| 2 | 10.141214645147677 | 1 |
| 3 | 5.951496780137107e-9 | 1 |
| 4 | 1.8946163107633334e-10 | 已达门 |

该真实尾的原有限 audit 返回 actualMetric=5.10895113851701e-15、
fullD=3.151711866860741e-15、minLeading=.9109817816944088、
minD=.9998014643636979、formalCurvature=8.046307246484698、
maxPhysicalPV=8.083648491780919e-5。它们仅是此小 warm 的原有限
角向/径向 audit，不替代最终 full H 尾、连续全角、无限深或闭口证书。

原完整 checkpoint SHA256：
`302662026a7e213647d8bfb2813f970174c8c919bb6f4d406e073ef9f3c110de`。
紧凑结果另保于 `WORK/newg-wide-lambda0p002-m24-warm025-accepted.json`；
完整可再生 states/J/packet 仍只留 scratch，未入仓。

## 2. 明确中断与独立算法接续

原 worker 在 13:23:58.699 UTC 自动开始 `.5 H` 的 native call10 full-J。
检查上述首 warm 后，按授权给 session42787 Ctrl-C，实际返回 exit130。
原目录的独立 `termination.json` 记录已完成 checkpoint、取消点与原因；
原 run/source/config 保留。这个未完成 `.5 H` 调用被明确取消，不能记成
射击失败或耗时终态。

新 chord3 的第一次启动（session77831）通过原631节点初域门，且原
`initialCheckpoint` 载入成功，随后因新 native run 的父目录 `runs`
不存在，在 native lazy初始化报 ENOENT。14.65秒真实终态，0次数学
native batch，0次射击迭代。该失败目录/trace/run 完整保留；不是 chord
数学失败。补建该父目录后，用全新 `-r1` 输出与 trace、相同完整输入
重新启动，session54314。没有重做首 warm，也没有放宽任何门。

当前实际独立输出为
`WORK/newg-wide-lambda0p002-m24-actual-chord3-r1`；
完整非秘密必要 argv/env 为同前缀 `-command.json`；新 native run 位于
`WORK/newg-bounded-chord-native/runs/actual-lambda0p002-chord3-r1`。
它从原 `.25 H` checkpoint 接 `.5 .75 .9`，然后 full H 和原最多8次外迭代。
这仍是运行中状态，本条没有宣称后续 warm 或原全门通过。

## 3. 完整复现接续命令

WORK 与 TOPIC 取前条安装记录的实际目录。先按
`2026-11-20-m3-bounded-chord-tail-entry.md` 生成独立 chord/native source，
并确保原 `.25 H` checkpoint 的实际 hash 和原 gate 如上。
下列配置生成只加算法键、初猜检查点和日志路径，不改物理 tail 参数。

~~~bash
WORK=/workspace/scratch/1b6d88ecddf3/m3-work
TOPIC=/workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct
python - "$WORK" <<'PYCFG'
from pathlib import Path
import json,sys
w=Path(sys.argv[1])
p=w/'newg-wide-m24-port/tail-settings-chord3-r1.json'
c=json.loads((w/'newg-wide-m24-port/tail-settings.json').read_text())
c.update(chordMaxCorrections=3,
    initialCheckpoint=str(w/'newg-wide-lambda0p002-m24-actual/tail_0001.json.gz'),
    traceFile=str(w/'newg-wide-lambda0p002-m24-actual-chord3-r1-worker-trace.jsonl'))
p.write_text(json.dumps(c,indent=2)+'\n')
(w/'newg-bounded-chord-native/runs').mkdir(exist_ok=True)
PYCFG
env -u LD_LIBRARY_PATH -u LD_PRELOAD -u GITHUB_TOKEN -u GH_TOKEN \
  OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  PYTHONUNBUFFERED=1 \
  VISIBLE_FLEX_SPARSE_PYTHON=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  VISIBLE_FLEX_SPARSE_LINEAR_HELPER="$TOPIC/scripts/nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py" \
  VISIBLE_FLEX_NATIVE_MANIFEST="$WORK/newg-bounded-chord-native/native-manifest.json" \
  VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=00e9fff1b36e5fa56396eb246012aa87e9fc3e7b1afdf24e4f02265568e17d26 \
  VISIBLE_FLEX_NATIVE_RUN_DIR="$WORK/newg-bounded-chord-native/runs/actual-lambda0p002-chord3-r1" \
  python -u "$TOPIC/scripts/resume_m3/portable_prefix_continue.py" \
  --source-topic "$WORK/newg-bounded-chord-native" \
  --short-bridge "$WORK/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py" \
  --profile "$WORK/multistage-linear-root-profile.json" \
  --chart "$WORK/bootstrap/reference/chart.json" \
  --port "$WORK/newg-wide-m24-port/linear-port.json" \
  --tail-config "$WORK/newg-wide-m24-port/tail-settings-chord3-r1.json" \
  --raw-restart "$WORK/newg-wide-lambda0p002-m24-linear/inner-00.npz" \
  --core-module "$TOPIC/scripts/resume_m3/material_support_factory.py" \
  --core-config "$TOPIC/scripts/resume_m3/multistage_wide_circle_lambda0p002.json" \
  --amplitude .06 --warp-reference .06 --modes 24 --angular 768 \
  --audit-angular 512 --nodes 401 --max-nodes 6000 --tol 1e-6 \
  --bc-tol 1e-7 --physical-bc-tol 2e-9 --tail-warmup .5 .75 .9 \
  --outdir "$WORK/newg-wide-lambda0p002-m24-actual-chord3-r1"
~~~

实际运行在新目录，重复复现必须另选新的 outdir、traceFile 和 native
run directory，不能覆盖已登记响应。base profile 的 delta 仍为
.06414432506418023，原 raw 的 p0 再按原语义应用；不能先换成冻结后
的 delta 再把同一个 p0 加一次。

本次实际绑定：

| 对象 | SHA256 |
|---|---|
| 原 M24 linear raw | 1bb631d68796af48821e71baeb696a9ffa7f66f92d7cdcb3af84e27ebe08076e |
| 新 r1 tail config | 635396b13a60d0eafa0483489961edf3b5797ae3f127b0cfd33ff759c5b5e827 |
| 首 warm 紧凑实录 | e3a37543ac57c4ee8a390ec0673cc53776d8114163bd9ab96eee46b5802b8eef |
| 原进程中断实录 | f1d9e88a1e67bf91784784a1e98f88767c5716c1e0007cbcf43a63f8629727fc |

## 4. 保留的验收与未支付项

新算法最多在一个 fresh-J 上做3次修正（fresh步加两次复用），每次
trial 保原真实 residual、10级线搜、域门；返回 DN 前强制重算末态
完整原 Jacobian。原 shooting tolerance2e-9、maxIterations36、prefix
outer8，以及原 prefix metric≤1e-6/BC/真实尾各门全部保留。
`shootingAlgorithm=bounded-chord-v1` 明示算法改变，不能称原路径身份相同。

原 M24 合格 linear 前缀仍只是设计锚；最终 actual tail 完整返回后，
必须重新按最终物理 delta/q/c 生成固定合同，保 mean1168/GL6 与正在
另付的真 primitive/C² 对象之间的区别，再推进固定场细化。本条没有
将小 warm 的机器量级有限 audit 当成固定 g 的完整族或整题完成。
