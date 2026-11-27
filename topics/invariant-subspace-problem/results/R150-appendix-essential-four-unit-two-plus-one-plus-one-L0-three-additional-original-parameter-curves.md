# R150：L0 九行原 rho 矩阵的三个新增参数子式

日期：2026-11-27（台北时间）；会话：Astra-ISP-8542378f-20261127。AI-assisted GPT-6 Astra Pro。

**结论范围。** 在已付原 L0 物理图上，每个原解的同一 $(\lambda,w)$ 还必须满足三条必要曲线 $C_8,C_5,C_2=0$。本稿完整支付它们的原理想来源和全部消元主元零纤维；未排空整个 L0。

## 1. 同一原低 rho 输入

沿用[原八行曲线](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-eight-by-eight-original-parameter-curve.md)及[完整原必要输入](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-full-original-paid-rho-leading-system.md)，保原同一点的 $E_1,N_1,E_{B,\mathrm{odd}},E_{B,\mathrm{even}}$，在已证原 $P_1$ 系数非零图代回同一个 $t=-\beta/\alpha$。记清分母并只剥已付单位后的原 rho 多项式为 $F_E,F_N,F_o,F_e$，其次数分别为 $5,5,6,7$。

使用以下九个真实原行，索引从零开始：

| 索引 | 原多项式行 |
|---:|---|
| 0,1,2 | $F_E,\rho F_E,\rho^2 F_E$ |
| 3,4,5 | $F_N,\rho F_N,\rho^2 F_N$ |
| 6,7 | $F_o,\rho F_o$ |
| 8 | $F_e$ |

每行次数不超过七；列为 $\rho^7,\rho^6,\ldots,\rho,1$。旧 $C_{39,53}$ 对应删去第7行，本次不重算这一旧结论，而分别删去第8、5、2行，得到三个新的 $8\times8$ 矩阵 $M_i$。源码由各行系数重新构造原多项式，逐行断言一致。

## 2. 完整多项式证书，不倒置点上主元

每个矩阵在 $\mathbb Q[\lambda,w]$ 上作分数自由消元；每个除法都验证商乘除数等于原分子。逆向恢复常数坐标的 cofactor 行 $c_i$，逐列实际验证

$$
c_iM_i=(0,\ldots,0,D_i).
$$

三矩阵共24个系数恒等式全部通过，并再直接回乘原多项式行：

$$
\sum_j(c_i)_j\,r_j=D_i.
$$

这是通常多项式身份；任何消元主元在某个参数点为零都不影响该身份。每个原解的真实单项式列末坐标为1，因此必有 $D_i=0$。

对 $D_i$ 只剥已付原物理单位和独立完整返回过的 $W,G,K,V,\alpha$ 因子，得到 $C_i$。源码准确核验 $D_i=s_iC_i$，并核验 $s_i$ 的所有非常数因子均在已付单位中；没有把局部 $\beta$ 首项当全域单位。

| 删行 | 完整 $D_i$ 双次数 / 项数 | 必要 $C_i$ 双次数 / 项数 |
|---:|---:|---:|
| 8 | (84,126) / 8324 | (39,54) / 1884 |
| 5 | (88,126) / 8670 | (40,53) / 1848 |
| 2 | (88,127) / 8760 | (40,54) / 1890 |

规范源码表示的 SHA256：

| 曲线 | SHA256 |
|---|---|
| $C_8$ | `16720813d546e77a4847da2ab9777eb6d009ced33085a7164e9e78909f14c36b` |
| $C_5$ | `e794abe1f3c03c6cbda5fa7474b4a7d3a4e5b70e6996c0ee19dc3e5cbeb0cb05` |
| $C_2$ | `9090d7ebd9cea351271a0ddd7b7d7a9bce16da6d333045cf49f05b276af0d36d` |

所有原 $P/N$ 方程仍是必要条件；新三曲线仅增加原参数约束，不替换原同 rho/t 返回。

## 3. 实际执行身份

- 自含源：[2026-11-27-unit211-L0-three-additional-original-parameter-curves-8542.py](../notes/2026-11-27-unit211-L0-three-additional-original-parameter-curves-8542.py)，16480字节。
- 源 SHA256：`6a2e37636bc190e4fa9d6e4299f1e66f27e0d2657f6e75284f28bf19ea87537a`。
- 实际墙钟51.704209952秒，峰值RSS103552 KiB，exit0。
- 源alarm230秒、外部硬限240秒、地址空间4GiB；没有放宽旧失败门重跑。
- 标准输出22074字节，SHA256 `820283fb181053c5ee626f2b19e9ab529a34ff964786a903b81e70a93feb552e`。
- [小回执及三个完整返回轮廓](../notes/2026-11-27-unit211-L0-three-additional-original-parameter-curves-execution-8542.json)。

源码末尾会将可重算系数缓存写到 scratch 的固定路径；复现前建立其父目录即可。缓存不是证书输入，也不入库。后续可从本源码原行重新生成曲线，继续首项组合或原参数覆盖，不能从这些必要曲线本身宣称一般 L0 无解。
