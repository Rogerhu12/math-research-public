# 未被原 epigraph 规则接受的试探点：独立同态诊断

日期：2026-11-14。新增 `scripts/frame_metric_epigraph_trial_audit.py`，不修改已发布求解器、原运行结果或任何原始状态。公开人工与实际回执尚待生成，不记未执行的检查为通过。

## 1. 本次消费的事实

公开运行 `43637739532` 对最大度量误差进行了唯一一次 SLSQP 调用，因墙钟预算结束。原规则同时要求全部形状条件和辅助上界覆盖真实度量误差，因此最终仍选择了原状态 `81a154d3464fd329bd384572fbf9f067c93a9e588f454c909f9e1ba239905433`。本次不改变这一事实，不把该运行改称收敛。

同一回执的 `lowest_delta_trial_may_be_ineligible` 保存了第 54 个试探点的全部 163 个系数：

- 物理 SHA256：`5d383918734118c105af3cfc2571731cdbefc2ad23939a4eb43a973e50b472ea`。
- 原辅助 $\delta=0.2651667068964935$。
- 原 $100\times192$ 网格直接 $\max\eta=0.26528271919508084$。
- 原辅助上界缺口约为 $1.16012\times10^{-4}$，超过原 $10^{-9}$ 容差。
- 该记录的帽高、原系数盒、signed-z、球 $1.01$ 和条带 $0.39$ 均通过各自原数值筛选。

来源为 `notes/actions-43637739532-1-metric_epigraph/frame-metric-epigraph-audit.json.gz`，解码后 1,600,886 字节，SHA256 为 `b4d34b0d37928b2f3ffeacf5de3a072068a6314e474fb72c6cd4adb3ae9c5bc5`。这里只解析已发布 JSON，没有本地重新评价几何。

## 2. 七输入与原失败的保留

前六个报告由冻结的 `prepare_maximum` 重放；第七个完整报告另外核对：

1. 解码/存储字节来源与全部冻结源码；
2. 原初态、原最终接受态、原完整度量、$b_0$、帽高行和参数盒；
3. 原目标配置、准确工作节点与完整目标评价身份；
4. 保存试探点的 binary64 系数、有理身份、canonical 物理 SHA、正辅助 $\delta$ 及其原历史记录。

实际分支要求第七份报告确有那一次既有优化调用，但新 driver 不再调用优化器。人工分支使用显式标注的小载体和零求解 fixture，不把它们冒充研究回执。

消费的对象就是原来保存的唯一试探点，不再次搜索历史记录，也不修改当前系数以满足条件。原报告的最终接受态仍为原状态。输出单独记录“此试探点未被原规则接受”，保留旧辅助数值、有理身份和失败标志。

## 3. 唯一同态评价

保持相同的完整 $g$、固定 $b_0$、单一共同原函数与全部系数，依次只读评价：

- 原 $100\times192$ 工作网格；
- 含完整结构节点的 $160\times384$ 细网格；
- 相同 160 层径向、768 角点。

保留真实 $E-1$、$F/a$、最大算子误差、完整径向分布、曲率、面积、镜像点对、帽高、位置两端完整二 jet、球、条带及 signed-z。工作网格还明确给出与原试探记录的标量回放差，避免把末位浮点评价差混同系数变化。

每档有两套清楚区分的布尔量：

- 帽高/系数盒、当前 signed-z、球、条带分别是否通过；
- **原封存的同一个**辅助 $\delta$ 是否通过两条除式以及直接 $\eta\le\delta$。

原 $\delta$ 在细网格上可能继续失败，或出现更大缺口；本次不重新赋值。若以后从该物理状态重新启动另一优化过程，应公开重新设置起始辅助界，并作为新求解配置记录。这个未来动作不在本 driver 内完成。

任何有限网格通过都不证明连续同度量、完整嵌入或全曲面 reach。最大度量误差降低与曲率、镜像法弦改善也不是同一件事。

## 4. 针对性人工与失败输出

人工主流程生成七个明确标注的报告，保持实际输入/输出调用链。它构造一个与原接受点不同、帽高和放宽形状门通过、辅助界故意不足的人工物理点，验证：

- 只消费保存的物理向量，不调用旧或新优化器；
- 原辅助界不足仍保留，未通过点不会被改称原已接受态；
- 完整同态细网格与角加倍输出可写出；
- 错误第七 SHA 和改坏 trial canonical 身份被拒绝；
- 错误仍保存小 JSON，summary 绑定完整报告字节。

这只覆盖新的消费与诊断分支，不重复旧 SLSQP 数学检查，也没有运行任何实际候选。

## 5. 公共命令

```sh
python topics/visible-flex-new-mechanism/scripts/frame_metric_epigraph_trial_audit.py \
  --check-only \
  --out "$RUNNER_TEMP/metric-epigraph-trial-development.json"
```

同一公开任务随后只运行一次实际诊断：

```sh
python topics/visible-flex-new-mechanism/scripts/frame_metric_epigraph_trial_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-independent_height_solve/frame-independent-height-bounded.json \
  --anchor-input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --short-audit topics/visible-flex-new-mechanism/notes/actions-43627111925-1-short_entry_audit/frame-entry-short-bounded-initial-audit.json.gz \
  --height-audit topics/visible-flex-new-mechanism/notes/actions-43630874689-1-height_polytope_audit/height-polytope-bounded-audit.json.gz \
  --prior-joint-audit topics/visible-flex-new-mechanism/notes/actions-43634358250-1-quartic_joint_audit/quartic-joint-audit.json.gz \
  --resume-audit topics/visible-flex-new-mechanism/notes/actions-43635770962-1-joint_resume/quartic-reused-joint-resume.json.gz \
  --epigraph-audit topics/visible-flex-new-mechanism/notes/actions-43637739532-1-metric_epigraph/frame-metric-epigraph-audit.json.gz \
  --expected-input-sha256 c1d81da9640c4fa2598a94e54b1e203e028c3bf914afeba5e25944b4360c6f46 \
  --expected-anchor-sha256 6ff0b179af88589c1d87ee3408f068f14b02c310e2a9b300759426fa4550f1e3 \
  --expected-short-sha256 9d64a1ea03745405bd72fce6078eace92e02f3987be6ae079b75f0b71f69502c \
  --expected-height-sha256 f457282f0a21cd27802748066537caa4cf90c687c63c73d62b0391ce2435d1a3 \
  --expected-prior-joint-sha256 e344e6e0a62be10dfa8dad4f52e4b889191f462b97bb19dd4b1cc0283f6f33dc \
  --expected-resume-sha256 40deb9dffa6882b14dd445d981f2ed09b1f4d488dbaa83e952c768537f91375d \
  --expected-epigraph-sha256 b4d34b0d37928b2f3ffeacf5de3a072068a6314e474fb72c6cd4adb3ae9c5bc5 \
  --out "$RUNNER_TEMP/metric-epigraph-saved-trial-audit.json"
```

实际模式继续限定 `Rogerhu12/math-research-public` 的 Actions，七个输入都在本课题 `notes`。旧代码和旧输出全部保持冻结。
