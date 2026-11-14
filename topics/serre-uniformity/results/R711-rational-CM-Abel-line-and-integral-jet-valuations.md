# R711 — 原有理 CM Abel 直线、整数 jet 赋值及实际深盘的二次缺口

状态：**已证明的下降与局部判据；$p=137147$ 的额外单位条件仍未证明。**
本条继续使用 R575 的实际正三次商，不使用相反扭向的秩零结论。
取 $p\ge41$、$p\equiv5\pmod6$，所有 $M_m$、$z_{\rm f}$、$s=a-1$
及 $P_p$ 均保持 R705/R710 的原定义。

## 1. 结论

令 $M_*=M_{p-3}$。R705 已证明 $M_*\ne0$ 且
$v_p(M_*)=4-p$。本条证明对每个 $m\ge2$、$m\equiv2\pmod3$，

$$\boxed{M_m/M_*\in\mathbb Q_p,
\qquad v_p(M_m)\in\mathbb Z\cup\{\infty\}.} \tag{711.1}$$

这来自同一有理 CM 点、原正商的微分和**所有阶共用的一个常数**；
不从复数非消失、有限数值或未经证明的整 cotangent 比较推断。
结合 R710 的平方下降，还证明这些实际 jets 全部包含在一个固定
有限未分歧 $p$ 进域内。旧文中避免未经证明的未分歧断言仍是必要的；
这里新增第 2–5 节的原商/参数/端点证明后才作此加强。

令 $j_*=(p-2)/3$，

$$b_*=[V^{j_*}]P_p(V)=\frac{p^{p-4}M_*}{(p-2)!}\in\mathcal O^\times.$$

则完整归一原函数满足

$$\boxed{\widetilde P_p(V):=P_p(V)/b_*\in\mathbb Z_p\langle V\rangle,}$$

且在原粗参数 $v=(a-1)/p^3$ 中同样属于
$\mathbb Z_p\langle v\rangle$。换参模 $p$ 精确为 $V=(3/8)v$。

在 $p=137147$，R710 的实际残差最低次数三由此给出一个真正的
$\mathbb Z_p$ 上的二次余因子：原标量 Abel 零在 $v_p(a-1)>3$
开盘内精确满足

$$v\bigl(v^2+A v+B_0\bigr)=0,\qquad A,B_0\in p\mathbb Z_p,$$

其中

$$\boxed{v_p(B_0)=1+v_p(M_2).} \tag{711.2}$$

若能进一步证明这个实际 $M_2$ 为 $p$ 单位，则二次式为
Eisenstein，其两个根都有 $v_p(a-1)=7/2$。于是原 primitive 在
实际 $\mathbb Q_p$ 深盘 $v_p(a-1)\ge4$ 只有中心零。
**本条没有证明该单位条件，也没有以此宣布原高度或 Serre 候选排除。**

## 2. 不依赖 Mordell–Weil 非消失的有理几何

R616 的原几何给

$$X_1=Z_p,\qquad j=6912a^3(1-a^3),\qquad
c_0:a=0,\quad c_1:a=1,$$

并保留同一个指定的 $\mu_6$ 稳定 CM 项链。两个点都在
$X_1(\mathbb Q)$；$s=a-1$ 是 $c_1$ 处的 $\mathbb Q$ 有理一次参数。
原实际商

$$q_1:J_{X_1}\longrightarrow A_{\theta,1},\qquad
f(x)=q_1[x-c_0]$$

在 $\mathbb Q$ 上定义。有理同源分母可先用一个非零整数统一清除，
只改变下文共同的非零常数。此处需要商的存在及其原微分识别，
不需要 $\beta=f(c_1)$ 非挠，也不需要 $A(\mathbb Q)$ 的秩结论。

设 $F$ 为实际正形式
$g_{\theta,+}=\operatorname{AI}_{\mathbb Q(\sqrt{-3})/\mathbb Q}
(\Psi_\theta\kappa_4)$ 的实 Hecke 系数域。其 Fourier 系数来自
共轭理想对的和。因为 CM 基域类数为一，理想生成元在
$K=\mathbb Q(\zeta_3)$；有限部分只含 $\theta$ 的阶整除 $p+1$
的值、三次角色 $\kappa_4$ 的值，以及原 $\epsilon_3$ 的符号。
$6\mid p+1$，所以这些数均在 $\mathbb Q(\zeta_{p+1})$ 中。
共轭理想配对使 Fourier 系数为实数，故

$$F\subseteq\mathbb Q(\zeta_{p+1})^+.$$

只用此包含关系即可，不需要把某个秩结论反过来用于确定系数域。
由于 $p$ 不整除 $p+1$，圆分扩张在 $p$ 未分歧；其算术 Frobenius
由 $p\equiv-1\pmod{p+1}$ 给出复共轭，故在实子域上为恒等。
所以 $p$ 在 $F$ 完全分裂，

$$F\otimes\mathbb Q_p\simeq\prod_{\sigma:F\hookrightarrow\mathbb Q_p}\mathbb Q_p.$$

相应 $\sigma$-特征不变微分可选为
$\omega_\sigma\in H^0(A_{\mathbb Q_p},\Omega^1)$，定义在
$\mathbb Q_p$ 上。选择与 R575/R705 实际正 tame 线对应的那个嵌入。
因为 $f-\beta$ 是在 $\mathbb Q$ 上定义的形式态射，特征零形式群
对数的系数也在 $\mathbb Q$，所以

$$J_\sigma(s):=\omega_\sigma\!\left(
\log(f(c_1+s)-f(c_1))\right)\in s\mathbb Q_p[[s]]. \tag{711.3}$$

这里使用的是群单位附近的形式增量，不是声称常数
$\log_p\beta$ 是有理代数数；即使 $\beta$ 为挠点，(711.3) 仍成立。

## 3. 所有阶共用同一个 Kodaira–Spencer 标量

R575 (575.13)、(575.24)–(575.25) 识别的正商正是
$A_{\theta,1}$，其实际 tame 线是
$F_1=H_0-4\zeta^2H_2$。R592 的原 Hodge/flat 变换是

$$\mathcal F_{\rm flat}=u_1^2\mathcal F_t,\qquad
dz_{\rm f}=\frac{b}{u_1^2}dt.$$

因此

$$\mathcal F_{\rm flat}\,dz_{\rm f}=b\mathcal F_t\,dt.$$

Kodaira–Spencer 把 $\omega^{\otimes2}$ 送到固定非零杯积规范倍数
的 $b\,dt$。故存在一个与 $s$ 无关的非零常数 $c_\sigma$，使

$$q_1^*\omega_\sigma=c_\sigma\mathcal F_{\rm flat}\,dz_{\rm f},$$
$$\boxed{J_\sigma(s)=c_\sigma\mathcal I(z_{\rm f}(s)).} \tag{711.4}$$

二者在 $s=0$ 都取零，故积分后没有自由常数。这个比较保持原
Hodge 基、原商、正 CM 嵌入和原参数。$c_\sigma$ 不被假定为单位；
更不允许对不同 $m$ 分别更换一个常数。

## 4. 未缩放的整个 flat/coarse 换参在有理系数域内

本节只证明所属域，暂不声称未缩放系数全整。
R592 的 Gauss–Manin 矩阵为

$$
\frac d{dt}\binom\omega\eta=
\begin{pmatrix}
-t^2/(4t^3+27)&-9/(2(4t^3+27))\\
-3t/(2(4t^3+27))&t^2/(4t^3+27)
\end{pmatrix}\binom\omega\eta.
$$

它的系数在 $\mathbb Q[[t]]$。值为 $I_2$ 的基本解矩阵通过唯一
特征零系数递推得到，故全部系数在 $\mathbb Q$。
矩阵中各幂次的模三类别以及初值还给

$$u_1\in\mathbb Q[[t^3]],\quad v_1\in t^2\mathbb Q[[t^3]],
\quad u_2\in t\mathbb Q[[t^3]],\quad v_2\in\mathbb Q[[t^3]].$$

这些包含关系可直接代入微分方程验证；初值和唯一性保证全级数
满足，而不只是在有限阶检查。因而

$$z_{\rm f}=u_2/u_1=tZ(t^3),\quad Z(T)\in\mathbb Q[[T]],
\quad Z(0)=-1/6.$$

由原两个 $j$ 公式，设 $R(a)=a^3(1-a^3)$，严格有

$$\frac{t^3}{4t^3+27}=R(a),\qquad
t^3=\frac{27R(a)}{1-4R(a)}.$$

在 $a=1+s$ 处，右边在 $s\mathbb Q[[s]]$，线性项为 $-81s$。
因此

$$\xi:=z_{\rm f}^3=\Xi(s)\in s\mathbb Q[[s]],\qquad
\Xi'(0)=(-1/216)(-81)=3/8,$$

且形式逆 $s=\Xi^{-1}(\xi)$ 同样在 $\xi\mathbb Q[[\xi]]$ 中。
所有整性和收敛精度仍由 R710 的实际缩放给出；本节没有把这个
有理级数误称为无分母级数。

把 (711.3) 与 (711.4) 通过这个完整有理逆变换复合，得到

$$c_\sigma\sum_{j\ge1}\frac{M_{3j-1}}{(3j)!}\xi^j
=J_\sigma(\Xi^{-1}(\xi))\in\mathbb Q_p[[\xi]].$$

所以

$$\boxed{c_\sigma M_{3j-1}\in\mathbb Q_p\quad(j\ge1).} \tag{711.5}$$

高阶阶乘当然可能被 $p$ 整除，但它是有理数；这不妨碍所属域
结论，并且没有被从赋值估计中删除。

## 5. 原非零端点固定共同赋值类

R705 给 $M_*\ne0$，所以 (711.5) 允许除以同一个非零端点：

$$\frac{M_m}{M_*}=
\frac{c_\sigma M_m}{c_\sigma M_*}\in\mathbb Q_p.$$

由 $v_p(M_*)=4-p\in\mathbb Z$，得到 (711.1)。同样可见
$v_p(c_\sigma)\in\mathbb Z$，但这里没有该整数的大小或单位性
结论。所有实际 quotient 微分赋值仍须加上它。

为了说明未分歧断言的精确依据，再用 R710 已证明的
$M_*^2\in K_0$，其中 $K_0$ 有限未分歧。令
$u_*=p^{p-4}M_*$，则 $u_*^2\in\mathcal O_{K_0}^\times$。
奇剩余特征下，单位的平方根只需至多二次未分歧扩张：先在剩余域
添平方根，再以单位导数 $2u$ 作 Hensel 提升。
故 $K_*=K_0(u_*)$ 未分歧，而全部 $M_m$ 由 (711.1) 都在 $K_*$。

这一步下降的是原已标记 jets；它不表示任意 CM 模形式值都未分歧。
所用关键新增输入是原 $\mathbb Q$ 有理 Abel 系数直线和实际非零
整数赋值端点。没有该输入，R710 的半整数格才是合法结论。

## 6. 完整整系数原函数与改进后的零残差界

R710 已证明 $P_p=\sum b_jV^j\in\mathcal O\langle V\rangle$，
$b_*$ 是单位。由所有 $M_m/M_*$ 在 $\mathbb Q_p$，各个
$b_j/b_*$ 也在 $\mathbb Q_p$。其赋值非负并趋于无穷，故

$$\widetilde P_p=P_p/b_*\in\mathbb Z_p\langle V\rangle.$$

第 4 节的完整有理换参说明粗缩放变换
$V=\Xi(p^3v)/p^3$ 的系数在 $\mathbb Q_p$。R710 又已证明它
属于整数 Tate 代数，所有非线性系数的赋值严格正。因此它实际是
$\mathbb Z_p$ 上的 Tate 自同构，并有

$$V\equiv(3/8)v\pmod p.$$

归一粗函数
$\widetilde P_p^{\rm coarse}(v)=\widetilde P_p(\Xi(p^3v)/p^3)$
也在 $\mathbb Z_p\langle v\rangle$ 中，拥有同一个剩余最低次数。

对 R705 的有限实际前缀，如果
$C_{p+2-m}C_{p-m-1}=0\pmod p$，原平方同余先给
$v_p(M_m)\ge3/2-m$；结合整数赋值，现可严格加强为

$$\boxed{v_p(M_m)\ge2-m.} \tag{711.6}$$

在 $p=137147$，R706/R710 的实际值因此给

$$v_p(M_2)\ge0,\qquad v_p(M_5)\ge-3,\qquad v_p(M_8)=-7.$$

相应 $\widetilde P_p^{\rm coarse}$ 的一次、二次系数在
$p\mathbb Z_p$，三次系数为单位，所有系数整。这个加强仍不能
决定 $M_2$ 是单位、可被 $p$ 整除还是零。

## 7. 真实剩余二次式及深盘的准确条件

在 $p=137147$，对完整的 $\mathbb Z_p$ 粗函数作 R710 已证明的
Weierstrass 构造，得到

$$\widetilde P_p^{\rm coarse}(v)
=W_3(v)U(v),\qquad U\in\mathbb Z_p[[v]]^\times,$$

其中 $W_3$ 首一，所有低次系数被 $p$ 整除。原函数常数为零，
$U(0)$ 为单位，故 $W_3(0)=0$，从而严格写成

$$W_3(v)=v(v^2+A v+B_0),\qquad A,B_0\in p\mathbb Z_p.$$

原粗函数的一次系数只有线性换参贡献，精确为

$$[v]\widetilde P_p^{\rm coarse}
=\frac{3}{8}\frac{pM_2}{6b_*}
=\frac{pM_2}{16b_*}.$$

另一方面该系数是 $B_0U(0)$。因 $U(0),16,b_*$ 都为单位，
得到 (711.2)，包括 $M_2=0$ 时两边都为 $+\infty$ 的约定。

若 $v_p(M_2)=0$，则 $v_p(B_0)=1$，二次式
$v^2+Av+B_0$ 是 Eisenstein。其两根均有赋值 $1/2$，所以原
$s=p^3v$ 的赋值为 $7/2$。它们既不属于 $\mathbb Q_p$，也不
属于 $v_p(s)\ge4$ 的实际候选区域。中心零此时简单，故该区域
没有非零原标量 Abel 零。

若 $v_p(M_2)\ge1$，则仅能断言 $B_0\in p^2\mathbb Z_p$；
二次式的根可能在实际深盘内，必须继续计算同一 $A,B_0$ 或证明
相应原系数界。若 $M_2=0$，则 $B_0=0$，真实特征零首阶可以
是二或三，仍不能由剩余首阶三直接决定。

整个论证仅处理原实际商的一个 Abel 线性泛函。即便未来验证
$M_2$ 为单位完成这里的局部零隔离，R634/R699 的真实高度外积
仍含同一 $\Lambda$、CM 对数常数和 $\ell_h$。本条没有把这些
未知输入删去，也没有把两个可能 Abel 零直接计为已排除。

## 8. 依赖与证明范围

本条前六节不需要 $L'(g_{-1,+},1)L(g_{-1,-},1)\ne0$：使用的
是 R575 已识别的原商、R616 的原有理 CM 点几何、R592 的有理
Gauss–Manin 变换，以及 R705 的实际端点非零。
若进一步用 R682 的已归一 $t_i$、共同首阶和真实高度外积，仍须
保留 R616 的上述解析非消失前提。一般素数的该前提、例外素数
的 $M_2$ 单位性，以及原高度首项都没有在本条中得到证明。
