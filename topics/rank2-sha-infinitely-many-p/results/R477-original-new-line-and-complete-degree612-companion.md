# R477 — 新算术线在原六 sigma 二输出中的完整伴随与单位条件行

日期：2026-11-14。**状态：已证明。** 对 R474 的同一个原压缩
二输入，完整第一轴算术投影准确分离出
$S_{\rm new}\otimes\Lambda_{612}$。伴随质量为 $5824/3$，
有真实 scalar core $\lambda$；其全测度与单位限制都是整
卷积单位。本篇由此支付带任意完整伴随测试的原新曲线中央行，
并写清反卷积对两个原压缩输入条件的真实转置。没有将投影后
的域与投影前的独立六 sigma 隐藏事件等同。主目标仍未完成。

## 1. 同一二输入的实际四倍下降

沿用 R471、R474 的 $b=17$、共同物理周期和
$$
F=\sigma^4\sigma(2z)\sigma(8z)\in\mathcal S_{72},\qquad
H=\Theta^2\in\mathcal S_4,
$$
$$
\lambda=-\bar\pi_0^{-1},\qquad
\beta=-\lambda,\qquad \kappa=p/\bar\pi_0^2,\qquad d=p-1.
\tag{1}
$$
令 $A$ 是原六 sigma 的总输出，$D=t_1+t_2$ 是两个原
Theta 的总输出。这里 $H$ 的测度为
$\nu_\Theta*\nu_\Theta$，仍保与两个独立输入之间的推前方向。

取真实输出
$$
W=A+4D,\qquad V=2A-9D,\qquad
T=\begin{pmatrix}1&4\\2&-9\end{pmatrix},\quad\det T=-17.
\tag{2}
$$
其完整来源为
$$
\widetilde\Phi(w,v)=F(w+2v)\Theta(4w-9v)^2.
\tag{3}
$$
极化准确满足
$$
T\begin{pmatrix}72&0\\0&4\end{pmatrix}T^t
=\begin{pmatrix}136&0\\0&612\end{pmatrix},
\qquad
\widetilde\Phi\in\mathcal S_{136}\boxtimes\mathcal S_{612}.
\tag{4}
$$
所有指数与半特征都是原标准规范：两次数偶，交叉项
$72\cdot2+4\cdot4(-9)=0$。没有删掉一个有理平坦 twist。
R474 的 $B=4D$、$Q=8A-9B$ 正是 $Q=4V$，并且
$$
\Phi(w,q)=\widetilde\Phi(w,4q).
\tag{5}
$$
这给原 degree9792 伴随方向的**真实四倍下降**，不是仅对
有限个 Taylor 系数重新命名变量。

记 $\widetilde\nu_0=T_*(\nu_F\otimes\nu_H)$，
$\widetilde\Psi=R_W\widetilde\Phi=R_V\widetilde\Phi$，
$\widetilde\nu_1=\nu_{\widetilde\Psi}$。R474 的两个完整核心在
尺度四的单位坐标变换下原样成为
$$
\widetilde\nu_i|_{W\in p\mathbf Z_p}
 =\beta[\kappa,1]_*\widetilde\nu_{1-i},\qquad
\widetilde\nu_i|_{V\in p\mathbf Z_p}
 =\lambda[1,\kappa]_*\widetilde\nu_{1-i}.
\tag{6}
$$
同样，所有 $n,m\ge0$ 的完整双深度身份仍保两个输出及相应
测试的缩放。

## 2. 整个第一轴的真实 rank-one 算术投影

在整个 $\mathcal S_{136}$ 上先取原 geometric principal 投影
$$
\Pi_0G(w)=\frac16\sum_{\zeta\in\mu_6}G(\zeta w).
$$
R466、R470 给 principal 二十三维空间上的完整算子
$N_7=\mathscr M_{\gamma_7}/\gamma_7$、
$N_{19}=\mathscr M_{\gamma_{19}}/\gamma_{19}$。原规范为
$\gamma_7=(5+\delta)/2$、$\gamma_{19}=4+\delta$。
定义
$$
E_{\omega^2}
 =\frac1{18}\sum_{j=0}^{17}\omega^{-2j}N_7^j,\qquad
\boxed{P=\frac{I-\omega N_{19}}2\,E_{\omega^2}\Pi_0.}
\tag{7}
$$
(7) 的 $N_{19}$ 因子只作用于已选的 $N_7=\omega^2$ 空间。
在该空间，R466 的完整中心身份
$N_{19}=\omega D_{33}N_7^2$ 给
$D_{33}=\omega N_{19}$，所以该因子正是 $(I-D_{33})/2$。

R466 已支付相应的整个有限角色及曲线身份，R470 支付完整
来源投影；因此
$$
P^2=P,\qquad \operatorname{rank}P=1,\qquad
\operatorname{im}P=\langle S_{\rm new}\rangle,\qquad
S_{\rm new}(w)=w^6+O(w^{12}).
\tag{8}
$$
这里 $S_{\rm new}$ 是实际固定曲线 $E_{2312}:y^2=x^3+2312$
在共同 $b=17$ 框中的来源；曲线秩二及普通、惰性桥分别见
R466、R469。它不是由本篇某个零质量判据新认定的曲线。

在当前 $p>19$、$p\ge71$ 的 ray 上，(7) 的全部分母及两个
prime-to-$p$ CM trace 规范是单位。故 $P$ 保持原整 theta 格。
它在**完整二变量来源的第一轴**作用，而非只对 $v=0$ 的
边际作用。由于 (8)，存在唯一实际全纯来源
$\Lambda\in\mathcal S_{612}$ 使
$$
\boxed{
P_W\widetilde\Phi(w,v)
 =P_W\widetilde\Psi(w,v)
 =S_{\rm new}(w)\Lambda(v).
}
\tag{9}
$$
第二个等号使用 $P R_W=P$，因为 $\Pi_0$ 已包含反射。
给定 (7) 后，(9) 是完整可计算定义。例如
$$
\Lambda(v)=[w^6]\,
 \frac{I-\omega N_{19,W}}2
 \left(\frac1{18}\sum_{j=0}^{17}\omega^{-2j}N_{7,W}^j\right)
 \Pi_{0,W}\bigl[F(w+2v)\Theta(4w-9v)^2\bigr].
\tag{10}
$$
每个 CM 算子均是原已付的完整有限纤维 trace；没有删掉其余
逆像。式 (10) 定义整个函数，下面有限系数只用于提供可复核
的实际数值，不用于从局部片段猜整个来源。

## 3. 伴随的全部质量、整性及初始系数

在 $v=0$，R471 的整组合及 R466 的精确投影给
$$
\widetilde\Phi(w,0)=F(w)\Theta(4w)^2=-\frac{280}{111}W_*(w),
$$
$$
P W_*=-\frac{3848}{5}S_{\rm new}.
$$
因此
$$
\boxed{\Lambda(0)=\frac{280}{111}\frac{3848}{5}
=\frac{5824}{3}=:c.}
\tag{11}
$$
$5824=2^6\cdot7\cdot13$，故 $c$ 在当前普通处为单位。

整性不仅是质量的断言。$P_W\widetilde\Phi$ 是原完整整
二变量 Amice 来源。$S_{\rm new}(\Omega_p\log(1+T_W))$
的首非零项为 $\Omega_p^6T_W^6$，其系数是单位。
在 (9) 中提取 $T_W^6$ 系数并除以 $\Omega_p^6$，便得到
$\Lambda(\Omega_p\log(1+T_V))\in\mathcal O[[T_V]]$。
所以 $\nu_\Lambda$ 是完整有界整测度，且由 (11) 是
Iwasawa 卷积代数中的单位。

记 $\overline\Lambda=\Lambda/c$。证书直接计算 (10) 的
$v^0,v^6,v^{12},v^{18}$ 全 theta 系数，得到
$$
\boxed{
\begin{aligned}
\overline\Lambda(v)
={}&1+\frac{6561796}{5}\,b\,v^6
-\frac{36571799189284}{1925}\,b^2v^{12}\\
&-\frac{1072590962703380524108}{875875}\,b^3v^{18}
+O(v^{24}).
\end{aligned}
}
\tag{12}
$$
这些分母只有固定小素数。它们不是新的普通素数扫描。
对应 R474 原 $q$ 变量的伴随是
$\Lambda_2(q)=\Lambda(4q)$；例如归一后的 $q^6$ 系数为
$26877116416b/5$。尤其该单位伴随不是常数来源。

### 3.1 为什么每一列是完整 theta 系数

证书在 $\mathbf Q[x,y]/(y^2=x^3+1)$ 中用
$$
Dx=2y,\qquad Dy=3x^2
$$
计算原 $F=\sigma^{72}f(x)$ 与 $U=\sigma^{64}u(x)$ 的
$q$ 展开。联合的 sigma 指数为
$$
\log\frac{\sigma(w+8q)^{72}\sigma(w-9q)^{64}}
               {\sigma(w)^{136}}
=-\sum_{j\ge2}
 \frac{72\,8^j+64(-9)^j}{j!}\,
 D^{j-2}x(w)\,q^j.
\tag{13}
$$
一次项中的 $\zeta(w)$ 系数恰为零。每个算出的 $q^{6k}$
系数都是完整 degree136 theta 多项式，精确落在
$\sigma^{136}x^2X^j$、$0\le j\le22$ 的二十三列内。
对这一整列应用 (7)，结果与相应的
$[q^{6k}]\Lambda_2\cdot S_{\rm new}$ 在所有二十三坐标严格相等。
因此 (12) 不使用截断的 $w$ 级数替代整个第一轴投影。

## 4. 伴随的真实 core 与单位限制

第一轴 $P$ 与完整第二轴的深度限制、测试及来源核心交换。
对 (6) 的 $V$ 式应用 $P_W$，再用 (9)，得到
$$
\nu_{S_{\rm new}}\otimes
 \bigl(\nu_\Lambda|_{p\mathbf Z_p}\bigr)
=\lambda\,\nu_{S_{\rm new}}\otimes[\kappa]_*\nu_\Lambda.
$$
这里不能用 $S_{\rm new}$ 的质量相消，因为它的质量为零。
应按第3节提取其单位系数 $\Omega_p^6T_W^6$，从而合法取消
整个非零第一因素。结果为
$$
\boxed{\nu_\Lambda|_{p\mathbf Z_p}
       =\lambda[\kappa]_*\nu_\Lambda.}
\tag{14}
$$
于是 $\Lambda$ 的当前真实 $K_{612}$ 特征为 $+1$，
与 $S_{\rm new}$ 的 $K_{136}$ 特征 $-1$ 分别保留。没有
由同余猜测整个 degree612 的绝对标量。

令 $\nu_\Lambda^\times=\mathbf1_{\mathbf Z_p^\times}\nu_\Lambda$。
(11)、(14) 给
$$
\nu_\Lambda^\times
=\nu_\Lambda-\lambda[\kappa]_*\nu_\Lambda,\qquad
\nu_\Lambda^\times(\mathbf Z_p)=c(1-\lambda).
\tag{15}
$$
$1-\lambda$ 在当前 ray 上也是单位。可直接验证：若
$\lambda\equiv1\bmod p$，则基曲线 $E_0:y^2=x^3+1$ 的
Frobenius trace $a_p=\pi_0+\bar\pi_0$ 满足
$a_p\equiv-1\bmod p$。因 $p\ge71$ 且
$|a_p|\le2\sqrt p$，必有 $a_p=-1$。但 $E_0$ 的有理二挠点
$(-1,0)$ 使 $\#E_0(\mathbf F_p)$ 为偶数，故 $a_p$ 为偶数，
矛盾。因此
$$
\boxed{\nu_\Lambda,\quad \nu_\Lambda^\times
       \text{ 均为有界整卷积单位}.}
\tag{16}
$$
同样，任意完整环带的测度准确为
$$
\nu_\Lambda|_{p^n\mathbf Z_p^\times}
=\lambda^n[\kappa^n]_*\nu_\Lambda^\times.
\tag{17}
$$
这些全测度身份保留所有伴随测试，不仅给某一个矩。

## 5. 新曲线中央零实际传播到整条伴随条件行

令
$$
\rho_P=\nu_{P_W\widetilde\Phi}
       =\nu_{S_{\rm new}}\otimes\nu_\Lambda,\qquad
J_{\rm new}(u)
=\int_{\mathbf Z_p^\times}\langle W\rangle^{du}
 d\nu_{S_{\rm new}}(W).
\tag{18}
$$
对任意完整连续伴随测试 $h(V)$，准确的全 $u$ 身份是
$$
\boxed{
\int_{W\ {\rm unit}}
 \langle W\rangle^{du}h(V)\,d\rho_P
=J_{\rm new}(u)\,\nu_\Lambda(h).
}
\tag{19}
$$
特别允许 $h$ 是任意实际紧开 $V$ 条件的指示函数乘连续测试。
例如全部深度与全部环带分别给
$$
\begin{aligned}
\int_{W\ {\rm unit},\,V\in p^n\mathbf Z_p}
 \langle W\rangle^{du}h(V)\,d\rho_P
 &=\lambda^nJ_{\rm new}(u)\,
        \nu_\Lambda\bigl(h(\kappa^nV)\bigr),\\
\int_{W\ {\rm unit},\,V\in p^n\mathbf Z_p^\times}
 \langle W\rangle^{du}h(V)\,d\rho_P
 &=\lambda^nJ_{\rm new}(u)\,
        \nu_\Lambda^\times\bigl(h(\kappa^nV)\bigr).
\end{aligned}
\tag{20}
$$
原 $S_{\rm new}(0)=0$ 及其真实 scalar core 给
$J_{\rm new}(0)=0$。所以若待反证的实际算术失败条件为
$J_{\rm new}'(0)=0$，则 (19)、(20) 的所有这些**完整伴随**
中央导数确实为零。这一零传播具有已识别的原曲线来源；
不是从两态核心或质量零自行赋零。

另一方面，(19) 的第一轴保持 $W$ 为单位这一完整条件，
并没有给 $W$ 再添加一个未运输的局部子域。相同理由也不
允许把 $P_W$ 与任意混合 $A,D$ 条件交换。$P_W$ 已在有限
theta 来源空间上完整定义；一般混合域限制未必仍属于
那个固定第一轴空间。

## 6. 合法的反卷积及原两个压缩输入条件的转置

令 $\eta=\nu_\Lambda^{-1}$ 为 (16) 的完整整卷积逆。实际来源
恒等式为
$$
(\operatorname{id}_W\otimes *_V\eta)\rho_P
=\nu_{S_{\rm new}}\otimes\delta_0.
\tag{21}
$$
对连续测试 $g(W,V)$，反卷积的真实转置是
$$
(\mathcal T_\eta g)(W,V)
=\int g(W,V+t)\,d\eta(t),
$$
$$
\boxed{
\int g\,d(\nu_{S_{\rm new}}\otimes\delta_0)
=\int\mathcal T_\eta g\,d\rho_P.
}
\tag{22}
$$
它只在实际伴随方向作用，保 $W$，因此对于
$g=\mathbf1_{W\ {\rm unit}}\langle W\rangle^{du}h(V)$，
(22) 与 (19) 完全相容。单位限制的伴随
$\nu_\Lambda^\times$ 也可按同样方法单独反卷积。

但原两个压缩输入由
$$
A=\frac{9W+4V}{17},\qquad
D=\frac{2W-V}{17}
\tag{23}
$$
恢复。于是 $V\mapsto V+t$ 真实改变它们为
$$
A\mapsto A+\frac4{17}t,\qquad
D\mapsto D-\frac1{17}t.
\tag{24}
$$
例如附带原 $A\in p^n\mathbf Z_p$、$D$ 单位的测试，必须变成
$$
\int
 \mathbf1_{\,A+4t/17\in p^n\mathbf Z_p}\,
 \mathbf1_{\,D-t/17\in\mathbf Z_p^\times}\,
 g(W,V+t)\,d\eta(t).
\tag{25}
$$
不能把 (25) 简化成原来的两个指示函数。
若只在 $W$ 单位部分看 $A$ 深管，其精确几何式为
$9W+4V\in p^n\mathbf Z_p$；它在 $V$ 单位部分形成一条随
$W$ 移动的管，仍不是 (20) 的单独 $V$ 条件。

此外，反卷积不与限制 $V\in p\mathbf Z_p$ 自动交换。
事实上 (21) 的右侧第二因素是 $\delta_0$，它的真实限制为
自己；若误把 (14) 无条件反卷积成 $\lambda$ core，就会
错误得到 $\delta_0=\lambda\delta_0$。式 (22)–(25) 保留的
实际测试正是必须处理的补偿。

## 7. 证书与尚未删除的联合信息

本篇将新算术线的中央零接到同一个原 $F_{72}\otimes\Theta^2$
来源的完整第一轴投影，并把伴随下降为固定 degree612。
已知的全 $\Lambda$、全环带、任意完整伴随测试及其合法单位
反卷积都由 (9)、(14)、(19) 支付。

它不把投影后的 $\rho_P$ 当作原未投影的
$\widetilde\nu_0$，也不把 $A$ 的总深度当作原六 sigma
分别深。与 R465 原六输入投影伴随的进一步相等，必须另给
整个伴随方向及其全部原输入的具体映射；只比较两个非零
质量不足以建立这个映射。

- [完整精确投影与伴随系数脚本](../scripts/check-r477-rank-one-companion.py)。
- [完整二十三维投影及伴随系数数据](../scripts/check-r477-rank-one-companion.json)。
- [R474：同一个原二输出两态核心及 Riemann 域](R474-original-six-sigma-two-output-core-and-exact-riemann-domains.md)。
- [R471：原六 sigma 与两个 Theta 的完整因式](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)。
- [R466：新曲线的全有限角色与来源身份](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)。
- [R469：新曲线普通、惰性及 Sha 桥](R469-e2312-full-weight-square-ordinary-inert-sha-bridges.md)。

