# R236：二次扭曲与分歧平移的正投影，及剩余阶四非 CM 非消失

日期：2026-11-13。状态：**已证明。**

本篇处理 R226/R227 后真正剩余的 $p\equiv7\pmod8$ 阶四分支。
用一个保持原实际深度零特征线的全局 involution 消去全部 CM 谱；
其混合相对迹没有 singular 主项，regular 误差与 R213 完全同阶，
只增加系数二。证明 CM 符号一致时使用 Deuring 的准确固定点数，
并逐个证明固定点的扭曲符号；不把二次自扭曲、普通 Jacquet–Langlands
对应或正根数当成未经证明的符号兼容。

## 1. 对象与结论

保留 R213 的实际小惯性分支、同一个 $K$、$\lambda$ 和实际三次角色。
现在设

$$p\equiv7\pmod8,\qquad \operatorname{ord}(\theta)=4,
\qquad \Xi=(\theta\vartheta^{\pm1})\circ\lambda,\qquad\Omega=\Xi^{-1}.$$

因 $p\equiv2\pmod3$，实际有 $p\equiv23\pmod{24}$。
$\Omega$ 的阶为十二，且 $\Omega|\mathbb A_{\mathbb Q}^{\times}=1$。
R226 给 $\theta(z_2)=1$，故它的 prime-to-$p$ 准确环类导子是 $a=c$。
仍记

$$D=|D_K|,\quad M=Da^2,\quad h=h(\mathcal O_a),\quad
a_D=\prod_{q\mid D}q^{v_q(a)},\quad a_0=a/a_D,$$

$$\mathcal L_a=\prod_{q\mid a}(1-\chi_K(q)/q)^{-1},\qquad
\mathcal T(M)=\max_{1\le m<M}\tau(m).$$

这里 $a_D\mid9$，但下面的精确不等式保留 $a_D$。

**定理 236.1。** 若

$$\boxed{
p>\frac{2a_D^2\,4^{\omega(D)}16^{\omega(a_0)}
\mathcal T(M)^2 M}{h\mathcal L_a^2},
}                                                        \tag{236.1}$$

则存在平凡 nebentype、权二、准确水平 $p^2$、有限尖点参数
$\{\theta,\theta^{-1}\}$ 的**非 CM** 新形式 $f$，使

$$\boxed{L(\tfrac12,\pi_{f,K}\otimes\Xi)\ne0.}            \tag{236.2}$$

这对两个实际三次符号分别成立。没有另选 Hecke 素数，亦不要求
$D$ 固定或 $p\nmid aD$ 以外的新素数互素条件。

沿用 R213 §6 的有效有限乘积 $X_u,T_u,\beta_u$，可取

$$\boxed{C^{\rm tw}_\epsilon=
324X_{\epsilon/4}T_{\epsilon/8}^{\,2}\beta_{\epsilon/2}^{-2}} \tag{236.3}$$

使 $p\ge C^{\rm tw}_\epsilon M^{1+\epsilon}/h$ 推出 (236.2)。
因此对每个 $\nu>0$，有与 $K,a,p$ 全无关、一般无效的常数
$C_\nu$，使 $p\ge C_\nu M^{1/2+\nu}$ 推出同一非 CM 非消失。

## 2. 保持实际特征线的 involution

令

$$F=\mathbb Q(\sqrt{-p}),\qquad\chi=\chi_F,
\qquad B=B_{p,\infty},\qquad L=K_p.$$

在 $B_p$ 中选 $j$ 满足

$$j^2=-p,\qquad jz=\bar z j\quad(z\in L).                \tag{236.4}$$

这是可能的：$L/\mathbb Q_p$ 不分歧，$B_p$ 是唯一的 division
四元数代数，而 $-p$ 的赋值为奇数。把 $j$ 也记为只在 $p$ 处
非平凡的有限 adelic 元。其 reduced norm 为 $p$，且
$\chi_p(p)=1$；后者亦由 $p=N_{F_p/\mathbb Q_p}(\sqrt{-p})$ 直接得到。

在平凡中心角色的 quaternionic 自守 Hilbert 空间上定义

$$({\cal M}_\chi\phi)(g)=\chi(\operatorname{Nrd}g)\phi(g),
\qquad S=R(j){\cal M}_\chi.                              \tag{236.5}$$

$\mathcal M_\chi$ 良定义：全局有理 reduced norm 为正，故有限部分的
$\chi$ 在左边 $B^\times(\mathbb Q)$ 上为一；中心 reduced norm 为平方。
它是酉算子，且 $\mathcal M_\chi$ 与 $R(j)$ 交换。
由 $j^2=-p$ 为局部中心元，

$$\boxed{S^*=S,\qquad S^2=1.}                           \tag{236.6}$$

记 $U_B^1=1+\mathfrak P_B$，
$J=L^\times U_B^1=\mathbb Q_p^\times\mathcal O_{B_p}^{\times}$。
$\theta$ 通过
$\mathcal O_{B_p}^{\times}/U_B^1=\mathbb F_{p^2}^{\times}$ 延拓到 $J$，
在中心上为一。对单位有

$$\theta^2(u)=\chi_p(\operatorname{Nrd}u).                \tag{236.7}$$

确实，两边都是 $\mathbb F_{p^2}^{\times}/\mathbb F_p^{\times}$
的唯一非平凡二次字符。$\mathcal M_\chi$ 因而把右 $\theta$ 特征线
送到右 $\theta^{-1}$ 特征线，而任意 division 一致化元的共轭在
剩余域上为 Frobenius，$R(j)$ 把它送回 $\theta$ 特征线。

在 $q\ne p$，$\chi_q$ 未分歧，因此
$\chi_q\circ\operatorname{Nrd}$ 在**任何共轭极大序单位群**上为一。
所以 $S$ 保持 R213 在全部位置选取的同一个测试向量空间 $H$。
该空间在每个 $\pi\in\mathcal F_\theta(p^2)$ 上为一维，且没有
一维自守表示；$\theta$ 阶四已排除后一种可能。

R213 的 $R(f)$ 是一个正标量乘 $H$ 上的正交投影。
因此 $S$ 与 $R(f)$ 交换；这里不需要 $S$ 与所有 Hecke 算子交换。

## 3. 全部 CM 成分上的符号相同

先在一个参考极大序上证明共同符号为 $+1$，再回到实际的
Gross–Prasad 共轭极大序和 (236.4) 的 $j$。

### 3.1 参考序上的有限空间与固定点符号

$F$ 在 $p,\infty$ 都不分裂，故可嵌入 $B$。固定一个全局
$j_0\in B$，$j_0^2=-p$，以及包含 $\mathbb Z[j_0]$ 的极大序 $R_0$。
用只在 $p$ 处等于 $j_0$ 的 adele 定义 $S_0$。
在 $p$ 用同一个 $\theta$；在所有其他有限处用 $(R_0)_q^\times$。
所得空间记为 $H_0$。

每个右理想类都贡献 $H_0$ 的一维。需要核查的是单位的 $\theta$
值。任一共轭极大序的单位在无穷处有正范数，且为整单位，所以范数
为一；其整迹位于 $\{-2,-1,0,1,2\}$。其阶因此为 $1,2,3,4,6$。
$\theta$ 在中心和三阶元上为一；对阶四元，其 projective 剩余类是
阶二元，值为

$$(-1)^{(p+1)/4}=1\qquad(p\equiv7\pmod8).$$

所以这些单位均被 $\theta$ 杀死。于是 $S_0$ 在按极大序右理想类
给出的基中是一个带单位复数权的置换。

若类 $[g]$ 被 $R(j_0)$ 固定，中心的 $\mathbb Q$ 类数一允许写成

$$g j_0=\gamma g u,
\qquad\gamma\in B^\times(\mathbb Q),
\quad u\in\widehat R_0^{\times}.                        \tag{236.8}$$

比较 reduced norm 的各有限赋值得 $\operatorname{Nrd}\gamma=p$。
在 $q\ne p$，$g_q^{-1}\gamma g_q$ 为整单位；在 $p$，$\gamma$ 的
division 赋值为一，故其 reduced trace 属于 $p\mathbb Z_p$。
因此 $\operatorname{Trd}\gamma\in p\mathbb Z$。
正定性给 $|\operatorname{Trd}\gamma|<2\sqrt p$；$p>4$，所以

$$\operatorname{Trd}\gamma=0,\qquad\gamma^2=-p.$$

由 Skolem–Noether，用一个全局 $x\in B^\times(\mathbb Q)$ 共轭并
将 $g$ 左乘 $x^{-1}$，可假设 $\gamma=j_0$。这不会改变
$\chi(\operatorname{Nrd}g)$。

现在逐处算固定点对 $\operatorname{tr}S_0$ 的权。

在 $q\ne2,p$，$\mathbb Z_q[j_0]=\mathcal O_{F,q}$。
若 $q$ 在 $F$ 分裂，则 $\chi_q=1$。若它惰性，(236.8) 说明
$g_qR_{0,q}$ 对应的格由 $\mathcal O_{F,q}$ 保持。
未分歧二次域上的秩一格是主格，因此
$g_q\in F_q^\times R_{0,q}^{\times}$，从而
$\chi_q(\operatorname{Nrd}g_q)=1$。在 $2$，由于
$-p\equiv1\pmod8$，$F$ 分裂，故同样 $\chi_2=1$。

在 $p$，$F_p/\mathbb Q_p$ 分歧，故
$B_p^\times=F_p^\times\mathcal O_{B_p}^{\times}$。写
$g_p=m k$，其中 $m\in F_p^\times$，$k\in\mathcal O_{B_p}^{\times}$。
由 (236.8)，

$$u_p=k^{-1}j_0^{-1}k j_0.$$

$j_0$ 共轭在剩余域上为 Frobenius，所以

$$\theta(u_p)=\theta(k)^{-2}
=\chi_p(\operatorname{Nrd}k)
=\chi_p(\operatorname{Nrd}g_p).$$

最后一步用 $\chi_p$ 杀死 $F_p$ 的范数。因此在固定点上

$$\boxed{\chi(\operatorname{Nrd}g)\theta(u_p)=1.}          \tag{236.9}$$

这是真正的符号计算；没有将“固定类存在”直接等同于“迹贡献为正”。

### 3.2 Deuring 计数迫使每个 CM 符号为正

极大序右理想类与特征 $p$ 的几何超奇异椭圆曲线同构类对应，
范数 $p$ 的唯一双边素理想作用对应 Frobenius。
因此上述置换固定点恰为 $\mathbb F_p$ 中的超奇异 $j$ 值。
Deuring 的准确公式在 $p\equiv7\pmod8$ 时给其数目为 $h(-p)$。
配合 (236.9) 得

$$\boxed{\operatorname{tr}(S_0|H_0)=h(-p).}               \tag{236.10}$$

相应的两项标准输入分别见 Voight, *Quaternion Algebras*,
§42.2.4、Theorem 42.3.2、§42.3.13，以及 Nakaya (2019),
作者稿 p.2, Theorem 2。这里只使用其理想类/Frobenius 对应与准确
有限计数，不从它们取得任何变化域的分析常数。

$\mathcal M_\chi$ 把 $\pi$ 送到 $\pi\otimes\chi$，而右平移不改变
其自守表示。因此非自扭曲的两个表示对 $\operatorname{tr}S_0$ 的
总贡献为零。$\pi\simeq\pi\otimes\chi$ 恰是来自 $F$ 的 CM
表示。R181 §5 已完整计数：准确水平 $p^2$、平凡 nebentype、这一
阶四有限类型的 CM 空间维数恰为 $h(-p)$。每个这样的表示在
$H_0$ 中贡献一条线，$S_0$ 在其上为 $\pm1$。
(236.10) 因而迫使全部 $h(-p)$ 个符号都是 $+1$。

### 3.3 回到实际测试函数

每个 $q\ne p$ 的实际 Gross–Prasad 极大序都可写成
$g_q(R_0)_qg_q^{-1}$，且除有限多个 $q$ 外可取 $g_q=1$。
记 $g^{(p)}$ 为这些共轭元的 adele。由

$$S_0R(g^{(p)})
=\chi(\operatorname{Nrd}g^{(p)})R(g^{(p)})S_0,$$

实际空间的全部 CM 符号只乘同一个 $\pm1$。
又 $j j_0^{-1}\in\mathcal O_{B_p}^{\times}$，范数为一，故
$\theta(jj_0^{-1})\in\{\pm1\}$；把 $j_0$ 换成 (236.4) 的 $j$
再使全部符号同乘此数。

因此存在一个由实际序和 $j$ 决定、与 CM 形式无关的
$\varepsilon\in\{\pm1\}$，使

$$\boxed{S|H_{\rm CM}=\varepsilon\operatorname{id}.}      \tag{236.11}$$

可以用上述参考序和共轭元精确计算 $\varepsilon$；下述绝对值估计
对两个符号相同，不需要另外选择有利的实际类型。

## 4. 正谱过滤与混合核

定义

$$P_{\rm nc}=\frac{1-\varepsilon S}{2},
\qquad A=R(f)P_{\rm nc}.                               \tag{236.12}$$

$P_{\rm nc}$ 为正交投影，且与 $R(f)$ 交换，所以 $A$ 为正算子；
由 (236.11) 它杀死全部 CM 谱。它可保留非 CM 扭曲对的线性组合，
这无碍：若这种组合有非零 $\Omega$ 周期，其中至少一个非 CM
表示的同一个实际测试向量具有非零周期，Waldspurger/Pi 谱公式遂给
(236.2)。不要求筛后的谱分解仍逐个形式对角化。

令 $J_S$ 是 $R(f)S$ 的同一双环面周期分布。则

$$J(A)=\frac{J(f)-\varepsilon J_S}{2}\ge0.               \tag{236.13}$$

设 $f_j(x)=f(xj^{-1})$，只在 $p$ 平移。右卷积约定给

$$R(f)S=R(f_j)\mathcal M_\chi,$$

其核为

$$K_S(g,h)=\chi(\operatorname{Nrd}h)
\sum_{\gamma\in B^\times(\mathbb Q)/\mathbb Q^\times}
f_j(g^{-1}\gamma h).                                  \tag{236.14}$$

因此它的几何展开使用两个环面角色 $\Omega$ 与
$\Omega\chi_K^F$，其中
$\chi_K^F=\chi\circ N_{K/\mathbb Q}$。这些是**同一实际角色的**混合
周期，而不是更换了可自由选择的辅助角色。

## 5. 混合迹的两个 singular 轨道均消失

实际角色有精确等式

$$\boxed{\Omega^6=\chi_K^F.}                            \tag{236.15}$$

证明：$\theta^2$ 是 Cartan 的唯一二次角色，即行列式的 Legendre
字符；$\det\bar\rho_{E,p}$ 是模 $p$ 圆分字符。
$p\equiv3\pmod4$ 时对应二次域正是 $F$。三次因子取六次后消失，
$\theta^{-6}=\theta^2$，得到 (236.15)。

恒等 singular 轨道的稳定子角色为 $\chi_K^F$；它非平凡，因为
$F\ne K$，前者在 $p$ 分歧而后者在 $p$ 惰性。其积分为零。
非平凡正规化子 singular 轨道的稳定子角色为
$\Omega^2\chi_K^F=\Omega^8$ 或其逆，阶为三，积分也为零。
因此

$$\boxed{J_{S,\rm irreg}=0.}                            \tag{236.16}$$

这一步使用真实稳定子上的角色正交性；不是对 regular 估计进行
形式相减。恒等轨道也可直接由 $p$ 处的奇赋值支集看出为零。

## 6. 混合 regular 误差的完整统一界

### 6.1 $p$ 处的支集与单位相位

R213 的测试函数为

$$f_p(zu)=\theta(z)^{-1}\quad(z\in L^\times,u\in U_B^1),
\qquad f_p=0\quad\hbox{在 }B_p^\times\setminus J.$$

平移 $f_{j,p}(x)=f_p(xj^{-1})$ 支撑在 division 奇赋值陪集 $Jj$。
写 regular 代表为 $1+jx$，$\xi=-p x\bar x$。
$v_p(\xi)=1+2v_p(x)$ 为奇数。两个环面变量可取单位代表，所以
奇赋值支集等价于

$$\boxed{v_p(\xi)<0.}                                  \tag{236.17}$$

在这个范围内令 $x=p^m u$，$m\le-1$。
将 $1+jx$ 乘中心 $p^{-m}$ 后，右乘 $j^{-1}$，其剩余单位就是
$\bar u$；其余项属 $\mathfrak P_B$。
对 $t_1,t_2\in\mathcal O_L^\times$，被积函数中的相位为

$$f_{j,p}(t_1^{-1}(1+jx)t_2)
\Omega_p(t_1)^{-1}\Omega_p(t_2)
\chi_p(Nt_2)
=\theta(u)\theta(t_2)^4=\theta(u).$$

这里用 $\Omega_p=\theta$、$\chi_p\circ N=\theta^2$；中心 $p$ 的值
为一。R213 归一化下 $\operatorname{vol}(\mathbb Q_p^\times\backslash
L^\times)=1$，故

$$\boxed{|I_{S,p}(\xi)|\le1,\qquad
I_{S,p}(\xi)=0\text{ 若 }v_p(\xi)\ge0.}                \tag{236.18}$$

### 6.2 其余地方仍是支撑体积上界

在 $q\ne p$，测试函数没有改变，两个角色只相差未分歧的
$\chi_q\circ N$，故准确单位导子相同。
R213 所用的误差上界同样适用于这两个不同角色：
Feigon–Whitehouse 作者稿 pp.31–34 的 Lemma 4.15 及
Lemmas 4.17–4.19 在换元后直接取绝对值，留下

$$\operatorname{vol}(T_q\cap R_q^\times)
\operatorname{vol}\{z: \text{相应 regular 代表可进入 }R_q^\times\}.$$

额外的混合角色只有模一的相位，不改变任何支撑体积。
这些引理在未分歧二次代数的常数为一；在 $q\mid D$，仍用 R213
直接的紧环面界 $4q^{-v_q(D)}$，避免任何依赖局部域的未知常数。
无穷处仍不超过四。

于是所有局部权完整保留。设

$$B_q(j)=\begin{cases}
L_q^2q^{-2n_q+j/2},&0\le j<2n_q,\\
L_qq^{-n_q},&j=2n_q,
\end{cases}\quad
n_q=v_q(a),\quad L_q=(1-\chi_K(q)/q)^{-1}.$$

### 6.3 反向端点使算术进程仍通过零

无穷处和 $q\ne p$ 的原支撑给

$$\xi=\frac{y}{y-M},\qquad0<y<M,\qquad y\in\mathbb Z.$$

由 $p\nmid M$，(236.17) 等价于

$$\boxed{p\mid M-y.}                                   \tag{236.19}$$

不能直接把这个平移进程按 $M/p$ 计数而漏掉 $+1$；真正可用的是
**换到另一个端点**。令 $z=M-y$，则 $0<z<M$、$p\mid z$。
对 $q\mid a_0$ 有 $v_q(M)=2n_q$，从而严格恒等

$$\min(v_q(y),2n_q)=\min(v_q(M-y),2n_q).                 \tag{236.20}$$

除数函数乘积 $\tau(y)\tau(M-y)$ 也对称。因此原来的局部加权上界
逐项变成

$$|I_S(\xi_y)|\le
\frac{4\,4^{\omega(D)}}D\tau(z)\tau(M-z)
\prod_{q\mid a_0}B_q(\min(v_q(z),2n_q)).                \tag{236.21}$$

固定这些截断赋值 $j_q$，允许的 $z$ 全是
$p\prod q^{j_q}$ 的正整数倍，个数确实至多 $M/(p\prod q^{j_q})$。
用 R213 的逐素数有限和

$$\sum_{j=0}^{2n_q}q^{-j}B_q(j)<16q^{-2n_q}$$

得到与原迹完全相同的误差

$$\boxed{|J_S|\le E,
\qquad E=\frac{4a_D^2\,4^{\omega(D)}16^{\omega(a_0)}
\mathcal T(M)^2}{p}.}                                  \tag{236.22}$$

证明中没有新增 $D$ 依赖或关于变化环类导子的固定参数常数。

## 7. 正主项、阈值与接回全部类型

R213 已给

$$J(f)=\frac{4h\mathcal L_a^2}{M}+I_{\rm reg}(f),
\qquad |I_{\rm reg}(f)|\le E.$$

由 (236.13) 和 (236.22)，

$$J(A)\ge\frac12\left(\frac{4h\mathcal L_a^2}{M}-2E\right).$$

(236.1) 使右端严格为正。§4 的正谱论证给一个非 CM 的非零实际
环面周期，继而给 (236.2)。$\Omega$ 与 $\Xi$ 的中心值相同仍由
基变换的 Galois 不变性及 $\Xi^\sigma=\Xi^{-1}$ 得到。

有效常数 (236.3) 是 R213 在 $a=c$ 时的常数 $162$ 的两倍；
相同的统一 Siegel/环类数下界给所述平方根形式。

令 $a^*=bc$、$M^*=D(bc)^2$。结合 R213（阶数大于四）、
R227（$p\equiv3\pmod8$ 的阶四）、本文（$p\equiv7\pmod8$ 的阶四），
以及 R87 的旧 Steinberg 参数，得到全部实际参数共用的有效充分条件

$$p\ge C_\epsilon\frac{(M^*)^{1+\epsilon}}
{h(\mathcal O_{bc})}.                                  \tag{236.23}$$

这里 $C_\epsilon$ 可取上述各已给有效常数的最大值；R213 的
环类数比单调性说明 $a\mid bc$ 时该条件涵盖每个实际准确导子。
每个需要的尖点类型都得到非 CM 非消失，R172 的有限有理投影、
R177 的全类型单位理想、R181 的实际整行接口遂给

$$\boxed{
p\ge C'_\nu(M^*)^{1/2+\nu}
\quad\Longrightarrow\quad j(E)\in\mathbb Z
}                                                        \tag{236.24}$$

对**全部**实际小惯性同余分支成立。这里一般无效的常数只来自
已明确标出的统一 Siegel 下界；(236.23) 本身有效。

特别，任一非整 $j$ 的实际异常表示都满足

$$M^*\gg_\delta p^{2-\delta}\quad(\delta>0).             \tag{236.25}$$

与 R220 同一全局二次扭曲导子结合，
$N_{E'}\gg_\delta D T p^{4-\delta}\gg_\delta Dp^{5-\delta}$。
这消除了阶四过滤原有的 $1/(2-1/\sqrt e)$ 指数损失，
但依然没有给 $M^*$ 上界，也没有排除整 $j$ 的实际异常曲线。
因此本篇仍不是主题 README 所要求的绝对 Serre 一致性终结。

## 8. 已发表来源与准确范围

1. Tomoaki Nakaya, *The number of linear factors of supersingular polynomials
   and sporadic simple groups*, **Journal of Number Theory 204** (2019),
   471–496, DOI [10.1016/j.jnt.2019.04.015](https://doi.org/10.1016/j.jnt.2019.04.015)。
   [作者稿](https://arxiv.org/pdf/1809.02363)，p.2, Theorem 2，明确列出
   $p\equiv7\pmod8$ 时的数目 $h(-p)$；只使用这一已发表的经典
   Deuring 公式。
2. John Voight, *Quaternion Algebras*, GTM **288**, Springer (2021),
   [Chapter 42](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)，
   pp.783–797；§42.2.4 给范数 $p$ 双边素理想与 Frobenius 的对应，
   Theorem 42.3.2 给超奇异曲线与理想类对应。固定点的额外二次
   扭曲符号是本文 §3.1 的新计算，没有隐含引用归一化的扭曲 JL。
3. Brooke Feigon and David Whitehouse, *Averages of central L-values of
   Hilbert modular forms with an application to subconvexity*,
   **Duke Math. J. 149** (2009), 347–410，
   [作者稿](https://bfeigon.ccny.cuny.edu/Average_L-values.pdf)，
   pp.31–34, Lemmas 4.15–4.19。本文用其直接绝对值/支撑体积证明，
   并明确解释为何适用于两个相差未分歧字符的混合角色；分歧于 $K$
   的地方只用直接的 $4q^{-v_q(D)}$ 紧性界。
4. Qinghua Pi, **JNT 191** (2018), 213–245，
   [作者稿](https://arxiv.org/abs/1707.07307)，§2.3–2.4、Proposition 5.1
   及 Lemmas 6.1–6.6；R213 已逐式匹配的原主项与局部归一化。
   本文混合核的恒等式、两个 singular 项、$p$ 处相位及整数求和
   都已重新证明。
5. R181 §5：阶四 CM 谱的准确维数；R214/R226：同一实际导子
   和二进分支；R213/R227：其他类型的非消失与有效常数；
   R172/R177/R181：实际有限投影、全类型单位理想与整性接口。
