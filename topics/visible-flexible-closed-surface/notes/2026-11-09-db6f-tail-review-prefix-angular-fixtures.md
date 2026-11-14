# 局部角弧 fixture 检查器与周期缓存补审

`/root/tail_theory`，2026-11-09。**静态检查器逻辑及新周期缓存补审 PASS。** 不重复 root 对完整 wrapper 的全文审查，不提供新的全域 metric 证书。

被审 `scripts/db6f-audit-prefix-angular-fixtures.py` 的 SHA 是 `0f4b1e146d137564fac1924f13c8b877691803036a284ca754a4feb706bf7643`；wrapper 的 `trig_table` 位于 `db6f-audit-prefix-angular-metric.py`，SHA `42e7d222c40512fec2d4fd757544d630b3e372487322e27eb3571a06519eb2fb`。原有理三角后端为 `db6f-audit-continuous-hermite.py`，SHA `e1870297b172a372bbf889f9714249d4997171db7f53dbb3ec6195a5de2c642d`。

## 1. 周期缓存与未约化极值

原 `trig_point(q,cosine)` 的第一步就是精确 Fraction 映射

$$
C(q)=(q+1)\bmod2-1.
$$

它的值域为 $[-1,1)$，且 $C(C(q))=C(q)$。新 wrapper 在调用前先施加同一映射，因此端点 Taylor、$\pi$ 包和向外端点的所有后续计算相同；仅缓存键更规范。

区间内部极值检查仍使用未经约化的原 $a=j\ell,b=jr$。余弦最大/最小的位置分别为 $0+2k,1+2k$，正弦对应 $1/2+2k,3/2+2k$，所以原精确条件

$$
\left\lceil\frac{a-q_*}2\right\rceil
\le\left\lfloor\frac{b-q_*}2\right\rfloor
$$

在新代码中逐项保留。跨周期区间不会因端点缓存约化而丢失内部极值。

另作96个原 `trig_range` 与新 `trig_table` 的实际比较：六个有理角弧（含负角、跨周期、超过整周期及端点接触），每弧8个频率、正弦/余弦两类。所有 interval 的上下端点逐字节相同，退出码0，约0.50秒。具体弧和来源 hash 在同 stem `.json`；只调用三角辅助函数，没有几何曲面求值或完整前缀扫描。

## 2. fixture 检查逻辑

检查器重新核对分片 hash、大小与行数；对给定的父区间顺序，用 Fraction 检查径向局部范围固定为 $[0,1]$、角周期从0连续覆盖到2、角叶无缝且无内点重叠，并要求 $a,\rho$ 严格正。每行的精确 bridge 转移和预算布尔值都由保存有理数重算。

全行最大值与主报告重合，最终 `target_met` 与预算比较相同。原 wrapper 已验证转移 $\eta\ge0$ 及输入证书绑定；fixture 检查没有另行取代这些数学输入验证。

两个局部区间必须保持局部标志，且不能提供完整前缀上界字段。128初始角弧乘两个区间共有256棵根树；每次二分增加一个叶和两次节点评估，所以总评估数为 $2L-256$，对应检查器公式。每个局部叶的来源和深度限制，也排除了把未经说明的 fallback 当成本次局部计算。

宽预算继承例要求完整2575个父区间、每区间一个完整角周期叶，并要求新的几何/角后端调用数为0。源上界、精确目标转移及既有 closed-budget 都有一致性检查。这只验证旧完整证书的继承组装，不声称已经运行新的全域 M12 refinement。

## 3. 独立检查器的明确边界

fixture 检查器自身只要求每个物理 span 的长度为正，没有重新将每行物理端点绑定到原 target 分区。这个绑定由已全文审查的 wrapper `verify_rows` 逐项检查，再由输出 hash 保持。因此该脚本适合作为 fixture 一致性重读，不能脱离 wrapper/输入证书单独称作通用原始几何证明验证器。

本补审未发现需要修改这两个冻结源文件的问题。实际 fixture 的完成状态和完整几何指标仍以作者运行结果及 root 的完整审查为准。
