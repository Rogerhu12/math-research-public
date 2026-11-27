# Phi=0 判别式零图：两因子精确 QQ 重数与严格 146 个不同基点覆盖

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 新结论

在有序图
$$
b=1,\quad c=\frac12,\quad \ell=\frac32,\quad
u=\frac{3+\rho}{2},\quad Q=1-\rho^2
$$
中，完整原解可能对应的不同 $(\rho,\lambda)$ 基点数至多 **146**。

这是对旧 168 点界的严格改进。它只计此有序图的基点，不把另一 B/C 交换图并入同一数字，也不声称这些候选都是原解或整个 $\Phi=0$ 面已经排空。

使用的三条同点原必要曲线仍为
$$
F=F_{26,26},\qquad G=C_{31,50},\qquad H=C_{34,48}.
$$
本次没有重算原 cofactor 或整结式。新输入是原 $57$ 阶 Sylvester 矩阵在两个已识别 QQ 因子处的局部赋值，以及实际新模余式的完整 Bézout。

## 2. 已付的首一投影与完整纤维排除

记
$$
R=\operatorname{Res}_{\rho}^{(26,31)}(F,G),\qquad
S=\operatorname{Res}_{\rho}^{(26,34)}(F,H).
$$
这里的上标表示固定原次数，矩阵分别为 $57,60$ 阶；参数特化导致的首项下降不会更换矩阵。

已有
[R150-appendix-unit211-Phi-zero-exceptional-PB-exact-infinity-2033-monic-cover.md](R150-appendix-unit211-Phi-zero-exceptional-PB-exact-infinity-2033-monic-cover.md)
支付：完整 R 的 QQ 次数恰为 2033，首项在 $1009$ 处为单位。按该首项规范后，
$$
R\in\mathbb Z_{(1009)}[\lambda]
$$
首一。实际储存的模 R 与这一规范至多差一个非零模常数。

令
$$
\phi_1=\lambda-\frac12,\qquad
\phi_6=\lambda^6+\frac35\lambda^5-\frac94\lambda^4
-\frac7{10}\lambda^3+\frac{63}{80}\lambda^2
+\frac{39}{80}\lambda+\frac5{64}.
$$
两者都是已付真 QQ 不可约因子。结果
[R150-appendix-unit211-Phi-zero-exceptional-two-genuine-boundary-image-complete-QQ-fiber-exclusions.md](R150-appendix-unit211-Phi-zero-exceptional-two-genuine-boundary-image-complete-QQ-fiber-exclusions.md)
已排除 $\phi_1\phi_6=0$ 的两个整个 QQ 原纤维，包括六次域的全部复嵌入。

本次证明精确 QQ 重数：
$$
v_{\phi_1}(R)=10,\qquad v_{\phi_6}(R)=2.
$$

## 3. 原固定矩阵的赋值证书

先分别在原多项式中作
$$
\rho=s-1,\qquad \rho=s+3.
$$
源逐个 QQ 系数构造平移，并用反平移完整乘回 F、G。固定 Sylvester 结式在这种变量平移下不变；这也是多项式系数的两个三角、对角为一的基变换。

对每个平移后的 $57$ 阶原矩阵 $A$，求每个非零条目的真实 $\phi$ 次赋值。每次除以 $\phi$ 都验证完整乘回。最小权完美匹配实际给出整数行列对偶 $(a_i,b_j)$，满足
$$
a_i+b_j\le v_\phi(A_{ij}),\qquad
\sum_i a_i+\sum_jb_j=\sum_i v_\phi(A_{i,\pi(i)}).
$$
全部不等式及匹配上的总和等式都已实际核对，完整对偶和匹配保存在回执中。

定义
$$
B_{ij}=\phi^{-a_i-b_j}A_{ij}.
$$
由于上述对偶不等式，每个 $B_{ij}$ 都是 QQ 多项式；负指数方向只是乘以 $\phi$ 的正幂。逐项整除或乘法均核对。于是
$$
\det A=\phi^E\det B,\qquad E=\sum_i a_i+\sum_jb_j.
$$

实际得到：

| 因子 | 原 $\rho$ 平移 | 真实 QQ 匹配赋值 $E$ |
|---|---|---:|
| $\phi_1$ | $s-1$ | 9 |
| $\phi_6$ | $s+3$ | 1 |

这已经支付 $R$ 的相应 QQ 整除下界，尚不借用任何模高重数。

## 4. 完整 QQ 核再支付各一次

将 B 的每项对 $\phi$ 取余，并对每项验证商、余式的完整乘回。因为 $\phi$ 是真不可约 QQ 因子，$K=\mathbb Q[\lambda]/(\phi)$ 为域。

把 $K^{57}$ 按 $1,\lambda,\ldots,\lambda^{\deg\phi-1}$ 的 QQ 基写成正则表示。源得到：

| 因子 | QQ 矩阵阶 | 实际 QQ 秩 |
|---|---:|---:|
| $\phi_1$ | 57 | 56 |
| $\phi_6$ | 342 | 336 |

对每个矩阵，源实际取出非零 QQ 右核列并完整乘回；再把同一列组回 $K^{57}$，对原 B 的全部 57 条 K 行再次完整乘回为零。因此 $\det B=0$ 于 K，故
$$
\phi_1^{10}\mid R,\qquad \phi_6^2\mid R
$$
在 QQ 中成立。

已保存的完整模 R 在 $\bar\phi_1,\bar\phi_6$ 处的整多项式重数分别恰为 $10,2$。R 首一且在 $1009$ 处整，两个 $\phi$ 也首一且在 $1009$ 处整；更高 QQ 整除必然约化为更高模整除。因此这些模重数是合法上界，本次 QQ 下界达到它们，精确重数即为 $10,2$。

## 5. 真 QQ 余投影与新的完整模 Bézout

由此定义真正的首一 QQ 多项式
$$
R_*=\frac{R}{\phi_1^{10}\phi_6^2}.
$$
它的次数恰为
$$
2033-10-2\cdot6=2011.
$$
首一多项式除法还保证 $R_*\in\mathbb Z_{(1009)}[\lambda]$。两个整参数纤维已经排除，所以每个实际原基点仍满足
$$
R_*(\lambda)=S(\lambda)=0.
$$

源实际从完整已存的模 R 中整除 $\bar\phi_1^{10}\bar\phi_6^2$，对商乘回；随后对这个新的完整 2011 次模余式和完整 2050 次模 S 作新的 xgcd。实际返回
$$
\deg\gcd(\bar R_*,\bar S)=146,
$$
两个 Bézout 标签次数分别为 $1903,1864$，完整组合乘回了所报 gcd。没有把旧 $\gcd(\bar R,\bar S)$ 直接相除并冒充新 gcd。

令 $C=\gcd(R_*,S)$ 在 QQ 中首一。由于 C 是首一 $R_*$ 的首一因子，它的系数在 $\mathbb Z_{(1009)}$ 中：可用 Gauss 引理，或用 $\mathbb Z_{(1009)}$ 的整闭性与根的整性证明。于是 $\bar C$ 保持次数并整除两条实际模多项式，故
$$
\deg C\le146.
$$
不需要宣称 S 的模次数等于其 QQ 次数；只需它是完整固定原行列式的真实约化，这点已由原输入支付。

## 6. 为什么计数覆盖不同 $(\rho,\lambda)$ 点

固定一个允许的 $\lambda_0$，设有 r 个不同原基点
$$
(\rho_1,\lambda_0),\ldots,(\rho_r,\lambda_0).
$$
这些 $\rho_i$ 同时为三条原曲线的根，因此对每个固定 Sylvester 矩阵都有相应 Vandermonde 核列
$$
(1,\rho_i,\rho_i^2,\ldots)^{\mathsf T}.
$$
它们线性独立。原 QQ 曲线对 gcd 为一，因而不存在共同垂直线；每个这样的纤维有限，且不同根数不超过所用固定矩阵容许的次数。即使某些原首项在 $\lambda_0$ 退化，固定矩阵仍保留这些独立核列。

一个多项式方阵在 $\lambda_0$ 的秩缺陷至少 r，意味着其行列式的消失阶至少 r：用常数可逆行列变换把该点矩阵化为标准秩形后，至少 r 行全部被 $\lambda-\lambda_0$ 整除即可。

所以 $v_{\lambda_0}(R),v_{\lambda_0}(S)\ge r$。已排除的 $\phi_1\phi_6$ 在允许的 $\lambda_0$ 上非零，故除去这些因子不会改变此处 R 的消失阶；于是
$$
v_{\lambda_0}(C)\ge r.
$$
对所有 $\lambda_0$ 求和即得不同有序基点总数不超过 $\deg C\le146$，不是仅仅“至多 146 个不同 $\lambda$”。

## 7. 实际执行身份

源：
[2026-11-27-unit211-Phi-zero-exceptional-original-R-two-QQ-local-multiplicities-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-exceptional-original-R-two-QQ-local-multiplicities-input-8542.py)。

- blob：5ec233e8b95e6f0aac44a68ce0013efae5072188。
- SHA256：68dbc91f83a7a0b85f8686c35798c9df0b8f86502f7b10d573fca01ee8281b0c。
- run/job：46031522866 / 140616280825。
- source commit：4bcf0ccd2d663f0b1aec4f264efd48959106e875。
- 内层：0.749304956 秒 / 78760 KiB / exit 0。
- stdout：5445 字节，SHA256 3e38fd1f6c13ab46735f4a7949cf83cf8ec56debfd56d49d75be8a4da1c29160。

实际检查包括 118 个平移系数、132 次赋值除法、6498 次对偶缩放乘回、6498 次模 $\phi$ 余式乘回、两个完整 QQ 核乘积和 114 个原 K 行乘积。全部新数学返回在 0.678 秒前完成。普通 ISP 未因此完成。
