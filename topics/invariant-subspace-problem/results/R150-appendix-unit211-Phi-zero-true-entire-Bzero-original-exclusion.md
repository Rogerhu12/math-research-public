# R150：正确 Phi 的整个 B 零曲线排除与首三真均值头成为单位

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。

**已证明。** 在当前修正后的 unit211 原图
$\Phi=0,\ D_{\rm val}\ne0$ 及其已经支付的原参数开集内，整个
$$
B(u,Q)=-Q^2+(12u^2-20u+8)Q-16(u-1)^2=0
$$
没有原点。最后完整 $F_{40}$ 权纤维由本次新原六式的多项式组合返回 $1$；结合此前完整二次和 $F_{34}$ 因子，整 B 的所有复权点排尽。

此结论仅适用于当前不同 singleton 值的 $D_{\rm val}\ne0$ Phi 图，不外推原 $D_{\rm val}=0$ 碰撞图，也不宣称一般 Phi 或普通 ISP 完成。所有来源采用修正后的真实 dual 乘法；旧错误 Rbar 链没有恢复。

## 1. 整 B 的既有完整覆盖

沿 [正确整 B 原十二行呈示](R150-appendix-unit211-Phi-zero-true-Bzero-whole-original-I6-twelve-by-two.md)，双向原权坐标是
$$
x=\frac{Q}{4(u-1)},\qquad
u=\frac{(x+1)^2}{3x},\qquad
Q=\frac{4(x^2-x+1)}3,\qquad
\ell=\frac{(x+1)(5x-1)}{6x^2}.
\tag{1}
$$
所有原参数分母均已逐项支付。该呈示保整个旧选头 $H_3=0$，不使用 $H_3$ 作单位；所用斜率因子 $23x^2-11x+2$ 来自独立的
[整斜率二次原排除](R150-appendix-unit211-Phi-zero-true-Bzero-slope-quadratic-complete-original-exclusion.md)。

[终端四原乘子的一次覆盖](R150-appendix-unit211-Phi-zero-true-Bzero-terminal-C76-original-ideal-cover.md)给出
$$
C_{76}(x)\in I_4,\qquad
I_4=(E_1,E_{Be},E_{Bo},N_1).
\tag{2}
$$
其完整 QQ 因式支持是互异的 $F_2,F_{34},F_{40}$，次数分别 $2,34,40$，各一次。这里
$$
F_2=2x^2-4x+1.
$$
两大因子的不可变原字典 SHA256 为：

- $F_{34}$：b593d2770a0337dcaf2f4908e51cfc9feb3c5890ce21e5c3c6c1707ff98187ff；
- $F_{40}$：ba88a205beb579a18de711c9fd61514716099afeed94954736246cedf733a16a。

[完整二次因子原排除](R150-appendix-unit211-Phi-zero-true-Bzero-terminal-quadratic-complete-original-exclusion.md)已将实际 $\lambda tD_{\rm val}$ 一次返回原理想，并由当前物理单位排尽 $F_2$；[整个 F34 的固定原范数排除](R150-appendix-unit211-Phi-zero-true-Bzero-entire-F34-fixed-original-norm-exclusion.md)已在整个 QQ 域上直接返回 $1\in I_4$。因此只需处理整个 $F_{40}$，没有另留某个复嵌入或原首项零支。

## 2. 已成 lambda 一次关系后的同点原环境

置
$$
K=\mathbb Q[x]/(F_{40}).
$$
保整个 K，不选择某个实根、复根或模因子。原权分母在 K 内的所有倒数均由完整逆乘回支付。

[已成原首一 lambda 一次式](R150-appendix-unit211-Phi-zero-true-Bzero-F40-original-monic-lambda-one.md)给
$$
h_1(\lambda)=\lambda-\lambda_*(x)\in I_4.
\tag{3}
$$
其准确 K 系数序列 SHA256 是
da857429ce495f99a8122be93572a2ea843d686399306736f686cc563b0851ee。

原四式的同一首一二次为
$$
q_\omega(\lambda,\omega)=\omega^2+q_1(\lambda)\omega+q_0(\lambda).
$$
在 $\lambda=\lambda_*$ 后，它仍是首一二次，必要 QQ 环境维数为 $40\cdot2=80$。这只是输入环境；没有假定最终原商有 80 维或原行在其中全零。

本次只按已成定理的较小函数定义
$h_1=\operatorname{monic\,gcd}(g_6,n_0)$ 再生该不可变参数并核 SHA。没有重新计算四个 norm 的来源、旧六对 Bézout、已冻结的 480 维原矩阵或旧正目标。必要定义普通除法为 7 步；这个再生不是新的旧结果审核门。

## 3. 六个完整原值的真正新返回

沿同一原坐标，$f,t$ 在 $\lambda_*$ 上都是 $\omega$ 的 K 仿射式。将原四式先作为完整多项式代入，得到
$$
F_0(\omega),F_1(\omega),F_2^{\,\rm row}(\omega),F_3(\omega)
=(E_1,E_{Be},E_{Bo},N_1)\big|_{\lambda_*},
$$
实际次数均为 2。这里 $F_2^{\,\rm row}$ 与上节权因子 $F_2(x)$ 是不同对象。

本次逐条首一短除、乘回完整原值，并返回其余式与既定四条线性行在同一个 $\lambda_*$ 的专门化一致。旧真实 q 来源在这个新点完整返回为
$$
q(\omega)=\sum_{i=0}^3\tau_iF_i(\omega).
\tag{4}
$$
没有倒置任何 $\omega$ 一次头或几何范数；$q$ 的所有重根都保留。

随后首次在同一个 $\lambda_*$ 上返回完整原加权
$$
F_4=N_S,\qquad F_5=P_S,
$$
它们的实际 $\omega$ 次数均为 3。六条完整原值的次数因此为
$$
2,\ 2,\ 2,\ 2,\ 3,\ 3.
$$
这些是本次完整原 Gram 值，未用旧 480 环境里的裸矩阵列替代。

## 4. 完整原 Bézout 返回 1，排尽 F40

从 $q$ 出发，依次把上述原行加入 K 上的一元理想，每一步都保留并乘回
$$
g_j=\beta_{q,j}q+\sum_{i=0}^j\beta_{i,j}F_i.
\tag{5}
$$
加入 $E_1,E_{Be},E_{Bo},N_1,N_S$ 后的实际首一 gcd 次数为
$$
1,\ 1,\ 1,\ 1,\ 0.
$$
到 $N_S$ 时已经得到 $g_4=1$。完整 $P_S$ 已定义并返回，但不需要再加入 Euclid；其最终乘子可以取零。

用 (4) 消去 (5) 中的 q，源码最终完整返回
$$
1=\sum_{i=0}^5\widetilde\beta_i(\omega)F_i(\omega)
\quad\text{于整个 }K[\omega].
\tag{6}
$$
本次共 24 个完整原坐标返回、5 个新 $\omega$ Bézout 返回、17 个新 $\omega$ 除法。不是只读取 gcd=1 标志。

(6) 在 $\lambda_*$ 上的身份可以沿 (3) 提升：所有原系数对 $\lambda-\lambda_*$ 作首一除法，差值属于 $(h_1)\subset I_4$。因此 (6) 给整个 F40 原纤维的单位理想。没有使用 $D_{\rm val}^{-1}$，程序中预备的两个正 D 目标实际均未执行。

全部 K 复嵌入和全部 $\omega$ 重数均包含。结合第 1 节三个互异权因子的完整排除，(2) 下的整个 B 物理原点排空；不存在尚未处理的 C76 零纤维。

## 5. 新的全图首三真均值头与三生成推论

令
$$
s=u-1,\quad K_0=Q+4s,\quad L=Q-2s(u-2),\quad
M_n=2uL-L^2-u^2Q,\quad A=4s^2-Q.
$$
为避免和上文常数域 K 混淆，本节把原权式 $Q+4s$ 写成 $K_0$。

正确 f62 首次原头记录中，按 $(T^2,Tz,z^2)$ 排列的前三行
$(R_{\rm true},W_4,O)$ 的矩阵 $H_{012}$，已经完整返回准确分解
$$
\det H_{012}
=\frac{M_n^3L^4\,A\,B}{8K_0^3(1-Q)^4}.
\tag{7}
$$
这是原 run 46106007773 / job 140858793293 的既成记录，源 f62e66a27d5c999a54d03631ab8d3b31297e7aa2；本次仅读该实际记录，没有重跑头计算。其分子原因式常数为 $-1/512$，乘 $A B(-M_n)^3(-L)^4$；分母为 $K_0^3(Q-1)^4/64$，故 (7) 的符号、幂次和常数均准确。

各项单位来源是：
$$
M_n=4bcQ(1-Q),\qquad
P_{02}=2sL,\qquad P_f=4s^2K_0.
$$
当前原 $bc,Q,1-Q,s,P_{02},P_f$ 均已支付；$A$ 来自
[整个 A 零曲线排除](R150-appendix-unit211-Phi-zero-true-Azero-second-linear-and-whole-curve-exclusion.md)，$B$ 来自本篇。因此 (7) 在**整个当前正确 Phi、物理 D 非零权图**成为单位。

在这一原已付权环 $\mathcal S$ 上，把前三真均值写成
$$
H_{012}
\begin{pmatrix}T^2\\Tz\\z^2\end{pmatrix}
+L_0(\lambda)+L_T(\lambda)T+L_z(\lambda)z=0.
$$
使用 (7) 的原 adjugate，三个二次单项 $T^2,Tz,z^2$ 都可化为 $1,T,z$ 的 $\mathcal S[\lambda]$ 线性组合。每次替换严格降低 $(T,z)$ 总次数，所以**前三真均值商**在 $\mathcal S[\lambda]$ 上由
$$
1,\ T,\ z
$$
生成；加入 $N_1,N_S,P_S$ 等原条件后的商仍由这三项生成。

这是有限生成的陈述，**不声称自由秩 3、不付 lambda 首一式、不付全 Phi 空性**。此推论的头是修正后的真实 Rbar，不恢复任何旧 wrong-Rbar 的头、H42、583 或其它已撤回来源。

## 6. 唯一新实际执行

源：[F40 首一 lambda 后完整原值](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-F40-lambda-one-original-values-8542.py)，blob edbf56c8ad46479cfe5c69ee39c7c8a3d36cb421，SHA256：

18d564ff3b28972d7476cbdc367d50ea1e624ffafccd9c8ea0d9edfb56c1191c。

run **46127656231**，job **140925725598**；source commit
75ba60fabf2a120fdd63ab389158a5503a636388。
真实 pull 到 54cc47b608e210ab046f0a33b4a42a97cac7b6ee，时间 2026-11-28 08:50:33.619026 UTC，两 README 无变。

数学末阶段 15.400696364 秒，驱动 **15.431740162 秒**，最大 RSS **56524 KiB**，exit **0**；预算 120 秒/1 GiB，外驱动 135 秒。stdout **3376** 字节，SHA256：

640514078f18bdae798bb7dae46e1f5dc853c67d34132262ca6a1b3c469f045b。

[小回执](../notes/2026-11-28-unit211-Phi-zero-B-F40-and-whole-B-execution-8542.json)保存完整实际身份及原返回摘要。系数只留定义与 SHA，不保存 15829 字节 lambda 参数或 35101 字节二次系数载荷。两个旧大矩阵的实际内存失败保持冻结，本次没有重启它们。
