# 原指定 Phi(U^m) 的有限 Euler 算子诊断

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**状态：原公开 Actions 已成功完成；精确有限结论见 [R1134](../results/R1134-original-single-source-low-Euler-obstruction.md)。**
本次不是端值扫描，也不重复至 500000 的旧窗口。
它只为指定单源的 Hermite 消去选择方向；有限结果不能代替一般素数的微分方程或原非零证明。

## 原源及独立验收

固定同一原 $v^2=-108$、$p=6k-1$、$N=k-1$、$m=(p-1)/2$。
原 Lamé 续稿 (T31) 已证明
$$
\Phi(U^m)=\delta^{-1}\sum_{s=0}^N c_s\delta^{-6s}D^{6s}U
=U\sum_{i=0}^N h_iU^{3i}.
$$
这里
$U(t)^{-1/2}=t\sum c_s t^{6s}$，且该函数满足
$y''=3v^2y^5$、$y(0)=0,y'(0)=1$。
因此全部 $c_s$ 由分母 $6s(6s+1)$ 的有限递推生成；
这些分母在本范围均是 $p$ 单位。
多项式上的真实
$$
D^2=4(U^3+v^2)\partial_U^2+6U^2\partial_U
$$
直接给所有有限高导数，不作数值差分。

程序必须同时通过三个原来源验收：

- $D^{p-1}U=\delta=-[U^{p-2}](U^3+v^2)^m\ne0$。
- 完整纯极源恒等式
  $U^m=\sum_{s=0}^N c_s D^{p-3-6s}U/(p-2-6s)!$。
- R1061.85–86 的独立完整配对
  $\sum_i h_i\binom m{2k-1-i}(v^2)^{k+i}=-1$。

没有为归一化而除未知 $h_0$ 或 $h_N$。

## 有限问题与矩阵

仅计算 $p=101,107,131,137$。
置 $z=-U^3/v^2$、$\widetilde H(z)=\sum_i(-v^2)^ih_i z^i$。
检查
$$
L=\sum_{j=0}^d z^jP_j(\Theta),\qquad
\Theta=z\partial_z,\quad \deg P_j\le r,\quad r\le4,\quad d\le2
$$
是否有非零系数组合满足 $L\widetilde H=0$。
最大矩阵的十五列按 $(j,i)$ 排列，其完整行是
$$
M_{n;(j,i)}=(n-j)^i\widetilde h_{n-j},
\qquad 0\le n\le N+2,
$$
越界系数按零，$i=0$ 时幂取一。
所有最高次行都保留；本四素数上行数大于列数。
若最大矩阵满列秩，全部较小子类也无核。
若有核，输出原核及各较小界的准确非零核，供纸面回到源上证明；
不把拟合式登记成全 $p$ 身份。

满秩时日志只给实际独立行索引、其非零行列式、原多项式系数哈希和源验收结果。
不把可重算系数表、矩阵或证书存入仓库、artifact 或 Release。
有限输出的 scope 始终限于四个指定原输入。

## 执行与来源

- 脚本：[original_single_source_euler.py](../scripts/original_single_source_euler.py)。
- 请求：[original-single-source-euler-request.json](original-single-source-euler-request.json)。
- 公开 workflow：serre-original-single-source-euler.yml，仅请求文件的 main push 触发。
- 固定 SageMath 10.6 镜像，数学预算 300 秒、预留 20 秒。
- 原全部公式：[Lamé 续稿 §10](2026-11-27-original-lame-tridiagonal-short-flag-continuation.md)，
  [R1061 §20.3](../results/R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md)。
- 本地/V8 不执行数学程序；所有矩阵、秩、系数与行列式只由本公开 Actions 产生。

真实 run46050577346/job140680567162 已完成，全部十五列矩阵满秩，指定 minor 为36/30/63/7；三项原源验收全部通过。完整结论、source/request/result 哈希及有限范围均见 R1134。本次完成，不重跑。
