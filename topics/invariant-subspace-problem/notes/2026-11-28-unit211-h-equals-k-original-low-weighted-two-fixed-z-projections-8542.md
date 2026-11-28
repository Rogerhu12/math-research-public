# 新输入：h=k 的完整原低加权差与两个固定 z 投影

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted GPT-6 Astra Pro。尚未执行，不预记任何原标量或排空。

## 原范围与必要定义

保持已刊正确碰撞图 $ABQ(1-Q)P_f\ne0$、$bcP_{02}\ne0$，$\lambda$ 为非零原孤立均值；原 $\lambda=1/2$ 已用第五列秩排除。记
$$
A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1,
$$
$$
\xi=B/A,\quad \ell=A^3/B^2,\quad T=A^2/B,\quad h=k=1+\xi,\quad
w=\lambda-1-T,\quad z=Qt .
$$
真实 $f,V,X,Y$ 与四行 Gram 只从正确 f33/bb534 定义前缀恢复，不读旧错 R，也不执行旧五行 cofactor、四 individual N/P 的 NV 标量或其因式分解。新源实际逐项确认同点原 $Low_w=NS-PS+E_{W2}$。

记 $\delta=1-Q$，$X=x+\rho y,Y=x-\rho y,\rho^2=\delta$。由于 $p+q=2$，
$$
K_w=2[t^2+(5u-4x-2)t+2(x^2-\delta y^2)
+4x+4\delta y-4ux+2u^2-6u+Q].
$$
完整自由 $f$ 的修正必须保留：
$$
Low_w=2P_{02}(2\lambda-1)w
-bct[K_w+4(f-u)(t-2)].
$$
$NS=bN_4(g_B)+cN_4(g_C)-2\lambda P_{02}\ell h^2$，
$PS=bP_2(g_B)+cP_2(g_C)-P_{02}\ell h^3$，以及
$$
E_{W2}=b(2p-u-X)E_B+c(2q-u-Y)E_C
$$
全部从同一个完整 Gram 计算。低式与其右端完整相等，不把只在 f=u 成立的旧低式套到自由 f。

## 真正新目标

将 $E_1,E_B^{odd},Low_w$ 各作为同一 z 的原多项式。只清已付参数分母、只剥各行系数的已付共同内容，逐行乘回完整原式。不得假设 Loww 为二次；按实际整个系数环的次数形成固定 Sylvester：
$$
\operatorname{Res}_z(E_1,Low_w),\qquad
\operatorname{Res}_z(E_B^{odd},Low_w).
$$
每次 Bareiss 精除都以乘回返回；矩阵采用原全局次数，任意专门化后的首项下降仍在该矩阵内。两投影是同一有限 z 根的必要条件，不据多变量 gcd 宣称空集，也不假结果首项非零。

本次不以 NV 或其斜率消去 z，因而整个 $\Delta=0$、$T_{\rm num}=0$ 原纤维仍在。不会再次生成先前已完成的 NV 四标量。原 D 不作为逆或模幂目标。

## 已付支持与旧 S0 来源

唯一允许的多项式支持为 $A,B,Q,1-Q,P_f,M=4bc(1-Q),P_{02},\lambda,2\lambda-1,S$，其中
$$
S=2\xi+3-2\lambda=(2\lambda-1)(2\lambda^2-1)/A.
$$
S=0 用[既有完整原碰撞排除](../results/R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-equal-values-complete-exclusion.md)，并已静态复读其自含真实 Gram、Af=0 碰撞支及原第五列 lambda-half 三来源。当前 p+q=2 图以 $q_{\rm old}=(1-\rho)/(1+\rho)$ 转旧 p=1；$Q(1-Q)\ne0$ 保证所有必要值非零且不相等相反。没有把旧错误 compact 链作为这个单位的理由，没有重跑旧成功计算。

未知 $u,u-1,\Phi,\Delta$ 或新投影内容全保留，不作为单位。当前已成 t=0 排除并不被用来偷除未返回的原式项。

## 冻结源与资源

新源 basename：2026-11-28-unit211-h-equals-k-original-low-weighted-two-fixed-z-projections-8542.py。

SHA256：cbc275f1f3e870611591d597e47f2e35bc4bf99af1b27b5b1aeeb609cdf9ecd9。7158 字节，180 秒/4 GiB，内外所有计时钳制到同一绝对截止。

必要直接依赖为已刊 bb534 源，完整 SHA256 00d513d603f862ef6b484176fe4d9da3b766e0047d46a87ec8f575622aa8ca14；仅执行 NerrB 定义前的 5116 字节，SHA256 eba270645031173eb0fd2c0908a4fb72cda25ce662a4140fb47289ad1b07e192。它又只执行 f33 的 4540 字节原坐标前缀，完整依赖 SHA256 2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2。两份依赖都只在 runner 临时目录取必要定义，不执行已成投影尾。

仅保存源码、参数定义、原输出次数/SHA与小回执；不保存大系数或矩阵缓存。资源触界时按实际最后完整 checkpoint 冻结，换新的原输入。
