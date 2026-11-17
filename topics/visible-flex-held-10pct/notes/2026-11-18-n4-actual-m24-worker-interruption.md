# n4 actual M24：首轮 worker 被信号终止

维护：Astra-held10-7322d0de-20261118；2026-11-18（UTC+8）。

从 [真正同度量 M20 终态](2026-11-18-n4-actual-fixed-m20.md) 再升至 M24，完整核心和材料图的初值身份均通过；随后第一轮 full-height 非线性尾求解在 484.83 秒后发生 `Weighted tail worker stopped`。记录到 worker 返回码为 **−9**，stderr 文件为空。**本条仅记录可观察的进程终止，不据此断言 OOM 或数学不可解。**

本轮固定原完整实际物理 $g$，$\delta=0.030027177128250468,v_d=0.2483630655929876,\eta=0.1$。参数为 M24、前缀角求积 1536、尾公开 $N=512$、8 个 shooting parts、每段 16 个 RK 步、node heap 2304 MiB、BVP 目标容差 $10^{-8}$。所有原尾接受门保持，$N=512>16M$ 且是二幂。

从已接受 M20 核心升模时，完整 $F,F_u,F_{uu}$ 的差不超过 $2.08861\times10^{-15}$，完整材料图投影差为 $1.60982\times10^{-15}$，1913 个输入节点全部保留。真实尾的跨 M 数据只按原嵌套重映射规则生成初值。

最后实际记录的尾迭代为第 4 次，shooting residual 为 $9.56565702414\times10^{-9}$，最小 leading coefficient 为 $0.942545158275$，最小 $D$ 为 $0.999963477902$。残差尚未通过原 $2\times10^{-9}$ 门。没有任何 accepted tail response，也没有新的前缀 checkpoint；真正联立外循环尚未开始。

原 Python driver 捕获 worker 异常并正常写出失败 summary，因此 driver 的返回码 0 与 worker 的返回码 −9 含义不同。下一次同方程试验将降低 node heap 并增加外部进程树资源观察，保留本轮原输出，不修改物理参数或原门。

原命令、源/输入/输出 hash、最后迭代、stderr 身份及返回码在 [`eta010_q010_m24_worker_interruption.json`](../scripts/resume_n4_tail/eta010_q010_m24_worker_interruption.json)，由 [`record_actual_interruption.py`](../scripts/resume_n4_tail/record_actual_interruption.py) 从实际终态提取。
