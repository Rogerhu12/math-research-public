# R475 — 真立方联合 normal 接口与三高轴的原首提升不可见区

日期：2026-11-14。**状态：已证明。** 本篇保同一个真实立方首核、同一个仿射修正 $R$ 和原 $M$。R459 在 **$J(P^{(2)})\in p^2\Gamma_L$ 这一较强提升条件下**的分支值与法向导数必须联立；该 $J$ 层联合必要类对 R468 的三个高轴逐点不变。单有整个 $M(P^{(2)})\in p^2\Gamma_{L+13}$ 时，前两块各十三条 carry 首次商必须另付，不能直接套用该类。独立于这一区分，在第三块接触有至少三阶余量时，三个高轴对这个真实首核的**整个原首 Bockstein** 都没有影响。这不需要参考 $J$ 可逆，也不需要原首像缺陷 $\gamma=0$。

第三块余量为零、一、二时，所有影响准确集中在最后三、二、一条原第三块行；给出单位三角式，并保原首像的商。这里没有把高轴不变性误说成三条完整中央条件没有算术内容，也没有从首提升不变性推第二次提升不变。

## 1. 保原来源、立方和完整三权参数

固定 $p=6s-1>83$、$1\le\ell<s-13$。原有限来源和完整目标均按 R459/R468 保留：
$$
L=2s+\ell,\qquad
M_z=c_*U_{0,z}m_{13}J_z,
\qquad
\Gamma_{L+13}=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^{\ell+13}\epsilon^2).
\tag{1}
$$
相对 Euler 算子记为 $\mathcal E$；在 $Y=\mathscr R$ 坐标为 $Y\partial_Y$，在原 $\Theta$ 坐标为 $(\Theta/17)\partial_\Theta$。总 charge 仍是 $\mathcal E_{\rm tot}=\mathcal E+40$。

取 R459 的实际来源
$$
\bar P=t^rF^3Q,\qquad r\ge1,\quad
F(0,1)=0,\quad F_\Theta(0,1)Q(0,1)\ne0,
$$
$$
h=\operatorname{ord}_wF(t(w),\bar\vartheta(w)),\qquad
k=2h+r-s\ge0,
\qquad k<\min(s-h,\ell,h).
\tag{2}
$$
在 $Y$ 坐标中以 $F_Y$ 替代 $F_\Theta$；两者的非零条件相同。按 R459，三个真实 Euler 值满足
$$
\operatorname{ord}P_0=r+3h=s+h+k,\qquad
\operatorname{ord}P_1=r+2h=s+k,\qquad
\operatorname{ord}P_2=r+h=s-h+k\ge\ell.
\tag{3}
$$
特别 $\bar P\in K_1(J)\subset K_1(M)$。式 (2) 是真实可读窗，不删除 $k<h$ 或任一 carry。

按 R468，改变高轴是
$$
g_z=g_\circ e^{\lambda_z(w)},\qquad
\lambda_z=w^{s-3}(u+vw+xw^2)+w^sH_z(w).
\tag{4}
$$
这里 $H_z$ 是完整原 $t$ 到 $w$ 换参尾，$a=p\kappa$ 保持原值。三个真正中央失败迫实际参数 $z_*$ 等于 R468 的唯一完整 Hensel 解；(4) 作为比较坐标使用，不赋予三个可自由选择的算术来源。

## 2. 三轴保同一个候选及联合必要类

由 $k<s-h$ 和 (2)，
$$
3h+r<2s,\qquad h<2s/3<s-3.
\tag{5}
$$
最后的不等式使用 $s\ge15$。因此 (4) 不改变 $F$ 的接触阶 $h$ 及其首系数。它也不改变 (3) 的三个阶，故同一个 $F,r,Q$ 在所有三个高轴下仍是同一个真实首核候选。

记 $\psi(t)$ 为 $F=0$、$\psi(0)=1$ 的正规分支。沿用 R459 的实际单位
$$
F(t(w),\bar\vartheta(w))=w^hu(w),\quad
e=(\mathcal EF)(t(w),\bar\vartheta(w)),\quad
C=(t(w)/w)^rQ(t(w),\bar\vartheta(w)).
$$
为免与高轴坐标 $u$ 混淆，以下将这三个首值记为
$u_F=u(0)$、$e_F=e(0)$、$C_F=C(0)$。
它们在 (4) 下均不变。

取任意实际来源提升 $P^{\rm base}$ 和因子系数提升，定义原仿射空间
$$
\mathcal A_P=\bar R^{\rm base}+\overline{\mathcal W},\qquad
R^{\rm base}=(P^{\rm base}-t^r\widetilde F^3\widetilde Q)/p.
\tag{6}
$$
它是同一个原格中的修正空间；既不除 $t^r$，也不把 $F$、$Q$ 自身加入来源。

以下保留 R459 §3 明示的附加条件 $J(P^{(2)})\in p^2\Gamma_L$，不以原 $M$ 的 $p^2$ 提升替代它。当 $r>2k$ 时，准确的 $J$ 层联合必要映射是
$$
\mathcal N_{h,k}(R)=
\left(
R(t(w),\psi(t(w)))\bmod w^{2h+k+1},
(\mathcal ER)(t(w),\psi(t(w)))\bmod w^{h+k+1}
\right).
\tag{7}
$$
同一个 $R\in\mathcal A_P$ 必须达到
$$
\boxed{\left(
-\frac{2C_Fu_F^4}{a e_F}w^{2h+k},
\frac{5C_Fu_F^3}{a}w^{h+k}
\right).}
\tag{8}
$$
因此真实联合必要类是 (8) 减去 $\mathcal N_{h,k}(R^{\rm base})$ 在
$\operatorname{coker}(\mathcal N_{h,k}|_{\overline{\mathcal W}})$ 中的类。

**定理 1。** 这个 $J$ 层完整联合必要类在三个高轴 (4) 下逐点不变。若 $r\le2k$，只保 R459 已付的导数分量，该类同样不变。原 $M$ 层是否有同样的必要类，须先支付两条十三行 carry 首次商；本定理不跨过该条件。

**证明。** 分支 $\psi$、原 $t(w)$、来源 $\mathcal W$ 和 (6) 均不随 (4) 改变；(5) 又使 (8) 的全部首值不变。故映射、仿射偏移、目标和余核中的类都相同。改变因子提升只令 $\bar R^{\rm base}$ 改变一个 $F^2$ 倍数，两个分量均为零，正是 R459 的准确提升不变性。$\square$

定理没有把两个分别可达的 jet 认作联立可达。R472 的单导数满射也不因此成为 (7) 的满射。

## 3. 原总 charge 后的准确首阶

剥下已经支付的 $w^{13}$ 后，将完整原 carrier 的正规单位记为 $A_0(w)$。R468 的 $W_i$ 因而是
$$
W_0=A_0P_0,\qquad
W_1=A_0(P_1+40P_0),\qquad
W_2=A_0(P_2+80P_1+1600P_0).
\tag{9}
$$
这里的 $A_0$ 包含原 $P_{134}/U_0$；只用其已付的原点单位性，没有在其他角点将它倒置。

由 (3) 得
$$
\boxed{\operatorname{ord}W_1=s+k\ge s,\qquad
\operatorname{ord}W_2=r+h.}
\tag{10}
$$
第二个式子的首项准确为
$$
\boxed{W_2=b_0w^{r+h}+\cdots,\qquad
b_0=6A_0(0)C_Fu_Fe_F^2\in k^\times.}
\tag{11}
$$
含 $P_1,P_0$ 的总 charge 项分别从 $s+k$、$s+h+k$ 开始，高于 $r+h$，故没有用相对 Euler 替换原总 charge。$p>83$ 保系数六为单位。

## 4. 完整原首 Bockstein 的不可见区

令
$$
\delta=r+h-\ell\ge0.
\tag{12}
$$
由于 $\bar M_z$ 对高轴相同，所有首 Bockstein 的靶均为同一个原 $C_1(M)$，可以直接比较。

**定理 2。** 若 $\delta\ge3$，则对同一个真实首核 $\bar P$ 有
$$
\boxed{\beta_1^{M_z}(\bar P)=\beta_1^{M_\circ}(\bar P)
\quad\text{对全部三个高轴成立。}}
\tag{13}
$$
这在取首像商之前已有相同的显示代表，不需要 $J_\circ$ 可逆或 $\gamma=0$。

**证明。** R468 的六条原边界只读取
$$
d_{1,i}=[w^{s-13+i}]W_1,\qquad
d_{2,i}=[w^{\ell+i}]W_2,\quad0\le i\le2.
$$
由 (10)，三条 $d_{1,i}$ 恒为零。若 $\delta\ge3$，三条 $d_{2,i}$ 也全部为零。将其代入 R468 式 (25)，完整变化即为零。原 $H_z$ 及其全部换参尾按 R468 已由真实首核端点消失；这里没有先删尾再取商。$\square$

特别，由 $r+2h\ge s$ 及 $r\ge1$，
$$
r+h\ge\lceil(s+1)/2\rceil.
$$
故准确的统一范围是
$$
\boxed{\ell\le\lceil(s+1)/2\rceil-3
\quad\Longrightarrow\quad (13).}
\tag{14}
$$
原 $\ell=1,2$ 窗在全部 $p>83$ 自动满足 (14)。因此即使这些窗中存在真实高 $b_F$、真实左右缺陷，不能只靠改变三个高轴使该立方候选的原首 Bockstein 发生变化。

## 5. 仅余的三、二、一条最高第三块行

当 $\delta<3$ 时，写
$$
W_2=w^{\ell+\delta}(b_0+b_1w+b_2w^2+\cdots),
$$
其中 $b_0$ 为 (11)。记 $e_j=\epsilon^2w^{\ell+10+j}$，$j=0,1,2$；它们是原完整目标中的行 $L+10+j$。
R468 的全部六条变化现在准确缩为
$$
\boxed{
\beta_1^{M_z}(P)-\beta_1^{M_\circ}(P)=
\begin{cases}
a\{u b_0e_0+(u b_1+v b_0)e_1+
(u b_2+v b_1+x b_0)e_2\},&\delta=0,\\
a\{u b_0e_1+(u b_1+v b_0)e_2\},&\delta=1,\\
a u b_0e_2,&\delta=2,
\end{cases}}
\tag{15}
$$
右端仍取在同一个原 $C_1(M)$ 中。

在显示的环境尾空间中，三种映射分别有秩三、二、一，其主块是以 $ab_0$ 为对角的三角矩阵。这是实际 cube 的单位首系数，不是抽象反模型。**通过原首像商之后秩可以下降，不能将环境秩当作可见 Bockstein 秩。** 每种情形必须继续检验对应尾向量在原像中的类。

式 (15) 保留了所有原十三行；并未以高轴只剩三条尾为理由删去另外十条原 carry，也没有改 $G_2=C_2(J)/\overline H$ 的定义。

## 6. 完整中央条件与下一位的准确边界

定理 1–2 是在固定其余原系数时，对高轴比较的严格不变性。三个完整中央失败仍约束这些其余系数与实际 $z_*$ 的关系：必须保 R468 全部三权、完整换参尾及三位 Hensel 等式。不能由高轴比较不变，推出这些全局实际等式没有约束。

同样，(13) 不证明第二 Bockstein 不变。原完整公式仍为
$$
\begin{aligned}
M_z=c_*U_{0,\circ}\{&m_{13}J_\circ+
p\epsilon(w^{10}P_2+w^{13}H_z)J_\circ\mathcal E_{\rm tot}\\
&+\frac{p^2\epsilon^2}{2}
(w^7P_2^2+2w^{10}P_2H_z+w^{13}H_z^2)
J_\circ\mathcal E_{\rm tot}^2\}\pmod{p^3},
\end{aligned}
\tag{16}
$$
其中 $P_2=u+vw+xw^2$。对真正首次提升 $P^{(2)}=P^{\rm base}+pR$，第一条含 $p$ 的项还会读到同一个 $R$；所有这些项必须在真实第二余核中再商去原首 Bockstein 像。

因此后续实际问题已缩得更准确：在 (14) 中，先将同一个 $R$ 的 $J$ 层法向条件连同两条十三行首次商恢复为真正 $M$ 层条件，再计算完整下一位；在余量零、一、二的窄带，先计算 (15) 在真实原首像中的类。没有将来源饱和当作物理像饱和，也没有从本篇推出 R418 的全量词预算或无穷素数非零。

## 7. 单个原来源的完整有限证书

[check-r475-cubic-three-axis-invisibility.py](../scripts/check-r475-cubic-three-axis-invisibility.py)
在 $p=239,s=40,D=40$ 使用真实四个电荷 $37,38,39,40$，构造
$\mathcal H_DY^{37}(Y-\rho_{<15}(t))^3$。
它的四个 canonical 多项式次数分别为 $46,32,15,2$，不超过原上界
$149,154,155,161$；真实接触是 $(r,h,k)=(10,15,0)$。
保整个 $P_{134}/U_0$、总 charge 四十及原 $t$ 高尾后，
$\ell=25,24,23,22$ 四个截断的变化恰为三、二、一、零条尾。
这是一条实际来源的一次恒等式核验，没有扫描素数，也没有为该来源声称任何中央零。
