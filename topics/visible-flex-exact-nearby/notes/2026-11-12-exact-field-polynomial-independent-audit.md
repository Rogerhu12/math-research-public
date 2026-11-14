# 精确 Fourier/time 多项式保存合同的独立核查

2026-11-12，independent_audit。已通读下列完整源码及调用预算；本核查不重跑
大角网格，也不把尚在运行的实际 package 当成已完成。

- `scripts/fourfold_phase_actual_field_fourier_package.py`：
  `c5198dcc172d4c2ef271370d4fc9b1bf39c749f20e04835e4c39cccf7498734a`。
- `scripts/fourfold_boundary_fourier_budget.py`：
  `bf1947cdfd89749cc04b48f5ee48855500044fa40340d9ed765025912af43d7e`。

## 1. 选定的多项式本身是准确对象

真实实角节点上的每个 time Taylor 系数都是实数。原区间的虚部包含零，
故将节点值选为其实部的准确 dyadic 中点，只需支付实区间半径；这不是
将一个真正复值函数的虚部删去。节点中点经过有向 DFT 后，正频系数再
选准确复 dyadic 中点，零频选准确实中点。负频由正频的准确复共轭定义。

源用 `man_exp` 保存每个实数为有符号整数乘二的整数幂，逐数准确读回。
每个四时间层的 gzip shard 有 SHA、形状、time 起止和对象 identity；
完整 reload 检查连续 time 覆盖与全部系数。保存的 P 因而是固定有限
多项式，不是一个以后可任意选点的区间多项式。

## 2. 节点误差、DFT 误差与负频

若第 i 个 time 系数的节点半径为 e_ij，则每个离散 Fourier 系数的
节点误差都不超过平均值 N^-1 sum_j e_ij。另加保留正频中最大的
`abs(directed_DFT_ball-selected_coefficient)`，得到同一层的统一系数费用。
零频实投影所抛掉的有向 DFT 虚部也包含在该费用中。

真实 time 系数的 Fourier 系数满足 c_(i,-k)=conj(c_(i,k))。P 的负频
又按同一关系准确定义，因此正频的完整误差界直接给负频；不需要再把
独立计算的负 DFT 中点当作 P 的定义。K<N/2 排除了 Nyquist 自共轭
端点的特殊问题。后面的重建预算为非零频乘2，保留了这两侧费用。

## 3. 时间/角矩形补集与物理尺度

当前域证书先提供真实函数在复时间半径 R 和物理角带 S 上的模 M，
故第 i 个 time 系数具有角带模 M/R^i。对每层分别付保留频率 alias、
系数误差和遗漏角频；再将全部遗漏 time 层与完整 Fourier 几何和相乘。
两部分正好覆盖矩形截断的补集，没有漏掉 time 与角频同时越界的角落。

程序的 P 是 sum_(i,k) c_(i,k) u^i exp(4ik theta)。它近似物理
f=dtheta/dtau，不额外乘 time 半宽 h。重建中的 `frequency_scale=4`
与节点 theta_j=pi*j/(2N) 相同，零频保留；一、二阶角导数费用中的
4、16 因子来自这个真实 Fourier 频率。

## 4. 范围

源码对当前选择的一个真实 analytic germ extension 给完整误差合同。
全实际分段时间场还须覆盖其余 active germs；保存 P 与局部误差也不
等于真实 flow、reference composition、返回图或 PDE 逆。源中的范围
标识保留了这些区别。此轮源码与误差合同未发现实质缺口。
