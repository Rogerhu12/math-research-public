# R626 — 原 V 核的小闭包、两中央共同深域与完整有限边界

日期：2026-11-15。**状态：已证明。**

本篇处理 R621 已存在的 $V$ 深补域。
先支付 whole $\mathcal S_{2104}$ 的全部中心和绝对平方，
再在整个原联合上将它的十六项 lift 准确转回原 $K_0$ 的
degree8 核。结果没有引入一个大辅助池：
原 $R/V$ 联合只有 R539 的两个真实态；
R617 的第一矩在 $V$ 上实际为 scalar，第二矩只分成两个
明确的旧 $\mathcal S_8$ 截面。

由此，原 $Y,W$ 同时深的整个域具有 scalar 返回，并逐个保持
原 $C,F,G$ 和同一个 $q$。
R621 的三个补偿也得到完整的 $H/V$ 核返回与两个实际 word 域。
这些物理映射不交换；全部单位补支及第二态都保留，
没有将补域或新极点行赋中央零。

## 1. 原轴、现有射线与整个 theta 格

沿用 R617、R621 的规范
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad\kappa=p\lambda^2,
$$
以及
$$
R=(1+3\omega)c+d,\quad K_0=c+(2+3\omega)d,\quad
a=-3\omega/8,
$$
$$
V=a_ZZ+a_QQ+2\delta r+b_KK_0,\quad
a_Z=(-2+\omega)/2,\quad a_Q=(4+3\omega)/2,\quad
b_K=-(1+6\omega)/8,
$$
$$
Y=V+aR,\qquad W=V+(a+2)R .
\tag{1}
$$
原完整六变量来源仍为
$\mu_0=\nu_{B_C}\otimes\nu^\flat$。
在 $(C,Z,Q,r,R,K_0)$ 中，实际 Hermitian 极化对角为
$(1,6,2,1,8,8)$。这不是把 $C$ 的全局 theta 格认作 degree1：
其实际 odd3 覆盖始终按原 $v=\delta C$ 保持。$V$ 不含 $C,R$。

整行 $8V$ 的非零输入系数为
$$
\boxed{
4(-2+\omega),\quad4(4+3\omega),\quad16\delta,\quad-(1+6\omega)
}
\tag{2}
$$
分别对应 $(Z,Q,r,K_0)$。
故完整第一轴属于标准 even 空间
$$
N=6\cdot112+2\cdot208+768+8\cdot31
=2104=8\cdot263 .
\tag{3}
$$
$Z,Q,K_0$ 的线丛均为标准 even；
唯一 odd sigma 输入 $r$ 在 (2) 中有偶乘子，所以没有剩余半特征。
$V\perp R$；其余全部伴随在下面的完整可逆框架中保持。

现有 R515 射线已经给 $\pi_0\equiv1\bmod263$。
结合原 dyadic 条件，完整中心准确为
$$
\boxed{
g_\pi=\pi_0/\bar\pi_0
\equiv1579+2104\omega\pmod{4208},\qquad
g_\pi^2\equiv1+2104\pmod{4208}.
}
\tag{4}
$$
没有增加新 CRT 条件。当前素数不等于 $263$。

## 2. entire degree2104 的 canonical quarter 算子

令 $m=N/8=263$。在标准 Schrödinger 基 $e_j$、$j\bmod N$ 上，
原完整 quarter lift 是
$$
\mathsf T^N_{(s+r\omega)/4}e_j
=i^{s(j+mr)}e_{j+2mr},\qquad r,s=0,1,2,3 .
\tag{5}
$$
定义
$$
\mathcal A_N=\frac14\sum_{t\in E[4]}\mathsf T_t^N
                  -\frac12\sum_{t\in E[2]}\mathsf T_t^N,\qquad
\mathcal B_Ne_j=(-1)^je_{1579j+1052}.
$$
对 (5) 全部十六项求和，准确得
$$
\boxed{\mathcal A_N=-\mathcal B_N,\qquad
       \mathcal A_N^2=\mathcal B_N^2=I.}
\tag{6}
$$
例如四次和只在 $j+mr\equiv0\bmod4$ 时保留；
再减去完整二挠项，置换乘子成为
$1-2m^2+4m\equiv1579\bmod N$，符号正是 (6)。
这没有把 canonical lift 当成没有中心的点置换。

(4) 在两个基本 Heisenberg 生成元上的完整作用为
$$
X\longmapsto-X^{1579},\qquad Z\longmapsto-Z^{1579}.
$$
$\mathcal B_N$ 实现这两个负中心号。
不可约性遂给 $K_N=c_p\mathcal B_N$。
下面只支付实际需要的绝对平方，不猜 $c_p$ 的号。

## 3. 一个真实两 sigma 锚支付绝对平方

取
$$
a_0=2,\qquad b_0=10\delta(3+\omega)=10+50\omega,\qquad
Na_0+Nb_0=4+2100=N .
$$
完整两轴来源
$$
F(z,t)=\sigma(a_0z-\bar b_0t)\sigma(b_0z+\bar a_0t)
       \in\mathcal S_N\otimes\mathcal S_N
\tag{7}
$$
交叉项为零，矩阵行列式 $N$ 是当前单位。
两个轴的全部二挠 lift 都为 $+1$：
对半周期 $\ell/2$，两条 sigma 的整周期分别为
$\ell$ 与 $5\delta(3+\omega)\ell$。
后者模二是非零 CM 单位倍，保原唯一 odd 半特征，
所以两个半特征号相乘为 $+1$。
第二轴同理，完整 Gaussian 因子由正交性相消。

在整个 $E[2]$ 固定子空间上，$\mathcal B_N=+I$；
这也由 (6) 对 $e_{2j}+e_{2j+N/2}$ 逐列直接验证。
原两个 sigma 同时深的标量为 $\beta^2=\lambda^2$，
而 (7) 的两轴同时深是同一真实域。
于是 $(K_N\otimes K_N)F=F$，即 $c_p^2=1$。
记 $\epsilon_p=-c_p$，得到
$$
\boxed{
K_{2104}=\epsilon_p\mathcal A_N,\qquad
\epsilon_p\in\{1,-1\},\qquad K_{2104}^2=I .
}
\tag{8}
$$
$\epsilon_p$ 是这个原规范下的实际号，不作可任意选择的参数，
也不将它认成 $\chi_{33}$ 或 $\chi_{65}$。

## 4. 保全部伴随的 quarter 运输

(2) 对任意 $t\in E[4]$ 的完整输入平移中，
$Z,Q$ 分别移动一个整周期，
$r$ 移动一个偶整周期；其 canonical 乘子全部为 $+1$。
因此整个原联合上严格有
$$
\boxed{
\mathsf T^{2104}_{8V,t}\mu_0
=\mathsf T^8_{K_0,-(1+6\omega)t}\mu_0 .
}
\tag{9}
$$
这里 (9) 是来源恒等式，保原全部输入和伴随。
证明可在任一完整正交化框架中逐因子写 canonical 指数：
其乘积的线性指数正是第一轴的指数，全部交叉项为零；
前三个因子的整周期恒等式付掉相应因子，
剩余恰为显示的 $K_0$ lift。
$N(1+6\omega)=31$，它在 $E[4]$ 上可逆，且置换 $E[2]$。
$N$ 被八整除使这些 canonical quarter lift 在更换周期代表后
无额外相位。故全十六项和与全二挠和均可真正重新编号：
$$
\boxed{\mathcal A_{2104,8V}\mu_0
       =\mathcal A_{8,K_0}\mu_0 .}
\tag{10}
$$

R539 已在原两个 sigma 上付清
$\mathcal A_{8,K_0}\mu_0=K_{8,R}\mu_0$，保其余四输入。
令 $\mu_1=K_{8,R}\mu_0$。由 $V\perp R$，两个 whole 核交换，
所以 (8)–(10) 给完整两态
$$
\boxed{
K_R\mu_i=\mu_{1-i},\qquad
K_V\mu_i=\epsilon_p\mu_{1-i},\qquad i=0,1 .
}
\tag{11}
$$
没有把单深第二态删除或赋成原曲线的算术行。

## 5. 原 Y/W 同时深的完整算术返回

对全部 $u,v\ge0$，(11) 给
$$
\boxed{
\mu_i|_{\{R\in p^u,V\in p^v\}}
=\lambda^{u+v}\epsilon_p^v
 (P_{R,\kappa^u}P_{V,\kappa^v})_*
 \mu_{i+u+v\ ({\rm mod}\ 2)} .
}
\tag{12}
$$
原 $\{Y,W\in p^n\}$ 恰为 $\{R,V\in p^n\}$，
因为 (1) 的行列式是单位 $2$。
故
$$
\boxed{
\mu_0|_{\{Y,W\in p^n\}}
=\epsilon_p^n\lambda^{2n}
 (P_{R,\kappa^n}P_{V,\kappa^n})_*\mu_0 .
}
\tag{13}
$$
右侧物理映射同时把原 $Y,W$ 乘 $\kappa^n$，
逐个保持整个正交补。

特别，$C,F,G$ 与整个 $Y/W$ 平面正交。
同一个原 $q_{+,N_0}$ 的所有 $D/E/G$、
$\kappa^{-N_0}$ 及完整 carry 条件均逐点保持。
因此对任意 carry 深度 $N_0\ge1$、共同深度 $n\ge0$，
完整 Mellin 身份是
$$
\boxed{
\begin{aligned}
\int_{\substack{Y,W\in p^n\\Y/\kappa^n\ {\rm unit}}}
 q_{+,N_0}\langle Y/\kappa^n\rangle^{d_pu}\,d\mu_0
 &=\epsilon_p^n\lambda^{2n}\beta^{N_0}J_S(u),\\
\int_{\substack{Y,W\in p^n\\W/\kappa^n\ {\rm unit}}}
 q_{+,N_0}\langle W/\kappa^n\rangle^{d_pu}\,d\mu_0
 &=6\delta\,\epsilon_p^n\lambda^{2n}\beta^{N_0}J_T(u).
\end{aligned}}
\tag{14}
$$
原两个中央零可合法传入 (14) 的整个域。
这里的观察是显示的归一观察，不能换成未经比较的 native 测试。
这也没有给任意 $W$ 附加测试下的条件 $S$ 中央赋零。

## 6. R617 两个条件矩的实际小闭包

对原 $R$ 作矩与 $V$ 的完整核交换，因为 $V\perp R$。
由 (10)，其作用只剩旧 $K_0$ 上的 $\mathcal A_8$。

第一矩中的 $g_8=x^2y_\wp\sigma^8$ 在整个 odd $\mathcal S_8$
内；R617 已证 $\mathcal A_8g_8=-g_8$。
因此第一矩的**整五变量**来源满足
$$
\boxed{\nu_1|_{\{V\in p\}}
       =\epsilon_p\beta(P_{V,\kappa})_*\nu_1 .}
\tag{15}
$$
这是一条真正 scalar 的首矩返回，不是只在一条边际上成立。

第二矩的两个显式因子为
$$
\Theta_2=\Theta(2z)=\sigma^8(x^4-8bx),\qquad
D_8=\sigma^8(x^4+4bx).
$$
完整二挠平均给
$$
\frac14\sum_{E[2]}\mathsf T_t(x\sigma^8)
=-\frac{\Theta_2}{12b},\qquad
\frac14\sum_{E[2]}\mathsf T_t(x^4\sigma^8)=\frac{\Theta_2}{3}.
\tag{16}
$$
例如用原 $e^3=-b$、
$c_t^8=(9e^4)^{-1}$ 的半周期公式逐项展开即可得 (16)。
在这个 entire even type-zero 二维块上，
$\mathcal A_8=I-2\operatorname{Avg}_{E[2]}$，遂有
$$
\mathcal A_8D_8=D_8,\qquad \mathcal A_8\Theta_2=-\Theta_2,
$$
$$
\boxed{
h_8=2(\omega-1)D_8-4\omega^2\Theta_2,\qquad
\mathcal A_8h_8=\sigma^8\{(-6-2\omega)x^4+(24+40\omega)bx\}.
}
\tag{17}
$$
这是整个来源式，不是只比较质量。

用 R617 的同一公共因子，定义
$$
\xi_D=\frac{\Omega^2}{42}\nu_{B_C}\otimes
 (\nu_{f_1}\otimes\nu_\Sigma-\nu_{f_3}\otimes\nu_\Theta)
 \otimes\nu_\sigma\otimes\nu_{D_8},
$$
并以 $\Theta_2$ 替换 $D_8$ 定义 $\xi_\Theta$。
则
$$
\nu_2=2(\omega-1)\xi_D-4\omega^2\xi_\Theta .
\tag{18}
$$

R621 的 $H=\delta(C-r)$、$K_b=\delta(C+r)$ 仍保原
$B_C\otimes\sigma$ 因子。$V$ 核只动 (17) 的 $K_0$ 因子，
因此整个 $H$ 格仍是原标准 $\mathcal S_6$，不发生 hidden gluing
增长。三个实际来源的完整 scalar 表是
$$
\boxed{
\begin{array}{c|cc}
\text{来源}&H\text{ 核}&V\text{ 核}\\ \hline
\nu_1&\beta&\epsilon_p\beta\\
\xi_\Theta&\beta&\epsilon_p\beta\\
\xi_D&\beta&\epsilon_p\lambda
\end{array}}
\tag{19}
$$
每条都保全部其余坐标及任何真实转置测试。
不得把 (18) 的两个不同 $V$ 符号合成一个任意 scalar。

## 7. 完整 H/V 物理框架及 q 的准确移动

记
$$
s=48/263,\qquad U=H+V,\qquad X=H+sV .
$$
准确有
$$
\operatorname{Gram}(H,V)=
\begin{pmatrix}6&-6\\-6&263/8\end{pmatrix},\quad
U\perp H,\quad X\perp V .
\tag{20}
$$
为明确保其余三个伴随，可取
$$
L_1=Z-\bar a_ZK_b,\quad
L_2=Q-\bar a_QK_b/3,\quad
L_3=K_0-4\bar b_KK_b/3 .
$$
它们都与 $H,V$ 正交。
$(V,X,L_1,L_2,L_3)$ 相对原 $(C,Z,Q,r,K_0)$ 的完整行列式为
$215/8$；其逆及全部 Gram 保存在证书。
$p\ge71$ 排除 $5,43$，旧射线排除 $263$，
所以此完整框架是当前处的整自同构。
三个 $L_i$ 之间的交叉项原样保留。

记 $\mathsf A=P_{H,\kappa}$、$\mathsf B=P_{V,\kappa}$。
在 $(H,V)$ 上，它们准确为
$$
\boxed{
\mathsf A=
\begin{pmatrix}\kappa&0\\1-\kappa&1\end{pmatrix},
\qquad
\mathsf B=
\begin{pmatrix}1&s(1-\kappa)\\0&\kappa\end{pmatrix}.
}
\tag{21}
$$
二者固定全部 $L_i$，但**不交换**：
$$
\mathsf A\mathsf B-\mathsf B\mathsf A
=(1-\kappa)^2
 \begin{pmatrix}-s&-s\\1&s\end{pmatrix}.
\tag{22}
$$

$\mathsf B$ 在原五坐标中为
$$
\begin{aligned}
C'&=C,\\
Z'&=Z+(\kappa-1)(-72-24\omega)V/263,\\
Q'&=Q+(\kappa-1)(8-24\omega)V/263,\\
r'&=r-(\kappa-1)16\delta V/263,\\
K_0'&=K_0+(\kappa-1)(40+48\omega)V/263 .
\end{aligned}
\tag{23}
$$
因此 $C,F,G,D,E$ 逐个保持，整个正支 $q_{+,n}$ 真正不变。
但 R613 的负支没有这个不变性：
$$
F_\tau'=F_\tau+(\kappa-1)48(1+\omega)V/263,\qquad
G_\tau'=G_\tau-(\kappa-1)(72+480\omega)V/263 .
\tag{24}
$$
原 $L$ 变成 $L-(\kappa-1)24\delta V/263$；
原 $J,A,H_{613}$ 同时增加
$(\kappa-1)24(1+\omega)V/263$。
所以 cap/ex 和负支仍须按 (24) 完整运输。

$\mathsf A$ 则保持 $(Z,Q,K_0)$，而
$$
C'=C+(\kappa-1)H/(2\delta),\quad
r'=r-(\kappa-1)H/(2\delta).
$$
原测试准确变为
$$
\boxed{
\begin{aligned}
D'&=D+(\kappa-1)\omega H/(2\delta),\\
E'&=E+(\kappa-1)(14+\omega)H/(2\delta),\\
G'&=G-(\kappa-1)(21-3\omega)H/(2\delta).
\end{aligned}}
\tag{25}
$$
$C/F$ 单位条件也同转置，不能只移动多项式的字母。

## 8. 原三个有限补偿的真实单层返回

本节先对 (19) 中任一完整来源 $\xi$ 写公式。
其 $H$ 标量记为 $b_H=\beta$，$V$ 标量记为 $b_V$。
对 $k=1$ 使用 $\xi=\nu_1$；
对 $k=2$ 分别使用 $\xi_D,\xi_\Theta$，最后按 (18) 合并。
所有来源前面的原常数已包含在 $\xi$ 中。

R621 的有限多项式及有理余项记为 $T_k,R_k$。
同一三个补偿为
$$
\begin{aligned}
B^{(0)}&=\int_{\{H\in p,V\ {\rm unit}\}}V^{-k}\,d\xi,\\
B^{(c)}&=-\int_{\{H\ {\rm unit},V\in p\}}T_k(U,H)\,d\xi,\\
B^{(r)}&=\int_{\{H,V\ {\rm unit}\}}R_k(U,H,V)\,d\xi .
\end{aligned}
\tag{26}
$$
现在两个深支都在同一个实际小闭包内完整返回：
$$
\boxed{
\begin{aligned}
B^{(0)}
 &=b_H\int_{U\ {\rm unit}}(U-\kappa H)^{-k}\,d\xi,\\
B^{(c)}
 &=-b_V\int_{X\ {\rm unit}}
 T_k\bigl(X+(1-s)\kappa V,\ X-s\kappa V\bigr)\,d\xi .
\end{aligned}}
\tag{27}
$$
这保全部其他变量。第一个单位等价来自
$V\circ\mathsf A=U-\kappa H$；
第二个来自 $H\circ\mathsf B=X-s\kappa V$。
没有把 $H$ 单位移成旧 $X$ 以外的任意边际。

显示前两阶可见必须保的常数项：
$$
\begin{aligned}
T_1\circ\mathsf B
 &=-5X^{-1}-(2870/263)\kappa V X^{-2}+p^2\mathcal O,\\
T_2\circ\mathsf B
 &=10X^{-2}+(6220/263)\kappa V X^{-3}+p^2\mathcal O ,
\end{aligned}
\tag{28}
$$
只在显示的 $X$ 单位域使用。
这些条件质量项并不因整个来源的总质量为零而消失。

若附原 $q$，(27) 第一式使用 $q\circ\mathsf A$，
第二式可用 $q\circ\mathsf B=q$，仅限真正的正支。
若附 cap、负支或其他 cut，全部使用 (23)–(25)。

## 9. 两个真实 word 域与完整单位补支

再分 (27) 的归一域，而不删除任何部分：
第一式按 $V$ 单位／深分，第二式按 $H$ 单位／深分。
因为
$$
U\circ\mathsf B=X+(1-s)\kappa V,\qquad
X\circ\mathsf A=sU+(1-s)\kappa H,
$$
且 $s$ 为单位，得到完整有限公式
$$
\boxed{
\begin{aligned}
B^{(0)}
={}&b_H\int_{\{U,V\ {\rm unit}\}}
        (V\circ\mathsf A)^{-k}\,d\xi\\
&+b_Hb_V\int_{X\ {\rm unit}}
        (V\circ\mathsf A\mathsf B)^{-k}\,d\xi,\\
B^{(c)}
={}&-b_V\int_{\{X,H\ {\rm unit}\}}
        (T_k\circ\mathsf B)\,d\xi\\
&-b_Vb_H\int_{U\ {\rm unit}}
        (T_k\circ\mathsf B\mathsf A)\,d\xi .
\end{aligned}}
\tag{29}
$$
再加 (26) 的 $B^{(r)}$，便是 R621 的整个 $\mathcal B_k$。
两条 word 项保不同的实际物理映射，不能因两个源标量相同
就相认。

在原点的真域分别是
$$
\boxed{
\begin{aligned}
\mathscr D_{HV}
 &=\{H\in p,\ V-(\kappa^{-1}-1)H\in p\},\\
\mathscr D_{VH}
 &=\{V\in p,\ H-s(\kappa^{-1}-1)V\in p\}.
\end{aligned}}
\tag{30}
$$
逆幂只在第一条已显示的深轴上使用。
它们分别是 $\mathsf A\mathsf B$、
$\mathsf B\mathsf A$ 的实际整像，源系数同为 $b_Hb_V$。
(29) 的两个单位双条件项正是归一后的真实补支，
不是另加的假想边界。若附 $q$，两个 word 项分别保
$q\circ\mathsf A\mathsf B$、
$q\circ\mathsf B\mathsf A$。

### 9.1 同一个原 carry 的精确 word 交域

以下固定原 carry 深度 $N_0\ge1$，仍用 R594 的同一个
$q_{+,N_0}$，不另选右逆。令
$$
\begin{aligned}
C_X&=C+(\kappa-1)X/(2\delta),\\
D_X&=D+(\kappa-1)\omega X/(2\delta),\\
E_X&=E+(\kappa-1)(14+\omega)X/(2\delta),\\
G_X&=G-(\kappa-1)(21-3\omega)X/(2\delta).
\end{aligned}
\tag{30a}
$$
这四条以及 $X$ 都与原 $R,V$ 正交，因而是真正的 $Y/W$
共同伴随。这里不对它们另赋 core。

因为正支 $q\circ\mathsf B=q$，
$q\circ\mathsf B\mathsf A=q\circ\mathsf A$。
完整两个 carry 指示的 $C,D$ 行之差准确为
$$
\begin{aligned}
C\circ\mathsf A\mathsf B-C\circ\mathsf A
 &=-\frac{s(1-\kappa)^2}{2\delta}V,\\
D\circ\mathsf A\mathsf B-D\circ\mathsf A
 &=-\frac{s\omega(1-\kappa)^2}{2\delta}V .
\end{aligned}
\tag{30b}
$$
第二个系数是单位。若 $\Gamma_{\mathsf A\mathsf B,N_0}$
与 $\Gamma_{\mathsf B\mathsf A,N_0}$ 表示
$\Gamma_{+,N_0}$ 在这两个真实映射下的原像，则
$$
\boxed{
\Gamma_{\mathsf A\mathsf B,N_0}
 \cap\Gamma_{\mathsf B\mathsf A,N_0}
 =\{V\in p^{N_0},\ D_X\in p^{N_0},\ C_X\ {\rm unit}\}.
}
\tag{30c}
$$
这是 carry **指示域**的相等，不是关于多项式非零支撑的断言。
证明是从两条 $D$ 同时深和 (30b) 得 $V\in p^{N_0}$；
随后 $D\circ\mathsf A\equiv D_X\bmod p^{N_0}$、
$C\circ\mathsf A\equiv C_X\bmod p$。逆向同理。
原 $F$ 单位条件没有丢失：在 $N_0\ge1$ 的 carry 内，
它恰等价于显示的 $C$ 单位条件。

(19) 因而在这个真实交域给
$$
\boxed{
\xi|_{\Gamma_{\mathsf A\mathsf B,N_0}\cap
             \Gamma_{\mathsf B\mathsf A,N_0}}
=b_V^{N_0}(P_{V,\kappa^{N_0}})_*
 \bigl(\xi|_{\{D_X\in p^{N_0},\,C_X\ {\rm unit}\}}\bigr).
}
\tag{30d}
$$
它保全部共同伴随和其他 cut 的实际转置。

令 $t_0=s(1-\kappa)/(2\delta)$。在 (30d) 的归一坐标中，
定义同一实际六次多项式
$$
\mathcal P_{N_0}(v)=
\widehat P_p\left(
 \frac{D_X}{\kappa^{N_0}}+\omega t_0v,\
 E_X+(14+\omega)t_0\kappa^{N_0}v,\
 G_X-(21-3\omega)t_0\kappa^{N_0}v\right).
\tag{30e}
$$
原 $\widehat P_p$ 的全部 $\lambda,\kappa$ 系数及整右逆原样保留；
$D_X/\kappa^{N_0}$ 只在显示的深域使用。
两个完整权分别严格为
$$
\begin{aligned}
(q\circ\mathsf B\mathsf A)\circ P_{V,\kappa^{N_0}}
 &=\frac{\mathbf1_{\{D_X\in p^{N_0},\,C_X\ {\rm unit}\}}{b\Omega^6}
   \mathcal P_{N_0}(V),\\
(q\circ\mathsf A\mathsf B)\circ P_{V,\kappa^{N_0}}
 &=\frac{\mathbf1_{\{D_X\in p^{N_0},\,C_X\ {\rm unit}\}}{b\Omega^6}
   \mathcal P_{N_0}(\kappa V).
\end{aligned}
\tag{30f}
$$
故权的差具有精确有限形式
$\sum_{j=1}^6(\kappa^j-1)p_jV^j$；
常数项消去，且每个 $\kappa^j-1$ 是单位。
这只是一条同权身份，未声称其余系数或积分非零。

尤其对任意完整有界实际测试 $f,g$，交域上的整个差为
$$
\begin{aligned}
&\int_{\Gamma_{\mathsf A\mathsf B,N_0}\cap
             \Gamma_{\mathsf B\mathsf A,N_0}}
 \bigl[(q\circ\mathsf A\mathsf B)(f\circ\mathsf A\mathsf B)
      -(q\circ\mathsf B\mathsf A)(g\circ\mathsf B\mathsf A)\bigr]\,d\xi\\
&=\frac{b_V^{N_0}}{b\Omega^6}
 \int_{\{D_X\in p^{N_0},\,C_X\ {\rm unit}\}}
 \bigl[\mathcal P_{N_0}(\kappa V)
           (f\circ\mathsf A\mathsf B\circ P_{V,\kappa^{N_0}})
       -\mathcal P_{N_0}(V)
           (g\circ\mathsf B\mathsf A\circ P_{V,\kappa^{N_0}})\bigr]\,d\xi .
\end{aligned}
\tag{30g}
$$
把 (29) 的真实单位指示、有理函数或原日志放进 $f,g$ 即可使用；
不能只保 (30f) 而把两条不同 native 测试相认。
两个 carry 各自离开 (30c) 的部分仍保留在 (29) 的完整分区内。

## 10. 原四单位域仍完整运输

R621 的原四单位域为
$$
\mathscr F_4=\{H,K_b,H+K_b,H-K_b\ {\rm unit}\}.
$$
在 $\mathsf B$ 下，
$$
H'=H+s(1-\kappa)V,\qquad
K_b'=K_b-s(1-\kappa)V .
\tag{31}
$$
因此 $C$ 的单位条件 $H+K_b$ 保持，
其余三条按 (31) 移动。
令 $X_b=K_b-sV$，则在本层真正的 $V$ 深返回后，
四条单位指示准确成为
$$
\boxed{\{X,X_b,X+X_b,X-X_b\ {\rm unit}\}.}
\tag{32}
$$
这里用了余下 $\kappa V$ 项属于 $p$，没有把 (32) 当成旧
$\mathscr F_4$。原 $K_b$ 深、$H+K_b$ 深、$H-K_b$ 深三个失败支
仍按同一公式逐个运输。
$\mathsf A$ 下则使用 (25) 和原 $H\mapsto\kappa H$；
不把其像错误地放回 $H$ 单位域。

## 11. 与原中央和 R621 有限式的完整联立

(29) 是 R621 中 $\mathcal B_1,\mathcal B_2$ 的实际新表达，
所以可原样代入该篇已付
$$
P_1=-36b_K\Omega^5I_1+\mathcal B_1,\qquad
P_2=-12\alpha\Omega^5I_1+\mathcal B_2,
$$
以及
$$
\alpha P_1-3b_KP_2=\alpha\mathcal B_1-3b_K\mathcal B_2 .
\tag{33}
$$
它没有增添新的负矩值或新的算术来源。
(19)、(25)、(29)、(32) 保同一有限来源、原 $q$ 和全部实际切集。

原两中央零合法进入的是 (14) 的整域，
以及 R617/R621 已显示的原中央与 native 环带组合。
它们并不自动使 (27) 的 $X$ 负矩、
(29) 的两个不同 word 项或 (26) 的有理余项为零。
尤其单层 $V$ 核在原 $\mu_0$ 上仍有第二态；
只有第一条件矩的 (15) 和第二条件矩的 (17)–(19)
支付了上述 scalar／有限分解。

本篇的新增实质是：原 $V$ 深补偿有了无格增长的实际小闭包，
原 $Y/W$ 同时深有了同 $q$ 的完整算术返回，
而两种相反次序的补偿及全部单位失败支都已成为明确真域。
最终还须比较 (29)、(33) 的实际值；主目标未由局部非零完成。

## 精确文件与依赖

- [check-r626-original-v-core-and-finite-native-boundary.js](../scripts/check-r626-original-v-core-and-finite-native-boundary.js)
- [check-r626-original-v-core-and-finite-native-boundary.json](../scripts/check-r626-original-v-core-and-finite-native-boundary.json)
- [R539：原整个 degree8 核和两态](R539-original-degree8-mixed-st-core-and-amplified-central-domain.md)
- [R515：已经固定的模 263 射线](R515-original-two-dimensional-st-source-and-same-source-sigma-carry.md)
- [R533：原 entire degree6 核](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)
- [R613：两个真实 carry 的交域](R613-original-reflected-carry-intersection-and-complete-two-state-return.md)
- [R617：原条件矩和 norm8 环带](R617-original-norm8-annulus-and-negative-five-pole.md)
- [R621：有限极点补偿与原四单位域](R621-original-six-degree-finite-pole-compensation.md)

BigInt 证书核定 2104 列上的全十六项 quarter lift、
二挠锚、完整中心、六变量输入系数、实际五变量框架、
原 $q$ 的所有不变和移动行、两个 word 的同 carry 交域与有限权差、两个旧 $\mathcal S_8$ 因子。
绝对平方、完整来源运输、无限深度和全部 word 域由正文证明。
