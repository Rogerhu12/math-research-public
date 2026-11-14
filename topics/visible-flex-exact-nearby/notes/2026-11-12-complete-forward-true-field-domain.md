# δ5 完整前向真实 field 的全角/复时间芽覆盖

**状态：已证明，R65 的实际完整 forward 输入。**
准确对象仍是 δ5 affine、显式对称、完整无限 R33 图；
原点 0d17500a…、方向 8db5d57d…，准确
$p=-7789843107295549/4611686018427387904$。
没有转用旧近镜像浮点对象。

## 完整覆盖

规范 index：
data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_sharp_time_domain_forward.json.gz。
全部 550 段完成，其 SHA256 为
5cf017df6f91a1e5d29a6464a9c3fcf8b82586fda10f9c28fcbd14d218ca6271。
相同字节保存在 forward_complete_snapshot.json.gz。

准确时间/芽继承闭包报告：
data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_sharp_time_domain_forward_complete_closure.json.gz，
SHA256 ce0f479c193de10e0a6ca6792176d38c24c574e1720ddf05aadcd16978e480bd。
源 fourfold_phase_forward_domain_cover_verify.py：
e4c4282fdb85e14c91debb61962718cfdbd7cbb98fd57e1981245cedd44668e7。

所有段的真实物理时间从准确 $-\pi/2$ 接到准确 $+\pi/2$。
547、548 两段各在一次真实整段域失败后分成两个闭子段；
其余段不需要时间二分，共 552 个最终叶。
失败尝试保留在闭包中。闭包共含 518 个直接芽域及 381 条继承链接，
这里包括祖先域依赖，不将该数冒充最终时间叶数。
全部 587 个闭包文件的名称、字节数和 SHA 均在报告中。

## 数学作用域

每个最终叶按 R65 的准确 $\tau=c+hu$ 定义局部复时间盘 $|u|\le3$，
物理角带宽为 $1/64$，并保留该真实实时间径向像需要的所有相邻样条芽。
普通芽支付 $D$ 排零及 $\operatorname{Re}(-K)>0$；
转折芽支付 $D$ 排零和消根后的 $\operatorname{Re}Q>0$，
而不是强迫跨根的 $-K$ 保正。
反射继承同时改变真实时间中心、方向和实际 radial germ，全部盘包含用准确
有理数加有理数倍 $\pi$ 再有向比较；没有用端点相近代替整个复盘包含。

每一物理段的归一化子区间准确覆盖 $[0,1]$，无重叠内部、无缺口；
这些段再按准确参考时间网格连接，故覆盖全部前腿。
每个叶的正确实际 spline germ 由 sharp sine 单调端点决定；
相邻芽在真实 knot 的匹配阶和小帽收费仍须保持。
此处没有把整条分段函数声称为跨所有 knots 的单个全纯芽。

输出明确 whole_forward_leg=true、whole_both_branches=false。
R77 证明该显式对称对象的全 principal return 为真实前腿映射的平方，
所以后续优先验证一次完整前腿。
该恒等式不允许把保存的 $P\circ H$ 直接平方，也不丢掉第二次复合的域和误差。

本项只完成真实局部场域覆盖；完整小缺陷密度、有序积分、参数源、
实际共轭/KAM 和 PDE 逆仍需继续。
旧 full index 在环境杀进程时停于 280 段，该文件原样保留；
新的 forward-only 任务从相同已完成叶恢复，最后全部实际完成。

## 重放闭包

    python scripts/fourfold_phase_forward_domain_cover_verify.py \
      --index data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_sharp_time_domain_forward.json.gz \
      --snapshot data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_sharp_time_domain_forward_complete_snapshot.json.gz \
      --out data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_sharp_time_domain_forward_complete_closure.json.gz \
      --require-full --bits 192

直接域的完整计算入口保持 fourfold_phase_sharp_time_domain_cover.py；
使用原始 source SHA 582d97cf…、Q256/root512、N512、160 bits、
完整 forward 段、原有种子和 resume 记录。闭包不重跑已完成的 Fourier/time 预算。
