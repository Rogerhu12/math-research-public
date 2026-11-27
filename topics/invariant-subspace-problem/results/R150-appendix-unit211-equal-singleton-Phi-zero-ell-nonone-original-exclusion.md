# R150 unit211：h=k、Phi=0、ell≠1 的完整原排除

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127（AI-assisted GPT-6 Astra Pro）。

## 1. 结论与保留纤维

在 [原 unit211 atlas](R150-appendix-essential-four-unit-two-plus-one-plus-one-original-U-value-atlas.md) 的 h=k 碰撞图上，**Phi=0、ell≠1 的全部复原点均被排除**。这来自同一点的八个未缩放原 Gram/均值/N/P 行以及两个完整 QQ 结式；不使用旧 D≠0 值图上的 Phi 排除。

Phi=0 中的 ell=1 特例仍完整保留。其原式强迫 u=2，再由原碰撞矩得到

$$
 8\lambda^4-24\lambda^3+24\lambda^2-12\lambda+3=0.
$$

本篇不使用该四次的某个根，也不声称这个互补纤维已排空。它须独立返回原 Q 与 Gram；完整 h=k 和普通 ISP 均尚未因此完成。

## 2. 同一碰撞的合法仿射解

沿用[整个 J=Q 原碰撞排除](R150-appendix-unit211-equal-singleton-entire-JQ-zero-original-exclusion.md)的完整定义：

$$
 A=2\lambda^2-2\lambda+1,\quad
 B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
 \xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,
$$
$$
 S=2\xi+3-2\lambda,\quad \eta=\xi+3-2\lambda,\quad
 w=\lambda-1-T,\quad d=1-Q,
$$
$$
 b=\ell/2+(u-\ell)\rho/(2d),\quad c=\ell/2-(u-\ell)\rho/(2d),
 \quad \rho^2=d,\quad p=1+\rho,\ q=1-\rho.
$$

此前独立的整个 T0=0 与整个 J=Q 碰撞排除，现支付 Pf=T0(J−Q)≠0。原 S=0 全图排除以及 A、B 非零也均已付。

Phi=0 的准确原式为

$$
 (1-\ell)Q=2(u-1)(u-2).
$$

在本篇明确保留的 ell≠1 图上，

$$
 Q=\frac{2(u-1)(u-2)}{1-\ell},\qquad T_0=4-4u-Q. \tag{1}
$$

仍采用原 P02、G、Pc、NF、NC。两个原仿射式为

$$
 P_c+P_ff+bcQ\Phi t=0,\qquad
 N_C+N_Ff+bcQS\xi t=0.
$$

因为 Phi=0，

$$
 \Delta=\Phi N_F-S\xi P_f=-S\xi P_f\ne0.
$$

所以整个本面都合法、唯一恢复

$$
 f=-P_c/P_f,\qquad
 t=-(N_C+N_Ff)/(bcQS\xi). \tag{2}
$$

(2) 不倒 NF；NF=0 的所有参数纤维仍被保留。源把 (1)、Delta 身份及两条 (2) 原式完整乘回。

ell=1 时原 Phi 条件只给 u=1 或2；u=1已在原域排除，故保留 u=2。A³−B²=−lambda²(8lambda⁴−24lambda³+24lambda²−12lambda+3)，而 lambda≠0 已付，得到开头显示的完整四次。这说明 ell≠1 参数化没有吞掉其余原点。

## 3. 八原行未缩放重建

用 (1)、(2) 的同一个 f,t，直接取 H=1 重建四维原 Gram。实际检查：

- E0、N0、P1、NV、二、三阶原矩；
- 两个孤立值均为 h=k=1+xi 的同点原目标；
- B/C 两条原均值、N、P 行的共轭关系。

rho 的两条实际原行同时存在，且 rho≠0，因此合法提取偶、奇系数；没有把单条二次代数方程擅自当作两个系数零式。得到八行在 QQ[lambda,u] 的原必要分子。仅剥除已经支付的原单位，其完整大小为：

| 行 | lambda 次数 | u 次数 | 项数 |
|---|---:|---:|---:|
| E1 | 41 | 5 | 252 |
| EBe | 51 | 7 | 416 |
| EBo | 45 | 6 | 321 |
| N1 | 35 | 4 | 179 |
| NBe | 65 | 10 | 726 |
| NBo | 61 | 9 | 618 |
| PBe | 77 | 12 | 1014 |
| PBo | 73 | 11 | 887 |

每个分母均逐因子审查，只使用 A、B、本图 ell−1、Q、rho²、bc、整个碰撞已付 Pf 与原 S。分子还可使用原 lambda、P02 和此前整个等权碰撞排除支付的 u−ell。不存在把新首项或多变量函数域中的一般非零因子冒充原单位。

## 4. 固定十一阶、九阶原投影与 QQ 单位

E1、EBo 对 u 的次数分别是5、6。固定使用其全部移位行组成 11×11 Sylvester 矩阵。E1、N1 的次数5、4给固定9×9矩阵。每条移位行均逐系数重建到原多项式，不随参数特化删行，不倒 u 首项。

因此任何原复解，包含上述首项变零的纤维，必须使两个 QQ[lambda] 行列式消失。实际原次数分别为463、337。只移除与已付原单位的 gcd 因子后，得到必要多项式 R143、R80：

| 原对 | 固定阶 | 原次数 | 移除后次数 | 规范升幂数组 SHA256 |
|---|---:|---:|---:|---|
| E1/EBo | 11 | 463 | 143 | 0d3f44bf266b013e6a9ee3a0de4cc3618ce56109551c4f71d320b272ac8d7580 |
| E1/N1 | 9 | 337 | 80 | aee17e029431ed6860e0b339a91bdefa8610ba31c1e0cc5eccff907790106e45 |

R143 的单位 gcd 循环标签为 A2:77、ell−1:25、S:15；R80 为 A2:62、ell−1:20、S:8。数字表示实际 gcd 循环次数，不是整块标签多项式的乘方。每一次整除及全部去除因子与剩余分子的乘回均成立。

完整 QQ 扩展 Euclid 实际返回

$$
 \gcd_{\mathbb Q[\lambda]}(R_{143},R_{80})=1.
$$

每步 Bézout 及累计两个原输入的组合都实际乘回；最终覆盖为常数1。故两条必要多项式不存在公共复根，排空整个本面。这里没有有限域抽样，也没有以多变量 gcd=1 代替单位理想。

R143 规范数组9123字节，源会确定性再生；R80 数组3007字节保在小回执。完整源保留参数、全部原构造、固定行检查、精确投影及 QQ Bézout，不保存可再生大矩阵。源获得单位后立即停止后续投影，没有增设全源重放门。

## 5. 实际执行

- [冻结源](../notes/2026-11-27-unit211-equal-singleton-Phi-zero-original-two-parameter-return-8542.py)：blob 1ddb0d712e96dad64efaaf4295bb804d03723403，12054字节，SHA256 33e266f56cf57959d538216dc347a38f871435d4fdb8633f134f559cf1ed8996。
- 实际 run46016119553、job140563577560；Python3.12.14、python-flint0.9.0、单线程。
- 源0.876927922秒，驱动0.939318221秒，峰值45852KiB，内层退出0。
- stdout24573字节，SHA256 29e7a4dee0ef9c317ac546848d1390f40966a2a6f0c8d97a7f66c7a560a653a7。
- 实际pull：2026-11-27 14:27:51.501601 UTC；提交9b749875f8896e53d3c101ecd39fc1365bbfc864，两README无差异。
- [原执行及数学小回执](../notes/2026-11-27-unit211-equal-singleton-Phi-zero-ell-nonone-original-exclusion-receipt-8542.json)。

该返回只关闭 ell≠1 的 Phi=0 碰撞面。互补 ell=1,u=2 四次域、其他 h=k 面和普通 ISP 的开放状态严格保留。
