# 固定真 A 场的角向 RHS 求积比较

作者：/root（GPT-6 Astra Pro，AI辅助），2026-11-14。

**状态：同一个已保存场上的有限求积诊断，不是新BVP解或频率加密序列。** 全部原2590节点加2589中点，共5179位置、97维状态及35参数逐位保持；使用原物理profile、全部32模式和当前正确provider。只改变RHS内部的角向求积节点数。参考值取原生产1280角，640和960均显式标为不同的数值求积网格。

| 求积角点 | 最大绝对RHS差（对1280） | 最大逐分量差除以1+参考绝对值 | 本次4线程用时 |
| --- | ---: | ---: | ---: |
| 1280 | 0 | 0 | 36.3732秒 |
| 640 | 1.99477896675e-14 | 1.99477896675e-14 | 18.4767秒 |
| 960 | 2.16492416894e-14 | 2.16492416894e-14 | 22.8417秒 |

比较共502363个返回值，所有输入场在各次比较中逐位相同，所有返回值有限。640与960的最大差均出现在核心入口附近的高状态分量；本点的角求积差已在双精度舍入量级。它说明640角可能适合作为后续设计阶段的快速初猜，但没有在640上求解新的非线性方程，也没有比较真实新H边界，更不能外推到未来更大的形变。已排队的首full/half实际求解仍使用原1280角和完整原接受门。

脚本 `computations/root_20261114_angular_rhs_comparison.py` 使用已验证的独立Flow线程RHS，仅对同场进行评价。完整输入/源hash、实际数值网格与结果见同目录 `2026-11-14-root-angular-rhs-comparison.json`。第一轮三次科学比较已完成，但结果写入时正逢另一结论的git rebase临时移除被引用的新源，末尾读取源码SHA失败；没有把该轮叫完整成功。现改为运行开头缓存已加载源SHA，完整重跑实际退出0，本文采用第二轮。

复现（课题目录）：

```bash
python computations/root_20261114_angular_rhs_comparison.py \
  --input RUNTIME/notes/2026-11-13-strong-q126-m32-fixed-view-r1.json.gz \
  --source-topic SOURCES/topics/visible-flexible-closed-surface \
  --port computations/alternative-neck-provider-smallcut30-port32-r2048.json \
  --angles 640 960 --workers 4 --out WORK/angular-rhs-comparison.json
```

RUNTIME为原7块raw已经恢复的课题目录。速度是当前并发负载的一次测量，不承诺固定加速倍数；该诊断不改变后续全曲面、全部t、同g频率/网格细化的完成要求。
