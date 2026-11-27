# R1021 — 两条原 δ-new 秩二来源的完整低层函数、三挠点相位与全字关系

日期：2026-11-27 UTC。**已证明。** 本篇把 R981 的
$E_{54925}$、$E_{8125}$ 两条真实秩至少二来源，分别还原为
$S_{10}$ 中的两个明确中间函数，并给出完整 degree30 多项式、
原三挠点提升、与十三处的全部24个非零字及真实乘法关系。
原第四阶方向的全部六个 degree30 分量一并保留；其中三个
$\delta$-new 补线实际有非零质量，不被当作新的中央零。

本篇的新算术必要行只有 R981 原两条 canonical 中央。
所有微分、平移和有限投影都先作为完整来源身份处理。
R1022 的同一特征零39纤维 trace 与 R1020 的唯一 primitive 类
可直接消费这些身份，但本篇不将某个字、协变导数或乘积免费赋零。

## 1. 四个实际中间方向及原二处投影

仍固定
$$
E:y^2=x^3+1,\quad X=x^3,\quad
D=\frac d{dz},\quad Dx=2y,\quad Dy=3x^2,\quad
\delta^2=-3,\quad \omega=(-1+\delta)/2.
\tag{1}
$$
写 $S_N=H^0(E,\mathcal O(NO))$ 的原 theta 实现
$\sigma^N L(NO)$，并定义
$$
\nabla_N=D-N\frac{\sigma'}{\sigma}.
$$
以下所有函数使用同一原 $\sigma$，不是另选线束平移。

在 $S_{10}$ 中置
$$
\begin{aligned}
q&=\sigma^{10}(X+1),&q_0&=\sigma^{10}(5X-4),\\
u_A&=\sigma^{10}y(X+4),&
u_C&=\sigma^{10}y(X-2),&
u_B&=\sigma^{10}xy,\\
\Psi&=\sigma^{10}x^2(X-8),&
\Psi_{00}&=\sigma^{10}x^2(X+10).
\end{aligned}
\tag{2}
$$
最后两条分别是 R978 的 $\Psi_{125}$、$\Psi_{12500}$；
$q$ 正是 R1015 的完整第二个标准来源。

### 1.1 不靠好位特征确定原 dyadic 线

对三个非零二挠点 $e^3=-1$，仍用 R985 的 canonical lift
$$
T_u^{(N)}f(z)=e^{-N\eta(u)(z+u/2)}f(z+u),
\qquad \mathscr S_N=\sum_{u\in E[2]\setminus O}T_u^{(N)}.
$$
原 cosigma identity 的准确平方常数是
$$
e^{-2\eta(u)(z+u/2)}\sigma(z+u)^2
=c_e\sigma(z)^2(x-e),\qquad c_e=-\frac1{\sqrt3\,e}.
\tag{3}
$$
说明其符号：再次平移 $u$ 给 $c_e^2(3e^2)=1$；
在实半周期 $e=-1$ 处左端原点值为正，固定该根，
其余两根由原 CM 旋转取得。这里的 $\sqrt3$ 与原二处
有限矩阵相同，未逐行另选符号。

把 $x(P+u)=e+3e^2/(x-e)$ 代入 (3)，再对 $e^3=-1$ 求和，
逐项得到
$$
\mathscr S_{10}\{\sigma^{10}(X+c)\}
=\frac{\sigma^{10}}{3\sqrt3}
\{(10c-1)X+c+8\},
\tag{4}
$$
以及
$$
\mathscr S_6\{\sigma^6(X+c)\}
=\frac{\sigma^6}{\sqrt3}\{(c-1)X+c+8\},
\qquad
\mathscr S_6(\sigma^6x)=\sqrt3\,\sigma^6x.
\tag{5}
$$
另一方面，$\sigma(2z)=-2y\sigma^4$，且三个非零二挠点都满足
$T_u^{(4)}\sigma(2z)=-\sigma(2z)$。
所以把 (5) 乘上这个原 degree4 函数时，
$\mathscr S_{10}$ 的符号准确反转。

由 (4)–(5)，实际本征如下：
$$
\begin{array}{c|ccccc}
f&q&q_0&u_A&u_C&u_B\\ \hline
\mathscr S_{10}\text{ 本征}&+\sqrt3&-\sqrt3&-\sqrt3&+\sqrt3&-\sqrt3\\
\epsilon&1&0&0&1&0\\
a&4&2&5&1&1 .
\end{array}
\tag{6}
$$
第二行以 R1015 已定的 $q$ 的 $\epsilon=1$ 锚固定；
第三行不是从两处 CM 算子猜出：
在 $W_2\otimes W_5$ 上，完整几何 $\mu_6$ 特征、
(6) 的二处特征与奇偶性唯一决定 $g_5=-\omega$ 的六次角色。
故它确定原整个 $T_5$ 角色。

### 1.2 实际投影与两个 old 权

令
$$
\Pi_{2,0}=\frac{\sqrt3-\mathscr S_{10}}{2\sqrt3},
\qquad
\Pi_{2,1}=\frac{\sqrt3+\mathscr S_{10}}{2\sqrt3}.
$$
直接微分 (2) 给完整身份
$$
\boxed{
\nabla_{10}^3q=120u_A+216u_C,\qquad
\Pi_{2,0}\nabla_{10}^3q=120u_A,
}
\tag{7}
$$
$$
\boxed{
\nabla_{10}u_B=\frac{10q+q_0}{3},\qquad
\Pi_{2,1}\nabla_{10}u_B=\frac{10}{3}q,
}
\tag{8}
$$
$$
\boxed{
\nabla_{10}u_A=4\Psi+5\Psi_{00},\qquad
\nabla_{10}u_C=5\Psi+4\Psi_{00}.
}
\tag{9}
$$
例如 $D\{y(X+4)\}=9x^2(X+2)$；
$D^3(X+1)=48y(7X+1)$，给 (7)。

与 R1018 的
$$
\frac1{24}\nabla_{10}^4q=65\Psi+61\Psi_{00}
$$
合并，实际两旧权矩阵的行列式为
$$
\boxed{\det\begin{pmatrix}4&5\\65&61\end{pmatrix}=-81.}
\tag{10}
$$
若记左两实际函数为 $A=\nabla_{10}u_A$、
$B=\nabla_{10}^4q/24$，则整个来源恒等式是
$$
\Psi=(5B-61A)/81,\qquad
\Psi_{00}=(65A-4B)/81.
\tag{11}
$$
这没有声称连接保持某个中央零子空间。

## 2. 原三挠点提升的完整相位与 rational kernel

取 $v_3=(c,\delta)$，$c^3=-4$。原三同源公式给
$$
x(\delta z)=-\frac{X+4}{3x^2},\qquad
y(\delta z)=\frac{\delta y(X-8)}{9X},
\qquad \delta v_3=t_3=(0,-1).
\tag{12}
$$
$v_3$ 不在 $\ker\delta$；
这里不能把 ramified 的 $\ker\bar\delta=\ker\delta$ 当成其补方向。

固定原 theta-group 的相位，令
$$
C_3=-e^{-3\eta(v_3)v_3/2}\sigma(t_3).
$$
比较除子与原点值，得到准确 cosigma 式
$$
e^{-3\eta(v_3)(z+v_3/2)}\sigma(\delta z+t_3)
=C_3\,\sigma(z)^3(y+\delta).
\tag{13}
$$
负支由原 $\sigma$ 的奇性给出
$$
e^{3\eta(v_3)(z-v_3/2)}\sigma(\delta z-t_3)
=-C_3\,\sigma(z)^3(y-\delta).
\tag{14}
$$
由于下文取十次幂，两支的共同常数均是 $C_3^{10}$，
并无一个可另选的负根。其代数性也直接由 R985 的有限阶
canonical lift 与 rational Miller norm 证明；本篇使用 (13)
选定的准确根。

记 $P_\pm=[\delta]P\pm t_3$，则加法公式给
$$
\begin{aligned}
x_+&=\frac{2\delta x(y-\delta)}{(y+\delta)^2},&
y_+&=-\frac{y^3-9\delta y^2-9y+9\delta}{(y+\delta)^3},\\
x_-&=-\frac{2\delta x(y+\delta)}{(y-\delta)^2},&
y_-&=\frac{y^3+9\delta y^2-9y-9\delta}{(y-\delta)^3}.
\end{aligned}
\tag{15}
$$
定义同一个完整线性算子
$$
\boxed{
\mathcal D_{\mathrm o}
=-\frac{T_{v_3}^{(30)}D_\delta-T_{-v_3}^{(30)}D_\delta}
{8C_3^{10}}:S_{10}\longrightarrow S_{30}.
}
\tag{16}
$$
对 $f=\sigma^{10}R$，(13)–(15) 给其完全代数的式子
$$
\boxed{
\mathcal D_{\mathrm o}f
=-\frac{\sigma^{30}}8
\{(y+\delta)^{10}R(P_+)-(y-\delta)^{10}R(P_-)\}.
}
\tag{17}
$$
(17) 作用于整个 $L(10O)$。在 $y+\delta=0$ 或 $y-\delta=0$
处，显示的十次零恰支付 $R(P_\pm)$ 的全部可能极；
因此像是完整 $S_{30}$ 截面，不是局部形式或有极的任意乘法。

取原 $\ker\delta$ 生成元使与 $v_3$ 的中心为 $\omega$。
$D_\delta f$ 是 $\phi_0$，两个平移是其实际 $\pm1$ 坐标；
(16) 因而恰为 R981 的 $\phi_{\mathrm o}=(0,1,-1)$ 方向。
两个坐标在 deck 作用下有不同的特征 $\omega,\omega^2$，
故它们的差不可能使一个非零 $f$ 消失。
这同时证明 $\mathcal D_{\mathrm o}$ 注入，并付清其原有限三型
$(c,\eta)=(1,1)$。

## 3. 两条实际 degree30 多项式

把 (2) 代入完整式 (17)，相消全部分母，得到
$$
\boxed{
\mathcal D_{\mathrm o}u_A=F_A=\sigma^{30}P_A(X),
}
$$
$$
\boxed{
P_A=X^5-76X^4-1880X^3+1792X^2+896X-512,
}
\tag{18}
$$
以及
$$
\boxed{
\mathcal D_{\mathrm o}u_B=\frac{15}{2}Q_B,\qquad
Q_B=\sigma^{30}xP_B(X),
}
$$
$$
\boxed{
P_B=(X+4)\left(X^3-\frac{108}{5}X^2-\frac{96}{5}X-\frac{64}{5}\right).
}
\tag{19}
$$
两个原未归一的奇提升系数分别准确为
$-8C_3^{10}$、$-60C_3^{10}$；(19) 的 $15/2$ 不是待定比例。

一个较短的展开核查是：置
$$
F_\pm=y^3\mp9\delta y^2-9y\pm9\delta.
$$
对 $u_B$，(17) 的大括号化为
$$
-2\delta x(y^2+3)\{(y+\delta)^4F_+-(y-\delta)^4F_-\}.
$$
内括号准确等于
$2\delta(-5X^3+108X^2+96X+64)$，给 (19)。
对 $u_A$ 同样展开给 (18)；仅用 $y^2=X+1,\delta^2=-3$。

完整原点规范是
$$
m_0(F_A)=1,\quad [z^6]F_A=-78,\qquad
Q_B=z^4-\frac{676}{35}z^{10}+O(z^{16}).
\tag{20}
$$
这里采用 $\sigma=z+z^7/210+\cdots$、
$x=z^{-2}-z^4/7+\cdots$。两条来源的所有系数固定，
(18) 无分母，(19) 只需清分母5。

## 4. 全部有限类型与 R981 的真实 canonical 身份

(6)、(16) 给
$$
F_A:(\epsilon,a;c,\eta)=(0,5;1,1),\qquad
Q_B:(\epsilon,a;c,\eta)=(0,1;1,1).
\tag{21}
$$
前者为 principal 几何型，后者为 type4；
它们未被预先当成同一几何主型。

令 $\pi=(7+\delta)/2$，沿用 R1015 的自然十三极化及
$\chi_j(2)=\zeta_{12}^j$。
对每个实际 degree $N$，用原 canonical lift 定义
$$
\mathcal L_{N,b}(f)=
\sum_{i=1}^{12}\chi_{b-6}(i)\,
T_{iv_{13,N}}^{(13N)}D_\pi f.
\tag{22}
$$
$v_{13,N}$ 是相应原自然极化的对偶生成元。
为与原 $\delta$-old 嵌入完全相容，取
$[\delta]v_{13,30}=v_{13,10}$ 于 $E[\bar\pi]$。
原 even-degree lift 的 functoriality 给准确身份
$$
\mathcal L_{30,b}(D_\delta f)
=D_\delta\mathcal L_{10,b}(f).
\tag{23}
$$
它保中心、Weyl-dual 相位和实际生成元，不将两个 degree 的中心
参数直接混同。

定义两个完整 raw 来源
$$
\boxed{
f_A=\mathcal L_{30,0}(F_A),\qquad
f_B=\mathcal L_{30,4}(Q_B).
}
\tag{24}
$$
因为 (22) 的十二项属于不同的 deck 字，各项系数非零，
$F_A,Q_B$ 非零遂给 $f_A,f_B\ne0$。
其所有坏位标签分别是
$$
(0,5,0;1,1),\qquad(0,1,4;1,1).
$$
这正是 R981(8) 的全 $2\times3\times5\times13$ 标签，
包括原 $\chi_3(\delta)=+i$、odd 五线及两个十三分支；
不是只核两个好位特征。

R981 的先验算术识别和 R976 同一次完整66列的一维性，因此给
$$
\boxed{
f_A=\gamma_A\Phi_{54925,1},\qquad
f_B=\gamma_B\Phi_{8125,1},\qquad
\gamma_A=[z^6]f_A\ne0,\quad\gamma_B=[z^6]f_B\ne0.
}
\tag{25}
$$
$\gamma_A,\gamma_B$ 在这里是 (13)、(18)、(19)、(22) 所定义的
固定有限代数式的实际第六系数，不是可以更改的相位。
本篇随后一直使用完整 raw 来源，所以没有为某个 $p$ 除以
一个尚未证明为单位的 $\gamma$。
两条来源质量均为零，由 R981 已证的实际 canonical 线承担。

## 5. 全部24个字和一个准确的整函数乘子

令 $\alpha=\delta\pi$。
取 $u_3\in E[3]$ 满足 $[\pi]u_3=v_3$，
并保 (22) 的 $v_{13,30}$。
互素3、13部分在 degree390 上的原 Heisenberg 乘子没有额外符号：
其交叉费用是 $390/(3\cdot13)=10$，为偶整数。
由 (13)–(16)，两个完整来源精确为
$$
\boxed{
f_A=-\frac1{8C_3^{10}}
\sum_{\substack{s=\pm1\\1\le i\le12}}
s\chi_6(i)\,
T_{iv_{13,30}+su_3}^{(390)}D_\alpha u_A,
}
\tag{26}
$$
$$
\boxed{
f_B=-\frac1{60C_3^{10}}
\sum_{\substack{s=\pm1\\1\le i\le12}}
s\chi_{10}(i)\,
T_{iv_{13,30}+su_3}^{(390)}D_\alpha u_B.
}
\tag{27}
$$
这就是39字中全部24个单位字；其余15个字为零。
三处的减号、十三处的两个完整 profile 和全部 scalar 都在式中。

令 $\mathcal P_{s,i}$ 取该实际字，
$B_{s,i}=\alpha(iv_{13,30}+su_3)$ 为其标准目标平移点。
由于
$$
r_3=\frac{u_B}{u_A}=\frac{x}{X+4}
=-\frac1{3x(P)x(\delta P)},
\tag{28}
$$
同一个原 lift 内完整地有
$$
\boxed{
\mathcal P_{s,i}f_B(P)
=\frac2{15}\chi_4(i)\,
r_3(\alpha P+B_{s,i})\,\mathcal P_{s,i}f_A(P).
}
\tag{29}
$$
这是一条整来源身份；$r_3$ 的显示极由 $u_A$ 的零完整支付。
当 R1022 把同一个字移至标准 $S_{10}$ 来源时，(29) 就是
$$
Q_{s,i,B}(Q)=\frac2{15}\chi_4(i)r_3(Q)Q_{s,i,A}(Q).
\tag{30}
$$
所有外部 $G^p$、Miller $h^e/h_i$、$P_{10}$、$Z$ 与平移仍位于
完整乘积内。若改用 (25) 的第六系数规范，只再乘
$\gamma_A/\gamma_B$；无其它可选常数。

(29) 也给实际字质量比例
$$
m_{s,i}(f_B)=\frac2{15}\chi_4(i)r_3(B_{s,i})m_{s,i}(f_A).
\tag{31}
$$
这里的 $B_{s,i}$ 是 primitive39点。
$u_A,u_B$ 的零仅在二挠或三挠支撑上，因此这24个点处
(31) 的显示来源分母不为零。

必须区分 (28) 与 R1015 的 $r=1/(4xx(2P))$。
当前
$$
r_3^3=\frac{X}{(X+4)^3}
$$
不是在全部 primitive39点上可随意换成一个常数。


### 5.1 可分别承接真中央零的两个三处分支

只对三处拆和，保留完整十二个十三字，记
$$
A_s=\sum_{i=1}^{12}\chi_6(i)
T_{iv_{13,30}+su_3}^{(390)}D_\alpha u_A,\qquad
B_s=\sum_{i=1}^{12}\chi_{10}(i)
T_{iv_{13,30}+su_3}^{(390)}D_\alpha u_B.
$$
$u_A,u_B$ 都为奇函数，而 $\chi_6(-1)=\chi_{10}(-1)=1$。
原 canonical lift 的反演公式遂给整个函数身份
$$
A_+(-z)=-A_-(z),\qquad B_+(-z)=-B_-(z).
\tag{31a}
$$
因此
$$
\boxed{
\Pi_{\rm even}A_+=-4C_3^{10}f_A,\qquad
\Pi_{\rm even}B_+=-30C_3^{10}f_B.
}
\tag{31b}
$$
相反分支取相反符号。两个右端已经为完整主型，
所以这里的 even 部分也是它们的完整 principal 部分。

对目标惰性 $p$，$d=p+1$ 为六的倍数，原 Gaussian 也是偶函数。
(31a) 的 odd 余项故在所有实际 $[z^{dh}]$ 读取中严格为零，
不是仅首位模 $p$ 的消失。完整 Newton 中央遂满足
$$
\boxed{
j(A_+)=-4C_3^{10}j(f_A),\qquad
j(B_+)=-30C_3^{10}j(f_B).
}
\tag{31c}
$$
坏 canonical 条件因此确实允许选同一个 $+3$ 分支，
对两个完整十二字和分别使用中央零。
它们仍各只是原一条必要行的比例；不能进一步给十二个十三字
分别赋零。将该分支改写为标准 $S_{10}$ 来源时，
共同的三处位移、Miller、$P_{10}$ 与原点读取也仍须保全。


## 6. 第四阶的全部六项返回

为把实际补项显示完整，另置
$$
F_C=\sigma^{30}
(X^5+518X^4-1232X^3-5984X^2-2560X-512),
$$
$$
E_q=\sigma^{30}
(X^5-58X^4+2224X^3+2656X^2+2048X-512),
$$
$$
E_0=\sigma^{30}
(X^5-220X^4+280X^3-5120X^2-8320X-512).
\tag{32}
$$
它们均以质量一规范。
同 (17) 的完整展开给
$$
\mathcal D_{\mathrm o}u_C=-F_C/2,
$$
$$
(T_{v_3}^{(30)}D_\delta+T_{-v_3}^{(30)}D_\delta)q
=2C_3^{10}E_q,
$$
$$
(T_{v_3}^{(30)}D_\delta+T_{-v_3}^{(30)}D_\delta)q_0
=-8C_3^{10}E_0.
\tag{33}
$$
其实际有限类型为
$$
F_C:(1,1;1,1),\qquad
E_q:(1,4;1,0),\qquad E_0:(0,2;1,0).
$$
另外两条原 old 函数完整为
$$
D_\delta\Psi=\sigma^{30}
(X^5+236X^4+1888X^3+4096X^2+1280X+1024),
$$
$$
D_\delta\Psi_{00}=\sigma^{30}
(X^5-250X^4-2000X^3-3680X^2+1280X+1024).
\tag{34}
$$

对 (19) 的实际 $Q_B$，整个第四阶身份为
$$
\boxed{\begin{aligned}
\nabla_{30}^4Q_B=8\{&
11888D_\delta\Psi+11860D_\delta\Psi_{00}\\
&+16740E_q+7404E_0+16340F_A+7021F_C\}.
\end{aligned}}
\tag{35}
$$
可完全逐系数检查：其左端除以 $\sigma^{30}$ 是
$$
570024X^5-2913552X^4-10733184X^3
-9047808X^2-2027520X-36864.
$$
一般核查式为
$$
\begin{aligned}
D^4x^m={}&4m(2m+1)(m+1)(2m+3)x^{m+2}\\
&+8m\{m(2m+1)(m+1)+(m-1)(m-2)(2m-3)\}x^{m-1}\\
&+16m(m-1)(m-2)(m-3)x^{m-4},
\end{aligned}
\tag{36}
$$
逐代 $m=1,4,7,10,13$ 即得 (35)。
这里没有一次未登记的有限精度或数值计算。

### 6.1 全十三 profile 后的真实 old 费用

用 (22) 对 (35) 施 $\mathcal L_{30,0}$。
若将第 $i$ 字的完整 fourth gauge 写为 R1018(19) 的
degree390、target degree30 版本，则
$\chi_8(i)\chi_{10}(i)=\chi_6(i)$，给完全相同的左端。
原 $c_*=3\omega^2\nu_\pi$ 与 R1018(23) 准确给
$$
\mathcal L_{30,0}(D_\delta\Psi)=c_*^{-1}D_\delta\Phi_*,
$$
$$
\mathcal L_{30,0}(D_\delta\Psi_{00})
=\frac{\omega}{18480c_*}D_\delta\Psi_{27462500}.
\tag{37}
$$
所以 (35) 的整个 old 部分就是
$$
\boxed{
\frac8{c_*}D_\delta
\left(11888\Phi_*+\frac{11860\omega}{18480}\Psi_{27462500}\right).
}
\tag{38}
$$
该式可直接进入 R1022 的真正同窗身份
$h_{N,\delta\pi}(D_\delta g)-h_{N,\pi}(g)=O(z^{N+1})$；
其 Gaussian 质量费用在那里完整相消。
这不是只将两个 source 方向相认后声称它们的读者相同。

其余三个非 canonical 补项不能删除。
由 R981 的完整标签公式，$\mathcal L_{30,0}E_q$、
$\mathcal L_{30,0}E_0$、$\mathcal L_{30,0}F_C$
在 R976 的 $\delta$-new 谱中分别为
$(4,3),(0,5),(1,3)$；该篇实际全66列回执证明三条线质量非零。
特别第一个 $(4,3)$ 不能混作同好位特征的 $\delta$-old $\Phi_*$。
本篇无需用数据库的 rank 字段来排除把它们当作新 canonical 零。

## 7. 可直接消费的算术必要行与完整适用范围

对目标惰性素数，若 R981 两条实际 canonical 中央均坏，
则由 (25)，整个 raw 来源满足
$$
j_{f_A}=j_{f_B}=0.
\tag{39}
$$
这是本篇两条新增可用输入；它们仍是既有两条固定真曲线的中央，
不是24条独立字零。

将 (26)–(27) 代入 R1022 的同一个39纤维特征零平坦 trace，
再使用其完整 $P_{10}/Z$ 和全部 Gaussian／质量账本，
给两个实际 target 的全 $p^{H+1}$ 必要同余。
R1020 的算子
$$
\mathfrak M_H(\eta)=
D^{-1}\{(1-S_H\mathcal C)\mathcal C(\eta-\ell_O)\}
\quad\text{in }F/F^p
$$
可统一作用于这些整个 first-Cartier 身份。
其中所有原点留数、两支旧质量及曲率项仍按该篇原式返回。
不能把 (39) 改写成每个 $\mathfrak M_H$ 字都为零。

(7)–(11)、(29)、(35)、(38) 提供的是这些真实必要行之间可使用的
完整固定函数关系。尤其行列式 $-81$ 支付两个 old 方向的源端
独立性；将其变成中央强迫仍必须消费相应实际外权。
$\nabla$ 穿过 (13)、十三 Miller 或 $P_{10}$ 时的连接补偿，
由原比值逐次微分并保留，不能因一个 scalar 行列式非零而略去。

固定来源分母、canonical torsion lift 和原整数格只增加固定有限
坏集；raw 式 (26)–(27) 的使用不反演 $\gamma_A,\gamma_B$。
增长平坦权及深度 $H$ 的所有成本由 R1022 的真实全精度证明承担。
## 8. 两条真 canonical 之间的完整四阶 Lamé 算子

本节保留 (26)–(27) 的 raw 规范及全部24字。
它给一个明确的整个算子把 $f_B$ 送到 $8f_A$；
因此在两条原 canonical 坏条件下，确有这两个完整来源的中央零。
这里不将零分别分配给任何单字，也不宣称微分算子一般保持中央零。

### 8.1 固定源端的完整消项

将不含 $\sigma^{10}$ 的有理部分记为
$$
U_B=xy,\qquad U_A=y(X+4),\qquad X=x^3.
$$
原 $Dx=2y,Dy=3x^2$ 逐项给
$$
DU_B=5X+2,\qquad D^2U_B=30xU_B,
\qquad D^2(xU_B)=8y(7X+1).
\tag{40}
$$
所以准确有
$$
\boxed{
(D^2-54x)D^2U_B
=(D^4-1620x^2)U_B=60U_A.
}
\tag{41}
$$
式 (41) 的算子顺序固定为先 $D^2$，再 $D^2-54x$；
未把 $x$ 与导数交换。
以 $\nabla_{10}=D-10\sigma'/\sigma$ 作用于整个来源，
同式就是
$$
(\nabla_{10}^4-1620x^2)u_B=60u_A .
$$
所有中间有理部分在 $O$ 的极阶至多九，
故本次作用仍给实际整个 degree10 来源，没有隐含的极部截断。
尤其，原 $D^4U_B=600U_A+1080U_C$ 中的 $U_C$ 已被
$1620x^2U_B$ 准确消掉；
这里的乘法项本身仍是算子的一部分，未被当作额外中央零。

### 8.2 完整十三 profile、三处分支和绝对系数

置
$$
a_{s,i}=iv_{13,30}+su_3,\qquad
B_{s,i}=\alpha a_{s,i},\qquad
\mathcal I_{s,i}=T_{a_{s,i}}^{(390)}D_\alpha .
$$
在本节实际 word 来源的域上定义
$$
\mathscr D_{s,i}=\mathcal I_{s,i}\nabla_{10}\mathcal I_{s,i}^{-1},
\qquad x_{s,i}(z)=x(\alpha z+B_{s,i}).
$$
原 canonical lift 的显式式子是
$$
\boxed{
\mathscr D_{s,i}
=\alpha^{-1}D_z-10\zeta(\alpha z+B_{s,i})
+\frac{390}{\alpha}\eta(a_{s,i}).
}
\tag{42}
$$
这由
$\mathcal I_{s,i}f(z)=
e^{-390\eta(a_{s,i})(z+a_{s,i}/2)}
f(\alpha z+B_{s,i})$
直接微分得到，因而保留了原 $\alpha$ 缩放、指数相位和全部常数。
(42) 作用于 $\mathcal I_{s,i}(\sigma^{10}R)$ 时，
其结果准确是 $\mathcal I_{s,i}(\sigma^{10}DR)$；
代数性由原 canonical lift 与本节显示的有理部分承担，
没有更换一个自由连接。

令 $\mathcal P_{s,i}$ 为 (29) 的实际 word projector，
并按原顺序定义
$$
\boxed{
\mathscr O=
\sum_{\substack{s=\pm1\\1\le i\le12}}
\chi_8(i)
 \bigl(\mathscr D_{s,i}^4
       -54x_{s,i}\mathscr D_{s,i}^{\,2}\bigr)
 \mathcal P_{s,i}.
}
\tag{43}
$$
这里先取实际 word，再施其同一个规范算子；
不把 projector 越过非恒定乘子。
将 (41) 逐字代入 (27)，并用
$\chi_8\chi_{10}=\chi_6$，完整得到
$$
\boxed{\mathscr O f_B=8f_A.}
\tag{44}
$$
绝对常数为
$60\cdot(1/60)/(1/8)=8$；
两个三处符号 $s$ 原样保留，
没有添加 Weyl-dual、三处或十三处相位。
该证明不反演 $\gamma_A,\gamma_B$。

同样，对 §5.1 的单正三支、完整十二个十三字，
相应的算子准确把 $B_+$ 送到 $60A_+$。
这些始终是十二字的整个和。
特别，原两条坏条件现在可准确写为
$$
j(f_B)=0,\qquad j(\mathscr O f_B)=8j(f_A)=0.
\tag{45}
$$
第二个零来自已证明的整个像 (44)，
没有使用微分、乘法或单字零的免费传播。

### 8.3 原 P10 中对应的全部曲率

在共同 target 坐标，用 R887/R1024 的原
$$
L=D-10G,\qquad
e=10\mathcal H^p Z^{p+9},\qquad
LP_{10}=e .
$$
对任意完整有理 $f$，Leibniz 逐项给
$$
\begin{aligned}
L^2(P_{10}f)&=P_{10}D^2f+2eDf+(Le)f,\\
L^4(P_{10}f)&=P_{10}D^4f+4eD^3f
 +6(Le)D^2f+4(L^2e)Df+(L^3e)f .
\end{aligned}
\tag{46}
$$
取 $f=U_B$，使用 (40) 后，得到整个曲率身份
$$
\boxed{\begin{aligned}
&(L^4-54xL^2)(P_{10}U_B)-60P_{10}U_A\\
&\quad=(4L^2e+12xe)\,DU_B
 +(L^3e+126xLe+240ye)\,U_B .
\end{aligned}}
\tag{47}
$$
其右端没有 $P_{10}$。
更准确地，$e=10\mathcal H^pZ^p\cdot Z^9$ 的前因子被 $D$ 杀掉，
所以右边只涉及 $L^jZ^9$、$0\le j\le3$ 和显示的固定有理来源。
这并没有删除 $G$、$\mathcal H$ 或原 $Z$。

若先执行实际外部平移以保持同一个原 $P_{10}$，
则以 $f=U_B(P+R)$、$x=x(P+R)$、$y=y(P+R)$ 解释 (40)–(47)；
$L$ 中的 $G$ 仍是实际同点原模型。
例如正三支标准字在同 $O$ 表达中使用
$x(P+S)=-2x/(y+1)$。
不能以未平移的 $U_B$ 或 $x$ 替代它们。
其余 Miller、十三字符与 $Z^{-b-1}$ 都继续留在完整测试中。

对整个实际测试 $a$，令 $M=D+10G$。
Cartier 杀完整 exact 给准确伴随
$$
\mathcal C\!\left(
a(L^4-54xL^2)h\,\omega_E\right)
=
\mathcal C\!\left(
\{M^4a-54M^2(xa)\}h\,\omega_E\right).
\tag{48}
$$
平移版本同样保其真实 $x(P+R)$。
(48) 不删曲率 (47)，也不将新测试
$M^4a-54M^2(xa)$ 直接当成原测试。
把 (45) 放入 R1020/R1026 的同一读者时，
真正需要消费的是这些完整测试、(47) 的曲率、
全部质量／留数以及原 $\chi_8$ profile。
本节已付两真 canonical 的整个固定算子与完整返回，
尚未证明其伴随测试由原平坦权的相邻返回生成。


## 9. 原三字返回的共同权、degree130 Miller 与全部十三 profile

本节承接 R1028 §5–6 的共同 $W_\infty$ reader。
凡写到这个权，均保留该文已经支付的特征 $p$ 第一 primitive
低窗范围；原特征零 $V_\delta$ 与 $W_\infty^p$ 的全函数差
没有被改成零。这里的新内容是将两条实际正三处分支、
旧行和原十三字放在同一坐标中，付清 Miller、平移、
$\delta/\pi$ 缩放及完整四阶算子的归一。

### 9.1 固定三次根与实际平移

在第一步 $\delta$ 的 target 上记
$$
S=(0,1),\quad h=1-y,\quad \kappa^3=h,\qquad
\Phi_-=\kappa,\quad \Phi_+=x/\kappa,\quad
r_S=\Phi_+/\Phi_-=x/\kappa^2 .
\tag{49}
$$
$\kappa$ 始终取 R1022 的原
$-(y_{\rm up}+\delta)/(\delta x_{\rm up})$；
不另选一个三次根。
$\Phi_\pm$ 在原点都以 $z^{-1}$ 为首项，且
$$
\Phi_-^3=1-y,\qquad
\Phi_+^3=-(1+y),\qquad
\Phi_+\Phi_-=x .
$$
原 $S$ 的 $\zeta(S)=\eta(S)$ 和 addition identity 给
$$
D\log\Phi_+=\frac{y-1}{x}=:j_S,\quad
D\log\Phi_-=\frac{y+1}{x},\quad
\boxed{D\log r_S=-\frac2x.}
\tag{50}
$$

保留原正分支 $u_3\in E[3]$、$[\pi]u_3=v_3$。
由于 $[\delta]v_3=(0,-1)=-S$ 且 $\pi$ 在
$\ker\delta$ 上作用为 $-1$，所以
$$
[\delta]u_3=S,\qquad [\pi]S=-S.
\tag{51}
$$
在相位式中可直接取实际 lift $S=\delta u_3$；
其在 $E$ 上的点仍是 $(0,1)$。
定义固定常数
$$
C_S=e^{-\eta(S)S/2}\sigma(S).
$$
比较 logarithmic derivative 和原点首项，得到整个恒等式
$$
\boxed{
T_S^{(N)}(\sigma^N R)
=C_S^N\sigma^N\Phi_+^N R(P+S).
}
\tag{52}
$$
$C_S^3$ 的代数性由 degree3 canonical lift 给出，
故本式只需原固定有限扩域及有限坏分母；
$C_S$ 是上述复规范选定的准确根。
$T_S^{(130)}$ 本身在原 $E$ 上具有三次 monodromy，
这里在 (49) 的固定 cover 上使用它，不将它误称为
$S_{130}$ 的 theta-group 自同构。

### 9.2 两条正分支的真实 degree130 标准来源

置
$$
G_A=\mathcal L_{10,0}(u_A),\qquad
G_B=\mathcal L_{10,4}(u_B).
$$
R1021(23) 和互素3、13 cross fee $10$ 给
$$
\boxed{
A_+=T_{u_3}^{(390)}D_\delta G_A
     =D_\delta T_S^{(130)}G_A,\qquad
B_+=T_{u_3}^{(390)}D_\delta G_B
     =D_\delta T_S^{(130)}G_B.
}
\tag{53}
$$
这些都是完整十二字之和，没有重新标记某个好位本征线，
也没有给 $G_A,G_B$ 单独赋中央零。

以下暂写 $N=130$、$G=\sigma^N R_G$。
用 $\sigma(\delta z)=\delta\sigma^3x$，式 (52) 给
$$
\frac{R_{D_\delta T_SG}}{x^N}
=\delta^N C_S^N\Phi_+^N R_G(P+S).
$$
因为 $N\equiv1\pmod3$，
$\Phi_+^N=x^N\kappa^{-N}
=x^N h^{-44}\kappa^2$，所以这是原 mode2。
R1022 的 degree130 Miller 函数必须为
$$
h_{2,N}=\frac{x^2}{(1+y)^{44}},
\qquad x^Nh^{-44}h_{2,N}=1.
$$
于是实际标准化
$f_2(P)=Q_2(P+S)/h_{2,N}(P)$ 中，整个来源准确为
$$
\boxed{Q_2=\delta^{130}C_S^{130}G.}
\tag{54}
$$
这同时锁定了两条正分支全部十二字的同一个常数。
不能把此处的指数44换成最终 degree10 的指数4。

### 9.3 共同 $F_p$ 项及旧行多出的准确项

以下 $F_p=Z+\rho_p(x^2/y)^p$ 仅引用 R887 §7 的原函数。
R1028 的全三字式给
$$
B_0=-\frac{c_px}{3y},\qquad
B_1=\frac{c_px^2}{3y(1-y)},\qquad
g_{0,\infty}=\frac23+B_0^pF_p,\qquad
g_{2,\infty}=h^{2s-1}B_1^pF_p .
$$
正分支的整个第一返回是
$3\delta^{-N}g_{2,\infty}^p h^{4s}f_2$。
由于 $p=6s-1$，
$$
p(2s-1)+4s=\frac{p^2+2}{3}.
$$
将真正的 $h_{2,N}$ 代入，完整消去显示幂后得到
$$
\boxed{
\frac{h^{(p^2+2)/3}B_1^{p^2}}{h_{2,N}}
=\frac{c_p}{3}\,
 y^{-p^2}(1+y)^{(2p^2+N)/3}.
}
\tag{55}
$$
此式只用 $x^3=-(1-y)(1+y)$；
其出现的整数幂 $(2p^2-2)/3$ 为偶数，故没有待定符号。

定义同一个实际权
$$
\boxed{\mathcal K_p=-c_p(x/y)^{p^2}F_p^p.}
\tag{56}
$$
它是函数域中的 $p$ 次幂，因而 $D\mathcal K_p=0$。
将 (54)–(55) 代回，旧、新的完整共同模型返回分别是
$$
\boxed{\begin{aligned}
\bar A_{130,\delta}^{\,\infty}(D_\delta g)
 &=2R_g+\mathcal K_pR_g,\\
\bar A_{130,\delta}^{\,\infty}(A_+)
 &=-\mathcal K_p r_S^{p^2}
      R_{T_S^{(130)}G_A},\\
\bar A_{130,\delta}^{\,\infty}(B_+)
 &=-\mathcal K_p r_S^{p^2}
      R_{T_S^{(130)}G_B}.
\end{aligned}}
\tag{57}
$$
这里新行的负号来自
$3B_0^{p^2}=-c_p(x/y)^{p^2}$，
以及 $(2p^2+N)/3$ 为偶数。
式 (57) 的每个完整乘积都下降到实际 $\delta$ target；
固定 cover 上的单个 $r_S$ 或 $T_SG$ 不必分别下降。
特别不能把旧行的 $2R_g$ 删除。

$\mathcal K_p$ 与 $r_S^{p^2}$ 被 $D$ 杀掉，
因此它们在本节同点的有限微分算子中确可保留为水平因子。
但这不是说它们可以移出中央函数、特征零 Newton 读者
或未经支付的第一 primitive。
Cartier 的准确规则仅是
$C^2(r_S^{p^2}\xi)=r_SC^2(\xi)$；
$F_p^p$、$\Phi_+^{130}$、全部测试和来源仍按原顺序处理。

### 9.4 最终 degree10 平移与四阶算子的准确缩放

令 $v=v_{13,10}$，
$$
a_i=iv,\quad B_i=\pi a_i,\quad
\mathcal I_i=T_{a_i}^{(130)}D_\pi,\qquad 1\le i\le12.
$$
用固定完整 Miller 因子 $M_i$ 记其有理部分：
$$
R_{\mathcal I_i(\sigma^{10}U)}(P)
=M_i(P)\,U(\pi P+B_i).
$$
$M_i$ 是该原 canonical lift 与原 sigma 比值所指定的函数；
不允许逐字重新归一。
式 (52) 因而给实际同点字
$$
R_{T_S\mathcal I_i(\sigma^{10}U)}(P)
=C_S^{130}\Phi_+^{130}(P)\,
 M_i(P+S)\,U(\pi P+B_i-S).
\tag{58}
$$
最后的负号是 (51) 的 $\pi S=-S$。
因此反次序 $N=130$ 标准化中的外部 $+S$，
到最终 degree10 来源准确成为 $-S$；
不能沿用另一顺序的未转换 $U(P+S)$。

在这个实际字的有理部分上，准确的源端导数是
$$
\boxed{
\mathscr D_i^{S}
=\pi^{-1}
\left(D-130j_S-D\log M_i(P+S)\right).
}
\tag{59}
$$
它作用于 (58) 时，结果恰为同一整前因子乘
$(DU)(\pi P+B_i-S)$。
由于 (56) 的两个水平因子被 $D$ 杀掉，
(59) 对 (57) 的共同权后之字仍有同样作用。
其四次幂没有新增 $\delta^{-4}$：
经原 $D_\delta$ 拉回时
$\pi^{-1}D_{\delta\text{-target}}$ 正好变成
$\alpha^{-1}D_{\rm source}$，与 (42) 完全一致。

令 $\mathcal P_i^S$ 为
$T_S\mathcal P_iT_S^{-1}$ 的实际 transported word projector，
并在 (57) 上按同一共同乘子再共轭；
这只定义原完整十二字的有序分解，
不将其投影越过任意别的乘子。
对应算子
$$
\mathscr O_{\rm mid}
=\sum_{i=1}^{12}\chi_8(i)
 \left((\mathscr D_i^S)^4
       -54x(\pi P+B_i-S)(\mathscr D_i^S)^2\right)
 \mathcal P_i^S
$$
于是严格给
$$
\boxed{
\mathscr O_{\rm mid}
\bar A_{130,\delta}^{\,\infty}(B_+)
=60\,\bar A_{130,\delta}^{\,\infty}(A_+).
}
\tag{60}
$$
这是 (41) 与 $\chi_8\chi_{10}=\chi_6$ 的完整同点身份；
没有新三处相位，也没有改变任何十三 profile。
第一 Cartier 对这三个角色同时取 $p$ 次根，
$\chi_8,\chi_{10},\chi_6$ 分别变成
$\chi_4,\chi_2,\chi_6$，其乘法关系保持；
第二 Cartier 恢复原角色。

后续整个 $\pi$ trace 仍必须使用
$\pi^{-10}\operatorname{Tr}_{[\pi]}
(V_\pi\,\bar A_{130,\delta}/R_\pi^{10})$。
在饱和范围 $V_\pi\bmod p=v_\pi^{p^2}$，
它也是显示的水平因子，但不允许移到 trace 外。
原 $P_{10},Z^{-b-1}$ 及其全部曲率 (47) 继续位于完整乘积中。
因此 (60) 付清了实际 $O^\dagger$ 应从哪一组字、
哪一个缩放和哪一个真实平移生成；
它没有提前断言伴随测试已由 canonical 必要行消去。


### 9.5 原点全窗与真正的固定同 charge 来源

先只在式 (57) 的实际 $\delta$ target 原点工作。
R1028 的完整式和 R887 的 $F_p$ 给
$$
W_\infty=c_pu^pF_p,\qquad
\mathcal K_p=-W_\infty^p,\qquad u=x/y.
$$
因为
$W_\infty=1-y^{-2p}+c_pu^pZ=1+O(z^{p+1})$
且 $r_S^3=(y+1)/(y-1)=1+O(z^3)$，
原首项为一的固定根给
$$
\boxed{
\mathcal K_p+1=O(z^{p^2+p}),\qquad
r_S^{p^2}-1=O(z^{3p^2}).
}
\tag{61}
$$
乘上式 (57) 的完整 $\sigma^{130}$ 来源后，其原点均正则。
所以在真正 native degree130 的全部系数
$n\le H(p+1)<p^2$ 中，整个旧返回恢复 $g$，
整个新返回分别恢复 $T_SG_A,T_SG_B$，均为模 $p$ 的准确身份。
这里没有在其余十三个核点删去 (61) 的误差，
也没有将此模 $p$ 观察升格为模 $p^K$ 的全 trace 身份。

事实上，存在更强且不用 (61) 的特征零比较。
由 (53)，固定来源
$$
\widehat A=T_S^{(130)}G_A,\qquad
\widehat B=T_S^{(130)}G_B
$$
严格满足 $A_+(z)=\widehat A(\delta z)$、
$B_+(z)=\widehat B(\delta z)$。
置 $d=p+1$、
$q_\delta=\delta^d/3\in1+p\mathcal O$。
沿 R978/R1022 的原 Tate 归一，
先在正整数权核系数，再由原解析唯一性得到
$$
\boxed{
J_{390,A_+}(v)=q_\delta^vJ_{130,\widehat A}(v),\qquad
J_{390,B_+}(v)=q_\delta^vJ_{130,\widehat B}(v).
}
\tag{62}
$$
两条来源的实际质量为零，故
$j_{390,A_+}=j_{130,\widehat A}$、
$j_{390,B_+}=j_{130,\widehat B}$。
于是原两条 canonical 坏条件确实给这两个完整固定三次 cover
来源的 charge65 中央零；并非只利用
$\delta^{p+1}\equiv3\pmod p$。

整性和原收敛窗无需猜测一个新的 translated-theta 定理。
记原 regularized Gaussian 为
$G_{D,f}(z)=e^{-Dc z^d}f(z)$。
完整恒等式
$$
\boxed{
G_{130,\widehat A}(z)
=\exp\!\left(130c(q_\delta^{-1}-1)z^d\right)
 G_{390,A_+}(z/\delta)
}
\tag{63}
$$
对 $\widehat B$ 也成立。
原 $v_p(c)=-1$，而 $q_\delta-1\in p\mathcal O$，
故额外指数参数整；$\delta$ 是单位。
其整 Hurwitz 系数、完整原点窗口及严格内盘收敛
均从已付的原390来源与整指数乘法继承。
原 $d\ell$ 读者只取整个来源的 principal 部分；
投影不能移到某个单字或某个外权之前。

若希望与 R989 的首项规范完全一致，可直接用 R981 的
$\Psi_{35}=z^6+O(z^{12})$、
$\Psi_{53}=z^6+O(z^{12})$ 定义两个固定来源
$$
\widetilde\Psi_{35}(z)=\delta^6\Psi_{35}(z/\delta),\qquad
\widetilde\Psi_{53}(z)=\delta^6\Psi_{53}(z/\delta).
\tag{64}
$$
它们仍以 $z^6$ 为首项，质量为零；原坏条件给
$j_{130,\widetilde\Psi}=0$。
因此四条真实算术必要行可统一为
$$
\Phi_*,\quad\Phi_{260},\quad
\widetilde\Psi_{35},\quad\widetilde\Psi_{53},
\qquad n=65,\quad q=n/17=65/17.
\tag{65}
$$
后两条是固定三次 cover 上的实际来源，
不能认作原完整22维 $S_{130}$ 的两条新向量。

更精确地，令 $w=z^6$，则 R989 的 inner 满足
$$
\boxed{
B_{\widetilde\Psi,65}(w)
=B_{\Psi,195}(w/\delta^6)
 \exp\!\left(130c(q_\delta^{-1}-1)w^s\right).
}
\tag{66}
$$
R989 的按 $w$ 次数 Hurwitz 代数对单位缩放及此整指数封闭；
其全部 $h\ge9$ 尾界因此原样成立。
第七、第八完整整端点也保持：至 $8s-1$，
额外指数至多用七次项，所有相应阶乘是单位。
在同一个五高轴 family 中，(65) 因而都使用相同的
$e^{(65/17)\eta_x}$ 和同一完整六位必要式。
这给两条可直接代入的实际同 charge 行，
并没有改变原旧六行、删除较低卷积，
或声称两个不同高轴 family 在 $x\ne0$ 时相同。

## 依据

- R978、R1015、R1018：原 $S_{10}$ 两条 old、$q$、完整十三
  profile、Weyl-dual 相位及 $c_*$ 的绝对规范。
- R981：两条固定曲线的实际独立点、全坏位角色、Schwartz、
  同一全权平方和通常全 Selmer 桥。
- R976：本篇使用的完整66列一维性、两条第六系数规范及
  三个补线的真实非零质量。
- R985：原 canonical Heisenberg lift、相位与 Miller 代数性。
- R1020、R1022：同一个 whole target 的唯一 primitive 类与
  原39纤维全精度 trace；本篇未以字零替换其完整读者。

- R1028、R989：末六原权的完整共同低窗，以及原五高轴/六位必要式与全部 Hurwitz 尾。第9节保固定三次 cover 和真实 Gaussian，未将其冒认原22维来源。

## 10. 同两条 canonical 的准确一阶算子与唯一曲率

本节保留 §8–9 的全部实际 word projector、原 Miller、$\chi_8$
和 $\alpha/\pi$ 缩放。它将同一个来源间算子降为一阶，
不添加任何新曲线或未付中央零。

### 10.1 固定有理来源的一阶身份

沿原 $U_B=xy$、$U_A=y(X+4)$，直接由
$DU_B=5X+2$ 得
$$
\boxed{(2yD-9x^2)U_B=U_A.}
\tag{67}
$$
两项的原点极阶都至多九，所以这是完整 $\mathcal S_{10}$
来源之间的身份。对整个 $u_i=\sigma^{10}U_i$，
准确写为
$(2y\nabla_{10}-9x^2)u_B=u_A$；
不能把 $\nabla_{10}$ 换成未补偿的全函数导数。

它与 §8 的四阶式完全相容，且有更强的算子恒等：
$$
\boxed{
D^4-54xD^2-60(2yD-9x^2)
=(D^2-24x)(D^2-30x).
}
\tag{68}
$$
展开时必须使用
$D^2x=xD^2+4yD+6x^2$。
原 $U_B$ 满足 $(D^2-30x)U_B=0$，
所以原四阶在这条实际来源上的作用恰为一阶的60倍；
没有将两个算子在任意输入上等同。

### 10.2 完整24字、正三支与绝对规范

保持 (42) 的实际 $\mathscr D_{s,i}$，
置
$$
y_{s,i}(z)=y(\alpha z+B_{s,i}),\qquad
\boxed{
\mathscr Q=
\sum_{\substack{s=\pm1\\1\le i\le12}}
 \chi_8(i)\bigl(2y_{s,i}\mathscr D_{s,i}
                  -9x_{s,i}^{\,2}\bigr)\mathcal P_{s,i}.
}
\tag{69}
$$
仍先投影实际 word，再使用其完整连接。
由 $\chi_8\chi_{10}=\chi_6$ 和原 raw 常数，
(67)逐字给
$$
\boxed{
\mathscr Q f_B=\frac{2}{15}f_A,\qquad
\mathscr Q_+ B_+=A_+.
}
\tag{70}
$$
第一系数为 $(1/60)/(1/8)=2/15$；
第二式的两个完整正支没有额外的 $1/8,1/60$，
故系数准确为一。两式都保留全部十二个十三字之和，
未把中央零分别赋给单字。

对 §9 的实际 $\delta$ target，
令 $\mathscr Q_{\rm mid}$ 由 (69) 换成
$$
2y(\pi P+B_i-S)\mathscr D_i^S
 -9x(\pi P+B_i-S)^2
$$
及同一个 transported projector 给出。
(59) 中准确是 $\pi^{-1}D$；再经 $D_\delta$ 拉回才是
原 $\alpha^{-1}D$，没有新增一个 $\delta^{-1}$ 费用。
所以 $\mathscr Q_{\rm mid}$ 也把整个正 $B$ 返回送到正 $A$ 返回。
对 R1028/R1032/R1034 的共同模 $p$ 权，
只有已经显示为 $p$ 次幂的共同因子可在这一步保为水平；
其后仍须保原完整 $\pi$ trace 和 $P_{10}/Z$ 读者。

第一 Cartier 把三个十三角色依次送到
$\chi_4,\chi_2,\chi_6$，其乘积关系继续成立；
第二次恢复原角色。这没有改变 (70) 的绝对规范。
在两条原 canonical 坏假设下，已付的实际零准确是
$j(f_B)=0$ 和 $j(\mathscr Q f_B)=(2/15)j(f_A)=0$。

### 10.3 原 P10 中只有一项曲率

在共同的实际 degree10 target，保持
$$
L=D-10G,\qquad M=D+10G,\qquad
P=P_{10},\qquad e=LP=10\mathcal H^pZ^{p+9}.
$$
Leibniz 与 (67)准确给
$$
\boxed{
(2yL-9x^2)(PU_B)-PU_A
=2yeU_B
=20\mathcal H^pZ^{p+9}x(X+1).
}
\tag{71}
$$
这一次没有 $Le,L^2e,L^3e$。
真实伴随对整个实际测试 $a$ 是
$$
\boxed{
C\bigl(a(2yL-9x^2)h\,\omega_E\bigr)
=C\bigl((-2yMa-15x^2a)h\,\omega_E\bigr).
}
\tag{72}
$$
$-15$ 包含 $D(2y)=6x^2$ 的费用，不能误写成 $-9$。
若先执行实际外部平移，则这里的 $x,y,U_B,U_A$
都在同一个真实平移点取值；
$G,P_{10},Z$ 仍是该完整读者的原模型。
所有 Miller、$\chi_8$ 及 cut 留在 $a$ 中，
没有把 (72) 当作原测试已自动封闭。

R1034 的固定
$R_\gamma=-2xy/[3(X+4)]$ 还给精确同点匹配
$$
R_\gamma U_A=-\frac23x(X+1),\qquad
2yeU_B=-3eR_\gamma U_A.
$$
因此其一阶分部积分可以与 (71)逐项联立，
且唯一曲率的比例为 $-3$，不是未定常数。
但对任意测试作这两次分部积分只会恢复同一恒等式：
还须证明实际测试 $-2yMa-15x^2a$
确由原两 canonical、同一高窗和已付合法平坦族的完整行生成。
本节没有把这个缺口替换为微分、乘法或奇主部的免费中央零。

## 11. 一阶算子的完整限制谱及真正转置

本节仍在原 $p=6s-1>13^4$ 的同一个函数域与 $D,G,Z,P_{10}$ 中工作。
它计算 (67)、(72) 的完整 $p$ 次关系；不把这个谱关系解释为
$p$ 条新的 canonical 零。

### 11.1 原椭圆曲线上的一阶限制幂

置
$$
V=2yD=4(X+1)\frac{\partial}{\partial x},
\qquad
\beta_V=\frac{dx}{4(X+1)}.
\tag{73}
$$
$\beta_V$ 是 $V$ 的对偶微分。
在三个 $e^3=-1$ 的点，$\beta_V$ 的留数为 $1/(12e^2)$。
因 $e^p=e^{-1}$，Cartier 后留数为 $e^2/12$，
恰是 $-x\beta_V$ 的留数。
两者都是从 $\mathbf P^1_x$ 拉回的微分，在无穷点正则；
其差在 $\mathbf P^1$ 上全纯，故差为零。因此
$$
\boxed{C\beta_V=-x\beta_V,\qquad V^p=-x^pV.}
\tag{74}
$$
第二式的规范可直接由一变量恒等核对：
若 $V=a\partial_x$、$V^p=bV$，则
$b=-a^p\partial_x^{p-1}(a^{-1})$，
而 Wilson 公式给
$C(a^{-1}dx)=-(\partial_x^{p-1}a^{-1})^{1/p}dx
=b^{1/p}a^{-1}dx$。
这些等式先在 $k(x)$ 成立，再沿可分二次扩张延至 $k(E)$；
没有用未知的比例常数。

令 $m=(p+3)/2$。因为 $V\log y=6x^2$ 且 $6m=9$ 于剩余域，
有完整函数域 gauge
$$
\boxed{
Q_1=2yD-9x^2=y^mVy^{-m},\qquad
Q_1^p+x^pQ_1=0.
}
\tag{75}
$$
这里 $x^p$ 是 $F^p$ 中的中心标量。
该恒等保留 $y^m$ 的全部零极，不把 gauge 当成原整源格的单位变换。

### 11.2 原 P10 联络的曲率项

沿 (71) 的 $L=D-10G$、$M=D+10G$，
原 $D^p=0$ 与 $D^{p-1}G=r_0^p$ 准确给
$$
L^p=-10\mathcal H^p,\qquad
M^p=10\mathcal H^p,\qquad \mathcal H=G+r_0.
\tag{76}
$$
对这两个秩一联络，曲率关于向量场为 $p$ 次线性。
所以 (74) 给
$$
(2yL)^p+x^p(2yL)=-10(2y\mathcal H)^p,
\qquad
(2yM)^p+x^p(2yM)=10(2y\mathcal H)^p.
$$
这也可由 $\nabla_V^p-\nabla_{V^p}=(2y)^p
(\nabla_D^p-\nabla_{D^p})$ 直接核对。
因此完整有限模型的一阶算子
$$
\boxed{
Q_L=2yL-9x^2=y^m(2yL)y^{-m},
\qquad
Q_L^p+x^pQ_L=-10(2y\mathcal H)^p.
}
\tag{77}
$$
右侧是原模型的确定函数，不是应被舍掉的误差。
特别是，裸 $Q_1$ 的零多项式不能替代 $Q_L$ 的关系。

### 11.3 真转置与相同右端

(72) 的准确伴随是
$Q^\dagger=-2yM-15x^2$。
令 $n=(p+5)/2$；$6n=15$，故
$$
\boxed{
Q^\dagger=-y^{-n}(2yM)y^n,\qquad
(Q^\dagger)^p+x^pQ^\dagger=-10(2y\mathcal H)^p.
}
\tag{78}
$$
外面的负号经奇数次 $p$ 幂仍保留。
于是右端与 (77) 相同，不能误改为正号。
这里没有遗漏 $D(2y)=6x^2$ 的转置费用。

一个可直接检查的测试是 $a=c^p y^{-n}$：
其非 $G$ 的伴随部分确相消，
$$
Q^\dagger(c^p y^{-n})=-20yG\,c^p y^{-n}.
$$
但这只描述该具体测试的作用。
要把它用于原中央值，仍须证明原 cut、全部外权和物理矩阵
确实提供这个测试；不能从此式反向添加一行零。

所有实际 word 的平移、Miller 和 $\alpha^{-1}/\pi^{-1}$ 连接
必须按 §10 的完整共轭一起运输。
有限角色也保留在整个词内：
在惰性素数上 $\chi_8^p=\chi_4$，
不能在 $p$ 次关系中把它擅自固定为 $\chi_8$。
本节没有把局部 (77) 不加条件地提升为
跨不同 projector 的一个全局标量多项式。

### 11.4 实际零的范围没有扩大

由 (67) 再作用一次即得
$$
\boxed{Q_1^2U_B=9x^5y.}
\tag{79}
$$
它在 $O$ 有十三阶极，已越过原 $\mathcal S_{10}$ 的十阶帽。
所以即使裸算子满足 (75)，也不能把
$U_B,Q_1U_B,\ldots,Q_1^{p-1}U_B$
全部叫作已经支付的 canonical 来源。

目前真正的零仍只有 (70) 所指的两条原完整来源及其已经证明的
合法同窗返回。新的限制谱将实际伴随约束压到一个确定的
一阶算子和原 $\mathcal H$ 曲率；
它没有自动证明测试族对 $Q^\dagger$ 封闭。
后续必须在 R1034 的同一个高精度物理矩阵、$\beta/\gamma$
两种合法平坦权、实际 cut 和完整十三字中证明这种生成关系。

## 12. 原三处 norm 的完整 G 交叉与第一个实际单位

这一节只用 R887 的原指定 $Z,G,\mathscr F_p$ 和 R1024 的实际
三挠平移。它支付把 $\delta$ 的完整 sigma 连接接到三支平均时
必须保留的项，不以这个局部单位另加中央零。

写 $S=(0,1)$、$r_0=x^2/y$、$\rho_p=c_p^{-1}$。
下标 $\delta,\pm$ 分别表示 $[\delta]$、$P\mapsto P\pm S$ 的实际拉回。
原加法公式直接给
$$
y\,y_+y_-=3\delta y_\delta,\qquad
j_++j_-=\frac{2y}{x},\qquad
r_0+r_{0,+}+r_{0,-}=\delta r_{0,\delta}.
$$
利用 R887 的全 $\mathscr F_p$ cocycle，而非另选 primitive，
遂得
$$
\boxed{
\mathscr F_p+\mathscr F_{p,+}+\mathscr F_{p,-}
=-\delta\mathscr F_{p,\delta},\qquad
Z+Z_++Z_-=-\delta Z_\delta.
}
\tag{80}
$$
例如第二式中的 $r_0^p$ 项准确相消，因为 $\delta^p=-\delta$。
它是整个函数域等式。

### 12.1 三支平均与 CM 拉回并不具有同一个 G

定义原实际差
$$
K_\delta=\delta G_\delta-G-G_+-G_-.
$$
原 $\delta^2x_\delta=x+x_++x_-$ 和 $DG=-x+c_pZ^{p-1}$ 给
$$
\boxed{
DK_\delta
=c_p\left\{
3(Z+Z_++Z_-)^{p-1}
-Z^{p-1}-Z_+^{p-1}-Z_-^{p-1}
\right\}.
}
\tag{81}
$$
这里使用 (80) 和 $\delta^{p-1}=-1$。
右端的交叉项没有被加法关系删掉。

为锁住水平项，沿 R1024 定义原有限算子
$$
\mathcal G_T(f)=-\sum_{i=0}^{p-2}
 \frac{(-1)^iT^{i+1}D^if}{(i+1)!},\qquad
\Pi_Tf=\sum_{i=0}^{p-1}\frac{(-T)^iD^if}{i!}.
$$
置
$$
a_\pm=Z_\pm-Z=h_\pm^p,\qquad
b=Z_\delta/\delta-Z=h_\delta^p/\delta
       =\frac{a_++a_-}{3},\qquad j=2y/x .
$$
因 $\delta^2x_\delta=3x-Dj$，同一个原有限和准确给
$$
\boxed{
\delta G_\delta-3G-j
=3\{\mathcal G_{Z+b}(x)-\mathcal G_Z(x)\}
-\Pi_{Z+b}j.
}
\tag{82}
$$
平移的相应式就是 R1024(25)。
故以下水平项始终由 (82) 与那两个实际平移式定义，
不能换成自由参数。

逐原有限 Taylor 和分开非水平部分，有完整等式
$$
\boxed{
K_\delta=
c_p\sum_{\ell=1}^{p-1}\frac{(-1)^{\ell-1}}{\ell}
 \left(3b^\ell-a_+^\ell-a_-^\ell\right)Z^{p-\ell}
+k_\delta^p .
}
\tag{83}
$$
所有分母都是单位，$k_\delta^p$ 是 (82) 指定的剩项。
特别 $\ell=1$ 整项由 $3b=a_++a_-$ 精确消失。

### 12.2 不依赖未知 Fermat 商的首项

R1024 的原 $h_\pm$ 和 R887 的 $h_\delta$ 给
$$
a_+=-3\rho_pZ^{2p}+O(Z^{5p}),\quad
a_-=3\rho_pZ^{2p}+O(Z^{5p}),\quad b=O(Z^{5p}).
$$
(83) 的 $\ell=2$ 因而准确贡献
$9\rho_pZ^{5p-2}+O(Z^{8p-2})$。
$\ell=3$ 使用
$a_+^3+a_-^3=(a_++a_-)\{(a_++a_-)^2-3a_+a_-\}$
得阶至少 $10p-3$；$\ell\ge4$ 的阶至少 $9p-4$。

还必须核水平项不能抢在它之前。
R1024(26) 的原水平公式对三支使用后，
$-\Pi_Z(j_++j_-)+\Pi_Zj_++\Pi_Zj_-$ 完全相消。
平移剩项的首项含
$a_\pm\Pi_Zx_\pm$；
$x_\pm(O)=0$ 且其 CM3 型迫 $\Pi_Zx_\pm=O(Z^{2p})$，
故它从 $4p$ 起。其余平移项至少含 $a_\pm^2$，同样从 $4p$ 起。
CM 支的首项含 $b\Pi_Z(\delta^2x_\delta)$，
从 $7p$ 起；其余项更高。
对最后可能有 $p$ 阶极的有限 Taylor 坐标，
显示 $b^\ell$ 或 $a_\pm^\ell$ 的阶仍严格支付上述界。

所以 $k_\delta^p=O(Z^{4p})$。
整个 $K_\delta$ 及 (83) 的显示和都为 $\mu_6$ 型五；
水平指数 $mp$ 因而必须满足 $m\equiv1\pmod6$。
$4p$ 以后的第一个允许水平指数是 $7p$。于是
$$
\boxed{
K_\delta=9\rho_p Z^{5p-2}+O(Z^{7p}),\qquad
9\rho_p\in k^\times .
}
\tag{84}
$$
这里原 $Z^p$ Gaussian 水平项及 $6p-1$ 非水平项都已经实际相消；
不需要假定原三处 Fermat 商为单位或为零。

### 12.3 它在完整一阶运输中的位置

原 sigma 的三支 norm 与 $\delta$ 拉回具有相同的
$\delta x$ Miller 因子。
但在有限模型中，它们的 degree10 拉回连接分别使用
$\sum_{T\in\ker\delta}G_T$ 和 $\delta G_\delta$。
准确差为
$$
\boxed{
\left(D-10\delta G_\delta\right)
-\left(D-10\sum_{T\in\ker\delta}G_T\right)
=-10K_\delta.
}
\tag{85}
$$
因此 (84) 是已经固定的原模型交叉，
不能在 $\gamma$ 的 Jacobian 或 (72) 的真实转置中省掉。
原 $P_{10}$ 的运输还须继续保留其整个 $\Xi$、
实际 cut 与原十三 trace；(85) 没有以一个连接前缀替代这些数据。
本节未把 (84) 的单位冒作已被坏 canonical 假设迫零的读数。

## 13. 两条实际 δ-new 来源的三个二挠译像

本节的 $f$ 分别为原完整 $f_A,f_B$，或它们在 R981
所用的同一固定非零归一倍数。全部十二个十三字保持。
对 R967 的三个指定二挠点与原 degree390 Weyl lift，准确有
$$
\boxed{
\Pi_0T_T^{390}f=\frac1{\sqrt3}f
\quad(0\ne T\in E[2]).
}
\tag{86}
$$
$\sqrt3$ 仍为 R967 锁定的正实根。
这里的正号不能由 degree10 target 的裸来源猜测。

### 13.1 完整有限模型的直接证明

R981 的两条实际来源均为 dyadic $\epsilon=0$，
采用 R959/R967 的同一个二处向量；这里
$f_0=e_0-e_2$、$f_1=e_1+e_3$：
$
\phi_2=f_0+t f_1,\qquad t=(\sqrt3-1)/\sqrt2.
$$
实半点 $T=(-1,0)$ 的原 Fourier 作用是 $(-1)^n$，
所以只把二处向量换为 $f_0-tf_1$；三、五、十三处完整向量不变。
R967 的原酉矩阵投影准确为
$$
\frac{1-t^2}{1+t^2}\phi_2=\frac1{\sqrt3}\phi_2.
$$
其另一二处特征使 R981 的
$a+b+\epsilon+c\equiv0\pmod3$
失效，故没有几何 principal Hermite 系数。
两来源在三、五处都奇，整体仍偶；二处替换不改变这项。
R967 的完整 Weil／Hermite 交织因此对这两个实际张量逐系数适用，
给整个 entire 截面的 (86)，不是只给质量或某一低 jet。
CM 将三个原半点及其 Weyl lift 循环，正号和同一个
$\sqrt3$ 均保持。

### 13.2 degree10 负号为何不能沿用

独立的绝对规范核对可在原 $U_A,U_B$ 上完成。
R967 的实半点 addition 及 $c_T=1/\sqrt3$ 给
$$
T_T^{10}(\sigma^{10}U_B)
=\frac{\sigma^{10}y}{3\sqrt3}(X-3x-2),
$$
$$
T_T^{10}(\sigma^{10}U_A)
=-\frac{\sigma^{10}y}{\sqrt3}(X+6x^2+4).
\tag{87}
$$
分别投影回 $U_B$、$U_A$ 的实际 CM 角型，
两个系数确实都是 $-1/\sqrt3$。

但原 $\alpha=\delta\pi=2+7\omega$ 满足
$$
\alpha(r/2)=\omega r/2+(1+3\omega)r
\quad(r=1,\omega,\omega^2).
$$
在原 $\Lambda=(1-\omega)^{-1}\mathcal O_K$ 上
$E(1,\omega)=3$，故 degree10 的 Weyl 换代表相位为
$\exp(\pi i\,10\cdot3/2)=-1$。
原严格交织
$T_T^{390}D_\alpha=D_\alpha T_{\alpha T}^{10}$
于是恰好再添一个负号，恢复 (86)。
原三、十三中心与二挠点的 degree390 交换子都是一；
保持全部有序 lift 后，没有改动五、十三角色或原 raw 常数。

### 13.3 真中央授权及其使用范围

(86) 的常数项说明每个实际译像仍质量零。
它是固定的 whole degree390 截面，原代数 half-point 公式
在排除 $2,3$ 后整；同一个完整 Gaussian 和 Newton 读者只取
$\mu_6$ 主型。因此整个收敛函数准确满足
$$
\boxed{
J_{390,T_Tf}(v)=\frac1{\sqrt3}J_{390,f}(v),\qquad
j_{390,T_Tf}=\frac1{\sqrt3}j_{390,f}.
}
\tag{88}
$$
所以原两条坏 canonical 假设确实支付这六个固定 translated
来源的中央零，无须另加秩假设，也没有给单个十三字赋零。

对 R1034 的 $\chi_\alpha$ 读取，这项授权先用于
$T_T^{390}f$ 的同一个合法特征零 flat 返回。
若要改为平移已经得到的 target，准确变权是
$$
\boxed{
\mathcal T_{\alpha,W}(T_T^{390}f)
=T_{\alpha T}^{10}\mathcal T_{\alpha,W(\,\cdot-T\,)}(f),
}
\tag{89}
$$
这里 $\mathcal T$ 含原全部 sigma、未平均 trace 与绝对相位。
它由完整纤维重排和原 Weyl 交织给出。
不能将右侧的 $W(\cdot-T)$ 换回 $W$。
特别原 meromorphic $h_\chi(f)$ 在 target 的二挠点可能有极，
其直接平移到 $O$ 后不自动属于原中央读者的整源域。
(89) 中的权差、$P_{10}$ 运输和 cut 仍须一并消费。

## 14. δ 适配连接的首单位与完整曲率抵消

本节保持 §12 的原 $Z,G,\delta$，令
$$
j_\delta=2y/x,\qquad b_\delta=Z(\delta P)/\delta-Z(P),\qquad
A_\delta=\delta G(\delta P)-3G(P)-j_\delta .
\tag{90}
$$
这是把 degree10 的原模型沿 $[\delta]$ 拉回到 degree30 时实际出现的连接差，
不同于 §12 的三个平移连接之和 $K_\delta$。
以下均在 R887 §19 已付的同一个有限整窗口内读取。
仍记 $\rho=c_p^{-1}$、$q_\delta=\delta^{p+1}/3\in1+p\mathcal O$。

### 14.1 原有限 Taylor 规范锁定全部首项

原 R887 (107) 给
$Z=z-\kappa_5z^{5p}+O(z^{11p})$，
$\kappa_5=(3/5)^p/c_p$。
因为 $\delta^p=-\delta$，有 $\delta^{5p-1}=-9$，故
$$
b_\delta=10\kappa_5Z^{5p}+O(Z^{11p})
       =6\rho Z^{5p}+O(Z^{11p}).
\tag{91}
$$
这里没有把 $z$ 当作全局有理参数；所用次数均在原整窗口内。

以 $\mathcal G_T(x)$ 表示原 $G$ 的有限 Taylor 多项式，只把显示的
$Z$ 换为 $T$。原 sigma division 给
$\delta^2x(\delta P)=3x-Dj_\delta$。
逐项保原 $p-1$ 个项，准确得到
$$
\boxed{
A_\delta
=3\{\mathcal G_{Z+b_\delta}(x)-\mathcal G_Z(x)\}
 -\Pi_{Z+b_\delta}j_\delta .
}
\tag{92}
$$
这里 $\Pi_T=\sum_{i=0}^{p-1}(-T)^iD^i/i!$。
所用恒等是 $\mathcal G_T(Dj)=\Pi_Tj-j$；
不留一个任意 horizontal 初值。

原 $\partial_T\mathcal G_T(x)|_{T=Z}
=-\Pi_Zx+c_pZ^{p-1}$。
$\Pi_Zx$ 在原点正则，原 CM 型使其首可能次数为 $2p$；
因此它乘 (91) 的贡献从 $7p$ 起。
二次以上的 $b_\delta$ 项更高。
同样 $\partial_T\Pi_Tj|_{T=Z}=-\Pi_ZDj$，
其与 $b_\delta$ 的差从 $7p$ 起。
最后 $\Pi_Zj_\delta$ 的型只允许 $p,7p,\ldots$ 次项。

其第一个系数也由原特征零来源固定：
$j_\delta=\delta\zeta(\delta z)-3\zeta(z)$，
故先在特征零除 $p$ 再约化，
$$
[z^p]j_\delta
=(\delta^{p+1}-3)[z^p]\zeta
=-3c_p\,\frac{q_\delta-1}{p}\pmod p.
$$
这里用 $p[z^p]\zeta\equiv-c_p$，
即原同一个 Gaussian 的 Hasse 系数；
没有在剩余域中直接除以零。

于是完整首式为
$$
\boxed{
A_\delta
=3c_p\frac{q_\delta-1}{p}\,Z^p
 +18Z^{6p-1}+O(Z^{7p}).
}
\tag{93}
$$
$18$ 对本课题全部 $p>13^4$ 为单位。
另一个独立核对是原全函数微分式
$$
DA_\delta
=3c_p\{(Z+b_\delta)^{p-1}-Z^{p-1}\}.
$$
由 (91) 其首项为 $-18Z^{6p-2}$，
恰为 (93) 中非水平项的导数。
首 $Z^p$ 系数则必须保留原费马商，不能由这个微分式删掉。

### 14.2 真实 P 模型中同阶曲率恰好相消

令
$$
\widehat P_{30,\delta}
=\delta^{-10}\frac{P_{10}(\delta P)}{x^{10}} .
$$
它在原点从 $z^{30}$ 起，首系数一。
因为 $D\log x=j_\delta$，
原曲率方程逐项给
$$
\boxed{
(D-30G)\widehat P_{30,\delta}
=10A_\delta\widehat P_{30,\delta}
 +10\delta^{-9}
  \frac{\mathcal H(\delta P)^pZ(\delta P)^{p+9}}{x^{10}} .
}
\tag{94}
$$
右边第二项不是原 $30\mathcal H^pZ^{p+29}$，
因此不能用 (93) 的单位直接宣布两个 $P$ 模型首差为单位。

准确地，$\mathcal H=(3/5)z^5+O(z^{11})$，
$\delta^{6p}=-27$。
(93) 的首非水平项在 (94) 中贡献
$180z^{6p+29}$。
适配曲率与原 $P_{30}$ 曲率的同阶差却是
$$
10(\delta^{6p}-3)(3/5)^p z^{6p+29}
=-180z^{6p+29}.
$$
这两个显示贡献完全抵消。
首水平 Gaussian 串仍须原样保留；
这个抵消没有给整个比例赋常数。

为明确锁定真正留下的初始化，沿 R887 (105)–(106) 记
$$
c_a(j)=[w^j](\sigma^\circ/z)^{-a},\qquad
e_{a,p}=c_a(p)+(1-a)\kappa_5c_a(s).
$$
该有限 Taylor 证明对当前 $a=10,30<p$ 原样成立。
在同一原窗口中，
$$
\boxed{
\frac{\widehat P_{30,\delta}}{P_{30}}
=\exp\{-30c(q_\delta-1)z^{p+1}\}
 \{1+(-27e_{10,p}-e_{30,p})z^{6p}
       +O(z^{6p+6})\}.
}
\tag{95}
$$
指数参数整，仍由原 $c=[z^{p+1}]\log(\sigma/z)$ 固定。
显示指数只在这个有限窗口截取，所需指数次数至多五、阶乘均为单位；
没有宣称任意阶的形式指数都整。
公式由完整 $\sigma(\delta z)=\delta\sigma^3x$
和两个原 $P_a$ 的 (106) 直接相除得到。
去掉显示 Gaussian 后，$z^{6p}$ 是一个真实 horizontal 系数；
本节既未赋其零，也未赋其单位。
(94) 的曲率不能由裸连接抵消替代，
(95) 的全低卷积也不能从原高位物理矩阵中删除。

本节无新增数学执行。

## 15. 三个二挠 lift 的完整 Pauli 返回与真实 fourth 余项

本节继续用 §13 的同一两个完整 $f$，保持全部十三字。
记 $U_r=T_{r/2}^{390}$、$V_r=T_{r/2}^{378}$
（$r=1,\omega,\omega^2$），并令 $S_N$ 为相应三个 lift 之和。
所有代表和正实 $\sqrt3$ 均沿 R967，不重新选中心。

### 15.1 whole 和式及两种不同的中心

R967 §3 已付 CM 对三个指定 lift 的严格循环；
它们也保持偶性。
因此 $S_{390}$ 与原 principal 投影交换。
$f$ 本身 principal，故 §13 的三个准确投影立即给整个截面恒等
$$
\boxed{S_{390}f=\sqrt3 f.}
\tag{96}
$$
这里的推理使用整个和式已 principal，不把一个未成轨道的译像直接等同于其投影。

中心还可完全核定。
原 Weyl 公式是
$T_u^NT_v^N=\exp(\pi iN E(u,v))T_{u+v}^N$，
且 $E(1/2,\omega/2)=3/4$。
因 $1+\omega=-\omega^2$，偶 degree 下 $T_{-T}^N=T_T^N$，准确得到
$$
U_1U_\omega=iU_{\omega^2},\qquad
V_1V_\omega=-iV_{\omega^2},
$$
及其循环式；反向乘法各添负号。
两种 $S_N$ 都平方为 $3I$，但其有序 Pauli 中心确实相反。
不能只凭抽象二维表示把 (96) 的标量移给 $S_{378}$。

### 15.2 一个实际 whole degree378 来源

置
$$
B_{12}=\sigma^{12}y^2=\frac14\sigma^4\sigma(2z)^2,\qquad
F=f/B_{12}.
$$
$B_{12}$ 在 $O$ 恰六阶零，在三个二挠点各恰二阶零。
原 $f$ 在这些点分别至少六阶、二阶零，故
$F$ 是完整 degree378 截面。
它的质量为 $c_6(f)$；不能因为 $f$ 质量零就给 $F$ 赋质量零。

写 $T=(e,0)$、$e^3=-1$，原准确 Miller 乘子为
$$
q_T^2=\frac{e^2}{\sqrt3}(x-e),\qquad
x_T=\frac{e(x+2e)}{x-e},\qquad
y_T=-\frac{3e^2y}{(x-e)^2}.
$$
逐项回乘给
$$
T_T^{12}B_{12}=q_T^4B_{12},\qquad
q_T^{-4}T_T^{390}f=B_{12}T_T^{378}F .
\tag{97}
$$
没有遗留 scalar。
特别原 whole 关系 (96) 等价于
$$
\boxed{\sum_Tq_T^4T_T^{378}F=\sqrt3F,}
$$
而所需的另一和式准确是
$$
\boxed{\sum_Tq_T^{-4}T_T^{390}f=B_{12}S_{378}F.}
\tag{98}
$$
两者的权方向不同。
确切 cocycle 为
$q_T^4(q_U^4\circ t_T)=-q_{T+U}^4$（$T\ne U$），
使 (97) 的加权 degree378 算子恢复 degree390 的 $+i$ 中心。
这明确支付了两个 degree 之间的相位差。

### 15.3 fourth 和式的全部两个来源

定义同一个实际 dyadic 伴随
$$
g=(U_1-1/\sqrt3)f .
$$
由上述 Pauli 乘法及 (96)，直接解得
$U_rf=f/\sqrt3+r g$。
在函数作用 $C_\omega f(z)=f(\omega z)$ 的规范下，
$C_\omega U_1=U_{\omega^2}C_\omega$，故
$C_\omega g=\omega^2g$。
$g$ 偶且在 $O$ 从 $z^2$ 起；不把它赋成新的 principal canonical。

坐标 $e=-r$，而
$$
\sum_{e^3=-1}q_e^{-4}
=\frac{9(1-2X)}{(X+1)^2},\qquad
\sum_{e^3=-1}e\,q_e^{-4}
=-\frac{9x(X-2)}{(X+1)^2}.
$$
因此实际第四费用的全部返回为
$$
\boxed{
\sum_Tq_T^{-4}T_T^{390}f
=\frac{9(1-2X)}{\sqrt3\,y^4}f
 +\frac{9x(X-2)}{y^4}g .
}
\tag{99}
$$
右边整体 whole 已由 (97) 支付。
第二项不能因为 $g$ 非 principal 而删除：
$xg$ 的整体 CM 型恰为 principal。
同样不能把其中任一非常数乘子移出中央读者。

其质量也完全可追。
若 $f=\sigma^{390}P_f(X)$，
实半点加法给
$g=9\cdot3^{-195/2}P_f'(-1)z^2+O(z^8)$。
从 (99) 得
$$
m_0(S_{378}F)=81\cdot3^{-195/2}P_f'(-1).
$$
故两个真正 degree378 dyadic 分量
$$
F_\pm=\frac12(F\pm S_{378}F/\sqrt3)
$$
准确满足
$$
\boxed{
S_{378}F_\pm=\pm\sqrt3F_\pm,\qquad
m_0(F_\pm)=\frac12\{c_6(f)\pm3^{-94}P_f'(-1)\}.
}
\tag{100}
$$
这不是对其五、十三标签的保留声明；
除去 $B_{12}$ 后必须重新支付该 degree 的完整算术谱。
也没有给 $F_\pm$ 或 (98) 新增中央零。

### 15.4 固定有理原函数及完整 P10 费用

(99) 的第一项系数有完整的固定 Hermite 身份。
令
$$
\mathscr W=\frac{9(1-2X)}{y^4},\qquad
\mathscr R=\frac{x(X+4)}{y^3}.
$$
直接使用
$$
D\frac{xP(X)}{y^3}
=\frac{(2-7X)P+6X(X+1)P'}{y^4}
$$
并取 $P=X+4$，得到
$$
\boxed{\mathscr W\,\omega_E=d\mathscr R+\omega_E.}
\tag{101}
$$
因此它并非一个可以在特征零删除的裸 exact；原全纯项为一。

在原同点 finite reader 中，对完整实际测试 $a$，
$DP_{10}=10GP_{10}+10\mathcal H^pZ^{p+9}$ 给
$$
\boxed{\begin{aligned}
C(P_{10}\mathscr W a\,\omega_E)
={}&C(P_{10}a\,\omega_E)
-C(P_{10}\mathscr R(D+10G)a\,\omega_E)\\
&-10\mathcal H Z\,C(Z^9\mathscr R a\,\omega_E).
\end{aligned}}
\tag{102}
$$
这保留原曲率和全部 $D a$。
用于原字时 $a$ 含整个 Miller、cut 和 Fourier 权，
所有函数必须按实际外部 pull 放到同一个点。
特别 (102) 不能替换 (99) 中真实的 $g$ 项。
任何对含 $\sqrt3$ 系数再施 Cartier 的步骤均保其半线性根，
不假定该常数被 Frobenius 固定。

(96) 是原算术假设已授权的 whole 行；
(98)–(102) 则将所需第四费用准确落到两条实际来源和确定连接项。
本节没有从这些不同的行之间跳过权差，也没有新增数学执行。

## 16. 实际二处分量 frame、完整物理回接与一个真实层间关系

本节仍读取 R1034 的同一个 $h_\chi(f)$。
不改变原特征零 flat 来源，不给它增加一个中央零，
也不以新 finite frame 替代该篇的完整物理矩阵。
新处是把二挠运输的 fourth 权放进一个完全指定的两分量 frame；
其两分量相依，且其原 $P_{10}$ 初始化可准确回接。

### 16.1 全部函数和初始化

在本节特征 $p$ 中置
$$
n=(p+5)/2<p,\qquad
Z_2=Z(2P),\quad G_2=G(2P),\quad
\widehat Z=Z_2/2,
$$
$$
v_2=\frac{X^2+20X-8}{(X+1)^2}
=\frac{8y(2P)}{y(P)},\qquad
K=2^{-n}(-y)^{-n}P_n(2P)v_2^{-p^2},
$$
$$
\boxed{
\mathbf P=\begin{pmatrix}P^{[0]}\\P^{[1]}\end{pmatrix}
=K\begin{pmatrix}x^p\\1\end{pmatrix}.
}
\tag{103}
$$
$P_n=-Z^p(D-nG)^{p-1}Z^{n-1}$ 是原指定有限模型，
没有另选一个同低 jet 的解。
$D\widehat Z=1$，且 $\widehat Z$ 对三个二挠平移严格不变。
原点有
$P^{[0]}=z^{10}(1+\cdots)$、
$P^{[1]}=z^{2p+10}(1+\cdots)$，
因为 $4n=2p+10$。
同时 $P^{[1]}=x^{-p}P^{[0]}$ 是完整全函数身份。

令
$$
\widehat G=\frac12G_2-\frac34r_0,\qquad
\widehat{\mathcal H}=\frac12\mathcal H(2P).
$$
所有 $p$ 次幂因子求导为零，原 $P_n$ 方程准确给
$$
\boxed{\begin{aligned}
D\mathbf P={}&10\widehat G\,\mathbf P+\mathbf E,\\
\mathbf E={}&2^{1-n}n(-y)^{-n}v_2^{-p^2}
 \mathcal H(2P)^p Z_2^{p+n-1}
 \begin{pmatrix}x^p\\1\end{pmatrix}.
\end{aligned}}
\tag{104}
$$
原 $D^{p-1}r_0=-r_0^p$ 又逐项给
$\widehat G^p+D^{p-1}\widehat G=\widehat{\mathcal H}^{\,p}$。
因此曲率并没有因换 frame 消失；(104) 是本节始终保留的实际曲率。

### 16.2 原二处 Pauli 矩阵的准确运输

对 $T=(e,0)$、$e^3=-1$，原 degree2 矩阵为
$$
q_T^2
\begin{pmatrix}x_T\\1\end{pmatrix}
=M_e\begin{pmatrix}x\\1\end{pmatrix},
\qquad
M_e=\frac1{\sqrt3}
\begin{pmatrix}-1&-2e\\e^2&1\end{pmatrix},
\qquad M_e^2=I .
$$
二倍图在 $T$ 下不变，而
$y_T=-q_T^{-4}y$、$v_{2,T}=-q_T^4v_2$。
记 $\varepsilon=(-1)^{n+1}$，逐项得到完整矩阵恒等
$$
\boxed{
\mathbf P(P+T)
=\varepsilon\,q_T^{\,10-4p^2}M_e^{(p)}\mathbf P(P).
}
\tag{105}
$$
矩阵上标表示逐项 Frobenius。
它包含整个 finite 初始化，不是只比较其 logarithmic 导数。

同时 $r_0(P+T)-r_0(P)=-(4/3)j_T$，故
$$
\widehat G(P+T)-\widehat G(P)=j_T .
$$
这项标量连接式不足以替代 (105)；
后者真正支付了完整原点初值和两分量运输。
选择 $v_2^{-p^2}$ 的方向也不可反：
它正好产生 $10-4p^2$，以匹配原 $\chi_\alpha$ 的 fourth 变权。
另有整个 CM 图上的准确身份
$
\boxed{
v_2(\alpha P)^{-1}\chi_\alpha(P)
=\frac{y(P)}{(2\alpha)^3y(2\alpha P)}
=\chi_{2\alpha}(P).
}
\tag{105a}
$
它由 $v_2=8y(2P)/y(P)$ 直接回乘，说明当前权真正对应整个
norm156 Jacobian；两分量保留了 $390/156=5/2$ 的二处费用。
(105a) 并未另宣称一个已付的新特征零 flat 来源；
本篇物理输入仍是原 $h_\chi$，其完整回接如下。

### 16.3 原 χ 译源的完整恒等及 source Cartier 顺序

写 $\mathcal A(f)=\mathcal T_{\alpha,\chi_\alpha^{p^2}}(f)$，
保持原全部未平均 trace、$R_\alpha^{10}$ 和原 Weyl 中心。
这是 R1034 实际特征零 $h_\chi$ 的约化。
对其中任一实际 target $h$，定义
$$
\boldsymbol\eta_b[h]
=\widehat Z^{-b-1}\mathbf P\,R_h\,\omega_E .
$$
若原 $T=r/2$、$Q=\alpha T$，令 $M_Q$ 使用这个**实际代表**
的 degree2 lift。
R1021 §13 已核 $Q$ 与标准代表 $\omega r/2$ 相差一枚负号，
所以若改用显示的标准点矩阵，它是 $M_Q=-M_{e_Q}$；
不能漏掉这项换代表相位。

完整 (89) 及 $\chi_\alpha$ 的 fourth 变权给
$$
\mathcal A(U_Tf)
=q_Q^{-4p^2}T_Q^{10}
  \mathcal A(q_T^{-4p^2}f).
$$
利用 $\widehat Z_Q=\widehat Z$ 和 (105)，准确化成
$$
\boxed{
\boldsymbol\eta_b[\mathcal A(U_Tf)]
=\varepsilon M_Q^{(p)}
 \tau_Q^*\boldsymbol\eta_b[
       \mathcal A(q_T^{-4p^2}f)] .
}
\tag{106}
$$
这里 $M_Q^{-1}=M_Q$。
在标准点矩阵的写法中，右边整体常数是 $-\varepsilon M_{e_Q}^{(p)}$。

这是整个实际字的恒等，没有先移走 Miller 或 cut。
在当前固定剩余扩张中，$M_Q$ 的系数属于 $\mathbf F_{p^2}$。
施两次 Cartier 后的准确常数为
$\varepsilon M_Q^{(1/p)}$，而不是任意将它改成原矩阵。
原 whole $S_{390}f=\sqrt3f$ 可在 (106) 左边直接求和。

必须保 source 端顺序：$q_T^{-4p^2}$ 经两次 Cartier 后，
是在完整 source trace **内部**乘 $q_T^{-4}$。
它乘的是原曲率和全部测试已经进入后的 source 微分；
不能把它提前换成
$q_T^{-4}U_Tf$，也不能立即套 (98) 的原 degree378 来源。
$\mathcal A(q_T^{-4p^2}f)$ 在此仅是一个明确亚纯代数输入，
未被赋予新的原中央零。
(106) 真正去掉的是 target 端未付的任意运输参数，
不是将 source Cartier 与 fourth 费用认成可交换。

### 16.4 回到同一个完整物理矩阵

此处的改变必须支付特征零读者。
沿 R1034 (19)，给 $Z,G,P_n$ 取同一指定有理整 lift，
$n$ 取当前这个整数；固定有理 $x,y,v_2$ 不变。
由 (103) 定义 $\widetilde{\mathbf P},\widetilde{\widehat Z}$。
在原好参数 $u=x^{-1/2}$ 上，
$$
\widetilde{\widehat Z}=u\times\mathcal O[[u^6]]^\times,\quad
\widetilde P^{[0]}=u^{10}\times\mathcal O[[u^6]]^\times,\quad
\widetilde P^{[1]}=u^{2p+10}\times\mathcal O[[u^6]]^\times .
$$
原有限算子的首系数模 $p$ 为一，所以这里的单位是真实单位。
所有正负整数幂均整；未把一个特征零 $p^2$ 次幂只按 Frobenius 处理。

设 $\ell_0=0,\ell_1=2p$。
对同一个原整 $A_\chi$，定义
$$
\tau^{[i]}_m=[T^m](\widetilde P^{[i]}A_\chi)(P(T)),
\qquad T=\widetilde{\widehat Z}(P),
$$
$$
\boxed{
\widehat M^{[i]}_{h,m}
=[z^{(p+1)h}]
  \frac{(\sigma^\circ)^{10}}{\widetilde P^{[i]}}
  \widetilde{\widehat Z}^{\,m},\qquad
g_h=\sum_{m\le(p+1)h+\ell_i}
       \widehat M^{[i]}_{h,m}\tau^{[i]}_m .
}
\tag{107}
$$
$\tau^{[i]}_m$ 全整，并从 $m\ge\ell_i+6$ 起。
第二个分量是同一来源的另一读取，不增加独立必要零。
当 $H\le2p-5$ 时，两种实际 native 指标仍都小于 $2p^2$。

还可明确锁定与原 $P_{10}/Z$ 的完整转换。
在 $T=\widetilde{\widehat Z}$ 上置
$$
\psi(T)=\widetilde Z(P(T)),\qquad
R(T)=\widetilde P^{[0]}/\widetilde P_{10}.
$$
二者分别是整参数和整单位。
矩阵
$B_{mn}=[T^m]R(T)\psi(T)^n$
因而为有整逆的下三角矩阵，其对角均为单位。
准确有
$$
\boxed{\boldsymbol\tau^{[0]}=B\boldsymbol\tau,\qquad
       \widehat M^{[0]}B=M.}
\tag{108}
$$
这不是只约化的关系：所有实际高位、原 $\Xi$ 初始化、
R616/R619 两坏带和低回填都由同一原 $M$ 回接。
原 Newton 权及 R1034 的 $p^H$ 全尾继续作用于同一个 $g_h$。

为核分母，把 (107) 逐项写成
$z^{m-\ell_i+6j}U_\sigma^{10}
 W_0^{5-(m-\ell_i)/2-3j}$。
实际角色只留整数指数，且 $m\ge\ell_i+6$。
R614/R616/R619 原同一个坏因子计数因此逐项适用；
在本篇实际范围 $p^2\widehat M^{[i]}$ 整。
不能把 $v_2^{-p^2}$ 在特征零低位的费用删掉。

第一个实际耦合也可核定。原整窗口给
$$
\widehat Z=z-16\kappa_5z^{5p}+O(z^{11p}).
$$
到相对 $5p-1$ 以前，
$(\sigma^\circ)^{10}/P^{[0]}$ 仅有原整 Gaussian 的
$(p+1)$ 倍次项；其它首差从 $6p$ 起。
因此对第一分量 $m=p^2+b$、$b\equiv5\pmod6$，准确有
$$
\boxed{
\widehat M^{[0]}_{h,p^2+b}\equiv0\ (p\le h\le p+3),\qquad
\widehat M^{[0]}_{p+4,p^2+5}\equiv-80\kappa_5,
}
\tag{109}
$$
且同一 $h=p+4$ 的其余 $b\ge11$ 项为零。
这里的单位属于新矩阵，未与原 $-5\kappa_5$ 冒认相同。
所用 Gaussian 只在该有限窗截取，阶乘仍为单位。

### 16.5 固定支撑、真实伴随和两分量的不同角型

$P^{[i]}$ 在原三个二挠点至少 $4p^2$ 阶零。
$\widehat Z$ 的这些零点为 simple；
其它 $\widehat Z$ 零点由原 $P_n(2P)$ 的 $Z_2^p$ 因子
消掉全部 $b<p$ 的 cut。
所以未施伴随的 whole canonical 输入只剩 $O$ 和
$E[4]\setminus E[2]$ 的极。
后者共12点，是两个自由 $\mu_6$ 轨道。

在这12点，完整帽为
$$
\operatorname{pole}\boldsymbol\eta_b
\le p^3+(n-b-2)p+1 .
\tag{110}
$$
第三 Cartier 因而至多 double。
在真正 $r=p$ 的物理页，
第一分量要求 $b\equiv5$，第二分量要求 $b\equiv3\pmod6$；
两种对应输入的第三层都为型 $5$。
原点无留数，二挠点没有极，型 $5$ 又排除全纯 $\omega_E$。
因此每个这样的**实际分量**第三层在两个轨道上至多四个坐标。
不能把同一个 $b$ 下另一分量的不同 CM 型删掉。

原一阶 transpose 在真正同点时准确简化为
$$
\boxed{
\widehat Q^\dagger
=-2y(D+10\widehat G)-15x^2
=-2y(D+5G_2).
}
\tag{111}
$$
它对普通二挠 pull 满足
$\tau_T^*\widehat Q^\dagger(\tau_T^*)^{-1}
=-q_T^{-4}\widehat Q^\dagger$。
但原第 $i$ 字的真实 $x_i,y_i$ 在 $P-R_i$，
故完整公式仍是
$$
\widehat Q_i^\dagger a_i
=-2y_i(D+5G_2)a_i
 +15y_i(r_0-r_{0,i})a_i .
$$
末项等于 $5y_iD\log(y/y_i)a_i$；
在固定平方根扩张上可用 $(y/y_i)^{5/2}$ 作准确 gauge，
却不能因此改变原 source 的归一或删掉整个 Miller/test。
曲率项始终是 (104) 对应的
$-C(2y_i a_i\mathbf E\,U_i\omega_E)$。

在原12点，一次真实伴随的上界为
$p^3+p^2+(n-b-3)p<2p^3$，第三层仍至多 double。
移动 $R_i$、原 Miller 的表面极和其它完整字支撑
还须按原顺序合并或逐项保留；
(110) 的四坐标结论不预先授给这些未合并的分拆项。
同点固定 cover $r^2=y$ 上
$y^{-5/2}U_A=D(2x/r)$，
正与 (111) 成对偶，但不删除 $G_2$ 或 (104)。

### 16.6 一个实际第二层标量只读原第一 primitive

两分量的关系还能真正消去一个高层自由量。
令 $\nu_{1,i}=C\eta_i$、
$\nu_{2,i}=C^2\eta_i$，
$c^\sharp_i=(\nu_{2,i}/\omega_E)(O)$；
本段使用上述物理 $r=p$ 页，原点留数为零。
由 $P^{[1]}=x^{-p}P^{[0]}$，严格有
$$
\nu_{2,1}=C(x^{-1}\nu_{1,0}).
$$
仍用 R1020 的同一个
$\varphi_*=\varphi-dJ_{p-6}$，
它在 $\widehat Z$ 中从 $p-1$ 阶起，
$C\varphi_*=\omega_E$。
写原唯一 primitive 类
$\nu_{1,0}=dK_{b,0}+f_{2,0}^p\varphi_*$。
又令
$x^{-1}=\sum_{j\ge0}a_j\widehat Z^{2+6j}$，
其中 $a_0=1$，所用次数全部严格小于 $p$。

$x^{-1}$ 的二阶零使
$x^{-1}f_{2,0}^p\varphi_*$ 从 $p+1$ 阶起，
故它完全不进入以下真实槽：
$$
\boxed{
(c^\sharp_1)^p
=\sum_{j=0}^{s-1}
 a_j(p-2-6j)
 [\widehat Z^{\,p-2-6j}]K_{b,0}.
}
\tag{112}
$$
右边仅含 $p-2,p-8,\ldots,3$ 的原第一 primitive 系数，
没有一个新的任选高层 scalar。
这些系数的指数均非 $p$ 倍数，所以不受 $F^p$ 代表歧义影响。
在第二分量实际 $b\equiv3$ 页，(112) 是非空的真实返回；
不能把它与第一分量的 $b\equiv5$ scalar 混为同一项。

本节由 (107)–(108) 保留全部物理精度。
(106)、(111)、(112) 给的是原两条 canonical 的同一完整测试关系；
它们仍须连同原所有低行、(104) 曲率、实际 source Cartier
和十三字一起使用，未声称已经迫出新的非零中央值。
没有新增数学执行。

## 17. 二倍 sigma 的完整字规范、二挠不变的真实平坦返回与四挠边界的一条整关系

日期：2026-11-27。本节继续使用 (103)–(112) 的同一 $\alpha=\delta\pi$、同一原 Gaussian 与原物理矩阵。以下平坦返回由特征零的实际有理函数构造，不由改写有限 frame 宣称存在。它使原二挠来源的完整恒等式在**同一个目标函数**上成立；没有给它的任意有理倍数赋中央零。

### 17.1 全部原字中的二倍 sigma 与平方根规范

在固定有限扩域与固定覆盖 $r^2=y$ 上保留原 Weyl 函数
$q_R(P)=e^{-\eta(R)(z+R/2)}\sigma(z+R)/\sigma(z)$。
由原 $\sigma(2z)=-2y(z)\sigma(z)^4$ 和 $\eta(2R)=2\eta(R)$，完整有
$$
q_{2R}(2P)=\frac{y(P+R)}{y(P)}q_R(P)^4,
\qquad
q_R(P)^{10}=q_{2R}(2P)^{5/2}
 \left(\frac{y(P)}{y(P+R)}\right)^{5/2}.
\tag{113}
$$
右侧的平方根以第一式及原 $q_R$ 定义：
$q_{2R}(2P)^{1/2}=q_R(P)^2r(P+R)/r(P)$。
因此它没有一个可自由改变的符号或 Weyl 相位。

令 $n=(p+5)/2$。对 (26)–(27) 的每一个实际字，准确地
$$
y(P)^{-n}q_R(P)^{10}U(P+R)
=r(P)^{-p}q_{2R}(2P)^{5/2}
 \bigl[y(P+R)^{-5/2}U(P+R)\bigr].
\tag{114}
$$
其中两条实际低层输入变为
$$
y^{-5/2}U_A=D\left(\frac{2x}{r}\right),\qquad
y^{-5/2}U_B=\frac{x}{r^3}.
$$
在原 source 坐标中使用 $P\mapsto\alpha P$ 时，导数仍乘原来的 $\alpha$；(114) 没有重置这个尺度。所有外部 $g$、Miller、cut 与移动 $R_i$ 继续乘在整个右侧。特别是第一式为裸有理函数的 exact，不意味着乘上原 $P$、外权后仍为 exact。

原字标签在倍乘后为 $(s',i')=(-s,2i\bmod13)$。因为
$\chi_6(2)=-1$、$-\chi_{10}(2)^{-1}=\omega$，完整 profile 分别满足
$$
s\chi_6(i)=s'\chi_6(i'),\qquad
s\chi_{10}(i)=\omega\,s'\chi_{10}(i').
\tag{115}
$$
(113)–(115) 始终使用实际中心 $2R$。若将它改为一个标准代表，必须同时施行由原 $q_R$ 确定的二进矩阵；半整数次数的表达不能把这个代表差当成一个任意标量，更不能将其当成新的 canonical 来源。

### 17.2 在原二挠平移下真正不变的平坦权

置
$$
w(P)=\chi_\alpha(2P)
=\frac{y(2P)}{\alpha^3y(2\alpha P)}.
\tag{116}
$$
它在原点为 $1+O(z^6)$，在每个非零 $\ker\alpha$ 点为准确三阶零，并对每个 $T\in E[2]$ 满足
$w(P+T)=w(P)$。其全部简单极是
$[2\alpha]^{-1}(E[2]\setminus\{O\})\setminus[2]^{-1}(E[2]\setminus\{O\})$；
共有 $456$ 个，沿 $[\alpha]$ 映到十二个 $E[4]\setminus E[2]$ 点。被减去的十二个点处分子、分母同时简单消失，比值为单位；原 $E[2]$ 处则 $w=1$。这也逐点支付了 (116) 的支撑。

取 R1034 的任一
$H=2p-11$ 或 $2p-5$，令
$N=H(p+1)$、$k=N/6$、$a=p^2-k$，并使用已定义的原截断
$$
V_w=w^a B_{a,k}(w),\qquad
B_{a,k}(T)=\sum_{j=0}^k(-1)^j\binom{a+j-1}{j}(T-1)^j.
\tag{117}
$$
由于 $a+k=p^2$，完整有
$$
V_w=1+O(z^{N+6}),\qquad
\operatorname{ord}_{T}V_w\ge3a>N+1\quad(0\ne T\in\ker\alpha),
\qquad
\overline V_w=w^{p^2}.
\tag{118}
$$
最后一个等号只在特征 $p$ 中使用；特征零的全部高位继续采用 (117)。

用原未平均的全 $\alpha$ 迹定义
$$
h_w(f)=\sigma^{10}\alpha^{-10}
 \operatorname{Tr}_{[\alpha]}
 \left(V_w\,\frac{R_f}{R_\alpha^{10}}\right),
\qquad f=\sigma^{390}R_f .
\tag{119}
$$
同 R1034 的整条纤维展开给
$h_w(f)(\alpha z)-f(z)=O(z^{N+1})$。
每个新极在目标 $E[4]\setminus E[2]$ 的阶至多 $p^2$。其余有限点没有极，原点首阶与 $f$ 相同；对当前两条 canonical 及其二挠译源，质量为零且首阶至少二。对未平移的 principal 来源首阶至少六。

具体地，记 $B_2=X^2+20X-8$。未平移的整个目标可写为
$$
h_w(f)=\sigma^{10}A_w,\qquad
A_w=\frac{x^2P_w(X)}{B_2(X)^{p^2}},\quad
P_w\in\mathcal O_p[X],\quad\deg P_w\le2p^2.
\tag{120}
$$
整性直接来自原固定好位模型上的整有理函数、整数截断系数及度 $39$ 的整迹；$B_2$ 的判别式为 $432$，没有新增随 $p$ 变化的坏分母。用原 $u=x^{-1/2}$ 展开，(120) 是 $u^{-4}$ 乘一个整的 $u^6$ 级数。因此 R1034 §5 的完整 Hurwitz 尾、两条坏带及原 Newton 重构原样适用，准确给
$$
j_{390,f}-j_{10,h_w(f)}\in p^H\mathcal O_p .
\tag{121}
$$
这里已使用两边质量零；一般质量的 $\log q_\alpha$ 项仍按 R1034 保留。

### 17.3 同一个目标上的真实二挠恒等式

(116)–(117) 在特征零已经对 $E[2]$ 不变，所以原全迹与真实 Weyl 算子严格满足
$$
h_w(T_T^{390}f)=T_{\alpha T}^{10}h_w(f).
\tag{122}
$$
这里没有 R1034 的 $W(P-T)/W(P)$ 剩余权。完整 $\mu_6$ 投影亦与 (119) 交换。

由本篇 §13、§15 已付的原 source 身份，(122) 给
$$
\Pi_0T_{\alpha T}^{10}h_w=\frac1{\sqrt3}h_w,\qquad
\sum_{0\ne T\in E[2]}T_{\alpha T}^{10}h_w=\sqrt3\,h_w.
\tag{123}
$$
仍使用 §13 的实际代表：$\alpha T$ 与对应标准半周期的 degree-$10$ Weyl 算子相差负号。因此若
$S_{10}$ 是三个**标准**二挠算子的和，则整个目标准确满足
$$
\boxed{S_{10}h_w=-\sqrt3\,h_w,\qquad
 \Pi_0T_{T'}^{10}h_w=-h_w/\sqrt3.}
\tag{124}
$$
这不是只比较原点的质量。相应的实际 translated 中央读数也由 (121) 与 (122) 在同一精度内返回原 canonical 条件，但它们仍由原来源身份关联，未被计成四条独立的中央零行。

### 17.4 与原 $M$、原 $\chi_\alpha$ 及两个有限 frame 的全部回接

在 (103) 去掉 $v_2^{-p^2}$，记
$$
K_0=2^{-n}(-y)^{-n}P_n(2P),\qquad
\mathbf P_0=K_0(x^p,1)^{\mathsf t},\qquad
\widehat Z=Z(2P)/2.
\tag{125}
$$
它仍具有原点首阶 $10,2p+10$。它的特征零整 lift 由原同一 $\widetilde P_n$ 构造。在 (107)–(108) 中以该 lift 取代原 $\widetilde{\mathbf P}$，仍得到整可逆的三角变换 $\tau^{[0]}=B_0\tau$ 及
$\widehat M^{[0]}B_0=M$。因此 (121) 用的是原物理 $g_h$；两个原坏带、全部 Gaussian、原 $\Xi$ 与新四挠极都在这条准确矩阵关系中，不能用 $\mathbf P_0$ 的模 $p$ 恒等式删除高位费用。

此外有完整函数等式
$$
w=\chi_\alpha\,\frac{v_2(P)}{v_2(\alpha P)}.
$$
故对全模 $p$ 迹，
$$
A_w(f)=v_2^{-p^2}\mathcal A(v_2^{p^2}f),\qquad
\boxed{\widehat Z^{-b-1}\mathbf P_0 A_w(f)\omega_E
=\widehat Z^{-b-1}\mathbf P\,\mathcal A(v_2^{p^2}f)\omega_E.}
\tag{126}
$$
$\mathcal A$ 是 (106) 的原 $\chi_\alpha^{p^2}$ 迹，此处仅将其作为全亚纯迹使用。右侧的 $v_2^{p^2}f$ 没有被赋中央零。两次 Cartier 后，$v_2$ 只能在原 source 的完整 $C^2$ 微分中提出；不能把 (126) 简写为对裸 $f$ 乘 $v_2$ 的新中央条件。虽然 $v_2y=8y(2P)$，同样不能把未取 $p^2$ 次的 $y$ 穿过 $C^2$。

### 17.5 完整 Pauli 关系与第一分量的真正 $[2]$ 迹零

沿用 (105) 的 $M_e$ 及 $\varepsilon=(-1)^{n+1}$。现在没有 $v_2$ 的第四费用，准确有
$$
(\mathbf P_0)_T=\varepsilon q_T^{10}M_e^{(p)}\mathbf P_0.
$$
对整个目标置
$\boldsymbol\eta_b=\widehat Z^{-b-1}\mathbf P_0 A_w\omega_E$。
由 (124) 及 $\widehat Z_T=\widehat Z$ 得全微分恒等式
$$
\boxed{\sum_{T\ne0}\varepsilon M_e^{(p)}
                  \tau_T^*\boldsymbol\eta_b
=-\sqrt3\,\boldsymbol\eta_b.}
\tag{127}
$$
矩阵顺序与 (105) 相同；不是将 Weyl 算子乘法顺序误搬到列函数矩阵。

现在对 $E[2]$ 取未平均迹。因为
$\sum M_e^{(p)}=\operatorname{diag}(-(\sqrt3)^p,(\sqrt3)^p)$，
而对 $p\equiv5\bmod6$ 有
$\varepsilon(\sqrt3)^p=-\sqrt3$，(127) 的第一分量严格给
$$
\boxed{\operatorname{Tr}_{[2]}\eta_{b,0}=0,\qquad
       \operatorname{Tr}_{[2]}C^j\eta_{b,0}=0\quad(j\ge0).}
\tag{128}
$$
第二式使用 Cartier 与可分有限迹的交换，所有常数依原半线性取根。这里并未给第二分量的迹赋零。

### 17.6 实际 $r=p,b=5$ 页的四个边界系数

对整个未平移 canonical 输入，在目标 $E[2]$ 有
$\operatorname{ord}A_w\ge2$。这是由 (123) 的质量零与译源偶性得到的真实二阶消失；$\mathbf P_0$ 在这些点正则，$\widehat Z$ 为一阶零。因此 $\eta_{5,i}$ 在这些点极阶至多四。其局部系数为偶函数，留数为零，第一 Cartier 已消去整个极。原点亦正则；其他 $\widehat Z$ 零点仍由原 $P_n(2P)$ 的完整 $Z(2P)^p$ 因子支付。

在十二个 $E[4]\setminus E[2]$ 点，整个微分的极帽为
$$
d_{E[4]}(\eta_{b,i})\le p^3+(n-b-2)p+1<2p^3.
\tag{129}
$$
这与 (110) 的真实费用相同：旧 frame 的 $v_2^{-p^2}$ 极已由 (120) 的新实际目标极替代。于是第三 Cartier 至多有二阶极。第一分量在当前页的真实 $\mu_6$ 型为五，故准确写成
$$
C^3\eta_{5,0}
=\frac{xP_3(X)}{B_2(X)^2}\omega_E,\qquad
P_3=p_0+p_1X+p_2X^2+p_3X^3.
\tag{130}
$$
第二分量型为一，可能含全纯 $\omega_E$；本节没有将它删掉。逐字分裂后的移动 $R_i$ 和 Miller 极也不能套用整个输入的 (129)。

下式是完整有理迹，不是单点拟合：
$$
\operatorname{Tr}_{[2]}
 \left(\frac{xP_3(X)}{B_2(X)^2}\omega_E\right)
=\frac1{16}
 \operatorname{Tr}_{K[X]/(B_2)/K}
 \left(\frac{P_3(X)}{(X-8)(X+1)^2}\right)
 \frac{x}{y^2}\omega_E .
\tag{131}
$$
确切常数可在目标 $(-1,0)$ 核定。其四个原像有
$x=-1\pm\sqrt3$，每个配两个 $y$ 符号，且
$y_{\rm down}=B_2/(8y^3)$、$\omega_{\rm up}=dy_{\rm down}/(6x_{\rm down}^2)=(1/6+O(y_{\rm down}^2))dy_{\rm down}$。
因此双极系数为
$-\frac1{48}\operatorname{Tr}(P_3/((X-8)(X+1)^2))$；
目标 $x\omega_E/y^2$ 的双极系数为 $-1/3$，给出 $1/16$。
迹的型及支撑将整个返回限制在这一条线上，故该常数确定全式。

模 $B_2$ 写 $P_3=a+bX$，则
$(X-8)(X+1)^2=27(19X-8)$，且
$$
\operatorname{Tr}\frac{a+bX}{27(19X-8)}
=-\frac{11a+4b}{162}.
$$
再以 $X^2=-20X+8$、$X^3=408X-160$ 返回四个原系数，(128)–(131) 严格给
$$
\boxed{11p_0+4p_1+8p_2-128p_3=0.}
\tag{132}
$$
该整关系在所有当前目标好位成立，无新增变化分母。它排掉第一分量的一个真实四挠边界方向；其他三个方向、第二分量的全纯项、原 (112) 的第一 primitive 卷积及整个物理 $M$ 均继续保留。(132) 本身不被升级成原中央矛盾。

## 18. 同一个实际双分量读者的二挠端点与完整四挠槽

本节仅使用 §17 的真实 $h_w$，以及同一个 $b=5$ 输入
$\boldsymbol\eta_5$。第二分量在此处也取 $b=5$；不能将它与 (112) 所涉第二分量自身的 $b=3$ 物理页混同。

### 18.1 高层实际标量返回三个二挠点

记
$$
\nu_i=C^2\eta_{5,i},\qquad
c=\frac{\nu_0}{\omega_E}(O),\qquad
c^{p^2}=\tau_{p^2+5}^{[0]} .
\tag{133}
$$
最后一式是原 Cartier 系数规则，使用 (125) 的实际有限 frame。它并未将原物理矩阵替成恒等矩阵。

(129) 给 $\nu_i$ 在十二个四挠点的极阶至多 $p+1$，而 §17.6 已付它们在 $O$ 与全部 $E[2]$ 正则。当前两分量的真实 $\mu_6$ 型分别是一、五。所以
$\nu_1/\omega_E(O)=0$；若 $T_r=(-r,0)$、$r\in\mu_3$，存在 $a,b$ 使
$$
\frac{\nu_0}{\omega_E}(T_r)=a,\qquad
\frac{\nu_1}{\omega_E}(T_r)=rb .
$$
(128) 在下点 $O$ 给 $c+3a=0$。对 (127) 取两次 Cartier 后，其常数仍为
$\varepsilon M_e^{(p)}$ 与 $-\sqrt3$；在 $O$ 读第一行，利用
$e=-r$、$e^p=-r^{-1}$、$\varepsilon/(\sqrt3)^p=-1/\sqrt3$，准确得到
$a-2b=-c$。因此
$$
\boxed{
\frac{\nu_0}{\omega_E}(T_r)=-\frac c3,\qquad
\frac{\nu_1}{\omega_E}(T_r)=\frac{rc}{3}\quad(r\in\mu_3).
}
\tag{134}
$$
这条端点关系来自整个实际 trace、有限 frame 与原 Pauli 相位，不是把 source 的标量直接搬到一个改变了权的 target。它同时保留 $c$ 的真实物理入口 (133)。

### 18.2 两个完整多项式及其全部 Cartier 槽

存在准确多项式 $\mathcal Q_w,\mathcal R_w$，使
$$
\nu_0=\frac{\mathcal Q_w(X)}{B_2(X)^{p+1}}\omega_E,\qquad
\nu_1=\frac{x\mathcal R_w(X)}{B_2(X)^{p+1}}\omega_E,
\quad
\deg\mathcal Q_w\le2p+2,\quad \deg\mathcal R_w\le2p+1.
\tag{135}
$$
这是全局支撑、CM 型与原点正则性给出的整个返回，不仅是某个核点的余式。$c=[X^{2p+2}]\mathcal Q_w$。
由于 $B_2(-1)=-27$ 且 $(-27)^{p+1}=729$，(134) 精确化为
$$
\boxed{\mathcal Q_w(-1)=\mathcal R_w(-1)
       =-243[X^{2p+2}]\mathcal Q_w.}
\tag{136}
$$

写 $m=(p-1)/2=3s-1$，并定义原完整多项式
$$
F_Q=\mathcal Q_w(X)(X+1)^mB_2(X)^{p-1},\qquad
F_R=\mathcal R_w(X)(X+1)^mB_2(X)^{p-1}.
$$
逐一保留所有 $x^{kp-1}dx$ 槽的 hyperelliptic Cartier 公式给
$$
C\nu_0=\frac{x}{B_2^2}
 \sum_{j=0}^3
 [X^{(6j+4)s-j-1}]F_Q^{\, [1/p]}\,X^j\,\omega_E,
\tag{137}
$$
$$
C\nu_1=\frac1{B_2^2}
 \sum_{j=0}^4
 [X^{(6j+2)s-j-1}]F_R^{\, [1/p]}\,X^j\,\omega_E.
\tag{138}
$$
这里 $[X^d]F^{[1/p]}$ 表示先取整个实际系数 $[X^d]F$，再取它的 $p$ 次根；不是对多项式变量取根。等价地，第一行的四槽依次为
$4s-1,10s-2,16s-3,22s-4$；第二行五槽为
$2s-1,8s-2,14s-3,20s-4,26s-5$。

为核全槽范围，将 (135) 第一式写成
$(yB_2^2)^{-p}F_Q\,dx/2$。
$\deg_XF_Q\le(9p-1)/2$，只有 $k=2,5,8,11$ 满足
$kp-1\equiv0\bmod3$ 并位于该次数帽内。第二式相应为
$(yB_2^2)^{-p}xF_R\,dx/2$，只有 $k=1,4,7,10,13$。
这证明没有遗漏末端槽或全纯项。由 (132)，第一行四个原系数还准确满足
$$
11[X^{4s-1}]F_Q+4[X^{10s-2}]F_Q
+8[X^{16s-3}]F_Q-128[X^{22s-4}]F_Q=0.
\tag{139}
$$

### 18.3 两个分量的整个边界关系

令 $\mu_i=C\nu_i$。对 (127) 再取 Cartier，并用
$\varepsilon(\sqrt3)^p=-\sqrt3$，完整向量满足
$\sum M_e\tau_T^*(\mu_0,\mu_1)^{\mathsf t}
=\sqrt3(\mu_0,\mu_1)^{\mathsf t}$。
因此存在两个实际标量 $A,B$，使
$$
\boxed{
\mu_1=\frac14\sum_{T_r\ne0}r^2\,\tau_{T_r}^*\mu_0
  +A\,\omega_E+B\,\frac{(X+1)^3}{B_2(X)^2}\omega_E.
}
\tag{140}
$$
证明只用原四元平移代数：记
$D_1=\sum e\tau_T^*$、$D_2=\sum e^2\tau_T^*$。
在迹零子空间上有
$D_1D_2=-4$、$\sum\tau_T^*=-1$，
所以 $\mu_1-\frac14D_2\mu_0$ 为 $E[2]$ 不变微分。
它的型为一，极只在十二个四挠点且至多二阶。下降后准确属于
$\langle\omega_E,\omega_E/y^2\rangle$；
拉回第二基为 $128(X+1)^3\omega_E/B_2^2$，固定常数吸收到 $B$。
第一分量的三个剩余边界方向，以及 (140) 中两个标量，均未被赋零。

最后，§15 的实际
$\mathscr R=x(X+4)/y^3$ 满足
$D\mathscr R=-v_2$，因为
$v_2=1-\sum_{T\ne0}q_T^{-4}=8y(2P)/y(P)$。
于是原完整一阶算子准确有
$$
[Q_1,\mathscr R]=-16y(2P),\qquad
[\widehat Q^\dagger,\mathscr R]=16y(2P).
\tag{141}
$$
这是真正下降到 $[2]$ 底曲线的乘子；但 (126) 中未取 $p^2$ 次的因子仍不得穿过 Cartier。后继联立须使用 (133)–(140) 的同一实际多项式、完整物理矩阵与曲率，不能仅凭 (141) 为任意测试赋中央零。
