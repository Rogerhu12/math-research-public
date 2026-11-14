# R448 — 保独立伴随的真实反射与完整 principal carry 行

日期：2026-11-14。**状态：已证明。** R445 的总输出算子在保留原
独立伴随 $U$ 的完整来源上，准确等于物理第一输出的普通反射：

$$
\boxed{\Psi_i=K_A\Phi_i=R_Y\Phi_i,\qquad U\text{ 固定}.}
$$

因此其 principal 行相同这一点可以保任意 $h(X,U)$，不必先忘掉
原 sigma 输入。本篇给这个反射在原三个输入上的真实矩阵、联合
carry 行及其整逆，并把 R441 非零管写成同一第二输出条件下的两条
不同深管。它没有将原 $J'_S=0$ 扩张成任意 $U$ 测试的中央零。

## 1. 同一个完整三变量来源的较小物理张量格

使用 R439、R443、R445 的同一固定 ray、周期、$b=17$ 和

$$
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad
\eta=\eta_{5,p}\in\{1,-1\},\qquad p>19.
\tag{1}
$$

原残余物理输入记为 $(Z,H)$，独立 sigma 输入仍为 $c$。原输出是

$$
W=Z+H,\quad Q=9Z-17H,\quad
Y=Z+c,\quad X=H-c,
$$
$$
A=Q+26c=9Y-17X,\qquad U=Q-280c.
\tag{2}
$$

令 $A_0=G_{16}R_{16,16}$，$A_1=D_-A_0$；第三态 $A_R=R_YA_1$
使用 R446。统一记 $i\in\{0,1,R\}$，其实际残余来源为

$$
\mathcal L_i^{\rm phys}(y,v)=\sigma(y+v)A_i(y,v),
\qquad A_i\in\mathcal S_{32}\boxtimes\mathcal S_{16}.
$$

在 R445 的生成函数中，换到物理生成变量
$y=w+9a,\ v=w-17a$，完整得到

$$
\boxed{\Phi_i(y,v,u)=
\sigma(y-v-280u)\sigma(y+v-8u)
A_i(y+9u,v-17u).}
\tag{3}
$$

这仍然是同一个三变量测度，$u$ 对偶于完整输出 $U$。
其 $Y/X$ degree 是 $34,18$；原 $U$ degree 仍为 $85680$。
全部三个交叉项准确是

$$
Y/X:\ -1+1=0,
$$
$$
Y/U:\ -280-8+32\cdot9=0,\qquad
X/U:\ 280-8-16\cdot17=0.
\tag{4}
$$

两个 sigma 在 $y$ 或 $v$ 的周期平移上的奇半特征互相抵消，
在 $u$ 方向的系数又都是偶数；$A_i$ 的两个 level 均为偶数。
因此没有平坦 twist，整个全纯来源属于

$$
\boxed{\Phi_i\in
\mathcal S_{34}\boxtimes\mathcal S_{18}\boxtimes\mathcal S_{85680}.}
\tag{5}
$$

原 Amice 级数整和正式群首阶基的整消元，进一步支付 (5) 的整
张量性。这里不从 $U$ 边际恢复联合，也不只检验有限 Taylor 阶数。

## 2. 完整总 A 核心确实就是保 U 的物理反射

在 (5) 上，R443 的两个 whole-space 核心可完整使用：

$$
K_Y=K_{34}=R_Y,\qquad K_X=K_{18}=-I.
\tag{6}
$$

原 $(Y,X)$ 与 $(W,A)$ 的矩阵行列式是 $-26$，$U$ 不变。
所以两个物理输出同时深与 $W,A$ 同时深是同一个整域。用同一
$\lambda^2$ 和共同缩放比较其完整核心，得到

$$
K_WK_A\Phi_i=-R_Y\Phi_i.
\tag{7}
$$

R431、R443 的整个 $W$ 算子，现逐个保 $U$ 系数，仍是

$$
K_W=\frac12\sum_{t\in E[2]}
                 T_t^{(34)}\otimes T_t^{(18)}\otimes I.
\tag{8}
$$

因为偶 degree 的规范二挠 lift 满足 $T_{-t}=T_t$，(8) 与 $R_Y$
交换。三个原来源的完整 $W$ 核心都已由 R439、R446 支付为
$K_W\Phi_i=-\Phi_i$；整个 $K_W^2=I$。所以 (7) 给

$$
\boxed{K_A\Phi_i=R_Y\Phi_i.}
\tag{9}
$$

这严格加强了只在 $u=0$ 上知道的反射式。它没有将
$\Phi_R$ 与 $R_Y\Phi_1$ 混同：后者是在整个三变量来源上反射，
前者则是固定 sigma 分裂下的第三残余来源；它们仅在忘却 $U$
后的对应边际相同。

## 3. 原三个输入上的准确反射

物理反射是

$$
(Y,X,U)\longmapsto(-Y,X,U).
$$

由 R445 的逆坐标，它在原 $(W,Q,c)$ 上准确为

$$
\boxed{\begin{aligned}
W'&=\frac{-4W-Q-26c}{13},\\
Q'&=\frac{-2380W+81Q-3640c}{221},\\
c'&=\frac{416c-17W-Q}{442}.
\end{aligned}}
\tag{10}
$$

所有分母在当前 $p>19$ 都为单位。该变换平方为一、行列式为负一，
并逐式保持 $X=(9W-Q)/26-c$ 与 $U=Q-280c$。
它一般不保持原 $c$ 单位条件、$Q$ 深条件或 $W$ 深条件。

特别

$$
W'=X-Y=:V.
\tag{11}
$$

所以 (9) 可保任何仅依赖 $X,U$ 的完整测试，但一个 $W$ 深条件
会变成 $V$ 深条件，不能随着反射被省略。

## 4. 全部 h(X,U) 的 principal 行和真实联合 carry

令 $d=p-1$。对连续 $h\in C(\mathbf Z_p^2,\mathcal O)$，定义

$$
\Gamma_i(z;h)=
\int\mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{dz}
             h(X,U)\,d\nu_{\Phi_i}.
\tag{12}
$$

$z$ 为原 principal 权参数。由 $\langle-Y\rangle=\langle Y\rangle$、
(9) 和 $X,U$ 不变，准确有

$$
\boxed{\Gamma_{\Psi_i}(z;h)=\Gamma_i(z;h)
\quad\text{对全部连续 }h(X,U).}
\tag{13}
$$

以下先取 R439 的原两态 $i=0,1$，其残余 $Q$ 核心互换。
原第一层单位 carry 是

$$
\mathscr B=\{Q,c\text{ 都单位},\ A=Q+26c\in p\}.
$$

保持 $U$，并只规范化确实深的 $A$，令

$$
\mathfrak b_i^{\,U}
 =(W,A/\kappa,U)_*
       (\mathbf1_{\mathscr B}\nu_{\Phi_i}).
$$

在其规范输出上，$Y'=(17W+A/\kappa)/26$、
$X'=(9W-A/\kappa)/26$。定义 $B_i(z;h)$ 为使用
$\mathbf1_{Y'\ {\rm unit}}\langle Y'\rangle^{dz}h(X',U)$ 的完整行。

R445 的三轴式在 $r=1$ 给

$$
\mathfrak b_i^{\,U}
 =\lambda\nu_{\Psi_i}
   +\eta\lambda^2[1,1,\kappa]_*\nu_{\Phi_{1-i}}.
\tag{14}
$$

由 (13)，其完整 principal 行是

$$
\boxed{B_i(z;h)=
\lambda\Gamma_i(z;h)
+\eta\lambda^2\Gamma_{1-i}(z;h(X,\kappa U)).}
\tag{15}
$$

这保留了原输入的独立伴随信息。它不是把 R442 的已忘却测度公式
直接附加一个隐藏条件。

### 4.1 第一层 carry 恰返回原伴随单位行

R445 的真实 $U$ 核心是
$K_U\Phi_i=-\eta\Psi_{1-i}$。在 (13) 的同一完整测试下，

$$
\Gamma_i|_{U\in p}
 =-\eta\lambda[1,\kappa]_*\Gamma_{1-i}.
\tag{16}
$$

这里把 (12) 视为 $(X,U)$ 上的有界测度，权参数仍全保。
因此 (15) 也可准确写成

$$
\boxed{B_i=\lambda\,\Gamma_i|_{U\ {\rm unit}}.}
\tag{17}
$$

原 carry 确实有 $U$ 单位，(17) 两侧支持相容。
这说明完整 joint principal carry 与原 $U$ 单位行之间没有额外
反射余项，但不把该行赋零。

### 4.2 联合两行的整逆不损失精度

在连续测试空间定义

$$
(\mathcal S h)(X,U)=h(X,\kappa U),\qquad
h_0(X,U)=h(X,0),\qquad t=\eta\lambda.
$$

则 (15) 的两行算子是

$$
\lambda\begin{pmatrix}I&t\mathcal S\\t\mathcal S&I\end{pmatrix}.
\tag{18}
$$

$1-\lambda^2$ 在当前 ray 为单位。以下给出
$I-\lambda^2\mathcal S^2$ 的完整整逆：

$$
\boxed{\mathcal R h=
\frac{h_0}{1-\lambda^2}
+\sum_{m\ge0}\lambda^{2m}
              \bigl(\mathcal S^{2m}h-h_0\bigr).}
\tag{19}
$$

由于 $h$ 在紧空间上均匀连续，$\mathcal S^{2m}h-h_0$ 一致趋于零。
非阿基米德范数下，(19) 因而在连续函数范数中收敛，且
$\|\mathcal R h\|\le\|h\|$。逐项望远镜相消严格给

$$
(I-\lambda^2\mathcal S^2)\mathcal R
=\mathcal R(I-\lambda^2\mathcal S^2)=I.
\tag{20}
$$

所以原联合行可由

$$
\boxed{\begin{aligned}
\Gamma_0(z;h)
 &=\lambda^{-1}
   \{B_0(z;\mathcal Rh)-tB_1(z;\mathcal S\mathcal Rh)\},\\
\Gamma_1(z;h)
 &=\lambda^{-1}
   \{B_1(z;\mathcal Rh)-tB_0(z;\mathcal S\mathcal Rh)\}
\end{aligned}}
\tag{21}
$$

完整整恢复。其对原中央求导也成立；这些算子不依赖 $z$。
本证明使用测试函数的范数收敛，不声称缩放测度向 $U=0$ 的
Dirac 测度在测度范数中收敛。

若 $h$ 不含 $U$，则 $\mathcal Sh=h$，
$\mathcal Rh=h/(1-\lambda^2)$，(21) 正好还原 R442 的单位矩阵。
若 $h$ 支持于 $U$ 单位，则 $\mathcal Sh=0$，
(15) 简化为 $B_i(z;h)=\lambda\Gamma_i(z;h)$。

## 5. 原非零域在同一第二输出条件下的两条深管

由 (2)，准确有

$$
Q=(1260W-3640X+13U)/153,\qquad
c=(9W-26X-U)/306.
\tag{22}
$$

取 $n\ge1$。R441 的原域
$\mathscr D_n=\{W,Q\in p^n,\ c\text{ 单位}\}$ 因而等价于

$$
\boxed{\mathscr D_n=
\{X\text{ 单位},\ W\in p^n,\ U-280X\in p^n\}.}
\tag{23}
$$

确实，在 $W\in p^n$ 下，$Q\in p^n$ 等价于最后一个条件，
继而 $c\equiv-X\pmod p$。反射 (10) 则给

$$
\boxed{R_Y\mathscr D_n=
\{X\text{ 单位},\ V\in p^n,\ U-280X\in p^n\}.}
\tag{24}
$$

所以两管共享同一个完全合法的第二输出条件

$$
h_n(X,U)=\mathbf1_{X\ {\rm unit}}\,
          \mathbf1_{U-280X\in p^n}X^6.
\tag{25}
$$

这个条件支持于 $U$ 单位，故 $\mathcal S h_n=0$。由 (15)，

$$
\boxed{B_i(z;h_n)=\lambda\Gamma_i(z;h_n).}
\tag{26}
$$

这仍是未插入 $W$ 或 $V$ 深条件的完整行。
在 $\mathbf1_{Y\ {\rm unit}}h_n$ 的支持上，$W$ 深和 $V$ 深两管
不交：若两者都在 $p$ 内，则 $2Y=W-V$ 非单位，矛盾。

对任意态 $i$，设 $\Gamma'_{i,W^n}(h_n)$、
$\Gamma'_{i,V^n}(h_n)$ 分别为这些真实深管上的中央导数。由 (13)
所用的完整反射，准确有

$$
\boxed{\int\mathbf1_{W\in p^n}
\mathbf1_{Y\ {\rm unit}}d\log_p\langle Y\rangle h_n\,d\nu_{\Psi_i}
=\Gamma'_{i,V^n}(h_n).}
\tag{27}
$$

特别 $i=0$ 时，(23) 的同一原值由 R441 已证

$$
v_p\bigl(\Gamma'_{0,W^n}(h_n)\bigr)=5n
\qquad(n>0\text{ 偶数}).
\tag{28}
$$

(27) 把它准确放到反射来源的另一管上，没有使两管在同一来源中
自动相等，也没有删掉 $W,V$ 都为单位的其余部分。

## 6. 原算术中央控制的准确边界

对于不含 $U$ 的完整 $h(X)$，原来源 $\Phi_0$ 忘却 $U$ 后就是
$\mathcal K_0$，所以

$$
\Gamma_0(z;h(X))
 =-\frac23J_S(z)\int h\,d\nu_{G_{18}}.
\tag{29}
$$

因此原 $J'_S(0)=0$ 确实控制所有这些完整行。
本篇 (13)、(15)、(21) 允许保留 $U$ 并准确追踪来源，却没有把
(29) 的右侧公式自动扩大到任意 $h(X,U)$。

对特别的 (25)，还有真实不交分拆

$$
\Gamma'_0(h_n)
=\Gamma'_{0,W^n}(h_n)+\Gamma'_{0,V^n}(h_n)
 +\Gamma'_{0,\{W,V\notin p^n\}}(h_n).
\tag{30}
$$

原 (28) 仅控制第一项；其余两项和完整左侧仍须从实际原来源支付。
R445 的两层运输也仍保留 (23) 的内部条件。后续的目标是将这些
明确的 joint 行接回原算术来源，或控制其补域，而不是把“可合法
测试”改写成“这个测试已知为零”。主目标未完成。

## 依赖

- [R431：完整总和核心及正交双输出](R431-original-degree52-full-core-and-fixed-thirteen-ray.md)。
- [R439：原残余两态及完整核心](R439-original-residual-companion-two-state-core-and-exact-depth-comparison.md)。
- [R443：整个 degree34/18 核心](R443-original-residual-quarter-source-and-complete-central-return.md)。
- [R445：保 sigma 的完整三坐标、四态及真实两层管](R445-original-sigma-retained-three-coordinate-core-and-four-state-carry.md)。
- [R446：第三残余态及其真实 W 核心](R446-original-three-state-quarter-closure-and-one-layer-full-carry.md)。
- [R441：同一原深管的精确非零值](R441-original-sixth-moment-row-and-uniform-same-depth-nonvanishing.md)。
