# R121：中央基准补偿后，31+1 个真实第四查询可联合支付

日期：2026-11-14。**已证明。** 本稿在 [R101](R101-finite-replication-and-signed-fourth-character-costs.md)、[R102](R102-finite-query-fourth-cost-control-and-cone-quotient.md) 的真实传递与有限复制上，加入 [R117](R117-static-weight-one-reduction-and-reciprocal-costs.md) 的互反圈中央控制。R118 已完成原式 7/8 非零子式，支付完整两模式 $G\notin\mathcal R_8$ 的前提；本稿没有新的研究计算。

结论是：可在同一个共同物理区间、同一个合法归一 $C^\infty$ 三矩圆上，固定 **32 个独立实查询**，使真实有限、同 scalar/frame 端口且 $M=T=0$ 的路径同时匹配它们的任意实目标。31 个查询来自已证独立的真实响应方向，另一个查询湮灭整个 $\mathcal R_8$ 而检测 $G$。所有实际基准成本均保留。

这比分别证明“31 查询可调”和“新增一个查询可调”多支付了一个联调步骤。证明先修正每个固定第三 prototype 的中央基准，再按明确顺序选择两组有限整数，并在乘积盒上应用一次 Brouwer；不需要连续选取介值定理的根。

## 1. 有限真实空间与一个共同查询系统

采用 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md) 的完整 canonical 第四成本空间 $\mathcal U_4$ 和响应空间

$$
\mathcal R_8=\operatorname{span}\{
\mathcal B_P(\tau):P\in E_8,\ \tau\in W\}
\subseteq\mathcal U_4.
$$

它们是同右锚、完整 $-4,-2$ 两模式的真实有限函数空间。R116 由完整 $m=8$ 纯尾投影的准确秩，证明至少存在 31 个真实独立原方向

$$
K_i=\mathcal B_{P_i}(\tau_i),\qquad 1\le i\le31.
\tag{1}
$$

此处只使用这个完整算子独立性下界，不把 31 当作 $\dim\mathcal R_8$ 的等号。

R117 的权一商公式与 R118 的真非成员证书给一个非零商方向。选择实线性泛函

$$
\lambda:\mathcal U_4\longrightarrow\mathbb R,\qquad
\lambda(\mathcal R_8)=0,\quad \lambda(G)\ne0.
\tag{2}
$$

可令 $\lambda=\ell\circ\Pi_1$，其中 $\Pi_1$ 是真实 profile 权一投影，$\ell$ 分离 $G$ 与该权的完整响应空间。R105 的完整有限 Laurent 表示使 $\Pi_1$ 是真实有限空间上的线性映射，不是对每条实际路径丢弃未付项。

这里 $[G]$ 确实属于实际成本商。R117 的互反族在商中的权一公式为

$$
[\Pi_1 V_{Y_N(h)}]
=2N\kappa(h-h_*)[G]+[\mathcal E(h)],
\qquad \kappa>0,
$$

其中 $\mathcal E(h)$ 与外复制整数 $N$ 无关。固定一个 $h\ne h_*$，对两个连续整数 $N,N+1$ 的实际成本作线性差，得到非零倍的 $[G]$。由于 $\Pi_1\mathcal U_4\subseteq\mathcal U_4$ 及 $\mathcal R_8\subseteq\mathcal U_4$，这也直接给 $G\in\mathcal U_4$。这只是 span 的论证，没有把成本的负号当作可直接行走的路径。

先固定后文需要的有限小控制族、真实连接及其紧 scalar 包络，再选共同物理区间 $I$。按 R105 与 [R96](R96-single-profile-faithfulness-for-affine-Volterra-spaces.md)，可在这个 $I$ 上取同一个非退化、归一、满足三条矩约束的 $C^\infty$ profile 圆，并以有限模式实/虚部查询忠实表示 $\mathcal U_4$。因此 (2) 可表示为这个固定圆上的一个固定实查询线性组合。

另选固定查询映射

$$
Q:\mathcal U_4\longrightarrow\mathbb R^{31}
$$

使

$$
\mathsf K=(Q(K_1)\ \cdots\ Q(K_{31}))
$$

可逆。它也由同一个圆的有限查询表示。矩阵

$$
\begin{pmatrix}
\mathsf K&Q(G)\\
0&\lambda(G)
\end{pmatrix}
\tag{3}
$$

可逆，故 $(Q,\lambda)$ 是 32 个独立查询。以后 profile、右锚、$I,Q,\lambda$ 都不随目标或复制次数变化。

本稿下文对任意 $r$ 个独立原响应方向及相应可逆 $r\times r$ 矩阵都成立；取 $r=31$ 得到上述具体下界。

## 2. 先固定全部真实端口与物理包络

固定一个 scalar 常值 germ $g$，所有控制块均取 frame $I_3\to I_3$。$I_3$ 是三维单位 frame，与物理区间 $I$ 区分。

对每个 $i=1,\ldots,r$，先按 R70/R71/R89 固定：

$$
A_i(s),\quad |s|\le\varepsilon_i,\qquad
M_{A_i(s)}=sP_i,
$$

以及

$$
M_{L_i}=0,\qquad T_{L_i}=\tau_i,\qquad V_{L_i}=v_i.
\tag{4}
$$

$A_i(s),L_i$ 的首末 scalar germ 都是 $g$，frame 都准确复位。跨 germ 零矩连接如有使用，其成本已在 $v_i$ 或 $A_i$ 的真实成本中，不另设为零。

再固定 R117 的真实中央互反族

$$
Y_N(h),\qquad h\in J=[h_*-\delta,h_*+\delta],
\quad 0<\delta<h_*/2,\quad N\in\mathbb N,\ N\ge1.
$$

它由 $k=2,-1/2$ 的正整数圈对、反号对、固定有限零矩连接及整条路径的真倒行组成。取全部端口同为 $g$、frame $I_3\to I_3$。R117 已证明

$$
M_{Y_N(h)}=T_{Y_N(h)}=0,
$$

以及在 (2) 的同一个查询下

$$
\boxed{
\lambda(V_{Y_N(h)})=N a(h-h_*)+e(h),
\qquad a=2\kappa\lambda(G)\ne0,
}
\tag{5}
$$

其中 $e$ 连续，与外 bulk 圈数 $N$ 无关。全部桥、校 frame、倒行、导数权 $0,2,4$、端点势与历史成本都包含在真实 $V_{Y_N(h)}$ 内；只有在 $\lambda$ 下、使用已证商恒等，才得到 (5)。

辅助桥的圈数、IFT 参数族及 $J$ 在最初固定，不随后来的 $N$ 增大。$Y_N$ 增大 $N$ 只重复同一有限组 bulk 常态；不扩大 $h,k,\omega$ 的包络。$A_i(s)$ 也只使用已经固定的小闭参数区间。

这有限组紧控制族共同给 $h$ 的正下界及 $\omega$ 的有限界。因此可以在任何后续大整数选择之前，一次选择 $I$，使所有族满足

$$
h>0,\qquad \xi+\omega(s)\ge\eta>0
\quad(\xi\in\overline I).
\tag{6}
$$

随后才按第 1 节选共同合法圆和查询。所有后续重复、拼接与倒行均在这个固定物理许可内。

## 3. 固定第三 prototype 的中央基准必须先修正

若直接把原 $L_i$ 放入 R102，新增查询中会出现

$$
2n\sum_i\lambda(v_i).
$$

它随响应复制整数 $n$ 增长。若忽略此项，随后选择另一整数 $N$ 支付 $\lambda$，再用 $n$ 支付 $Q$，会产生未付的参数选择循环。下面在开始选择 $t$ 盒之前准确移除这一项。

对每个固定实数 $-\lambda(v_i)$，R117 的 (5) 与介值定理给有限整数 $N_i$、有限参数 $h_i\in J$，使真实中央块

$$
C_i=Y_{N_i}(h_i)
$$

满足

$$
\lambda(V_{C_i})=-\lambda(v_i),\qquad
M_{C_i}=T_{C_i}=0.
\tag{7}
$$

只选择有限多个固定根；不需要它们对任何参数连续。它们使用已经固定的 $J$ 和物理包络，因此不会在选定 $I$ 后重新扩域。

定义修正后的第三 prototype

$$
\widehat L_i=L_iC_i,\qquad
\widehat v_i=v_i+V_{C_i}.
$$

R83/R101 的真实同锚传递对两个各自 $M=0$ 的块准确给 $T,V$ 直接相加。因此

$$
\boxed{
M_{\widehat L_i}=0,\quad
T_{\widehat L_i}=\tau_i,\quad
V_{\widehat L_i}=\widehat v_i,\quad
\lambda(\widehat v_i)=0.
}
\tag{8}
$$

原方向 $K_i=\mathcal B_{P_i}(\tau_i)$ 完全不变。一般的 $Q(\widehat v_i)$ 不为零，后面完整保留。

(7) 没有实现 $-V_{L_i}$；只匹配一个固定查询的负值。$C_i$ 的其他第四成本、长度和位移都是真实附加量。

## 4. 修改 prototype 后的完整复制代数仍逐式成立

先固定一个有限 $t_i$ 区间，选固定整数 $m_i$，定义

$$
A_{i,t_i}=A_i(t_i/m_i)^{m_i}.
$$

每个小块的二阶矩阵相加，所以 $M_{A_{i,t_i}}=t_iP_i$。其第三、第四成本不作线性假设。

因为 $\widehat L_i$ 的 $M=0$，真实重复和同 $k$ 倒行给

$$
T_{\widehat L_i^n}=n\tau_i,\qquad
V_{\widehat L_i^n}=n\widehat v_i,
$$

$$
T_{(\widehat L_i^n)^R}=-n\tau_i,\qquad
V_{(\widehat L_i^n)^R}=n\widehat v_i.
\tag{9}
$$

令

$$
C_{i,t}=A_{i,t}A_{i,-t}
$$

并使用 R101 的同一个真实词

$$
Z_i(t_i,n)=
A_{i,t_i}\,\widehat L_i^n\,A_{i,-t_i}\,
(\widehat L_i^n)^R\,(C_{i,-t_i})^R.
\tag{10}
$$

$C_{i,\pm t}$ 的整块矩阵为零，故末尾真倒行的使用合法。逐段 third 传递与 R101 完全相同，只把旧 $v_i$ 换成 $\widehat v_i$；$\tau_i$、$P_i$ 以及全部 second/third 交叉项保持原式。得到

$$
\boxed{
M_{Z_i}=T_{Z_i}=0,\qquad
V_{Z_i}=E_i(t_i)+n(2\widehat v_i+t_iK_i),
}
\tag{11}
$$

其中

$$
E_i(t_i)=V_{C_{i,t_i}}+V_{C_{i,-t_i}}
$$

连续、偶，且与 $n$ 无关。它依赖已固定的 $m_i$，但没有遗漏 $A_{i,t_i}$ 自身的高次历史。

把所有 $Z_i$ 拼接。因每块 $M=T=0$，真实 fourth 成本相加：

$$
V_{Z(t,n)}
=E(t)+n\left(2\widehat v_\Sigma+\sum_{i=1}^r t_iK_i\right),
$$

$$
E(t)=\sum_iE_i(t_i),\qquad
\widehat v_\Sigma=\sum_i\widehat v_i.
\tag{12}
$$

由 (2)、(8)，新增查询精确简化为

$$
\boxed{\lambda(V_{Z(t,n)})=\lambda(E(t)).}
\tag{13}
$$

这里没有随 $n$ 增长的漏项。也没有把 $E(t)$ 设为零；它是后面标量盒映射的一个完整输入。

## 5. 选择次序：t 盒和 m，然后 N，最后 n

给定任意目标

$$
y\in\mathbb R^r,\qquad z\in\mathbb R.
$$

令

$$
t^0=-2\mathsf K^{-1}Q(\widehat v_\Sigma),\qquad
\mathcal C=t^0+[-1,1]^r.
\tag{14}
$$

这是用已经修正的完整 prototype 成本定义的中心。它不依赖后面要选的 $m_i,N,n$。

现在为每个坐标选覆盖 $\mathcal C$ 的有限区间，取固定 $m_i$，使其中所有 $t_i/m_i$ 都在原小族的范围内。于是 $E$ 已成为 $\mathcal C$ 上固定的连续函数。

### 5.1 先固定新增中央整数 N

在紧集 $\mathcal C\times J$ 上，

$$
B_\lambda=
\sup_{(t,h)\in\mathcal C\times J}
|z-\lambda(E(t))-e(h)|<\infty.
$$

选一个有限正整数

$$
N>\frac{B_\lambda}{|a|\delta}.
\tag{15}
$$

这个选择不涉及 $n$，正是因为 (13) 已经付清了 $\lambda(\widehat v_\Sigma)$。

### 5.2 N 固定之后再选响应整数 n

对已固定的 $N$，完整实际族 $h\mapsto V_{Y_N(h)}$ 连续。因此

$$
B_Q=
\sup_{(t,h)\in\mathcal C\times J}
\left\|
\mathsf K^{-1}\bigl(y-Q(E(t))-Q(V_{Y_N(h)})\bigr)
\right\|_\infty<\infty.
$$

选有限正整数

$$
n>B_Q.
\tag{16}
$$

这里保留了 $Y_N(h)$ 在 $Q$ 下的全部成本。它可以含 $N^2,N^3$ 或其他由真实历史产生的大项；不需要证明这些项小，也不把它们当作只有线性 $G$。因为 $N$ 已固定，只用其紧参数族上的有限性即可。

于是 (15) 与 (16) 没有相互依赖的循环。

## 6. 在一个乘积盒上求根

定义

$$
\begin{aligned}
\mathcal F_t(t,h)
&=t^0+\frac1n\,
 \mathsf K^{-1}\bigl(y-Q(E(t))-Q(V_{Y_N(h)})\bigr),\\
\mathcal F_h(t,h)
&=h_*+\frac{z-\lambda(E(t))-e(h)}{Na}.
\end{aligned}
\tag{17}
$$

这是 $\mathcal C\times J$ 上的连续映射。由 (15)、(16)，其像落在同一乘积盒内。闭有限维凸盒的 Brouwer 定理给一个不动点 $(t_*,\widehat h)$。

第一行的不动点方程与 (14) 合并得到

$$
Q\bigl(V_{Z(t_*,n)}+V_{Y_N(\widehat h)}\bigr)=y.
$$

第二行及 (5)、(13) 给

$$
\lambda\bigl(V_{Z(t_*,n)}+V_{Y_N(\widehat h)}\bigr)=z.
$$

定义真实有限拼接

$$
B=Z(t_*,n)\,Y_N(\widehat h).
$$

两大块均 $M=T=0$，故其完整成本准确相加，并保同 germ、frame $I_3\to I_3$。因此

$$
\boxed{
M_B=T_B=0,\qquad Q(V_B)=y,\qquad\lambda(V_B)=z.
}
\tag{18}
$$

证明只用连续性与有限整数。没有需要从一族介值根中选择连续分支，没有要求 $e$ 可微，也没有把大整数极限当成实际路径。

## 7. 32 查询联合满射与固定真实基准

取 R116 的 31 个真实独立原方向，得到

$$
\boxed{(Q,\lambda)(\mathcal S_g)=\mathbb R^{32}}
\tag{19}
$$

在上述共同物理区间和固定合法圆的真实有限成本半群上成立。这里 $\mathcal S_g$ 是 $M=T=0$、同 scalar/frame 端口的实际路径成本集合；(19) 不取闭凸锥，不放松为实数圈数，不在半群中假设负路径。

更一般地，可取完整 $\mathcal R_8$ 的任意真实原生成基，设其未知真实维数为 $r$，同一证明给 $r+1$ 个固定查询的任意共同目标。本稿不计算这个未知 $r$。

若预先有一个固定完整基准成本 $V_*$，把其路径先纳入最初的物理包络，再取

$$
y=-Q(V_*),\qquad z=-\lambda(V_*).
$$

则真实插入块满足全部 32 查询的准确抵消。若原装配的插入贡献为 $4V_B$，相应目标除以四即可。完整的 $V_*$、各 $\widehat v_i$、$E(t)$、$e(h)$ 和 $V_{Y_N(h)}$ 都进入了方程，没有一个被以“中央”名义删除。

共同区间、圆与查询可用于所有目标。每个目标只改变有限 $N,n$ 及最终盒内参数；(14) 的 $t$ 盒和各固定 prototype 不随目标变。

## 8. 可选的真实四块闭浸入数据

若要同时沿用 R45 的位置闭合，最初再固定一个真实 $M=0$、frame $I_3\to D$ 的基准 $J_0$，首末 germ 都为 $g$，其中 $D=\operatorname{diag}(-1,1,-1)$。把它加入最初包络，使用 (18) 指定

$$
(Q,\lambda)(V_B)=-(Q,\lambda)(V_{J_0}).
$$

令 $P=BJ_0$。零矩传递给 $V_P=V_B+V_{J_0}$、$T_P=T_{J_0}$。对这个同一个实际 $P$ 使用 R45 的

$$
P\,P\,P^R\,P^R
$$

四块，得到完整 $M=T=0$、frame 和 scalar 端芽复位。若 $P$ 的本地位移为 $\Delta$，实际前缀 frame 下的四项位移为

$$
\Delta,\quad D\Delta,\quad-\Delta,\quad-D\Delta,
$$

故中心线准确闭合。四个零矩块的真实成本均为 $V_P$，总第四成本为 $4V_P$，所以同一组 32 查询仍准确为零。这里使用同 $k$ 真倒行和 R45 的四块，不把倒行当负成本。

该几何结论只得到有限光滑正则浸入环带的数据。位置从未在各块之间重置；各段长度和位移均真实累积。

## 9. 联调已付与仍未付的部分

本结果付清的是一个具体有限维联调缺口：新增商查询与任意一批独立响应查询可以在同一个实际词中一起匹配。必要步骤是先付每个固定 prototype 的 $\lambda(v_i)$，并在乘积盒论证中把 $N$ 放在 $n$ 之前。

未受这些查询检测的 $\mathcal U_4/\mathcal R_8$ 其他方向仍然可能存在。即使将来知道 $\dim\mathcal U_4=r+1$，还需要明确所用 $r+1$ 查询在该完整空间上单射，才能把查询等式升级为完整 fourth 函数等式；本稿没有宣称当前商恰好一维。

此处的 31 个查询是同一合法光滑圆上的完整模式实查询，不宣称它们自动等于先前所有 $m=8$ 尾系数。也没有由 $G$ 的完整非成员性质推出它的 pure $m=8$ 投影非成员。

完整 pure/mixed 周期函数、逐 $s$ 的 ruling、低阶和第四阶双 collar、更高阶收敛、有限等距族、闭嵌入材料面、reach 与宏观位移都未由 (18) 自动支付。后续必须继续识别真实成本商及这些几何条件。
