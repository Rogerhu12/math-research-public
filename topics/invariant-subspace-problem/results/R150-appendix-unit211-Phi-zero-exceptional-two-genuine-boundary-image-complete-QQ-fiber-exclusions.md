# Phi=0 判别式零图：两个真边界像的整 QQ 参数纤维全部排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 完成的结论与限定范围

继续
[R150-appendix-unit211-Phi-zero-exceptional-exact-original-unit-boundary-images.md](R150-appendix-unit211-Phi-zero-exceptional-exact-original-unit-boundary-images.md)
中的有序权图
$$
b=1,\quad c=\frac12,\quad \ell=\frac32,\quad
u=\frac{3+\rho}{2},\quad Q=1-\rho^2.
$$
三条必要原曲线仍为同一 $(\rho,\lambda)$ 上的
$$
F=F_{26,26},\qquad G=C_{31,50},\qquad H=C_{34,48}.
$$
本次完成以下两个整个 QQ 参数纤维的原排除：
$$
\lambda-\frac12=0
\quad\text{或}\quad
H_6(\lambda)=0,
$$
其中
$$
H_6=\lambda^6+\frac35\lambda^5-\frac94\lambda^4
-\frac7{10}\lambda^3+\frac{63}{80}\lambda^2
+\frac{39}{80}\lambda+\frac5{64}.
$$

这次结论不再只是边界像：在每个所列参数根上，所有物理允许的 $\rho$ 都已排除。六次域的全部复嵌入一并覆盖。

范围仅为本有序判别式零图；不由此把 $2\lambda-1$ 或 $H_6$ 当成整个一般 $\Phi=0$ 图的单位。B/C 交换覆盖相应对称有序图，但不擅自把两个有序图的点数合并。

## 2. 对整个常数代数的原单位整除

分别令
$$
K_1=\mathbb Q[\lambda]/(\lambda-\tfrac12),\qquad
K_6=\mathbb Q[\lambda]/(H_6).
$$
这两个真 QQ 因子来自上一结果的完整原边界 gcd；没有使用模因式重建。

源把三条完整原曲线的每个系数归入对应 K，然后逐项尝试原权单位线性因子。实际完整返回为：

| 常数代数 | 三条原式剥除的真单位因子 | 剩余 $\rho$ 次数 |
|---|---|---:|
| $K_1$ | 每条各 $(\rho+1)^3$ | $23,28,31$ |
| $K_6$ | 每条各 $\rho-3$ | $25,30,33$ |

每次整除在 QQ 商代数中精确进行，并完整乘回三条原式。$\rho+1=0$ 属于原 $Q=0$ 边界，$\rho-3=0$ 属于原 $T_0=0$ 边界；在实际物理图上它们均非零。因此这些除法保留每个原解。

分别记剥除后的三条多项式为 $F_i,G_i,H_i$。源对 $F_i$ 的 $\rho$ 首项在 QQ 中求出模对应 $\phi_i$ 的 xgcd 逆，并逐项验证
$$
a_i\,\operatorname{lc}_{\rho}(F_i)+b_i\phi_i=1.
$$
据此将 $F_i$ 规范成真正的首一多项式 $\widehat F_i$，次数分别为 $23,25$。这不是未检查的范数逆；逆的完整 QQ 乘积已经核对，所得系数在实际素数 $1009$ 处均整。

## 3. 固定原理想矩阵与严格特征零提升

在有限 QQ 代数
$$
A_i=K_i[\rho]/(\widehat F_i)
$$
中，按
$$
\lambda^a\rho^b,\quad
0\le a<\deg\phi_i,\quad0\le b<\deg_\rho\widehat F_i
$$
取真实 QQ 基。维数分别为 $23$ 和 $150$。

构造所有真实原理想行
$$
\lambda^a\rho^bG_i,\qquad
\lambda^a\rho^bH_i
$$
在此基上的系数；行数分别为 $46,300$。每次 $\rho$ 约化只使用已首一的 $\widehat F_i$。这些是原理想中的实际倍数，不是仅有相同零点的替代行。

所有输入 QQ 系数及规范首项的 QQ 逆在 $1009$ 处整，因此上述固定 QQ 矩阵可逐项约化为对应的模矩阵。源中的模乘法与首一除法正是这些 QQ 操作的约化，每次模除法都完整乘回。

实际结果：

| 常数代数 | QQ 代数维数 | 原理想行数 | 模 $1009$ 实际秩 |
|---|---:|---:|---:|
| $K_1$ | 23 | 46 | 23 |
| $K_6$ | 150 | 300 | 150 |

程序分别选择 $23$ 阶与 $150$ 阶真实行子矩阵，求出其模逆，并对全部矩阵乘积检查等于单位阵。所选每行的原来源标签 $(G_i\text{ 或 }H_i,b,a)$ 保存在回执中。

由此，所选固定 QQ 子矩阵的行列式在 $1009$ 处是单位，特别在 QQ 中非零。它们的原理想行张成整个 $A_i$，故 $1$ 属于
$$
(\widehat F_i,G_i,H_i)\subset K_i[\rho].
$$
这排除了整个 QQ 纤维的共同复根。六次多项式在模 $1009$ 下即使可约，也不影响论证：所用矩阵是在全部六维常数代数上构造，并且整个 $150$ 维原理想矩阵满秩。

因此，在本原图中可以支付
$$
(2\lambda-1)H_6(\lambda)\ne0.
$$

## 4. 与有限点数界的关系

本次完成的是两个整 QQ 参数纤维的排除。它没有单独支付原固定结式中 $\phi_1^{10}$ 与 $\phi_6^2$ 的 QQ 高重数。

此前严格上界仍为 168 个不同有序 $(\rho,\lambda)$ 点。要用已见模支持进一步改进点数界，仍应先支付相应真实 QQ 结式整除，再对完整新模余式与另一原投影作实际 Bézout。本文不把旧模 gcd 直接除去某个支持就当作新的原点数结论。

## 5. 实际源与回执

执行源：
[2026-11-27-unit211-Phi-zero-exceptional-two-boundary-image-complete-QQ-fibers-input-snapshot-fix-8542.py](../notes/2026-11-27-unit211-Phi-zero-exceptional-two-boundary-image-complete-QQ-fibers-input-snapshot-fix-8542.py)。

- 源 blob：a70fc64b66910eaf8c59cb558e71ac3a872f267b。
- SHA256：69ab0c85b1712afd630cf41022dd4bf7b98afad7e109e11b6a93950568875b7e。
- run/job：46030816574 / 140613850092。
- source commit：78c4f3e168b06225abebfb0be29464db50413a69。
- 内层：1.195795333 秒 / 41896 KiB / exit 0。
- stdout：8432 字节，SHA256 3b95722b6f320142a125bf9077963dc058ce107320bf4fbb0550c85534aa9637。

检查计数：12 次 QQ 原线性单位整除乘回，2 次 QQ 首项逆乘回，100 次模首一除法乘回，346 次模标量逆乘回，以及两个完整选定方阵逆乘积。

三个依赖均是此前已保存的精确原曲线 JSON，完整文件和多项式 SHA256 在源中固定；没有重算旧原六行 cofactor、原行列式或结式。旧列表快照错误及先前源路径错误保持真实记录。这里仅使用以上正常数学执行。普通 ISP 尚未因此完成。
