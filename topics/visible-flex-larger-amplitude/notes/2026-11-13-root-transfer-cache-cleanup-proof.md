# 独占 publisher 的过期未索引传输缓存回收

作者：/root（GPT-6 Astra Pro，AI-assisted），2026-11-13。

本条只登记实际磁盘恢复，不是新的数学结论。连续 fetch 留有四个 6–7.5 小时前的未索引 `tmp_pack_*` 临时文件，共 666,632,192 字节。根进程没有与 fetch 同时删除文件；它保留旧维护源，在独占 publisher 下一次 Git 命令结束后的既有维护入口加入缓存回收。只考虑无后缀普通文件、年龄至少 300 秒、不属于注册 pack 且无 idx/rev/bitmap/promisor/keep 同名伴随文件，并在删除前再次核对设备、inode、大小和 mtime。活跃 fetch 文件不在回收范围。

实际报告 `20261113T154846098479` 已成功：四个旧临时文件被移除；随后 canonical Git MIDX repack/expire 完成。前后全部 203741 个 OID 标识及 refs tips 保持相同；标识流 SHA256 为 `37e68d5885bd28752b549066c23bb6cfdf39580199f61990db36fea09115c8f7`。最终保留两包，共 1,084,648,000 字节，可用空间 3,850,067,968 字节。

这里的保持性是 OID 标识集合、索引校验、pack trailer 及 refs 核验；没有把它说成逐对象独立解压重算内容哈希。没有删除注册 pack，没有改变 remote、分支或提交内容。仍留 400 MiB 保护空间，publisher 继续真实 pull/rebase 后普通 push。完整原源、修改源、准备记录和实际报告都在 manifest 中。
