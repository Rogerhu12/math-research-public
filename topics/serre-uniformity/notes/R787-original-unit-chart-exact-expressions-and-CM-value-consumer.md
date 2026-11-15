# 原 R787 单位选行块：精确表达式、518 位点值收缩与准确接受接口

日期：2026-11-15。状态：**本篇证明精确表达式的原函数身份，并给出不重做旧提升的实际消费契约；尚未运行新的 CM 收缩，没有预填原点的十四个展开坐标。**

原映射始终为第4号 $f_4$，次数1206，$f_4(c_0)=O$，原目标为
$C:y^2=x^3+b$。使用 [R786](../results/R786-original-power5-sections-and-129-Laurent-recovery.md)、
[R787 方法](R787-original-power5-relation-solver-method.md)、
[R824 实际维数](../results/R824-certified-original-pole-module-splitting-from-Schur-minor.md)、
[R790](../results/R790-certified-original-CM-fiber-jets.md) 和
[R792](../results/R792-original-beta-composition-and-Galois-cube-root.md) 的同一字段、基顺序、原 CM 点 $P_1$ 与相位。

本篇区分三类完成状态：精确的有限行列式表达式；该表达式在实际辅助素数幂下的值；已经由独立准确证书接受的十四个有理坐标。前两类不自动变成第三类。已有 R792/R809 的展开坐标接口不能仅换一个来源 SHA 就读取本篇的新表达式。

## 1. 原全部行、常数核和字段

记
$$
L=\mathbb Q(B_{\rm fld},s),\qquad B_{\rm fld}=\lambda b,
\qquad s^2=-3,\qquad t=\xi_{41}+\xi_{41}^{-1}.
\tag{U1}
$$
原坐标顺序仍为 $B_{\rm fld}^i s^j$，$j=0,1$ 外层、$0\le i<7$。
$\lambda$、原首一七次多项式、原 $t$ 多项式及其嵌入均逐项读取原 R781/R787 字段描述，不改为另一扭曲或另一实根。

令 $F\in\operatorname{Mat}_{2580\times1234}(\mathbb Z)$ 为旧原
`R787-real-power5-row-0000..1233.json.gz` 给出的矩阵。每个基截面已经包含一次 $82^{10}$；行按 $v^n t^r$，$0\le n\le128$、$0\le r<20$ 排列，$v=\xi^{-10}q_Y$。原相位和 $t$ 下降已在旧完成阶段认证，不重算。

原 rational-blocks 中的20个常数主元列、1214个自由列和准确整数零空间给
$$
Z\in\operatorname{Mat}_{1234\times1214}(\mathbb Z),\quad
Z_P=-U,\quad Z_Q=dI,\quad E_0Z=0,
\tag{U2}
$$
其中 $d>0$ 且在原辅助素数处为单位。$Z$ 的输入是原已存整数行和对角尺度，不能以模素数零空间替代。

以 $G=FZ$ 记分母展开，所以 $G_0=0$。原 Laurent 源为
$$
Y(v)=v y(v)=-\frac1{246^3}\sum_{m=0}^{128}R_m\kappa^{-(m+1)}v^m.
\tag{U3}
$$
定义 $C\in\operatorname{Mat}_{2560\times1214}(L)$：先将 $G\mathbf c$ 与 $Y$ 相乘，取 $v^1,\ldots,v^{128}$，再逐阶取20个 $t$ 坐标。$F_A$ 是 $F$ 的前2560行。于是原关系为
$$
F_A\mathbf a-C\mathbf c=0,\qquad \mathbf b=Z\mathbf c.
\tag{U4}
$$
本篇的129个原条件恰是 Laurent 指数 $-1,\ldots,127$。$m=0$ 已由 (U2) 准确消去，其余 $m=1,\ldots,128$ 就是 (U4)。不多加不存在的 $A$ 的 $v^{128}$ 条件，也不删掉 $B$ 的 $v^{128}$。

与原无逆递推一致，全部清行形式为
$$
246^3\kappa^{m+1}A_{m-1}
+\sum_{j=0}^m R_{m-j}\kappa^jB_j=0\quad(0\le m\le128),\qquad A_{-1}=0.
\tag{U5}
$$
每阶是 $L(t)$ 中一条等式，即20个 $L$ 坐标、280个有理坐标。乘 $\kappa^{m+1}$ 在20个 $t$ 坐标间一般混合。因此不能沿用原未清矩阵的个别选行，直接把它们替换为同编号的清行矩阵行。本篇始终用原未清 (U4) 定义选行块；(U5) 只作与旧完整源的等价说明。

## 2. 一个真正可逆的2420阶原 L 块

原实际 chart 与 rational-blocks 给：

- $J$：原 $F_A$ 的1234个行号，$F_0=F_A[J]$；
- $R$：其余1326个行号，保持原保存顺序；
- $I$：原 Schur 矩阵的1186个主元行号；
- $P_S$：其1186个主元列号；
- $Q_S$：其余28列，原规范自由列 $f=1186\in Q_S$。

所有行列号读取原实际文件，不重新选主元。令有序行集
$\mathcal J=(J,R[I])$，并置
$$
M=\bigl[F_A[\mathcal J]\ \ -C[\mathcal J,P_S]\bigr]
\in\operatorname{Mat}_{2420}(L),\qquad
r_f=C[\mathcal J,f].
\tag{U6}
$$
原 Schur 矩阵是 $S=C[R]-F_A[R]F_0^{-1}C[J]$，故
$$
\det M=\det(F_0)\det(-S[I,P_S]).
\tag{U7}
$$
这里1186为偶数，但实现仍保列顺序及负号，不能用符号约定偷换原右端。

原实际素数为 $\ell=1000000753$。branch0 的
$(B_{\rm fld},s)=(3197390,99932770)$；已成常数20阶、$F_0$ 的1234阶、Schur 的1186阶子式分别为
$322380492,336446771,296007862\pmod\ell$。原 selection 已核原所有分母、$246\lambda$ 及 $\kappa$ 可约化且为单位。于是 (U7) 在原 $L$ 中非零。原全部14个分支也有同一原 chart 的单位性；后继使用整体 $\ell$ 进坐标时仍须消费该完整来源。

**命题 U.1（无展开的精确原函数关系）。** 以
$$
x_f=M^{-1}r_f=\frac{\operatorname{adj}(M)r_f}{\det M}
\tag{U8}
$$
定义前1234个坐标 $\mathbf a_f$ 与后1186个坐标 $(\mathbf c_f)_{P_S}$，并设
$(\mathbf c_f)_f=1$、其他27个自由坐标为0。令 $\mathbf b_f=Z\mathbf c_f$。这些是原 $L$ 中唯一的准确坐标，并满足原全部129阶、每阶280个有理坐标条件，因此
$$
A_f=yB_f,\qquad B_f\ne0.
\tag{U9}
$$

证明：R786 的零点计数已把完整 (U4) 的核准确识别为
$H^0(5H-E)$。R824 的真实非零 Schur 子式与 Riemann--Roch 合并，已证明该空间的维数恰为28。选行系统的核也恰为28，因为 (U6) 可逆，全部28个自由坐标可任取。完整核包含在选行核中，二者维数相同，故相等。令自由坐标为指定标准向量便得 (U8)–(U9)。由于 $Z$ 单射且指定自由值为1，$B_f\ne0$。证毕。

这使用的是已证明的完整核维数和一个真实单位子式，不是宣称“某个选行解通过全部行”的一般规则。没有求出或伪称已经存有 $F_0^{-1}$ 的有理展开；旧 `A_inverse_over_Q_computed=False` 仍然准确。

同一论证对全部28个 $f\in Q_S$ 成立，给整个 $H^0(5H-E)$ 的准确表达式基。它不声称全部28个大有理向量已经数值展开，也不替代原正在运行的各个展开坐标生产者。

## 3. 来源绑定的表达式格式与可执行操作

表达式不是一个无法读取的“存在解”标签。最小描述明确保存：

| 节点 | 输入与实际含义 |
|---|---|
| `original_field` | 原字段完整描述及 R781 field 文件 SHA；$B_{\rm fld}=\lambda b,s^2=-3$ |
| `original_F_rows` | 原1234个完成文件及其129×20 shape、原顺序、整数尺度 |
| `constant_kernel` | 原 $P,Q,U,d$ 文件，按 (U2) 定义 $Z$ |
| `original_Laurent_operator` | 原 $R_0..R_{128},\kappa^0..\kappa^{129}$、(U3) 和完整约化规则 |
| `unit_chart_solve` | 原 $J,R,I,P_S,Q_S$、free列1186、(U6) 的符号、原非零子式来源 |
| `linear_response` | 一个准确 $L$ 行 $\ell$ 与常数 $c$，表示 $c+\ell x_f$ |
| `bordered_determinant` | 明确矩阵 $\begin{psmallmatrix}M&r_f\\-\ell&c\end{psmallmatrix}$；与 `linear_response` 的关系见(U10) |

原矩阵条目按 (U2)–(U4) 的有限加乘、原字段取逆和 $t$ 多项式约化计算，不依赖未知几何模型或新的 Laurent 尾。可按需产生行块而不先展开2420²个大系数。原单位子式是 `unit_chart_solve` 的非零分母证明。

准确恒等式为
$$
\Delta(\ell,c):=\det\begin{pmatrix}M&r_f\\-\ell&c\end{pmatrix}
=\det M\,(c+\ell M^{-1}r_f).
\tag{U10}
$$
因此该格式支持有明确定义的有限算法：精确有理/数域行列式展开；按合法素点或素数幂评价；以及合并两个共享 $M,r_f$ 的线性响应。第一种若尚未执行就不写展开坐标标志，第二种只给实际精度，第三种不重建旧关系。

对当前第1186方向，已有完整 current 给其素数幂评价，无需执行新的矩阵求逆或 Dixon 迭代。对尚无 current 的其他自由方向，不能从一个已成方向推得其数值；可以复用已成 R824 模核作为模 $\ell$ 的实际值，或保持精确表达式。

## 4. 原 CM 点值只是四个准确线性响应

R790 给每个原 M2 基的
$$
\widehat\psi_i=82^2 T_iE_6/E_4^2,
\quad (\widehat\psi_i(P_1),\widehat\psi_i'(P_1)),
\quad z=a-1.
\tag{U11}
$$
逐 R775 原 power2–5 recipe，使用
$(v,d)(w,e)=(vw,dw+ve)$，合成原1234个五次基的值行 $e_0$ 和一阶行 $e_1$，均在 $K=\mathbb Q(s)$ 中。它们已经带 $82^{10}$，不再乘 $82^{10}$、$246^3$、$\kappa$ 或 cusp 相位。相同非消失局部平凡化用于分子、分母。

对 $j=0,1$ 定义
$$
\ell_{A,j}=(e_j,0),\quad c_{A,j}=0;
\qquad
\ell_{B,j}=(0,(e_jZ)_{P_S}),\quad c_{B,j}=(e_jZ)_f.
\tag{U12}
$$
令 $A_j=c_{A,j}+\ell_{A,j}x_f$、$B_j=c_{B,j}+\ell_{B,j}x_f$。
若有真实合法约化证明 $B_0\ne0$，则准确的原有限值已经由
$$
y(P_1)=\frac{\Delta(\ell_{A,0},0)}{\Delta(\ell_{B,0},c_{B,0})}
\tag{U13}
$$
定义；分母非零来自该实际约化见证。该表达式是原 $L$ 中的具体值，但其十四个有理坐标尚不因此算出。

同理，
$$
y'_z(P_1)=\frac{A_1B_0-A_0B_1}{B_0^2}.
\tag{U14}
$$
若只得到模 $\ell$ 的 $B_0=0$，不能称特征零有共同零，也不能称点为 $O$。任何 $A_0=B_0=0$ 的准确分支必须由准确表达式零证书或原完整局部代数证明，然后才可使用 R792 的一阶/更高阶分支。

原 R790 两坐标是 $a+d\zeta$，转换到本篇 $1,s$ 时是
$(a-d/2)+(d/2)s$。本初次收缩始终留在原积分 $B_{\rm fld},s$ 基中，不先将518位大坐标乘 $\lambda^i$；最后若确有展开的有理坐标输出到 R792，再仅施一次 $B_{\rm fld}=\lambda b$ 与 $s=1+2\zeta$。

## 5. 直接消费真实518 current的最小算术

实际完成文件为 `R787-prime-1000000753-dixon-00000518.json.gz`，
73180954 bytes，SHA256
`4997a05b79ab9e7c7f9286fc483b1f459ff6e23fa18df5344bd8ef0eb80f10f5`。
其字段是1234×14的 `A_L_coordinates`、1214×14的 `C_L_coordinates`、
`digits=518`、同原 chart SHA、原完整模关系标志。应由实际已结束 run/source/core/manifest 链消费，不能只钉这个单文件而忽略原来源。

置 $M_\ell=\ell^{518}$。由原全14分支单位 chart，(U8) 有同一 $\ell$ 进整解；旧完整提升的唯一性说明当前坐标就是它模 $M_\ell$ 的值。
新算术只需：

1. 核所有原 CM 有理分母在 $\ell$ 处为单位；合成 $e_0,e_1$ 的准确 $K$ 值及其模 $M_\ell$ 值。已经完成的 recipe 乘积若有同源输出可直接复用。
2. 用准确稀疏 $Z$ 恢复当前 $\mathbf b=Z\mathbf c\bmod M_\ell$；或先把 $e_j$ 收缩成 $e_jZ$，二者只能选一种实际路径，不能都重复做。
3. 计算四个长度1234/1214的点值收缩，得到 $A_0,A_1,B_0,B_1\bmod M_\ell$，每个仅14个原积分坐标。保存真实来源、原 normalized free coordinate、原尺度和新收缩结果。
4. 在原14个模 $\ell$ 分支逐一评价 $B_0$。任一非零值已证明特征零 $B_0\ne0$；全部14个非零才给整体 $\mathcal O/M_\ell$ 中的单位性。
5. 全部14个分支为单位时，先在模 $\ell$ 求出标量环逆，再作 $u\leftarrow u(2-B_0u)$ 的逐步倍精度 Newton 提升；每步准确乘回，直到518。这里只是一个14维交换代数元素的逆，不是新建大矩阵逆或原 Dixon 方向。
6. 输出 $y_0=A_0/B_0$ 以及可选 $y'_0$ 的14个模 $M_\ell$ 坐标。若部分分支不为单位，初次实现只保各分支实际情况和合法的非零见证，不伪造完整精度的整体商。
7. 可对14个模坐标作一次有理重构建议。任何得到的有理14元组仍是 `candidate`；下一节的准确出口未通过以前，不能送入原 R792 成功分支。

原正确点可能比整条2420长解的共同分母小得多，但本篇没有高度定理保证518位足够。也不将共轭对称、椭圆曲线方程或高精度吻合独自用作原点身份认证。

## 6. 展开点值的准确接受只有两个明确出口

设重构建议为 $q\in L$，并记
$$
\ell_q=\ell_{A,0}-q\ell_{B,0},\qquad c_q=-q c_{B,0}.
\tag{U15}
$$
在已有 $B_0\ne0$ 的前提下，$q=y(P_1)$ 当且仅当以下任一准确证书成立。

### 6.1 原 L 的 bordered determinant 零证书

准确计算并验证 $\Delta(\ell_q,c_q)=0$。这可以由分数自由消元或原字段行列式算法产生；完整原表达式语义、所有尺度及符号都已由 (U1)–(U12) 固定。
仅在一个或多个有限素数处为零不够；若采用模整数算法，必须有实际的准确重构/高度界及全部原字段坐标认证。

### 6.2 一个可乘回的行空间证书

给出真正准确的 $u\in L^{2420}$，逐坐标认证
$$
u^TM=\ell_q,
\qquad u^Tr_f+c_q=0.
\tag{U16}
$$
由 $Mx_f=r_f$ 立刻得到 (U15) 的响应为0。这只需最终乘回，不要求对全部原关系向量作数值展开。但 $u$ 也不能仅是模向量或未认证重构。若 $u$ 自己仍以精确 solve-expression 保存，第二条必须有独立准确零证书，不能把同一个未知等式换一种写法后宣布完成。

两种出口都是确定的可执行任务，成本应由实际输入测定，不能预称比旧1186提升便宜。初次最小消费者只做第5节、建立 (U13) 的源绑定表达式及真实非零见证；其状态分清 `exact_expression_defined`、`modular_value_computed`、`expanded_coordinates_exactly_certified`。

## 7. 全部300条权六的真正隐式特征零来源

同一方法适用于原 R824 权六系统。旧准确基有1506列、142阶，准确常数核有1486列，原 A 选行1506个，剩余1314行；真实 Schur rank1186。原
$$
\deg(6H-E)=426>2g-2=252,\qquad h^0(6H-E)=300
\tag{U17}
$$
给完整核维数。于是原2692×2692选行块对300个标准自由右端分别定义整个 $H^0(6H-E)$ 的准确 $L$ 基。原全部142阶判据仍通过“完整核包含、维数相同”保证；若消费其数值模方向，必须读取已完成的 R824 原 branch/profile，不能从五次方向凭空补出六次方向。

因为 $\deg(6H-E-P)=425>252$ 对每个点成立，完整线性系统无基点。故这些真正的300个隐式分母作为 $V_6$ 截面，所生成的理想层恰为 $\mathcal O(-E)$。这一步比一个带未知残余零的单独 $B$ 更强，但仍不宣称300个展开向量已算。

这给 R836 的 $T'_m$ 一个合法特征零起点：可对这些具体表达式作原规范导数、乘法和两图齐次化，所生成的截面身份由表达式和几何公式证明，而不是由模标签猜测。随后若想把一个模核提升为新的准确 RR 空间，仍须具备准确包含和维数夹逼；一个模核维数本身不能自动给特征零核的下界。原 R836 的295维/567维出口保持不变。

## 8. 首次执行的实际源闭包与产物边界

首次公开 Actions 的最小来源为：

| 来源 | 必须消费的完成文件 |
|---|---|
| 已结束的原518 run | 原 full manifest、run/core/input、当前518文件、原 chart/selection；同原93d3核心及原配置 |
| 原 R787 载体 | 原 rational-blocks 的准确 $Z$ 和选行；原 R786 cert/index；原 R781 field及选行表达式所需 $R/\kappa$ 来源 |
| 原 R790 成功源 | cert、stage manifest、146个准确 CM 行及各原 recipe 身份 |
| 原 R775 续传源 | 原 M2/power2–5 recipe 文件，与 R786/R790 曾用文件逐 SHA 相同 |

若仅做数值 CM 收缩，1234个旧 q 展开大行不必再次读入内存；精确表达式描述仍钉其原 index/manifest 和原全部行来源。后继真正求行列式/行空间证书时，必须从仍活跃载体恢复这些实际原行，而不是用摘要重造数据。

建议独立结果类型 `R787-original-implicit-CM-value`，而非伪装成旧 `actual_y_map_recovered` 的展开 recipe。阶段为 `source-chart`、`CM-basis-values`、`CM-contraction`、`denominator-unit-witness`、`implicit-point-expression`、可选 `point-coordinate-candidate`，以及将来实际运行的 `exact-point-acceptance`。每阶段有完整源配置与原子完成标志，预算只影响运行，不改变数学身份。

机器结果至少明确：原 $f_4$、次数1206、原 free1186、原129/280完整关系由命题U.1保证的方式、实际518而非新提升、原积分字段、是否全14分支单位、实际商精度、是否已有独立准确点坐标证书。没有完整证书时不填 $x_0$、不宣称 $\beta_A$ 的核前像、η 或高度已算。

源码、参数、纸面证明及简明运行/SHA登记可入Git；机器回执、原行、表达式 DAG 的可重算展开、向量、矩阵及模点值只在一日 active artifact/carrier 中续传。
