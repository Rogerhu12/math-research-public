# R465：保名义因子与回代缺陷的全列切向预收缩

作者：ChatGPT（AI；exact_refinement）。日期：2026-11-16。

**可信度：已证明（下述明确的准确实线性系统及其恒等式）；尚无新科学执行、浮点误差界或实测加速。** 本文区分原成功分支的准确实程序、把实际保存字词作为系数的线性系统，以及195真正执行的浮点方向循环。三者不能因公式相似而混称。新收缩保全部225 Gram矩、224方向、226状态、双mean与原最终责任，不改已发表195、207。

## 465.1 实际阻点与本节的最小对象

[R412](R412-actual195-finite-root-tangent-resource-partial-before-positive-current-J.md) 原195在18000秒停止：零高度请求已返回，首个正高度尚未返回完整current J，异常落在 differentiatedOriginalSolve 的期限检查。没有原native试步或R273校正可用来检验新方向质量。

实际 kernel 为 geometry_20261115_original64_finite_trace_variation.mjs，11427B，SHA742ab15a2168084167eeab9879a074ee1cd586d33f324e837223134a8cbf9705；flow SHAa7a90668a7d2f4df93e0bd03d665f439dab2fb2461bedf544725cd01c2a7b470，loader SHA55b2a4a344ae2eb7d78f26b7954b20f9cbe4e4969588bf3a236e7828d6f299ae，均属于source4ad7fb771218585af1091c9d322c9d61b64a949c。下面只针对其中一次**实际接受的局部root更新**已有的factor/forward/solution字词。

记root维数$J=M+1$、Gram矩数$B=2M+1=2J-1$、方向数$K=2M$。本次$M=112,J=113,B=225,K=224$。用$R$记实际保存的lower Cholesky factor，$z$记原forward向量，$s$记原backsolve输出。$F$与$C$分别为原residual和独立Gram对象；不假定$C=F_L$。

原195已按批形成全部224方向；fromCaptured不重跑原primal root/RHS。因此本节不是“免去224次primal求根”。目标是免去每个方向都形成完整$J\times J$因子方向张量，并减少该段的准确实操作结构。全部有限角求和、flux、RK及物理返回仍须支付。

## 465.2 三层对象和不能省略的区别

**第一层：一致的准确实执行。** 固定原成功trace，按原有限公式在准确实数中执行时，若Cholesky存在，
$$
RR^T=C,\qquad Rz=F,\qquad R^Ts=z.
$$
[R305](R305-literal-gram-root-contraction-and-nominal-factor-defects.md)已证明这时
$$
ds=C^{-1}\bigl(dF-(dC)s\bigr).
$$
该式不要求root最终残差为零，但要求这一准确实factor/solve图的一致性。

**第二层：名义系数线性系统。** 现在只固定实际tape里各有限字词代表的实数$R,z,s$。对于给定输入方向$f$及$\gamma\in\mathbb R^B$，令$D=\sum_k\gamma_k T_k$，定义未知量$X,u,v$满足
$$
\begin{aligned}
XR^T+RX^T&=D,\qquad X\text{为lower},\\
Xz+Ru&=f,\\
X^Ts+R^Tv&=u.
\end{aligned}\tag{1}
$$
这里$T_k$是原Gram组装对第$k$矩的准确结构系数，下一节逐项给出。只要求$R$的对角非零；原成功Cholesky还给正对角。(1)有唯一解。

这正是195的因子方向、forward方向及backsolve方向公式在**保留原名义系数、把方向算术解释为准确实运算**时的线性系统。它不要求已保存的$R,z,s$满足第一层等式，也没有从某个很小的数值残差推断其导数为零。本节预收缩的精确目标是(1)。

**第三层：实际浮点方向循环。** 195对(1)的各项再作binary64乘加除；所得$\widehat X,\widehat u,\widehat v$一般不准确满足(1)。新预收缩也将产生另一组舍入。准确实等价不推出逐字相等、相同误差、FD已过、邻域分支不变或IEEE roundmap导数存在。§465.8把这些方向缺陷全部写出。

名义系统(1)是一个明确的系数对象，而不是把一般光滑程序的未知缺陷导数擅自设零。下一节同时给它的一个准确实局部实现，说明此区别。

## 465.3 一般缺陷恒等式与名义系统的局部实现

沿任意光滑矩阵/向量族定义
$$
E=RR^T-C,\qquad a=Rz-F,\qquad b=R^Ts-z,\qquad H=RR^T=C+E.
$$
直接相乘有
$$
Cs-F=a+Rb-Es.
$$
因此
$$
\boxed{
H\,ds=dF-(dC)s+da+(dR)b+R\,db-(dE)s.
}\tag{2}
$$
这是[R305 §305.6](R305-literal-gram-root-contraction-and-nominal-factor-defects.md)的原缺陷恒等式，全部符号保留。没有理由从某一点$E,a,b$小或为零，推出$dE,da,db$小或为零。

(1)的合法解释不是对上述任意族作这种推断。固定名义点$R_0,z_0,s_0,C_0,F_0$，按准确实乘积定义$E_0,a_0,b_0$。对于输入$f,D$，在充分小的$\epsilon$上明确构造
$$
\begin{aligned}
C_\epsilon&=C_0+\epsilon D,&F_\epsilon&=F_0+\epsilon f,\\
R_\epsilon&=\operatorname{chol}(C_\epsilon+E_0),\\
z_\epsilon&=R_\epsilon^{-1}(F_\epsilon+a_0),\\
s_\epsilon&=R_\epsilon^{-T}(z_\epsilon+b_0).
\end{aligned}\tag{3}
$$
因为$C_0+E_0=R_0R_0^T$正定，连续性保证充分小邻域中的Cholesky存在。正对角唯一性给$R_{\epsilon=0}=R_0$，其余两式在零处也恰好恢复$z_0,s_0$。微分(3)得到(1)。

在这个**明确定义的局部实现**中，$E_0,a_0,b_0$是固定参数，故相应导数按定义为零。此事实没有宣称原浮点程序输入改变时，其真实形成缺陷恒定；(3)也不替换原primal求值。它只给名义系数线性系统的一个精确解释。195的方向代码在准确实方向算术中的方程与(3)的微分相同，实际浮点误差仍另付。

特别地，下面的收缩保$H=RR^T$而不是把它冒成$C$，保实际$b=R^Ts-z$；$a$的值已通过实际$z,s$参与名义系数。任意光滑族的$da$仍留在(2)，未被静默删除。

## 465.4 完整225个Gram结构矩阵

设原literal平方根字词为$\sigma_2$，各Gram矩为$\beta_0,\ldots,\beta_{2M}$。原组装是
$$
C_{00}=1+\beta_0,\qquad
C_{i0}=C_{0i}=\sigma_2\beta_i\quad(i\ge1),
$$
$$
C_{ij}=\delta_{ij}+\beta_{|i-j|}+\beta_{i+j}
\quad(i,j\ge1).
$$
定义$T_k=\partial C/\partial\beta_k$。于是$T_0=I$；对于$k\ge1$，
$$
(T_k)_{00}=0,\qquad
(T_k)_{0i}=(T_k)_{i0}=\sigma_2\mathbf1_{i=k},
$$
$$
(T_k)_{ij}=\mathbf1_{|i-j|=k}+\mathbf1_{i+j=k}
\quad(i,j\ge1).
$$
第一行/列指示在$i\le M$时才有贡献，$k$范围始终是$0,\ldots,2M$。因此
$$
D=dC=\sum_{k=0}^{2M}T_k\,d\beta_k.\tag{4}
$$

这里保原gramCos所有225列；每个$d\beta_k$仍由完整有限角和及原$b_n$表达式得到。不能用存储的$c_{ni}c_{nj}$重建$g_{n,i\pm j}$；独立舍入的literal表不保证这种准确恒等式。本收缩只使用组装索引，没有使用三角函数乘积等式。

定义$S_s\in\mathbb R^{J\times B}$满足
$$
S_s\gamma=\left(\sum_k\gamma_kT_k\right)s.
$$
其原结构展开为
$$
(S_s\gamma)_0=\gamma_0s_0+\sum_{j=1}^M\sigma_2\gamma_js_j,
$$
$$
(S_s\gamma)_i=\sigma_2\gamma_is_0+
\sum_{j=1}^M(\gamma_{|i-j|}+\gamma_{i+j})s_j
\quad(i\ge1).\tag{5}
$$
对角的$\gamma_0$和$\gamma_{2i}$都在；最大下标恰为$2M$，没有截去最后Gram矩。

## 465.5 Cholesky方向的唯一显式形式

令$A=R^{-1}$。对称矩阵$K_0$的$\Phi(K_0)$定义为：严格下三角保持原项、对角取一半、严格上三角置零。则
$$
\Phi(K_0)+\Phi(K_0)^T=K_0.
$$

**引理。** 对称$D$下，(1)第一式的唯一lower解是
$$
X=R\,\Phi(ADA^T).\tag{6}
$$

**证明。** 左乘$A$、右乘$A^T$，令$Y=AX$。两矩阵均lower，故$Y$也是lower。方程变为$Y+Y^T=ADA^T$；对称性逐项唯一确定$Y=\Phi(ADA^T)$，再乘$R$即得(6)。反向代入也成立。证明没有用$C=RR^T$。证毕。

逐条展开(1)第一式的lower项，正是195的
$$
X_{ii}=
\frac{D_{ii}-\sum_{k<i}(X_{ik}R_{ik}+R_{ik}X_{ik})}{2R_{ii}},
$$
$$
X_{ij}=
\frac{D_{ij}-\sum_{k<j}(X_{ik}R_{jk}+R_{ik}X_{jk})-R_{ij}X_{jj}}
{R_{jj}}
\quad(i>j).
$$
这里把方向运算解释为准确实数，不能利用此等价断言重新分组的binary64乘加相同。两次代回也逐项对应(1)第二、三式，故本引理确实对应已读原函数的全部行/列，没有另挑一个隐式J作为目标。

## 465.6 只收缩需要的backsolve缺陷作用

记
$$
b=R^Ts-z.
$$
用$a_i=A^Te_i$表示$A$第$i$行的转置，并令
$$
v_i=\sum_{j<i}b_j a_j+\tfrac12b_i a_i.
$$
定义一次预装配矩阵
$$
Q_{ik}=a_i^T T_k v_i,\qquad
0\le i\le M,\quad0\le k\le2M.\tag{7}
$$

**定理。** 对任意$\gamma\in\mathbb R^B$，令$D=\sum_kT_k\gamma_k$，$X$为(6)，则
$$
Xb=RQ\gamma.\tag{8}
$$

**证明。** 设$K_0=ADA^T$。逐行展开，
$$
(\Phi(K_0)b)_i
=\sum_{j<i}a_i^TD a_j\,b_j+\tfrac12a_i^TD a_i\,b_i
=a_i^TDv_i.
$$
代入(4)，即为$\sum_kQ_{ik}\gamma_k$。由(6)乘$R$得(8)。上三角没有被遗漏：$D$本身对称，(6)正是唯一lower方向；$\Phi$的半对角是所需的准确系数。证毕。

这一步不形成全部$X$，但保留它对真实$b$的全部作用。若$b$恰为准确零，$Q=0$；若只是很小、或普通浮点点积给出零，不能据此把准确$b$改为零。

## 465.7 全方向的最终收缩与复杂度

由(1)和$R^Ts=z+b$，
$$
\begin{aligned}
Ds
&=(XR^T+RX^T)s\\
&=X(z+b)+R(u-R^Tv)\\
&=f+Xb-Hv.
\end{aligned}
$$
代入(5)、(8)，得到
$$
\boxed{
v=H^{-1}\bigl[f-\Gamma\gamma\bigr],\qquad
\Gamma=S_s-RQ,\qquad H=RR^T.
}\tag{9}
$$
$H^{-1}$用实际$R$的两次三角代回评价，不用$C^{-1}$，不重新分解当前$C$。$RQ$前的负号属于$\Gamma$；最终右端因此保留$+RQ\gamma$。

对全部$K$方向，若原输入矩阵分别为$f\in\mathbb R^{J\times K}$、$\gamma\in\mathbb R^{B\times K}$，同一个$R,z,s$只预装配一次$\Gamma$，应用
$$
V=R^{-T}R^{-1}(f-\Gamma\gamma).\tag{10}
$$
全部224列仍在；没有低秩截断、列抽样或只保三个active方向。

### 不用三角表乘积的预装配

$A$为lower，所以$a_i$和$v_i$均只在$0,\ldots,i$有支持。对固定$i$，下面的系数汇总恰实现(7)：

1. 把$a_{i,0}v_{i,0}$加入$Q_{i,0}$。
2. 对$j=1,\ldots,i$，把$\sigma_2(a_{i,0}v_{i,j}+a_{i,j}v_{i,0})$加入$Q_{i,j}$。
3. 对$r,s=1,\ldots,i$，把$a_{i,r}v_{i,s}$分别加入$Q_{i,|r-s|}$与$Q_{i,r+s}$。
4. 形成下一行之前，把$b_i a_i$加入前缀向量$\sum_{j\le i}b_j a_j$。

第3步使用所有有序$(r,s)$对；不能只取一半而忘补对称权。$r=s$给$Q_{i,0}$及$Q_{i,2r}$两项；第零行/列由步骤1、2单独处理，不能再混入第3步。全过程只用原literal$\sigma_2$和整数索引。

形成$A$需要$O(J^3)$；上述各行的双循环总量为$O(\sum_i i^2)=O(J^3)$。形成$S_s$为$O(J^2)$，$RQ$为$O(J^2B)=O(J^3)$。随后全部$K$列的矩阵作用及两次代回为$O(J^2K)$。额外预装配内存为$O(J^2)$，不再需要195的$J^2K$方向因子张量。

因此被替换的factor/solve部分从$O(J^3K)$变为
$$
O(J^3+J^2K).
$$
这只是准确实操作结构。没有以此推断实际运行秒数、峰值内存或一个job完成全部576段。原角向投影、flux/RK矩阵作用和exact defect形成的实际费用仍在。

## 465.8 一般缺陷导数和浮点方向缺陷完整保留

对于§465.3的一般光滑族，由
$$
dR=R\Phi\!\left(A(dC+dE)A^T\right)
$$
及(2)，可把完整方向写为
$$
\boxed{
H\,ds=dF-\Gamma\,d\beta+
da+R\,db-(dE)s+
R\Phi(A(dE)A^T)b.
}\tag{11}
$$
$\Gamma$由当前名义$R,z,s$构成，(11)保有$dE,da,db$及它们全部必要作用。若$dE$不是原225结构的组合，最后一项不能用(7)的225列表冒充完成。

式(9)与(11)的关系现在明确：对名义系数系统(1)，方向方程本身指定$dE=da=db=0$；对任意实际光滑误差族或实际浮点计算，这些项不自动为零。不能用本节宣称R305的缺陷问题被普遍消除。

特别地，设195实际浮点输出为$\widehat X,\widehat u,\widehat v$，把这些保存数字当实数，**按准确实乘积定义**方向方程缺陷
$$
\begin{aligned}
\varepsilon_E&=\widehat X R^T+R\widehat X^T-D,\\
\varepsilon_a&=\widehat Xz+R\widehat u-f,\\
\varepsilon_b&=\widehat X^Ts+R^T\widehat v-\widehat u.
\end{aligned}
$$
令$v^\circ$为(9)的准确解。线性代数给出
$$
\boxed{
H(\widehat v-v^\circ)
=\varepsilon_a+R\varepsilon_b-\varepsilon_Es
 +R\Phi(A\varepsilon_E A^T)b.
}\tag{12}
$$
这是通过原浮点方向数组定义的精确恒等式；没有假定三个$\varepsilon$小。

新实现若产生$v_{\rm new}$，定义其对(9)的总形成残差
$$
\nu=Hv_{\rm new}-(f-\Gamma\gamma).
$$
则
$$
H(v_{\rm new}-\widehat v)
=\nu-\varepsilon_a-R\varepsilon_b+\varepsilon_Es
 -R\Phi(A\varepsilon_EA^T)b.\tag{13}
$$
新预装配中的近似逆、$b$投影、$Q/\Gamma$形成、矩阵乘和两次代回误差都属于$\nu$，不能把它们只记成最后一次三角solve误差。

(12)、(13)不要求后继为通过原native门另算完整旧方向或作对拍。它们说明为何仅凭名义因子缺陷小、公式等价或一个普通浮点残差，就不能宣称新旧逐字相等或方向误差已控制。若以后需要严格界，可用真实外包的$\nu,\varepsilon$及可证逆界支付；本节不预付该证书，也不新设它为科学前门。

## 465.9 实际字词残差如何进入实现

原tape的$R,z,s$均为binary64字词。数学上的$b=R^Ts-z$应解释为这些字词所代表实数的**准确有限点积差**。先用普通binary64点积再把得到的零称为准确$b=0$，会重新丢掉本节保留的项。

一个明确可实现的选择是：在Actions内逐字拆为符号、整数尾数与二进制指数，准确累积每个$b_i$的有限dyadic和，然后以明确尺度/舍入策略转入预装配。只有整数累积确实为零，才能记exact_backsolve_defect_zero=true。该做法不需要原数学模型重算，也不恢复旧被删tape；它消费同一当前接受更新的真实三份向量/因子。

数值实现必须另外声明：

- 若将非零准确$b_i$投影为binary64，投影误差及可能下溢不等于准确缺陷为零。
- 可以保二幂尺度或更宽的方向算术；它们都必须给独立数值来源，不能把转换隐藏在原195标签后。
- 若具体实现采用原逐因子算法作为有限表示失败时的内部回退，要保存真实原因/计数，不能在资源到期后反复回退，也不能把回退当新数学接受条件。
- $R^{-1}$与$\Gamma$的形成只影响切向数值实现；不允许把这些近似结果写回原factor、原$z,s$、primal、worker last或缓存。

第一项与(12)、(13)共同界定误差责任。本文没有选择未来运行的精度、实测阈值或新的root预算，也没有执行这些整数/浮点科学运算。

## 465.10 与195原函数的逐项接点

原kernel的精确接口是 differentiatedOriginalSolve(point, dr, dbeta, tables, dims)。其中：

| 实际字段 | 本文对象 | 原尺寸 |
|---|---|---|
| point.solve.factor | $R$，row-major lower | $J^2$ |
| point.solve.forward | $z$ | $J$ |
| point.solve.solution | $s$ | $J$ |
| dr | 全部$f$列 | $JK$ |
| dbeta | 全部$\gamma$列，moment-major | $BK$ |
| tables.sq2 | 原literal$\sigma_2$ | 一个字词 |
| dims.J/K/M | 原完整维数 | $113/224/112$ |

原loader已经在不改solve数值语句的观察点保存factor、forward、solution；接受更新还保存原L、e、res、backtrack、alpha。不需要为此重算原primal或另选root，也不需要新增科学输入。

最小独立源码变更应限于：

1. 新增一个独立factor-contraction helper，输入上述同一tape与方向矩阵，输出同形状的$J\times K$方向；实现明确的defect形成、原结构预装配和两回代。
2. 从195 kernel独立派生，只替换该factor/solve函数及其来源/schema；residualAndGramDirection、initialDirection、原接受alpha、全225矩、splitRhsDirection及最后dL更新保原责任。
3. 新flow/loader独立身份只绑定该新kernel/helper，不改原noJ RK/body、原root的接受/拒绝和最终338行定义。
4. 新client/hook/入口更新实际source closure与有限统计，保当前完整H请求、当前withJ→R273→原noJ试步→FD/fullDN/fresh audit原链。现195和207保持冻结。
5. 根trace无接受更新时仍直接使用原target方向；不为预装配构造不存在的factor。全224结果形成完成前不提交新dL；资源异常保实际stage/raw地址和未付范围。

这里给的是可落实的切点，不把尚未派生的source称为已可运行，更不替未来request选择父/参数/run。全图接线完成前不能仅把一个helper登记成新的current J。

## 465.11 全root、RK、means与物理端口责任

对每次实际成功root的有限接受序列，保原$\alpha_i=2^{-k_i}$和
$$
dL_{i+1}=dL_i-\alpha_i\,ds_i.
$$
当前切向改变只作用于(1)的数值求解实现；原root停止检查、原trial分支、原primal括号及全部字词仍由原程序生成。非成功root不凭收缩公式制造切向。

对固定的实际tape，原角向导数输入与名义factor系数组成线性映射；将每一步(1)替换成准确等价的(9)，逐步归纳保全部返回方向。在实际binary64中，重新分组导致的差异要按前述数值范围另记，不能从该归纳推出逐字一致。

原RHS两mean行仍分别为$r_xwL_0$的完整shape方向与$r_xw$的零shape方向；后者保为完整行。新source不能删mean、减到223列、截掉第225个Gram矩，或把root vector113与shape224混为一维数。完整每段仍为226×224、577节点/576stage，Pi端口原缩放也保留。

最终112高度到338行边界响应中，一阶行来自该新切向，原second/mean-second等有限差分责任仍须实际执行；没有把全部338行冒成解析/严格J。原全129248残差行、原sigma、R273 eta、native32×10、严格下降、D/S/A、2e-9、fullDN/FD及最后物理audit均不由本推导改变。

## 465.12 资源结论和本节没有支付的事项

R412的零高度计数27772次root全部零更新；其实际5063.5455199240005秒中没有非零接受更新的factor方向循环。故本节不能声称会消除这部分已见成本。原195首正高度累计包含28383次完成的接受更新方向，但没有函数级计时；不能把全部12912.70058027秒指定为本函数独占。

本节只严格证明：对指定名义系数系统，可以以$O(J^3+J^2K)$预收缩替代$O(J^3K)$的factor方向形成，并保全部原Gram结构及backsolve缺陷作用。真实性能还取决于准确defect形成、预装配条件数、角求和、RK传播、运行时与当前root更新数。没有6小时完成保证，也没有用局部代数结果补填195未完成的正高度J。

本文不含本地模型求值、编译、AST、fixture、独立对拍或新Actions计算。后继需要新的明确source/schema和真实当前tape；已刊195、207以及其他正在运行的source不改变。

## 来源

- [R305：literal Gram收缩与名义分解缺陷](R305-literal-gram-root-contraction-and-nominal-factor-defects.md)，最终13673B，SHA26ebd720353f32114ef3eee62e9c98a3bed615f00ef372a3227e3a132aa13d8c；§305.6是一般缺陷导数的直接来源。
- [R411：原binary64成功trace及逐循环切向](R411-original64-finite-root-trace-matched-variation-and-full-return.md)，12390B，SHA1d66947d6d02b1dac50aa6348e94b56c959336fa1ca52b1ee1450bd6b6ec342c。
- [R412：actual195实际资源部分范围](R412-actual195-finite-root-tangent-resource-partial-before-positive-current-J.md)，run43771125613；本节只使用已记录执行范围，不复用其已清现场。
- 原195完整recipe/request/流程与两个mean、全338返回合同见其[完整接口](../notes/2026-11-15-request195-original64-finite-trace-r273-complete112-interface.md)。
