# 公开13/14：两次实际参考输入与N4096入口失败

## RET86：终态导读与完整历史记录

**已知后继终态：** 本文原 run13 science/pure 两次失败及 run14 输入成功均保其原真实来源和当时未知。随后实际异常在[normal 构造记录](2026-11-27-run13-actual-normal-constructor-source-guard.md)明确，两 run 后来官方 cancelled，未返回完整修后场；[独立终态记录](2026-11-27-runs13-14-actual-cancelled-without-complete-science.md)原字保留。

本版保留原笔记全部非 JSON 叙述、数值表、公式、时间顺序、来源与参数链接、接受/拒绝及错误/未知原文。2 个重复嵌入的 JSON 改为各自固定全文和精确行号引用；它们的所有原字段、命令、标量、缺值和 whole 身份仍在同一完整旧文件中。这里没有把原 JSON 重编码成数值载体，也没有改动科学源、request、ready、实际输入、checkpoint 或报告。

**完整旧文件：** 21639 字节；SHA256 `1f2ae23384116cdc6e7c5acbabb0aba9b636c8196275705d2d8b7991325f37cb`；Git blob `152fc29e9359502e3415688503606f3968594dbe`；固定提交 `0ff96dc0001b35cac2301f942e55292fe0f808ed`。[完整旧版](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run13-entry-failure-and-run14-actual-reference.md)。旧 whole-hash 读者应从该提交恢复原件；当前紧凑笔记有独立新身份，不能冒旧字节。逐块对应与恢复说明见[RET86 完整交付表](../computations/terminal-run10-14-narrative-retention-86-complete-delivery.json)。

下文“当前”“未返”“准备”均保各原节的时间作用域；旧 running 不覆盖已知官方终态。原文所称“以下完整对象”现在由紧接其后的固定完整记录链接承接，不是声称该 JSON 仍内嵌于当前正文。首次准备的 null 也不覆盖后面真正返回的事实。

这两次参考构造均真实返回0；它们的固定数值reference、carrier、input、node、scalar及target文件whole SHA与原12相同，而本次run/source归属、preparation和history/provenance文件保持各自实际身份。没有从相同数值输入推断出新求解场。

公开13在完整参考之后真实执行N4096 science及pure，分别返回1/8.492643880999935s和1/6.1936070869999185s。科学report与pure输出均未生成；仅完整command计划实际存在。当前记录不能区分入口、构造、守卫或数值失败，原异常链尚未读到，不能猜因或放宽目标/来源。

公开14的完整M320科学子进程在16:08:47 UTC的索引仍running；真实sourcecommit a9ab24c38efa6a56c17f5285fc8c8f7a5f886709、launcher596e137f6e381a2fdbc882a559a30b664c6e985095867535f3b32d7fa61c417c、PID4009。其16:08:45点e013173c13416cafc6c09d8ccad4c86993c85424c90fd6a6024c10808bc72594只属normal进度，不能填accepted、final、metric或geometry结果。

## 完整原始紧凑记录

固定读取提交04e3e5541dd83142ec445b5c95e462152627001a下：
- [13完整阶段1–4](https://github.com/Rogerhu12/math-research-public/blob/04e3e5541dd83142ec445b5c95e462152627001a/topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46028002241-1-part-001.md)，30067B，blob9de98344e8605dfd4dcda66c2759d1472bdaf7c7，SHA256 83a4ff77b0fbd9794edcfe3c51508cb02af663d8cbf08fea4468845d262f022a。
- [14完整阶段1–2](https://github.com/Rogerhu12/math-research-public/blob/04e3e5541dd83142ec445b5c95e462152627001a/topics/visible-flex-larger-amplitude/notes/2026-11-27-public-actions-46028184571-1-part-001.md)，16602B，blobbe5daabc639905ebc87078d67f9ea38b882cffe2，SHA256 98eb4446b33c6a75d35b962381101c09dbdd8b253046c170e6fd733f5640d4ab。

这些完整卷保所有原argv、输入与输出身份、源码、队列与真实返回；下面再保本次各实际输入与失败身份，科学数组和原日志仍只runner。

## 实际maker与reference

> **原 JSON 01：两 run 的完整 maker/reference 实际记录。** [固定旧版完整记录，第 19–310 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run13-entry-failure-and-run14-actual-reference.md#L19-L310)。


两个reference都保2218全leaf/完整无限尾、accuracy_reached=false、无丢弃未解尾；它们没有读取完整新物理场，未付范围如实保留。e640只是原scalar参数投影，d492是整个scalar identity，不相混。

## 13两次实际失败

> **原 JSON 02：run13 science/pure 两次真实失败。** [固定旧版完整记录，第 316–361 行](https://github.com/Rogerhu12/math-research-public/blob/0ff96dc0001b35cac2301f942e55292fe0f808ed/topics/visible-flex-larger-amplitude/notes/2026-11-27-run13-entry-failure-and-run14-actual-reference.md#L316-L361)。


不把缺report理解成某个数学不可能性；不把8.5秒据此命名为零F/J，实际执行到哪里须原异常与将来真实诊断说明。

## 已接回同runner的完整异常读取

使用已刊完整read_actual_followup_failure_chain.py原字8679B，SHA2565d25f3936fee3ae40966718ec39af16ff19ae4513fe36758af907f21baf78360、blob22e64456b28a246329513397e4ebb22f5687805e。两步从原completed status绑定实际run/step/source/log，只读最多64000原log-tail bytes和每个7000字符的第一/末异常，分别报是否截断和是否完整原日志；没有科学重跑/fixture/新门。

完整参数文件[actual13原异常读取](../computations/resume-20261127-run13-actual3-4-first-and-last-tracebacks-ready.json) 10254B / 8912a9b73b77d015b04f0390646a0e114b7014daae024aa54217a7bff8b5cdb6。新活13队列7654B / 911000c1770d5983377a941b8d9a906ad4b29c8f4b6afefc9fe87fbffd5d6a8b，两step原样，finish=false。

旧活13三个对象（reference、science、pure）均已自然返回，才从活队列退休；全三个原对象固定保347fffd9de5ed11c2cc8cda999943743c1553e39下resume-20261127-followups-13.json（93488B/8563e8619cb88493458ccd2ee351b178aae520d731305a07e669776e8fb7ac76）。原maker全对象保99b59启动提交，原完整科学ready c043及3模式仍在。没有删参数/输出/selector，失败与未知仍完整保。读回真实异常后接完整修复与新独立输出路径，不复用失败路径或冒成功父。
