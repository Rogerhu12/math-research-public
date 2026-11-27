# 五位 companion 首次返回：原费用已形成，checkpoint 序列化异常已修

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

[首次运行 46045307104](https://github.com/Rogerhu12/math-research-public/actions/runs/46045307104)，job 140662977474，固定提交 468c8a40bd07b72998cbb9199b7c95b2a6a72e57，源码 blob 56996cf06750e51b883604965c912e466f176836。这次失败为实现层的 JSON 类型异常，不是资源超时，也不是原数学关系不成立。

实际原回执见 [2026-11-28-five-bit-s2-companion-first-serialization-receipt-8542.json](2026-11-28-five-bit-s2-companion-first-serialization-receipt-8542.json)。运行 0.14652138700000705 秒，最大子进程 RSS 39924 KiB，退出码 1。已返回四个准确阶段：

| 阶段 | 秒 |
|---|---:|
| 完整低层 primitive Gram | 0.007976636000009307 |
| 同一完整 Schur 的四块 | 0.024376934000002848 |
| 同来源内部平方 | 0.03335186800001111 |
| 同一真实上源费用 | 0.050385693000009724 |

费用的分母仍准确为 $S^2e_4^2\delta^2\epsilon^3$。在五个初等对称变量中，每个分子条目至多 688 项，普通次数至多二十三；这与原权变量的次数五十不是同一种次数定义。整个来源没有改变，后续平方迹仍未返回。

异常发生在原子 checkpoint 的 JSON 编码：python-flint 的多项式指数 tuple 含 fmpz，原 list(p) 没有把它们转成 Python int。因此编码在写临时文件之前抛出 TypeError: Object of type fmpz is not JSON serializable，外层捕获明确给 fileProduced=false。没有假装得到可续算矩阵文件。

修正版 blob 7ca2a2d4993ddf33f2292dd1b512d201b0c84d5a 仅作三处序列化转换：checkpoint 与最终系数表中的两个指数列表逐个取 int；加权次数统计同样先转换指数。全部数学运算、来源、180 秒/4 GiB 资源界、原子保存和正性目标均保持原样。首次异常与修复分开保留，修复后的实际执行须另看其回执。

本条没有给出 S2 正性结论；它只说明新的表示已经形成了同一真实费用，以及为何该首次文件尚未保存。
