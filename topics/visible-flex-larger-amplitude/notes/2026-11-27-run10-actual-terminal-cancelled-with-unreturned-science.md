# 原 run10 实际终态：科学步骤取消，完整场与后继读数未自然返回

## RET86：终态导读与完整历史记录

**已知终态：** 原 run10 已为 completed/cancelled，原因未知；只见四个必要步骤返回 0，完整科学、pure、最终 13 成员和 typed 未返回。新 Fejér 分支不补成原 run10 完成。本文完整终态、全部原源/参数/进度和未付责任保原文。

本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。5 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。

**完整旧文件：** 28909 字节；SHA256 `1e9f274b14d10689f5d93f9f96b51f15e3526abfb0f0dc14960d425f1e31e9b5`；Git blob `546838f35b556015b6aed38a65c80800b23308d9`；固定提交 `0ff96dc0001b35cac2301f942e55292fe0f808ed`。[完整旧版](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run10-actual-terminal-cancelled-with-unreturned-science.md)。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET86 完整交付表](../computations/terminal-run10-14-narrative-retention-86-complete-delivery.json)。

下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。

记录时间：2026-11-27 15:09:03 UTC。本条只登记实际公开 API、原完整小分卷与原队列；不重新执行科学，不把取消解释成数学失败，不把随后独立 Fejér 目标的运行当作本分支完成。

## 1. 实际终态与可确认范围

公开运行 [45972294636/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45972294636) 的 API 已返回 `status=completed`、`conclusion=cancelled`，API 的 `updated_at` 为 `2026-11-27T15:06:33Z`。实际 job `140415391810` 同样为 `completed/cancelled`；其第 5 个工作流步骤 `Execute public research and publish independent compact records` 已 `completed/cancelled`。这里的工作流步骤 5 对应整个研究控制器，控制器正在执行的科学阶段也编号 5，两个编号的职责分开记录。

运行创建与开始时间均为 `2026-11-27T09:16:11Z`，工作流声明的 350 分钟预算与该终态接近。**尚没有已读、尺寸合规的原日志或 annotation 证明具体取消原因，因此本记录不将原因写成超时、人为取消、科学异常或数值失败。** 通用 GitHub fetch 拒绝 job-detail/annotation 端点；现有 job-log 专用接口只能整读，尚未取得全日志字节数，故没有无界读取未知大小日志。此访问边界不改变实际 cancelled 终态。

最新公开索引仍是 `2026-11-27 15:04:42 UTC` 的运行中快照，明确仅阶段 1–4 完整返回。没有阶段 5 的自然退出码、完整 report 返回记录或实际最终 13 成员 checkpoint 身份；后继纯读和均值/剖面费用步骤也没有实际返回。后续字段均保持未知，不补空历史、不造成功或失败的场结论。

完整终态 API 关键原字段如下。完整 run API 文本的实际 UTF-8 身份为 `7e02da5771922fe88fbe52eadfa9e72d21b5fbb5abb58190667b22fbab3088dc` / 13356 B；下表/JSON只是明确选出的状态字段，不冒充原全文。

> **原 JSON 01：官方 run 终态字段投影。** [固定旧版完整记录，第 15–30 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run10-actual-terminal-cancelled-with-unreturned-science.md#L15-L30)。


实际完整 job/step 状态响应：

> **原 JSON 02：官方 jobs 完整对象。** [固定旧版完整记录，第 34–97 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run10-actual-terminal-cancelled-with-unreturned-science.md#L34-L97)。


## 2. 固定的公开证据位置

| 内容 | 仓库路径 | Git blob | UTF-8 字节 | SHA256 |
|---|---|---|---:|---|
| 末次已刊索引 | notes/2026-11-27-public-actions-45972294636-1.md | aa0cd34df366739dd42964932653d655a4063ea2 | 7962 | cb16cc9f03be8d286d130a5410277aae150063d9520fcd9211b3bc636ad96258 |
| 完整实际阶段 1–4 | notes/2026-11-27-public-actions-45972294636-1-part-001.md | e914a571f6fe2c228e6662ad2b144363c8486881 | 38575 | 0b1de8d544053aa5e67f80b144a65274c2f111825845482e68c5c278ef9f7cee |
| 原三后继完整队列 | computations/resume-20261127-followups-10.json | 9ff6a4417bf86c034b879abf9a72c84129b38b0f | 92609 | 26ed8e7b68467931cfb5198c7eac76941d3f82ebb5db8a928d5d7a79a2a74a34 |

上述路径都相对 `topics/visible-flex-larger-amplitude/`。阶段 1–4 的原记录包含各次完整命令、全部输入/输出文件记录、实际 source commit 和原紧凑返回值；其 38,575 B 原字节在本次终态核查时仍完全相同。此条没有移动、删除或把三后继对象标成已完成。

原完整科学/纯读 ready 为 `computations/run10-detached-closure-values-complete-ready.json`，87,763 B / `ab9d21b4f7f9169ccb241cce418e218ab66dda88d98749498d1b69326ef48b85`，blob `04e986cf6c3a8b734d51f14cd49672ea8d1fbb89`。完整参数/来源表为 `computations/run10-detached-closure-values-complete-parameter-and-source-provenance.json`，33,613 B / `26b5b3d389cadd652f11c5599c110fb7c5dd5d3ce37891cd95e3b24060826d27`，blob `39cf32f1701f1424d3a01d3371b60ed8a6e8e197`。

## 3. 已真正返回的四个必要步骤

四项均返回 0；其必要输入生成/源码再生成功不等于科学场成功。以下保每项实际 source commit、源码、parent 与所有实际输出文件记录，不保存任何数组或 raw 科学正文。

> **原 JSON 03：原四个必要步骤的完整实际返回。** [固定旧版完整记录，第 115–306 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run10-actual-terminal-cancelled-with-unreturned-science.md#L115-L306)。


实际参考是 `512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b`，完整模型 `081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5`，实际 carrier `71f0048e2c6c973625fd110c6980c24242d2cf67b7dd7da5dd9e889fde26a22d`；完整 target canonical `e7110482f9bd2eb723e96c99f5bbaa8a85aa11a81519c5204a296fb1bad9a049` 与 whole target 文件 SHA `b24080447828d8ffb49ae146dd5672d34bf6f5cec512054633b6f849c2bdabfb` 不混用。实际全 binding 文件为 `4ace8184408aa0c7cac7970ba6fc96565c68786a518cd9d280a1a97ef82b50cf`。

当前参考 scalar 的实际完整积分叶为 **2218**，`scalar_tolerance_reached=false`；旧 run05 carrier 再生中的 **2397** 叶属于其明确独立的历史恢复职责。这两个叶数不替换，也没有把未达精度目标写成已认证。M160/J923/N2048/P7377 与全标量参数 `e640aec831df350fa69740650b723a7d2d55676ca64ffb5ddabbacb3ab7d6dfa` 仍按原记录保留。

## 4. 真正开始但没有自然返回的科学步骤

实际子进程是在源码提交 `9dce039498a177d870ccc87970df7bd05e419a98` 下启动，launcher 全 SHA `22069c4bb56a4ca4820b3f608cf720a36b036534e6b1e90b5f467f8eed21e604`，PID `4475`。完整 scientific driver 是 `fullclosed_run10_detached_closure_so3_qp.py` / `c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1`，normal 为 `6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4`；后继完整 pure reader 为 `2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e`。这些源和原 75 个角色继续按已刊全参数/来源表定位。

末次实际有界进度写于 `2026-11-27 15:04:38 UTC`，观察于 `2026-11-27T15:04:41Z`。完整小进度身份与全部原 43 个标量如下；它是运行中的观察，既不代表已接受方向，也不代表最终字段/geometry、连续证明或精化成功。

> **原 JSON 04：最后完整同点进度观察。** [固定旧版完整记录，第 318–386 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run10-actual-terminal-cancelled-with-unreturned-science.md#L318-L386)。


由此只能确认当时同一 child 的完整 closure 请求已有 1,861,924 次实际返回、原积分 895,509 次返回、命中 966,415 次、当时记录的 closure failures 为 0；最后 point 是 `a45bc0249e792ac0f3c574f41ef6787989b2a271abc39e28548c29f4ccf690f9`。**这些计数不排除之后异常，也不证明该点已接受或最终完成；没有完整 report 时不能据它恢复最终 typed 列表、最终根或控制词。**

## 5. 原完整参数及未返后继

原三完整队列对象的 149/7/32 个参数全部如下原样保留；373/357/48 个原 summary selectors 仍在上表固定 blob 的完整队列中，未裁剪。第一项确已启动，第二/三项只见准入，没有实际运行返回证据。下列 `actual_return_seen=false` 表达“尚无已刊完整返回”，不擅断言 runner 从未内部开始后继。

> **原 JSON 05：原三后继完整参数与未返回边界。** [固定旧版完整记录，第 394–622 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run10-actual-terminal-cancelled-with-unreturned-science.md#L394-L622)。


## 6. 保留的责任与后续边界

- 原科学 5 没有自然完整返回；其初始/最终指标、接受方向数、最终 13 成员文件、完整末点根及所有新增 typed/protected/发现顺序保持未知。
- 原 pure 与 all-batch mean/profile 未返回；不能把准备好的源或进度计数改写为费用已经支付。
- 原 run07/08/09 等完整未返来源责任及此 run10 自身未知历史均保留。新 Fejér 目标显式不同，不能把 run12 的新图、新 mesh 或其运行进度当作原 run10 同题续接；旧物理值/证书不迁移。
- 本条不触发旧输入重跑，不重写任何 queue/source。当前 run12 独立全问题继续，M320/N4096/J1845 的准备也必须保持各自真目标、真输入和模式边界。
- 原 raw 文件始终只留 runner；没有为跨 runner 把旧 scientific 输出拆成“参数”、转存 Git、Release 或 artifact。

本终态只结束了该工作流的执行窗口，没有完成原研究目标，也没有提供不可解结论。
