# R674：准确参考尾的连续 profile、完整六 jet 与同角余项

日期：2026-11-20。会话：Astra-resume-public-20261120 / fullclosed_solver。

**状态：下面的区间构造与误差传递已作纸面推导，并逐项对照现有源码接口；没有执行新的科学计算。** geometry_path 正据此写独立的新 reader。本文不把已有非零 $\lambda$ 的有限点读出提升为连续证书，不更改已发布旧核，也不增 fixture 或独立检查门。

依据是 [R671](../results/R671-exact-reference-tail-affine-lift.md) 的真实新场、[R657](../results/R657-complete-closed-relative-Gram-and-same-scalar-enclosure.md) 的准确标量 Taylor / Gram 抵消、[R670](../results/R670-direct-same-angle-first-geometry-with-complete-tails.md) 的首 jet 同角盒，以及 [R672](../results/R672-complete-lowmode-sixjet-curvature-with-laurent-remainders.md) 的完整六 jet / Laurent 余项。新部分只在径向 profile 和它的误差支付；全部原 $q$、core、角模与解析 $e_r(\Theta)$ 都保留。

## 1. 准确对象与需要改变的接口

令旧 profile 为 $\chi,f_0=\chi(R+S-s)$。本轮固定 $\lambda$，$\eta$ 的两个断点均取原准确节点，且 $\eta=1$ 从旧 $\chi$ 的准确支撑起点 $S-w$ 开始。因此 $\eta\chi=\chi$，R671 可写为

$$
h=(1-\lambda)\chi+\lambda\eta,\qquad
f=(1-\lambda)f_0+\lambda\eta a,\qquad
k=-\lambda\eta I,
$$

$$
F=q+f e_r+(Hh+k)e_z,
\qquad I(s)=\int_s^S\cos\alpha(u)\,du.
\tag{1}
$$

$a,I$ 来自原同一个 FullHold 整数 oracle；$\alpha'=-\kappa$，$a'=\sin\alpha$，$I'=-\cos\alpha$。$S,R$、原符号节点、自由 binary 系数及派生 core 槽沿用 R662/R671 的准确解释，不改为浮点 carrier 的另一条曲面。

记 $Z=Hh+k$。全六 jet 为

$$
\begin{aligned}
X&=q+f e_r+Ze_z,& V&=q_s+f_s e_r+Z_s e_z,\\
T&=q_\phi+f\rho e_\theta,& AA&=q_{ss}+f_{ss}e_r+Z_{ss}e_z,\\
VT&=q_{s\phi}+f_s\rho e_\theta,&
EE&=q_{\phi\phi}+f(\rho_\phi e_\theta-\rho^2e_r).
\end{aligned}\tag{2}
$$

所有 $\phi$ 导数已包含旋转架连接项。新 $Z$ 不依赖角，故 $T,VT,EE$ 没有额外竖直 profile 项。

现有 R670/R672 把这些径向系数称为次数至多6的多项式。对非零 $\lambda$ 这不再正确。合法替代是“有限 Bernstein 多项式加已付、逐导数的连续误差”，不能只把新的节点/Gauss 数组交给旧 degree-six 核。

## 2. 精确分片和最少 oracle 调用

每个原胞必须与以下准确位置相交后，才建立一个 profile 多项式：原 FullHold 的全部 scalar 分段边界、$\eta$ 两节点、旧 $S-w$ 断点。端点仍是 $\alpha S+\beta$，$\alpha,\beta\in\mathbb Q$。先消去相同 $S$ 的代数相关项，再用原 $S$ 外盒确定次序和正宽度；不能凭浮点显示位置合并极短片。

在 $\eta=0$ 的整片，新修正及前二导严格为零，直接使用旧准确多项式，不查询未定义在旧 prefix 上的 $I$。其余片位于原 Hold 内部。每个闭片只使用它所属的一个完整 scalar 解析段：该段 $\kappa$ 为常数或准确五次 smoothstep，$\alpha$ 为至多六次多项式。对接缝两侧分别包围闭片并取并集，原 $C^2$ 接口保证没有遗漏；不跨越高导数改变公式的边界套一个 Taylor 余项。

最直接的实现是在每个当前径向子片的准确符号中点 $s_*$ 查询一次 $(a_*,I_*)$，并缓存这个准确位置。一次 FullHold 的 `at_box` 已给 $a$ 和累计高度；以整数向外减法

$$I_*=(\hbox{总高度增量})-(\hbox{当前位置高度增量})$$

得到原 $I$ 的盒。这里不是把普通浮点积分相减后重新定义函数。

若同 job 已保存新 factory 的 profile carrier，还可复用它的 `reference_values/reference_absolute_error`：将同一实际模型、同一 SHA、`reference_active=true` 的 $a/I$ carrier 加减已经向外的绝对误差，得到严格 anchor 盒。该 anchor 必须由保存的 `(cell,u)` 还原准确符号位置，且与当前片处于同一完整 scalar 解析段。它可在小片外，但余项半径必须覆盖 anchor 到整片的最大距离。不能把零填充的 inactive 行当成 scalar 值。

这两种方法均使用真实积分盒作常数项，而不是用样值拟合 $a$ 或 $I$。首版采用子片中心查询即可；不需要另外重算一套旧连续证书。

## 3. 同一个 Taylor jet，分别形成 0 / 1 / 2 阶多项式

写 $t=s-s_*$，并由原准确曲率积分得到

$$\alpha(s_*+t)=\sum_{j=0}^{6}\alpha_j t^j.$$

不存在的高次系数取零。令归一化 Taylor 系数满足

$$
\sin\alpha(t)=\sum_{j\ge0}p_jt^j,
\qquad \cos\alpha(t)=\sum_{j\ge0}c_jt^j.
$$

$p_0,c_0$ 用原严格三角函数核包围。由链式法则，

$$
p_{j+1}=\frac1{j+1}\sum_{k=0}^{j}(k+1)\alpha_{k+1}c_{j-k},
$$

$$
c_{j+1}=-\frac1{j+1}\sum_{k=0}^{j}(k+1)\alpha_{k+1}p_{j-k}.
\tag{3}
$$

取 $n\ge3$，定义同一个准确 Taylor jet 的两个形式多项式

$$
A(t)=a_*+\sum_{j=0}^{n-1}\frac{p_j}{j+1}t^{j+1},
\qquad
J(t)=I_*-\sum_{j=0}^{n-1}\frac{c_j}{j+1}t^{j+1}.
\tag{4}
$$

式(3)–(4)的每个系数用向外区间包住其真实值。$A^{(r)},J^{(r)}$ 的系数由同一 power jet 按准确下降阶乘直接形成，$r=0,1,2$，然后分别转换到当前 piece 的 Bernstein 系数。

**不要对已经含重复 $a_*/I_*$ 区间的 Bernstein 控制点直接做区间差分来生成这些导数。** 真实常数项在导数中应准确消去；独立区间相减却可能把 anchor 宽度放大为 $1/h$、$1/h^2$。分别形成 power 导数仍是同一个 Taylor 多项式的导数，不是另拟合三个互不相关函数。现有 R657 `power_to_piece` 可直接复用。

### 3.1 完整 Bell 余项

令 $K_j\ge\|\kappa^{(j)}\|_\infty$，所取范围至少包含 anchor 与当前片之间的整段。令 $A_{j+1}=K_j$，并置

$$
\mathcal B_0=1,\qquad
\mathcal B_{m+1}=\sum_{j=0}^{m}\binom mj A_{j+1}\mathcal B_{m-j}.
\tag{5}
$$

$\alpha$ 次数不超过6，故 $A_j=0$ 对 $j>6$。对 $e^{i\alpha}$ 的导数恒等式归纳，得到

$$
\bigl|(\sin\alpha)^{(m)}\bigr|,
\bigl|(\cos\alpha)^{(m)}\bigr|\le\mathcal B_m.
$$

设 $r_*\ge\max_{s\in\mathrm{piece}}|s-s_*|$。分别对真实 $a^{(r)}$、$I^{(r)}$ 作 Taylor 定理，得到

$$
|a^{(r)}-A^{(r)}|\le
\varepsilon_{a,r}:=\frac{\mathcal B_n r_*^{n+1-r}}{(n+1-r)!},
$$

$$
|I^{(r)}-J^{(r)}|\le
\varepsilon_{I,r}:=\frac{\mathcal B_n r_*^{n+1-r}}{(n+1-r)!},
\qquad r=0,1,2.
\tag{6}
$$

这是分别对各阶导数的证明，不是对一个 $C^0$ 误差不合法地求导。常数项和其它系数的区间宽度已经保存在控制点区间中；(6)仅是截断误差，不再次把 anchor 宽度加到导数误差。

首版 $n=5$ 时需要

$$
\mathcal B_5=K_0^5+10K_0^3K_1+15K_0K_1^2
 +10K_0^2K_2+10K_1K_2+5K_0K_3+K_4.
\tag{7}
$$

位置、一导、二导余项依次按 $r_*^6,r_*^5,r_*^4$ 缩小。若采用 $n=3$，只需到 $\kappa''$，但二导余项仅按 $r_*^2$ 缩小；它不是相同精度的免费替代。

### 3.2 曲率导数无需新数值拟合

在宽度 $w$ 的 ramp，$\kappa=\kappa_L+\Delta\kappa\,S_5(u)$，$u\in[0,1]$，$S_5=10u^3-15u^4+6u^5$。可直接使用

$$
K_0\le\max(|\kappa_L|,|\kappa_R|),\quad
K_1\le\frac{15|\Delta\kappa|}{8w},\quad
K_2\le\frac{6|\Delta\kappa|}{w^2},
$$

$$
K_3\le\frac{60|\Delta\kappa|}{w^3},\quad
K_4\le\frac{360|\Delta\kappa|}{w^4},\quad
K_5\le\frac{720|\Delta\kappa|}{w^5}.
\tag{8}
$$

其中 $\max|S_5''|=10\sqrt3/3<6$；其余值由显式导数及区间端点/驻点得到。也可先对准确 Bernstein 多项式作物理导数、再限制到需要的范围，取控制点绝对值上界；与(8)取较小者仍严格。常曲率片 $K_{j>0}=0$。所有 $w^{-j}$ 均是物理长度，不得误作单位子片参数。

## 4. 新 profile 的多项式与三个独立误差

在当前片上，$\chi,\eta$ 均为准确多项式。构造

$$
\widehat f=(1-\lambda)f_0+\lambda\eta A,
\qquad
\widehat Z=H[(1-\lambda)\chi+\lambda\eta]-\lambda\eta J.
\tag{9}
$$

用(4)的解析导数和准确 Leibniz 公式直接形成 $\widehat f^{(r)},\widehat Z^{(r)}$，不对含共同 anchor 盒的结果再做区间差分。令 $E_j\ge\|\eta^{(j)}\|_\infty$，则

$$
e_{f,r}=|\lambda|\sum_{j=0}^{r}\binom rj E_j\varepsilon_{a,r-j},
\qquad
e_{Z,r}=|\lambda|\sum_{j=0}^{r}\binom rj E_j\varepsilon_{I,r-j}
\tag{10}
$$

分别控制 $|f^{(r)}-\widehat f^{(r)}|$ 和 $|Z^{(r)}-\widehat Z^{(r)}|$，$r=0,1,2$。$Hh$ 是准确多项式，因此没有额外的 $H\varepsilon_I$ 项。特别在 $\eta=1$ 片，(10)退化为 $|\lambda|\varepsilon_{a,r}$ 和 $|\lambda|\varepsilon_{I,r}$。

$n=5$ 时，位置 profile 的次数至多10，一导至多9，二导至多8；连同原 $q$ 可统一升阶至10。先在同一 Bernstein 控制点上合并

$$q_R+\widehat f(\hbox{有限解析角系数}),\qquad q_{Z0}+\widehat Z,$$

以及相应导数，再取盒，保留真实大数抵消。绝不能先分别把 $q$、$f$、$Z$ 取全片绝对值再相加。

每次径向加密可在新符号中心重建该片的 Taylor 模型，使(6)随新半宽缩小。仅对一个已经固定的大片多项式做 de Casteljau，却沿用原大半径误差，不会自动缩小 Taylor 误差；报告须区分这两种来源。

## 5. 保留 R670 / R672 的完整角余项

原 core 给出的 $\delta,\rho,\rho_\phi$ 不改。完整 Laurent 展开及其三类误差继续记为

$$
\varepsilon_r\ge|e^{i\delta}-P_{\rm fin}|,\quad
\varepsilon_\rho\ge|i\rho e^{i\delta}-Q_{\rm fin}|,
$$

$$
\varepsilon_B\ge|(-\rho^2+i\rho_\phi)e^{i\delta}-B_{\rm fin}|.
$$

这些是 R670/R672 已付的完整 Laurent $>M$ 高尾与实相位指数余项之和，不能只保留低角模。原 $L+1,\ldots,M$ 模另在合并控制点上付绝对值和，与这里的尾不同。

令 $R_\rho\ge\|\rho\|_\infty$，$R_B\ge\sqrt{\|\rho\|_\infty^4+\|\rho_\phi\|_\infty^2}$。对当前径向子片，完整新水平误差为：

| jet | 多项式有限部分之外的水平向量误差 | 竖直误差 |
|---|---|---|
| $X$ | $\|\widehat f\|\varepsilon_r+e_{f,0}$ | $e_{Z,0}$ |
| $V$ | $\|\widehat f_s\|\varepsilon_r+e_{f,1}$ | $e_{Z,1}$ |
| $T$ | $\|\widehat f\|\varepsilon_\rho+e_{f,0}R_\rho$ | 0 |
| $AA$ | $\|\widehat f_{ss}\|\varepsilon_r+e_{f,2}$ | $e_{Z,2}$ |
| $VT$ | $\|\widehat f_s\|\varepsilon_\rho+e_{f,1}R_\rho$ | 0 |
| $EE$ | $\|\widehat f\|\varepsilon_B+e_{f,0}R_B$ | 0 |

证明只需准确分解

$$f^{(j)}L-\widehat f^{(j)}L_{\rm fin}
=\widehat f^{(j)}(L-L_{\rm fin})
 +(f^{(j)}-\widehat f^{(j)})L.$$

对最后一项使用真实乘子模 $1,R_\rho,R_B$。因此没有遗漏 scalar 误差与角尾的交叉项，也无需把 scalar 误差再乘一个人为的大有限多项式界。$\widehat f^{(j)}$ 先作同片 Bernstein 细分再取绝对值；$e_{f,j},e_{Z,j}$ 是该片的统一常数，可以加到所有控制点，因为 Bernstein 基之和为1。

同角低模闭弧变换、全部原有限高模、Bernstein 凸包、真实第一形式和形算子计算都沿用 R670/R672。新 $a/I$ 仅是径向标量，不增加角带宽。六个向量都对同一个径向片和同一个闭角弧包围，所以支持、法向、曲率及见证距离的同角逻辑保持。

## 6. R657 的最小 Gram 消费者

以 $U=q_s,T_0=q_\phi,C=\widehat f_s,D=\widehat Z_s,F=\widehat f$ 代入 R657 的同一 $P+C_1\cos\delta+S_1\sin\delta$ 表；目标 scalar 近似直接使用这里的同一 $A$。完整径向乘积先在 Bernstein 系数处形成，原第0–4阶角导数、非带限第四导预算及闭弧包围不变。径向次数须由实际输入次数动态升阶，不能保留“至多12”作为新模型上限。

这先包围近似场

$$\widehat V=U+C e_r+D e_z,\qquad
\widehat T=T_0+F\rho e_\theta.$$

再支付(10)。由于水平与竖直正交，

$$\epsilon_V=\sqrt{e_{f,1}^2+e_{Z,1}^2},\qquad
\left|\frac{T-\widehat T}{a\rho}\right|
\le\epsilon_W:=\frac{e_{f,0}}{a_-}.
\tag{11}
$$

这里先准确约去 $\rho$，不在小 $\rho$ 处把 scalar 误差多放大一次。若同盒已有 $B_V\ge|\widehat V|$、$B_W\ge|\widehat T/(a\rho)|$，则三项的额外误差为

$$
\Delta_E=2B_V\epsilon_V+\epsilon_V^2,
$$

$$
\Delta_M=B_W\epsilon_V+B_V\epsilon_W+\epsilon_V\epsilon_W,
$$

$$
\Delta_G=2B_W\epsilon_W+\epsilon_W^2
 +\frac{\varepsilon_{a,0}(2|A|+\varepsilon_{a,0})}{a_-^2}.
\tag{12}
$$

最后一项正是原目标 $a$ 与多项式 $A$ 的差；若沿用 R657 `relative` 已支付此项，(12)中不得再加一次。先确认 $a_->0,\rho_->0$ 再除法。将近似三项盒分别扩张 $[-\Delta_E,\Delta_E]$ 等，然后使用原准确对称矩阵谱范数公式，便得到新真实 relative Gram 的连续界。

$B_V$ 和 $B_W$ 可从已经消去大数抵消的近似 Gram 分子得到。若 $\widehat G$ 明确指修正前的分子商 $(|\widehat T|^2-A^2\rho^2)/(a^2\rho^2)$，可取

$$B_V=\sqrt{\max(0,1+\overline{\widehat E})},\qquad
B_W=\sqrt{\max(0,\overline{\widehat G}+\overline{A^2/a^2})}.$$

这样无须退回独立的巨大 $q_s$ 与 lift 盒。本段是一个完整有效的最小扩展，不依赖新的数值采样。

### 准确参考尾的额外符号抵消

若要进一步收紧，写 $\ell=\lambda\eta$、$b=(1-\lambda)f_0$，则准确有

$$f^2-a^2=(\ell^2-1)a^2+2\ell ba+b^2.$$

在 $\lambda=1,\eta=1$ 上此项逐字为零，不应独立支付两份 $a$ 的误差。类似地令

$$u=b_s+\ell_s a,\qquad v=(1-\lambda)H\chi_s+\ell_s(H-I),$$

则 $f_s=u+\ell\sin\alpha$、$Z_s=v+\ell\cos\alpha$，所以

$$f_s^2+Z_s^2=u^2+v^2+2\ell(u\sin\alpha+v\cos\alpha)+\ell^2.$$

这保留 $\sin^2\alpha+\cos^2\alpha=1$。在准确参考尾且 $q=0$ 时，两个纯 lift 分子严格消去。它是代数收紧，不是把近似 scalar 当作新目标，也不是首版有效性必需的额外门槛。

## 7. 源码接口核对点与范围

新 helper 的最小返回值应包括：准确 piece/anchor 身份、$A^{(0,1,2)}$ 与 $J^{(0,1,2)}$ 的 Bernstein 外盒、$\widehat f^{(0,1,2)}$ 与 $\widehat Z^{(0,1,2)}$、各阶(6)/(10)误差、实际次数、同原 scalar/oracle/model SHA。R657 额外直接消费 `a_poly0/a_error0`。

已从现有源确认的连接位置：

1. R670 `Direct.cell/field_boxes`：替换径向 profile 生成与 tail 数组，保留同角完整 transform 和几何代数。
2. R672 `piece_definitions/field_blocks`：扩充竖直 scalar 误差与水平(第5节)误差；内存块预算的字面 `7` 是旧控制点数，须改为实际次数加1。原 `elevate(...,degree=6)` 也须显式改为本片实际统一次数。
3. R657 `physical_components/numerator_controls/relative`：使用新 $F,C,D$ 与同一 $A$，付(12)。旧 `if not piece[4]` 的 `piece[4]` 仅表示旧 $\chi$ active；$\eta$ 更早激活，不能用它跳过新 lift。只把这个旧 flag 留给旧 $\chi$ 多项式的生成。
4. 所有 raw/profile/bundle 的 canonical model identity 必须一致。不能用旧报告与相同 $q$ 数组拼接成新模型证书；optional first-geometry 下界也必须来自同一新 field/model。

新 $\eta,h,f,k$ 都是径向标量，半周、反射和上下镜像结构不变；新帽三 jet 与旧帽相同。因此在完整新位置/首 jet 盒已经支付后，R670 的两盘、支持嵌入、直径及两符号 held 见证论证可直接沿用。R672 的曲率则使用新六 jet 与真实第一形式，不用目标 $g$ 代替。

**旧非平面 marker 标签不能原样沿用。** `fullclosed_nonplanar_coefficients.py` 的水平轴 trace 使用旧 $\chi(R+S-s)$，且把整胞称为多项式。一种充分路线是在每个上述解析 piece 对两个新水平轴 trace 支付严格非零点，再用实解析延拓；它不排除由完整嵌入直接推出轴 trace 非零的更短证明。原非零 $Z$ 角模 Hermite 见证仍有效，因为新 $Hh+k$ 只改 $Z_0$：若某个非零角模多项式有一个非零原三 jet，它不可能在任意开子片恒零。结合半转对称与两个轴 trace，可沿原证明排除平面开片。这个充分条件尚未实际支付时，首版不标记 marker/E3 已付；不能把未付解释为真实平面片。

本文不给任何新候选的连续数值上界、reach 或完成标签。上述 source 扩展在公开 Actions 对实际新 bundle 返回完整覆盖之后，才有相应候选结论。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
