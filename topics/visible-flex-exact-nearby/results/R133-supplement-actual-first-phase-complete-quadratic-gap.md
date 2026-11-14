# R133 补充：当前首相位区间的实际全整数第四根间隙

**状态：已证明（当前完整首相位输入区间的算术，不含尚未辨认的根连接系数）。**

公开 Actions [43598755503](https://github.com/Rogerhu12/math-research-public/actions/runs/43598755503) 已完成全部11项数学门，实际子过程退出码0，新增数学时间1.8177038739999958秒。
本次严格消费先前δ*有限部原件，不重算原圆共轭、scalar cover、积分或root。
解析覆盖依据为[二次norm与完整有限CF基定理](R133-supplement-quadratic-norm-gap-after-first-scalar-phase.md)。

## 1. 完整输入和实际身份

定义
$$
\rho=\frac{5831714953207175+\sqrt5}{21212218271020390}.
$$
令$\mathcal J_\beta$为本次原生过程所记录的完整有向球区间；其来源是
[实际δ*有限部](R133-supplement-actual-selected-parameter-first-symbol-finite-part.md)的$-\Xi(\delta_*)/4$。
该原生区间整体包含于以下向外十进制描述：
$$
\mathcal J_\beta\subset
(18.4783243050269,\ 18.4783387425197).
$$
下面的全区间结论作用于原生$\mathcal J_\beta$；
这行放宽显示不把结论扩大到额外新增的十进制端点邻域。

| 实际对象 | SHA256或提交 |
|---|---|
| workflow事件与科学checkout | a4ea523a52b6b6d8d9c5d61c1746afb5ff1e5a10 |
| 六输入manifest | eb4d3c4b4a57808fce7bac72d6270144322cabb248caa2c5949aeabd751ea180 |
| 数学源 | d9ed9139d5955429f7cf33835f981adce810c18106a9403334ed6d6ed8e671dc |
| 执行driver | bbb6015e79202302093a38f5e173d144be11ea8e3d033daa243e5c74bdc711f9 |
| 原δ*完整native | 06070fd3b4bd7a3e4ba17d99821c0f6ad06393863bf538f9a8157b6187e60dbb |
| 新完整native | db861442f5b895362abe090306c2899b3771282269b7ccc5743d820e79f8bff3 |
| 实际process.json | afa699e3e86fc1d6678c35606b116dd8074a6ce7adfca246d8804532e32e0f0b |

[实际过程与全部门](../notes/first_symbol_quadratic_gap_ci/run-43598755503-1/consumers/process.json)
还保存完整有向系数球、最小间隙、最坏候选以及退出记录；
同目录压缩native保存全部候选与完整算术证据。

## 2. 高整数和完整有限整数

原目标是精确二次无理数。其本原整数多项式为
$$
10606109135510195\,x^2
-5831714953207175\,x
+801634672549129=0,
$$
判别式准确等于5。六输入中的有界连分数目标、精确unimodular矩阵、上述系数与判别式全部实际核过。

对于整个$\beta\in\mathcal J_\beta$，$b=\beta/(2\pi)$满足$|b|<4$。
完整极限norm区间$16\sqrt5\,b$与每个整数的距离严格大于
$$
0.217432842839813.
$$
最近整数为105。因此定理中$\mu=1/8$以及$N_0=2^{34}$的全高频二次修正条件均实际通过；这处理所有$|n|\ge N_0$，没有进行有限截止外推。

余下$97\le n<N_0$由原定理的连分数基有界整系数枚举完整覆盖。
需要逐个有向分离的候选共1502个，四个根剩余类分别为375、372、382、373个。
每个候选都通过完整区间分离与整数norm身份；
所有未列候选由同一基覆盖定理获得$1/16$的加权距离，不能将此表解释为随机抽样。

实际最小有限加权距离严格大于
$$
0.0007196196965228997.
$$
它在$n=1635$、第四根剩余类2处取得最坏候选：
$P=1798$，$N=6540$，基坐标$(22,-32)$，convergent index 11。
其整数二次norm准确为549312122180。

## 3. 同一个完整算术结论

原定理将上述全高频与完整有限候选合并，再用圆弦的全范围下界。
结果为：对每个$\beta\in\mathcal J_\beta$、每个整数$|n|\ge97$以及
每个$\zeta\in\{1,i,-1,-i\}$，
$$
\boxed{
\left|e^{i(2\pi n\rho+\beta/n)}-\zeta\right|
>\frac{1}{512|n|}.}
$$
负整数由同一实系数的复共轭和四根集合的闭合性覆盖。
于是对应的高频标量对角逆具有至多512的一阶导数损失常数；
完整193低head及独立mean不在此标量除法中删除。

本结论保留了真实$\beta/n$的一阶相位，未以principal gap减去同阶粗界。
特别地，$n=1635$的接近确已支付；不能再把所有中间整数当成未检查部分。

当前输入$\beta$仅为$-\Xi(\delta_*)/4$。
实际有向返回中的$b_{\rm root}^{\rm fin}$、声明接口项、两行positive/root匹配及strong余项仍须证明并放入同一完整operator。
原过程明确记录
`actual_full_return_beta_identification_proved=false`。
本结果因此不授全PDE逆、真参数Schur、非线性闭族或最终完成标准。
