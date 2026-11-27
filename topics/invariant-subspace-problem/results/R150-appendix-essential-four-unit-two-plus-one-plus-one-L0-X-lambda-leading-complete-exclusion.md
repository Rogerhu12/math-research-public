# R150：L0 原 X 曲线的整个 lambda 首项零面已排除

日期：2026-11-27（台北时间）；会话：Astra-ISP-8542378f-20261127。AI-assisted GPT-6 Astra Pro。

**结论。** 在原已付 L0 图中，必要曲线 $X_{34,52}(\lambda,w)$ 的 $\lambda$ 首项处处非零。因此 $X$ 可在已付原参数局部环上首一化为34次多项式；此结论保全部首项零纤维，不宣称整个 L0 排空。

## 1. 原输入与准确首项

沿用[原八行曲线 C](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-eight-by-eight-original-parameter-curve.md)及[原完整参数曲线系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-three-original-parameter-curves-system.md)。自含源从原 Frobenius Gram 重新生成全部原式，重建 $C=C_{39,53}$ 的八列 cofactor，并计算完整 $X=\operatorname{Res}_\rho(F_E,F_N)$、仅剥已付原单位。

两个原曲线的规范 SHA256 分别是：

- $C$：`6057a487720992327d9e065ec6b7ef5e54896637f1c756a28391fd734737b50c`；
- $X$：`519fe7c69a0cf7c05283aa66833331b64e7654bb6ec0daec606c49b2c2a02f68`。

源码逐项验证

$$
\operatorname{lc}_\lambda X=
\frac1{288}w^{11}(w+1)^9(2w+1)^5H_7(w),
$$

其中

$$
H_7(w)=9w^7+190w^6+1584w^5+4278w^4+5215w^3+3204w^2+960w+112.
$$

原 $w=0$ 支已完整排除。以下分别返回另两个线性因子和整个七次因子，没有先假定其中任何因子非零。

## 2. 两个完整原参数纤维的 QQ Bézout

直接把 $w=-1$ 或 $w=-1/2$ 代入两条必要曲线，不除其新首项。在 $\mathbb Q[\lambda]$ 中实际求并乘回

$$
a_{w_0}(\lambda)C(\lambda,w_0)+b_{w_0}(\lambda)X(\lambda,w_0)=1.
$$

| $w_0$ | 原特化 C/X 次数 | 两 Bézout 系数次数 | 系数合并 SHA256 |
|---|---:|---:|---|
| $-1$ | (32,24) | (23,31) | `1c8dc3119ce4c16316b1a0654a4d5334fd72b47b21716a65d43b9dd3280597a2` |
| $-1/2$ | (33,29) | (28,32) | `3fe89094458a82546070c8c023609ae6550e35d3c374252b655add2dbc65b74d` |

每条身份完整计算两个乘积及其和。这排除全部对应原纤维，并支付 $w+1$ 与 $2w+1$。

## 3. 整个七次曲线的完整有理数覆盖

假设某个原点满足 $H_7(w)=0$。因它还满足 $C=X=0$，其 $\lambda$ 必须同时为以下两个完整 Sylvester 结式的零点：

$$
R(\lambda)=\operatorname{Res}_w(C,H_7),\qquad
S(\lambda)=\operatorname{Res}_w(X,H_7).
$$

实际在 QQ 上取得完整非零 $R$，其次数为273，SHA256为

`ca33bb5db44724d0958a119048ff549c0052cbddb2176a6f170fda88d6f424ad`。

没有删去 $R$ 的任何因子。源码核验 $R$ 的首项在素数1009处为单位，且除该首项后的所有有理系数在 $\mathbb Z_{(1009)}$ 内。

对完整 $S$ 计算模1009的约化。两个输入所有分母均为1009单位，且原消去变量 $w$ 的次数52和7在约化后完整保持，所以得到的就是原 QQ Sylvester 结式的约化。结果为231次，SHA256为

`c720b2d7910e2b588e429226857bfdf443fe51e8b021f5ce681586ded581b9ae`。

随后实际计算并验证

$$
a\overline R+b\overline S=1
\quad\text{于 }\mathbb F_{1009}[\lambda],
$$

两系数次数为230、272，合并SHA256为

`f00f2bc4afa3b1cba5954d973da72fe54d9781542b2f94e3190ded8d9cf4139c`。

若原 $R,S$ 有共同复根，取其在 QQ 上的单首项最小多项式 $h$。由 $R$ 的单首项版本在 $\mathbb Z_{(1009)}$ 内及 Gauss 引理，$h$ 的系数也在此环；用单首项 $h$ 长除 $S$ 不离开该环。于是正次数的 $\bar h$ 同时整除 $\overline R,\overline S$，与实际 Bézout 身份矛盾。

所以 $H_7$ 的所有复根均排除；无须选择其嵌入或证明其不可约，也未从一般多变量模单位提升特征零判空。

## 4. 合法首一化与下一原输入

现在首项全部因子均由独立原返回支付。于是

$$
X_m=\frac{X}{\operatorname{lc}_\lambda X}
\in \mathbb Q[w,\mathcal S^{-1}][\lambda]
$$

确为34次首一多项式，其中新增单位仅为 $w+1,2w+1,H_7$。源码检查分母全部来自这些已付单位并回乘 $X_m\operatorname{lc}_\lambda X=X$。

这允许在同一已付环对其余原参数曲线作 $\lambda$ 除法，逐条保留原组合及余式；没有倒置余式的新首项。原同 rho/t 点和全部原 P/N 约束仍须处理，首一化本身不等于一般 L0 排空。

## 5. 真实执行

- 自含源：[2026-11-27-unit211-L0-X-lambda-leading-complete-original-return-8542.py](../notes/2026-11-27-unit211-L0-X-lambda-leading-complete-original-return-8542.py)，19666字节。
- 源SHA256：`579c3c755b7356598085dd1577a9951736c85f6ada1e8e6e4346e1f02f0d5029`。
- 实际21.538033089秒、RSS95836 KiB、exit0；源alarm180秒、外部硬限190秒、地址空间4GiB。
- stdout18493字节、SHA256 `41594763babc0cbc80c20b5e04cdc6b4c0f795e106c0d1e73f863816f59b0fdc`。
- [原返回小回执](../notes/2026-11-27-unit211-L0-X-lambda-leading-complete-original-return-execution-8542.json)。

原曲线在本次自含来源中再生，不读取 scratch 系数缓存；这里没有重跑任何已冻结的大投影或完整单位门。
