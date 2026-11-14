# R195：真实位置族的径向带状 normal、单边界 Schur 与同一 LM 方向

**状态：完整有限维等价证明；一次真实 193 维耦合 normal 对照已执行。** 本条只替换线性方程求解，不改 R187/R190/R191 的场、物理 metric、完整角 primitive、曲率引导、残差行、权重、参数域或实际 Armijo。当前输入仍是 dense normal；新的 band accumulator 尚未实现。

## 1. 原有限布局与支撑

R190 在 $J$ 个径向 cardinal cubic 基、$K$ 个 sine 偶角模下，按原顺序保存
$$
z=(\theta_{j,k},\phi_{j,k},Z_j,Z_{\rm cut},\rho_j),
\qquad n=J(2K+2)+1.
$$
R187 无 $\rho$ 块，故 $n=J(2K+1)+1$。R191 的真实曲率引导复用同一个完整位置族及明确 stateLayout，没有新增状态变量。

每个 $B_j$ 支撑四个相邻均匀径向区间。任一精确物理点的 $B_j,B_j',B_j''$ 只有至多四个相邻编号可能非零。完整角三角函数及 quarter primitive 都在同一 $s$ 求值；角积分的一阶矩不扩大径向支撑。因此同一个 actual metric 行或 actual curvature 行，只依赖这几个相邻径向块，以及全局末高 $Z_{\rm cut}$。

定义径向块
$$
x_j=(\theta_{j,1},\ldots,\theta_{j,K},
\phi_{j,1},\ldots,\phi_{j,K},Z_j,\rho_j)
$$
（R187 删除最后一项），块宽 $b=2K+2$ 或 $2K+1$。将 $Z_{\rm cut}$ 放最后。每行的径向块跨度至多 3，所以
$$
(H_{ff})_{ij}=0\quad\text{当}\quad |i-j|>3,
\qquad H=J_F^TJ_F.
$$
全局末高产生一个边框列。完整非线性链和角高模仍全部留在非零块内。

这首先是精确支撑论证。实际 binary64 knot 判断可能有舍入，代码不会据此静默删项。它扫描实际输入 $H$ 的所有元素；任一带外非零都拒绝求解，阈值准确为零。真实 193 维输入的带外项全部为零；人工加入 $10^{-300}$ 也确实被拒绝。

## 2. 与冻结 dense LM 相同的缩放及工作矩阵

按原编号每列使用
$$
s_i=\begin{cases}1/\sqrt{H_{ii}},&H_{ii}>0,\\1,&H_{ii}=0.\end{cases}
$$
负对角或非有限数据被拒绝。传入的额外 diagonal 仅用来报告与 $H_{ii}$ 的差，不能改变尺度。零列不把其对角补成任意正小数。

与冻结 fd2d_dense_normal_lm.cjs 一样，先平均 $H_{ij},H_{ji}$，再分别按两个乘法顺序缩放，最后平均两份缩放条目，构造对称工作存储。未平均的实际缩放输入另存，用于报告原方程残差；每种实际舍入调整独立报告。

设 $S=\operatorname{diag}(s_i)$，$P$ 将径向块顺序补回原顺序。理想实数记号中
$$
A=P^TSHS P,\qquad \widehat g=P^TSg.
$$
实际 $A$ 是上段明确的浮点对称化结果。对同一个 $\lambda>0$，
$$
(A+\lambda I)q=-\widehat g,\qquad d=SPq.
$$
$\lambda$ 的含义不变，没有隐式 pivot floor、额外 shift、伪逆或截断方向。一次给定 $\lambda$ 失败只报告失败；增加阻尼须由原 LM 明确发起。

精确正半定 $H$ 加 $\lambda I$ 是 SPD。这个理论不自动消除实际舍入或输入错误；实际每个 field pivot 和 border Schur 都必须真正为正且有限。

## 3. 带状 Cholesky 不产生带外填充

记径向部分为 $B=A_{ff}+\lambda I$。按块编号从小到大消元。若 $i-j>3$，则 $B_{ij}=0$，且
$$
L_{ij}=\left(B_{ij}-\sum_{k<j}L_{ik}L_{jk}\right)/L_{jj}.
$$
由已处理列的带宽归纳，全部 $k<j$ 满足 $i-k>3$，故 $L_{ik}=0$；因此 $L_{ij}=0$。因子仍只有三块半带宽。

实现逐标量算同一递推，每行只存本块及前三块，stride=$4b$，起点
$$
\max(0,(\lfloor i/b\rfloor-3)b).
$$
内积采用补偿求和。实际 pivot $p_i$ 必须满足 $0<p_i<\infty$；否则返回 band_cholesky 失败、实际 pivot/编号/阻尼。下三角除法结果也必须有限。原数组全程不改。

## 4. 单个 global border 的准确 Schur 公式

完整工作系统为
$$
\begin{pmatrix}B&v\\v^T&c\end{pmatrix}
\begin{pmatrix}q_f\\q_c\end{pmatrix}
=-\begin{pmatrix}\widehat g_f\\\widehat g_c\end{pmatrix},
\qquad c=A_{cc}+\lambda.
$$
同一个带状因子解两组 RHS：
$$
u=-B^{-1}\widehat g_f,\qquad t=B^{-1}v.
$$
定义
$$
\gamma=c-v^Tt,\qquad
q_c=\frac{-\widehat g_c-v^Tu}{\gamma},\qquad
q_f=u-tq_c.
$$
代回第一行、第二行，分别得到 $Bq_f+vq_c=-\widehat g_f$ 与 $v^Tq_f+cq_c=-\widehat g_c$，故等价于完整系统。

完整矩阵 SPD 时，对 $(-B^{-1}v,1)$ 的二次型恰为 $\gamma>0$。反过来，$B$ SPD 且 $\gamma>0$ 的平方完成给出完整 SPD。因此边框检查不可省。代码直接拒绝 $\gamma\le0$ 或非有限，不替换成 epsilon。

零 Jacobian 列的 $H$ 行和 $g$ 分量均为零。原 scale=1 与明确 $\lambda$ 给方向准确零；实际五维全零例子保留此性质。

## 5. 方向、模型量与真实试步

方向返回原 provider 参数顺序。模型量仍是
$$
\ell=g^Td,\quad Q=q^TAq,\quad
R_{\rm pred}^2=R^2+2\ell+Q,
$$
半平方范数的预测下降为 $-\ell-Q/2$。

同时报告工作矩阵残差与未对称平均的原缩放方程残差
$$
(SHS+\lambda I)Pq+Sg.
$$
小核另按原编号直接 dense 点乘检查后者。重排、点积及分解顺序会改变最后浮点位，故只称同一实数系统，不冒方向逐字节相同。

内核不调用 value、不改变参数盒、不消去 R192 坐标。独立 adapter 仅替换线性 backend；其 evaluationNorm、lmStep、runLM 与 helper 函数文本从已冻结 dense 源原样复制，保留全部真实 value、异常、trial trace、全/半/四分试步和阻尼更新。任何接受仍依赖新实际值与原 Armijo；没有因为线性预测较小就接受。

## 6. API 与复杂度

方向核 scripts/fd2d_scaled_band_border_lm_R195.cjs：

~~~javascript
const prepared = kernel.prepareBandBorderNormal(normal, guided.definition);
const direction = kernel.solvePreparedBandBorder(prepared, lambda);
// 同一个 normal 可复用 prepared 改明确 lambda。
const direction2 = kernel.solveDampedNormal(normal, {
  definition: guided.definition, lambda
});
~~~

成功返回 direction、scaledDirection（均原编号）、scale、slope、quadratic、predictedSquaredNorm、predictedReduction、info；失败返回 ok=false 与 phase。结构不兼容/带外非零属于输入错误，直接抛出明确异常。

保原策略的 adapter scripts/fd2d_band_border_lm_adapter_R195.cjs：

~~~javascript
const lm = createBandBorderLM(kernel, guided.definition);
const actual = await lm.lmStep({z, normal, value, lambda, ...originalOptions});
// lm.runLM 也使用同一 backend；不会额外调用 normal/value。
~~~

从 dense 输入扫描全部原 $H$ 仍需 $O(n^2)$，且调用者原 dense normal 仍存在。内核不另造 dense 工作矩阵或 dense 因子。局部带状存储为 $O(Jb^2)$，分解工作为 $O(Jb^3)$；两个 RHS 和单 border 更低阶。未来按原行账本直接累积 band/border 才能去掉原 dense 输入分配，本条没有宣称该 accumulator 已实现。

## 7. 一次真实 193 维对照

不可变输入为 notes/2026-11-12-fd2d-direct-position-R191-curvature-weight02-01.json。按其四份 frozen sources、B32 bundle 构造实际 provider：J12/K7/N64，guide=9.5、weight=.01、nodeShare=.5，193 维。**只实际组一次 normal**，V8 2006ms、16405 行，
$$
R^2=4.384082096786088\times10^{-5}.
$$
同一 $\lambda=.0011111111111111111$：

| 项 | 实际值 |
|---|---:|
| 带外非零数 | 0 |
| 新/旧方向相对 L2 | $3.4267215126552416\times10^{-14}$ |
| 方向最大绝对差 | $2.461138931542095\times10^{-16}$ |
| 原缩放方程独立最大残差 | $3.2526065174565133\times10^{-18}$ |
| 新旧预测 $R^2$ 差 | $6.776263578034403\times10^{-21}$ |
| 新预测 $R^2$ | $.00004101244285920853$ |
| 实际 border Schur | $.005709939853307366$ |

单次 prepare13ms、band solve33ms、dense prepare+solve135ms；不是重复或跨尺寸 benchmark。prepared 数值存储307240B，因子98304B，不含调用者原 dense H。此前同一 normal 的首个 band 调用总71ms，也如实记录，不是另组 normal。

checker 还测试零列、field 非 SPD、border 非 SPD、$10^{-300}$ 带外项的真实拒绝；没有再跑 whole JVP 或 nonlinear trial。adapter 只完成实际 V8 编译和 frozen policy 文本同一核，下一主线真实 LM 才是其实际接入。无 OS 进程，不能填 shell exit=0。

可复现小核为 scripts/fd2d_scaled_band_border_lm_R195_check.cjs，报告 notes/2026-11-12-fd2d-R195-band-border-actual-check-01.json。从保存 fixture 构造 coupled provider 后调用 checkR195(kernel,dense,normal,provider.definition,fixture.lambda) 即可；不需重跑此前 nonlinear 轨迹。
