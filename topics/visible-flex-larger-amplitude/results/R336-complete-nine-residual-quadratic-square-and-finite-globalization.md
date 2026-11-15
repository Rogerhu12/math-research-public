# R336：完整九维残差二次模型平方、有限候选选择与真实全局化边界

作者：ChatGPT（amplitude）；日期：2026-11-15。类型：条件代数证明及 Request157 的独立有限算法合同。本文不包含新科学数值计算。

依据是 [R335 的 actual154 原始读回](R335-actual154-full-nine-curvature-and-seventy-straight-trials.md) 与 [R332 的完整九维 ambient 曲率公式](R332-complete-nine-merit-curvature-and-honest-trust-proposals.md)。actual154 完成八个方向、七十个真实直线试探；其中大负曲率候选的完整实际 merit 可大幅上升，而二阶 merit 模型仍预测下降。这使“保留三个残差二次模型再平方”的具体实验有依据，但不证明所有失配都来自被省略的三、四次项，也不证明下述模型将给出大步接受。

本文的准确实数恒等式针对同一固定字面系数的有限模型。运行实现仍为 Decimal50 / ROUND_HALF_EVEN，不是区间外包、离散舍入映射的导数、连续方程的误差证书或非零全场解。

## 1. 原问题、冻结坐标与新的提案目标

设 $F:\mathcal U\subset\mathbb R^9\to\mathbb R^3$ 为原完整三方程，所有三个分量仍保留原单位和原权重一。原 merit 为

$$
W(p)=\frac12 F(p)^TF(p).
$$

在当前真实参数点 $p$ 固定

$$
D=\operatorname{diag}(\max(1,|p_1|),\ldots,\max(1,|p_9|)).
$$

$D$ 可逆；一个外方向的模型求解过程中不随内部变量 $y$ 改变。记

$$
f=F(p),\qquad A=DF(p)D,\qquad
B_i=D\,D^2F_i(p)\,D,\quad i=1,2,3.
$$

这里 $DF(p)$ 表示原 Jacobian，不与对角矩阵 $D$ 混同。$B_i$ 为完整九阶对称矩阵，未截掉参数列、交叉项或某个残差分量。定义三个二次残差与其平方目标

$$
Q_i(y)=f_i+A_i y+\frac12y^TB_i y,\qquad
Q(y)=(Q_1(y),Q_2(y),Q_3(y))^T,\qquad
\Phi(y)=\frac12\|Q(y)\|_2^2 .
$$

Request157 在显式相对球 $\|y\|_2\le\Delta$ 内作有限模型求解；本次 $\Delta=0.01$ 是新的实验策略，actual154 的真实末半径只记录为来源，未声称继承。参数仍来自 actual154 的原九个持久 Decimal50 字符串；不把它们转换成 binary64 后再补零。

$\Phi$ 是提案模型的目标，真实接受始终比较 $W$。模型内部点不写入真实参数 owner，也不冒称原方程已在该点求值。

## 2. 完整梯度、Hessian 与低秩项的作用范围

令第 $i$ 行

$$
K_i(y)=A_i+(B_i y)^T .
$$

由 $B_i=B_i^T$ 直接得到

$$
DQ(y)=K(y),\qquad
\nabla\Phi(y)=K(y)^TQ(y),
$$

以及

$$
\nabla^2\Phi(y)
=K(y)^TK(y)+\sum_{i=1}^3Q_i(y)B_i.
$$

证明：逐项应用乘积法则，
$\partial_j\Phi=\sum_iQ_i\,\partial_jQ_i$，
$\partial_{jk}\Phi=\sum_i(\partial_jQ_i)(\partial_kQ_i)+Q_i\partial_{jk}Q_i$，
代入 $\partial_{jk}Q_i=(B_i)_{jk}$ 即得。

因此在 $y=0$，

$$
\nabla^2\Phi(0)=A^TA+\sum_i f_iB_i,
$$

正是 R332 的原 merit 相对坐标 Hessian。新的区别并不是再改这个原点 Hessian，而是在内部移动后继续使用整个 $Q(y)$、完整 $K(y)$ 和上式更新后的 Hessian。

$K^TK$ 的秩至多为三，这不允许把全部九维问题缩成三个固定参数或删掉六个方向：$\sum_iQ_iB_i$ 一般具有完整的九维作用，$K(y)$ 的行空间也随 $y$ 变化。运行实现始终保留所有九列，不加新的数值秩截断。

为避免缩放乘法的有限舍入使上下三角分别形成不同字，源码只形成 $i\le j$ 的 $H_{k,ij}D_iD_j$ 再原字镜像；未缩放的完整原 Hessian 仍保存。该约定使后续多项式使用一个明确的对称有限系数矩阵；它不声称该矩阵是准确实导数的区间外包。

## 3. 与 ambient 二阶 merit 模型的准确差别

对固定 $z\in\mathbb R^9$，记

$$
a=Az,\qquad b_i=z^TB_i z .
$$

沿模型直线 $\alpha z$，

$$
\Phi(\alpha z)
=\frac12\left\|f+\alpha a+\frac12\alpha^2b\right\|^2
$$

严格展开为

$$
\Phi(\alpha z)
=\frac12\|f\|^2+\alpha f^Ta
+\frac{\alpha^2}{2}\bigl(\|a\|^2+f^Tb\bigr)
+\frac{\alpha^3}{2}a^Tb
+\frac{\alpha^4}{8}\|b\|^2 .
$$

前面到二次项为止是 ambient merit 二阶 Taylor 模型。后三、四次项来自对二次残差的完整平方，不是新原方程或新的三阶、四阶残差导数。

四次系数非负，但三次系数可有任意符号；因此不能从四次项非负推出沿每条射线单调，也不能用唯一的标量半径修正代表整个九维求解。Request157 在每次内部更新后重形成 $K(y)$ 与 $\nabla^2\Phi(y)$，可改变全部九个坐标的提案方向；每条射线上的回溯只是这个有限九维求解中的子步骤。

源码将为每个真实外试探保存三项 $Q(\alpha z)$、完整 $\Phi(\alpha z)$、四个展开项，以及实际 $F(p+\alpha Dz)-Q(\alpha z)$ 和 $W-\Phi$。这使“模型中已保留的大项”和“二次残差模型仍未包含的真实误差”可由 Actions 原输出区分。本文没有在本地用 actual154 的数组重新计算 $a,b$ 或任何这些数值。

## 4. 一个完整九维的残差 QR 预条件提案

在某个模型点 $y$ 令 $g=K^TQ$，内层步半径为 $\delta>0$。若 $g\ne0$，定义

$$
\lambda=\frac{\|g\|_2}{\delta}>0,\qquad \mu=\sqrt{\lambda}.
$$

使用完整 $12\times9$ 增广系统

$$
s_{\rm GN}
=\arg\min_s
\left\|
\begin{bmatrix}K\\\mu I_9\end{bmatrix}s
+
\begin{bmatrix}Q\\0\end{bmatrix}
\right\|_2^2 .
$$

准确实数下矩阵满列秩且满足

$$
(K^TK+\lambda I)s_{\rm GN}=-g.
$$

若 $s_{\rm GN}\ne0$，

$$
g^Ts_{\rm GN}
=-\|Ks_{\rm GN}\|^2-\lambda\|s_{\rm GN}\|^2<0,
$$

又由 Cauchy–Schwarz，

$$
\lambda\|s_{\rm GN}\|^2
\le -g^Ts_{\rm GN}
\le \|g\|\|s_{\rm GN}\|,
\qquad
\|s_{\rm GN}\|\le\delta.
$$

这是一个明确的全九维下降及半径条件恒等式，不需要删除小奇异方向，也不改变三个残差行的权重。它是候选之一，未取代完整 $\nabla^2\Phi$ 的移位 Newton 或负曲率候选。

实际源码沿用 frozen149 的完整列主元 Householder QR，保留九阶三角回代；不以 $K^TK$ 作该 QR 求解的输入。保存 $\lambda,\mu$、完整九解、十二项原增广残差、九项 stationarity 残差、列排列及对角。有限形成的 $\mu^2$ 和 $\lambda$ 不预称逐字相等，QR 残差也不构成外包证明；每个实际形成的候选仍会按自身的模型斜率和完整 $Q$ 重新评价。

## 5. 有限候选算法与明确的资源范围

每个原外方向至多执行32次多项式内部更新。每次更新的21个固定候选槽为：

1. 上节的一个完整残差 QR 提案；
2. 一个完整九阶移位 Newton 提案；
3. 一个完整九维 Cauchy 提案；
4. 九个完整有限谱方向的正负两个符号，共18槽。只有实际形成的方向曲率为负时，它们才以负曲率候选身份进入模型回溯；所有未使用槽也保留原因。

谱引导沿用 frozen154 的完整 Jacobi 运算，最多64次 sweep；不把有限特征值或正交残差当作证书。移位 Newton 仍对完整九阶矩阵作 Cholesky，每个更新最多32个移位 bracket 加32个 refinement。失败枢轴、每个实际移位、完整九解和九项线性残差保留；因子矩阵细胞仅保明确的 canonical Decimal JSON SHA，不声称独立导出了全部因子文件。

候选的端点先径向投影到全局相对球，再以投影后端点与当前 $y$ 的差作为实际模型弦 $h$。不是继续使用投影前的斜率或曲率。准确实数下两端在球内时，所有 $y+\beta h$、$0\le\beta\le1$ 都在球内；浮点实现不借此宣称准确球证书，而是逐个试探保存并比较实际形成的范数。

对每个有效候选最多试20个模型档 $\beta=2^{-j}$。这些试探只评价固定系数多项式，绝不新增原699节点 forward、RHS、Hessian 或物理域计算。模型工作轨迹的接受条件为

$$
\Phi(y+\beta h)<\Phi(y),\qquad
\Phi(y+\beta h)\le\Phi(y)+c_A\beta\,g^Th.
$$

$g^Th<0$ 是普通下降情形；$g^Th=0$ 只在实际形成的 $h^T\nabla^2\Phi(y)h<0$ 时允许作负曲率逃逸。后者准确实数下由二阶展开给出足够小 $\beta$ 的严格下降；有限20档不保证找到该档。

这里

$$
c_A=\frac{3602879701896397}{18014398509481984}
$$

是原 binary64 字面常数0.2的准确提升，满足 $0<c_A<1$；运行中的比较仍按原 Decimal50 算术执行，未偷偷换成精确有理数 $1/5$。

每条候选射线取首个满足内部规则的已计算点，随后在这些射线返回点中选择 $\Phi$ 最小者更新内部工作点。模型半径根据该实际模型弦和完整模型下降量更新；控制器的 $\alpha$ 固定传1，避免仅因为模型射线回溯就机械减半。更新后仍受原外球半径限制。全候选池拒绝时内部点不变、模型半径除四。此规则属于新提案算法，不改变物理 owner 或原外半径控制。

固定预算的上界为每外方向32次模型更新、672候选槽、13,440个多项式射线试探、2,048个移位尝试和32个完整残差 QR；八个外方向最多256个模型更新。实际有限错误、提早停止、未使用槽、未访回溯后缀以及未访更新索引全部记录。预算到期既不声称模型最优，也不等同于原方程失败。

## 6. 完整有限信息的选择定理

令 $\mathcal E$ 为本次固定模型所有已经完整评价的有限点；只把满足

$$
\|y\|\le\Delta,\quad
\Phi(y)<\Phi(0),\quad
g_0^Ty<0,\qquad g_0=A^Tf
$$

的点纳入集合 $\mathcal E_-$。这里允许某个已经评价的点不曾成为内部工作轨迹的接受点；这不会改变原工作轨迹或重新执行科学模型。

**命题。** 若 $\mathcal E_-$ 非空，按 $(\Phi,\text{首次完整评价序号})$ 的字典序取 $y_\star$，则 $y_\star$ 有有限已存三残差、在声明的形成球内、具有原点形成的严格下降斜率，并满足

$$
\Phi(y_\star)\le\Phi(y)\quad\text{对所有 }y\in\mathcal E_-.
$$

证明仅是非空有限集合上取最小值。它不需要 $\Phi$ 凸、不需要精确谱分解，也不推出相对球上的全局最小值或原非线性 $W$ 的最小值。

未完整评价、非有限、超形成球或原点斜率不合条件的点不能因为预期很好而被补入。内部函数未完成时输出明确 partial/exception；不把未执行的模型档填成拒绝或数值零。实际源码逐点保存九坐标、三项 $Q$、$\Phi$、内部 Armijo bound、原点斜率、候选序号及失败；没有用单一计数替代全部轨迹。

即使选出的 $y_\star$ 在上述集合最优，也只形成物理提案 $d=Dy_\star$。源码随后在原当前参数上重新作完整第一 forward 方向响应，取得实际原三向量 $v$ 和 $s=f^Tv$；若这个实际斜率不有限或不严格负，不进入本主路径的真实回溯。没有用多项式斜率冒替这次实际响应。

## 7. 真正外层接受及模型与真实余项

主路径只试真实直线

$$
p_\alpha=p+\alpha d,\qquad \alpha=2^{-j},\quad j=0,\ldots,19.
$$

每个实际点重新评价原完整三方程及原有限域，接受条件仍为

$$
W(p_\alpha)\le W(p)+c_A\alpha s,\qquad s<0.
$$

主路径未给出下降方向或20档全拒后，才进入原149的独立完整GN/normal回退；其20外档、12×20内normal预算、R299已有轨迹全merit选择与所有原最终责任不变。两条路径分别记录，不把新的多项式内部档计作原物理试探，也不以模型改善直接替代一次真实接受。

外层半径仍调用原控制器：本主路径的预测下降改成 $\Phi(0)-\Phi(\alpha y_\star)$，normal回退仍用它自己的原线性残差预测；任意实际原接受回溯的减半规则和两路径全拒后的除四规则保留。模型比值不新增为接受门。

若理想有限模型在整段内三次可微，且对 $G(y)=F(p+Dy)$ 的三阶导数张量有已知上界 $L$，则二阶余项满足

$$
G(y)=Q(y)+R(y),\qquad
\|R(y)\|\le \frac{L}{6}\|y\|^3 .
$$

于是

$$
|W(p+Dy)-\Phi(y)|
\le \|Q(y)\|\,\|R(y)\|+\frac12\|R(y)\|^2.
$$

这给出“二次残差平方优于只保二阶 merit”仍需承担的精确余项责任。Request157没有计算或认证这样的全段 $L$，也没有把有限采样差异冒成这个界；真实回溯继续承担接受责任。

准确实数且 $s=DW(p)d<0$ 时，足够小的正 $\alpha$ 满足 Armijo，这是方向导数定义和 $0<c_A<1$ 的直接结果。20个固定档仍不保证覆盖它。若使用有限算出的 $s_{\rm alg}$，设准确斜率 $\theta=s_{\rm alg}+e$，足够小步的充分条件是

$$
e<-(1-c_A)s_{\rm alg},\qquad s_{\rm alg}<0.
$$

更保守的充分条件为 $|e|<(1-c_A)|s_{\rm alg}|$。本实验没有给出这个导数误差外包，故不把已存有限负斜率当成严格可接受步存在性证书。

## 8. 与原 normal 目标的数学区别

原149 normal路径的后两个方程目标是

$$
c(p)+\alpha\,v_{2:3},\qquad c=(F_2,F_3),
$$

路径写作

$$
q(\alpha)=p+\alpha d+P\,w(\alpha).
$$

$P$ 为同一外方向形成的两列物理normal；每次内更新重新计算原方程和实际两列响应。它并不是令两项残差永远等于零，也不是仅对固定 $Q$ 做多项式计算。R299只在这个原工作调用已经完成后，挑选该真实已算轨迹中原全三merit最小的有限点；内目标误差没有被加为新的外接受门。

相反，Request157 主模型同时降低三个 $Q_i$ 的平方，没有固定后两项到上述线性目标，且模型内部没有额外原方程调用。两者不是同一个约束问题、同一条曲线或同一个二阶预测。

对任何可微实际曲线，准确关系为

$$
\frac{d^2}{d\alpha^2}W(q(\alpha))\bigg|_0
=q'(0)^T\nabla^2W(p)q'(0)+\nabla W(p)^Tq''(0).
$$

主路径为直线，$q''=0$；normal曲线一般不满足这一条件。因此即使保留了完整残差二次平方，也不能把它直接称为 normal 路径的完整曲率模型。运行的两路径字段保留此区别。

## 9. 有限系数、二阶forward和求解误差边界

令实际使用的有限模型系数为 $\widehat f,\widehat A,\widehat B_i$。若另有真正外包

$$
\|\widehat f-f\|\le\epsilon_f,\quad
\|\widehat A-A\|\le\epsilon_A,\quad
\left(\sum_i\|\widehat B_i-B_i\|^2\right)^{1/2}\le\epsilon_B,
$$

并且单次多项式评价额外误差为 $\epsilon_{\rm eval}$，则在 $\|y\|\le\Delta$，

$$
\|\widehat Q(y)-Q(y)\|
\le\epsilon_f+\epsilon_A\Delta
+\frac12\epsilon_B\Delta^2+\epsilon_{\rm eval}
=:\epsilon_Q.
$$

故

$$
|\widehat\Phi-\Phi|
\le\|Q\|\epsilon_Q+\frac12\epsilon_Q^2+\epsilon_{\Phi,\rm eval}.
$$

若还包住 $\widehat K-K$，例如
$\epsilon_K=\epsilon_A+\epsilon_B\Delta+\epsilon_{K,\rm eval}$，则形成梯度的一个直接界为

$$
\|\widehat K^T\widehat Q-K^TQ\|
\le \|K\|\epsilon_Q+(\|Q\|+\epsilon_Q)\epsilon_K.
$$

Hessian的代数差也必须同时包含 $K$、$Q$ 与每个 $B_i$ 的误差。例如忽略另列的最终形成舍入项时，

$$
\|\widehat{\nabla^2\Phi}-\nabla^2\Phi\|
\le (2\|K\|+\epsilon_K)\epsilon_K
+\epsilon_Q\left(\sum_i\|B_i\|^2\right)^{1/2}
+(\|Q\|+\epsilon_Q)\epsilon_B .
$$

这些是条件误差公式，不是当前已付外包。初末54个二阶轴FD、54个持久第一FD及54个原binary64投影FD只能按各自实际范围读回；整列相对误差小并不自动保证最弱响应、负曲率或取消后的方向准确。完整系数SHA同样只能证明身份，不能界定误差幅度。

同理，实际Cholesky/QR形成和回代误差不会因保存了线性残差便自动变成条件数无关的解误差证书。factor细胞仅SHA的记录明确不作独立因子审计。没有改动原门来掩盖这些未付误差责任。

## 10. 实际可执行范围与未付结论

独立搜索源为 [完整九维残差二次平方提案器](../computations/geometry_20261115_nine_control_decimal_residual_quadratic_trust.py)，接线见 [Request157完整接口](../notes/2026-11-15-request157-complete-nine-residual-quadratic-square-interface.md)。它复用冻结154的完整二阶forward模型和有限谱/移位辅助函数，复用冻结149的原真实模型、完整QR、normal路径与外半径控制；旧源码不变，新的producer身份和来源闭包独立。

初末完整二阶轴FD、持久第一FD、原投影第一FD、160位/深14的标量Arb、完整453圆及原full112线性右残差全部保留。原binary64投影检查不冒同一持久Decimal点的连续证书；高109非共振、真实native尾、非线性fullDN与非零全场接受仍需各自实际完成。

本实验只运行一批原八方向。既不再机械连续32批小步，也不预断大步可行。真正待测的是：完整九维的三残差二次平方是否形成更有效的有限位移；它与真实三残差的差在多大步长开始主导；以及是否实际通过旧的域、斜率和Armijo条件。失败、资源partial、模型预算耗尽和未访问后缀分别输出，不互相改名。

所有科学运算只在本公开仓库Actions执行。本地工作限源文本、数学推导与身份/JSON元数据；未运行新的模型、优化、Hessian、FD或数值fixture。
