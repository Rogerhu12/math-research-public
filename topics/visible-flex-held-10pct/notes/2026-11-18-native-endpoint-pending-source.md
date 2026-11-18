# 字面圆弧端点的原生尾 pending 内解恢复入口

**可信度：源码准备与身份检查；不是新的数值解或连续误差证明。** 本条只准备真正 $\lambda=1$ 的独立恢复入口。准备过程没有 import 数学模型，也没有重算内解、均值、metric 或尾部流。实际主线由另一个已有入口 `run_m3_trace_path_native_endpoint_v2.py` 推进；不能把其执行与本条的源码准备混成一次求解。

## 需要补的接口

原 `resume_m3_trace_path_native_pending_v2.py` 服务于原 V8 内解到新原生尾的首次转换，使用的 raw binder 严格限定 $0<\lambda<1$。到字面端点时，真实 raw 与 runtime plan 已经保存原生来源。因此直接传 `plan.native_tail_source_sha256` 给 provider 构造器，会错误地将当前原生图当作历史 V8 图计算差集；直接沿用 partial binder 则会正确拒绝端点。

新文件 `scripts/resume_closed/resume_m3_trace_path_native_endpoint_pending.py` 独立解决这两项接口问题，已执行和已绑定的旧文件保持原样。它从 `plan.active_tail_provider.historical_native_source_sha256` 读取历史图，同时要求 manifest、整个存储的 provider、raw 的 provider、当前 plan 的原生来源图完全一致。历史图只说明该原生程序从哪两个原始文件派生，不充当本次实际响应。原内解使用的 affine 锚也必须带同一个真实原生 manifest 及原 `.05` 投影门标记。

## 恢复范围

端点 binder 要求 $\lambda=1$、lift strength 为 1、`literal_R44_endpoint` 分支、完整八个参数和七个控制、原 base profile 加一次 $p_0$、全部 mesh/cubic/RMS 及明确的失败请求。任何未知或不符字段仍报错。没有把 raw cubic 标成物理 quintic，也不补造缺失的 `yp`。

入口仅恢复原成功内解返回后的控制流：保留其全部状态和真实诊断，接实际尾响应、原 BC/history 行以及原总预算中尚未用过的 outer 索引。完整同 H 的已接受响应直接复用；改变 H 后仍调用同一绑定原生 provider 的原 DN/Jacobian/audit。原门和后处理公式不变；没有重复已接受内解或为了确认而重解同 H。

这里的入口尚未通过本条运行。未来仅在真实成功 raw、对应失败请求和真正同 H 完整接受记录都存在时调用其 `--prepare`，随后按所生成的 observer 命令恢复；不存在这些输入时不能编造一个终态。

## 来源与复现

紧凑记录 `scripts/resume_closed/native_endpoint_pending_source_preparation.json` 保存新源、原生 pending 父源、原控制流 runner、端点两读器和 provider helper 的完整 SHA-256，并引用只放 scratch 的 literal 变换清单。

实际源码准备 `24c9b9` 返回 0：共十二项明确 literal 替换，AST 通过；逆序替换后逐字恢复父源。没有加载模块或执行数值。重新核查只需读取清单，核 SHA-256，使用 `ast.parse` 解析新源，再按清单反向替换并与父源字节比较。该检查不是一条新的数学验收，也不提供跨算术实现的连续误差界。
