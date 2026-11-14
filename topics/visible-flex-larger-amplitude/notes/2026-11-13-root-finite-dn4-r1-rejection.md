# 完整DN4首包拒绝与稳定归一重算

2026-11-13，/root，AI辅助。首包虽实际formal0/1233.71秒，但不能作为完整Jacobian证明；此前显示的36.5865和小于37结论撤回。原主包/resource保持原SHA，不篡改。尚未登记R116。

准确Fraction消费者发现4组中共2587个保存的complete项小于其自身保存的complete remainder，触发原门退出1。定位cell11/seg3/row0：真实s严格正，但宽Arb球`cbg=s+abs(ell)`含0，有限项除法返回nan；Python `max`可能静默忽略nan。不是物理分母为0，也不是可跳过的频率。详见同名rejection.json。

fresh `root_outer_actual_finite_dn4_v2.py`先严格包围`s/(s+|ell|)`与`ell/(s+|ell|)`：s使用正上下端，|ell|使用非负准确上下端，每个端点商的分母为严格正；仅完成端点商后合成Arb区间。有限源及其全部导数对(s,ell)线性，故先归一化与最终除cbg完全一致。随后每个有限项与完整尾都强制finite及非负，再取径向sup。保留所有10793叶/20非零中心/92输入/46输出/完整dc2与mean、inverse余项。4进程全量fresh运行中；只有新主包与准确消费者全部通过后才登记严格Jacobian结论。

本次拒绝不涉及已保存的R115/R114或原signed源积分；那些实现各有独立域与finite门。R106导出的完整Hessian条件工具仍是数学恒等证明，不能代未完成的数值中心矩阵。
