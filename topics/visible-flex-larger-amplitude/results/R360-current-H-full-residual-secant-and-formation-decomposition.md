# R360：当前正 H 的完整残差差额、状态形成和有限割线分解

作者：ChatGPT /root（AI 协作），2026-11-15。性质：**已证明的有限数据恒等式及条件误差界**。无新科学计算；没有把 actual145 的线性模型认作实际 noJ 映射的准确导数，也没有改变原非线性接受条件。

## 1. 本结论解决的具体责任

[R343](R343-actual145-current-H-R273-and-positive-height-line-search-stop.md)记录 actual145 的五次 fresh 当前系统与十九次实际回溯。保存矩阵的仿射终点与实际 noJ 残差不同；单凭两种范数无法判断差异来自基点两条计算路径、试步状态形成、矩阵方向、有限 root/RK 或真正非线性变化。

本结论给出对**同一次当前模型、同一全部状态方向**的逐行准确分解。它只使用已经形成的有限字词，第一部分完全不要求 root 可微、分支稳定、Jacobian 正确或连续角证书。第二部分才在明示的准确实参考映射上引入导数和 Taylor 余项。两部分不能相互偷换。

原程序来源为 public source commit a513ada7d1dbe1b2fa51d3f1f987c59b48233dba：

| 来源 | SHA-256 |
|---|---|
| 原 shooting core 78718-tail-tangent-core.mjs | ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3 |
| 原恢复 engine tail_resumable_engine.mjs | 1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8 |
| actual145 当前 R273 hook | f13b0a0d3f7e6d3487f0eda92dc9e76117137ee106c9f33471e762e35c9106e0 |
| 当前系统 exact_20261115_original_r273_current576_system.py | 3557608524becae2bbf1c2100af12c865082329efccbd5078008cb2c8591c101 |
| 当前完整 QR/exact 读回入口 | d5d9874242499df7a79fe4411a420de0cfe8464c64c80dd9c18ec501d226a296 |

原 core 是本仓库 topics/visible-flexible-closed-surface/scripts/ 下的文件；其冻结依赖由本题 source-dependencies.json 和原恢复 helper 提供，不从私有仓库计算。数学定义与来源身份不同：下面的定理对任何满足声明尺寸和固定系数的数据成立，不能从源码 SHA 推出某次实际数值结果。

## 2. 全部原行与固定当前模型

令 $M=112$、$K=2M$、$D=576$。状态为
$X=(X_0,\ldots,X_D)$，每个 $X_n=(Q_n,\Pi_n)\in\mathbb R^K$。
同一次当前模型中，固定实际 cut target $h$、原 far 对角系数 $G$、原全部几何/字面表、原 stage 分割，以及实际正尺度
$\sigma_0,\ldots,\sigma_D$。当前 H 在本模型内不变化。

原方程顺序是：

$$
r_{\rm cut}(X)=Q_0-h,\qquad
r_n(X)=\Phi_n(X_{n+1})-X_n\quad(0\le n<D),\qquad
r_{\rm far}(X)=\Pi_D-GQ_D.
$$

共有 $M+DK+M=129248$ 行。原有两 mean 随每个完整 $K+2$ 状态 flow 计算；这里的 shooting 未知量仍是原 $K$ shape 坐标，不能把 mean 删出实际 RHS 或改称原最终338行已付。

保存矩阵 $\widehat A$ 的完整作用为

$$
(\widehat A v)_{\rm cut}=v_{0,Q},\qquad
(\widehat A v)_n=\widehat J_n v_{n+1}-v_n,\qquad
(\widehat A v)_{\rm far}=v_{D,\Pi}-Gv_{D,Q}.
$$

$\widehat J_n$ 是该次实际 withJ 返回并保存的字词。它在此只是明确矩阵，不预设 $\widehat J_n=D\Phi_n$。$G$ 也取本模型实际保存字词。R273 的577个惩罚块用于选择方向；它们**不属于**上述129248原方程，不能加入以下原残差范数。

令 $W$ 为行尺度矩阵：cut 用 $1/\sigma_0$，stage $n$ 用 $1/\sigma_n$，far 用 $1/\sigma_D$。本文只在所有被用字词有限且 $\sigma_n>0$ 时使用准确实提升。若有非有限数或零尺度，应记录原异常和未付范围，不能强行作有理数除法。

## 3. 对实际形成状态的逐行恒等式

把每个 finite binary64 字词提升为它表示的准确二进有理数。负零与正零的数值提升都是零，原字节身份与负零位置仍应另外保留；数值恒等式不声称字词相同。

设 $\Delta$ 是当前完整返回方向。原第 $k$ 档的 $\alpha=2^{-k}$，并按原逐坐标表达式形成

$$
T_\alpha=\operatorname{fl}\bigl(X+\operatorname{fl}(\alpha\Delta)\bigr),
\qquad
q_\alpha=T_\alpha-X-\alpha\Delta.
$$

这里 $T_\alpha$ 必须是原实际 trial 的全部字词。不能只在另一个语言里用同一数学式重造，再称为原状态；乘法和加法各自的舍入、下溢和零符号均可能不同。$q_\alpha$ 在准确提升之后相减，因此同时包含实际乘法与加法的形成差。即使 $\alpha$ 是二幂，也不自动将它设为零。

保存 withJ 基点残差记为 $\widehat r_J$；在同一个 $X$ 上重新执行完整原 noJ 后，所得准确提升记为 $\widehat r_0$；原 trial 的完整 noJ 残差记为 $\widehat r_\alpha$。这三个符号表示**实际执行记录**，不要求它们来自同一个连续函数或数值上可重复的过程。

对 cut 原式没有单独 ev 数组的情形，观察器须明确用原实际 $Q_0,h$ 字词及相同减法形成该行，并把这项形成来源写出；不得谎称该数组原先已存。stage residual 与 far end 则直接使用原返回数组。原 report 的 max norm 与这组准确提升行还须按第5节区分。

定义

$$
\ell_\alpha=\widehat r_J+\alpha\widehat A\Delta,\qquad
b=\widehat r_0-\widehat r_J,
$$

$$
s_\alpha=
\widehat r_\alpha-\widehat r_0-\widehat A(T_\alpha-X),
\qquad
d_\alpha=\widehat r_\alpha-\ell_\alpha.
$$

**定理1（完整当前模型差额分解）。** 在上述有限性、完整性和来源固定条件下，全部129248行准确满足

$$
\boxed{d_\alpha=b+\widehat A q_\alpha+s_\alpha.}
$$

证明。由 $T_\alpha-X=\alpha\Delta+q_\alpha$，逐行代入右边：

$$
\begin{aligned}
b+\widehat A q_\alpha+s_\alpha
&=(\widehat r_0-\widehat r_J)+\widehat A q_\alpha
 +\widehat r_\alpha-\widehat r_0-\widehat A(T_\alpha-X)\\
&=\widehat r_\alpha-\widehat r_J-\alpha\widehat A\Delta=d_\alpha.
\end{aligned}
$$

证明只用准确实加减和线性性；不使用任何 Jacobian 正确性或近似相等。cut、所有stage及far都在同一个行序中，因此恒等式覆盖完整原问题，而不是前三模或某一最坏行。证毕。

$b$ 表示本次基点 withJ/noJ 实际残差路径差。$\widehat A q_\alpha$ 是已保存矩阵对真实状态形成差的作用。$s_\alpha$ 是在实际有限位移 $T_\alpha-X$ 上的割线缺陷。最后一项尚未区分矩阵方向误差、实际程序误差与准确非线性余项，不能只因它大就选定其中一个病因。

若未执行 noJ 基点，仍可直接测 $d_\alpha$；但 $b$ 与 $s_\alpha$ 的分离尚未支付。不能用“上一个接受 norm 等于下一 withJ norm”替代完整 $\widehat r_0$。

## 4. cut/far 仿射行给出的可分离范围

令 $L_{\rm bd}X-c$ 为原 cut/far 两组准确仿射表达式。固定本模型的 $h,G$ 后，保存矩阵对应行正是 $L_{\rm bd}$。对任一已观察边界评价定义其形成差

$$
e_{\rm bd}(Y)=\widehat r_{{\rm bd},N}(Y)-(L_{\rm bd}Y-c).
$$

这包含原 $GQ$ 乘法、减法，以及明确重复形成 cut 行的舍入，不假设为零。

**推论2。** 同一次基点和试步的边界割线缺陷恰为

$$
(s_\alpha)_{\rm bd}
=e_{\rm bd}(T_\alpha)-e_{\rm bd}(X).
$$

证明。将两次 $\widehat r_{{\rm bd},N}$ 展开，准确仿射差
$L_{\rm bd}(T_\alpha-X)$ 被 $\widehat A_{\rm bd}(T_\alpha-X)$ 抵消。证毕。

因此，边界行不存在该仿射方程自身的二阶余项。若边界差额非零，应分别检查 $b_{\rm bd}$、$L_{\rm bd}q_\alpha$ 和两次原边界形成误差，不能归因于 stage root 非线性。反过来，边界差额小不约束 stage 行，更不能证明原完整 J 正确。

这里要求 $G,h,\sigma$ 和坐标定义实际相同。跨请求改变 H、替换far矩阵、改端口缩放或用另一个模型的权重时，不能沿用此抵消。每个新模型必须重新绑定自己的系数。

## 5. 原严格 max norm 与准确提升读数

记准确提升后的原尺度范数为

$$
\nu_\alpha=\|W\widehat r_\alpha\|_\infty,\qquad
m_\alpha=\|W\ell_\alpha\|_\infty .
$$

原程序打印的 norm 记为 $\widehat\nu_\alpha$。它逐次执行浮点绝对值、除法和 max；不能自动把它与准确有理数 $\nu_\alpha$ 逐字或数值认同。定义实际可测的
$\varepsilon_\alpha=|\widehat\nu_\alpha-\nu_\alpha|$。原接受仍按它自己的 $\widehat\nu_\alpha<\widehat\nu_J$；以下诊断不替换原门。

**推论3（完整差额的上下界）。**

$$
|\nu_\alpha-m_\alpha|
\le \|Wd_\alpha\|_\infty
\le \|Wb\|_\infty+\|W\widehat A q_\alpha\|_\infty+\|Ws_\alpha\|_\infty .
$$

证明。左边是同一范数的反三角不等式，右边由定理1和三角不等式。$W$ 固定且各尺度严格正，故各项合法。证毕。

对任一已明确的行 $i$ 还有直接见证

$$
\|Wd_\alpha\|_\infty
\ge \frac{|\widehat r_{\alpha,i}|-|\ell_{\alpha,i}|}{\sigma(i)}.
$$

右边为正时就是该次准确提升数据的严格正下界；并不是任意精度、任意方向或所有较小 $\alpha$ 的普遍误差下界。若只知道打印 norm，应先减去对应的实际 $\varepsilon$ 或严格上界，不能将显示十进制当准确范数参与证明。

原模型的 $L^2$ merit、惩罚目标及未预条件 gradient 均不能代替这个原 $\ell^\infty$ 接受量。完整读取可报告 cut/stage/far 各组和全局的准确最大值及见证行，但不应为了诊断新增一个非线性接受阈值。

## 6. 何时才能进一步解释为导数与非线性余项

另选择一个**明确的**准确实参考 $F_*$，定义在包含 $X$ 和 $T_\alpha$ 的凸邻域。它必须固定同一实际几何/表/端口/方程顺序，并明确选择下列哪一种对象：

- [R283](R283-finite-root-trace-differentiation-with-literal-tables.md)、[R305](R305-literal-gram-root-contraction-and-nominal-factor-defects.md)所讨论的固定成功 root 分支及有限更新的准确实延拓；
- 真正隐式 root 定义的准确有限方程映射，其导数还需真实 $F_L$ 可逆、root 误差与相应来源条件。

两种对象的导数不必相同；原 Gram 迭代矩阵也不能未经证明充作真实 root 方程导数。IEEE 程序本身更不能因存在某个有限差分而被宣布可微。

假设所选 $F_*$ 为 $C^2$。定义该次实际 noJ 评价的误差

$$
e_0=\widehat r_0-F_*(X),\qquad
e_\alpha=\widehat r_\alpha-F_*(T_\alpha),\qquad
v_\alpha=T_\alpha-X.
$$

**定理4（有明确准确参考时的完整分解）。**

$$
s_\alpha=
\bigl(DF_*(X)-\widehat A\bigr)v_\alpha
+\int_0^1(1-t)D^2F_*(X+t v_\alpha)[v_\alpha,v_\alpha]\,dt
+(e_\alpha-e_0).
$$

证明。对向量函数 $t\mapsto F_*(X+t v_\alpha)$ 两次用微积分基本定理，得到带积分余项的 Taylor 恒等式。再代入 $e_0,e_\alpha$ 的定义，并减去 $\widehat A v_\alpha$。积分逐分量定义，故覆盖全部原行。证毕。

若已给出严格界

$$
\|W(DF_*(X)-\widehat A)v_\alpha\|_\infty\le J_\alpha,\quad
\sup_{0\le t\le1}
\|WD^2F_*(X+t v_\alpha)[v_\alpha,v_\alpha]\|_\infty\le H_\alpha,
$$

$$
\|W(e_\alpha-e_0)\|_\infty\le E_\alpha,
$$

则

$$
\|Ws_\alpha\|_\infty\le J_\alpha+\tfrac12H_\alpha+E_\alpha.
$$

这三个界是额外需要支付的实际数学责任，本文没有填任何数值。R314/R325 的逐 root、名义线性求解、完整方向、RK与端口误差框架可用于构造它们，但某一个field的证书不能自动扩张到全部576段、该次正H、全部闭位移段或另一个状态。

## 7. 可直接执行的诊断，不改原数学实验

未来 request172 可在保持 actual145 的同一显式六参数、H路径、warm政策和原32×10/严格下降/2e−9门下实施：

1. 每个实际 fresh 模型记录完整当前状态、target、sigma、$\widehat J$、返回方向和原withJ残差身份。观察器先复制实际字词，不保存可变别名；清理大矩阵前，先完成所需准确线性作用或保留明确的临时作用数据。
2. 在相同模型状态执行一次完整原 noJ 基点；观察是否全行一致，不由 norm 相同推出。任何额外调用必须明确计数，不谎称原145已经做过。
3. 对原实际访问的十档候选，使用**该次** $T_\alpha$ 和原返回残差计算定理1；已接受与已拒绝都记录，原未访问档不补成已访问。
4. 若原十档真实耗尽，可另做明确列出的较小 $\alpha$ 诊断。它们不是追加到原接受搜索中的第十一档，不得修改 worker last、成功warm、返回的原失败或迭代计数；只提供新执行的割线数据。
5. 原guard、root异常或资源停止没有完整残差时，保持错误、已完成行/阶段与未付后缀。不能将该试步记为全残差零、无穷或一种已完成的范数拒绝。
6. 所有科学算术和实际 root/RK 调用只在公开 Actions；读回只传必要原数值、完整范围/身份和明确未付范围，不编码、分块搬运全部大数组。没有新的raw Git/Release/artifact归档。

这是明确可复现的后续实验设计；本文没有声称 request172 已发布、运行或返回。原145已删除的状态不能从SHA恢复，必须在新job真实再生。新run的实际轨迹即使与R343不同，也按本次实际来源记录，不能伪填原第五轮或原最坏行。

## 8. 结论的边界

已证明的是完整当前系统的准确数据恒等式、仿射边界抵消、原尺度范数界，以及有明确 $C^2$ 参考时的 Taylor 分解。它们把下一计算需要区分的量写成可测对象。

尚未证明 actual145 的哪个误差项主导，未证明某个更小步必被接受，未取得当前正H的完整导数误差界、非零native解、最终338×112响应/fullDN或README闭面与比例目标。单方向有限割线，即使逐档缩小，也不构成全Jacobian、连续闭段或精确存在性证书。
