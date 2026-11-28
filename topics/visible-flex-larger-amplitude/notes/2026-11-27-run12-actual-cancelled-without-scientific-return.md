# 公开 run12 的真实取消终态：完整科学步骤未自然回传

## RET86：终态导读与完整历史记录

**已知终态：** run12 官方 completed/cancelled，原因未知。两必要输入实际返回 0；完整科学没有观察到自然返回，report/final/typed/pure 均不能据取消补成已完成。下文全部 48 原观察字段保其固定完整记录。

本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。4 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。

**完整旧文件：** 22062 字节；SHA256 `ef9e35d7a5280c8ace4680530952a58374db9745caa4657492c3e739f4d376d2`；Git blob `54b339f3c1ff338aac2378c84f48d7371617cc8c`；固定提交 `0ff96dc0001b35cac2301f942e55292fe0f808ed`。[完整旧版](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run12-actual-cancelled-without-scientific-return.md)。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET86 完整交付表](../computations/terminal-run10-14-narrative-retention-86-complete-delivery.json)。

下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。

## 1. 已核终态

在 **2026-11-27 19:48:01 UTC** 的实际只读观察中，公开运行 [46011377225/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46011377225) 的官方 API 为 `completed / cancelled`。Job `140547455454` 及其第 5 个 research step 也为 `completed / cancelled`。这是运行终态，不是原完整求解器的正常完成记录。

官方 run 的 `created_at`、`run_started_at` 均为 `2026-11-27T13:56:02Z`；`updated_at` 为 `2026-11-27T19:46:23Z`。后者是官方 run 更新时间，不冒充本工具未返回的单独 job 完成时间。初始实际 head 为 `ed9fbfec354330d11b0e46ef61a4d0565b88dfc6`。请求声明的 workflow 上限为 350 分钟、controller admission budget 为 20000 秒；请求明确运行中的科学 child 不因 admission budget 自动被记作完成。本记录没有独立核实取消的具体主体或日志原因。

完整官方 job 包装返回及准确 run 字段投影如下；字段投影不是完整 raw API 响应的别名：

> **原 JSON 01：官方终态投影与完整 jobs。** [固定旧版完整记录，第 11–98 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run12-actual-cancelled-without-scientific-return.md#L11-L98)。


## 2. 原公共小卷仍只有两个真实输入返回

终态观察时，公共索引仍保存 **19:41:24 UTC** 的进行中记录，而不是一份新增自然科学返回。已完成阶段只列出原两次必要输入：

- 阶段 1：`prepare-complete-fixed-fejer-r690-inputs-20261127`，`completed`，exit `0`，5.893721085999999 秒；实际 source commit `97051366b05adc2a6aa27c845f712c5b79edfdff`，完整入口 SHA-256 `89cc6c07e7d9e6188c35151199d38f7df301737630cec233c52195cddfb43e60`。
- 阶段 2：`prepare-fixed-fejer-complete-R690-reference-2218-first-20261127-run12`，`completed`，exit `0`，430.2165345 秒；实际 source commit `6e7fc7dc687960599e398087f9e1f574bdc2a738`，完整入口 SHA-256 `e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb`。

这两记录的原完整命令、全部实际输入、输出 record、source commit、完整输出 SHA 和紧凑数值仍逐字在下列原分卷内。本次未修改、删除或重新执行这些输入阶段，也未把终态当作新的科学返回。

> **原 JSON 02：原索引和完整返回分卷身份。** [固定旧版完整记录，第 109–124 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run12-actual-cancelled-without-scientific-return.md#L109-L124)。


完整公开路径：

- `topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46011377225-1.md`。
- `topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46011377225-1-part-001.md`。

原分卷的两个 JSON 对象均完整存在；未见第三个自然返回对象或第二卷。其完整返回对象的关键实际字段如下，其余完整原字段以以上固定整 blob 为准：

> **原 JSON 03：两个必要输入的完整实际记录。** [固定旧版完整记录，第 133–291 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run12-actual-cancelled-without-scientific-return.md#L133-L291)。


## 3. 未自然返回的真实科学 child

最后公开 scalar 记录的 step 为：

`complete-fixed-fejer-immutable-point-first-20261127-run12`

其实际 child PID 为 `3347`；实际 scientific source commit 为 `a3df4eae39988724cca2cc3c38927e583c24eb2e`，实际 launcher SHA-256 为 `0c1ff0aa2de30fcd490efb4bddd1972613c0f0afb1257d1af0170ac7e60bb5bf`。该 child 的退出码在已发布观察里仍为 null。没有把 GitHub 的 `cancelled` 换成一个未观察到的 Python/launcher exit code。

该入口对应已刊完整 Fejér M160/J923/N2048、7377 material radial observations、完整 1,333,370 个外层变量、原 32 段 normal partition 和原完整数值预算。正式数学目标是预先公开的 RN-even64 Fejér 七项图及完整 R690 标量律；它没有借旧 warm 选出的未知图。原 request 与完整 argv 责任继续保存在原已刊输入/求解计划及完整 followup 队列：

`topics/visible-flex-larger-amplitude/computations/resume-20261127-followups-12.json`

已刊完整求解族中的 driver `477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd`、normal `1aa64d7731333f8ae008f86b717421abbbbfdb7f4c3edb1173f93754364bd778` 和 pure reader `274d159e6c5ef9ac13a149b456394a9e53afecf753f5d8d39d0b1e224ecbc45b` 限定这一未返责任。新 stage-point/meridian-cache/batching 源没有替换该运行中的旧源。

## 4. 完整最后标量观察及边界

最后发布的 actual normal 数据时间为 **19:41:20 UTC**。它确实记录了 full point `507253778ce58f9025ca9078abb81bcecd3698e2f540c6bfaeaec9c06ab34902`，当前 scope requested angular order 为 2，scope angle count 为 1，已缓存角数为 1228。closure 请求/返回均为 1,769,743，逻辑失败为 0；原 closure 返回 848,643，缓存命中 921,100；scope started/closed 为 6171/6170。

这些是最后一次被公共索引捕获的 mutable scalar 观察。它们没有报告该 full point 已被接受、没有给出新的 Phi/Gram/完整 geometry 数值，也不能给出自然结束时的最后点。原 closure/key 计时仅覆盖它们各自的 instrumented scope，不是整个 F/J/求解时间。

以下保留这一完整已发布观察对象，含真实小文件 byte/SHA 与全部 48 个被选标量，不从其他运行补字段：

> **原 JSON 04：最后完整同点进度观察。** [固定旧版完整记录，第 315–388 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run12-actual-cancelled-without-scientific-return.md#L315-L388)。


## 5. 未返报告、checkpoint 和历史的处理

本次公开证据没有返回这一科学阶段的 complete report、最终 checkpoint record、pure readout 或后续费用结果。原 runner 内是否已有 incomplete report、initial/accepted checkpoint、方向矩阵或 partial root packet，只能由真实文件进一步确定；本记录没有读取这些 raw 文件，也不将其假定为空或不存在。

因此，当前没有可由本记录提供的、已验证 `complete=True` 且同 source/model/point 的完整 13 成员 `final.npz`。不能用最后 mutable point SHA 代替完整点数组，不能把进度中的根字或输入 reference 充作 final，也不能构造一次没有发生的 accepted transition。纯 reader、同场费用及其他未返后继继续是未完成责任。

这一运行可能产生的永久地点、typed row、保护角色、发现顺序和未发布末场均没有被置空。原已知 P0/G/history 输入与其来源仍保完整记录。新固定目标的地址重解释和潜在完整有限包络责任继续依原已刊明确政策；它不把 run12 的未知实际历史伪称已逐字继承。

## 6. 本次实际操作范围

本次只读取官方公开 run/job 元数据、已存在且小于 100000 字节的索引/分卷，以及原 source/参数身份。没有取消、重跑、修改 job、缩减原科学预算、生成数值 fixture 或变更 Git refs。取消原因尚未由有界原日志证实；本记录不凭墙钟时间推定具体数值失败或约束种类。后续完整求解须使用真实可用输入和明确完整来源的新入口，其结果仍待实际自然返回。
