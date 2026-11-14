# R111 的现有绝对 mean 入口：只读接口观察

日期：2026-11-13。状态：已读取完整源并核 SHA 的接口观察；没有读取实际 M28 场盒，没有执行新的物理 RHS、Node、Newton，也没有新增或修改 wrapper。R111 已完成的精确常数与实际场输入继续分开。

## 完整源与现有导出

computations/strong_mean_homotopy_exact.js：

- SHA256 e3529092246444db572868f0dc747480b06becbdcecc907f3aff2dcc137b5d1e，完整 UTF-8 源 17281B。
- 现有公开导出：SCHEMA、Q、I、readI、velocityJets、evaluateInput、selfCheck。
- velocityJets 位于当前源第 105–115 行；公开导出位于第 252 行。
- 原 evaluateInput 第 162–163 行只积累同伦槽 1 和 3；其返回的 delta_mean_prime / delta_mean_second 不是绝对 m、m′。不得改标签后拿来支付两个不同 Gauss 网格的绝对误差。

## 不改变引擎的准确调用数据

每个物理 s / 计算角 ψ 盒，给同一实际有限场的：
\[
 d=F_\psi,\quad e=F_{\psi\psi},\quad
 f=F_{s\psi},\quad g=F_{s\psi\psi}.
\]
这些角导数不含独立高度均值。每个分量带四个 interval 槽，依次为 value、u、s、us：

- d 的每分量输入 [d_i,0,f_i,0]。
- e 的每分量输入 [e_i,0,g_i,0]。
- c 输入 [a_s/a,0,a_{ss}/a-a_s²/a²,0]。
- v 输入 [v,0,v_s,0]。

所有 0 都是引擎自身 Q/I 的精确零区间。对 a、a_s、a_ss 必须先证明它们来自同一 profile 的一致 jets；c 与 c_s 由同一比值计算，不接受两个自由、不相关的中心数。这里 u 列为零是“单个绝对场”，没有把真实设计控制的导数删掉，因为本观察不做新设计延拓。

调用现有 velocityJets(d,e,c,v,bits) 后：

- out.velocity[2][0] 是完整 V_z 的盒。
- out.velocity[2][2] 是其真实固定 ψ 的 s 导数盒。
- 槽 [1]/[3] 才是同伦导数/混合导数。
- out.P、out.W、out.D 保留 P=|d|²、W=|d×e|²、D=W−c²P³ 的完整域；函数自身仍要求三个 value 下界严格正。
- 速度包括 v d，不能置 v=0 后继续称 full mean。完整径向导数同时包含 c_s 和 v_s。

已有 API 因而足够；无需为取得绝对 mean 再建立一个物理 wrapper 或更改冻结源。

## 角平均与覆盖

若目标是精确连续 ψ 平均，对每个完整角盒 [x_j,x_{j+1}]（x=ψ/(2π)）乘正权 x_{j+1}−x_j 后累加上述两个输出槽；每个 s slab 必须覆盖全部 [0,1]，没有遗漏、重复或独立的角 Jacobian。该平均恰给 m、m′ 的区间。

若目标是原有限 N 角规则，则分别包围全部 N 个原角点，再以精确 1/N 累加；这与上一段的连续角积分是两个不同功能。原有限角点的浮点评价误差仍另加。不得把连续角盒证明直接写成原有限角表逐值已验证。

## 按原物理区间消费 R111

coarse 和 fine 各自使用自己的原物理 PPoly 节点 s，不用 raw numerical t 的长度代替。可将 s slab 再切分以对齐这些原节点；完整 Gauss6 的每个原区间仍全部保留。

对某一原物理区间 [a,b]：

1. 在每个覆盖它的 s slab 先完成完整角平均，得到 m′ 的上下界。
2. 对该原区间的所有 slab 取下界的最小值 A 与上界的最大值 B，令 Ω=B−A。这里是径向 sup 的并集，不能用 s 权平均冒代。
3. 按 R111 加 (b−a)²Ω/40 到位置预算；查询点最后部分区间同理。
4. mean 一阶结点跳的上界为 (b−a)Ω/2；这个界不将数值 Gauss 原函数自动变为 C²。
5. 原 NumPy6 规则、样本误差、端点映射和累计求和另按 R111 §5 加入。

两个原网格不同，必须分别计算这些绝对积分误差。已有同伦差 m′ 盒只能用于明示同一共同 quadrature operator 的差；不能对原 Q_coarse、Q_fine 直接替换。

若最终选精确 H=∫m 作为数学有限面的均值，则其 H′=m、H″=m′ 与同一锚保持一致，R111 量化其到原数值位置的差。profile 与非均值 knot jets 的一致性、真实 PDE 及闭合/reach 仍独立，不由本调用自动得到。

## 仍未完成

实际 M28 全物理包及 coarse/fine 完整绝对场盒未在本观察中加载。没有生成新的 m/m′ 数值，没有核销原 Gauss6 表或全场浮点评价。下一本地执行仍先完成原 full-tail audit 和已准备的 batch8 物理后处理，不重解已过的 2208 节点 Newton。
