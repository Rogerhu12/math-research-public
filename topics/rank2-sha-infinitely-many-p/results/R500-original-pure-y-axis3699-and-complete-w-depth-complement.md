# R500 — 原 degree3699 纯 Y 斜轴、真实三输入压缩与 W 深浅补域

日期：2026-11-14。**状态：已证明。** 在 R493、R497 的同一个原
六 sigma 来源上，本篇增加一条真正正交于 $Y,T_c$ 的固定斜轴
$V$。其 degree 为 $3699$；一条兼容固定 ray 和原两 sigma 锚
支付整个 odd theta 核心 $\chi_p\lambda$，其中
$\chi_p^2=1$，不预先选择符号。剩余三个完整伴随也有准确共同
核心。

R497 的原 $S$ 测试因而可以保 $V$ 深度，且第一 $Y$ 的全部
CM 投影与之严格交换。在 $V$ 深的同一域里，非零小管的
$Z$ 深条件恰等于 $W'$ 深条件；唯一补域变成同一来源的
$W'$ 浅层部分。本文进一步合法消去三个共同伴随深度，将全部
剩余积分压到一个显示的两变量五 sigma 来源与一个独立 sigma。
补域未被赋零，主目标未完成。

## 1. 同一五 sigma 和固定纯 Y 轴

保持 R493、R497 的原周期、$b=17$、
$$
\delta^2=-3,\quad \gamma=(5+\delta)/2,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2.
\tag{1}
$$
五个未缩放输入按
$\boldsymbol u=(\xi_1,\xi_2,\xi_3,c,d_0)$ 排列，剩余独立 sigma
输入为 $x=\xi_4$。记
$$
z=(\delta,2\delta,\gamma,1,2),\qquad
a=(2+2\delta,2\delta,2+2\delta,3+\delta,4),
$$
$$
Z=z\boldsymbol u,\qquad W'=a\boldsymbol u,\qquad
Y=Z+\bar\gamma x,\qquad T_c=\gamma Z-27x.
\tag{2}
$$
R493 已付整个原来源的 $Z$ core 和 $W'$ core 均为 $\beta$，
并且原 sigma 的 $x$ core 也是 $\beta$。
这里 $W'$ 不含 $x$，其物理核心也固定 $x$。因此原完整六输入
身份是五输入身份张量 $\nu_\sigma$；取 $x$ 的一次 Amice 系数
$\Omega$ 就能严格约去该非零因子，给五输入本身的 $W'$ 核。
这不是直接忘掉一个质量为零的独立 sigma。
$Z$ 与 $W'$ 的完整 Gram 是
$$
\langle z,z\rangle=27,\qquad
\langle a,a\rangle=72,\qquad
\langle a,z\rangle=37+3\delta.
\tag{3}
$$

置 $\alpha=37+3\delta$，定义
$$
\boxed{V=\frac{27W'-\alpha Z}{2}.}
\tag{4}
$$
其五个系数全部为 CM 整数：
$$
\boxed{
v=\left(\frac{63+17\delta}{2},\
9-10\delta,\ -17+14\delta,\ 22+12\delta,\ 17-3\delta\right).
}
\tag{5}
$$
在 $\mathbf Z[\omega]$ 中依次为
$$
(40+17\omega,\ -1-20\omega,\ -3+28\omega,\
34+24\omega,\ 14-6\omega).
$$
准确有
$$
\boxed{\langle v,z\rangle=0,\qquad
       \langle v,v\rangle=3699=27\cdot137.}
\tag{6}
$$
$V$ 不含 $x$，所以同时正交于 $Y,T_c$，保持 R497 的全部纯
$T_c$ 测试。后面所有深度都使用这个 (4) 的物理尺度，没有
再把它除以一个 $p$ 相关数。

## 2. 保全部输入的完整坐标与三伴随

给出一个固定、可逆、原普通处整的完整框架
$$
\boldsymbol u\longmapsto (Z,V,Q_1,Q_2,Q_3).
\tag{7}
$$
为完全指定它，令
$$
D=\begin{pmatrix}\bar z_1&\bar z_2\\
                  \bar v_1&\bar v_2\end{pmatrix},\qquad
\det D=81+54\delta.
$$
对 $j=3,4,5$ 定义
$$
\begin{pmatrix}b_j\\c_j\end{pmatrix}
=-D^{-1}\begin{pmatrix}\bar z_j\\\bar v_j\end{pmatrix},
\qquad Q_{j-2}=u_j+b_ju_1+c_ju_2.
\tag{8}
$$
这显示指定了每个系数。每个 $Q_i$ 都同时正交于 $Z,V$，
从而也正交于 $W'$。三者彼此不要求正交；它们的共同深度
仍是完全指定的实际事件。

附脚本给 (7) 的整个矩阵 $\mathcal M$、逆及完整 Gram。
前两个 Gram 块恰为 $\operatorname{diag}(27,3699)$，与后面
三个坐标的所有交叉项均为零。行列式准确为
$$
\boxed{
\det\mathcal M=\frac{3699-2466\delta}{7},\qquad
\operatorname{Norm}(\det\mathcal M)=\frac{3699^2}{21}.
}
\tag{9}
$$
系数及其逆的坏素数只在 $2,3,7,137$ 中。当前普通 ray
$p\ge71$ 且 $p\equiv1\bmod3$，故没有 $p=137$，(7) 是原
$\mathbf Z_p^5$ 整自同构。因此
$$
\boxed{\boldsymbol u\in(p^n\mathbf Z_p)^5
\ \Longleftrightarrow\
Z,V,Q_1,Q_2,Q_3\in p^n\mathbf Z_p.}
\tag{10}
$$
这是完整事件等价，不是忘却隐藏输入后的边际比较。

## 3. 兼容固定 ray 与整个 odd3699 的真实绝对符号

在 R487 的高 $13,19$ 次固定 ray 和 R488 的
$\pi_0\equiv2\bmod29$ 上，只增加
$$
\boxed{\pi_0\equiv1\pmod{137}.}
\tag{11}
$$
$137$ 与此前固定模数互素，故这是兼容的固定单位 CRT 类。
脚本先合并 R487、R488 的完整代表，再加入 (11)，给出唯一代表
和新模数，并直接验证其范数为单位。与已有 CM ray-class 素理想
定理相同，仍得到无穷多个不同普通有理素数。

原 ray 已有 $g_\pi=\pi_0/\bar\pi_0\equiv1\bmod54$，因此
$$
\boxed{g_\pi\equiv1\pmod{7398}=\pmod{2\cdot3699}.}
\tag{12}
$$
(5) 的五个系数中前三个模二为单位，后两个为零。
每个 CM 单位保持 sigma 唯一的奇半特征，所以第一 $V$ 轴确实
是原奇 $\mathcal S_{3699}$。原交叉项由 (6)、(8) 消失，不添
随其他生成变量变化的半特征。

R370、R454 的完整 odd theta 交织与 (12) 给
$$
K_{3699,p}=\chi_p I
\tag{13}
$$
在整个原奇空间成立。仍须支付实际标量，不能将 (13) 免费改写
成 $+I$。

使用原两 sigma 的完整锚。置
$$
a_*=6\delta,\qquad b_*=3\delta\gamma\gamma_{19},\qquad
\gamma_{19}=4+\delta.
$$
准确有
$$
N(a_*)=108,\quad N(b_*)=3591,\quad
N(a_*)+N(b_*)=3699,
$$
$$
\begin{pmatrix}a_*&b_*\\-\bar b_*&\bar a_*\end{pmatrix}
\overline{\begin{pmatrix}a_*&b_*\\-\bar b_*&\bar a_*\end{pmatrix}}^{\,t}
=3699I.
\tag{14}
$$
$a_*$ 模二为零，$b_*$ 模二为单位，所以两个输出都有同一个
原奇半特征。该矩阵的行列式 $3699$ 在当前普通处为单位。
两个原独立 sigma 同时深的标量是 $\beta^2=\lambda^2$；
两个 degree3699 输出依次应用 (13) 时的标量是
$\lambda^2\chi_p^2$。这两个深域由 (14) 精确相同。
原联合两 sigma 来源非零，取消共同可逆推前后得到
$$
\boxed{\chi_p^2=1.}
\tag{15}
$$
这是原完整锚支付的真实符号；本篇保留
$\chi_p\in\{1,-1\}$，不选择其值，也不以未知中央导数定标。

## 4. 原来源的全部三组核心

令 $\mu$ 是 (2) 五个 sigma 的联合，常数 $-1/84$ 包含在内。
(13)–(15) 对第一 $V$ 的整个 theta 截面逐点作用，保其他四个
坐标，故
$$
\boxed{\mu|_{V\in p\mathbf Z_p}
=\chi_p\lambda[I_Z,\kappa,I_3]_*\mu.}
\tag{16}
$$
这里后面三坐标的 Gram 可有内部交叉项，但与 $V$ 的全部交叉
项为零，因此不妨碍原单轴完整 trace。

原五 sigma 同时深给 $\beta^5$；(10) 把它变成
$Z,V,\mathbf Q$ 同时深。分别取消 R493 的 $Z$ core $\beta$
与 (16)，得到准确的三伴随共同核心
$$
\boxed{
\mu|_{\mathbf Q\in(p\mathbf Z_p)^3}
=\chi_p\lambda^3[I_Z,I_V,\kappa I_3]_*\mu.
}
\tag{17}
$$
用到 $\chi_p^{-1}=\chi_p$，没有把共同深度拆成三个尚未证明的
单独 scalar core。

所以对任意非负整数 $r,s,t$，
$$
\boxed{
\mu|_{Z\in p^r,\ V\in p^s,\ \mathbf Q\in(p^t)^3}
=\beta^r(\chi_p\lambda)^s(\chi_p\lambda^3)^t
 [\kappa^r,\kappa^s,\kappa^tI_3]_*\mu.
}
\tag{18}
$$
另一个独立输入 $x$ 及其全部测试均保留。

在 $(Y,T_c,V,\mathbf Q)$ 中，(16)、(17) 只改变后四个坐标。
因此它们与第一 $Y$ 的全部 canonical CM trace、反射及角投影
逐项交换，含完整中心；也严格保持 R497 的正次数纯 $T_c$
测试及其单位校正。这一交换不是仅由 principal 边际猜得。

## 5. 原算术行现在保任意 V 深度

令 $\mathfrak h_{b,p}^{\times}$ 是 R497(21) 已精确构造的同一个
固定正次数算术测试。其完整第一来源是 $S$。
由 (16)、(17)，对任意 $s,t\ge0$，同一原六输入给
$$
\boxed{
\int_{\substack{V\in p^s,\ \mathbf Q\in(p^t)^3\\
                T_c\ {\rm unit},\ Y\ {\rm unit}}}
 \langle Y\rangle^{du}\,
 \mathfrak h_{b,p}^{\times}(T_c/\Omega)\,d\rho_0
=\chi_p^{s+t}\lambda^{s+3t}J_S(u).
}
\tag{19}
$$
这里没有第一 Mellin 权的额外尺度因子，因为这些核心真正固定
$Y,T_c$。若 $J'_S(0)=0$，(19) 的全部实际中央为零。
这项传播现在由完整原来源支付。

R493 的 $\mathcal T$ 固定 $Y$，且
$h=\omega^2\mathcal T_*\rho_0$。所以令
$$
V^{\mathcal T}=V\circ\mathcal T^{-1},\quad
\mathbf Q^{\mathcal T}=\mathbf Q\circ\mathcal T^{-1},\quad
T_c^{\mathcal T}=T_c\circ\mathcal T^{-1},
$$
就得到 (19) 在真实 $h$ 上的完整版本，右侧再乘 $\omega^2$。
$V^{\mathcal T}$ 仍为纯 $Y$ 伴随，核心仍是
$\chi_p\lambda$；第一 $Y$ 的全部 CM 投影同样严格交换。

## 6. 小管 Z 深条件与同一 W' 深条件完全等价

(4) 给实际物理式
$$
\boxed{W'=(\alpha Z+2V)/27,\qquad N(\alpha)=1396=4\cdot349.}
\tag{20}
$$
排除固定素数 $349$ 后，$\alpha,27$ 都是单位。
在 $V\in p^n\mathbf Z_p$ 内，
$$
\boxed{
Z\in p^n\mathbf Z_p\quad\Longleftrightarrow\quad
W'\in p^n\mathbf Z_p.
}
\tag{21}
$$
若 $Z$ 不在 $p^n$，则更精确有 $v_p(W')=v_p(Z)<n$，
因为 $2V$ 无法与较浅的 $\alpha Z$ 相消。

取
$$
\Gamma_n=
\{V,\mathbf Q\in p^n,\ T_c\ {\rm unit},\ Y\ {\rm unit}\}.
$$
由 (10)、(21) 和 $Y=Z+\bar\gamma x$，
$$
\boxed{
\begin{aligned}
\Gamma_n\cap\{W'\in p^n\}
 &=\{Z,V,\mathbf Q\in p^n,\ x\ {\rm unit}\}
   =\mathcal D_n,\\
\Gamma_n\cap\{W'\notin p^n\}
 &=\Gamma_n\setminus\mathcal D_n .
\end{aligned}
}
\tag{22}
$$
$\mathcal D_n$ 正是 R493、R497 的五个原 sigma 同时深、
剩余 sigma 单位的真实网格。因此 R497 的单位第五阶结论
原样给此处第一支的中央 $\mathcal C_n^\times\ne0$，
$v_p(\mathcal C_n^\times)=5n$；同一个测试也用于 (19)。

在 $s=t=n$ 时，$\chi_p^{2n}=1$。准确的原中央式是
$$
\boxed{
\lambda^{4n}J'_S(0)=\mathcal C_n^\times+
 \int_{\Gamma_n\cap\{W'\notin p^n\}}
  d\log\langle Y\rangle\,
  \mathfrak h_{b,p}^{\times}(T_c/\Omega)\,d\rho_0 .
}
\tag{23}
$$
经 $\mathcal T$ 运输后，$W'$ 变成旧 $W$，同一不交分拆及全部
测试转置成立。没有把 (23) 的浅支赋零。

## 7. 合法压缩到显示的两变量五 sigma 与一个独立 sigma

本文的三个 $Q_i$ 已有 (17)，可以准确消去共同深条件，而不
遗失其系数。定义显示的整个两变量来源
$$
\boxed{
\mathcal L(z,v)=-\frac1{84}
 \prod_{j=1}^5\sigma(z_jz+v_jv)
 \in\mathcal S_{27}^{\rm odd}\boxtimes\mathcal S_{3699}^{\rm odd}.
}
\tag{24}
$$
这里 $z_j,v_j$ 全部在 (2)、(5) 显示；这就是将三个真正的
$Q$ 生成变量置零后的完整来源。两个轴的交叉项为零，
没有未定的辅助来源或新半特征。
其 $Z$ 边际是 R497 的 $B_{27}$；$W'$ 边际准确为
$$
\mathcal L(\alpha u/27,2u/27)
=\frac{\omega^2}{84}\sigma(4u)^3\sigma(2\delta u)^2.
\tag{25}
$$
(24) 保 $Z$、$V$、$W'$ 的实际 scalar cores
$\beta,\chi_p\lambda,\beta$，因为相应限制不含被忘却的 $\mathbf Q$。

对只依赖 $Z,V,x$ 的任意实际可积测试，(17) 给
$$
\boxed{
\int_{\mathbf Q\in(p^t)^3}f(Z,V,x)\,d\rho_0
=(\chi_p\lambda^3)^t
 \int f(Z,V,x)\,d(\nu_{\mathcal L}\otimes\nu_\sigma).
}
\tag{26}
$$
这支付真正的三输入压缩；并未将原五 sigma 的独立深事件先
冒认为只有 $Z,V$ 深。

在此三输入来源中，准确的两个域是
$$
\widetilde\Gamma_n=\{V\in p^n,\ T_c\ {\rm unit},\ Y\ {\rm unit}\},
$$
$$
\widetilde{\mathcal D}_n
=\{Z,V\in p^n,\ x\ {\rm unit}\}
=\widetilde\Gamma_n\cap\{W'\in p^n\}.
\tag{27}
$$
(19) 与 (26) 给完整中央
$(\chi_p\lambda)^nJ'_S(0)$。
小管值为
$$
\boxed{
\widetilde{\mathcal C}_n^\times
=(\chi_p\lambda^3)^{-n}\mathcal C_n^\times
=(-\chi_p)^n\lambda^{2n}\mathcal A^\times(\kappa^n),
\qquad v_p(\widetilde{\mathcal C}_n^\times)=5n.
}
\tag{28}
$$
$\mathcal A^\times$ 是 R497 已保全部 log 项及全尾的同一个函数。
因此完整剩余方程是
$$
\boxed{
(\chi_p\lambda)^nJ'_S(0)
=\widetilde{\mathcal C}_n^\times+
 \int_{\widetilde\Gamma_n\cap\{W'\notin p^n\}}
 d\log\langle Y\rangle\,
 \mathfrak h_{b,p}^{\times}(T_c/\Omega)
 \,d(\nu_{\mathcal L}\otimes\nu_\sigma).
}
\tag{29}
$$
(29) 已没有未注明的隐藏输入；它保唯一实际浅支的全部
$Z,V,x$ 条件。

## 8. 三输入中的 W' 核仍须准确运输移动测试

在真正 $(Z,V,\mathbf Q)$ 坐标中，$W'$ 的物理核心是
$$
\boxed{
C_{W'}=
I+\frac{\kappa-1}{1944}
\begin{pmatrix}
1396&2(37-3\delta)\\
274(37+3\delta)&548
\end{pmatrix}
}
\tag{30}
$$
作用于 $(Z,V)$，三个 $Q_i$ 及 $x$ 都固定。
显示的秩一矩阵除以 $1944$ 是幂等矩阵，迹为一；
其行正是 (20) 的 $W'$，故它把 $W'$ 乘以 $\kappa$。
附证书按 (7) 的完整矩阵直接验证。

更直观的完整测试转置是
$$
\boxed{
\begin{aligned}
Z&\longmapsto Z+\frac{\kappa-1}{72}(37-3\delta)W',\\
V&\longmapsto V+\frac{\kappa-1}{72}\,274\,W',\\
Y&\longmapsto Y+\frac{\kappa-1}{72}(37-3\delta)W',\\
T_c&\longmapsto T_c+\frac{\kappa-1}{72}\gamma(37-3\delta)W'.
\end{aligned}}
\tag{31}
$$
所以 (29) 中的 $V$ 深条件、$Y,T_c$ 单位条件及多项式测试，
在 $W'$ 核下均必须按 (31) 改变。三输入来源的真实 core
并没有使这些条件自动不变。下一问题已准确缩到 (24)、(29)：
用同一来源的 $Z,V,x,W'$ 核及全部移动测试控制这个浅支；
本篇没有由 (28) 的非零删除它。

## 证书与依赖

- [原完整框架、fixed ray、odd 锚及 W' 真域比较脚本](../scripts/check-r500-original-pure-y-axis3699.py)；
  [精确数据](../scripts/check-r500-original-pure-y-axis3699.json)。
- [R493：原六 sigma 的真实 T、W' 和 degree27 core](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R497：同一个正次数纯伴随 S 测试和单位第五阶](R497-original-degree918-positive-companion-and-six-sigma-arithmetic-grid.md)。
- [R487：兼容高 norm13/19 固定 ray](R487-original-cm-mixed-tubes-and-common-core-reference-carry.md)。
- [R488：原 norm29 细分及真实状态规范](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)。
- [R454：whole odd theta 的完整中心与两 sigma 绝对平方锚](R454-original-odd33-core-and-exact-residual-slope-transport.md)。

