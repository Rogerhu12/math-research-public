# R817 — 固定普通素数的三个原负二单位值与三个固定 Heegner 循环非零

日期：2026-11-15。**状态：已证明；唯一固定素数的完整计算已在公开 Actions 成功执行。**

在固定
$$
p_*=7993,\qquad \pi_*=69-32\omega
$$
及下面明确的系数域嵌入下，R806 的三个原型四负二矩都是单位。除去保留的原普通周期后，三个余值为
$$
2522,\qquad 2828,\qquad 3696\pmod {7993}.
$$
因此 R804 的三个指定 canonical Soulé 特殊化类在这个普通素位均非零；
R814 中先于 p 固定的三个 generalized Heegner cycles 的实际 p-adic
Abel–Jacobi 配对也均非零，故这些固定循环在 Chow 群中非零。
在同一个有限 CM 轨道模中取其实际有限角色投影，三个循环还线性独立。

这不是在另一个素数的非消失结论，也没有证明原秩二曲线在7993的完整
$\Sha[p^\infty]$ 有限。原三个中央导数及 R801 的完整线性负二行与外部仍保留。

## 1. 固定对象和本篇检测的范围

沿用 [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)：
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad b=17,\quad\theta=17^{1/6}.
$$
三个实际截面是
$$
D_{j,17}(z)=\theta^{-4}D_{j,1}(\theta z),\qquad
[z^4]D_{j,b}=1,\qquad j\in\{4,10,16\}.
\tag{1}
$$
它们是原标准 $S_{34}$ 中
$$
\mathcal B_4=\ker(\mathcal A_{13}^3+\omega)
$$
的三条完整 Hecke 角色线；有限角色、二处向量和十七处标签均是
R806 的 $(v_-,j=4,10,16)$，不由本篇的三个模 p 特征值重新猜定。

保持原 Néron 微分 $dx/(2y)$，以及
$$
\Omega_{p,0}=\theta\Omega_p,\qquad
I_{j,-2,p}=\int_{\mathbf Z_p^\times}x^{-2}\,d\nu_{D_{j,17}}(x).
\tag{2}
$$
$\nu_D$ 是原 ordinary theta 测度。其矩约定为
$$
\int_{\mathbf Z_p}x^m\,d\nu_D(x)
=\Omega_p^m m![z^m]D(z).
\tag{3}
$$
没有改换物理测度变量、单位域、primitive Euler 或周期。

本篇的 $p_*$ 不冒认为包含所有后续几何条件的巨大 CRT 射线上的素数。
这里不使用该射线上的任何辅助斜门、深核、$q_N^*$ 逆矩阵或密度结论。
所用算术输入只需要原曲线在 p 好且普通、$p\nmid34$，
原有限角色在 p 未分歧，以及下面显示的 primary 和17余类。
R804、R806 和 R814 的原 theta/Katz/局部比较在这些条件下逐式适用；
其中固定代数常数只需非零，不要求它们在7993为单位。

R814 的同一个 $\psi,g,\chi_j$ 和三个 cycle 已先于 p 固定。
其固定导子只含 $2,3,7,13,17$，故本篇 p 不碰这些导子。
同一个固定 companion 复值非零在7993仍给相应的 Katz companion 值非零；
ordinary Euler 的两项赋值不同，排除了该点的例外零。
没有为本篇检测重新选择 $\psi$、$\chi_j$ 或循环。

## 2. 唯一检测素数、Frobenius 和系数嵌入

公开 producer 从固定整数开始，直接验证
$$
7993\text{ 是素数},\qquad
\mathbf N(69-32\omega)=7993,
$$
$$
69-32\omega=1+2\delta(-22-28\omega),\qquad
69-32\omega\equiv\delta\pmod {17}.
\tag{4}
$$
素性使用到 $\lfloor\sqrt{7993}\rfloor=89$ 的完整试除；
代码没有另选素数或遇零后继续扫描的分支。

(4)给 $E_0:y^2=x^3+1$ 的原 $2\delta$-primary 生成元。
取
$$
\mathfrak p_*=(\pi_*),\qquad
\omega\longmapsto4748\pmod {7993};
$$
实际有
$$
4748^2+4748+1=0,\qquad 69-32\cdot4748=0
\quad\text{于 }\mathbf F_{7993}.
\tag{5}
$$
因此在所选嵌入中 $v_{p_*}(\pi_*)=1$。
R806 的完整有限公式给
$$
\eta_j(\mathfrak p_*)=\eta_j(\bar{\mathfrak p}_*)=-1
\qquad(j=4,10,16).
\tag{6}
$$
特别是 $\sqrt{17}=\theta^3$ 仍是 R804 的同一个不分歧 Artin 基；
没有将十八阶全局角色替换成这个局部二次限制。

系数域 $E=K(\zeta_{18})=\mathbf Q(\zeta_9)$ 在本篇 p 分裂。
选择其一个嵌入满足
$$
\zeta_{18}\longmapsto203,\qquad
203^6=4748,\qquad203^9=-1\pmod {7993}.
\tag{7}
$$
固定(5)后，有三个满足(7)的 $\zeta_{18}$ 选择。
producer 取最小整数代表只是指定这一个系数嵌入；
另外两个选择循环置换下面三条全局线。
因此三个值全非零的结论不依赖这一排序。
不据“最小根”把它认作先前另一个未指定嵌入中的同名全局标签。

## 3. 原整测度与真正的单位 depletion

这里必须使用整测度，不能只把一个形式 Taylor 系数叫作负矩。

原 ordinary theta 构造在好普通素位、prime-to-p degree34 的 Néron
模型上给整的标准 theta 格。具体地，
$\mathcal O(34[0])$ 的 Weierstrass 基由
$\sigma_b^{34}x_b^a y_b^\epsilon$、$\epsilon\in\{0,1\}$、
$2a+3\epsilon\le34$ 构成；
其在原点的允许首阶为 $0,\ldots,32,34$，首系数为单位。
原 cubical 刚化及 ordinary 形式群到 $\widehat{\mathbf G}_m$ 的整同构
把此格送入有界的整 Amice 测度。
该构造正是 R806 §4、§6 所用的 $\nu_D$，并保原 CM 周期。
在 $j=0$ CM 规范中，可能的二次 Gaussian 刚化差由
$\mu_6$ 的权2排除，故这里是原 $\sigma_b$，不是另换过
$\exp(cz^2)\sigma_b$ 的来源。

本篇只需其型四子格
$$
E_{a,b}(z)=b^{5-a}\sigma_b(z)^{34}x_b(z)^{3a},
\qquad a=0,\ldots,5.
\tag{8}
$$
$b=17$ 是 p 单位。
原 halfperiod 和 CM13 的整有限算子在 $p_*$ 处没有分母；
第5节还直接验证三个谱投影的 $z^4$ 归一量是单位。
所以(1)在这个 p 的每条实际测度均为整有界测度。
这同时说明原 $\Omega_p$ 是单位；下文不把它数值化。

置
$$
m=p_*-3=7990.
$$
在 $\mathbf Z_{p_*}^\times$ 上，
$x^{-2}\equiv x^{p_*-3}\pmod {p_*}$；
在 $p_*\mathbf Z_{p_*}$ 上，$x^{p_*-3}$ 的值属于
$p_*^{\,p_*-3}\mathcal O$。由整有界性，
$$
\boxed{
I_{j,-2,p_*}\equiv
 \Omega_{p_*}^{p_*-3}(p_*-3)![z^{p_*-3}]D_{j,17}(z)
 \pmod {p_*}.
}
\tag{9}
$$
这里的非单位补项没有被凭空删去：它的显示估值给出(9)。
也没有用深核符号推这个同余。
(9)是原同一个单位负二矩的第一层，不是高正矩的另一条来源。

## 4. 原 sigma 的整个所需整系数窗

写
$$
w=bz^6,\qquad x_b(z)=z^{-2}A(w),\qquad
\sigma_b(z)=z\exp F(w).
\tag{10}
$$
由 $x_b''=6x_b^2$ 及 $y_b^2=x_b^3+b$ 得
$$
A_0=1,\qquad A_1=-\frac17,
$$
$$
A_n=\frac{\sum_{i=1}^{n-1}A_iA_{n-i}}
               {(n-1)(6n+1)}\quad(n\ge2).
\tag{11}
$$
由 $D^2\log\sigma_b=-x_b$ 得
$$
F_n=-\frac{A_n}{6n(6n-1)}\quad(n\ge1).
\tag{12}
$$
置
$$
s=\frac{p_*-1}{6}=1332,\qquad R=s-1=1331.
$$
在 $1\le n\le R$ 内，(11)、(12)以及下面指数递推的所有分母
都是 p 单位；$6n+1=p_*$ 的首共振发生在 $n=s$，在所用窗之外。

令
$$
E(w)=\exp(34F(w)),\quad E_0=1,\quad
E_n=\frac{34}{n}\sum_{k=1}^n kF_kE_{n-k}.
\tag{13}
$$
producer 在全 $0\le n\le1331$ 窗上还验证原方程
$$
(A-3wA')^2=A^3+w.
\tag{14}
$$
因此计算的是 $b=17$ 原曲线经(10)提取固定 b 幂后的完整系数，
而不是一段另选的近似 theta 数据。

对(8)，直接核指数可得
$$
[z^{p_*-3}]E_{a,b}
=b^{s-1}\,[w^{s-6+a}]\,E(w)A(w)^{3a}.
\tag{15}
$$
六个实际下标为1326至1331。
公开完整余行是
$$
r=(5672,\ 7337,\ 5968,\ 7380,\ 3056,\ 1587)
\in\mathbf F_{7993}^{\,6},
\tag{16}
$$
其中 $r_a$ 是(15)右边除去公共 $b^{s-1}$ 的系数。
公共正矩乘数为
$$
(p_*-3)!\,17^{s-1}=2586\pmod {7993}.
\tag{17}
$$
于是(8)的实际归一矩余行是
$$
2586r=(637,\ 6093,\ 6758,\ 5389,\ 5732,\ 3573).
\tag{18}
$$
所有到此为止的计算只用(11)–(15)的整窗。

## 5. 三个完整原特征线及非零余值

producer 从 R732/R798 已提交的算法重新生成全部13除点 trace：
在参数2至7拟合完整型四算子，再用8、9的完整 trace 核验；
没有读取保存的数值矩阵作为输入。
原 canonical halfperiod $P_4$ 同时由三个实际二挠平移生成，
其绝对号由 R798 的原 S 锚固定。

完整特征零恒等式为
$$
[\mathcal A_{13},P_4]=0,\qquad P_4^2=P_4,\qquad
\operatorname{rank}P_4=3,
$$
$$
\det(T-\mathcal A_{13})=T^6-T^3+1,\qquad
\det(T-\mathcal A_{13}|_{\mathcal B_4})=T^3+\omega .
\tag{19}
$$
全部固定有理系数在 $p_*$ 的分母都是单位。

令 $Q_0=P_4E_{0,b}$。对 $\mu^3=-\omega$，
原谱投影正是
$$
Q_\mu=
\frac{\mathcal A_{13}^2+\mu\mathcal A_{13}+\mu^2I}
     {3\mu^2}Q_0.
\tag{20}
$$
按照 R806 的完整角色标签，在(7)的嵌入中
$$
(\mu_4,\mu_{10},\mu_{16})=(315,\ 6749,\ 929).
\tag{21}
$$
三者互异。每个(20)都直接满足
$P_4Q_\mu=Q_\mu$、$\mathcal A_{13}Q_\mu=\mu Q_\mu$。
在(8)的升幂基下，$z^4$ 首系数就是第六坐标。
三个实际归一量及归一向量为：

| 标签 | $[z^4]Q_{\mu_j}$ | $D_{j,17}$ 的六坐标模7993 |
|---|---:|---|
| $4$ | $527$ | $(5827,1651,5731,6895,4982,1)$ |
| $10$ | $3835$ | $(6538,7372,4082,6622,3375,1)$ |
| $16$ | $5752$ | $(7385,1122,7548,4441,6617,1)$ |

三个归一量非零，故没有以 p 非单位缩放来源。
三个非零特征向量属于不同实际特征值，因而在
$\mathbf F_{7993}$ 上严格独立并张满 $\mathcal B_4$ 的约化。
此论证不使用把有限域整数代表送入 $\mathbf Q(\omega)$ 后计算的秩。

(16)在三个归一向量上的值依次为
$$
5818,\qquad236,\qquad5769.
\tag{22}
$$
再乘(17)并用真正的 depletion (9)，得到
$$
\boxed{
\begin{aligned}
\Omega_{p_*}^{-7990} I_{4,-2,p_*}&\equiv2522,\\
\Omega_{p_*}^{-7990} I_{10,-2,p_*}&\equiv2828,\\
\Omega_{p_*}^{-7990} I_{16,-2,p_*}&\equiv3696
\end{aligned}\pmod {7993}.
}
\tag{23}
$$
所以
$$
\boxed{v_{p_*}(I_{j,-2,p_*})=0\quad(j=4,10,16).}
\tag{24}
$$
(23)的 $\Omega_{p_*}^{-7990}$ 是保留的原 period 因子，
不是某个选为1的数值周期。其单位性足以给(24)。

## 6. 原 canonical 类和固定 AJ 配对非零

R804 的三个原类保持完整定义
$$
z_{j,p}=\frac1{30}\operatorname{pr}_K
 \operatorname{tw}_{\nu_j}(e_{\eta_j}u_\infty),\qquad
\nu_j=\eta_j\psi_0^{-1}\bar\psi_0^2 .
\tag{25}
$$
它们来自原模 $34\delta$ 的同一个全 ray class 椭圆单位塔；
没有用(23)的一个局部对数逆像重新命名全局类。

原比较为
$$
\log_j(\operatorname{loc}_{\mathfrak p_*}z_{j,p_*})
=-34^2c_j\theta^9\Omega_{p_*}^4
 \frac{1+\pi_*/\bar\pi_*^2}{1+\bar\pi_*/\pi_*^2}
 I_{j,-2,p_*}^{\,2}.
\tag{26}
$$
$c_j$ 是 R806 固定的非零代数常数；本篇没有另证
$v_{p_*}(c_j)=0$，也不需要这一单位断言。
两个 Euler 均非零，其比准确属于
$p_*^2\mathcal O^\times$。
$\sqrt{17}$ Artin 基、原30平滑、$\theta^9\Omega_{p_*}^4$
及式中负号全按 R804 保留。
由(23)直接得
$$
\boxed{
\operatorname{loc}_{\mathfrak p_*}z_{j,p_*}\ne0,\qquad
z_{j,p_*}\ne0\quad(j=4,10,16).
}
\tag{27}
$$
不需要先假设一般严格 Selmer 核为零。

再采用 R814 已固定的共同 $\psi,g,\chi_j$ 和 $\Delta_j$。
记其同规范实际 AJ 配对为 $\mathcal A_{j,p}$。
[R814(31)](R814-common-fixed-good-pair-and-three-original-aj-squares.md)给
$$
\mathcal A_{j,p_*}^{\,2}
=-\frac{34^4c_j\theta^9\Omega_{p_*}^4\mathcal E^{\log}_{p_*}}
 {\mathfrak d_{j,p_*}\mathfrak u_{j,p_*}(0)
  E^{\rm Iw}_{j,p_*}E^{\rm BDP}_{j,p_*}}\,
 I_{j,-2,p_*}^{\,2}.
\tag{28}
$$
所有因子的定义仍是同一 fixed good pair：
$E^{\rm Iw}\in1+p_*\mathcal O$，
$v_{p_*}(E^{\rm BDP})=-2$；
$\mathfrak d$ 是非零 de Rham 泛函比，
$\mathfrak u(0)$ 是增广完成环中真实单位的非零常数。
没有省去第二个 companion 或把两 Euler 互换。
所以
$$
\boxed{\mathcal A_{j,p_*}\ne0\quad(j=4,10,16).}
\tag{29}
$$

由于 p-adic AJ 是定义在有理等价类上的映射，(29)证明
R814 这三个先于 p 固定的代数循环在相应 Chow 群中非零。
这一步是由一个实际非零实现值推出循环非零；
不是由复循环非零倒推 p-adic AJ 非零。

## 7. 同一有限域中实际角色投影的 Chow 独立

还须把三个循环置于同一个固定对象中，才能谈线性独立。

取 R814 §5 的共同有限 CM isogeny orbit。
令 H 是包含其原 level 结构、conductor34 isogenies 和三个
$\chi_j$ 的共同有限阿贝尔定义域；可取相应有限 ray class 与
ring class 域的合成。另取一个共同系数域 E' 包含 $g$ 的系数和三个
$\chi_j$ 的值。二者均在选择 p 以前固定。
在 $X=W_2\times A_0^2$ 的原代数投影中工作，并保 BDP 构造的全部
CM isogeny、norm 权重和有限 level 运输。

三个有限角色满足
$$
\chi_{10}=\chi_4\epsilon,\qquad
\chi_{16}=\chi_4\epsilon^2,
$$
其中 $\epsilon$ 是 R814(4) 的真实非平凡三次角色，导子17。
它们在共同 $G=\operatorname{Gal}(H/K)$ 上互异。

为明确作用规范，把共同 balanced CM 因子
$\omega_{A_0}\eta_{A_0}$ 的 Tate/norm 运输包括在这个原有限轨道模中。
这是同一个代数 CM 对应，不随 j 改动。
于是 $\Delta_j$ 的 descent 正是
$V_g(2)\otimes\chi_j$ 的原有限角色投影。
在“G 只作用几何轨道、固定 E' 系数”的规范下，显示幂等元是
$$
e_j=\frac1{|G|}\sum_{\sigma\in G}\chi_j(\sigma)\,\sigma,
\qquad
e_j\Delta_j=\Delta_j,\qquad e_i\Delta_j=0\ (i\ne j).
\tag{30}
$$
等价地，$\sigma\Delta_j=\chi_j(\sigma)^{-1}\Delta_j$。
若改用相反 Artin 约定，(30)的所有角色同时取逆；
三个投影仍是同一组互斥幂等元。
这里固定的是 R814 的标准 finite descent，而不是把任意三个
unweighted isogeny 图分别放进三个新造副本。
BDP 的图循环构造及其有限域见 §2.3、Remark2.6；
其 balanced CM 对应见 §2.4。
式(30)也正是该有限轨道 norm 投影在 Chow 层面的重标：
共同 norm/CM 因子留在轨道向量中，只有真正有限的 $\chi_j$ 进入幂等元。
不对系数 E' 额外施 Galois 共轭。

现在若
$$
a_4\Delta_4+a_{10}\Delta_{10}+a_{16}\Delta_{16}=0,
\qquad a_j\in E',
$$
对其依次施(30)，得到 $a_j\Delta_j=0$。
由(29)及有理系数 Chow 群的 E' 线性结构，均有 $a_j=0$。
因此
$$
\boxed{\Delta_4,\Delta_{10},\Delta_{16}
\text{ 在该共同固定、实际投影的 Chow 模中线性独立。}}
\tag{31}
$$
扩张系数域不改变此独立性。
有限定义域再扩张也不杀这些有理等价类，因为 restriction 后的
corestriction 是非零扩张次数。
本结论针对实际角色投影后的循环，不声称所有未投影轨道图独立。
其理由是(30)与非零实现，而不是三个模 p 数值彼此不相等。

## 8. 公开执行、重现参数和完整输出来源

唯一执行记录：

| 项目 | 实际值 |
|---|---|
| source commit | `3d62c7f1f103db981bfe9da0b43cef1ecfc5c89e` |
| public run | [43752389762](https://github.com/Rogerhu12/math-research-public/actions/runs/43752389762) |
| job | [132928993680](https://github.com/Rogerhu12/math-research-public/actions/runs/43752389762/job/132928993680) |
| producer | [check-r817-fixed-prime-original-negative-two.py](../scripts/check-r817-fixed-prime-original-negative-two.py) |
| parameters | `--workers 4`；唯一固定 `p=7993,b=17` |
| exact runtime | Python、python-flint `0.9.0` |
| script SHA256 | `c3e8b90cd013d312e84439ec65c0b175ca530a85020929aa57b3fbcd73be3f4c` |
| stdout | 2812 bytes，exit0，`PASS` |
| stdout SHA256 | `4e22f54ffcf57ec9dd295d408aa8338bda0f93c1a99c0b5f99f86d22cc533672` |

两份实际依赖的 SHA256 为：
$$
\begin{aligned}
&\texttt{check-r732-original-type-five-cm13.py}:\\
&\quad\texttt{d1b3c2f851e9ec6b6d6b6655141e36b4bb1108a30e57ff8365b5f583d880e469},\\
&\texttt{check-r798-type-four-halfperiod-and-cm13.py}:\\
&\quad\texttt{f6a1fe72d01b0c804059a06395c5a9c5d78e54d5742a6ca9af957febec9661b3}.
\end{aligned}
$$
完整小输出已亲读，包括三个未归一谱向量、归一量、
(16)–(23)、整窗数组 hash 和完整算子 hash。
数组只在公开任务内存中生成；没有可重算数据另存仓库或 Release。
本篇也未增加第二个素数检查或另一个“通过”为止的筛选。

## 9. 本结论以后仍需保持的区别

(24)、(27)、(29)是在同一固定 $p_*$ 上的三个原非零值。
(31)是固定几何循环在同一有限域/系数模中的结论。
它们并不证明这些循环在另一个 p 的 Abel–Jacobi 配对非零；
一个固定非零循环的不同 p-adic realization 仍可能遇到未解决的核问题。

原指定来源的实际负二行仍是
$$
\lambda^{2N}\Omega_p^2
 \sum_{j=4,10,16}\alpha_{j,N}I_{j,-2,p}.
\tag{32}
$$
三个循环的独立和逐角色平方(28)都不是(32)的线性独立定理。
本篇不为三个平方根选出未经支付的相容代数符号，
不删除 R807/R809 的原联络、R801 的高阶项及真实 W 外部，
也没有从这个唯一检测推出原三个中央导数不能同时为零。

## 10. 证明依赖

- [R798](R798-original-halfperiod-two-types-and-e-depth-second-source.md)：原 canonical halfperiod、完整 CM13 及型四三维格。
- [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)：完整 $(v_-,j)$ 来源、十八阶有限角色、原 $\nu_D$、period 及 primitive Katz 平方。
- [R804](R804-original-order-eighteen-soule-classes-and-negative-two-localization.md)：同一个 $34\delta$ 全局类、30平滑、$\sqrt{17}$、两个 Euler 的方向及(26)。
- [R811](R811-canonical-soule-classes-and-global-heegner-comparison.md)：指定 canonical 类的真实全局比较；本篇的(27)也可直接由非零局部化推出。
- [R814](R814-common-fixed-good-pair-and-three-original-aj-squares.md)：先于 p 固定的共同 good pair、三个有限角色、同一几何来源及完整(28)。
- Bertolini–Darmon–Prasanna，*Generalized Heegner cycles and p-adic Rankin L-series*，
  Duke Math. J.162 (2013)，§2.3–2.4、Theorem5.13：
  [作者全文](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP1.pdf)。
- Castella，*Tamagawa number conjecture for CM modular forms and Rankin–Selberg convolutions*，
  [固定 v3 全文](https://arxiv.org/html/2407.11891v3)，
  Theorems3.2.1–3.2.2及§5.1：与 R814 相同的原 finite descent、
  AJ 配对和 ordinary Euler，没有使用任何新的非消失前提。
