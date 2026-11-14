# R522 — 三度共同伴随的完整偶张量与同一 S/T 正六次测试

日期：2026-11-14。**状态：已证明。** 原六 sigma 中存在一个范数仅为
三的共同伴随 $H_0=\xi_1-\xi_3+x$。它同时正交于原 $Y,W,W'$，
并是原三阶几何的特征行。这个方向的整个 odd theta 空间只有一个
偶分量，因此一个显示的正六次测试就对其余五个真实输出给
**全部测度身份**。特别，同一测试同时返回原 $S$ 和两条原 $T$
观察，并被原 $W$ 核、三阶几何原样保留。

在原五深一单位网格上，该同一测试的中央仍严格非零，赋值为
$5n$。完整第五阶只含原 sigma 的正第一矩；log 质量项整条为零。
三个原观察的第五阶及一条单位差也全部算出。这里的非零子管与
完整中央之间仍保准确补域，没有由边际身份删掉混管条件。

## 1. 同一原六输入与小共同伴随框架

沿用 R493、R510、R516 的原规范
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=3+\omega,\quad\bar\gamma=2-\omega,\quad b=17,
$$
$$
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1,\qquad
\rho=-\nu_\sigma^{\otimes6}/84.
\tag{1}
$$
原变量次序是 $\xi=(\xi_1,\xi_2,\xi_3,x,c,d_0)^t$。
三个完整观察是
$$
\begin{aligned}
Y&=(\delta,2\delta,\gamma,\bar\gamma,1,2)\xi,\\
W&=(\delta,2\delta,\gamma,\bar\gamma,3\delta,4)\xi,\\
W'&=(4+4\omega,2+4\omega,4+4\omega,0,4+2\omega,4)\xi.
\end{aligned}
\tag{2}
$$
令 $W_2=W\mathcal T^2=-\omega^2W-\omega W'$。
原边际准确为
$$
Y_*\rho=\nu_S,\qquad
W_*\rho=6\delta\nu_T,\qquad
W'_*\rho=0,\qquad
(W_2)_*\rho=-6\delta\omega^2\nu_T.
\tag{3}
$$

取以下三个**原六输入行**：
$$
\boxed{
\begin{aligned}
H_0&=(1,0,-1,1,0,0),\\
H_1&=(-1,2,\omega,1+\omega,0,0),\\
H_2&=(-2-40\omega,18-18\omega,2-38\omega,
                         4+2\omega,42,84+126\omega).
\end{aligned}}
\tag{4}
$$
它们分别作用于 $\xi$。直接完整 Gram 计算给
$$
\boxed{
\operatorname{span}(H_0,H_1,H_2)
=\operatorname{span}(Y,W,W')^\perp,\qquad
\operatorname{Gram}(H_0,H_1,H_2)
=\operatorname{diag}(3,7,18144).
}
\tag{5}
$$
特别 $H_0$ 的正交性也可由
$\delta-\gamma+\bar\gamma=0$ 及 $W'$ 的第一、第三系数相等直接看出。

完整框架
$$
\mathcal F=(Y,W,W',H_0,H_1,H_2)
\tag{6}
$$
的观察块仍是 R516 的原三乘三 Gram，两个块的交叉项全零。
其行列式准确为
$$
\boxed{\det\mathcal F=-108864-72576\omega
=-36288(3+2\omega).}
\tag{7}
$$
完整矩阵、逆、Gram 均存于证书。
因 $36288=2^6\cdot3^4\cdot7$，(6) 在当前所有普通处是整自同构；
没有遗忘原六输入的任何坐标。

原 R493 的真正三阶矩阵还满足
$$
\boxed{
H_0\mathcal T=\omega^2H_0,\qquad
H_1\mathcal T=H_1,\qquad H_2\mathcal T=H_2.
}
\tag{8}
$$
这将共同伴随的三阶作用完整对角化，且保原观察块的真实作用。
本篇不因此给 $H_2$ 猜测单层核心。

## 2. 整个 H0 方向确为标准 odd degree3

在 (6) 中把 $H_0$ 的生成变量记为 $z$，其余五个生成变量记为
$\boldsymbol t$。原来源在 $z$ 方向的三个非零系数为 $1,-1,1$。
其余五个输出与 $H_0$ 的完整 Hermitian 交叉全零。
所以沿 $z$ 的周期变换没有隐藏 $\boldsymbol t$ 项，其半特征
正是三个原奇 sigma 的乘积，即标准 odd 半特征。

因此完整联合在这一方向属于
$$
\boxed{\mathcal S_3^{\rm odd}\otimes V_{\rm rest}.}
\tag{9}
$$
$V_{\rm rest}$ 是其余五个真实输出的全部系数空间；
观察块中的交叉极化原样保留，不必假定它为五个独立一维空间。
(9) 不是只对某条边际的维数判断。

该三维空间的完整基可取
$$
\sigma(z)^3,\qquad x_\wp(z)\sigma(z)^3,\qquad
B_3(z):=-y_\wp(z)\sigma(z)^3
       =\frac{\sigma(2z)}{2\sigma(z)}.
\tag{10}
$$
这里 $y_\wp=x_\wp'/2$，与原
$\sigma(2z)=-2y_\wp(z)\sigma(z)^4$ 的规范相同。
前两项为奇函数，第三项为偶函数，且
$$
\boxed{B_3(z)=1+\frac{3b}{10}z^6+O(z^{12}).}
\tag{11}
$$
例如由 $\sigma(z)=z+bz^7/210+\cdots$ 直接作 (10) 的商，
第六系数为 $(2^6-1)b/210=3b/10$。

$B_3$ 的 Amice 变换整且质量为一：将 sigma 的 Amice 写为
$\Omega T U(T)$、$U(0)=1$，(10) 的商等于
$(1+T/2)U(2T+T^2)/U(T)$。在 $p>2$ 时它是整卷积单位。

## 3. 保完整其余五轴的偶张量身份

令 $\bar\rho$ 是真正忘去 $H_0$ 的五输出推前，定义物理反射
$$
R_0=I-\frac23\bar H_0^{\,t}H_0.
\tag{12}
$$
它固定 (6) 的其他五行，把 $H_0$ 变为 $-H_0$。
由 (9)–(11)，取 $z$ 的偶部分准确得到整个来源身份
$$
\boxed{
\frac{\rho+(R_0)_*\rho}{2}
=\nu_{B_3}\otimes\bar\rho.
}
\tag{13}
$$
$B_3(0)=1$ 保证这里没有未定绝对标量。
由于 (9) 的整个偶子空间只有这一条线，(13) 是完整函数和
完整测度身份，不是有限 jet 相合。

因此对任意偶连续函数 $f(H_0)$、任意其余五输出的连续测试
$g(Y,W,W',H_1,H_2)$，严格有
$$
\boxed{
\int f(H_0)g\,d\rho=\nu_{B_3}(f)\,\bar\rho(g).
}
\tag{14}
$$
允许 $g$ 含这些五输出的任意真实紧开条件，包括混合 $Y/W$
管；(14) 不允许在 $g$ 中再暗含一个未运输的 $H_0$ 条件。

特别由 (11)，
$$
\boxed{
(\text{忘 }H_0)_*
 \left\{\frac{H_0^6}{216b\Omega^6}\rho\right\}
=\bar\rho.
}
\tag{15}
$$
其中 $216=6!\cdot3/10$。这是同时解开原两个完整边际要求的
明确正次数测试，也保比两个边际更多的五变量来源。

## 4. 真实 H0 核与单位正测试

现有 ray 给 $g_\pi\equiv1\bmod6$，故 entire
$\mathcal S_3^{\rm odd}$ 的完整 Heisenberg 交织为 scalar。
真实非零锚 $\sigma(\delta z)$ 属于同一标准 odd 空间；
固定普通单位 $\delta$ 的拉回与原 sigma 核交换，其实际核心为
$\beta=-\lambda$。于是绝对标量已付：
$$
\boxed{
K_{3,H_0}=-I,\qquad
\rho|_{H_0\in p^n}
=\beta^n[I_{\rm rest},\kappa^n]_*\,\rho.
}
\tag{16}
$$
此处包含 whole odd 半特征及绝对号，不只给 projective 交织。

将 (16) 用于第六矩，定义
$$
\boxed{
q_p(H_0)=
\frac{H_0^6}{216b\Omega^6(1+\lambda\kappa^6)},\qquad
d\rho^\sharp={\bf1}_{H_0\ {\rm unit}}q_p(H_0)\,d\rho.
}
\tag{17}
$$
新增分母模 $p$ 为 $1$。准确有
$$
\boxed{(\text{忘 }H_0)_*\rho^\sharp=\bar\rho.}
\tag{18}
$$
等式的系数为一：第六矩的 $H_0$ 深部分是
$-\lambda\kappa^6$ 倍全第六矩，故单位部分为
$1+\lambda\kappa^6$ 倍，不是质量因子 $1+\lambda$。

同一证明适用于原四个实际来源 $(u,v,z,h)$。
构造这些来源的 $W$ 平移、$W$ 核及 $W'/2$ 核都与 $H_0$
正交，严格保 (9) 的标准 degree3 方向；
无需把 $H_0$ 一并加到原 quarter 覆盖。
第一 $Y$、第一 $W$ 的实际 CM 算术投影也与该方向正交。
因此 (13)、(18) 保原 S/new/Href/T 的完整条件行。
参考的未知导数及非零质量仍保持原值，没有被此测试赋零。

另外 $H_1$ 是标准 odd degree7；现有 ray 给
$g_\pi\equiv1\bmod14$，真实 $\sigma(\gamma z)$ 锚给其 whole
核心同样为 $\beta$。它与 $H_0,Y,W,W'$ 全正交，故可在 (18)
另附 $H_1$ 单位条件，准确再乘 $1+\lambda$。
这也对原四态成立。此推论不使用尚未支付的 $H_2$ 单层核。

## 5. 同一测试的原三条算术行及三阶几何

由 (3)、(18)，完整第一测度是
$$
\boxed{
Y_*\rho^\sharp=\nu_S,\qquad
W_*\rho^\sharp=6\delta\nu_T,\qquad
W'_*\rho^\sharp=0,\qquad
(W_2)_*\rho^\sharp=-6\delta\omega^2\nu_T.
}
\tag{19}
$$
因此对全部 Mellin 变量，
$$
\boxed{
\begin{aligned}
\int_{Y\ {\rm unit}}\langle Y\rangle^{du}\,d\rho^\sharp&=J_S(u),\\
\int_{W\ {\rm unit}}\langle W\rangle^{du}\,d\rho^\sharp&=6\delta J_T(u),\\
\int_{W_2\ {\rm unit}}\langle W_2\rangle^{du}\,d\rho^\sharp
 &=-6\delta\omega^2 J_T(u).
\end{aligned}}
\tag{20}
$$
它们使用同一个原来源、同一个正六次测试及同一个 $H_0$ 单位条件。
若再附 $H_1$ 单位，三式均准确再乘 $1+\lambda$。
原 $J'_S=J'_T=0$ 因而消掉这些相应的完整中央行。

(8) 使整个 (17) 在原 $\mathcal T$ 下不变：$H_0$ 乘
$\omega^2$ 不改变六次幂或单位域。它也被旧 $W$ 核的物理
缩放原样保留，因为 $H_0\perp W$。

令 $h=\omega^2\mathcal T_*\rho$ 是原真实二挠态，同样定义
$h^\sharp={\bf1}_{H_0\ {\rm unit}}q_p(H_0)h$。
完整边际为
$$
\boxed{
\begin{array}{c|rrrr}
 &Y&W&W'&W_2\\ \hline
\rho^\sharp&S&6\delta T&0&-6\delta\omega^2T\\
h^\sharp&\omega^2S&0&-6\delta\omega T&6\delta\omega^2T .
\end{array}}
\tag{21}
$$
表中每项都是整条来源，不只质量。
并且 $h^\sharp$ 保原完整 $W$ scalar 核
$\beta[\kappa,I_5]$，所有纯 $W$ 伴随条件都照旧保留。

## 6. 原五深一单位网格与完整质量零

保原实际独立域
$$
\mathcal D_n=\{\xi_1,\xi_2,\xi_3,c,d_0\in p^n\mathcal O,\
                        x\ {\rm unit}\},\qquad n\ge1.
\tag{22}
$$
在此 $H_0,H_1,Y,W,W_2$ 都是单位，而 $W'\in p^n$。
$H_0=x+\xi_1-\xi_3$，故 (17) 的单位指示在此自动成立。

令五个深输入共同缩放为 $T$，自由 $x$ 不动，置
$$
Z=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+c+2d_0,\qquad
L=\xi_1-\xi_3.
$$
对 $T\in p\mathcal O$ 定义
$$
\mathcal A_Y(T)=
\frac{d}{216b\Omega^6(1+\lambda\kappa^6)}
\int_{x\ {\rm unit}}\int
 \log\langle\bar\gamma x+TZ\rangle(x+TL)^6
 \,d(-\nu_\sigma^{\otimes6}/84).
\tag{23}
$$
五个独立 sigma 的共同核心给
$$
\boxed{
C_{Y,n}:=\int_{\mathcal D_n}d\log\langle Y\rangle\,d\rho^\sharp
=\beta^{5n}\mathcal A_Y(\kappa^n).
}
\tag{24}
$$

这里还有一条完整质量身份：
$$
\boxed{\rho^\sharp(\mathcal D_n)=0.}
\tag{25}
$$
因为测试只使用 $(\xi_1,\xi_3,x)$，剩余独立
$(\xi_2,c,d_0)$ 的深 sigma 质量逐个为零。
相同原因使 (23) 中
$\log\langle x\rangle+\log\langle\bar\gamma\rangle$
的整条贡献消失。因此没有被省略的 log 加权质量项；
固定单位尺度的 log 也不会改变 (24)。

## 7. 完整第五阶、全尾与当前 ray 的单位性

按五个深输入次序，设
$$
\boldsymbol z=(\delta,2\delta,\gamma,1,2),\qquad
\boldsymbol l=(1,0,-1,0,0).
$$
完整混合矩系数为
$$
C_j=j!(5-j)!\!
\sum_{\substack{I\subset\{1,\ldots,5\}\\|I|=j}}
\prod_{i\in I}z_i\prod_{i\notin I}l_i.
\tag{26}
$$
精确计算全部 $32$ 个子集给
$$
\boxed{
(C_0,C_1,C_2,C_3,C_4,C_5)
=(0,0,0,-48-96\omega,\ 384+480\omega,\ -4320-1440\omega).
}
\tag{27}
$$
总次数小于五全为零；第五阶恰由每个原 sigma 的第一矩组成。
在 log 的展开中 $j=3,4,5$ 给
$$
A_5=\sum_{j=1}^5
 \frac{(-1)^{j-1}}{j\bar\gamma^j}
  \binom6{5-j}C_j
=\frac{309216-480000\omega}{16807}.
\tag{28}
$$
记
$$
\boxed{
a_Y=-\frac{A_5}{84\cdot216}
=\frac{-3221+5000\omega}{27\cdot7^6},
\qquad
Na_Y=\frac{1021}{3^5\cdot7^7}.
}
\tag{29}
$$
原 sigma 的正第一单位矩准确为
$I_1=(1+\lambda\kappa)\Omega$。
于是 (23) 的完整第五阶为
$$
\boxed{
[T^5]\mathcal A_Y
=\frac db\,a_Y\,
 \frac{1+\lambda\kappa}{1+\lambda\kappa^6}.
}
\tag{30}
$$
(30) 是准确式，不只是模 $p$ 同余，且无未知 log 矩。

$1021$ 是素数，当前 $p\equiv7\bmod64$ 排除 $p=1021$；分母素因子 $3,7$
也已在原固定坏集之外。因此 (30) 在整个现有普通 ray 都是单位，
无需使用 R518 的大素数门或再增加射线。
这不改变已经采用的任何更细共同 ray。

测试次数只有六，所有系数整，余项的 log 分母不超过当前次数。
因此
$$
v_p([T^r]\mathcal A_Y)\ge-\lfloor\log_pr\rfloor.
\tag{31}
$$
原五 sigma 的同时 $\mu_6$ 型还给
$\mathcal A_Y(\zeta T)=\zeta^5\mathcal A_Y(T)$，
故只出现 $r\equiv5\bmod6$ 的幂。
对 $p\ge71,n\ge1$，所有 $r>5$ 的项赋值严格大于 $5n$。
从而
$$
\boxed{v_p(C_{Y,n})=5n,\qquad C_{Y,n}\ne0
\quad\text{对每个 }n\ge1.}
\tag{32}
$$

## 8. 同一网格上两条 T 观察及准确局部差

在 (23) 中分别以 $W,W_2$ 的实际五输入行和自由 $x$ 系数
替换 $Y$，记相应函数为 $\mathcal A_W,\mathcal A_{W_2}$。
质量仍由 (25) 整条消失，所有常数 log 都为零。
脚本用同一完整 (26) 计算，得到
$$
\boxed{
a_W=6\delta a_Y,\qquad
a_{W_2}=\frac{-1990+3350\omega}{9\cdot7^6}.
}
\tag{33}
$$
它们的第五系数均是
$(d/b)a_L(1+\lambda\kappa)/(1+\lambda\kappa^6)$。

所以第一条归一差的第五阶严格消去：
$$
[T^5]\left(\frac{\mathcal A_W}{6\delta}-\mathcal A_Y\right)=0,
$$
$$
v_p\left(\frac{C_{W,n}}{6\delta}-C_{Y,n}\right)\ge11n
\quad\text{若该差非零；为零时也成立。}
\tag{34}
$$
这里使用实际 $\mu_6$ 型及 (31)，没有把高阶系数预认成单位。

第二条原 T 归一差有显示单位：
$$
\boxed{
\Delta=
\frac{a_{W_2}}{-6\delta\omega^2}-\frac{a_W}{6\delta}
=\frac{272-320\omega}{81\cdot7^4},
\qquad N\Delta=\frac{256}{3^7\cdot7^5}.
}
\tag{35}
$$
因此
$$
\boxed{
v_p\left(\frac{C_{W_2,n}}{-6\delta\omega^2}
                       -\frac{C_{W,n}}{6\delta}\right)=5n.
}
\tag{36}
$$
完整全域中，(20) 对应的两条 T Mellin 函数本来就相等；
所以 (36) 迫使其实际补域给出反号补偿。
本篇不把这种已知全域恒等与一个非零子域值相混淆。

## 9. 同一个测试送到原 h 的 W 深管

由 (8)、$Y\mathcal T=Y$ 及 $h=\omega^2\mathcal T_*\rho$，
置 $\mathcal E_n=\mathcal T\mathcal D_n$，有
$$
\boxed{
\int_{\mathcal E_n}d\log\langle Y\rangle\,dh^\sharp
=\omega^2C_{Y,n},\qquad v_p=5n,\qquad W\in p^n.
}
\tag{37}
$$
正六次测试与 $H_0$ 单位条件在这里**完全没有移动**。
$H_1$ 单位也保留，因为 (8) 的第二式成立。
原六输入条件仍是
$$
(\mathcal T^{-1}\xi)_j\in p^n\ (j\ne x),\qquad
(\mathcal T^{-1}\xi)_x\ {\rm unit}.
\tag{38}
$$
它们不会被单独一个 $W$ 深条件替代。

旧 $W$ 核保 (17) 的整测试，但它仍改变第一 $Y$ 权，
并须运输 (38) 的其余条件。相应物理矩阵是原
$I+(\kappa^r-1)\bar W^{\,t}W/72$；
$H_0,H_1,H_2$ 均被固定。
因此 (37) 支付了此前伴随测试本身的移动问题；
第一观察和实际补域的比较仍须在同一来源上继续。

## 10. 全部补域与已付接口

令
$\Gamma_Y=\{Y,H_0\ {\rm unit}\}$，
$\Gamma_W=\{W,H_0\ {\rm unit}\}$，
$\Gamma_{W_2}=\{W_2,H_0\ {\rm unit}\}$；
测试均用 (17) 的 $q_p$，不再把 $H_0$ 单位重复计入。
因为 $\mathcal D_n$ 包含于这三个真实域，准确有
$$
\boxed{
\begin{aligned}
J'_S(0)&=C_{Y,n}+
 \int_{\Gamma_Y\setminus\mathcal D_n}d\log\langle Y\rangle\,q_p\,d\rho,\\
6\delta J'_T(0)&=C_{W,n}+
 \int_{\Gamma_W\setminus\mathcal D_n}d\log\langle W\rangle\,q_p\,d\rho,\\
-6\delta\omega^2 J'_T(0)&=C_{W_2,n}+
 \int_{\Gamma_{W_2}\setminus\mathcal D_n}d\log\langle W_2\rangle\,q_p\,d\rho.
\end{aligned}}
\tag{39}
$$
若另附 $H_1$ 单位，则左边均再乘 $1+\lambda$，
$\mathcal D_n$ 的局部项不变，补域相应取真正交集。

新接口是 (13)、(18) 的完整五输出身份、(20) 的同一 S/T 正测试、
(30) 的正第一矩单位首项及 (37) 的未移动测试。
原三条补域并非同一个域；(34)–(36) 也没有让它们自动消掉。
主目标尚未由本篇完成。

## 精确证书与依赖

- [BigInt 完整框架、三度规范与全部第五阶脚本](../scripts/check-r522-common-degree3-positive-arithmetic-test.js)；
  [整个矩阵、逆、Gram、反射、混合矩与三个首项](../scripts/check-r522-common-degree3-positive-arithmetic-test.json)。
  同一主体已在当前 V8 实际执行。旧六输入几何、全部混合项和
  精确范数均通过；无浮点近似。
- [R493：原六 sigma、三阶几何和真实二挠态](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R510：原 W2/T 归一与全部伴随](R510-original-w2-companion-and-fifteen-axis-central-words.md)。
- [R516：同一三维共同伴随空间和原完整格](R516-original-rotated-common-companion-cores-and-word-intersections.md)。
- [R497：原普通周期、五深域和完整正矩规范](R497-original-degree918-positive-companion-and-six-sigma-arithmetic-grid.md)。
