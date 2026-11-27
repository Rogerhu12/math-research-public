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
