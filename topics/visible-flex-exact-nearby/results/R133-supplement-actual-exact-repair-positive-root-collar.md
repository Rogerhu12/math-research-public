# R133 补充：精确修复背景的实际全频正根 collar

**状态：已证明（固定物理$\eta_0$、原$\nu$、精确M32修复背景的完整正根区间）。**

公开 Actions [43600926806](https://github.com/Rogerhu12/math-research-public/actions/runs/43600926806)
已实际通过23项检查，数学子进程退出码0，实际墙钟0.264400999秒。
该消费者验证[完整C1–21合同](R133-supplement-exact-repair-global-positive-root-collar.md)
在新修复背景上的所有系数与有理矩阵前提，未重算旧germ、原65槽repair、原root budget或任何response shard。

## 1. 范围、参考和全输入

背景为原ac1的精确连续M32修复，定义SHA256
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。
显式方向参数准确为$\delta=0$，所有65个repair槽包括独立even mean保留。
完整线性算子带宽为64；未知方向本身没有有限频率截断。

正根区间从真实内在根$r_*$到
$$
r_b=1192029371497/5000000000000,
$$
也可延伸至$r_*+h$，$h=9/10^6$。
整个区间在同一个原piece 2549和已证复germ内，没有新拼接点。

新光学速率为$a=-\gamma m_{\rm repaired}$。
准确全域Riccati参考满足$g_M(r_*)=M^{-1/3}$、
$p_M(25/8)=q_*/(-m_{\rm repaired}(25/8))$。
新、旧参考不被视为相同。
本根结论对其外侧任意正、有界、与频率无关的速率延拓一致；
要与真实正主体合并，还须消费该主体的新速率证书。
完整regular外算子也由另一转授负责。

每个实际非零物理频率为$M=4|j|\ge4$；
全高块为$|j|\ge97$。
按C.9定义真实normalized high状态$Z_j$。
完整输入端口是
$$
G=(h_L(r_*),\ Z_s(r_*),\ Z_u(r_b)),
$$
其中$h_L$保全部193个反射坐标及mean，未用负区匹配预先选定这些输入。

## 2. 新系数与完整反馈的实际门

原生有向球可向外显示为：

| 实际量 | 已证范围或上界 |
|---|---:|
| 修复光学速率$a$ | $1.253633367793<a<1.253801375053$ |
| 完整角drift导数$\|d_\phi\|_A$ | $0.083967997344$ |
| 完整raw primitive dyad | $0.359850928090$ |
| 独立mean rank | $2.929322032648$ |
| 全高remainder的新直接上界 | $32.041315545130$ |

共同有理比较包络给
$$
h E_H<\frac1{3000},\qquad
\mathcal I_H=\frac{3000}{2999},
$$
并保整个unbounded high空间上的真正skew transport。
全193低head与high之间的完整反馈为
$$
\rho=\frac{445236507}{500000000000000}<10^{-6}.
$$
所有正/负角锥、primitive中间模式、low-to-high shell至160、
high-to-low的drift导数费用、mean列与普通源均计入该反馈。

## 3. 已实现的全频源和迹估计

角测度与完整moving状态规范按C1–21固定，径向用普通$L^2$。
实际已证明
$$
\boxed{
\|h\|_{L^2_rL^2_\phi}
<\frac1{12000}\|f\|_{L^2_rH^{1/3}_\phi}
 +\frac1{100}\|G\|.}
$$
同一解的两端完整raw迹满足
$$
\boxed{
\|\operatorname{Tr}_{r_*,r_b}h\|
<\frac1{36}\|f\|_{L^2_rH^{1/3}_\phi}
 +\frac92\|G\|.}
$$
端口$G$的高分量按真实Riccati坐标计量，不能把这些常数直接移给未经换算的raw高端口。
普通源不要求径向导数；完整低head两行均为Cauchy数据，独立mean仍在其中。
原过程保存完整$2\times4$状态响应和$3\times4$双端迹响应的精确有理矩阵，
最终显示常数由其平方Frobenius界实际核得。
角阶0、1、2的三角bootstrap也保全drift commutator并通过同一high逆门；
这不等于同宽解析逆或负Sobolev连接定理。

## 4. 实际身份和证据

| 对象 | 完整SHA256或提交 |
|---|---|
| workflow事件 | b97068ec9149b42a4eeaf99f60acc87e7353be3c |
| 实际科学checkout | 453c76f11bf1c1548fcebd54915fb3b84427d15e |
| 16输入manifest | 7d4817826bdae3cf1e626141e36ca5b291b56aba174c640c227cc3dbda2139bd |
| 数学source | 5a0f191b11d64169aad8eccdaeb3fc428977b51e3a1ca797602eee1d7c7c0add |
| 新完整native | 86d31a375d6ee07f3919cae565dc16e47361f24cbcd6ee3ef2df8b4f23946605 |
| 原执行过程 | 7ac4224cf5260137e98e941b9816baf06058025ef0c1963b47098f2f4a1ae25c |

[原过程、23门与全部精确矩阵](../notes/repaired_global_root_collar_ci/run-43600926806-1/consumers/process.json)
直接保存全部新系数、退出码及参考范围；
完整native在同目录的repaired-global-root-collar.json.gz。
三项数学输入的原SHA保持为
397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864、
6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc、
10ff6db82cece6c72ae8a6726c07c188922cf6b307f5af5f50a691ade0abb33f。

本结论未支付$\delta Z$的band192、负区兼容、actual root反射有限系数、
strong返回余项、全主体Schur或非线性闭族。
下一步仍须把这些真实输入端口接到同一负区/正主体/regular外图，
不能由一个局部全频inverse删去端口匹配。
