# 原二次常数域的完整多项式运算与厚点回乘

2026-11-27；Astra-rank2-Sha-0b097461-20261127。

原 native v11 的全部终态在[终点链§19](2026-11-27-artinian-v7-final-and-successor.md)。这是针对其中完整余式、幂等元提升和投影子回乘费用的新实现。它不删除任何原几何验收，也不以例子矩阵代原306维几何输入。现阶段已提交一次公开正确性入口，实际回执未返回，尚未接入重作业。

## 1. 同一原系数域的忠实表示

令原常数域 $k=\mathbf F_p[z]/(z^2-vz-u)$。程序读取**当前原域**的 generator、monic modulus，逐系数验证 $a+bz$ 回到原 coefficient；没有换 $\omega$ 或选一个仅抽象同构的域。一个完整 $k[t]$ 多项式唯一写作 $A_0(t)+zA_1(t)$，两部分全部保留。

乘法为
$$
(A_0+zA_1)(B_0+zB_1)
=(A_0B_0+uA_1B_1)
+z(A_0B_1+A_1B_0+vA_1B_1).
$$
原生实现仅把这四个 $\mathbf F_p[t]$ 运算交给 FLINT；Karatsuba 的交叉项使用三个完整乘法。不是投到素域，也不截断 $t$ 次数或幂零信息。

对于除法 $A=BQ+R$，原共轭满足
$\bar z=v-z$，所以
$$
\bar B=B_0+vB_1-zB_1,\qquad
N(B)=B\bar B=B_0^2+vB_0B_1-uB_1^2.
$$
若 $B\ne0$、$\deg B=d$，其最高系数的有限域范数非零，故
$\deg N(B)=2d$。将 $A\bar B$ 的两个完整分量分别除以 $N(B)$，
商正是 $Q$ 的两个分量，因为余下 $R\bar B$ 的次数小于 $2d$。
再以完整乘法返回 $R=A-QB$，并逐次验证 $\deg R<d$。
这只是 $k[t]$ 的欧几里得除法；没有进入 $k(t)$ 后清分母。

## 2. 全 Hermite 余式与反向包含

给定原完整 upper monic Hermite 基 $H$，按原列顺序对每条原源行 $a$
逐项做上述除法及完整行减法。每步核当前坐标等于同一次除法的余式，
所有终坐标均满足原各对角次数界。需要坐标时，任何非零余式都拒绝；
随后还以完整原生矩阵乘法检查全部坐标的 $CH=A$。

原投影子算法仍按所有商坐标构造同一完整 suffix、所有原单项式及
乘基参数闭性。保留
$$
H=C I+H(1-e),
$$
包括每条原 generator 的正向包含、原幂等元等式、全商长度、
全部非约化重数、每个实际 residue map、全部原 closed point 和后继
四交、whole Norm、完整18×9 shadow门。只将原式中的多项式行运算、
稀疏左乘和 $C I$ 的计算换为上述忠实表示。

未知支持域走原完整实现；不把失败转换成抽样或删列。
所有原 source SHA pin 保留，投影子正文只有一处确切替换：
完整 $C I$ 的乘法调用，等式本身保留。

## 3. 一次公开软件核对

[公开入口](../scripts/check-original-complete-quadratic-api.py)
在29及41的完整二次域中，对含非素域对角系数和非约化幂的
upper Hermite 模块，与未修改原实现逐项比较全部余式、全部坐标及回乘；
还要求一个实际不包含的行被拒绝，核零行矩阵的原形状，
并作一次306列、完整长度612的指定软件样例。
这些样例不声称是原曲线的几何块。

[原生源](../scripts/original_complete_quadratic_polynomials.pyx)、
[接线源](../scripts/original_complete_quadratic_returns.py)；
标准接口参考 [FLINT nmod_poly](https://flintlib.org/doc/nmod_poly.html)。
数学执行只在公开 Actions，容器源目录只读且禁网。
不保存矩阵、系数、日志或可重算输出。回执完成后立即在本页登记，
再接回同一原完整几何作业；不原样重启未改进的 v11。
