# R1092 — 原 FM 截面在另外六个三挠点的精确 Cartier 值与单位性

**状态：已证明。** 本条在原固定曲线、原 Miller 归一和相对 Cartier 中给出一个新读数。它不把另外六个三挠点的值与原 $e$、$K_4$ 或原两条短障碍混同。

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126 / o1_theta。

## 1. 原对象与结论

沿用 [R1061](R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md) §§9、16、17、19、20 的原对象：
$$
E:\quad V^2=U^3-108,\qquad
\omega=\frac{dU}{2V},\qquad
C:\quad V^2=R^6-108,\quad q(R,V)=(R^2,V).
$$
设
$$
p=6k-1>3,\qquad m=\frac{p-1}{2}=3k-1,\qquad N=k-1.
\tag{1092.1}
$$
本课题原应用范围为 $p\ge41$。以下原 Cartier 恒等式实际上对所有满足 (1092.1) 的素数成立。

对 $P\in E[3]\setminus\{O\}$，令 $g_P$ 是原 Miller 函数，满足
$$
\operatorname{div}(g_P)=(-P)-p(P)+(p-1)(O),
\qquad
g_P=z_O^{p-1}(1+O(z_O)),
\tag{1092.2}
$$
其中 $z_O$ 是原微分切向为 $1$ 的整局部参数。因为 $pP=-P$，这正是 R1061 中的原函数，不是另选同除子的未定标截面。定义
$$
C_{\rm rel}(U^m g_P\omega)=\theta_P\,\omega^{(p)}.
\tag{1092.3}
$$
输入只在 $P$ 有至多 $p$ 阶极点，在 $O$ 整；Cartier 后只有一个可能的简单极点，其留数必为零，故 (1092.3) 的输出确实全纯且 $\theta_P$ 是标量。

在 R1061 的原 FM 参数中，
$$
\theta_P=\Phi(U^m)(F P).
\tag{1092.4}
$$
特别地，若 $P\in E(\mathbb F_p)$，这里没有相对 Frobenius 参数的偷换：$FP=P$。写原已固定截面
$$
\Phi(U^m)=U\,H_p(U^3),\qquad \deg H_p\le N.
\tag{1092.5}
$$

令 $a\in\mathbb F_p^\times$ 为唯一满足 $a^3=432$ 的元素，并令
$$
P=(a,18),\qquad
E_*:\quad Y^2=X^3-9X+9,\qquad
a_p(E_*)=p+1-\#E_*(\mathbb F_p).
$$
则有精确恒等式
$$
\boxed{\quad
\Phi(U^m)(P)=a\,H_p(432)=-a_p(E_*)\pmod p.
\quad}
\tag{1092.6}
$$
若进一步
$$
p\equiv2\ \text{或}\ 5\pmod9,
$$
则 $a_p(E_*)$ 是奇数，且不被 $p$ 整除。因此
$$
\boxed{\ H_p(432)\ne0.\ }
\tag{1092.7}
$$
原 $E[3]$ 中满足 $U^3=432$ 的全部六个点上的 $\Phi(U^m)$ 都是单位。

这里原两点 $U=0$ 仍有 $\Phi(U^m)=0$；其一阶读数 $e$ 与四阶读数 $K_4$ 的非零问题不由 (1092.7) 自动解决。

## 2. 同一原三挠点的 Tate 规范与 Miller 函数

原三除式为
$$
\psi_3(U)=3U(U^3-432).
$$
故另外六个三挠点恰为
$$
U^3=432,\qquad V=\pm18.
\tag{1092.8}
$$
因 $p\equiv2\pmod3$，立方在 $\mathbb F_p^\times$ 上双射，所以所选 $P=(a,18)$ 是实际 $\mathbb F_p$ 三挠点。

置
$$
W=U-a,\qquad v=18,\qquad t=\frac{a^2}{6}.
$$
直接由 $a^3=432$ 得
$$
t^2=12a,\qquad t^3=48v,\qquad tv=3a^2.
\tag{1092.9}
$$
原椭圆曲线变成
$$
V^2=W^3+\frac{t^2}{4}W^2+tvW+v^2,
\qquad P=(0,v).
\tag{1092.10}
$$
令
$$
\ell_+=V-v-\frac t2W,\qquad
\ell_-=V+v+\frac t2W.
$$
它们满足
$$
\ell_+\ell_-=W^3,\quad
\operatorname{div}(\ell_+)=3(P)-3(O),\quad
\operatorname{div}(\ell_-)=3(-P)-3(O).
\tag{1092.11}
$$
其中 $\ell_+=0$ 正是 $P$ 处的三重切线。因此
$$
g_P=\frac{W}{\ell_+^{2k}}.
\tag{1092.12}
$$
其除子由 $6k=p+1$ 立即得到 (1092.2)。在原点
$W=z_O^{-2}+\cdots$、$V=-z_O^{-3}+\cdots$，
$\ell_+=-z_O^{-3}+\cdots$，且 $2k$ 为偶数，所以 (1092.12) 的首项确为 $+z_O^{p-1}$。没有待定的 $\mathbb F_p^\times$ 标量。

作为同归一的交叉核对，$C_{\rm rel}(g_P\omega)=\omega^{(p)}$：输出全纯，原点的合法 $p-1$ 阶 Cartier 读数为 $1$。这就是 R1061 中 $\Phi(1)=1$ 的同一个规范。

原双覆盖保持为
$$
C:\quad R^2=W+a;
\tag{1092.13}
$$
不得把它改成 $R^2=W$。后一替换会改变本条实际 Picard 输入。

## 3. 原三挠 étale cover 与真实椭圆商

在 $C$ 上取由 $q^*(P-O)$ 给出的三挠 étale cover。其函数域可写成
$$
x^3=\ell_+,\qquad z^3=\ell_-,
\qquad xz=W,\qquad R^2=xz+a.
$$
于是其仿射方程为
$$
xz=R^2-a,\qquad z^3-x^3-txz=2v.
\tag{1092.14}
$$
这里 $q^*(P-O)\ne0$，因为 $q_*q^*=[2]$ 且 $P$ 的阶为 $3$。因此正规化后的覆盖连通，次数为 $3$，无分歧，属为 $4$。它是原固定 $C$ 的指定三挠覆盖，不是另一个同属曲线。

定义原两条非平凡角色微分
$$
u=\frac{x}{R}\,\omega,\qquad
\nu=\frac{z}{R}\,\omega.
\tag{1092.15}
$$
它们全纯：$R=0$ 处的简单分母被 $\omega$ 的分歧零抵消；在原 $O$ 上，$x,z,R$ 的极阶相同；其余点没有极点。

覆盖具有实际反射
$$
\iota(x,z,R)=(-z,-x,R).
$$
它在底椭圆曲线上诱导 $V\mapsto -V$，因而交换 $u,\nu$。置
$$
h=z-x,\qquad y=(3h-t)R.
$$
其商是实际椭圆曲线
$$
E^\dagger:\quad
y^2=(3h-t)(-h^3+3ah-at+2v),
\qquad
\omega^\dagger=\frac{dh}{2y}.
\tag{1092.16}
$$
事实上 $x,z$ 可由 $h,R$ 的一个二次方程恢复，$\iota$ 是其非平凡自同构。下面的显式模型证明该商光滑且属为 $1$。

令 $D=d/\omega$。由 (1092.11) 得
$$
Dx=z^2-\frac t3x,\qquad
Dz=x^2+\frac t3z,
$$
故
$$
D h=-\frac{3h-t}{3}(x+z).
$$
从而实际微分拉回为
$$
\boxed{\quad
\pi^*\omega^\dagger=-\frac{u+\nu}{6}.
\quad}
\tag{1092.17}
$$
这个 $-1/6$ 是原模型直接算出的数，不是由属或同源类选定的任意比例。

## 4. 相对 Cartier 与原 $\Phi$ 值的精确比较

在 (1092.14) 中，$p+1=6k$ 给出
$$
\frac{z/R}{(x/R)^p}
=\frac{xz\,R^{p-1}}{x^{p+1}}
=(W+a)^m\frac{W}{\ell_+^{2k}}
=U^m g_P.
\tag{1092.18}
$$
因此
$$
C_{\rm rel}(\nu)=\theta_P\,u^{(p)}.
$$
反射 $\iota$ 与相对 Cartier 相容，且交换 $u,\nu$，所以同样
$$
C_{\rm rel}(u)=\theta_P\,\nu^{(p)}.
$$
应用到 (1092.17)，并利用有限可分商的 Cartier 自然性，得到
$$
C_{\rm rel}(\omega^\dagger)
=\theta_P\,(\omega^\dagger)^{(p)}.
\tag{1092.19}
$$
因而 $\theta_P$ 精确等于这个实际椭圆商在微分 $\omega^\dagger$ 下的 Hasse 系数。

这里全部参数 $a,v,t$ 都在 $\mathbb F_p$，故 (1092.19) 无额外的常数 $p$ 次根。一般参数时必须保留相对 twist；本条选择实际 $\mathbb F_p$ 点支付了该区别。

## 5. 实际椭圆商到固定 $E_*$ 的明确二次扭曲

使用 (1092.9)，置
$$
r=\frac{6h}{t},\qquad \lambda=-\frac{tv}{9}=-\frac{a^2}{3}.
$$
方程 (1092.16) 严格化为
$$
y^2=\lambda(r-2)(r^3-9r+9),\qquad
\omega^\dagger=\frac{t\,dr}{12y}.
\tag{1092.20}
$$
取有理点 $(r,y)=(2,0)$ 为原点。再作实际双有理变换
$$
X=1-\frac1{r-2},\qquad
Y=\frac{y}{(r-2)^2},
$$
得到
$$
Y^2=\lambda(X^3-9X+9),\qquad
\omega^\dagger=\frac t6\,\frac{dX}{2Y}.
\tag{1092.21}
$$
检验多项式变换只需
$$
(r-2)^3\left[\left(1-\frac1{r-2}\right)^3
-9\left(1-\frac1{r-2}\right)+9\right]
=r^3-9r+9.
$$
曲线 $E_*$ 的判别式为 $2^4 3^6$，而 $\lambda,t$ 均非零，所以这些变换没有任何 $p>3$ 的坏分母或退化纤维。

$t/6\in\mathbb F_p^\times$ 的微分重标不改变相对 Hasse 系数。若
$$
b_p=[X^{p-1}](X^3-9X+9)^m,
$$
则 (1092.21) 的实际 Hasse 系数是 $\lambda^m b_p$。标准有限域求和可直接核
$b_p\equiv a_p(E_*)\pmod p$：Euler 判别把点数化成该三次多项式的 $m$ 次方之和，次数 $3m<2(p-1)$，唯一非零正次幂和读数是 $X^{p-1}$。

最后
$$
\lambda^m=\left(\frac{-a^2/3}{p}\right)
=\left(\frac{-3}{p}\right)=-1
\qquad (p\equiv2\pmod3).
$$
结合 (1092.19)，得到
$$
\theta_P=-a_p(E_*)\pmod p.
$$
由于 $FP=P$、$U(P)=a$、$a^3=432$，这正是 (1092.6)，包括其符号。

## 6. 二挠分裂域与目标模 $9$ 类的单位性

令 $\vartheta=\zeta_9+\zeta_9^{-1}$，它满足
$$
\vartheta^3-3\vartheta+1=0.
$$
置 $x=2+\vartheta-\vartheta^2$。直接计算
$$
x^2=6-3\vartheta,\qquad
x^3=9x-9,\qquad
\vartheta=\frac{6-x^2}{3}.
\tag{1092.22}
$$
所以 $X^3-9X+9$ 的分裂域正是
$$
\mathbb Q(\zeta_9+\zeta_9^{-1}),
$$
而不是仅有相同判别式的一个未识别三次域。式 (1092.22) 的分母只含 $3$，在所有 $p>3$ 都可约化。

若 $p\equiv2$ 或 $5\pmod9$，其在
$(\mathbb Z/9\mathbb Z)^\times/\{\pm1\}$ 中的像具有阶 $3$。因此 Frobenius 在三个非零二挠点上传递，$E_*(\mathbb F_p)$ 没有非零二挠点。其有限群阶为奇数，故 $a_p(E_*)$ 为奇数，特别不为 $0$。Hasse 界给
$$
|a_p(E_*)|\le2\sqrt p<p\qquad(p\ge5),
$$
从而 $a_p(E_*)\not\equiv0\pmod p$。

这证明 (1092.7)。由于 $\Phi(U^m)=U H_p(U^3)$，另六个三挠点的 $U$ 坐标均非零且其立方相同，六个读数全部为单位。这个最后运输使用原截面的确切 $\mu_3$ 形状，不删去非有理点的 Frobenius 标签。

## 7. 范围、小素数与未闭接口

本证明用到的分母只有 $2,3$，以及非零的 $a,t,v$。三次多项式判别式为 $3^6$，曲线判别式为 $2^4 3^6$。因此对 $p=5$ 也没有额外例外；$2\sqrt5<5$，奇点数论证照常成立。$p=11,17,23,29$ 等满足 (1092.1) 的素数同样没有新的退化。无需用数值窗口补小素数。

局部 Cartier 恒等式 (1092.6) 对每个 $p>3$、$p\equiv5\pmod6$ 成立；其中 $\Phi,H_p$ 采用同一 Miller construction。它在课题原应用范围 $p\ge41$ 与 R1061 的全局 FM 截面完全一致。单位性的新增算术条件确为 $p\equiv2,5\pmod9$；在 $p\equiv8\pmod9$ 时本条不声称 $a_p(E_*)$ 非零。

本条没有证明 $H_p(0)\ne0$，也没有证明 $H_p(0)$ 与 $H_p'(0)$ 不能同时为零。原短 $\eta_k,\nu_k$、指定 $e,K_4$ 和 primitive/Legendre 同标签读数仍需真实三分布或行列式比较。特别不能把另六点的值单位加上次数界，直接当成原两点低 jet 的单位证明。

## 来源与原输入定位

- R1061 §§9、16：原 $C\to E$、Miller 首项、相对 Cartier 与 $\Phi$ 的实际 FM 归一；§§19–20：原 $e,K_4$ 和 $J$ 核的范围。
- 本文 (1092.10)–(1092.22) 给出从同一原输入到明确椭圆商、微分、二次扭曲和二挠分裂域的全部代数证明，不引用“同 CM”“同 $j$”或未定标同源类作替代。
- 点数与 Hasse 系数的比较已在 §5 用有限域幂和直接证明；最后只使用椭圆曲线的 Hasse 界。
