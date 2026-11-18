# λ=1 的独立读取、原返回内解续接与接缝接口

**类别：已执行的源码/AST 准备；没有新的数值解或端点验收。** 当前生产同伦 runner 已允许目标 $\lambda=1$，而旧读取器明确只接受 $0<\lambda<1$。这里新增独立端点接口，不改任何已执行的 partial 源，也不为端点构造假 checkpoint。

## 1. 端点按实际定义分派

已绑定的 `m3_circle_trace_path_model.py` 对每个同伦值创建独立 Flow/BVP 类和固定 core factory。其 `circle_trace_homotopy_core.py` 在 $\lambda=1$ 直接调用已有 R44 replacement core；`synchronous_core_lift.py` 在同一点直接安装原完整 `exact_core_lift` 和原 analytic parameter Jacobian，不再乘一个中间 partial 系数。

本次新 reader 因此要求：

- 精确的 `lambda_value=1`、`path_lambda=1` 与 `partial_lift_strength=1`。
- 实际 `path_definition.branch='literal_R44_endpoint'`。
- 原 M8、25 状态、全部七物理控制和原尺度、gauge/warp `.06`。
- 原 base profile 加完整 $p_0$ 一次、原 `(.5,.9)` lift 窗、完整原 source/chart/port/尾身份。

生产 serializer 的历史 `core_kind` 字符串仍含 `partial_lift`。新接口保留这个真实字段值，**不靠这个名称猜测数学定义**；以同伦值、实际 branch 和全部 source identity 明确分派。没有修改 solver/exporter 的字段来伪装一次新执行。

定义上的端点入口是 R44 的 $\Gamma$，其保护弧具有原完整迹控制；这与浮点反函数/求积的误差认证、全 prefix metric、闭合及 reach 是不同事项。reader 不自动领取一个新的圆弧数值证书，也不放宽任何原求解门。

## 2. 四个独立接口

| 新文件，均在 `scripts/resume_closed/` | 原冻结父文件 | 变化范围 |
|---|---|---|
| `m3_trace_path_endpoint.py` | `m3_trace_path_prefix.py` | 只接受 $\lambda=1$，增加 literal R44 branch，改正端点 scope/descriptor |
| `m3_trace_path_endpoint_inner.py` | `m3_trace_path_pending_inner.py` | 显式端点 reader 与 branch；原 raw/sidecar/失败请求、完整 cubic/RMS 验证保持 |
| `resume_m3_trace_path_endpoint_pending.py` | `resume_m3_trace_path_pending_v2.py` | 引用独立端点 binder/source；原 post-tail/剩余 outer 控制流不变 |
| `finish_m3_trace_path_endpoint_seam.py` | `finish_m3_trace_path_saved_audit.py` | 在真实端点上只补缺失 seam，保已存完整 prefix audit；原 seam 函数不变 |

原已接受内解不重跑。若端点只有 pending tail，完整 raw/cubic/full $p$/RMS 和旧真实 affine 锚按原格式恢复；真正同高度响应直接复用，未知高度仍交原 worker 的完整 DN/Jacobian/audit 和 $2\times10^{-9}$ 门。总 outer 索引仍为 $0,\ldots,7$。

若端点已经有物理 quintic 和完整 audit、只缺 seam，则读取原系数，必要的原 core/inlet constructor 恢复一次，只运行原 `seam_audit`，不重 prefix audit、mean-height 原函数积分、BVP、C² 插值或 native solve。该接口不先插入假的 `tail_seam` 通过完整 reader；真实 seam 完成后才验收完整记录。

## 3. 实际准备来源

`prepare_m3_trace_endpoint_interfaces.py` 固定四个父文件 SHA-256，逐个应用列出的文字变换，严格逆变换回父文件，再用 Python AST 解析新文本。调用 `47783d` 真正退出 0，只做文本与语法工作；没有导入数学模型、构造 core、绑定合成 checkpoint 或调用任何方程。

完整可再生的文字变换清单保存在
`closed_work/m3-trace-endpoint-interfaces-v1.json`，SHA-256 为
`2eb2fc0d7f4ad1586edb9fa6e3927d932af8cd6c3cb401a226f1734e37448a6c`。
仓库的紧凑来源记录为 `scripts/resume_closed/m3_trace_endpoint_interface_preparation.json`。

四个新文件 SHA-256：

- endpoint reader：`e5ef9f62349e318fef3f844d603f6dc39a047107c3fff6ec4f3449a4367cd407`。
- endpoint raw binder：`4e6d4ced67b3a2c61768e3006293d0e6d11bde8f68b3cb95f8dd230dad8a0b48`。
- endpoint pending runner：`6babf4591b0ef0356c2f090b5708555b32a7505e484005fa65568fd9b5e50c13`。
- endpoint seam-only runner：`57fc88c34780de3b5e892b3e4302225c65316633926c9a7baf2c193a278b2210`。

复现文本生成可在没有这些输出文件的新 checkout 中执行：

```sh
python scripts/resume_closed/prepare_m3_trace_endpoint_interfaces.py --record NEW_TRANSFORM_RECORD.json
```

工具拒绝覆盖已经存在的独立版本。各入口的命令行参数与其原 partial 父版本一致；只有实际达到对应完整输入状态时才调用。没有为了准备接口而重复旧 BVP、旧 metric、旧积分或现有 tail。

## 4. 不包含的升级

这四个接口保持 M8 和现有全部七槽，没有实现 R47 的升阶接口，也没有重缩物理控制。它们只消除旧读取器的明确端点适用范围障碍。是否存在通过原门的 $\lambda=1$ 完整终态、其真实 metric 和后续固定 $g$ 收敛，须由实际执行结果分别回答。
