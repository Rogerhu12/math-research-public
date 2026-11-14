# R345 — 原 degree 三的绝对 core 相位、全部普通环带单位与中间 Cartier 行

日期：2026-11-13。**状态：以下原范数迹的完整三挠交织、绝对六次相位、
全部普通素数的单位质量，以及真实 Verschiebung 核的中间 Cartier
系数均已证明。这里没有证明原两条固定负矩联合非零，也没有把辅助
质量的单位性当作原目标中央导数非零。主目标未完成。**

本文补上 [R341](R341-original-active-triple-joints-degree-three-core-and-overlap-source.md)
留下的实际相位，接 [R336](R336-ordinary-original-zeta-as-verschiebung-and-two-full-negative-rows.md)
及 [R343](R343-original-three-torsion-phase-and-two-complete-faber-observers.md)
的真实核多项式。全部比较仍在原 $E_{17}$ 周期、原 sigma 半特征和
原普通测度内。

## 1. 同一原规范与结论

令
$$
E_b:y^2=x^3+b,\qquad b=17,\qquad
K=\mathbf Q(\delta),\quad \delta^2=-3,\quad \omega=(\delta-1)/2,
$$
$$
D=d/dz,\quad x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,
\quad \sigma=z+\cdots,\quad \Theta=x\sigma^2.
\tag{1}
$$
对普通 $p=6s+1>7$，采用 R300、R316 的实际 CM 嵌入和参数
$$
\pi=\psi_b(\mathfrak p),\quad \pi\bar\pi=p,\quad
v_p(\pi)=1,\quad
\varepsilon=\psi_0(\mathfrak p)/\psi_b(\mathfrak p)
=\left(\frac b{\mathfrak p}\right)_6,
\quad \kappa=p/\bar\pi^2.
\tag{2}
$$
原测度的 Amice 变换是 $G(\Omega_p\log(1+Z))$，并保持
$$
T_p=\bar\pi[\bar\pi^2]_*\psi_p,
\qquad \psi_p\nu=(x\mapsto x/p)_*(\nu|_{p\mathbf Z_p}).
\tag{3}
$$
以下三个真正截面构成整个 $\sigma^3L(3O)$：
$$
A=\sigma^3,\qquad B=x\sigma^3=\sigma(\delta z)/\delta,
\qquad C=y\sigma^3=-\sigma(2z)/(2\sigma(z)).
\tag{4}
$$
它们的 $\mu_6$ 型为 $3,1,0$，质量为 $0,0,-1$。
R341 已通过实际三输入微分多项式证明 $C$ 的有界整测度，而不是
从 (4) 的商擅自定义一个 Mellin 商。

**定理 1。** 令 $\eta_p\in\mu_6$ 是唯一满足
$$
\pi\eta_p\equiv1\pmod{3\mathcal O_K}
\tag{5}
$$
的单位。则完整原算子准确为
$$
\boxed{T_p A=\eta_p A,\qquad
T_p B=\varepsilon^3B,\qquad T_p C=\eta_p C.}
\tag{6}
$$
而且
$$
\boxed{
\eta_p=\frac{\psi_{1/4}(\mathfrak p)}{\psi_b(\mathfrak p)}
=\left(\frac{4b}{\mathfrak p}\right)_6
=\varepsilon\left(\frac2{\mathfrak p}\right)_3.
}
\tag{7}
$$
$\psi_{1/4}$ 是固定曲线 $y^2=x^3+1/4$ 的实际 CM 角色。此处
不需要该曲线的解析秩或任何未证特殊值。

特别置 $\pi^\circ=\psi_{1/4}(\mathfrak p)$，则
$$
\boxed{\lambda_C=\lambda_A=\eta_p/\bar\pi=1/\bar\pi^\circ.}
\tag{8}
$$
对每个普通 $p>7$，$1-\lambda_C$ 都是单位，因而 R341 的全部
$C$ 环带质量都是单位。证明先确定绝对相位，再证明单位性。

## 2. 原周期中的真正对称三挠 lifts

记 $\Gamma$ 为 (1) 的复周期格，$\eta_\Gamma$ 为它原来的准周期。
对非零 $T\in E_b[3]$ 选一个复 lift，仍记为 $T$，满足 $3T\in\Gamma$。
在原三次线丛上定义
$$
\boxed{
(U_Ts)(z)=
\frac{\exp(-\eta_\Gamma(3T)z)}{2y(T)\sigma(T)^3}\,s(z+T).
}
\tag{9}
$$
这同时保留了原周期指数和常数。一般不能把指数中的
$\eta_\Gamma(3T)$ 换成 $3\zeta(T)$；两者的差正是一般三挠点的
非零 reduced zeta，删去后就丢失了真实切线的线性项。

原 sigma 的准周期公式和 Legendre 关系说明
$$
e^{-\eta_\Gamma(3T)z}
\frac{\sigma(z+T)^3}{\sigma(z)^3\sigma(T)^3}
\tag{10}
$$
是椭圆函数，除子为 $3(-T)-3(O)$，首 Laurent 项为 $z^{-3}$。
因此它就是在 $-T$ 的切线函数的负值；常数由首项完全确定。
这给 (9) 的代数矩阵，也证明不同复 lift 不留下未定的周期倍数。
这里只用复 sigma 核定 algebraic theta lift；没有在非正式的
$p$-adic 三挠点上非法代入一个局部 sigma 级数。

取
$$
\beta^2=b,\quad Q=(0,\beta),\qquad
R=(a,c),\quad a^3=-4b,\quad c=-\delta\beta.
\tag{11}
$$
真实 CM 公式
$$x(\delta z)=-\frac{x^3+4b}{3x^2},\qquad
y(\delta z)=\frac{y(x^3-8b)}{\delta^3x^3}
$$
在 $R$ 给 $\delta R=Q$。在基 $(A,B,C)$ 中，列表示各基向量的像，
(9) 准确给
$$
\boxed{
U_Q=\begin{pmatrix}
-1/2&0&3\beta/2\\
0&1&0\\
-1/(2\beta)&0&-1/2
\end{pmatrix},\qquad
U_R=\begin{pmatrix}
1/2&-a/2&c/2\\
-1/a&0&c/a\\
-1/(2c)&-a/(2c)&-1/2
\end{pmatrix}.
}
\tag{12}
$$
为核定全部常数，在 $Q$ 处未除 $2\beta$ 的三列分别是
$-C-\beta A,2\beta B,3bA-\beta C$。
在 $R$ 处令 $m=3a^2/(2c)=2c/a$，在 $-R$ 的切线为
$y+mx-c$；未除 $2c$ 的三列分别是
$$cA-mB-C,\qquad -acA-aC,\qquad c^2A+cmB-cC.$$
它们由椭圆加法式逐项得出；例如切线乘积
$(y-mx+c)(y+mx-c)=(x-a)^3$ 支付全部分母。

令 $J:s(z)\mapsto s(-z)$，其矩阵是 $\operatorname{diag}(-1,-1,1)$。
直接计算得
$$
\boxed{
U_Q^3=U_R^3=1,\quad JU_QJ=U_Q^{-1},\quad JU_RJ=U_R^{-1},
\quad U_QU_R=\omega U_RU_Q.
}
\tag{13}
$$
特别这是完整 Heisenberg 作用，包含中心相位。
对每个三挠平移，满足 order 三和 $JU_TJ=U_T^{-1}$ 的 lift 唯一：
两个 order 三 lifts 之比属于 $\mu_3$，而对称性再要求该比的平方为一。
这解释了为何后文的对称规范不再留下一个任意三次根。

由 (13)，$R+kQ$ 的同一个唯一对称 lift 为
$$\boxed{U_{R+kQ}=\omega^kU_Q^kU_R\qquad(k\in\mathbf F_3).}\tag{14}$$
其 order 三和对称性可直接核定，因而不是只按 projective 矩阵
选择的相位。

## 3. 范数 p 的完整交织方向及绝对标量

对原奇范数 CM 元 $h$，仍取
$$r_h(z)=\frac{\sigma(hz)}{\sigma(z)^{Nh}}.$$
R300 的逐支 division 证明，以及 R316 对奇 sigma 半特征的核定，
在 $N=3$ 给同一个原算子
$$
\boxed{
T_p(\sigma^3f)=\frac{\bar\pi}{p}\sigma^3
\operatorname{Tr}_{[\pi]}
\left[\left(\frac{r_{\bar\pi}}{r_\pi}\right)^3
f\circ[\bar\pi]\right].
}
\tag{15}
$$
这不是裸的有理函数迹。$r_h$ 的首项常数为 $h$，且是偶函数；
原三次 CM 格使 Gaussian 完全相消，奇范数还保持奇 sigma 的
二挠半特征。(15) 中所有这些因子都保留。

**准确交织为**
$$
\boxed{T_pU_T=U_{gT}T_p,\qquad
g=\pi\bar\pi^{-1}\in(\mathcal O_K/3)^\times.}
\tag{16}
$$
这里是 $\pi/\bar\pi$，不是它的逆。确实，先沿 $[\bar\pi]$
拉回，一个输入平移 $T$ 变成 $\bar\pi^{-1}T$；再沿 $[\pi]$
推迹，输出的平移就是 $\pi\bar\pi^{-1}T$。
也可以在 (15) 的每支 $\pi w=z$ 上直接以
$w\mapsto w+\bar\pi^{-1}T$ 换元，得到同一方向。

还需付清该计算的中心常数。原 $r_h^3$ 给
$[h]^*\mathcal O(3O)\simeq\mathcal O(3pO)$ 的真实对称同构：
$r_h$ 偶，因此它与 $J$ 交换。两侧的三挠 lifts 都由这个同构
传送，并保留 order 三及对称性。推迹的支置换也保留两者。
由于 $p\equiv1\pmod3$，中间线丛的三挠交换子 $e_3^p$ 正是 $e_3$。
于是任何可能的标量差都在 $\mu_3$ 内，且同时等于自己的逆；
由 §2 的唯一性它必为一。这证明了 (16) 的绝对相位。
给 $r_h$ 同时提出其首项 $h$ 只改变整个 (15) 的公共标量，
不改变此交织；这个公共标量将在下一段用真实 $B$ 行固定。

写
$$
\pi\equiv a_0+c_0\delta\pmod3,\qquad
a_0\in\{1,-1\},\quad c_0\in\mathbf F_3.
\tag{17}
$$
因为 $\delta^2=0$ 在 $\mathcal O_K/3$ 中，
$$
g=1+2(c_0/a_0)\delta,\qquad
gQ=Q,\quad gR=R+kQ,\quad k=2c_0/a_0.
\tag{18}
$$
实际 Frobenius 在 $Q=(0,\sqrt b)$ 上的作用是
$b^{(p-1)/2}$；另一方面 $\delta Q=0$，故 (17) 在该点作用为
$a_0$。因此
$$a_0=b^{(p-1)/2}=\varepsilon^3.\tag{19}$$

$U_Q$ 的三个不同本征线准确为
$$
B\ (1),\qquad v_+=C-\delta\beta A\ (\omega),\qquad
v_-=C+\delta\beta A\ (\omega^2).
\tag{20}
$$
由 (16)，$T_p$ 在这些线上对角。$B=\sigma(\delta z)/\delta$ 的
尺度是普通单位，且该缩放与原 (3) 交换；所以 R316 的已付完整
sigma core 直接给
$$T_pB=\varepsilon^3B=a_0B.\tag{21}$$
这正是绝对标量的锚，不是从有限项目表示猜测标量。

若三条线的 $T_p$ 本征值依次为 $m_0,m_1,m_2$，(14)、(16) 及
$U_RB=-a\,v_+/(2c)$ 给
$$m_{j+1}/m_j=\omega^{k(j+2)}\quad(j\bmod3).$$
故
$$
m_0=a_0,\qquad m_1=m_2=a_0\omega^{2k}
=a_0\omega^{c_0/a_0}.
\tag{22}
$$
将 (20) 换回 $(A,B,C)$ 即证明 (6)，其中
$\eta_p=a_0\omega^{c_0/a_0}$。
由于 $\omega=1-\delta\pmod3$，逐项乘法给
$$
(a_0+c_0\delta)\,a_0(1-(c_0/a_0)\delta)=1\pmod3.
$$
所以它满足 (5)。六个 $\mu_6$ 单位在 $(\mathcal O_K/3)^\times$
中各不相同，且该群恰有六个元素，证明唯一性。

## 4. 固定参考曲线支付角色及全普通单位性

考虑
$$E^\circ:y^2=x^3+1/4.$$
它的全部八个非零三挠点都是 $K$-有理的：
$$
(0,\pm1/2),\qquad
(-1,\pm\delta/2),\quad(-\omega,\pm\delta/2),
\quad(-\omega^2,\pm\delta/2).
\tag{23}
$$
曲线方程和三除法多项式 $3x(x^3+1)$ 直接核定这张完整表。
因此对于每个当前的分裂好素数，其实际 Frobenius
$\pi^\circ=\psi_{1/4}(\mathfrak p)$ 在 $E^\circ[3]$ 上恒等，给
$$\pi^\circ\equiv1\pmod3.$$
它与原 $\pi$ 生成同一个素理想，故 $\pi^\circ/\pi\in\mu_6$；
由 (5) 的唯一性，$\pi^\circ/\pi=\eta_p$。

这也准确确定了剩余角色的方向。由 $u^6=1/(4b)$ 的同构
$(x,y)\mapsto(u^2x,u^3y)$，Frobenius 交换差为坐标自同构
$u^{p-1}$。在 (1) 的解析参数中，坐标乘 $(v^2,v^3)$ 对应
CM 元 $v^{-1}$，所以实际 Hecke 比值的约化是
$$\eta_p\equiv(4b)^s\pmod{\mathfrak p}.$$
$\mu_6$ 在剩余域中单射，这给完整特征零单位 (7)，而非任取
这个剩余数的某个 lift。

取共轭后，$\bar\pi^\circ=\eta_p^{-1}\bar\pi$，所以 (8) 成立。
假设 $1-\lambda_C$ 不是单位，则选定的 $\mathfrak p$ 整除
$\bar\pi^\circ-1$，从而
$$
p\mid N(\bar\pi^\circ-1)=\#E^\circ(\mathbf F_p).
$$
由 (23)，该点数被九整除。另一方面 Hasse 界在 $p>7$ 给
$$0<\#E^\circ(\mathbf F_p)<2p.$$
若它被 $p$ 整除，就只能等于 $p$，与九的整除性矛盾。因此
$$\boxed{1-\lambda_C\in\mathcal O_p^\times}\tag{24}$$
对所有当前普通素数成立。这也可表成 trace 的独立短证：
若损失单位则 $\operatorname{Tr}(\pi\eta_p)=1$，但 (5) 迫该
trace 模三为二。此处正好排除 R341 的全部薄例外候选。

## 5. 原整测度、全部深度与 tame 均保留

(6) 是完整测度等式，因此
$$
\boxed{
\nu_A|_{p\mathbf Z_p}=\lambda_C[\kappa]_*\nu_A,
\qquad \nu_C|_{p\mathbf Z_p}=\lambda_C[\kappa]_*\nu_C.
}
\tag{25}
$$
对每个 $n\ge0$，准确有
$$
\boxed{
\nu_C(p^n\mathbf Z_p)=-\lambda_C^n,\qquad
\nu_C(p^n\mathbf Z_p^\times)=-\lambda_C^n(1-\lambda_C).
}
\tag{26}
$$
两者都是单位。$A$ 的全部深度和环带质量则为零。
R341 的 $\rho_2=-[\delta^{-1}]_*\nu_C$ 因此有正的代数规范质量
$\lambda_C^n$ 与 $\lambda_C^n(1-\lambda_C)$；这里“正”仅指所写
符号，不赋予 $p$-adic 测度实数的正性。

设 $C=\sum C_mz^m$。完整正权矩为
$$
\int_{\mathbf Z_p^\times}x^m\,d\nu_C
=(1-\lambda_C\kappa^m)\Omega_p^m m!C_m.
\tag{27}
$$
第 $n$ 环带输出除以 $p^n$ 后，tame $j$ 分支及 weight $u$ 的
完整尺度仍为
$$
\lambda_C^n\tau(\bar\pi)^{-2nj}
\langle\bar\pi\rangle^{-2n(p-1)u}.
\tag{28}
$$
因此所有尺度导数和 carry 继续存在。尤其 $\lambda_C$ 是单位，
不是 $p$ 的倍数；不能因 (26) 的单位性而删去无限深度边界。
准确有限分解仍为 R341 的
$$
\nu_C=\sum_{n=0}^{N-1}\lambda_C^n[\kappa^n]_*(\nu_C^\times)
+\lambda_C^N[\kappa^N]_*\nu_C.
\tag{29}
$$

## 6. 从实际 C core 到真实核的中间 Cartier 系数

这一步把相位接到 R336 的实际 $p$ 同源，并非从核底部直接猜中间项。
记
$$
H=\binom{3s}{s}b^s=\bar\pi\bmod\mathfrak p,\qquad
f_V=P(X),\quad X=x^3,\quad \deg P=s,\quad P\text{ monic},
$$
$$
T=36X(X+b)(P'^2-PP'')-6(7X+4b)PP'.
\tag{30}
$$
R336 已证明
$$H^2x(V)P^2=xT,$$
其中 $T$ monic degree $2s$。微分并保留 $V^*dz=Hdz$，给
$$
\boxed{
M=PT+3X(PT'-2P'T),\qquad
y(V)=H^{-3}yM/P^3.
}
\tag{31}
$$
$M$ monic degree $3s$；其最高次中导数两项的贡献相消。

原 sigma 的 norm 二式有负号
$\sigma(2z)=-2y\sigma(z)^4$。
把它与真实 $\sigma(\bar\pi z)=\bar\pi\sigma(z)^p f_{\bar\pi}(z)$
按两种次序复合，得到特征零恒等式
$$
C(\bar\pi z)=2^{p-1}C(z)^p
\frac{f_{\bar\pi}(2z)}{f_{\bar\pi}(z)}.
\tag{32}
$$
约化后，(31) 把该实际比值准确写为
$$
\boxed{R:=\frac{f_V(2z)}{f_V(z)}
=\frac{M(X)}{(X+b)^{3s}}.}
\tag{33}
$$
$R$ 在 $O$ 正则且 $R(O)=1$。在所需的 $z^{p-1}$ jet 内，
所有原系数整；$C(z)^p\equiv-1\pmod{(p,z^p)}$。
由 (32)、$\bar\pi^{p-1}\equiv1$，因此
$$[z^{p-1}]R=-C_{p-1}.\tag{34}$$

另一方面 (27) 的 $p-1$ 权在单位上是质量模 $p$，给
$$
\boxed{\eta_p\equiv H-C_{p-1}\pmod{\mathfrak p}.}
\tag{35}
$$
这里周期因子没有被漏掉：原正式同构的 $p$-series 比较给
$H\Omega_p^{p-1}=1\pmod p$。再用 $(p-1)!=-1$，(27) 左端的
质量为 $-1+\eta_p/H$，右端为 $-C_{p-1}/H$，即 (35)。

对 (33) 乘原微分，得到真实有理式
$$
R\,dz=\frac{M(x^3)}{2y^p}\,dx.
\tag{36}
$$
$M(x^3)$ 次数 $9s<2p-1$，所以 Cartier 仅提取一次
$x^{p-1}=x^{6s}$：
$$
\mathcal C(R\,dz)=([X^{2s}]M)^{1/p}\,dz.
\tag{37}
$$
为比较 (34) 与 (37)，必须保留一个真实局部坐标项。
用 R336 的 $u=x^{-1/2}$、$v=-y/x^{3/2}$，有 $dz=du/v$。
若 $F$ 在 $O$ 正则，且其 $z$-jet 到 $p-1$ 阶整，则
$$
\boxed{[u^{p-1}](F/v)=HF(O)+[z^{p-1}]F.}
\tag{38}
$$
证明中 $j=0$ 的贡献是 $[u^{p-1}]v^{-1}=H$。
对 $1\le j\le p-2$，$z^jdz=d(z^{j+1})/(j+1)$ 的该系数为零；
所需 primitive 到 $u^p$ 阶整，因为 $z$ 的首个可能非整项
在 $u^p$，乘上其余正阶因子后已超出该范围。
最后 $z^{p-1}dz$ 的首项给一。这证明 (38)，也说明不能把该
比较当成特征 $p$ 中存在一个完整的 $z$ 坐标而删去 $H$。

将 (38) 用于 $R$，再用 (34)–(37)，得新的实际中间行
$$
\boxed{
[X^{2s}]M=H-C_{p-1}=(4b)^s
=\frac{b^{3s}}{HP(0)}\quad\text{于 }\mathbf F_p.
}
\tag{39}
$$
最后一个等号使用 R343 完整三挠除法递推已经证明的
$HP(0)=(b/2)^{2s}$。此前底部候选与中间系数之间的比较，在
这里由同一原 trace、周期及 Cartier 行全部付清。

## 7. 同一 sigma 的一个新的立方对角行

为避免与三次截面 $A=\sigma^3$ 混淆，这里记 $A_0=\sigma/u$。
准确有
$$C=-vA_0^3,\qquad C\,dz=-A_0^3du.$$
把 (38) 用于 $C$ 并用 $C(O)=-1$，(35) 给
$$
\boxed{[u^{p-1}]A_0^3=H-C_{p-1}=(4b)^s\ne0.}
\tag{40}
$$
R336 原 AS 支的第一修正在 $u^{5p}$。因此至所需 $u^{p-1}$，
可以使用它已经证明的准确对数：令 $t=-bu^6$，则
$$
\log A_0=\sum_{n=1}^{s}
\frac{(1/3)_n}{(5/6)_n}\frac{t^n}{6n}
\pmod{t^{s+1}}.
$$
这段的所有分母均为单位。于是 (40) 也等价于完全有限的同余
$$
\boxed{
[t^s]\exp\left(\frac12\sum_{n=1}^{s}
\frac{(1/3)_n}{(5/6)_n}\frac{t^n}{n}\right)=(-4)^s\pmod p.
}
\tag{41}
$$
这里确实给出了同一原 sigma 的一个全普通素数单位行。
它是 $u$ 坐标中的立方对角，而 R343 的两个目标是原 $z$ 坐标的
$\alpha_1$ 和准确 Wronskian 二次型。R336 的完整椭圆对数因子
$h$ 仍连接这两种观察，(40)–(41) 不允许直接删掉这个因子，
也不证明两个指定行不能同时为零。

## 8. 精确证书与后续接口

[精确脚本](../scripts/check-jzero-degree-three-exact-core-phase-and-middle-coefficient.py)
及 [JSON](../scripts/check-jzero-degree-three-exact-core-phase-and-middle-coefficient.json)
有 41 项精确检查，核定两组原对称 lift、完整交换子、全部六个
CM 剩余类的交织及 primary 相位、固定参考的三挠表，并在 R336
已有的同一个 $p=13,b=17$ 真实纤维上核定 (35)、(39)、(40)。
该有限纤维仅核规范；全部素数的证明在 §§2–7，没有新增素数扫描。

本结果把 R341 的所有候选损失单位素数排除，并给原核多项式
一个与真实全 core 相连的中间约束。R341 的混合联合身份因此可
在全部普通素数上使用单位的 $C$ 环带质量。剩余工作仍是把这些
已付的联合域或 (39) 的真实约束用于原 $S$ 的中央观察；不能把
辅助测度质量单位、有限群表示非零，或新立方对角非零替代该步骤。

所用输入均为仓库中完整证明的原接口：

- [R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)、
  [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)：
  原 sigma 整性、真实 division 迹、原周期和 sigma 的绝对 core。
- [R341](R341-original-active-triple-joints-degree-three-core-and-overlap-source.md)：
  三次截面的完整有界测度与原混合联合身份。
- [R336](R336-ordinary-original-zeta-as-verschiebung-and-two-full-negative-rows.md)：
  $D^p=HD$、真实 AS 支及 Verschiebung 核的全部规范。
- [R343](R343-original-three-torsion-phase-and-two-complete-faber-observers.md)：
  标准三挠除法递推给出的完整 $HP(0)$ 相位，以及两条目标 Faber 行。
