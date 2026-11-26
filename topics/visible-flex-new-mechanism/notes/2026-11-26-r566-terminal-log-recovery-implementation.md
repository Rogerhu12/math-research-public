# B030 原终态日志的只读恢复

日期：2026-11-26。这里只恢复既有输出，没有新科学计算。

原 run45828479581 / job139938706452 / commit
`9704840a2a00dd8345435f8024fea07187dd9923` 已由 API 元数据显示 completed/success。
专用 logs connector 多次返回 Transport closed，没有返回任何科学正文；
本地公开 API 请求也遇到 HTTP403。任务成功状态不能替代真实 scientific FINAL。

本包使用公开 Actions 的只读 `contents:read/actions:read` 权限，
先核对固定 run/job/commit 的终态，再从原 job logs endpoint 一次读取完整原 stdout。
下载重定向后不向存储地址转发 GitHub 凭据。整个恢复器只用 Python 标准库，
不 import 原物理源码、NumPy、SciPy，不做 ODE、优化、求积、旧方向或 parity 检查。

原正文按字节流完整计算 SHA256，逐行检查所有带标签 JSON。
每个完整快照都核对原81q的 binary64 SHA，保留所有标签计数、拒绝原因计数、
真实保留q的全部变化、小型运行元数据及完整累积费用。
最后真实完整快照的原 JSON 文本只输出一次；其中保留 actual/pending 物理约束、
working rows、实际与拟议 trust、最后试探、后端状态和全部费用，不能把试探当接受。
若没有 FINAL，就明确最后完整 checkpoint 之后的未冲刷工作未知，
不能以0记入科学成本，也不能靠 run success 宣布目标完成。

原 stdout 不写文件，不生成 artifact/Release，不提交 Git，不切块传送。
公共恢复 run 的 stdout 只包含紧凑全解析收据和一个必要的最后实际状态，
后继研究可据此构造真实新输入。恢复器的网络/解析耗时独立列为元数据成本，
不能重复算入原已付科学时间。本地只做 AST/JSON/hash。
