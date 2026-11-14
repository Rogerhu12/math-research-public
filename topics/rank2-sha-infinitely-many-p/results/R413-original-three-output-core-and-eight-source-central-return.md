# R413 — 原三输入的完整总和 core、三正交输出与八来源整返回

日期：2026-11-14。**状态：已证明。** 本篇在 R399 的同一原三输入 $\nu_D\otimes\nu_L\otimes\nu_C$ 上，支付总输出 $W=x_1+x_2+x_3$ 的完整 core，保留另外两个独立连续输出；不是只对 $W$ 的边际重复已知 core。三个真正正交输出的整个 theta 格分别为 degree $72,216,8208$，相应固定整算子阶为二、二、四。原乘积来源进一步使第三算子的平方恰为负一，所以实际返回只需至多八条固定来源。完整三输出正则化及原三输入 primitive 除法均保持整。仍未将任何隐藏移动管赋成中央零。

## 1. 同一原三输入和真正整坐标

沿用 R399、R398 的 $E_b:y^2=x^3+b$，$b=17$，
$$
D=\sigma^{16}x^2(X+b),\quad
L=\sigma^{38}x(X^2+20bX-8b^2)Q_4(X),\quad
C=\sigma^{18}(X-8b)P_2(X),\quad X=x^3.
$$
原目标 $T=DLC$ 是已付的 $E_{24}$ 首项一来源。
令
$$
\rho=\nu_D\otimes\nu_L\otimes\nu_C,\qquad
Y=x_1+x_3,\quad Z=x_1+x_2,\quad W=x_1+x_2+x_3.
\tag{1}
$$
取 R407 的固定 ray（也可以取 R410 的子类），$p>19$，并按需要排除 $79$。
记
$$
\pi_{17}=\pi_{24}=-\pi_0,\quad
\lambda_0=\bar\pi_0^{-1},\quad\lambda=-\lambda_0,\quad
\kappa=p/\bar\pi_{17}^2,\quad\beta=\kappa/p=\lambda^2.
\tag{2}
$$

定义原总输出的两个正交伴随：
$$
R=x_1+x_2-3x_3,\qquad U=19x_1-8x_2,
$$
$$
\begin{pmatrix}W\\R\\U\end{pmatrix}
=M\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix},\qquad
M=\begin{pmatrix}1&1&1\\1&1&-3\\19&-8&0\end{pmatrix}.
\tag{3}
$$
准确有
$$
\det M=-108,\qquad
M\operatorname{diag}(16,38,18)M^{t}
=\operatorname{diag}(72,216,8208),
\tag{4}
$$
$$
M^{-1}=\begin{pmatrix}
2/9&2/27&1/27\\
19/36&19/108&-1/27\\
1/4&-1/4&0
\end{pmatrix}.
\tag{5}
$$
因此它是同一 $\mathbf Z_p^3$ 的整自同构，没有丢掉任何原输入。
特别“三个原输入全在 $p$ 内”等价于 $W,R,U$ 全在 $p$ 内。

## 2. 完整张量 theta 格，含整性

推前 $M_*\rho$ 的三个变量 Amice 来源是
$$
\boxed{
\mathcal H(z,r,u)
=D(z+r+19u)L(z+r-8u)C(z-3r).
}
\tag{6}
$$
它满足
$$
\boxed{
\mathcal H\in\mathcal S_{72}\boxtimes\mathcal S_{216}
                 \boxtimes\mathcal S_{8208},\qquad
\mathcal S_N=\sigma^N L(NO).
}
\tag{7}
$$

为完整说明 (7)，分别将 $z,r,u$ 加一个原格周期。三个输入的增量均是整数倍周期；$16,38,18$ 都是偶数，故三条原线丛的半特征乘积为一。准周期指数的对角项正是 (4)，三个交叉项分别为
$$
16+38-54=0,\qquad16\cdot19-38\cdot8=0,\qquad
16\cdot19-38\cdot8=0.
$$
所以没有剩余交叉 Gaussian 或平坦 twist。来源本身整条全纯，故确实是显示的三个外积线丛的全局截面，而不仅是逐个 Taylor 系数的形式猜测。外积线丛的全局截面就是相应有限维张量积。

(7) 在每个当前素数还是**整张量格**中的元素。具体地，每个偶 degree 的原基
$$
\{\sigma^Nx^i:0\le i\le N/2\}
\cup\{\sigma^Nyx^j:0\le j\le N/2-2\}
\tag{8}
$$
在正式群参数中的首阶互异，覆盖 $0,\ldots,N$ 中除 $N-1$ 外的阶，首系数为单位。三变量的 (6) 是原整 Amice 级数：三个线性输入分别对应整正式群变换，$M\in\operatorname{GL}_3(\mathbf Z_p)$，而原三测度整有界。
在 (8) 的张量基中按首阶逐次消元，就逐个得到整系数。这里用的是正式群／Amice 参数；没有通过除以大阶乘来证明整性。

## 3. 三个整个空间的绝对 core

对任意偶 $N$，使用 R300/R407 的同一个真实 division trace
$$
\mathscr M_a(\sigma^Nf)=\sigma^N
\operatorname{Tr}_{[a]}
 \left[(r_{\bar a}/r_a)^N f\circ[\bar a]\right],\qquad
r_a=\frac{\sigma(az)}{\sigma(z)^{Na}},
$$
$$
K_N=\frac{\bar\pi_{17}}p\mathscr M_{\pi_{17}}.
\tag{9}
$$
它保持完整 $\mathcal S_N$；原根单位平均及 (8) 的首阶消元证明它保持整格，并给
$$
\nu_F|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_{K_NF}.
\tag{10}
$$
这些都是完整测度式，适用于全部 tame 和所有奇偶部分。

原含中心 theta 交织为
$$
K_N\mathsf T_v=\mathsf T_{gv}K_N,\qquad
 g=\pi_0/\bar\pi_0\pmod{2N},\qquad
\mathsf T_{(1+N)v}=\mathsf T_v.
\tag{11}
$$
从同一个 R407 ray 直接作 CM 整数运算，得到
$$
\begin{array}{c|c|c}
N&g\pmod{2N}&\text{相应中心幂}\\ \hline
72&91+72\omega&g^2=73=1+72\pmod{144}\\
216&379+216\omega&g^2=217=1+216\pmod{432}\\
8208&13339+4104\omega&g^4=8209=1+8208\pmod{16416}
\end{array}
\tag{12}
$$
所有模数只使用原 ray 已固定的 $2,3,19$ 部分，没有另选随 $p$ 变化的角色。

完整 Heisenberg 表示不可约，故 (12) 先给对应算子幂为标量。以下用三个**真实非零锚**确定绝对标量：

- $N=72$：原 $T$ 的完整 core 给 $K_{72}T=T$。
- $N=216$：取 $\Theta(6\delta z)$，其中 $\Theta=x\sigma^2$，其 degree 为 $2N(6\delta)=216$。R316 的原 Theta core 为 $\lambda_0$；$6\delta$ 是当前普通嵌入的单位，所以与单位尺度推前交换，得到 $K_{216}\Theta(6\delta z)=-\Theta(6\delta z)$。
- $N=8208$：令 $\alpha=(3\delta)(4+\delta)$，$N\alpha=513$，取原两条 $D(\alpha z),H(\alpha z)$。R399 的原 $D,H$ core 是 $\lambda_0J$，且
  $$JD=\frac{\delta}{72b}H,\qquad JH=24b\delta D,\qquad J^2=-1.$$
  单位 $\alpha$ 的推前保这整个矩阵，故 $K_{8208}$ 在这两条实际锚上是 $-J$，其四次幂为一。

因此在**整个**显示空间上准确有
$$
\boxed{K_{72}^2=I,\qquad K_{216}^2=I,\qquad K_{8208}^4=I.}
\tag{13}
$$
原点质量为零的锚仍是非零全函数，故此处没有使用未知中央导数。

同一 (12) 和非零锚还证明三个算子在固定 theta 系数域上不随 $p$ 变化：两个素数的算子交织同一个有限 theta 群自同构，故只差标量，而显示锚的像固定了该标量。

### 3.1 总输出算子的明确固定 CM7 表达

令 $\gamma=3+\omega$、
$$N_{7,72}=\mathscr M_\gamma/(\omega\gamma)$$
作用于整个七十二维空间。R399 已付
$$
(\gamma/\bar\gamma)^9\equiv91+72\omega\pmod{144}.
$$
所以 $N_{7,72}^9$ 与 $K_{72}$ 交织同一个**完整含中心**自同构。
R398 对真实 $T$ 给 $\mathscr M_\gamma T=-\gamma T$，因此
$N_{7,72}^9T=-T$。由不可约性和非零锚，准确得到
$$
\boxed{K_{72}=-N_{7,72}^9.}
\tag{14}
$$
这不是只在旧十三维 type0 块中的身份。故下文新增总输出来源由同一个固定 CM7 trace 完全指定，没有留下绝对相位。

## 4. 真正保留两个隐藏坐标的总输出 core

在 (7) 中记
$$
K_W=K_{72}\otimes I\otimes I,\quad
K_R=I\otimes K_{216}\otimes I,\quad
K_U=I\otimes I\otimes K_{8208}.
\tag{15}
$$
它们整、可交换。定义
$$
\widetilde{\mathcal H}=K_W\mathcal H,\qquad
\widetilde\rho=(M^{-1})_*\nu_{\widetilde{\mathcal H}}.
$$
由 (10) 逐个张量列得到完整联合式
$$
\boxed{\rho|_{W\in p\mathbf Z_p}
=\lambda A_*\widetilde\rho,}
\tag{16}
$$
其中
$$
\boxed{
A=M^{-1}\operatorname{diag}(\kappa,1,1)M
=I+\frac{\kappa-1}{72}
\begin{pmatrix}16\\38\\18\end{pmatrix}
\begin{pmatrix}1&1&1\end{pmatrix}.
}
\tag{17}
$$
它逐个保留 $R,U$，将 $W$ 乘 $\kappa$，行列式为 $\kappa$。
其逆只在 $W\in p$ 的像上使用；不是全 $\mathbf Z_p^3$ 的整自同构。
$K_W^2=I$ 给准确第二次返回 $\widetilde{\widetilde\rho}=\rho$。

此外两个完整 $W$ 推前完全相同：
$$
\boxed{W_*\widetilde\rho=W_*\rho=\nu_T.}
\tag{18}
$$
因为设置 $r=u=0$ 时 $\mathcal H(z,0,0)=T(z)$，而 $K_{72}T=T$。
所以 $\rho-\widetilde\rho$ 是一个明确实际来源的完整 $W$ 推前核。
这里不额外声称这个差来源本身非零，也不据 (18) 将其受限叶域推前设零。

## 5. 原乘积 core 把十六列减少为至多八列

记 $K_{\mathrm{tot}}=K_WK_RK_U$，并对 (6) 定义
$$
\mathcal J\mathcal H(z,r,u)
=(JD)(z+r+19u)L(z+r-8u)C(z-3r).
$$
原三输入同时深的 core 是 $\lambda_0^3J$。由 (3) 的整可逆性，
该域就是三个新输出同时深的域。和 (10) 的三个完整输出 core 比较，得到
$$
\boxed{K_{\mathrm{tot}}\mathcal H=-\mathcal J\mathcal H.}
\tag{19}
$$
对同一个实际来源 $\mathcal J\mathcal H$ 再作相同比较，因 $J^2=-1$，有
$$
K_{\mathrm{tot}}\mathcal J\mathcal H=\mathcal H,\qquad
K_{\mathrm{tot}}^2\mathcal H=-\mathcal H.
$$
(13) 又给 $K_{\mathrm{tot}}^2=K_U^2$，因此
$$
\boxed{K_U^2\mathcal H=-\mathcal H.}
\tag{20}
$$
这条关系及其全部算子平移在实际子空间
$$
\mathcal V=\operatorname{span}\{
K_W^aK_R^bK_U^c\mathcal H: a,b,c\in\{0,1\}\}
\tag{21}
$$
上成立，因为三个算子可交换。于是 $\dim\mathcal V\le8$，
$K_W^2=K_R^2=I$、$K_U^2=-I$、$K_{\mathrm{tot}}^2=-I$ 在该空间上成立。
记 \( \mathcal V_{\mathcal O} \) 为 (21) 中八条实际来源的 \( \mathcal O \)-张成格；它由这些关系保持，且每条来源均整。没有把 $\mathcal J$ 对部分 core 的交换性当作额外假设；需要的两次等式直接来自原两个乘积来源的全深输入。

## 6. 全部真实三输出环带与整正则化

对 $F\in\mathcal V_{\mathcal O}$，令 $\nu_F$ 为三个新输出中的实际有界整测度。
全部深度准确满足
$$
\nu_F|_{W\in p^i,R\in p^j,U\in p^k}
=\lambda^{i+j+k}[\kappa^i,\kappa^j,\kappa^k]_*\nu_{K_W^iK_R^jK_U^kF}.
\tag{22}
$$
每条公式保留另外两个输出的全部连续测试；(22) 没有用三个边际代替联合。

令 $d=p-1$，$\chi_{\ell,u}(x)=\omega_p(x)^\ell\langle x\rangle^{du}$，
$\mathscr J_F(\mathbf u)$ 表示在 $W,R,U$ **全部为单位**的实际立方体上的三变量 Mellin 行。
先取 $|q_i|_p<1$，给真实输出赋值为 $(i,j,k)$ 的环带乘 $q_1^iq_2^jq_3^k$，使用各自的单位部分。这是定义在零轴为零的连续测试，故给真正收敛的积分 $\mathscr Z_F(\mathbf q;\mathbf u)$。
置
$$
A_i=q_i\lambda\omega_p(\beta)^{\ell_i}
                 \langle\beta\rangle^{du_i}.
$$
(20)–(22) 的三个整几何级数准确给
$$
\boxed{
\mathscr Z_F=
\frac{\displaystyle\sum_{a,b,c=0}^{1}
 A_1^aA_2^bA_3^c\,
 \mathscr J_{K_W^aK_R^bK_U^cF}(\mathbf u)}
 {(1-A_1^2)(1-A_2^2)(1+A_3^2)}.
}
\tag{23}
$$
符号 $1+A_3^2$ 来自真实 $K_U^2=-I$，不能改成另外两个轴的分母。

principal 分支上 $1-\lambda^2$、$1+\lambda^2$ 都为单位，
且 $\langle\beta\rangle^{du_i}\in1+p\mathcal O\langle u_i\rangle$。
因此 $q_1=q_2=q_3=1$ 给一个整 Tate 函数，三种取值顺序相同。
原八条来源和每条完整单位立方体都保留，没有把任意一个新来源认成第三条 rank-two 曲线。

## 7. 同一个原三输入 primitive 因子也可整消除

对任意 $F\in\mathcal V_{\mathcal O}$，把“原三个输入不全在 $p$ 内”的条件运输到 $(W,R,U)$；按 (3)，就是三个输出不全深。由 (22)，在真正收敛域已有
$$
\mathscr Z_F^{\rm prim}
=\mathscr Z_F-e\,\mathscr Z_{K_{\rm tot}F},\qquad
 e=\lambda^3q_1q_2q_3
 \omega_p(\beta)^{\ell_1+\ell_2+\ell_3}
 \langle\beta\rangle^{d(u_1+u_2+u_3)}.
\tag{24}
$$
这是同一个实际三输出族中的矩阵因子，不能换成标量 $1-\lambda^3$。
因为 $K_{\mathrm{tot}}^2=-I$ 在 $\mathcal V$ 上成立，准确逆是
$$
\boxed{
\mathscr Z_F=
\frac{\mathscr Z_F^{\rm prim}
      +e\,\mathscr Z_{K_{\mathrm{tot}}F}^{\rm prim}}
 {1+e^2}.
}
\tag{25}
$$
R410 在未细化的原 ray 上已经证明 $1\pm\lambda^6$ 为单位，
故 principal 正则化后 $1+e^2$ 是整 Tate 单位。
(25) 因而对整个实际来源向量保留任意中央 jet 理想和每一个 $p$ 精度；这个矩阵整逆不把单独一条 primitive 行的零等同于其未限制行的零。没有假定 $J'_S$ 或 $J'_T$ 非零。

## 8. Y/Z 移动管在新完整坐标中的准确位置

原观察没有被更换。从 (5) 直接有
$$
\boxed{
Z=\frac{3W+R}{4},\qquad
Y=\frac{51W-19R+4U}{108}.}
\tag{26}
$$
因此 R399 中的实际双碰撞域现在准确是
$$
\boxed{
\mathcal D_{N,N}
=\{W\text{ 为单位}, R+3W\in p^N, U+27W\in p^N\}.
}
\tag{27}
$$
证明是先用 $Z\in p^N$ 得 $R\equiv-3W$，再由 $Y\in p^N$ 得 $U\equiv-27W$；所有分母是当前素数的单位。反向代入立即成立。
这个域是两个明确的移动管，**不是** (23) 的三个原点单位轴。

若对 $W$ 的第 $r$ 个深层使用 (16)，其余条件完全按 (17) 运输：
$$
\boxed{
Y\circ A^r=Y+\frac{17}{36}(\kappa^r-1)W,\qquad
Z\circ A^r=Z+\frac34(\kappa^r-1)W.}
\tag{28}
$$
例如对任意连续 $\varphi(W,R,U)$ 和 $r,n,m\ge0$，
$$
\begin{aligned}
&\int_{W\in p^r,\,Y\in p^n,\,Z\in p^m}
              \varphi(W,R,U)\,d\rho\\
&=\lambda^r\int_{\substack{
Y+(17/36)(\kappa^r-1)W\in p^n\\
Z+(3/4)(\kappa^r-1)W\in p^m}}
 \varphi(\kappa^rW,R,U)\,
 d\rho^{(r)},
\end{aligned}
\tag{29}
$$
其中 $\rho^{(r)}=(M^{-1})_*\nu_{K_W^r\mathcal H}$，只在原两态之间变化。
指定精确 $W$ 环带时，再在右边保留 $W$ 为单位的相同条件即可。
没有删去任何由 (28) 产生的 moving-center 项。

## 9. 真正新增及仍需支付的条件

本篇已把原第三超平面 $W$ 接到**同一个完整联合**，并保其两个独立伴随输出；给出固定绝对算子 (14)、两态总和 core (16)、至多八来源的三轴整返回 (23) 和原三输入 primitive 的整逆 (25)。
原 R399 移动管在这个共同模型中的精确坐标是 (27)，其每一次总和 core 运输由 (28)–(29) 完整给出。

但是 (23) 的原点环带与 (27) 的移动管仍有区别。它们的比较不能只用矩阵可逆或整分母替代。尤其 $W_*\rho=W_*\widetilde\rho$ 不会自动给各移动管中的推前相等。
要由两条真实中央失败推出矛盾，仍需在本篇的固定实际八来源中支付这些移动管与全部补域的中央关系。
主目标没有完成；本篇也没有新增任何中央零假设。

### 直接依赖

R300 的整个偶 degree division trace、含中心交织及普通整性；
R316 的原 Theta 与 sigma core；R387/R396 的真实 $D,H$ 四次块；
R398 的实际 $T$ 与绝对 CM7 标量；R399 的同一三输入、完整原 core 和移动管；
R407 的原固定 ray 及整 tensor 方法；R410 的六次单位排除。

所有新坐标、域、绝对标量与八来源返回均在本文证明。没有调用新的未证中央非消失，也没有以有限样本推出无穷素数结论。
