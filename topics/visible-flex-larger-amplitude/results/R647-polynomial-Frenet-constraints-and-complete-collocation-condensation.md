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
