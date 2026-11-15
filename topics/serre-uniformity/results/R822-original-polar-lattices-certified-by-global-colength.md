# R822：以实际全局余长度认证原两图极前像

日期：2026-11-15。状态：完整纸面证明及有限域消费者的严格边界；
尚未取得或填写原 A/B 的新矩阵、Hermite 候选、极理想或其实际次数。

本条使用原 [R805 两仿射图与整基](R805-original-two-affine-charts-and-small-polar-divisor-adapter.md)、
[R811 两图极前像](R811-original-normal-polar-ideal-preimages-and-two-chart-certificates.md)、
[R791 实际 Hom 次数与原模型规范](R791-certified-original-Hom-descent-and-eta-inputs.md)。
它保留 R811 已冻结的完整 unimodular transcript 方案作为一个正确方法，
另证明一个更小的**充分认证条件**：用实际得到的两图子格的全局余长度，
与独立已证的原函数极除子次数比较，即可排除遗漏的核向量。
已知次数只进入最后的精确比较，不生成任何候选系数、矩阵秩或对角次数。

## 1. 原对象和两张图

始终取原系数域
$$
 L=\mathbf Q(b,\zeta),\qquad \zeta^2+\zeta+1=0,\qquad s=1+2\zeta ,
$$
其中 $b$ 是原 producer 所给的同一模型参数。
原 Fourier/normal 输入的 $b^i,sb^i$ 两块换基仍为
$$
 a+s c=(a+c)+2c\zeta.                                      \tag{822.1}
$$
不选择新的根、CM 方向或目标曲线缩放。

在原光滑曲线 $Y_L$ 上，R805 的真实无基点铅笔
$\langle\tau,\sigma\rangle\subset H^0(Y_L,\mathcal H)$
给有限平坦映射
$$
 \pi:Y_L\longrightarrow\mathbf P^1_L,\qquad
 z=\sigma/\tau,\quad t=\tau/\sigma,\quad zt=1.               \tag{822.2}
$$
其次数和两个仿射环的自由秩均为 $N=272$。
写
$$
 U_\tau=\{\tau\ne0\},\quad U_\sigma=\{\sigma\ne0\},\qquad
 R_\tau=\Gamma(U_\tau,\mathcal O_Y),\quad
 R_\sigma=\Gamma(U_\sigma,\mathcal O_Y).
$$
这里 $R_\tau$ 是 $L[z]$ 上的原整闭自由代数，
$R_\sigma$ 是 $L[t]$ 上的同一对象的第二张图。
原 normal 基为
$$
 \beta_{\tau,a}=d_a/\tau^{\epsilon_a},\qquad
 \beta_{\sigma,a}=d_a/\sigma^{\epsilon_a}
                  =t^{\epsilon_a}\beta_{\tau,a},
\quad
 (\epsilon_a)=(0,1^{144},2^{127}).                          \tag{822.3}
$$
因此同一个函数的坐标列从 $\tau$ 图到 $\sigma$ 图按
$$
 c_\sigma(t)=D(t)c_\tau(1/t),\qquad
 D(t)=\operatorname{diag}(t^{-\epsilon_a})                 \tag{822.4}
$$
运输。反方向是
$\operatorname{diag}(z^{-\epsilon_a})c_\sigma(1/z)$，
因为 $D(1/z)^{-1}=\operatorname{diag}(z^{-\epsilon_a})$。

令 $y=y_{f_4}$ 是原 index 4 映射在 $Y_L$ 上的真实 $y$ 函数。
原关系 $A=yB$ 中 $A,B\in H^0(Y_L,5\mathcal H)$，$B\ne0$。
两图实际 regular 乘法矩阵分别是
$$
 M_{A,\tau}=M_{A/\tau^5},\quad M_{B,\tau}=M_{B/\tau^5},
 \qquad
 M_{A,\sigma}=M_{A/\sigma^5},\quad M_{B,\sigma}=M_{B/\sigma^5}.
                                                               \tag{822.5}
$$
第二图的两个矩阵都含同一个齐次因子 $t^5$，它在比值中相消。
以下不把某一截面错误地作为 degree 0 函数运输。

令 $E=(y)_\infty$。独立于任何 R811/R822 候选，R791 已认证
$$
 \deg_L E=\deg(f_4)=1206.                                   \tag{822.6}
$$
具体地，原三次商 $\phi:X_1\to Y$ 满足
$\phi^*E=3f_4^*[O]$，两边取次数后消去 $\deg\phi=3$。
这不是把 $\deg(y_C:C\to\mathbf P^1)=3$ 再乘一次；
后者已经出现在前述等式的右边。

## 2. 候选数据不预设为 $R_\tau$-理想

假设实际求得
$$
 H_\tau,W_\tau\in\operatorname{Mat}_N(L[z]),\qquad
 H_\sigma,W_\sigma\in\operatorname{Mat}_N(L[t]),             \tag{822.7}
$$
并认证下列三组条件。

1. $\det H_\tau\ne0$、$\det H_\sigma\ne0$，且完整的矩阵多项式恒等式
   $$
   M_{A,\tau}H_\tau=M_{B,\tau}W_\tau,\qquad
   M_{A,\sigma}H_\sigma=M_{B,\sigma}W_\sigma                 \tag{822.8}
   $$
   在原 $L$ 中成立。不能只验部分行、若干模素数或选出的解。

2. 两个 $L[z]$、$L[t]$ 子格在重叠区**相等**。例如提供两组
   Laurent 矩阵 $C_{\sigma\tau}$、$C_{\tau\sigma}$，精确验证
   $$
   D(t)H_\tau(1/t)=H_\sigma(t)C_{\sigma\tau}(t),             \tag{822.9}
   $$
   $$
   \operatorname{diag}(z^{-\epsilon_a})H_\sigma(1/z)
           =H_\tau(z)C_{\tau\sigma}(z),                   \tag{822.10}
   $$
   每个系数均在相应的 $L[t,t^{-1}]$、$L[z,z^{-1}]$ 中。
   两个方向都必须成立；单向包含不足以拼接成同一子格。

3. 从候选的真实特征零系数计算
   $$
   d(H)=\deg_z\det H_\tau+
                    \operatorname{ord}_{t=0}\det H_\sigma, \tag{822.11}
   $$
   然后精确验证 $d(H)=1206$。
   对实际下三角、非零首一对角的 column-Hermite 候选，这可以直接取
   所有真实对角多项式的次数之和，以及第二图对角多项式的 $t=0$
   消失阶之和。原次数不是写进这些多项式或其元数据的代用品。

置
$$
 J_\tau=H_\tau L[z]^N\subset R_\tau,\qquad
 J_\sigma=H_\sigma L[t]^N\subset R_\sigma.                  \tag{822.12}
$$
在这一步，$J_\tau,J_\sigma$ **只是底环上的子模**。
无需先证明它们对 $R_\tau,R_\sigma$ 的乘法封闭。

## 3. 乘法方程给出包含

**引理 822.1。** 式 (822.8) 蕴含
$$
 J_\tau\subset \Gamma(U_\tau,\mathcal O_Y(-E)),\qquad
 J_\sigma\subset \Gamma(U_\sigma,\mathcal O_Y(-E)).          \tag{822.13}
$$

**证明。** 取 $H_\tau$ 的任意列对应的函数 $v\in R_\tau$；
相应 $W_\tau$ 列对应 $w\in R_\tau$。
式 (822.8) 在真实整闭代数中是
$(A/\tau^5)v=(B/\tau^5)w$。
由于 $Y_L$ 整且 $B\ne0$，其函数域内 $yv=w\in R_\tau$。
光滑曲线每一闭点的局部环是 DVR，故条件 $v\in\mathcal O_{Y,P}$、
$yv\in\mathcal O_{Y,P}$ 正好等价于
$$
 \operatorname{ord}_P(v)\ge
       \max(0,-\operatorname{ord}_P(y))
       =\operatorname{mult}_P E .
$$
对整张图的每一闭点应用即可。对任何底环线性组合结论仍成立。
第二图证明相同。这里使用真实原矩阵所表示的代数，而不是把某个
未知嵌入或有理函数模型的模近似当成原代数。证毕。

## 4. 双向包含拼接的是底空间上的子格

**引理 822.2。** 式 (822.9)–(822.10) 把 $J_\tau,J_\sigma$ 拼接为
$$
 \mathscr J\subset \pi_*\mathcal O_Y
$$
的一个 $\mathcal O_{\mathbf P^1_L}$-子格，并且
$$
 \mathscr J\subset \pi_*\mathcal O_Y(-E).                   \tag{822.14}
$$

**证明。** 两图的原 normal 基正是 $\pi_*\mathcal O_Y$ 的两个自由框架，
其变换为 (822.4)。两个精确 Laurent 包含使 (822.12) 在交集上的像相等，
故标准层粘合得到 $\mathscr J$。
两矩阵行列式非零，故两个子模各为秩 $N$ 的自由模，并且余模为挠模；
所以 $\mathscr J$ 与 $\pi_*\mathcal O_Y$ 同秩，差只支撑在有限闭点上。
引理 822.1 给出的局部包含在交集上一致，遂得到 (822.14)。
论证只用 $\mathcal O_{\mathbf P^1}$-线性性，没有预设
$\mathscr J$ 是 $\pi_*\mathcal O_Y$-子代数或理想。证毕。

## 5. 实际全局余长度及完整性

对于支撑有限的 $\mathbf P^1_L$ 上的层 $\mathscr Q$，记
$$
 \ell_L(\mathscr Q)=
 \sum_{x\in|\mathbf P^1_L|}
 [\kappa(x):L]\operatorname{length}_{\mathcal O_{\mathbf P^1,x}}
                                  (\mathscr Q_x).
                                                               \tag{822.15}
$$
剩余域次数已经包含在内，不能把“闭点个数”当成这个长度。

**引理 822.3。**
$$
 \ell_L\bigl((\pi_*\mathcal O_Y)/\mathscr J\bigr)=d(H).       \tag{822.16}
$$

**证明。** 在 $z$ 仿射直线上，候选余模是
$L[z]^N/H_\tau L[z]^N$。
由 PID 上的 Smith 分解，其 $L$-维数为
$\deg_z\det H_\tau$；这里涵盖全部有限 $z$ 点及每个不可约因子的次数。
这张图遗漏的只有 $\mathbf P^1$ 的无穷远点，在第二张图中它是
$t=0$，剩余域为 $L$。该点的 DVR 余长度等于
$\operatorname{ord}_{t=0}\det H_\sigma$。
两项相加就是 (822.15)。不能再加
$\deg_t\det H_\sigma$，否则会把两图重叠部分重复计数。证毕。

**定理 822.4（实际全长认证）。** 条件 (822.7)–(822.11) 蕴含
$$
 \mathscr J=\pi_*\mathcal O_Y(-E),\qquad
 J_\tau=\{v\in R_\tau:yv\in R_\tau\},\quad
 J_\sigma=\{v\in R_\sigma:yv\in R_\sigma\}.                 \tag{822.17}
$$
特别地，两个候选事后自动成为原整闭环的完整极理想。

**证明。** 因为 $\pi$ 有限，推前对拟凝聚层正合。于是
$$
 0\longrightarrow\pi_*\mathcal O_Y(-E)
  \longrightarrow\pi_*\mathcal O_Y
  \longrightarrow\pi_*\mathcal O_E\longrightarrow0.
$$
有限层的 $L$-长度满足
$$
 \ell_L(\pi_*\mathcal O_E)
       =\dim_L H^0(E,\mathcal O_E)=\deg_L E=1206.            \tag{822.18}
$$
把引理 822.2 的包含插入上式，得到挠层正合列
$$
 0\longrightarrow
   \bigl(\pi_*\mathcal O_Y(-E)\bigr)/\mathscr J
 \longrightarrow
   (\pi_*\mathcal O_Y)/\mathscr J
 \longrightarrow \pi_*\mathcal O_E\longrightarrow0.
$$
故第一项的长度为 $d(H)-1206$。实际认证 $d(H)=1206$ 后，此长度为零；
所有局部长度非负，所以第一项是零层。由此得到等式，并在两张仿射图上
取截面即得 (822.17)。证明没有把“候选核向量存在”替换成完整性；
完整性来自这个确切的有限长度差。证毕。

**推论 822.5。** 在原 $B\ne0$ 下，每张图的投影
$$
 \ker [M_A,-M_B]\longrightarrow\{v\in R:yv\in R\},
 \qquad (v,w)\longmapsto v
$$
是同构。因此通过本定理认证的 $H$ 与相应 $W$ 的列也是完整核的一组
底环基。这里 $w=yv$ 的唯一性来自整环内 $B\ne0$，无需另外恢复
特征零的大 unimodular 矩阵。

## 6. 认证失败时的含义

实际数据必须保留，不得用 1206 修补候选。

- 完整乘法式或重叠包含尚未通过：只能保留当前候选，不能登记极理想。
- 前两组通过且 $d(H)>1206$：已得一个严格或可能严格的子格；
  长度差真实测量尚未补齐的有限余模，不能称为完整极前像。
- 前两组通过而 $d(H)<1206$：与已认证原函数及原次数不相容，
  必须检查来源、尺度、两图运输或验证过程；不能降低原映射次数。
- 只有完整方程、双向拼接、非零行列式和真实长度等式全部通过，
  才能登记 (822.17)。

原方法中完整 column-Hermite transcript 仍然给出另一套充分证明。
本条只说明上述精确长度证书允许省掉它，而不是宣称原方案错误。

## 7. 有限域 HNF / CRT 的原域接口

本条允许后继在有限域中生成候选，再执行上述特征零认证。
它不假设原 14 次数域存在一个模素数不可约的 14 次多项式。

原域可按
$$
 L=\mathbf Q[B,Z]/(m_b(B),Z^2+Z+1),\qquad \deg m_b=7        \tag{822.19}
$$
表示；这里的 $m_b$ 是原 A/B producer 的同一有理多项式。
选择素数 $\ell\ne3$、$\ell\equiv1\bmod3$，实际检查所有输入分母可约化，
且 $m_b\bmod\ell$ 无重因子。随后实际分解
$$
 m_b\bmod\ell=\prod_i f_i,\quad \deg f_i=d_i,\qquad
 Z^2+Z+1=(Z-\omega_1)(Z-\omega_2)
$$
中的所有不可约因子和两个不同的根。于是准确地
$$
 \mathcal A_\ell
 =\mathbf F_\ell[B,Z]/(m_b,Z^2+Z+1)
 \simeq\prod_i
 \left(\mathbf F_{\ell^{d_i}}\times
       \mathbf F_{\ell^{d_i}}\right).                    \tag{822.20}
$$
即使 $m_b$ 本身不可约，也仍有这两个 degree 7 因子，
不能把二者当成一个 degree 14 域。

两图的 $[M_A,-M_B]$ 在每个真实因子中分别计算。
完整满秩、核及 monic column-Hermite 数据必须由该因子中的实际运算产生；
不能把特征零的秩数填入返回值。
同一素数各因子的结果若有不相容的 Hermite degree profile，
该素数不用于该 profile 的系数重构。

各因子的原 $B$ 多项式坐标先经普通 CRT 合并；
两个 $Z$ 根的结果再由实际可逆的二乘二 Vandermonde 合并，
从而恢复原 $1,\zeta$ 两块各 7 个 $\mathbf F_\ell$ 坐标。
这两步都须保留因子/根/原模型身份和精确的模回代。
它们不作数值根匹配，也不更换原 $b$。

canonical column-Hermite 的 $H$ 一旦固定，$W=M_B^{-1}M_AH$
在分式域中唯一。因此好素数的两图 $H/W$ 是同一特征零数据的约化。
跨素数只对完整、相容的 degree profile 累积 CRT；不能因为第一个素数
选出某 profile，就永远忽略后来另一个反复出现的 profile。
可以为实际遇到的各 profile 保留各自最新 CRT 状态并公平推进。
每一状态只保最新完整大向量及小 SHA 历史，已成模阶段不重算。

严格有理重构得到的矩阵仍只是候选。最终必须在原特征零 $L$ 中
重新核实 (822.8) 的全部系数、(822.9)–(822.10) 的全部坐标、
真实非零对角/行列式，以及 (822.11) 的实际全局长度。
这使有限域中的坏素数、偶然秩退化或错误重构都不能产生假的原极理想。
本节只规定可执行后继的正确接口；尚无该消费者的真实输出。

## 8. 本条推进与未完成量

本条把原完整极前像的最终认证缩小为：
两图的实际候选矩阵、完整原乘法方程、双向 Laurent 拼接和一个独立的
实际长度等式。它直接消除了必须在特征零保存、回放全部大 Euclid
列操作才能证明完整性的要求。

原 $A/B$ regular-multiplier producer 尚待实际完成；本条没有计算
其矩阵，没有输出任何原极理想，也没有从 1206 填入一个“实际结果”。
原 radicals、小除子、五函数 DAG、刚性化比较函数、
$\eta$、高度，以及原同源核的坐标提升均未因本条自动完成。

