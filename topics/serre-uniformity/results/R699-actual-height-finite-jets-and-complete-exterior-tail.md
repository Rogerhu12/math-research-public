# R699：真实规范高度的有限 jet 输入、外积首阶的有限范围及完整尾界

日期：2026-11-14。状态：**下列结构与估计已证明；尚未算出实际规范高度常数，亦未证明实际外积首项为单位或排除全部原候选。** 本文继续 R634/R682 的同一 $c_1$、商、刚性化、截面和 $Y$-线性修正，使用 R690/R694/R696 已证明的原候选坏处靶值 $\omega=\omega_0=0$。涉及正秩商的结论始终保留 R616 的实际本原非消失前提。

新增内容：把真实高度的无限尾部归约到明确的有限规范输入；给实际外积一个统一小于 $4$ 的线性斜率；用代数微分算子把其可能首阶限制到可核验的有限整数集合。有限精度下看似零的系数不因此成为精确零。

## 1. 保留实际高度，不以 Abel 积分代替

采用 R634 的记号

$$
 X=X_1,\quad G=g(X),\quad A=A_{-1,1},\quad
 F=\operatorname{End}_{\mathbb Q}^0(A),\quad g=[F:\mathbb Q],
 \quad \beta=q[c_1-c_0].
\tag{699.1}
$$

假定同一个实际乘积

$$
 L'(g_{-1,+},1)L(g_{-1,-},1)\ne0.
\tag{699.2}
$$

R616 给 $A(\mathbb Q)\otimes\mathbb Q=F\beta$ 及实际对数同构；R682 给各 $L_i=\log_p(\beta)_i\ne0$ 和共同 Abel 首阶 $m\ge1$。写

$$
 z=a-1,\qquad
 t_i=1+T_i z^m+O(z^{m+1}),\qquad
 T_i\ne0,\quad T_i\ne T_j\ (i\ne j).
\tag{699.3}
$$

原高度为

$$
 \Lambda_h=\lambda^F_{p,h}-2\ell_h(P),
 \qquad P=\log_p\phi_*[x-c_0].
\tag{699.4}
$$

其 $r=g-1$ 个坐标使用 R634 的加权迹对偶基，不去掉实际 $\kappa=qq^\dagger$。在 R696 的原候选分支上，令

$$
 d_i=\Lambda_i(c_1),\quad
 V_i=t_i^2-t_g^2,\quad
 W_i=d_i t_i^2-\Lambda_i,\quad
 E_{ij}=W_iV_j-W_jV_i.
\tag{699.5}
$$

所有原候选满足 $E_{ij}=0$。R634 Theorem 634.3 证明每个 $E_{ij}$ 在 $c_1$ 盘上非恒零；R682 给

$$
 \operatorname{ord}_{c_1}V_i=m,\qquad
 \operatorname{ord}_{c_1}E_{ij}\ge m+1.
\tag{699.6}
$$

这里没有 $m=1$ 的默认值，也没有把后一个界强化为 $2m$。

## 2. 外积不依赖 $A$ 的 $F$ 相容 splitting

**引理 699.1。** 保持 $Y$ 的 splitting、全局角色、截面和全部 $p$ 外数据不变，仅在 R634 容许的 $F$ 相容对称 splitting 之间改变 $A$ 的 splitting，(699.5) 的 $E_{ij}$ 作为同一局部函数完全不变。

证明。R634 (634.11)–(634.12) 给两个规范高度之差为对数上的二次型。两个 splitting 都 $F$ 相容，所以该型在 $F\otimes\mathbb Q_p=\mathbb Q_p^g$ 上为对角型。存在 $R\in F\otimes\mathbb Q_p$，使

$$
 \Lambda'_h(x)-\Lambda_h(x)
       =\operatorname{Tr}(hR\,t(x)^2).
\tag{699.7}
$$

记 $r_i=R_i/\kappa_i$。实际坐标满足

$$
 \Lambda'_i-\Lambda_i=r_i t_i^2-r_g t_g^2,\qquad
 d'_i-d_i=r_i-r_g,\qquad W'_i-W_i=-r_gV_i.
\tag{699.8}
$$

外积因而不变。这是同一截面上 log functions 的精确比较，不是只在有理点比较后任意延拓。$\square$

故可在计算中选一个代数的 $F$ 相容 splitting。具体地，$H^1_{\mathrm{dR}}(A/\mathbb Q)$ 是秩二的 $F$-模，Hodge 子模秩一；选一个 $F$-线补空间。极化交替配对为 $F$-双线性交替配对取迹，故该线自动各向同性，得到定义在 $\mathbb Q$ 上的 Lagrangian 补空间。

在此选择下，对称线丛的曲率张量是代数的。Picard 零次线丛的规范曲率为零：$[-1]^*L\simeq L^{-1}$，而 $[-1]^*$ 在 $H^0(\Omega^1)\otimes H^1_{\mathrm{dR}}$ 上为 $+1$，规范函子性给曲率等于其负数。$2\ell_h(P)$ 是全纯一重积分，也不改变曲率。因此

$$
 \alpha_i=\sum_{b=1}^{s_i}\omega_{ib}\otimes[\eta_{ib}],
 \qquad \omega_{ib}\in q^*H^0(A,\Omega^1),\qquad
 \bigcup\alpha_i=0
\tag{699.9}
$$

是 $\Lambda_i$ 的曲率；其数据可在某个有限数域上取值。分裂后的坐标基也仅需加入有限个代数数。实际规范高度中的周期及 $Y$-线性高度没有因此消失，将在第 4 节保留。

## 3. 同一个 $c_1$ 高度盘的真实整尺度

令 $R$ 为有限 $p$ 进扩张的整数环，含 R592 的实际细水平 CM 标记、$\mu_3$ 和

$$
 \lambda=\varpi^{p^2-p},\quad \varpi^{p^2-1}=p,\qquad
 v_p(\lambda)=\frac p{p+1}.
\tag{699.10}
$$

R592 §4 证明实际细盘为 $\operatorname{Spf}R[[\tau]]$，其中 $\tau=t/\lambda$，且此盘映入真实整模曲线，而非仅其穿孔泛纤维。椭圆族为

$$
 E_t:y^2=x^3+tx-1.
\tag{699.11}
$$

剩余有效 $\mu_3$ 在 $t$ 上乘本原三次单位根，故粗盘整环为 $R[[\tau^3]]$。这里只取阶数 $3$ 的 tame 商，$p>3$。

**引理 699.2。** 同一个粗盘上

$$
 w=\frac{a-1}{\lambda^3}=\frac z{\lambda^3}
\tag{699.12}
$$

是整参数，且 $R[[w]]=R[[\tau^3]]$。

证明。保持 R592 (592.38) 的真实公式，

$$
 \frac{t^3}{4t^3+27}=a^3(1-a^3).
\tag{699.13}
$$

右侧在 $a=1$ 的导数为 $-3$。隐函数定理在 $\mathbb Z[1/6][[t^3]]$ 给

$$
 a-1=-\frac{t^3}{81}+O(t^6).
\tag{699.14}
$$

若 $T=\tau^3$，则

$$
 w=-\frac T{81}+
       \sum_{n\ge2}b_n\lambda^{3(n-1)}T^n,\qquad
 b_n\in\mathbb Z_p.
\tag{699.15}
$$

线性系数是单位，形式逆也整。$\square$

记

$$
 b_p=3v_p(\lambda)=\frac{3p}{p+1}<3.
\tag{699.16}
$$

整个较大区域 $v_p(z)\ge3$，包括边界 $v_p(z)=3$，都在此盘内，因为

$$
 v_p(w)\ge3-b_p=\frac3{p+1}>0.
\tag{699.16a}
$$

所以以下完整尾界不遗漏该边界。更深的 $v_p(z)\ge4$ 子域当然也包含在内。当前 R317 (317.2) 另有 $v_p(d)=1$ 或 $2$、$v_p(b)\ge1$，故其已筛选族满足 $v_p(r)\ge4$；由于 $p\equiv2\pmod3$，此处 $v_p(a^2+a+1)=0$，从而 $v_p(a-1)=v_p(r)$。本文不依赖这个附加筛选来覆盖整个 $v_p(z)\ge3$ 区域，也未借用另一个 $c_0$ 盘或 $d$-商。

在上述模型上选闭点 $Q\ne c_1$，其闭包与该盘特殊点不交；必要时作有限代数基扩张。可在不同的光滑特殊点附近用 étale 坐标选代数提升，无须引入超越的极点位置。每个 de Rham 类可用只在 $Q$ 有极点的第二类微分表示：在仿射曲线 $X\setminus\{Q\}$ 上计算 de Rham 上同调，单个极点处的留数由留数定理为零。

以下选这样的 $\eta_{ib}$。所用全纯微分及仅在 $Q$ 有极点的代数微分在 (699.12) 形式盘上均无水平极点。乘一个有限标量后它们在此盘上整：闭点光滑，唯一可能的局部极点除子是特殊纤维，其有限阶垂直极点可用一个固定的 $\varpi$ 次幂消去。因此可给出有限整性证书

$$
 \rho=f_\rho(w)\,dw,\qquad
 v_p([w^n]f_\rho)\ge a_\rho\quad(n\ge0).
\tag{699.17}
$$

$a_\rho$ 不必最优；它来自代数模型上的清分母和正则性证明，不能用只检查有限个 Taylor 系数代替。本文未声称这些 $a_\rho$ 均非负或与 $p$ 无关。

## 4. 规范高度中必须保留的有限全纯部分

对 (699.9) 的内积分在 $c_1$ 归零。BMS §3.3.3 的构造可这样实施：选代数微分 $\gamma_i^0$，仅在 $Q$ 有极点，其极部恰抵消

$$
 \sum_b\omega_{ib}\int_{c_1}^x\eta_{ib}.
\tag{699.18}
$$

所需极部是代数的，因为更改内积分常数只增加全纯微分。所需留数总和为 $\bigcup\alpha_i=0$，Riemann–Roch 因而给 $\gamma_i^0$，它也满足 (699.17)。定义

$$
 U_i(x)=\int_{c_1}^x
   \left(\sum_b\omega_{ib}\int_{c_1}^{(\cdot)}\eta_{ib}
                         +\gamma_i^0\right),\qquad U_i(c_1)=0.
\tag{699.19}
$$

极部抵消保证这是平凡线丛上曲率 $\alpha_i$ 的一个 log function 沿无零截面的取值；它一般不是实际规范高度。

固定 $H^0(X,\Omega^1)$ 的代数基 $\xi_1,\ldots,\xi_G$，令

$$
 I_j(x)=\int_{c_1}^x\xi_j.
\tag{699.20}
$$

**定理 699.3。** 存在唯一实际常数 $c_{ij}$，使

$$
 \boxed{\quad\Lambda_i(x)=d_i+U_i(x)+\sum_{j=1}^G c_{ij}I_j(x).\quad}
\tag{699.21}
$$

证明。实际 $\Lambda_i$ 与 $U_i$ 的曲率相同，BMS Proposition 3.5、Remark 3.6 给差的微分为全局全纯微分。按 $\xi_j$ 展开，在 $c_1$ 取值固定常数。全局规范的内积分周期、实际截面刚性化产生的全纯差及 $-2\ell_i(P)$ 全包含于 $c_{ij}$。$\square$

BMS §7.3.1 明确指出：以任意同曲率原函数替换规范高度时，必须同时改变全局高度的线性部分。本文不改变 R634 的关系，故不能直接设 $c_{ij}=0$。

令

$$
 \Gamma_i=\gamma_i^0+\sum_j c_{ij}\xi_j.
\tag{699.22}
$$

每个 $\omega_{ib}$ 在 $c_1$ 至少消失 $m-1$ 阶，而 $\int\eta_{ib}$ 至少消失一阶。因此

$$
 \Lambda_i-d_i=\int_{c_1}^x\Gamma_i+O(z^{m+1}).
\tag{699.23}
$$

实际高度的一次系数是 $g_{i,0}=(\Gamma_i/dz)(c_1)$，不是 Abel 的 $T_i$ 或原 $M_2$。最早可能的外积系数为

$$
 [z^{m+1}]E_{ij}
 =2\bigl(g_{j,0}(T_i-T_g)-g_{i,0}(T_j-T_g)\bigr)\quad(m>1),
\tag{699.24}
$$

而当 $m=1$ 时为

$$
 [z^2]E_{ij}=2\bigl(
 (2d_iT_i-g_{i,0})(T_j-T_g)
 -(2d_jT_j-g_{j,0})(T_i-T_g)\bigr).
\tag{699.25}
$$

这里只识别实际待算量，没有断言右侧非零。

## 5. 最多 $2G-1$ 阶高度 jet 恢复全部规范差

用 $w$ 参数设

$$
 J_{nj}=[w^n]I_j,\qquad 1\le n\le2G-1.
\tag{699.26}
$$

**引理 699.4。** $J$ 列秩为 $G$。可以通过代数计算选 $G$ 个行指标 $n_1,\ldots,n_G\in[1,2G-1]$，使 $J_*=(J_{n_k,j})$ 可逆，且

$$
 \begin{pmatrix}c_{i1}\\\vdots\\c_{iG}\end{pmatrix}
 =J_*^{-1}
 \begin{pmatrix}
 [w^{n_1}](\Lambda_i-d_i-U_i)\\
 \vdots\\
 [w^{n_G}](\Lambda_i-d_i-U_i)
 \end{pmatrix}.
\tag{699.27}
$$

证明。若一个全纯微分的积分在 $1,\ldots,2G-1$ 阶全部系数为零，则微分在 $c_1$ 至少有 $2G-1$ 阶零；非零全纯微分的零除子次数为 $2G-2$，矛盾。故 jet 映射单射。$\square$

因此，除代数曲率、模型和微分外，完整 $\Lambda_i$ 的规范输入只有 $d_i$ 及至多 $2G-1$ 阶实际高度 jet。它们包含真实 $\ell_i$，本文尚未计算其数值。(699.27) 是恢复公式，不是说这些规范输入已由有限代数计算自动得到。

若只求尾界，给右侧各数可靠赋值下界已经足够：用 $J_*^{-1}$ 的确切条目与右侧差值下界逐项取最小值，给各 $c_{ij}$ 的下界。对减法不得把未证抵消当作已发生。

### 5.1 利用真实 $\mu_3$ 规范，把高度常数降到 $g(Y)$

前述 $G$ 维构造不使用甲板对称。实际 R593 还有更强的结构：它对完整修正线丛取 $\mu_3$ 范数并保留 Picard 零次项，给真正的线性化；$c_0$ 被甲板固定，且实际截面按 $s_h(c_0)=1$ 唯一归一。因此实际截面和采用相容 splitting 的规范局部高度均甲板不变。本节只利用这一个已经固定的规范，不换截面。

首先可把第 2 节的补空间同时选为 $F$ 及 $\mu_3$ 相容。令 $H=H^1_{\mathrm{dR}}(A/\mathbb Q)$，$H^{1,0}$ 为其 Hodge 线 $F$-子模。取一个 $F$-线性投影 $P:H\to H^{1,0}$，其在 $H^{1,0}$ 上为恒等。若 $T$ 为甲板生成元在扩张域上的作用，置

$$
 \bar P=\frac13\sum_{u=0}^2 T^{-u}PT^u.
\tag{699.27a}
$$

$\bar P$ 仍是 $F$-线性投影，在 Hodge 子模上恒等，并与 $T$ 交换。Galois 只置换 $T,T^2$，故它下降到 $\mathbb Q$。其核为秩一的 $F$-补空间，所以仍 Lagrangian。引理 699.1 保证此选择不改变实际 $E_{ij}$。R593 的完整线性化、实际 $s_h$ 与规范 log 的函子性于是给

$$
 \delta^*\Lambda_i=\Lambda_i.
\tag{699.27b}
$$

这里 $P(x)=\log\phi_*[x-c_0]$ 也在甲板下不变，故固定的 $-2\ell_i(P)$ 没有被删去。

取一个甲板稳定的有限极点集合 $D$，避开 $c_0$ 和 $c_1,\delta c_1,\delta^2c_1$ 的相关形式盘；可把第 3 节的 $Q$ 换成一个这样的轨道，并在有限基扩张后取第二类代表。实际正 holomorphic CM 型使 $\delta^*\omega_{ib}=\zeta\omega_{ib}$。在 (699.9) 中，曲率甲板不变迫其第二因子属于 $\zeta^2$ 特征。对第二类代表施以有限特征投影，可取

$$
 \delta^*\omega_{ib}=\zeta\omega_{ib},\qquad
 \delta^*\eta_{ib}=\zeta^2\eta_{ib}.
\tag{699.27c}
$$

所有微分仍代数，第二类代表只在 $D$ 有极点，且在所需形式盘上正则。换成多极点并不改变第 3 节的整性论证。

**必须在这里用固定点 $c_0$ 作为内积分基点。** 令

$$
 S_i=\sum_b\omega_{ib}\int_{c_0}^{(\cdot)}\eta_{ib}.
\tag{699.27d}
$$

因为 $\delta c_0=c_0$，(699.27c) 及积分函子性给 $\delta^*S_i=S_i$，没有额外内积分常数。选择代数 $\gamma_i^{\rm inv}$ 抵消其极部，再按 $\mu_3$ 平均，即可保持同样极部且满足 $\delta^*\gamma_i^{\rm inv}=\gamma_i^{\rm inv}$。定义

$$
 U_i^0(x)=\int_{c_0}^x(S_i+\gamma_i^{\rm inv}),\qquad
 \bar U_i(x)=U_i^0(x)-U_i^0(c_1).
\tag{699.27e}
$$

$dU_i^0$ 不变，$c_0$ 固定且 $U_i^0(c_0)=0$，所以 $U_i^0$ 本身严格不变；$\bar U_i$ 也不变，且在 $c_1$ 为零。其曲率仍为 $\alpha_i$。

故唯一的全纯微分

$$
 \vartheta_i=d(\Lambda_i-d_i-\bar U_i)
\tag{699.27f}
$$

满足 $\delta^*\vartheta_i=\vartheta_i$，从而

$$
 \vartheta_i\in
 H^0(X,\Omega^1)^{\mu_3}=\phi^*H^0(Y,\Omega^1).
\tag{699.27g}
$$

最后一个等式也在分歧点正则：若局部商参数为 $u=t^3$，不变微分的形式是 $t^2g(t^3)\,dt=\tfrac13g(u)\,du$，没有产生极点。

设 $G_Y=g(Y)$，取 $H^0(Y,\Omega^1)$ 基 $\upsilon_1,\ldots,\upsilon_{G_Y}$，并令

$$
 I_j^Y(x)=\int_{\phi(c_1)}^{\phi(x)}\upsilon_j.
\tag{699.27h}
$$

于是得到保持同一规范的精确表达

$$
 \boxed{\quad
 \Lambda_i(x)=d_i+\bar U_i(x)
            +\sum_{j=1}^{G_Y}c_{ij}^Y I_j^Y(x).
 \quad}
\tag{699.27i}
$$

这把自由的规范全纯常数从 $G$ 个降至 $G_Y$ 个；若 $G_Y=0$，该和为空。此处不声称整个 $\Lambda_i$ 是 $Y$ 上的 Vologodsky 函数。这里只下降差的全纯微分；有限覆盖上的不变 Vologodsky 函数不能不经证明就在同一函数类别中下降。

### 5.2 固定 CM 点之间的一重周期不能隐去

当在 $c_1$ 展开 (699.27e) 时，必须保留

$$
 P_{ib}^{(2)}=\int_{c_0}^{c_1}\eta_{ib}.
\tag{699.27j}
$$

其精确局部表达为

$$
 \bar U_i(x)=
 \int_{c_1}^x\left(
   \sum_b\omega_{ib}\int_{c_1}^{(\cdot)}\eta_{ib}
   +\gamma_i^{\rm inv}\right)
 +\sum_bP_{ib}^{(2)}\int_{c_1}^x\omega_{ib}.
\tag{699.27k}
$$

这些是同一 $c_0,c_1$ 及所选实际第二类代表的一重 Vologodsky 周期；不是代数常数，也不是已经由 $L_i$ 算出的数。它们属于明确的非高度周期输入。若直接平均以 $c_1$ 为基点的原函数，也会以 $\int_{c_1}^{\delta c_1}\eta$ 的形式遇到这些常数，不能在平均时删掉。

由于 $\phi:v=a^3$ 在 $c_1$ 不分歧，且 $dv/dz=3$ 为 $p$ 单位，第 5 节的 jet 单射证明可在 $Y$ 上应用。因而用

$$
 J^Y_{nj}=[w^n]I_j^Y,\qquad
 1\le n\le2G_Y-1,
\tag{699.27l}
$$

可选一个可逆的 $G_Y$ 阶子矩阵，并由至多 $2G_Y-1$ 阶的实际
$\Lambda_i-d_i-\bar U_i$ jet 唯一恢复全部 $c_{ij}^Y$。若 $G_Y=0$，无需任何此类 jet。新增的周期输入 (699.27j) 必须先计入 $\bar U_i$，不能把维数降低解释成所有非代数输入已降为只有 $G_Y$ 个数。

采用本节分解时，第 6 节的高度偏移常数可替换为

$$
 \begin{split}
 A_i^{\rm inv}=\min\{&
 a_{\gamma_i^{\rm inv}},\
 \min_b(a_{\omega_{ib}}+a_{\eta_{ib}}),\\
 &\min_b(v_p(P_{ib}^{(2)})+a_{\omega_{ib}}),\
 \min_j(v_p(c_{ij}^Y)+a_{\phi^*\upsilon_j})\}.
 \end{split}
\tag{699.27m}
$$

后面的完整高度及外积尾界原样成立。第 8 节仍只需长度至多四的代数字母：周期只是其常数系数，不改变微分算子构造。

## 6. 真实高度与 Abel 函数的完整系数下界

设

$$
 \ell_p(n)=\lfloor\log_p n\rfloor\quad(n\ge1),\qquad \ell_p(0)=0.
\tag{699.28}
$$

若 $\rho$ 满足 (699.17)，逐项积分给

$$
 v_p\left([w^n]\int_0^w\rho\right)
       \ge a_\rho-v_p(n)\ge a_\rho-\ell_p(n).
\tag{699.29}
$$

若 $\rho,\sigma$ 均满足 (699.17)，则

$$
 v_p\left([w^n]\int_0^w\rho\int_0^{(\cdot)}\sigma\right)
       \ge a_\rho+a_\sigma-2\ell_p(n).
\tag{699.30}
$$

内积分分母的指数不超过 $n$，外积分分母为 $n$，所以此界控制全部卷积，没有略去高阶项。定义

$$
 A_i=\min\left\{
 a_{\gamma_i^0},
 \min_b(a_{\omega_{ib}}+a_{\eta_{ib}}),
 \min_j\bigl(v_p(c_{ij})+a_{\xi_j}\bigr)
 \right\}.
\tag{699.31}
$$

零项赋值为 $+\infty$。真实赋值可以换成已认证的更小有理下界。由 (699.21)，对所有 $n\ge1$，

$$
 \boxed{\quad
 v_p([z^n](\Lambda_i-d_i))
       \ge A_i-b_p n-2\ell_p(n).
 \quad}
\tag{699.32}
$$

换元损失恰为 $b_p n$，因为 $w=z/\lambda^3$，没有额外未知坐标变换。

取实际分量微分 $\varpi_i\in q^*H^0(A,\Omega^1)$，使

$$
 t_i=1+L_i^{-1}\int_{c_1}^x\varpi_i.
\tag{699.33}
$$

令 $a_i^{\rm Ab}$ 为 $\varpi_i$ 在 $w$ 盘上的 (699.17) 下界，置

$$
 T_i^{\rm bd}=\min\{0,a_i^{\rm Ab}-v_p(L_i)\}.
\tag{699.34}
$$

它只是赋值下界，不同于 (699.3) 的 $T_i$。对所有 $n\ge0$，

$$
 v_p([w^n]t_i)\ge T_i^{\rm bd}-\ell_p(n).
\tag{699.35}
$$

这保留了实际 CM 对数的分母损失；$L_i\ne0$ 不等于 $L_i$ 为单位。

## 7. 实际外积的统一斜率及有限尾证书

定义

$$
 B_i^V=2\min\{T_i^{\rm bd},T_g^{\rm bd}\},\qquad
 B_i^W=\min\{v_p(d_i)+2T_i^{\rm bd},A_i\},
\tag{699.36}
$$
$$
 A_{ij}^E=\min\{B_i^W+B_j^V,B_j^W+B_i^V\}.
\tag{699.37}
$$

由 $V_i(0)=W_i(0)=0$ 和 (699.32)–(699.35) 的系数卷积，对整个无穷级数有

$$
 \boxed{\quad
 v_p([z^n]E_{ij})\ge A_{ij}^E-b_p n-4\ell_p(n)
 \quad(n\ge1).
 \quad}
\tag{699.38}
$$

各乘积因子的指数不超过 $n$。两次单积分的乘积损失至多 $2\ell_p(n)$，高度二次积分与 $V$ 的乘积损失至多 $4\ell_p(n)$。这没有删除同靶低阶高度项。

对 $n\ge1$，$\ell_p(n)\le(n-1)/(p-1)$。故令

$$
 A'_{ij}=A_{ij}^E+\frac4{p-1},\qquad
 B_p=b_p+\frac4{p-1}=3+\frac{p+7}{p^2-1},
\tag{699.39}
$$

可得

$$
 v_p([z^n]E_{ij})\ge A'_{ij}-B_p n,\qquad
 B_p\le\frac{106}{35}<4\quad(p\ge41).
\tag{699.40}
$$

在较深子域 $v_p(z)\ge4$，完整尾的净线性增长至少 $34/35$。这是斜率的统一性；$A'_{ij}$ 仍含实际微分整格、规范常数、$\log_p\beta$ 及 $d_i$ 的赋值，本文未给与 $p$ 无关的下界。对 $v_p(z)=3$ 不能使用 $B_p<4$ 的线性放大；必须保留 (699.38) 的对数损失，下面另作完整处理。

**推论 699.5。** 设实际非零外积

$$
 E_{ij}(z)=\sum_{n\ge\nu}e_nz^n,\qquad e_\nu\ne0,
\tag{699.41}
$$

且已经精确证明更低系数全为零。若存在 $N>\nu$，使

$$
 v_p(e_n)+4(n-\nu)>v_p(e_\nu)\quad(\nu<n<N),
\tag{699.42}
$$
$$
 A'_{ij}+(4-B_p)N-4\nu>v_p(e_\nu),
\tag{699.43}
$$

则 $E_{ij}$ 在 $z\ne0,\ v_p(z)\ge4$ 上无零。

证明。对 $n\ge N$，(699.40) 和 (699.43) 给 $e_nz^n$ 的赋值严格大于 $e_\nu z^\nu$，且下界随 $n$ 增长。中间项由 (699.42) 处理。唯一最低赋值项不可能相消。$\square$

可用 (699.38) 获得更短截断，也可用同一证明把 $4$ 换为更深的 $s$。不能仅凭 $B_p<4$ 就断言 (699.42) 成立。

### 7.1 包含 $v_p(z)=3$ 边界的有限尾证书

令

$$
 c_p=3-b_p=\frac3{p+1},\qquad
 q_p(n)=c_p n-4\lfloor\log_p n\rfloor.
\tag{699.43a}
$$

在整数区间 $p^k\le n<p^{k+1}$ 内，$q_p(n)$ 严格递增。跳点上的差为

$$
 q_p(p^{k+1})-q_p(p^k)
   =\frac{3(p-1)p^k}{p+1}-4>0
   \qquad(k\ge1,\ p\ge41).
\tag{699.43b}
$$

因此对任意 $N\ge1$，若 $k_N=\lfloor\log_p N\rfloor$，有准确的下包络

$$
 \inf_{n\ge N}q_p(n)
 =Q_p(N):=\min\left\{
 \frac{3N}{p+1}-4k_N,\
 \frac{3p^{k_N+1}}{p+1}-4(k_N+1)
 \right\}.
\tag{699.43c}
$$

证明只需比较当前区间的左端 $N$ 与下一跳点；所有更后跳点由 (699.43b) 递增。特别，当 $N=p^K$、$K\ge1$ 时，

$$
 Q_p(p^K)=\frac{3p^K}{p+1}-4K\xrightarrow[K\to\infty]{}+\infty.
\tag{699.43d}
$$

**推论 699.5b（含边界的完整证书）。** 在 (699.41) 及其精确低阶消失前提下，若存在 $N>\nu$，使

$$
 v_p(e_n)+3(n-\nu)>v_p(e_\nu)
       \quad(\nu<n<N),
\tag{699.43e}
$$
$$
 A_{ij}^E+Q_p(N)-3\nu>v_p(e_\nu),
\tag{699.43f}
$$

则实际 $E_{ij}$ 在整个 $z\ne0,\ v_p(z)\ge3$ 上无零。可特别选 $N=p^K>\nu,\ K\ge1$，将 (699.43f) 化为

$$
 A_{ij}^E+\frac{3p^K}{p+1}-4K-3\nu>v_p(e_\nu).
\tag{699.43g}
$$

证明。由 (699.38)，对全部 $n\ge N$，
$$
 v_p(e_n)+3(n-\nu)
 \ge A_{ij}^E+q_p(n)-3\nu
 \ge A_{ij}^E+Q_p(N)-3\nu.
$$
结合有限中间项，首项在 $v_p(z)=3$ 严格占优；当 $v_p(z)>3$，每个相对差再增加 $(n-\nu)(v_p(z)-3)>0$，同样无零。$\square$

此证书的无限尾截断一定可选得有限，因为 (699.43d) 趋向无穷；有限中间项 (699.43e) 是否成立仍是实际计算问题。该边界估计只有正斜率 $3/(p+1)$，没有与 $p$ 无关的正下界，但不需要任何更强的系数整性假设。

## 8. 只依赖代数微分数据的有限首阶范围

取包含 (699.19)、(699.20)、(699.33) 中全部非零微分的有限字母表

$$
 \mathscr A=\{\rho_a=f_a(z)\,dz\},\qquad f_a\in K_0(X),
\tag{699.44}
$$

其中 $K_0$ 为有限数域；所有微分在 $c_1$ 正则。$D=d/dz$ 是 $K_0(X)$ 的代数导子。对字 $v$ 定义在 $c_1$ 归零的迭代积分 $I_v$，约定 $I_\varnothing=1$，于是

$$
 D I_{av}=f_aI_v.
\tag{699.45}
$$

shuffle 公式由乘积求导和基点值直接证明。$t_i$ 是常数加长度一积分，$\Lambda_i$ 是常数加长度至多二积分，故 $E_{ij}$ 是有限组长度至多四的 $I_v$ 的常数线性组合。系数可含实际 $d_i,c_{ij},L_i^{-1}$，字母却全是代数数据。

对每个所需字构造

$$
 \mathcal L_\varnothing=D,\qquad
 \mathcal L_{av}=\mathcal L_v\circ(f_a^{-1}D).
\tag{699.46}
$$

则 $\mathcal L_vI_v=0$，且非零算子阶数为 $|v|+1\le5$。当 $f_a(c_1)=0$ 时可有表观极点；以下允许这些极点。

在 $K_0(X)\langle D\rangle$ 中取这些算子的一个非零公共左倍数 $\mathcal L$。这只需有限线性代数：对阶数 $u,v$ 的两个算子，令左乘子阶数分别不超过 $v,u$，比较乘积系数，未知数比方程多一，得到非零公共左倍数，阶数不超过 $u+v$。微分算子环无零因子，故非平凡解不会给零乘积。递归即得

$$
 \mathcal L E_{ij}=0,\qquad
 \mathcal L=\sum_{j=0}^d a_j(z)D^j\ne0,\quad a_j\in K_0(X).
\tag{699.47}
$$

此算子无需任何规范高度常数的数值。

对非零 $a_j$，记

$$
 k_j=\operatorname{ord}_{c_1}a_j,\qquad
 a_j=a_{j,k_j}z^{k_j}+O(z^{k_j+1}),\qquad
 \mu=\min_j(k_j-j).
\tag{699.48}
$$

定义

$$
 \mathcal P_{\mathcal L}(T)=
 \sum_{k_j-j=\mu}a_{j,k_j}(T)_j,\qquad
 (T)_j=T(T-1)\cdots(T-j+1).
\tag{699.49}
$$

它非零，因为参与的最高 $j$ 给独有的最高次项。

**定理 699.6。** 令

$$
 \mathscr N_{ij}=
 \{n\in\mathbb Z_{\ge m+1}:\mathcal P_{\mathcal L}(n)=0\}.
\tag{699.50}
$$

在 (699.2) 下，实际 $E_{ij}$ 的首非零阶 $\nu$ 属于有限非空集 $\mathscr N_{ij}$。特别

$$
 \nu\le\max\mathscr N_{ij}.
\tag{699.51}
$$

证明。写 $E_{ij}=e_\nu z^\nu+O(z^{\nu+1})$，$e_\nu\ne0$。在 $\mathcal L E_{ij}$ 的 $z^{\nu+\mu}$ 系数中，更高的 $E_{ij}$ 系数不可能出现；该系数是

$$
 e_\nu\mathcal P_{\mathcal L}(\nu).
\tag{699.52}
$$

即使 $j>\nu$，下降阶乘为零也给正确贡献。由 (699.47)，$\mathcal P_{\mathcal L}(\nu)=0$，再用 (699.6)。R634 已给非恒零性，故集合非空。$\square$

算子、Laurent 首系数和整数根检查都只需有限代数输入。不必假定 $c_1$ 为算子的普通点或正则奇点。(699.51) 未给 $\nu$ 的实际值，更未决定 $v_p(e_\nu)$。只有有限精度近似时，较低系数“未见非零”不能代替精确消失证明；应用推论 699.5 必须另给这种证明或其他足够强的零点证书。

## 9. 收束后的输入与仍需进行的实际计算

在同一个 $X_1,c_1,q,\mathscr L_h,s_h$ 上，后续需要：

1. 代数的 $F$ 相容曲率、单极点第二类代表、$\gamma_i^0$，以及真实 $w$ 盘上的整性证书；
2. 实际 $L_i,d_i$ 及 (699.27) 所需的有限规范高度 jet；也可用 §5.1–§5.2 把自由高度常数降到 $g(Y)$，同时明确计算新增的固定第二类周期 (699.27j)；
3. 代数算子 (699.47)–(699.50) 给首阶有限候选集合；
4. 对真实首项及有限中间项作精确/有证误差计算；对完整 $v_p(z)\ge3$ 域用 (699.43e)–(699.43g) 覆盖无穷尾，对较深子域也可用 (699.40)。

这不是已经完成上述计算的声明。R697 的原 $M_2$ Cartier 平方根可进入 Abel 数据，不能直接放进 (699.24)–(699.25) 的实际 $\Gamma_i,d_i$，也不能替代 (699.2)。变化 $d$ 的商仍遵守 R597 的运输限制。本文未从固定 $p$ 的有限范围或收敛性推出绝对 Serre 一致性。

## 来源及准确使用范围

- A. Besser, J. S. Müller, P. Srinivasan, *p-adic adelic metrics and Quadratic Chabauty I*, arXiv:2112.03873 v4，<https://arxiv.org/pdf/2112.03873>。Proposition 3.5、Remark 3.6、§3.3.3（printed pp.15–16）给同曲率差与代数极部构造；§3.3.1 给迭代积分微分系统；§7.3.1（printed p.55）明确任意曲率原函数与规范高度之间的全纯积分差。非恒零性用 R634 已全面核对的 Theorem 7.9。
- 本仓库 R592 §4–§7：实际细 CM 盘、$\lambda$ 的绝对尺度、tame 商和真实 $j$ 公式。本文对高度另作第二类微分、规范差和整性证明，没有直接把其全纯微分尾界改称高度尾界。
- 本仓库 R616、R634、R682、R690、R694、R696：同一实际正秩前提、外积函数、任意共同 Abel 首阶和原候选零坏处靶值。


本仓库直接依赖：[R592](R592-actual-integral-CM-jet-lattice-and-complete-tail.md)、[R593](R593-actual-quotient-height-and-uniform-bad-place-support.md)、[R616](R616-original-CM-point-difference-and-explicit-height-basis.md)、[R634](R634-CM-calibration-eliminates-actual-height-matrix.md)、[R682](R682-common-CM-Abel-order-and-saturated-QC-jets.md)、[R690](R690-actual-two-adic-height-vanishes-via-full-level-cover.md)、[R694](R694-three-adic-elliptic-tail-model-and-actual-CM-zero-orbit.md)、[R696](R696-actual-global-CM-isomorphism-forces-zero-bad-height-target.md)。
