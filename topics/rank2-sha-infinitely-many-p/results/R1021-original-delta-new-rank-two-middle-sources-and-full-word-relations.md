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
