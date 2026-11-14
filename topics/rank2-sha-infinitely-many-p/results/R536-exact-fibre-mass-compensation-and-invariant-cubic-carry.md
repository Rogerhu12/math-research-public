# R536 — 原 carry 的整纤维质量消去与不变三分支测试

日期：2026-11-14。**状态：已证明。** 本篇对
[R531](R531-hidden-two-frame-native-central-carry.md) 的同一真实
carry 作有限纤维补偿。新增测试仍对原完整四输出
$\pi_4=(Y,W,W',G)$ 返回原来源，原 $Y/W/W_2$ 权保持不动；
同时，原五深、一单位网格上的加权质量及全部常数 log 贡献
**严格为零**，而原三个中央的赋值仍准确为 $n$。

构造支付的是实际七行、十列线性问题，而非按未知数个数判断。
完整 $\lambda,\kappa$ 矩阵有显示整右逆；只删除一个固定整数的
有限素因子，不增加新的 ray 条件。再将三个互不相交的原 carry
分支平均，得到真正 $\mathcal T$ 不变的同一测试。它把非零网格
送进原 $h$ 的 $W$ 深管，原 $W$ 核也保持该测试。
最后的 $Y$ 权变化和完整补域仍显示保留，主目标尚未完成。

## 1. 同一原六输入与已付完整框架

全部符号沿用 R531：
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=3+\omega,\quad\bar\gamma=2-\omega,\quad b=17,
$$
$$
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1,\quad
\rho=-\nu_\sigma^{\otimes6}/84.
\tag{1}
$$
原输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$。保 R531 的完整行
$$
\begin{aligned}
H_0&=(1,0,-1,1,0,0),&
H_1&=(-1,2,\omega,1+\omega,0,0),\\
C&=H_0/\delta,&
D&=(1,\omega^2,-2\omega,0,1,2+3\omega),\\
F&=D+C,& E&=F+13C,\\
G&=13H_1+(3-2\omega)F.
\end{aligned}
\tag{2}
$$
两套真实框架准确为
$$
(C,F),\quad(D,E),\qquad
D=F-C,\quad E=F+13C,\quad
C=(E-D)/14,\quad F=(E+13D)/14.
\tag{3}
$$
$C,F,D,E,G$ 全与 $Y,W,W'$ 正交；其余原观察仍为
$$
W_2=-\omega^2W-\omega W',\qquad
Y_*\rho=S,\quad W_*\rho=6\delta T,\quad
W'_*\rho=0,\quad (W_2)_*\rho=-6\delta\omega^2T.
\tag{4}
$$

R531 已付整个六行矩阵、逆、Gram 及四轴实际核心。
$C,F,D,E$ 的实际整 theta 覆盖分别为 odd3、odd117、even14、
even1638，**全部核心都是 $\beta$**；尤其保实际 Theta 锚的负号。
$G$ 原样保留，不给它另猜单轴核心。设
$$
\pi_4=(Y,W,W',G).
$$
对 $n\ge1$，原 carry 仍是
$$
\boxed{
\Gamma_n=\{C,F\ {\rm unit},D\in p^n\}
        =\{D\in p^n,E\ {\rm unit}\}.
}
\tag{5}
$$
它是同一个原联合中的域，未将两个边际当成独立来源。

## 2. 十个完整消去方向

R522 的整个 odd degree3 基为
$$
\sigma^3,\quad x_\wp\sigma^3,\quad
B_3=-y_\wp\sigma^3.
$$
其角型和初始次数分别为 $3,1,0$。故第二、第四、第五 Taylor
系数在整个空间上都为零，而第六系数由唯一偶线给出。
换成实际 $C=H_0/\delta$ 后，保其余五输出的准确矩身份是
$$
\boxed{
(\text{忘 }C)_*(C^2\rho)
=(\text{忘 }C)_*(C^4\rho)
=(\text{忘 }C)_*(C^5\rho)=0,
}
$$
$$
\boxed{
(\text{忘 }C)_*(C^6\rho)
=-8b\Omega^6(\text{忘 }C)_*\rho.
}
\tag{6}
$$
这使用整个 theta 空间，允许其余五输出的任意连续测试；
特别 $C^5$ 的消失不是只在第一 $Y$ 边际上的偶奇判断。

按以下固定次序列十个齐次六次单项式：
$$
\boxed{
\begin{aligned}
(\phi_0,\ldots,\phi_9)=(&C^2G^4,C^2FG^3,C^2F^2G^2,C^2F^3G,C^2F^4,\\
 &C^4G^2,C^4FG,C^4F^2,C^5G,C^5F).
\end{aligned}}
\tag{7}
$$
再令 $\phi_*=-C^6/8$。对任意十个整系数 $x_j$，定义
$$
Q=\phi_*+\sum_{j=0}^9x_j\phi_j.
\tag{8}
$$
由 (6)，无论这些系数怎样取，严格有
$$
\boxed{
(\text{忘 }C)_*
 \left\{\frac{Q}{b\Omega^6}\rho\right\}
=(\text{忘 }C)_*\rho.
}
\tag{9}
$$
因此后面为真实局部质量而选择系数，不会改变完整原算术来源。
同样的 (6)–(9) 对原四个实际来源成立，因为生成它们的观察轴
核和平移都保持完整 $C$ 方向。

## 3. 七个真实行的定义

把 (8) 通过 (3) 写成
$$
P(D,E,G)=Q\!\left(\frac{E-D}{14},\frac{E+13D}{14},G\right)
       =\sum_{k+j+\ell=6}a_{kj\ell}D^kE^jG^\ell.
\tag{10}
$$
全部 $14$ 的分母已包含在 $a_{kj\ell}$ 中，后面不再额外乘
一个 $14^{-6}$。

设
$$
u_j=\frac1{1+\lambda\kappa^j}\quad(0\le j\le6),\qquad
\mathcal R_pP=\sum a_{kj\ell}u_jD^kE^jG^\ell.
\tag{11}
$$
这是按 $E$ 次数的真正单位逆。$u_0=(1+\lambda)^{-1}$ 由 R410
为单位，其他 $u_j$ 模 $p$ 为一。全部 $\lambda,\kappa$ 保留。

在原五深、一单位网格
$$
\mathcal D_n=
\{\xi_1,\xi_2,\xi_3,c,d_0\in p^n,\ x\ {\rm unit}\}
\tag{12}
$$
上共同缩放五个深输入，记
$$
D=TD_f,\quad E=e_0x+TE_f,\quad G=g_0x+TG_f,
$$
$$
e_0=\frac{-14-28\omega}{3},\qquad
g_0=\frac{32+31\omega}{3}.
\tag{13}
$$
$D_f,E_f,G_f$ 的五系数是 (2) 相应行删去 $x$ 列所得：
$$
\begin{aligned}
D_f&=(1,\omega^2,-2\omega,1,2+3\omega),\\
E_f&=((-11-28\omega)/3,-1-\omega,(14+22\omega)/3,1,2+3\omega),\\
G_f&=((-37-14\omega)/3,21-3\omega,(-5+17\omega)/3,
                                            3-2\omega,12+11\omega).
\end{aligned}
\tag{14}
$$
这些是同一个原输入下的行，不是额外独立测度。

令 $\mathcal C$ 表示取五个变量
$\xi_1\xi_2\xi_3cd_0$ 的系数。对每个 $k=0,\ldots,5$，定义真实
质量行
$$
\boxed{
\mathcal M_k(\mathcal R_pP)=
\sum_{j+\ell=6-k}a_{kj\ell}u_j
 \left\{j e_0\,\mathcal C(D_f^kE_f^{j-1}G_f^\ell)
       +\ell g_0\,\mathcal C(D_f^kE_f^jG_f^{\ell-1})\right\}.
}
\tag{15}
$$
指数为负的项以其前系数为零而省去。第七行是
$$
\boxed{
\mathcal L(\mathcal R_pP)=
\sum_{j+\ell=2}a_{4j\ell}u_je_0^jg_0^\ell.
}
\tag{16}
$$
它正是实际中央第一阶的非 log 系数，不是抽象秩条件。

目标七行向量为
$$
\boxed{(\mathcal M_0,\ldots,\mathcal M_5,\mathcal L)
=(0,0,0,0,0,0,1).}
\tag{17}
$$
所有行对 (8) 的十个系数线性。按 $E$ 次数分别构造固定矩阵
$A^{(j)}\in M_{7,10}(\mathbf Q(\omega))$ 及固定列
$v^{(j)}\in\mathbf Q(\omega)^7$：前者是 (7) 各列对 (15)–(16)
的贡献，后者是 $\phi_*$ 的贡献。则完整实际方程为
$$
\boxed{
A_p x_p=b_p,\qquad
A_p=\sum_{j=0}^6u_jA^{(j)},\qquad
b_p=e_6-\sum_{j=0}^6u_jv^{(j)}.
}
\tag{18}
$$
$e_6=(0,0,0,0,0,0,1)^t$。所有七个矩阵和七个固定列均在证书
中由原 (2)、(14) 的精确系数构造并完整保存。

## 4. 显示整右逆，而非维数猜测

置
$$
\tau=(1+\lambda)^{-1},\qquad
A_+=\sum_{j=1}^6A^{(j)},\qquad A_0=A^{(0)}.
$$
因为 $\kappa\in p\mathcal O$，
$$
A_p\equiv A(\tau):=A_++\tau A_0\pmod p.
\tag{19}
$$
精确证书给两个固定有理 CM 矩阵
$B_0,B_1\in M_{10,7}(\mathbf Q(\omega))$，并逐项核定
$$
\boxed{
A_+B_0=-I_7,\qquad
A_+B_1+A_0B_0=I_7,\qquad
A_0B_1=0.
}
\tag{20}
$$
这三个特征零矩阵等式包含全部七行，而不是模某个试验素数
的秩检查。完整 $B_0,B_1$ 存于 JSON。

也可不依赖预存数表重建它们：把 (20) 按各右端列排列成
$21\times20$ 的固定有理 CM 线性系统，按列从零起消元。
其主元列准确为 $0,1,\ldots,16$；置其余三列未知量为零，
所得显示解就是本篇使用的 $B_0,B_1$。
脚本从原行构造该系统、求出这两个矩阵，并再次逐系数验证
(20)。

两个矩阵所有有理系数分母的最小公倍数为固定整数
$$
\boxed{
D_*=
4537451588264139836451244660234336276993718104462606281191442193986936120.
}
\tag{21}
$$
本篇只再删除
$$
p\mid 2\cdot3\cdot7\cdot13\cdot17\cdot D_*
\tag{22}
$$
的有限素数。它们与 $p,\lambda,\kappa,n$ 的取值没有隐藏依赖；
原无限 ray 删去此有限集后仍无限。

由 (20)，
$$
\boxed{
B(\tau)=\frac{B_0+\tau B_1}{\tau-1},\qquad
A(\tau)B(\tau)=I_7.
}
\tag{23}
$$
而
$$
\tau-1=-\frac{\lambda}{1+\lambda}
$$
在原 ray 上是单位。故 (22) 外 $B(\tau)$ 整。
于是
$$
N_p=A_pB(\tau)\equiv I_7\pmod p
$$
有整逆，$\det N_p\equiv1\bmod p$。定义**有限、准确的**系数
$$
\boxed{
x_p=B(\tau)\,[A_pB(\tau)]^{-1}b_p.
}
\tag{24}
$$
这是一个 $7\times7$ 矩阵的通常逆，未留下近似解或未收敛级数。
(24) 使所有十个系数整，并给
$A_px_p=b_p$，所以实际全部 $\lambda,\kappa$ 下的 (17) 精确成立。
这一构造没有先将 $u_j$ 改成一后继续沿用近似系数。

令 $Q_p$ 为 (8) 配 (24) 的多项式，$P_p$ 为 (10)。
$Q_p$ 允许上述明确的 $p$ 依赖；后文固定首项来自准确的
$\mathcal L=1$，不是把一个含 $p$ 的系数误当成固定代数常数。

## 5. 原 carry、原四输出和原算术行全保

在 (5) 上定义
$$
\boxed{
q_{n,p}(\xi)=\frac1{b\Omega^6}
 \left(\mathcal R_pP_p\right)(D/\kappa^n,E,G),
\qquad
d\rho_{n,p}={\bf1}_{\Gamma_n}q_{n,p}\,d\rho.
}
\tag{25}
$$
$D/\kappa^n$ 在此整，且 (11)、(24) 的全部系数整；
测试在域外延为零后是有界连续函数。

用实际 $D$ 核还原 $D/\kappa^n$，再逐个 $E^j$ 用实际
$E$ 单位系数 $1+\lambda\kappa^j$ 消去 (11)，最后用 (9)，得
$$
\boxed{(\pi_4)_*\rho_{n,p}=\beta^n(\pi_4)_*\rho
\quad\text{对每个 }n\ge1.}
\tag{26}
$$
因此原 $Y/W/W_2$ 的全部 Mellin 行准确为
$$
\boxed{
\begin{aligned}
\int_{\Gamma_n,\ Y\ {\rm unit}}\langle Y\rangle^{du}q_{n,p}\,d\rho
 &=\beta^nJ_S(u),\\
\int_{\Gamma_n,\ W\ {\rm unit}}\langle W\rangle^{du}q_{n,p}\,d\rho
 &=6\delta\beta^nJ_T(u),\\
\int_{\Gamma_n,\ W_2\ {\rm unit}}\langle W_2\rangle^{du}q_{n,p}\,d\rho
 &=-6\delta\omega^2\beta^nJ_T(u).
\end{aligned}}
\tag{27}
$$
第一权没有缩放或移动。比 (27) 更强的 (26) 还允许任意完整
$\pi_4$ 测试和混合紧开条件。
同一结论适用于原四个实际来源和保持这些伴随的原第一 CM 投影。

## 6. 同一网格的质量整条消失

R531 已逐点证明 $\mathcal D_n\subset\Gamma_n$，
$Y,W,W_2$ 单位且 $W'\in p^n$。
共同缩放原五个深 sigma，令
$$
\mathcal P_p(T;\boldsymbol t,x)=
(\mathcal R_pP_p)(D_f,e_0x+TE_f,g_0x+TG_f).
\tag{28}
$$
因为原 $D=TD_f$，在 $T=\kappa^n$ 时 (25) 的
$D/\kappa^n$ 准确成为 $D_f$。

(28) 总次数为六。对五个独立 sigma 作积分，只有总次数五
能够非零；次数小于五全为零，而次数六与五个原 sigma 的
总角型不合。总次数五时五个输入都取第一矩，剩余自由变量
必为 $x$ 的一次幂。因此完整质量多项式准确为
$$
\boxed{
-\frac{I_1}{84b\Omega}
 \sum_{k=0}^5\mathcal M_k(\mathcal R_pP_p)\,T^{5-k}=0,
\qquad I_1=(1+\lambda\kappa)\Omega.
}
\tag{29}
$$
这就是 (15) 六行的全部作用；没有被省略的高阶质量项。

因同一剩余自由幂总是 $x$，换成
$x\log\langle x\rangle$ 或乘任意固定尺度 log 后仍乘 (29)
的同一零系数。故对所有 $n\ge1$，
$$
\boxed{
\int_{\mathcal D_n}q_{n,p}\,d\rho=0,\qquad
\int_{\mathcal D_n}\log\langle x\rangle q_{n,p}\,d\rho=0.
}
\tag{30}
$$
原三个观察中全部
$\log\langle a_L\rangle+\log\langle x\rangle$
贡献都严格为零；这里只用了 (17)，没有将 log 矩的模 $p$
消失冒认成整条消失。

## 7. 固定单位第一项与全部深度

对 $L=Y,W,W_2$，仍写
$$
L=a_Lx+TZ_L
$$
如 R531 式 (29)。定义
$$
\mathcal A_L(T)=
\frac{d}{b\Omega^6}\int_{x\ {\rm unit}}\int
 \log\langle a_Lx+TZ_L\rangle\,
 \mathcal P_p(T;\boldsymbol t,x)\,d\rho.
\tag{31}
$$
五个 sigma 的实际核心给
$$
\boxed{
C_{L,n}:=\int_{\mathcal D_n}
d\log\langle L\rangle q_{n,p}\,d\rho
=\beta^{5n}\mathcal A_L(\kappa^n).
}
\tag{32}
$$
(29) 使常数项以及全部常数 log 部分消失。
第一阶只有 $D_f^4$ 的部分能贡献，而 (16)–(17) 将其自由
系数**准确固定为一**。因此
$$
\boxed{
[T]\mathcal A_L
=\frac db\,\alpha_L(1+\lambda\kappa),
}
\tag{33}
$$
其中三个完全固定的代数常数为
$$
\boxed{
\alpha_Y=-\frac{36+54\omega}{49},\quad
\alpha_W=-\frac{180+102\omega}{49},\quad
\alpha_{W_2}=-\frac{60+6\omega}{49}.
}
\tag{34}
$$
例如
$$
\alpha_Y=-\frac{
 [\xi_1\xi_2\xi_3cd_0]D_f^4Z_Y}{84\bar\gamma},
\qquad
[\xi_1\xi_2\xi_3cd_0]D_f^4Z_Y=216+216\omega.
$$
所以本篇保完整 $\lambda,\kappa$ 时仍没有未知的首项系数。

准确范数为
$$
N\alpha_Y=\frac{324}{343},\quad
N\alpha_W=\frac{3492}{343},\quad
N\alpha_{W_2}=\frac{468}{343}.
\tag{35}
$$
当前 $p\equiv7\bmod64$、$p\ge71$ 排除其所有分子素因子
（唯一大于 $71$ 的候选为 $97$，不在此 ray）。
连同 (22)，三者皆单位。

因为 (24) 的全部系数整，log 高项仍满足统一界
$$
v_p([T^r]\mathcal A_L)\ge-\lfloor\log_pr\rfloor.
\tag{36}
$$
对任意 $n\ge1,r\ge2$，有
$rn-\lfloor\log_pr\rfloor>n$。所以
$$
\boxed{
v_p(C_{Y,n})=v_p(C_{W,n})=v_p(C_{W_2,n})=n
\quad\text{对全部 }n\ge1.
}
\tag{37}
$$
这与 (30) 的严格零质量同时成立。

两条原 S/T 归一差同样有固定单位：
$$
\boxed{
\frac{\alpha_W}{6\delta}-\alpha_Y
 =\frac{104+205\omega}{147},\qquad
\frac{\alpha_{W_2}}{-6\delta\omega^2}-\alpha_Y
 =\frac{127+173\omega}{147}.
}
\tag{38}
$$
其范数分别为 $1501/1029$、$1147/1029$，分子为
$19\cdot79$、$31\cdot37$，也被当前 ray 排除。因此同一域、
同一测试上两个实际归一中央差均有赋值 $n$。
这里不把局部差认成原完整中央差；完整补域仍见下文。

## 8. 三个不相交的真实分支与不变测试

原三阶几何 $\mathcal T$ 在这些完整行上满足
$$
\boxed{
C\mathcal T=\omega^2C,\qquad
F\mathcal T=F,\qquad G\mathcal T=G,\qquad Y\mathcal T=Y.
}
\tag{39}
$$
证书用原六乘六矩阵精确核定这些式。
对 $j=0,1,2$，令
$$
\zeta_j=\omega^{2j},\quad
D_j=F-\zeta_jC,\quad E_j=F+13\zeta_jC,
$$
$$
\Gamma_{n,j}=\{C,F\ {\rm unit},D_j\in p^n\}.
\tag{40}
$$
$D_j$ 是 R528 原三个整数 degree14 行；$3E_j$ 都在同一个
even1638 whole 空间。因此四轴核的绝对号与 R531 相同，
没有因旋转而猜一个新相位。

令
$$
q_{n,p}^{(j)}=
\frac1{b\Omega^6}(\mathcal R_pP_p)(D_j/\kappa^n,E_j,G)
\quad\text{于 }\Gamma_{n,j}.
$$
这对应完整源多项式 $Q_p(\zeta_jC,F,G)$；
$\zeta_j^6=1$ 保固定 $-C^6/8$，其余消去矩仍为零。
故每一支都完整返回
$$
(\pi_4)_*({\bf1}_{\Gamma_{n,j}}q_{n,p}^{(j)}\rho)
=\beta^n(\pi_4)_*\rho.
\tag{41}
$$

三支两两不交：若两条 $D_j,D_k$ 都深，其差
$(\zeta_k-\zeta_j)C$ 必深，但 $\zeta_k-\zeta_j$ 和 $C$ 都是单位。
它们的并集准确为
$$
\boxed{
\Gamma_n^{(3)}
=\{C,F\ {\rm unit},\ F^3-C^3\in p^n\}
=\coprod_{j=0}^2\Gamma_{n,j}.
}
\tag{42}
$$
这里 $p\ne3$，三个根的差都是单位，因此深度没有损失。

定义单一的有界测试
$$
\boxed{
\mathfrak q_{n,p}=
\frac13\sum_{j=0}^2
 {\bf1}_{\Gamma_{n,j}}q_{n,p}^{(j)}.
}
\tag{43}
$$
它满足
$$
\boxed{
\mathfrak q_{n,p}\circ\mathcal T=\mathfrak q_{n,p},\qquad
(\pi_4)_*(\mathfrak q_{n,p}\rho)=\beta^n(\pi_4)_*\rho.
}
\tag{44}
$$
三阶不变性是逐支完整转置所得，不是只平均三个边际。

原 $\mathcal D_n$ 只有 $D_0$ 深；另外两条 $D_j$ 的自由 $x$
系数非零且为单位。因此在该真实网格上，(43) 正好是
$q_{n,p}/3$。所以其质量仍严格为零，三条中央及 (38) 的局部
差仍有赋值 $n$。

## 9. 同一未移动测试进入原 h 的 W 深管

原实际来源身份是
$$
h=\omega^2\mathcal T_*\rho,\qquad W\mathcal T=W',\qquad
Y\mathcal T=Y.
$$
设 $\mathcal E_n=\mathcal T\mathcal D_n$。由 (39)–(44)，严格有
$$
\boxed{
\int_{\mathcal E_n}\mathfrak q_{n,p}\,dh=0,\qquad
\int_{\mathcal E_n}d\log\langle Y\rangle\,\mathfrak q_{n,p}\,dh
=\frac{\omega^2}{3}C_{Y,n}.
}
\tag{45}
$$
其赋值为 $n$，并且整个 $\mathcal E_n$ 都满足 $W\in p^n$、
$Y$ 单位。所有原输入条件仍是
$(\mathcal T^{-1}\xi)_i\in p^n$（$i\ne x$）及
$(\mathcal T^{-1}\xi)_x$ 单位。

测试 (43) 只依赖 $C,F,G$，这些行全正交于旧 $W$。
故旧 $W$ 的真实核心原样保持整个测试及三个 carry 分支。
原 $h$ 有完整 $W$ scalar 核 $\beta$，所以
$\mathfrak q_{n,p}h$ 也有同一核。

具体令
$$
P_{W,\kappa^n}
=I+\frac{\kappa^n-1}{72}\bar W^{\,t}W,\qquad
\mathcal E_n^0=P_{W,\kappa^n}^{-1}\mathcal E_n.
$$
则 (45) 的中央准确等于
$$
\boxed{
\beta^n\int_{\mathcal E_n^0}
d\log\left\langle
Y+\frac{(\kappa^n-1)(37-3\delta)}{72}W
\right\rangle\mathfrak q_{n,p}\,dh.
}
\tag{46}
$$
这里完整单位条件是括号内的线性式为单位，原
$\mathcal E_n^0$ 的全部条件也照旧保留。
(45) 的零质量允许固定单位总尺度的 log 消去，但不能删除
(46) 中加在 $Y$ 上的 $W$ 项。
这是本篇真正跨入原 $W$ 核后的剩余混合权。

## 10. 完整补域和未完成的中央问题

(26) 或 (44) 都保原完整算术行。若原反证输入为
$J'_S=J'_T=0$，则例如
$$
\boxed{
0=\frac13C_{Y,n}
+\int_{(\Gamma_n^{(3)}\cap\{Y\ {\rm unit}\})\setminus\mathcal D_n}
d\log\langle Y\rangle\,\mathfrak q_{n,p}\,d\rho.
}
\tag{47}
$$
两个 $T$ 观察有相应的完整分解。原 $h$ 的第一 $Y$ 行同样是
$\omega^2\beta^nJ'_S$，故 (45) 的非零 $W$ 深子管仍有
确切的其余域补偿。

本篇新支付了整纤维逆、全部深度的严格零质量、原三阶不变性
及同一个旧 $W$ 核的真实运输。它没有将 (46) 的移动权认作
原未移动的 $Y$，也没有删除 (47) 的补域。
无限素数主目标仍须用实际混合来源关系控制这些剩余项。

## 精确证书

- [check-r536-exact-fibre-mass-compensation.js](../scripts/check-r536-exact-fibre-mass-compensation.js)
- [全部固定矩阵、右逆及原六维几何 JSON](../scripts/check-r536-exact-fibre-mass-compensation.json)

脚本使用 BigInt 的 $\mathbf Q(\omega)$ 精确运算，从原六输入行
生成全部七层实际矩阵；完整求出并验证 (20)，核定固定整数
(21)，以及三阶矩阵、三个 carry 行、全部固定首项和范数。
它已在当前 JavaScript 执行环境中精确执行。没有用样本素数或
数值秩替代实际整右逆；$p$ 依赖的有限逆和全部量词由 (18)–(24)
的严格代数证明支付。
