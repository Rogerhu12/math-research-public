# R298：平台矩阵为零仍有严格三阶 self 响应，以及一个指定 profile 的真实十观测控制

日期：2026-11-15。**完整纸面证明；没有执行新的符号程序、profile 求积、研究扫描或人工测试。**

本稿回答 [R295](R295-final-grid-forces-zero-platform-matrix-and-exact-self-history-principal.md) 留下的一个具体问题：已经令真实平台矩阵 $\mathbf T_B$ 全部为零，是否就能把单包 self 历史的三阶主项当成低阶数据？

答案在真实响应层是否定的，而且有一个完全显式的方向。取原八矩算子
$P(u,v)=J(u''v'')$ 与 R261 的 $\chi_{30}$，其完整第四响应 $K_*$ 满足

$$
\boxed{
\pi K_*=0,\qquad \mathbf T(K_*)=0,\qquad
\mathfrak q_u(K_*)=
\frac{3}{512}\int (u'')^2(u''')^2>0
}
\tag{1}
$$

对每个非零实紧支撑 $u$ 成立。式 (1) 是完整 self 值，没有隐藏的 $C^2$ 余项。

再用 [R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md) 的九个真实响应，得到固定单个 $u$ 的十观测满射。R222 的有限真实控制定理由此给实际 $M=0$、第三算子 $T=\kappa\mathfrak H$、universal pure 为零的闭 hook，使平台矩阵和这个指定 self 值同时取任意给定值。

该实际结论允许重新选择几何，保全部控制基准与真实历史；不声称保持已经冻结的 Gaussian germ、全域 Morse 性、全部 Gaussian 能量或同一目标度量。也没有把一个指定 $u$ 推广成全部有限模板的 $q_i$，更没有令整个函数 $u\mapsto\mathfrak q_u$ 为零。

## 1. 同一规范下的两个有限观测

沿用 R105 的真实有限成本空间 $U$、完整响应空间 $\mathcal R$ 和 universal pure 投影 $\pi$。记

$$
P_{\rm univ}=\pi U,\qquad L_{\rm resp}=\pi\mathcal R.
$$

这里 $P_{\rm univ}$ 是函数空间；它不同于本稿的八矩算子 $P=J(u''v'')$。

对固定实紧支撑 $u$，定义全 $U$ 上的线性观测

$$
\boxed{
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u\odot u,0).
}
\tag{2}
$$

第二个输入 $\phi=0$ 只用于真实 universal 原式的代入，不要求它本身是一条合法、非退化的 profile 圆。所有输入仍用同一右锚，$[x^2]_{\rm left}$ 抽取真实共同左 collar 的二次多项式系数。

在 R292/R295 的实际 $M_B=0$、完整第三 hook 及另外已经构造的 $\pi V_B=0$ 条件下，(2) 就是那两篇的单包 self $q_B(u)$。其中用到的 pure 是实际成本的完整函数身份，不能由 $\pi U=\pi\mathcal R$ 等空间命题代替。

平台矩阵的全 $U$ 延拓采用 R297 的原查询。取实包 $u$ 全在 $v$ 左侧，定义

$$
\mathfrak t_{u,v}(V)=
-\frac14[x^2]_{\rm left}[a^2b^2]\,
V(a^2u\odot u,bv).
\tag{3}
$$

这里 $a,b$ 是形式实幅参数。R297 从完整 canonical 恢复证明，(3) 对实际路径准确为
$\mathcal T_B(\mu(u),\mu(v))$，其中

$$
\mu(u)=\left(
\int(u'')^2,\quad
\int x(u'')^2,\quad
\int\{x^2(u'')^2+2(u')^2\}
\right).
\tag{4}
$$

三个固定左包、三个固定右包各取相同宽度和三个不同中心，其三矩向量各为一组基。用这两组**准确三矩**反解 (3) 的九个原查询，得到固定线性映射

$$
\mathbf T:U\longrightarrow {\rm Mat}_{3\times3}(\mathbb R).
\tag{5}
$$

因此下文的矩阵坐标和 (2) 都在同一个真实 $U$ 上有定义；没有在 pure 核外任意选择补空间，也没有把单包自身的三矩设成零。

## 2. $\chi_{30}$ 的全部二次尾矩准确为零

[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md) 已付完整
$\chi_{30}\in Z=\ker\Delta$，以及

$$
K_u^\tau(w)=\tau(w;u,u)
=-J^3(\mathscr A_{\tau,u}w),\qquad
\mathscr A_{\tau,u}=D^2(aD^2)+D(bD)+c,
\tag{6}
$$

其中 $D=D_x$，$Jf(x)=\int_x^{r_*}f$。共同右端的三个常数为真零；所有左尾保留。

置 $r=u''$。R261 §3.1 的完整零阶系数是

$$
c_{30,u}
=\frac{3u''u^{(5)}+9u'''u^{(4)}}{256}
=\frac3{512}D^3(r^2).
\tag{7}
$$

故对 $j=0,1,2$，

$$
\boxed{\int x^j c_{30,u}\,dx=0.}
\tag{8}
$$

三次分部积分只使用 $u$ 的真实紧支撑。式 (8) 是随所有 $u$ 变化的原身份，不是三个采样值。

采用 R83/R217 的完整第四响应规范

$$
\begin{aligned}
K_{E,\tau}(F,\phi)
={}&2\tau(\Phi_E D;D)
-4\tau(\phi;\phi,\Phi_E D)\\
&+4\Phi_E(\phi,\tau(\phi;D)),
\qquad D=F-\phi^2 .
\end{aligned}
\tag{9}
$$

这是原真实响应方向，不是任意新定义的四次算子。对 $\tau\in Z$，对角身份及其极化

$$
\tau(u;u,u)=0,\qquad
\tau(w;u,u)+2\tau(u;u,w)=0
\tag{10}
$$

使 (9) 的纯四次部分准确抵消。因此
$K_{E,\tau}\in\mathcal R\cap\ker\pi$。

如果 $u$ 在 $v$ 左侧，R297 的同锚全式给

$$
\boxed{
\mathfrak t_{u,v}(K_{E,\tau})
=-\frac14\int c_{\tau,u}(x)\,
p_E(\mu(v);x)\,dx,
}
\tag{11}
$$

其中 $p_E(\mu(v);x)=\Phi_E(v,v)(x)$ 在 $u$ 支撑处的真实左二次尾。式 (11) 仍保其常数、一次及二次部分。

由 (8)，对每个八矩 $E$ 都有
$\mathbf T(K_{E,\chi_{30}})=0$。特别令

$$
\boxed{K_*=K_{E_{r_0},\chi_{30}},\qquad
\Phi_{E_{r_0}}(u,u)=P(u,u)=J(r^2),}
\tag{12}
$$

便有 (1) 的前两个等式。这不是把 $P(u,u)$ 称为紧支撑；它一般在左端是非零常数。

## 3. 完整 self 值就是严格正的三阶能量

在 (9) 中代 $F=u\odot u$、$\phi=0$，准确得到

$$
K_{E,\tau}(u^2,0)=2K_u^\tau(\Phi_E(u,u)).
\tag{13}
$$

对任意这里出现的真实 $w=\Phi_E(u,u)$，(6) 给

$$
[x^2]_{\rm left}K_u^\tau(w)
=-\frac12\int\mathscr A_{\tau,u}w
=-\frac12\int c_{\tau,u}w.
\tag{14}
$$

第二个等号使用 $a,b$ 及它们的全部导数在 $u$ 的两侧为零，故两项散度的边界为零。它**没有**要求 $w$ 的左多项式尾为零。由 (2)、(13)，

$$
\boxed{
\mathfrak q_u(K_{E,\tau})
=-\frac14\int c_{\tau,u}\Phi_E(u,u).
}
\tag{15}
$$

现在取 (12)，记 $R=r^2$。原正右积分满足 $(JR)'=-R$，从而

$$
\int R'''JR
=-\int R''(JR)'
=\int R''R
=-\int(R')^2.
\tag{16}
$$

第一步的 $JR$ 左常数确实保留；乘它的 $R''$ 在左端为零，所以这一步没有遗漏端项。将 (7)、(16) 代 (15)，得

$$
\boxed{
\mathfrak q_u(K_*)
=\frac3{2048}\int(R')^2
=\frac3{512}\int (u'')^2(u''')^2 .
}
\tag{17}
$$

若 $u$ 是非零实紧支撑函数，(17) 严格正。否则连续函数
$(u'')^2(u''')^2$ 恒为零，因而 $D((u'')^2)=0$；
$(u'')^2$ 为常数，并因外 collar 为零而处处为零。
于是 $u$ 仿射且紧支撑，只能为零，矛盾。

### 3.1 对 R295 五类未决主系数的直接回答

R295 的实际 self 分裂为

$$
q_B(u)=-\frac18\int
\mathcal K_B(x;u,u',u'')(u''')^2\,dx
+\mathcal L_B(u),
\qquad \mathcal L_B\in C^2,
\tag{18}
$$

其中

$$
\mathcal K_B=\int_B\frac{k(1+e^2)}h\,\Lambda^2\,ds.
$$

该文已经单独证明 $u^2$ 主系数因 $M_B=0$ 自动为零。式 (17) 进一步给出一个准确的剩余响应方向：在 (18) 的线性成本层，其主多项式为

$$
\boxed{\mathcal K_{K_*}=-\frac3{64}(u'')^2.}
\tag{19}
$$

式 (19) 是由完整 (17) 读出的 principal 方向，不把一个响应线性组合冒作一条实际路径的 $\Lambda$。它显示其余五类中的 $(u'')^2$ 通道并不由 $\mathbf T=0$ 消灭；本文不需要预判另外四类是否独立。

这个能量不能被当成 $C^2$ 多项式观察。举例取一个真实光滑 $u_0$ 和支撑于其 $u_0''\ne0$ 区域的实 cutoff $\chi$，令

$$u_N=u_0+N^{-5/2}\chi\cos(Nx).$$

则 $u_N\to u_0$ 于 $C^2$，但由准确 (17)，

$$
\frac{\mathfrak q_{u_N}(K_*)}{N}
\longrightarrow
\frac3{1024}\int (u_0'')^2\chi^2>0.
\tag{20}
$$

这里仅是纸面高频极限证明，没有运行任何 profile。若要固定一个最初给定的有限 polynomial $C^2$ 观察映射，R295 §7 的最大秩纤维与固定光滑纠正论证适用；不能以新增这些低阶观察便宣 (17) 已固定。本文后面的实际控制则把**一个指定 $u$ 的数值**作为新线性成本观察，并不将 (17) 改称 $C^2$ profile 泛函。

## 4. 九个平台坐标加一个指定 self 的严格三角右逆

现在固定一个非零实紧支撑 profile $u_*$，并缩记
$q_*=\mathfrak q_{u_*}$、$d_*=q_*(K_*)>0$。

R297 已给九个真实 pure-zero 响应。采用其精确规范，

$$
(\zeta_0,\zeta_1,\zeta_2)
=(64\chi_{32},-32\chi_{37},64\chi_{40}),
\qquad
R_{ij}=16K_{E_{p_j},\zeta_i},
\quad 0\le i,j\le2,
\tag{21}
$$

满足

$$
\pi R_{ij}=0,\qquad \mathbf T(R_{ij})=e_{ij}.
\tag{22}
$$

这里 $e_{ij}$ 是矩阵单位；(22) 引用其完整原尾证明，不重新求九个数值列。记准确有限实数
$q_{ij}=q_*(R_{ij})$。无需计算它们的具体值就可定义

$$
\boxed{
\widetilde R_{ij}=R_{ij}-\frac{q_{ij}}{d_*}K_*,
\qquad \widetilde R_\star=\frac1{d_*}K_*.
}
\tag{23}
$$

于是对
$F_*=(\mathbf T,q_*):U\to\mathbb R^9\oplus\mathbb R$，

$$
\boxed{
F_*(\widetilde R_{ij})=(e_{ij},0),\qquad
F_*(\widetilde R_\star)=(0,1),\qquad
\pi\widetilde R_\bullet=0 .
}
\tag{24}
$$

这是原函数空间内的精确三角结构，十阶行列式在未作 (23) 的列中就是 $d_*\ne0$。没有浮点 rank、没有把九条原列重做消元，也没有把 $q_{ij}$ 当作可独立任意指定的形状常数。

因此

$$
\boxed{
(\pi,F_*)(U)=P_{\rm univ}\oplus\mathbb R^{10},\qquad
(\pi,F_*)(\mathcal R)=L_{\rm resp}\oplus\mathbb R^{10}.
}
\tag{25}
$$

准确商仍为 $P_{\rm univ}/L_{\rm resp}$；本稿不假定所有权上都有
$\pi U=\pi\mathcal R$。

响应层的 (24) 本身尚非负成本或实际可达结论。下一节用真实有限控制词支付这一点。

## 5. 一个指定 $u_*$ 的真实十观测联调

**定理。** 在 R222/R297 的共同端口和真实有限生成库范围内，先选定共同合法物理区间 I 与右锚，再固定其中任意非零实紧支撑 $u_*$。对任意

$$
p\in P_{\rm univ},\qquad A\in{\rm Mat}_3(\mathbb R),
\qquad b\in\mathbb R,
$$

存在实际有限同端口、frame $I\to I$ 块 D，满足

$$
\boxed{
M_D=T_D=0,\qquad
\pi V_D=p,\qquad
\mathbf T(V_D)=A,\qquad
q_*(V_D)=b.
}
\tag{26}
$$

固定紧目标集可用同一个有限控制词取得 $C^1$ 目标截面。

**证明。** R297 已核 (21) 的完整 W prototypes 是 R222 一般控制定理允许的真实原响应。新增 (12) 也是同一类完整 W 响应。式 (23) 只用有限个原响应和准确实系数，满足 R222 的一般 $m=10$ 假设，观测矩阵由 (24) 恰为单位阵。

为明确没有把 span 当作实际支付，写出该定理在这里的成本结构。每个实际第三 prototype 的成本先追加真实 full-pure 校正；改后基准记 $\widehat v_j$，有 $\pi\widehat v_j=0$，但其所有 mixed 值仍保留。有限复制词准确给

$$
V_{Z(t,n)}
=E_0(t)+n\left(2\sum_{j=1}^{10}\widehat v_j
+\sum_{j=1}^{10}t_j\widetilde R_j\right).
\tag{27}
$$

其中 $E_0(t)$ 是真实 $C^1$ 偶基准，与最后的复制数 n 无关。用 R212 同一个真实 full-pure 截面支付
$p-\pi E_0(t)$ 后，十观测准确为

$$
F_*(V_{\widetilde Z})
=\mathcal E(t,p)+n(2v_\Sigma+t),
\qquad
v_\Sigma=\sum_jF_*(\widehat v_j).
\tag{28}
$$

$\mathcal E$ 包含原基准以及 pure 校正自身带来的全部九矩和 $q_*$ 成本；不假定其为零或线性。先在
$t^0=-2v_\Sigma$ 附近固定一个有限盒，固定覆盖该盒的实际小参数族和 pure 截面，再选择有限整数 n。R222 的 Brouwer／统一收缩解

$$
t=t^0+n^{-1}\{(A,b)-\mathcal E(t,p)\}
\tag{29}
$$

给 (26)；在紧目标集上选 n 也大于统一导数界，得到真实 $C^1$ 截面。负系数进入允许的小参数，所有复制次数仍为正整数；没有使用负路径或负成本。证毕。

### 5.1 共同区间与查询的选择顺序

第十列不造成选择循环。先固定 full-pure 库、九个 (21)、一个 (12)、背景 hook 和所有 frame/scalar 桥的有限原生成器及小参数包络；这些原方向不依赖 $u_*$。然后选共同合法 I，固定九矩查询的六个包及 $u_*$。

这时 (17) 对任意这样的非零 $u_*$ 都严格非零。随后才确定 (23) 的实系数、(27) 的参数盒与最后的有限重复次数。大系数和大目标只增加同一小族的有限重复，不扩大先选的 scalar 包络。所有真实右锚、完整传入 history、端口复位和 h 的正下界保持。

本结论没有要求任意事先冻结的狭窄 I、固定总长或固定空间位移都允许上述库。它也不将 (26) 中随目标改变的几何称为同一度量内的等距变形。

## 6. 真实闭 hook：矩阵零与单个 self 零可以共同取得

将一个实际闭 hook 背景 $X_0$ 先纳入上述有限库，保

$$
M_{X_0}=0,\qquad T_{X_0}=\kappa\mathfrak H,\qquad \kappa\ne0.
$$

其成本属于 U，仍用 R210/R222 的真实 $X_0X_0^{\rm rev}$ 论证；取半只说明空间归属，不作实际成本减半。

给定目标 $A,b$，对 (26) 指定

$$
p=-\frac14\pi V_{X_0},\quad
\mathbf T(V_D)=\frac14\{A-\mathbf T(V_{X_0})\},\quad
q_*(V_D)=\frac14\{b-q_*(V_{X_0})\}.
\tag{30}
$$

把同一实际 D 插入 Klein 的一类 prototype，连同四个正确 ambient 副本。原规范给

$$V_X=V_{X_0}+4V_D.$$

所以

$$
\boxed{
X\text{ 是有限真实闭 hook},\quad
M_X=0,\quad T_X=\kappa\mathfrak H,\quad
\pi V_X=0,\quad \mathbf T_X=A,\quad q_X(u_*)=b .
}
\tag{31}
$$

修改后的真实位移由 Klein 字闭合，未要求 D 位移为零。取 $A=0,b=0$ 就支付该单包 self；取 $A=0,b=1$ 则给同样下层条件下 self 非零的实际几何。两条几何一般不同，不把它们视为固定旧度量的变形。

### 6.1 在真实矩阵零约束内，三阶通道也不能普遍消失

还有一个直接保留整函数差的实际见证。对原响应 $K_*$ 使用 R83/R101 的两个配对词，得到同端、frame I、$M=T=0$ 的实际块 $Z_+,Z_-$，使

$$V_{Z_+}-V_{Z_-}=2tK_*,\qquad t\ne0.$$

其 full-pure 与九矩完全相同。将它们分别插入同一个背景的同一类 Klein prototype，再用 R297 的一般 $m=9$ 定理，对二者的**共同** pure／矩阵基准选择同一实际校正 D。得到两条真实闭 hook $X_+,X_-$，满足

$$
M_{X_\pm}=0,\quad T_{X_\pm}=\kappa\mathfrak H,\quad
\pi V_{X_\pm}=0,\quad\mathbf T_{X_\pm}=0,
$$

并且整个真实函数差为 $8tK_*$。因此对共同 I 内的每个实紧支撑 u，

$$
\boxed{
q_{X_+}(u)-q_{X_-}(u)
=\frac{3t}{64}\int(u'')^2(u''')^2 .
}
\tag{32}
$$

全部公共基准、mixed 校正和真实历史在这个差中准确相消。由于 (32) 不是 $C^2$ profile 泛函，两条实际几何中至少一条的 R295 三阶 principal 不为零。故

$$
M=0,\quad T=\kappa\mathfrak H,\quad \pi V=0,\quad
\mathbf T_B=0
$$

这些完整实际条件本身，仍不能普遍推出 R295 主多项式的五个未决 jet 类全部消失。这是对该普遍蕴含的真实反例；不是把响应层的 (19) 直接当成一条无基准路径。

## 7. 单包数值、整函数和窄几何族必须分开

本稿完成了三项新的准确结论：

1. 原 $\chi_{30}/P$ 响应的整个三矩矩阵为零，而 self 完整为 (17) 的非零三阶能量。
2. 加入一个**先固定的非零实 $u_*$** 后，十个观测在 pure-zero 响应上有准确三角右逆，并可保全部基准真实同时控制。
3. 真实闭 hook 的 $\mathbf T_B=0$ 约束仍允许三阶 self 通道；式 (32) 给整个 profile 函数差的严格见证。

以下没有因此支付：

- 一个有多个不同真实单包的模板要求全部 $q_i=0$。本文没有证明这些多个 self 观测与九矩的联合独立性，也没有证明所有单包同一个系数方向就能共同支付。
- 令 $q_B(u)=0$ 对所有 u 成立是原函数身份，远强于 (31) 的一个数值目标。
- R295 当前最终模板的 $\mathbf T_B=0$ 只是必要门。它还须与全部 self、平台常数／一次尾、内部通量、端 germ 和同一个 gauge 的 ruling 条件相容。
- R222/R297 的一般实际控制不自动保 R227/R241 的特定 Gaussian germ、Morse 性、已付全部 Gaussian 原函数系数或固定目标度量。那些是额外的真实约束族问题，不能由 (24) 的响应满射替代。
- 本稿没有用新的科学计算，也没有把有限数值控制当作完整第四 period、完整 ruling 或主课题的有限等距族完成。

来源为 R83/R101 的完整实际响应规范、R217 的配对词与公共校正原则、R222 的一般有限观测定理、R261 的原局部系数、R292/R295 的实际 self 及平台分裂，以及 R297 的九个矩阵单位。每个右积分与原四倍 Klein 成本均按这些来源保留。
