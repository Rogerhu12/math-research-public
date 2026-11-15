# 原中央剪切的一阶项与固定表示返回的准确门槛

日期：2026-11-15。**状态：下列同一测度上的解析变分、完整 moving 权/质量项、固定有限 theta cover 的周期差，以及固定 Katz 函数的条件判据均已证明。没有证明原中央零会使剪切的一阶负矩为零；没有把物理剪切识别成同一个自守表示中的自由 test-vector 变化。**

本文接 [R754](../results/R754-original-finite-inertia-shares-and-etale-source-trace.md) 的实际有限门。目标仍是原 $S_{34},T_{72},U_{136}$，不把 $S_{34}$ 的六维型零空间与另两种线丛混同。所说中央平方分别来自 [R295](../results/R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)、[R397](../results/R397-e24-original-ordinary-square-and-full-selmer-bridge.md)、[R469](../results/R469-e2312-full-weight-square-ordinary-inert-sha-bridges.md)。

## 1. 同一完整来源和一个真实 unitary 参数

固定一个已允许的普通素数 $p$，以及原有界联合测度 $\mu$。所有原伙伴、有限角分支、实际 prime-core 归一及来源常数都包含在 $\mu$ 和下面的权中。先在同一原 $p$ 整格上工作，不忘任何伙伴。

令 $Y,Z$ 为两个正交实际线性观察，Hermitian 范数为
$$
\langle Y,Y\rangle=N,\qquad
\langle Z,Z\rangle=M,\qquad
\langle Y,Z\rangle=0,\qquad r=M/N .
\tag{1}
$$
$N$ 可以是34、72、136；一般 $M$ 不等于 $N$。本节只要求原固定分母在所用 $p$ 处是单位。沿一个共轭固定的有理参数方向定义
$$
a(u)=\frac{1-ru^2/4}{1+ru^2/4},\qquad
b(u)=\frac{u}{1+ru^2/4},
$$
$$
Y_u=a(u)Y+b(u)Z,\qquad
Z_u=-r b(u)Y+a(u)Z .
\tag{2}
$$
准确有 $a(u)^2+r b(u)^2=1$，所以 (2) 保持完整 Gram 矩阵，且
$$
Y_0=Y,\qquad \dot Y_0=Z,\qquad
Z_0=Z,\qquad \dot Z_0=-rY .
\tag{3}
$$
这是实际单位ary小剪切，不以仅有相同范数的另一个来源代替原来源。对有理 $u$ 清分母后的整 theta 轴，其 cover 随 $u$ 而变；范数保持不等于所有 $u$ 已经落在同一个固定整 theta 模中。

令 $\mathcal C$ 是原有限门的交集，包括伙伴深度门和所需的浅层单位门。取足够大的整数 $M_0$，使 (2) 的所有矩阵元在 $u\in p^{M_0}\mathbf Z_p$ 上与原矩阵模各门的模数相同。于是同一 $p$ 整支撑上的每一个有限指示函数严格不变。若原格经过一个固定伸缩，先把这个伸缩所需的额外 $p$ 幂计入 $M_0$。

特别，
$$
1_{Y_u\in\mathbf Z_p^\times}=1_{Y\in\mathbf Z_p^\times}.
\tag{4}
$$
任何固定有限乘法角色或加性 Fourier 门，在同样缩小的参数盘上也逐点不变。这一步只固定真实有限门，不声称能同时冻结无限层门或不同 core-word 的像格。

允许有限正多项式权随参数移动，记为 $f_u$。它包括全部原伙伴和实际门 $\mathcal C$；在参数盘上，指示部分已固定，而正多项式部分及已付的有限归一因子解析地变化。写
$$
f=f_0,\qquad \dot f=\left.\partial_u f_u\right|_{u=0}.
\tag{5}
$$
若要求只改变观察而不改变权，就取 $f_u=f$。两种约定在下面明确区分。

## 2. 完整单位 Mellin 变分，包括质量和尺度

令 $d_p=p-1$。先取固定有限角色 $\chi$，并定义实际两变量函数
$$
\mathscr M(u,s)=
\int_{Y\in\mathbf Z_p^\times}
 \chi(Y)\langle Y_u\rangle^{d_p s}f_u\,d\mu .
\tag{6}
$$
(4) 保证它确实是原剪切观察的单位域积分。在原参数盘和 $s\in\mathbf Z_p$ 上，
$\log\langle Y_u\rangle$ 一致收敛；有界测度与有限解析权允许逐项微分。

更一般地，若原观察还带一个已显示的解析单位尺度 $c(u)$，$c(0)=1$，令
$$
\dot Y_0=\alpha Y+Z,\qquad \alpha=c'(0).
$$
式 (2) 的纯 unitary 规范是 $\alpha=0$。定义
$$
\mathscr M_f(s)=
\int_{Y^\times}\chi(Y)\langle Y\rangle^{d_p s}f\,d\mu ,
$$
$$
\mathscr M_{\dot f}(s)=
\int_{Y^\times}\chi(Y)\langle Y\rangle^{d_p s}\dot f\,d\mu .
\tag{7}
$$
于是准确有
$$
\boxed{
\partial_u\mathscr M(0,s)
=\mathscr M_{\dot f}(s)
 +d_p s\left[
 \alpha\mathscr M_f(s)+
 \int_{Y^\times}\chi(Y)\langle Y\rangle^{d_p s}
          \frac ZY f\,d\mu\right].
}
\tag{8}
$$
有限角色的导数为零；它并没有被删除，而是在这个参数盘上严格局部常数。

在原共同 ordinary 周期 $\Omega_p$ 下，定义真实第一来源
$$
\nu_D=\Omega_p^{-1}Y_*(Zf\mu),\qquad
I_D(\chi,s)=
\int_{\mathbf Z_p^\times}
x^{-1}\chi(x)\langle x\rangle^{d_p s}\,d\nu_D(x).
\tag{9}
$$
若某个已付正交 theta 分裂使 $D$ 成为实际标准截面，(9) 就是该截面的原单位负一矩；否则 (9) 仍只是已定义的同源推前，不能先套曲线标签。

写
$$
J_f'(0)=d_p\int_{Y^\times}\chi(Y)\log\langle Y\rangle f\,d\mu .
$$
从 (8) 得到
$$
\boxed{
\partial_u\partial_s\mathscr M(0,0)
=J_{\dot f}'(0)+d_p\alpha\,\mathscr M_f(0)
 +d_p\Omega_p I_D(\chi,0).
}
\tag{10}
$$
同时，
$$
\boxed{\partial_u\mathscr M(0,0)=\mathscr M_{\dot f}(0).}
\tag{11}
$$

因此 moving 权给 $J_{\dot f}'(0)$，移动尺度给实际单位质量
$d_p\alpha\mathscr M_f(0)$。只有分别已证明相应项为零时才能省略。局部质量不能从另一个未切全来源的零质量借用。

原 $\lambda H_W$、$\gamma\lambda H_V$ 以及其他 core 系数，应放入实际 $f_u$ 或式外的显示系数。若它们不随 $u$ 变化，便完整保留原乘子；若有参数依赖，其导数是 (5) 的一部分。本式不把经过不同 word 运输的权或域相认。

### 2.1 全正权也读到同一个错位一阶矩

对每个非负整数 $n$，同一来源的普通矩满足
$$
\left.\partial_u\int Y_u^n f_u\,d\mu\right|_{u=0}
=\int Y^n\dot f\,d\mu
+n\alpha\int Y^n f\,d\mu
+n\Omega_p\int x^{n-1}\,d\nu_D(x).
\tag{12}
$$
这是真正的 $n-1$ 阶矩，不是原 $n$ 阶矩在权空间上的微分。以合法正权趋近零，只得到 (10) 的负一支；不能把 $n$ 因子先删掉后认作原中央权导数。

## 3. Fourier 一阶项和固定 theta cover 的周期差

现在取固定权 $f$，并假定已按 [R745](../results/R745-finite-p-gates-algebraic-theta-sources-and-orthogonal-jets.md)、
[R752](../results/R752-native-mod-p-two-source-closure-and-point-inertia-extraction.md)
在一个真实有限 cover 上分出正交的 $Y,Z$ theta 变量。剩余伙伴全部可保为系数，或先作已付的有限正阶正交矩。

记未缩放的联合生成函数为 $F(z,w)$；约定其测度 Fourier 变换为
$F(\Omega_p z,\Omega_p w)$。于是
$$
A(z)=F(z,0),\qquad
D(z)=\partial_wF(z,0),\qquad
Y_*(Zf\mu)=\Omega_p\nu_D .
\tag{13}
$$
(9) 与这里的 $D$ 因而使用同一个 ordinary 周期，没有额外伸缩测度变量。

实际剪切后的第一生成函数是
$$
A_u(z)=F(a(u)z,b(u)z).
$$
由 (3)，其准确一阶项为
$$
\boxed{\dot A_0(z)=zD(z).}
\tag{14}
$$
如果同时有尺度 $\alpha$，再加 $\alpha zA'(z)$；
moving 权再加其本身的真实生成函数，正与 (8) 相符。

令 $j_N(\ell,z)$ 为这个固定 cover 上原第一 theta 线丛的全部自动因子，包括半特征与有限平坦特征。正交分裂意味着
$$
D(z+\ell)=j_N(\ell,z)D(z).
$$
因此
$$
\boxed{
(z+\ell)D(z+\ell)-j_N(\ell,z)\,zD(z)
=\ell\,j_N(\ell,z)D(z).
}
\tag{15}
$$
若 $D\ne0$，对任一非零周期 $\ell$，右边不是零函数。

**固定 cover 结论。** $zD$ 不是这个固定第一线丛的截面；进一步拉到任意固定有限椭圆 cover，(15) 对其非零周期仍然成立。乘一个定义在该 cover 上的非零椭圆有理 gauge 也不会消掉右边。因此不能仅凭 (2) 保范数，就把物理剪切的 first jet 当作固定 $H^0(L_N)$ 中的任意 test vector。

这不排除另一个完整自守实现。它精确指出该实现必须记录的额外项：向量
$$
\binom{zD}{D}
$$
的周期转移矩阵为
$$
j_N(\ell,z)
\begin{pmatrix}1&\ell\\0&1\end{pmatrix}.
\tag{16}
$$
加性周期是 $\ell=\int_\ell dz$。$dz$ 在任何有限椭圆 cover 上都没有椭圆有理原函数：非恒定有理函数的微分在其极点处有极，而 $dz$ 是非零全纯微分。这里陈述的是实际周期/连接项；**不把 (16) 的底层 holomorphic extension 宣称为非分裂**。

有限 $p$ 平移的平坦特征可先拉到共同 cover，半特征也包含在 $j_N$ 中，所以它们不改变 (15) 的加性差。若有额外非正交漂移，应先写完整自动因子再微分；不能以 (15) 替代未付的漂移消去。

在分布语言中，同一事实是
$$
\dot\nu(g)=\int Z\,g'(Y)f\,d\mu .
\tag{17}
$$
其 Fourier 变换为 $\Omega_p zD(\Omega_p z)$。这是一个明确的一阶分布呈示，而不是另一个无条件有界 theta 测度。本文不需要、也不声称所有这种分布都无有界呈示。

## 4. 何种固定 Katz 身份才足以传播中央零

下面给一个可以逐项检查的充分条件，而非认定原剪切已经满足它。

假设在同一参数盘上，存在一个**与 $u$ 无关**的完整 Katz/自守函数 $\mathcal L(s)$，以及已付的解析单位 $C(u,s),Q(u,s)$，使
$$
\boxed{
C(u,s)\mathscr M(u,s)^2=\mathcal L(s)Q(u,s).
}
\tag{18}
$$
“单位”包括实际 Euler、周期、局部 toric pairing 和整个 finite-character 规范；不能把另一个变动的全局 Hecke 角色藏入 $Q$。

若原 $u=0$ 满足
$$
\mathscr M(0,0)=0,\qquad
\partial_s\mathscr M(0,0)=0,
\tag{19}
$$
则 (18) 在 $u=0$ 给 $\operatorname{ord}_{s=0}\mathcal L\ge4$。
再由 (18) 对所有 $u$，可得
$$
\mathscr M(u,0)=0,\qquad
\partial_s\mathscr M(u,0)=0.
\tag{20}
$$
这是特征零解析整环中平方的阶数结论；没有选择平方根符号。故
$$
\boxed{
J_{\dot f}'(0)+d_p\alpha\mathscr M_f(0)
+d_p\Omega_p I_D(\chi,0)=0 .
}
\tag{21}
$$

(21) 就是所需的实际额外门槛。若固定权、纯 unitary 规范且原单位质量零，它才简化成 $I_D=0$。已付的非零点 logarithm 若与同一个 $D$ 匹配，就会排除 (18) 与 (19) 同时成立；这并不自行证明原题所需的 (18)。

若只定义形式平方 $\mathcal K(u,s)=C(u,s)\mathscr M(u,s)^2$，却没有固定 $\mathcal L$，则没有 (20)。设 $\mathscr M(u,0)=0$ 并写 $A(u)=\partial_s\mathscr M(u,0)$，有
$$
[s^2]\mathcal K(u,s)=C(u,0)A(u)^2.
$$
在 $A(0)=0$ 时，
$$
\left.\partial_u[s^2]\mathcal K\right|_0=0,\qquad
\left.\partial_u^2[s^2]\mathcal K\right|_0
=2C(0,0)\dot A(0)^2 .
\tag{22}
$$
所以第一变分自动看不见非零 $\dot A$；第二变分恰保留其平方，而不是又一条自动为零的行。

对真正双线性公式
$\mathscr M^+(u,s)\mathscr M^-(u,s)=\mathcal L(s)Q(u,s)$，
应分别保两侧 period 和角色。如果两质量为零，两侧一阶中央量为 $A^\pm(u)$，则
$[s^2](\mathscr M^+\mathscr M^-)=A^+(u)A^-(u)$；
在 $A^\pm(0)=0$ 时第二变分是
$2\dot A^+(0)\dot A^-(0)$。
没有已付的 same-embedding/good-pair 身份时，不能把两因子认成同一个平方，更不能从一个乘积零推出两因子各零。

## 5. 原权、剪切权及有限点支的区别

原三个中央族在非负合法权 $n$ 上使用
$$
\varepsilon_{A,n}=\psi_A^{n+1}\bar\psi_A^{-n},
\qquad \operatorname{type}(\varepsilon_{A,n})=(n+1,-n),
\tag{23}
$$
其中 $A$ 分别是原 $E_{17},E_{24},E_{2312}$。它们各自的完整 ordinary 平方及 Euler 都已经付清；三条不是同一个 degree34 空间的三个任意向量。

若 (13) 的某个型五分量正是 R735/R748 的 $D_k$，(12) 中该分量的正权是 $n-1$，其对应的 norm-weight-one 点为
$$
\psi_k^{n}\bar\psi_k^{1-n},
\qquad \operatorname{type}=(n,1-n).
\tag{24}
$$
到 $n=0$ 是 $\bar\psi_k$ 的真实负一支。有限角色还须按
[R748](../results/R748-original-type-five-ramified-good-pair-and-point-eigenspaces.md)
完整运输；另一 dyadic 型三来源使用
[R751](../results/R751-second-dyadic-character-point-fields-and-inertia-extraction.md)
的实际角型与点域。不能用总角型或 norm-weight-one 条件替换这些有限角色。

式 (23) 和 (24) 的无穷型相差 $(-1,+1)$，并且实际第一曲线角色也可以不同。partner jet 保持整个多变量 Fock 数据，并不把这两个第一因子自动变成同一 Hecke motive。这个精确错位和 (15) 是同一个物理变分的两个可见面。

若 $D$ 是 R752 的完整有限 tame 池，必须先作已付的
$D_k/P_{+,k}$ 加乘法角色分解，才可使用有限点公式。所有系数、角色、Euler 和点域留在原有限 carrier 中。这里不对原未识别的中央 height 值或无限日志级数施加 point-only inertia projector。

## 6. 已发表双线性和 height 公式的实际适用范围

Disegni 的 *The p-adic Gross–Zagier formula on Shimura curves*
([作者全文](https://disegni-daniel.perso.math.cnrs.fr/pyzz-pst.pdf)，式(1.4.2)、Theorem C)
在固定自守表示、固定全局角色及其对偶中给出
toric-period 乘积与同一 $L$ 值及局部 pairing 的关系。
root-negative 分支对应 canonical ordinary height 和 cyclotomic 导数。
这能够检验 (18)，但不自行提供把 (14) 连同 (16) 放入那个固定表示的映射。

本题原 $J_A'(0)$ 通过完整平方控制的是 Katz 反圆分支的二阶项。
[R39](../results/R39-cm-height-linear-period-matrix.md)、
[R40](../results/R40-anticyclotomic-second-coefficient-and-full-selmer.md)
保留了完整 Selmer/Sha 块；它们的具体四次 CM 曲线数据也不能直接移到本题的三条六次曲线。
[R168](../results/R168-cyclic-energies-and-heegner-height-variation.md)
的 splitting 改变量 $-\lambda\log P\log Q$ 是另一个已付变化。
改变 splitting 后的高度不能再次无证等同 canonical splitting 的同一原 Katz 导数。

Burungale–Disegni 的已发表综述性陈述也明确区分 pairing 非零与高秩非退化
([AIF 70 (2020), p.2078](https://www.numdam.org/item/10.5802/aif.3381.pdf))。
本文没有用任一这样的“pairing 非零”代替原 rank-two regulator 或完整 Selmer determinant。

## 7. 对原同域有限门的直接后果

R754 的三块实际平均比例为
$(p-3)/(p-1),1/(p-1),1/(p-1)$，连同
$\lambda H_W,\gamma\lambda H_V$，和仍准确等于原 primitive 行。
这些是已识别有限点 carrier 中的合法 source trace/point-factor 关系。

式 (10) 说明它们可以作为**真正剪切一阶项**的算术分量；
式 (18)–(21) 则精确列出何时原中央零能够传播到这条一阶项。
现有同域核心、有限 Fourier 与点公式尚未支付 (18)。
周期差 (15) 排除了最直接的“同范数所以固定有限 theta 空间内自由变向量”步骤；
它没有排除保留完整连接/其他自守实现后建立 (18) 的可能。

因此下一项需要的是原固定来源的完整双线性或 mixed-motive 映射，并保所有 moving 权、局部 pairing 和原失败补域。这里既没有新增中央零假设，也没有将已知非零负一矩的局部块直接替代完整原中央行。


## 附录 A. 原全来源的 angular commutator 与 first jet 的实际块

这一节固定式(5)的 $f$，单独分析 (14) 的 source/observation 部分。
moving 权、质量和尺度仍按 (10) 完整另加，不在此被吸收或删去。

设原联合生成函数的全局单位类型为 $R\in\mathbf Z/6\mathbf Z$：
$$
F(\zeta z,\zeta w,\zeta\mathbf v)
 =\zeta^R F(z,w,\mathbf v)
 \qquad(\zeta\in\mu_6).
\tag{A1}
$$
$\mathbf v$ 是仍保留的其他伙伴频率；可先作指定的有限正阶伙伴矩，再将它们置零。$R$ 总是指做完这些实际权后的类型。例如，若原测度类型为 $r$，所乘正齐次权总次数为 $q$，则类型变为 $r-q$，不是 $r+q$。原六 sigma 来源以及总次数为6的倍数的原权给 $R=0$。

原线性单位/深度门在同时乘 $\zeta$ 下保持不变。若使用它们的有限加性 Fourier 展开，(A1) 是**全部真实分支之和**的等式；单个平移分支不一定独立满足它。没有以角型消失删掉其中的门或相位。

对第一轴定义真正的几何投影
$$
(\Pi_a^Y F)(z,w)
 =\frac16\sum_{\zeta\in\mu_6}\zeta^{-a}F(\zeta z,w).
\tag{A2}
$$
这里仅旋转第一轴。它一般不保持原 mixed cut；(A2) 作为完整带权来源的有限操作定义，不把移动后的域冒认原域。

令
$$
D_j(z)=\partial_w^jF(z,0).
$$
由 (A1) 直接微分得
$$
D_j(\zeta z)=\zeta^{R-j}D_j(z),\qquad
\partial_w^j(\Pi_a^YF)(z,0)
 =\begin{cases}
 D_j(z),&a\equiv R-j\pmod6,\\
 0,&a\not\equiv R-j\pmod6 .
 \end{cases}
\tag{A3}
$$
这保留所有伙伴：对任一指定伙伴方向的 j 次导数均成立；
若该方向之外还保留频率，先按其实际总类型分解即可。

取原 principal 情形 $R=0$。
原第一边际只读取
$$
F(z,0)=(\Pi_0^YF)(z,0).
\tag{A4}
$$
但剪切的一阶项严格读取另一个块：
$$
\boxed{
D_1=\Pi_5^Y D_1,\qquad
\partial_w(\Pi_0^YF)(z,0)=0,\qquad
\dot A_0(z)=z\,\partial_w(\Pi_5^YF)(z,0).
}
\tag{A5}
$$
伙伴一阶 jet 同时是伙伴的型一部分。因此 (A5) 的完整二轴标签为
first-$Y$ 型5与伙伴型1，总型仍为0。
这不是从维数猜测，而是 (A1) 的逐项系数身份。

准确地，记 $\iota_u^*F(z)=F(a(u)z,b(u)z)$，
$\Pi_0^z$ 为输出一变量的型零投影，则
$$
\boxed{
\Pi_0^z\left.\partial_u\iota_u^*F\right|_0
-\left.\partial_u\iota_u^*(\Pi_0^YF)\right|_0
=zD_1(z).
}
\tag{A6}
$$
输出乘 $z$ 恰把型5改成型0；它没有把输入先变成原型零 toric eigenline。
因此先作 first-$Y$ 型零投影与先作 physical shear 的 first jet 不交换。

更一般地，若 $P$ 是作用在第一轴、与 $\mu_6$ 交换且像在型零中的有限算子，
例如未加额外 moving 门前的真实原 $S$ 线投影，则
$$
\left.\partial_u\iota_u^*(PF)\right|_0=0 .
\tag{A7}
$$
(A7) 只针对固定权的 observation first jet。
如果权随 $u$ 移动，$J_{\dot f}'$ 仍是 (10) 中的一项，不由 (A7) 变零。
若实际投影同时搬运了 gate，必须对完整搬运来源使用 (A7)，不能将它倒换成原 gate 的等式。

式 (A3) 还说明：在先投型零的来源上，伙伴的前五个正阶 jets 全为零，第一次可能返回同角块的是第六阶。
这不删除 Cayley 中 $a(u)$ 的尺度高阶项。例如完整第二阶生成函数为
$$
\left.\partial_u^2A_u(z)\right|_0
=z^2D_2(z)-r zA'(z),
\tag{A8}
$$
其中 $D_2$ 读取 first-$Y$ 型4，而第二项是实际 norm-preserving 尺度补偿。
它与 (12) 的 falling-factorial 矩完全相符。

最后，对一般 $R$ 和有限角色 $\chi$，若
$\chi(\zeta)=\zeta^c$，零权中央积分的角条件是 $c=R$；
其剪切负一项使用 $D_1$ 型 $R-1$，仍要求
$c-1=R-1$。所以这套身份保留原 finite tame branch。
R752 的 $D_k$ 与 $P_{+,k}$ 及其不同乘法角角色必须按其完整组合使用，
不能把 (A5) 理解成只留下一个裸型五截面。

(A5)–(A7) 给出 (18) 所需固定表示门的一个具体检验：
原边际 Katz 角色来自 first-$Y$ 型零块，
而已知 point-log 的 shear first jet 来自实际 off-diagonal 型5/型1块。
若有合法跨块 raising/connection 恒等式，必须同时支付这次角权转移、完整坏处角色、周期差(15)与 moving 权。
原第一边际的中央零本身没有删除该 off-diagonal 来源。


## 附录 B. 原 Cayley 家族的全局酉作用与完整十七处 gluing

以下针对 R762 的实际来源，不排除另一种尚未构造的 automorphic 实现。
记 $H_{33}=S/\sigma$，并固定原两输入
$\nu_\sigma(c)\otimes\nu_{H_{33}}(v)$，
$Y=c+v$、$Z=(33c-v)/34$。
R762 的 $r=33/1156$、$a=(1-r u^2/4)/(1+r u^2/4)$、
$b=u/(1+r u^2/4)$ 给出实际矩阵
$$
g_u=
\begin{pmatrix}
a&-b/34\\
33b/34&a
\end{pmatrix},
\qquad
(c_u,v_u)^t=g_u(c,v)^t,\qquad
c_u+v_u=aY+bZ .
\tag{B1}
$$
这里 $(c,v)^t$ 是两个**物理观察**组成的列，式 (B1) 使用观察的 dual/row Gram 作用。准确的恒等式是
$$
g_u D g_u^*=D,\qquad D=\operatorname{diag}(1,33),
$$
而不是通常在向量列上书写的 $g_u^*Dg_u=D$。
若把原 Hermitian 向量空间记为 $V=(K^2,D)$，真正用于通常列向量规范的有理酉元是
$$
G_u=g_u^*,\qquad G_u^*D G_u=D.
$$
等价地，可在对偶空间 $V^*$ 上使用 (B1) 的 $g_u$。
以下全局 Weil/toric 作用使用 $G_u$（或按此约定运输后的对偶作用），
不把两个矩阵规范混用。对有理 $u$，这个完整有理酉作用合法；
它不被附录 A 的 first-jet 周期差否定。

### B.1 有理共轭真正搬运的是完整 toric period

令 $T_{Y,Z}=U(KY)\times U(KZ)$，其中观察与向量轴按上述 Hermitian 对偶识别。
对自守函数 $f$ 和通常列向量规范的有理酉元 $G$（本家族取 $G=G_u$），
Haar 测度按共轭运输后准确有
$$
\mathcal P_{T,\alpha}(R_G f)
 =
\mathcal P_{G^{-1}TG,\ \alpha\circ\operatorname{Ad}_G}(f).
\tag{B2}
$$
这是利用左 $U(V)(K)$ 不变性 $f(tG)=f(G^{-1}tG)$ 后的变量替换。
把无穷处作用转到有限 Schwartz 时，须同时执行这个整个有理元的
共轭及其局部 splittings；(B2) 不把未积分的 theta 值改成 period。

原发表定理是 Borade–Franzel–Girsch–Yao–Yu–Zelingher，
*On tori periods of Weil representations of unitary groups*，
Selecta Mathematica **31** (2025), Article 49，
§4.2.2 与 Theorem 5.6
（[原文](https://doi.org/10.1007/s00029-025-01047-4)）。
其 seesaw 从固定全局 toric 角色 $\alpha,\beta$ 出发，要求
$\beta=(\chi_W^{-2}\chi_V)\circ j^{-1}\,
\alpha|_{K^1}$、各处完整 root/splitting 条件及指定 toric period。
它判定这个 period 在整个 theta lift 上是否恒零。
它没有断言未作 $\alpha$ 投影的任意 Jacobi 斜限制都等于该 period。

### B.2 原来源的全部十七处配对

用 R735/R761 的共同 $E_1$、原加性角色和极化规范。
原 $\sigma$ 与任意标准 $H_{33}$ 截面的17处因子都是球向量：
$17\nmid2\cdot3\cdot33$，标准 degree33 的有限 theta 系数仅在
$2,3,11$ 处改变。回 $b=17$ 的固定微分伸缩恢复原周期和代数标量，
不把共同框的球向量重新选成一个分歧17向量。

17处的两原格自对偶。整 unipotent 的二次相位在格上为1，
单位伸缩保持格，自对偶 Fourier 变换保持格指示函数；
原未分歧 unitary splitting 在这些单位上平凡。
所以原两输入的**对角** norm-one 环面固定其完整17处 tensor。

整伙伴 $w=34w_0$ 的实际加法图是
$$
(z,w_0)\longmapsto(z+33w_0,z-w_0).
\tag{B3}
$$
其 pullback 正是 $S_{34}\otimes S_{1122}$。
在17-primary 部分，(B3) 的 kernel 是整个 $E[17]$；
其 canonical lift 在两因子上给互为对偶的 Heisenberg 作用。
旧球线的像因此是两十七维 Schrödinger 模之间的
canonical perfect gluing tensor。此断言也可不使用 theta 常数：
两个不可约 Heisenberg 模的对角不变空间为一维，
其非零不变 tensor 对应一个非零 intertwiner，
由不可约性可逆。实际 pullback 非零，所以该 intertwiner 是完美配对。
整体标量及相位由 (B3) 的原 pullback 固定；此处只使用其非零性，
没有据此计算任何未给出的 toric-period 常数。

设第一轴的有限环面为 R757 的
$g_0=2+4\delta$、$\tau_j(g_0)=\zeta_{18}^j$。
第二轴的标签按**同一个对角环面的实际作用**定义，所有
quadratic splitting 均随上述 Heisenberg 对偶运输。
十七维模只缺 $j=9$。完整 gluing 表是
$$
\begin{array}{c|rrrrrrrrrrrrrrrrr}
j_Y&0&1&2&3&4&5&6&7&8&10&11&12&13&14&15&16&17\\ \hline
j_Z&0&17&16&15&14&13&12&11&10&8&7&6&5&4&3&2&1 .
\end{array}
\tag{B4}
$$
每一对都非零：完美 intertwiner 限制到每个单重本征线仍可逆。
(B4) 并未说对伙伴取值或取某个 jet 后每一对都存活。
它正好说明不能在取值之前删去那些整 tensor 分量。

(B1) 的对偶作用，等价地通常向量规范中的 $G_u$，与对角环面交换，
通常不与 $T_{Y,Z}$ 的两个独立因子交换。
固定整个 Weil 空间因而没有冻结原第一轴的有限 Hecke 角色。

### B.3 原非零 tangent 位于哪些真实分量

原
$$
F(z,w)=
 \sigma(z+33w/34)H_{33}(z-w/34)
$$
满足 $F(z,0)=S(z)$、$\partial_wF(z,0)=D_S(z)$。
R757 的同向标签中，$S$ 属于 $\tau_{12,Y}$；
R761 的完整公开分解则为
$$
D_S=\frac{11}{21}D_\omega+R_{\rm prim},\qquad
D_\omega\in\tau_{3,Y},\qquad
R_{\rm prim}\in\tau_{1,Y}\oplus\tau_{7,Y}\oplus\tau_{13,Y}.
\tag{B5}
$$
结合 (B4)，相应伙伴标签依次为
$6$（原 S 边际）、$15$（$D_\omega$ first jet）及
$17,11,5$（primitive first jets）。
这些不同角色均在同一实际 tensor 中，并非新添的独立输入。

设 $\Pi_{12,Y}$ 是第一轴完整17处投影。
其有限作用与伙伴求导交换，故
$$
\left.\partial_w\Pi_{12,Y}F(z,w)\right|_{w=0}=0,
\qquad
\left.\partial_wF(z,w)\right|_{w=0}=D_S(z)\ne0.
\tag{B6}
$$
因此先在全 joint 上保原 Katz 角色，再作同一 first jet，
得到的来源已经不是 R762 的非零 tangent。

结论限定为这个实际接口：
(B1) 对应的有理酉元 $G_u=g_u^*$ 与 period 共轭 (B2) 都合法；
现成定理作用于全 $\alpha$-period，而 R762 使用的是未投影斜限制。
若要证明原同一 $L_p$ 的单位因子身份，必须额外证明该 period
准确等于 R762 的整条 $\mathcal M(u,s)$，包括
(B4)–(B6) 的 cross-block 和实际 p-local 向量。
只投影后应用 seesaw 会换掉已支付的非零切向来源。
本附录不从这一具体区别推出任何一般“无 automorphic 实现”定理，
也不添加原中央零条件。
