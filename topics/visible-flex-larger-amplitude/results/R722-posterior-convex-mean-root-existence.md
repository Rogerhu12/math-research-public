# R722 — 候选残差驱动的凸均值根存在：替代粗端层余量的后验充分条件

2026-11-27（UTC）。**已证明：对 R709 的同一完整三均值方程，一个准确归一化的正半球候选及其完整准确残差，可以先定位闭单位球上的全部凸极小点，再证明其严格正乘子，从而得到唯一的准确均值根、正垂直界、严格小于一的半径界和完整 Jacobian 逆界。** 本条不要求 $b<k_-$、$b<k_z$ 或 $k_++2b<L$，也不要求收缩。

新内容是**从候选和误差直接证明根存在**，而不是在已存在的根附近补一个误差估计。R709 §6 和 R710 原本已经有存在后的候选误差传播；它们不能倒过来单独承担本条的存在证明。本结果不改变原 working mean、profile、32-stage normal 或优化算法，不增加独立执行门。

**当前第 17 次 wide-seed 运行尚未支付本条所需的完整准确残差与全角条件。** 以下没有把实际初值、trial、打印残差、可变进度、候选 $\widehat D$ 或未返回快照提升为准确根或几何证书。

## 1. 同一准确方程与适用范围

固定一个角 $\phi$。沿用 [R708](R708-supported-unit-meridian-seed-contraction.md)、[R709](R709-global-convex-mean-closure-without-contraction.md) 的完整数据：

- $U$ 是严格内部支持，长度为 $L$；$E\subset U$ 是全部端层，完整物理测度为 $b$。
- $L_c=L-b>0$ 是全部中央段总长度，每一个中央段自身也有严格正长度。
- 在全部 $E$ 上，准确参考满足 $|T_0(s,\phi)|=1$、$T_{0,z}(s,\phi)\ge0$；$0\le\chi(s)\le1$。这些是整个端层的事实，不能以有限节点检查代替。
- 帽端、core、完整补集与准确 scalar 都属于同一个固定参考。完整目标是
  $$
  K(\phi)=P(\phi)-\Gamma(\phi)
       -\int_{[0,S]\setminus U}T_0(s,\phi)\,ds.
  \tag{1}
  $$
  其中任何准确无限尾、分片或端口贡献都没有被删去。

对满足分母非零的方向或向量 $y$，记
$$
Y(s,y)=(1-\chi)T_0+\chi y,\qquad
B(y)=\int_E\frac{Y(s,y)}{|Y(s,y)|}\,ds.
\tag{2}
$$
真正需要的方程始终是
$$
F(v)=L_cv+B(Nv)-K=0,\qquad
N(v)=v/|v|,\qquad v\ne0.
\tag{3}
$$

以下存在性证明只要求 $T_0,\chi$ 可测并满足上述准确几何条件。讨论经典角导数时，再使用第7节明确的角向正则性和积分内微分条件。端层与中央长度对角固定；若它们依赖另一外参数，仍要付 [R721](R721-supported-seed-width-and-profile-sensitivity.md) 已列的移动边界和乘积项。

本条中的 $b$ 也可替换为已付的完整端层测度上界 $\bar b\ge |E|$。为简洁，第2—7节写真实 $b$；第8节给所有长度和候选都只有向外区间时的有理判据。$b,L_c,K$ 和 $\alpha$ 有长度单位，$v,d,r,\eta,\zeta$ 无量纲。

## 2. 闭球势在零分母处也有定义

固定 $\phi$，对所有 $y\in\mathbb R^3$ 定义 R709 的势
$$
\psi_s(y)=
\begin{cases}
\displaystyle
\frac{|(1-\chi)T_0+\chi y|-(1-\chi)}{\chi},
   &\chi>0,\\[5pt]
T_0\cdot y,&\chi=0,
\end{cases}
\qquad
\Psi(y)=\int_E\psi_s(y)\,ds.
\tag{4}
$$

这里不先要求 $Y\ne0$。即使某个 $Y$ 为零，范数本身仍连续且凸，所以 $\psi_s$ 仍是合法的凸连续函数；只是在该处不能擅自使用梯度公式。

对 $\chi>0$，范数的反三角不等式给
$$
|\psi_s(y)-\psi_s(z)|\le |y-z|,\qquad \psi_s(0)=0.
\tag{5}
$$
$\chi=0$ 的线性分支也满足同一式。故 $|\psi_s(y)|\le|y|$，$\Psi$ 在整个 $\mathbb R^3$ 上有限、凸、连续，并为 $b$-Lipschitz。

$\chi\downarrow0$ 的延拓是准确的。对靠近零的正 $\chi$ 作范数平方差有理化，得到
$$
\psi_s(y)=
\frac{2(1-\chi)T_0\cdot y+\chi|y|^2}
 {|(1-\chi)T_0+\chi y|+(1-\chi)}
 \longrightarrow T_0\cdot y.
\tag{6}
$$
该极限在有界 $y$、所有单位 $T_0$ 上一致；这里只在分母接近 $2$ 的 $\chi\downarrow0$ 区域使用有理化式，不把它偷用在 $\chi=1,y=0$。

因此
$$
f(y)=\Psi(y)-K\cdot y
\tag{7}
$$
在闭单位球 $\overline{\mathbb B}=\{|y|\le1\}$ 上必有极小点。这一步不使用 $|K|>b$ 或 $K_z>b$，也没有预先假定整个球上都能归一化 $Y$。

### 2.1 正半球帽上的完整梯度

若 $|y|\le1$ 且 $y_z\ge\zeta>0$，则对 $\chi>0$
$$
|Y(s,y)|\ge Y_z\ge\chi\zeta,
\tag{8}
$$
而由三角不等式还有 $|Y|\ge1-2\chi$。二者共同给
$$
|Y|\ge\max(1-2\chi,\chi\zeta)
      \ge\frac{\zeta}{2+\zeta}>0.
\tag{9}
$$
$\chi=0$ 时 $Y=T_0$，范数正好为一。因此在该帽及其小邻域中可真实地作积分内方向微分，
$$
\nabla\Psi(y)=B(y),\qquad
M(y):=DB(y)
=\int_E\frac{\chi}{|Y|}
 \left(I-\frac{YY^T}{|Y|^2}\right)\,ds.
\tag{10}
$$
$\chi=0$ 的 Hessian 为零。完整 $3\times3$ 矩阵 $M$ 对称半正定，而且由 (8)
$$
0\preceq M(y),\qquad \|M(y)\|_{\rm op}\le\frac b\zeta.
\tag{11}
$$
正半球的任意有界小邻域都有非零分母；(8) 又直接控制二阶积分的被积函数。这说明 (10) 没有把球上其它可能不可微的点混入推导。

连接该帽中任意两点的直线段仍在帽中。故在整条线段上
$$
|B(y)-B(z)|\le\frac b\zeta|y-z|.
\tag{12}
$$
这不是只在单位球面切向方向上的界，而是完整三维方向变化的界。

## 3. 后验存在与唯一性定理

**定理 1。** 在第1节的准确数据条件下，给一个准确非零候选 $\widehat v$。定义
$$
\widehat r=|\widehat v|,\qquad
\widehat d=\widehat v/\widehat r,\qquad
\widehat\alpha=L_c\widehat r>0.
\tag{13}
$$
要求 $\widehat d_z>0$，并有针对完整准确方程的向外上界
$$
|F(\widehat v)|\le\varepsilon,\qquad \varepsilon\ge0.
\tag{14}
$$
这里 $|\widehat d|=1$ 是准确定义，不是某组近似单位工作字的标签。

令
$$
\eta=\frac{2\varepsilon}{\widehat\alpha},\qquad
\zeta=\widehat d_z-\eta,
\tag{15}
$$
$$
\Delta=\varepsilon+\frac b\zeta\,\eta,\qquad
\alpha_-=\widehat\alpha-\Delta,\qquad
\alpha_+=\widehat\alpha+\Delta.
\tag{16}
$$
若准确地有
$$
\boxed{\qquad
\zeta>0,\qquad \alpha_->0,\qquad \alpha_+<L_c,
\qquad}
\tag{17}
$$
则 (3) 有唯一合法的非零均值根 $v_*=r_*d_*$，且
$$
|d_*|=1,\qquad d_{*,z}\ge\zeta,\qquad
|d_*-\widehat d|\le\eta,
\tag{18}
$$
$$
\boxed{\qquad
0<r_-:=\frac{\alpha_-}{L_c}
 \le r_*\le
r_+:=\frac{\alpha_+}{L_c}<1.
\qquad}
\tag{19}
$$
全部准确端层归一化分母非零。结论包括 $\varepsilon=0$，此时 $\eta=\Delta=0$，候选本身就是准确根。

所谓合法根，指原方程中的完整端层归一化和积分确有定义的 $v\ne0$；不把在 $Y=0$ 处任意挑一个凸次梯度称为原物理方程的另一个根。

### 3.1 候选支撑不等式先定位全部极小点

因 $\widehat d_z>0$，第2节保证 $\Psi$ 在 $\widehat d$ 可微。置
$$
\widehat K=B(\widehat d)+\widehat\alpha\widehat d,\qquad
e=K-\widehat K.
$$
(14) 给 $|e|\le\varepsilon$。对任意 $y\in\overline{\mathbb B}$，凸支撑不等式给
$$
\begin{aligned}
f(y)-f(\widehat d)
&\ge (B(\widehat d)-K)\cdot(y-\widehat d)\\
&=\widehat\alpha(1-\widehat d\cdot y)
   -e\cdot(y-\widehat d)\\
&\ge
\frac{\widehat\alpha}{2}|y-\widehat d|^2
-\varepsilon|y-\widehat d|.
\end{aligned}
\tag{20}
$$
最后一步使用的准确几何恒等式是
$$
1-\widehat d\cdot y
=\frac{|y-\widehat d|^2+1-|y|^2}{2}
\ge\frac{|y-\widehat d|^2}{2}.
\tag{21}
$$

现在取闭球上的任意全局极小点 $y_*$。其函数值不大于 $f(\widehat d)$，故 (20) 强迫
$$
|y_*-\widehat d|\le2\varepsilon/\widehat\alpha=\eta.
\tag{22}
$$
这对**全部**极小点同时成立。因此它们全都满足 $y_{*,z}\ge\zeta>0$，落入第2节的光滑帽。这里是先用全局凸连续势定位，再取得可微性；不存在先假设未知极小点的分母正而倒用该结论的循环。

### 3.2 严格正乘子排除内点

连接 $\widehat d$ 和 $y_*$ 的完整线段都在 $y_z\ge\zeta$ 的闭球帽中。由 (12)(22)
$$
|B(y_*)-B(\widehat d)|\le (b/\zeta)\eta.
$$
于是
$$
\left|K-B(y_*)-\widehat\alpha\widehat d\right|
\le\varepsilon+(b/\zeta)\eta=\Delta.
\tag{23}
$$
特别，
$$
0<\alpha_-\le|K-B(y_*)|\le\alpha_+.
\tag{24}
$$

若 $y_*$ 在开单位球内，光滑目标的必要条件是 $B(y_*)-K=0$，与 (24) 矛盾。所以 $|y_*|=1$。球面处的凸一阶条件给
$$
K=B(y_*)+\alpha_*y_*,\qquad \alpha_*\ge0.
\tag{25}
$$
其外法向乘子正好为 $|K-B(y_*)|$。由 (24)
$$
\alpha_-\le\alpha_*\le\alpha_+<L_c.
\tag{26}
$$
令 $d_*=y_*$、$r_*=\alpha_*/L_c$、$v_*=r_*d_*$，便得到原完整方程 (3) 以及 (18)(19)。

### 3.3 正乘子本身给唯一性，不要求全势严格凸

在上述极小点处，凸支撑式对任何 $z\in\overline{\mathbb B}$ 给
$$
\begin{aligned}
f(z)-f(d_*)
&\ge (B(d_*)-K)\cdot(z-d_*)\\
&=\alpha_*(1-d_*\cdot z)
\ge\frac{\alpha_*}{2}|z-d_*|^2.
\end{aligned}
\tag{27}
$$
因 $\alpha_*>0$，闭球极小点唯一。这个二次增长来自正球面乘子与球的几何，**不是**未经证明的 $\Psi$ 全局严格凸性。

任何原方程的合法根 $v=rd$ 都有 $r>0$，并满足
$K=B(d)+L_crd$。在该点，逐个准确范数的凸支撑式积分给
$B(d)\in\partial\Psi(d)$；当存在一致正分母时这就是普通梯度。故它同样满足闭球的凸极小值条件，其方向只能是 $d_*$；原方程再给 $r=r_*$。这个论证不先要求假设中的其它根也在北半球，也不将潜在的非光滑次梯度解冒成物理根。证毕。

## 4. 存在之后可收紧误差，不反向使用未证根

定理1成立后，使用 R709 的同一凸单调性，对根和候选的方程相减并点乘 $d_*-\widehat d$，得到
$$
\frac{\alpha_*+\widehat\alpha}{2}
 |d_*-\widehat d|^2
\le \varepsilon |d_*-\widehat d|.
$$
因此可取
$$
\eta_1=
\frac{2\varepsilon}{\widehat\alpha+\alpha_-}
\le\eta,\qquad
|d_*-\widehat d|\le\eta_1.
\tag{28}
$$
相同帽上的完整 Lipschitz 界继续给
$$
|B(d_*)-B(\widehat d)|\le (b/\zeta)\eta_1.
\tag{29}
$$
直接从两条完整向量方程比较，而非先分开径向与方向再相加，有
$$
\boxed{\quad
|v_*-\widehat v|
\le\frac{\varepsilon+(b/\zeta)\eta_1}{L_c}.
\quad}
\tag{30}
$$
半径的范数反三角不等式随即给
$$
|r_*-\widehat r|
\le\frac{\varepsilon+(b/\zeta)\eta_1}{L_c}.
\tag{31}
$$
(30) 是可选的较紧零阶向量界。已有 R709/R710 更保守的误差上界依旧成立，不必删去或改写原实现。关键顺序是先由第3节独立完成存在，再用 (28)；不能先拿 (28) 中未知的 $\alpha_-$ 当已存在根的证据。

## 5. 完整 mean Jacobian 的逆界

在准确根处写 $P_d=I-dd^T$、$r=r_*$、$M=DB(d_*)$。R709 的完整 Jacobian 原式不变：
$$
J=F_v=L_cI+\frac{MP_d}{r}.
\tag{32}
$$
第2节给 $M\succeq0$ 和 $\|M\|\le M_0:=b/\zeta$。在
$\mathbb R^3=\operatorname{span}\{d\}\oplus d^\perp$ 中，
$$
J=
\begin{pmatrix}
L_c&d^TM|_{d^\perp}/r\\
0&L_cI_{d^\perp}+P_dM|_{d^\perp}/r
\end{pmatrix}.
\tag{33}
$$
正切块对称且不小于 $L_cI$，所以整矩阵可逆。保留径向—正切非对角项后，
$$
\boxed{\qquad
\|J^{-1}\|\le
\frac1{L_c}\left(1+\frac{M_0}{L_cr_-}\right).
\qquad}
\tag{34}
$$
这是原完整非对称矩阵的普通 Euclidean 算子范数界。不能把正切块的下界写成整个 $J$ 的最小奇异值至少 $L_c$，也没有只求其某个子块。

上述逆界不要求任何形如 $q<1$ 的限制。若有独立更紧的完整 $M$ 上界，可以用它改善 (34)；本定理不要求先新算 $B_d,B_{dd}$ 才能证明零阶存在。

## 6. 与准确角 jet、投影架、R711 profile 的衔接

定理1已给准确 $0<r_-\le r\le r_+<1$、$d_z\ge\zeta>0$。为复用 R710 的高阶界，可以直接使用其 §2 已证的完整帽分母
$$
\nu_*=
\sqrt{\frac{1-\sqrt{1-\zeta^2}}2}>0.
\tag{35}
$$
它对连接候选方向与真实方向的整条非单位线段也成立，不只对两端单位方向成立。新证明中较简单的 (9) 已足够取得可微性；(35) 只用于后续更紧的原导数费用。

在原数据的完整角导数实际存在时，仍使用同一 $J$：
$$
Jv_\phi=K_\phi-B_\phi,\qquad d_\phi=P_dv_\phi/r.
\tag{36}
$$
令
$$
N_2(v;w)=
-\frac{2(d\cdot w)P_dw+d|P_dw|^2}{r^2}.
$$
则完整二角式仍是
$$
\begin{aligned}
Jv_{\phi\phi}={}&K_{\phi\phi}-B_{\phi\phi}
 -2B_{d\phi}d_\phi-B_{dd}[d_\phi,d_\phi]
 -M N_2(v;v_\phi),\\
d_{\phi\phi}={}&P_dv_{\phi\phi}/r+N_2(v;v_\phi).
\end{aligned}
\tag{37}
$$
这里 $B_\phi,B_{\phi\phi},B_{d\phi},B_{dd}$ 为固定方向的偏导，所有三分量及交叉项都保留。新零阶存在证书没有凭空支付 (36)(37) 的实际残差或导数费用；它只是提供这些已有公式所需的真实根域和逆界。

对于同一准确水平单位径向向量 $e$，
$$
w=\frac{e-(e\cdot d)d}{|e-(e\cdot d)d|}
$$
的分母至少为 $\zeta$。所以不需要额外要求 $d$ 的水平分量非零。R711 的十二片平滑三角 profile 对所有 $0<r<1$、$0<\delta<1/8$ 已给唯一 $0<\lambda<\pi$；本条得到的紧根区间可直接进入其已有幅度与两角 jet 结论。这里没有重新证明 R711，也没有把其 profile 方程的根存在替代三均值根存在。

R710 的完整零、一、二总残差、准确参考角界、profile 矩、节点四 jet 及工作字差仍需逐项付清。定理1不声称 normal 六控制 Jacobian 满秩，不声称全部32段已选根同支，也不声称 physical sixjet、Gram、曲率或 reach 已认证。

## 7. 全角统一、重叠拼接与正则性

令 $\mathcal C_1,\ldots,\mathcal C_n$ 是整个角圈的有限闭区间覆盖，所有周期接缝均属于覆盖。对每个 $\mathcal C_i$，允许选择不同的实际候选中心，甚至不要求这些中心自身在交界连续；但该胞上的残差与 (17) 必须是针对**所有** $\phi\in\mathcal C_i$ 的准确向外界。

若每胞都满足定理1，则每个真实角存在唯一准确根。交叠处两份证明针对同一个准确 $K,T_0,\chi,L_c$，所以唯一性迫使所证根相同。有限个严格正余量给全角共同的正 $r_-$、正 $\zeta$ 和严格小于一的 $r_+$，没有在角胞之间另选符号或另选极小点。

进一步假设：

1. 准确 $K$ 是角变量的 $C^2$ 函数；
2. $T_0$ 的所需角导数存在，且在完整 $E$ 上有可积分的一致支配界；
3. 区间与 $\chi,L_c$ 对角固定，所有 piece 的原匹配关系真实成立。

正分母、完整 $J$ 可逆和隐函数定理给局部 $C^2$ 根；上述唯一性把它们拼成同一全角 $C^2$ 分支。若只支付了较低正则性，就只声明相应较低正则性，不从有限工作 jets 虚构高阶光滑。

数据的真实 $2\pi$ 周期使根有同一周期。某个正交对称只有在完整数据真的满足相应变换、且两侧都属于已证域时才由唯一性继承。有限节点、half-turn 标签或仅覆盖 $[0,\pi/2]$ 不自动给全圆，反射与端口亦不能靠 metadata 布尔值补齐。

单一 literal 角的 (14)(17) 只能证明该角。全部实际 batch 的 literal 角都通过，也不等于整个连续角圈通过。

## 8. 只有向外有理输入时的完整可执行判据

本节只是准确不等式接口，不提供一个以零误差填充的运行 fixture。假设同一个角或整个闭角胞已给出
$$
0<L_-\le L_c\le L_+,\qquad |E|\le b_+,
$$
$$
0<\widehat r_-\le|\widehat v|\le\widehat r_+,\qquad
\frac{\widehat v_z}{|\widehat v|}\ge z_0>0,\qquad
|F(\widehat v)|\le E_0.
\tag{38}
$$
所有端点都是准确有理数或经证明包含它们的向外有理界。候选可取实际保存的 binary64 向量按准确二进有理数解释；其欧氏范数和准确归一化需另作向外平方根/除法，不能把已保存的近似 $d$ 当成准确单位向量。

定义完全有理的量
$$
a_-=L_-\widehat r_-,\qquad a_+=L_+\widehat r_+,\qquad
\eta_0=\frac{2E_0}{a_-},
$$
$$
\zeta_0=z_0-\eta_0,\qquad
D_0=E_0+\frac{b_+}{\zeta_0}\eta_0,
$$
$$
A_-=a_--D_0,\qquad A_+=a_++D_0.
\tag{39}
$$
在只对已证正分母作除法的前提下，足够检查
$$
\boxed{\qquad \zeta_0>0,\qquad A_->0,\qquad A_+<L_-.\qquad}
\tag{40}
$$
证明是：真实 $\widehat\alpha=L_c|\widehat v|\in[a_-,a_+]$，真实误差不超过 $E_0$，故定理1的定位距离不超过 $\eta_0$、帽高度至少 $\zeta_0$、误差修正不超过 $D_0$。于是原定理给
$$
d_{*,z}\ge\zeta_0,\qquad
\frac{A_-}{L_+}\le r_*\le\frac{A_+}{L_-}<1,
\tag{41}
$$
$$
|d_*-\widehat d|\le\eta_0,\qquad
\|J^{-1}\|
\le\frac1{L_-}
 \left(1+\frac{b_+/\zeta_0}{L_-(A_-/L_+)}\right).
\tag{42}
$$
存在证明完成后，还可用
$$
\eta_{1,0}=\frac{2E_0}{a_-+A_-},\qquad
|v_*-\widehat v|
\le\frac{E_0+(b_+/\zeta_0)\eta_{1,0}}{L_-}
\tag{43}
$$
收紧误差。

任何实现的除法、平方根、残差范数、区间传播若用有限算术，都必须向外封口。不可只对最终显示值增加一个未经证明的容差。宽盒或 (40) 未通过表示本充分证书未付，不能据此认定方程无根、working Newton 失败或当前物理场无解。

### 8.1 这里的 $E_0$ 究竟包含什么

若工作程序形成 $R_w=\widehat L_c\widehat v+\widehat B-\widehat K$，则一种充分的完整账是
$$
E_0\ge
|R_w|_{\rm upper}
+\delta_B+\delta_K
+\delta_{L_c}|\widehat v|_{\rm upper}
+\delta_{\rm residual\ arithmetic}.
\tag{44}
$$
$\delta_B$ 包括全部四端层的准确积分、准确 $T_0$、端层位置/权/阶跃及候选准确归一化与工作归一化之间的差；$\delta_K$ 包括完整帽端、core 逆图、所有补集与准确尾；$\delta_{L_c}$ 包围工作和准确中央长度。工作浮点加和与范数必须由最后一项或直接完整区间求值承担。若直接包围准确 (3)，不必人为再重复分项；不能遗漏任一输入误差。

在一个 whole-angle 胞上可以保同一个实际候选中心 $\widehat v$，再对 $K(\phi),T_0(s,\phi)$ 的全部角范围求 (44)。候选不需要是每个角的 working Newton 结果；但是其实际来源、固定参考、原完整积分域和被比较的工作角 jets 必须明确。更宽角胞可能使 $E_0$ 增大，这是实际费用的分辨率问题，不是删除角域的许可。

正权有限求积也有自己的凸势，但其完整权重总和与目标不同。对离散方程证明 (40) 不能自动替代准确连续方程；离散到准确的完整差仍属于 (44)。

## 9. 为什么这是真正增加的存在范围

本条件不要求先有 R709 的粗根。它以完整实际候选残差定位全局凸极小点，所以只要候选与准确费用足够接近一个合法的正半球根，(17) 可以在粗 $K_z>b$ 失败时仍成立。

准确地说，若某个固定数据的真实根满足 $0<r_*<1$、$d_{*,z}>0$，取趋近该根的候选，并且其完整向外残差上界趋零，则
$$
\widehat\alpha\to L_cr_*>0,\quad
\eta\to0,\quad
\zeta\to d_{*,z}>0,\quad
\Delta\to0.
$$
因此最终会满足 (17)。这个陈述只说明充分条件覆盖每个严格内部的合法根邻域；它没有承诺某组固定 binary64 工作字或有限900秒费用预算一定给出足够小的误差。

也可用一个纯解析的抽象数据族看出 $K_z>b$ 确非必要。取 $T_0=e_x$，全部端层总长为 $b>0$，每端的 cutoff 按原对称五次阶跃满足
$\chi(1-t)=1-\chi(t)$。令 $d=e_z$。于是
$$
B_x(e_z)=B_z(e_z),\qquad
B_x(e_z)+B_z(e_z)\le\sqrt2\,b,
$$
所以 $B_z(e_z)\le b/\sqrt2$。令 $L_c=b$、$\widehat v=e_z/8$，并**定义准确目标**
$$
K=B(e_z)+(b/8)e_z.
$$
此时准确残差为零、$\widehat\alpha=b/8$，本定理满足全部严格条件。另一方面
$$
K_z\le b(1/\sqrt2+1/8)<b
$$
（$1/\sqrt2<7/8$ 由平方比较即得），所以旧条件 $b<K_z$ 不可能成立。

这只是同一均值定理假设内的解析例证；没有执行数值积分或 fixture，也没有声称这个人为定义的 $K,T_0$ 就是当前 Fejér 完整参考。它不替当前运行支付任何费用。

## 10. 已公开数学核和实际接口的精确区别

本文完整读取了 R708、R709、R710、R711 和 R721。R708 给原收缩域；R709 已给全局凸势与无收缩唯一性，但其存在步骤仍依赖粗 (3)；R710 的费用以已存在准确根为前提；R711 给合法均值长度后的 profile 根；R721 分析已存在根的参数敏感性。这里新增的是第3节候选支撑式对**尚未知位置的全部闭球极小点**的定位，以及由此取代粗存在条件。

当前完整来源为：

| 来源 | 完整 SHA256 | 本文使用范围 |
|---|---|---|
| [R708](R708-supported-unit-meridian-seed-contraction.md) | 0b17480e32b43f0aeec81a324aa8a099dac5f2cf5f6c6b11ec36950ce722bb34 | 原完整支持、单位端层和原收缩域 |
| [R709](R709-global-convex-mean-closure-without-contraction.md) | 0899ae28564b64468c81746d2543f1ab4d4ed455b2752af0d3e46be8fceba830 | 凸势、完整方程、正切 Jacobian 与既有误差结构 |
| [R710](R710-supported-unit-seed-complete-angular-jet-error-bounds.md) | dd96a501a4758ac9097b1cc51afafa165fd4ee8faaeea09360fc6adb0b704ec5 | 整帽分母、完整一二角 jet 与工作字费用 |
| [R711](R711-smooth-triangle-central-profile-and-geometric-comparison.md) | 7df73fc19224cde3c315d31dfce053892f86ff9af03f376ecee62fdce47b9fe6 | $0<r<1$、$0<\delta<1/8$ 的完整 profile |
| [R721](R721-supported-seed-width-and-profile-sensitivity.md) | 14a0b6205f89fa68e5ec04de5960ca19859fccfebac015e01fadb02f75c7363a | 端层宽度、移动边界与 profile 参数范围 |
| [fixed_fejer_axisymmetric_reference.py](../scripts/resume_20261126/fixed_fejer_axisymmetric_reference.py) | e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb | 当前准确固定参考与完整 scalar/材料图来源 |
| [fixed_fejer_supported_meridian_reference.py](../scripts/resume_20261126/fixed_fejer_supported_meridian_reference.py) | ad52a217269c2a30ce9886acb45492e0e825d3a2654f9ed045dc430951d1e15a | 实际 seed 的完整均值、支持及十二片 profile 公式 |
| [fixed_fejer_reference_accurate_mean_residuals.py](../scripts/resume_20261126/fixed_fejer_reference_accurate_mean_residuals.py) | ae67ecac9f205cdb2378a7f981d5d60fc723e1caadd5281dff54395d358564a0 | 全部准确端层/补集积分与三套总残差 |
| [fixed_fejer_reference_seed_angular_profile_error_bounds.py](../scripts/resume_20261126/fixed_fejer_reference_seed_angular_profile_error_bounds.py) | 0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b | 原完整 R709/R710/R711/R713 算术 |
| [fixed_fejer_stage_observed_normal_packet_accurate_field_input.py](../scripts/resume_20261126/fixed_fejer_stage_observed_normal_packet_accurate_field_input.py) | 720bbfc1071a3e56598fd096ec420e8cb5a44a60e06b28d33ff0f1c37e3038b3 | 当前 observed 同点、完整 source/packet 与动态 seed 绑定 |
| [fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py](../scripts/resume_20261126/fixed_fejer_stage_observed_accurate_reference_control_radial_boxes.py) | 03dceaf721d5a93758a0c61055b6f409a240bb235e22f846874cf45e7bca15bd | WholeMean 的完整 whole-angle 数学复用与准确径向域 |

ae67 的 ActualMeanBatch.assemble_sums 已计算准确 $K$ 的三套 jets、完整端层三套积分、$L_c\widehat v+B-K$ 的三套向量包围和范数。它仍将旧的 $b<k_-$、$b<k_z$、$k_++b<L_{c,-}$ 写入其原 R709 条件字段。

0471 的 mean_jet_bounds 仍明确检查那些粗条件，随后才从它们生成 $r_\pm,\zeta$。03dc 的 enclose_reference_mean 也在调用该完整核之前检查旧 R709 字段；未付时仍返回 EnclosureUnavailable。它的 WholeMean 仅绕过旧 literal CLI 的来源构造以绑定实际 whole-angle 对象，不曾改变粗条件的数学含义。

因此本文**没有让现有代码自动接受新证书**。今后若实现独立后验消费者，应明确引用本条、消费同一完整准确 $E_0,L_c,b,\widehat v$ 与 (40)，返回自己的存在/包含来源；不能把旧 all_pointwise_R709_sufficient_inequalities_proved 写成 true，也不能把未满足的 $K_z>b$ 数值改标为满足。取得合法根域后，可明确复用原完整角 jet 算术；相应来源变化需真实保留。

原 ae67/0471 独立 literal-batch CLI 仍绑定其原 477499/274d 来源；当前 720b→03dc 的 whole-angle 路径绑定 observed 实际对象。两个入口不能因方程相同而互换报告标签。本文没有改源码、参数、预算或已排任务。

## 11. 实际证据和未付边界

若把本条用于实际场，候选必须来自完整真实报告或合法的同点不可变快照；准确参考、完整输入文件、seed 参数、literal 角序列或 whole-angle 域、全部原始数组及其源身份仍要逐一绑定。可变 progress 上的 point、工作 residual 的显示值、prepared input 成功或某个缓存计数都不是 (14) 的证据。

特别地，候选
$$
\widehat D=K-B(N\widehat v)
$$
的正垂直分量或 $|\widehat D|<L_c$ 单独不足以证明它等于 $L_cv_*$。本条还明确支付 (20) 的全局定位、正帽、误差修正和严格正乘子。若 $\widehat d$ 不是准确单位方向，或 $E_0$ 没有包含完整四端层/补集/尾与所有工作差，证明不能启动。

本条没有：

- 认证当前17或任何其它运行的准确均值根、profile 根或32-stage normal 根；
- 把单角结论升级为全圆，或把有限样本升级为全径向/全曲面；
- 生成工作 physical sixjet 的完整误差、连续 Gram/K/support、闭面外向、全部混合点对、全 phase、握持整像幅度、R716 中心矩或 reach；
- 承诺原 Newton 或后处理在声明预算内完成。

新的存在性充分条件可在真实费用返回时提供一个较少保守的可选分支。它不阻塞原完整工作求解；未能付清本证书时，保持“未付”即可，原真实运行及其全部未知历史责任继续保留。
