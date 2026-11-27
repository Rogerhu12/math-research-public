# R150 工作记录：补齐 NC/PC 原值投影后剩余 32 未变

日期：2026-11-27（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 实际输入与返回

在有序 $h=1$ 的 $\Phi=0,z_n=0$ 原图中，此前原投影已用 $E_1,E_B,E_C,N_1,N_B,P_B$。本次真正新增另一 singleton 的 $N_C,P_C$，没有改用随机 cofactor 组。

对每个新原行 $r$，取同一个首一 $\ell$ 代数中的 $(r,\ell r)$，对实际单位目标 $H^3$ 作完整 Cramer 返回。最终分母和两系数原身份都已乘回。随后尝试只除已经支付的四个原范数因子；实际两项均无可消因子。

| 新原 core | 双次数 $(\lambda,\rho)$ | 总次数 | 项数 |
|---|---|---:|---:|
| $C_{NC}$ | $(122,21)$ | 143 | 2706 |
| $C_{PC}$ | $(128,21)$ | 149 | 2838 |

其 primitive integer SHA256 依次为

- $\texttt{afd038035acea37d36780ddd263906daf370c8f615ccf3cd613e8179f23cf5bd}$；
- $\texttt{a8d662d5b384b697f1e1f2925f40ccb031a78d32484eba60dfdf4dda2e3fd400}$。

与同一原 $F$ 作固定 $\rho$ 结式，两个矩阵均为 35 阶，两输入的 $\rho$ 次数在 1009 下保持。完整模投影次数分别为 3159、3243。再用同一 $\rho$ 的整数和 $C_{NC}+C_{PC}$，其固定 35 阶完整模投影也为 3243 次。

三次均对 [真 QQ 共同覆盖的 32 次模上界](../results/R150-appendix-unit211-Phi-zero-rank-one-value-32-point-cover-and-four-norm-units.md) 作完整 Bézout，所有乘积都返回原 32 次多项式。最终标签为 $1,0,0,0$；剩余 SHA256 始终是
$$
\texttt{a97d9ceb641c3c5162af051160864103b4dc8d6a0431a740e3c932378d4f9dec}.
$$

因此这三个新原输入没有进一步缩小严格 32 点界。特别不能从新增八式已全部出现就宣称它们没有共同原点，也没有把分开的投影根视作同一点解。

## 冻结身份

源：[缺少的 NC/PC 原值输入](2026-11-27-unit211-Phi-zero-rank-one-value-missing-NC-PC-original-Gauss-input-8542.py)。

- blob：$c92ba6fb5cec66fc2b0a680f4b4b58999e9e420e$；
- SHA256：$845c3ab2c24e0c2a982c453192467e2d37b2d0e2a569369d4cd40b7c92e37eb8$；
- Actions run/job：46006078572 / 140529465165；
- 内层实际 exit：0；3.158219039 秒；56972 KiB；
- stdout：14062 字节，SHA256 $8faa5654ca003c383de2122e843d605ace70c45dfa6f0824f163d47ad87455be$；
- pin source commit：$02f4d2adf4ed8d3337e5d4486a5d9812e6bbf4c7$；
- 实际 pull 到 $c1bd68ef5987d6c735b8b36e5a42711454773415$，13:19:30.415482 UTC 核两 README blob 均无变。

新的完整输入应进入已取得的精确 $H_8$ 常数商，保同一个 $\rho,\ell$ 与全部八行原来源，而非继续追加同类单投影或重跑旧 QQ 大结式。ordinary ISP 未宣称完成。
