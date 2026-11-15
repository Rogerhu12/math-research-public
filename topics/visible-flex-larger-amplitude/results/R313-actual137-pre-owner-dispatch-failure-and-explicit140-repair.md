# R313　actual137：fresh64 与完整 R273 已完成，owner 前入口分派阻断及 140 的明确修复

本条记录 **request137 的实际读回**。原公开作业完成了 fresh64 全 J／完整 R273 方向与两份输入 packet；其后独立 guard 子进程返回 `1`，没有形成 guard 回执、persistent128 科学摘要或后继组件结果。公开日志没有保留该子进程的异常正文。对本轮冻结入口与实际命令的逐字检查，另行确定了一个足以阻断启动的参数分派错误：外层 guard 把 `--command` 后的 `--owner-child` 当作自身入口，再因第一个参数不匹配而抛错。**异常名称是源码逻辑推断，不是日志直接观察。**

这次结果没有提供新的 128 初始范数、试步、末态、完整导数或物理审计数值；不撤销 [R308](R308-actual133-persistent128-shooting-tolerance-and-identical-fresh-replay.md) 中 actual133 已真实取得的 shooting tolerance 与独立全量 replay。下一 request140 保留原 owner 和原接受条件，修正入口与异常传输，并用已独立发表的 R305 算子组件承担新的完整 stage 导数请求。

## 313.1　实际来源与读取范围

| 项目 | 原记录 |
|---|---|
| repository | `Rogerhu12/math-research-public` |
| run / attempt | `43709832101` / `1` |
| source commit | `f9bdab0245e7aaa7f2b4ab62edeea805cfa6bfd3` |
| compute job | `132798770009`；science step failure，cleanup success |
| report job | `132802625988`；success |
| compute 原日志 | 108574 B；SHA256 `216962f7b00aa87b7e65c3bb9eedc5e1104da063c0ddfe2ba56ce38a564d642c` |
| report 原日志 | 30602 B；SHA256 `3549b673741086d6d201835bcaf412bd6be49ea0add5b478c2023dde4bd96669` |
| `BEGIN_VISIBLE137_SCALAR_SUMMARY` 内 JSON | 12945 B；SHA256 `004d2f8cd10d53847159e0271178fa185d82a94bd2141dabc49e7858a6463fc1` |

上述 summary 的字节口径不含日志时间戳、BEGIN／END 行及其分隔 LF。compute 中 `persistent128_final.summary` 与 report 的该原 JSON 对象一致，compute 同时记录了相同的字节数与 SHA。本地仅解析 JSON、读取原值、核文件／文本身份及 AST；没有重算模型、范数、矩阵、root、RHS、J 或 QR。

本轮执行入口 `geometry_20261115_native_final128_same_job.py` 为 26366 B／`470803fadada94b94d5a6b4359894d4f043aeea0f13bae833b30ed2014618841`；桥 `geometry_20261115_native_final128_bridge.mjs` 为 14400 B／`f5641d7fc28773d76244103a89e1d3d76304c562faa4a25cbc8fe6c81c26af29`。原 owner 源仍为 `767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322`；两处只读生命周期／fallback 插入可逐字逆回原文件，所得内存源 43500 B／`b26db088e577be75ee06025a6dcb905a3a31a84360bd6eaf74b7600986eb501b`，AST 可解析。这项源码事实不等于该 owner 已实际运行。

## 313.2　实际已完成的 fresh64 与完整 R273

fresh 调用仍以 actual91 保存的原 failed73 state 作为初猜，并真实执行本次完整 576 段 withJ；没有从已删除的 113 或 133 raw 用 hash 伪造恢复。

| 项目 | 原字段字面值 |
|---|---|
| complete state | 577 × 224；state SHA `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6` |
| fresh snapshot `result.json` | 1316 B；`3d9e0a5bbf281384b2fbacd18f59694c492f5d7c19c622b5de2812b689bcb28c` |
| complete stage J raw SHA | `1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4` |
| original64 norm | `6.0618737006888706e-05`；f64le `71f299f11bc80f3f` |
| complete R273 direction raw SHA | `4bb396b069f5c32a3d77a08531ad2cdefbd3ece7fd8f63c56baed84f13976ce6` |
| QR result SHA | `e8e1841b19ee6b7a04531983ca0772caba54dce9f5b07cd191472c16140b9b05` |
| original readback rows | `129248` |
| QR calls / formation calls | `1153` / `1152` |
| complete node penalties | `577` |
| factor 与全部 constant bytes | `464891392` |
| 原 factor elapsed seconds | `22.48843169500003` |
| eta | CLI `1`；f64le `000000000000f03f` |

本次 fresh64 系统的 exact affine 最大规范化缺陷原显示为

$$
9.685623139820915231844260456306540893890861679791289092058094119\times10^{-11}.
$$

该值来自保存的 dyadic exact readback，最坏 `stage / node9 / Q1 / global row2128`；matrix identity 为 `9b2332d1056a1bb6634130d2a2f73e778b57c693c9f7fe01d4bbe155f485875b`。它属于本次 **fresh binary64 仿射系统**，不是尚未启动的 persistent128 末范数。对应保存的基态 exact 最大值原显示 `6.061873700688870870601158412977629481529154353251182450024889837E-5`，最坏 `node10 / Pi76 / global row2539`。

factor 报告的 `dtype=float128`、16 B、`significand_bits=64` 是原 longdouble 工作格式记录，不能据 dtype 名称改称该 QR 在 binary128 的 113-bit significand 中执行。真正 binary128 primal owner 是另一个此轮尚未形成科学回执的进程。

## 313.3　实际 packet 与尚未执行的后继范围

原 trace packet 已写完整 226 维态、576 段、129248 行、6943 个原子 RK 步、2048 角点及独立 literal 表：

| 原件 | bytes | SHA256 |
|---|---:|---|
| `complete-input.bin` | 10348368 | `1c9df6b2aa203d526eee11fe443ebcb474584c677b76ed3901b6a0f6c1f37aa8` |
| `packet-binding.json` | 3660 | `ed11469799fbd67f52238b36afabc485119044d76222a543a3d161c49f2abe96` |
| `physical-input.packet` | 5104360 | `1c9fab18574bb130f905daef5fcff66163a0fe987528ace2d9bc81829fc52151` |
| `physical-input-binding.json` | 7343633 | `318177de33c02ef0885c77ba10bcbd8f4b098641b82763cc2b1e2c98264320f7` |

physical packet 原记录 `query_count=7488`、`atomic_audit_steps=6943`。packet writer 声明不调用 RHS／root／J；它导出了后继所需原字段，**不代表 7488 queries 或 6943 audit steps 已经执行**。

实际 bridge 返回：`child_exit.status=1`，`signal=null`，`error=null`；`wall_guard=null`，`summary=null`，`actual_post_owner_component_flags=null`。外层 `persistent128_scientific_summary=null`。日志没有 owner 的初始评价、任何 128 方向／trial／末态或独立 replay 记录；没有 stage 全列、112 边界响应、338 行 endpoint 或 physical audit 的返回记录。

## 313.4　实际预算、退出与原 native 责任

bridge 前实际 budget record 已把 fresh64／R273 的时间计入同一全局时钟：

| 原字段 | 值 |
|---|---:|
| global total seconds | 19200 |
| global remaining seconds | 18293 |
| remaining scientific seconds | 18173 |
| readback cleanup reserve | 120 |
| actual owner seconds | 6000 |
| actual independent replay reserve | 1200 |
| reserved independent audit allowance | 2130 |
| `owner_can_start` | `true` |
| 原 outer elapsed seconds | `907.237564652` |

compute 最末 `global_final128_child_exit` 明确 `returncode=70`、`actual_child_returncode=70`、`global_wall_budget_exhausted=false`。这次没有达到全局资源期限。

`procedure_complete=true` 只表示外层按既定协议受控返回。与此同时，原 summary 明确 `summary_complete=false`、`transport_complete=false`、`summary_transport_exit_code=70`。两组字段必须一起读取，不能把 procedure true 或 report job success 当作科学成功。

原64 worker 在独立实验返回后按既定 sentinel 停止：`PERSISTENT128_CONTROLLED_ORIGINAL64_STOP_AFTER_INDEPENDENT_OWNER`；`original64_nonlinear_trial_calls=0`，`original_driver_exit_code=2`。原 response 的 `converged=null`、`residual=null`。这不是一次原十档 line search 拒绝；本轮没有执行原64 nonlinear trial。

`native_accepted=false`、`fullDN_completed=false`，且没有把任何 128 状态回写成旧64原生成功缓存。guard receipt 未出现时原 bridge 先记录 `persistent128_cleanup_deferred`；之后 workflow 的 always cleanup 成功。raw 未上传 artifact／Release／Git；不存在可由本轮 packet 或末态 hash 续接的保存现场。

## 313.5　源码确定的启动阻断，及日志证据的边界

冻结 bridge 实际构造两层命令：

```text
python helper --wall-guard-seconds N --wall-guard-receipt FILE
    --command python helper --owner-child --packet ...
```

冻结 helper 的 `main()` 在检查 wall guard 前执行：

```python
if "--owner-child" in sys.argv:
    require(sys.argv[1] == "--owner-child", "Explicit owner entry")
```

在上述外层命令中，membership 条件因子命令的参数而为真，但 `sys.argv[1]` 实际是 `--wall-guard-seconds`。因此，按照这两份固定源码，**外层进程必在进入原 wall guard 函数前触发该 require**，其异常消息为 `Explicit owner entry`，类型由本 helper 的 `require` 定义为 `ValueError`。这项推论只需要原参数排列和 Python 控制流；没有执行任何本地科学或伪造失败输出。

它与实际 `status1 / no guard / no owner summary` 相符。原 watcher 只转发约定 marker 的 JSON，而 bridge 把 guard 的 stderr 继承进 worker stderr；普通 Python traceback 未作为 marker 事件输出。原 summary 的 `actual_error=null` 和 `scalar_log_forwarding_errors=[]` 因而不能证明 child 没有异常。**日志未直接显示 ValueError 的正文；本条不把源码推断冒作原日志捕获。**

## 313.6　明确独立的后继修复与未付责任

request140 的新 helper 只按 `sys.argv[1]` 选择自身入口，guard 的 `--command` 尾部不再参与外层分派。新 bridge 单独保存 guard／owner 的 stderr，转发原 UTF-8 正文及原 bytes／SHA；非 UTF-8 或超出单个有界文本事件时明确标 transport incomplete。新 probe 把 bridge 的实际 transport 标志纳入原传输判定；这些变动不调整 native norm、32×10、原容差、root policy、R273 eta 或独立 final 责任。

140 另外采用已发表的 [R305](R305-literal-gram-root-contraction-and-nominal-factor-defects.md) 独立算子实现替代 stage 导数组件。准确实恒等式、名义分解缺陷与实际有限运算图的范围按 R305 保留：不声称旧逐 dL 图的 word 等价、方向误差界或 `C=F_e`。这项科学实现变更与本次入口工程修复分别登记。

下一实际执行仍须重新形成 fresh64 输入，在同一仍存活的 binary128 owner 末态上付独立 replay、完整 stage 图、112 边界响应、338 行读出和物理审计。各预算耗尽与缺失后缀必须原样返回，不能借 R308 的旧末态身份或本次 packet 成功声称这些责任已经完成。
