# 固定有限弧长坐标的全径向正性准则

**解析不等式已证明；本次数值代入使用浮点，未作向外舍入，因此不称严格区间证书。** 对前条β=.75的新候选，覆盖全部509个quintic胞元的下界浮点评估为 `.1152143973420771`，不是只检查径向样本点。

设N为偶数，I_N为含单cos Nyquist项的实三角插值。基函数

$$l_j(\phi)=N^{-1}\left[1+2\sum_{k=1}^{N/2-1}\cos k(\phi-\phi_j)+\cos \tfrac N2(\phi-\phi_j)\right]$$

的离散正交关系给 $\sum_jl_j^2=(N-1+\cos^2(N\phi/2))/N\le1$，故 $\|I_N\|_{\infty\to\infty}\le\sqrt N$。

若一个径向胞上 $|F_{s\phi}|\le B$，范数的反三角不等式直接给

$$\|q_N(s,\cdot)-q_N(t,\cdot)\|_\infty\le\sqrt N B|s-t|.$$

此步不除q，不先假设它正。F_sφ是归一胞坐标的四次向量多项式，把其径向系数变为Bernstein控制向量；凸包性质及各控制向量的角Fourier系数l1界给B。R/T/Z分量界分别是 $\sum|\nu R_j+T_j|$、$|R_0|+\sum|R_j+\nu T_j|$、$\sum|\nu Z_j|$，三者欧氏范数组合后取五个控制向量的最大值。

在每胞的n等分点，角网格Q给下界 $\ell=\min_\phi^{\rm grid}q_N-(\pi/Q)\sum_k|k\widehat q_{N,k}|$（求和含正负频率）。任意径向点距最近等分点不超过h/(2n)，故整胞下界为 $\min\ell-h\sqrt N B/(2n)$。严格包围后若正，则所有构造节点上q=q_N>0，也使有限q_N系数具有所需C²径向正则性，无循环假设；随后前条的隐式圆周坐标在全段有定义。

本次N2048、Q4096、n4。最差胞381、s∈[.9275,.93]：角下界代入 `.1736886696928441`，径向扣量 `.058474272350767006`，B=`4.134755450417543`。全胞B最大 `5.626455634950988`；固定ρ的全角下界代入 `.15211767782160537`。上述裕量很大，但脚本未提供各浮点FFT/平方根/多项式运算的定向误差封闭，严格数值正性仍留这一明确差距。

复现源 `parallel_20261117_arclength_positivity.py`，参数 `--input parallel-model-inward-svd-b075.json.gz --construction-angles 2048 --angles 4096 --radial-subdivisions 4 --out parallel-model-inward-b075-arclength-positivity.json`，同前条PYTHONPATH/单线程环境。父SHA256 `852a673f4464090f003fd44c3247a819cf9bae0418d07caf97f8edb0e3d39471`；源 `4da40fcad310801453b0d05783a979df562652fb1b2fa54501a17d8c18edf908`；输出 `27a21741a5a2fc7917a03da0eb851edcccfa2cf56c16c56b33eb6aa843ea46f7`。raw留scratch；没有改候选、目标g或原求解器。

本条保留原浮点评估的范围；后续[R638](../results/R638-global-positive-arclength-coordinates-for-two-prefixes.md)用有方向区间运算结清两条实际候选的全域正性条件。
