# R713 — 平滑三角 profile 的完整有理矩、三重准确 moment 与实际批次费用

2026-11-26。**已证明：对 R711 的任意准确有理数 $0<\delta<1/8$，全部十二片 profile 的任意绝对矩有明确有限有理表达；由这些矩可在任意真实幅度处同时向外包围 $A_\delta,A_\delta',A_\delta''$，并把已绑定实际工作三 moment 的全差额支付为严格费用。** 本文还给出新全正半径分支到 R710 两角 jet 费用链的完整接法，以及中央逐点 $h,h_s$ 的完整分片区间评价。

准确 profile、存在范围与微分下界来自 [R711](R711-smooth-triangle-central-profile-and-geometric-comparison.md)，准确均值根条件来自 [R709](R709-global-convex-mean-closure-without-contraction.md)，其余均值、方向、投影架、两角与四参考 jet 误差传播使用 [R710](R710-supported-unit-seed-complete-angular-jet-error-bounds.md)。本文不重证这些已登记结果。

这项证明支付的是完整准确中央 profile 及其工作三 moment 费用。它不把准确三均值残差、原参考/材料角费用或完整 normal 链费用设零，不凭小工作残差宣布几何证书，也不修改正在运行的求解源。

## 1. 全十二片的准确矩

记
$$a=\frac14,\quad c=a-\delta>0,\quad k=\frac\delta c,\qquad
I_5(u)=\frac52u^4-3u^5+u^6.$$
首 quarter 的准确函数为
$$
H_\delta(t)=
\begin{cases}
kI_5(t/\delta),&0\le t\le\delta,\\
(t-\delta/2)/c,&\delta\le t\le a-\delta,\\
1-kI_5((a-t)/\delta),&a-\delta\le t\le a.
\end{cases}
\tag{1}
$$
后三个 quarter 按 R711 完整反射或取负。整个 $h_\delta$ 有 $|h_\delta|\le1$ 和 $h_\delta(1-t)=-h_\delta(t)$。

对整数 $n\ge0$，定义
$$J_n=\int_0^1I_5(u)^n\,du,\qquad M_n=\int_0^1|h_\delta(t)|^n\,dt.$$
则每个 $J_n,M_n$ 都是有理数，且
$$
\boxed{\begin{aligned}
M_n=4\bigg[&\delta k^nJ_n+
\delta\sum_{j=0}^n(-1)^j\binom nj k^jJ_j\\
&+\frac{c}{n+1}\left((1-k/2)^{n+1}-(k/2)^{n+1}\right)\bigg].
\end{aligned}}
\tag{2}
$$

**证明。** 首 ramp 换元 $t=\delta u$ 给第一项；末 ramp 换元 $a-t=\delta u$，完整展开 $(1-kI_5(u))^n$ 给第二项；中段换元 $y=(t-\delta/2)/c$，积分区间为 $[k/2,1-k/2]$，给第三项。四个 quarter 的绝对值都是同一 $H_\delta$ 的反射，所以乘四。全部十二片都在其中，没有忽略 ramp 或重新归一化权。证毕。

特别 $M_0=1$、$0\le M_n\le1$。完整有符号矩为
$$
\int_0^1h_\delta(t)^n\,dt=
\begin{cases}M_n,&n\text{ 为偶数},\\0,&n\text{ 为奇数}.\end{cases}
\tag{3}
$$
奇矩零是准确反射恒等式；它不声称某个浮点求积的奇数和逐字为零。

## 2. 完整有限有理递推

设 $p_0(u)=1$、$p_{n+1}(u)=p_n(u)I_5(u)$，并写
$$p_n(u)=\sum_{j=0}^{6n}p_{n,j}u^j.$$
每一阶只有以下完整三项更新：
$$
p_{n+1,j+4}\mathrel{+}=\frac52p_{n,j},\quad
p_{n+1,j+5}\mathrel{-}=3p_{n,j},\quad
p_{n+1,j+6}\mathrel{+}=p_{n,j}.
$$
然后
$$J_n=\sum_{j=0}^{6n}\frac{p_{n,j}}{j+1}.
\tag{4}$$
全部运算在 Fraction 域中准确进行；式(2)末 ramp 的交错抵消不依赖浮点消去精度。任意指定有限阶数都只需有限多项式运算。检查 $M_0=1$ 和 $0\le M_n\le1$ 是此准确公式的实现核对，不是科学可行性预试。

## 3. 同时向外包围三个准确中央 moment

定义
$$A(\lambda)=\int_0^1\cos(\lambda h_\delta(t))\,dt.$$
被积函数第 $q$ 阶幅度导数绝对值不超过 $|h_\delta|^q$。紧幅度区间上一致有界，所以可逐阶求导，并得到全实轴界
$$|A^{(q)}(\lambda)|\le M_q\le1.
\tag{5}$$

取任意偶数 $L\ge2$。对 $j=0,1,2$，令
$$
P_{j,L}(\lambda)=
\sum_{\substack{0\le n\le L\\n\text{ 为偶数},\ n\ge j}}
\frac{(-1)^{n/2}M_n}{(n-j)!}\lambda^{n-j}.
\tag{6}
$$
则对任意真实 $\lambda$，
$$
\boxed{\quad
|A^{(j)}(\lambda)-P_{j,L}(\lambda)|
\le M_{L+1}\frac{|\lambda|^{L+1-j}}{(L+1-j)!},
\qquad j=0,1,2.
\quad}
\tag{7}
$$

**证明。** $A^{(n)}(0)$ 对奇数 $n$ 为零，对偶数 $n$ 为 $(-1)^{n/2}M_n$。故(6)正是 $A^{(j)}$ 在零点、至 $L-j$ 次的完整 Taylor 多项式。三个余项虽然阶数分别为 $L+1,L,L-1$，所用函数导数都是同一个 $A^{(L+1)}$；用(5)得到(7)。它对所有实幅度成立，不需要 $e^{|\lambda|}$ 因子。证毕。

一次准确矩递推到 $L+1$ 就支付三个余项。默认 $L=48$ 是准确评价算法参数；提高它不改 profile 或固定 $g$。

对于工作字 $\widehat\lambda$，先将其转成精确 binary64 有理数。所有矩系数准确；使用有向 dyadic Horner 算术评价(6)，加入(7)的对称余项区间，就得到
$$A^{(j)}(\widehat\lambda)\in\mathcal A_j,\qquad j=0,1,2.
\tag{8}$$
每一次消费者自身舍入都向外。因此(8)不需要假设原 NumPy、BLAS、libm、Gauss 权或求和的精度。

## 4. 真实工作三 moment 的全差额

设实际完整 batch 在同一 $\widehat\lambda$ 处保存了三个工作字 $\widehat a_0,\widehat a_1,\widehat a_2$。将各字准确转成有理数，并定义
$$
\boxed{\quad
E_j=\max\{|\inf\mathcal A_j-\widehat a_j|,
|\sup\mathcal A_j-\widehat a_j|\}.
\quad}
\tag{9}
$$
则 $|A^{(j)}(\widehat\lambda)-\widehat a_j|\le E_j$。这一次支付准确积分与真正工作字之间的全差额，包括实际十二片192节点求积、width、trig、浮点求和等内部路径造成的差异。无需重演原求积，也不要求另一批次的 BLAS 调用逐字相同。

(8)(9)针对的是工作幅度 $\widehat\lambda$。准确根 $\lambda_*$ 通常不同；根移动单独由下一节支付，不能混为同一费用或遗漏。

## 5. 全正半径分支的地板与幅度三重费用

设 R709 的准确均值条件给
$$0<r_-\le r=|v_*|\le r_+<1.$$
R711 保证唯一 $\lambda_*\in(0,\pi)$，且
$$\arccos r_+\le\lambda_*\le2\arccos r_-.$$
R711 还给 $-A'(\lambda)\ge\sin\lambda/3$。若实际候选已向外证明位于 $(0,\pi)$，则它与准确根之间整段可取
$$
\boxed{\quad
m=\frac13\min\left\{
\sin\widehat\lambda,\sqrt{1-r_+^2},
2r_-\sqrt{1-r_-^2}\right\}>0.
\quad}
\tag{10}
$$
证明是正弦在 $(0,\pi)$ 为凹函数，其在候选与准确根范围凸包上的最小值不低于端点最小值；两个准确根端点的正弦分别是后两项。

实际代码对正弦、平方根及除三作向外计算，只采用严格正的下界。若有限精度尚不能分离零，不能称准确根不存在；那只是本次包围不足。

设 R710 已给准确 $r,r_\phi,r_{\phi\phi}$ 的盒 $\mathcal R_0,\mathcal R_1,\mathcal R_2$，实际幅度角 jet 为 $\widehat\lambda_1,\widehat\lambda_2$。由于 $|A''|,|A'''|\le1$，直接采用完整 R710 拆分：
$$E_{\lambda,0}=\frac{\sup|\mathcal A_0-\mathcal R_0|}{m},$$
$$
E_{\lambda,1}=
\frac{\sup|\mathcal A_1\widehat\lambda_1-\mathcal R_1|
+E_{\lambda,0}|\widehat\lambda_1|}{m},
$$
$$
\begin{aligned}
E_{\lambda,2}=\frac1m\big[&
\sup|\mathcal A_1\widehat\lambda_2+
\mathcal A_2\widehat\lambda_1^2-\mathcal R_2|\\
&+E_{\lambda,0}(|\widehat\lambda_2|+\widehat\lambda_1^2)
+2|\widehat\lambda_1|E_{\lambda,1}+E_{\lambda,1}^2\big].
\end{aligned}
\tag{11}
$$
零阶根移动、第一角 jet 移动与平方差都保留。新的 source 使用准确盒(8)，而不是把工作 residual 单独当准确残差。

旧五段的 $\epsilon<r_-/4$、$\lambda<\pi/2$ 和 $(1-4\epsilon)$ 平台地板不属于新 profile，消费者不读取或沿用。

## 6. 中央 $h,h_s$ 的完整区间评价

对一个已经关联到中央物理段的准确归一化位置盒 $\mathcal T\subset[0,1]$，逐一与十二个准确有理子区间求交。每个非空交集都使用(1)的完整多项式和
$$H_\delta'=g_\delta/c.$$
四 quarter 的值符号与参数方向分别保留。每一步按有向区间四则和整次幂求值，再对全部交集取 hull。已知 $0\le H_\delta,g_\delta\le1$、$|h_\delta|\le1$ 的集合交是准确范围约束，不是裁剪未知工作值。

若中央段准确长度盒为 $\mathcal L_i$，则
$$h_\delta(t)\in\mathcal H,\qquad
(h_\delta)_s(t)\in\mathcal H_t/\mathcal L_i.$$
消费者用同一个 seed 的准确相对中央端点与所给准确 $S$ 盒构造 $\mathcal L_i$。因此中央 $h,h_s$ 的评价费用可以真正计算，而不是要求外部填零。

但准确位置盒与实际 cell/u/literal-phi 地址的关联仍是独立输入责任。一个任意数值盒不能自行证明它对应某个真实物理点；输出明确保留该关联尚未独立验证的标志。

## 7. 四参考向量 jet 与完整范围

由 R710 的 $d,w$ 两角盒、新 $\lambda$ 三重盒及中央 $h,h_s$，完整计算
$$T=\cos\alpha\,d+\sin\alpha\,w,\qquad\alpha=h\lambda,$$
$$T_\phi=\cos\alpha\,d_\phi+\sin\alpha\,w_\phi
+(-\sin\alpha\,d+\cos\alpha\,w)\alpha_\phi,$$
$$\begin{aligned}
T_{\phi\phi}={}&\cos\alpha\,d_{\phi\phi}+\sin\alpha\,w_{\phi\phi}
+2(-\sin\alpha\,d_\phi+\cos\alpha\,w_\phi)\alpha_\phi\\
&+(-\sin\alpha\,d+\cos\alpha\,w)\alpha_{\phi\phi}
-T\alpha_\phi^2,
\end{aligned}$$
$$T_s=(-\sin\alpha\,d+\cos\alpha\,w)h_s\lambda.$$
边层与外补集继续使用 R710 完整原式。逐分量与同场实际四向量字比较，得到四项费用；不以 unit norm 小误差替代方向误差。

本文并未支付：准确三均值总方程零/一/二阶残差、原参考与固定材料角包围、实际节点关联、normal 有限链全部隐式与积分误差、完整六 jet/Gram、嵌入/帽/reach/握持。这些输入缺失时不能默认零。

## 8. 完整源码与执行状态

独立完整源码 supported_smooth_triangle_seed_angular_jet_error_bounds.py 绑定 R711 provider、mean、driver、pure reader 的真实 SHA。实际批次继续使用 R710 已修复的单快照报告/数组前后 SHA 合同：准确费、完整 seed、当前 fixed scalar/chart、原顺序 literal phi 和实际保存的15数组必须同源。原三 moment 从这些实际数组读取，不另科学重算工作值。

代码区分准确 profile moment 已由本模块计算与外部准确费用仍未认证。所有科学评价只允许本公开仓库 Actions；当前只做 stdlib AST/compile/源码比较，没有执行有理矩、区间求值、均值、F/J 或科学 fixture。

即使未来一个实际 batch 返回 complete，也只覆盖该真实 batch 和请求节点；不自动支付全部连续角、完整 normal 链或 README 完成标准。
