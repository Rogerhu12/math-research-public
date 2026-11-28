# GRQ 原成功日志载体读取的真实失败及首次入口修复

原首次 run [46138256969/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46138256969)，event `7445e773c297c47168b2f2e26832121a55718ff2`，job `140958293729`，在 2026-11-28 11:06:43 UTC 真实失败。失败为 `unique original scientific log`：GitHub 完整 ZIP 内使用实际编号后的 step/job 名称，没有代码预写的那一个精确成员名。失败处在第一个 `original()` 的完整文件选择，位于任何原 GCS/GPR 私有载体恢复以及所有新 GRQ 求积之前。因此原已付数学未重算，GRQ 完成子格为零。

完整失败日志 ZIP 为 79328 B，SHA256 `888e7d6ef50a3cebbf7a23ce146e972bdc083fcae7f224520ec8b31da5434384`。原失败和原工作流保持原样，真实 API 与完整日志身份见同名 JSON。

新 reader 逐个读取整个 ZIP 的每个非目录成员到 EOF，保留实际时间戳后的科学 marker，要求所有副本只产生一个逐字节相同的完整回执，再强制原完整 bytes/SHA、原成功 attempt/event、complete/proved 两门。root 用两份原完整成功 ZIP 独立实测：GCS 得原 19866 B / `201c8215275b04dfa69c6a9b03248dea6bde01bd782969d006c823088c0637b7`，GPR 得原 2950 B / `586c1a68fd29bcb622fc2a932f0f82b6fa52468215491bec41490d9265c327c9`；每份的 job/step 副本完全相同。此步骤只读旧实际日志，零数值目标、零大载体恢复。

新首次 push 入口 `fourfold-codazzi-true-ratio-original-run-log-recovery.yml` 采用已实际验证的原 run 日志端点；metadata 仍强制原 attempt 1 及成功 event。29 个整源码/证明的 SHA 与所有 Python AST 已逐一核验。除日志读取和新入口路径外，原数学、所有 root/whole SHA、范围、私有 prefix、同一正 E 和全部四个真实分支均不改。

它继续执行 [GRQ 的全域实际任务](../results/R149-supplement-fixed-label-whole-first-ratio-quadrature-and-real-reflection.md)，没有预报新的科学成功；真实全高响应及完整闭族验收仍需完成。
