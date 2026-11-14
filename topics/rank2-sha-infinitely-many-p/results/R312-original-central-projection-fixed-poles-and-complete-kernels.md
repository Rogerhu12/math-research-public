# R312：固定极点商上的原中央投影、准对数取消与两条完整核

日期：2026-11-13。**状态：以下固定五维全纯 theta 空间、除以同一真实参考后的中央线性投影、普通完整卷积核及其全部小环带界、惰性完整 Newton 双级数均已证明。该投影准确消去第三类原函数的任意线性项；单独证明准对数非零不提供原中央非零。原目标的跨素数非零仍未证明。**

本篇固定 R307–310 的实际 $b=17$、$X=x^3$、
$$
H=H_3=\sigma^{34}x^2(X-8b)D(X),\quad
D(X)=(X+4b)C_3(X),\quad
C_3=X^3-204bX^2-384b^2X+64b^3,
$$
以及原秩二来源 $S=H_1=Hg$，其中
$$
g=\frac1{28(X+4b)}
 +\frac{27X(X+4b)}{28C_3(X)},\qquad
H(0)=1,\quad g=z^6+\cdots .
\tag{1}
$$
一切测度、Gaussian、权和周期均沿 R295、R301、R308、R310；没有重新选参考。

## 1. 原极点商确有一个固定的五维全纯 theta 实现

在包含 $D$ 全部根的固定数域 $L$ 上，令 $\mathcal P$ 为 R310 的全部二十四个简单极。由 $X$ 给出的商 $E/\mu_6\simeq\mathbf P^1_X$ 可知
$$
\mathcal V
=\{R\in L(E)^{\mu_6}:\operatorname{div}_\infty R\le\mathcal P\}
=L\cdot1\oplus\bigoplus_{D(r)=0}L\cdot\frac1{X-r}.
\tag{2}
$$
这里在 $O$ 正则的条件就是 $X=\infty$ 处没有多项式正次项。四个分母根不同，且均非零、不是 $-b$，所以 $X-r$ 的零在 $E$ 上确为六个简单点。部分分式直接证明 (2)，不需要新的有限素数试验。

乘以同一个 $H$ 给一一对应
$$
\boxed{
H\mathcal V
=\left\{\sigma^{34}x^2(X-8b)Q(X):\deg Q\le4\right\}.
}
\tag{3}
$$
这是原 degree-$34$ theta 空间中的一个真实五维全纯子空间。事实上 $D$ 的四个多项式 $D/(X-r)$ 线性独立并张成次数至多三的全部多项式；再加首一四次 $D$ 即得 (3)。在 $O$，最高次数四的 $Q$ 给正则常数，次数至多三则至少从 $z^6$ 开始；在其他点没有极。

特别，
$$
B_r:=\frac H{X-r}
\tag{4}
$$
是四条真实全纯 theta 截面，各有质量零，并且
$$
S=\sum_{D(r)=0}A_r B_r,\quad
A_{-4b}=\frac1{28},\quad
A_r=\frac{27r(r+4b)}{28C_3'(r)}\ (C_3(r)=0).
\tag{5}
$$
$H_5$ 也属于 (3)，且 $H_5-H$ 在四条 $B_r$ 的张成中。

(3) 只是一份准确的原 theta 子空间。除了 R306–308 已识别的三条来源外，没有给四条 $B_r$ 各自附加一个秩二 Hecke 角色，也没有声称它们的中央导数同时为零。

## 2. 同一参考的中央投影

先作一个一般的准确代数运算。设 $\mathcal M_T(u)$ 是对来源 $T$ 线性的同一解析变换，$\mathcal M_H(0)=m_H\ne0$。定义
$$
\boxed{
\mathscr L_H(T)
=\left(\frac{\mathcal M_T}{\mathcal M_H}\right)'(0)
=\frac{\mathcal M_T'(0)m_H-\mathcal M_T(0)\mathcal M_H'(0)}
       {m_H^2}.
}
\tag{6}
$$
它对 $T$ 线性，并且
$$
\boxed{\mathscr L_H(H)=0,\qquad
\mathscr L_H(H(R+c))=\mathscr L_H(HR).}
\tag{7}
$$
因此在 (2) 上，它是商空间 $\mathcal V/L$ 的真实线性泛函。等价地，对微分 $R\,dz$ 而言，它忽略全纯微分 $c\,dz$，却没有删除 $H$ 这个乘子。

普通处取 $\mathcal M=M$ 为 R310 的完整单位 Mellin 变换，
$$
m_H=1-\bar\pi_3^{-1}\in\mathcal O^\times.
$$
惰性处取 $\mathcal M=\mathcal J$ 为 R301 的完整 Newton 变换，此时 $m_H=1$。原 $S$ 在两处都满足 $\mathcal M_S(0)=0$，故
$$
\mathscr L_H(S)=\frac{\mathcal M_S'(0)}{m_H}.
\tag{8}
$$
所以 $\mathscr L_H(S)\ne0$ 正好是 R295/R303 已支付的同一个充分中央输入。式 (6) 没有把参考自身的未知斜率置零。

## 3. 准对数的单独线性方向准确消失

R310 的唯一规范原函数 $V$ 满足 $V'=g,V(0)=0$。写 $C=HV$，则
$$
\nabla_H C=S,\qquad \nabla_H=\partial_z-H'/H.
$$
对任意常数 $\lambda$，不论其是否代数，都有准确分解
$$
V=\lambda z+(V-\lambda z),\qquad
\nabla_H(\lambda zH)=\lambda H.
$$
因此
$$
\boxed{
\mathscr L_H(\nabla_H(HV))
=\mathscr L_H(\nabla_H(H(V-\lambda z))).
}
\tag{9}
$$

在 R310 的复 sigma 写法中，
$$
V(z)=
\sum_a\varrho_a\log\!\left(-\frac{\sigma(z-P_a)}{\sigma(z+P_a)}\right)
+2z\sum_a\varrho_a\zeta(P_a).
\tag{10}
$$
所以其中准对数和产生的整个线性项，被 (9) 准确杀掉。若将 (10) 用代数普遍向量扩张提升运输到某个 $p$ 进 realization，同样结论逐式成立。这里不需要假定 $\zeta(P_a)$ 在原形式收敛圆盘之外仍能由 Laurent 级数直接求值：对任意常数的 (9) 已经足够。

(9) 不删除 (10) 的非恒定 sigma 比，不把其 monodromy 置零，也不声称准对数本身为零。它说明单独对 $\sum\varrho_a\zeta(P_a)$ 应用线性独立定理，即使得到非零，也不能把该数直接当作 (8)。所有高阶 Taylor 系数及原卷积仍然存在。

## 4. 普通处的精确完整核

固定 $p>7$、$p\equiv1\pmod3$，置 $d=p-1$。沿原形式周期和整 Amice 变换，R310 给
$$
\nu_S=\nu_H*\nu_g,\qquad
\nu_H,\nu_g\text{ 均为有界整测度},\qquad
\nu_g(\mathbf Z_p)=0.
$$
星号是加法卷积。令
$$
\ell_H=\frac{M_H'(0)}{m_H},
$$
并对 $y\in\mathbf Z_p$ 定义真正的单变量测试核
$$
\boxed{
K_{H,p}(y)=\frac1{m_H}
\int_{\mathbf Z_p}
\mathbf1_{x+y\in\mathbf Z_p^\times}
\bigl(d\log_p\langle x+y\rangle-\ell_H\bigr)\,d\nu_H(x).
}
\tag{11}
$$
其被积函数在每一个固定的 $y\bmod p$ 小圆盘上有统一收敛的解析展开，排除的 $x$ 剩余类在该圆盘内固定。因此 $K_{H,p}$ 是局部解析函数；$\ell_H\in p\mathcal O$，从而整个核的值在 $p\mathcal O$。

由完整加法卷积和 Fubini，准确得到
$$
\boxed{
\mathscr L_H(S)=\int_{\mathbf Z_p}K_{H,p}(y)\,d\nu_g(y).
}
\tag{12}
$$
同一公式适用于其他有界 $\nu_R$ 的 $HR$。式 (11) 明确保留了两单位相加后变成非单位的区域及参考斜率；没有用两个乘法 Mellin 函数的乘积取代加法卷积。

在 $y=0$，
$$
K_{H,p}(0)
=\frac{M_H'(0)-\ell_Hm_H}{m_H}=0.
\tag{13}
$$
因此 $R\mapsto R+c$ 在测度侧增加 $c\delta_0$，被 (12) 准确杀掉。这里的 $\delta_0$ 只是这个人为增加的常数的 Amice 变换；没有断言原测度自身在零点有某个原子。

## 5. 所有小环带及完整负矩

当 $y\in p\mathbf Z_p$ 时，$x+y$ 是单位当且仅当 $x$ 是单位。由
$$
\log\langle x+y\rangle
=\log\langle x\rangle+\sum_{n\ge1}
             \frac{(-1)^{n-1}}n(y/x)^n
$$
以及 (13)，可在原有界测度下逐项积分。$H(az)=H(z)$ 对 $a\in\mu_6$ 成立，故 $\nu_H$ 在 $[a]$ 下不变。这使
$$
\int_{\mathbf Z_p^\times}x^{-n}\,d\nu_H(x)=0
\quad\text{若 }6\nmid n.
$$
于是得到包含全部负权的准确核
$$
\boxed{
K_{H,p}(y)
=-\frac d{m_H}\sum_{k\ge1}
\frac{y^{6k}}{6k}
\int_{\mathbf Z_p^\times}x^{-6k}\,d\nu_H(x),
\qquad y\in p\mathbf Z_p.
}
\tag{14}
$$
没有将这里的负矩换成已知的零权质量；它们都是原同一参考测度的实际值。

若 $y\in p^N\mathbf Z_p$、$N\ge1$，则每一项赋值至少
$$
6kN-v_p(k)\ge6N.
$$
故
$$
\boxed{
K_{H,p}(p^N\mathbf Z_p)\subset p^{6N}\mathcal O,\qquad
v_p\!\left(\int_{p^N\mathbf Z_p}K_{H,p}\,d\nu_g\right)\ge6N.
}
\tag{15}
$$
第二式使用的是原 $\nu_g$ 的整有界性。因而 (12) 的所有环带精确重构，舍去 $p^N\mathbf Z_p$ 的误差有 (15) 的统一界。这没有给 $\nu_g$ 额外假定一个未经证明的标量 $p$-core。

这个界使原问题成为可以从单位区和有限个小环带计算的完整非零问题；它本身并不证明任一截断非零，更不证明跨 $p$ 无穷命中。

## 6. 惰性处的完整核及可证明的重排

固定 $p\ge11$、$p\equiv5\pmod6$、$p\ne17$，令
$$
d=p+1,\quad s=d/6,\quad
R=p^{-1/(2p)},\quad c=[z^d]\log(\sigma/z),\quad
\kappa=34c,\quad v_p(\kappa)=-1.
$$
沿同一个真实 Gaussian 写
$$
\widehat H=e^{-\kappa z^d}H=\sum_{j\ge0}h_jz^j,\qquad
g=\sum_{n\ge1}g_nz^{6n}.
$$
R308/R310 的完整估计给
$$
\|\widehat H\|_R=1,\qquad
v_p(h_j)\ge-\frac j{2p},\qquad
v_p(g_n)\ge
\left\lceil\frac{6-6n}{p^2-1}\right\rceil .
\tag{16}
$$

对 $n\ge1$，定义
$$
\boxed{
W_{n,p}=
\sum_{h\ge\lceil n/s\rceil}
(-1)^{h-1}(h-1)!\,\kappa^{-h}h_{dh-6n}.
}
\tag{17}
$$
然后原中央投影准确等于
$$
\boxed{\mathscr L_H(S)=\sum_{n\ge1}g_nW_{n,p}.}
\tag{18}
$$
这保留全部 $h$，不是只读首个 $d$ 次系数。

证明从 R301 的定义出发：
$$
\mathcal J_T(u)=\sum_{h\ge0}[z^{dh}]
(e^{-\kappa z^d}T)\kappa^{-h}(u)_h,\qquad
(u)_h'(0)=(-1)^{h-1}(h-1)!.
$$
对一般 $R_0=r_0+\sum_{n\ge1}r_nz^{6n}$，$n=0$ 部分准确是
$r_0\mathcal J_H'(0)$，在 (6) 中被减掉；剩余即 (17)–(18)。

这里还必须证明所有重排合法。对原 $g$ 的每一个双级数项，(16) 给赋值下界
$$
\begin{aligned}
&v_p((h-1)!)+h-\frac{dh-6n}{2p}
                         +\frac{6-6n}{p^2-1}\\
&\qquad =
v_p((h-1)!)+\frac{h(p-1)}{2p}
+6n\left(\frac1{2p}-\frac1{p^2-1}\right)
+\frac6{p^2-1}.
\end{aligned}
\tag{19}
$$
括号为正；当双索引离开任意有限集合时，右边趋于无穷。每个 $h$ 下又只有有限多个 $n\le dh/6$。因此这是真正的无条件收敛 $p$ 进双族，可以按 $h$ 或按 $n$ 求和，得到 (18)。

同一证明适用于满足对应 Gauss 界的其他原有理局部输入。若 $g$ 的一个真实替换与它相差
$p^N t^6\mathcal O[[t^6]]$，其中 $t=x^{-1/2}$，R301 的同一参数半径界使其 $\mathcal J$ 差属于
$$
p^{N+1}\mathcal O_p\langle u\rangle.
\tag{20}
$$
这里 $\mathcal O_p$ 是输入系数所在有限扩域的整数环；输入在 $\mathbf Q_p$ 时就是 $\mathbf Z_p$。确实，Gaussian 删除后的来源范数至多 $p^{-N}R^6$，其 $h$ 次 Newton 系数的赋值至少
$N+\lceil(h(p-1)+6)/(2p)\rceil$；常数项为零，而 $h\ge1$ 时后一个整下界至少一。$H$ 的真实单位参考使除以 $\mathcal J_H$ 后仍保持 (20)。这只是带明确高位误差的比较，不将替换后的局部输入宣称为原 Hecke 来源。

## 7. Frobenius 接口的准确可用范围

若某个实际提升或同源迹已经给出
$$
\mathcal T(HR)=HR_1+aH
\tag{21}
$$
作为完整原函数或相应分布等式，那么 (6)–(7) 无条件给
$$
\mathscr L_H(\mathcal T(HR))=\mathscr L_H(HR_1).
\tag{22}
$$
因此 $\eta\mapsto\eta+a\,dz$ 的全纯缺项确实可以通过这个**同一参考**投影消掉。这为 R310 的第三类微分提供了一个准确商空间接口。

但仅知道模 $p$ 的 $\mathcal C^2\eta-\eta=a_pdz$，还没有 (21) 的完整原同源/分布等式。其物理同源、$H$ 比值、移动极点及原高位误差仍须逐项支付。式 (20) 说明这些误差在实际 Newton 变换中的精确可用范围；不能由裸 Cartier 等式声称整个中央导数保持不变。

本篇的非零目标始终是 (12) 或 (18) 对 (1) 的实际值。没有用准对数的单项、四个任意新来源、参考斜率或有限素数样本替代它。

直接依赖：
[R295](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)、
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)、
[R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)、
[R308](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)、
[R310](R310-jzero-actual-rankzero-frame-third-kind-and-central-transpose.md)。

