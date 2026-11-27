# Phi=0 主图 v=-1/4：真实原三多项式将值参数缩为 lambda=1/2，未排空

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 原范围与实际返回

接 [主 rho 头零的八权参数覆盖](../results/R150-appendix-unit211-Phi-zero-main-rho-head-eight-weight-cover.md)。本次只把上一完整模 gcd 的线性因子用于选择一个新的确切 QQ 纤维
$$
v=-\frac14,\qquad
(u,Q,\ell)=\left(\frac34,\frac54,\frac12\right).
$$
先实际核验
$$
H_7(-1/4)=-169/512\ne0
$$
以及该主图六个已付权单位均非零，所以在这个纤维使用保存的 $C_6,C_9,C_{71,29}$ 合法。它没有在整 $H_7=0$ 分支使用只付补图的 P6/P9。

三个完整原多项式的 $\lambda$ 次数仍为 $6,9,29$。实际 QQ 欧氏及每一步完整 Bézout 乘回给出
$$
\gcd\bigl(C_6(-1/4,\lambda),C_9(-1/4,\lambda),
C_{71,29}(-1/4,\lambda)\bigr)=\lambda-\frac12.
$$
前两输入的 Bézout 系数次数为 $7,4$，第三输入保持同一 gcd。没有把各多项式的首项或未知因子先当作单位。这严格证明该权纤维的每个原解都满足 $\lambda=1/2$，但没有排除该原值点。

同一次新输入还对保存的完整首一 $R_{543}$ 作准确 QQ 短除，得到
$$
R_{543}(v)=(v+1/4)R_{542}(v),
\qquad (v+1/4)\nmid R_{542}.
$$
由于整个 $v=-1/4$ 原纤维尚未排除，程序没有使用这个商作原必要覆盖，也没有执行随后预备的余覆盖模 Bézout。此前不同主权参数上界仍是八个。

剩余真实小输入是同一原点
$$
(u,Q,\ell,\lambda)=
\left(\frac34,\frac54,\frac12,\frac12\right)
$$
的完整原均值、N1、矩关系及物理 $D\ne0$；不能援用另一个特殊有序权图上的同名 $\lambda=1/2$ 结论。

## 原源、完整参数与执行

原源：[2026-11-27-unit211-Phi-zero-main-rho-head-minus-quarter-original-fiber-and-remaining-Gauss-input-8542.py](2026-11-27-unit211-Phi-zero-main-rho-head-minus-quarter-original-fiber-and-remaining-Gauss-input-8542.py)

Git blob：26513973caef07f02ca38f7ca30c6af274884953。  
SHA256：d7514bd9d050465db0b26bf3ce2f12d044686df1261c0fc3fd60e4fd8f48e4db。

- run/job：46055411350 / 140696587869。
- source commit：83b53b2001cb696c05c4b67525a770431f6045fa。
- 内层退出码 0；0.095425016 秒；37584 KiB。
- stdout：6287 字节；SHA256 964105ab394fc4f9ca43a6108599c1300c3fc0eee627fb8c23974d4a089b3566。
- 2026-11-27 19:15:50 UTC 实际规则读取的两份 README blob 均未变。

完整三多项式、Bézout 系数和 gcd 保存为 [原 lambda 纤维精确参数](2026-11-27-unit211-Phi-zero-main-minus-quarter-lambda-half-exact-input-8542.json)，解压原文 7134 字节，SHA256 3a7a082fdb8e569dfc4c1e5501c54f7ffd3558ef4b85746f1a4e90714fad0f2f。

[小执行回执](2026-11-27-unit211-Phi-zero-main-minus-quarter-lambda-half-execution-8542.json) 明确区分已完成的 QQ 约束、仅检测而未获准使用的线性除法，以及没有执行的后续模返回。本次没有重算任何原结果式，也没有关闭整主图或普通不变子空间问题。
