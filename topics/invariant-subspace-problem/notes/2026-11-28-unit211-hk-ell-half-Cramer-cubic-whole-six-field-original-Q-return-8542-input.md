# 新输入：碰撞整 $\ell=1/2$ 的 Cramer 三次常数域与八条原 $Q$ 方程

日期：2026-11-28。会话：Astra-ISP-8542378f-20261127。

**这是尚未执行的新输入说明。** 已完成的五个固定 $Q$ 结式、$K_2[u]$ 十二次公因式及其二十四次有理范数不重跑。本源仅重建八条原式的必要定义，以新三次式识别已付参数，再在完整常数域中第一次对同一个 $Q$ 返回原方程。结果取决于首次真实输出；本说明不预先宣称排空。

## 1. 已成结果和准确原范围

只取正确 $h=k$、$\ell=1/2$ 的原碰撞图。原物理 $\lambda=1/2$ 整支先前已独立排除，故

$$
K_2=\mathbb Q[\lambda]/(3\lambda^2-2\lambda+1),\qquad
\ell=\frac12,\quad
\xi=1-\lambda,\quad T=\frac{1-\lambda}{2}.
$$

不选某一个复嵌入。沿用已刊整图的原单位

$$
u(u-1)Q(1-Q)M P_{02}\Delta,
\qquad
M=u-u^2-\frac Q4,
$$

以及原恒等式

$$
T_0=J-Q=2M,\quad P_f=4M^2,\quad
P_{02}=-2M(u-2).
$$

因此 $u-2$ 也为单位。$\Delta$ 只由整个正确碰撞 $\Delta=0$ 的独立排除支付；没有从模幂零推支付。这里不倒 $m=u-\ell$、$\Phi$、物理 $D$、新的线性头或权范数。

先行准确结论是
[R150-appendix-unit211-hk-ell-half-original-five-Q-cofactors-and-entire-sextic-u-cover.md](../results/R150-appendix-unit211-hk-ell-half-original-five-Q-cofactors-and-entire-sextic-u-cover.md)。
其唯一首次运行 run46154286626 / job141007395347，实际 6.111232795 秒、44384 KiB、exit 0；整支尚未排空。它在同一原局部化理想中给首一 $g_{12}(u)$，其规范编码 SHA256 是

3714806312a65901fa4cee34d459124cc7ef1cf4d5c10d72faee853fd7f375e7。

其有理范数为非零有理常数乘 $F_6^4$，$F_6$ 是实际完整 QQ 分解的单个六次不可约因子，规范系数编码 SHA256 为

0f8be1fab30e5fc1be7583839d9ce4161bbcd071fb7e4a4b750936713626ba7d。

这些是已付参数的身份，不是本次待重算的目标。原 $\Delta$ 单位的来源：
[R150-appendix-unit211-hk-corrected-entire-Delta-zero-finite-DVR-original-exclusion.md](../results/R150-appendix-unit211-hk-corrected-entire-Delta-zero-finite-DVR-original-exclusion.md)。

## 2. 真正新的三次入口，不倒 $Q$ 线性头

在 $K_2[u,Q]$ 令 $e=u-1$，定义

$$
\begin{aligned}
C&=(2u-13)+(56-19u)\lambda,\\
Z&=(25u-41)+(52-35u)\lambda,\\
A_q&=4-5\lambda,\\
B_q&=(29u-27)+(39-46u)\lambda,\\
C_q&=-u-9+(2u+15)\lambda,\\
r&=4ueC,\qquad L_Q=QZ-r,\\
H_3&=2uA_qC^2-B_qCZ+C_qZ^2.
\end{aligned}
$$

新源第一次逐系数验证原 Cramer 定义的三个恒等式

$$
\begin{aligned}
3\Delta&=A_qQ^2-2eB_qQ+8ue^2C_q,\\
3T_{\rm num}&=MQ L_Q,\\
Z^2(3\Delta)
 -(A_qZQ+A_qr-2eB_qZ)L_Q&=8ue^2H_3.
\end{aligned}
$$

其中 $\Delta=\Phi N_F-S\xi P_f$、
$T_{\rm num}=P_fN_C-P_cN_F$，均直接来自已刊真原恢复。最后一式是多项式组合，整个 $Z=0$ 支保留。这里还没有断言 $H_3$ 单独属于原 Gram 理想：其用途是提供一个短的、可由原定义再生的常数参数。

将 $H_3$ 除其非零 $K_2$ 首项得首一 $h_3$。新源只对这个新三次式的六次有理范数做完整 QQ 因式分解，并逐项乘回。若该范数是已付不可约 $F_6$ 的非零有理倍数，则 $h_3$ 在 $K_2[u]$ 不可约；否则将完整分解保留，不把一个未经证明的常数代数当作域。

随后只比较五个明确定义的候选

$$
h_3^j\overline{h_3}^{\,4-j},\qquad 0\leq j\leq4
$$

与已付 $g_{12}$ 的规范编码身份。源码使用与先行源完全相同的编码：依 $\lambda$ 基指标、$u$ 次数、$Q$ 次数及有理系数排序。匹配只识别已付参数，不执行旧五结式、旧公因式或旧二十四次范数。不能唯一匹配时，源码明确报告参数识别未完成，原支保留。

如果匹配 $j=4$ 或 $0$，只需对应一个完整三次常数域；如果 $0<j<4$，两个完整三次常数域都必须返回。每个域

$$
K=K_2[u]/(h)
$$

具有六个有理坐标，保留全部 $\lambda,u$ 嵌入。没有从一个数值根代替整个域。原 $j$、$4-j$ 重数始终记录，后续只在所有对应剩余域均关闭后才使用幂零提升。

## 3. 原八式只重建必要定义

唯一依赖为

[2026-11-28-unit211-hk-entire-ell-half-constant-field-scaled-original-Q-cofactors-8542.py](2026-11-28-unit211-hk-entire-ell-half-constant-field-scaled-original-Q-cofactors-8542.py)。

冻结 blob：53d57ae6baf7a9fdf3867a95952833a570317797。全源 SHA256：

44b7c44c5e4ba5408a8662e6f2579be23c6bf9effd0d9d2a59993eb827ca79cb。

只取首 10525 字节，截在 paid 初始化之前，前缀 SHA256：

45b9c4dfe94dddfbf2c7118dcf9ca65df0ce8ab163cd80147bc0b8e4cb2fdd86。

AST 只删除旧顶层断言、旧顶层日志/统计增量和旧时钟/资源设置；保留必要的精确算术类及原 Gram 定义。类内真逆元、精确除法与乘回断言继续保留。外层本源独占绝对 180 秒截止和 4 GiB 硬限。它不进入旧八式归一、任何固定结式、公因式或范数尾段。

原八式名称依次为

$$
(E_1,E_{B,e},E_{B,o},N_1,N_{B,e},N_{B,o},P_{B,e},P_{B,o}).
$$

它们仍以同一个 $H=MQ\Delta$ 的真原 Gram 构造，原缩放次数依次为 $(2,2,2,3,3,3,3,3)$。真实 dual 平方使用 $v_m(d,d)_1=2d_0d_1$。没有旧错误 compact mean 来源。

每条原有理式写为

$$
R_i=\frac{n_i(Q)}{\delta^{a_i}},\qquad \delta=1-Q.
$$

所有 $n_i$ 在整个常数域中逐项专门化，保全部 $Q$ 最高项下降。原 $\rho$ 二次扩张中的偶、奇两部分都保留；没有挑选 $\rho$ 符号。

## 4. 完整常数逆和已付 $Q$ 主分量

常数代数的所有逆元通过 $K_2[u]$ 的完整扩展欧几里得计算得到，随后在全部六个有理坐标内乘回 $1$。只有新六次范数的完整不可约性成立后才把它称作域。若发现非单位，源码输出其完整常数因子并保留该组件，不无证选择一个根或一个商。

在 $K[Q]$ 定义

$$
U(Q)=Q(1-Q)M(Q)\Delta(Q).
$$

若它在整个常数组件中恒零，该组件与本图的原单位局部化没有交集，可以直接保留准确的“已付权因子整组件为零”结论；不冒称执行了八原式目标。

否则对每个 $n_i$ 反复计算与 $U$ 的真公因式，将同一个原已付因子的全部主分量重数取尽：

$$
n_i=d_i\widetilde n_i,\qquad d_i\mid U^{N_i}.
$$

每次完整乘回 $n_i=d_i\widetilde n_i$，且每个取出的因子实际整除原 $U$。不能仅删一个平方自由因子后遗留重数，也不能删除任何未知 $Q$ 首项。所有零多项式原行保留。

这是合法的原单位局部化，不使用 $D$、未知范数、新参数头或任意 $Q$ 根。

## 5. 同一 $Q$ 的完整八源返回

新源第一次在完整 $K[Q]$ 中累积原行 Bézout：

$$
\sum_{i=1}^8 B_i(Q)\widetilde n_i(Q)=g_Q(Q).
$$

每一步返回全部八个坐标，未参与的原行系数为零。若公因式已为 $1$，后续原行不必继续做欧几里得，但此前八条原定义都已构造，完整八源身份仍逐项返回。

设 $N=\max_iN_i$。因为 $d_i\mid U^N$，定义

$$
\Omega_i=B_i\,\frac{U^N}{d_i}\,\delta^{a_i}.
$$

不取新的逆，源码完整验证

$$
\boxed{\ \sum_{i=1}^8\Omega_i R_i=U^N g_Q.\ }
$$

实际校验先乘共同 $\delta^{\max a_i}$，逐 $Q$ 系数、每个系数全部六个有理坐标乘回。因此这不是只在选定根上的返回，也不是只返回归一后的方程。

若 $g_Q=1$，原 $U$ 已付，整个常数域的全部原 $Q$ 解排除。若 $g_Q$ 非恒定，全部剩余 $Q$ 多项式及其重数保留，本源只给新的必要覆盖。零原行或未识别常数分量均不被当作排空。

## 6. 原十二次参数重数的最后提升

已付 $g_{12}\in I_{\rm orig}$。若所有实际因子 $h$ 的整个剩余域均由上节原单位返回关闭，则

$$
I_{\rm orig}+(h)=(1)
$$

在本图的原单位局部化环 $R$ 中成立。这里不能断言单个 $h$ 在整个 $R/I_{\rm orig}$ 中幂零。若 $0<j<4$，先由 $h_3,\overline{h_3}$ 互素及 $g_{12}=h_3^j\overline{h_3}^{\,4-j}\in I_{\rm orig}$ 得 CRT 分解

$
R/I_{\rm orig}\ \cong\
R/(I_{\rm orig},h_3^j)\ \times\
R/(I_{\rm orig},\overline{h_3}^{\,4-j}).
$

在第一个分量内才有 $h_3^j=0$，第二个分量内才有 $\overline{h_3}^{\,4-j}=0$。各剩余域的原返回给相应 $I_{\rm orig}+(h)=(1)$；若 $1=a+hb$、$a\in I_{\rm orig}$，有限几何级数给 $1-(hb)^n\in I_{\rm orig}$，因此该 $h^n$ 主分量为零。所有主分量都关闭后，CRT 才给 $I_{\rm orig}=(1)$。若 $j=0$ 或 $4$，只有单个主分量，直接使用其准确指数。

不需要把 $g_{12}$ 先替换为无证明的平方自由方程，也不需要裸模 $D$ 幂零提升。

本次只涉及正确碰撞的整 $\ell=1/2$；其余权支仍保留。原八式既含均值、jet 与个别 N/P，最终若真返回单位，其来源严格是这些同点原式。是否全部完成，只按首次实际记录判断。

## 7. 冻结源、预算与输出

新源：

[2026-11-28-unit211-hk-ell-half-Cramer-cubic-whole-six-field-original-Q-return-8542.py](2026-11-28-unit211-hk-ell-half-Cramer-cubic-whole-six-field-original-Q-return-8542.py)

冻结 blob：41453eb91fc9f2d1a8104cfa923acccbedd25f92。

SHA256：3f64a0378d7f7ef568786a73e062ab66bdc83e68978d1f5c37d1a0fe11698a0c。

UTF-8：18007 字节。单一首次预算：180 秒 / 4 GiB，外层 195 秒。仅上述一份固定依赖；不访问网络，不恢复任何系数缓存。输出只有次数、全部分量状态、参数定义、字节数、SHA 与小乘回统计。没有可重算大系数载荷。

当前状态：源码及输入已构造并静态自查，**尚未执行**。首次真实日志必须分别说明新三次身份、参数识别、各完整常数域返回及仍未关闭的组件；工作流外层绿色不替代数学返回。
