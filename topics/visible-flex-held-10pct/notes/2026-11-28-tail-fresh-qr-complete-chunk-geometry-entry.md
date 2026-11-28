# 真正 QR final physical-H 的 fresh 全尾小块导出入口

状态：**工程接线与写入合同已实现并检查；尚无新 λ1 几何阳性返回。**
本条不重算旧 R90 的 1152 段证书。

## 原有缺口

旧 `actual_stage0_after_full_height.py` 绑定原 λ=.002/M24/raw-H 特定输入。
旧 `chunked_tail_geometry_resume_v2.py` 从真实的 −9 和部分 inner suffix 恢复，
不能为了给未来新 λ1 导出而虚构该失败或先故意运行一次超大 Node 进程。

新 `scripts/resume_20261128/tail/qr_complete_tail_geometry_chunks.py`
直接从新 QR/native4/chord3/8outer 的实际最终 physical-H 开始。
它先调用 `qr_actual_coupled_prefix.accepted_coupled` 的全部真实来源门，
再使用原 `resume_20261126/seam_run_tail_geometry_v2.py`
（SHA `c165678d912761163ef29cfca1eb9c4dfc4bbf3102de6a00b228ca537f727615`）
的 background、stage0、完整 merge/index 和原连续证书流程。
没有产生新的 native/BVP 求解，也没有改原 finite-map 或证书数学源。

## 实际完整定义

入口使用 QR summary.result 的真 final run，
height-reference 指向其真实 full_height_binding 的 `candidate_H`，
factor=1、原 numpy 高度算术。
raw-H 另列，绝不替换该定义。
native record 从该真正协调器的 `summary.parent/native-runs` 搜索，
并由原 `select_native` 逐个完整 state 精确匹配；不是用猜测的 packet 同目录。

stage0 首先由原 exporter 生成；其全谱 contract、global mean chain、
所有 Cartesian 两jet和证书均作为本新场的真实输入保留。
后续默认每批 8 段，允许 1–16 段，从内到外生成。
每个批次共用原未重置 global mean；
除 stage0 实际 inner node 外，续批还绑定上一批真实 outer node。
不是独立拼接多个场或逐批重定 mean。

每个保存段重新检查原 stage/status、boundInput、完整 spectrum/spectrumContract、
sourceSHA256、mapHash、physicalParameters、有限值和 mean-chain 两端身份；
相邻段的 literal radius 及完整 Cartesian/Fourier value/first/second coefficients 必须准确相等。
总段数由真实 mean chain 得到，不把未来输入锁到旧 1152 或 M24。
原 merger 再检查全 stage 覆盖、stage0—stage1、全部邻接并建立完整 canonical index。
新 sidecar 明示实际所有 chunk/component/额外边界锚；
原 bundle 的 legacy “sole explicit anchor” 文字保留为原字节，不被冒充本次完整施工说明。

## 可恢复执行与资源

每次真实子进程 dispatch 前先保存原数学 argv 和真实包装 argv；
随后记录实际 PID、/proc start ticks、command SHA、boot ID 和实际观察到的 returncode。
同一 outdir 有 flock，仍存活的同身份 child 阻止重复启动。
若先前 child 终态未知，只把它确实已写完且逐字绑定的完整 stage 当作已保存段，
不从进程不存在推断 returncode。
未知/未保存部分由 `--resume` 接着生成；已有完整段不重算。

只有原子进程实际负 returncode 或 ≥128 的已观察异常退出才允许缩小下一 chunk；
数学正失败不被自动改成成功，原日志、原 source/mean、所有已写段继续保存。
最终 complete 的 metric、曲率、deep collar、投影单射等原门全部保留。
原内部 K<10 预算失败仍会给原“不在 allocations 内”的结果，
不会因新包装或已有更宽几何界而改写为通过。

原 `geometry_disk_guard.py` 和 `.mjs` 继续分别保护科学输出所用的
`Path.write_text/write_bytes` 和 `fs.writeFileSync`，
每次写前实际要求 free ≥ 完整待写长度 + 至少 128 MiB。
这不是对所有系统调用或其他进程占盘的保证。
新 `geometry_recursive_write_guard.py` 把同一 Python guard 传播至嵌套 Python；
`NODE_OPTIONS` 传播原 Node guard，故 stage0 内部的 Node 也受到相同写门。
新 guard 的 dispatch 小日志也使用受门保护的 Path write。
默认 Node heap=512 MiB，允许明确另设 ≥256 MiB；资源选择不改原数学输入或验收。

## 真实检查

环境 reset 后，最早一次 help 因整个旧 checkout/依赖暂缺而实际 exit1；
这不是几何或数学失败。恢复 checkout 与两个新源后：

- 两源编译及 fresh 入口 `--help` 实际 return0。
- 实际 I/O-only probe 分别执行未包装与包装的同一 Python→Python→Node 过程；
  两个 256-byte 测试输出逐字相等，SHA 都是
  `40aff2e9d2d8922e47afd4648e6967497158785fbd1da870e7110266bf944880`。
- 真实两个嵌套 dispatch 已记录：Python child 的 argv 加入 guard；
  Node argv 本身不改，继承原 Node preload。
- probe 完整小 summary 为
  `held10-design-work/fresh-geometry-resource-dispatch-check-20261128/summary.json`，
  SHA `a307ef49c7ba35443b465bbefaa6980ac98786bf7926db73580e1c62a83c60b8`，
  实际 runner exit0。

这个 probe 只核执行/写入组织，没有构造数学测试场，没有跑 native/BVP，
没有假 λ1、假 source gate 或新几何证书。

原 exporter 源码直接核实：
stage 与 manifest 都把同一 `physical.parameters` 写作 physicalParameters；
所有段同一 input/sourceSHA256，shared node 保留原 mean chain。
原 pipeline 的 stage0 证书、合并和 complete 返回原样继承。
读代码核同不冒称已运行未来 λ1 的正向输入。

## 源码及复现

| 文件 | SHA-256 |
|---|---|
| `qr_complete_tail_geometry_chunks.py` | `0bc3a31e348a5885b45ae082486aa470d39693684d3960bcd3ead61cc35fd5ee` |
| `geometry_recursive_write_guard.py` | `3a3f864be6047953e26c7a54bea352a294c12a5217cc8104a67547bf0ad34fa4` |
| 原 `geometry_disk_guard.py` | `be2b17d39083db9bb437cfe6732e5de2e342eab9a7c9189149a914898fd0926c` |
| 原 `geometry_disk_guard.mjs` | `ed84e80264979153f8d4c54d5ef25598d6b1235f7166e1c170b7d745e0dca9f0` |

真实新耦合终态到来后，从它的 summary.result.run 取唯一 final run：

```text
python scripts/resume_20261128/tail/qr_complete_tail_geometry_chunks.py
  --source-run <actual-final-QR-run.json>
  --coupling-summary <actual-QR-coordinator-summary.json>
  --outdir <fresh-outside-repository-geometry-root>
  --phase all --chunk-stages 8 --node-heap-mib 512 --disk-reserve-mib 128
```

路径从 topic 工作目录解释。实际可用 `--phase stage0` 先取得新 cut，
随后原 outdir/完全相同数学输入 `--phase all --resume` 继续。
若中途停止，同一 `--resume` 按完整逐段 receipt 接回。
没有旧 1152 数值重生、旧 bounds 继承或完成标准降门。
