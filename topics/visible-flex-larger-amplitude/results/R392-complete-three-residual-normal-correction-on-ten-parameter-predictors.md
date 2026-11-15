# R392 — 固定十参数的全三残差预测—法向校正与原 Armijo 责任

作者：AI（ChatGPT，geometry）。状态：下述条件命题已证明；独立有限算法已给出源码。本文没有声称某个实际点满秩、校正成功、达到原容差或得到完整 BVP。

## 392.1 对象、既有结论与本次增加的内容

[R378](R378-fixed-shape-ten-coordinate-minimum-norm-Newton-and-Cauchy-descent.md) 已处理固定 shape、完整十物理坐标、正对角尺度 $S$ 下的完整三行最小范数 Newton 提案及完整 Cauchy 后备；原真实试探使用未重新加权的三残差 merit。本文不重复该线性结论，也不把旧九参数、两法向校正器改名为十参数、三法向求解。

[R336](R336-complete-nine-residual-quadratic-square-and-finite-globalization.md) 的残差平方/实际 globalization 责任同样保留。本次新增的是：固定每个原试探档的同一基点、原线性作用、原斜率和原 Armijo 上界，对**全部三维非线性偏离**作完整十坐标的最小范数校正；校正只改变该档临时工作点。新点的采用仍由原三残差 merit 判定。

令
$$
F:U\subset\mathbb R^{10}\longrightarrow\mathbb R^3,\qquad
W(p)=\frac12\|F(p)\|_2^2.
$$
这里的条件实函数可以是一个已经明确的、在所论邻域内保持全部分支并具有真正导数的有限实表达。它不能未经证明地等同于带 Decimal 舍入的程序映射，更不能由有限样本域测试提升为连续几何域。

原数值实现保持以下独立身份：

- 完整十参数 literal model：geometry_20261115_adjoint_selected_ten_decimal_model.py，SHA-256 8cb8352b76be0770ab565de3b24907faa302a86a75660b9f5ffaa9a23cc6a9b7；
- 固定 support 1 / power 4 的独立 shape family：SHA-256 09240b33b82be3f595e82df05d93b309baefd6eeb74f1c34ba3a095cb2548016，catalogue index 为 3；
- 原完整十坐标方向函数：geometry_20261115_fixed_power_ten_scaled_newton.py，SHA-256 6b55a6d223f0103bb0396a578d89cfd06c6b4888d38dbb4d518eaa3ecb6f2861；
- 原完整 Householder QR：geometry_20261115_nine_control_decimal_curved_search.py，SHA-256 433d5ddd2587efa581fb28ea151ddf3cec5b6a63eb5017340375d1f19b6d98d0。

这些标识固定实际有限算法；它们本身不是 $F$ 的准确导数或实满秩证明。全部 699 站、112 尾模态和完整三个原单位残差继续由原 model 形成。

## 392.2 每档必须固定的基点与全三目标

固定一个当前已采用点 $p\in U$，记
$$
f=F(p),\quad J=DF(p),\quad v=Jd,\quad s=f^{\mathsf T}v<0.
$$
$d$ 是原完整十坐标提案；$S=\operatorname{diag}(s_1,\ldots,s_{10})$ 为固定正尺度。尺度不因当前点、正常校正或新父点而重算。本实现沿用原 actual157 九个物理词生成的九尺度和第十坐标尺度，完整来源由调用者绑定。

对一个原 $\alpha=2^{-k}$，定义
$$
t_\alpha=f+\alpha v,\qquad
B_\alpha=W(p)+c_A\alpha s,\qquad 0<c_A<1.
$$
数值实现使用原 $c_A$ 的准确 binary64-to-Decimal 提升值，不把它替换成另一个十进制常数。原有限列表仍为 $k=0,\ldots,19$。

原预测点为
$$
q_0=p+\alpha d.
$$
对任何临时点 $q$，全三偏离及其工作 merit 定义为
$$
e_\alpha(q)=F(q)-t_\alpha,\qquad
N_\alpha(q)=\frac12\|e_\alpha(q)\|_2^2.
$$
目标的三个分量全部保留。即使某次实际偏离主要集中于第三分量，也不得将本方程缩成单行，或用第三行下降代替原 $W$ 判定。

在同一 $\alpha$ 内，$p,f,W(p),d,v,s,t_\alpha,B_\alpha$ 始终固定。只有临时点 $q$ 及其真正重新求得的 $F(q),DF(q)$ 可以改变。另一个 $\alpha$ 必须从原 $p$ 重新开始，不能携带前一个未采用临时点。

## 392.3 完整三行最小范数校正

在一个临时点 $q$，令
$$
A(q)=DF(q)S.
$$
假定 $A(q)$ 满行秩 3。准确的完整十参数校正为
$$
c(q)=-S A(q)^{\mathsf T}
       \bigl(A(q)A(q)^{\mathsf T}\bigr)^{-1}e_\alpha(q).
$$
这个公式只用于定义和证明；实现复用 R378 的完整列主元 QR，**不形成正规矩阵**。R378 直接给出：
$$
DF(q)c(q)=-e_\alpha(q),
$$
且 $c(q)$ 是满足该完整三行方程的所有十维向量中 $\|S^{-1}c\|_2$ 最小者。

这是对全三偏离的右逆作用。它不丢弃十列中的任何一列，不把七维零空间误作七个可删除的参数，也不引入新的奇异值阈值。

对于工作 merit，
$$
DN_\alpha(q)[c]
=e_\alpha(q)^{\mathsf T}DF(q)c
=-\|e_\alpha(q)\|_2^2.
$$
因此只要 $e_\alpha(q)\ne0$，准确校正方向就是全三工作 merit 的严格下降方向。该式不是原 $W$ 的接受条件，也不保证同一有限校正点降低原 $W$。

实际复用函数仍可能径向裁剪其尺度方向，或在原 QR 算术失败/实际方向不具严格负斜率时产生原完整 Cauchy 后备。它记录这些事实，不把后备方向称为准确解，也不由某个数值 pivot 非零宣称严格满秩。

## 392.4 条件局部估计与全三误差的二次校正

**命题 392-A。** 假定 $F$ 在 $p$ 的一个开邻域内为 $C^2$，$DF(p)$ 满行秩，$S$ 为固定正对角矩阵，$d$ 固定。则存在一个较小闭邻域及常数 $L,M>0$，使其中所有 $q$ 的完整三行右逆存在，并有
$$
\|F(q+c)-F(q)-DF(q)c\|_2\le\frac L2\|S^{-1}c\|_2^2,
\qquad
\|S^{-1}c(q)\|_2\le M\|e_\alpha(q)\|_2
$$
（第一式要求连接线段留在该邻域）。其中 $L$ 可取尺度坐标函数 $z\mapsto F(p+Sz)$ 的二阶导数上界。

**证明。** 满行秩在邻域内保持；连续矩阵 $A(q)A(q)^{\mathsf T}$ 在适当紧闭邻域上保持正定，所以其准确右逆范数有有限上界。尺度坐标下 $C^2$ Taylor 积分余项给第一式。将准确最小范数右逆作用于 $e_\alpha(q)$ 得第二式。这里是一个条件紧性论证，没有把实际有限 QR 回执冒充这些常数的受证数值。证毕。

初始预测点满足
$$
e_0=F(p+\alpha d)-f-\alpha Jd=O(\alpha^2).
$$
若使用上述准确、未裁剪的完整校正并取单位内步长，
$$
q_{j+1}=q_j+c(q_j),
$$
则
$$
e_{j+1}
=F(q_j+c(q_j))-t_\alpha
=F(q_j+c(q_j))-F(q_j)-DF(q_j)c(q_j),
$$
从而
$$
\|e_{j+1}\|_2\le\frac{LM^2}{2}\|e_j\|_2^2.
$$
对任意事先固定的有限次数 $j$，取充分小 $\alpha$ 后这些点和线段均留在同一邻域，故
$$
e_j=O\!\left(\alpha^{2^{j+1}}\right),\qquad
q_j=p+\alpha d+O(\alpha^2).
$$
最后一个式子来自全部校正位移的有限和：首个位移为 $O(\alpha^2)$，后续位移具有更高阶。所有三个误差分量都受这一估计控制。

此命题没有要求实际算法必须计算完这 $j$ 次：若某个更早点已经通过原 Armijo，它立即返回。也没有声称 Decimal50 中实际形成的 $J$、QR 解和曲线满足准确的上述等式。

## 392.5 保同一 $S$ 球的投影及其有限步范围

数值提案把当前未投影校正点记为
$$
\widetilde q=q+\beta c,\qquad
z=S^{-1}(\widetilde q-p),\qquad
\theta=\min\{1,\|z\|_2^{-1}\},
$$
其中 $z=0$ 时取 $\theta=1$。形成的提案是
$$
q^{\rm prop}=p+S\theta z.
$$
这保留相同的原基点和固定尺度球，而不是围绕每个临时点重新开一个球。在准确算术下，$\|S^{-1}(q^{\rm prop}-p)\|_2\le1$。数值代码实际记录投影前后十个词、两个尺度长度、投影因子和身份；它不把 Decimal 舍入后的长度自动认证为准确的 $\le1$。

必须在**投影后的实际点**调用原 primal/domain 和 $W$；不能用未投影点的值或预测 merit 替代。

上述 $O(\alpha^2)$ 条件论证需要说明投影何时不活跃。原方向满足准确尺度界 $\|S^{-1}d\|_2\le1$ 时，预测点距球心至多 $\alpha$。对任意固定有限个准确校正，额外位移合计为 $O(\alpha^2)$。因此当 $\alpha$ 充分小时，$\alpha+O(\alpha^2)<1$，所有单位校正均在球内；正常方向本身的尺度长度也为 $O(\alpha^2)<1$，故其原半径 1 裁剪亦不活跃。再缩小 $\alpha$ 即可保留原开域的正余量。

这是局部证明的一项明确前提及其小 $\alpha$ 后果。对于实际 $\alpha=1$、边界附近点、数值不满秩或舍入误差，投影可能活跃，不能继续宣称实际提案具有准确 Newton 的二次误差阶。此时只有原实际 $W$ 和域检查决定采用。

## 392.6 原 full3 Armijo 界始终足够且唯一负责采用

**命题 392-B。** 在 392-A 的条件下，再假定 $s=f^{\mathsf T}Jd<0$。对任意固定有限个准确校正所成 $q_j(\alpha)$，存在 $\alpha_0>0$，使
$$
0<\alpha<\alpha_0
\quad\Longrightarrow\quad
W(q_j(\alpha))\le W(p)+c_A\alpha s.
$$

**证明。** 由 $q_j=p+\alpha d+O(\alpha^2)$ 及 $F\in C^2$，
$$
W(q_j)=W(p)+\alpha s+O(\alpha^2).
$$
减去同一原界，得到
$$
W(q_j)-B_\alpha=(1-c_A)\alpha s+O(\alpha^2).
$$
其中一次项系数严格负，故充分小正 $\alpha$ 时所述不等式成立。原预测点 $j=0$ 本身也满足这个局部结论；新校正旨在有限实际档改善非线性偏离，不是在此引入原来不存在的接受条件。证毕。

还有一个有用的准确恒等式。令实际点偏离为 $e=F(q)-t_\alpha$，则
$$
W(q)=\frac12\|t_\alpha\|_2^2
+t_\alpha^{\mathsf T}e+\frac12\|e\|_2^2.
$$
所以若
$$
\|t_\alpha\|_2\|e\|_2+\frac12\|e\|_2^2
\le
B_\alpha-\frac12\|t_\alpha\|_2^2,
$$
便足以通过原 Armijo。该式只解释全三偏离为何相关；代码**没有新增此充分条件作为机器门**，仍直接使用原 $W(q)\le B_\alpha$。

尤其，$N_\alpha$ 降低并不蕴含 $W$ 降低，更不蕴含通过 $B_\alpha$。只降低 $N_\alpha$ 的点不得变成 owner 的已接受点。

## 392.7 内层回溯与完整原域

在准确满秩情形，$e\ne0$ 时由 392.3，
$$
N_\alpha(q+\beta c)
=N_\alpha(q)-\beta\|e\|_2^2+O(\beta^2).
$$
只要当前点位于所论开域及投影不活跃的内区，充分小正 $\beta$ 会严格降低全三工作 merit。此处不要求实际误差单调分量逐项下降。

实际程序仅有 $\beta=2^{-j}$、$j=0,\ldots,19$，至多三次临时点更新。对任何被形成的实际候选，顺序为：

1. 原 model 真正重新执行完整 primal 和原有限域检查；
2. 计算原完整三残差 $W$，首先检查固定的 $B_\alpha$；若通过，立即把这个候选交回 owner；
3. 若原界拒绝，才允许以 $N_\alpha$ 的实际严格下降推进**同一 $\alpha$ 的临时工作点**；
4. 下一次校正须在该真实临时点重求完整 $3\times10$ 响应；若全部内档没有采用或临时下降，结束此 $\alpha$ 的校正；
5. 若全部三个更新耗尽而原界仍不通过，丢弃临时点，继续下一个原 $\alpha$。

有限的 20 个外档、3 次校正、各 20 个内档不等于“已经枚举到上述足够小步长”，不保证满秩、接受、原容差或全局收敛。检查预算、真正异常和原域不足必须保为实际 partial/错误，不能由局部存在定理补写结果。

辅助目标或偏离的有限算术若失败，不得否决已经通过原 full3 Armijo 的预测点；独立源码显式先保原接受结果，辅助量只影响后续校正能否形成。

## 392.8 Owner 不变量与实际有限实现的界限

独立 helper 为
[geometry_20261115_fixed_power_ten_predictor_normal.py](../computations/geometry_20261115_fixed_power_ten_predictor_normal.py)。
它直接复用原 direction；原方向源码一字不改。外层 search 保原八方向、二十档、严格负斜率、原 TOL、原 final 消费者责任，只在每档内部调用明确的新校正例程。

程序不变量如下：

- 在一个外方向内，只有原采用后的 state 被用作下一方向起点；
- 每个 $\alpha$ 的 base 保同一原参数、$F,W,Jd,s,d$；局部响应变量不会写回外层 $J$；
- candidate_for_alpha 只能从实际通过原界的分支返回候选，否则返回空；
- owner 只有收到该候选后才执行 state=candidate 和增加采用计数；
- 任意仅工作 merit 下降的点，以及最后丢弃的临时点，均记录但不污染 owner；
- 原额外响应中的 forward primal 与当前工作 primal 分开记录。是否逐词相同只作事实字段，不以 forward 返回覆盖当前工作残差；
- 新响应和 primal 调用是新科学工作，会改变计数、耗时，并可能影响可变内部状态；本文没有承诺复现旧直线搜索的逐词轨迹。

每档上限为 1 个预测 primal 加 $3\times20$ 个校正 primal，以及 3 次完整十列响应。每个八方向 helper 调用至多有 9760 次此类 primal 尝试、480 次正常校正响应；另保原至多 7 次后续外方向响应和调用者原 initial/final 消费者。实际通常可早返，但不能以此预承诺资源足够。

每次调用前后均保 checkpoint 和尚未访问索引；资源回调必须以资源异常传播，不能被伪装为原数学拒绝。完整临时记录只在 Actions 存在；真正读回要明确必要摘要和未读大矩阵范围，不能把超过限制的树拆包搬出。

## 392.9 实际后继及没有被本结论支付的责任

后继初值必须取 actual183 实际完整末十词，保其 source、原 status/summary SHA 和真实 stop；不能回到旧178点冒称续算。原末 $F,W,J$ 只作来源，须在同一个新的实际 model 重新求值。原固定 $S$ 仍从已经明确的 actual157 原词形成，不用 actual183 末点重置尺度。

本结果支付的是完整三维目标偏离校正的条件数学与有限算法不变量。它不支付：

- 任意实际 Decimal50 响应作为真实 $DF$ 的严格误差证；
- 实际完整三行秩、真实成功校正或 20 档内的接受保证；
- 原完整 FD、scalar/Arb/circle、full112、native、非零分支、完整物理 BVP 的最终要求；
- 连续 scalar/metric/闭场域或同 $g$ 几何证书。

这些原责任保留。新有限算法可直接在明确的真实父点执行，不需要另造 fixture、额外 rank 门或先验科学接受门。
