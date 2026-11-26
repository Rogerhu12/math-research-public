# R618 从接口到实际模型：全平 post 尾、固定 E、全部 2J 核心及完整 Jacobian

日期：2026-11-27；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

本条新增的是可调用的完整高度/均值/位置算子源码及其数学定义，
不是一个已运行的数值结论。没有绑定预想的下一 q，没有 request/workflow，
没有本地科学执行。正常原全 S 续算继续自然运行；任何后继科学输入
必须来自真正结束的原日志。

源码为：

- `scripts/r618_fixed_metric_numerical_chain_20261127.py`：
  同一冻结参考 E 的稳定求值、同分支均值根、完整连接和实际位置目标微分。
- `scripts/r618_growing_post_fixed_metric_height_20261127.py`：
  完整 1130q 原场的零响应嵌入、新 post 字典、真正全平尾、独立 core P0、
  全部 2J 从属高度、完整 τ 路径、全 S Jacobian、系数输出和持帽的真实均值积分。

复用已证 R587、R613、R618 以及已发布的固定 E 身份/零入口说明，
不重做旧内口或旧方向门。下面只写实现所新增的必要连接及实际边界。

## 1. 冻结的是完整连续函数，输出网格不重定义 E

给真正完成的原场 $f_*$、原 $W_*$、literal q、amp、canonical512 定义、
全部原内口/connector/core 定义及 source hashes，冻结

\[
E_*(r)=W_*^2(r)+e_*(r),\qquad
\left\langle\frac{N_*}{u_*}\right\rangle=1.
\]

这里括号仍是同一个连续角均值，$e'_*$ 仍由同根的
$2\langle wG\rangle/\langle w\rangle$ 定义。
`FrozenTargetIdentity` 的完整 source JSON、数学场 JSON、各自 hash
及合成 target hash 都进入新模型；它另核 literal q、completed origin、
原 amplitude、所有 source 文件以及递归恢复出的原完整 reconstruction。
只给径向节点表不能通过这个身份契约。

原对象也不能由外部任意传入后只贴上述字符串。唯一公开构造入口
`restore_from_frozen_reference` 从冻结 source 原文字取出完整 reconstruction，
从 `all_literal_parameters.original_reconstruction_arguments` 取出原构造参数，
用绑定原 SHA 的 `restore_model` 恰好重建一次，再将这个实际对象与
target/reconstruction/arguments 身份绑定后进入新构造器。
全部原 paid q、knots、forced 定义和内口沿原路径保留；原 ODE/connector/core
重建费用照常累计，没有新做原内 DtN 或旧 readout 门。
任意已构造而无此对象绑定的旧模型会被拒绝。

当前源码提供固定角求积数 `mean_points` 的数值求值器，
其值是上述同一函数的近似，并明确留下连续根、角求积、径向系数、
DtN/ODE 和 roundoff 误差。`mean_points` 与实际位置输出的 N 分离，
同一模型中所有 trial 和输出网格调用同一个均值规则；细化时仍近似同一连续函数。
没有将 trial 高度重新解出的 E 当作冻结参考 E。

旧高度始终按原 canonical512 定义保存，未换回随工作 N 的均值。
把这一个固定原函数的连续角均值转移至 $h$ 只是一种等价记号；
源码保留原未转移的高度表达并直接求 $p_0$。
新增所有 post 项都是正偶余弦，连续均值为零，
所以这种固定记号选择不丢参数导数，也不重定义物理高度。

## 2. 参数空间真增加，而且不在原内尾留下固定有限角带

原 q 有 1130 项。其 $H=q_0$ 和 amp 成为冻结参考的一部分；
其余1129项全部以相对原 q 的响应保留，原 body/forced/compact/core 字段都不删。
固定 $J\ge32$ 为偶数，新增三组独立 post 响应：

1. 原28个 compact 径向函数乘新偶频 $34,36,\ldots,J$。
2. 每一偶频 $2,4,\ldots,J$ 的真正全平解析尾列，定义到真正 $r_c=.22$。
3. 每一偶频 $4,6,\ldots,J$ 的独立 core $P_0$ lift。

另有完整 core homotopy 参数 $0\le\tau\le1$。
排除自由 core $j=2$，是为了保留原固定非圆首谐波
$P_{0,2}=-3\varepsilon/R$；并没有把其他旧参数或新尾部 $j=2$ 响应删掉。
物理幅度保持原 `1e-5`，没有靠降低 amp 达到阈值。

若尾径向多项式取全部次数 $0,\ldots,K$，参数数为

\[
1129+28\frac{J-32}{2}+\frac J2(K+1)
+\left(\frac J2-1\right)+1.
\tag{1}
\]

这只是字典计数；本条没有擅自选定一份科学输入的 $J,K$ 或 q。
高阶空间用 `embed_response` 按频率、径向次数和 τ 原样嵌入，新增系数为零；
参考 E、原 q、amp、cutoff 和真实函数定义保持相同。
角求积或精度细化带来的数值误差变化另行记录，不把浮点逐位相等冒充连续恒等。

### 为什么不能只用旧 compact 新频率

若全部新高频仍只支撑在 $r>.226$，则在开区间 $(.22,.226)$
新空间仍只有原固定有限 post 角带。R617 的有限带障碍在那里没有改变。
为此新增下面的全平解析尾，而不是把有限口以下设零。

还要避免所有新频率在 $r=.65$ 同时被迫有零二-jet：
原 compact 在该处结束，原 R602 correction 的 cutoff 从该处开始。
新的独立 $P_0$ lift 因此要求其 cutoff 左端严格小于 `.65`，
与 compact 的开支撑重叠。这个要求在构造器内检查；
它没有修改已经发布的原 R602 cutoff，也没有改变零响应原场。

## 3. 真实全平解析尾与它的非零强迫源

令 $u=\ell/(r-r_c)$，$x=(r-r_c)/(r_b-r_c)$，
$r_a\ge r_0=.30$、$r_a<r_b$，$r_b$ 在 core 前。
用原 C∞ step 取 $\chi=1$ 于 $r\le r_a$、$\chi=0$ 于 $r\ge r_b$。
对 $0<a\le40$ 和整数 $k\ge0$，定义

\[
T_k(r)=\chi(r)x^k
\exp\left[-\frac{u^2-u_a^2}{a}\right],\qquad
u_a=\frac\ell{r_a-r_c},\qquad T_k(r_c)=0.
\tag{2}
\]

在 $r_c<r\le r_a$，记 $G=\exp[-(u^2-u_a^2)/a]$，则

\[
G'=\frac{2u^3}{a\ell}G,\qquad
G''=\left(\frac{4u^6}{a^2\ell^2}
-\frac{6u^4}{a\ell^2}\right)G.\tag{3}
\]

源码把这些项与 $x^k$、$\chi$ 的全部0/1/2阶导数作真实乘积，
再乘角余弦，得到 $f,f_r,f_{rr},f_\theta,f_{\theta\theta},f_{r\theta}$。
任何固定阶径向导数都是有限多项式因子乘 Gaussian，
所以在 $r_c$ 延拓为真正 C∞ 全平函数。
原尾 $W=Ae^{-u(2-\sin u)}$ 满足

\[
Ae^{-3u}\le W\le Ae^{-u},
\]

任意固定 $W$ 的逆幂和任意固定阶导数，只增加多项式及 $e^{Cu}$ 因子。
因此每个有限尾响应仍属于 R587 的快速全平类 $\mathcal I(W)$，
同根内帽变量的全平结论可以用于这些真实新高度。
这个说明不是一个 uniform-$J$ 非线性逆定理。

这些新列**不宣称是旧齐次解**。其真实源逐项输出为

\[
\boxed{L_jT_k=rW T_k''+rW'T_k'-j^2W'T_k.}\tag{4}
\]

若之后采用 R618 的 affine forced-DtN 消元，(4) 是需要真正消费的非齐次源；
它不能替代由完整非线性残差要求的源，也不能因为已知旧齐次 mouth
就把 affine 项设成零。源码 `exact_tail_source_observation`
完整返回每个 $(r,j,k)$ 的(4)，并明确这一区别。

原全部 modes2…22 的 true mouths 和原 forced4 mouth 原样保留。
新列是一个从真 cap 到 body 都有定义的解析输入，故它本身没有新 Riccati
积分费；这不免除之后证明其残差或构造真实特解的费用。
有限浮点下若 Gaussian underflow，计数单独记出；
数学定义仍是(2)，不是在那个浮点半径以下改成一个零区间。

## 4. 独立 P0、完整2J及真正原场零入口

新的 core lift 用同一冻结 $W$：

\[
A_c(r)=-\int_r^R\frac{dt}{W(t)},\qquad
f_Q=\chi_c(r)A_c(r)Q(\theta).\tag{5}
\]

在 core 的真开邻域 $\chi_c=1$，所以
$W(f_Q)_r=Q$ 准确成立，$P_0=Q,P_1=0$。
数值源码直接支付一次共享径向积分并使用
$A_c'=1/W,A_c''=-W'/W^2$ 的真实 jets，
不会用一个伪造的有限 core 点代替积分或端式。
积分以 $R-r=\delta y^{1/(1-\alpha)}$ 改变量，
并用 $1-t^2=(\delta/d)(2-\delta/d)$ 稳定评价原 core W。
求积 error estimate 仍只是观察，不自动成为 rigorous bound。

令 $T(P)$ 为 R618 的完整连续 core 目标

\[
T(P)=\frac{c(e(P)+2P)P_{\theta\theta}-P_\theta^2+(2c+1)S}{R},
\quad c=\frac\alpha{1+\alpha},\quad
S=\frac12\sum_j j^2p_j^2.\tag{6}
\]

原实际 core $P_{1,*}$ 包括原512 root及原所有2…44 correction。
记 $\Delta_*=T(P_{0,*})-P_{1,*}$。
新旧自由参数的 bare core 增量分别为 $\delta P_0,\delta P_1^{\rm bare}$；
新增解析尾与 compact 的两项都为零，而(5)只给 $\delta P_0$。
实际新增 correction 系数采用

\[
\boxed{\delta c=T(P_{0,*}+\delta P_0)-T(P_{0,*})
-\delta P_1^{\rm bare}+\tau\Delta_*.}\tag{7}
\]

它乘的仍是原真实 $K_c=\chi\delta^{\alpha+2}/[k(\alpha+2)]$。
新高度直接等于**原完整高度**加所有 bare 响应再加 $K_c\delta c$。
所以零响应、τ0 的原高度逐项不动；没有把原512 core 静默改成另一个精确 core。
原 core map 的所有参数影响经过(7)重新归入完整隐式 $e(P)$ 链，
并非冻结了旧 correction 的参数导数。

实际 core 为

\[
P_1=T(P_0)-(1-\tau)\Delta_* .\tag{8}
\]

源码以有限 Laurent convolution 算(6)及它的完整参数导数，
保留每一个正偶频到 $2J$；零频准确恒为零，浮点表达的零频误差另行记录。
这不受旧44模式列表或当前输出网 Nyquist 截断。
输出/mean/core 求积规则都要求 $N>4J$，而位置目标保留每个当前可分辨奇频。

R618 已证的核心残差在完整 τ 路径上仍为

\[
D_R=R(1-\tau)\left[
\Delta_*-\frac{\langle\Delta_*/u^3\rangle}{\langle u^{-3}\rangle}
\right].\tag{9}
\]

代码同时算完整 $D_R$ 和(9)的差，不删除 core 行来伪装通过。
选τ1才到达目标 core map；数值根/求积/roundoff 的差额仍待验证。

### τ未到1时也保留真正的 ζ′ 导数

固定 $e_{*,R},e'_{*,R}$ 不变，任意τ均使用

\[
\zeta_R=\frac{e(P_0)-e_{*,R}}2,\qquad
e'_{\rm eff}=-2\frac{
\langle P_1/u^3\rangle+\langle P_{0,\theta\theta}/u\rangle/[R(1+\alpha)]}
{\langle u^{-3}\rangle},\qquad
\zeta'_R=\frac{e'_{\rm eff}-e'_{*,R}}2.\tag{10}
\]

只有τ1时才可代入 R618 的简化 $S$ 端式。
`core_direction` 在任意τ对(10)的分子、分母、$u$、隐式 $e(P_0)$、
全部 $P_1$ 和τ项同时求导；并返回整个 $\delta D_R$。
因此未完成的 core homotopy 没有偷用已经到τ1的端式。

## 5. 真固定 E 的 body 连接与完整离解链

写 $p_0=-W+s$、$d=s+f_r$，$p=-W+d$，$q=f_\theta$，$t=f_{\theta\theta}$。
用 split形式计算

\[
u^2=1+(e_*-1)+2Wd-d^2-\frac{p^2q^2}{b^2},
\qquad b^2=r^2-q^2.\tag{11}
\]

内尾求 $\lambda=s/W$，先把 turning 方程除 $W^2$ 前有理化，
同时存储 $(e_*-1)/W^2$，不以两个接近1的数相减制造信号。
core求 $\zeta=Ws$，以 $v=\zeta+Wf_r$ 写
$u^2=e_*+2v-v^2/W^2-p^2q^2/b^2$。
中段直接使用 $s$。以上只是同一个均值根的稳定变量。

令

\[
C=E_*t+rp,\quad B=f_{r\theta}-q/r,\quad
M=r+pt-q^2/r,\quad \omega=r^2/(u^3b^3),
\]

及

\[
K=(e_*+Wd)t+rd-Wq^2/r,\qquad
Q=E_*B^2+W'K+\tfrac12e'_*M-Cf_{rr}.\tag{12}
\]

R618 的真正均值径向导数和残差，在消掉 $2WW'$ 的大项后变成

\[
s'=\frac{\langle\omega Q\rangle}{\langle\omega C\rangle},\qquad
D=C(s'+f_{rr})-E_*B^2-W'K-\tfrac12e'_*M,\qquad R=\omega D.
\tag{13}
\]

这两式直接进入源码，不用点态 $C^{-1}$。
平均 $c_0=\langle\omega C\rangle$ 的符号取自同一参考场，允许正或负；
若声明的括号端点、正域或同符号导数失败，就给真实未解析状态，
不寻找另一个方便的均值根。当前端点和尝试点的检查只是浮点分支观察，
不是整个连续括号上的区间单调性证明。

对每个实际六-jet方向 $H$，先由 R618 的隐式链求 $\delta s$，
再保留

\[
\begin{aligned}
\delta K&=W\delta p\,t+(e_*+Wd)H_{\theta\theta}
+r\delta p-2WqH_\theta/r,\\
\delta Q&=2E_*B\delta B+W'\delta K+\tfrac12e'_*\delta M
-\delta C f_{rr}-CH_{rr},\\
\delta s'&=\frac{
\langle\delta\omega Q+\omega\delta Q\rangle
-s'\langle\delta\omega C+\omega\delta C\rangle}{c_0},\\
\delta R&=\delta\omega D+\omega\delta D.
\end{aligned}\tag{14}
\]

这里 $\delta E_* = \delta e_* = \delta e'_* =0$。
每一方向的 $\delta f$ 包含(7)的完整隐式 core 根、所有2J项、
新解析尾、新 reciprocal-W lift 及τ项，不省略任何离解权导数。

mean方向只在固定 `mean_points` 上求一次。
输出角网使用同一个 $s,s',\delta s,\delta s'$，不会在每个输出网重新定义它们。
位置链随后完整使用

\[
\delta W_* = \Pi\left[(\delta b\,\Pi R+b\Pi\delta R)JT
-b\Pi R\,\Pi(\delta a)T\right],\qquad
\delta S=\delta W_*/\sqrt{E_*}.\tag{15}
\]

全 Jacobian 的每个方向都调用这条链。
同一 block 的完整 core 导数在 mean/output 两个网间共享；
没有先计算一个旧截断 Jacobian 再丢弃它。

## 6. 分离均值网后，数值 S→η 仍须付实际 primitive/mean alias

源码的离散目标确实是完整 $S_N$，而它的 Jacobian准确微分这个离散表达。
但不能把该目标的条件恒等式当作已经验证的实际离散 metric。
因为即使固定 mean functional 的 root 已解准，输出 N 上

\[
\langle a_N\rangle_N-1
\]

仍可能非零。实 primitive 矩阵删去零模及 Nyquist，因此

\[
D_N\Pi_N(a_N-1)
=(a_N-1)-\langle a_N-1\rangle_N
-\widehat{(a_N-1)}_{N/2}(-1)^k .\tag{16}
\]

同样有 $\langle R_N\rangle_N$ 和 $R_N$ 的 Nyquist 项。
完整连续均值/primitive 的恒等式需要这些误差和其余 alias 预算。
两份源码都明确保留以下同场读数：

- 输出 `mean(a)−1` 和 `mean R`；
- `a−1` 与 R 的 Nyquist 观察；
- “S→η及导数 jets 只是条件恒等观察”的标志；
- “同根、两个 primitive 和 mean alias 尚未付清”的标志。

`evaluate` 因而把 η 命名为 `conditional_eta_identity_observation`。
真正 metric 资格仍需原双步长的实际位置差分、角求积/primitive预算，
以及全部 radial/DtN/ODE/core/roundoff误差。
新增完整系数输出已经把全部正频贡献合并到2J，
并提供 $\widehat W=W-s$、
$\widehat e=e_*+2Ws-s^2$、
$\widehat e'=e'_*+2W's+2(W-s)s'$ 的稳定 split，
供随后同场 R606/R615 扩展消费；本条不独立重跑那个观察门。

## 7. 真实 mean-height 与持帽定位，不把有限口以下设零

均值斜率修正 $s$ 还需要真正积分，才得到完整物理位置。
选择保持原内帽的位置，定义

\[
h(r)-h_*(r)=\int_{r_c}^r s(t)\,dt.\tag{17}
\]

这保留持帽开集；core 处的积分值 $C$ 是整个中央柱的共同平移。
下半片关于 $z=C$ 反射，故两个 core 闭截面仍位于 $C\pm h_{\rm core}$，
中央柱是同一个截面的直母线延拓，长度不变；截面不必是圆。
其角速度长度仍为 $R$，所以横向度量仍是 $R^2d\theta^2$。
原上帽由(17)固定；这个定位没有通过逐时最优刚体对齐
偷换位移要求。

`integrate_mean_height` 实现 body 各段的真实积分及可选的全部参数方向积分。
由于旧有限 DtN evaluator 不能评价真 cap 至有限口之间的所有点，
该段的真实积分及误差必须附 target/response/model/mouth 身份和 `true_tail_evidence`。
输入 tail anchor 本身必须由同一 model SHA 下的真实尾定义产生并接受核对，
不同 Gaussian 参数或字典的 anchor 不能在消费端重新贴成当前模型身份。
源码没有默认零延拓，也不把 SciPy 的 error estimate 当严谨区间。
只有原场零响应时，$s\equiv0$ 是参考定义的准确恒等式，
可以直接返回零积分而不制造一份新的尾部近似。

积分返回值（含这个准确零入口）还绑定完整 response SHA、全部实际径向
坐标的 SHA、frozen target 及包含 J/字典/数值规则的 model SHA。
`geometry_with_mean_height` 消费积分时逐一核同一身份，不能把响应 a 的
高度积分与响应 b 的斜率拼成一张位置场。`evaluate` 的 state 另外绑定全部
输出角节点及固定 mean 角节点；`jacobian`、`coefficient_fields` 和 geometry
都核同一 response/target/model/grid。数据形成后若坐标数组被改写也拒绝，
相同节点数或相同 shape 不能替代完整坐标身份。

任意积分点调用的仍是同一原径向场、新完整高度和固定 mean rule。
原 compact preparer 的 N4 仅用于获得与角网无关的原径向系数，
随后真正角函数在声明的 `mean_points` 上评价；N4不是一个科学角求积。
两点原径向 bookkeeping 的额外工作完整计费，临时缓存清理不清零任何计数。

`geometry_with_mean_height` 返回实际 X、完整高度二-jets及相应角/混合位置表达。
平面 $Y_{rr}$ 仍需同一实际位置的直接读出；不会从六个高度 jets
虚构未提供的第三高度导数。第6节的数值 alias 条件继续适用。

## 8. 当前交付的确切范围

这已经是一套可消费完整原高度的模型：真实新增函数进入六 jets，
固定 E 的均值与连接进入 actual S，全部原参数/新参数进入完整 Jacobian，
端部τ0原场和τ1目标之间的所有项均有对应源码。
它保留原全部 mouths、原场所有工作径向点和 fine 点；
全角带可增长，新全平尾不在有限 mouth 以下截断，core lift 与 compact 重叠。

同时，当前没有宣称：任意 trial 的平均根都全域可解、有限角带已经有严格根、
无限角带的统一逆估计已经存在、全部尾强迫已经消去，或 README 已完成。
每个固定有限 J 仍受 R617 限制；这里提供的是实际可增长的响应空间，
不是把有限采样或一个条件接口重新命名为完成。
随后只有在真正原 S 终态到达、具体 J/字典/规则/误差预算绑定并公开发布后，
才可进行新科学计算；全部必要重建、根尝试、拒步、解析尾、lift及 mean-height
求积工作均由累计计数保留。
