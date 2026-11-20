# R141：同一 WVC low193 的定向双侧 Green 认证与完整193观察

2026-11-20，`visible-exact-astra-ac637-20261120`。

**已证明：下述精确比较问题、完整 Green Gram 递推、真实系数缺陷转授和全区间横截性定理。尚未执行其科学数值，未宣称任何严格小量门已过。** 配套纯数学模块为 [fourfold_codazzi_low_centre_verified_green_math.py](../scripts/fourfold_codazzi_low_centre_verified_green_math.py)。它没有数值导入、文件读写或运行入口；接受同一已 admission 的 WVC context、明确的精确比较系数和有限试探 charts。所有实际求值须在单独的公共 Actions 目标内完成。

本篇要认证的系数是 [R137](R137-continuous-signed-centre-and-exact-endpoint-system.md) 的真实变系数低频中心 $A_L^c$。它是 **WVC hybrid centre**：principal speed 保留原全参数族的 $\eta_\delta=-\gamma m_\delta$，lower coefficients 来自原 repaired centre。这里的“真实系数”指这一已定义中心的完整函数，而不是 midpoint 模型；不把它改名为 $DF(Q^{\rm repair})$。原 actual-family 差、完整高反馈、真正物理外行和有限 $\rho$ 桥仍须分别支付。

这一区别直接来自 [signed packet 模块](../scripts/fourfold_codazzi_true_collar_signed_packet_math.py) 的 `_complete_centre_packet`、`actual_eta_identity`、`centre_mean_is_separate_from_actual_eta`，以及 [assembly](../scripts/fourfold_codazzi_collar_dual_feedback_math.py) 的 `prepare_complete_kernel_context`：body principal 读取原 `complete_delta_bounds.radial_speed`，同一个量在 family 差的两边保持相同。本篇不调用几何刚性来替代这一 hybrid 算子的认证。

## 1. 精确空间、方程和全部观察

设 $I=[a,R]$ 是原真实正根到 $R=25/8$ 的区间。低频实坐标次序固定为

$$
 x=(x^o_1,\ldots,x^o_{96},x^m,x^e_1,\ldots,x^e_{96})\in\mathbb R^{193}.
 \tag{G.1}
$$

归一化正弦/余弦坐标、ordinary $dr$、原 moving-phi 表示中的独立 even mean 与原 transmission 均保持不变；不把这一角零模替代其他 physical density-mean 行，也不在此变换到物理角 theta。记 $n=193,p=97,q=96$。本篇的 mixed boundary operator 为

$$
 B_ax=x^e(a),\qquad
 B_Rx=\bigl(x^o(R)+p_0x^e(R),x^m(R)\bigr),
 \qquad p_0=13/80.
 \tag{G.2}
$$

这正是低参考 $G_D$ 和 R137 中低 block 的边界，非原独立物理外行的免费替代。首先认证

$$
 x'=A_L^c(r)x+W(r)f(r),\quad B_ax=0,\quad B_Rx=0,
 \qquad f\in L^2(I;\mathbb R^k).
 \tag{G.3}
$$

其中 $A_L^c$ 由 `context.centre_matrix(HEAD, HEAD, box)` 在整个 box 上包围，$k$ 由声明的 source role 决定。源不要求径向导数。

原固定权在第 $i$ 段是

$$
 S_i=\operatorname{diag}(I_{96},q_i,q_iI_{96}),\qquad q_i>0.
 \tag{G.4}
$$

这些 $q_i$ 是原 WVC exact reference choices；它们并非待解函数。令 $R_a$ 取 root odd96 和 root mean，$R_b$ 取 outer even96，且

$$
 \Theta=\operatorname{diag}\bigl((1+16j^2)^{-5/12}\bigr)_{j=1}^{96}.
$$

完整 observation 是

$$
 \mathcal Ox=(Sx,\ R_ax(a),\ \Theta R_bx(R))
 \in\mathscr Z:=L^2(I;\mathbb R^{193})\oplus\mathbb R^{97}\oplus\mathbb R^{96}.
 \tag{G.5}
$$

三个槽使用直和 Hilbert 范数。原子的总数准确为193。式(G.5)只对真实 $H^1$ 解定义；没有从一个任意 $L^2$ 输入读取 trace，也没有用 body 范数直接推断端点范数。

## 2. 保留真实根长度的精确 midpoint 比较

将原155个比较段写为 $I_i=[r_i,r_{i+1}]$，$i=0,\ldots,m-1$。所有段界及原 cutoff joins 保持；第一个左端仍为原真实根 $a$。记

$$
 h_i=r_{i+1}-r_i>0,\qquad \tau=(r-r_i)/h_i\in[0,1].
 \tag{G.6}
$$

选择一个明确的精确 dyadic 矩阵 $H_i\in\mathbb R^{193\times193}$。例如它可以是已声明的 binary64 长度 midpoint 与矩阵 midpoint 的**精确 dyadic 乘积**；若把该乘积再次舍入，则必须明确把舍入后的 dyadic 定义为模型。浮点 `expm` 的输出不是精确模型定义。

在真实区间上定义比较生成器

$$
 \bar A_i=H_i/h_i,\qquad
 \bar\Phi_i(\tau)=e^{\tau H_i},\qquad
 \Delta(r)=A_L^c(r)-H_i/h_i\quad(r\in I_i).
 \tag{G.7}
$$

因此模型整段 transfer 为 $e^{H_i}$，不依赖把真实根替换成某个 midpoint。所有积分仍用 $dr=h_i\,d\tau$；缺陷也保留 $h_i^{-1}$。一条真实长度 enclosure 足以向外包围它们。模型与实际系数可以依赖同一个固定参数；interval implementation 同时覆盖原允许的参数值，而没有把参数改成径向任意控制。

对同一 $H_i$ 作精确归一化子分段是合法的：在 $[u,v]\subset[0,1]$ 上用 $(v-u)H_i$，真实长度为 $(v-u)h_i$。这是同一个比较模型。当前源码的第一个 adapter 保持一个原 panel 对应一个 generator；若另加 refined adapter，须明确保存这一 parent/coordinate map，不能把原 body domain 默默换掉。

**系数范围限制。** 当前 `context.centre_matrix` 在原 parent coefficient packet 上取 enclosure。缩小归一化 box 能收紧 $e^{\tau H_i}$，却不会自动收紧这个 parent 上的真实 $A_L^c$ enclosure。若实际缺陷因此太大，需要从原函数构造真正的 subinterval coefficient adapter；切小 box 本身不是新的系数定理。

## 3. 用有限精确 charts 建立比较 Green

在每个节点先选一个完整 $193\times193$ 精确 dyadic 试探矩阵 $\widehat T_i$。试探可来自浮点设计，但必须在本次定向计算中证明所需逆存在。下述覆盖后得到实际使用的 $T_i$；由于 $13/80$ 不是 dyadic，覆盖后的矩阵一般是精确有理矩阵，而不再一律称为 dyadic。为严格保留边界，覆盖 $\widehat T_0$ 的前97列为

$$
 N_a=\begin{pmatrix}I_{97}\\0_{96\times97}\end{pmatrix},
$$

覆盖 $\widehat T_m$ 的后96列为

$$
 N_R=\begin{pmatrix}-p_0I_{96}\\0_{1\times96}\\I_{96}\end{pmatrix}.
 \tag{G.8}
$$

后一组列准确使用有理数 $13/80$；它不是某个浮点近似 Robin。覆盖后矩阵须通过定向逆检查。记

$$
 E_i=T_{i+1}^{-1}e^{H_i}T_i,\qquad
 \widetilde E_i=T_i^{-1}e^{-H_i}T_{i+1}.
 \tag{G.9}
$$

数学上 $\widetilde E_i=E_i^{-1}$；实现分别算 $e^{H_i}$ 与 $e^{-H_i}$，不对可能极病态的整段 $e^{H_i}$ 作浮点求逆。按97/96块分解每个矩阵。

左侧从 $Z_0=0_{96\times97}$ 开始，递推

$$
 U_i=E_{11,i}+E_{12,i}Z_i,\qquad
 Z_{i+1}=(E_{21,i}+E_{22,i}Z_i)U_i^{-1}.
 \tag{G.10}
$$

右侧从 $Y_m=0_{97\times96}$ 开始，递推

$$
 V_i=\widetilde E_{21,i}Y_{i+1}+\widetilde E_{22,i},\qquad
 Y_i=(\widetilde E_{11,i}Y_{i+1}+\widetilde E_{12,i})V_i^{-1}.
 \tag{G.11}
$$

所有显示的逆均须由定向算术证明。令

$$
 L_i=T_i\binom{I_p}{Z_i},\qquad
 R_i=T_i\binom{Y_i}{I_q},\qquad
 F_i=(L_i,R_i),\qquad
 F_i^{-1}=\binom{\ell_i}{\rho_i}.
 \tag{G.12}
$$

再证明每个 $F_i$ 可逆。这里没有把 trial chart 可逆等同于真实左右子空间横截；横截由完整 $F_i$ 的逆另行证明。

**命题1。** 若(G.9)–(G.12)的所有逆通过，则 $\bar L=\partial_r-\bar A$ 配(G.2)有唯一 Green 逆 $\bar G:L^2\to H^1$。其两侧齐次空间在每个真实半径都互补。

**证明。** 从定义逐项得

$$
 e^{H_i}L_i=L_{i+1}U_i,\qquad
 e^{-H_i}R_{i+1}=R_iV_i.
 \tag{G.13}
$$

所以 $L_i$ 恰张成满足左边界的齐次解在 $r_i$ 的值，$R_i$ 恰张成满足右边界的齐次解在该点的值。二者的维数为97和96。节点处 $F_i$ 可逆，任一内部点的 frame 是 $e^{\tau H_i}F_i$，仍可逆。故没有非零满足两侧边界的齐次解。Variation of constants 给下节的完整核；系数逐段有界、段数有限，其结果在 ordinary $H^1$ 中并满足两边界。证毕。

这一证明使用有限 $193$ 状态矩阵、$97$ 与 $96$ carriers。无需建立一个把所有径向未知量拼成的大矩阵。若某个 chart inverse 不通过，结论仅为本次有限 chart 未认证；不能登记实际算子奇异。

## 4. 有符号 Green 的完整两侧公式

在 $r\in I_i$ 定义

$$
 L_i(r)=e^{\tau(r)H_i}L_i,\quad R_i(r)=e^{\tau(r)H_i}R_i,
$$
$$
 \ell_i(r)=\ell_i e^{-\tau(r)H_i},\quad
 \rho_i(r)=\rho_i e^{-\tau(r)H_i}.
 \tag{G.14}
$$

记 $C_i=U_i^{-1}$、$D_i=V_i^{-1}$。若 $r\in I_i,s\in I_j$，则

$$
 \bar G(r,s)=
 \begin{cases}
 -L_i(r)C_i\cdots C_{j-1}\ell_j(s),&i<j,\\
 -L_i(r)\ell_i(s),&i=j,\ r<s,\\
 R_i(r)\rho_i(s),&i=j,\ r>s,\\
 R_i(r)D_{i-1}\cdots D_j\rho_j(s),&i>j.
 \end{cases}
 \tag{G.15}
$$

这由(G.13)的准确有序乘积得到。对角的跳为
$L_i(r)\ell_i(r)+R_i(r)\rho_i(r)=I$，所以 $\bar L\bar G$ 的 delta 系数为 $I$。左端只出现满足左边界的 $L$ 支，右端只出现满足右边界的 $R$ 支；因此(G.15)证明命题1中的 source 断言。source 对角的取值不影响 ordinary $L^2$ 积分，但两侧三角都必须保留。

对一条声明源 $W(s)$，将完整矩阵乘积先组成

$$
 O_{L,i}(r)=S_iL_i(r),\quad O_{R,i}(r)=S_iR_i(r),
$$
$$
 I_{L,i}(s)=\ell_i(s)W(s),\quad
 I_{R,i}(s)=\rho_i(s)W(s).
 \tag{G.16}
$$

只有在这里以后才取 Gram 或正上界。source 的方向、真实 mean 和左右 signed cancellation 没有在相乘之前被替换成一个总标量。

原 atoms 的两端 carrier 为

$$
 A_a=R_aL_0=I_{97},\qquad A_R=\Theta R_bR_m=\Theta.
 \tag{G.17}
$$

源码由实际 boundary frame 取这两矩阵；不以“一般 trace 常数”代替它们。

## 5. 整个 source、body 和193 atoms 的 Gram 递推

对每个完整 panel 定义

$$
 \begin{aligned}
 P_{L,i}&=\int_{I_i}I_{L,i}(s)I_{L,i}(s)^T\,ds,&
 P_{R,i}&=\int_{I_i}I_{R,i}(s)I_{R,i}(s)^T\,ds,\\
 Q_{L,i}&=\int_{I_i}O_{L,i}(r)^TO_{L,i}(r)\,dr,&
 Q_{R,i}&=\int_{I_i}O_{R,i}(r)^TO_{R,i}(r)\,dr.
 \end{aligned}
 \tag{G.18}
$$

这些是实际 covariance，维数分别为97或96；$P$ 依赖本条完整 source，$Q$ 只依赖模型及同一 $S$。令

$$
 A_0=0,\qquad A_{i+1}=C_i^T(A_i+Q_{L,i})C_i,
$$
$$
 B_m=0,\qquad B_i=Q_{R,i}+D_i^TB_{i+1}D_i.
 \tag{G.19}
$$

同 panel 的两个三角量为

$$
 T_{L,i}=\int_{I_i}\int_{I_i\cap\{r<s\}}
 \operatorname{tr}\!\left(O_{L,i}(r)^TO_{L,i}(r)
 I_{L,i}(s)I_{L,i}(s)^T\right)dr\,ds,
$$
$$
 T_{R,i}=\int_{I_i}\int_{I_i\cap\{r>s\}}
 \operatorname{tr}\!\left(O_{R,i}(r)^TO_{R,i}(r)
 I_{R,i}(s)I_{R,i}(s)^T\right)dr\,ds.
 \tag{G.20}
$$

完整 body 的 Hilbert–Schmidt 范数平方准确为

$$
 g_B^2=\sum_{i=0}^{m-1}\left[
 \operatorname{tr}(A_iP_{L,i})
 +\operatorname{tr}(D_i^TB_{i+1}D_iP_{R,i})
 +T_{L,i}+T_{R,i}\right].
 \tag{G.21}
$$

root97 与 outer96 各自使用

$$
 J_0=A_a^TA_a,\qquad J_{i+1}=C_i^TJ_iC_i,
$$
$$
 K_m=A_R^TA_R,\qquad K_i=D_i^TK_{i+1}D_i,
 \tag{G.22}
$$

其完整平方分别为

$$
 g_a^2=\sum_i\operatorname{tr}(J_iP_{L,i}),\qquad
 g_R^2=\sum_i\operatorname{tr}(K_iP_{R,i}).
 \tag{G.23}
$$

因此

$$
 \|\mathcal O\bar G W\|\le
 g:=\sqrt{g_B^2+g_a^2+g_R^2},\qquad
 g_A:=\sqrt{g_a^2+g_R^2}.
 \tag{G.24}
$$

**命题2。** (G.18)–(G.24)是完整真实 $L^2$ source 到(G.5)的上界，没有遗漏模式、段或 atom。

**证明。** 对任一矩阵核 $UV$，有
$\|UV\|_F^2=\operatorname{tr}(U^TU\,VV^T)$。
将(G.15)按两个 panel 的顺序分区。对 $i<j$，所有 output panels 对 source panel $j$ 的贡献由左乘积的 covariance $A_j$ 合成；(G.19)第一行正是将这一乘积再向右推进一个 panel。$i>j$ 同理由第二行合成。$i=j$ 的全部面积恰为(G.20)两个三角，故(G.21)等于完整核的 Hilbert–Schmidt 平方。两个 atoms 由(G.17)和相同有序乘积给(G.22)–(G.23)。Hilbert–Schmidt 范数支配算子范数，三输出槽实际正交，得(G.24)。不同 source 的输出并不因此正交；若组合它们，必须在实际共同 source 空间上另外保留 cross terms 或使用有效三角界。证毕。

这里存储的递推状态随 panel 数线性增长；没有 $155^2$ 个 $193^2$ 矩阵 kernel 表。所有 trace 乘积可用 $d^2$ 项内积计算，无须为取一个 trace 再作完整 $d^3$ 矩阵乘法。

## 6. 如何用区间算术真正包围连续积分

每个 panel 选准确有理 cuts
$0=\tau_0<\cdots<\tau_v=1$。对一个**整个闭 box**
$\tau\in[\tau_j,\tau_{j+1}]$，用有向矩阵指数包围
$e^{\tau H_i}$ 与 $e^{-\tau H_i}$，继而包围(G.16)及其完整 Gram。
真实 mass 为

$$
 \mu_{ij}=h_i(\tau_{j+1}-\tau_j)>0.
 \tag{G.25}
$$

Gram 的 entrywise interval enclosure 乘以这一个真实 mass 后求和，包围(G.18)。这里使用的是 interval integration，既不是点值 quadrature，也没有断言每个区间矩阵本身在所有任意 entry 选择下都为半正定；其实际被包围对象是同一 Gram covariance。

对(G.20)，两个分离 subboxes 的准确面积为 $\mu_{ij}\mu_{ik}$；同一 subbox 的每一个三角准确面积为 $\mu_{ij}^2/2$。在整个对应 rectangle 上包围 trace integrand，再分别乘这两个面积即可。对同一小格只使用面积的一半，但保留左右两个不同 integrands；不能删掉另一方向，也不能把同格当成只存在一个分支。true $h_i$ 的向外上界用于面积上界。

实现中的算子范数可用一个矩阵 $M$ 的完整 Gram $M^TM$ 的 Gershgorin 上界：

$$
 \|M\|_2^2\le
 \max_i\left[(M^TM)_{ii}+\sum_{j\ne i}|(M^TM)_{ij}|\right].
 \tag{G.26}
$$

在有向 enclosure 上对右侧取上端点仍有效。相应地，所有 trace 和最终平方根也必须为有限有向上界；没有数值下界通过浮点绝对值制造出来。

配套模块使用 python-flint 的 `arb_mat.exp()` 和 `arb_mat.inv()`。软件接口见 [python-flint arb_mat 文档](https://python-flint.readthedocs.io/en/latest/arb_mat.html)；矩阵指数的 directed scaling/squaring 与 Taylor remainder 见 [FLINT matrix exponential 文档](https://flintlib.org/doc/arb_mat/arb_mat_exp.html)。不可认证的逆、非有限输出或不严格为正的长度均使当前认证失败，不切换到 pseudoinverse。文档说明软件语义；数学对象和误差转授由本文证明。

## 7. 从精确比较到真实变系数低193逆

对以下 source 单独形成完整(G.18)–(G.24)：

| 源角色 | 准确的 raw $W(s)$ | 输入单位 |
|---|---|---|
| `ordinary_raw_low_source` | $I_{193}$ | ordinary $L^2_r\mathbb R^{193}$ |
| `transformed_low_source` | $S^{-1}$ | 原 transformed body $L^2$ |
| `true_coefficient_defect` | $(A_L^c-\bar A)S^{-1}$ | 原 transformed body $L^2$ |
| `low_second_kind_correction` | $(A_L^c-D_f)S^{-1}$ | 原 transformed body $L^2$ |
| `centre_high0_return_source` | $C=A^c_{LH}|_{97\ldots160}$ | ordinary $L^2_r\mathbb R^{128}$ |

最后一列只是完整 return multiplier 的输入源；非局部的 $CFB$ 不能冒充这一条 local $W$。

记缺陷 source 的 body 上界为 $\varepsilon$，全部 atoms 上界为 $e_A$。若实际定向结果证明

$$
 \varepsilon\ge\|S\bar G\Delta S^{-1}\|_{L^2\to L^2},\qquad
 \varepsilon<1,
 \tag{G.27}
$$

则真实低193逆 $G_L=(\partial_r-A_L^c)^{-1}$ 配(G.2)存在。对表内或任何同单位已完整认证的 source $W$，若其 model body/atoms 上界为 $g_B,g_A$，则

$$
 \begin{aligned}
 \|SG_LW\|&\le b_W:=\frac{g_B}{1-\varepsilon},\\
 \|(R_a\operatorname{ev}_a,\Theta R_b\operatorname{ev}_R)G_LW\|
 &\le a_W:=g_A+e_A\frac{g_B}{1-\varepsilon},\\
 \|\mathcal OG_LW\|&\le\sqrt{b_W^2+a_W^2}.
 \end{aligned}
 \tag{G.28}
$$

**命题3。** (G.27)蕴含上述可逆性和(G.28)，且 solution 的 atoms 是真实 trace。

**证明。** 置 $u=Sx$，原方程等价于

$$
 u=S\bar GWf+\underbrace{S\bar G\Delta S^{-1}}_{E}u.
 \tag{G.29}
$$

由(G.27)，$I-E$ 在同一 ordinary body $L^2$ 可逆，故第一条界成立。所得 raw $x$ 又由(G.29)等于两个 $\bar G$ 输出之和；其源为 $L^2$、系数逐段有界，因此 $x\in H^1$ 且满足(G.2)。把两个完整 atoms receiver 施于该等式，得到第二条界；真实直和给第三条。齐次解同样满足 $u=Eu$，从严格小量得零。任一 ordinary $L^2$ 源已有解，故是实际 BVP 逆。这里的 Neumann 步只在已经由(G.15)–(G.26)完整算出的具体 signed Green 缺陷上使用；没有拿端点 SVD 或裸系数范数直接充作 $\varepsilon$。证毕。

若(G.27)不通过，只说明该具体 enclosure 未认证本次低193比较；不能推断 $A_L^c$ 有核。

## 8. 正确的增广二类逆与 atoms 输入

低中心在 R137 的同一空间 $\mathscr Z$ 上为

$$
 H_L=\mathcal OG_D(A_L^c-D_f)S^{-1}\pi_B,
 \tag{G.30}
$$

其中 $\pi_B$ 只读 body 输入。所有独立 atom 输入经 $H_L$ 映为零，$I-H_L$ 在 atoms 输入上仍有 identity。这正是一个方算子；不把 $L^2$ source 与 body-plus-atoms 输出直接强行认同。

令 $h=(h_B,h_A)\in\mathscr Z$，利用(G.3)严格解出

$$
 (I-H_L)^{-1}h
 =h+\mathcal OG_L(A_L^c-D_f)S^{-1}h_B.
 \tag{G.31}
$$

证明只需令 $x=G_D(A_L^c-D_f)S^{-1}u_B$，由 $u_B=h_B+Sx$ 得
$x'=A_L^cx+(A_L^c-D_f)S^{-1}h_B$，两侧边界同为(G.2)。没有对 $h_B$ 求导或读取它的端点。

若表内 `low_second_kind_correction` 的(G.28)输出为 $b,a$，则

$$
 \|(I-H_L)^{-1}\|
 \le\left\|\begin{pmatrix}1+b&0\\a&1\end{pmatrix}\right\|_2
 =\frac{\sqrt{(2+b)^2+a^2}+\sqrt{b^2+a^2}}2.
 \tag{G.32}
$$

这个界保留全部193 atoms。若只需要某条完整 source，直接用(G.28)可避免再付这个统一二类逆上界。

## 9. 真实全区间横截性：点接收器与点源列的两个 Gram

节点 SVD 不控制真实节点之间的角度。本节给不同的连续证据。先在比较模型中定义 source covariance 的另一个方向递推

$$
 \mathcal P_{L,m}=0,\qquad
 \mathcal P_{L,i}=P_{L,i}+C_i\mathcal P_{L,i+1}C_i^T,
$$
$$
 \mathcal P_{R,0}=0,\qquad
 \mathcal P_{R,i+1}=D_i(\mathcal P_{R,i}+P_{R,i})D_i^T.
 \tag{G.33}
$$

这里 $P$ 使用 `true_coefficient_defect`。对任一整个 $r$-box $J\subset I_i$，定义

$$
 a_J\ge\sup_{r\in J}
 \left\|u\longmapsto S(r)\int_I\bar G(r,t)\Delta(t)S(t)^{-1}u(t)\,dt\right\|.
 \tag{G.34}
$$

一个可直接实施的平方上界是下列矩阵在整个 $J$ 上的最大特征值上界：

$$
 O_{L,i}(r)\mathcal P_{L,i}O_{L,i}(r)^T
 +O_{R,i}(r)(\mathcal P_{R,i}+P_{R,i})O_{R,i}(r)^T.
 \tag{G.35}
$$

理由是源侧本 panel 的实际两个部分分别被**同一正半定 covariance 的完整积分**支配。不同 source radial pieces 是实际正交输入，因此核行的平方恰为这些 Gram 之和；本式不依赖任意 interval entries 的 Loewner 顺序。

另用 $W=S^{-1}$ 在(G.16)定义 $I^0_{L,i},I^0_{R,i}$。令

$$
 b_J\ge\sup_{s\in J}
 \left\|v\longmapsto S(\cdot)\bar G(\cdot,s)S(s)^{-1}v\right\|_{\mathbb R^{193}\to L^2}.
 \tag{G.36}
$$

它的一个完整平方上界是

$$
 (I^0_{L,i}(s))^T(A_i+Q_{L,i})I^0_{L,i}(s)
 +(I^0_{R,i}(s))^TB_iI^0_{R,i}(s)
 \tag{G.37}
$$

在整个 $J$ 上的最大特征值上界。这里 $A_i,B_i$ 是(G.19)的 **body-only** output covariance；它们没有混入 atoms。两处 complete local covariance 只做有效的正半定外包，不把点 source 当成 $L^2$ 函数。

比较模型的 weighted oblique projections 在 $I_i$ 内为

$$
 \bar P_L^S(r)=O_{L,i}(r)I^0_{L,i}(r),\qquad
 \bar P_R^S(r)=O_{R,i}(r)I^0_{R,i}(r).
 \tag{G.38}
$$

用完整 signed products 和(G.26)求整个 $J$ 上共同上界 $p_J$。若(G.27)通过，则真实 $A_L^c$ 的两侧 oblique projections 满足

$$
 \max_{\alpha=L,R}\sup_{r\in J}\|S(r)P_\alpha(r)S(r)^{-1}\|
 \le p_J+\frac{a_Jb_J}{1-\varepsilon}=:p_J^{\rm true}.
 \tag{G.39}
$$

**命题4。** 式(G.39)控制每个真实半径上的两个完整子空间，不只是某一列或节点。

**证明。** 由(G.29)得到 weighted resolvent kernel identity

$$
 SG_LS^{-1}=S\bar GS^{-1}
 +(S\bar G\Delta S^{-1})(I-E)^{-1}(S\bar GS^{-1}).
 \tag{G.40}
$$

固定第二个 kernel argument $s$，比较列属于 body $L^2$；沿 $r$ 只有有限跳，其值由(G.36)控制。固定第一个 argument $r$，缺陷接收器是(G.34)的有界 functional。于是 correction kernel 的整个 $(r,s)$ 范数由 $a_Jb_J/(1-\varepsilon)$ 控制。沿对角，$\bar G$ 与 $G_L$ 的左右极限分别为 $-P_L$、$P_R$；correction 没有 delta 跳，故两个极限均满足(G.39)。在 piecewise $S$ 的节点分别用左、右值，同一个 raw projection 得到相同覆盖结论。式(G.35)、(G.37)按整个 boxes 计算，所以没有未检查的内部半径。证毕。

raw 投影的共同上界可取

$$
 p_{J,\rm raw}^{\rm true}
 =\max(1,q_i)\max(1,q_i^{-1})p_J^{\rm true}.
 \tag{G.41}
$$

若 $\widehat L(r),\widehat R(r)$ 各自是对应真实 raw 子空间的任意正交列 frame，则

$$
 \sigma_{\min}\bigl(\widehat L(r),\widehat R(r)\bigr)
 \ge\frac1{\sqrt2\,p_{J,\rm raw}^{\rm true}}>0
 \qquad(r\in J).
 \tag{G.42}
$$

确实，对 $z=\widehat L\alpha+\widehat R\beta$，有
$\|\alpha\|\le\|P_Lz\|$、$\|\beta\|\le\|P_Rz\|$，故
$\|\alpha\|^2+\|\beta\|^2\le2(p_{J,\rm raw}^{\rm true})^2\|z\|^2$。
这是真实连续 BVP 的 quantitative transversality，并非将 midpoint 的浮点最小奇异值向外舍入后改称证明。

## 10. 独立边界与 jump 输入的范围

(G.3)当前源接口是 ordinary $L^2$，其输出 atoms 已全付。原独立边界、mean、外 height、affine jumps 的 **输入列** 仍必须保持原单位；它们不会因为输出有193 atoms 就自动得到认证。

在本篇低模型内，任意 raw 左边界 $l\in\mathbb R^{96}$、右边界 $r\in\mathbb R^{97}$ 可以用准确有限 lift 单独处理。比较模型在第 $i$ 段上的两列为

$$
 X_l(t)=R_i(t)D_{i-1}\cdots D_0\,(B_aR_0)^{-1}l,
$$
$$
 X_r(t)=L_i(t)C_i\cdots C_{m-1}\,(B_RL_m)^{-1}r.
 \tag{G.43}
$$

两个显示边界矩阵因命题1而可逆。把两列放在同一个矩阵后计算完整 output Gram，可付它们的共同 Hilbert operator norm；不可把两列对同一 output 的交叉项擅自置零。真实系数解为
$X+G_L\Delta X$，也可由(G.29)得到 model body 除以 $1-\varepsilon$、atoms 加 $e_A$ 乘该 body 的界。实际 port-to-$(l,r)$ 转换及其原范数仍须支付。

有限 jump 列使用(G.15)的准确单侧 kernel 值作为 lift，保留它自己的输入范数；不可给 impulse 乘一个 ordinary source 的 $\sqrt h$。当前数学模块尚未实现(G.43)或原七 port 的逐列 adapter，因此没有把这些输入写进其已求值范围。两条原 RHS 的完整转授同样尚未完成。

## 11. 何时必须保留或吸收完整 CFB

R137 的完整 centre 仍是

$$
 H_c^{\rm cont}=\mathcal OG_D\bigl[A_L^c-D_f+C\mathcal FB\bigr]S^{-1}\pi_B.
 \tag{G.44}
$$

其中 $B$、$C$ 两端只见 modes97..160，但 $\mathcal F$ 保持完整有符号 $G_0,J,J^*$、两个 cutoff 导数和 R137 的所有辅助状态。不是把 high 回路设为零。

由(G.31)有准确 ordered identity

$$
 (I-H_L)^{-1}\mathcal OG_D=\mathcal OG_L.
 \tag{G.45}
$$

所以 low 认证后，仍须处理

$$
 I-\mathcal OG_LC\mathcal FB S^{-1}\pi_B.
 \tag{G.46}
$$

这个算子的 atoms 输入仍不参与回路。若证明完整 body loop

$$
 \|SG_LC\mathcal FB S^{-1}\|<1,
 \tag{G.47}
$$

可据其余完整 source/atoms bounds 反演(G.46)。单独 `centre_high0_return_source` 的(G.28)并不证明(G.47)，因为它后面还要乘同一完整 $\mathcal FB$。可直接组合有符号核再算界；不用把每个原已有粗范数机械相乘。

若当前完整高回路上界不通过，可以改进同一 signed composition，或转到 R137 的完整1217-state/609-endpoint系统，将 $CFB$ 同时吸收到 reference inverse。不能删除高项来保留 low 的良好条件数；也不能因上界失败而宣称实际核存在。反过来，若主要失败来自 $A_L^c$ parent coefficient 包络过宽，改成609 endpoint本身并不收紧这条系数包络，仍须真正的系数 adapter。

即使(G.44)的连续 centre 全部认证，R137 (S.18a)–(S.18c) 的原 finite principal lift、radial projection、$\rho_2-\rho_*$ 和右 lift defect 仍须支付。原 W2C actual-family 差、真实 outer/mean/high observation、全部七独立 port 与两 RHS 也仍须在同一算子上转授。本文没有完成这些目标。

## 12. 源码对应与可执行顺序

配套纯模块实现了以下有向计算接口。

| 函数 | 本文公式与完整范围 |
|---|---|
| `build_comparison_model` | (G.8)–(G.13)，全部155 panel、真实两端边界、有限 charts 与 signed carriers |
| `source_matrix` | 第7节五条明确 source role；真实 $h_i$ 与实际 hybrid $A_L^c$ |
| `local_factors` | (G.14)–(G.16)，整个归一化 box 的正负 matrix exponential |
| `panel_gram_packet` | (G.18)、(G.20)、(G.25)，两个同 panel 三角 |
| `complete_gram_norm` | (G.19)、(G.21)–(G.24)，body、root97、outer96分别返回 |
| `source_covariances` | (G.33)，点接收器所需完整源侧 covariance |
| `actual_low_source_bound` | (G.27)–(G.28)、(G.32)，严格 gap 和明确未完成 flags |
| `whole_box_projection_bound` | (G.34)–(G.42)，整个 box 的真实横截性与 raw frame 下界 |

一个公共 owner 的顺序可固定为：完整原 admission/context；读取或明确定义本次精确 generators/charts；完成全部 model transfers 和边界；先算完整 defect packets 与(G.27)；再算声明的 source packets 与所有 whole-box(G.42)。每个目标只在其所有 panels、全部原 atoms 和所有 boxes 完成时保存完整标量。私有矩阵、Gram arrays 与试探 frames 不作为大型可重算证书提交；保存源码、精确输入定义、hash、run和小结论。试探的浮点设计与真正定向认证是不同的数学目标，但不能把同一次浮点证据既算设计又登记为认证。

模块用同一私有 model token 约束 packets、Gram totals 和 projection receiver，防止不慎混合不同模型或 source role；没有据此增加用户审批或外部审阅流程。它仅做结构静态/AST检查时不会执行任何科学量。本文登记时：该模块已静态通过，科学求值数为0，所有数值小量与成功 flags 仍待公共实际结果。

后续原课题的全无限维逆、实际响应、负侧返回、非线性存在、闭合匹配、可见幅度和 reach 完成标准均保持不变。
