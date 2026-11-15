# R150：未推自然32阶结果与最小临时重建

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

## 实际中断位置

原临时 session run43679903558 在2026-11-15 09:57 UTC结束。步骤 selected-natural-u-schur-through32 的数学实际退出0，但发布摘要时把历次pull记录全部累积，文件达到100000字节上限，触发“only small execution summaries may be published”。未强行绕过仓库上限；主分支没有该步回执。作业临时来源数组随结束不可继续使用。

运行日志 ISP_REMOTE_STEP 记：execution source48fbd2f22a5ee247906eb5c73fe2b3fd73816051，数学8.913560867000342秒、墙钟8.989100837003207秒；原raw65518B、SHAd3cf7a1bc57ca39e39fe6c4c3c63d8ef664bf5cfb5eac97b9b654b6d0fe155c5。日志列出全部36指数，最后四个17、18、18、21，总243。此处只记录未推检查点；按用户要求重做未推结果之后，才能形成该步正式结论。

此前八阶、十六阶及零/无穷远三阶的小回执和证明已实际推送；其来源代码、输入身份和临时文件哈希仍在main。丢失的是作业临时数组，不是已推文本。

## 最小输入恢复与数学比较

[新会话源码](2026-11-15-r150-recovery-small-session-789f.py)只读明确固定的历史Git对象到临时目录，不使用或创建Release资产。历史提交8c6304e273e64b0544d3dd58bc0e48a672a87c36保原native、3333来源forward/backward、985选列来源DAG、规范kernel36、point模型、selected小回执和primitive原式。各字节数和SHA直接列于[新请求](2026-11-15-r150-recovery-small-session-request-789f.json)，每份实际读取都核验。

临时丢失的selected字典模型、unit-row profile及自然first缓存需由原字典/源码最小重建；不重整条Dixon、LLL或旧normal-form消元。重建的压缩字节若含新mtime，必须使用其真实新输入身份，不冒称旧压缩SHA。数学runner与native可以保原源码，外层明确登记新输入绑定和同一原I,J。

已推十六阶回执保存0至16阶全部51份 source/Schur/residual 文件的SHA。重建来源数组若只有64字节输入binding变化，可按公开的固定二进制头规格将其binding映回旧值后逐完整字节核验全部51份，验证同一原数学内容。新32阶必须真实执行并发布其独立回执，不能把旧日志标记为新run。

## 防止摘要与同步历史再次失控

每次pull仍真实执行pull --rebase并核两README，逐条完整记录到作业日志。发布摘要只附最近两条pull记录、累计条数及全部pull记录的规范JSON哈希；HANDOFF继续记录最近已读提交。

回执展示层对两个已验证的重复36阶数组保存规范JSON身份，不重复铺开。若其他可重算参数数组使小摘要接近上限，省去数组正文并保字节数、SHA及字段名；数学内存对象和临时完整回执不变。写checkout前先核100000字节边界，主回执不分片、不编码上传、不放大工件。

每个数学步骤仍保持独立来源SHA、完整参数、实际run/step、实际退出码和完整临时回执SHA。失去数学回执的外层超时只记真实失败，不补写完成标志。所有结论逐项实际push，非快进继续pull --rebase重推。

## 同时继续的不依赖旧大数据的数学

完整三normal校正只依赖已推的first、second-pure、second-normal、third、single-cubic五个小回执和源码。新接口先保全部2295高来源的990列真核，再把其低1088像加入第三页；不丢弃高来源，也不预判新秩。这项可先于自然32阶恢复执行。
