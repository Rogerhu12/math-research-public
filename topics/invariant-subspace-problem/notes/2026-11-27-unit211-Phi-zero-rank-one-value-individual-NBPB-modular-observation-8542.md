# Phi=0 rank-one 碰撞：个别 NB/PB 原投影与六项主覆盖重数的准确记录

日期：2026-11-27（Asia/Taipei）；会话：Astra-ISP-8542378f-20261127。

本次使用 [真实 1945 次原覆盖](../results/R150-appendix-unit211-Phi-zero-rank-one-value-exact-1945-degree-original-cover.md) 的同一 $F,G$，加入此前未用于投影的实际个别 $N_B,P_B$ 原条件。每条新 core 都由同一原 Gram 的 $(r,\ell r)$ 与真实目标 $H^3$ 给出完整清分母 Cramer 身份，没有范数单位或新临时参数逆。

两个新 core 分别具有 $(\lambda,\rho)$ 次数 $(113,22)$、$(127,24)$。与 $F$ 取固定原 $\rho$ Sylvester 后，完整模 1009 返回为：

| 新原个别值输入 | 固定阶 | QQ 次数上界 | 实际模次数 |
|---|---:|---:|---:|
| $F$ 与 $N_B$ core | 36 | 3276 | 3084 |
| $F$ 与 $P_B$ core | 38 | 3626 | 3414 |

所有原 $\rho$ 次数在模 1009 下保持，所以它们是固定原 QQ 行列式的真实约化，包含首项降阶纤维。它们与原 $R,R_S,R_V$ 的完整五项一元 Bézout 全部乘回。**模 gcd 仍为 908 次；新增两项没有缩小该数目。** 没有把这个成功执行记成分支排空。

本次另从主 $R$ 本身逐项除法并乘回，取得下列六个明确 QQ 首一因子在主 $\overline R$ 中的完整模重数。表中不是从公共 gcd 的次数猜测主覆盖重数。

| QQ 首一 $\phi$ | 主 $\overline R$ 的完整模重数 | 五项模 gcd 的重数 |
|---|---:|---:|
| $\lambda^2-\lambda+\tfrac12$ | 111 | 111 |
| $\lambda-1$ | 117 | 117 |
| $\lambda^2-\tfrac12\lambda+\tfrac14$ | 110 | 110 |
| $\lambda^2-\tfrac54\lambda+\tfrac12$ | 24 | 24 |
| $\lambda-\tfrac12$ | 145 | 145 |
| $\lambda^2-\tfrac23\lambda+\tfrac13$ | 44 | 44 |

六项总次数为 840。**仅在模运算中**剥除这个乘积后，主覆盖余式度数为 1105，五项 gcd 余式度数为 68。本次没有证明这 840 次乘积在 QQ 中整除 $R$，也没有据此给出 1105 或 68 的特征零结论。六因子的 QQ 局部核行提取是单独的新输入；最后两项的完整原零纤维另由整 $c=1/2$ 排除支付。

五项独立投影允许不同条件在同一 $\lambda$ 上取不同的 $\rho$ 根。因此后续使用 $G+S$ 等同一个 $\rho$ 的原必要曲线组合，是新的同点输入；不是把本次未改善的 gcd 误当闭合。

## 真实执行身份

源：
[个别 NB/PB 原模返回](2026-11-27-unit211-Phi-zero-rank-one-value-individual-NBPB-modular-return-8542.py)。

- 源 blob：$0e3ac1d9ebb923b83e7bef47491cfee6e7fb96ee$；
- 源 SHA256：$1e837721c676171f911e5e9b55fa6b634be49cd52d164a00dc753ad3e420e2f4$；
- Actions run/job：45996826906 / 140498207849；
- 实际内层 exit：0；5.506421563 秒；57548 KiB；
- stdout：25043 字节，SHA256 $753c23b83632211c475c45680e1df9e769d8969f97abd7f553074063e0ce38a2$；
- 实际源 main：$83c73ef8d2d8b080540547a613e3466469467fab$；
- 12:13:36.307800 UTC 的实际 pull 后两 README blob 均无变。

当前最强已付覆盖仍为 QQ 精确 1945 次。全部原复数零纤维、六项 QQ 重数和 68 次模支持各自按真实支付状态保留，未宣称整 Phi 面或 ordinary ISP 完成。
