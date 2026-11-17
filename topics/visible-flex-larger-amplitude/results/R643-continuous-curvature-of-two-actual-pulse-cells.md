# R643：两个真实 pulse 胞元的连续主曲率界

2026-11-17，Astra-larger-parallel-16f63c8b（AI辅助）。**已证明的范围：** 在R638同一标准IEEE binary64四则、平方根及向外舍入模型下，对R640固定的**未规范化**共同五次场，下面两个完整胞元的所有径向位置和角度满足

| 胞元（从0计） | 保存的精确binary端点 | 最大绝对主曲率的严格上界 |
|---|---|---:|
| 458 | [.9695,.96975] | 6.312502664412336 |
| 817 | [.9999843749999884,1] | 7.037155882755413 |

可使用向上放宽的有理界 **6.313和7.038**。两胞分别位于既有旧前缀曲率较大处及新pulse的末端。本条不是全部818胞的曲率证书，不把raw曲率转给规范化G，也不由曲率上界单独推出reach。

## 1. 原场身份与本次实际对象

输入为`parallel-pulse-a5-complete-base.json.gz`，SHA256

`26e53e8cdbdf6205a8bd9b2976cd4bcd36ad8734b0aca69512d705d826c5af72`。

与[R640](R640-certified-cylindrical-embedding-of-the-pulse-prefix.md)相同，保存节点及全部位置、一阶、二阶jet作为精确binary实数，逐胞取唯一Hermite五次式，保全部M320模。该场的全域C²嵌入已经由R640支付；这里直接计算其真实六jet及形算子，没有重求解ODE、重算原M112段的二阶jet或使用标量参考曲线代替实际曲面。

本次原场曲率计算不含a(s)及其积分。因此末胞的原几何五次式可以直接覆盖整个胞元，无需按R641精确标量的极短pulse分界另分两片；这不遗漏任何几何位置。

## 2. 保留径向关系的标量不变量

写真实映射为旋转标架中的R/T/Z系数。令

\[
 V=F_s,\quad T=F_\phi,\quad N=V\times T,
 \qquad E=V\cdot V,\quad F_1=V\cdot T,\quad G=T\cdot T,
\]

\[
 e=N\cdot F_{ss},\qquad f=N\cdot F_{s\phi},\qquad
 g=N\cdot F_{\phi\phi}.
\tag{1}
\]

这里N尚未单位化；旋转标架是正交标架，(1)的标量值就是空间实际值。

位置五次Bernstein控制向量按R640由两端三jet直接向外形成。一阶、二阶径向控制向量分别为相邻控制差乘5/h、4/h。乘积使用完整Bernstein乘积恒等式

\[
 (pq)_k=\sum_{i+j=k}
 {\binom mi\binom nj\over\binom{m+n}k}\,p_iq_j.
\tag{2}
\]

因此没有先把V、T等整个胞元各自装进大盒，再丢掉共同径向变化的抵消。E、F₁、G的径向次数依次为8、9、10；e、f、g依次为12、13、14。每个径向控制系数都是有限实三角多项式，前三者的最高物理角频率不超过4M=1280，后三者不超过6M=1920。

同一旋转坐标中的分量是明确的sin/cos有限谱，按这些分量的**普通角导数**直接形成(1)的一阶及二阶角导数。由于标量乘积消除了公共旋转，这些就是所需的真实标量角导数。实现按乘积律保留全部项，例如

\[
 N_{\phi\phi}=V_{\phi\phi}\times T
   +2V_\phi\times T_\phi+V\times T_{\phi\phi},
\]

\[
 e_{\phi\phi}=N_{\phi\phi}\cdot F_{ss}
 +2N_\phi\cdot(F_{ss})_\phi+N\cdot(F_{ss})_{\phi\phi}.
\tag{3}
\]

此处(3)中的导数按上述坐标分量求值；不能把单个旋转分量的导数误替为带标架连接项的空间向量分量，再混用两套乘积公式。s的最高导数仍为二阶，有限角谱使所需混合角导数全部存在。

## 3. 每个径向位置、每个角度的覆盖

固定Q=16384个等分角，使用冻结f512有向变换包围上节每个Bernstein控制系数p及其直接形成的p′、p″。所有实际带宽均小于Q/2；没有截断标量乘积或高频二导。

沿用[R641](R641-continuous-Gram-certificate-for-one-pulse-cell.md)已经证明的三角多项式Bernstein不等式：若p″的频率不超过K，则

\[
 \|p''\|_\infty\le
 {\max_j|p''(2\pi j/Q)|\over1-K^2\pi^2/(2Q^2)}=:B_2,
\tag{4}
\]

分母在程序内向下计算并检查正性。对同一个标量不变量的全部径向控制系数取最大B₂，便同时控制全胞元所有径向位置的角二导。

随后对径向Bernstein控制值及其一阶角导数做两次有向de Casteljau二分，得到4个闭子胞。固定一个子胞和一个角节点，控制值凸包给p、p′的区间。任意最近角节点距离至多δ=π/Q，所以

\[
 p(s,\phi)\in p(s,\phi_j)
   +[-\delta,\delta]p_\phi(s,\phi_j)
   +[-\tfrac12\delta^2B_2,\tfrac12\delta^2B_2].
\tag{5}
\]

式(5)每项向外计算。它覆盖该子胞全部s和相应角邻域；四个子胞及全部角邻域的并覆盖整个真实胞元。这里的Q和径向子分只控制证书的区间松弛，没有改变几何场或给出新的求解精化层。

本次直接形成二导，避免了先对有区间宽度的角网格值反变换，再把所有独立系数区间逐模乘k²所造成的无关放大。未因此忽略任何有限谱或舍入项。

## 4. 从实际Gram与第二基本形式到曲率

在每个覆盖盒内，完整区间计算给E>0及

\[
 W^2=EG-F_1^2>0.
\]

这是实际参数Gram的正定性，不把数值ODE或目标g的误差当作其替代。取单位法向N/W，对V、T作准确Gram–Schmidt，第二基本形式的对称矩阵为

\[
 B_{11}={e\over WE},\qquad
 B_{12}={f-F_1e/E\over W^2},
\]

\[
 B_{22}={g-2F_1f/E+F_1^2e/E^2
             \over W(G-F_1^2/E)}.
\tag{6}
\]

所有分母使用实际区间下端，全部运算有向；(6)的两个特征值恰为主曲率。若各盒给|B₁₁|≤u、|B₁₂|≤v、|B₂₂|≤w，则绝对值比较矩阵的Perron根给

\[
 \max(|\kappa_1|,|\kappa_2|)
 \le {u+w+\sqrt{(u-w)^2+4v^2}\over2}.
\tag{7}
\]

式(7)再次向上包围，再遍历全部盒取最大。与[R279](R279-finite-field-direct-continuous-curvature-certificate.md)的实际六jet责任一致，本次没有把全域采样最大值升级为连续界。

| 实际连续量 | 胞458 | 胞817 |
|---|---:|---:|
| E下界 | .9999999946107984 | .9999998167713589 |
| EG−F₁²下界 | .036981386570856534 | .03770280150424166 |
| (7)上界 | 6.312502664412336 | 7.037155882755413 |
| 最差径向子胞，角节点编号 | 1，3562 | 3，43 |

表中输出数字表示实际binary端点；正文的6.313和7.038是更宽的有理界。最后两胞累计实际计算30.478秒。相同冻结源在Q=8192时对胞817给7.235923529981248；Q=16384仅收紧同一场的证明包围，未变换候选或目标度量。

## 5. 来源、复现与剩余责任

[冻结源码](../notes/2026-11-17-parallel-root-pulse-curvature-direct-cell.py)，7949B，SHA256

`8fceba9ac17a3dc79ad4d35b6e38767007f1b45179c59f9589a7ff050349efb3`。

唯一有向算术/变换依赖为R638的`parallel_20261117_arclength_interval_positive.py`，SHA256

`f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`。

入口及出口校验实际输入、依赖和执行源；完整节点/三jet的finite、shape、单调性和角网格带宽门实际检查。基础整数三角、FFT及IEEE模型沿用R638，不依赖普通库FFT的未付误差。

以T为课题目录、WORK为仓库外工作目录：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  "$T/notes/2026-11-17-parallel-root-pulse-curvature-direct-cell.py" \
  --input "$WORK/parallel-pulse-a5-complete-base.json.gz" \
  --interval-source "$T/scripts/parallel_20261117_arclength_interval_positive.py" \
  --out "$WORK/parallel-root-pulse-curvature-direct-cells458-817-q16384.json" \
  --cells 458 817 --angles 16384 --radial-subdivisions 4
```

最终报告SHA256为`826977647454fab3761d530abb30d04c995ba0507ce16f28c7fad5c3c740b284`；同源Q8192胞817报告为`499ca31d0a060db3dea4993d9b08138ab40fbc22ed63002a0fad3ed50f1d28e3`。报告保完整角二导预算、实际正定下界和最差盒；raw均不入库。`geometry_amplification`只读核对了新不变量微分、带宽、连续覆盖及(6)–(7)，没有重跑大场或重复审核冻结的f512基础。

**剩余范围。** 其余816胞曲率未由本条支付；G的曲率必须另计真实λ、λ′、λ″。全t嵌入、全闭面、完整D、固定H、held、含反射商距离和全局法向碰撞/reach均不由两个局部曲率界推出。
