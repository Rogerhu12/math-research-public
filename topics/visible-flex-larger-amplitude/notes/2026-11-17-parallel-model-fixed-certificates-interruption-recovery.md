# 两个固定证书批次的中断与不重复续接

2026-11-17。只记录已观察的执行中断，不把它当数学失败或完整终态。原两个工具 session（38130、58019）均已不存在；18:39:50 UTC 的只读 OS 核对也未发现两个 worker。两目录均没有 `result.json`，日志没有正常终态或异常退出尾。最后完整单胞文件时间分别约 18:24:35–36 UTC；中断原因未知。

## 1. 实际保留下来的完整结果

旧 `progress.json` 只每八胞写一次，所以不可用它代替单胞账。新准备入口已逐份读取原报告，核对固定计划键、准确有理范围、所有参数、原输入/源/依赖 SHA、严格覆盖标志和数值 finite 性：

- Gram：710 份完整报告（0…709）全部有效，0 个超界、0 个异常。最大严格界 **2.6347339042318526e-07**，在胞 **709**；还有原计划的109个调用待完成。首缺胞710没有完整报告；无旧逐call开始日志，不能区分它是在计算中被中断还是尚未开始，准确标为 `interrupted_or_unresolved_next_call`。
- 曲率：56个新胞（0…55）的完整 G 证书，加458/817两份已刊复用，共58胞有效、0失败。当前最大上界 **7.046075380943313**，来自原已付817。新λ报告有57份（0…56），所以 **λ56必须复用，只补缺失G56**。剩余为759次λ调用和760次G调用；未重跑已完成代表胞。

这仍不构成全前缀证书。全部原候选26e53、q4096、准确标量、两份原固定计划和角/径向预算不变。

## 2. 最小恢复机制

冻结新源 `parallel-model-fixed-certificates-resume.py`，20391 B，SHA256：

`e024c7aa3d011090d79d00f8db97f931520e0b0abbacf9e24a7487cb71964627`。

默认只准备复用清单，已实际完成两个模式且新几何调用数都是0。执行时须逐字段等于已冻结清单；所有完整旧槽原样复用，原完整失败/异常也不会通过重跑抹去。仅无完整报告的槽可执行一次；首个未决槽与其后未访问槽分别标记。输入/源/清单变化或旧证据身份不符会阻止完整接受。

新源直接调用原 d066 Gram 核、e6 λ 核与582/459 G核；没有更改算术、角网格、径向分割或标量求积。Gram恢复直接调用原engine，没有采用旧driver的启动缓存，因此不声称恢复调用与旧调用具有相同计时。Gram仍16384证明角/4096构造角/4096面板；G仍原Q4096/8sub，已刊817的Q8192/8sub继续复用。新原始输出进入独立 recovery 目录，不覆盖旧日志或旧报告。每次调用开始与完整验证后均写 journal，且每完成一槽保存 progress；若再次中断，可以据这些记录恢复。未新增 reach、闭合或固定g精化声明。

两份冻结清单：

| 文件 | SHA256 |
|---|---|
| `parallel-pulse-gram-fixed-recovery.manifest.json` | `b7f56ca5c0a47dde3ff2b7b4e695b7721aa20db2420ab2a4dbce4aa8708971cb` |
| `parallel-pulse-curvature-fixed-recovery.manifest.json` | `f0e8b5859ff67d3af3220e0cda98163136188093929d3eb6879cae22ad24bac7` |

## 3. 准确入口

在研究仓库根目录，T=`topics/visible-flex-larger-amplitude`，WORK为原仓库外工作目录。分别令 MODE 为 `gram`、`curvature`，已执行下列准备命令；真正恢复只需在同一命令末加 `--execute`。上述两次准备调用均未执行新几何计算：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  "$WORK/parallel-model-fixed-certificates-resume.py" \
  --mode "$MODE" --topic "$T" --work "$WORK" \
  --manifest "$WORK/parallel-pulse-$MODE-fixed-recovery.manifest.json" \
  --outdir "$WORK/parallel-pulse-$MODE-fixed-recovery"
```

全部报告和清单为可再生原始证据，保留研究仓库外；必要科学源与说明进入版本管理。续跑继续原完整计划，不以本次中断或已用时长作为研究停止理由。

## 4. 真实启动回执

18:50:38 UTC 的 detached Popen/start_new_session 尝试在命令返回后没有保留进程；两日志为空、两个新输出目录尚不存在，零数学调用，不把该尝试算成恢复成功。随后采用持久前台执行会话：Gram session57122 在18:50:56准确开始710/all；曲率session58085在18:51:01只补G56，18:51:05已进入λ57。G56确已完成，因此此时完整曲率为59/818、零失败；Gram仍以实际单片journal继续，未预写终态。

实际启动记录 `parallel-model-fixed-certificates-recovery-session-launch.json` SHA256 `ead86dfe7f3b152a374f26347d5c319c10a4812a32958e55f7c981adc8397f9c`。两日志为 `parallel-pulse-gram-fixed-recovery.log`、`parallel-pulse-curvature-fixed-recovery.log`；各新目录仍用第3节outdir。正式保留源为 `notes/2026-11-17-parallel-model-fixed-certificates-resume.py`，与WORK中e024源逐字相同。model是两个固定批的唯一终态读者；未重复完整旧胞或已付λ56。
