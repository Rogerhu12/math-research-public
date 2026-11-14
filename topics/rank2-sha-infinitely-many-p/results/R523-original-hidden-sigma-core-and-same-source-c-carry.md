# R523 — 隐藏 CH 的绝对 sigma 核、同源 C/D carry 与非零算术小管

日期：2026-11-14。**状态：已证明。** 本篇在 R513、R519 的同一个原六输入中支付隐藏量 $C_H$ 的一层 scalar，并由真实共同深域支付其正交隐藏轴。对实际来源 $h=\omega^2\mathcal T_*\rho_0$，独立 sigma 输入 $C$ 与五 sigma 输出 $D$ 给至多两个实际来源的完整核心闭包。

其中的两单位近相消域准确回到同一来源。用原正伴随测试逐隐藏次数整逆，可把该 carry 的完整中央接回原 $S$；同一测试在一条明确的原输入小管上仍非零。所有旧 $W$ 条件、四个原五 sigma 伴随和 carry 补域都保留。这个非零子域尚不能排除完整中央中的抵消。

## 1. 新的真实隐藏轴及完整 odd 定标

保 R513 的
$$
C=C_4+C_H,\quad N(C_4)=72/103,\quad N(C_H)=31/103,
\quad C_4\perp C_H,
$$
以及
$$
Q_0\perp Q_b,\quad N(Q_0)=5,\quad N(Q_b)=515,\quad
a_0=\langle Q_0,C\rangle=(-11-5\delta)/14.
$$
在原输入顺序 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$ 中，定义
$$
\boxed{
B=103C_H=(31+\omega)\xi_1+(-21+21\omega)\xi_2
 +(-31-30\omega)\xi_3-c+(-2-3\omega)d_0.
}
\tag{1}
$$
这是一个真正的 CM 整行，不需要再加二倍覆盖。准确有
$$
N(B)=3193=31\cdot103,\qquad
B\perp Y,T_c,W,W',W_2,C_4.
\tag{2}
$$
五个非零系数模二均为单位，所以第一轴是标准 odd 半特征。

在已固定 ray 上增加
$$
\boxed{\pi_0\equiv1\pmod{31}.}
\tag{3}
$$
沿用 R509 的模 $103$ 条件、R513 的模 $49$ 条件以及 R518 已付
$\pi_0\equiv1\bmod1013$。(3) 是兼容的固定单位 CRT 细分。
它给
$$
g_\pi\equiv1\pmod{6386}=1\pmod{2\cdot3193}.
$$
完整 odd Heisenberg 交织遂为 scalar，但还须绝对锚。
令
$$
\gamma_{31}=5+6\omega=2+3\delta,\qquad N\gamma_{31}=31.
$$
非零固定来源
$$
\sigma(\gamma_{31}\gamma_{103}z)\in\mathcal S_{3193}^{\rm odd}
$$
的真实 core 是原 sigma 的 $\beta=-\lambda$。
因此在整个标准 odd 空间中，
$$
\boxed{K_{3193,p}=-I,\qquad B:\beta.}
\tag{4}
$$
(2) 使原十六个 $W$ 四挠来源都处于同一第一轴格；其第一参数
没有 flat twist。故 (4) 对原四态全部成立，保所有实际伴随。

## 2. 第二条隐藏 scalar 由相同事件支付

定义
$$
\boxed{D_H=31Q_0-a_0B.}
\tag{5}
$$
精确计算给
$$
N(D_H)=1612=4\cdot13\cdot31,\qquad D_H\perp B.
\tag{6}
$$
从 $(Q_0,Q_b)$ 到 $(B,D_H)$ 的行列式范数为 $49972/25$，
所有相关分母在当前普通处为单位。因此
$$
\{Q_0,Q_b\in p^n\}=\{B,D_H\in p^n\}
\tag{7}
$$
是同一个完整原输入事件。

R513 已付左侧的整个共同核心 $\lambda^{2n}$。
先取 $B$ 的 (4)，它固定 $D_H$；在 (7) 中取消这个真实推前，
准确得到
$$
\boxed{D_H:\beta,\qquad
\nu_\mu|_{\{B\in p^r,D_H\in p^s\}}
=\beta^{r+s}(P_{B,r}P_{D_H,s})_*\nu_\mu.}
\tag{8}
$$
这里 $\mu$ 可为原任意四态。证明使用整个共同事件和 (4)，
没有从范数 $1612$ 猜 whole theta scalar。
$B,D_H$ 都是纯 $Y$、纯旧 $W$ 伴随，原完整 CM 条件行可保它们。

## 3. 同一个 h 的独立 sigma 与原五输入

令
$$
h=\omega^2\mathcal T_*\rho_0,\qquad
C\mathcal T=\omega^2x
$$
为 R493、R506 的实际身份。定义
$$
\boxed{
D=31C-B=103C_4-72C,\qquad
A=D+72C=103C_4.
}
\tag{9}
$$
完整 Gram 为
$$
C\perp D,\quad N(C)=1,\quad N(D)=2232;
\qquad A\perp B,\quad N(A)=7416,\quad N(B)=3193.
\tag{10}
$$
两种正交输出的真正变换及反解是
$$
\boxed{
\binom A B=\begin{pmatrix}1&72\\-1&31\end{pmatrix}\binom D C,
\quad
\binom D C=\frac1{103}
 \begin{pmatrix}31&-72\\1&1\end{pmatrix}\binom A B.
}
\tag{11}
$$
其行列式 $103$ 在当前处为单位。

回到 $\mathcal T$ 之前的五个实际输入
$(\xi_1,\xi_2,\xi_3,c,d_0)$，(9) 的完整行是
$$
\boxed{
D\mathcal T
=30\omega\xi_1+21\omega^2\delta\,\xi_2-\omega\xi_3
 +c-\omega^2\gamma d_0.
}
\tag{12}
$$
它不含原自由 $x$；范数
$900+1323+1+1+7=2232$。
五个显示 CM 单位的乘积为一。
所以在保其余四个五 sigma 伴随时，$h$ 的 $C$ 输入确实是一个
独立 sigma。忘掉那四个伴随后，其准确 $(D,C)$ 生成函数为
$$
\boxed{
-\frac{\omega}{84}\,
\sigma(c)\sigma(30z)\sigma(21\delta z)\sigma(z)^2\sigma(\gamma z).
}
\tag{13}
$$
(13) 只是显示这个已付完整因式的边际，不把它拿来定义隐藏事件。

为完整保原五输入，写 (12) 的五个系数为
$\boldsymbol d=(30\omega,21\omega^2\delta,-\omega,1,-\omega^2\gamma)$。
以 $c$ 的系数一作 pivot，取
$$
R_j=\xi_j-\bar d_jc
\quad(j=\xi_1,\xi_2,\xi_3,d_0).
\tag{14}
$$
这些行与 $D$ 正交，整个 $(D,\mathbf R)$ 矩阵行列式为
$\pm2232$，当前处为单位；四个 $R_j$ 的完整非对角 Gram 保留。
$C$ 是原独立 sigma 输入，旧 $W$ 是这些四个 $R_j$ 的线性函数。
下文从不忘掉 $\mathbf R$ 的原事件。

## 4. 两个 even 核和同一个来源交换

原 $g_\pi\equiv91+72\omega\bmod144$，并有模 $31,103$ 的一型。
完整 CRT 计算给
$$
\begin{array}{c|c|c}
N&g_\pi\bmod 2N&g_\pi^2\bmod2N\\ \hline
2232&1675+2232\omega&2233=1+2232\\
7416&5563+7416\omega&7417=1+7416.
\end{array}
\tag{15}
$$
在 $h$ 的实际 $\mathcal T$ 表示中，(12) 的第一 theta 空间是
标准 even $\mathcal S_{2232}$；$A\mathcal T$ 的六个系数同样为
CM 整数且有四个 odd 系数，给标准 even $\mathcal S_{7416}$。
它们与相应全部伴随的交叉项为零。

(15) 在整个 Heisenberg 群上使两个平方各为 scalar。
非零锚
$$
\Theta(6\gamma_{31}z)\in\mathcal S_{2232},
\qquad
\Theta(6\gamma_{103}z)\in\mathcal S_{7416}
$$
均为原 degree2 来源的单位 CM 拉回，其归一核心为 $-1$。
所以在两个整个空间中准确有
$$
\boxed{K_{2232,p}^2=K_{7416,p}^2=I.}
\tag{16}
$$
这是 $h$ 实际表示中的更小空间；不将它免费用于 R519 中原
$\rho_0$ 的更大第一覆盖。

在 (11) 的同一个两输入同时深域中，先取 $C$ 或先取 $B$ 的
$\beta$ 核，再取另一 even 轴。两种物理同时缩放相同，故取消
共同 $-\lambda^2$ 和真实推前，得到完整来源身份
$$
\boxed{K_Dh=K_Ah=:h_1,\qquad h_0:=h.}
\tag{17}
$$
由 (16)，两个 even 核都交换 $h_0,h_1$。
$K_D$ 只动五输入而固定独立 sigma $C$，所以 $C$ 在两来源上
均保 $\beta$；由 $A\perp B$，$K_A$ 同样保 $B$ 的 $\beta$。
因此完整核心表为
$$
\boxed{
\begin{array}{c|cc}
\text{轴}&h_0&h_1\\ \hline
C&\beta h_0&\beta h_1\\
B&\beta h_0&\beta h_1\\
D&\lambda h_1&\lambda h_0\\
A&\lambda h_1&\lambda h_0 .
\end{array}}
\tag{18}
$$
表中每项还乘对应的真实物理压深。
这给至多两个实际来源的闭包，不需要另声称它们线性独立。
旧 $W$ 在两来源上仍有归一核 $-1$；所有表项都固定 $W$。
$h_1$ 仍有独立 sigma $C$，故其整个 $W$ 边际也为零。

## 5. 真正的两单位 carry 和完整隐藏矩

对 $r\ge1$，定义同一个完整域
$$
\boxed{
\Gamma_r=\{A\in p^r,\ C,D\text{ 均为单位}\}
        =\{A\in p^r,\ B\text{ 为单位}\}.
}
\tag{19}
$$
这是 (11) 的逐点等价；$72,103$ 都是单位。
记 $P_{A,r}$ 为真实 $A$ 压深，它就是 $P_{4,r}$，但本篇在
$h_0,h_1$ 上可以用任意深度并保来源交换。

对任意完整连续测试 $F$，准确有
$$
\boxed{
\int_{\Gamma_r}F(A/\kappa^r,B,\mathbf R)\,dh_i
=\lambda^r\int_{B\ {\rm unit}}
 F(A,B,\mathbf R)\,dh_{i+r\bmod2}.
}
\tag{20}
$$
逆尺度只用于 $A\in p^r$ 的实际像。
若 $F$ 不依赖 $B$，右侧准确变成
$\lambda^r(1+\lambda)$ 倍同一来源的 $(A,\mathbf R)$ 推前。
若附 $B^j$，因子则为
$$
\boxed{1+\lambda\kappa^j.}
\tag{21}
$$
(20) 保全部 $B$ 测试和四个原伴随；不能将 (21) 对 $j=0$
的值拿来替代其余矩。

## 6. 已知原 S 行的有限 B-unit 整逆

R497 的无常数项固定正多项式为
$$
\mathfrak h_b(t)=\sum_{k=1}^6c_kb^{-k}t^{6k}.
\tag{22}
$$
$c_k$ 采用该篇 (16)–(19) 的精确有理数。
对 $h=\omega^2\mathcal T_*\rho_0$，它的真实伴随是
$$
T_h=T_c\circ\mathcal T^{-1}
=\gamma Y-34\omega C.
$$
故整条来源身份为
$$
(Y)_*\{\mathfrak h_b(T_h/\Omega)\nu_h\}
=\omega^2\nu_S.
\tag{23}
$$
没有先加 $T_h$ 单位指示。

置
$$
\epsilon=\frac{34\omega}{103},\qquad
T_0=\gamma Y-\epsilon A,\qquad T_h=T_0-\epsilon B.
\tag{24}
$$
$T_0,B$ 都是真正的 $Y$ 伴随，且 $T_0$ 与 $B$ 正交。
定义完整有限多项式
$$
\boxed{
\widehat{\mathfrak h}_p
=\sum_{k=1}^6c_kb^{-k}
 \sum_{j=0}^{6k}\binom{6k}{j}
 \frac{(-\epsilon)^j}{1+\lambda\kappa^j}
 (T_0/\Omega)^{6k-j}(B/\Omega)^j .
}
\tag{25}
$$
所有分母都是单位。$j>0$ 时显然如此；若 $1+\lambda$ 非单位，
则 $\pi_0\mid\bar\pi_0-1$，故 $p\mid\operatorname{Tr}\pi_0-1$。
$p\ge71$ 与复绝对值界迫 $\operatorname{Tr}\pi_0=1$，
却与 $\pi_0\equiv1\bmod27$ 的迹同余二矛盾。

对 (25) 逐 $B$ 次数用 (21)，得到完整第一测度身份
$$
\boxed{
(Y)_*\{{\bf1}_{B\ {\rm unit}}\widehat{\mathfrak h}_p\,dh\}
=\omega^2\nu_S.
}
\tag{26}
$$
这里 $j=0$ 的项完整除以 $1+\lambda$，没有把它漏掉。
每个展开项仍有总次数 $6k$，原 principal 型保持。

取正偶数 $r$。在 $\Gamma_r$ 上令
$$
Y_r=Y+\frac{a_Y}{72}(\kappa^{-r}-1)A,\qquad
T_{0,r}=\gamma Y_r-\epsilon A/\kappa^r,
\quad a_Y=1+3\omega.
\tag{27}
$$
这准确撤回 $A$ 的物理压深，其余四伴随与 $B$ 全保。
将 (25) 中 $T_0$ 换成 $T_{0,r}$ 得 $\widehat{\mathfrak h}_{p,r}$。
(20)、(26) 给真正的算术 carry 行
$$
\boxed{
\int_{\Gamma_r,\ Y_r\ {\rm unit}}
 \langle Y_r\rangle^{du}
 \widehat{\mathfrak h}_{p,r}\,dh
=\lambda^r\omega^2J_S(u),\qquad 2\mid r.
}
\tag{28}
$$
第一单位条件和整个测试都按 (27) 移动。
没有把原未归一化 $Y$ 当作这个已知中央权。

## 7. 实际新测试的完整首五阶

仍在 $\mathcal T$ 之前的原五输入上计算。
令
$$
\boldsymbol z=(\delta,2\delta,\gamma,1,2),\quad
\boldsymbol d=(30\omega,21\omega^2\delta,-\omega,1,-\omega^2\gamma),
$$
$$
\ell_i=\gamma z_i-\epsilon d_i,\qquad q=-1727/103.
\tag{29}
$$
原 $Y$ 是 $Z+\bar\gamma x$，
$T_h=\gamma Z-27x$，而 $T_0$ 准确变成
$$
T_0=\sum_i\ell_i\xi_i+qx.
\tag{30}
$$
这保全部五个独立输入，没有将 $\sum d_i\xi_i$ 和 $Z$ 认作
一个输出。

由 (25)，在固定系数整的普通处，
$$
\widehat{\mathfrak h}_p
\equiv\mathfrak h_b(T_h/\Omega)
-\frac{\lambda}{1+\lambda}\mathfrak h_b(T_0/\Omega)\pmod p.
\tag{31}
$$
第一项的完整第五阶常数是 R497 的 $\alpha\ne0$。
下面给第二项的精确有限公式，避免从有限模数猜整体。

写
$$
\sigma_{b=1}(z)=z\sum_{j\ge0}a_jz^{6j},\qquad
\prod_{i=1}^5(\ell_i+z_i s)=\sum_{a=0}^5P_as^a.
$$
$a_0,\ldots,a_5$ 由 R497(11) 的原有理递推取得。
定义
$$
\boxed{
\begin{aligned}
\alpha_0=-\frac1{84}
\sum_{k=1}^6&c_k(6k-5)!\,a_{k-1}
 \sum_{a=1}^5\frac{(-1)^{a-1}}a
 \binom{6k}{5-a}q^{6k-5+a}\bar\gamma^{-a}\\
&\hspace{27mm}\cdot a!(5-a)!\,P_a .
\end{aligned}}
\tag{32}
$$
这个公式正是 log 的 $a$ 次项与多项式的 $5-a$ 次项的全部
碰撞。$a=0$ 的 log 常数及加权 sigma 矩并未在完整积分中删除，
只在模 $p$ 的单位判断时使用它们属于 $p\mathcal O$。
将 (32) 的 $\ell_i,q$ 换成 $\gamma z_i,-27$，精确返回 R497
显示的整个 $\alpha$；附脚本严格核了这个校准。

因此新同深解析积分的第五阶满足
$$
\boxed{
[T^5]\widehat{\mathcal A}_p
\equiv\frac{\omega^2d}{b}\,
 \frac{\alpha+\lambda(\alpha-\alpha_0)}{1+\lambda}
 \pmod p.
}
\tag{33}
$$
$\alpha_0/\alpha$ 的 $\delta$ 坐标非零，不能把该式擅自认成
原来的单位；下一节支付这个实际因子。

## 8. 沿现有 1013 ray 的严格单位证明

清 $\alpha$ 和 $\alpha-\alpha_0$ 四个有理坐标的最小公倍数
分母 $D_*$，置
$$
u=D_*\alpha,\qquad v=D_*(\alpha-\alpha_0)\in\mathbf Z[\omega].
\tag{34}
$$
这两个固定整数都非零。附 JSON 完整列出 $D_*,u,v$、
两范数及下面的固定门槛。

复用 R518§5 的 Norm–Trace 引理，保持同一个门槛规范：
若
$$
\boxed{p>(Nu+Nv+1)^2,\qquad p\nmid D_*}
\tag{35}
$$
而 $u\bar\pi_0-v$ 不是普通处的单位，则
$$
p\mid N(u\bar\pi_0-v)
=Nup-\operatorname{Tr}(u\bar v\bar\pi_0)+Nv.
$$
由 $|\operatorname{Tr}(u\bar v\bar\pi_0)|
\le2\sqrt{NuNv}\sqrt p$ 和 (35)，严格迫使
$$
\operatorname{Tr}(u\bar v\bar\pi_0)=Nv.
\tag{36}
$$
本篇实际整数的精确证书是
$$
\boxed{
\begin{array}{c|ccccc}
\bmod1013&D_*&Nu&Nv&\operatorname{Tr}(u\bar v)&
 \operatorname{Tr}(u\bar v)-Nv\\ \hline
&183&224&484&88&617 .
\end{array}}
\tag{37}
$$
R518 已付的同一个 $\pi_0\equiv1\bmod1013$ 排除 (36)。
所以在该固定 ray、(3)、(35) 以及原固定坏集之外，
$$
\boxed{\alpha+\lambda(\alpha-\alpha_0)\in\mathcal O^\times.}
\tag{38}
$$
不需要再选择一个随 $p$ 变化的类，也不需要新的大模数。
(35) 虽是很大的固定有限门槛，却不影响该固定 ray 上普通素数
的无穷性。所有固定整数由 (29)、(32)、(34) 完全确定，
不是没有说明的有效常数。

## 9. 同一原输入小管仍非零，并真实进入 carry

在 $h$ 的原 $\mathcal T$ 表示中，取
$$
\boxed{
\mathcal D_n^h
=\{\text{五个原 sigma 输入均在 }p^n,\ x\text{ 单位}\}
=\{D,\mathbf R\in p^n,\ C\text{ 单位}\},
\qquad n\ge1.
}
\tag{39}
$$
此时 $Y$、$B=31C-D$、$A=D+72C$ 全为单位。
$B$ 单位指示没有改变该小管上的 (25)。

五个原输入的同时深核给系数 $\beta^{5n}$。
低于第五阶的项全部由五个独立 sigma 的质量零消失。
(33)、(38) 给单位第五阶。
测试次数至多三十六、其全部系数整，故对高项仍有
$$
v_p([T^j]\widehat{\mathcal A}_p)\ge-\lfloor\log_pj\rfloor.
$$
$p\ge71,j>5,n\ge1$ 时 $jn-\lfloor\log_pj\rfloor>5n$。
因此
$$
\boxed{
v_p\!\left(
 \int_{\mathcal D_n^h}d\log\langle Y\rangle
                  \widehat{\mathfrak h}_p\,dh
\right)=5n.
}
\tag{40}
$$
这里没有把整条中央非零偷换成小管非零。

对正偶数 $r$，令
$$
\mathcal D_{n,r}^h=P_{A,r}\mathcal D_n^h.
$$
利用 (11)、(14)，其完全等价的实际条件为
$$
\boxed{
A/\kappa^r\in\mathcal O,\quad B\text{ 单位},\quad
\mathbf R\in(p^n)^4,\quad
31A/\kappa^r-72B\in p^n.
}
\tag{41}
$$
因 $p\ne31$，(41) 自动使 $A/\kappa^r$ 为单位，
也使原 $C=(A/\kappa^r+B)/103$ 为单位。
所以这个域的 $A$ 深度准确为 $r$，且严格位于同一个
$\Gamma_r$ 中。它还保 $W\in p^n$：原五输入全深时如此，
而 $P_{A,r}$ 固定旧 $W$。

按 (27) 运输整个第一单位权与测试，(18)、(40) 给
$$
\boxed{
v_p\!\left(
 \int_{\mathcal D_{n,r}^h}d\log\langle Y_r\rangle
                \widehat{\mathfrak h}_{p,r}\,dh
\right)=5n,\qquad 2\mid r.
}
\tag{42}
$$
来源系数 $\lambda^r$ 为单位，故没有改变该赋值。
这是原五 sigma 非零网格的真实像，不是凭输出数量相同定义的
替代隐藏事件。

最后，(28) 的完整中央必须分成
$\mathcal D_{n,r}^h$ 与
$$
\{\Gamma_r,\ Y_r\text{ 单位}\}\setminus\mathcal D_{n,r}^h.
\tag{43}
$$
在 $J'_S(0)=0$ 的反证假设下，(43) 的中央准确等于 (42) 的负值。
该补域包含其余 $\mathbf R$ 条件和真实近相消支；本篇不把它置零。
原旧 $W$ 核若继续使用，也须移动 (27)、(41) 中的整个测试和域。

## 证书与依赖

- [完整隐藏轴、whole 中心及第五阶程序](../scripts/check-r523-hidden-sigma-core-and-c-carry.mjs)；
  [完整精确数据](../scripts/check-r523-hidden-sigma-core-and-c-carry.json)。
  同一 BigInt/CM 函数已在 V8 执行，包含全部原六行、两框架、
  两个中心平方、固定测试、$\alpha$ 校准、$\alpha_0$ 及 (37)。
- [R513：原隐藏输入及 C4/CH 分解](R513-original-hidden-odd-cores-and-b0-reflection-kernel.md)。
- [R519：原 C4 whole 八层返回和全部 B0 移权](R519-original-c4-eighth-core-and-complete-b0-transport.md)。
- [R518：已付固定 Norm–Trace 引理及 1013 ray](R518-original-e-unit-inverse-and-same-source-arithmetic-carry.md)。
- [R497：原正伴随多项式、完整来源抽取和第五阶规范](R497-original-degree918-positive-companion-and-six-sigma-arithmetic-grid.md)。
- [R506：原独立 C-sigma、真实反射和旧 W](R506-original-reflection-axis-four-core-and-complete-w-c-rectangles.md)。

本篇支付了真正的一层隐藏 sigma 核、同源两输入 carry、完整
算术行和其中非零的原输入小管。固定曲线上无穷多个 $p$ 的主目标
仍需控制 (43) 这类完整补域；新增来源 $h_1$ 未被另赋算术身份。
