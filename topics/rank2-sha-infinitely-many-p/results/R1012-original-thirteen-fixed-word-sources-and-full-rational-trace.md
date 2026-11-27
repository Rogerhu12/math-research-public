# R1012 — 原十三字线的固定 degree10 来源、真实算术伴线与完整有理迹

日期：2026-11-27 UTC。**已证明：R1010 的十三项都可在原相位下实现为固定 degree10 扭线的真实截面；隔核权的十三个字系数全部非零。两条原秩二来源的十二个非平凡字，在完整几何主型投影后分别落到已指定的两条算术来源，而不是任取一个好位谱线。** 第二条的伴线准确是 $E_{571220}$ 的原 $(1,4,10)$ 类型。两核的质量匹配组合给同一个伴线减去两个明确的 old 向量，其差完整等于 $3\Delta_{125}/4$。

本篇同时给出不需要选择任何 torsion 根的 degree13 有理函数迹。它保留所有纤维，可直接消费 R1010 的六次、七次权以及后续的长窗平坦权。加权之后的 $P_{10}$、Miller 及两 exact 项仍用下文显示的完整形式；算术中央零只施在原两条 canonical 来源上。

## 1. 原绝对相位与十三字

沿 R987、R1004、R1010，记

$$
 E:y^2=x^3+1,\quad X=x^3,\quad
 \delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
 \pi=(7+\delta)/2,\quad \bar\pi=(7-\delta)/2.
 \tag{1}
$$

固定原 $u_\pi\in E[\pi]$、$u_{\bar\pi}\in E[\bar\pi]$ 及 degree130
Heisenberg 提升的中心根 $\zeta$。这里是 R987 的实际根，已含
$130/13=10$ 的中心幂次。置

$$
 \varepsilon(a)=(a/13),\qquad
 g=\sum_{a\bmod13}\varepsilon(a)\zeta^a,\qquad g^2=13.
 \tag{2}
$$

取先于 $p$ 固定的有限数域扩张 $L/K$，包含这些点、提升及其 Miller 数据。
本篇 $\mathcal S_{130}$ 指完整的130维 theta 截面空间；原几何
principal 22维空间由 $\Pi_0$ 另取。式(3)不宣称保持该22维子空间。
对 $f\in\mathcal S_{130}$ 定义完整加性投影

$$
 \mathcal P_{\pi,i}f
 =\frac1{13}\sum_{a=0}^{12}\zeta^{-ia}T_{a u_\pi}f,
 \qquad 0\le i\le12.
 \tag{3}
$$

它们在整个 $\mathcal S_{130}$ 上互相正交、和为恒等；
这里没有先作几何 $\Pi_0$。使用 R987 的原代数提升，

$$
 T_u f(z)
 =\sigma(\pi z)^{10}
       \frac{f(z+u)}{\sigma(\pi(z+u))^{10}},
 \qquad u\in E[\pi].
 \tag{4}
$$

若 $f=\sigma^{130}R_f$，

$$
 R_\pi=X^2+(2+6\delta)X+(40+24\delta)/13,\qquad
 \sigma(\pi z)=\pi\sigma(z)^{13}R_\pi(X),
 \tag{5}
$$

则 $\mathfrak f=R_f/R_\pi^{10}$ 的普通 deck 平移与 (4) 满足

$$
 \frac1{13}\sum_a\zeta^{-ia}\mathfrak f(P+a u_\pi)
 =\frac{\pi^{10}\mathcal P_{\pi,i}f(P)}
        {\sigma(\pi z)^{10}}.
 \tag{6}
$$

所以 (3) 的根与 R1010 的 Kummer 字可以准确配准。
具体选 $S\in E[\bar\pi]\setminus\{O\}$，使相应 Kummer 函数的
deck 角色在 $u_\pi$ 上恰为 $\zeta$。这样的 $S$ 唯一：
$S\mapsto(\tau\mapsto\tau\kappa/\kappa)$ 是
$E[\bar\pi]$ 到 $E[\pi]$ 字符群的同态；若字符平凡，则
$\kappa$ 下降，迫 $(S)-(O)$ principal，因而 $S=O$。
两群同为13阶，故该同态是同构。这也证明配准不需要猜一个十三次根。

令

$$
 \operatorname{div}h=13(S)-13(O),\quad
 h(z)=z^{-13}+\cdots,
 \qquad
 \operatorname{div}\kappa=[\pi]^*((S)-(O)),\quad
 \kappa(z)=\pi^{-1}z^{-1}+\cdots.
 \tag{7}
$$

同除子和同首项给整个身份
$\kappa^{13}=[\pi]^*h$。
因此

$$
 \mathfrak f=\sum_{i=0}^{12}f_i\kappa^i,\qquad
 f_i\in L(E_{\rm target}),\qquad
 \kappa^if_i=\frac{\pi^{10}\mathcal P_{\pi,i}f}
                         {\sigma(\pi z)^{10}}.
 \tag{8}
$$

全部选择先于 $p$ 固定；对共轭核采用 R987 已支付的 Weyl-dual
相位，不把它替成任意共轭平方根。

## 2. 每个字的实际 degree10 线束和完整十维返回

因为 $f$ 是 degree130 整 theta 截面，
$\mathfrak f$ 只在 $[\pi]^{-1}(O)$ 有极，每点至多10阶。
这个极帽在 (6) 的全部十三项下保持。除以 $\kappa^i$，得到

$$
 \boxed{f_i\in H^0\!\left(E,
       \mathcal O\bigl((10-i)(O)+i(S)\bigr)\right).}
 \tag{9}
$$

当 $i=11,12$ 时，$10-i$ 是负数，准确表示原 $O$ 处分别
至少一、二阶零，不能把它改成额外极帽。每个显示线束的 degree
都是10，故由椭圆曲线 Riemann–Roch，其完整截面空间恰为十维。
这给实际固定的扭线来源，不是一个随 $p$ 任择的有理函数空间。

还可把十维来源逐字返回标准全 $\mathcal S_{10}$。
令

$$
 R_i=4iS,\qquad 10R_i=iS,\qquad
 D_i=(10-i)(O)+i(S).
 \tag{10}
$$

选择唯一原 Miller 函数 $h_i$ 满足

$$
 \operatorname{div}h_i=D_i-10(R_i),
 \tag{11}
$$

并把 $O$ 处的首 Laurent 系数规范为一。
对 $i=0$ 和 $i=10$，除子为零，取 $h_i=1$。
其它情形的除子 degree 和群和均为零，故确为 principal，
该规范使函数及相位唯一。
若 $h_T$ 是首项为 $z^{-13}$、除子为 $13(T)-13(O)$
的原十三 Miller 函数，则另有完整检查

$$
 h_i^{13}=h_S^{\,i}/h_{R_i}^{\,10}
 \qquad(i\ne0).
 \tag{12}
$$

两边在 $O$ 的首项同为 $z^{13(10-i)}$，所以没有遗漏常数。

定义

$$
 Q_i(P)=h_i(P+R_i)f_i(P+R_i).
 \tag{13}
$$

则 $Q_i\in L(10O)$，其完整基可以固定为

$$
 1,x,x^2,x^3,x^4,x^5,\quad y,xy,x^2y,x^3y.
 \tag{14}
$$

于是 $\sigma^{10}Q_i$ 是一个真实标准 degree10 theta 来源。
不只读取其主型两列，也不把十三挠平移当作 $\mathcal S_{10}$
上的无相位自同态：相位及线束变化已经由 (11)–(13) 支付。

### 2.1 加权 Cartier 输入的全部运输

沿 R1010，令 $i=i_j\equiv-pj\pmod{13}$、
$e_j=(i_j+pj)/13$，并保同一个原 $Z,P_{10}$。
一个完整字微分为

$$
 \eta_{j,p}=g_j^p h^{e_j}Z^{-7}P_{10}f_i\,\omega_E.
 \tag{15}
$$

对 (13) 的同一固定平移，整个拉回准确为

$$
 \boxed{\tau_{R_i}^*\eta_{j,p}
 =(g_j\circ\tau_{R_i})^p
  (h\circ\tau_{R_i})^{e_j}
  \left(\frac{Z^{-7}P_{10}}{h_i}\circ\tau_{R_i}\right)
  Q_i\,\omega_E.}
 \tag{16}
$$

这里 $\tau_{R_i}^*\omega_E=\omega_E$。
所有 $P_{10}$、$Z$、Miller 和 $g_j$ 均在右边保持，
不能只留下 $Q_i$ 后套未平移的中央读者。
R1010(37) 的第一 Cartier 去增长指数，可以在 (15) 或 (16)
上作同一运算；固定平移与 Cartier 交换，所以两种次序相同。
这也给两个 exact 层的准确运输，未将它们商掉。

## 3. 隔核权的十三个字全部出现

置

$$
 v_\pi=\frac{R_\pi(X)}{(X+1)^2},\qquad
 W=v_\pi^\ell,\quad \ell=6\ \hbox{或 }7,
 \qquad W=\sum_{j=0}^{12}g_{\ell,j}\kappa^j.
 \tag{17}
$$

原 sigma 的完整恒等式 $\sigma(2z)=-2y\sigma(z)^4$ 给

$$
 \boxed{v_\pi
 =\frac{16\sigma(z)^3\sigma(\pi z)}
        {\pi\,\sigma(2z)^4}.}
 \tag{18}
$$

所以这个 degree 零权同时带原2、13两端；
它不是单纯的十三处算术角色扭曲。
它在 $O$ 值一，在其余十二个 $\pi$ 核点各有一阶零，
在三个非零二挠点各有四阶极。

将 (17) 作完整 deck Fourier 投影。目标上的极帽准确为

$$
 \boxed{g_{\ell,j}\in
 H^0\!\left(E,\mathcal O\bigl(
             4\ell\mathcal D_2+j(S)-j(O)\bigr)\right),}
 \quad \mathcal D_2=E[2]\setminus\{O\}.
 \tag{19}
$$

其中每一个字在三个 $\mathcal D_2$ 点都**恰有**
$4\ell$ 阶极：在任一原 $E[2\pi]$ 分支处，十三个平移和中
只有一个平移项碰到 $W$ 的二挠极；该项的 Fourier 系数非零，
所以最高主部没有另一个项可以抵消。除以 $\kappa^j$ 不改变
这些阶，因为两组十三纤维与 $[\pi]^{-1}(\mathcal D_2)$ 不交。

在原 $O$ 处，只有 $a=0$ 的 deck 项有非零常数；
其它十二项均至少从阶 $\ell$ 起。因此

$$
 \kappa(P)^j g_{\ell,j}(\pi P)
 =\frac1{13}+O(z^6).
 \tag{20}
$$

用 (7) 的真实首项和 $z_{\rm target}=\pi z$，得到

$$
 \boxed{g_{\ell,j}(z_{\rm target})
       =\frac1{13}z_{\rm target}^{\,j}
          +O(z_{\rm target}^{\,j+1})\qquad(0\le j\le12).}
 \tag{21}
$$

因而十三个字全部非零，且每个在 $O$ 的阶准确为 $j$。
其首系数在所有 $p\nmid13$ 的好约化仍为单位。
同一证明适用于任何已显示的 $W$ 满足
$W(O)=1$、$W|_{E[\pi]\setminus O}=0$；
若其二挠极帽为 $4m\mathcal D_2$，则 (19) 用 $m$ 代 $\ell$。
这涵盖按固定 $v_\pi$ 多项式给出的长窗平坦权。

## 4. 全十三质量及六阶是原两核数据的准确 Fourier 变换

设 $f$ 为原几何主型。沿 $u_\pi$ 的平方、非平方两个轨道，
把 R1004 的全部质量和六阶分别写为

$$
 m_\pm=m_c\pm m_e,\qquad
 b_\pm=b_c\pm b_e,\qquad
 m_0=f(0),\quad b_0=[z^6]f.
 \tag{22}
$$

这里 $m_e,b_e$ 是实际轨道值之半差，不另选一个二次根。
式 (3) 直接给

$$
 \boxed{\begin{aligned}
 m(\mathcal P_{\pi,0}f)&=(m_0+12m_c)/13,\\
 [z^6]\mathcal P_{\pi,0}f&=(b_0+12b_c)/13,\\
 m(\mathcal P_{\pi,i}f)&=(m_0-m_c+\varepsilon(i)g m_e)/13,\\
 [z^6]\mathcal P_{\pi,i}f
   &=(b_0-b_c+\varepsilon(i)g b_e)/13
       \qquad(i\ne0).
 \end{aligned}}
 \tag{23}
$$

证明只用 $\sum_{a\ne0}\zeta^{-ia}=-1$ 和
$\sum_a\varepsilon(a)\zeta^{-ia}=\varepsilon(i)g$；
因 $\varepsilon(-1)=1$，没有额外负号。
所有十三项以及原 $a=0$ 的质量、六阶均在 (23) 内。

例如 $\mathcal K,\mathcal C_{130}$ 的原 $m_0=b_0=0$。
R1007 的两个实际 $h_\pi$ 给

$$
 \boxed{
 m(\mathcal P_{\pi,0}\mathcal K)=\frac{15-9\delta}{14560},
 \qquad
 m(\mathcal P_{\pi,0}\mathcal C_{130})
       =\frac{15-113\delta}{14560}.}
 \tag{24}
$$

对其它十二字，R1004 两条实际质量的 $X$ 系数都非零。
若 $X=-1-3\delta+e$，则
$e^2=-108/\pi$，故 $(ge)^2=-108\bar\pi$。
这个数在 $\bar\pi$ 处赋值为一，因而 $ge\notin K$。
(23) 中的 $K$ 项与非零 $Kge$ 项不能相消。
所以 K/C 的十三个源字也全部非零。
若要在每个剩余域保这些非零值，须排除这些固定代数数的完整范数分子；
不将特征零非零偷换成无删集的逐素数单位性。

## 5. 两条真秩二来源的实际算术伴线

记原质量零且首 $z^6$ 系数为一的来源为
$\Phi_*,\Phi_{260}$。
R973 已确定其有限标签分别为 $(0,0,0)$、$(1,4,4)$。
令

$$
 \Psi=\Psi_{125},\qquad
 x_\pi=D_\pi\Psi,\quad x_{\bar\pi}=D_{\bar\pi}\Psi,
 \qquad
 \theta=\omega^2\pi=-1-2\delta,\quad
 t=\omega\bar\pi=-1+2\delta.
 \tag{25}
$$

两个 raw pull 的质量均为一。
R987 的两个实际 old 向量规范为

$$
 L_\pi=\frac{t x_{\bar\pi}-x_\pi}{t-1},
 \qquad
 L_{\bar\pi}
   =\frac{\theta x_\pi-x_{\bar\pi}}{\theta-1}.
 \tag{26}
$$

两者质量均一，且直接保全两个 raw pull 给

$$
 \boxed{L_{\bar\pi}-L_\pi=\frac34\Delta_{125}.}
 \tag{27}
$$

确实 $\theta t=13$、$\theta+t=-2$，故
$(\theta-1)(t-1)=16$，两列的差系数恰为 $12/16$。

再令 $\Psi_{571220}$ 是 R973/R976 完整 $(1,4,10)$ 共同块的
质量一来源。它对应的全局角色为
$E_{571220}:y^2=x^3+571220$ 的原角色。
这里依靠已付的全部2、3、5、双13参数认同它，不由两个好位特征值猜测；
本篇不把这条质量非零伴线指定为另一条秩二中央。

原两轨道质量是

$$
 m_\pi=\frac{(3-\delta)\sqrt\pi}{332640},
 \qquad
 m_{\bar\pi}=-\frac{(3+\delta)\sqrt{\bar\pi}}{332640},
 \tag{28}
$$

其中两个根及后一负号逐字采用 R987 的相位。
置

$$
 \nu_\pi=g m_\pi/13,\quad
 \nu_{\bar\pi}=g m_{\bar\pi}/13,\quad
 \rho_\pi=-\frac{11(1+\delta)}{40},\quad
 \rho_{\bar\pi}=-\frac{11(1-\delta)}{40}.
 \tag{29}
$$

那么对每个 $i\ne0$，有整个 degree130 来源身份

$$
 \boxed{\begin{aligned}
 \Pi_0\mathcal P_{\pi,i}\Phi_*
   &=\frac{\Phi_*}{12}
        +\varepsilon(i)\nu_\pi L_\pi,\\
 \Pi_0\mathcal P_{\pi,i}\Phi_{260}
   &=\frac{\Phi_{260}}{12}
        +\varepsilon(i)\rho_\pi\nu_\pi\Psi_{571220}.
 \end{aligned}}
 \tag{30}
$$

共轭支的两式完整把
$(\pi,\nu_\pi,\rho_\pi,L_\pi)$ 换成
$(\bar\pi,\nu_{\bar\pi},\rho_{\bar\pi},L_{\bar\pi})$。
两条 primitive 来源的 $i=0$ 字均为零，源于完整
$Q_\pi\Phi=Q_{\bar\pi}\Phi=0$，不是只源于质量为零。

### 5.1 全有限角色证明

在与 (3) 配准的 Schrödinger 模型中，
$\mathcal P_{\pi,i}$ 是第 $i$ 坐标投影。
几何 $\mu_6$ 在十三坐标上作用的像为平方群
$H\subset\mathbf F_{13}^{\times}$。
若 primitive 环面向量为 $\chi(v)$、$\chi(0)=0$，
其第 $i\ne0$ 坐标再作**整个**几何主型平均，准确给

$$
 \frac1{12}\{\chi(v)+\varepsilon(i)\varepsilon(v)\chi(v)\}.
 \tag{31}
$$

其余2、5因子的几何角色须与十三因子同时平均；
由于原整个向量主型不变，它们准确把每个平方轨道上的系数恢复为
$\chi(v)$，不会在 (31) 再添一个标量。

乘 $\varepsilon(v)$ 将实际十三环面标签 $b$ 改成 $b+6$。
对 $\Phi_*$，$b=0$ 的自然向量是 $\varepsilon(v)$，
伴向量是 $\mathbf1_{v\ne0}$。
R987 的绝对比例 $x_\pi=a\delta_0$、
$x_{\bar\pi}=b\mathbf1$、$a/b=t$，使这条伴线的质量一规范
正是 $L_\pi$。

对 $\Phi_{260}$，固定的2、5类型为 $(\epsilon,a)=(1,4)$，
故伴标签唯一为 $(1,4,10)$，恰是上述
$\Psi_{571220}$，且其质量非零、重数一。
最后，R993 的完整核身份
$m(T_u\Phi_{260})=\rho_\pi m(T_u\Phi_*)$
给 (23) 的每一个非零字质量都相差准确的 $\rho_\pi$。
质量一规范于是确定 (30) 的全部系数。
这付的是整个来源身份；没有只在原点拟合一条谱线。

### 5.2 原完整六阶数据的独立返回

R1004 的 $\Phi_*,\Phi_{260}$ 两条 $b_\pi$ 的二次 trace
同为 $-1/6$，故 (23) 的非符号项准确为
$(1+1/12)/13=1/12$，与 (30) 一致。
将该篇实际 $X$ 系数相除，还准确给

$$
 \boxed{[z^6]L_\pi=\frac{17992}{3}+8190\delta,\qquad
        [z^6]\Psi_{571220}=\frac{27820}{3}.}
 \tag{32}
$$

后一式可以逐个完整坐标核：

$$
 [X]m_\pi(\Phi_{260})=\frac{-5+3\delta}{3628800},
 \qquad
 [X]b_\pi(\Phi_{260})
      =\frac{1391(-5+3\delta)}{544320},
 \tag{33}
$$

其商为 $27820/3$。
前一式亦直接由 (26)、
$[z^6]\Psi_{125}=-26/3$、
$\pi^6=253+1260\delta$ 返回。
因此全有限类型证明的两条实际伴线还通过原同次第六阶独立检查，
不依赖重新运行或生成新的系数数据。

## 6. 质量匹配后的全字关系与非零中央输入

定义两个真正的 canonical 线性组合

$$
 F_\pi=\Phi_{260}-\rho_\pi\Phi_*,
 \qquad F_{\bar\pi}=\Phi_{260}-\rho_{\bar\pi}\Phi_*.
 \tag{34}
$$

R993 已付其分子分别被 $R_\pi,R_{\bar\pi}$ 恰整除一次。
(30) 进一步给所有非零字的完整返回

$$
 \boxed{
 \frac{\Pi_0\mathcal P_{\pi,i}F_\pi-F_\pi/12}
      {\varepsilon(i)\rho_\pi\nu_\pi}
       =\Psi_{571220}-L_\pi=:\mathcal R_\pi,}
 \tag{35}
$$

另一支同式给
$\mathcal R_{\bar\pi}=\Psi_{571220}-L_{\bar\pi}$。
原质量、首项及双支差准确为

$$
 \boxed{\begin{aligned}
 m(\mathcal R_\pi)&=m(\mathcal R_{\bar\pi})=0,\\
 [z^6]\mathcal R_\pi&=3276-8190\delta,\\
 [z^6]\mathcal R_{\bar\pi}&=3276+8190\delta,\\
 \mathcal R_\pi-\mathcal R_{\bar\pi}
       &=\frac34\Delta_{125}.
 \end{aligned}}
 \tag{36}
$$

故在原惰性共同 Tate 读者上，对每个原好 $p$，

$$
 \boxed{j_p(\mathcal R_\pi)-j_p(\mathcal R_{\bar\pi})
       =\frac34(p+1)\log_p(\pi/\bar\pi)\ne0.}
 \tag{37}
$$

这里使用 R978 已付的同一质量一 raw pull；
$\pi/\bar\pi$ 的两个十三赋值不同，所以它不是单位根。
在两 canonical 坏假设下，$j_p(F_\pi)=j_p(F_{\bar\pi})=0$，
(35) 遂把 (37) 写为两条**指定**、质量匹配的字读数之差。
它没有声称每一个 $\mathcal P_{\pi,i}F_\pi$ 仍是算术中央零。
保留 (16) 的完整权，才可将这些实际字读数继续送入 R1010
及长窗的两 exact 运算。

## 7. 不选 torsion 根的完整 degree13 有理迹

用 $\mathsf A_\pi(X)$ 专指原 x-map 多项式，避免与 R1007
的十维线性算子混名。其完整定义是

$$
 \mathsf A_\pi
 =13R_\pi^2-(42X+24)R_\pi R_\pi'
       -36X(X+1)(R_\pi R_\pi''-(R_\pi')^2),
 \tag{38}
$$

并有
$x(\pi P)=x\mathsf A_\pi/(\pi^2R_\pi^2)$。
这是从 (5) 二次对数微分直接得到的整个 degree4 首一多项式。
置

$$
 \mathsf B_\pi=(\mathsf A_\pi+3X\mathsf A_\pi')R_\pi
                        -6X\mathsf A_\pi R_\pi',\qquad
 U=X(\pi P),\qquad
 \mathcal F(X,U)=X\mathsf A_\pi^3-\pi^6U R_\pi^6.
 \tag{39}
$$

$\mathsf B_\pi$ 是 R1007 的完整首一 degree6 y-map。
$\mathcal F$ 是 $X$ 的首一 degree13 多项式；
因分子与分母互素，原有理映射
$X\mapsto X\mathsf A_\pi^3/(\pi^6R_\pi^6)$
的 degree 恰为13，故 $\mathcal F$ 是
$L(X)/L(U)$ 的完整最小多项式。
在好约化中它仍可分；这里保全部十三纤维。

对任意已显示的有理权 $W(X)$，若
$f=\sigma^{130}x^2P_f(X)$，则定义同一个未平均 trace

$$
 A_{W,p}(f)
 =\pi^{-10}\operatorname{Tr}_{[\pi]}
               \bigl(W^p R_f/R_\pi^{10}\bigr).
 \tag{40}
$$

由真实 x-map，逐项有

$$
 \boxed{
 A_{W,p}(f)
 =\pi^{-6}x(Q)^2
  \operatorname{Tr}_{L(X)/L(U)}
       \left(\frac{W(X)^pP_f(X)}
                   {\mathsf A_\pi(X)^2R_\pi(X)^6}\right).}
 \tag{41}
$$

十三个 $E$ 纤维点给十三个不同的 generic $X$；
若两个点有相同 $X$，它们相差 $\mu_6$，其 $\pi$ 像也相差
同一个单位，故对 generic $Q$ 只能是同一点。
所以 (41) 不漏二、三倍纤维，也不额外除13。

对首一 degree13 多项式，完整 Lagrange 插值给

$$
 \operatorname{Tr}(r)
 =[X^{12}]\operatorname{rem}_{\mathcal F}
                   (r\,\partial_X\mathcal F).
 \tag{42}
$$

这个式子先在可分纤维逐根证明，再作为函数域身份成立。
同时准确有

$$
 \partial_X\mathcal F
 =\frac{\mathsf A_\pi^2\mathsf B_\pi}{R_\pi}
       +6\frac{R_\pi'}{R_\pi}\mathcal F.
 \tag{43}
$$

将 (43) 代入 (41)–(42)，得到本篇的完整实际返回：

$$
 \boxed{
 A_{W,p}(f)
 =\pi^{-6}x(Q)^2[X^{12}]
   \operatorname{rem}_{\mathcal F(X,U)}
    \left(\frac{W(X)^pP_f(X)\mathsf B_\pi(X)}
                 {R_\pi(X)^7}\right).}
 \tag{44}
$$

余式始终在 $L(U)[X]/(\mathcal F)$ 的全部十三维上计算；
各分母取该整个商代数中的逆。
特别 $W=v_\pi^\ell$ 时，输入准确为

$$
 \frac{P_f\mathsf B_\pi R_\pi^{\ell p-7}}
                    {(X+1)^{2\ell p}}.
 \tag{45}
$$

原 $\mathsf A_\pi^2$ 的 apparent 分母已经在整条身份中消去，
没有删掉其零点的补项。
式 (42) 对 $r=1$ 返回 $[X^{12}]\partial_X\mathcal F=13$，
也独立核了未平均 trace 的规范。
R1010 的 $13\pi^{-10}$ Kummer 式与 (44) 是同一个 trace
的两种完整读取，不是两个不同的来源。


### 7.1 完整乘积之后的三个真实轨道

仍令 $f$ 为原几何 principal 来源，$W=W(X)$ 为本篇或 R1013 的
显示权。把全部因子留在上游，定义

$$
 \mathfrak F_i=\kappa^if_i
   =\frac{\pi^{10}\mathcal P_{\pi,i}f}{\sigma(\pi z)^{10}},
 \qquad
 G_j=\kappa^jg_j
   =\frac1{13}\sum_{a=0}^{12}\zeta^{-ja}W(P+a u_\pi).
 \tag{46}
$$

在特征 $p\ne13$ 中，完整 deck 求和给

$$
 [\pi]^*A_{W,p}(f)
   =13\pi^{-10}\sum_{j=0}^{12}G_j^p\mathfrak F_{-pj},
 \tag{47}
$$

其中下标在 $\mathbf F_{13}$ 中解释。证明是 $W^p$ 的第 $j$
字具有 deck 角色 $pj$，与 $\mathfrak F_i$ 相乘后只有
$i+pj=0$ 的项在全13项 trace 中保留；保留项的系数准确为13。

对每个原 CM 单位 $\lambda\in\mu_6$，定义
$a_\lambda\in\mathbf F_{13}^{\times}$ 使
$[\lambda]u_\pi=a_\lambda u_\pi$。其像是平方群
$H\subset\mathbf F_{13}^{\times}$，而 $2$ 是非平方。
令 $\mathscr R_\lambda=[\lambda]^*$。由 $W$ 与 $f$ 的 principal
性质，逐项换 deck 标签得

$$
 \mathscr R_\lambda G_j=G_{a_\lambda j},\qquad
 \mathscr R_\lambda\mathfrak F_i
     =\lambda^{-10}\mathfrak F_{a_\lambda i},\qquad
 \Pi_{-10}=\frac16\sum_{\lambda\in\mu_6}
                         \lambda^{10}\mathscr R_\lambda.
 \tag{48}
$$

因此 (47) 的完整和准确收缩为

$$
 \boxed{\sum_{j=0}^{12}G_j^p\mathfrak F_{-pj}
 =G_0^p\mathfrak F_0
   +6\Pi_{-10}\bigl(G_1^p\mathfrak F_{-p}\bigr)
   +6\Pi_{-10}\bigl(G_2^p\mathfrak F_{-2p}\bigr).}
 \tag{49}
$$

这三个轨道仍保完整 $W$、Frobenius 的 $-p$ 标签、全部字相位和
原 $P_{10},Z$ 的随后读取。对两条 primitive 来源，
$\mathfrak F_0=0$；对 $\mathcal K,\mathcal C_{130}$，零字仍是
R1007 已付的实际 whole trace，不能删除。

投影在整个 $G_j^p\mathfrak F_{-pj}$ 之后进行。(49)不许可把
$\mathcal P_i f$ 预先换成 $\Pi_0\mathcal P_i f$；乘法权一般
不与这个几何投影交换。因此它给 R1013 真正可用的三个保权代表，
没有给加权字线添任何未证明的 canonical 零。

## 8. 依赖与实际继续使用范围

- [R973](R973-original-degree130-arithmetic-spectrum-and-e260-source.md)、
  [R976](R976-original-cross-complete-22-and-66-spectrum.md)：全部有限类型、
  $(1,4,10)$ 的实际算术身份和质量一规范。
- [R987](R987-original-thirteen-two-orbits-and-normalized-central-difference.md)、
  [R993](R993-original-thirteen-boundary-values-and-common-frame.md)：
  原 Heisenberg 根、两核质量、$\rho_\pi$ 及完整一次消核。
- [R1004](R1004-original-thirteen-full-sixth-kernel-jets.md)、
  [R1007](R1007-original-thirteen-equivariant-cartier-model-and-kernel-readout.md)：
  同次全22质量/六阶及原 x、y 映射和全部适配读数。
- [R1010](R1010-original-thirteen-weighted-trace-and-two-exact-compression.md)：
  同一隔核权、第一 Cartier 十三项返回及原两 exact。

本篇使用的实际数据仍来自 run 45916324833 /
job 140236318135 / source 56f5c405d885932a9d8b213a5cdb431376fa2ea3，
没有重算原 CM、扫描素数或写生成矩阵文件。
固定字线已由 (9)–(16) 付全十维，真实算术伴线已由 (30)–(36)
付全来源，长窗可直接把自己的显示 $W$ 代入 (44)。
两 canonical 坏条件如何同这些完整加权字、两个 exact 和原低卷积联立，
仍须在原同一点继续处理；(37) 是可消费的非零输入，不代替该联立步骤。
