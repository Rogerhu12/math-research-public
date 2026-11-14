# 零高度 J 独立审计与首次完整 DN 内层尝试

2026-11-14，exact_refinement，AI 辅助。**状态：零高度导数审计及严格缓存复用已经实际执行；完整 DN 的首次内层未接受，尚未调用任何新非零高度的真实尾。**

公开 Actions run `43584222071`、源提交 `a47c0f96b7a5843deb8d8ffea181beab6eb6696e`，结果 artifact `14109339087`。原始结果归档于 `public-actions-43584222071-1-coupling/`。以下只读取这次真实结果，不是重算、拟合或放宽接受门。

## 1. 完整零高度 J 的独立恒等式

消费者 `exact_20261114_zero_tail_response_audit.py` 使用已经完成的 T96/N1024 零 H 响应，SHA `08d1e4865cb00d7d48ab169ce387a60119f304bc4dc4953eb8fd029fdbff1160`。本次消费者没有再调用尾求解器。

对于同一旋转背景，线性化 Darboux 给出

$$J_{rr}=\frac{w_r}{w}\left(\operatorname{diag}\frac{(2j)^2}{r}-J_r\right).$$

完整保存 J 的实际诊断为：

| 诊断 | 原输出值 |
| --- | ---: |
| 二阶 J 与上述恒等式的最大绝对差 | `3.2531097531318665e-6` |
| 按各条目/各列尺度归一的最大相对差 | `1.3205334828336765e-12` |
| slope J 的全部非对角项最大绝对值 | 0 |
| second J 的全部非对角项最大绝对值 | 0 |
| mean-slope J 最大绝对值 | 0 |
| mean-second J 最大绝对值 | 0 |
| height block 与单位阵的最大差 | 0 |
| slope J 最大绝对条目 | `32802.403742635055` |
| second J 最大绝对条目 | `2853441.7406707397` |

相对条目诊断的分母是 `max(1,abs(reference_entry))`；列诊断使用相应列的最大绝对值与 1 的较大者。这里的二阶绝对差具有自身单位和很大的系数尺度，不能直接把曲面 metric 的 `1e-6` 阈值移作该导数恒等式的验收门。

这份实际结果未显示原零高度极小对称差分造成 height/mean/模间结构崩坏。它核对的是同一有限射击图上的端点线性化关系，不证明有限射击图本身已经达到径向、角向、频率或深度极限。

另一个独立读数是实际 shooting slope J 与 ready 预计算线性图的差：最大绝对值 `269.9741620038767`，最大相对条目/列值 `0.011685073299067024`。二者不能互相替换。原真实零尾的高图条件数仍须保留为精度和后续非零问题的诊断信息，不能由本次端点恒等式抹掉。

## 2. 零缓存确实命中，新 H 尾尚未发生

`true-tail_imported-zero-uses.jsonl` 只有一次准确同零 H、`jacobian=True`、`audit=False` 的命中，引用的原响应 SHA 与上文一致。原 worker 正常初始化后，`true-tail_trace.jsonl` 只有一条 backend 记录；没有 `request`、`iteration`、`response` 事件，没有 `true-tail_0001.json.gz`，stderr 为空。

因此本次确实复用了之前的完整实际零尾和 J，没有重复先前约 805 秒的求解，也没有产生任何新的非零 H 真实尾求解。读取旧 audited response 作为初始锚点不等于本次执行了最终 audit。

原完整 DN driver 的状态是 `inner-newton-not-accepted`。outer iteration 0 的 affine inner 从初始 690 节点走到记录的 878 节点，原 SciPy 状态为 2，消息为 collocation Jacobian singular；保存的 RMS 最大值为 null，边界最大值为 `0.00196416148118607`。完整 driver elapsed 为 `121.39040719599996 s`，`new_coupled_finite_acceptance=False`。这属于未接受的前缀/控制内层，不能改记为“新非零尾不收敛”；其实际域和 Newton 诊断另由前缀线处理。

被动消费者 `exact_20261114_tail_trace_report.py` 本次也已实际退出，`diagnostic_complete=True`、无读入问题。它只整理原日志和响应，不执行求解、不修改任何原文件或阈值。完整 failed/pending/checkpoint 数据仍由原 artifact 保留，未被当作新的接受初态。

## 3. 原始证据

| 文件 | SHA-256 |
| --- | --- |
| `zero-height-J-audit.json` | `6399790a1d1565102767e4a3b6b418915082e309f4c2e0195395b613f9cd6c35` |
| `full-DN-tail-diagnostics.json.gz` | `1e86a58d92851e4e30a2b3145847102a9a6efbf407da624fbf3c7d0a3f513dfc` |
| `full-DN/true-tail_imported-zero-uses.jsonl` | `d838e9ad2acacfa6f0442b7c4236cad0874f265733180b1439d204acbb036c55` |
| `full-DN/true-tail_trace.jsonl` | `e0a71ca4b7c17d6bcd4835aae7d69238c2b576cd603b25735f9dcd94c6301030` |
| `full-DN/driver-status.json` | `dc2d88ac60892d888c317ecce6185918e6fa4e0544887f8e3754bbe2dcdf8b63` |

本条没有新的非零尾、完整前缀接受、完整六 jet 闭合、全族嵌入/reach 或目标幅度结论。课题仍未完成。
