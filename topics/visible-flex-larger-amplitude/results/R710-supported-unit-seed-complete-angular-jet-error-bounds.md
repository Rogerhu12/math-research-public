# R710 — 固定支撑单位 seed：完整均值两角 jet、投影架和四套参考场费用

状态：条件误差定理及对应可执行有理区间核；不重新证明 R708/R709 的准确均值存在，不声称任何尚未向外支付的工作输入已经满足条件。本组件不作为新 seed 首次完整求解的准入门。下述输入都属于同一个固定 seed、同一 literal 角和同一批实际工作字。

## 1. 已有根界和本条消费的数据

沿用 R709 的准确方程
$$
F(v,\phi)=L_cv+B(Nv,\phi)-K(\phi),\qquad N(v)=v/|v|.
$$
准确单位参考在完整四端层满足 $T_{0,z}\ge0$，端层总长度至多 $b$。有完整物理界
$$
0<k_-\le |K|\le k_+,\quad K_z\ge k_z,\quad
b<\min(k_-,k_z),\quad k_++b<L_{c,-}\le L_c\le L_{c,+}.
$$
所有长度单位保持一致；实际 $L_c,b$ 从准确相对端点和准确 $S$ 包围推得，不以工作 np.diff 宽度代替。定义
$$
r_-=(k_--b)/L_{c,+},\qquad
r_+=(k_++b)/L_{c,-}<1,\qquad
\zeta=(k_z-b)/(k_++b)>0.
$$
R709 给唯一准确根 $v_*$，半径 $r_-\le r_*\le r_+$、方向 $d_{*,z}\ge\zeta$。

取一个实际完成批次的三套工作字 $\widehat v_0,\widehat v_1,\widehat v_2$，均按准确 binary64 有理数解释，不先把工作 $d$ 当它们的准确归一化。设 $\widehat r=|\widehat v_0|\in[a_-,a_+]$，$a_->0$，并已付候选准确方向 $\widehat d=N(\widehat v_0)$ 的正垂直下界 $\widehat\zeta>0$。三项输入费用 $E_0,R_1,R_2$ 分别包围：

1. 准确完整 $F(\widehat v_0)$ 的范数。
2. 准确完整一角总方程在形式 jet $(\widehat v_0,\widehat v_1)$ 的范数。
3. 准确完整二角总方程在形式 jet $(\widehat v_0,\widehat v_1,\widehat v_2)$ 的范数。

第二、三项不是原 metadata 中打印的工作残差本身。它们须包括准确四端层、完整补集 $K$、准确 $L_c$、参考角 jet、实际归一化/权/位置、所有 trig 与求和费用。缺少这些费用时，本条不能将其设成零。

直接消费 R709 的证明，并将分母取正下界，得
$$
E_d=\min\{2,\;2E_0/[L_{c,-}(a_-+r_-)]\},\quad
\zeta_*=\min(\widehat\zeta,\zeta),\quad L_B=b/\zeta_*,
$$
$$
E_r=(E_0+L_BE_d)/L_{c,-},\qquad
E_v=E_0/L_{c,-}+(L_B/L_{c,-}+r_+)E_d.
$$
因此 $|d_*-\widehat d|\le E_d$、$|r_*-\widehat r|\le E_r$、$|v_*-\widehat v_0|\le E_v$。这没有重新要求 $q<1$，也没有要求 $E_v<|\widehat v_0|$ 的小根球。

## 2. 两个北半球方向之间的完整端层分母

**引理。** 若 $y$ 位于两个单位方向的线段中，且两端垂直分量均至少 $\zeta_*>0$，则对任意单位 $T_0$、$T_{0,z}\ge0$ 和 $0\le\chi\le1$，
$$
|(1-\chi)T_0+\chi y|\ge
\nu_*=\sqrt{\frac{1-\sqrt{1-\zeta_*^2}}2}>0.
$$

证明：写 $h=|y_h|,z=y_z$。凸性给 $h^2+z^2\le1,z\ge\zeta_*$。由 $T_0\cdot y\ge-h$，
$$
|(1-\chi)T_0+\chi y|^2
\ge(1-\chi-\chi h)^2+\chi^2z^2.
$$
右端作为实 $\chi$ 的二次式，其全实数最小值是
$z^2/[(1+h)^2+z^2]$。分母不超过 $2(1+\sqrt{1-\zeta_*^2})$，分子至少 $\zeta_*^2$，即得所述界。限制 $\chi\in[0,1]$ 只会提高最小值。证毕。

这里线段内部的 $y$ 不必单位；因此该界确实可用于完整两根间的积分微分，而没有把端点结论偷用到整段。

## 3. 所需完整边层导数上界

在该线段上，记 $A=(1-\chi)T_{0,\phi}$、$D=(1-\chi)T_{0,\phi\phi}$，并有完整端层一致界 $|T_{0,\phi}|\le U_1$、$|T_{0,\phi\phi}|\le U_2$。仅消费 [R694](R694-so3-low-order-signed-quadrature-error-algebra.md) 已列归一化导数常数，不重复认领其证明：
$$
\|DN(Y)\|\le1/|Y|,\quad
\|D^2N(Y)\|\le6/|Y|^2,\quad
\|D^3N(Y)\|\le36/|Y|^3,
$$
保留所有方向得到
$$
M=B_d,\quad P=B_\phi,\quad Q=B_{\phi\phi},\quad
N_1=B_{d\phi},\quad C=B_{dd}.
$$
为避免混淆，下文 $N_1$ 是一个矩阵，和归一化映射 $N$ 不同。定义数值上界
$$
M_0=b/\nu_*,\quad C_0=6b/\nu_*^2,\quad C_1=36b/\nu_*^3,
$$
$$
N_0=6bU_1/\nu_*^2,\qquad N_d=36bU_1/\nu_*^3,
$$
$$
Q_d=6bU_2/\nu_*^2+36bU_1^2/\nu_*^3.
$$
它们分别包围 $\|M\|,\|C\|,\|B_{ddd}\|,\|N_1\|,\|B_{dd\phi}\|,\|B_{d\phi\phi}\|$。例如
$$
B_{d\phi\phi}[h]=\int_E\chi\{
D^2N(Y)[h,D]+D^3N(Y)[h,A,A]\}\,ds.
$$
所有 $\chi,1-\chi$ 因子都真实保留在准确式中，上界只用其模不超过1。没有丢掉混合项或某个端层。

## 4. 不靠小根球的归一化导数变化

令 $D_1=DN(v_*)$、$\widehat D_1=DN(\widehat v_0)$，$D_2=D^2N(v_*)$、$\widehat D_2=D^2N(\widehat v_0)$。有
$$
\delta_1:=\|D_1-\widehat D_1\|
\le {E_r\over r_-a_-}+{E_d\over a_-},
$$
$$
\delta_2:=\|D_2-\widehat D_2\|
\le {6E_r(r_++a_+)\over r_-^2a_-^2}
 +{12E_d\over a_-^2}.
$$
证明第一式只需 $DN(v)=(I-dd^T)/r$ 及
$\|dd^T-ee^T\|\le|d-e|$。第二式用
$$
D^2N(v)[h,k]=r^{-2}\{
-(d\cdot k)h-(d\cdot h)k-(h\cdot k)d
+3(d\cdot h)(d\cdot k)d\}.
$$
括号张量范数至多6，对单位 $d$ 的变化为至多 $12|d-e|$；再分开 $r^{-2}$ 的变化即可。这些都是两端的准确代数比较，不需要两条 $v$ 之间的线段远离零。

## 5. 完整一角 jet

同一准确根 Jacobian 为 $J_*=L_cI+M_*D_1$。R709 的正切块证明给
$$
\eta={1\over L_{c,-}}\left(1+{M_0\over L_{c,-}r_-}\right)
\ge\|J_*^{-1}\|.
$$
这里 $\eta$ 是完整通常 Euclidean 范数的逆界，未把非对称 $J_*$ 当作最小奇异值至少 $L_c$ 的矩阵。

候选中心的准确 Jacobian 为 $\widehat J=L_cI+\widehat M\widehat D_1$。整方向线段界给
$$
\Delta_J={C_0E_d\over r_-}+M_0\delta_1
\ge\|J_*-\widehat J\|.
$$
设 $h_j\ge|\widehat v_j|$。将准确一角方程在根与候选中心相减，并只把已知候选 $\widehat v_1$ 放进差值，有
$$
\boxed{E_{v_1}=\eta(R_1+\Delta_Jh_1+N_0E_d)
\ge|v_{*,\phi}-\widehat v_1|.}
$$
候选 $R_1$ 真实包含 $K_\phi$ 和所有实际积分费用；不能只付一个形式 $J$ 差就漏掉目标导数。

## 6. 完整二角 jet：固定候选和未知一角误差分开

准确二角方程写为
$$
Jv_2+Q+2N_1d_1+C[d_1,d_1]+M D^2N(v)[v_1,v_1]-K_2=0,
\qquad d_1=DN(v)v_1.
$$
先把 $v_1,v_2$ 固定为工作字，只移动零阶根。置
$$
c_1=h_1/a_-,\quad
c_2=6h_1^2/a_-^2,\quad
e_1=\delta_1h_1,\quad e_2=\delta_2h_1^2.
$$
上述二角左端的变化至多
$$
\begin{aligned}
D_2^{(0)}={}&\Delta_Jh_2+Q_dE_d\\
&+2(N_dE_dc_1+N_0e_1)\\
&+C_1E_dc_1^2+C_0(2c_1e_1+e_1^2)\\
&+C_0E_dc_2+M_0e_2.
\end{aligned}
$$
各行依次对应 Jacobian/纯角项、混合矩阵、二方向张量、归一化二阶项。不能把最后 $M D^2N$ 隐入常数而不支付 $M$ 和 $D^2N$ 的两份变化。

再在准确零阶根处把 $v_1$ 从候选移到真实值。设 $E_1=E_{v_1}$，该变化至多
$$
D_2^{(1)}
={2N_0E_1\over r_-}
+{C_0+6M_0\over r_-^2}(2h_1E_1+E_1^2).
$$
因此
$$
\boxed{E_{v_2}=\eta\{R_2+D_2^{(0)}+D_2^{(1)}\}
\ge|v_{*,\phi\phi}-\widehat v_2|.}
$$
$R_2$ 是同一个候选完整二角总方程的准确残差上界，$D_2^{(0)}$ 和 $D_2^{(1)}$ 则只付根位置和未知一角解变化，不重复或省略工作积分费用。

## 7. 方向、半径和投影架的有理区间输出

对每个分量，先用实际工作字和上述三项范数误差建立准确 $v_0,v_1,v_2$ 的盒。以准确根半径 $[r_-,r_+]$ 与该盒计算的范数盒相交，记结果 $r$，再完整计算
$$
d=v_0/r,\quad
d_1=v_1/r-v_0(v_0\cdot v_1)/r^3,
$$
$$
d_2=v_2/r-
{2v_1(v_0\cdot v_1)+v_0(|v_1|^2+v_0\cdot v_2)\over r^3}
+{3v_0(v_0\cdot v_1)^2\over r^5}.
$$
方向零阶还可与 $|d-\widehat d|\le E_d$、每分量 $[-1,1]$、$d_z\ge\zeta$ 的准确盒相交。半径角 jet 完整为
$$
r_1=d\cdot v_1,\qquad
r_2=d\cdot v_2+|v_1|^2/r-(v_0\cdot v_1)^2/r^3.
$$
有理区间计算保依赖损失，绝不把区间中点当实际准确值。

由同一个准确固定图输入 $e,e_1,e_2$，令
$$
a=e\cdot d,\quad a_1=e_1\cdot d+e\cdot d_1,\quad
a_2=e_2\cdot d+2e_1\cdot d_1+e\cdot d_2,
$$
$$
y=e-ad,\quad y_1=e_1-a_1d-ad_1,\quad
y_2=e_2-a_2d-2a_1d_1-ad_2.
$$
因准确 $e$ 是水平单位向量且 $d_z\ge\zeta$，有 $|y|\ge\zeta$。对 $(y,y_1,y_2)$ 使用同一完整归一化公式，得到 $w,w_1,w_2$ 的区间。这里 $e$ 的盒必须已支付固定图 trig 和原输入误差，不能把 provider 的普通浮点 e 字当准确单位向量。

所有区间端点是 Fraction。平方根以整数 isqrt 给向外二进有理上下界；除法只对已证明的正分母进行。计算所得盒与实际保存 d/w 字的逐分量距离给完整工作误差，包含被比较工作归一化和内积的全部舍入影响，不再假设其 libm 误差为零。

## 8. 中央幅度及两角 jet

由 R709 的真实根长度区间及 $0<\epsilon<\min(1/8,r_-/4)$，准确幅度根唯一在 $(0,\pi/2)$，且
$a_\epsilon(\lambda)\ge\cos\lambda$ 给 $\lambda\ge\arccos r_+$。
实际工作字 $\widehat\lambda$ 也须在该开区间。

完整 profile 常值平台总长为 $1-4\epsilon$，其余部分满足 $|h_\epsilon|\le1$，所以在连接准确根与候选的区间上
$$
-a_\epsilon'(\lambda)\ge
m:=(1-4\epsilon)\min\{
\sin\widehat\lambda,\sqrt{1-r_+^2}\}>0,
\qquad |a_\epsilon''|,|a_\epsilon'''|\le1.
$$
$m$ 的两项均实际向外计算。这不调用未经证明的工作 a' 最小值。

输入三个已付盒 $A_j$ 包含准确 $a_\epsilon^{(j)}(\widehat\lambda)$，它们来自实际完成批次三个 profile moment 字加完整准确积分费用。设 $R,R_1^\rho,R_2^\rho$ 是上一节准确 $r,r_1,r_2$ 的盒，$\|\cdot\|_{\rm abs}$ 表示标量区间最大绝对值。先得
$$
E_{\lambda_0}={\|A_0-R\|_{\rm abs}\over m}.
$$
取实际 $\widehat\lambda_1,\widehat\lambda_2$，再得
$$
E_{\lambda_1}=
{\|A_1\widehat\lambda_1-R_1^\rho\|_{\rm abs}
 +E_{\lambda_0}|\widehat\lambda_1|\over m},
$$
$$
E_{\lambda_2}=
{\|A_1\widehat\lambda_2+A_2\widehat\lambda_1^2-R_2^\rho\|_{\rm abs}
 +E_{\lambda_0}(|\widehat\lambda_2|+\widehat\lambda_1^2)
 +2|\widehat\lambda_1|E_{\lambda_1}+E_{\lambda_1}^2\over m}.
$$
这三式分别是准确零、一、二角方程的残差差值；最后一式保留 $a''$ 的角一阶平方变化。工作 a(0) 的权和不参与这些准确函数恒等式，所有求积差已在 $A_j$ 中支付。

## 9. 完整参考节点四 jet 和实际字的费用

对于中央节点，用准确 profile 盒 $h,h_s$ 和上一节三套 $\lambda$ 盒形成
$\alpha=h\lambda,\alpha_1=h\lambda_1,\alpha_2=h\lambda_2,\alpha_s=h_s\lambda$。
sin/cos 通过有理 Taylor 多项式及全实数导数不超过1的余项向外计算，不依赖工作 libtrig。按真实公式计算
$$
T=c_\alpha d+s_\alpha w,\quad
T_\phi=c_\alpha d_1+s_\alpha w_1+\alpha_1(-s_\alpha d+c_\alpha w),
$$
$$
T_{\phi\phi}=c_\alpha d_2+s_\alpha w_2+2\alpha_1(-s_\alpha d_1+c_\alpha w_1)
+\alpha_2(-s_\alpha d+c_\alpha w)-\alpha_1^2T,\quad
T_s=\alpha_s(-s_\alpha d+c_\alpha w).
$$
其中 $c_\alpha=\cos\alpha,s_\alpha=\sin\alpha$，后者不是径向变量 $s$。

对于端层节点，消费准确 $T_0,T_{0,\phi},T_{0,\phi\phi},T_{0,s}$ 和准确 $\chi,\chi_s$ 盒，完整形成
$$
Y=(1-\chi)T_0+\chi d,\quad
Y_1=(1-\chi)T_{0,\phi}+\chi d_1,\quad
Y_2=(1-\chi)T_{0,\phi\phi}+\chi d_2,
$$
$$
Y_s=(1-\chi)T_{0,s}+\chi_s(d-T_0).
$$
再用完整归一化一二角 jet 和 $T_s=Y_s/|Y|-Y(Y\cdot Y_s)/|Y|^3$。分母下界可用准确 $d_z\ge\zeta$ 的端层界。支撑外直接使用准确原参考四 jet。

每个所得向外向量盒直接和此次实际 provider/cache 的四套工作字比较，输出逐分量和 Euclidean 范数上界。这样所有被比较工作实现中的加法、乘法、trig、归一化和形状相关求和费用都在整输出差中，不能在末端另把它们默认为零。节点的准确 scalar、profile 位置/宽度和原参考盒仍由其真实消费者提供，本组件不伪造这些输入盒。

## 10. 可执行接口与来源范围

配套源将以完整实际 driver/report/seed/provider/kernel 身份读取一个真实完成均值 batch，校验 batch 原始数组 SHA、literal 角序列和 seed identity；只在公开 Actions 消费原始数组。费用请求须同一 batch、同一角，完整列出 $E_0,R_1,R_2$、准确 $S/K$ 与参考角界、profile 三矩费用、固定图盒，以及所请求节点的实际字和准确输入盒。不提供任一费用则拒绝该条件计算，不把它设成零。

结果区分：已执行的有理条件计算、外部输入费用的认证责任、实际批次工作值、请求节点范围。它不是全角或全曲面完成证书，未认证的外部费用不能被输出摘要升级。它不改变当前 seed 的根算法、正常求解预算、全部 free 变量、normal 同支链、原完整几何筛或 README 完成标准。

所有外层 normal 引入的进一步积分/隐式误差仍由 R707 的完整链承担；本条只使新固定参考四 jet 的费用可被该链真实消费。

## 11. 完整源码接口与必须提供的费用

配套完整源为 supported_unit_seed_angular_jet_error_bounds.py。它提供 mean_jet_bounds(seed, working, fees)、bound_reference_node(mean, node) 和独立 CLI；没有改任何已排科学求解源码。全部科学入口要求实际公开 Actions 仓库，源码本地只做 stdlib AST/compile/py_compile、重复字面 key/keyword 和尾空白检查，没有数值试验或科学模块导入。

完整 CLI 的参数为 --repo、--report、--batch-index、--fees、--output；可用 --batch-arrays 指向另一个路径，但必须逐 SHA 等于原实际批次；可指定 --precision-bits（默认160）和 --taylor-order（默认48）。没有附带一个假装准确费用为零的可执行请求。本次新 seed 首跑无需调用这层。

实际报告先捕获完整 bytes 和 SHA，再由已锁完整 d788 纯 reader 核验，要求 reader 返回同一 SHA；raw JSON 只解析捕获的 bytes，完成批记录与 pure 结果逐值一致。随后再核 e482 driver、30ea provider、bd9c kernel 和同一完整 seed model 的真实身份。读取相应完成批记录的原始 npz 时重新校验完整 SHA、seed identity、全部 literal phi.hex、所有九个向量数组和六个标量数组的 shape、float64 类型、有限性。读完全部数组后再次核 report 和 raw 数组 SHA 未变；费用请求也只解析一次捕获 bytes，并记录该 bytes 的摘要。没有 raw 报告或数组经集成上传。当前 batch 的完整角列表必须和费用请求逐项相同，不静默漏角。

费用请求 schema 为 actual-supported-unit-seed-accurate-fee-request-v1，binding 必须包含且逐项等于当前读取对象：

- report_sha256。
- supported_unit_seed_identity_sha256。
- actual_raw_batch_sha256。
- fixed_scalar_metric_identity_sha256。
- fixed_chart_core_sha256。

每个角的 fees 必须显式包含以下量；所有数或区间端点是有理字符串或整数，工作字另用 canonical float.hex。

| 字段 | 准确含义 |
|---|---|
| accurate_S_enclosure | 同一准确符号域 $S$ 的向外正区间。准确相对支撑/端层参数直接从 seed model 读取。 |
| K_norm_lower、K_norm_upper、K_vertical_lower | 本角完整准确 $K$ 的下/上界，必须包括整个补集与无限尾。 |
| accurate_reference_unit_and_nonnegative_vertical_on_complete_boundary | 所列完整端层假设的外部已付声明；本算术核不会自行认证它。 |
| accurate_centered_total_equation_residual_norms | 三个非负上界 $E_0,R_1,R_2$，分别针对同一实际候选零、一、二 jet 的准确完整总方程。 |
| boundary_reference_phi_norm_upper、boundary_reference_phiphi_norm_upper | 完整端层原参考的两角导数范数上界。 |
| accurate_profile_moment_absolute_errors | 准确 $a,a',a''$ 在实际候选 lambda 上与批次三个 profile moment 工作字的绝对差。 |
| accurate_fixed_chart_radial_jets | e、ep、epp 三个 world 向量盒，含全部固定图/三角函数费用。 |
| fixed_chart_e_is_the_accurate_horizontal_unit_radial_vector | 投影架下界所用准确几何事实的外部已付声明。 |

外部费用来源对象 external_fee_provenance 原样保留。程序检查其对象/角/源身份和所有必要字段，不谎称这一步验证了其数学上界；输出 input_fees_certified_by_this_module 与 external_fee_enclosures_certified_by_this_module 均为 false。这和 R707 的条件核性质相同。缺项、矛盾正界或不能解析的正分母明确失败，且失败不表示物理场不存在。

每个可选节点给 region、准确地址、same_field_node_binding、四套 actual_working_fields，以及该 region 所需准确输入盒。节点 binding 和地址必须同 seed、provider、literal 角。端层需完整 accurate_original_reference 四 jet、accurate_chi 和 accurate_chi_s；中央需 accurate_h 和 accurate_h_s；支撑外需原参考四 jet。节点工作字和其准确径向地址的外部消费者仍承担来源证明，本模块的 external_node_values_and_accurate_input_enclosures_verified_by_this_module 明确为 false，不能用仅写一个来源字符串来升级为整场证书。

## 12. 向外算术、π 与实际工作差

所有区间运算都先用准确 Fraction 完成端点运算，再向外舍入至声明的二进精度，避免不受控增长的有理分母。平方单独处理跨零区间，不能把同一区间的独立乘积下界误用于平方根。sqrt 的整数 isqrt 上/下界包含准确实根；已知正半径、单位范数和半球事实只用于合法区间相交。

sin/cos 使用整个 Taylor 多项式和全实数导数范数至多1的 Lagrange 余项，不依赖系统 libm 的正确舍入。π 由
$$
\pi=16\arctan(1/5)-4\arctan(1/239)
$$
和两条交错 arctan 级数的下一项余项向外得到。这个身份可由准确有理正切加法验证正切为1、并将 $4\arctan(1/5)-\arctan(1/239)$ 定位在 $(0,\pi/2)$ 得出；交错余项也直接来自 $1/(1+x^2)$ 的有限几何级数积分。因此不把一串未经包围的十进 π 载体当准确边界。

完整均值输出含 v/d/w/lambda 三套区间、全部实际字差、两角残差传播常数、半径盒及准确长度界。节点输出含四套向外 world 向量、逐分量与 Euclidean 误差上界。完成一个实际 batch 的条件运算只使报告 complete=true；全角/整面/外层 normal/几何证书字段始终为 false。程序逐角原子写入已经完成的结果，后角失败不会丢掉前面的条件计算，也不会把已算部分冒全部成功。

这里交付的是完整证明和可执行费用消费核。补齐本 seed 的准确完整残差/矩积分/固定图/节点输入盒仍是独立工作，不能以本核存在代替那些费用，也不能将它变成尚在推进的新科学入口的等待条件。
