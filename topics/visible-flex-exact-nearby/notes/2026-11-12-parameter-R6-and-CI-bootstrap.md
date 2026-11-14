# 实际参数扩域与并行参考恢复入口

## 已完成的数学计算

对象、准确 δ5、参考、时间分割和真实源均保持不变。
`fourfold_parameter_expanded_time_domain.py` 读取已证明的主 germ R6 域，
重新计算扩大径向圆盘上的完整无限 primitive 及参数预算，而不是更换旧R3报告的半径标签。
在实际第18段，独立 Q1024 和 Q512 两模型均证明中心和 η=10^-9 整个实参数盒的
一、二参数导数有完整R6界；Q512版本耗CPU约8.923秒。
点值采样可继续在自己已付的R3域上用另一 primitive 节点数。
若复用一个已建中心模型，调用者声明的节点数须与该模型一致。
其它真实 germ 仍按原R3域支付完整连续 crossing caps。

Q512版本实际获得中心 |fp|<1193.806、|fpp|<24291.682，
整盒 |fpp|<24291.683，实际 D 下界>0.1082348267、−K 下界>0.6918704381。
这些较宽域模数允许在同一完整 alias/时间尾预算中多域取优。
`fourfold_parameter_expanded_layout.py` 对实际第18段重算原预算：
中心 target=10^-9、N2048/K639 的时间DFT从 Nt30 减到22；
整盒二阶源 target=10^-7，仅用R6即允许 Nt18。
这是解析误差布局和剩余实际节点RMS门的计算，未声称这些新采样已经完成。

完整真源的全频首积分、时间有序二次项和空间导数仍按 R82/R86 支付。
中心一阶源与整盒二阶源的 hybrid 接口使用真实实参数线上的均值定理；
没有把中心源当整盒源，也没有假设未付的第三参数导数。

## CI 入口及实际状态

新增 `.github/workflows/visible-exact-forward-reference-bootstrap.yml` 只为这个课题恢复
原550段前腿的有限参考缓存；根README授权所需workflow修改。
源 `fourfold_ci_forward_reference_bootstrap.py` 调用原浮点驱动的原前腿，完成后不启动后腿。
初始化、准确几何定义、旧驱动源SHA、Q256、1032条共网格射线、容差2e−12均保持。
它要求每个raw输入、U/L分片、Q分片及其manifest逐一匹配历史SHA。
不同浮点结果会保存失败原因，不会自动改成新的参考或转授既有证明。

在本地实际运行 `--check-existing --no-archive` 已通过全部35个U/L和Q分片；
小报告保存为 `2026-11-12-CI-forward-reference-local-existing-check.json`。
此时远端作业尚未运行，不能把本地缓存检查称为远端恢复成功。
运行时固定 Python 3.12.14/trixie、numpy2.3.5、scipy1.17.0、python-flint0.9.0、sympy1.14.0。
即使版本相同也不假定字节相同，实际SHA门仍须通过。
恢复后只将U/L和Q打包到Actions artifact供分段计算，不把可重建的大缓存加入Git。

GitHub仓库Actions任务记录实际可读且已有任务在运行；管理权限查询返回403，
这里只记录其无权读取管理设置，没有据此声称无法运行普通已授权workflow。
CI失败时继续本地计算与强逆/非线性缺口，不以设施等待停止。
