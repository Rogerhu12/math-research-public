# 本轮资源处理的实际观察

这里只记录工作副本与临时文件的驻留状态，不是数学结果；没有删除 Git 对象、refs 或数据历史。

- 只读 pack 检查64939留下37106B报告，SHA50239a0c…，其最终工具回执在截断中丢失；后续poll报Unknown process，不能冒称exit0。报告给38包、同分区联合冗余仅163827B；未据此删除包。
- root在c5f478观察发布shell无GIT_INDEX_FILE覆盖。七个旧任务/tmp upload-index由原字节SHA逐件约束，压为六个完整gzip，每个解压SHA/长度核同才移除原件；bc322d实际exit0，逻辑回收89317349B。原字节保留于/tmp/db6f-retired-upload-indexes，恢复说明在root-retired-upload-index-preservation.json。它们不是当前Git index。
- coupled只读候选f84ee1/exit0给42件已发布历史f64共112283725B，排除全部活动/未来绑定与正式M12 r01。root再次核本地idx、禁网cat-file解码、tree/index/工作区SHA后，031de1实际exit0以skip-worktree移除工作副本，观察free909287424→1018945536，selected Git状态clean。
- 下一独立工具eaf687观察42件重新出现、inode改变、内容大小仍同，free899215360。原因未查明，不能把这次回收写成持久成功。
- root将primary配置改为noncone并以47条规则明确排除同42路径；5123e6中git子进程0，但根“当场移除42”断言失败（实际0件被移除），因此没有写虚构成功报告。check-rules实际6b367f/0确认42路径均应排除。再refresh selected status/reapply，0b5690实际exit0当场42件不存在、free1008152576；下一工具84855e又看到42件重现、free892690432。模式内容保留，不猜工具/同步层原因。

今后发布前以实际free和当时的sparse reapply结果为准，不降低原helper的race-retry空间门；若需旧数据，local Git中完整对象已逐字核验。原候选清单及恢复脚本均保留。当前数学脚本/参数/绑定未变；本节任何文件存在/不在也不代表solver存活或成功。
