# Phi=0 例外有序权图的完整原排除

数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 结论与原图范围

此前[整 S 四次域排除与严格 112 覆盖](R150-appendix-unit211-Phi-zero-exceptional-whole-S-moment-quartic-exclusion-and-112-cover.md)中的例外有序权图现已全部排除。

原坐标保持
$$
\ell=\frac32,\qquad
u=\frac{\rho+3}{2},\qquad
Q=1-\rho^2,
$$
以及同一原 $T,z=Qt,\lambda$ 和真实物理单位
$$
D=\ell(2\lambda^2-2\lambda+1)-T^2\ne0.
$$
这正是原 $\Phi=0$ 头退化分类中的例外权图；并非仅假设 $\ell=3/2$ 的整张一般权面。B/C 交换后的有序图由同样的交换对称覆盖。

本证明同时保留首个二次头 $H_{6,4}=0$ 的整个分支；没有把它当作单位。新的完整固定结式模 1009 为 553 次，和一个此前真实已付、在 $\mathbb Z_{(1009)}$ 上首一的 1977 次原余投影实际 Bézout 等于 1。因此全部复参数均排除。

整张 $\Phi=0$ 面尚未由本文排除：整首个二次头零曲线、旧主曲线及其他未付接口继续保留。普通 ISP 尚未完成。

## 2. 已付完整原来源

[首个原二次头图上的 D 必要方程](R150-appendix-unit211-Phi-zero-first-quadratic-head-actual-D-sixth-degree-necessary-equation.md)已构造完整原理想身份
$$
BD\in(R,W,O,N1)
$$
并仅剥已付权单位，得到精确保存的
$$
P_6(u,Q,\lambda)=0
\qquad(H_{6,4}\ne0).
$$
$P_6$ 的次数为 $(39,20,6)$，3101 项。它是同一点的真正原 D 必要条件，不是新的数值拟合或仅凭模运算重建的候选多项式。

本次直接读取该完整精确输入，再代入上述例外权坐标；没有重新计算原 cofactor、D 目标或失败的长行模块。精确得到
$$
P_6\!\left(\frac{\rho+3}{2},1-\rho^2,\lambda\right)
=\rho^{10}(\rho+1)^{13}(\rho-1)^5\,C(\rho,\lambda).
\tag{2.1}
$$
每次除法均逐系数乘回。实际次数及项数为
$$
(\deg_\rho,\deg_\lambda)P_6|_{\rm ex}=(41,6),\quad224\text{ 项},
$$
$$
(\deg_\rho,\deg_\lambda)C=(13,6),\quad98\text{ 项}.
$$
(2.1) 中被剥除的三个纯 $\rho$ 因子确实已付：$1-Q=\rho^2\ne0$ 及 $Q=(1-\rho)(1+\rho)\ne0$；$\rho+1$ 亦对应 $2(u-1)$。没有剥除任何未分类的原权因子。

## 3. 整个首项零分支由乘法保留

记原首个头的规范残因子为 $H_{6,4}$。完整代入恒等式是
$$
-12H_{6,4}\!\left(\frac{\rho+3}{2},1-\rho^2\right)
=\frac{\rho^2(\rho+1)^2}{4}\,h_4(\rho),
\tag{3.1}
$$
其中
$$
h_4(\rho)=11\rho^4-14\rho^3+44\rho^2-18\rho+9.
$$
源码从原头的准确多项式逐项核回 (3.1)。

因此每个原解都满足同一个必要方程
$$
\boxed{N(\rho,\lambda):=h_4(\rho)\,C(\rho,\lambda)=0.}
\tag{3.2}
$$
当 $H_{6,4}\ne0$，原 D 身份给 $C=0$；当 $H_{6,4}=0$，已付的 $\rho(\rho+1)$ 单位和 (3.1) 给 $h_4=0$。两种情况合为 (3.2)，而不需要倒置 $h_4$，也不需要预先排除它的任何复根。

$N$ 的实际次数为 $(17,6)$，126 项，其规范 SHA256 为
$$
\texttt{7631fb4365eba83584ccc85e5f81c904d6c45d49a0fb7b7a93e60b6981bc317e}.
$$
清分母后 $2^{29}N$ 是本次固定输入的本原整数多项式，完整乘回已执行。完整 126 项和其 3343 字节原系数载荷见[精确输入](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-exceptional-complete-P6-original-Gauss-exact-input-8542.json)。

## 4. 新固定原 Sylvester 结果式

沿用此前完整原必要多项式 $F(\rho,\lambda)$，其 $\rho$ 次数为 26；保存的原 $F$ 是本原整数多项式。定义
$$
S_{\rm new}(\lambda)
=\operatorname{Res}_{\rho}\bigl(F(\rho,\lambda),\,2^{29}N(\rho,\lambda)\bigr),
\tag{4.1}
$$
使用固定次数 $(26,17)$ 的原 43 阶 Sylvester 矩阵。

每个原解都同时满足 $F=N=0$，故 $S_{\rm new}(\lambda)=0$。此推论在所有 $\lambda$ 处都成立，包括两个 $\rho$ 首项退化的纤维：共同有限根直接给固定 Sylvester 的评价核列，无须把任何 $\lambda$ 首项声明为单位。

源码实际核定模 1009 后两个完整输入仍保持 $\rho$ 次数 26、17，再计算这个固定原矩阵行列式的准确模约化。结果是非零的 553 次多项式
$$
\overline S_{\rm new}\in\mathbb F_{1009}[\lambda].
$$
其完整多项式 SHA256 为
$$
\texttt{6f9b055c35fd352551dc4a6201565dee4299c0114b124c6e8ba38ebcbdc3cc56}.
$$
全部 554 个系数已保存。这里不声称 $S_{\rm new}$ 在 $\mathbb Q$ 上的次数恰为 553；下节只需要它是固定整数矩阵行列式的准确约化。

## 5. 已付首一余投影与真正的 Gauss 返回

此前准确原投影
$$
R(\lambda)=\operatorname{Res}_{\rho}(F,G)
$$
使用固定次数 $(26,31)$ 的 57 阶 Sylvester 矩阵。它在 $\mathbb Q$ 上的完整次数 2033 及最高次系数在 $\mathbb Z_{(1009)}$ 中为单位，已经由原无穷远次数证书支付。

此前各整纤维排除及准确有理整除已支付
$$
Q_{\rm paid}=\phi_1^{10}\phi_6^2\phi_D^3\phi_J^4,
$$
其中
$$
\begin{aligned}
\phi_1&=\lambda-\tfrac12,\\
\phi_6&=\lambda^6+\tfrac35\lambda^5-\tfrac94\lambda^4
-\tfrac7{10}\lambda^3+\tfrac{63}{80}\lambda^2
+\tfrac{39}{80}\lambda+\tfrac5{64},\\
\phi_D&=\lambda^6-3\lambda^5+\tfrac{27}{8}\lambda^4
-\tfrac{17}{8}\lambda^3+\tfrac{27}{32}\lambda^2
-\tfrac3{16}\lambda+\tfrac1{32},\\
\phi_J&=\lambda^4-\tfrac{157}{35}\lambda^3
+\tfrac{1221}{140}\lambda^2-\tfrac{257}{35}\lambda+\tfrac{229}{105}.
\end{aligned}
$$
次数合计为 $10+12+18+16=56$。本次仅用 $\phi_J^4$，没有把模重数 8、整体提升失败或后续部分提升尝试当作 $\mathbb Q$ 整除。

于是
$$
R_*(\lambda)=R(\lambda)/Q_{\rm paid}(\lambda)
$$
是一个真实的 1977 次有理多项式；按已付的 1009 局部单位归一，它首一且系数属于 $\mathbb Z_{(1009)}$。所有 $Q_{\rm paid}=0$ 的原纤维此前已整体排除，所以尚可能存在的原点必须满足 $R_*=0$。

本次没有重放旧 $R_*/S$ 的 Bézout 作为审核门。直接对新条件实际得到
$$
\boxed{
A(\lambda)\,\overline R_*(\lambda)
+B(\lambda)\,\overline S_{\rm new}(\lambda)=1
\quad\text{于 }\mathbb F_{1009}[\lambda],
}
\tag{5.1}
$$
其中 $\deg A=552$、$\deg B=1976$，完整乘积已逐项核回。代码另保留旧 2050 次原投影组成三项完整恒等式，但其最终系数恰为零；本证明实际上不再需要该旧第三项。

为什么 (5.1) 排除所有复根：若 $R_*,S_{\rm new}$ 有共同复根，其首一有理公因子 $H$ 非常数。由于 $R_*$ 在局部整环 $\mathbb Z_{(1009)}$ 上首一，该整闭环中的首一因子 $H$ 也具有局部整系数。首一除法又使 $H$ 在同一环上整除 $S_{\rm new}$。所以 $\overline H$ 保持正次数，并同时整除 (5.1) 左侧的两个多项式，与右侧为 1 矛盾。

因此不存在尚余的复 $\lambda$，继而不存在任何原 $\rho,T,z$。合此前已闭的四类整纤维，整个原例外有序权图排空；B/C 交换后的图亦同。

## 6. 唯一实际执行与精确载荷

源码：
[2026-11-27-unit211-Phi-zero-exceptional-saved-P6-entire-first-head-original-Gauss-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-exceptional-saved-P6-entire-first-head-original-Gauss-input-8542.py)。

- source blob：2af0d184866b7850b7683e8c4d31e7ed426758ea。
- source SHA256：de686261b7ffb8c815e0cb21801e00e94f667e8a62aa3e3113025d2513a3a025。
- run/job：46051278305 / 140682930945。
- source commit：95797a950ab7b388947292e7eb2648382be1acf3。
- 内层耗时：0.143938009 秒；最大 RSS：41564 KiB；退出码：0。
- stdout：6788 字节，SHA256 bdf2f5eba48e87a25f475f7a7b173262f55150e9f4404ea5b332275bc3e913f6。

原代入在 0.031679226 秒完成，新完整固定结果式在 0.067629636 秒完成，完整 Bézout 1 在 0.074550190 秒返回。本次预算保持 120 秒/1 GiB，没有扩大任何已冻结计算。

[小回执](../notes/2026-11-27-unit211-Phi-zero-exceptional-complete-P6-original-Gauss-execution-8542.json)和[精确输入](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-exceptional-complete-P6-original-Gauss-exact-input-8542.json)保存全部阶段、原 126 项及完整新模结果式。2026-11-27 18:41:12 UTC 真 pull 后，两份 README 的 blob 均无变化。

本结论已经由上述完整原条件、真实有理整除及准确 Gauss 返回证明，不以任何旧程序重放或更高 $\phi_J$ 重数作为额外完成条件。整例外图已闭，继续课题其余开放输入。
