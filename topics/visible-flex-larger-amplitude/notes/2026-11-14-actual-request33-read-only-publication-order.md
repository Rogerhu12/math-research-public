# actual33：目录移动报 EACCES；只读封存移到发布之后

实际公开 run [43615232598](https://github.com/Rogerhu12/math-research-public/actions/runs/43615232598)，source `c6584d0486f1b5e57d5884ea2b27592893420aeb`，job `132508749093`。下载器旧SHA `0108d824f39e1808cf64bbd599667efa707f852b0ed715627a7ee87e46e280e8`。

16:22:41.6760361Z日志记录metadata verified；16:22:48.5218510Z记录 `exclusive_payload_publication_failed`，phase为 `moving-validated-payload`，errno13，且由本程序独占创建的部分目标已成功清理。随后完整收到235561097B、程序exit2。完整压缩包及提取检查已经通过，后续带状步骤未开始；没有新的数值结果或矩阵失败。

实际旧源码先 `make_read_only(payload, extraction)` 将所有目录设为0555，随后才逐项跨父目录移动。该顺序在实际环境的目录移动阶段报EACCES。request34把顺序改成：所有核验完成后独占mkdir新目标；保持原验证目录可写直到全部子项与最后的receipt移动完毕；随后 `make_read_only(target, extraction)`，成功后才能启动科学消费者。目标不覆盖已有目录，仍保唯一run/attempt、所有原PIN和完整ZIP/成员/原数组校验。失败记录数字errno/固定phase，不记录敏感URL。

下载器新SHA `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859`。这是传输文件权限的次序修复，原band数值源 `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390` 不变，输入仍actual28完整原件。31原子rename失败未记errno，不能将33的具体errno冒填到31。34不是重复已经完成的科学试验：31/33均没有进入科学计算。
