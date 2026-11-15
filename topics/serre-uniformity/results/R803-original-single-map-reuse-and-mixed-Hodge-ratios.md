# R803：单个原映射复用、694维混合 Hodge 比值与原 η 的精确加法接口

日期：2026-11-15。状态：**本篇证明原单映射复用的数学接口、最小新增低权输入及完整主函数运输；没有运行新的坐标求解、极除子或高度计算。**

本篇接 [R791 的真实结果](R791-certified-original-Hom-descent-and-eta-inputs.md)、
[R794 的真实基变换](R794-certified-original-low-degree-eta-basis.md) 和 R787 原函数接口。
原 $f=f_4$、$C/L:y^2=x^3+b$、$K=\mathbb Q(\zeta)$、$s=1+2\zeta$、
$L=K(b)$、$q,c_0,c_1$、原微分和实际 $\kappa=qq^\dagger$ 均不改变。
本篇的函数合成以一份已经通过全部原关系的 $y_f=A/B$ 为输入；
正在运行的 R787 不因本篇而改写或重做。

## 1. 复用五个已证方向，不假设整数循环生成

R791 的真实算子为
$$
T(f)=D_{\rho^{-1}}\sigma(f),\qquad
D_u(x,y)=(u^2x,u^3y),\qquad
\rho^6=\sigma(b)/b.
\tag{803.1}
$$
它是原 Galois 作用与目标同构的复合，不是 $Y$ 的自同构。
记
$$
\rho_j=\prod_{i=0}^{j-1}\sigma^i(\rho),\qquad \rho_0=1.
$$
于是
$$
T^jf=D_{\rho_j^{-1}}\sigma^j(f),\qquad
h_j^{\rm map}:=(T^jf)^*\omega_C=\rho_j\sigma^j(h_f).
\tag{803.2}
$$
本篇的上标 $\mathrm{map}$ 区分此原映射微分与下文的 NS 元素 $h_j$。

R794 证明 $\mathbb Q[T]f$ 是整个十二维有理 Hom 空间，
却没有证明 $\mathbb Z[\zeta,T]f$ 等于原完整整数 Hom 格。
因此若 $Df_i$ 才是轨道的整数和，不能凭有理循环性除以 $[D]$，
更不能任选一个椭圆除法原像。

本篇直接用原五个整数映射
$$
g_j=f+T^jf,\qquad1\le j\le5.
\tag{803.3}
$$
它们在 R791 已给原 $F^0$ 的完整基
$$
h_j=\kappa^{-1}e_R(S_j-r_j),\quad
S_j=T^j+T^{-j},\quad
e_R=\kappa v_R^\dagger v_R,
\tag{803.4}
$$
其中
$$
(r_1,r_2,r_3,r_4,r_5)
=\left(\frac{31}{67},-\frac{41}{67},-\frac{34}{67},
\frac{34}{67},\frac{103}{134}\right).
$$
R794 的真实可逆矩阵 $C$ 满足 $H_{\rm selected}=H_{\rm R791}C$。
所以算出这五个原方向后按同一个 $C$ 运输，即得到所选五方向；
不需要先从有理循环式构造五个低次数 $f_i$ 本身。

R764 已给完整整数 Hom 格在原 $c_0$ 和全部原 cusp 的零平移。
因此 (803.3) 没有新的 Abel 常数或目标平移。

## 2. 必须补全的四个方向及42阶准确短基

沿用 R767
$$
\mathcal L=K_Y+\mathcal D,\qquad
g(Y)=127,\quad\deg\mathcal L=272,\qquad E=P_0+P_1,
$$
其中 $\mathcal D$ 是二十个 cusp，$P_0,P_1$ 是原两个阶三椭圆点。
原粗曲线线丛等式给
$$
\boxed{
M_6(\Gamma_Y)=H^0(3\mathcal L+2E),\quad
\deg(3\mathcal L+2E)=820,\quad\dim M_6=694.}
\tag{803.5}
$$
普通 $V_3=H^0(3\mathcal L)$ 只有690维。混合 Hodge 三积属于 (803.5)，
不能无证放入普通 $V_3$。

实际上
$$
M_6=V_3+E_4V_1+\langle E_6,\eta_{\rm Ded}^{12}\rangle.
\tag{803.6}
$$
证明沿 R767 的两层主部：$E_4$ 在每个 $P_i$ 给一阶最高主部，
$V_1$ 在两点的评价满射，故补出第一层的两维；
$E_6,\eta_{\rm Ded}^{12}$ 给第二层的两维，因为原
$$
(E_6/\eta_{\rm Ded}^{12})(P_0)=-24s,\qquad
(E_6/\eta_{\rm Ded}^{12})(P_1)=24s
$$
不同。这证明维数差恰为四，不指定未经读取的行号。

具体基严格读取已经完成的 “R775-basis-M6-complete.json.gz”。
它的真实 SHA256 为
“70ff7536b50bf99ffb422b7c17dd320b535738fcfcc562fd1597eebcb7a0b299”；
该 producer 是成功 run43679160495。
其普通690行逐 recipe 对应 R786 原 power3。
已只读核对原 stage 的四条实际补行（零起始）：

| 原 M6 行号 | 原准确 recipe |
|---:|---|
| 690 | $E_4T_0$，原 M2 第0行 |
| 691 | $E_4T_{73}$，原 M2 第73行 |
| 692 | $E_6$ |
| 693 | $\eta_{\rm Ded}^{12}$ |

它们分别保持原 “elliptic_layer_product” 与 “level_one” schema。
这里仅抄录已有成功产物并核原 SHA，没有在本地计算新数学。
不能重新选一份几何基代替这些 $K$ 定义原基。

**定理803.1。** 原完整 $q_Y^0,\ldots,q_Y^{41}$ 前缀在 $M_6(Y/L)$ 上单射。

**证明。** 若这42项为零，参考 cusp 的零阶至少42。
原二十 cusp 是一个 degree20 的 $L$ 闭点，故每个 cusp 都有该零阶。
非零 (803.5) 截面的零次数于是至少840，大于820，矛盾。$\square$

这个界包括指数41，不能误写成只读41项。
原 $q_Y,\xi$ 的40坐标给一个 $1680\times694$ 有理矩阵。
所有原 basis 配方的 Fourier 系数属于 $\mathbb Q(\xi)$，
所以矩阵条目确在 $\mathbb Q$；这不把原扭曲曲线上的每个基截面泛称为
$\mathbb Q$ 定义。

新增四行的准确前缀尤其小：
$$
E_4=1+O(q_Y^{82}),\qquad E_6=1+O(q_Y^{82}),\qquad
\eta_{\rm Ded}^{12}=q_Y^{41}+O(q_Y^{123}).
\tag{803.7}
$$
旧690行直接截读 R786，原补行中的 $E_4T_i$ 在本范围只是读取旧 M2 行。
若整数基统一为 $\widehat F=82^6F$，则
$$
\widehat{E_4T_i}=82^4 E_4\widehat T_i,\qquad
\widehat{E_6}=82^6E_6,\qquad
\widehat{\eta_{\rm Ded}^{12}}=82^6\eta_{\rm Ded}^{12}.
\tag{803.8}
$$
所以无需重算 E1、半线性迹、普通高幂、旧 Fourier 系数，
也无需运行 R777 的全部142阶和 $M_{12}$ 分支。
新的准确694阶短 minor 仍须实际生成；不把旧长有限域 minor 当作本次短 minor。

## 3. 五个新混合三积仅收缩旧56张量

按 R745/R774 的原规范写
$$
h_f=\sum_{a=0}^5v_a\omega_a,\qquad
h_j^{\rm map}=\sum_{a=0}^5w_{j,a}\omega_a,\qquad
w_{j,a}=\rho_j\sigma^j(v_a).
\tag{803.9}
$$
也可由原 R791 整矩阵 $T^je_4$ 与 R759 原十二微分列合成同一个 $w_j$；
若两种接口均使用，须准确核同一列，不再乘一次 $\rho_j$。

原公共整数行及解析标度为
$$
F_a(Q)=QG_a(q_Y),\quad q_Y=Q^3,\quad
\omega_a=\frac{\alpha}{7}F_a(Q)\frac{dQ}{Q},\quad
h_f=2\pi iH_f\,d\tau,
$$
$$
H_f=\frac{\alpha}{1722}\sum_av_aF_a,\qquad \alpha^3=4.
\tag{803.10}
$$
定义
$$
U_0=H_f^3,\qquad U_j=H_j^{\rm map}H_f^2\quad(1\le j\le5).
\tag{803.11}
$$
每个微分有相同的原 $\mu_3$ 字符，三积字符为一；
作为 weight6 形式在上半平面及 cusp 全纯，故都在 (803.5)。
尤其
$$
\boxed{h_j^{\rm map}/h_f=U_j/U_0\in L(Y).}
\tag{803.12}
$$
这里只是同权形式之比，没有给 $U_0$ 任取一个立方根。

R774 的56个原文件
“R774-cubic-monomial-00.json.gz” 至 “-55.json.gz”
保存 $G_aG_bG_c$，$0\le a\le b\le c\le5$。
对 $1\le j\le5$，
$$
U_j=\frac{4q_Y}{1722^3}
 \sum_{a\le b\le c}m_{j;abc}G_aG_bG_c,
\tag{803.13}
$$
其中混合系数准确为
$$
m_{j;aaa}=w_{j,a}v_a^2,
$$
$$
m_{j;aab}=w_{j,b}v_a^2+2w_{j,a}v_av_b,\qquad
m_{j;abb}=w_{j,a}v_b^2+2w_{j,b}v_av_b,
$$
$$
m_{j;abc}
=2(w_{j,a}v_bv_c+w_{j,b}v_av_c+w_{j,c}v_av_b)
\quad(a<b<c).
\tag{803.14}
$$
这些来自三因子的多项式展开，不沿用纯立方的1、3、6重数给混合项。
将 $w_j=v$ 代回才回到纯立方重数。

本次只读取旧张量的指数0至40，输出 (803.13) 的指数1至41，
并给指数0准确零；前面的 $q_Y$ 只移一次。
$U_0$ 直接读 R774 已成原 $H_f^3$ 的两个所需 block 与原有理行尺度，
不重新收缩它的旧56项。
原 $b$、$1,\zeta$ 与 $1,s$ 的坐标换算保持 R774/R797 的原约定：
$$
(a+sb)(R+sS)=(aR-3bS)+s(bR+aS).
\tag{803.15}
$$
本次新增的是五个 $14\times112$ 标量收缩，
不是新的 Hodge、period、Hom、三积或 Laurent 生成。

## 4. 一个有理块，有限右端，完整代回

令 $A_{\rm short}$ 是 (803.8) 原694个整数尺度基的
$1680\times694$ 矩阵。由定理803.1，它的有理秩为694。
选择真实694个独立行，得到同一个准确有理可逆块 $A_I$。

将每个 $U_j$ 的完整原 $L$ 值按14个有理坐标拆开；
六个 $U_j$ 合计至多84条有理右端。每条右端按原数据给自己的有理尺度。
准确解
$$
A_{\rm short}X_j=\operatorname{coeff}(U_j).
\tag{803.16}
$$
若先对整数右端 $N_j$ 求 $A_IX'_j=(N_j)_I$，则输出中必须恢复
相应原有理尺度。对于整数尺度基 $\widehat F_i=82^6F_i$，
$$
U_j=\sum_i(X_j)_i\widehat F_i
    =\sum_i82^6(X_j)_iF_i.
\tag{803.17}
$$
两种坐标不能混用，尽管 (803.12) 的共同标度在比值中最终会抵消。

不需形成完整的特征零逆矩阵。
可复用一个合法辅助素数下的 $A_I$ 解算器，
分组对各真实右端作 Dixon 提升。
每次重构用固定矩形界 $|a|\le A,\ 0<b\le B,\ 2AB<M$，
例如 $A=B=\lfloor\sqrt{(M-1)/2}\rfloor$，随 $M$ 增长；
最后必须代回全部1680个原坐标行。
只有完整准确等式成立，才发布各 $U_j$ 的原694基坐标和比值。

这一步没有原 $L$ 上的新大 kernel：相同有理方块只服务有限右端。
位数、短 minor、耗时及成功状态均由实际 Actions 决定，不在本篇预填。

## 5. 从原 $A/B$ 到五个完整加法函数

给定已认证原 $u=y_f=A/B$，其中 $A,B\in V_5(Y/L)$。
原基定义在 $K$ 上，故 $\sigma$ 对它们只作用于 $L$ 系数。
保持
$$
C_j=\rho_j^{-3}\sigma^j(A),\qquad D_j=\sigma^j(B),\qquad
w_j=C_j/D_j=y_{T^jf}.
\tag{803.18}
$$
这里的 $D_j$ 只是本节分母截面，不是 R791 的 theta 拉回除子。

R791 已证明下列原微分公式及群律，本篇直接复用：
$$
x_f=3(u^2-b)h_f/du,\qquad
x_{T^jf}=3(w_j^2-b)h_j^{\rm map}/dw_j.
$$
因而
$$
\boxed{
r_j^{x}:=\frac{x_{T^jf}}{x_f}
=\frac{U_j}{U_0}\frac{w_j^2-b}{u^2-b}\frac{du}{dw_j}\in L(Y).}
\tag{803.19}
$$
不同于 (803.4) 的有理数 $r_j$，上标 $x$ 标记这里的函数比值。
两分子 $x$ 有相同的 deck 字符，所以其比确在 $Y$；
这不是将 $x_f$ 本身误认为 $Y$ 上的函数。

不要求一个全局参数才能实现微分比。
取原 $\mathscr D=(2\pi i)^{-1}d/d\tau=(q_Y/82)d/dq_Y$，并定义
$$
W_0=B\mathscr DA-A\mathscr DB,\qquad
W_j=D_j\mathscr DC_j-C_j\mathscr DD_j,
$$
$$
F_0=A^2-bB^2,\qquad F_j=C_j^2-bD_j^2.
\tag{803.20}
$$
则
$$
\boxed{r_j^x=\frac{U_jF_jW_0}{U_0F_0W_j}.}
\tag{803.21}
$$
$\mathscr D$ 对单个模形式的非模项在同权 Wronskian 中消掉。
几何上 $W_0,W_j$ 是 $H^0(10\mathcal L+K_Y)
=H^0(11\mathcal L-\mathcal D)$ 的截面；
因此 (803.21) 是全局同线丛截面之比。
若实现同时改用 $q_Yd/dq_Y$，两个 $W$ 同乘82而相消；
不得只在一侧删掉这个因子。

对 $1\le j\le5$，$r_j^x-1$ 不是零函数。
否则 $x_{T^jf}=x_f$，曲线方程在函数域中推出
$y_{T^jf}=\pm y_f$，故 $T^jf=\pm f$。
但 $f$ 在 $\mathbb Q[T]\simeq\mathbb Q(\zeta_{21})$ 上生成秩一模，
而此范围的 $T^j\ne\pm1$，矛盾。
同理 $u^2-b,W_j,U_0$ 均非零。

于是原完整割线公式给
$$
\boxed{
y_{g_j}
=-u+\frac{(w_j-u)(2+r_j^x)}{r_j^x-1}
-\frac{(w_j-u)^3}{(r_j^x-1)^3(u^2-b)}.}
\tag{803.22}
$$
它首先在稠密开集成立，故是整个 $L(Y)$ 中的准确恒等式。
孤立点的分母为零必须按函数域等价式或局部环正规化；
未约分分母的零除子不是 $(y_{g_j})_\infty$。

(803.18)–(803.22) 可以保存为源绑定的有限有理运算和微分表达式，
不强制展开为巨大单一分式。只要原 $A/B$ 与 (803.16) 已实际认证，
它们已指定五个真实函数，不需要另解五套新的 Laurent kernel。
但函数表达式完成不等于其极除子已经计算。

## 6. 三同源比较、原范数常数及所选基的全部运输

记 $P_g=(y_g)_\infty$、$P_f=(u)_\infty$，并置
$$
\lambda_j=2+r_j=\deg(g_j)/1206=p_j/q_j,\qquad
(p_j,q_j)=
(165,67),(93,67),(100,67),(168,67),(371,134).
\tag{803.23}
$$
这里的 $p_j,q_j$ 是既约整数对。
原 $\alpha_3=1-\zeta^2$ 的同源保持 R791 的全部常数：
$$
y_{[\alpha_3]g}
=\frac{y_g(y_g^2-9b)}{3s(y_g^2-b)},\qquad
P_{[\alpha_3]g}=3P_g+\operatorname{div}(y_g^2-b).
\tag{803.24}
$$

令
$$
\mathcal N_g=N_{L/K}(y_g^2-b),\qquad
\mathcal R_j=\mathcal N_{g_j}^{\,q_j}/\mathcal N_f^{\,p_j}.
\tag{803.25}
$$
每个 norm 使用真正的 $\sigma^k(y_g^2-b)$，包括 $\sigma^k(b)$。
记
$$
Z_j=q_j\sum_\sigma P_{\sigma g_j}
       -p_j\sum_\sigma P_{\sigma f},
$$
$$
Z_j^R=q_j\sum_\sigma P_{[\alpha_3]\sigma g_j}
       -p_j\sum_\sigma P_{[\alpha_3]\sigma f}.
$$
原除子与原主函数有准确等式
$$
\boxed{Z_j^R-3Z_j=\operatorname{div}\mathcal R_j,\qquad
\eta_{h_j}=[Z_j/q_j]=[Z_j^R/(3q_j)].}
\tag{803.26}
$$
这就是 R791 的三次同源修正，不只保留其 Jacobian 类。

**必须区分 norm 与同靶运输后的乘积。**
若为了复用同靶函数而取
$$
\widehat{\mathcal N}_g=
\prod_{k=0}^6\bigl(y_{T^kg}^2-b\bigr),
$$
则 (803.1) 准确给
$$
\rho_k^6=\sigma^k(b)/b,\qquad
\boxed{\widehat{\mathcal N}_g
=\frac{b^7}{N_{L/K}(b)}\,\mathcal N_g.}
\tag{803.27}
$$
因此若 $\widehat{\mathcal R}_j
=\widehat{\mathcal N}_{g_j}^{q_j}/\widehat{\mathcal N}_f^{p_j}$，
必须恢复
$$
\boxed{\mathcal R_j
=\left(\frac{b^7}{N_{L/K}(b)}\right)^{p_j-q_j}
 \widehat{\mathcal R}_j.}
\tag{803.28}
$$
这个非零域常数不改变主除子，却属于原截面、Poincaré 对数和高度的规范，
不能删成1。

这些原 norm 也有准确有理下降。
由 R791，$c(f)=-[\zeta^2]f$、$cTc=T^{-1}$，所以
$c(g_j)=-[\zeta^2]T^{-j}g_j$。
$y$ 平方消去 $-[\zeta^2]$ 的符号，
而 $N_{L/K}(\rho_j)^6=1$，因为 $N_{L/K}(\rho)=\zeta^2$。
于是 $c(\mathcal N_{g_j})=\mathcal N_{g_j}$，
同样 $c(\mathcal N_f)=\mathcal N_f$，故 (803.25) 在 $\mathbb Q(Y)^\times$。
不能用省掉 (803.27) 标量后的同靶乘积冒充这条下降。

最后保持 R794 的实际列矩阵 $C=(c_{ji})$。
原线性规则为
$$
\eta_{{\rm selected},i}=\sum_{j=1}^5c_{ji}\eta_{h_j}.
\tag{803.29}
$$
取正整数 $n_i$ 使全部 $n_ic_{ji}/q_j$ 为整数，则实际比较函数为
$$
\mathcal P_i=\prod_{j=1}^5
 \mathcal R_j^{\,n_ic_{ji}/q_j},
$$
$$
n_i\sum_j\frac{c_{ji}}{q_j}Z_j^R
-3n_i\sum_j\frac{c_{ji}}{q_j}Z_j
=\operatorname{div}\mathcal P_i.
\tag{803.30}
$$
因此基变换的有理分母、三同源、范数和函数常数均显式保留。

如同 R794，(803.26)–(803.30) 只给这些具体拉回代表之间的准确比较。
原选定对称线丛若还相差 Picard 二挠，仍须在足倍数上明确比较截面；
其 $c_0$ 刚性化及函数首项不能因 $J\otimes\mathbb Q$ 类相同而略去。
本篇没有把尚未计算的二挠比较函数或局部刚性化常数设为1。

## 6.1. 只改正负号即可把所有所需普通幂降到八

令 $g_j^\pm=f\pm T^jf$。原次数的平行四边形恒等式给
$$
\deg g_j^-+\deg g_j^+=4\deg f=4824.
\tag{803.32}
$$
而原范数恒等式
$$
(1\pm T^j)^*(1\pm T^j)=2\pm S_j
$$
说明按原次数去迹后，
$$
h_j^+=h_j,\qquad h_j^-=-h_j.
\tag{803.33}
$$
因此可选固定符号
$$
(\varepsilon_1,\ldots,\varepsilon_5)=(-1,1,1,-1,-1),
\qquad \widetilde g_j=f+\varepsilon_jT^jf.
\tag{803.34}
$$
五方向仍准确独立，不涉及整数格除法或新的最短向量搜索。
新 NS 列基为 $H_\varepsilon=H_{\rm R791}\operatorname{diag}(\varepsilon)$，
所以 R794 的同一所选基准确满足
$$
H_{\rm selected}=H_\varepsilon\operatorname{diag}(\varepsilon)C.
\tag{803.35}
$$
原函数只需在 (803.22) 中把 $w_j$ 换成 $\varepsilon_jw_j$；
$x$ 比 $r_j^x$ 不变，五个混合比值也不新增。

**正负号变换必须运输主函数。** 原椭圆曲线乘积上的准确恒等式为
$$
\operatorname{div}(x_1-x_2)
=\Delta+\Gamma_{[-1]}-2(\{O\}\times C)-2(C\times\{O\}).
$$
沿 $(f,T^jf)$ 拉回，立方后降到 $Y$，得到
$$
A_j^x:=(x_f-x_{T^jf})^3
=(u^2-b)(1-r_j^x)^3\in L(Y)^\times,
$$
$$
\operatorname{div}A_j^x
=P_{g_j^+}+P_{g_j^-}-2P_f-2P_{T^jf}.
\tag{803.36}
$$
这在两点都为 $O$、二挠点或 $\phi$ 分歧处也包含准确重数，
因为它是 Cartier 除子的拉回等式，不是有限仿射图上的集合比较。
取真正 norm
$$
\Lambda_j=N_{L/K}(A_j^x)
$$
后，$P_{T^jf}$ 的七个共轭恰为 $P_f$ 的七个共轭，
所以
$$
\operatorname{div}\Lambda_j
=C_j^++C_j^--4C_f,\quad
C_j^\pm=\sum_\sigma P_{\sigma g_j^\pm},\quad
C_f=\sum_\sigma P_{\sigma f}.
\tag{803.37}
$$
不能把 $(1-r_j^x)^3$ 改成 $(r_j^x-1)^3$ 而漏掉原七次 norm 的负号。

写 $\lambda_j^+=p_j/q_j$ 如(803.23)，则
$\lambda_j^-=(4q_j-p_j)/q_j$ 也为既约分数。
令 $Z_j^\pm=q_jC_j^\pm-p_j^\pm C_f$，$p_j^+=p_j$、
$p_j^-=4q_j-p_j$。于是
$$
Z_j^++Z_j^-=q_j\operatorname{div}\Lambda_j.
\tag{803.38}
$$

还可直接接 R791 原真实实下降代表，避免先求较大正号极除子。
用(791R.6)的完整 $x$ 公式，记
$$
k(z)=-\frac{\zeta(z^2+3b)}{3(z^2-b)},\qquad
x_{f_R}=k(u)x_f,\quad x_{T^jf_R}=k(w_j)x_{T^jf}.
$$
定义实际函数
$$
\Lambda_j^R
=N_{L/K}\!\left((u^2-b)
       (k(u)-r_j^x k(w_j))^3\right).
\tag{803.39}
$$
它是原 $(x_{f_R}-x_{T^jf_R})^3$ 的真 norm；
$k$ 的 $-\zeta/3$，立方后的 $-1/27$，均按原式保留。

对正、负号各定义原三同源函数
$$
\mathcal R_j^\pm
=\frac{N_{L/K}(y_{g_j^\pm}^2-b)^{q_j}}
       {N_{L/K}(u^2-b)^{p_j^\pm}},
\qquad
Z_j^{R,\pm}-3Z_j^\pm=\operatorname{div}\mathcal R_j^\pm.
$$
对原实下降 $f_R$ 应用同一个平行四边形除子等式，得到
$$
Z_j^{R,+}+Z_j^{R,-}=q_j\operatorname{div}\Lambda_j^R.
$$
因此选择负号时，直接运输原 R791 正号代表的函数是
$$
\boxed{
Z_j^{R,+}+3Z_j^-=
\operatorname{div}\!\left(
\frac{(\Lambda_j^R)^{q_j}}{\mathcal R_j^-}\right).}
\tag{803.40}
$$
这只需较小的负号极除子、原 $f$，以及显式函数；
不需要先计算较大的 $P_{g_j^+}$。

该比较也保留复共轭常数。
由 $c(f)=-[\zeta^2]f$、$c(f_R)=f_R$ 和 $cTc=T^{-1}$，
准确有
$$
c(\Lambda_j)=-\Lambda_j,\qquad c(\Lambda_j^R)=-\Lambda_j^R.
\tag{803.41}
$$
负号来自交换两点的差及七次 norm，而 $N(\rho_{-j})^6=1$。
若需要在 $\mathbb Q(Y)$ 中给比较函数，
可使用 $\Lambda_j/s$、$\Lambda_j^R/s$，
但须同时保留这个明确的 $s$ 因子；
它不是可以无记录约去的高度常数。

统一置
$$
\Theta_j=
\begin{cases}
\mathcal R_j^+,&\varepsilon_j=1,\\
(\Lambda_j^R)^{q_j}/\mathcal R_j^-,&\varepsilon_j=-1.
\end{cases}
$$
则固定原 R791 代表与新符号代表之间的准确式为
$$
Z_j^{R,+}-3\varepsilon_jZ_j^{\varepsilon_j}
=\operatorname{div}\Theta_j.
\tag{803.42}
$$
将(803.30)中的 $Z_j$ 换成
$\varepsilon_jZ_j^{\varepsilon_j}$、$\mathcal R_j$ 换成 $\Theta_j$，
就连同同一个 $C$ 和原清分母整数完成所有所选方向的主函数运输。
原对称线丛的二挠比较与 $c_0$ 刚性化边界仍按§6保留。

## 7. 成本真正减少在哪里，极除子又需要什么

在已有原 $A/B$ 后，新增的核心输入只为：

1. 四个原 $M_6$ 补方向的0–41准确系数，普通690行全部读取旧 R786；
2. 五个混合三积的新14坐标标量收缩，旧56张量与旧 $H_f^3$ 直接读取；
3. 一份694阶有理块的有限右端坐标求解、完整代回；
4. 五个源绑定的 (803.18)–(803.22) 运算表达式，以及§6/6.1保全部常数的符号选择与主函数表达式。

不需新 V7/V8 长尾才定义这五个函数，不需五个新的 $L$-Schur 系统，
也不需构造 $Y$ 的一个高次数平面模型。
这不修改已成的 R797/R799/R800 结果，它们仍是另一条较低次数除子路线的有效输入。

只保原正号时，次数2970/1674/1800/3024/3339会使通用 R793 界达到
普通幂12/8/8/13/14、完整条件312/193/199/329/358。
§6.1 的确定符号选择消除了这一明显代价，准确参数改为：

| $j$ | $\varepsilon_j$ | 已证 $\deg\widetilde g_j$ | 普通幂 $m$ | 残余次数 $e$ | 完整条件数 $N$ |
|---:|---:|---:|---:|---:|---:|
| 1 | $-1$ | 1854 | 8 | 322 | 202 |
| 2 | $1$ | 1674 | 8 | 502 | 193 |
| 3 | $1$ | 1800 | 8 | 376 | 199 |
| 4 | $-1$ | 1800 | 8 | 376 | 199 |
| 5 | $-1$ | 1485 | 7 | 419 | 170 |

这些度由已完成 R791 的度及平行四边形恒等式严格推出，
没有宣称对新列运行了另一次 Hom/Gram 计算或完成任何新秩。
最大普通幂与 R794 的低次数选择同为八；最大条件数202只比196多六项。
若未来采用这条通用界，最高分母指数为201，现有至195的基尾不能冒称已经覆盖。
只在确实选择该消费者时才补缺口，不为纸面比较预先生成它们。

尽管如此，不能把极除子步骤当作免费工作。
本篇的函数表达式由群律直接给出；若后继又对这些同一函数求一次完整
Laurent kernel，仍会引入本来希望避免的大系统。
比较两条路线应分别记录“函数构造”和“完整极除子/Jacobian”成本。

即使保存有理运算表达式而不展开，约分问题仍然真实存在。
例如 (803.21) 两侧未约分的截面都在
$$
H^0(24\mathcal L+2E-\mathcal D),\qquad
\deg(24\mathcal L+2E-\mathcal D)=6512.
\tag{803.31}
$$
而 $r_j^x=x_{T^jf}/x_f$ 的实际极次数至多1608：
$X$ 上两条 $x$ 函数的次数各为 $2\cdot1206$，
商的极次数至多4824，再按 $\deg\phi=3$ 降至 $Y$。
这已经显示许多真实消去，不能从 (803.31) 的分母直接计极点。
加法式 (803.22) 还会有进一步消去。

可复用 R798 的固定 $V_3,V_6$ 乘法和 R793 的 span/colon/flip，
但还须实际实现：在既有除子表示中对上述源绑定表达式求正确的商、公共零和极除子，
并保主函数乘积。当前没有该实现的耗时或完成数据。
如果该除子接口最终成本更高，仍可选择 R794/R801 的低次数路线；
本篇不据一个较小的有理方块预称全部 $\eta$ 计算更快。

## 8. 接续与认证边界

低权混合比值任务可独立于原 $A/B$ 的返回准备；
只有实际成功后才能标记 $U_j$ 坐标已知。
函数合成另外消费原 $A/B$ 的成功 producer 与原坐标规范，
不能把一个仍运行的请求当作输入。

每一层均保独立完成字段：短 $M_6$、混合三积、原基坐标、
原函数表达式、完整极除子、原 $\eta$、刚性化和高度。
前一层的成功不自动令后者为真。
新算术仅在本公开仓库 Actions 执行；
脚本、参数、run 与输出 SHA 入 Git，
准确矩阵、坐标和可重算证书仅在当前一日活跃 bundle 传递。

本篇没有计算实际 $\eta_h$、高度首项或全 $p$ 排除，
没有重开已经完成的原 $p=41$ 有理点分类。

## 来源

- 本仓库 R767（2026），式(767.8)、§§4–5：原粗曲线线丛与两椭圆主部。
- 本仓库 R772/R778（2026）：原 $K$ 定义基、20 cusp 算术轨道及42项 $M_6$ 注入。
- 本仓库 R774/R786/R775 实际结果（2026）：同一原56张量、普通690基、694条原配方及尺度。
- 本仓库 R791 实际结果（2026），§§2–5：真实 $T,\rho$、五个原方向、群律和三同源主函数。
- 本仓库 R794 实际结果（2026）：保原 $\kappa,e_R$ 的准确五维列基变换。
- 本仓库 R793/R798/R801（2026）：原极除子表示、固定乘法接口和较低次数长尾路线。

