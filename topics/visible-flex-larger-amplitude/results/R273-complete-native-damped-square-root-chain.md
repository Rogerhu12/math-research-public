# R273：原 native 完整块链的阻尼平方根最小二乘及原无穷范数接受的区别

分类：已证明，有限实数组条件定理；作者：ChatGPT（exact_refinement / root）；日期：2026-11-14。

## 273.1 结论、对象与范围

本结果给出一个**有限实数组问题的完整条件定理**：原 cut、全部 shooting stage 和原 far 行，在原 sigma 权重下加入正的方向阻尼后，可以沿块链作正交消元，得到完整平方根因子及唯一最小二乘方向。无需形成正规矩阵，也无需 Riccati 图的显式逆。每个节点的正则项恰加入一次；消元产生的纯常数残差完整保留。

同时证明：该方向非零时严格降低线性模型的二范数平方，但这不能推出原无穷范数下降，也不能推出原 nonlinear guards 通过。后续仍必须使用原真实非线性试步。这里没有选择本题的阻尼参数，没有实现新求解器，没有运行数值，也没有给原接受流程增加线性缺陷门。

本定理的实际对应输入是 `exact_20261114_rawcell0_direct_ld_system.py` 定义的独立有限矩阵：1372 个 stage、每节点 224 个原 Q/Pi 变量、112 个非零模式；868 个新 direct-LD 后一次 cast 的原坐标 binary64 块和 504 个原 actual28 块。所有已存 base、残差、cut、far、H、sigma 和原 577 节点映射保持。**定理不假定这些保存的 Jacobian 是精确非线性导数。**

原实现的具体接受依据见公开冻结源码 [78718-tail-tangent-core.mjs](../../visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs) 中 `scaleFor`、`evaluate` 和 `solve`。原 cut 行除以 `scales[0]`；stage $n$ 的全部 shape 行除以 `scales[n]`；far 行除以 `scales[depth]`。原十个试步为 $2^{-k}$，$k=0,\ldots,9$，成功求值后要求 `test.norm < ev.norm`。调用者的原 tolerance、root/branch guards 以及之后的完整 J/audit 均不由本结果改变。源码口径另见 [R266](R266-native-block-Newton-defect-and-original-scaled-descent.md)。

## 273.2 原权重下的完整有限方程

令 $M\ge1$、$K=2M$、$D\ge1$。每个节点的方向为

$$
\delta_n=(\delta_{n,Q},\delta_{n,\Pi})\in\mathbb R^K,
\qquad n=0,\ldots,D.
$$

给定有限实矩阵 $J_n\in\mathbb R^{K\times K}$、stage 残差 $r_n\in\mathbb R^K$、cut 残差 $r_c\in\mathbb R^M$、far 残差 $r_f\in\mathbb R^M$，以及原 far 对角矩阵 $G\in\mathbb R^{M\times M}$。所有数可以是保存的有限 binary64 字节所指定的精确实数；不把显示十进制重新定义为另一对象。

定义 $\mathcal A\delta+r$ 的行序和含义如下。

| 行块 | 方向项 | 已存残差 | 原分母 |
|---|---|---|---|
| cut，$M$ 行 | $[I_M\ \ 0]\delta_0$ | $r_c$ | $\sigma_0$ |
| stage $n$，$K$ 行 | $J_n\delta_{n+1}-\delta_n$ | $r_n$ | $\sigma_n$ |
| far，$M$ 行 | $[-G\ \ I_M]\delta_D$ | $r_f$ | $\sigma_D$ |

全部 $\sigma_n$ 都是原定义给定的正有限实数。原 576 段实现中它们由 `scaleFor` 的实际字节给出；扩展系统在新增节点复用原 parent stage 的 sigma，并在原 577 节点保持原字节。不得把一个模态的 gain 换成另一模态，也不得把原端口已经付过的 Pi 除法再施一次。

令 $W$ 为上表逐行分母的倒数对角矩阵，$N=(D+1)K$。cut 与 far 各 $M$ 行，因此完整原方程共有

$$
DK+2M=(D+1)K=N
$$

行。选定正可逆对角块 $T_n\in\mathbb R^{K\times K}$，记 $T=\operatorname{diag}(T_0,\ldots,T_D)$，并置

$$
\delta=Tz,\qquad A=W\mathcal AT,\qquad \rho=Wr.
\tag{273.1}
$$

$T$ 是明确的方向坐标选择，不改变目标 H 或原方程。一个可用的纯代数选项为 $T_n=\sigma_n I_K$，即 $z_n=\delta_n/\sigma_n$；这时 cut、far 的同节点尺度可精确约消，stage 的左块为 $-I_K$，右块为 $J_n\sigma_{n+1}/\sigma_n$。这里的等式指精确实数组模型；具体浮点形成误差留至 §273.8 单独记录。

对任意给定 $\eta>0$，定义

$$
m_\eta(z)=\frac12\|Az+\rho\|_2^2+
                 \frac{\eta^2}{2}\sum_{n=0}^D\|z_n\|_2^2.
\tag{273.2}
$$

阻尼只用于选择方向。其正则项不进入原 nonlinear residual，也不修改最终原方程或原 tolerance。尤其，允许模型在 cut/far 行上有非零线性余量，不等于改变原 cut H 或 far 图；实际 nonlinear 读回仍逐行检查同一目标。

## 273.3 定理：严格凸性、唯一性与方向大小

**定理 273-A。** 在 §273.2 的条件下，$m_\eta$ 有唯一极小点 $z_\eta$。令

$$
H_\eta=A^TA+\eta^2I_N,\qquad g=A^T\rho.
$$

则

$$
H_\eta\succeq\eta^2I_N,
\qquad H_\eta z_\eta=-g,
\qquad \|z_\eta\|_2\le\frac{\|\rho\|_2}{\eta}.
\tag{273.3}
$$

这些是数学恒等式，不要求算法显式形成 $A^TA$。

**证明。** 对任意非零 $v$，

$$
v^TH_\eta v=\|Av\|_2^2+\eta^2\|v\|_2^2
             \ge\eta^2\|v\|_2^2>0.
$$

故目标严格凸且强制增长，有唯一临界点，也是唯一全局极小点。其一阶条件给出 (273.3) 的线性方程。又因 $m_\eta(z_\eta)\le m_\eta(0)=\|\rho\|_2^2/2$，舍去非负的残差平方即得方向大小界。证毕。

该界不保证原非线性域合法，也不表示任意很大的 $\eta$ 都能让原无穷范数下降。$T$ 很大或原域余量很小时，原坐标方向 $Tz_\eta$ 仍需实际检验；§273.7 甚至给出任意 $\eta>0$ 都无无穷范数下降的精确线性反例。

## 273.4 完整平方根 front，不丢纯常数余量

用下列块写 (273.2) 的仿射残差：

$$
C=\frac{[I_M\ \ 0]T_0}{\sigma_0},\quad c=\frac{r_c}{\sigma_0},
$$

$$
L_n=-\frac{T_n}{\sigma_n},\quad
V_n=\frac{J_nT_{n+1}}{\sigma_n},\quad
b_n=\frac{r_n}{\sigma_n},
$$

$$
F=\frac{[-G\ \ I_M]T_D}{\sigma_D},\quad f=\frac{r_f}{\sigma_D}.
\tag{273.4}
$$

stage 残差就是 $L_nz_n+V_nz_{n+1}+b_n$。

从 carry $(P_0,c_0)=(C,c)$ 和常数能量 $\kappa_0=0$ 开始。处理 stage $n<D$ 时，将下列完整 front 的列按 $(z_n,z_{n+1},1)$ 排列：

$$
\mathcal F_n=
\begin{bmatrix}
P_n&0&c_n\\
\eta I_K&0&0\\
L_n&V_n&b_n
\end{bmatrix}.
\tag{273.5}
$$

第一项是以前全部行压缩后的 carry，第二项是节点 $n$ **唯一一次**加入的正则项，第三项是原完整 stage 的全部 $K$ 行。第一步是 $M+2K$ 行；此后是 $3K$ 行。

对当前节点的前 $K$ 列作完整正交 QR，并把同一个左正交变换施于 next 块和仿射列。得到

$$
Q_n^T\mathcal F_n=
\begin{bmatrix}
R_n&S_n&a_n\\
0&\widehat P_{n+1}&\widehat c_{n+1}
\end{bmatrix},
\tag{273.6}
$$

其中 $R_n$ 是可逆的 $K\times K$ 上三角块。下半部仍有 next 节点列；不能直接丢掉。对它再作一个完整正交压缩：

$$
\widehat Q_n^T
\begin{bmatrix}\widehat P_{n+1}&\widehat c_{n+1}\end{bmatrix}
=
\begin{bmatrix}P_{n+1}&c_{n+1}\\0&d_n\end{bmatrix}.
\tag{273.7}
$$

保留 $K\times K$ 的 $P_{n+1}$ 和 $K$ 维 $c_{n+1}$；同时保存纯常数向量 $d_n$，或保存可追溯的完整向量及其平方和账，并令

$$
\kappa_{n+1}=\kappa_n+\|d_n\|_2^2.
\tag{273.8}
$$

$P_{n+1}$ 可以秩亏。这里不逆它，不删秩，不加额外 ridge；它只是保全剩余残差能量的 carry。第一段的 $d_0$ 有 $M$ 行，以后的 $d_n$ 有 $K$ 行。

最后一个节点 $D$ 没有后续 stage。使用完整 front

$$
\mathcal F_D=
\begin{bmatrix}
P_D&c_D\\
\eta I_K&0\\
F&f
\end{bmatrix},
\tag{273.9}
$$

加入节点 $D$ **唯一一次**的正则项，以及原 far 的全部 $M$ 行。正交 QR 给出

$$
Q_D^T\mathcal F_D=
\begin{bmatrix}R_D&a_D\\0&d_D\end{bmatrix},
\qquad \kappa=\kappa_D+\|d_D\|_2^2.
\tag{273.10}
$$

最后 $d_D$ 有 $K+M$ 行。整个过程中，cut 仅在初始 carry 出现一次，far 仅在最后 front 出现一次，全部 $D$ 个 stage 各一次，全部 $D+1$ 个 $\eta I_K$ 各一次。

## 273.5 完整能量不变量、满秩与回代

**定理 273-B。** 按 (273.5)–(273.10) 作精确正交变换，存在上块双对角可逆矩阵

$$
\mathcal R=
\begin{bmatrix}
R_0&S_0&&&\\
&R_1&S_1&&\\
&&\ddots&\ddots&\\
&&&R_{D-1}&S_{D-1}\\
&&&&R_D
\end{bmatrix},
\qquad a=(a_0,\ldots,a_D),
$$

使对每个完整 $z$ 都有

$$
2m_\eta(z)
=\sum_{n=0}^{D-1}\|R_nz_n+S_nz_{n+1}+a_n\|_2^2
 +\|R_Dz_D+a_D\|_2^2+\kappa
=\|\mathcal Rz+a\|_2^2+\kappa.
\tag{273.11}
$$

因此

$$
\mathcal R^T\mathcal R=A^TA+\eta^2I_N,
\quad \mathcal R^Ta=A^T\rho,
\quad \|a\|_2^2+\kappa=\|\rho\|_2^2.
\tag{273.12}
$$

每个 $R_n$ 的精确最小奇异值至少为 $\eta$，而唯一最小方向由以下单次块回代给出：

$$
z_D=-R_D^{-1}a_D,
\qquad
z_n=-R_n^{-1}(S_nz_{n+1}+a_n),\quad n=D-1,\ldots,0.
\tag{273.13}
$$

这里的逆符号表示三角解，不要求形成逆矩阵。最小模型值为 $m_\eta(z_\eta)=\kappa/2$。

**证明。** 初始 carry 完整表示 cut 残差平方。假设此前已处理部分可以表示为已保存的 $R_i,S_i,a_i$ 平方项、$\|P_nz_n+c_n\|_2^2$ 和常数 $\kappa_n$。将当前 node 正则项和 stage 项加入后，它们的和恰为 $\|\mathcal F_n(z_n,z_{n+1},1)^T\|_2^2$。正交变换 (273.6) 保范数，分离已消元节点平方项与剩余 next 残差；第二次正交变换 (273.7) 又保范数，给出新的 carry 和纯常数 $\|d_n\|^2$。这证明逐步不变量。最后按 (273.9) 加原 far 和最后一个正则项，(273.10) 同样保范数，得 (273.11)。比较两边关于 $z$ 的二次、一次、常数项即得 (273.12)。

当前 front 前 $K$ 列的块为 $[P_n^T\ \eta I_K\ L_n^T]^T$；任何 $v\in\mathbb R^K$ 在这些列上的平方范数至少为 $\eta^2\|v\|_2^2$。以前的消元不会移除这个下界，因为节点 $n$ 的独立 $\eta I_K$ 行在此时才加入，而且在别的变量列上全为零。正交 QR 保持这个列 Gram，故 $R_n^TR_n\succeq\eta^2I_K$。最后 front 对同样的独立 $\eta I_K$ 行完全相同。因各 $R_n$ 可逆，上块三角 $\mathcal R$ 可逆。(273.13) 使全部可变平方项为零，并由定理 273-A 得到唯一极小点和最小值。证毕。

**常数项不能用差数代替。** 实现宜累计各 $\|d_n\|^2$ 的原向量证据；不通过两个可能很接近的大数 $\|\rho\|^2-\|a\|^2$ 相减来定义最小残差。若只要方向，纯常数项不会改变最小点；但丢掉它会改变完整目标值、模型下降和同模型比较，所以这里仍要求保全。

**不形成正规矩阵。** (273.12) 是用于证明的恒等式。算法只对局部 front 作正交变换和三角回代。可选的任意 $H_\eta^{-1}b$ 也可用一次 $\mathcal R^T$ 解和一次 $\mathcal R$ 解获得，无需形成 $A^TA$ 或用相减的 Schur complement；这不是本结果要求立即实现的额外功能。

## 273.6 完整模型的下降与截停后验

将一阶条件与 $z_\eta$ 内积，得到

$$
\rho^TAz_\eta
=-\|Az_\eta\|_2^2-\eta^2\|z_\eta\|_2^2.
\tag{273.14}
$$

若 $z_\eta\ne0$，右侧严格为负。对任意 $0<\alpha\le2$，

$$
\|\rho+\alpha Az_\eta\|_2^2-\|\rho\|_2^2
=-\alpha(2-\alpha)\|Az_\eta\|_2^2
  -2\alpha\eta^2\|z_\eta\|_2^2<0.
\tag{273.15}
$$

这同时给出线性残差平方的严格下降，而不只是含正则项的目标下降。若 $z_\eta=0$，则恰有 $A^T\rho=0$，此定理不许报告非零下降方向。

对实际未精确完成的 $z$，定义**同一个完整模型**的 stationarity residual

$$
q= A^T(Az+\rho)+\eta^2z.
$$

则由 $q=H_\eta(z-z_\eta)$，

$$
\|z-z_\eta\|_2\le\frac{\|q\|_2}{\eta^2},
\qquad
m_\eta(z)-m_\eta(z_\eta)
=\frac12q^TH_\eta^{-1}q
\le\frac{\|q\|_2^2}{2\eta^2}.
\tag{273.16}
$$

证明只用定理 273-A 的谱下界。此式与 [R263](R263-projected-KKT-and-damped-model-error.md)、[R267](R267-two-point-damped-model-posterior-bound.md) 的后验思想一致，但不能把预条件坐标中的小 residual 冒成本式的完整 $q$。也不能把模型误差界冒成原 nonlinear acceptance。

有限截停方向仍应保存实际全模型的 $Az$、$\rho^TAz$、正则项和完整 residual；若没有证实真实二范数下降，不得仅凭 QR 返回、局部 $R_n$ 可逆或某一三角 residual 小而宣称下降。反之，这些模型诊断不成为禁止原 trial 的额外科学门：原 trial 自己判断同一方向是否有效。

## 273.7 二范数下降不推出原无穷范数下降

**反例 273-C。** 取一维变量、两个残差行：

$$
A=\begin{bmatrix}1\\-2\end{bmatrix},
\qquad \rho=\begin{bmatrix}1\\9/10\end{bmatrix},
\qquad \eta>0.
$$

有 $A^T\rho=-4/5$、$A^TA=5$，因此唯一阻尼方向为

$$
z_\eta=\frac{4}{5(5+\eta^2)}>0.
$$

它满足 (273.14)–(273.15) 的严格二范数下降，但对每个 $\alpha>0$，第一残差为 $1+\alpha z_\eta>1$，所以

$$
\|\rho+\alpha Az_\eta\|_\infty
\ge1+\alpha z_\eta>1=\|\rho\|_\infty.
\tag{273.17}
$$

因而不存在可降低该无穷范数的正试步，任意增大 $\eta$ 也不能改掉这个符号事实。该反例否定从“严格二范数下降”直接推出“原无穷范数下降”的一般推论；它不是对本题当前实际 1372 矩阵的数值描述。

更一般地，若 $R=\|\rho\|_\infty>0$，对固定方向 $d$ 有

$$
\left.\frac{d}{d\alpha}\right|_{\alpha=0+}
\|\rho+\alpha d\|_\infty
=\max_{i:\,|\rho_i|=R}\operatorname{sgn}(\rho_i)d_i.
\tag{273.18}
$$

**证明。** 非活跃行有严格有限间隙，在充分小正 $\alpha$ 内不会超过所有活跃行；每个活跃行在同一充分小区间保持非零原符号，其绝对值为 $R+\alpha\operatorname{sgn}(\rho_i)d_i$。对有限个这样的仿射函数取最大，得到 (273.18)。证毕。

右侧严格负时，仿射无穷范数在某个正小区间下降；这个区间未必包含原程序有限十个试步中的任一个。右侧不严格负也不能仅凭二范数判断真实非线性结果。这里不据该式选新阈值或更换原十步。

## 273.8 三层对象、浮点形成与原 nonlinear 读回

必须分别记录以下对象。

1. **给定有限数组的精确模型。** $J,r,G,\sigma,T,\eta$ 的字节指定实数；(273.1)–(273.18) 对这个模型成立。实际 $1/\sigma$ 一般不是 dyadic，不能把一次 binary64 除法的结果默认为精确权重。
2. **实现形成与分解的有限数组。** 具体 floating front、QR、恢复 $Tz$ 都有舍入。若保存的是 $\widehat A,\widehat\rho$，则它们需要独立完整身份；不能将其与精确 $W\mathcal AT,Wr$ 混为一谈。局部 QR 理论下界不是浮点结果的精度证书，也不是新数值阈值。
3. **原 nonlinear evaluator。** 保存的 $J$ 不自动等于真实数学 $DF$，新短步矩阵也不是旧长步 rounded J 的逐位代替。原 evaluator 有自己的有限算术和 guards；其真实 norm 与失败必须保全。

可用的精确线性缺陷仍是对**恢复后的完整原坐标 binary64 $\delta$**，按原已存数组先计算

$$
e_n=J_n\delta_{n+1}-\delta_n+r_n
$$

以及同一 cut/far 行，然后精确除以原 sigma。它不通过形成的 QR front 读回，也不先把 $J/\sigma$、$r/\sigma$ 舍入成另一个用于验收的矩阵。此完整 dyadic/rational 读回在现有 consumer 中已经可用；它用于解释方向，而非添加原程序没有的试步门。

若另有一个定义于同一节点变量及行空间的可微实函数 $\mathcal F$ 与其精确导数 $D\mathcal F$，则关于实际 nonlinear 下降的推论还需要支付 $J-D\mathcal F$ 与非线性余项。对更新 $y+\alpha\delta$，一般只能写成

$$
W\mathcal F(y+\alpha\delta)
=W\mathcal F(y)+\alpha W\mathcal A\delta
 +\alpha W(D\mathcal F(y)-\mathcal A)\delta
 +W\mathcal R_{\rm nl}(\alpha,\delta),
\tag{273.19}
$$

且还须注明 $r$ 与 $\mathcal F(y)$ 的保存/表示差。没有这些界，就不能从 QR、阻尼模型或某行 exact residual 直接推出数学 nonlinear 下降。原 R266 已给出相应缺陷与余项的条件框架；本结果不免除它们。

**1372 与原 576 的范围还需分开。** 新方向在全部 1373 节点定义；原 native replay 使用原 577 节点限制 $P\delta$。即使新短步仿射模型下降，也不能不经证明地把它转为旧原 evaluator 的下降：有限 Jacobian 形成不同，且阻尼最小二乘不要求所有内部线性连续方程精确为零。最终必须实际运行原

$$
y^{\rm old}+\alpha P\delta,
$$

用原 target、原 far、原原始 sigma 和原十个 $\alpha$ 求值；所有原 root/branch 拒绝照实保留。只有原 `test.norm < ev.norm` 才是该试步的原接受条件；最终收敛仍用原调用者 tolerance 及后续全部原检查。

## 273.9 最小可实施接口与资源合同（尚未实现）

本节是将来必要时的接口草案，不是已存在的可运行文件，也不请求在本轮新矩阵结果之前另派计算。

拟独立组件可以只借用同一 frozen system 的 `stage_bytes()`、`all()`、`raw()`、`old_to_new` 和完整 `binding`，由构造参数显式给 $\eta>0$ 与 $T$，保持原源不改。它不请求第二次 J、不复算 RHS、不生成新的 H、far 或 sigma。

最低数据流为：

- `factor(system, eta, column_scales, deadline, output_directory)`：一次原 J 流，保存每个 $R_n,S_n,a_n$、最后 $R_D,a_D$、全部纯常数向量/能量账、所有输入和形成源身份。
- `solve_base()`：按 (273.13) 回代完整 $z$，恢复完整原坐标 $\delta=Tz$，保存 signed zero、raw SHA、恢复舍入与非有限记录；同时抽取原 577 节点限制，禁止局部覆盖或删模。
- `readback_original_rows()`：在同一原矩阵/原残差/原 sigma 上调用完整原行读回；另行标明 formed-front/triangular residual，不能混用。
- 原 nonlinear replay 是独立下游入口；该组件不把 factor success、模型 gap、线性 exact norm 或 $\eta$ 值当作新的 native 接受门。

矩阵结构仍只有邻接节点，没有必须保留的额外 global border；cut 和 far 分别位于两个端点。每个 front 最多 $3K$ 行、$2K+1$ 列，最后 front 为 $2K+M$ 行、$K+1$ 列。时间量级为 $O(DK^3)$；完整因子存储为 $O(DK^2)$，可在 artifact 中逐块写出并按反序读回。以本题 $K=224,D=1372$ 计，若按完整方阵保存全部 $R_n,S_n$，原始 factor 大小约 1.10GB；若利用上三角存储，仍需明确实际编码、转置/回代和完整 SHA，不能以压缩名义丢项。

这个资源估计不是本轮计时或 RSS 实测。实际实现须分别记录 front 工作区、LAPACK workspace、factor RAM/磁盘策略、累计和每步时间、RSS、声明预算以及中止处；到预算时保全已完成因子，不假装完整方向已形成。

原 J、r 与 source 身份必须冻结于同一个模型。尝试另一 $\eta$ 会得到另一个方向选择问题，但仍用同一原方程；没有证据时不能把重复调参称为收敛，也不能放宽最终原容差。是否实际实现、选择哪个正 $\eta$、是否需要完整无穷范数模型，应依据新矩阵的一致求解与原真实试步回执继续决定。

## 273.10 对当前课题的确定贡献

现已完整证明：原权重、完整端点和全部阶段可以被保全在一个不形成正规矩阵的平方根阻尼问题中；两次局部 QR 的 carry/常数能量没有遗漏，每节点正则项不重复，完整方向有唯一性与回代公式。也已证明不能以严格二范数下降替代原无穷范数规则。

本结果没有实际候选数值，没有新 native 接受，不支付闭曲面、固定度量、operator、reach、held 或同度量收敛的尚缺证据。其用途是：若当前新有限矩阵方向仍无效，下一算法可以改变方向选择方式，同时让原方程和最终原接受逻辑保持明确。
