# R647：多项式隐式Frenet残差、度量输运与完整节点消元

2026-11-17，Astra-larger-parallel-16f63c8b（AI辅助）。**表示与线性消元恒等式已证明；矩阵条件数和误差读数是有限数值证据。** 本条复用[R354](R354-full-Frenet-velocity-and-closed-step-Hermite-remainders.md)的速度公式及[R624](R624-finite-frenet-fourier-convolution-jacobian.md)的完整Fourier卷积，不重新登记它们。新增的是保留独立位置/速度的多项式约束、对应的实际度量缺陷输运、全部节点/中点耦合方程的精确消元，以及原M160参考场上的完整局部矩阵读数。

没有运行新的全局BVP。既有显式1.03求解不改。下述有限投影多项式方程**不等于**原有限投影显式RHS，不能沿用后者的接受标签；物理正确性仍须由实际场、目标g、分支及全部几何验证支付。

## 1. 连续约束及正分支

令实际空间映射为$F(s,\phi)$，独立速度为$V$。在旋转正交架中，仍用R624的准确连接导数

\[
 d=F_\phi,\quad e=F_{\phi\phi},\quad
 Q=d\cdot d,\quad W=|d\times e|^2,
 \quad k=a'/a,
 \quad H=W-k^2Q^3.
\]

定义三个多项式残差

\[
 r_0=V\cdot d,\qquad
 r_1=V\cdot e+kQ,\qquad
 r_2=V\cdot V-1.                 \tag{1}
\]

在$Q,W>0$下，$r_0=r_1=0$迫使$V$的$\operatorname{span}(d,e)$分量等于$-kQ(Qe-(d\cdot e)d)/W$。再用$r_2=0$及正向条件$V\cdot(d\times e)>0$，得

\[
 V={-kQ(Qe-(d\cdot e)d)+\sqrt H(d\times e)\over W},
 \qquad H>0.                    \tag{2}
\]

反代也成立。这只是R354公式的约束表示；负分支必须另行排除。式(1)在任意有限实$F,V,k$上都定义，包含$H<0$的试探状态；这表示代数残差可评价，**不表示该试探状态是实等距解**。

特别地，逐角对$V$的三行导数矩阵为$[d^T;e^T;2V^T]$，其行列式

\[
 2V\cdot(d\times e)
\]

在正分支上为$2\sqrt H$。所以去掉显式平方根没有消除分支退化。后面的有限Galerkin速度矩阵还须独立检查；逐角可逆本身不自动证明有限压缩矩阵可逆。

## 2. 对真实映射的度量缺陷输运

若$F_s=V$，则精确微分给

\[
 Q_s=2d\cdot V_\phi
     =2\partial_\phi r_0-2V\cdot e
     =2kQ+2(\partial_\phi r_0-r_1).
\]

因此

\[
 \boxed{\left({Q\over a^2}\right)_s
   ={2\over a^2}(\partial_\phi r_0-r_1).}       \tag{3}
\]

对声明的固定正密度$\rho(\phi)$与目标$g=ds^2+a(s)^2\rho(\phi)^2d\phi^2$，令
$\eta_0=Q(s_0)/(a(s_0)^2\rho^2)-1$。实际相对Gram三分量准确为

\[
 e_r=r_2,\qquad f_r={r_0\over a\rho},\qquad
 g_r=\eta_0+{2\over\rho^2}\int_{s_0}^s
             {\partial_\phi r_0-r_1\over a^2}\,du.       \tag{4}
\]

这些恒等式不假设残差为零。给出全角/全径向残差及初始误差界，就能据(4)界定实际度量；不能只检查被保留的低模。若高core系数变化，仍须按R240支付共同材料角与同一canonical度量的身份，不能把不同$\rho$的表达直接相减。

## 3. 保全部槽位的有限方程与Jacobian

保原$R,Z$的$0,2,\ldots,2M$余弦模与$T$的$2,\ldots,2M$正弦模，位置系数$Y$和速度系数$U$各有$n=3M+2$个分量。$V$是$U$的同一向量合成。残差奇偶性给出方正投影

\[
 C(Y,U;k)=
 \begin{pmatrix}
  P_{\sin,1:M}r_0\\
  P_{\cos,0:M}r_1\\
  P_{\cos,0:M}r_2
 \end{pmatrix}\in\mathbb R^{3M+2}.             \tag{5}
\]

没有删除任一原状态模、两个位置均值或任一残差均值。原M160的槽数为$160+161+161=482$。本次N2048满足$N>8M$，三种二次残差在旋转架中的最大物理频率$4M=640$完整落在Nyquist内。所有角点参与同一有限DFT；这仍是有限方程，未保留的$M+1,\ldots,2M$残差模不由(5)消失。

尤其$U=P V_*(Y)$并不推出$P r(Y,U)=0$，因为乘积与投影不交换。反向也不能在有限M上成立。后文实际原warm的非零(5)正展示这一差别。

固定k时，完整变分为

\[
 \delta r_0=d\cdot\delta V+V\cdot\delta d,\quad
 \delta r_1=e\cdot\delta V+V\cdot\delta e+2k d\cdot\delta d,
 \quad \delta r_2=2V\cdot\delta V.             \tag{6}
\]

令$D_n=inI+\Omega$，按R624同一DFT规范，定义逐角矩阵

\[
 A=\begin{pmatrix}V^T\\2kd^T\\0\end{pmatrix},\quad
 B=\begin{pmatrix}0\\V^T\\0\end{pmatrix},\quad
 C_V^{\mathrm{point}}=\begin{pmatrix}d^T\\e^T\\2V^T\end{pmatrix}.
\]

全部有符号频率的导数准确为

\[
 \widehat{\delta r}_\ell
 =\sum_n(\widehat A_{\ell-n}D_n+\widehat B_{\ell-n}D_n^2)\delta Y_n
  +\sum_n\widehat{C_V^{\mathrm{point}}}_{\ell-n}\delta U_n.    \tag{7}
\]

证明与R624一样只交换有限和。输出按(5)的sin/cos槽读取，输入按R/T/Z原槽读取，零模只出现一次，得到全部两个$n\times n$矩阵$C_Y,C_U$。k的变化另有$C_k=P(0,Q,0)$，在固定scalar的Newton中没有把它当未知控制。

## 4. 全部节点/中点方程的准确消元

给定J个节点$s_i$，令每节点的$Y_i,U_i$都为独立未知量。两端的原完整边界$B(Y_0,Y_{J-1})=0$共n行，本次仍为325左、157右。每节点施加n行$C(Y_i,U_i;k_i)=0$。每个胞元长度h，用同一三次Hermite式定义

\[
 Y_m={Y_i+Y_{i+1}\over2}+{h\over8}(U_i-U_{i+1}),\qquad
 U_m={3\over2h}(Y_{i+1}-Y_i)-{U_i+U_{i+1}\over4},         \tag{8}
\]

并施加全部n行$C(Y_m,U_m;k_m)=0$。未知数为$2nJ$；方程为$nJ+n(J-1)+n=2nJ$。式(8)就是该三次式及其真实中点导数，不使用一个新RHS替代速度。

假设本次线性化的各节点$C_{U,i}$可逆。记节点残差$c_i$，令

\[
 A_i=-C_{U,i}^{-1}C_{Y,i},\qquad
 b_i=-C_{U,i}^{-1}c_i,
 \qquad \delta U_i=A_i\delta Y_i+b_i.           \tag{9}
\]

在胞中点记$P=C_{Y,m},\;Q_m=C_{U,m},\;c_m=C(Y_m,U_m;k_m)$。将(9)逐项代入(8)的微分，得到完整相邻块方程

\[
 L_i\delta Y_i+R_i\delta Y_{i+1}=q_i,          \tag{10}
\]

\[
 L_i=P(\tfrac12I+\tfrac h8A_i)
        +Q_m(-\tfrac{3}{2h}I-\tfrac14A_i),
\]
\[
 R_i=P(\tfrac12I-\tfrac h8A_{i+1})
        +Q_m(\tfrac{3}{2h}I-\tfrac14A_{i+1}),
\]
\[
 q_i=-c_m-P{h\over8}(b_i-b_{i+1})
                  +Q_m{b_i+b_{i+1}\over4}.                \tag{11}
\]

原边界线性化原样保留。每个解$\delta Y$经(9)唯一恢复所有$\delta U$，满足完整节点及中点线性方程；反过来任一完整线性解都必须满足(9)–(11)。这证明了条件下的准确一一对应，不是删除速度方程或只保边界低模。相邻n×n结构可由既有分离边界QR消费者接收；本条没有执行全局QR或新的Newton。

此表示使用三次Hermite配点。没有仅凭公式阶数宣称整个含标量分段的候选已四阶收敛、C²或同g精化完成；这些仍需实际场构造与精化。

## 5. 原参考场上的实际有限读数

唯一短warm SHA为`1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057`；仅用于对比的长warm是原827节点adaptive参考，SHA `7feed9f91f60a28d42a0bce352d742804bf11f9b9e5dd567ea5ad871eacebe74`。没有读取1396或1719求解失败/中间场作父。

短warm取其保存的全部位置与原投影RHS速度；数值结果为：

| s / 位置 | $\|C\|_\infty$ | 数值$\sigma_{\min}(C_U)$ | 数值$\operatorname{cond}_2(C_U)$ |
|---|---:|---:|---:|
| 1.0066723715140464，node528 | 1.9434451156624943e−6 | .0723248303027796 | 306.2879465577983 |
| 1.0283496328972757，node581 | 1.103839856725084e−5 | .08019064956693132 | 285.7335247737237 |
| 1.03，node601 | 1.81895691394208e−5 | .06484117604088512 | 354.277687985982 |

这三个点的H和$V\cdot(d\times e)$均为正。表中条件数来自浮点SVD，是有限可行性证据，不是整个径向区间或所有Newton状态的严格可逆证书。

原长warm已登记的第592胞左RMS位置$s=1.0340417600208345$，直接用其原SciPy三次式及真实导数，得到H最小值`−4.8573519173638255e−6`、法向速度最小值`−.004879701487256784`。同点多项式残差和两个完整Jacobian仍为finite，$\|C\|_\infty=.021103669160015957$，数值$C_U$条件数1755.3631834332186。它既不满足约束，也不在正确正分支；此记录仅检验代数式在原平方根域外仍可评价。

四点的同一个确定方向上，完整卷积Jacobian与独立complex-step方向比较，相对差不超过`4.791e−16`。全部行列由(7)装配；这里没有把单方向数值比较称为所有矩阵项的区间证书。

另外，对原短warm第527完整胞`[1.0062555011028305,1.0066723715140464]`，实际形成两端节点和中点全部矩阵、执行(9)–(11)，并与未消元的完整线性式比较：节点消元绝对余项≤`5.173e−12`；中点两表达的绝对差≤`1.228e−11`、相对差≤`1.925e−15`。两个相邻块均482×482，原325+157边界完整声明；未求解全局系统。

## 6. 来源、入口与剩余工作

[冻结实现](../scripts/parallel_20261117_implicit_frenet_probe.py)，9150B，SHA256

`ba0b17fc85af8510c7c45b22a8facecd59061f53b3f7fd4adb48d3380c74e1a2`。

完整报告SHA256为`2b07907557c462ab340a08fa8304722a9d8455083b362fa7be280ae132cbbd23`，实际约2.260秒。报告保所有源与原输入SHA、全部数值范围和限制；原始参考和报告不入库。

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
  "$T/scripts/parallel_20261117_implicit_frenet_probe.py" \
  --topic "$T" \
  --warm "$WORK/parallel-hold-m160-short-bvp-warm.json.gz" \
  --long-warm "$WORK/parallel-hold-m160-bvp-adaptive-warm.json.gz" \
  --rms-report "$WORK/parallel-hold-m160-bvp-rms-domain.json" \
  --out "$WORK/parallel-root-implicit-frenet-probe.json"
```

报告输入、R624 Frenet源、HoldProfile/原Profile及原SciPy cubic源均在入口和出口核身份。全局非线性残差下降、完整边界接受、正分支、未保留角模、全连续实际metric、共享C²场、闭合/全t/reach/held和固定g精化尚未由本条支付。后续若执行新多项式BVP，必须用独立完整记录，不冒作原显式P RHS的续跑或接受解。

## 附：实际 binary 核心的严格有限 C_U 证书与正支唯一性

本节只处理 R647 所用原短 warm `1662ee34...` 的核心。它不接受该 warm 的完整场，不把失败 BVP 作父，也不覆盖任意尾点、有限容差节点或 NumPy FFT 的矩阵舍入。

### 准确来源与理想三角块

M160/N2048 的实际核心满足 R0=1、全部 Z 系数准确为零，固定标量首 jet 给 a(0)=1、a′(0)=0，故 k(0)=0。其 R1..R160 与 R638 已证 hold 场 `aa1cf41f...` 的 `original_core_coefficients` 逐个作 Fraction 匹配；后者第161..320模全为零。于是准确多项式

\[
\rho=R_0+\sum_{j=1}^{160}(1-\nu_j^2)R_j\cos(\nu_j\phi),\qquad\nu_j=2j
\]

就是 R638 同一个固定 ρ。只复用已刊报告 `d3fe8df3...` 的全角下界，取准确 \(\rho_*=159/1000\)；没有重复其区间变换或正性计算。

若先令理想 T_j=−ν_jR_j、U=e_z，则 d=ρe_φ、e=−ρe_R+ρ′e_φ。按未知量顺序 (δU_T,δU_R,δU_Z)，C_U 是

\[
 C_{U,0}=\begin{pmatrix}
 P_s\rho&0&0\\
 P_c\rho'&-P_c\rho&0\\
 0&0&2I
 \end{pmatrix}.
\]

P_s、P_c 为保留 sine/cosine 空间的正交 L² 投影；这里矩阵项表示相应乘法算子后投影。两个乘 ρ 的方块均至少为 ρ_*I。令

\[
 L=\sum_j\nu_j|(1-\nu_j^2)R_j|,\qquad
 B=2/\rho_*+L/\rho_*^2+1/2.
\]

逐块反解及三角不等式给 \(\|C_{U,0}^{-1}\|\le B\)。范数为平均 2π 积分的 L² 直积范数，等价于**正交归一化** Fourier 坐标的 Euclidean 范数；不能将本数值不加转换地叫作原未归一系数矩阵的逆范数。

### 保留所有 binary 缺口的扰动

逐项准确计算 ε_j=T_j+ν_jR_j。101 个 ε_j 非零，不能把保存的左关系当作实数中完全相等。相对上述理想 d/e，

\[
 \delta d_R=-\sum\epsilon_j\sin\nu_j\phi,\quad
 \delta d_T=\sum\nu_j\epsilon_j\cos\nu_j\phi,
\]
\[
 \delta e_R=-2\sum\nu_j\epsilon_j\cos\nu_j\phi,\quad
 \delta e_T=-\sum(\nu_j^2+1)\epsilon_j\sin\nu_j\phi.
\]

取 E0=Σ|ε_j|、E1=Σν_j|ε_j|、E2=Σ(ν_j²+1)|ε_j|，并把保存 `full_ode_rhs_at_nodes[0]` 的**全部**系数与 e_z 的差分别求 l1，记 V_R,V_T,V_Z。实际三者准确为零，非浮点“小于容差”。逐点矩阵条目绝对值和给

\[
 \|\delta C_U(\phi)\|_2\le
 \delta=E_0+3E_1+E_2+2(V_R+V_T+V_Z).
\]

投影范数不超过1，故同一 δ 也控制完整有限 Galerkin 算子的扰动。准确有理运算结果为

\[
\delta=\frac{1115869547203}{1237940039285380274899124224}
 \approx9.01392241782\times10^{-16}.
\]

E0≈9.49901274e−18，E1≈7.33330396e−17，E2≈6.71894110e−16；L≈18.0517233597，B≈727.1217064092。**准确分数比较**给 Bδ<1，显示值约6.55421865e−13。Neumann 引理遂给实际数学有限算子

\[
 \boxed{\|C_U^{-1}\|\le B/(1-B\delta)<728.}
\]

这证的是精确 binary 系数所定义的准确 Galerkin 算子。N2048 下相关投影积分次数至多6M=960<N，数学上的均匀 DFT 与其一致；实际 np.fft 舍入不在这份证书内。

### 同一实际核心的正支有限速度唯一性

这个补充由 geometry 会话给出，与上面的实际证书合用。设 d0=ρ_*−E1、e0=ρ_*−2E1。源同时以准确分数验证

\[
 d_0>0,\quad e_0>0,\quad
 (d\times e)_z\ge d_0e_0-E_0(L+E_2)>0.
\]

准确平面核心且 k=0 时，前两投影约束只线性依赖水平 U_R,U_T，完全不含 U_Z。在 U=e_z 处，C_U 为该水平方块与竖直2I的块结构；其已证可逆性使水平方块可逆。因此任何**准确有限 Galerkin**根都有 U_R=U_T=0。

选取逐角正支 \(U\cdot(d\times e)>0\)，由上面的正法向得 U_Z>0。U_Z−1 属于保留 cosine 空间，以它测试第三投影式便有

\[
0=\langle U_Z-1,P_c(U_Z^2-1)\rangle
 =\langle(U_Z-1)^2(U_Z+1)\rangle,
\]

故 U_Z=1。这一步没有假定未保留残差先逐角为零。该核心的准确正支速度唯一为 e_z。

若节点隐式加速度 A 定义为对准确 C(Y,U,k)=0 微分、并令 Y_s=U 所得，则在 U=e_z 处第三行正是 2A_Z=0，故全部 A_Z 系数准确为零。它不是对任意 collocation cubic 的二导或有限容差输出作字面零声明，也尚不构成完整 BVP 接受或镜像闭合证书。

### 冻结复现

标准库 Fraction 源 `parallel_20261117_implicit_core_rational.py` SHA256 `cf3d8a6bd30968145b2a3f47e76f481e8c4e6869105a6475a121f128a9c043a7`；完整有理报告 SHA256 `69042311240f2a3d00108ed6d4004b9ab17dbef691a5c316165468821a5ba6b1`，只在仓库外。报告含全部 E、L、B、δ、Bδ、逆界及正法向界的准确分数，不以显示小数作证明。

```bash
PYTHONDONTWRITEBYTECODE=1 python "$T/scripts/parallel_20261117_implicit_core_rational.py" \
 --warm "$S/parallel-hold-m160-short-bvp-warm.json.gz" \
 --reference "$S/parallel-negative-hold-complete-base.json.gz" \
 --rho-report "$S/parallel-negative-hold-arclength-interval-positive-final.json" \
 --rho-source "$T/scripts/parallel_20261117_arclength_interval_positive.py" \
 --out "$S/parallel-implicit-core-rational.json"
```

入口和出口均核固定输入 SHA；warm、reference、R638 报告、区间源的完整 SHA 分别为 `1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057`、`aa1cf41faf83a9e2b3e90167d0bc9e00e48c8d84cc2aec707c2da17c45f0ca15`、`d3fe8df338482e0ac01f3d65a2ee91baa5f2996814188a7adb31a4ec01ff9f37`、`f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d`。本节不运行新 BVP，也不重新计算 R638。

## 附：完整 Pr 的准确二次方向式与一次真实更新割线诊断

本节消费 R336 §3 的四次残差平方公式，不重报一般全局化定理。R336 处理二次 Taylor 模型，仍须支付模型与真实函数之差；这里的新增对象是 R647 固定网格、固定 `k=a'/a`、固定全部 BC 的独立 `Y/U` Pr 系统，其真实有限残差本身准确二次。未改正在运行的 `5b965` 源，未装配新 Jacobian、重解方向或新增 BVP。

### 1. 全部变量、行及方向公式

取 `M=160,N=2048,m=602,n=482`。未知量为所有节点的 `Y_i,U_i`，共 580328 个标量。残差保留 290164 个节点行、289682 个中点行和 482 个原边界行。原始系数 SSE 不换成角向积分范数，也不重加权。

令一个完整方向为 `(A_i,B_i)`。在节点，或用同一线性 Hermite 算子得到的中点上，记

\[
 d=D_\phi Y,\quad e=D_\phi^2Y,\quad V=\mathcal E U,
 \qquad \dot d=D_\phi A,\quad\dot e=D_\phi^2A,\quad\dot V=\mathcal E B.
\]

这里导数包含旋转坐标架导数，与冻结 `Frenet.jet` 完全相同。用原角投影 `P_r` 定义

\[
 j=P_r\begin{pmatrix}
 \dot V\cdot d+V\cdot\dot d\\
 \dot V\cdot e+V\cdot\dot e+2k\,d\cdot\dot d\\
 2V\cdot\dot V
 \end{pmatrix},\qquad
 q=P_r\begin{pmatrix}
 \dot V\cdot\dot d\\
 \dot V\cdot\dot e+k|\dot d|^2\\
 |\dot V|^2
 \end{pmatrix}.
\]

中点方向必须用完整公共三次式

\[
 A_m=(A_i+A_{i+1})/2+h(B_i-B_{i+1})/8,\qquad
 B_m=3(A_{i+1}-A_i)/(2h)-(B_i+B_{i+1})/4.
\]

边界贡献是 `j_bc=BA A_0+BB A_last`、`q_bc=0`。按原顺序堆叠全部行后，数学有限映射准确满足

\[
 R(X+\alpha D)=r+\alpha j+\alpha^2q. \tag{1}
\]

这里 `j=J_current D`，不是旧缓存 Jacobian 的乘积。公式不要求 `C_U` 可逆，不除根式 `H`；它也不替代物理正分支或几何门。若先将 `U` 作为非线性消元函数，仅以 `Y` 为变量，则不能照搬“准确二次”的断言。

### 2. 消费 R336：完整 raw SSE 和原回溯门

将 R336 §3 中的方向二阶项换成 `2q`，并去掉其目标的 `1/2`，得到

\[
 S(\alpha)=c_0+c_1\alpha+c_2\alpha^2+c_3\alpha^3+c_4\alpha^4,
\]

\[
 (c_0,c_1,c_2,c_3,c_4)=
 (r^Tr,\;2r^Tj,\;j^Tj+2r^Tq,\;2j^Tq,\;q^Tq). \tag{2}
\]

所有内积覆盖 580328 行。当前 `5b965` 门是 `S(alpha)<(1-.4 alpha)S(0)`。对正 `alpha`，它等价于

\[
 .4c_0+c_1+\alpha c_2+\alpha^2c_3+\alpha^3c_4<0. \tag{3}
\]

因此一次方向 pass 足以预测原有的 17 个 dyadic 门，不改变候选步长、顺序、目标或任何行；实际浮点 trial 仍须重新计算。源码另记录直接全残差与 (1) 的差，不能把数学多项式恒等式冒成逐位浮点等式。

保留完整当前线性缺陷 `e=r+j`，则

\[
 R(\alpha)=(1-\alpha)r+\alpha e+\alpha^2q. \tag{4}
\]

若 `e=0`，满步的原门恰为 `||q||²<.6||r||²`；半步的原门恰为
`4<r,q>+||q||²<8.8||r||²`。实际计算必须保留 `e`，不能只凭线性残差最大值把它设零。也不能因旧 factor 解得准就认定当前 `j≈−r`。

### 3. 原 run 日志支持的事实

读取原日志前 208 行，冻结为 scratch `parallel-implicit-quadratic-ray-log-prefix.jsonl`，SHA256 `523eb647fccc7918d78a433e80b065f0b8ff546a0a02e37566e578c789d9f418`。没有从这些 SSE 标量反拟合 `q`。

| fresh J | 完整线性相对残差（原记录） | 满步 SSE | 半步 SSE | 首次接受 alpha |
|---|---:|---:|---:|---:|
| 2 | 4.9142812e−6 | 9.855422058e−4 | 7.543179133e−5 | 1/4 |
| 3 | 1.4510018e−7 | 18.8230757854 | 1.17643951643 | 1/128 |
| 4 | 2.7879130e−6 | 4.59221363043 | .287035921815 | 1/64 |

J3/J4 的满步、半步 SSE 比约为 16，支持四次项主导的诊断方向；这张表自身不提供 `q` 向量证书。完整线性方程已解得小，而非线性较大步仍失败，两者应明确区分。

### 4. 完整方向实现核对与唯一一次真实割线

可复用 API 为 `local_terms(P,y,u,dy,du,k)`、`terms(P,Y,U,dY,dU)` 和 `analyze(P,Y,U,dY,dU,alphas,original_linear)`。第二个返回 `nodes/middle/boundary` 同形同序的 `j,q`；最后一个包括全向量 complex-step、直接试点残差、各不交方程组的内积贡献、原 17 门预测。没有 Jacobian 装配或线性求解。

首先在原 `1662` warm 上核一个源码明确写出的非 Newton、全槽平滑方向：全部 580328 行的 JVP 与 complex-step 相对 L2 差 `7.84913e−14`，节点/中点/BC 最大差分别 `1.08421e−19/5.81878e−16/3.38814e−21`。在 `alpha=1,.5,.25`，式 (1) 与直接试点的最大差为节点 `5.12e−16`、中点 `1.252e−11`、BC `1.056e−16`；中点差明确保留，不声称数值零。该 fixture 仅验证接口，不是 Newton 或物理解。

原 run 未保存逐位 `dy/du`，故没有重放其原方向。随后只读捕获了 iteration 4 和 5 的两个相邻已接受**代数迭代态**，定义新有限方向

\[
 D_{\rm eff}=(X_5-X_4)/(1/64).
\]

它含原更新舍入；重新组合 `X_4+(1/64)D_eff` 与 `X_5` 逐位相同，但不能把它等同原 Newton 方向，亦不能把代数迭代态升级为物理接受父。

本次全向量实读为

| 量 | 数值 |
|---|---:|
| `r²` | 2.8481095461615603e−5 |
| `r·j` | −2.8481095472155596e−5 |
| `||r+j||₂` | 5.423911371220497e−9 |
| `r·q` | 9.700253448880678e−6 |
| `j·q` | −9.700300556925102e−6 |
| `q²` | 5.228601106447963 |

`q²` 中节点 `r1=V·e+k|d|²` 占 `3.1496365277613076`，中点同组占 `1.7440473624667974`，合计约 93.6%；这里的归因来自所有真实 `q` 分量，不来自 SSE 拟合。

新割线的直接满步/半步 SSE 是 `5.2286011063537465/.32679711447844295`；原 17 步长预测首次通过仍为 `1/64`，此时直接 SSE 为 `2.7914325976643825e−5`。全向量 JVP complex-step 相对差 `3.02613e−12`，式 (1) 直接核对最大差 `3.64e−14`。割线的中点线性缺陷最大 `7.03397e−10`，原方向记录为 `1.40869e−10`，这个差异也说明两种方向不能逐位等同。

当前证据指出较大步失败的具体非线性来源；仅将节点 `C_U` 消元换成 `[C_Y C_U]` 零空间，若全方阵线性化可逆且仍准确解同一 `J D=−r`，精确算术下得到同一个方向，未必减小 `q²`。保全行的阻尼最小二乘会改变方向选择，是不同的后继算法；本节未执行、扫描或宣称它成功。

### 5. 冻结身份、命令与限制

- 新源：[已刊完整方向源码](../scripts/parallel_20261117_implicit_quadratic_ray.py)；当前 scratch `parallel-implicit-quadratic-ray.py`，9624 B，SHA256 `e67f7d1bf021fd88646e1a77057b4557418ff77ebd5032461d8a46dd7f6498fc`。
- Pr Problem 源 `parallel-model-implicit-frenet-newton.py`：`5b965b9c4f9979a5b8dcc38661de027570d04d55aceb86de0dc7b1217fb03aac`。多项式源 `parallel-root-implicit-frenet-probe.py`：`ba0b17fc85af8510c7c45b22a8facecd59061f53b3f7fd4adb48d3380c74e1a2`。
- 原 warm `parallel-hold-m160-short-bvp-warm.json.gz`：`1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057`。
- fixture report `parallel-implicit-quadratic-ray-fixture.json`：`14f244651cd2790034b1dcdfa4761dc24bdd5936a7b07def376218c78b874f1e`。
- 割线两端 `parallel-implicit-ray-base-capture.json.gz` / `parallel-implicit-ray-next-capture.json.gz`：`19ba03e7bec29587d4587d0b8731a955b58ab598ad56fddb63be39377a8c06f3` / `e3607befda246848f3d99f1de4ec9b9adbdb2056c5196b57fe914ed4c9459ffd`。
- 割线 report `parallel-implicit-quadratic-ray-secant.json`：`7dd1881e32479b31faa00bdc259343d825f21d3ec03e200a1ce5dbc088b54582`；有效方向 binary SHA `672891c95785a922077d6f079707207fce5a39b438830d50e93acec625bdad7b`。

在 scratch 根目录执行；省略最后两个参数即复现明确非 Newton fixture。

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_quadratic_ray.py \
  --topic math-research-public/topics/visible-flex-larger-amplitude \
  --problem-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_newton.py \
  --warm parallel-hold-m160-short-bvp-warm.json.gz \
  --polynomial-source math-research-public/topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_probe.py \
  --out parallel-implicit-quadratic-ray-secant.json \
  --base parallel-implicit-ray-base-capture.json.gz \
  --next parallel-implicit-ray-next-capture.json.gz
```

source guard 检查冻结 Problem/warm/多项式/标量/角基源；report 另记完整 mesh、节点和中点 k、全部 BA/BB/target 的 binary SHA，以及 `r,j,q` 全向量 SHA。普通 binary64 Fourier/jet 运算与 long-double 内积不是区间证书；elapsed 字段和平台差异可改变新 report 的文件 SHA。所有 raw 留 scratch，不入 Git。此节只交可核验的全局化诊断，不改变原 run、物理门、完成状态或同 g 精化责任。

## 附：全部 Pr 方程的 FFT 方向算子与准确系数伴随

本节接上面的二次余项诊断，给出保留完整有限问题的 `Jv` 与 `J^T w` 实现。它不通过节点 `C_U` 消元，因而计算这些作用不要求该子块可逆；尚未求解新的线性或非线性系统，也没有证明阻尼方法会成功。新源为 [parallel_20261117_implicit_matrix_free.py](../scripts/parallel_20261117_implicit_matrix_free.py)，10021 B，SHA256 `ff65c90a84bcdc8ff93c97c6f0ce4d2cfad723ec28d513040f2db5b0e760eca4`。

### 系数范数与 Fourier 权不能混淆

令 `S_Y` 是 `(R cosine,T sine,Z cosine)` 的普通三角合成，`S_C` 是三组约束的 `(sine,cosine,cosine)` 合成。其对应系数提取 `P` 满足

\[
 P={1\over N}D S^T,
\]

其中 `D` 的 cosine 常数槽为1，所有非零 cosine 和 sine 槽为2。本节求的是原 **Euclidean 系数残差平方和** 的伴随，不能直接把未加权角积分梯度当成它。给定一节点完整约束权 `w`，先令

\[
 (\eta_0,\eta_1,\eta_2)=S_C D_C w.
\]

记 `V=S_Y U`、`d=D_phi F`、`e=D_phi^2 F`。旋转架的真实角导为 `D_phi=partial_phi+Omega`，其中 `Omega^T=-Omega`，因此在周期角均值下 `D_phi^*=-D_phi`、`(D_phi^2)^*=D_phi^2`。由上一附节的完整方向式逐项分部，原系数 Jacobian 的准确转置为

\[
g_Y=D_Y^{-1}P_Y\{-D_\phi(\eta_0V+2k\eta_1d)
                         +D_\phi^2(\eta_1V)\},
\]
\[
g_U=D_Y^{-1}P_Y\{\eta_0d+\eta_1e+2\eta_2V\}.
\]

这里因 `N^{-1}S_Y^T=D_Y^{-1}P_Y`，没有遗漏额外 `N`；正弦系数提取本来就是 `-2 Im FFT/N`，也不再加负号。实现里的 `adjoint_pack` 恰将每个 cosine 系数取 normalized FFT 的实部、每个 sine 系数取负虚部，包括两个常数槽的准确权。

当前 M160/N2048 的输入及权函数频率不超过320；先形成的完整二次乘积频率不超过640，低于 Nyquist1024。三因子配对的最高频率960又小于2048，离散均值等于相应准确角积分。代码先计算完整乘积再 FFT；常连接与角导不混合不同频率，故可在这次完整 FFT 后只提取保留输出频率再施加连接导数。这不同于先截掉乘积前的因子，也没有遗漏高模向低模的卷积贡献。以上是准确有限数学等式，实际浮点 FFT 的舍入另列。

### 中点和边界的全部转置

局部中点返回 `(gYm,gUm)` 后，它对两端变量的贡献分别为

\[
\begin{array}{c|c}
Y_i&g_{Ym}/2-3g_{Um}/(2h)\\
Y_{i+1}&g_{Ym}/2+3g_{Um}/(2h)\\
U_i&h g_{Ym}/8-g_{Um}/4\\
U_{i+1}&-h g_{Ym}/8-g_{Um}/4.
\end{array}
\]

再加每个真实节点的局部贡献；原482条边界权以 `BA.T @ wbc` 和 `BB.T @ wbc` 加到两端 Y。所有290164节点行、289682中点行和482边界行均保留。打包变量顺序为所有Y节点再所有U节点；方程顺序为所有节点、中点、原BC。`CompleteLinear.operator()` 提供形状 `(580328,580328)` 的完整 SciPy `LinearOperator`。目标若为 raw SSE，梯度是 `2 J^T r`；若为其一半，梯度是 `J^T r`。

`LocalLinear` 只缓存实际 `d/e/V`，分块作全角 FFT，不装配全局或节点稠密 Jacobian；也不更改 scalar、mesh、模式、边界、残差范数或物理验收条件。

### 原暖场上的实际完整核对

用原 `1662ee34...` 暖场、完整 `5b965` Problem 和本节前已冻结的 `e67f7d1b...` 独立方向实现，实际报告为 `parallel-root-implicit-matrix-free-probe.json`，SHA256 `8ba00db64bc308e42ad2a5b7a08216e6f253b304f8bf0986ec8238466d19b107`。

- 一个明定全槽方向的全部580328个 `Jv` 分量与独立 `terms` 返回值逐位相同，三个分组最大差都为0。这是该次实际核对，不声称所有输入下 FFT 运算次序均逐位等同。
- 全部行的伴随点积为 `-0.0005208864078555887` 与 `-0.0005208864078557314`；差 `1.42677670707e-16`，相对这两个内积为 `2.73913215156e-13`。
- 实际节点0/528/581/601上，与完整已刊稠密 `CY.T @ w`、`CU.T @ w` 比较，最大相对 L2 差 `2.33643675784e-16`，最大绝对差 `4.36557456851e-11`。这是四个完整局部矩阵在指定权上的作用比较，不冒全矩阵区间误差证书。
- 实际几何缓存177389568 B；构造0.185秒、完整 `Jv` 0.323秒、完整转置0.237秒；整个诊断3.731秒、最大RSS337392 KiB。仅为该机器该次计时，不作为平台保证。

geometry 会话独立纸核了 Fourier 权、连接项及中点伴随；没有为本节重扫任何旧几何证书。这里解决的是完整算子的可计算性与实现核对，不把它称为新的 BVP、物理父或同g精化通过。

从仓库根，`WORK` 指仓库外的原输入目录：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_matrix_free.py \
 --topic topics/visible-flex-larger-amplitude \
 --problem-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_newton.py \
 --warm "$WORK/parallel-hold-m160-short-bvp-warm.json.gz" \
 --polynomial-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_probe.py \
 --ray-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_quadratic_ray.py \
 --ray-sha256 e67f7d1bf021fd88646e1a77057b4557418ff77ebd5032461d8a46dd7f6498fc \
 --out "$WORK/parallel-root-implicit-matrix-free-probe.json"
```

入口/出口核全部冻结原问题来源；详细完整SHA见源和前两附节。报告含耗时与路径，换目录或重跑可改变报告文件SHA。全部原数组与诊断报告留仓库外。

## 一次完整尺度/边界可行阻尼方向的实际消费

[固定µ=1的完整LM方向](../notes/2026-11-17-parallel-numerical-implicit-lm-direction.md)保原1662/全部580328行；完整列平方和、同S端点投影、原BB准确整数满秩证与tiny BC修正均付。唯一60/128 LSMR后真实满步SSE1.532103e−4→5.453865e−5，二次项q²2.926e−14；完整源/报告/实际ray与限制见该note。只有一次方向，未声称新BVP或物理接受。

## 附：保全部二次角谱的矩形残差及其完整伴随

这里固定原1662的Y/U空间、scalar、602网格与482条边界，只把每个径向节点/实际cubic中点的**输出**扩到全部二次角谱。它是与当前保留Pr不同的有限最小二乘目标；本节只形成可用残差/Jv/Jᵀv和一次原暖场诊断，未求解新线性系统或BVP，不改正在运行的927f预算。

### 准确频率、等价性与计数

R/T/Z的旋转架分量分别是cosine/sine/cosine，最高物理频率2M。真实角导含固定连接矩阵，保同一最高频率，并交换一阶导的奇偶性。故三组标量残差的完整空间是

\[
r_0\in\operatorname{span}\{\sin(2j\phi):1\le j\le2M\},\quad
r_1,r_2\in\operatorname{span}\{\cos(2j\phi):0\le j\le2M\}.
\]

每处共 `nout=6M+2` 系数；包括r2中的常数−1。在**固定一个径向配点**，这整个系数向量准确为0，当且仅当三个原点残差逐角都为0。这个有限多项式恒等式不要求节点C_U可逆；在另有Q/W/正确正分支条件时才接R647的点态Frenet等价。它不把径向节点/中点的结论扩到整个胞，也不保证存在非圆的有限模准确零解。

M160、602节点时，未知量仍为580328；行数变为：

| 方程组 | 完整行数 |
|---|---:|
| 602节点×962 | 579124 |
| 601实际中点×962 | 578162 |
| 原边界 | 482 |
| 总计 | **1157768** |

相对原580328行增加577440行，正是1203个配点各增加480个先前遗漏的系数。没有通过删变量使它重新方阵化，也没有将原边界行重复加权。

### 不等维Fourier空间的伴随

前一FFT附节的推导保持，但`S_C,D_C`属于2M标量模式输出，`S_Y,D_Y`仍属于M向量模式输入。给定完整权w，使用`eta=S_C D_C w`，仍有

\[
g_Y=D_Y^{-1}P_Y\{-D_\phi(\eta_0V+2k\eta_1d)
                         +D_\phi^2(\eta_1V)\},\qquad
g_U=D_Y^{-1}P_Y\{\eta_0d+\eta_1e+2\eta_2V\}.
\]

权场最高频率4M，乘V/d/e后最高6M。因此源对这种直接全乘积FFT实现要求 **N>12M**：当前2048>1920，最大960低于Nyquist1024。最后仍只取输入空间的频率；不能把输出权先截回M。分部恒等式中的三因子配对最高频率8M=1280，小于2048，准确离散均值与对应角积分一致。原中点四块的转置及BA/BB转置不变，只是输入残差块由482行扩为962行。

实现复用ff65的角jet、真实连接、缓存和完整Hermite前向，明确改动约束投影/权合成、局部输出及梯度尺寸、全局转置的行切片；`factory(base)`返回形状1157768×580328的完整算子。它不能直接冒作旧P.residual的同尺寸替代品：未来消费者须同时使用这个完整残差及相应判据，而不是只换矩阵标签。

### 原1662的一次真实全谱账

新源 `parallel_20261117_implicit_full_spectrum.py` SHA256 `36b979e5c7a825c870addf128c6e39272ff7ebd0ae05284fb4d7780c692ca016`；报告 `parallel-root-implicit-full-spectrum-probe.json` SHA256 `6db382d92644806ad72743441131260fb64ec00e880ac3d3f6830f92d8608361`。原准备报告63c9的身份完整绑定，未重跑求解或旧物理审计。

- 重选原保留行，raw SSE逐位等于已刊初值 `1.5321026127227238e−4`。
- 新增全部577440行的SSE为 `3.855150018530475e−8`。
- 完整谱raw SSE为 `1.5324881277245772e−4`；两部分浮点求和差 `3.34446e−20`，未写成数值零。

| 新增谱组 | 节点SSE | 中点SSE |
|---|---:|---:|
| r0 | 3.18229110105e−10 | 9.46614174791e−11 |
| r1 | 1.74946494143e−8 | 2.05593650187e−8 |
| r2 | 6.45429437408e−11 | 2.00522809814e−11 |

所以初始数据的主误差仍是已保留的中点r1（SSE1.53172995001e−4），不能把初始困难归因于遗漏谱，也不能据这份初账预测后续迭代的谱误差。

一个明定全槽方向的所有1157768行与独立原角jet的complex-step比较，相对L2差 `7.84912956e−14`、最大差 `5.81891306e−16`。完整不等维伴随点积分别为 `−.001713421340802767`、`−.001713421340802601`，绝对差 `1.66037e−16`，相对内积差 `9.69039e−14`。缓存仍177389568 B，实际Jv/Jᵀv耗时.205/.174秒，整个诊断3.102秒、RSS387444 KiB。以上是指定向量的普通浮点核对，不冒全矩阵区间舍入证书。

即使以后这些配点的全部角谱都足够小，真实公共三次/共同C²五次式的胞内导数、完整连续Gram、正确分支、闭合与精化仍须实际支付。本节没有改变物理接受、父身份或课题完成状态。

从仓库根运行，WORK为原输入目录：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_full_spectrum.py \
 --topic topics/visible-flex-larger-amplitude \
 --problem-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_newton.py \
 --warm "$WORK/parallel-hold-m160-short-bvp-warm.json.gz" \
 --polynomial-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_frenet_probe.py \
 --matrix-source topics/visible-flex-larger-amplitude/scripts/parallel_20261117_implicit_matrix_free.py \
 --original-preparation "$WORK/parallel-model-implicit-frenet-602-preparation.json" \
 --out "$WORK/parallel-root-implicit-full-spectrum-probe.json"
```

原warm、Problem、角基与scalar SHA承接前节；新源入口/出口核全部身份。原数组与含计时的报告在仓库外，重跑文件SHA可因计时/路径改变。
