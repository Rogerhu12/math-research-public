# R1100：原 full47 第一项全局 CM 高度非零

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：已证明，含精确有限计算。**

## 1. 结论

在原 $X=X_{\rm ns}^{+}(47)$ 上，取
$$
q=4513,\quad B=q+1-T_q,\quad
u_4=23y_{1728}-C_\infty,\quad
u_{16}=23y_{287496}-C_\infty.
$$
高度使用 [R1094](R1094-original-disjoint-CM-heights-and-first-global-intersection-functional.md)
的原整 Hecke 稳定各向同性分裂、$\chi_\ell(\ell)=-\log_q\ell$，
以及 [R1096](R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)
的原完整 MW 整格。
准确地
$$
\boxed{\quad q^{-1}h(Bu_4,Bu_{16})=818\pmod {4513}.\quad}
\tag{1}
$$
所以
$$
v_{4513}\bigl(h(Bu_4,Bu_{16})\bigr)=1.
\tag{2}
$$
这是原47曲线、原47标记、原CM点的真实全局高度；
未用无level $j$-line 高度或旧level41的系数代替。

本结论说明第一层高度配对至少有一个单位值。
它尚不证明全部73维高度矩阵可逆，
也尚不证明原八个 CM 管内的有理点唯一。

## 2. 不重做的已成理论输入

[R1094](R1094-original-disjoint-CM-heights-and-first-global-intersection-functional.md)
及 [R1096](R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)
已证明 $h_q(Bu_4,Bu_{16})\in q^2\mathbf Z_q$，
保留实际 Hecke 的所有分歧目标和粗模重数。
因此
$$
q^{-1}h(Bu_4,Bu_{16})
=\sum_{\ell\ne q}I_\ell(Bu_4,Bu_{16})
              \frac{\ell^{q-1}-1}{q}\pmod q.
\tag{3}
$$
原 $q$ 局部项确实消失，(3)不是忽略一个尚未计算的项。

三个本轮已付的交数公式是：

- [R1097](R1097-original-level47-odd-prime-CM-intersections-and-sparse-norm-sum.md)：
  所有奇好素数的原 marked norm 和，只有两条模 $47^2=2209$ 的进程；
  含 $\ell\mid n$ 的完整 quasi 层与真正2核筛选。
- [R1098](R1098-original-bad47-CM-intersections-and-exact-vertical-correction.md)：
  坏47处的完整 admissible Néron 投影、真实 coarse 长度及
  $23^2\mathcal D_qH+23\mathcal D_qb$；
  尖点行 $6/e_i$ 的贡献在 degree-zero Brandt 列上准确消去。
- [R1099](R1099-original-level47-dyadic-CM-intersections.md)：
  原2处 marked $Q_8$ 稳定子、有效 $V_4$ wild 商和
  $G_2=S_2/8$；全 Gaussian、anti-Gaussian 和 Hurwitz 半整数格均保留。

三处均使用
$$
\mathcal D_qf(1)=(q^2+3q+1)f(1)-2(q+1)f(q)+f(q^2).
\tag{4}
$$
这里 $T_{q^2}$ 是全 degree $q^2$ Hecke，不删非循环核。

## 3. 真实公开运行

新消费者为
[full_p47_first_global_CM_height.py](../scripts/full_p47_first_global_CM_height.py)，
方法为
[第一全局高度方法](../notes/2026-11-27-full-p47-first-global-CM-height-method.md)，
参数为
[固定请求](../notes/full-p47-first-global-CM-height-request.json)。

- source commit：`d8c3e9d68f02c72c5c60945442617f898eda7227`；
- [run45955885738](https://github.com/Rogerhu12/math-research-public/actions/runs/45955885738)；
- [job140362136569](https://github.com/Rogerhu12/math-research-public/actions/runs/45955885738/job/140362136569)；
- status：success，完整 receipt 的数学时间 **4.332482299999981 秒**；
- 数学上限900秒，reserve30秒；未触及截止；
- 原官方 SageMath10.6镜像：
  `sagemath/sagemath@sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879`。

运行核实际 checkout、两README和全部理论/代码hash；
PARI 因子分解 `proof=True`，无浮点等于零测试。
本次只计算新交数，不重算原 CM-log、秩、Hodge、MW 饱和或八盘标签。

## 4. 三个实际指标的局部读数

全部 raw CM cycle 都是同一原 $y_4,T_my_{16}$。

| $m$ | $G_2(m)$ | $H_{47}(m)$ | $b(m)$ | 奇好素交数之和 | 非零奇好素数个数 |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 | 0 | 0 |
| 4513 | 22 | 0 | 602 | 58 | 6 |
| 20367169 | 56063 | 2492 | 2657635 | 374326 | 5132 |

最后两列只是有限结果的小摘要；实际(3)按每个素数的独立交数乘
其自己的 Fermat 商，不用“交数之和”替代加权和。

2处两个真正格的未除4分子分别为：

| $m$ | 整数坐标格 | 半整数坐标格 |
|---:|---:|---:|
| 1 | 4 | 0 |
| 4513 | 24 | 64 |
| 20367169 | 72540 | 151712 |

坏47 Brandt 基的 weights 为 $(2,1,1,3,1)$；
唯一 weight2 标定 $E_4$ 为 index0，
原 $T_2E_4=E_4+2E_{16}$ 标定 $E_{16}$ 为 index1。
$q$ 的直接范数式独立给602，与实际 row-action 矩阵一致。
原
$$
(v_{16}((q+1)I-H_q)^2)_4=-2777221.
\tag{5}
$$
因此包含完整垂直修正后，
$$
I_2(Bu_4,Bu_{16})=10705984524,
\qquad
I_{47}(Bu_4,Bu_{16})=-62557815.
\tag{6}
$$
坏47负值是 admissible 交数的真实垂直贡献，
不把它强行改为水平正长度。

## 5. 完整全局和与非零

按(3)归一后的三个贡献是：

| 来源 | 对 $q^{-1}h\bmod4513$ 的贡献 |
|---|---:|
| 2处 | 4256 |
| 坏47处 | 1323 |
| 全部奇好素数 | 4265 |
| 合计模4513 | **818** |

完整非零局部交数表有5134个素数，
最大为162917471。有限范数和已涵盖所有允许 $A+B=8q^2$ 的项，
不存在未处理的大素数尾项。
原 $q$ 项由第2节的理论模 $q^2$ 消去，
所以表中5134项就是(3)的完整输入。

计算没有先假定(1)非零；零值同样是允许的完整 receipt。
真实值818不是0，合 $h\in q\mathbf Z_q$ 得(2)。

## 6. 完整复算哈希

仅保脚本、请求、run/job、小结论和hash；
长局部表、矩阵、因子分解和 theta series 均不入库、不上传artifact或Release。

| 对象 | SHA-256 |
|---|---|
| 消费者 | `d01af53cac1552a2da888572ee9003ab4bbbbcaa664acd9c71f78e8369c0e76d` |
| 方法 | `f7d106fdcd4dd3c6ca2071ec786fa302a034d1928622138b6b95142c2883e65d` |
| 请求 | `c36e118d309363eb0cb0ab80e5c8a06c1f6912f1b05b1b2d70a50523124cc1d4` |
| 完整结果对象 | `4ef0f1838fc285e4e8f1e22c9878e7e2eeab64846ab14880416b130ad51f85a4` |
| 完整局部高度表 | `48175cf7040c522c6f2c3ee7ff43aa7e06f4a99650f65ae8b454c4e235b62d06` |
| 原 Brandt $T_2$ | `0dd1ba53e56092b6bd9f251ad7e395795a7c06f310aefa0ba8f75773cf06e307` |
| 原 Brandt $T_q$ | `af702a652acfd5530e37bf5678ad2cbc7f2c44b0bd42f8f81993ecc10f371e0c` |
| 原 Brandt $T_{q^2}$ | `3bb1bc67795615562b28fbf3ac09dca1b960681a7eae3fef9152e92ab1f5a0df` |
| $q^2$ 全部奇好素交数表 | `8c7242ab605151ee45ded5cf69572f7cb164ef505c4b4dc32997b85f616ead37` |
| $q^2$ 奇好范数贡献 | `d701ebfbc2c9b9f7061584430690d709310dbbc925984a52036102e16493372b` |
| $q^2$ dyadic 范数贡献 | `d63f54101f081fc952a3eae92c6f584f95704ec2279d6110b3227a91c2efdf71` |
| $q^2$ 坏47水平范数贡献 | `a64998e3487132e3857b1e1a4ec227a56efed6a468308e41557568c21c2f5d99` |

hash 的数学对象格式是消费者中的 sorted-key、无空白 JSON。
root核对完整 receipt 的 canonical JSON hash、source及request，
与 job 成功状态一致。
消费者的两模2209进程、2处半格、Brandt方向和Fermat符号另经 global_route 逐式纸核；
未安排重复执行。

## 7. 对完整高度问题的实际意义

R1093、R1096 已给
$M=\mathcal T_{4513}u_4=\mathcal T_{4513}u_{16}$，
其中 $\mathcal T$ 为 rank73 的最大未分歧整 Hecke 代数。
原泛函
$$
\Gamma(T)=q^{-1}h(Bu_4,TBu_{16})
$$
可写为 $\operatorname{Tr}_{\mathcal T/\mathbf Z_q}(\kappa T)$。
(1)证明 $\operatorname{Tr}(\kappa)$ 是单位，
因而 $\Gamma$ 作为 $\mathbf Z_q$-线性泛函是满射，
且至少一个实际 Hecke residue block 上的 $\kappa$ 非零。

完整高度矩阵可逆仍需在每个 residue block 上证明 $\kappa$ 非零。
本次一个迹值不支付这个逐块条件。
后继继续选取实际小奇 Hecke 整基并读取相应高度，
再回到原八盘内部的真正 local height 与排点；
主目标仍是 README 中所有充分大 $p$ 的无条件一致性。
