# R141 补篇：实际物理外块闭合后的原七粗端口与非齐次列

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

本篇把[参考边界与实际外块](R141-supplement-reference-boundary-lifts-and-physical-outer-block-gate.md) B4–B21的**已付门之后**落实为明确的16行、14列小标量响应表。原negative-window七个high输入、八个完整high输出逐一保留，并加入两种ordinary low源、真正root-even96、已换chart的right97，以及独立physical height/Robin/mean三列。**目前没有假定待运行的low193或58量physical门已通过，也没有执行本篇数值。**

这是一项后继明确合同与纯源码；它不把条件性结论登记为实际完成，不重做已有R141、D、GH5、GH4、weighted或negative-high目标。全部下式只有在同一完整actual internal/physical gate实际通过后才可公共计算。

## P1. 准确状态、门及原端口

记低raw解为 $h_L$，$x=Sh_L\in L^2(I;\mathbb R^{193})$ 为body变量；另保原root odd96加moving mean的97观察、$\Theta$-weighted outer-even96观察及其联合193atoms。观察下标仍为
$J=B,R,O,A$，依次是body、root97、outer96、joint atoms193。

沿用 B.13、B.18–B.21：已付 $\kappa_B<1$ 与保存下界
$\gamma\le1-\kappa_B$、$\gamma>0$；已付实际right97 lift $\mathcal P$、joint193边界lift $\mathcal Q$、outer-low high-Poisson返回 $\mathcal J_b$，其四receiver界为 $p_J,q_J,j_J$。$q_J$对输入$(l,r)$联合Euclidean范数有效，故限制到$(l,0)$仍合法，未用right97界替代root-even96。

已成真实193外块的非负逆majorant记为

$$
M=(I-N)^{-1}_{\rm majorant}\in\mathbb R_+^{2\times2},
\qquad (\|r\|,\|b\|)^T\le M(e_r,e_b)^T,
\quad b=\Theta h_{L,2}^{\ne0}(R).
\tag{P.1}
$$

这里 $M$ 必须读自完整58量结果的四个已存upper；不得根据未过门的matrix或浮点SVD生成。原 $r=(\Theta(h_L^o+p_0h_L^e)(R),h_L^m(R))$始终包含独立moving mean。

高状态严格沿用[原negative-one报告](R133-supplement-full-delta-negative-one-positive-source-and-regular-ports.md) 的 $Y=M_\phi^{-1}Z$，其中 $M_\phi=|4j|\ge388$。为避免与(P.1)冲突，以下 $M_\phi$只表示频率权。原七非负输入大小按原顺序是

$$
d=(s,F_c,F_b,B,J_c,J_s,J_u).
\tag{P.2}
$$

$s$是原stable-root $Y$端口；$F_c,F_b$是普通 $L^2_rH^{-2/3}_\phi$源；$B$是原body独立outer/mean/head及$Y$-weighted jump输入；后三个jump保原新 $Y$单位。raw jump若从 $H^{-2/3}$输入，仍先付原报告的frame/Bessel转换，不能把raw jump大小直接放入$J_c,J_s,J_u$。这里的独立$B$不含待求$b$所产生的$\beta_b b$；ordinary高源也不含待求$x$所产生的$Bx$。这两项在反馈中单独保留。

原negative summary的八行完整系数记为 $R_{\alpha k}$，$k=0,\ldots,6$。输出次序为：body incoming stable-cut $Y$、collar incoming unstable-cut $Y$、true-root outgoing unstable $Y$、body-$Y$ sup、collar-$Y$ sup、全正区$Y$ sup、raw $L^2_rH^{-1}_\phi$、nonmean primitive $L^2_rL^2_\phi$。记raw行 $C_k$、body-$Y$行 $Y_k$。不从这些粗端口输出取得整高raw $L^2$。

## P2. 任一原high列的准确低返回

R141四源和B.8的已付receiver给 $g_{C,J},g_{0,J},g_{S,J}$，分别对应 `centre_high0_return_source`、`ordinary_raw_low_source`、`transformed_low_source`。第四角色 `low_second_kind_correction`仍由已付$\kappa_J$和边界$\mathcal P,\mathcal Q$完整保留；它不是可删除的source。

令 $d_C$是GH5完整family $\Delta C_0$ 的raw-$L^2$界。中心接收支集到160，family接收到288，故准确可取

$$
a_J=\sqrt{1+16\cdot160^2}\,g_{C,J}
 +\sqrt{1+16\cdot288^2}\,g_{0,J}d_C.
\tag{P.3}
$$

这来自对真正 $C_c$及$\Delta C_0$输入壳的有限投影，再用原 $H^{-1}$norm。原mean行、完整有序primitive和独立source被这些完整算子保留；没有把未知high场截至288。

对任意(P.2)数据，先以原整行求

$$
c(d)=\sum_k C_kd_k,\quad
t(d)=4\sum_kY_kd_k,\qquad
u_J=a_Jc(d)+u_J^{\rm low}.
\tag{P.4}
$$

其中 $u^{\rm low}$是本次已声明direct low源的真实hybrid-low响应。通过原实际内部闭合，

$$
v_B=u_B/\gamma,\quad
v_J=u_J+\kappa_Jv_B\quad(J=R,O,A).
\tag{P.5}
$$

若另有原raw root-even96数据$l$，将 $q_J\|l\|$加到(P.5)的每个$v_J$。$\mathcal Q$已经经过同一内部闭合，不能再次除以$\gamma$或重复加$\kappa_J$。其right97输入在本列取0，待求right97仍由$\mathcal P r$处理。

对第$k$个原high输入的单位列，(P.4)准确使用 $c=C_k,t=4Y_k$；无需重算原高逆。$4Y_k$是原negative外端even frame row的trace界，不从body-$H^{-1}$取端点。

## P3. 原 signed physical 方程与非齐次 RHS

沿用H.15–H.18的真实physical-angle/DN/mean chart，准确方程为

$$
r=A_bb+A_hy_H+g,\qquad
g=(-\Theta P_L\rho_B,\rho_C),
\tag{P.6}
$$

$$
h_H=G_HBx+P_bb+h_d,\qquad
y_H=T_xx+T_bb+t_d,\qquad
\mathcal Oh_L=x_0+\mathcal P r+\mathcal J_b b.
\tag{P.7}
$$

在(P.7)末式，$x_0$代表完整body+atoms观察，且其四receiver界为(P.5)的$v_J$。原Hilbert的odd/even符号已经在(P.6)中明确保留；$p_0-p_\delta$的项在$A_b$内。此时对真实97+96方块的右侧，

$$
e_r\le \|g\|+a_h\{t(d)+t_Xv_B\},\qquad e_b\le v_O.
\tag{P.8}
$$

第二式来自原 $b=O_bh_L$，不是附加一个任意outer96数据。先用(P.1)得到$R_d,B_d$，再取

$$
X_J=v_J+p_JR_d+j_JB_d,\quad
X_{\rm complete}=\sqrt{X_B^2+X_A^2}.
\tag{P.9}
$$

root97、outer96以及joint193三种观察都各自保存。联合atoms上界始终用原joint receiver，不能把两个分别估计的端点错误地赋予共同输入正交性。complete的平方和只来自body和atoms的真实Hilbert输出直和。

## P4. 独立physical height、Robin和mean如何进入两处

这三种数据同时驱动(P.4)中的高外affine列和(P.6)中的低right97源。两条路径都要保留，不能只加入其中一条。

原negative N.10–N.12的已存符号为
$B_a$=`independent_Robin_multiplier`、$C_a$=`independent_mean_multiplier`，
$U_-$=`negative_DN_fB_to_d`、$V_-$=`negative_DN_fB_to_mean`。
原mean输出三列为$(m_y,m_F,m_C)$，实际高affine输出四列为
$(\beta_b,\beta_F,\beta_R,\beta_C)$，各自保原literal input order。

真实独立height范数是原DN的
$F_B=\||D|^2\delta f_B\|_{H^{-5/6}}$；ordinary Robin残差范数是 $\|r_B\|_{H^{-5/6}}$；原mean残差为$|r_C|$。已完成chart给

$$
\begin{aligned}
\|\rho_B\|_{H^{-5/6}}
&\le(B_aU_-+C_aV_-)F_B+B_a\|r_B\|+C_a|r_C|,\\
|\rho_C|&\le m_FF_B+m_C|r_C|.
\end{aligned}
\tag{P.10}
$$

$\rho_C$是chart后的mean源；不是把$r_C$改名。$m_y$作用于完整$y$的项已经在$A_b,A_h$中，不能再次放入右侧或丢掉。

由于right97的非均值96槽与mean槽是真正输出直和，三种单一输入的$g$界可取

$$
g_F=\operatorname{hypot}(B_aU_-+C_aV_-,m_F),\quad
g_R=B_a,\quad g_C=\operatorname{hypot}(C_a,m_C).
\tag{P.11}
$$

相应(P.2)的唯一非零高外canonical输入为

$$
d_3=\beta_FF_B,\qquad
d_3=\beta_R\|r_B\|,\qquad
d_3=\beta_C|r_C|.
\tag{P.12}
$$

这三个$\beta$已包括原完整high exterior graph的frame/resolvent费用；不再额外乘同一个exterior resolvent。未知$b$的$\beta_b b$继续在(P.7)中保留，未混入(P.12)。actual angle、height和$\rho_C$单位均沿原外图，不从moving mean免费转为physical-density mean。

若独立数据被编码为原第4端口$B$，则原七端口表也能消费它；同一物理输入的后继应选择明确的(P.12)注入方式，不将它当作另外一个独立物理输入重复登记。多数据的响应使用正行向量之和，不假定对应解输出彼此正交。

## P5. 回收原全部八个high观察

对光滑head forcing这一项 $G_HBx$，新weighted合同W.9中root stable输入为0，故 $U=S_c$。所以已存$H_{\rm root}$除界住真正root outgoing外，也给该**特定head响应**的完整collar-$Z$ sup。由 $Y=M_\phi^{-1}Z$ 且 $M_\phi\ge388$，可取

$$
Y_{b,x}=H_Z/388,\quad Y_{c,x}=H_{\rm root}/388,
\quad Y_{*,x}=\max(Y_{b,x},Y_{c,x}).
\tag{P.13}
$$

head的body cut stable、collar cut unstable、root outgoing、body sup、collar sup、全域sup六行分别由
$Y_{b,x},Y_{c,x},Y_{c,x},Y_{b,x},Y_{c,x},Y_{*,x}$支配。这里没有将一个含任意root stable数据的rough高图的root-outgoing行当成其collar sup；那些数据仍逐列使用原八行$R_{\alpha k}$。

同一head项已付raw $L^2$上界$H_B$，且只有$j\ge97$高频。因此它的raw-$H^{-1}$及nonmean primitive-$L^2$两行均有上界

$$
H_{-,x}\le H_B/388,\qquad H_{I,x}\le H_B/388.
\tag{P.14}
$$

第一式用$\langle M_\phi\rangle^{-1}\le1/388$，第二式用真正primitive的$M_\phi^{-1}\le1/388$。这只降低一个已付光滑项的输出阶数，**不提升任何粗源的raw正则性**。

记(P.13)–(P.14)对应八行为$H_{\alpha x}$。完整实际解于是逐行满足

$$
\mathcal H_\alpha
\le \sum_kR_{\alpha k}d_k
 +H_{\alpha x}X_B
 +R_{\alpha3}\beta_b B_d.
\tag{P.15}
$$

三项依次为全部独立高数据、实际low-body forcing、以及待求outer-low的真实高Poisson列；同一反馈没有重付或遗漏。原head forcing在base-order及negative窗口是同一真实高算子，由原共同参考和唯一性识别，不能另造一个更光滑$G_H$。

另外保留真正root的两个高分量。其stable数据大小为$s$，outgoing大小由(P.15)的root行给出；原逆frame转换常数9作用于两component直和，故

$$
\|h_H(r_*)\|_{H^{-2/3}\times H^{-1}}
\le9\sqrt{s^2+\mathcal H_{\rm root}^2}.
\tag{P.16}
$$

高mean不存在于(P.16)；独立moving mean由低root97保留。原raw mixed root**输入**若用于$s$，其原 $9(17/16)$转换仍需在实际数据注入时付清，不能把(P.16)的反向因子倒用。

## P6. 具体14列和16行的可执行接口

纯模块 `fourfold_codazzi_completed_physical_gate_ports_math.py` 不含IO、数值imports或旧producer。入口

`complete_original_ports(api, core, admitted, closed, weighted, read_saved_gate_endpoint, emit)`

在原58量实际门之后运行。`core`为既有纯scalar模块，`admitted`保持其四源和完整negative对象；`closed`是同真实58量结果或其精确readback重建。它必须带true internal/physical gates、58条完整记录和same reference；任何缺失low/false门结果都不能调用。gap及$a_h$从已存原gate记录读回，不重新计算旧目标。weighted作为自身whole实际文件读取，绝不伪装成旧GH4。

14个输入列依次为：原7个(P.2)，ordinary raw low-$L^2$，transformed low-$L^2$（先一次$S^{-1}$），raw root-even96，already-charted right97，最后是(P.10)–(P.12)的height/Robin/mean三列。两种low源是明确的两种输入坐标，使用各自R141角色；给定物理RHS究竟放哪一列必须由其准确坐标转换决定。

16个输出依次为：待求right97、待求outer96，low body/root97/outer96/joint193/complete共5行，原8个high观察，以及(P.16)的真正root high mixed输出。每列依此次序保存；共 **224个新的小scalar记录**。所有初始source/closure计算是新响应公式的运行期中间量，不另宣称旧bounds被重新计算。

模块先保存该列$R_d,B_d$并使用读回upper形成low各行；完整low body保存后，再用于所有high行。最终root mixed行使用已存high outgoing readback。`emit`须whole-ball写入/完整读回/核包含原upper，模块还核返回方向。记录名用列号与固定output code，完整input/output order保留语义，不复制大数组。

这224量只有一个预先声明的完整目标：14列×16行全部完成。输入未具资格或中途失败，保存真实已完的column-major前缀与异常；不把前缀补零。future owner可在同一声明含此目标的公共小scalar运行中，待58量门通过后执行；也可在后继独立运行中消费whole58量成功。两种方式都不能重跑已成R141/D/GH目标。

## P7. 仍须保留的实际问题

本表完整结清其声明的原七high端口、两ordinary low源、实际两边界输入与三physical外源的响应，前提是实际门已经通过。它不为原low affine seam/jump自动制造Green点源界；若实际RHS含独立low跳项，须先提供其真正四receiver的完整响应，再按(P.4)–(P.9)同式接入。`L^2` ordinary源不能把Dirac jump当作零范数。

独立$\nu$或参数方向的实际source大小也没有被本表生成或设零。正区compact bump的既有零事实不删除germ、negative侧或原接缝带来的非齐次输入。原4roles的mean、physical-density两mean、physical-$\theta$读出、原primal/dual ports的具体数据映射均保持原资格。

即使本224量全部成功，原WPN finite行与radial mean-zero tail行的两个完整RHS、真实$G_H$与旧WJK $F$差或原finite-$\rho$新桥、negative连接及非线性邻域仍须分别完成。本篇不给它们置true，也不提前宣布最终精确可见闭族完成。
