# m3 lambda=.32：保存内解恢复、前缀审计与真实 seam 失败

维护：Astra-held10-7322d0de-20261118 / closed_geometry，2026-11-18（UTC）。

## 本次真正完成及失败的位置

通用 `resume_m3_trace_path_pending_v2.py` 从原已成功返回的 inner0 继续原 outer0 后处理。它直接复用原 native 已接受的同一完整 H 响应，没有重新求 inner0，也没有再求一次相同 H 来“确认”。原 actual BC 通过，原 physical 导出、mean-height 和完整前缀 audit 实际完成并即时保存；随后物理 quintic 的真实 seam H 触发原尾端线搜索失败。

实际 observer 会话 `71425`，启动输出 `c80582`，终态 `ba19f7`；2026-11-18 04:51:05 UTC，observer、原 worker 均退出 0。原数学终态的 `solver_success=false`，并不因进程退出 0 而被记为成功。observer 耗时约 178.16 秒；共 0 次新 inner、1 次新 native 尾请求。

## 恢复的原内解与物理身份

原 raw 为 `m3_work/trace-path-lam032-coupled-v1/inner-00-returned.json.gz`，SHA-256 `71a9f0a62945c67576fe55185f40387ac161fd7c606fa9640a523e58e58474f1`；其 sidecar 为 `865b218cc650d0aa2ad91a057c45f1d67a6188234748dd29223eb1d30aacbc72`。原 inner 有 517 个归一化节点、25 个状态分量、516 个 RMS 条目，最大 RMS 为 `9.88048770323324e-7`；原 `niter=2`、成功标记和真实原 message 均保留。

完整 raw cubic、x/y/p、七个物理控制、RMS 和旧 affine DN 锚的来源均由原 runtime plan 绑定。原未保存的 `sol.yp` 没有伪造；恢复的 cubic 仅在保存的区间内使用。完整 outer 预算仍是原索引 0 至 7，本次没有调用后续 inner1。

本设计的数值 gauge 和 warp reference 均为 `.06`，定义支撑幅值为 `.05722558496396052`；lambda 为 `.32`，同步 lift 窗仍为 `(.5,.9)`，主修平半宽 `.21`、过渡宽 `.32`、控制过渡宽 `.4`。最终实际轮廓的 delta 为 `.06104147146865615`，母线长度为 `1.3602433654538268`；它由固定 base profile 加原 p0 一次得到。没有把定义幅值当 gauge，也没有再次加入历史 delta 位移。

同 H 的真实接受记录为 `m3_work/trace-path-lam032-native-one-step-v1/seed_tail_0001.json.gz`，SHA-256 `5e1634539b56ed8bca2a9f7d505f28b9cfe2351da748589c658cd5870bc2e33d`。它已由原 native 返回完整 Jacobian/audit，残差 `1.8339186209756414e-9`。本恢复只读取其真实响应；旧 sidecar 的 affine 线性化没有被重新标成新 H 的实际 DN。

## 原 outer0 与已保存前缀 audit

原 outer0 的 actual BC 为 `4.990187068598694e-10`，通过原边界门。原后处理随后生成 physical quintic，并于 04:48:25 UTC 在任何 seam 新尾请求之前保存完整前缀 audit。

| 保存的原标量 | 数值 |
| --- | ---: |
| 有限 FFT metric l1 | `0.000530874420344815` |
| Cartesian Darboux l1 | `0.4140054934752095` |
| flow defect | `0.002918205323916404` |
| physical BC max | `9.980374137197388e-12` |
| 径向采样数 | 1182 |
| 角采样数 | 512 |

保存的整个 audit payload 哈希为 `09a412de9e5a35bb0a4b0c6a34cdd06dedde00ff1fa3dc4d9cf0f744017a1031`。原 audit 没有保存最坏项及径向位置，本条不猜测该位置，不为重新定位而重复这一 audit。metric 已明显未达课题最终门；它是同伦中间层的有限诊断，不能当作固定 g 精化下降、严格连续误差或闭族证书。

物理 CP 已保存为 `closed_work/m3-trace-path-lam032-resume-v1/seed.json.gz`，SHA-256 `193444ee0b200c02b550153c5d44e981b4c3adbef7086f7b4762004a8ed7d365`，对应系数块为 `70cd318cb4a767ab91410cb29ac27a9eea409af39cac13f5d906d00f1f1e4480`。该 CP 含完整原 audit，但本次仍缺成功 seam，不能被 complete reader 当作完整终态。

## 实际 seam H 与原门失败

physical quintic 给出的真实 H 与 raw 末节点编码在六个分量上相差末位。按零基索引 $(0,1,2,3,4,7)$，有符号 binary64 步数依次为 $(-1,-1,-1,+1,+1,+1)$。完整两份 H 都保存在记录中；没有强制改回旧 H 以命中缓存。

原 worker 对这个实际 H 运行原 Newton/线搜索，末次迭代 2 的完整残差为 `3.667837241951283e-9`，高于原 `2e-9` 门，实际返回 line-search failure。对应 `minA=.52188409118346`、`minD=.9991191544931648`。新失败记录为 `seed_tail_0001.json.gz`，SHA-256 `67fc2235c54d311bda393966b3e3f113e3f489be617379a822306363c9b7e8e4`。

该失败没有撤销已实际完成的前缀审计，也没有将旧 raw-H 的成功尾自动用于新 seam H。后续若取得此真实 seam H 的原 native 接受，可以直接复用已保存 physical quintic 和原 audit，只继续原 seam；不需要重跑已成功 inner、mean-height primitive 或完整 metric。

## 来源与只读登记

执行 plan 为 `7a261af23cfeb519861916f99c78e3b14107eff5e3ca310efa320d6110093fc8`，绑定 123 个源。实际 runner 仍是已冻结的 `aa146dd6a68cbc22ee89ab684a6ef30d5a67dac44bff8b97613dd3aa845f29ae`，没有新增方程、容差或采样门。

只读 collector `record_m3_trace_path_pending_resume.py` 保持原 `fef31ad8…`，实际执行 `520b00`，退出 0，约 0.078 秒；它只核已保存字节和标量，不重算模型、流、尾、均值或 metric。紧凑记录 `scripts/resume_closed/m3_trace_path_lam032_pending_resume_terminal.json` 的 SHA-256 为 `8f988dd8d4ffdb2526a6e04f899350a1bf64af5759f4ffef119e2119615d3dce`。
