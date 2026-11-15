# R670 — 原 carry 核对完整 Λ₂ 的四维整像与合法取消测试

日期：2026-11-15。**状态：已证明。**

本篇计算 R667 的原十一维整核对 $\Lambda_{2,N}$ 整条条件 A
来源的作用，而不只读取它的质量。结果是一个固定四维空间：
完整 whole $\mathcal S_{29}$ 型零的五个系数始终满足一个明确线性关系，
两个可能的 C 伴随核心符号下，原核的四条显示列都张满该空间。

该结论保全部实际 $\lambda,\kappa,\kappa^N$。
在原 ray 的同一个相对密度一子族，得到四维整右逆，且对所有
$N\in4\mathbf Z_{\ge1}$ 同时成立。
因此可另造同九条约束的测试，整条取消 $\Lambda_2$；
其余六条条件来源和所有原 S/T 补域不自动消失。
特别被取消的也包括该新测试的整个 R665 负一深支。
原固定 $q_N$ 及其已付非零系数保持原定义。

## 1. 要计算的完整来源映射

保 R594/R664/R665/R667 的
$$
b=17,\quad\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad\Omega\in\mathcal O^\times,
\qquad N\in4\mathbf Z_{\ge1}.
$$
令 $A_p$ 是原九条实际补偿行对二十个中性列的矩阵。
原整核和投影仍为
$$
\mathscr K_p=\ker A_p,\qquad
\Pi_p=I_{20}-B(\tau)(A_pB(\tau))^{-1}A_p,\qquad
\tau=(1+\lambda)^{-1}.
\tag{1}
$$
R594/R667 已付 $\mathscr K_p$ 是秩十一的整直和项。
对 $v\in\mathscr K_p$，以同样的二十列、原 D/E 换元和全部
E 单位逆构成 $\delta\widehat P_v$、$\delta q_{v,N}$。
于是
$$
(\pi_4)_*(\delta q_{v,N}\mu_0)=0,\qquad
\pi_4=(Y,W,W',G),
\tag{2}
$$
而所有九条补偿行的改变量也严格为零。

用 R667(10) 的同一门
$\mathcal H_N=\{C\ {\rm unit},D_*\in p^N\}$ 定义
$\delta\Lambda_{2,N}(v)$。计算以下整规范的**完整 A 来源**：
$$
\boxed{
\Phi_{N,p}(v)(z)=
\kappa^{2N}\lambda^{-N}\Omega^2
\int\exp(Az/\Omega)\,d\delta\Lambda_{2,N}(v).
}
\tag{3}
$$
它沿 A 仍是完整 standard odd $\mathcal S_{29}$ 的型零截面。
(3) 的缩放只规范其系数，不移动任何原物理 cut。

为保所有高层项，置 $t=\kappa^N$、
$\mathcal D_t=\partial_D+t\partial_E+tg\partial_G$、
$g=3-2\omega$。R665(20) 的实际行是
$$
\epsilon_D=-263/143,\quad\gamma_D=(-789+526\omega)/143,
$$
$$
E_*=E_\perp+\epsilon_DD_*,\quad
G_*=G_\perp+\gamma_DD_*,\quad
G_{00}=G_\perp-
       \left(-263/38+263\omega/57\right)C^\perp .
$$
对齐次四次权 P，定义整条来源算子
$$
\mathfrak T_4(P)(z)=\Omega^{-4}
       \int P\,\exp(Az/\Omega)\,d\nu_4 .
$$
则完整原四轴返回准确给
$$
\boxed{
\begin{aligned}
2b\,\Phi_{N,p}(v)
=\mathfrak T_4\bigl[&
(\mathcal D_t^2\delta\widehat P_v)
 (D_*,E_\perp+\epsilon_DtD_*,G_\perp+\gamma_DtD_*)\\
-\eta\lambda\,&(\mathcal D_t^2\delta\widehat P_v)
 (D_*,\kappa E_\perp+\epsilon_DtD_*,
 G_{00}+\kappa(G_\perp-G_{00})+\gamma_DtD_*)\bigr],
\qquad \eta\in\{\pm1\}.
\end{aligned}
}
\tag{4}
$$
第二行就是 C 单位的完整深补项；$\eta$ 没有被猜定或删除。
微分先于显示的线性代入。
原 $N\in4\mathbf Z$ 支付 D 核符号，$\lambda^N,\kappa^{-2N}$
已经完整放在 (3)，故 (4) 全部系数整。

## 2. 四次伴随权的精确 C 消元

这里可利用原 C 分离，但不能直接忘掉 (4) 的 C 单位补项。
R590/R594 的整个四输入来源在实际坐标上是
$$
\nu_4=\nu_{B_C}\otimes\nu_{\rm flat,3},
$$
$$
\boxed{
\nu_{\rm flat,3}
=\frac1{42}
(\nu_{f_1}(Z_f)\otimes\nu_\Sigma(Q_f)
-\nu_{f_3}(Z_f)\otimes\nu_\Theta(Q_f))
\otimes\nu_\sigma(r_f),
}
\tag{5}
$$
$$
f_1=-xy\sigma^6,\quad f_3=-y\sigma^6,\quad
\Sigma=\sigma^2,\quad\Theta=x\sigma^2 .
$$
下标 f 区别于后两个原 sigma 的 $Q=c+2d,L=2c-d$。
原 B 纤维有
$$
m_{B_C}(0)=1,\qquad m_{B_C}(j)=0\quad(1\le j\le5).
\tag{6}
$$
又 $A\perp C$，所以在 $\mathfrak T_4(P)$ 中，
任意四次 P 的正 C 次数都被 (6) 严格消掉，保**任意 A 测试**。
这一步在 (4) 已付全部限制之后进行；没有把原 C 单位改成全域。

对原四输入行 $V=(V_1,V_2,V_3,V_x)$，忘 C 后的完整行是
$$
V^{\rm flat}=
\left((V_1-V_3-2V_x)/6,\ (V_1+V_3)/2,\ V_2\right).
\tag{7}
$$
特别
$$
A=\frac{-2+\omega}{2}Z_f+
   \frac{4+3\omega}{2}Q_f+2\delta r_f .
\tag{8}
$$
而 R665 的真实 $C^\perp=C+29D_*/143$ 给
$$
\boxed{
E_\perp^{\rm flat}=\frac{406}{143}D_*^{\rm flat},
\qquad
G_{00}^{\rm flat}=G_\perp^{\rm flat}
-\frac{29}{143}\left(-263/38+263\omega/57\right)D_*^{\rm flat}.
}
\tag{9}
$$
因此 (4) 的两个完整四次权，在 (6) 之后都只含
$D_*^{\rm flat},G_\perp^{\rm flat}$。
定义五条真正的固定来源
$$
\Gamma_a(z)=\mathfrak T_4(D_*^aG_\perp^{\,4-a})(z),
\qquad0\le a\le4.
\tag{10}
$$
对任何完整原六次多项式 P，(4) 的结果都落在
$\operatorname{span}\{\Gamma_0,\ldots,\Gamma_4\}$，
系数可依 $\lambda,\kappa,t$，但来源本身固定。
这对原固定多项式也成立，不仅对核方向成立。

(9) 用于来源计算，未给原真实物理域作商。
D/C 单位、原三个 A 伴随以及 (4) 两行的区别仍全在原系数中。

## 3. 五个 whole S29 系数的准确关系

整个 $\mathcal S_{29}^{\rm odd}$ 型零空间为
$$
\sigma_b(z)^{29}y_b(z)
 \operatorname{span}\{x_b^{13},x_b^{10},x_b^7,x_b^4,x_b\}.
\tag{11}
$$
其原首阶依次为 $0,6,12,18,24$，首系数均为 $-1$。
所以同一截面的这五个 Taylor 系数准确决定整条来源，
不能再有未读的更高分量。

附证书直接由 (5) 计算五条 (10) 的五个原系数。
所需总次数至多 $4+24=28$。
在 $b=1$ 的规范下，使用
$$
\sigma(z)=z+\frac{z^7}{210}
-\frac{z^{13}}{1801800}
-\frac{23z^{19}}{366648282000}
+\frac{31z^{25}}{77920092890640000}+\cdots .
$$
这些系数由 $x''=6x^2$、$\zeta'=-x$ 和 $\sigma'/\sigma=\zeta$
精确递推，不来自数值采样。
在 (5) 只需同时保 f1、f3、Σ、Θ 和最后 sigma，
然后取伴随总次数四及 A 次数 $0,6,\ldots,24$；
这读取的是整个 (11) 的五个系数。

精确五乘五矩阵的秩为四。
若整条来源写作
$$
F=\sigma_b^{29}y_b
(c_{13}x_b^{13}+c_{10}x_b^{10}+c_7x_b^7+c_4x_b^4+c_1x_b),
$$
其完整且唯一的线性关系是
$$
\boxed{47360b^4c_{13}+64b^2c_7-32bc_4-69c_1=0.}
\tag{12}
$$
在 $b=1$ 下，原 Taylor 五行的零关系为
$$
-\frac{631741726639849}{919725840000}[z^0]
-\frac{49003089602893}{59030373402000}[z^6]
-\frac{2656249}{4204200}[z^{12}]
+\frac{2953}{4830}[z^{18}]+[z^{24}]=0 .
\tag{13}
$$
经 (11) 的完整三角换基，(13) 的五个多项式系数准确为
$(47360,0,64,-32,-69)$。附证书对每条 $\Gamma_a$ 整体核验 (12)。

一般 b 的恢复使用实际
$\sigma_b(z)=\theta^{-1}\sigma_1(\theta z)$、
$x_b(z)=\theta^2x_1(\theta z)$、
$y_b(z)=\theta^3y_1(\theta z)$、$\theta^6=b$。
四个原 sigma 与四次伴随微分的尺度正好相消。
(11) 的第 j 个基向量尺度为 $b^{-j}$，故 (12) 的 b 幂如显示。
没有在高阶行中悄悄把 b 固定为一。

记 (12) 的四维空间为 $\mathscr H_{29,b}$。
在当前 $p\ge71$、$b=17$ 下，它是一个饱和整格，
例如可用以下四个完整截面作整基：
$$
\boxed{
\begin{aligned}
H_{13}&=\sigma_b^{29}y_b
       \left(x_b^{13}+\frac{47360b^4}{69}x_b\right),\\
H_{10}&=\sigma_b^{29}y_bx_b^{10},\\
H_7&=\sigma_b^{29}y_b
       \left(x_b^7+\frac{64b^2}{69}x_b\right),\\
H_4&=\sigma_b^{29}y_b
       \left(x_b^4-\frac{32b}{69}x_b\right).
\end{aligned}}
\tag{14}
$$
首四阶 $0,6,12,18$ 对此基是单位三角矩阵；
分母 $69=3\cdot23$ 在当前 ray 上是单位。

由 (4)、(9)–(12)，得到一个**全深度、全参数**结论：
$$
\boxed{\Phi_{N,p}(v)\in\mathscr H_{29,b}
\quad\text{对所有实际 }v,\lambda,\kappa,N\text{ 成立}.}
\tag{15}
$$
(15) 不是仅 $\kappa=0$ 的降秩，也不是只由某一个形式参数的秩猜测。

## 4. 原十一维核的像确实等于整个四维格

为计算整像，取原二十列中零起编号
$$
j=1,2,3,4,
\quad\text{即}\quad
CFG^4,\ CF^2G^3,\ CF^3G^2,\ CF^4G .
$$
令
$$
v_{p,j}=\Pi_pe_j\in\mathscr K_p.
\tag{16}
$$
在 (3) 的完整来源上，取四条归一行
$$
\mathcal L_r(F)=2b^{\,1-r}[z^{6r}]F,\qquad0\le r\le3 .
$$
置实际整矩阵
$$
M_{N,p}=\bigl(\mathcal L_r(\Phi_{N,p}(v_{p,j}))\bigr)_
 {0\le r\le3,\ 1\le j\le4}.
\tag{17}
$$
原 $p$ 大于全部所用阶乘，(14) 又是单位三角基，
所以这四行准确读取 $\mathscr H_{29,b}$ 的整格。

模 $p$ 时 $t=\kappa^N$ 与 $\kappa$ 均为零。
R667(12) 的同一个 C 单位减深域计算适用于每个 A 原阶；
得到五行固定矩阵
$$
J_\eta(\tau)=J_{\eta,+}+\tau J_{\eta,0}.
$$
它们已完整保存在附 JSON；没有只计算质量行。
对每个选定列，仍用完整核分子
$$
v_j(\tau)=
\frac{-e_j-B_0A_+e_j
+\tau(e_j-B_0A_0e_j-B_1A_+e_j)
-\tau^2B_1A_0e_j}{\tau-1}.
\tag{18}
$$
于是
$$
M_{N,p}\equiv
\left(J_\eta(\tau)v_j(\tau)\right)_
 {r=0,1,2,3;\ j=1,2,3,4}\pmod p .
\tag{19}
$$
其行列式准确是
$$
\boxed{\det\overline M_\eta(\tau)
       =\frac{\mathscr D_\eta(\tau)}{(\tau-1)^4},
       \qquad \deg\mathscr D_\eta=4,\quad
       \mathscr D_+\ne0,\quad\mathscr D_-\ne0.}
\tag{20}
$$
完整两个四次分子、五乘四原分子矩阵和全部核列都在附证书。

为显示非零不是有限素数实验，两个分子常数项的 1 坐标准确为
$$
[\mathscr D_+(0)]_1=
-\frac{216731247691009800361962020441926058695130626434133767542256}
       {311347008299229310951241069352240047959061045},
$$
$$
[\mathscr D_-(0)]_1=
\frac{138581750299933471814849395033437249051800157607640372723556}
     {311347008299229310951241069352240047959061045}.
\tag{21}
$$
两者都非零，故 (20) 是固定非零有理式。

一个包含全部附证书分母的固定整数为
$$
D_{670}=
15397075423381649360109832516351734054429358252252174532664768577202658430141281939406017060604390352981810723511042739200000 .
\tag{22}
$$
保原全部 ray 和坏集，再删除 $p\mid D_{670}$ 的有限集合。
将 (20) 两分子代 $\tau=T/(T-1)$ 后清固定分母，
对其乘积应用
[固定 CM 多项式单位密度引理](../notes/2026-11-14-fixed-cm-polynomial-unit-density.md)。
在原 ray 再删 $O(\sqrt X\log X)$ 个素数，两个分子同时为单位。
原 $\tau-1$ 已是单位。

于是对实际未知符号 $\eta$，在同一相对密度一子族上，
$$
\boxed{M_{N,p}\in{\rm GL}_4(\mathcal O)
       \quad\text{对全部 }N\in4\mathbf Z_{\ge1}\text{ 同时成立}.}
\tag{23}
$$
这里 (19) 与 N 无关；实际矩阵的所有 $\kappa,\kappa^N$
修正仍在 (17)，由整矩阵逆完整支付。

给定任意 $H\in\mathscr H_{29,b}(\mathcal O)$，
定义实际系数和核向量
$$
(a_1,a_2,a_3,a_4)^t
=M_{N,p}^{-1}(\mathcal L_0(H),\ldots,\mathcal L_3(H))^t,\qquad
v_H=\sum_{j=1}^4a_jv_{p,j}.
\tag{24}
$$
由 (15)、(17) 和单位三角性，
$$
\boxed{\Phi_{N,p}(v_H)=H,\qquad v_H\in\mathscr K_p.}
\tag{25}
$$
因此
$$
\boxed{\Phi_{N,p}(\mathscr K_p)
       =\mathscr H_{29,b}(\mathcal O)}
\tag{26}
$$
是实际完整来源的整满射，核为秩七的整直和项。
它不是对七条全部条件来源或两个 S/T 混合域的满射断言。

## 5. 合法取消整条 Λ₂ 的新测试及其准确代价

令 $F_{2,N}^{\rm old}$ 为 R666/R667 的原固定测试所给
$\Lambda_{2,N}$，按 (3) 作同一规范。
(4)–(15) 对原多项式也成立，故
$$
F_{2,N}^{\rm old}\in\mathscr H_{29,b}(\mathcal O).
$$
在 (24) 取 $H=-F_{2,N}^{\rm old}$，得到实际整核向量
$v_{N}^{\rm kill}$。定义一个明确区别于原测试的
$$
\boxed{
q_N^{\rm kill}=q_N+\delta q_{v_N^{\rm kill},N}.
}
\tag{27}
$$
原 $q_N$ 的定义、文件和系数均不改变。
这里 $v_N^{\rm kill}$ 可随 N 改变；所以新的 kill 家族不能直接继承
R666/R669 对同一固定多项式给出的 N 深度递推。
每个固定 N 的完整来源取消及其 n 方向身份仍按本篇原式成立。

(1)–(2) 及 (25) 给出同一个新测试的三条准确结论：

1. 原九条补偿约束、原 $\pi_4$ 算术推前及原局部首项全部保持；
2. 它的整个条件 A 来源 $\Lambda_{2,N}^{\rm kill}$ 恒等为零，
   不只是质量零；
3. 它的其余六条 $\Lambda_{k,N}^{\rm kill}$、两个 S 的共同观察、
   各自 E 浅门及原 Y 外部仍须按完整新测试计算。

第二条也有直接且必要的后果。
R665 的原角型证明对每个同家族多项式都成立，所以
$$
\boxed{
\Delta_{N,n}^{\rm kill}
=2\beta^n\kappa^{2n}J_N^{\rm kill}\mathscr H_p(\kappa^n)=0
\quad(n\ge N).
}
\tag{28}
$$
也就是说，取消整条 $\Lambda_2$ 会同时取消该新测试的全部已知
负一 L 深支，而不是保留一个非零首项来强迫原中央矛盾。
原固定 $q_N$ 的 R665 非零结论和准确赋值仍完全不变。

在 R664/R667 的两个 S/T 原词上，原测试的完整分区是
$$
\mathcal O_{i,n}^Z+\mathcal L_{i,n}^Z+\mathcal C_{i,n}^Z
=(-1)^i\lambda^n\beta^N J_Z^* .
$$
新旧测试的实际差仍严格满足
$$
\boxed{
\delta\mathcal O_{i,n}^Z+
\delta\mathcal L_{i,n}^Z+
\delta\mathcal C_{i,n}^Z=0 .
}
\tag{29}
$$
所有 E 浅 cut、原 Y 外部、T 的完整混合单位观察和 log 质量
都依 R667(25)–(27) 转置；不能把 (29) 改成三项各为零。

新测试的 R665 全补偿变为
$$
\mathcal E_+^{\rm kill}-\mathcal E_-^{\rm kill}
+\mathcal R_{N,n}^{\rm kill}=0 .
\tag{30}
$$
这与 (28) 一致，却没有分别消去两个原 T 外部或 L 浅项。
特别本篇没有证明“所有深共同域之外的补偿消失”。

本篇给出的真正有限改进是：原十一维核对 $\Lambda_2$
恰有一个可精确操作的四维整像，缺失方向由 (12) 付清；
取消这一个完整来源后仍有七维真实核和其余六条条件来源。
要继续原中央问题，必须把这些自由方向用于同一个完整 S/T
混合观察及 (29) 的全部外部，不能只反复调节已知的质量。

## 精确文件

- [check-r670-full-lambda-two-image-and-exact-cancellation.js](../scripts/check-r670-full-lambda-two-image-and-exact-cancellation.js)
- [check-r670-full-lambda-two-image-and-exact-cancellation.json](../scripts/check-r670-full-lambda-two-image-and-exact-cancellation.json)

脚本只读取已发表 R594 二十列/右逆，并从原 sigma 递推和
(5) 的完整三输入来源构造全部五行；它保存：
五条固定来源的完整五 jet 矩阵、三角换基、整关系 (12)、
两个 $\eta$ 的五乘二十矩阵、四个实际核列的全多项式分子，
以及两个非零四次行列式。
没有额外素数采样或未付的高阶 theta 分量。

主要依赖：
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md) 的原整九行；
[R664](R664-original-double-s-rotation-and-common-companion-gate.md) 的七个条件 A 来源；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md) 的完整四轴及单位补项；
[R667](R667-original-kernel-visible-mass-and-seven-source-contraction.md) 的真实十一维核和全算术补偿。
