# R531 — 两套纯伴随框架的真实 carry、有限纤维补偿及原 Y/W 权

日期：2026-11-14。**状态：已证明。** 本篇在同一个原六 sigma 来源内，
构造两套正交的纯伴随二轴 $(C,F)$、$(D,E)$。四条轴均有付清绝对
符号的实际 scalar 核 $\beta=-\lambda$。其真实单位 carry
$$
\Gamma_n=\{C,F\ {\rm unit},\ F-C\in p^n\mathcal O\}
$$
正好是第二套框架的矩形 $\{D\in p^n\mathcal O,E\ {\rm unit}\}$。
一个固定六次多项式及逐次数的 $E$ 单位逆，因而在此同一 carry
上返回原完整四输出 $(Y,W,W',G)$；**原 $Y/W$ 权没有移动或重标度**。

固定多项式还使 $D^5E$ 项严格消失。原五深、一单位网格是上述
carry 的真实子域；同一测试在那里有非零中央，赋值准确为 $n$。
本篇算出整条有限质量多项式、全部常数 log 贡献和三条原观察的
首项。完整 carry 中的其余域始终保留，尚未从该子域非零推出
原完整中央非零。

依赖：[R522](R522-common-degree3-even-factor-and-same-st-positive-test.md)、
[R528](R528-degree14-three-orbit-positive-test-and-complete-mixed-row.md)、
[R471](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)
式 (12)–(13) 的原 sigma/Theta 核规范，以及
[R410](R410-original-deep-input-factors-are-units-on-one-fixed-ray.md)
的 $1+\lambda$ 单位性。

## 1. 原来源、观察与完整两套框架

沿用原规范
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
\gamma=3+\omega,\quad\bar\gamma=2-\omega,\quad b=17,
$$
$$
\lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1,\qquad
\rho=-\nu_\sigma^{\otimes6}/84.
\tag{1}
$$
原六输入次序是 $\xi=(\xi_1,\xi_2,\xi_3,x,c,d_0)^t$，观察行为
$$
\begin{aligned}
Y&=(\delta,2\delta,\gamma,\bar\gamma,1,2),\\
W&=(\delta,2\delta,\gamma,\bar\gamma,3\delta,4),\\
W'&=(4+4\omega,2+4\omega,4+4\omega,0,4+2\omega,4).
\end{aligned}
\tag{2}
$$
以下所有行均作用在同一个 $\xi$ 上。再令
$$
W_2=-\omega^2W-\omega W'
=(\gamma,2\delta,6+3\omega,3+2\omega,-1+\omega,4).
\tag{3}
$$
完整边际是
$$
Y_*\rho=\nu_S,\quad W_*\rho=6\delta\nu_T,\quad
W'_*\rho=0,\quad (W_2)_*\rho=-6\delta\omega^2\nu_T.
\tag{4}
$$

用 R522 的 $H_0=(1,0,-1,1,0,0)$、
$H_1=(-1,2,\omega,1+\omega,0,0)$，及 R528 的整数 degree14 行
$$
D=D_1=(1,\omega^2,-2\omega,0,1,2+3\omega)
\tag{5}
$$
定义
$$
\boxed{
C=H_0/\delta,\qquad F=D+C,\qquad
E=F+13C,\qquad G=13H_1+(3-2\omega)F.
}
\tag{6}
$$
这里 $E$ 是伴随行名，不是椭圆曲线名。准确变换为
$$
\boxed{
D=F-C,\quad E=F+13C,\qquad
C=\frac{E-D}{14},\quad F=\frac{E+13D}{14}.
}
\tag{7}
$$
完整行可写为
$$
\begin{aligned}
3F={}&(2-2\omega,-3-3\omega,1-4\omega,
                         -1-2\omega,3,6+9\omega),\\
3E={}&(-11-28\omega,-3-3\omega,14+22\omega,
                         -14-28\omega,3,6+9\omega),\\
3G={}&(-37-14\omega,63-9\omega,-5+17\omega,
                         32+31\omega,9-6\omega,36+33\omega).
\end{aligned}
\tag{8}
$$
精确 Hermitian Gram 给
$$
\boxed{
\begin{gathered}
C,F,D,E,G\perp Y,W,W',\\
C\perp F,\quad D\perp E,\quad G\perp C,F,D,E,\\
N(C)=1,\quad N(F)=13,\quad N(D)=14,\quad
N(E)=182,\quad N(G)=936.
\end{gathered}}
\tag{9}
$$
尤其 $(C,F)$ 与 $(D,E)$ 是**同一真实二维伴随平面**，不是从
两个边际分别拼出的独立输入。$G$ 原样保留。

两个完整六行框架
$$
\mathcal F_{CF}=(Y,W,W',C,F,G),\qquad
\mathcal F_{DE}=(Y,W,W',D,E,G)
\tag{10}
$$
的行列式分别是
$$
\boxed{
\det\mathcal F_{CF}=3744-14976\omega,\qquad
\det\mathcal F_{DE}=-52416+209664\omega.
}
\tag{11}
$$
其范数分别为
$$
2^{10}3^5\,7\,13^2,\qquad 2^{12}3^5\,7^3\,13^2.
$$
因此当前所有普通处的两框架都是整自同构。证书保存两矩阵、
完整逆及全部 Gram；没有遗失原六输入坐标。设
$$
\pi_4=(Y,W,W',G).
\tag{12}
$$
后文“保持其余输出”均至少完整保持 (12)。

## 2. 四个 whole 核、半特征和绝对号

物理 $C$ 的范数为一，**不把它冒认为标准 degree1 theta 空间**：
$H_0=\delta C$ 的真实整覆盖仍是 R522 的标准 odd degree3。
同理，$F,E$ 使用实际整数行 $3F,3E$。四条方向的整 theta 数据如下。

| 物理轴 | 实际整行 | 整 degree | 半特征 | 完整 $g_\pi$ 模数与值 | 非零绝对锚 |
|---|---|---:|---|---|---|
| $C$ | $H_0$ | $3$ | standard odd | $1\bmod6$ | $\sigma(\delta z)$ |
| $F$ | $3F$ | $117$ | standard odd | $1\bmod234$ | $\sigma(3\gamma_{13}z)$ |
| $D$ | $D$ | $14$ | standard even | $15\bmod28$ | $\Theta(\gamma z)$ |
| $E$ | $3E$ | $1638$ | standard even | $1639\bmod3276$ | $\Theta(3\gamma\gamma_{13}z)$ |

这里 $\gamma_{13}=4+\omega$，$N\gamma_{13}=13$。
整数行中模 $2$ 非零的系数数分别为 $3,5,4,4$。
在原 $j=0$ 格上，非零 $\mathcal O/2$ 系数均保 sigma 的标准
奇半特征，故表中 odd/even 判断包含整个半特征，不是只数解析奇偶。

现 ray 已有
$$
g_\pi\equiv27+8\omega\pmod{64},\qquad
g_\pi\equiv1\pmod{27\cdot7\cdot13}.
\tag{13}
$$
由 CRT，(13) 准确给出表中所有模 $2N$ 的值。
对 $E$，$1639=1+1638$ 在模 $4$ 为 $3$、在模 $9,7,13$ 都为 $1$；
对 $F$，模 $2,9,13$ 都为 $1$。
所以无需再细分 ray。

每个列出的整行与其余五行完全正交，原六 sigma 的周期变换
沿此轴没有隐藏交叉项。于是整个来源沿此轴属于表中完整 theta
空间张量其余五输出的系数空间。由原 whole Heisenberg 规范，
表中的交织均为 scalar；固定 CM 拉回与实际普通核严格交换。
锚中的 sigma 和 Theta 都有核心
$$
\beta=-\lambda
$$
（Theta 的符号用 R471 的实际证明），锚范数分别为
$3,117,7,819$，正好支付四个绝对标量。因此对
$L=C,F,D,E$，
$$
\boxed{
\rho|_{L\in p^r\mathcal O}
=\beta^r(P_{L,\kappa^r})_*\rho,\qquad r\ge0.
}
\tag{14}
$$
这里
$$
P_{L,t}=I+(t-1)\frac{\bar L^{\,t}L}{N(L)}
\tag{15}
$$
是真正原六输入矩阵；它只缩放 $L$，保正交的完整其余五行。
这是 actual measure 等式，包含中心相位与外部整标量。

同一证明适用于原四个实际来源。它们由第一 $W$、$W'/2$
的 whole 核和平移生成，而 (9) 使这些操作保持全部本篇伴随。
第一 $Y/W$ 的实际 CM 投影也保持这些方向及其 whole theta
半特征。因此本篇的逐项测度身份同样保原 S/new/Href/T 条件行；
没有向任何未知参考导数赋零。本篇不声称 $G$ 有一个新的 scalar 核。

## 3. 固定多项式：完整来源返回与第五项取消

R522 已付的整个 odd degree3 偶张量身份给
$$
(\text{忘 }C)_*(C^6\rho)=-8b\Omega^6(\text{忘 }C)_*\rho,
\qquad
(\text{忘 }C)_*(C^2\rho)=0.
\tag{16}
$$
其中 $\delta^6=-27$，所以 $216b\Omega^6/\delta^6=-8b\Omega^6$。
(16) 保任意其余五输出测试，特别可保 $F,G,Y,W,W'$ 的所有
混合紧开条件。

取固定正次数多项式
$$
\boxed{
Q(C,F)=-\frac{C^6}{8}
+\frac{3C^2F^4}{8\cdot11\cdot13^3}.
}
\tag{17}
$$
它的系数不含 $p,\kappa,\lambda,n$。由 (16) 的完整张量身份，
$$
\boxed{
(\text{忘 }C)_*
 \left\{\frac{Q(C,F)}{b\Omega^6}\rho\right\}
=(\text{忘 }C)_*\rho.
}
\tag{18}
$$
这已经保整个剩余五变量来源，不是若干矩相合。

按 (7) 展开：
$$
Q=\frac1{14^6}\sum_{k=0}^6q_kD^kE^{6-k},
\tag{19}
$$
其中
$$
\boxed{
(q_0,\ldots,q_6)=
\left(
-\frac{6041}{48334},\
 \frac{18144}{24167},\
-\frac{89943}{48334},\
 \frac{4844}{1859},\
-\frac{483}{286},\
0,\
\frac7{22}
\right).
}
\tag{20}
$$
特别 $q_5=0$ 是精确的特征零恒等。它也可直接从
$(E-D)^6$ 与 $(E-D)^2(E+13D)^4$ 的 $D^5E$ 系数算出；
(17) 的第二系数正好取消这一项。

## 4. 同一真实单位 carry 的完整有限逆

对 $n\ge1$，定义
$$
\boxed{
\Gamma_n=\{C,F\ {\rm unit},\ D=F-C\in p^n\mathcal O\}
=\{D\in p^n\mathcal O,\ E\ {\rm unit}\}.
}
\tag{21}
$$
第二个等号由 (7) 逐点成立：当 $D$ 深而 $E$ 单位时，
$E-D$ 与 $E+13D$ 都是单位；反之 $E=14C+D$ 是单位。
此处没有把 $C,F$ 当成独立 sigma 来源。

在 (21) 上置
$$
\boxed{
\widehat Q_{n,p}(D,E)=
\frac1{14^6b\Omega^6}
 \sum_{k=0}^6
 \frac{q_k(D/\kappa^n)^kE^{6-k}}
      {1+\lambda\kappa^{6-k}}.
}
\tag{22}
$$
它在 $\Gamma_n$ 上整且有界。正次数分母模 $p$ 为一；
$k=6$ 的分母为 $1+\lambda$，由 R410 已是单位。
将其在域外延为零，得到真正连续有界的紧开测试。

先用实际 $D$ 核把 $D/\kappa^n$ 返回完整 $D$，保 $E,\pi_4$；
再对 $E^{6-k}$ 的 $E$ 单位部分用真实 scalar 核。其准确系数是
$$
1-\beta\kappa^{6-k}=1+\lambda\kappa^{6-k},
$$
逐项消掉 (22) 的分母。最后用 (18) 并忘去 $F$，得到
$$
\boxed{
(\pi_4)_*\left\{{\bf1}_{\Gamma_n}
                  \widehat Q_{n,p}\rho\right\}
=\beta^n(\pi_4)_*\rho.
}
\tag{23}
$$
等式保任意完整四输出测试，包括真实混合 $Y/W$ 管和任意 $G$
条件。它不是只在多项式观察或某个第一边际上成立。

在 $(C,F)$ 中，所用 $D$ 缩放的实际矩阵为
$$
\boxed{
\binom{C'}{F'}=\frac1{14}
\begin{pmatrix}
13+\kappa^n&1-\kappa^n\\
13(1-\kappa^n)&1+13\kappa^n
\end{pmatrix}
\binom C F .
}
\tag{24}
$$
它保 $E$ 及原 $(Y,W,W',G)$。因此这里没有把
$\log\langle Y\rangle$ 偷换成移动后的第一权。

由 (4)、(23)，对所有 Mellin 参数，
$$
\boxed{
\begin{aligned}
\int_{\Gamma_n,\ Y\ {\rm unit}}
 \langle Y\rangle^{du}\widehat Q_{n,p}\,d\rho
 &=\beta^nJ_S(u),\\
\int_{\Gamma_n,\ W\ {\rm unit}}
 \langle W\rangle^{du}\widehat Q_{n,p}\,d\rho
 &=\beta^n6\delta J_T(u),\\
\int_{\Gamma_n,\ W_2\ {\rm unit}}
 \langle W_2\rangle^{du}\widehat Q_{n,p}\,d\rho
 &=-\beta^n6\delta\omega^2J_T(u).
\end{aligned}}
\tag{25}
$$
这些是同一个原来源、同一个 carry、同一个测试的三条原算术行。
原 $J'_S=J'_T=0$ 会消掉 (25) 相应的完整中央；没有增加新的
算术来源假设。

## 5. 原非零网格确实包含在同一 carry 中

保持原六输入事件
$$
\mathcal D_n=
\{\xi_1,\xi_2,\xi_3,c,d_0\in p^n\mathcal O,\ x\ {\rm unit}\}.
\tag{26}
$$
$D$ 的 $x$ 系数为零，而
$$
C\equiv F\equiv x/\delta,\qquad E\equiv14x/\delta\pmod{p^n}.
$$
所以
$$
\boxed{\mathcal D_n\subset\Gamma_n,\qquad
Y,W,W_2\ {\rm unit},\quad W'\in p^n.}
\tag{27}
$$
这是真正同一个原网格，未作 $A/Y$ 归一或替换原独立输入条件。

五个深输入共同缩放为 $T$。记
$$
\boldsymbol t=(\xi_1,\xi_2,\xi_3,c,d_0),\qquad
D_f=(1,\omega^2,-2\omega,1,2+3\omega)\boldsymbol t,
$$
$$
E_f=\left(\frac{-11-28\omega}{3},-1-\omega,
              \frac{14+22\omega}{3},1,2+3\omega\right)\boldsymbol t,
\qquad e_0=\frac{14}{\delta}=\frac{-14-28\omega}{3}.
\tag{28}
$$
则原 $D=TD_f$、$E=e_0x+TE_f$。在 $T=\kappa^n$ 时，
(22) 中 $D/\kappa^n$ **准确等于** $D_f$。

对 $L=Y,W,W_2$，写 $L=a_Lx+TZ_L$，其中
$$
\begin{array}{c|c|c}
L&a_L&Z_L\text{ 的五系数}\\ \hline
Y&\bar\gamma&(\delta,2\delta,\gamma,1,2)\\
W&\bar\gamma&(\delta,2\delta,\gamma,3\delta,4)\\
W_2&3+2\omega&(\gamma,2\delta,6+3\omega,-1+\omega,4).
\end{array}
\tag{29}
$$
定义真正解析函数
$$
\mathcal A_L(T)=
\frac{d}{14^6b\Omega^6}
 \int_{x\ {\rm unit}}\int
 \log\langle a_Lx+TZ_L\rangle
 \sum_{k=0}^6
 \frac{q_kD_f^k(e_0x+TE_f)^{6-k}}
      {1+\lambda\kappa^{6-k}}\,d\rho.
\tag{30}
$$
这里 $\rho$ 中五个 $\boldsymbol t$ 输入取完整测度，$x$ 仍只取单位。
分母中的 $\kappa,\lambda$ 对固定 $p$ 是固定参数，不随 $T$ 改变。
五个原 sigma 核给
$$
\boxed{
C_{L,n}:=\int_{\mathcal D_n}
 d\log\langle L\rangle\,\widehat Q_{n,p}\,d\rho
=\beta^{5n}\mathcal A_L(\kappa^n).
}
\tag{31}
$$

## 6. 常数项严格取消，第一项和整条质量项全部保留

原五个 sigma 的矩总次数小于五时全为零；第一次可能非零为
每个输入都取第一矩。$T=0$ 时，只有 $k=5$ 本可能给总次数五，
但 $q_5=0$。$k=6$ 的次数为六，原五输入的角型强迫总次数
为 $5\bmod6$，故也为零。因此
$$
\boxed{\mathcal A_L(0)=0}
\tag{32}
$$
对三条观察均精确成立；这包含全部 $\log\langle x\rangle$、
固定尺度 log 和质量贡献。

第一阶只有 $k=4$ 能贡献。完整五输入混合系数是
$$
\begin{aligned}
[\xi_1\xi_2\xi_3cd_0]D_f^4Z_Y&=216+216\omega,\\
[\xi_1\xi_2\xi_3cd_0]D_f^4Z_W&=792+216\omega,\\
[\xi_1\xi_2\xi_3cd_0]D_f^4Z_{W_2}&=288+216\omega,\\
[\xi_1\xi_2\xi_3cd_0]D_f^4E_f&=-816-48\omega.
\end{aligned}
\tag{33}
$$
设原 sigma 单位矩
$$
I_1=\int_{x\ {\rm unit}}x\,d\nu_\sigma=(1+\lambda\kappa)\Omega,\qquad
I_{1,\log}=\int_{x\ {\rm unit}}x\log\langle x\rangle\,d\nu_\sigma.
$$
其中 $I_{1,\log}\in p\mathcal O$。准确第一项为
$$
\boxed{
[T]\mathcal A_L=
\frac{d}{b(1+\lambda\kappa^2)}
\left[
\alpha_L\frac{I_1}{\Omega}
+m_1\frac{I_{1,\log}+\log\langle a_L\rangle I_1}{\Omega}
\right],
}
\tag{34}
$$
其中
$$
\boxed{
\begin{array}{c|c}
L&\alpha_L\\ \hline
Y&(-414-621\omega)/38454416\\
W&(-2070-1173\omega)/38454416\\
W_2&(-690-69\omega)/38454416
\end{array}
\qquad
m_1=\frac{345+759\omega}{19227208}.
}
\tag{35}
$$
这里 $\alpha_L$ 来自 log 的线性项，$m_1$ 来自多项式本身的
线性项。第二项没有被丢掉；它模 $p$ 消失，但通常不为零。

更完整地，删去 (30) 的 $d\log$ 后得到质量多项式
$\mathcal M(T)$。它准确为
$$
\boxed{
\mathcal M(T)=\frac{1+\lambda\kappa}{b}
 \sum_{r=1}^5\frac{m_rT^r}{1+\lambda\kappa^{r+1}}.
}
\tag{36}
$$
不存在其他质量项。为完全指定它，令
$$
B_k=[\xi_1\xi_2\xi_3cd_0]D_f^kE_f^{5-k};
\quad
(B_0,\ldots,B_4)=
(5680-13040\omega,\ 2880-7440\omega,\ 864-3408\omega,\
 -368-944\omega,\ -816-48\omega).
$$
则
$$
\boxed{
m_{5-k}=-\frac{(6-k)e_0q_kB_k}{84\cdot14^6},
\qquad 0\le k\le4.
}
\tag{37}
$$
证书还保存五个 $m_r$ 的约分有理系数。

(30) 中全部常数 log 贡献也因此准确为
$$
\boxed{
\frac db\,
\frac{I_{1,\log}+\log\langle a_L\rangle I_1}{\Omega}
\sum_{r=1}^5\frac{m_rT^r}{1+\lambda\kappa^{r+1}}.
}
\tag{38}
$$
本构造只取消常数项，**没有宣称 $\mathcal D_n$ 上的质量为零**。

## 7. 原 ray 上的单位首项和全尾

全部首项范数由精确有理计算给
$$
\begin{aligned}
N\alpha_Y&=\frac{3^4\,23^2}{2^8\,7^9\,11^2\,13^2},\\
N\alpha_W&=\frac{3^2\,23^2\,97}{2^8\,7^9\,11^2\,13^2},\\
N\alpha_{W_2}&=\frac{3^2\,23^2}{2^8\,7^9\,11^2\,13},\\
Nm_1&=\frac{3^2\,23^2}{2^6\,7^9\,11^2\,13}.
\end{aligned}
\tag{39}
$$
当前 $p\equiv7\bmod64$、$p\ge71$，不等于这些固定素因子。
所以三条 $\alpha_L$ 及 $m_1$ 在整个当前普通 ray 都是单位；
无需新增射线或新的大 $p$ 门。

所有测试系数及单位矩整；(30) 的 log 展开只带当前次数的
通常分母，故
$$
v_p([T^r]\mathcal A_L)\ge-\lfloor\log_pr\rfloor,\qquad r\ge1.
\tag{40}
$$
(34) 的 log 质量部分属于 $p\mathcal O$，非 log 部分是单位。
对 $n\ge1,r\ge2$，
$$
rn-\lfloor\log_pr\rfloor>n.
$$
结合 (31)、(32)，得到
$$
\boxed{
v_p(C_{Y,n})=v_p(C_{W,n})=v_p(C_{W_2,n})=n.
}
\tag{41}
$$
由 (36)、(39)，同一真实加权域的质量也满足
$$
\boxed{
v_p\left(\int_{\mathcal D_n}\widehat Q_{n,p}\,d\rho\right)=n.
}
\tag{42}
$$
这些都是同一原域、同一有限逆测试上的非零值。

两条原算术归一差同样有单位第一项：
$$
\begin{aligned}
\Delta_{WY}&=\frac{\alpha_W}{6\delta}-\alpha_Y
             =\frac{2392+4715\omega}{230726496},\\
\Delta_{W_2Y}&=\frac{\alpha_{W_2}}{-6\delta\omega^2}-\alpha_Y
             =\frac{2921+3979\omega}{230726496},
\end{aligned}
\tag{43}
$$
$$
N\Delta_{WY}=
\frac{19\cdot23^2\cdot79}{2^{10}3\,7^9\,11^2\,13^2},\qquad
N\Delta_{W_2Y}=
\frac{23^2\cdot31\cdot37}{2^{10}3\,7^9\,11^2\,13^2}.
$$
新增分子素因子也都不在当前 $p\equiv7\bmod64$ 的 ray。
所有相应 log 项仍按 (34) 保留且属于 $p\mathcal O$。
因此
$$
\boxed{
v_p\left(\frac{C_{W,n}}{6\delta}-C_{Y,n}\right)=
v_p\left(\frac{C_{W_2,n}}{-6\delta\omega^2}-C_{Y,n}\right)=n.
}
\tag{44}
$$
本篇没有把 (44) 的局部差当成原完整两个中央的差。

## 8. 完整零来源与确切补域

(23) 还给一个没有算术零假设的 whole joint 核：
$$
\boxed{
\mathcal Z_n=
 {\bf1}_{\Gamma_n}\widehat Q_{n,p}\rho-\beta^n\rho,
\qquad (\pi_4)_*\mathcal Z_n=0.
}
\tag{45}
$$
所以对任何真正 $\pi_4$ 条件、任何其上的连续测试，积分均为零。
例如在
$$
\mathcal U=\{Y,W\ {\rm unit}\}
$$
取 $d\log\langle Y\rangle$，其整个积分严格为零。

原未加权 $\rho$ 在 $\mathcal D_n$ 的中央从总次数五开始，且
所有高阶按原有界矩控制，故赋值至少 $5n$。由 (41)，
$$
v_p\left(\int_{\mathcal D_n}
 d\log\langle Y\rangle\,d\mathcal Z_n\right)=n.
\tag{46}
$$
因此 (45) 的同一真零积分是准确分解
$$
0=
\int_{\mathcal D_n}d\log\langle Y\rangle\,d\mathcal Z_n+
\int_{\mathcal U\setminus\mathcal D_n}
 d\log\langle Y\rangle\,d\mathcal Z_n.
\tag{47}
$$
第二项包含实际加权 carry 的剩余部分及原未加权来源的对应项，
其值被 (46) 迫为反号，而不能删掉。

若另假设原 $J'_S=0$，(25) 第一条仅给
$$
0=C_{Y,n}+
\int_{(\Gamma_n\cap\{Y\ {\rm unit}\})\setminus\mathcal D_n}
d\log\langle Y\rangle\,\widehat Q_{n,p}\,d\rho.
\tag{48}
$$
原 $J'_T=0$ 给两条同样完整的 $W/W_2$ 分解。
(41)、(44) 迫使这些真实补域付出具体非零补偿；本篇尚未将
这些补偿通过会改变 $Y$ 的原操作共同消掉。原任务的无限素数
完成标准因此仍未达到。

## 9. 精确证书与本篇新增范围

脚本
[check-r531-hidden-two-frame-native-central-carry.js](../scripts/check-r531-hidden-two-frame-native-central-carry.js)
和
[完整 JSON](../scripts/check-r531-hidden-two-frame-native-central-carry.json)
使用 BigInt 的 $\mathbf Q(\omega)$ 精确运算，保存并验证：

- 两套完整六行框架、逆、Gram、行列式及所有实际整数覆盖；
- 四条轴的完整模 $2N$ 中心、半特征计数与非零锚的准确 degree；
- 固定 $Q$ 的全部七个系数，特别 $q_5=0$；
- 三条观察的完整五输入首项、五项质量多项式和单位范数分解。

证书已在当前 JavaScript 执行环境中精确执行；没有用有限域
采样代替特征零身份。whole theta 与实际测度核的证明在正文，
不以脚本的有限数据断言整个来源。

新增的是：同一原 S/T 联合中的真实二轴单位 carry，有保持全部
原观察权的显式有限逆；原非零五深网格直接落在这一 carry 内，
而且固定纤维多项式取消常数 log 项后给单位的一阶中央与质量。
剩余问题明确在 (48) 的实际补域及改变 $Y$ 的原来源关系中。
