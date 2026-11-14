# R482 — 原二输出的完整五十一维来源空间与整伴随矩提取

日期：2026-11-14。**状态：已证明。** R474、R477 的同一个真实
二输入在第一轴恰好张满一个 $51$ 维空间。这是整个 theta
空间中的结论：上界来自完整二挠、四挠平移的两个约束，下界
由六个固定的非零有理行列式达到。全部来源均可由次数不超过
$53$ 的真实伴随多项式测试提取；principal 部分只需次数
$0,6,\ldots,42$。原五伴随八维块因而有一个完整来源提取接口。
此结论不把任何未投影中央导数宣称为零，主目标仍未完成。

## 1. 保留原二输入及两个输出

仍取原 $b=17$、同一个普通周期 $\Omega_p$，并沿用
$$
F(z)=\sigma(z)^4\sigma(2z)\sigma(8z),\qquad
H(z)=\Theta(z)^2,\qquad U(z)=H(4z).
\tag{1}
$$
原物理输入 $A,D$ 和真正输出为
$$
W=A+4D,\qquad V=2A-9D,\qquad
\widetilde\Phi(w,v)=F(w+2v)H(4w-9v).
\tag{2}
$$
这是 R477 的整个
$\mathcal S_{136}\boxtimes\mathcal S_{612}$ 来源。为使用较小的
原除法多项式，固定计算采用 $v=4q$：
$$
\Phi(w,q)=\widetilde\Phi(w,4q)
 =F(w+8q)U(w-9q)
 \in\mathcal S_{136}\boxtimes\mathcal S_{9792}.
\tag{3}
$$
两套伴随系数只相差 $4^j$，没有改变原物理 $V$。

记第一轴的完整对称平移为
$$
(T_t^{(N)}G)(w)
=\exp\{-N\eta_t(w+t/2)\}G(w+t).
$$
在整个 $\mathcal S_{136}$ 上定义
$$
B_2=\frac12\sum_{t\in E[2]}T_t^{(136)}-I,\qquad
K_4=\frac14\sum_{t\in E[4]}T_t^{(136)}
       -\frac12\sum_{t\in E[2]}T_t^{(136)}.
\tag{4}
$$
这里 $K_4$ 的下标表示四挠算子。**它不是另给整个
degree136 空间一个普通核心公式**；该空间已付的普通核心
仍是 R474 的 $K_{136}=RB_2$。

## 2. 两个完整约束及准确维数

取标准 $136$ 维 Schrödinger 基 $e_j$，下标模 $136$。
与 R416 相同的绝对中心规范给
$$
T_{(s+r\omega)/4}^{(136)}e_j
  =i^{\,s(j+r)}e_{j+34r},
 \qquad 0\le r,s<4.
\tag{5}
$$
因为 $136/4\equiv2\pmod4$，此处的中心指数与 R416 中
$72/4\equiv2\pmod4$ 的规范一致。直接对 $s,r$ 求和得
$$
\boxed{
B_2e_j=(-1)^j e_{69j+68},\qquad
K_4e_j=-(-1)^j e_{35j+68}.}
\tag{6}
$$
因此 $B_2^2=K_4^2=I$，两者交换，且
$$
\operatorname{tr}B_2=-68,\qquad
\operatorname{tr}K_4=-34,\qquad
\operatorname{tr}(B_2K_4)=-34.
\tag{7}
$$
例如 $B_2$ 的不动下标恰为全部奇数，$K_4$ 的不动下标为
$j\equiv2\pmod4$；乘积准确为 $-e_{103j}$。故
$$
\mathcal H_{51}:=\ker(B_2+I)\cap\ker(K_4+I)
\tag{8}
$$
满足
$$
\boxed{\dim\mathcal H_{51}
=\frac{136-\operatorname{tr}B_2-\operatorname{tr}K_4
                   +\operatorname{tr}(B_2K_4)}4=51.}
\tag{9}
$$

现在检查原来源，而非只检查同维空间。R474 已证明
$\sum_{E[2]}T_t^{(72)}F=0$，且 $U=[4]^*H$ 在所有规范
$E[4]$ 平移下不变。由于
$$
72\cdot8+64\cdot(-9)=0,
$$
第一轴平移在 (3) 中逐项分解为两个输入的标准平移；没有
残留 $q$ 的指数交叉项。所以
$$
(B_{2,W}\otimes I)\Phi=-\Phi.
\tag{10}
$$
R416、R474 又已在原 $F$ 上给出完整四挠核心式
$$
\left(\frac14\sum_{E[4]}T_t^{(72)}
       -\frac12\sum_{E[2]}T_t^{(72)}\right)F=-F.
$$
同一个分解及 $U$ 的四挠不变性遂给
$$
\boxed{(K_{4,W}\otimes I)\Phi=-\Phi.}
\tag{11}
$$
因此原二输出的每一个完整伴随系数均属于 $\mathcal H_{51}$。
式 (9) 是全部伴随次数共同的上界，并非在一个截断内观察到
秩不再增加后作出的推断。

## 3. 六个固定非零 minor 达到整个上界

在 $b=1$ 上用原 Weierstrass 坐标
$$
y^2=x^3+1,\qquad D x=2y,\quad D y=3x^2
\tag{12}
$$
计算。整个 $\mathcal S_{136}$ 有标准代数基
$$
\{\sigma^{136}x^i:0\le i\le68\}
\ \cup\
\{\sigma^{136}yx^i:0\le i\le66\}.
\tag{13}
$$
R471 的固定除法多项式给
$F=\sigma^{72}f(x)$、$U=\sigma^{64}u(x)$。由两个线性
$\zeta(w)$ 项相消，准确的全函数展开为
$$
\begin{aligned}
\frac{\Phi(w,q)}{\sigma(w)^{136}}
={}&f(x(w+8q))\,u(x(w-9q))\\
&\times\exp\left\{-\sum_{j\ge2}
\frac{72\,8^j+64(-9)^j}{j!}\,
D^{j-2}x(w)\,q^j\right\}.
\end{aligned}
\tag{14}
$$
每一阶都在 $\mathbf Q[x,y]/(y^2-x^3-1)$ 中准确运算。
式 (14) 给的是 (13) 中的整个第一轴系数，不是第一轴
原点的有限 jet。由 (3) 的极化，该系数自动具有 (13)
规定的全局极点界。

令 $C_j(w)=[q^j]\Phi(w,q)$。同时角特征为
$$
\Phi(\zeta w,\zeta q)=\Phi(w,q),\qquad
C_j(\zeta w)=\zeta^{-j}C_j(w)\quad(\zeta\in\mu_6).
\tag{15}
$$
于是 $j$ 偶时只含 $y$ 次数 $0$，奇时只含 $y$ 次数 $1$；
若该次数为 $\epsilon$，准确的 $x^i$ 同余是
$$
2i+3\epsilon\equiv4+j\pmod6.
\tag{16}
$$
附脚本按这六个互异角特征分别计算整列，所得非零方阵为：

| $j\bmod6$ | 选取的完整伴随次数 | 方阵阶数 |
|---|---|---|
| $0$ | $0,6,12,18,24,30,36,42$ | $8$ |
| $1$ | $1,7,13,19,25,31,37,43,49$ | $9$ |
| $2$ | $2,8,14,20,26,32,38,44$ | $8$ |
| $3$ | $3,9,15,21,27,33,39,45,51$ | $9$ |
| $4$ | $4,10,16,22,28,34,40,46$ | $8$ |
| $5$ | $5,11,17,23,29,35,41,47,53$ | $9$ |

各方阵取 (16) 允许的 $x$ 指数从小到大的前 $8$ 或 $9$
行；它们的全部有理条目和非零行列式均在 JSON 中明确保存。
脚本还保存至 $j=101$ 的原全坐标，但本命题只用表中
$51$ 列及六个非零行列式。由角特征不同，这 $51$ 列独立。
结合 (9)–(11) 即得
$$
\boxed{\operatorname{span}\{C_j:j\ge0\}=\mathcal H_{51}.}
\tag{17}
$$
特别其六个角特征空间维数准确为 $8,9,8,9,8,9$。
这一步是有限维全局 theta 恒等式的有理证书，不使用目标
素数扫描，也不以有限个中央值代替无穷性。

## 4. 固定坏集以外的整左逆

令 $\Delta$ 为一个固定非零整数，其素因子包含：
六个选定方阵全部条目的分母、六个非零行列式的分子、
$2\cdot3\cdot17\cdot53!$，以及此前原来源的固定坏集。
这些数由上表和附数据完全定义，无须猜测一个随 $p$ 改变
的矩阵。允许把 $\Delta$ 换成这些明确整数的乘积。

现在在 $b=17$ 返回原曲线。由
$$
\sigma_b(z)=b^{-1/6}\sigma_1(b^{1/6}z),\quad
x_b(z)=b^{1/3}x_1(b^{1/6}z),\quad
y_b(z)=b^{1/2}y_1(b^{1/6}z)
$$
及 (1)，第 $j$ 列的 $\sigma^{136}x^iy^\epsilon$ 系数
准确乘
$$
b^{(j+130-2i-3\epsilon)/6}.
\tag{18}
$$
(16) 保证指数为整数。在每个固定角特征块，(18) 分为
行因子与列因子；因为 $b$ 为单位，不引入新的非固定坏集。
从 $q$ 改回 $v$ 再把第 $j$ 列乘 $4^{-j}$，同样是单位。

记
$$
G_j(w)=[v^j]\widetilde\Phi(w,v)=4^{-j}C_j(w).
\tag{19}
$$
在 $\mathbf Z[\omega,\Delta^{-1}]$ 上，对任意落在 (8)
中的整 theta 系数向量 $G$，取各角特征的指定行并反演相应
方阵，得到唯一的整系数 $c_j(G)$，满足
$$
\boxed{G=\sum_{j\in\mathcal J}c_j(G)G_j,\qquad
\max\mathcal J=53.}
\tag{20}
$$
完整系数相等的理由是 (17)：指定行在各已知维数空间上
已经是同构，未选的行不能再增加一个自由误差。
这也给一个固定的线性左逆，复系数范数由固定常数控制。
在任意 $p\nmid\Delta$ 处，该左逆是整的，系数上确界范数
不增加。当前原 ray 中 $p\ge71$，所以所用阶乘本来就是
单位；删去其余固定有限坏集仍不改变无穷素数集的可用性。

## 5. 实际伴随多项式测试与全部第一轴条件

采用原 Amice 规范
$$
\widetilde\Phi(w,v)
=\int\exp\{(wW+vV)/\Omega_p\}\,
       d\nu_{\widetilde\Phi}(W,V).
\tag{21}
$$
这只是将
$\widetilde\Phi(\Omega_p\log(1+T_1),
\Omega_p\log(1+T_2))$
写成两个实际物理变量的 Laplace 形式。于是
$$
\nu_{G_j}
=\frac1{j!\Omega_p^j}
  (\operatorname{pr}_W)_*(V^j\nu_{\widetilde\Phi}).
\tag{22}
$$
对 (20) 中的 $G$，定义真实伴随测试
$$
\boxed{h_G(V)=\sum_{j\in\mathcal J}
       \frac{c_j(G)}{j!\Omega_p^j}\,V^j.}
\tag{23}
$$
得到整个测度恒等式
$$
\boxed{(\operatorname{pr}_W)_*
       (h_G(V)\nu_{\widetilde\Phi})=\nu_G.}
\tag{24}
$$
周期是同一个 $\Omega_p$；若使用 JSON 中的 $q$ 列系数
$a_j$，须取 $c_j=4^ja_j$，不能漏掉这一固定因子。

因此 (24) 保任意积分已定义的第一轴测试。尤其
$$
\int_{\{W\ {\rm unit}\}}\langle W\rangle^{du}h_G(V)
       \,d\nu_{\widetilde\Phi}
=J_G(u),\qquad d=p-1.
\tag{25}
$$
同一恒等式可以与独立旧伴随测度张量，再使用任意联合
紧开条件或连续测试。这一说法来自完整推前相等，不是从
总质量比推出隐藏域相等。若测试还涉及新的 $V$，就须
继续保留 (23) 的真实权，不能先将 $V$ 忘掉再恢复。

在 $p\nmid\Delta$ 处，$\Omega_p$ 为原单位周期，
$V\in\mathbf Z_p$，故 (23) 是整有界测试。它只有固定
次数 $53$；本提取步骤没有引入一个随 $p$ 或原来源次数
增长的次数成本。

## 6. 原八维 principal 块的准确位置及适用边界

$N_7,N_{19}$ 的完整交织置换原 $E[2]$、$E[4]$ 平移，
所以保 (8)。由 $W_*=-111\Phi(w,0)/280$，原七条
$N_7^jW_*$ 均在 $\mathcal H_{51}$。R480 又给
$$
P_{{\rm ref},W}\widetilde\Phi_i
=H_{\rm ref}(w)B_i(v),\qquad B_i(0)=\pm2/(27b)\ne0.
$$
因原投影也保 (8)，可知 $H_{\rm ref}\in\mathcal H_{51}$。
R476 的这八条完整第一轴来源独立，而 (17) 的 principal
维数恰为八。因此
$$
\boxed{
\Pi_0\mathcal H_{51}
=\operatorname{span}\{H_{\rm ref},W_*,N_7W_*,
                 \ldots,N_7^6W_*\}.}
\tag{26}
$$
这识别实际来源本身，不靠另一个 Schrödinger 算子与 CM
算子之间尚未确定的比例。对这八条来源，(23) 只需
$j=0,6,\ldots,42$。于是 R476 原五伴随分解的每一项均有
一个真实伴随矩提取，且所有旧伴随保持。

两个边界必须同时保留。第一，(25) 为每条 $G$ 给出它自己
的 $J_G$；它不由 $J_{\rm new}'(0)=0$ 推出其余 $50$ 维
的中央导数为零。特别 R480 的 $H_{\rm ref}$ 真实质量和
未知导数仍在。第二，(23) 对新 $V$ 加了实际多项式权；
这不自动保一个未证明的 $V$ 核心或旧混合管的核心。
R476 的标准 theta lift、其全极化和 R465 原 $W_t$ 的
条件运输仍须按真实来源逐项处理。

## 7. 来源和精确证书

- [固定全坐标与六个非零 minor 的脚本](../scripts/check-r482-complete-two-output-companion-span.py)。
- [六块有理矩阵、选定列、选定行及全部行列式](../scripts/check-r482-complete-two-output-companion-span.json)。
- [R416：完整四挠平移与绝对核心](R416-original-four-torsion-core-and-exact-second-state-marginals.md)（四挠规范见该证明）。
- [R471：原六 sigma 与 norm-two 因式](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)。
- [R474：原二输出与完整 E2 核心](R474-original-six-sigma-two-output-core-and-exact-riemann-domains.md)。
- [R476：完整八维来源基](R476-original-complete-xi-normtwo-bridge-and-integral-eight-source-basis.md)。
- [R477：真实 degree612 伴随](R477-original-new-line-and-complete-degree612-companion.md)。
- [R480：同时 CM 转伴随和两条算术行](R480-original-simultaneous-cm-companion-transfer-and-two-arithmetic-rows.md)。
