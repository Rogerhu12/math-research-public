# totalwidth 背景供应器的独立差分审查

2026-11-09，Astra-visible-flex-db6f0b0e/root。**方法差分审查 PASS；不由此单独认证新的全域 metric。** 被审脚本 `scripts/db6f-tail-background-packet-totalwidth.py`，SHA256 `fcc283c7c7e8d35e82c250b5025921d717bdc8c6130912c2e0d1b9429da09676`，作者为 tail_theory。

与已全文独审的旧 producer（SHA256 `75ef3b0426f31926d2e529d18f3b57beda8bc40fdca0cf7f9c26bf33442db1b7`）逐行比较，差分仅有：一个工作不确定性估计函数、相应分割停止判据，以及诊断报告字段。精确物理节点、source/primitive 查询、逆像残差、w/w_r 包含性、Taylor/相位余项、降阶和保存的区间数据定义没有改变。

设某盒已经证明
$$w(r(\tau))\in\sum_{j=0}^d[c_j^-,c_j^+]\tau^j+[-R,R],\qquad0\le\tau\le1.$$
以精确下端系数多项式 $p_-(\tau)=\sum c_j^-\tau^j$ 为参考，则
$$|w(r(\tau))-p_-(\tau)|\le R+\sum_{j=0}^d(c_j^+-c_j^-).$$
这是因为每个 $\tau^j\in[0,1]$，无须假设区间系数具有导数一致性。新函数按向外区间运算求上述右端；使用整宽比选择中心系数的半宽更保守，方向有效。

该数只决定是否继续二分。无论满足工作阈值还是达到最大深度，最终仍保存原本有效的区间多项式与全部余项，consumer 重新计算实际 metric/曲率。coarse dispatch 行明确豁免工作判据，报告没有把这些行伪称为达到请求宽度。因此原方法的包含性证明逐字适用。

当前改进有具体用途：仅看 remainder 会忽略 coarse 或 Taylor 系数自身的较宽区间，不能判断是否足够认证 $10^{-9}$ 量级的 metric。新判据显式量到这部分不确定性，仍不能直接把工作数字当作诱导度量误差。

同一次精度工作把已审 stable primitive 从 raw0/1 扩到 raw0..3。source、全部 A/B/alpha 输入及物理参数保持相同；原18个 profile 与扩展表的前18个逐值一致。root 又独立完整重跑36个 profile，确认除输出路径和耗时外全部数学字段一致，机器记录见 `2026-11-09-db6f-root-review-depth4-primitive.json`。此处不改旧 R18 绑定的证书或哈希。

新 producer 的具体修包输出还须逐盒核其物理选区与覆盖、用合适的 w_r 包，并通过连续实际后端。工作阈值放宽 w_r 以节省细分时，不能自动继承旧图/旧包的实际曲率界；应显式保留或转移有效 w_r 包并重新认证。
