# R542 — 原第三 sigma 支的完整算术投影与非齐次普通核心

日期：2026-11-14。**状态：已证明。**

R541 三支身份中的真实第三支，在 $[2]$ 覆盖上的整个 degree136
来源同时含有原 $S$ 和固定曲线 $E_{2312}$ 的非零分量。
本文给它的全部共同 CM 块、四条已识别秩零参考、十二个外谱，
以及无需另加射线的完整普通核心
$$
K_{136}F_\eta=-F_\eta-S(2z).
$$
所有计算在同一个完整二十三维来源空间中进行。没有从有限素数样本
判断来源身份，也不将第一边际的核心升成原六输入的联合核心。

## 1. 同一原第三支与完整多项式

保持 R541 的原六 sigma 来源 $\rho_0$、原观察 $Y$、实际矩阵
$\mathcal H$ 及同一 $b=17$、周期 $\Omega_p$：
$$
\rho_\eta=\omega^2\mathcal H_*\rho_0,\qquad
S_\eta=Y_*\rho_\eta,\qquad F_\eta(z)=S_\eta(2z).
$$
这里函数和其实际测度继续用同一来源记号。R541 §8 已证明
$$
F_\eta=-\frac{\omega}{84}
\sigma(2\delta z)\sigma(4\delta z)
\sigma(2\gamma z)\sigma(2\bar\gamma z)
\sigma(\gamma z)\sigma(\gamma_{13}z),
\tag{1}
$$
$$
\gamma=(5+\delta)/2,\quad\gamma_{13}=(7+\delta)/2,\quad
\omega=(-1+\delta)/2,\quad\delta^2=-3.
$$
它是整个 $\mathcal S_{136}$ 的型零截面。置
$$
X=x_\wp^3,\quad
r_\gamma=(2-6\delta)b/7,\quad
R_2=X^2+20bX-8b^2,
$$
$$
Q_{13}=X^2+(2+6\delta)bX+(40+24\delta)b^2/13.
$$
则原完整比值为
$$
F_\eta=\frac{\omega\gamma\gamma_{13}}8
\frac{(X-r_\gamma)Q_{13}}{(X+b)R_2}\,S(2z).
\tag{2}
$$
(2) 在整个 $S(2z)$ 中整除，不能只取带极的有理因子。

为给出可直接重建的全多项式，令
$$
A=X(X-8b)^3,\qquad B=64(X+b)^3.
$$
原
$$
S(z)=\sigma^{34}x_\wp^2
(X+b)(X-8b)(X^2-4bX/7+16b^2/7)
$$
及完整二倍公式给
$$
S(2z)=\sigma^{136}x_\wp^2 P_{S,2}(X,b),
$$
$$
\boxed{
P_{S,2}=64(X+b)^3(X-8b)^2
(A+bB)(A-8bB)
(A^2-4bAB/7+16b^2B^2/7).
}
\tag{3}
$$
将 (3) 代入 (2) 即得到 $F_\eta$ 的完整多项式 $P_\eta$。
因为 $A+bB=(X^2+20bX-8b^2)^2=R_2^2$，
分母 $(X+b)R_2$ 在 (3) 中确实整除。
$P_{S,2},P_\eta$ 的 $X$ 次数均为 $21$，总齐次权均为 $21$。
准确有
$$
F_\eta(0)=0,\qquad [z^6]F_\eta=-68+20\delta.
\tag{4}
$$
一般 $b$ 的缩放为
$$F_{\eta,b}(z)=b^{-1}F_{\eta,1}(b^{1/6}z).$$
这是同一有理来源的齐次恢复，不更换原实际普通周期。

## 2. 全部二十三维 CM 运算及循环维数

使用 R466/R476 已经证明的原算子
$$
M=N_7=\mathscr M_{\gamma}/\gamma,\qquad
N=N_{19}=\mathscr M_{\gamma_{19}}/\gamma_{19},\qquad
D=\omega^2NM^{16}.
$$
其完整定义是原无除范数 theta 迹，原纤维常数与半特征不变。
在整个型零空间
$$
\mathcal V_{136}=\sigma^{136}x_\wp^2K[X]_{\le22}
\tag{5}
$$
有
$$
M^{18}=I,\qquad D^2=I,\qquad DM=MD,\qquad N=\omega DM^2.
\tag{6}
$$
两个旧数据文件保存 (5) 上完整的 $23\times23$ 矩阵；
本篇没有重新生成 CM 纤维或只取环境中的部分谱。

将 (2)–(3) 的二十三个准确坐标代入 (6)，得到
$$
\boxed{M^9F_\eta=F_\eta+S(2z),}
\tag{7}
$$
且 $F_\eta$ 的 $M$ 最小多项式准确是
$$
\boxed{(t+1)(t^9-1).}
\tag{8}
$$
令 $F_\eta^\pm=(I\pm D)F_\eta/2$。其各自最小多项式为
$$
\boxed{\begin{aligned}
m_+(t)&=(t+1)(t^9-1),\\
m_-(t)&=(t-1)(t-\omega^2)(t^6+t^3+1).
\end{aligned}}
\tag{9}
$$
因此单个 $M$ 循环维数为 $10$，完整 $M,D$ 共同循环空间维数为
$10+8=18$。

**完整有限证明的内容。** 附脚本先用 (3) 的多项式乘法和准确整除
构造全部二十三个坐标，再对旧完整矩阵作有理数/二次域乘法。
(7) 是二十三行全部相等，不是质量或首项相等。
对 (8)、(9)，逐次列出 $v,Mv,\ldots$，前 $10$ 或 $8$ 列
作精确高斯消元皆独立，下一列的唯一关系恰为所写多项式。
这在有限维空间中完整证明最小性。所有非零投影坐标和关系均保存；
没有用目标普通素数的取样或浮点误差判断零。

## 3. 六条已识别算术线与十二个外谱

R466/R476 已支付的共同特征线使用以下规范：
$H_k$ 是其 $k=1,3,4,5$ 的实际秩零来源，归一 $H_k(0)=1$；
$S_{\rm new}$ 是 R466/R469 的实际 $E_{2312}$ 来源，首 $z^6$ 系数为一。
它们的周期、完整有限 Schwartz 数据及通常 Selmer 桥仍按原文，
不由本篇矩阵的特征值重新猜测曲线。

对整个 $F_\eta$ 的实际共同投影准确如下：

| 分量 | $M$ | $D$ | 对应来源 | 投影系数 |
|---|---|---|---|---|
| 原曲线 | $-1$ | $+1$ | $S(2z)$ | $-1/2$ |
| $k=1$ | $1$ | $+1$ | $H_1$, $D_1=-136$ | $-\delta/(9072b)$ |
| $k=3$ | $\omega$ | $+1$ | $H_3$, $D_3=-39304$ | $(3-\delta)/(9072b)$ |
| $k=5$ | $\omega^2$ | $+1$ | $H_5$, $D_5=-11358856$ | $(-3-\delta)/(9072b)$ |
| $k=4$ | $1$ | $-1$ | $H_4$, $D_4=668168$ | $-1/(1008b)$ |
| 新秩二曲线 | $\omega^2$ | $-1$ | $S_{\rm new}$, $D_2=2312$ | $\frac{26}{3}(1-\delta)$ |

这里 $D_k$ 是曲线 $y^2=x^3+D_k$ 的常数，与算子 $D$ 不同。
特别
$$
\boxed{\frac{I-M^9}{2}F_\eta=-\frac12S(2z),}
\tag{10}
$$
$$
\boxed{\Pi_{D=-1,M=\omega^2}F_\eta
=\frac{26}{3}(1-\delta)S_{\rm new}.}
\tag{11}
$$
(10) 也由 (7) 直接得到。其余每条投影先由 (6) 的有限群平均
得到全向量，再在 R466/R476 的已识别一维线中比较；
(11) 逐个比较已有 $S_{\rm new}$ 的全部二十三个系数。
四条参考系数的 $1/b$ 来自 (4) 的齐次权，不能删除。

除了表中六条线，还有四个不可约三维共同块。以 $b$ 乘其原点质量，
准确为
$$
\begin{array}{c|c|c|c}
D&M^3&\dim&b\,\mathrm{mass}\\ \hline
+1&\omega&3&(-3+\delta)/6048\\
+1&\omega^2&3&(3+\delta)/6048\\
-1&\omega&3&(1+\delta)/2016\\
-1&\omega^2&3&(1-\delta)/2016.
\end{array}
\tag{12}
$$
它们的完整投影为在 $M^9=1$ 部分施加
$$
\frac{I\pm D}{2}\,
\frac{I+\tau^{-1}M^3+\tau^{-2}M^6}{3},\qquad\tau=\omega,\omega^2.
\tag{13}
$$
每块非零且循环多项式是 $t^3-\tau$；它在 $K=\mathbb Q(\delta)$
上不可约，因为 $K$ 的整单位只有 $\mu_6$，其立方只有 $\{\pm1\}$。
故在分裂域中确有十二条非零共同外谱，不能只因原总质量零将它们删除。

四条参考总质量为
$$-\frac{3+\delta}{3024b},$$
四个外块总质量则为相反数；两条秩二来源质量都为零。
这准确解释 (4) 的质量零，并不使各块质量分别为零。

附数据中所有新坐标的分母最小公倍数为
$$
\boxed{\Delta_{\eta}=18144=2^5\,3^4\,7.}
\tag{14}
$$
使用整投影时保留 R466/R476 的原固定坏集及 $p>19$。
(11) 的系数范数是 $2704/9$，当前处也为单位。
没有增加新的同余射线或用随着 $p$ 变化的来源代替固定 $F_\eta$。

## 4. 同一个普通核心、全部深度和质量

R466 §10 已在整个 degree136 空间证明当前原射线上的绝对式
$$K_{136}=-M^9.$$
代入 (7) 得
$$
\boxed{K_{136}F_\eta=-F_\eta-S(2z).}
\tag{15}
$$
与此同时 $K_{136}S(2z)=S(2z)$。所以这两条真实来源闭成一个
显示的非齐次两态，且
$$
K_{136}^nF_\eta
=(-1)^nF_\eta+\frac{(-1)^n-1}{2}S(2z).
\tag{16}
$$
归一全空间 ordinary restriction 的外部因子仍是 $\lambda$，
空间内的 $K_{136}$ 不再重复乘这个因子。

固定 $2$ 是普通单位，乘二与深限制、$\kappa$ 缩放严格交换。
因此还原原物理 $Y$ 边际，得到对全部 $n\ge0$ 的**整条测度**等式
$$
\boxed{
\nu_{S_\eta}|_{p^n\mathbb Z_p}
=\lambda^n[\kappa^n]_*
\left((-1)^n\nu_{S_\eta}
+\frac{(-1)^n-1}{2}\nu_S\right).
}
\tag{17}
$$
特别
$$
\nu_{S_\eta}|_{p\mathbb Z_p}
=-\lambda[\kappa]_*(\nu_{S_\eta}+\nu_S).
$$
这保全部 tame、单位环带和紧开测试，不仅是 principal 一项。
由两条总质量均为零，其整个单位质量也严格为零：
$$J_{S_\eta}(0)=J_S(0)=0.$$

对单位 Mellin 函数，(17) 给准确归一的深环带行
$$
\int_{p^n\mathbb Z_p^\times}
\left\langle\frac{x}{\kappa^n}\right\rangle^{du}
d\nu_{S_\eta}(x)
=\lambda^n\left((-1)^nJ_{S_\eta}(u)
+\frac{(-1)^n-1}{2}J_S(u)\right).
\tag{18}
$$
若改用 $p^n$ 归一，必须另保 $\lambda^{2n}$ 的尺度及对数。
在原 $J'_S=0$ 的假设下，(18) 的中央只是
$(-\lambda)^nJ'_{S_\eta}$，未因此变成零。

(12) 的四块都在 $M^9=1$，所以各自核心为 $-\lambda$。
其单位质量是 $(1+\lambda)$ 乘表中原点质量；
R533 §3 的实际偶迹论证给 $1+\lambda$ 为单位。
故这些显示外块在当前处有非零单位质量。
它们的中央导数与四条参考中央仍不能被忽略。

## 5. 与原三支域和算术中央的准确连接

(10)–(11) 是 $[2]$ 覆盖上的真实算术投影。
将每个投影函数 $F(z)$ 变回 $F(z/2)$ 时，
$$
J_{F(z/2)}(u)=\langle2\rangle^{-du}J_F(u),
$$
$$
J'_{F(z/2)}(0)=J'_F(0)-d\log_p\langle2\rangle J_F(0).
\tag{19}
$$
两条秩二投影的质量为零，所以其中央返回没有漏掉尺度项；
参考和外块须逐项保 (19)，只有全和才因质量相消而消去共同尺度项。

R541 的整六输入身份仍是
$$
\rho_1=-\mathcal G_*\rho_0
=\mathcal R_*\rho_0+\rho_\eta.
$$
本文只对 $Y_*\rho_\eta$ 完成 (7)–(19)。
原 $\mathcal R/\mathcal G$ 支仍在 $[4]$ 的 degree544 覆盖，
全部 $C,F,G_{\rm hid}$ 测试及每支实际 cut 仍按 R541 转置。
不能用 (15) 宣称原六输入的 $Y$ 核等于某个只作用于 $(c,d_0)$ 的几何操作。

接续须付的是 (10)、(11) 的完整 CM 投影如何作用于同一个实际
受限积分域，及原两支补域、四参考、十二外谱的合法比较。
已识别 $S/E_{2312}$ 分量或显示非零质量本身不证明原中央
在无穷多个 $p$ 非零。主目标仍未完成。

## 精确来源和可再生证书

- [R541：原三支完整 sigma 身份及真实 cut](R541-original-degree8-second-state-and-exact-sigma-transport.md)。
- [R466：完整 CM 算子、五条有限角色与绝对普通核心](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)。
- [R476：整个二十三维块和实际参考的规范](R476-original-complete-xi-normtwo-bridge-and-integral-eight-source-basis.md)。
- [本篇精确脚本](../scripts/check-r542-original-eta-arithmetic-projections.mjs)。
- [全部源向量、共同投影、外块与最小多项式](../scripts/check-r542-original-eta-arithmetic-projections.json)。
- 原矩阵：[CM7](../notes/2026-11-14-theta-degree136-cm7-exact.json)、
  [CM19](../notes/2026-11-14-theta-degree136-cm19-exact.json)。

脚本的全部证明计算已在当前 JavaScript 环境以 BigInt 有理数执行。
新的有限运算只作用于既有完整矩阵；没有新加独立复跑或冻结流程。
