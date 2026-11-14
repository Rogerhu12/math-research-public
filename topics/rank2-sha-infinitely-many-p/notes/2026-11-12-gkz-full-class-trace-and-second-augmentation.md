# GKZ 的完整类群迹与原二阶增广行

日期：2026-11-12。状态：**下述对象比较和等变维数命题已证明。**
本篇核查的是 R130、R150、R154 的原完整 Heegner 点，不能用
未取全类群迹的单点或任意环面标记替代。结论不排除新的
非等变算术构造，也不声称已经控制原二阶矩。

## 1. 先保留原来的两个不同迹

固定本课题的一个 Heegner 域 $F$，取已经付清 Hall 分裂的
实际环类群
$$
 {\cal H}_\ell=C_\ell\times U\times\Gamma,\qquad
 \Gamma=\langle\tau\rangle\simeq C_p,\quad
 |C_\ell|=h_F,\quad |U|=u,\quad \ell+1=pu .
 \tag{1}
$$
这里 $C_\ell$ 是 R150 的真正阶二类群提升；$U$ 是原 cofactor
子群，不能因为 $p\nmid u$ 就从点的定义中删去。对以同一尖点
归零的原模参数化像 $P_\ell$，原点是
$$
 Q=[t_0]\sum_{c\in C_\ell,\ v\in U}P_\ell^{cv},\qquad
 N_\Gamma Q=0,\qquad N_\Gamma=\sum_{j=0}^{p-1}\tau^j .
 \tag{2}
$$
等式包含固定的杀扭整数 $t_0$。R154 在固定商上把
$C_\ell$ 和吸收进实际映射 $\Psi_D$，只把 (2) 改写成同一个
$u$ 项迹，并没有改变其值或产生一个 $h_F$ 因子。

因此原始完整类群和准确是
$$
 [t_0]\sum_{\sigma\in{\cal H}_\ell}P_\ell^\sigma
                =N_\Gamma Q=0.
 \tag{3}
$$
本题所需的行却是
$$
 D_2=\sum_{j=0}^{p-1}\binom j2\tau^j
 \tag{4}
$$
作用于原点的全部 $p$ 进完成中的规范对数列，见 R130、R161。
即使 (3) 为零，(4) 仍可能非零；把两者相同化会删掉正需要
研究的增广信息。

## 2. 原 GKZ 定理取的确实是全迹，并且经过 Fricke-plus

Gross–Kohnen–Zagier（1987）在引言印页 498–499 以全部
$h_F$ 个 CM 点之和定义 $P_{D,r}$，再减去相同次数的尖点，
得到 $y_{D,r}$；继而推到
$$
 J^*=\operatorname{Jac}(X_0(N)/w_N).
 \tag{5}
$$
其 Theorem C（印页 503）在 $J^*(\mathbb Q)\otimes\mathbb R$
的 $f$ 分量中描述这些全迹的共线性和 Jacobi 系数。
这个分量要求 $w_N$ 对微分的特征值为 $+1$，相应权二
$L$ 函数根数为 $-1$。原文 Theorem C 还保留
$(D,2N)=1$，不能把它未经另证直接当作本课题全部偶判别式
的版本。

对当前 $E389$，R157 已证
$$
 \pi w_{389}=-\pi,\qquad w_{389}f=-f .
 \tag{6}
$$
所以它的 $f$ 分量不在 (5) 中。单凭原 GKZ 的固定 Jacobi
级数，尚未进入 $E389$ 所在的 Fricke 分量；不应先赋予该
级数一个本曲线的非零原始基向量。

即使改用没有经过 (5) 的原完整 Heegner 除子，(3) 仍准确
说明其当前椭圆像已取了 $N_\Gamma$。这项判断不依赖
Fricke 的符号，也适用于原 $E17$ 的完整类群迹。

### 非基本判别式的旧导子项

GKZ IV §1（印页 541–542）的除子按 Hurwitz 规范包含
非本原二次型。若 $D$ 是本题的基本判别式、$\ell\nmid DN$，
则判别式 $D\ell^2$ 的二次型只有内容 $1$ 或 $\ell$ 两种。
内容为 $1$ 的部分是导子 $\ell$ 的完整环类轨道；内容
$\ell$ 的型除以 $\ell$ 后是判别式 $D$ 的原基层轨道，
平方根标签相应除以 $\ell$。本题 $D\ne-3,-4$，无额外
单位权。减去次数后的除子也按这两部分相加。

因此不能只写“非基本系数等于导子 $\ell$ 的原始轨道”。
不过在本题实际 $\Psi_D$ 下，前一部分由 (3) 消掉，
后一部分是已经由 $t_0$ 杀掉的基层完整迹；这些旧项不
恢复 (4)。这与原文 V §2 印页 558 通过 Hecke 递推处理
非基本判别式的方式相容。

## 3. 二次 genus 权在 $C_p$ 上恒为一

原文 I §2（印页 508–510）的 genus character 来自二次
Kronecker 符号。在一个固定的本原理想类轨道上，它是
取值 $\{\pm1\}$ 的同态 $\varepsilon$；非本原扩展可能为
零，须先按上一节拆开，而不能把零值当作新 $p$ 阶字符。

因为 $p$ 为奇数，
$$
 \varepsilon(\tau)^p=1,\qquad \varepsilon(\tau)^2=1
       \quad\Longrightarrow\quad \varepsilon(\tau)=1.
 \tag{7}
$$
故任何这样的二次加权全迹仍准确为
$$
 \sum_{c,v,j}\varepsilon(cv\tau^j)P_\ell^{cv\tau^j}
       =N_\Gamma\sum_{c,v}\varepsilon(cv)P_\ell^{cv}.
 \tag{8}
$$
非平凡 $\varepsilon$ 可以改变 $C_\ell U$ 方向、所落的
二次扭曲及其基层点；本篇**不声称所有这些新加权迹均为零**。
但 (8) 的 $\Gamma$ 权全为一，不能等同原 $D_2$ 权。
增加有限多个二次 genus 系数也不改变这个事实。

若真正采用 $\chi(\tau)=\zeta_p$，则应保留实际整式
$$
 {\cal Q}(T)=\sum_{j=0}^{p-1}(1+T)^j Q^{\tau^j}
       =N_\Gamma Q+T D_1Q+T^2D_2Q+\cdots .
 \tag{9}
$$
这里 (9) 在点群与 $\mathbb Z_p[T]$ 的张量积中解释，
不是把点群误作一个有乘法的坐标环。代 $T=\zeta_p-1$ 后，
(9) 才是 $p$ 阶字符的点值展开。
使用 $\chi^{-1}$ 会相应更换标签和低阶三角组合。
系数域的 $\zeta_p-1$ 与原点格的 $\tau-1$ 必须分别说明；
一个复特征点非零，并未给 (9) 的指定整系数为单位。

## 4. 保留原 full-level 行时的精确等变维数界

本节仅约束以下明确类型的构造。取 R137、R145 的实际
连通 full $\ell$-level 中心商，令
$$
 k=\overline{\mathbb F}_p,\quad G=\operatorname{PSL}_2(\mathbb F_\ell),
 \quad {\cal M}=k[\mathbb P^1(\mathbb F_\ell)],\quad
 I=\ker\!\left(\sum:{\cal M}\to k\right),\quad
 V=I/k{\bf1}.
 \tag{10}
$$
保留 $p\ge7$、$p\mid\ell+1$、$p\ne\ell$ 以及原实际
$T/U=C_p$ 两半轨道。因为 $p\mid\ell+1$，$k{\bf1}\subset I$。
R145 已按 Saunders（2022）§3 的奇
$p\mid\ell+1$ principal block 结构核定
$$
                    V\text{ 不可约},\qquad \dim_kV=\ell-1.
 \tag{11}
$$
具体地，Borel 的阶素于 $p$，$\mathcal M$ 是 projective；
其秩二置换作用给
$\operatorname{End}_G{\cal M}=k[J]/(J^2)$，所以
$\mathcal M=P(k)$，其三层为 $[k\mid V\mid k]$。
这里没有套用特征零 Steinberg 不可约性。

原 $D_2B$ 的系数向量 $w_2$ 在每个 $\tau^jU$ 轨道取值
$\binom j2$。保留两半轨道后，每一值恰重复 $u$ 次，故
$$
 \sum_v(w_2)_v=u\sum_{j=0}^{p-1}\binom j2
                    =u\binom p3=0\quad\text{于 }k .
 \tag{12}
$$
它在 $j=0,2$ 分别为 $0,1$，因而
$w_2\in I\setminus k{\bf1}$。R137 的实际 Fourier 独立性
证明该行没有被同源函数间的常系数关系消掉；$E17$ 的
唯一关系为全一，$E389$ 的非零总迹情形则连这条关系也没有。

**命题。** 若 $W$ 是有限维 $kG$ 模，且构造给出
$G$-线性映射
$$
 L:I\longrightarrow W,\qquad L(k{\bf1})=0,\qquad L(w_2)\ne0,
 \tag{13}
$$
则 $\dim_kW\ge\ell-1$。

**证明。** (13) 诱导 $V\to W$。其在 $\bar w_2$ 非零，
由 (11) 不可约性必单射，所以得到所述维数界。证毕。

因此一个维数不随 $\ell$ 增长、同时满足 (13) 的线性对象
不能保留原二阶行。忘掉 full-level 标记的 $G$-不变全迹
甚至直接杀掉 $I$。该命题没有声称任意有限维算术模型都
满足 (13)，也没有禁止非线性配对、指定 CM 取值、非
$G$-等变构造或随 $\ell$ 变化的向量值模形式。特别是，
它不能把原指定 CM 纤维的非零性问题判定为不可能。

## 5. 下一步真正需要补的比较

保留原 $C_\ell U$ 迹后的 (9)，是可继续研究的
$\zeta_p$-character 对象。若用扭曲 Gross–Zagier、向量值
theta 或类群变量的模性，至少还须付清：

1. 对象确实承载 (9)，包括原 $h_F$ 类群和、$u$ 项和及
   原 CM 标签，而非只承载 (3) 或 (8)。
2. 在 $\mathbb Z_p[\zeta_p]$ 上说明整格与基向量的规范；
   特征零共线性或非零高度不等于原点的 $\delta$ 原始性。
3. 把二阶字符展开同 R130 的全部完成中 $D_2$ 检验比较；
   不能先删去 cofactor $u$，也不能以泛点行非零替代实际取值。

上述是本篇留下的实际接口，不是额外假定这些比较已经存在。

## 来源与内部依赖

- B. Gross、W. Kohnen、D. Zagier，
  *Heegner points and derivatives of L-series. II*，
  **Math. Ann. 278 (1987), 497–562**；
  [作者原文](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01458081/fulltext.pdf)：
  引言 pp. 498–499、Theorem C p. 503、I §2 pp. 508–510、
  IV §1 pp. 541–542、V §2 p. 558。上述位置已直接阅读。
- J. Saunders，*Cohomology of $\mathrm{PSL}_2(q)$*，
  **J. Algebra 595 (2022), 347–379**；
  [正式版作者稿](https://arxiv.org/pdf/2002.04183v3)，
  §3 印页 8–10；此处系数特征为其 $r=p$、其 $q=\ell$。
- R130/R161：原完整二阶局部测试；R137/R145：实际
  Fourier 行及不可约 heart；R150/R154：完整类群迹和
  固定商；R157：原 $w_{389}$ 符号。这里仅用各自已付范围。
