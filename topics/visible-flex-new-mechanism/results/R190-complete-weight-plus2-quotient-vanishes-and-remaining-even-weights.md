# R190：完整权 +2 商的消失与剩余偶权清单

日期：2026-11-15。**纸面已证明，复用既有公开原式。** 本稿不编译新的研究目标，不重新生成 3974 个原因子、W、profile 响应或已完成的权 −2 函数核。使用已发布完整导出的几何支撑元数据，以及 R115 的完整两模式原式身份。

结论是

$$
\boxed{U_{2}=R_{2},\qquad H_2:=U_2/(R_2+\mathsf N U_3)=0.}
\tag{1}
$$

结合 R145、R188 和下文的统一支撑界，尚未排除的非零正仿射字符权只可能是

$$
\boxed{\sigma\in\{-8,-6,-4,0\}.}
\tag{2}
$$

(1) 是完整 canonical 成本函数商的结论，不只是静态部分、单个 pure 模式或某个幂尾的结论；(2) 也没有证明列出的四个权实际存在正字符。本文不把响应线性空间等同于实际成本半群，不据此宣告完整第四 period、ruling 或主课题完成。

## 1. 对象、权和来源

记

$$
U=\mathcal U_4,\qquad R=\mathcal R_8,\qquad
R=\operatorname{span}\{\mathcal B_E(\tau):E\in E_8,\ \tau\in W\}.
$$

全部对象保留同一 canonical 目标、同一个真实右锚、完整两个复相位模式和实际历史。正仿射作用 $\mathsf P_{H,d}$ 采用 [R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 的方向：

$$
S=(h,k,\omega)\longmapsto S_H=(Hh,k,\omega/H),\qquad H>0.
\tag{3}
$$

本稿首先只用 $d=0$。对 profile 算子的真权投影记为 $\Pi_\sigma$，即

$$
\mathsf P_{H,0}\Pi_\sigma=H^\sigma\Pi_\sigma.
\tag{4}
$$

一个 $j$ 阶 profile jet 权为 $-j$，右 Volterra 原函数增加权 $1$，乘 $\xi$ 增加权 $1$。右锚和支撑按真实正缩放共同输运；不重新选择原函数常数。有限 Laurent 表示保证这些真权投影在相关有限真实函数空间及其不变商上有定义。W 的仿射不变性来自 R89 §3，R 的不变性来自完整响应的协变。

局部第三势与完整第四局部密度采用 [R109](R109-local-density-of-the-complete-fourth-quotient.md)：

$$
N=N^{[0]}+N^{[2]},\qquad n-D_sN\in W,
$$

$$
L=L_0+L_2+L_4=v-\mathcal B_mN,\qquad m=m_0+m_2,
\tag{5}
$$

其中方括号和下标 $0,2,4$ 是**几何导数权**，不是 profile 真权。准确装配式为

$$
\begin{aligned}
L_0&=v_0-\mathcal B_{m_0}N^{[0]},\\
L_2&=v_2-\mathcal B_{m_0}N^{[2]}-\mathcal B_{m_2}N^{[0]},\\
L_4&=v_4-\mathcal B_{m_2}N^{[2]}.
\end{aligned}
\tag{6}
$$

这里的 $v$ 是先对真实场微分、代入实际 history RHS、最后才将累计 second/third 值置零得到的局部生成元；没有把历史导数置零。

### 1.1 完整原因子已发布

使用 [完整原因子 actual 记录](../notes/complete-original-derivative-factor-export-actual-20261114.md)：

- run：43651096112；
- source：2259b57065cfad67682f4c4319885fd5334c4f76；
- producer：literature_local_fourth_derivative_factors.py；
- producer SHA-256：02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf；
- 导出：notes/actions-43651096112-1-local_fourth_derivative_factors/local-fourth-derivative-factors-original-expressions.json.gz；
- gzip：2132064 bytes，SHA-256 9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a；
- raw：11864540 bytes，SHA-256 58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3。

它保存未降模 W 的完整 $N^{[0]},N^{[2]}$ 和两模式完整 $v_2,v_4$，共 3974 个原根；本稿不从旧静态降模代表反推未保存的导数势。

几何键的固定顺序为

$$
(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss}).
\tag{7}
$$

对这样的键 $a=(a_0,\ldots,a_9)$，令其**几何缩放指数**

$$
\kappa(a)=a_0-a_2+a_3+a_5+a_8.
\tag{8}
$$

式 (3) 使 $h$ 及其每个 $s$ 导数乘 $H$，$k$ 及其导数不变，$\omega$ 乘 $H^{-1}$；$\log h$ 变为 $\log h+\log H$。因此一个已存几何单项缩放后为 $H^{\kappa(a)}$ 乘 $\log H$ 的有限多项式。

逐条读取已发布的 potential_records 与 local_generator_records，得到下表。它只是完整既存几何键的清单事实，不是新的 profile 评价或归约。

| 完整原对象 | 原根数 | 最大几何指数 $\kappa$ |
|---|---:|---:|
| $N^{[0]}$ | 79 | 1 |
| $N^{[2]}$ | 93 | 0 |
| $v_2$，每个完整模式 | 665 | 1 |
| $v_4$，每个完整模式 | 1236 | 0 |

此时不能直接把 N 的几何指数冒充其 profile 真权。第 3 节将支付两者之间必须保留的常势差。

### 1.2 静态权 +2 的既有原式身份

[R115](R115-static-local-fourth-top-weight-payment-and-unresolved-next-block.md) 已证明所用静态降模代表的权 +2 只有几何单项 $h^2k^2$，且其系数准确为

$$
(L_0)_{h^2k^2,+2}=-\frac18\mathcal B_{p_2}(W_7).
\tag{9}
$$

其公开生产者使用逐系数模 W 的静态势代表。恢复本稿的未降模 $N^{[0]}$ 只加回 W 值势，故密度只相差 R 值项；(9) 对本稿所用原势准确推出

$$
\boxed{\Pi_2 L_0(S)\in R_2\quad\text{对每个 }S.}
\tag{10}
$$

这里 $W_7$ 是 v2 保留原索引 7 的完整第三模板，原 SHA-256 为 586788dc0fcf4aec7cc329277836c89e82ddb46a5739d71dfcd154cdece83a56。R115 的两个模式都已从原式回代为零；本稿不重新计算该身份。

原权 +2 小报告为 run 43645177423、source 2f1b809c0b0abb7a26303d36940edc203815f872 下的 local-fourth-quotient-weight-+2.json，4329 bytes，SHA-256 874c683855c9aef86a45602fc06cc3357fc5cff8bd7eeac64ecdae5150decd81。主摘要曾因自身体积输出限制而使用 fallback，不影响这个已单独保存的完整原式身份。

## 2. 局部 n、v 的缩放协变保留真实历史

R89 的完整传递协变适用于实际累计值 A、T、V，并保留其实际导数。R109 的真实演化是

$$
A'=m,\qquad T'=n-m\circ A,
$$

$$
V'=v+\mathfrak F(A,n)-m(AD,AD)-4m\bigl(\phi,T(\phi;D)\bigr).
\tag{11}
$$

$\mathsf P_{H,0}$ 与完整算子组合及这些极化交换。比较 (11) 在 $A=T=0$ 时的真实 RHS，得到

$$
n(S_H,\mathrm{jets}_H)=\mathsf P_{H,0}n(S,\mathrm{jets}),
$$

$$
v(S_H,\mathrm{jets}_H)=\mathsf P_{H,0}v(S,\mathrm{jets}).
\tag{12}
$$

这是从先求导的完整历史公式取局部值，不是先冻结零历史再求导。由于 (3) 不改变几何导数权，(12) 对 $v_0,v_2,v_4$ 分别成立。

现在用一个简单的有限指数事实：若有限几何表达式的全部指数 $\kappa\le K$，其在固定状态和 jets 上的缩放只含

$$
H^\kappa(\log H)^j,\qquad \kappa\le K.
$$

这些函数与任意 $H^\sigma$、$\sigma>K$ 线性独立。可置 $t=\log H$，化为不同特征指数的有限指数多项式独立性；这也可在每个真实线性坐标上逐项证明。因此严格协变 (12) 与第 1 节支撑表给

$$
\boxed{\Pi_\sigma v_2=0\quad(\sigma>1),\qquad
\Pi_\sigma v_4=0\quad(\sigma>0).}
\tag{13}
$$

这一步没有用不完备正规形判零，也没有把几何系数看成独立可达成本。

## 3. 势的缩放差及基点常数必须一起处理

### 3.1 沿所有真实水平路径的常势引理

考虑固定 $H>0$ 的差

$$
\Delta_H(S,u,w)=N(S_H;Hu,w)-\mathsf P_{H,0}N(S;u,w),
\qquad u=h_s,\quad w=k_s.
\tag{14}
$$

R109 的 $n-D_sN\in W$、(12) 以及 $\mathsf P_{H,0}W=W$ 给

$$
D_s\Delta_H\in W
\tag{15}
$$

对每条真实水平路径成立。以下等式先放在包含全部势系数及其缩放像的有限第三算子空间模 W 中。

N 只含静态项和速度二次项。令 $\psi$ 是 (14) 的任意真实商坐标。因加速度 $a=h_{ss},b=k_{ss}$ 在一个局部状态上可独立指定，$D_s\psi=0$ 的加速度系数迫使

$$
\partial_u\psi=\partial_w\psi=0.
$$

余下 $D_s\psi=0$ 变为

$$
X\psi=Y\psi=0,\qquad X=\partial_h,\quad
Y=\partial_k+\frac1{2h}\partial_\omega.
$$

而

$$
[X,Y]=-\frac1{2h^2}\partial_\omega.
$$

故 $\partial_\omega\psi=\partial_k\psi=\partial_h\psi=0$。状态域 $h>0$ 连通，得 $\Delta_H$ 在商中只依赖 H，是一个常算子类 $C_H$。按几何导数权分开：

$$
[N^{[2]}(S_H;Hu,w)]
=\mathsf P_{H,0}[N^{[2]}(S;u,w)],
\tag{16}
$$

$$
[N^{[0]}(S_H)]-\mathsf P_{H,0}[N^{[0]}(S)]=C_H.
\tag{17}
$$

方括号在本节始终表示模 W。特别，(17) 一般不能直接改写成未经修正的协变。

### 3.2 已选原势在参考常态的准确零值

这里可以使用的零值只有一个明确的参考态，而非任意路径端点：

$$
S_*=(1,1,1),\qquad \boxed{N^{[0]}(S_*)=0.}
\tag{18}
$$

(18) 来自原生产者的定义，不来自某次数值代入：

- raw_decomposition 取 $P_h=\int_1^h\ell_h(t,k,\omega)\,dt$，故 $P_h(1,k,\omega)=0$；
- endpoint_potential 取 $F_*(k,\omega)=\int_1^k a_*(v,1)\,dv+2\int_1^\omega b_*(k,t)\,dt$，故 $F_*(1,1)=0$；
- $N^{[0]}=P_h+F_*$，速度势 $P_{\rm acc}=N^{[2]}$ 在常态为零。

原几何积分出现 $\log h$ 时，其在 $h=1$ 仍为零。源中的 integrate_h_from_one、endpoint_potential 和固定 base $h=k=\omega=1$ 明确保留了这些常数。

R109 关于“一般路径的 N 初值不能删”的说明仍然完全有效。(18) 不是把每条路径的首末 germ 改成 $S_*$，也不把不同状态的势值重置为零。

### 3.3 高权势真实落入 W

由 (16) 和 $N^{[2]}$ 的最大几何指数 $0$，按第 2 节指数比较，

$$
\boxed{\Pi_\sigma N^{[2]}(S;u,w)\in W_\sigma\quad(\sigma>0).}
\tag{19}
$$

对 (17)，先投影到真权 $\sigma$，再分别取 S 和 $S_*$ 相减。设

$$
f_\sigma(S)=[\Pi_\sigma N^{[0]}(S)].
$$

得到

$$
f_\sigma(S_H)-f_\sigma((S_*)_H)
=H^\sigma\bigl(f_\sigma(S)-f_\sigma(S_*)\bigr).
\tag{20}
$$

左侧只有指数不超过 1 的有限 Laurent/log 缩放项。若 $\sigma>1$，指数比较迫使

$$
f_\sigma(S)=f_\sigma(S_*).
$$

最后用 (18)，右侧是零。因此

$$
\boxed{\Pi_\sigma N^{[0]}(S)\in W_\sigma\quad(\sigma>1).}
\tag{21}
$$

(19)、(21) 是**真实函数模 W**的结论，不要求原 DAG 自身没有高权项；也没有宣称全部 $N^{[2]}$ 属于 W。只有本稿指明的高权范围已被支付。若省略 (18)，(21) 最多只能得到“常算子模 W”，不足以直接进行下一节的低阶装配。

## 4. 完整几何导数权 2、4 的 profile 权 +2

采用 R73 八矩次序

$$
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1).
$$

其八个单位算子的真权依次为

$$
(-1,0,1,-3,-2,-2,-1,0).
\tag{22}
$$

因此 $m_0$ 使用的方向权至多 1。唯一正权方向为 $p_2$，而 R73 原点态式 $p_2=-kh/2$ 没有速度项，所以 $m_2$ 使用的方向权至多 0。这里不是把矩阵密度的几何系数也计入 profile 权。

完整响应的协变和双线性性给

$$
\Pi_2\mathcal B_m(N)
=\sum_E\mu_E(S,\mathrm{jets})\,
\mathcal B_E\bigl(\Pi_{2-w(E)}N\bigr),
\tag{23}
$$

其中 $\mu_E$ 是真实几何标量系数，$w(E)$ 为 (22)。逐项应用于 (6)：

1. $\Pi_2v_2=\Pi_2v_4=0$，由 (13)。
2. 对 $\mathcal B_{m_0}N^{[2]}$，输入权 $2-w(E)\ge1$，由 (19) 属于 W。
3. 对 $\mathcal B_{m_2}N^{[0]}$，输入权 $2-w(E)\ge2$，由 (21) 属于 W。
4. 对 $\mathcal B_{m_2}N^{[2]}$，输入权同样至少 2，由 (19) 属于 W。

每项因此都在真响应空间 R 中，得到

$$
\boxed{\Pi_2L_2(S,\mathrm{jets})\in R_2,\qquad
\Pi_2L_4(S,\mathrm{jets})\in R_2.}
\tag{24}
$$

全部符号按 (6) 保留；因最终每项独立在 R，结论不依赖将这些减号误作某种负成本实现。

## 5. 同一八矩规范化、全部 IBP 和真实 span

[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R163](R163-complete-normal-coefficient-cocycle-and-single-weight-character-head.md) 的参考状态为

$$
S_i^*=(1,k,d+k),\qquad d\in(0,1,-1,2),\quad k\in(0,1),
$$

并使用同一线性映射

$$
\Gamma(M)=\sum_i a_i(M)L_0(S_i^*).
\tag{25}
$$

由 (10)，对每个 M 有

$$
\Pi_2\Gamma(M)\in R_2.
\tag{26}
$$

所以完整归一化同时保留

$$
F_0=L_0-\Gamma(m_0),\qquad
\widetilde L_2=L_2-\Gamma(m_2),\qquad L_4,
\tag{27}
$$

并由 (10)、(24)、(26) 得三者的 +2 投影均逐点在 R 中。

再执行 R129 的完整水平分部积分。它只对几何系数作线性组合与 $X,Y$ 微分；profile 真权投影与这些操作交换。一个取值于固定有限空间 $R_2$ 的状态函数，其状态导数仍取值于 $R_2$。所有端势仍是原来的正几何导数权势，在实际平坦 germs 上为零。因此正规式的十四族状态系数全部满足

$$
\Pi_2F(S)\in R_2.
\tag{28}
$$

这里保留了三个加速度二次项、两个面积型项、五个速度四次项以及静态与全部速度二次项，没有由少数高层族外推完整密度。

R130 的真实 span 定理给

$$
U=R+\operatorname{span}\{F(S):F\text{ 为十四族},\ S\}.
$$

投影到 +2 并用 (28) 得 $U_2\subseteq R_2$。反向包含已由 R105 的真实响应构造支付，故 (1) 成立。特别，任何杀 R 的真实权 +2 仿射字符都为零；这里连正性假设都不需要。

## 6. 完整 canonical 第四成本的统一权支撑界

为了使“剩余偶权”清单不依赖尚未执行的新 head，直接用 R105 的无移动 $\xi$ 极点恢复式估计所有完整成本的 profile 权。

初阶分子为

$$
V_{Y_f}=\left(-\frac{f'}2,0,hf-\frac{hz-k}{2}f'\right),
\qquad z=\xi+\omega.
$$

故其全部 profile 权在 $[-1,0]$。真实 $s$ 微分、协变标架微分以及真实 $s$ 历史积分只改变几何系数，不扩大 profile 权区间。

设两输入分子的权区间之和为 $[L,U]$。R105 的式 (1)–(3) 给：

| 中间对象 | profile 权包含于 |
|---|---|
| $J,T_s$ | $[L,U]$ |
| $T_\xi$ | $[L-2,U-2]$ |
| $T_{s\xi}$ | $[L-1,U-1]$ |
| $B=J/(2h)$ | $[L,U]$ |
| $P=-(2h)^{-1}I(T_\xi)$ | $[L-1,U-1]$ |
| 完整 characteristic RHS $\mathcal R_H$ | $[L-1,U+1]$ |
| $\eta_0$ | $[L-2,U-1]$ |
| 新分子 $V_{\rm new}$ | $[L-2,U+1]$ |

例如 $K_0$ 是 $\xi$ 的至多二次多项式，$\lambda$ 与 $e=hz-k$ 至多一次；R105 已在 $\mathcal R_H,\eta_0,V_{\rm new}$ 中准确消去了移动的 $z^{-1},z^{-2}$ 项。因此表中没有未经控制的移动极点权。这是对完整原式的区间包含，可以是非锐界。

逐阶得到

$$
\operatorname{wt}(V_1)\subseteq[-1,0],\qquad
\operatorname{wt}(V_2)\subseteq[-4,1],\qquad
\operatorname{wt}(V_3)\subseteq[-7,2].
\tag{29}
$$

第四 forcing 的两类配对是 $V_1,V_3$ 和 $V_2,V_2$，二者输入权区间之和都包含于 $[-8,2]$。再用表中 RHS 行：

$$
\boxed{\operatorname{wt}(U)\subseteq[-9,3]\cap\mathbb Z.}
\tag{30}
$$

(30) 保留全部右原函数常数和实际历史，适用于完整 canonical 成本，而不只适用于局部零历史生成元。

R127 将尚存的正闭锥障碍缩成一个单整权正仿射字符；R145 证明该权必须为偶数。因此在本稿前候选权只有 $-8,-6,-4,-2,0,2$。[R188](R188-no-nonzero-positive-affine-character-at-weight-minus2.md) 已排除非零正权 −2 字符；(1) 排除全部杀 R 的权 +2 字符。故只剩 (2)。对 $-8,-6,-4,0$，本稿不从某个响应下界或某个单列身份推断其完整字符头部或正性。

## 7. 下一完整权的准确选择边界

既有完整五族 A/H 导出的真权元数据表明：权 0 只剩 $\bar A_{hh}$ 的一个原状态系数；其余四族在该权原式为零。第 1 节完整 $v_4$ 的几何指数 0 也只有四个键：

$$
h^{-4}h_s^4,\qquad h^{-3}h_s^2h_{ss},\qquad
h^{-2}h_{ss}^2,\qquad h^{-2}h_sh_{sss}.
$$

这使权 0 成为一个明确的较小完整 head 候选；但 $\widehat Q_4$、三个 $\widehat Q_2$ 系数、静态系数、同一 $\Gamma$ 与平移分母都仍须保留，不能仅处理那一个 A 系数。

尤其 R164 已指出权 0 的协变八矩乘子存在一维齐次自由方向 $p_1+4t_1$。权 −2 的唯一乘子公式不能直接搬到这里。下一实际若需要，应只消费已经保存的完整 N、v、静态与五族原根，新增该权确实缺失的收缩及完整关系；本稿不派发新研究任务，也不把这份输入缩减当作权 0 已结案。
