# R236 附录：多项式尺度主行与相对辅助下界的真实二次排核

日期：2026-11-14 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。

状态：root 已全文核验的完整条件定理。允许所有有限首位例外和任意辅助相位，不以矩阵池行列式为假设。保原 Haar 表示、原反射共轭以及真实 carry；不声称一般正常子商排除。

## 1. 精确系数范围和结论

逐位任取 X_i=N_i 或 Y_i=N_i(I+N_i)^(-1)。取复数主行 a 与辅助行 b，假设存在固定常数
$$
A>0,\qquad a_->0,\qquad c>0,\qquad J\in\mathbb N
$$
使
$$
|a_i|\le A(i+1)^{-2}\quad(i\ge0),
\qquad
|a_i|\ge a_-(i+1)^{-2}\quad(i\ge J),
\tag{1.1}
$$
$$
B:=\sum_{i\ge0}|b_i|<\infty,
\qquad
\left|\frac{b_i}{a_i}\right|\ge c(i+1)^{-2}\quad(i\ge J).
\tag{1.2}
$$
全部有限低位允许 a_i 或 b_i 为零；(1.2) 只在 (1.1) 保证 a_i 非零的高位使用。a_i、b_i 的相位均可任意，不要求 b_i 是 a_i 的正幂。

定义原范数收敛算子
$$
X=\sum_i a_iX_i,\qquad B_0=\sum_i a_i^2X_i^2,
\qquad Y=\sum_i b_iX_i,
$$
$$
\boxed{T=X^2-B_0+Y.}
\tag{1.3}
$$

**定理。** T 单射且值域稠密；同样适用于任何有限放大。

例如 a_i=(i+1)^(-2)、b_i=a_i κ_i，只要高位 |κ_i|≥c(i+1)^(-2) 且 Σ|a_iκ_i|<∞ 即符合。所有有限低位 κ_i 可以为零，包含迟首辅助；c 可以任意小，不要求 c≥1。

本稿使用[原N二次排核](R236-appendix-actual-slow-positive-quadratic-kernel-exclusion-by-joint-inverse.md)及[复相位N/Y扩展](R236-appendix-complex-mixed-cayley-quadratic-joint-inverse.md)的导子移位结构，但以下写出改变后的全部费用和选池，避免从常数 c=1 的情形免费扩展。

## 2. 原实际混合误差

在第 L 位切断低头 carry，低位取 N_i^[L] 或 Y_i^[L]，高位取 E_i，记 hat X_i。对全部 i，
$$
\|X_i\|,\|\widehat X_i\|\le3,
\qquad
\|X_i-\widehat X_i\|\le9\eta_{L-1}.
$$
故
$$
\|X\|,\|\widehat X\|\le6A,
\quad
\|B_0\|,\|\widehat B_0\|\le18A^2,
\quad
\|Y\|,\|\widehat Y\|\le3B.
$$
置
$$
M_T=54A^2+3B,\qquad D_T=324A^2+9B,\qquad K=\max(1,2M_T).
$$
真实差与导子差满足
$$
\|T\|,\|\widehat T\|\le M_T,
\qquad
\|T-\widehat T\|\le D_T\eta_{L-1},
$$
$$
\|\delta^m-\widehat\delta^m\|
\le2mD_TK^{m-1}\eta_{L-1}
\le2mD_TK^m\eta_{L-1}.
\tag{2.1}
$$
所有常数由原两行明确决定，没有隐去有限首位例外的范数。

对任意固定 h 头矩阵 D、L≥h，混合模型所有含头项 K_L 都属于有限头 nilpotent A_L=N_0^[L] 的正幂理想，系数在尾中。A_L^(2^L)=0，故若 r=2^L，则
$$
\widehat\delta^{2r}(D)=0.
\tag{2.2}
$$
辅助头项 b_i hat X_i 也无常数，因此不改变这一精确 nilpotence。

## 3. 小池常数及共享复背景逆

固定
$$
\boxed{\sigma=\min\left(\frac14,\frac1{16}\sqrt{\frac cA}\right)>0.}
\tag{3.1}
$$
令
$$
r=2^L,\quad q=\lceil\sigma r^2\rceil,
\quad I_L=\{L,\ldots,L+q-1\},\quad M_L=L+q.
$$
以后 L≥J，且充分大到 q≥2r、M_L≤2σr²。

对任意 F⊂I_L、|F|=r，设
$$
X_F=\sum_{i\notin F}a_i\widehat X_i.
$$
[R215 §§2–4](R215-slow-semigroup-resolvent-and-normal-annihilator-tail.md) 的统一真实半群界按 A 缩放，给
$$
\boxed{\|e^{zX_F}\|\le e^{16\sqrt{A|z|}}.}
\tag{3.2}
$$
选中位的准确一次系数是
$$
V_{j,F}=b_j+2a_jX_F
=2a_j(X_F+d_j),\qquad d_j=\frac{b_j}{2a_j},
\qquad |d_j|\ge\frac c{2M_L^2}.
\tag{3.3}
$$
令 ζ_j=overline(d_j)/|d_j|，每个真实逆平方用旋转 Laplace：
$$
(X_F+d_j)^{-2}=\zeta_j^2
\int_0^\infty t e^{-|d_j|t}e^{-\zeta_jtX_F}\,dt.
$$
全部积分相乘，|Σζ_jt_j|≤Σt_j。设 d=min|d_j|，由
16sqrt(At)≤dt/2+128A/d，完整单纯形积分给
$$
\left\|\prod_F(X_F+d_j)^{-2}\right\|
\le(2/d)^{2r}e^{128A/d}
\le(4M_L^2/c)^{2r}e^{256AM_L^2/c}.
$$
再用 |a_j|≥a_-/M_L²，得到
$$
\boxed{
\left\|\prod_FV_{j,F}^{-2}\right\|
\le 4^r a_-^{-2r}c^{-2r}M_L^{8r}
 e^{256AM_L^2/c}.
}
\tag{3.4}
$$
这个估计保留辅助真正相对尺度 b_j/a_j。不能把只对 b_j 的另一个预解半径换入。

## 4. 导子输入和有界弱单位

混合模型在 F 上的多重仿射最高项给
$$
\widehat\delta^{2r}(E_F^*)
=(-1)^r(2r)!E_F\prod_FV_{j,F}^2.
$$
定义
$$
U_L=\frac{(-1)^r2^r}{(2r)!\binom qr}
\sum_{|F|=r}E_F^*\prod_FV_{j,F}^{-2},
\qquad
R_L=\frac{2^r}{\binom qr}\sum_{|F|=r}E_F.
$$
于是
$$
\widehat\delta^{2r}(U_L)=R_L,
\qquad
\|U_L\|\le
\frac{8^r a_-^{-2r}c^{-2r}M_L^{8r}}{(2r)!}
 e^{256AM_L^2/c}=:C_L.
\tag{4.1}
$$
Boolean 层入射界给 ||Σ_(j∈I_L)E_j||≤(q+1)/2。q≥2r 时，
$$
\log\|R_L\|
\le\frac rq+\frac{r(r-1)}{2(q-r+1)}
\le\frac{r^2}{q}\le\frac1\sigma.
\tag{4.2}
$$
故平均算子范数不超过固定 e^(1/σ)。所选位最终离开每个固定有限柱，且其真空配对准确为2^(-r)，所以
$$
R_L\longrightarrow I\quad\text{WOT}.
\tag{4.3}
$$
σ 很小时这个范数常数可以很大，但它固定不随 L、r 变化。这是可用的弱单位，不是免费的一致逆界。

## 5. 全部实际费用的显式选择条件

置
$$
\varepsilon_L=4rD_TK^{2r}\eta_{L-1}C_L.
\tag{5.1}
$$
由 (2.1)、(2.2)、(4.1)，
$$
\|\delta^{2r}(U_L)-R_L\|\le\varepsilon_L,
\qquad
\|\delta^{2r}(D)\|\,\|U_L\|
\le\varepsilon_L\|D\|.
\tag{5.2}
$$

为使“充分大”完全可检查，可取任意 L_0≥max(4,J,h)，使对以后选用的 L≥L_0 同时有
$$
q\ge2r,\qquad M_L\le2\sigma r^2,
\tag{5.3}
$$
$$
\log^+(4rD_T)+2r\log K
+r\log^+\!\left(\frac8{a_-^2c^2}\right)
+8r\log M_L\le r^4.
\tag{5.4}
$$
每项都只含已给常数及显式 r=2^L，且左侧 O(r log r)，所以有限 L_0 存在；也可只沿逐个检验通过的 L 取序列，不需一个隐式域选择。

由 (3.1)、(5.3)，
$$
\frac{256A}{c}M_L^2
\le\frac{1024A\sigma^2}{c}r^4\le4r^4.
$$
原 carry 给 −log eta_(L-1)≥(770/16)r^4；舍去有利的 factorial 并使用 (5.4)，得到
$$
\log\varepsilon_L
\le-\left(\frac{770}{16}-5\right)r^4
<-43r^4.
\tag{5.5}
$$
因此无论 c 多小，选固定 σ 后真实 carry 都支付了全部共享逆和导子差。

## 6. 原核配对完成结论

对 f,g∈ker T 和任意固定有限头 D，完整有界导子转移给
$$
B(D\delta^{2r}(U_L)f,g)=B(\delta^{2r}(D)U_Lf,g).
$$
这是原 T 的原核；没有把 f,g 当成 hat T 的核。由 (5.2)、(5.5)，
$$
|B(DR_Lf,g)|\le2\varepsilon_L\|D\|\|f\|\|g\|\longrightarrow0.
$$
用 (4.2)–(4.3) 得 B(Df,g)=0 对所有物理有限头 D。原 P_h→I 强、P_hC=CP_h，取头矩阵把 P_hf 送至 P_hCf，立刻排除非零 f。T*=CTC 再给像稠密，完成定理。

## 7. 与旧结论的重叠及准确新范围

[R133](R133-quadratic-summable-rows-leading-sum-cyclicity.md) 的低首行和判据已覆盖非零首行和的部分。这里允许所有有限首位辅助为零，不能直接使用那条非零首行和假设。

[R236 多辅助矩阵池](R236-appendix-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages.md) 的重叠可作如下精确核对。只取纯 Y_i，并记原 Q_i=R_i-I=-2Y_i。令其主行 alpha_i=-a_i/2、辅助行 gamma_i=-b_i/2、a_*=-sum alpha_i、共同指数权 w=0。于是旧稿的 X_Q=sum alpha_i Q_i 正是本稿 X，旧 G_(2,0)=-sum alpha_i²Q_i² 正是 -B_0，辅助 Y_Q=sum gamma_i Q_i 正是 Y。取 F(U,V)=U²+V，旧真实实现 P_F(X_Q,Y_Q;G)=X²-B_0+Y 与本稿完全相同。根 (U,V)=(0,0) 处 F_V=1，所以旧平滑字符条件成立。

对 |a_i|=(i+1)^(-2)、高位 b_i=a_i²，取 I_(0,N)={N,...,2N-1}、I_(1,N)={4N,...,5N-1}。旧两行列式准确为
$$
\det\begin{pmatrix}\alpha_i&\alpha_j\\\gamma_i&\gamma_j\end{pmatrix}
=\frac14 a_i a_j(a_j-a_i).
$$
两池分离和反三角不等式给 |a_i|≥1/(4N²)、|a_j|≥1/(25N²)、|a_i-a_j|≥3/(16N²)。所以对全部横截选择 i,j 都有
$$
\frac3{6400}N^{-6}\le|\det|\le\frac{17}{1024}N^{-6}.
$$
这对 a_i 的任意复相位仍成立。两池各有 N 位、最低位≥N、最大主幅度≤N^(-2)/2，因此旧池条件及 log det^(-1)=O(log N) 全部支付。有限低位 b_i=0 不影响足够高的池。

故这整个纯 Y、规则幅度且 b_i=a_i² 的子族属于已知重叠，本稿不把它另计为首次排核。

本定理不要求那些矩阵池的全横截行列式下界，允许任意相位、任意逐位 N/Y，以及仅有 (1.1)–(1.2) 的辅助系数。不能从本稿条件未经证明就断言旧矩阵池条件成立。这里的新证明给的是这一整族统一的全域导子输入及实际 carry 费用。

它也不等同于一般“κ>2”高阶偏离：若 a_i~i^(-2)、b_i=a_i^κ，则 (1.2) 只自动覆盖 κ≤2，而 κ>2 的比值尺度更小。不同主尺度、辅助尺度和已有预解准则不能互换。

## 8. 正常商主缺口保持不变

一般正正常态对 S_N 或 S_Y 的全部右倍数湮灭，及任意未知限制/有限放大子商中的稠密像，均不由全 H 排核直接推出。若在未知商中使用 π(N_F)^* 代替物理 E_F^*，仍须付完整压缩乘法与泄漏；本稿没有借助该未付步骤。

符号范围仍按前两稿：本文T是原Haar二次式；[R200 §1](R200-boundary-right-shift-domains-and-forward-division-saturation.md)的负边界线性T_N/T_Y至少有真空核，其N=M继续开放。
