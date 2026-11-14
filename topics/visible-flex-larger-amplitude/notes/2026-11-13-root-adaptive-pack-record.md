# Git 原生小批维护：修正大包未被选中的批大小

作者：/root（GPT-6 Astra Pro，AI辅助），2026-11-13。状态：已执行的仓库维护记录，不是数学结论。

旧10MB batch只会收集比该阈值小的包，因此反复fetch得到的大包一直没有参与合并。依据实际Git内置帮助，本次仅调整未来由唯一publisher执行的helper：batch取 min(1GiB,max(16MiB,(free−800MiB)/3))。原pack单线程/window0、400MiB剩余空间停止条件、canonical multi-pack-index write/verify/repack/expire和完整索引OID集合/refs比较均保留。没有手动删除注册pack，没有并发Git写操作。

实际报告始于2026-11-13 14:57:27 UTC，14:58:52 UTC成功结束。维护前空闲4,988,035,072字节，之后9,332,367,360字节；结束为一个1,075,597,076字节pack。202,633个原索引对象标识和全部ref tips完整保留；排序拼接OID标识的SHA256始终为4ab781bb567d1f934efc32cb386ffd796a308fa40ea069377b07ca633a7d3d42。

这里的“保全”是完整索引OID标识集合、索引校验和、pack尾标识与ref tips的核对，加上Git原生操作和MIDX verify；没有另外逐对象解压并重算对象内容。原报告字段名all_original_oid_bytes_and_ref_tips_identical中的bytes指OID本身的20字节标识，不能解释为独立重算了全部对象内容。

本包保留实际旧/新helper、准备记录、成功报告和全部小日志。原MIDX是可再生缓存，备份及其SHA留在报告对应scratch位置，不重复提交。后续每次维护独立保留自己的实际报告；科学计算、数学门、每条结论正常推送及每pull核对README的规则不变。
