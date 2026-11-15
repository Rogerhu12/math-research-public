# R325：完整 literal root field 的逐步区间后验构造

本结果给出 R314 可执行的一种充分构造：从一个实际成功返回的有限 root 记录，保留全部 113 个 root 坐标、225 项独立 Gram 表、完整 226 态输出与 224 个 shape 输入列；另可一并处理六个独立几何/材料坐标。构造验证的是**固定所记分支的准确实表达**及其方向，不是 IEEE 舍入映射的导数，不证明动态 root 分支稳定，也不把 Gram 矩阵 $C$ 当作实际 $F_e$。

本结果没有当前运行数值。若区间域、正定性、逆界或预算未能支付，结论就是对应范围未决；不改变原 native 的任何接受条件。

## 325.1 明确对象及输入

固定 $M=112$、$J=M+1=113$、$K=224$。一个 field 的输入为完整 $y\in\mathbb R^{226}$，以及六个独立参数

$$
\gamma=(r,r',w,w_2,E,\mu).
$$

其中 $w_2,E$ 不由 $w$ 代换。频率、全部 cosine/sine 表、全部 $225=2M+1$ 项 Gram 表、原平方根常量和 orientation 都是原 packet 的 literal binary64 字，作为准确 dyadic 常数保留。特别地，angular $L$ 的零模输入系数为 $1$，投影的零模系数仍是实际 cosine 表第零列；两者不靠表恒等式合并。

由原物理表达准确形成 target $t(y,\gamma)$。原 finite root 的实际记录给出 $m\le29$ 个已接受更新，更新步长

$$
a_k=2^{-b_k},\qquad b_k\in\{0,\ldots,19\},
$$

及 normal-stop 或 fallback 的实际返回类型。固定这条记录，定义准确实对象

$$
e_0=0,\qquad
C_k=C(e_k,y,\gamma),\quad F_k=F(e_k,y,\gamma),
$$

$$
s_k=C_k^{-1}F_k,\qquad e_{k+1}=e_k-a_k s_k,\qquad
L_{\mathrm{ret}}=t(y,\gamma)+e_m.
\tag{325.1}
$$

这里的逆只在后面条件支付时有定义。若已证相应 $C_k$ 正定，(325.1) 与准确实 Cholesky 及两次三角回代的结果相同。最后沿原完整 RHS 公式形成

$$
\mathcal V(y,\gamma)=
(V_0,\ldots,V_{223},V_{224},V_{225}).
$$

两个 mean 行为原 $r'wL_{\mathrm{ret},0}$ 与 $r'w$，没有省略。

实际 binary128 程序提供名义字 $\widehat e_k,\widehat F_k,\widehat C_k,\widehat L_{c,k},
\widehat v_{c,k},\widehat s_k$ 以及数值方向。它们是后验中心和证据，不在定义中被宣布为准确实结果。后面的所有输入字从原 bytes 精确解码，短十进制不参与恢复。

本构造以**所选 field 的真实 binary128 输入字**为准确输入点。若该 field 来自某条实际 RK 前缀，本构造不自动支付该前缀相对于准确实 RK 的误差；这项边界必须单独记录。

## 325.2 整数向外区间

选整数精度 $p\ge1$，令 $B=2^p$。用整数对 $(\ell,u)$ 表示闭区间

$$
[\ell,u]_p=[\ell/B,u/B],\qquad \ell\le u.
$$

加减按整数端点精确形成。乘法先取四个整数乘积的最小值、最大值，再分别向下、向上除以 $B$。若 $0<\ell\le u$，倒数端点为

$$
\left[
\left\lfloor\frac{B^2}{u}\right\rfloor,\,
\left\lceil\frac{B^2}{\ell}\right\rceil
\right]_p.
\tag{325.2}
$$

负区间通过变号转为此情形；含零的分母不执行除法。若 $\ell\ge0$，平方根用

$$
\left[
\left\lfloor\sqrt{\ell B}\right\rfloor,\,
\left\lceil\sqrt{uB}\right\rceil
\right]_p.
\tag{325.3}
$$

整数平方根与平方比较即可决定第二端是否再加一。这里没有靠普通浮点值估计向外误差。

**包含性。** 加减直接由端点单调性成立。乘法的双线性函数在矩形上的极值在顶点，整数取整只向外扩张，故包含成立。正倒数严格递减，代入两端得到 (325.2)；平方根递增，得到 (325.3)。复合有限表达时逐层代入，便包含该表达在所有允许输入上的值。原 binary64/binary128 字解码成整数乘二次幂；若不落当前网格，也按同一向外规则包围，不能强称端点相等。

对区间方向采用

$$
D(a+b)=(a+b,\dot a+\dot b),\quad
D(ab)=(ab,\dot a\,b+a\,\dot b),
$$

$$
D(a/b)=
\left(a/b,\frac{\dot a\,b-a\,\dot b}{b^2}\right),\quad
D(\sqrt a)=\left(\sqrt a,\frac{\dot a}{2\sqrt a}\right).
\tag{325.4}
$$

在分母排零、平方根严格正的盒上，这是准确实链式法则的包含计算。区间变量之间的相关性可能使结果过宽，但不会使结果漏包。此陈述不是对任何舍入原语求导。

## 325.3 全部 $F,C$ 的形成范围

每一步从已得的 $e$ 盒及完整输入盒重建以下量：

1. 原物理 target、全部 112 momentum、angular $P,P_t,L,U$；
2. 原 $D,S,A$ 与真实分母，必须在该盒严格满足原 floor 条件；
3. 原 quad 与全部 113 cosine 投影，包含 $e$ 的直接项；
4. 原 $\rho$ 与完整 225 项独立 Gram 投影，再按原 Toeplitz/Hankel 加零模规则形成全部 $113\times113$ 的 $C$；
5. 原 flux 的全部 112 sine 投影及完整 RHS。

这给出盒 $\mathcal F_k,\mathcal C_k$，使真实准确值 $F_k,C_k$ 都被包含。没有把某个旧 $J$、另一 root policy 或另一状态的形成值代入。

对方向，angular 局部表达的六个独立坐标可选为

$$
(P,P_t,L,U,w_2,E).
$$

在当前 angular 盒上用 (325.4) 包围 quad、$\rho$、flux 对六坐标的偏导；每个请求方向再通过完整 target/momentum 的实际链式法则作用于这些偏导。所有 113/225/112 项投影都必须累计。$r,r',\mu$ 的作用留在原 target、momentum 和 RHS 系数中，不能只处理上述六个 angular 坐标就称已包括它们。

这是一种共享严格局部偏导的方法；它与逐列重复完整区间表达包围相同准确实对象，不要求两种计算给出相同区间端点。

## 325.4 不把候选逆当作证明

取一个**准确 dyadic** 方阵 $Y$。可先对名义 Cholesky/两次回代用区间求值，再取各元素区间的 dyadic 中点作为候选；这个构造方式本身不证明 $Y$ 是逆。

设逐项非负矩阵 $N$ 满足对当前整个 $\mathcal C$ 盒都有

$$
|I-YC|\le N,\qquad
q=\max_i\sum_jN_{ij}<1.
\tag{325.5}
$$

$N$ 的每个元素和行和须向外得到。则对盒中每一个 $C$，$YC$ 可逆，进而方阵 $C,Y$ 都可逆，并有

$$
|C^{-1}b|\le (I-N)^{-1}|Yb|.
\tag{325.6}
$$

**证明。** $\|I-YC\|_\infty\le q<1$，故 $YC$ 的 Neumann 级数收敛。逐项绝对值与非负矩阵乘法给

$$
|(YC)^{-1}|\le\sum_{j=0}^{\infty}N^j=(I-N)^{-1}.
$$

右乘 $Yb$ 得 (325.6)。方阵乘积 $YC$ 可逆意味着两个因子均可逆。证毕。

为了不再用近似逆计算右端，可取非负向量 $\bar v\ge|Yb|$。对任意整数 $r\ge0$，设 $\bar v_k\ge N^k\bar v$、$\bar s_r\ge\sum_{k=0}^{r-1}N^k\bar v$ 都按非负向外算术递推。则

$$
(I-N)^{-1}|Yb|
\le
\bar s_r+\frac{\|\bar v_r\|_\infty}{1-q}\mathbf1.
\tag{325.7}
$$

**证明。** 前 $r$ 项逐项由 $\bar s_r$ 控制。剩余项从 $N^r\bar v$ 起，其最大范数至多
$\|\bar v_r\|_\infty\sum_{j\ge0}q^j$。两者相加即得。若每次非负乘加上取整，递推向量仍是上界。证毕。

实现可以固定 $r=12$；这是计算后验上界的一种有限算法参数，不是科学接受阈值。$q\ge1$ 时本算法给未决，不能据此断言 $C$ 奇异。

## 325.5 正定与准确 Cholesky 的责任

若需要明确比较“准确实 Cholesky 原表达”，须另证整个相关对称 $C$ 盒中的正定性。一种直接充分方法是对原 Cholesky 三角递推作区间计算，并逐个验证每个对角平方根前的 pivot 区间下端严格正。

**证明。** 对任意实际对称矩阵 $C$，按固定三角顺序归纳：先前准确因子元素都在已计算区间中，因此下一 pivot、非对角除法结果也被包围。严格正 pivot 保证准确递推有定义。全部行完成即得到 $C=LL^\mathsf T$ 且 $L$ 对角严格正，故 $C$ 正定。证毕。

(325.5) 已经足以证明逆存在；正定步骤的作用是支付此处额外声明的准确 Cholesky 表达域。它不是加到原 native 上的接受门。

## 325.6 一步 primal 后验盒与形成缺陷的分离

在当前盒中，以实际名义解字 $\widehat s$ 为中心，向外形成

$$
\mathcal R=\mathcal C\,\widehat s-\mathcal F.
$$

由 (325.6) 或 (325.7) 取得逐分量 $E_s$，使对全部允许值都有

$$
|C^{-1}(C\widehat s-F)|\le E_s.
$$

则

$$
s=C^{-1}F\in\widehat s+[-E_s,E_s].
\tag{325.8}
$$

更新后取

$$
\mathcal E_+=\mathcal E-a\,\mathcal S.
\tag{325.9}
$$

这包含准确实的下一 $e$，无须把名义更新舍入误差设零。

需要另记两类量，不能混称：

- **名义点纯形成缺陷**：在实际 $\widehat e$ 字处准确重建 $F_0,C_0$，计算它们相对 $\widehat F,\widehat C$ 的区间差；
- **传播盒形成范围**：在已包含前面误差的 $\mathcal E$ 上重建 $\mathcal F,\mathcal C$。

后者包含传播不确定性，不能标为单次浮点形成误差。名义 factor/forward/backward 缺陷仍可完整读回，并保持 R314 的恒等式

$$
C_0\widehat s-F_0
=a+L_c b-R\widehat s
+(C_0-\widehat C)\widehat s-(F_0-\widehat F),
$$

其中

$$
R=L_cL_c^\mathsf T-\widehat C,\quad
a=L_c\widehat v_c-\widehat F,\quad
b=L_c^\mathsf T\widehat s-\widehat v_c.
$$

直接形成与分解形成的区间都包围同一准确残差；不要求两个区间的端点逐字相等。

## 325.7 全部方向的严格递推

对某个完整输入方向，已知 $e_k$ 与 $\dot e_k$ 的盒。按 §325.3 的完整形成及 (325.4) 求出

$$
\dot F_k\in\dot{\mathcal F}_k,\qquad
\dot C_k\in\dot{\mathcal C}_k.
$$

这里包含当前完整 $e,\dot e$ 盒，不只对名义旧点的外层输入求偏导。由准确恒等式

$$
C_ks_k=F_k
$$

微分得

$$
C_k\dot s_k=\dot F_k-\dot C_k s_k.
\tag{325.10}
$$

用已证 primal 解盒 $\mathcal S_k$ 形成

$$
\mathcal B_k=\dot{\mathcal F}_k-\dot{\mathcal C}_k\mathcal S_k.
$$

围绕实际数值方向字 $\widehat{\dot s}_k$，对完整残差

$$
\mathcal C_k\widehat{\dot s}_k-\mathcal B_k
$$

再次应用同一已证逆上界，得到 $\dot{\mathcal S}_k$。然后

$$
\dot{\mathcal E}_{k+1}
=\dot{\mathcal E}_k-a_k\dot{\mathcal S}_k.
\tag{325.11}
$$

**为何没有漏 primal 误差。** 右端明确使用整个 $\mathcal S_k$；若写成
$s_k=\widehat s_k+\Delta s_k$，则其中已经包含
$-\dot C_k\Delta s_k$。没有仅用 $-\dot C_k\widehat s_k$ 代替，也没有假设名义 factor/两回代残差的导数为零。

**全 trace 包含性。** 从准确 $e_0=0,\dot e_0=0$ 开始，(325.8)–(325.11) 逐步归纳包含每个准确实 $e_k,s_k,\dot e_k,\dot s_k$。每个真实使用的矩阵盒均已证明可逆，并在所声明 Cholesky 范围内证明正定；angular 与原 D/S/A 域也逐步支付。故固定有限序列结束时，$L_{\mathrm{ret}}$ 及每个请求方向均被包含。证毕。

相关的实际参数邻域中，准确表达有定义且这些矩阵可逆，因此固定序列表达可微；本证明不需要、也不推导原动态程序在该邻域选择同一分支。

## 325.8 完整 226 行及六个独立参数方向

把返回的 $L$ 与方向盒代入原完整 RHS，按 (325.2)–(325.4) 完整形成所有 226 行。对 224 个 shape 坐标逐列完成后，得到

$$
D_y\mathcal V\big|_{\text{224 shape inputs}}
\in\mathcal J_{226\times224}.
$$

两个 mean 输出必须在该矩阵中，不因其不反馈 shape 而删除。输入两个 mean 坐标未请求时，也不能称已经数值执行全部 226 输入列。

可另请求六个独立坐标 $(r,r',w,w_2,E,\mu)$，合计 $230$ 列。它们不是某个真实 profile 参数的完整链式响应：把它们接到实际 profile/采样位置的参数方向，还需要那个来源自己的准确链式法则，包括可能的 $dh$、端口比例变化和分段拓扑责任。

对任何名义 binary128 RHS/方向输出字，区间与该准确字相减就给严格误差包围。这包括 root target、angular 投影、Gram、solve、有限更新和最终 RHS 的形成误差。它不只是一条普通浮点范数的差。

## 325.9 来源、资源及完成字段

可执行消费者应保以下层次：

| 字段 | 成立所需范围 |
|---|---|
| 实际名义 tape 已返回 | 原成功 finite root、完整已接受更新、真实返回类型 |
| 固定 trace primal field 已包围 | 全部更新及完整 226 RHS 的区间域/solve 已支付 |
| 请求列已包围 | 每个明确请求列的全部更新、全部 226 行已支付 |
| 全部 224 shape 列已包围 | 0–223 完整列，不能用部分列代称 |
| 六个独立几何列已包围 | 明确的 224–229 六列全部完成 |
| 真正有限 $F=0$ 根 | 本构造不支付，须另用真实 $F_e$ 的根盒条件 |
| 整个 RK/stage/129248 行 | 本构造不支付，须另累计前后输入、RK、端口、cut/far |
| 原 native/边界112/338/物理审计 | 本构造不支付，必须保各自实际完整责任 |

预条件候选只能由明确字或已绑定的计算形成；所有 inverse/形成界在 Actions 用向外算术重新验证。缺少当前真实 state/tape 时不能从已删除 raw 的 SHA 恢复。发生未决域、未证正定、$q\ge1$、列缺失或墙钟结束时，保留已完成范围与未访问后缀。证书的资源部分不改变原求解结果。

与原 140/145 的关系仅为可独立使用同一真实输入来源；这里不加入它们的接受门，不推断它们未来的速度或结果。

## 325.10 来源

- [R283：完整 literal 表与成功有限 root 轨迹微分](R283-finite-root-trace-differentiation-with-literal-tables.md)。
- [R302：共享 root 记录与完整边界响应责任](R302-shared-finite-root-traces-and-complete-boundary-response.md)。
- [R305：准确实收缩与名义分解残差](R305-literal-gram-root-contraction-and-nominal-factor-defects.md)。
- [R314：严格后验值、方向与完整链式误差的充分条件](R314-verified-posteriori-bounds-for-literal-root-traces-and-directions.md)。

本结果支付的是上述有限区间构造的包含性证明。实际数值证书须由真实输入与完整运行取得；本文没有预填一次运行的证书成立、native 接受或最终场结论。
