# R512：固定紧母二阶规范的完整线性全路径方程与常态区段严格排除

日期：2026-11-16。**新的完整纸面结果；没有执行 profile 求积、原根恢复、数值秩、符号程序、开发检查或科学任务。**

本稿将 [R505](R505-complete-same-mother-ruling-and-real-nonsecant-local-paths.md) 的字面同形母库扩到一个明确的、固定有限秩二次规范。不是为每个路径段重新选一个规范：新增的第二母函数、完整二次规则和第三 Gram 都只选一次，随后作用于同一条真实词的全部位置。

核心结果是一条完整全路径等价式。用同一个第三规范准确承担第二规范的整个平方后，原第四 ruling 对新增紧母函数及剩余三个 Gram 常数是一个**线性函数方程**。原所有 second history 和 canonical 能量仍在右端。速度的严格正二次 Gram 不变，因此这种规范不能把能量约束的二次主部清掉。

这条等价式还给出一个已经闭合的全词结论：在本稿同形第一圆上，只要真实词含一个正长度的全 scalar 常态区段，任何这样的固定二次／第三规范都不能使全词的完整第四 ruling 为零。证明从右末实际微包前的真实 gap 读出非零原矩阵输出，故不是仅给一个可能为零的平方系数。原 R70 的常态 bulk 不能靠新增规范修复；后续必须构造真正非恒的完整连接段。

## 1. 第一母库、原恢复及新增规则

固定 R505 从起点选择的第一圆。所有最细实际包为同一个实偶、非零、光滑紧母 $u$ 的平移
$$
u_i(x)=u(x-y_i).
$$
共同宽度已收入 $u$；真实八副本、十二翻号副本和五个正权 block 的幅度全部收入 $a_i,b_i$：
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
\phi_\theta=f\cos\theta+g\sin\theta,
$$
$$
c_i(\theta)=a_i\cos\theta+b_i\sin\theta,\quad
d_i(\theta)=a_i^2-c_i(\theta)^2,\quad
R_i=a_i^2-b_i^2\ne0.
\tag{1}
$$
这里 $R_i\ne0$ 来自 [R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md) 的原 low/high 编码分别为 $-B/2$ 与 $8B$，$B>0$；每次共同非零幅复制只把 $R$ 乘以幅度平方，$g$ 翻号不改变 $R$，五块也只用正幅。下文严格排除实际上只需最右非零 $R_n$。

支撑严格不交，包之间及全体两端保正宽 collar。原
$D_\theta=f^2-\phi_\theta^2$ 和 $\Delta=f^2-g^2$ 的三矩为零。位置、幅度、右锚以及全部复制关系保持原 R280/R183/R505 的一次固定含义。

允许一个预先固定的原 E8 第二规范 $B_0D_\theta$，包括 $B_0=0$ 以及 R508 的 $P-cR_y$。本稿不改变它；新增部分由另一个实函数
$$
v\in C_c^\infty(J)
\tag{2}
$$
给出，其中 $J$ 严格包含于母包的固定活动区间。$v$ 不必等于 $u$ 的某个微分表达，也不要求偶性。令
$v_i(x)=v(x-y_i)$，其支撑位于第 $i$ 个包内。

取固定连续实线性泛函 $\ell_i$，满足 $\ell_i(u_j)=\delta_{ij}$。例如由于原 $u_i$ 支撑不交，可以直接取
$$
\ell_i(a)=\frac{\int a(x)u_i(x)\,dx}{\int u_i(x)^2\,dx}.
$$
定义
$$
\boxed{
\mathcal W_v(a,b)=\sum_i\ell_i(a)\ell_i(b)v_i .
}
\tag{3}
$$
这是一个固定、实、对称、有限秩的双线性规则，输出同一两端 collar 真紧。它不需要属于原 E8，也不声称是一个局部或平移不变的 universal 算子。

在当前实际圆上，其值准确是
$$
\boxed{
\mathcal W_v(D_\theta)=\sum_i d_i(\theta)v_i,\qquad
q_v:=\mathcal W_v(\Delta)=\sum_i R_i v_i .
}
\tag{4}
$$
原实际规范取
$$
w_\theta=B_0D_\theta+\mathcal W_v(D_\theta).
\tag{5}
$$
它对 $s$ 不变、随相位光滑、周期，并在两个 seed 上为零。所有 $v_i$ 是同一个固定母的实际平移，不为每个包单独选择一个解。

记
$$
q_0=B_0\Delta,\qquad q=q_0+q_v .
\tag{6}
$$
$q_0$ 可以在包间有原真尾；其全圆三矩使它双 collar 紧。$q_v$ 则在每个包外本来为零。两者不能混称为逐包紧。

## 2. 第三合法性与整个新增第三场的真实尾

### 2.1 原第三 Gram 合法性准确成立

新增规范的三个原配对为
$$
I_j(\phi_\theta,\mathcal W_v(D_\theta))
=\sum_i c_i(\theta)d_i(\theta)I_j(u_i,v_i),
\qquad j=0,1,2 .
\tag{7}
$$
不交支撑消掉所有 $i\ne j$ 的交叉。共同平移后的 $I_j(u_i,v_i)$ 是位置的次数至多 $j$ 的多项式；$I_2$ 完整含 $2u_i'v_i'$。

原八副本的共同幅度 $\alpha_\ell$ 满足
$\alpha_\ell^3=(-1)^\ell\binom7\ell$。在(7)中，$\phi$ 的一次幅度与规范的二次幅度恰给 $\alpha_\ell^3$，因此原第七差分准确杀掉三个完整配对。后续十二翻号及五个正权 block 保持这一零值。

所以
$$
\boxed{\mathbf I(\phi_\theta,\mathcal W_v(D_\theta))=0}
\tag{8}
$$
对所有相位成立。结合 $B_0D_\theta$ 已有的合法性，(5)满足原第三 ruling 条件；没有假定某个单包的三个交叉矩为零。

这里使用 [R408](R408-independent-second-gauge-invariant-fluxes-and-natural-character-extension.md)(4)的原合法性含义。R408 只为一般固定规则提供定义域，不自动支付(8)；本节已直接支付。

### 2.2 新增场不产生一条未记的 ordered 尾

原 second 场改变为
$$
Z_\theta=Z_\theta^{\,0}-Y_{\mathcal W_v(D_\theta)},
$$
其中上标 $0$ 保已固定的 $B_0$。单包新增项 $Y_{v_i}$ 在该包两侧为零。因此：

1. 原 second 单包的左仿射分子完全不变；
2. 左 outer 包看到的右 inner second 尾仍只依赖原 $\mu(u_j)$；
3. 对 $i\ne j$，原二次恢复中 $H(Y_{u_i},Y_{v_j})$ 的全部 forcing 都逐点为零，故在同一右锚下整个新增 mixed 场为零。

第三场的新增部分是原
$2Z_{\rm pair}(\phi_\theta,\mathcal W_v(D_\theta))$，保完整变化-profile 恢复。由上述不交性，它只留下 $i=j$ 的同包部分。单包第三输出在左侧至多仿射；对另一个紧 outer $Y_{u_k}$ 的配对准确是
$\int V_{Y_{u_k}}'\cdot\text{常向量}=0$。
不能将这条积分零改写成单包第三场左紧。

因此新增 $Y$–third 配对只改变 R505 的共同 self 函数；它没有增加新的跨包有序核。基准 $B_0$ 已有的全部真尾和 canonical ordered 核仍按原式保留。

## 3. 同一个 $(u,v)$ self 仍由原包装准确消去

将某个包搬回母坐标、位置参数记为 $t$。$Y_u$ 和 $Y_v$ 的原分子次数都至多一。它们的完整二次恢复由 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 给出至多
$(4,3,5)$ 的三个分量次数，故新增第三配对的共同平移次数在 R505 的至多十界内。原 $s$ 历史、右锚常数、$P_s,B_s$ 和外层导数均保留；固定 $v$ 不随 $s$ 变化。

于是新增 self 仍准确写成
$$
\sum_i c_i(\theta)^2d_i(\theta)\,P_s^{u,v}(y_i),
\qquad \deg P_s^{u,v}\le10 .
\tag{9}
$$
基准 self 与所有 canonical ordered 项仍是 R505 的原完整式。等背景十矩消两个 even 组合，十二个真实翻号副本消 odd 组合，五块原三个有序面积消反对称尾；新增部分(9)也由同一条链消去。

因此，在未加第三齐次规范前，
$$
\boxed{\frac1h\int V_{Y_\phi}'\cdot V_{\mathrm{third}}'=0}
\tag{10}
$$
对全部实际几何位置和相位成立。这里的第三场始终是原完整恢复，不是只有某个 leading 或局部 slot。

同时，完整 second 能量的 cross 核也不变：单包 $Y_{v_i}$ 左、右都紧，故它既不改变原左仿射向量，也不改变与右包常导数的完整边界积分。单包 self 仍是同一个 $(u,v)$ 的十次多项式。所以 R505 的相位恒等仍准确成立：
$$
\boxed{
\frac1h\int|V_{Z_{D_\theta}}'|^2
=\sin^2\theta\,\frac1h\int|V_{Z_\Delta}'|^2 .
}
\tag{11}
$$
即便新增规则不在 E8，(10)(11)也没有依赖其 universal 成员标签；它们来自当前真实包、实际幅度和原 forcing。

## 4. 同一个第三 Gram 处理整个平方：全路径等价式

固定一条真实几何路径及其全部传入历史。令 $Z_{\rm can,\Delta}$ 为该路径的 canonical second 场，不含(5)；它仍包含按原 Mraw 积分的完整 $\mathsf m(s)$。定义
$$
\mathscr E_{\rm can}(s)=
\frac1h\int|V_{Z_{\rm can,\Delta}}'|^2,\qquad
\mathcal B_s(q)=\frac1h\int
V_{Z_{\rm can,\Delta}}'\cdot V_{Y_q}' .
\tag{12}
$$
基准或新增第二规范的完整平方不能删掉。准确展开是
$$
\frac1h\int|V_{Z_{\rm can,\Delta}}'-V_{Y_q}'|^2
=\mathscr E_{\rm can}-2\mathcal B_s(q)
+\mathbf w_{\rm geom}(s)\cdot\mathbf I(q,q),
\tag{13}
$$
其中
$$
\mathbf w_{\rm geom}
=\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right),
\qquad d=h\omega-k.
$$
这里 $\mathbf I(q,q)$ 使用同一个原固定 $x$；所有 $I_2$ 中的 $2q'^2$ 均保留。式(13)是原完整物理配对，非 principal。

选一个实常向量 $\nu_*\in\mathbb R^3$，并且只选一次第三规范使
$$
\boxed{
\mathbf I(\phi_\theta,\chi_\theta)
=\sin^2\theta\left\{\nu_*-\frac12\mathbf I(q,q)\right\}.
}
\tag{14}
$$
原三个 Gram 泛函的同一个光滑右逆给真紧、光滑、相位周期、保两个 seed 的 $\chi_\theta$。$f,g$ 线性独立使每个 $\phi_\theta\ne0$，所以此右逆在全部相位上一致合法。

由(10)(11)(13)(14)，整个第四 ruling 准确为
$$
\boxed{
\mathscr K(s,\theta)
=-\sin^2\theta
\{\mathscr E_{\rm can}(s)
-2\mathcal B_s(q_0)
-2\mathcal B_s(q_v)
+2\mathbf w_{\rm geom}(s)\cdot\nu_*\}.
}
\tag{15}
$$
这是原平方与第三 Gram 的准确相消，不是把平方 forcing 本身置零。原完整第四 forcing 和全部周期成本仍保这些项。

**完整全路径规范定理。** 对这一条固定真实路径、同一第一圆和基准 $B_0$，存在本稿形式的同一个规范对 $(w_\theta,\chi_\theta)$ 使全部 $s,\theta$ 的第四 ruling 为零，当且仅当存在一个实紧母 $v$ 和三个实常数 $\nu_*$，满足
$$
\boxed{
2\mathcal B_s\!\left(\sum_iR_i v(\,\cdot-y_i)\right)
-2\mathbf w_{\rm geom}(s)\cdot\nu_*
=\mathscr E_{\rm can}(s)-2\mathcal B_s(q_0)
\quad\text{对整个实际路径的全部 }s .
}
\tag{16}
$$
必要性与充分性都直接来自(15)，而(8)(14)已经支付对应的第三合法性和真实 Gram。

(16)对未知 $(v,\nu_*)$ 是线性的。$\chi$ 本身对 $v$ 可以二次依赖，因为它保留了(14)的完整平方；这不改变(16)是线性全路径方程的事实。若此前别的段已经锁定第三 Gram，则(14)还必须等于那个固定向量，不能把 $\nu_*$ 再当自由常数。

### 一个确切有限接口，但不预授其像

在固定 profile 库中，原 $V_{Z_{\rm can}}'$ 对当前
$h,k,\omega,h_s,k_s,\mathsf m$ 由有限 Laurent–多项式系数、有限个原 profile 函数和固定右积分组成。因此(12)可写成
$$
\mathcal B_s(q_v)=\sum_{\alpha=1}^{N}
a_\alpha(s)\,\ell_\alpha(v),
\tag{17}
$$
其中每个 $\ell_\alpha$ 是明确的实连续线性紧 profile 泛函，来自完整(12)，并保全部包和尾。没有把新的 $v$ 拆成各包独立未知量。

把(17)、三个原几何权以及(16)右端放进它们的实际有限函数空间后，(16)就是一个准确有限线性像问题；所有函数关系须在该空间内处理。此处不以 $N$ 个显示生成式声称秩 $N$，也不声称任意预给路径右端都在像中。下一节正给一个完整不在像中的实际路径类别。

## 5. 第二母不能消掉真实速度二次项

固定当前真实状态
$$
X=(h,k,\omega,\mathsf m)
$$
和本稿同一个规范。令速度为
$a=(\gamma,\upsilon)=(h_s,k_s)$。原 second 分子对这两个速度仿射，所以(15)的括号具有形式
$$
a^{\mathsf T}C(X)a+2b_v(X)\cdot a+c_v(X).
\tag{18}
$$
新增 $q_v$ 只改变 $b_v,c_v$，不改变 $C$。同样，(14)只改变无速度项，不能改变这个二次矩阵。

这里按 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md) §1 固定
$
z=x+\omega,\qquad e=hz-k,\qquad Q=1+e^2.
$
原 [R507](R507-real-nonsecant-scalar-return-loops-under-one-complete-ruling.md) §2(7)–(8) 的真速度 Gram 给
$$
\boxed{C(X)>0}
\tag{19}
$$
在 $h>0,x+\omega>0$ 的每个实际状态上成立。为明确范围，其速度变分分子为
$$
\delta V_Z=(a_*/h,0,e a_*/h),\qquad
a_*=\delta\gamma\,a_h+\delta\upsilon\,a_k .
$$
在最右非零微包上，提出该包的非零公共系数 $R_n$ 后，
$
a_*'=\frac{Q}{8h^2}
\{\delta\gamma\,u'-(\delta\gamma z-\delta\upsilon/2)u''\}u''' .
$$
若真实 Gram 为零，右 collar 先迫 $a_*=0$。令括号为 $L$，则
$(L^2)'=-2(\delta\gamma z-\delta\upsilon/2)Lu'''=0$，平端给 $L=0$。当 $\delta\gamma=0$ 时非零母迫 $\delta\upsilon=0$；当 $\delta\gamma\ne0$ 时，该一阶关系及两侧光滑平端迫 $u=0$，矛盾。若其线性系数在内部过零，$u'$ 与 $u''$ 的连续性同样把两侧的线性解系数都迫为零，不能在该点粘一个新的紧解。

所以新规范不能把完整能量变成没有速度平方的自由两输入控制。其准确点态判据只是
$$
\Delta_v(X):=
b_v^{\mathsf T}C^{-1}b_v-c_v .
\tag{20}
$$
允许速度集为空、一个点或一个椭圆，分别对应 $\Delta_v<0,=0,>0$。这个判据必须随真实
$\mathsf m_s=M_{\rm raw}(X,a)$ 同时演化；不能逐点独立选择一个方便的 history。一个预设状态域内椭圆非空，也不自动证明原两端、frame、全部矩阵或 period 可连接。

## 6. 常态区段的严格非零二次系数

假设真实词包含一个正长度的开区段，其全部 scalar 为常数
$$
h=h_c>0,\qquad k=k_c,\qquad\omega=\omega_c.
\tag{21}
$$
frame 仍按原方程旋转，不是把整个几何场常数化。令
$$
M_c=M_{\rm raw}(h_c,k_c,\omega_c,0,0),\qquad
q_c=\Phi_{M_c}(\Delta).
$$
从该区段真实左端起记实际时间 $t$。原历史准确是
$$
\mathsf m(t)=\mathsf m_*+tM_c .
$$
因此在适应 frame 的原分子中，
$$
V_{Z_{\rm can,\Delta}}'(t)
=V_*'-tV_{Y_{q_c}}'.
\tag{22}
$$
$V_*'$ 保传入矩阵和原局部 second 场。frame 的共同旋转不改变(12)的内积。

(12)(22)立即给：
$\mathscr E_{\rm can}$ 是 $t$ 的二次多项式，其二次系数为
$$
\mathcal E_c(q_c,q_c)
=\frac1{h_c}\int|V_{Y_{q_c}}'|^2;
\tag{23}
$$
$\mathcal B_s(q_0+q_v)$ 对 $t$ 至多一次；三个几何权均为常数。故(16)若在整个开区段成立，必须有
$\mathcal E_c(q_c,q_c)=0$。

下面从原 tail 证明该系数严格正，而不是留下一个条件性平方。

取整个实际库中最右一个最细微包 $u_n$，其真实 $R_n\ne0$。在它左侧、前一包右侧的开放 gap 上，所有局部 outer 数据为零，只有该右包的真尾贡献。[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)(1)(2)在常 scalar 下给
$$
\boxed{
q_c(x)=
R_n\,\frac{K_0(x)}{8h_c}\,
J_e(u_n,u_n),
}
\tag{24}
$$
$$
K_0(x)=k_cz^2-\frac{k_c^2+1}{h_c}z,\quad
z=x+\omega_c,
$$
$$
J_e(u_n,u_n)=
\int\{[1+(h_cx+d_c)^2]u_n''{}^2
+2h_c^2u_n'{}^2\}>0,\qquad d_c=h_c\omega_c-k_c .
\tag{25}
$$
$J_e$ 是整个右微包的固定真值，不把单包矩置零。$K_0$ 不可能在一个开放 gap 恒零，因为 $h_c>0$ 且 $k_c^2+1>0$；$k_c=0$ 时它也等于 $-z/h_c$。因此(24)给
$$
q_c\not\equiv0.
\tag{26}
$$
全圆 $\Delta$ 的三矩使 $q_c$ 在两端 collar 都零。若(23)为零，则其第一分量给 $q_c''=0$，双 collar 紧性再迫 $q_c=0$，与(26)矛盾。故
$$
\boxed{\mathcal E_c(q_c,q_c)>0.}
\tag{27}
$$

**常态区段排除定理。** 本稿字面同形第一圆上，任何含(21)正长度开区段的真实词，都不能由一个固定(5)和一个固定第三规范满足整个第四 ruling。无论选择什么紧母 $v$、无论其幅度多大、无论如何保真实传入矩阵，(16)的右侧都有不可被左侧消去的严格正二次系数(27)。

这不是重新锚定 history 的结论。区段入口 $\mathsf m_*$ 只改变(22)的零次与一次项；两端桥、第三规范或在区段外添加的成本也不能取消区段内部一个非零二次多项式。

它同时解释 [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md) 的常态平方门在当前新库上为何真非零。该稿(39)的 canonical 二次项不依赖初始 $w,\chi$；本稿完整同形包装消其 $Y$–third 项，剩下(27)。所以允许更一般的、仍不随 $s$ 改变的二阶规范，也不能以初始数据改掉这个最高二次系数。这里仍只讨论本稿同一个第一圆，未排除别的圆或别的机制。

## 7. 原全词、period 与成本如何接线

(15)(16)作用于一条实际词的全部位置。若要通过它求全局规范，必须把所有原桥、标记段、返回段和端 germs 放入同一个函数方程；不能分别对每一段选一个 $(v,\nu_*)$ 后相加。

新增规则(3)的输出真紧，因此 R408 §6 的 universal 提升适用。若固定基准 $B_0$ 的单 self 带左尾，不把它直接称为 compact-output 规则；在当前圆上，$B_0\Delta$ 与 $B_0(f,g)$ 都真紧，可以按 R408 §7 的两个真实 Gram 泛函作一次固定有限秩提升，再与(3)相加。这个提升只用于准确识别当前规范的周期改变量，不改变实际(5)。

只有在同一真实词另外满足
$$
M=0,\qquad T=\tau\mathfrak H
$$
时，才可调用 R408 的完整周期公式
$$
\Delta V_\theta=2\tau L_f(w_\theta).
\tag{28}
$$
本稿没有借(28)删除局部(13)的平方，也没有从(16)推出上述两条低阶总端点条件。完整期函数的 affine 尾、包总量、全部内部部分通量和原十三行仍按同一个 $w_\theta$ 联立。

同样，(14)是同一个实际第三规范。它承担的平方仍保在原完整 forcing、传递和成本中；若后来改变路径或初始数据，全部 $\delta X^*$、真倒行、原 prototype 乘数及 Klein 基准继续由那条实际词恢复。一个有限秩规则或一个线性规范解，不是一个负时间几何块，也不自动属于原 canonical 成本空间 $U$ 或响应空间 $R$。

## 8. 对下一条实际连接的具体影响

本稿给出两个可以直接用于后继的准确判断。

第一，在固定真实词上，新增第二母和同一个第三 Gram 的问题确已降到(16)这一个线性全路径方程；未知母只通过(17)的有限真实线性泛函进入。任何要用它支付某条非恒长程桥的方案，都可以直接检验该完整右端是否属于这个像，而无需把原 square 当成新的非线性 profile 自由度。

第二，它没有清掉(18)的严格正速度二次 Gram，并且不能修复任何正长度常 scalar bulk。原 R70 常态圆加桥的总矩阵控制即使已经成功，仍不能作为当前同形圆的完整 ruling 词；必须先改变其真实内部几何。这个排除是整个该词的实际失败结论，不是说“尚未找到合适 $v$”。

本稿未证明存在一个同规范、全部 $M=0$、完整 period 归零的非恒闭词，也没有把每个状态的椭圆非空授为这种路径存在。R508/R509 的非正割局部实际出口仍有效，R509 的短段单侧矩阵边界也仍有效；下一步必须在同一个(16)和真实矩阵 ODE 下走出那个短段范围。固定度量有限等距族、闭嵌入及厚度主门仍未达成。
