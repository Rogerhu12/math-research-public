# R870：原 Y 有理 Picard 挠差、T7 谱块与可计算的校准整数

日期：2026-11-16。状态：**以下为原层41的完整纸面证明；未执行新数学计算。** 本文不重新编号 YP 已有的连接、主部或 Hecke 校准公式。新增的是：核清原五个整 Picard 点的真实 $\mathbb Q$ 定义域；在原好素数7证明一个准确的单算子挠判；由实际 $T_7$ 谱给出统一挠清除整数和逐谱块的有限 Picard 检验。实际谱仍只消费 R865 的成功产物，不预填任何因子、次数或数值。

始终使用原 $Y=W_{41}$、$g(Y)=127$、$B=J_Y$、$P_i=\phi(c_i)$、$t=a^3$、原主极化 $\lambda_Y$，以及 R791 的五个 $h_j$。本篇的 $T=T_7$ 是 R865 已证明的原 level82 循环7-isogeny对应；不是原 Hom 字中的半线性算子 $T_{\rm Hom}=\rho\sigma$。两者在本文明确区分。

## 1. 被测试的是真实哪五个整点

沿 [R849](R849-certified-original-global-function-and-five-polar-ideal-DAGs.md)、[GP](../notes/R839-original-global-addition-polar-ideals-and-eta-DAG.md)及 [RF](../notes/2026-11-16-original-c0-rigidified-Poincare-fibres-and-theta-section-DAG.md)，置
$$
\begin{gathered}
f=f_4,\qquad g_j=(1+T_{\rm Hom}^j)f,\\
(p_j,q_j)=(165,67),(93,67),(100,67),(168,67),(371,134),\\
\mathscr L_j=
N_{L/K}(I_{E_{g_j}})^{q_j}N_{L/K}(I_{E_f})^{-p_j}
=\mathcal O_Y(-Z_j),\\
\xi_j=[Z_j],\qquad \eta_{h_j}=\xi_j/q_j
\quad\text{于 }B(\mathbb Q)\otimes\mathbb Q .
\end{gathered}
\tag{870.1}
$$
最后一行的定义域将在命题870.1中证明；$\xi_j$ 本身是整 Picard 点，不是任取一个 $q_j$-除点。$q_j$ 不是原商同态 $q$，也不是 Fourier 参数。

本篇实际叶是 R849 原 DAG
R839-global-polar-exact-global-function-and-five-polar-expression-DAG.json.gz
中 five_original_polar_and_eta_outputs[str(j)].eta_degree_zero_fractional_ideal
的 tau、sigma 两分量。图的 SHA256 为
529822ba7ab26beeb06de8aeb466eedd3de63326e019e6b9a041096e554a2e79，
实际来源是 run43790410670、source391191590dcb8bcc6f8f2d777610726fa79dc2a3。
图中 real_descent_degree_zero_fractional_ideal 是另一个真实对象
$$
\mathscr L_j^R=\mathcal R_j\mathscr L_j^3,\qquad
[Z_j^R]=3\xi_j,
\tag{870.2}
$$
不能把它替换成 (870.1)，也不能删除原主函数 $\mathcal R_j$。

### 命题870.1：原五个 $\xi_j$ 确实属于 $B(\mathbb Q)$

**证明。** R616 §1 的 $c_0,c_1$ 为原 $\mathbb Q$ 点，$\phi$ 及 $t=a^3$ 亦在 $\mathbb Q$ 上定义，故 $P_0,P_1\in Y(\mathbb Q)$。先在 $K=\mathbb Q(\zeta)$ 上取 (870.1) 的真实七次范数。它是原 $Y_K$ 的实际 Cartier 除子或嵌入可逆理想，不只是一项数值 Picard 类。

RF §5 保留了原准确共轭关系
$$
c(g_j)=-[\zeta^2]T_{\rm Hom}^{-j}g_j,\qquad
c(g_{R,j})=T_{\rm Hom}^{-j}g_{R,j}.
\tag{870.3}
$$
原 $T_{\rm Hom}$ 以真实 $\sigma$ 和目标缩放运输七个分量；目标缩放及 $-[\zeta^2]$ 均保持 $O$，因而保持对应的极除子。原
$T_{\rm Hom}^7=[\zeta^2]$ 使循环越过第七项时仍保持该极除子。故复共轭仅置换完整七项极除子和，(870.1) 的两项真范数及 $Z_j$ 本身均不变。

这里得到的是 $Y_K$ 上 Cartier 除子的 Galois 不变性，故它下降为 $Y/\mathbb Q$ 上的 Cartier 除子。因 $\deg Z_j=0$，其实际线丛给出 $B(\mathbb Q)$ 中的整点 $\xi_j$；没有 Picard 类不变却未下降的 Brauer 障碍。RF 还给指定帧
$$
e_{0,j}=t^{-7(p_j-q_j)},\qquad e_{1,j}=1
\tag{870.4}
$$
的同一 $\mathbb Q$ 下降。$P_1$ 不在原极支撑中由 R843/R844 保证；在 $P_0$ 使用的是可逆模中的帧，不把负幂当成普通函数的有限值。证毕。

此证明没有声称各个非实 Hom $g_j$ 都在 $\mathbb Q$ 上定义。需要下降的是完整范数除子、可逆理想与帧。因此下面在 $\mathbb F_7$ 上的结论确实用于 $\xi_j$，不需要改成某个未证明的 $\mathbb F_{7^r}$。

## 2. 原曲线在7的好约化和真实 Eichler–Shimura 关系

[R865](R865-original-Hecke-T7-from-certified-level82-Fourier-rows.md)固定原
$$
G=C_3\pmod2\ \times\ N_{\rm ns}\pmod{41},\qquad
H=G\cap\operatorname{SL}_2(\mathbb Z/82\mathbb Z),
\tag{870.5}
$$
及其原 $-3$ 扭曲。原 $G$ 含全部标量矩阵。$T$ 是保持该 $G$-level82 结构并选一个循环7阶子群的八度对应，权二归一没有再除7。

**引理870.2。** 原 $Y$、$B$ 在7处有好约化。在 $\widetilde B/\mathbb F_7$ 上，记 $F$ 为7次幂 Frobenius、$V$ 为 Verschiebung，则原积分对应满足
$$
\widetilde T=F+V,\qquad FV=VF=[7].
\tag{870.6}
$$

**证明。** $7\nmid6\cdot82$。原 prime-to-7 level 模问题的光滑 proper 模型及其粗曲线在7光滑：椭圆点惯性在特征7仅有与7互素的2、3部分；尖点的原 level82 宽度亦与7互素。虽然有限 level 群的总阶可能含7，不能据此假称整个群的阶可逆；其7部分在该光滑覆盖上无固定点，相关局部商仍光滑。亦可在精细辅助水平上作光滑下降。Jacobian 随之为 $\mathbb Z_7$ 上的 abelian scheme。

原 $-3$ 扭曲的局部角色满足 $\chi_{-3}(7)=+1$，且在7未分歧，所以它在 $\mathbb Q_7$ 上平凡。原几何 involution 与循环7-isogeny对应交换，R865 §4 已核其原半线性方向。因此这里没有把全局原 $Y$ 换成另一个未扭曲的曲线。

循环7对应在普通 locus 的两支分别由 Frobenius 和对偶 Frobenius 给出。运输水平结构时，第二支通常保留标量 diamond $\langle7\rangle$；原 $G$ 含 $7I$，所以这个 diamond 在本原商上确为恒等。对 divisor 的 pull-push 因而给 (870.6)。该等式在完整 Jacobian 上成立：普通 locus 的 divisor 可表示任意 Picard 类，或者由对应的 proper 特化与 norm 的相容性直接延拓。特征7的超奇异点不被删去。

这使用的是同一循环对应的模解释；一般 diamond 形式可对照 Hida《Arithmetic of curves》Theorem6.1，而不是把一个 $X_0(N)$ 的计算矩阵移到原 $Y$。证毕。

## 3. 一个奇好素数已经单射全部有理挠

**引理870.3。** 若 abelian variety $A/\mathbb Q$ 在奇素数 $\ell$ 好约化，则
$$
A(\mathbb Q)_{\rm tors}\longrightarrow\widetilde A(\mathbb F_\ell)
\tag{870.7}
$$
单射，包含 $\ell$-primary 挠部分。

**证明。** 只需证明约化核 $A_1(\mathbb Q_\ell)$ 无挠。在原点取光滑整形式参数，核的坐标属于 $\ell\mathbb Z_\ell^g$。以整不变微分归一后的形式对数线性项为恒等。由 R724(724.26)–(724.27) 的沿射线积分，总次数 $n$ 项系数的 $\ell$ 赋值至少 $-v_\ell(n)$。

若 $x\ne0$，置 $a=\min_i v_\ell(x_i)\ge1$。对每个 $n\ge2$，
$na-v_\ell(n)>a$；故对数的某个最小赋值坐标仍以 $x_i$ 为首项，不可能全为零。对数在整个约化核收敛并单射。它将挠点送到特征零加法群的挠点0，所以约化核无挠。证毕。

这里没有要求挠点阶与7互素，也没有使用辅助 $\ell=1000000753$ 的518位点球。此处地方始终是原有理点的 $\mathbb Q_7$ 完成。

**定理870.4：原单算子准确挠判。** 对任意 $R\in B(\mathbb Q)$，
$$
R\text{ 为挠点}\quad\Longleftrightarrow\quad(T-[8])R=0 .
\tag{870.8}
$$

**证明。** 若 $R$ 为挠，$F\bar R=\bar R$ 且 $V\bar R=7\bar R$，故 (870.6) 给
$\overline{(T-[8])R}=0$。该点仍为有理挠点，(870.7) 迫其为0。

反向需要 $T-[8]$ 的核有限。原 Frobenius 的 Weil 特征值为 $\alpha$、
$7/\alpha$，其对应的 $T$ 特征值为
$\alpha+7/\alpha\in[-2\sqrt7,2\sqrt7]$。这不包含8。
因此 $T-[8]$ 在原切空间可逆，是一个真正同源，其核有限。证毕。

(870.8) 是全局群等式判据。把一个有限精度的局部对数算成0，或只检验一个剩余域点，均不是它的成功出口。

## 4. 由已成谱直接求真实的挠清除整数

设 R865 的准确成功产物为
$$
\chi_7(X)=\det(XI-T\mid H^0(Y,\Omega^1))
       =\prod_{i=1}^{r}f_i(X)^{m_i},
\qquad
m_7(X)=\prod_{i=1}^{r}f_i(X).
\tag{870.9}
$$
各 $f_i$ 为实际首一不可约整多项式。R865 的 Rosati 对称性已经给最小多项式恰为 $m_7$。本篇不重算127矩阵、特征多项式、分解或 CRT。

**命题870.5。** 原 Frobenius 多项式及约化点数为
$$
P_F(U)=U^{127}\chi_7(U+7/U),\qquad
\#\widetilde B(\mathbb F_7)=\chi_7(8).
\tag{870.10}
$$
特别地
$$
N_{\rm full}=\chi_7(8)>0,\qquad
N_0=m_7(8)>0
\tag{870.11}
$$
均杀掉 $B(\mathbb Q)_{\rm tors}$。

**证明。** $T$ 在一阶 Betti/Tate 空间上的特征多项式为 $\chi_7^2$。极化 Weil 配对将 $F$ 特征值配为 $\alpha,7/\alpha$，每对具有同一个 $T$ 特征值 $\alpha+7/\alpha$。故 (870.10) 的第一式成立。这里使用配对；单靠二次方程 $F^2-TF+7=0$ 不足以推出每个二维块的迹、行列式。

$1-F$ 为可分同源，核恰为 $\widetilde B(\mathbb F_7)$，所以其次数等于
$P_F(1)=\chi_7(8)$。这给 $N_{\rm full}$。又有准确整系数除法
$$
m_7(X)=(X-8)Q_0(X)+N_0,\qquad Q_0\in\mathbb Z[X].
\tag{870.12}
$$
在任一有理挠点上，$m_7(T)=0$ 与 (870.8) 给 $[N_0]R=0$。所有
$f_i$ 的根均小于8，故各 $f_i(8)>0$，从而 $N_0>0$。证毕。

因此，一旦真正的 $e=e_\eta$ 已识别并取实际 $d$ 使
$f=de\in\operatorname{End}_{\mathbb Q}(B)$，YP 中的
$(f-d)\xi_j$ 是有理挠点，直接有
$$
N_0(f-d)\xi_j=0\quad(j=1,\ldots,5).
\tag{870.13}
$$
这关闭了 YP.24 中统一整数 $N$ 的来源，可合法取 $N=N_0$；
不要求再猜五个挠差的最小阶，也不改变 $q_j,\kappa$ 或原极化。
此结论**不先验识别 $e_\eta$**，也不自动产生 YP.26 的具体主函数与规范纤维标量。

## 5. 实际每个 T7 谱块的有限 Picard 条件

令 R865 已成 CRT 多项式为 $E_i\in\mathbb Q[X]$，
$E_i\equiv1\bmod f_i$、$E_i\equiv0\bmod f_k$（$k\ne i$）。
保留原清分母 $d_i>0$ 和
$$
P_i=d_iE_i\in\mathbb Z[X],\qquad
n_i=f_i(8)>0,\qquad
A_i(X)=(X-8)P_i(X).
\tag{870.14}
$$
这是原真实对应的整数复合，不要求先展开一张新的127阶投影矩阵。
因 $f_iP_i$ 被首一 $m_7$ 整除，已有
$f_i(T)P_i(T)=0$ 于 $\operatorname{End}_{\mathbb Q}(B)$。

**命题870.6。** 对每个 $i,j$，以下三项等价：
$$
\begin{aligned}
E_i(T)\eta_{h_j}=0&\quad\text{于 }B(\mathbb Q)\otimes\mathbb Q,\\
A_i(T)\xi_j&=0\quad\text{于 }B(\mathbb Q),\\
[n_i]P_i(T)\xi_j&=0\quad\text{于 }B(\mathbb Q).
\end{aligned}
\tag{870.15}
$$

**证明。** 第一项等价于 $R=P_i(T)\xi_j$ 是挠点；正整数 $d_iq_j$ 不影响有理张量中的零性。第二项与其等价由 (870.8)。对该挠点，将
$f_i(X)=(X-8)Q_i(X)+n_i$ 代入，并使用
$f_i(T)R=0$，得到 $[n_i]R=0$。反向若非零整数杀掉 $R$，它当然为挠。证毕。

故识别一个单 $T_7$ 谱块在五方向上是否全 inactive，只需五个明确整 Picard 等式。没有把五次零对数或五个模素数零值当成这些等式。

### 5.1 对应怎样准确作用原两个理想

令 $\mathcal C_7$ 为原循环7对应的正规化，$a,b:\mathcal C_7\to Y$ 为原源、靶两映射。取与 R865 pull-push 一致的方向，定义
$$
\mathcal H(\mathscr L)=\operatorname{Nm}_b(a^*\mathscr L).
\tag{870.16}
$$
其 Picard 作用为 $T$；由于原对应自伴，若先采用另一方向，须同时用其规范对偶同构，而不能只换一个 Fourier Galois 指数。这里 norm 是有限平坦可逆模的行列式 norm，保分歧长度、剩余域次数与原 scalar diamond。它不是随意对几条生成函数各取 norm 后的理想。

对整多项式 $A(X)=\sum_r a_rX^r$，从原两图理想定义
$$
\mathcal H_A(\mathscr L_j)=
\bigotimes_r\mathcal H^r(\mathscr L_j)^{\otimes a_r}.
\tag{870.17}
$$
负系数用可逆模对偶。它的类为 $-A(T)\xi_j$，度数为0。因此
$$
A_i(T)\xi_j=0
\quad\Longleftrightarrow\quad
\dim_{\mathbb Q}H^0\!\left(Y,\mathcal H_{A_i}(\mathscr L_j)\right)=1.
\tag{870.18}
$$
维数只可能0或1：度零线丛的非零全局截面零除子为0，故必处处生成。
完整 RR 核为0才是这一 Picard 非零的准确证书；一个有限截断未找到截面不是证书。

实际消费者可选择 (870.18) 或 $A=n_iP_i$ 的等价版本，按已成有限对应的真实大小择小。这里保留未约化的 $A_i$；将多项式 mod $m_7$ 约化虽不改变 Jacobian 同态，却可能改变具体 divisor 代表，需要附带原主函数比较才能运输帧，不能默默删掉。

现有 R849 只已经给 $\mathscr L_j$ 的完整表达式；R868 的 $P_0$ 单极生成元和128维 RR 入口可供后继求解，但没有给 (870.17) 的 Hecke norm 矩阵或 (870.18) 的新核。本篇最小新算术不声称完成这些未算数据。

## 6. 从主元到原 YP 校准函数的方向

设某个后继已经准确证明两个原嵌入度零理想满足
$$
\mathscr A\otimes\mathscr B^{-1}=h\,\mathcal O_Y,
\qquad h\in\mathbb Q(Y)^\times .
\tag{870.19}
$$
它可能是 (870.18) 的实际主元，也可能是 YP.26 的实际 tensor 差。
必须保两图全部理想包含相等，而不只比较度数或模值。
设 $e_{\mathscr A,\nu},e_{\mathscr B,\nu}$ 为 $P_\nu$ 处实际帧，置
$$
c_\nu=\left.
\frac{h}{e_{\mathscr A,\nu}/e_{\mathscr B,\nu}}
\right|_{P_\nu}\ne0 .
\tag{870.20}
$$
即使 $h$ 在 $P_\nu$ 有零极，该帧比仍是非零单位值。乘 $h$ 的方向为
$\mathscr B\to\mathscr A$；故沿 $P_0$ 刚性化后，从 $\mathscr A$ 到 $\mathscr B$ 的规范同构是乘 $c_0/h$，其 $P_1$ 纤维标量为
$$
c_0/c_1 .
\tag{870.21}
$$
对原 $\mathscr A=\mathscr L_j^R$、$\mathscr B=\mathscr L_j^3$、
$h=\mathcal R_j$，(870.20) 给 $c_0=\kappa_j$、
$c_1=\mathcal R_j(P_1)$，恰恢复 RF 的
$\kappa_j/\mathcal R_j(P_1)$。这是一次方向校验；没有重新计算六个范数、
$\kappa_j$、原比较点或733节点。

对真正选定的 YP $f,d,N_0$，(870.13) 保证规范 Picard 同构存在。
要得到具体 (870.21)，仍须消费其真实 principal 比较函数、指定原帧和 norm
纤维；不能把 torsion 杀掉之后的主函数常数设置为1。
非 $p$ 项继续由同一有理纤维在全部地方求值，不能逐因子宣布为零。

## 7. 哪些实际谱信息足以确定原活跃投影

单 $T_7$ 的谱投影只按 $f_i$ 分组。若不同完整 adelic Hecke 等型部分在7有同一个因子，它们仍落在同一个 $E_i$ 块里。命题870.6 的五项全零证明整个粗块 inactive；至少一项非零只证明粗块内有活跃部分，不能自动把整个粗块命名为 $e_\eta$ 的分量。

一个无需第二算子的**充分分离条件**是：实际每个 $f_i$ 在 $\chi_7$ 中的重数 $m_i=1$。更一般地，可逐块适用该条件。证明如下：不分歧中心算子 $T_7$ 保持原完整 Hecke 等型分解；一个非零有理等型子块的切空间维数至少 $\deg f_i$，因为它带有域 $\mathbb Q[X]/(f_i)$ 作用。$E_i$ 全块维数恰为 $m_i\deg f_i$，所以 $m_i=1$ 时不能再分成两个非零有理等型子块，也不能含同一 simple 因子的多个拷贝。于是该块是一个完整等型块。这里用的是原 GL2-type 与完整 adelic Hecke 分解，不从一个随机矩阵的不可约多项式推任意几何 simple 性。

在这些真正分离的块上，若 (870.15) 已实际判完，令 $S$ 为至少一个原方向非零的块集，则
$$
e_\eta=\sum_{i\in S}E_i(T).
\tag{870.22}
$$
若仍有 $m_i>1$ 的未分离块，证书必须把它们列为 unresolved，而不是猜其内部支持。是否需要另一个原算子，等真实谱后才决定。

R865 的实际 $d_i$ 也直接给一个统一整化倍数
$$
d_*=\operatorname{lcm}_i d_i,\qquad d_*E_i\in\mathbb Z[X].
\tag{870.23}
$$
故任何由已证块构成的投影和都可取真整数 $d=d_*$。这是一个可用、未声称最小的对应分母，不是 R862 的 $E_A$ 分母；原 $E_A\phi^*=0$，绝不能拿它替代 YP 的 $e_\eta$。

## 8. 第一项真正新算术的最小消费契约

R870 首消费者只读取：

1. 实际成功 R865 的配置、最终证书、准确 $\chi_7$、不同因子和各 CRT
   $E_i,d_i,P_i$，以及这些项的原 bytes/SHA/source 闭包；
2. R849/R850 已成的五个 $\mathscr L_j$、原 $\mathbb Q$ 下降和帧的小来源。
   首 scope 只保实际读取的小 DAG、证书与来源 metadata，不为尚未执行的 norm-RR
   续传395MB旧载体；未来真正物化理想时再从当时活跃的已绑定来源取得必要闭包。

新算术只做整多项式求值、整除和有理系数最小公倍数：
$$
\chi_7(8),\quad m_7(8),\quad f_i(8),\quad
Q_0=\frac{m_7-m_7(8)}{X-8},\quad
Q_i=\frac{f_i-f_i(8)}{X-8},\quad
d_*,\quad A_i=(X-8)P_i .
\tag{870.24}
$$
全部恒等式逐系数准确乘回，因子和 CRT 只读原结果不重新分解。
同时输出 (870.17) 的有限对应/原理想引用计划，保 $j,p_j,q_j$、
$\xi_j=-[\mathscr L_j]$、两个实际帧、原 norm 与 $\mathbb Q$ 定义域。
这个有限小任务是真正的 $N$ 与可执行 Picard 检验输入生产者，不是再次生成127阶矩阵。

成功字段分别为 rational_torsion_annihilator_certified、
T7_minus_8_exact_torsion_test_certified、
uniform_spectral_integer_correspondence_denominator_certified 均为 true；
而 actual_eta_active_support_computed、
actual_YP_e_eta_selected、
actual_principal_comparison_functions_computed、
actual_non_p_local_heights_computed、
actual_original_height_computed 均为 false。

只有未来 (870.15)/(870.18) 的真实结果才能变更支持字段；只有实际主函数及 (870.20)
才能变更校准字段。原 $T_7$ 未成功时不造 run/artifact/谱 pins。
后继所有新算术只在本公开仓库 Actions，沿同 source/tag 原子续接；
机器回执、向量、矩阵仅在一日 active artifact/carrier 中续传。
Git 只放源码、参数、纸面证明与简明 run/SHA 登记。

## 文献与原来源

- H. Hida, *Arithmetic of Curves* (2011), [§6.1, Theorem6.1](https://www.math.ucla.edu/~hida/207b.1.12w/Lec12w.pdf)：Eichler–Shimura 的完整 diamond 形式。本文已单独核原标量 diamond 与 $-3$ 扭曲。
- K. Ribet and W. Stein, *Lectures on Modular Forms and Hecke Operators* (2011),
  [Theorem12.6.4、§12.7、Proposition12.7.1](https://www.wstein.org/books/ribet-stein/marked_up/2011-10-06-ch6.pdf)：对应特化、Weil 配对及特征多项式在 $\ell+1$ 的点数解释。
- 原 R616 §1、R791、R843/R844、GP/R849、RF §§1–6：同一五个 Cartier 除子、
  原 $\mathbb Q$ 下降、极化与实际帧；不以辅助定义域单一地方替代。
- 原 R724 §§3、8 与 YP §§6–7：活跃完整 Hecke 部分、形式对数全尾以及
  真实 $d,N$、刚性化和全部非 $p$ 校准；本篇只把其中明确的整数/挠判接缝向前推进。
