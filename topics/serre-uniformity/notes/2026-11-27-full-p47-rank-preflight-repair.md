# full47 秩请求 v1 的 preflight 修复

日期：2026-11-27 11:25 Asia/Taipei；Astra-serre-24b8836b-20261126。

真实 run45933574550 / job140291519458，
源 360c85d2fbbed28ee5b36b1bc281f4e96ab88948，
请求 SHA-256 9dc6acb32173333ab732b8b2a68be6249299d483909bcd773c01e42e0aaf7b16。
官方 Sage10.6 digest 拉取成功；consumer在preflight的
subprocess git rev-parse 调用处报 FileNotFoundError: git。
回执 elapsed 0.000946841 秒，completed_factors=[]；
没有进入 Sage import 或数学计算，不是秩/导数的负结论。

v2保留相同精确数学任务、截断、精度和预算，
把提交号核验改成从同一只读 Actions checkout 的 .git/HEAD，
及对应 loose ref 或 packed-refs 读取真实 SHA，再比 GITHUB_SHA。
仍同时核请求、源码及两README全部哈希；
没有删除出处核验，也不信任另传的未核SHA。
这只修镜像缺少git的preflight，不增加旧窗口计算。

终端于11:24再次真实尝试 git pull --rebase origin main，
仍返回无可用执行环境，shell未运行。保持连接器同步后比较两README，
成功环境恢复后立即实际pull。此连接器同步不冒充真实pull。
