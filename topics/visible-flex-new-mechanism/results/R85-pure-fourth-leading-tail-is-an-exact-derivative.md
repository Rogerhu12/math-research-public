# R85：真实 pure 第四幂尾的最低项是准确总导数

日期：2026-11-14。状态：**已证明**。本稿从 R56 的原始变系数恢复式保留全部第二、第三 histories，证明右端幂尾 $q=(c-\xi)^m$ 的 pure 第四最低候选阶 $4m-9$ 在真实零二阶矩阵桥上自动消去。它没有证明 $4m-8$ 或更高项消失，没有证明第四成本为零或同号。

## 1. 真正的右尾、场与局部改变量

取一条有限光滑真实路径 $s\in[0,L]$，满足 $h>0$、$\omega_s=k_s/(2h)$，首末有常值 scalar germs。固定共同右端 $c$，在其左侧一个开放小区间上取

$$q(\xi)=(c-\xi)^m,\qquad m\ge8,$$

并在 $\xi\ge c$ 外延零。查询点右方的 profile 只由这个尾决定，左侧如何延伸不影响本稿所有右锚公式。令

$$t=c-\xi,\quad z=\xi+\omega,\quad e=hz-k,\quad
\gamma=h_s,\quad \nu=\omega_s,\quad
\lambda=\frac{\gamma z-h\nu}{h^2},\quad
K_0=kz^2-\frac{k^2+1}{h}z.$$

全路径上 $c+\omega$ 有正下界，从而足够小的共同尾区间物理。所有 $s$ 导数固定 $\xi$；$c$ 不随 $s$ 改变。记

$$K=K_0+\lambda_s. \tag{1}$$

对任一 R56 forcing，保留它的完整数据 $P_H,B_H,W_H$，其中 $W_{H,s}=\mathcal R_H$、右锚 normal 分量为 $\rho_H=P_H+B_H/z$。定义局部修正

$$\widetilde W_H=W_H+\lambda P_H. \tag{2}$$

由 R56 原式逐项相加，准确得到

$$\boxed{\partial_s\widetilde W_H
=\frac{T_s}{2h^2}+K P_H+\frac{K_0}{z}B_H-\frac{\gamma}{h^2}\partial_sB_H.} \tag{3}$$

这不是删除 $-\lambda(P_H)_s$，而是把它连同真实局部端项完整转入 (2)。常值端芽上 $\lambda=0$，故

$$\widetilde W_H(0,\xi)=W_H(0,\xi),\qquad
\widetilde W_H(L,\xi)=W_H(L,\xi). \tag{4}$$

因而 (3) 与原式的完整 period 相同。路径内部两者一般不同，不能把这个修正或全部 histories 逐点置零。

## 2. 恢复场的最低切向部分

R56 恢复分子写为

$$V_H=(A_H,\ zP_H+B_H,\ eA_H-hW_H),\qquad Z_H=FV_H/z.$$

其中 $A_H=(W_H)_\xi/2+\eta_{0,H}/h$。把 R56 的完整 $\eta_0$ 和 (2) 代入，得

$$\boxed{A_H=
\frac12(\widetilde W_H)_\xi
-\frac12\lambda_\xi P_H
-\frac{T_{s\xi}}{2h^2}
+\frac{\gamma}{2h^2}(B_H)_\xi
-\frac1{2h}(P_H)_s.} \tag{5}$$

特别 $\lambda_\xi=\gamma/h^2$；(5) 没有把移动正交框架的分量当作普通固定坐标求导。

取两个场的最低部分分别为 $Y_{a(s)t^i}$、$Y_{b(s)t^j}$，其中 $i,j\ge2$，允许前面的 scalar 系数依赖 $s$。原始第一场的分子为

$$V_q=(-q'/2,0,hq-eq'/2).$$

因此两场分子的最低切向部分都沿 $(1,0,e_0)$，其中

$$z_0=c+\omega,\qquad e_0=hz_0-k,\qquad Q_0=1+e_0^2.$$

记

$$a_{ij}=\frac{i(i-1)j(j-1)}{i+j-3},\qquad
\mathcal C(s)=\frac{K(s,c)Q_0(s)}{8h(s)}. \tag{6}$$

由右积分 $\int_\xi^c(c-\eta)^n\,d\eta=t^{n+1}/(n+1)$，forcing $H(Y_{a t^i},Y_{b t^j})$ 的最低 normal 原函数为

$$P_H=\frac{Q_0}{8h}\,a_{ij}ab\,t^{i+j-3}+O(t^{i+j-2}). \tag{7}$$

而 $B_H$ 和 $T_s$ 都至少从 $t^{i+j-2}$ 开始。真正 $s$ 导数只作用于平滑系数，不降低 $t$ 的幂；移动框架的协变项也不降低它。故 (3) 给

$$\partial_s\widetilde W_H
=a_{ij}\mathcal C(s)ab\,t^{i+j-3}+O(t^{i+j-2}). \tag{8}$$

在 (5) 中，除第一项外所有项至少从 $t^{i+j-3}$ 开始。因此若 $\widetilde W_H=w(s)t^{i+j-3}+O(t^{i+j-2})$，恢复场的最低切向部分准确等于

$$-Y_{w(s)t^{i+j-3}}, \tag{9}$$

其余场分子高一阶。这里的负号来自恢复中的 $+(\widetilde W_H)_\xi/2$，与第一场的 $-q'/2$ 相反；它决定下文第三和第四式的符号。

式 (7)–(9) 只针对最低阶系数。它们没有把包含 normal 部分的完整恢复场替换成一个齐次场，也没有省略下一阶几何/局部项。

## 3. 真实第二、第三最低 histories

按 pure 模式的同一原始约定，取

$$Y=Y_q,\qquad Z_2=\mathcal I H(Y,Y),\qquad
U_3=\mathcal I H(Y,Z_2),$$

其中 $\mathcal I$ 为 R56 的正号、共同右锚恢复。两个 scalar histories 在 $s=0$ 都为零。令

$$p=2m-3,\qquad r=3m-6,$$

$$\widetilde W_2=b(s)t^p+O(t^{p+1}),\qquad
\widetilde W_3=u(s)t^r+O(t^{r+1}). \tag{10}$$

由 (8)(9)，这些是准确的系数微分方程：

$$\boxed{b'=a_{mm}\mathcal C,\qquad
u'=-a_{mp}\mathcal C b,\qquad b(0)=u(0)=0.} \tag{11}$$

第三式的负号来自 $Z_2$ 最低部分为 $-Y_{b t^p}$。即使某个 $s$ 恰有 $b(s)=0$，系数恒等式 (11) 仍成立，无须除以 $b$。

常值初始 germ 与零传入 histories 一起保证 (10) 的初值为零；若入口不是常值 germ，(2) 的局部入口修正不能擅自忽略。

附带地，由 (11) 有

$$u(s)=-\frac{a_{mp}}{2a_{mm}}b(s)^2. \tag{12}$$

它是最低系数的真实积分恒等式，不宣称完整 $W_3$ 是完整 $W_2$ 的平方。

## 4. pure 第四最低项的准确原函数

pure $-4$ forcing 按 R56/R71 为

$$H_4=-\frac1{16}H(Z_2,Z_2)-\frac14H(Y,U_3). \tag{13}$$

仍对第四 scalar 应用 (2)，记 $\widetilde W_4=W_4+\lambda P_4$。由 (8)(9)，(13) 的最低候选阶是

$$n=4m-9,$$

且

$$\boxed{[t^n]\partial_s\widetilde W_4
=\mathcal C\left(-\frac{a_{pp}}{16}b^2+\frac{a_{mr}}4u\right).} \tag{14}$$

第二项为正号，因为 $U_3$ 最低部分为 $-Y_{u t^r}$，而 (13) 的第二权重是 $-1/4$。第四两项都必须保留。

为避免依赖除以未知 history 的操作，定义常数

$$\beta_m=\frac{a_{mr}}{4a_{mm}},\qquad
\alpha_m=-\frac{a_{pp}}{48a_{mm}}+
\frac{a_{mr}a_{mp}}{12a_{mm}^2}.$$

直接用 (11) 微分得到

$$\boxed{[t^{4m-9}]\partial_s\widetilde W_4
=\frac d{ds}\left(\alpha_m b^3+\beta_m b u\right).} \tag{15}$$

核对只需
$3\alpha_m a_{mm}-\beta_m a_{mp}=-a_{pp}/16$ 与
$\beta_m a_{mm}=a_{mr}/4$。因此 (15) 是完整系数的总导数身份；没有通过状态取零删去真实混合项。

若再代 (12)，也可写成

$$[t^{4m-9}]\widetilde W_4(s)
=-\left(\frac{a_{pp}}{48a_{mm}}+
\frac{a_{mr}a_{mp}}{24a_{mm}^2}\right)b(s)^3, \tag{16}$$

采用零初始第四 scalar。(16) 的系数符号不能当作闭桥的第四成本符号，因为闭桥的 $b(L)$ 受二阶条件约束。

## 5. 零二阶矩阵已经足以消掉这个首项

假设整座真实桥的二阶矩阵为零。R73 给

$$W_2(L,\xi)=\Phi_{M_{\rm total}}(q,q)(\xi)=0.$$

末端常值 germ 又给 $\widetilde W_2(L)=W_2(L)$，所以 $b(L)=0$。由 (4)(15) 以及零初始 histories，

$$\boxed{[t^{4m-9}]V_4
=\left[\alpha_m b^3+\beta_m b u\right]_0^L=0.} \tag{17}$$

这里 $V_4=\int_0^L\mathcal R_{H_4}\,ds$ 是原始 pure 第四 period，而非内部局部修正。因为两个端点 $\lambda=0$，其最低系数与 $\widetilde W_4$ 端差相同。

值得明确：本结论**不需要**完整第三算子 $\mathcal T=0$，甚至不需要在末端另外设 $u(L)=0$；(15) 中每个端项都有 $b$ 因子。零二阶矩阵与常端芽已经支付这一最低阶消去。

若改取 $q=A_0t^m$，整个 pure 第四响应按四次齐次性乘 $A_0^4$，所以 (17) 保持。上面 $b,u$ 的公式按单位幅值定义；不能把含实际幅值的第二 history 三次方直接误读为六次 profile 响应。

## 6. 严格范围与后续系数

本稿的有限幂尾在右接缝为 $C^{m-1}$；$m\ge8$ 足以合法使用上述有限阶场、右积分和系数展开。它可以用于检测准确算子身份。若随后从某个实际函数值取得非零结论并推广到 $C^\infty$ profiles，仍须用保持 collars 的有限阶光滑逼近；本文没有把一个非零有限尾自动宣布为所有平尾 profiles 的障碍。

全部局部分析在同一右端 $c$，没有逐段改锚、改变 profile 或重置 histories。$\mathcal C$ 一般含几何二阶导数且可以变号；本稿不对它作正性假设。

真正待检验的项从 $t^{4m-8}$ 或更高开始。那里 (5) 的其余部分、$T_s,B_H$、$z,e$ 的一阶变化以及更多第二/第三 tail histories 都可能进入，不能继续仅使用 (11) 代替完整 R56 恢复。新的公开 Actions producer 将按 $t$ 幂保留这些真实系数与原始 ODE，不修改已冻结的 R56 源码或旧输出。

所以 (17) 是一个需要先消去的自动项，不是所求零第四成本环，也不是实幂尾的同号对偶泛函。完整 $V_4$、$P_0$、ruling、更多高阶及主课题几何完成门均仍未支付。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R84](R84-fourth-cost-semigroup-and-frame-length-bound.md)。证明为以上原始公式推导，不依赖尚未执行的研究计算。
