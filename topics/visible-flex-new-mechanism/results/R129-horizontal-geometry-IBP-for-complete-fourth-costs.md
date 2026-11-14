# R129：完整第四导数成本在真实水平几何上的分部积分正规式

日期：2026-11-14。**纸面已证明。** 本稿给出 [R124](R124-zero-matrix-static-tail-payment-and-remaining-derivative-costs.md) 剩余完整导数密度的准确几何分部积分接口。它适用于完整 profile 系数及其任何固定线性投影或真实函数商；没有运行新的研究符号计算或几何路径。新的原因子与 pure 尾实际尚未完成时，本稿也不预报其系数或商秩。

依据 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md) 与 [R112](R112-local-fourth-geometric-derivative-weights.md)。全部原系数和边界势保留；不把局部系数非零或某个二次式的符号直接解释为实际零矩路径的周期结论。

## 1. 真实几何与系数空间

写

$$
S=(h,k,\omega),\qquad h>0,\qquad
u=h_s,\quad w=k_s,\quad a=h_{ss},\quad b=k_{ss},\quad
j=h_{sss},\quad \ell=k_{sss}.
$$

真实约束始终是

$$
\omega_s=\frac{w}{2h}.
\tag{1}
$$

令

$$
X=\partial_h,\qquad
Y=\partial_k+\frac1{2h}\partial_\omega,\qquad
D_0=uX+wY.
\tag{2}
$$

这里 $D_0$ 只微分状态系数，不微分 $u,w,a,b$。对任意依赖 $S,u,w,a,b$ 的局部表达式，真实全导数是

$$
D_s=D_0+a\partial_u+b\partial_w+j\partial_a+\ell\partial_b.
\tag{3}
$$

式 (3) 只在它所作用的表达式不含更高 jets 时使用。尤其

$$
[X,Y]= -\frac1{2h^2}\partial_\omega;
$$

本稿没有把 $X,Y$ 当作可交换的普通坐标微分，也没有把 $\omega$ 固定。$h$ 的 Laurent 项和 $\log h$ 一律按真实链式法则求导。

取一个固定有限维实向量空间 $E$，其中元素可以是真实 profile 函数、完整相位算子，或这些函数对一个固定子空间的商。几何系数是 $E$ 值的 $S$ 上光滑函数。所有公式只使用向量加法和标量乘法，不需要假设冗余 profile 表达式线性独立。

在 pure $m=8$ 应用中，可以取有限多项式系数空间模 [R116](R116-full-m8-tail-response-rank-and-finite-query-control.md) 的固定响应像 $\mathcal T$。共同右锚 $c$、$r=c-\xi$ 与 profile 坐标 $\xi$ 对真实 $s$ 微分均固定。因而 (2)–(3) 只作用于几何系数，不能在分部积分途中改锚。

## 2. 适用的 jet 阶数与完整分解

给 $u,w$ 权一，$a,b$ 权二，$j,\ell$ 权三，给 $S$ 的函数权零。考虑含 jets 至三阶、对 jets 为多项式的两个齐次密度 $L_2,L_4$，导数权分别为二、四。它们必可唯一按 jet 单项式收集成

$$
L_2=p(S)a+q(S)b+Q_2(S;u,w),
\tag{4}
$$

其中 $Q_2$ 对 $u,w$ 为齐次二次式；以及

$$
\begin{aligned}
L_4={}&B_h(S;u,w)j+B_k(S;u,w)\ell\\
&+A_{hh}(S)a^2+A_{hk}(S)ab+A_{kk}(S)b^2\\
&+C_h(S;u,w)a+C_k(S;u,w)b+Q_4(S;u,w).
\end{aligned}
\tag{5}
$$

这里 $B_h,B_k$ 对速度为一次式，$C_h,C_k$ 为二次式，$Q_4$ 为四次式。各个系数均允许为零。

R112 的导数权结论本身不能作为静默截掉高阶 jets 的理由。本稿所需的三阶上限还可直接从完整 R56 原式的微分次数核对：第一场只含零阶几何，第二恢复场的局部值至一阶，第三恢复场的局部值至二阶；第四 characteristic RHS 使用这些场的至一次真实 cov 导数，以及相应 $\xi$ 导数。第三场的这一次真实微分最高至三阶。history 的真实 RHS 也按 R112 逐项保留，不能先将其值和导数同时设零。$N^{[2]}=P_{\rm acc}$ 是速度二次势，$m^{[2]}$ 同为速度二次式，故 $\mathcal B_mN$ 不新增第三阶以上的 jet。R124 的矩阵诱导项同样只含速度二次项。

因此 R124 要处理的完整

$$
\widetilde L^{[2]}=L^{[2]}+\Delta L^{[2]},\qquad L^{[4]}
\tag{6}
$$

具有 (4)–(5) 的形式。原式生产者仍应扫描实际可达的完整系数 DAG，并保留所有出现的 jets；若具体接口发现未支持的更高阶，它必须明确失败并保留原数据，不能把 (4)–(5) 当成删项许可。

## 3. 导数权二：准确速度二次式

定义权一边界势

$$
P_1=p u+q w.
$$

由 (3)，

$$
D_sP_1=p a+q b+(Xp)u^2+(Yp+Xq)uw+(Yq)w^2.
$$

于是准确恒等式为

$$
\boxed{L_2=D_sP_1+\widehat Q_2,}
\tag{7}
$$

其中

$$
\boxed{\widehat Q_2=Q_2-(Xp)u^2-(Yp+Xq)uw-(Yq)w^2.}
\tag{8}
$$

例如若某个人工标量项是 $L_2=\omega a$，则不能令系数导数为零；(8) 给其准确余项 $-uw/(2h)$。这是式 (1) 必须在全部系数上保留的直接例子，不是对当前研究密度的实际评价。

## 4. 导数权四第一步：保真消去三阶 jets

写

$$
B_h=\beta_{hh}u+\beta_{hk}w,\qquad
B_k=\beta_{kh}u+\beta_{kk}w.
\tag{9}
$$

取边界势的第一部分

$$
P_{3,a}=B_h a+B_k b.
$$

式 (3) 给

$$
\begin{aligned}
D_sP_{3,a}={}&B_hj+B_k\ell+(D_0B_h)a+(D_0B_k)b\\
&+\beta_{hh}a^2+(\beta_{hk}+\beta_{kh})ab+\beta_{kk}b^2.
\end{aligned}
\tag{10}
$$

因而设

$$
\begin{aligned}
\bar A_{hh}&=A_{hh}-\beta_{hh},\\
\bar A_{hk}&=A_{hk}-\beta_{hk}-\beta_{kh},\\
\bar A_{kk}&=A_{kk}-\beta_{kk},\\
\bar C_h&=C_h-D_0B_h,\qquad
\bar C_k=C_k-D_0B_k.
\end{aligned}
\tag{11}
$$

这里例如

$$
D_0B_h=(X\beta_{hh})u^2+(Y\beta_{hh}+X\beta_{hk})uw+(Y\beta_{hk})w^2,
\tag{12}
$$

对 $B_k$ 同理。所有 $\omega$ 导数和 $h$ 的 Laurent/log 导数均在 (12) 内，并未被丢掉。

从 (5) 减去 (10) 后，三阶 jets 被一个明确总导数准确移除，但同时留下了加速度二次项和新的速度二次乘加速度项。特别是人工项 $u j$ 余下 $-a^2$；只删除 $u j$ 会改掉实际积分。

## 5. 导数权四第二步：完整的非对称速度—加速度项

将 (11) 的两个二次式写成

$$
\bar C_h=\alpha u^2+\beta uw+\gamma w^2,\qquad
\bar C_k=\delta u^2+\varepsilon uw+\zeta w^2.
\tag{13}
$$

定义速度三次势

$$
\begin{aligned}
P_{3,v}
&=\frac13(u\bar C_h+w\bar C_k)\\
&=\frac13\{\alpha u^3+(\beta+\delta)u^2w
+(\gamma+\varepsilon)uw^2+\zeta w^3\}.
\end{aligned}
\tag{14}
$$

令

$$
H(S;u,w)=\frac{2\delta-\beta}{3}u
+\frac{\varepsilon-2\gamma}{3}w.
\tag{15}
$$

直接对 (14) 的速度变量微分给

$$
\bar C_h-\partial_uP_{3,v}=-wH,\qquad
\bar C_k-\partial_wP_{3,v}=uH.
\tag{16}
$$

因此

$$
\bar C_h a+\bar C_k b
=D_sP_{3,v}-D_0P_{3,v}+H(ub-wa).
\tag{17}
$$

这也可不选分量证明：$\bar C=(\bar C_h,\bar C_k)$ 对速度齐次二次，令 $P_{3,v}=(u\bar C_h+w\bar C_k)/3$；Euler 恒等式使 $(u,w)\cdot(\bar C-\nabla_{u,w}P_{3,v})=0$。两个速度变量中的这个多项式关系恰给剩余向量 $(-wH,uH)$，其中 $H$ 为一次式。式 (15) 是其完整系数。

两种可能余项为

$$
u(ub-wa),\qquad w(ub-wa).
\tag{18}
$$

它们不能未经检查就视作速度三次式的全导数。只有 (15) 的两个实际向量系数都为零时，全部 $\bar C_h a+\bar C_k b$ 才由此势及其状态导数支付。$D_0P_{3,v}$ 是新的速度四次式，也必须保留。

## 6. 完整恒等式与边界

设

$$
P_3=P_{3,a}+P_{3,v},\qquad
\widehat Q_4=Q_4-D_0P_{3,v}.
$$

则 (10)–(17) 合并为

$$
\boxed{L_4=D_sP_3+\mathcal N_4,}
\tag{19}
$$

其中

$$
\boxed{
\mathcal N_4=
\bar A_{hh}a^2+\bar A_{hk}ab+\bar A_{kk}b^2
+H(ub-wa)+\widehat Q_4.
}
\tag{20}
$$

这是一个指定的代数正规式，而非对所有可能局部势取商后的唯一最简表示；本稿不据它宣称各项积分独立。

对任一满足 (1) 的光滑有限路径 $B=[s_-,s_+]$，有完整积分身份

$$
\int_B(L_2+L_4)\,ds
= [P_1+P_3]_{s_-}^{s_+}
+\int_B(\widehat Q_2+\mathcal N_4)\,ds.
\tag{21}
$$

若路径两端为常值 germs，则 $u=w=a=b=0$，所以 $P_1$、$P_{3,a}$、$P_{3,v}$ 的两端值分别为零。式 (21) 的边界项准确消失。这对同一常值 germ 的闭控制字成立；即使两端状态不同，只要分别是常值 germs，这些正导数权势仍分别为零。

这个边界结论只用于本稿显式的 $P_1,P_3$。它不删除 R109 的权零端点势 $P_h+F_*$，也不删除固定桥的第四基准成本。没有常值 germ 时必须保留 (21) 的完整端差。

## 7. 与真实零矩 pure 成本的接合

在 R124 的真实零矩假设下，保持同一共同右锚，令 $E$ 为 pure 多项式空间模固定响应像 $\mathcal T$。将本稿应用于完整式 (6)，而非仅应用于诱导补项，得到

$$
\boxed{
[\Pi_8V_B]_{\mathcal T}
=\left[\int_B\bigl(\widehat Q_2+\mathcal N_4\bigr)\,ds\right]_{\mathcal T}
}
\tag{22}
$$

只要路径首末为常值 germs。若不是，则加上 (21) 的势端差。这里原 $N^{[2]}$、完整 $v^{[2]},v^{[4]}$ 及 R124 全部矩阵诱导项均已进入 $L_2,L_4$；本稿没有把 $N^{[2]}$ 假设为可调第三空间中的元素。

因为所有操作对 profile 系数都是线性的，任何固定线性投影、固定响应商或 pure 多项式奇偶投影都与 (7)、(19) 及积分交换。已经得到的准确多项式 packet 可直接供后继几何 consumer 使用；无需重编原 profile 表达式。几何微分产生的新系数也必须保留全部 $c,r$ 支撑，不能限制到旧响应列的支撑。

一个充分条件是：完整新系数代入后，(8)、(15)、(20) 的各个实际商系数全为零。此时 (22) 对所有满足其真实假设的路径均为零。其逆命题没有在此证明；若出现非零系数，仍可能有进一步水平身份、零矩约束或积分抵消。

本稿也不从 $\bar A$ 或 $\widehat Q_2$ 的形式符号推断真实成本锥。路径改变速度会同时改变矩阵积分和 frame 演化；R112 的长度重标度并不保留这些端口。完整混合成本、真正周期符号、第四 ruling、有限等距族及课题完成标准仍须继续支付。
