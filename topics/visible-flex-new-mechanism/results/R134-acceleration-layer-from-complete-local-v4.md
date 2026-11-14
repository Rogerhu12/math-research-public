# R134：完整第四成本的加速度层只由已发局部生成元决定

日期：2026-11-14。**已证明。** 本稿是 R109、R112、R129、R130 的原式推论，
不进行新的 profile 评价、forcing 编译或几何计算。它给出下一完整 mixed 消费的
严格分层：先处理五类加速度正规系数，无须先展开所有局部势响应。

## 1. 固定对象与导数权

保留 R109 的 canonical 目标、完整两 mode、同一右 collar 和真实原函数。
令
$$
S=(h,k,\omega),\qquad
u=h_s,\quad w=k_s,\quad a=h_{ss},\quad b=k_{ss},
\quad j=h_{sss},\quad \ell=k_{sss},
$$
并一直满足
$$
\omega_s=\frac{w}{2h},\qquad h>0.
$$
状态方向导数记作
$$
X=\partial_h,\qquad
Y=\partial_k+\frac1{2h}\partial_\omega,\qquad
D_0=uX+wY.
\tag{1}
$$

R73 的逐点二阶密度与 R109 的真实局部第三势分别分解为
$$
m=m_0(S)+m_2(S;u,w),\qquad
N=N_0(S)+N_2(S;u,w).
\tag{2}
$$
这里 $m_2$ 和 $N_2$ **都是速度 $(u,w)$ 的齐次二次式**，不含 $a,b,j,\ell$。

这比只说“几何导数权为二”更强，来源分别是：

- R73 的点态八矩公式只使用 $h,k,\omega,h_s,k_s$，
  故其权二部分就是速度二次；
- R109 式 (3)、(7) 中 $N_2=P_{\rm acc}$，
  而 R77 的对称加速度原函数 $P_{\rm acc}$ 本身是速度二次。
  $P_h$ 与端点势 $F_*$ 都属状态项 $N_0$。

因此不能用“权二也可能含加速度”来替换 (2)，也不能把
$N_2$ 擅自设为零或当作已在 $W$ 中。本稿完整保留它。

完整第四局部生成元为 $v=v_0+v_2+v_4$。R109 的商代表为
$$
L=v-\mathcal B_m(N),
\tag{3}
$$
其中 $\mathcal B$ 是 R83/R109 的完整两 mode 响应，关于 $m,N$ 双线性。
它在当前 $s$ 只进行 profile 运算，**不对几何状态或几何 jets 求 $s$ 导数**。
所以
$$
\begin{aligned}
L_2&=v_2-\mathcal B_{m_0}(N_2)-\mathcal B_{m_2}(N_0),\\
L_4&=v_4-\mathcal B_{m_2}(N_2).
\end{aligned}
\tag{4}
$$

## 2. 精确的导数层分离

由 (2) 与双线性，
$$
\mathcal B_{m_2}(N_2)
$$
是 $(u,w)$ 的齐次四次式，系数为仅依赖状态 $S$ 的完整第四 profile 算子。
它没有任何加速度或三阶几何 jet。因此可以唯一写成
$$
\mathcal B_{m_2}(N_2)
=\sum_{\nu=0}^4 R_\nu(S)u^{4-\nu}w^\nu.
\tag{5}
$$

同理，
$$
\mathcal B_{m_0}(N_2)+\mathcal B_{m_2}(N_0)
=\sum_{\nu=0}^2 S_\nu(S)u^{2-\nu}w^\nu.
\tag{6}
$$

R130 的八矩规范化还会从 $L_2$ 减去
$$
\Gamma(m_2),
$$
它同样仅是速度二次。因此：

1. 完整规范化 $L_2$ 中 $a,b$ 的两个线性系数，恰等于 $v_2$ 中的对应系数；
2. 完整 $L_4$ 中所有含 $j,\ell$、加速度二次或速度二次乘加速度的系数，
   恰等于 $v_4$ 中的对应系数；
3. 任何 $N_2$、$N_0$ 或八矩静态基准修正，都不能改变上述两个层次。

这些是原式恒等式，不以 profile 正规形式的独立性、数值采样或消元秩为前提。
对完整 mode $-4$ 和 $-2$ 同时成立；不能只核纯 mode 后推广。

## 3. 五类正规加速度系数的显式来源

把已发 $v_4$ 按真实几何 jets 写成
$$
v_4
=B_h(S;u,w)j+B_k(S;u,w)\ell
+A_{hh}(S)a^2+A_{hk}(S)ab+A_{kk}(S)b^2
+C_h(S;u,w)a+C_k(S;u,w)b+Q_4^v(S;u,w),
\tag{7}
$$
其中 $B_h,B_k$ 是速度一次式，$C_h,C_k$ 是速度二次式。
R129 已证明实际原式具有这个形状；若将来输入出现额外 jet 型，
消费者必须拒绝，不能静默丢弃。

令
$$
B_h=\beta_{hh}u+\beta_{hk}w,\qquad
B_k=\beta_{kh}u+\beta_{kk}w.
$$
从 (7) 减去真实导数
$$
D_sP_{3a},\qquad P_{3a}=B_h a+B_k b,
$$
得到
$$
\begin{aligned}
\bar A_{hh}&=A_{hh}-\beta_{hh},\\
\bar A_{hk}&=A_{hk}-\beta_{hk}-\beta_{kh},\\
\bar A_{kk}&=A_{kk}-\beta_{kk},\\
\bar C_h&=C_h-D_0B_h,\\
\bar C_k&=C_k-D_0B_k.
\end{aligned}
\tag{8}
$$
这里的 $D_0$ 只对状态系数求导，故不会凭空增加 profile 原函数或重锚。
尤其 $\omega$ 的状态导数必须使用 (1) 的 $Y$，不能把
$\omega_s$ 当作一个独立控制。

再记
$$
\bar C_h=\alpha u^2+\beta uw+\gamma w^2,\qquad
\bar C_k=\delta u^2+\varepsilon uw+\zeta w^2.
$$
取
$$
P_{3v}=\frac{u\bar C_h+w\bar C_k}{3},\qquad
H_1=\frac{2\delta-\beta}{3},\qquad
H_2=\frac{\varepsilon-2\gamma}{3}.
\tag{9}
$$
R129 的准确分部积分给
$$
L_4
=D_s(P_{3a}+P_{3v})
+\bar A_{hh}a^2+\bar A_{hk}ab+\bar A_{kk}b^2
+(H_1u+H_2w)(ub-wa)
+\widehat Q_4.
\tag{10}
$$
结合 (5)，
$$
\widehat Q_4
=Q_4^v-D_0P_{3v}-\mathcal B_{m_2}(N_2).
\tag{11}
$$

由 (8)、(9) 可以看出：
$$
\boxed{\bar A_{hh},\ \bar A_{hk},\ \bar A_{kk},\ H_1,\ H_2}
\tag{12}
$$
**全部只需已发 $v_4$ 的原根以及有限次真实状态微分。**
既不需要构造任何 $\mathcal B_{m_2}(N_2)$，
也不需要第三可调基重新编译、累计历史或新的第四 forcing。

但 (11) 也准确标出剩余义务：
**不能因此省略 $N_2$ 在速度四次正规系数中的贡献。**
同样，$v_2$ 的加速度线性部分只给完整 $\widehat Q_2$ 的原函数修正；
其速度二次基项仍须保留 (6) 和 $\Gamma(m_2)$。

## 4. 为什么这些是实际成本空间的元素

令 $E$ 是 R130 的有限真实 ambient 空间，$\mathcal U_4$ 为
实际有限同端口、frame 恒等、$M=T=0$ 路径的完整 canonical 成本的线性 span。

R130 已证明
$$
\mathcal U_4
=\mathcal R_8+
\operatorname{span}\left\{
\widetilde L_0,\ 
\widehat Q_2\text{ 的三个系数},\
\bar A_{hh},\bar A_{hk},\bar A_{kk},\
H_1,H_2,\
\widehat Q_4\text{ 的五个系数}
\right\},
\tag{13}
$$
右侧取所有实际状态 $h>0,k,\omega$ 的算子值。
因此 (12) 的每一个状态值，已经属于真正的 $\mathcal U_4$。
这里并没有把任意几何单项系数先当成独立可调成本；
这一解释依赖 R130 已完成的端口/frame/M/T 消去和微幅路径论证。

若某个 (12) 系数写成有限个线性独立状态函数的展开
$$
A(S)=\sum_\rho f_\rho(S)A_\rho
$$
（例如独立的 Laurent/$\log h$/多项式单项），则每个 $A_\rho$ 也在
$\mathcal U_4$。证明可取任意湮灭 $\mathcal U_4$ 的线性泛函，
由所有实际状态值为零和 $f_\rho$ 独立得到每个系数为零，
再用有限维双湮灭子定理。它不要求不同 profile 原式预先独立。

所以若公开消费者对某个这些系数给出
$$
A_\rho\notin
\mathcal R_8+\operatorname{span}\{N^jG\},
$$
并且以完整原式依赖上界和真实有理分离子式支付这个非成员，
就得到实际 $\mathcal U_4$ 的新商方向。
仅有正规形式余项或纯尾投影余项时，则必须保留各自较窄范围。

## 5. 下一消费的准确范围

可以先从已公开完整 derivative-factor 导出中，仅选取 $v_4$ 内涉及
$j,\ell$、$a^2,ab,b^2$、$u^2a,uwa,w^2a,u^2b,uwb,w^2b$ 的原根；
按 (8)、(9) 在几何系数层计算五类完整两 mode 算子。
这个步骤的输入/输出都可独立保存原 DAG 和哈希，且不评价任何旧响应。

如果五类都在已知可付空间中，已付的是加速度层，不是整个第四成本。
剩余 $\widetilde L_0,\widehat Q_2,\widehat Q_4$ 仍须支付；
尤其后两项保留完整 $N_0,N_2$ 响应。
反之，原式分离给出的新实际 span 方向也不自动是双向可达方向，
不把成本半群换成线性空间，不保证正性障碍消失。

共同物理区间、目标、右锚、真实路径常值端 germs 及两 mode 必须保持。
本稿不支付第四 ruling、高阶收敛、有限等距族、闭面嵌入或 reach。

来源：
[R73](../results/R73-pointwise-eight-matrix-and-local-third-bridge.md)；
[R77](../results/R77-weight-three-local-operator-actual-finite-controllability.md)；
[R109](../results/R109-local-density-of-the-complete-fourth-quotient.md)；
[R112](../results/R112-local-fourth-geometric-derivative-weights.md)；
[R129](../results/R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)；
[R130](../results/R130-true-fourth-span-from-horizontal-normal-coefficients.md)。
