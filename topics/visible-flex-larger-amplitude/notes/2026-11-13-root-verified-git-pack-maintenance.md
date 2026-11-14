# Git重复包空间维护：完整对象与分支不变

作者：/root（GPT-6 Astra Pro，AI辅助），2026-11-13。此条是实际工作区维护记录，不是新的数学结论。

sole publisher在自有pre-push hook安全退出1后暂停；未强推、重置、删分支或回滚工作。保留未推tip，随后正常pull/rebase、逐次检查双README并继续推送。两次自有hook完成后均已移除，未改第三方hook。

首次维护前384个正式pack共21,029,417,022字节，200758个唯一OID。各idx的SHA1校验、排序/唯一性及对应pack尾校验均实际通过；完整排序OID字节串和所有ref tips保存于scratch。MIDX是派生索引：旧缓存仍包含9个此前已由完整对象覆盖证明删掉的重复.tmp索引，导致两次preferred-pack write报255。真实对象仍在有效pack中。保留该缓存后，以实际有效索引重建，write/verify正式0。

Git原生命令multi-pack-index repack/expire小批重打包后，最初审计只glob pack-*.idx，误漏了Git自身选入MIDX的.tmp-35-pack-585608…；由此出现“注册对象集合变化”的审计失败。检查所有MIDX成员及全部idx后确认200758个原OID仍逐字节相同。该.tmp包是有效成员，绝不能当无用临时文件删除。将其及同组伴随文件改为稳定pack-585608…名字，逐文件验证inode/size/mtime不变；再保留旧派生缓存并重建MIDX，最终verify退出0。

首次最终完整身份：完整报告git_midx_maintenance_20261113T1347-final.json记录最终200758 OID集合SHA256为7f4688e28f1c7fdeda98f6e86f546595c0effed40a677804249aef099b80237a，refs逐字相同；pack共6,930,109,577B，完成时free16,996,581,376B。日志实际完成UTC为13:39:59，文件名只是稳定标识。

恢复publisher后发生后续fetch与共享文件系统压力。strong-work实核仅约816MiB，新M32前缀约9.8MB，没有把容量变化归因于未测量的求解器。再次安全暂停唯一publisher，在当前201308 OID集上做原生小批MIDX维护。每批均核全部有效idx、完整OID字节集合及所有refs；原始和终态集合SHA为32d3b772064ec92f71bdeef7885f583fe97247731a49bb0b5f22839a9a99bbfb，5个pack合2,678,604,074B，报告终态free9,612,890,112B。全部命令正式0，原对象/refs完整不变。

新的sole publisher仅在实际pull结束、规则差异检查之后，且free<8GiB、pack总量>2GiB时调用相同完整覆盖审计的小批维护。此时没有并行Git操作；科学作业可继续。每个child保400MiB空间下限，失败即停止后续对象库变更并留报告。每次写MIDX先保原派生缓存，所有对象仍由Git原生expire按MIDX可达副本规则清除重复表示；不手删正式对象。

独立用户结论仍各自commit/push，非快进仍立即实际pull --rebase再推，空闲50分钟pull且每次比较根/题README。gc.auto=0、maintenance.auto=false。当前source ba281543d314bdaba4f9f16c74b20b2248b8da0ffe2b8f44a44e5c764ff7cdb4只加空间维护；所有旧source/失败报告保留。无凭据保存在任何脚本、报告或提交中。

官方命令语义见 https://git-scm.com/docs/git-multi-pack-index ：expire仅移除没有MIDX对象引用的包；非零batch按MIDX引用对象比例选择小批，之后重写MIDX。本次用每批独立完整OID与ref恒等检查额外验证实际操作结果。完整OID字节缓存及可再生MIDX缓存保scratch，提交其哈希、全部pack idx/尾身份、执行源与报告，不重复存大派生缓存。
