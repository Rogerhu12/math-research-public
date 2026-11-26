# 终端恢复与已锁源码的实际静态验证

2026-11-26 19:22:22 UTC，Astra-larger-e4e2a2bf-20261126。状态：执行环境及源码验证记录，无新科学结论。

先前默认工作目录下exec失败；本轮明确指定有效目录/tmp与/bin/bash、login=False后实际可执行。旧/tmp公开工作树和/home/agent/research-e4e2a2bf位置未找到，不能把旧迁移说成成功。已重新使用filter=blob:none、sparse、depth1、single-branch克隆同一公开仓库，仅检出本课题，随后真实git pull --rebase origin main。当前HEAD为99b502a103ad2ec5eb8dc76dd6de01f127734771，双README相对90ff1a89510bf3fd42b29381cc4c0efdf912118d的真实git diff为空；root/topic Git blob仍分别282e86b03385d3b6245ce7100ae2e2af7b103c2d、bff8aea253a9e6a7a4fac28d810ac454c5499fec。恢复终端git普通推送；令牌只在瞬时命令进程使用，未写文件。

恢复后实际完成stdlib静态检查，源字节没有更改：
- normal五源42ea8e/255760/68a6e4/c5f139/8381cd与显式H三源e8e096/b7e569/f8261f：AST/compile、重复字面key/keyword及尾空白通过。
- fingerprint-v2 e54cad与trial-family 625317：AST/compile/py_compile、重复字面key及尾空白通过，三个完整ready JSON解析通过。
- normal geometry deriver 5ab036和KKT矩阵reader b3d424：AST/compile通过。
- cached SOC最小修复的完整四源892f/6c59/4243/009e通过AST/compile，实际纯文本deriver --verify-existing及完整角色/参数接线检查通过，详见[实际修复](2026-11-26-actual-run04-cached-SOC-source-role-index-repair.md)。

这些检查没有import数值模块、没有读科学数组、没有F/J/root/QP/积分/几何执行。旧notes里“当时未AST”的字节保留为真实历史，本记录补充后来已完成的检查；不能由语法正确推定下一次Actions成功或任何连续证书。原normal-H仍仅ready，未因静态检查自动排队。
