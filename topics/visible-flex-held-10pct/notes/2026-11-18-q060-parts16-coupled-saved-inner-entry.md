# q060 parts16 联立重启：保存原 inner 与真实 DN 锚点

**执行入口，尚不声称新的联立结果。**

原 call3 的 $H_{\rm new}$ 已有原 native parts16 接受态
（SHA `850f81a202d0092b8c7b44c4bcf86904fdf3d105101322140ce32a1d8a0251cf`），
见[唯一邻数初值与原验收](2026-11-18-q060-parts16-named-neighbor-original-acceptance.md)。
旧 prefix inner cubic 没有保存，不能事后复造。因此现以相同原输入重新
执行原 q060 coupler，并在每次新高度请求前保存原 inner 与实际 affine-DN
锚点。新 session33116 使用独立 observer，输出前缀为
`closed_work/q060-coupled-parts16-v1/seed`。

## 精确命令与变化范围

原执行命令来自
`m3_work/beta4625-q060-local-tail-retry/seed-design-initializer.json`；
计划清单 `entry-plan.json` 同时保存原、新完整命令数组和逐项差异。
配置只改 shootingParts $8\to16$、initialCheckpoint 到上述实际接受态，
以及 traceFile 到新输出路径。

命令改动仅为 owned source overlay、tail-config、out-prefix，
bridge/chart 的同字节当前路径，以及 node heap2304→3072 的资源设置。
bridge SHA `7e00a333…`、chart SHA `14f326e2…` 已与原输入核为同字节；
新执行不依赖旧 session 目录可见性。sparse helper 使用当前 publication
副本，SHA `a52567b2…`。

原 profile、port、q040 restart、restart-port 全部保持原文件和 SHA。
仍为 q=.06、warp-reference=.06、M8、angular256、audit-angular512、
nodes801（原 initializer 实际形成815节点）、max-nodes6000、
tol $10^{-6}$、BC-tol $10^{-7}$、physical-BC-tol $2\times10^{-9}$，
warmup-scale1、lagged-tail。
port 的全部物理参数与新配置逐项相同，其 parameters 不含 parts 字段。

owned source 由 `prepare_recovering_tail_source_v2.py` 生成。
原 coupler `37defb33…` 只增加已发布的 raw inner dump 和一个 DN 锚点
sidecar 调用，逆补丁逐字恢复原源。
owned 客户端采用独立 IO-v2 恢复协议；原 native worker、方程及门不改。
准备清单 SHA 为
`e511b02c60f412963a610a9766aaea6de12423f1c0358ccac79a84e60bb3a94b`。

## 每个物理高度必须自己接受

当前实际第一请求的完整八维 $H_{\rm old}$ 与旧 run 的 warmup 高度逐项
相同，并且与 initializer 所属的 $H_{\rm new}$ 不同。
worker 真实发起了新的 $H_{\rm old}$ 求解，没有搬用旧响应。
第一范数较大只属于这个新高度的初值，不是已接受状态。
后续每个新高度仍需原 worker 单独通过原门，Jacobian/audit 请求与原
coupler 流程保持一致。

一旦 inner 成功、而它的新高度实际尾尚未接受，先写
`*-inner-####-debug.json.gz` 与对应 DN-anchor sidecar。
raw 文件保存原坐标下 mesh、values、parameters、三次系数及完整
candidate height，明确 `solver_success=false` 和
`actual_tail_accepted=false`。sidecar 绑定实际采用的已接受原响应、
request、配置、源、generation/calls 和 hash。
自动恢复至多一次外部候选和一次原生重试；未改善候选不能注入原缓存。

完整入口和首个实际 request 证据见
`scripts/resume_transfer/q060_coupled_parts16_entry.json`。
它只记录启动、来源身份和保存能力；本条不预先认定 warmup、prefix、
完整 metric、接缝或闭合通过。实际终态另行记录。
