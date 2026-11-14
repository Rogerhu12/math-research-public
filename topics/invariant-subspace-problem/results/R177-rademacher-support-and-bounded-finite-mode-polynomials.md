# R177：联合 Rademacher 支撑柱体与有限一阶模式多项式的有界性分类

日期：2026-11-12（UTC）。作者：Astra-ISP-0c017065。
状态：完整证明；支撑柱体及复多项式归约已由 l2_moments 独立核验。本稿分类的是点态符号的实际有界性，不从中推出一般乘子的单射性。

## 1. 结论与两种不同的线性空间

令
$$
u=(u_1,\ldots,u_d)=c+\sum_{j\ge0}a_j\chi_j,\qquad
c,a_j\in\mathbb C^d,\qquad
\sum_j\|a_j\|^2<\infty.
\tag{1.1}
$$
$\chi_j$ 是 Haar 二进制坐标上的独立 Rademacher 符号。
各分量按 $L^2$、并几乎处处收敛。

定义复线性形式空间
$$
\mathcal V=
\left\{\ell\in(\mathbb C^d)^*:
\sum_j|\ell(a_j)|<\infty\right\},
\qquad
W=\bigcap_{\ell\in\mathcal V}\ker\ell.
\tag{1.2}
$$
这里不把一个实线性绝对可和条件自动当成复线性条件。
下面先确定实支撑，再证明 (1.2) 的 $W$ 正好是该实支撑无界方向的复线性包。

选任意复线性投影 $L$，满足
$$
\ker L=W.
\tag{1.3}
$$
于是 $L^2=L$，其像是 $W$ 的某个复线性补空间。
每个坐标形式 $e_k^*L$ 都在 $\mathcal V$ 中，因此
$$
\sum_j\|La_j\|<\infty.
\tag{1.4}
$$
从而
$$
v=Lu=Lc+\sum_jLa_j\chi_j
\tag{1.5}
$$
具有一致收敛的连续有界代表。

**定理1.1。** 对任意复多项式 $F\in\mathbb C[z_1,\ldots,z_d]$，以下等价：

1. $F(u)$ 本质有界；
2. 在随机向量 $u$ 的支撑中，每个点 $z$ 都满足
   $$
   F(z+w)=F(z)\qquad(w\in W);
   \tag{1.6}
   $$
3. 存在一个只依赖绝对可和复线性组合的实际表示；准确地，对任意满足 (1.3) 的 $L$，
   $$
   \boxed{F(u)=F(Lu)\quad\text{几乎处处}.}
   \tag{1.7}
   $$

所以有界的有限模式点态多项式，实际只依赖 $\mathcal V$ 所给的有界一阶组合。
这是随机变量或实际符号的等式。
若有界模式本身有代数关系，不要求原形式多项式 $F$ 在整个 $\mathbb C^d$ 上都沿 $W$ 不变。

特别，若 $\mathcal V=\{0\}$，则：

- $u_1,\ldots,u_d$ 作为随机变量在 $\mathbb C$ 上代数独立；
- 每个非恒定 $F(u)$ 都无界；
- 每个非零 $F(u)$ 仍在所有有限 $L^p$ 中。

最后一条没有给整个未知不变子空间提供固定的高可积正则器，因而不与 R163/R165 冲突。

## 2. 实 Rademacher 和的支撑定理

先独立证明有限维实结论。
令
$$
Z=\sum_{j\ge0}\varepsilon_jv_j\in\mathbb R^m,\qquad
\sum_j\|v_j\|^2<\infty,
\tag{2.1}
$$
其中 $\varepsilon_j$ 独立且以相等概率取 $\pm1$。

有限部分和在 $L^2$ 中 Cauchy，定义 $Z$。
标准的独立零均值有限方差收敛也给几乎处处版本：
对尾方差选可和的子序列界，再用有限部分和的 $L^2$ 最大不等式和 Borel–Cantelli，即得整个部分和序列几乎处处 Cauchy。
以下支撑证明只需 $L^2$ 极限、尾独立性及尾二阶矩界。

置
$$
K=\left\{\theta\in\mathbb R^m:
\sum_j|\langle\theta,v_j\rangle|<\infty\right\},
\qquad U=K^\perp.
\tag{2.2}
$$
$K$ 是线性子空间；在有限维空间中它自然闭。
令 $P_K,Q_U$ 为两个正交投影。

**定理2.1。**
$$
\boxed{
\operatorname{supp}Z
=
U+\operatorname{supp}(P_KZ).
}
\tag{2.3}
$$
右侧是正交分解 $\mathbb R^m=U\oplus K$ 下的一个闭柱体。

### 2.1. 有界方向的尾绝对可和

取 $K$ 的有限正交基 $\theta_1,\ldots,\theta_s$。
由
$$
\|P_Kv_j\|
\le\sum_{\nu=1}^s|\langle\theta_\nu,v_j\rangle|,
$$
得到
$$
\boxed{\sum_j\|P_Kv_j\|<\infty.}
\tag{2.4}
$$
因此
$$
C_K:=
\left\{\sum_j\epsilon_jP_Kv_j:
\epsilon_j\in\{-1,1\}\right\}
\tag{2.5}
$$
是紧集，并恰为 $\operatorname{supp}(P_KZ)$。

确切地，(2.4) 使乘积符号空间到 $K$ 的求和映射连续，故其像紧。
任意像点的任意邻域都包含一个有限符号柱的像，后者事件的概率为正，所以每个像点都在支撑内。
反向随机变量的值始终落在这个紧像中。

显然
$$
\operatorname{supp}Z\subseteq U+C_K.
\tag{2.6}
$$
真正需要证明的是反向包含。

### 2.2. 每条无界方向的尾部线性容量都无限

对每个 $n$，定义有限软符号和的集合
$$
\mathcal Z_n=
\left\{\sum_{j\in J}t_jQ_Uv_j:
J\subseteq\{n,n+1,\ldots\}\text{ 有限},
\quad -1\le t_j\le1\right\}.
\tag{2.7}
$$
它是平衡凸集。

若 $0\ne\theta\in U$，则
$$
\sum_{j\ge n}|\langle\theta,Q_Uv_j\rangle|
=
\sum_{j\ge n}|\langle\theta,v_j\rangle|
=\infty.
\tag{2.8}
$$
否则补回有限头后有 $\theta\in K$，与 $K\cap U=\{0\}$ 矛盾。
因此 $\mathcal Z_n$ 在每个非零实线性方向的支撑函数都为无穷。

有限维闭凸集的分离定理于是给
$$
\boxed{\overline{\mathcal Z_n}=U\qquad(n\ge0).}
\tag{2.9}
$$
具体地，如果闭包不是整个 $U$，分离某个外点就会产生一个非零线性形式在该闭凸集上有有限上界，与 (2.8) 矛盾。

(2.9) 只是软系数的逼近。
下一步把这些系数变成真正的 $\pm1$，并且付出一个由远尾方差控制的误差。

### 2.3. 有偏符号舍入

设 $J$ 有限、$t_j\in[-1,1]$。
取独立随机符号 $\delta_j$，使
$$
\mathbb E\delta_j=t_j.
$$
允许 $t_j=\pm1$，此时对应符号固定。
独立性给
$$
\mathbb E
\left\|\sum_{j\in J}(\delta_j-t_j)Q_Uv_j\right\|^2
=
\sum_{j\in J}(1-t_j^2)\|Q_Uv_j\|^2
\le\sum_{j\in J}\|v_j\|^2.
\tag{2.10}
$$
所以至少存在一个实际有限符号选择 $\epsilon_j=\pm1$，满足
$$
\left\|\sum_{j\in J}(\epsilon_j-t_j)Q_Uv_j\right\|
\le\left(\sum_{j\in J}\|v_j\|^2\right)^{1/2}.
\tag{2.11}
$$

这里只借有偏分布证明一个有限符号选择存在。
选出后，这个同样的有限符号配置在原来等概率的 Rademacher 乘积测度下仍有严格正概率。

### 2.4. 用真实有限柱事件逼近任意柱体点

固定 $y\in C_K$、$u_0\in U$ 和 $\epsilon>0$。
选充分远的 $n$，使
$$
\sum_{j\ge n}\|P_Kv_j\|<\epsilon,\qquad
\sum_{j\ge n}\|v_j\|^2<\epsilon^2.
\tag{2.12}
$$
按 (2.5)，选一个完整符号表示
$y=\sum_j\eta_jP_Kv_j$，并先固定前 $n$ 位为 $\eta_j$。
记完整头向量
$$
z_{\rm head}=\sum_{j<n}\eta_jv_j.
$$
则
$$
\|P_Kz_{\rm head}-y\|<\epsilon.
\tag{2.13}
$$

由 (2.9)，可用某个有限区间 $n\le j<N$ 内的软系数逼近
$u_0-Q_Uz_{\rm head}$：
$$
\left\|
\sum_{j=n}^{N-1}t_jQ_Uv_j-
(u_0-Q_Uz_{\rm head})
\right\|<\epsilon.
\tag{2.14}
$$
若最初仅用区间中的若干位，将其余软系数置0即可。

由 (2.11)—(2.12)，存在该区间的实际符号配置，舍入误差小于 $\epsilon$。
固定这个配置后，有限头加中段的 $U$ 分量与 $u_0$ 相差小于 $2\epsilon$。

剩余 $j\ge N$ 的 Rademacher 尾仍独立、均值零且二阶矩小于 $\epsilon^2$。
由 Chebyshev 不等式，
$$
\mathbb P\left(
\left\|\sum_{j\ge N}\varepsilon_jQ_Uv_j\right\|<2\epsilon
\right)>0.
\tag{2.15}
$$
与先前固定的有限符号事件相交仍有正概率。
在这个事件上，完整 $U$ 分量与 $u_0$ 的差小于 $4\epsilon$。

同时，无论中段和剩余尾的符号如何，
整个 $K$ 尾都由 (2.12) 控制，所以完整 $K$ 分量与 $y$ 的差小于 $2\epsilon$。
于是 $Z$ 落在 $u_0+y$ 的 $6\epsilon$ 邻域的概率为正。

$\epsilon$ 任意，得到 $u_0+y\in\operatorname{supp}Z$，证明 (2.3)。
这里的尾窗口按目标和精度选取，没有向一个未知不变空间索取收敛速度。

## 3. 实支撑无界方向的复线性包

回到 (1.1)，将 $\mathbb C^d$ 视为 $\mathbb R^{2d}$，对向量 $a_j$ 使用 §2 的 $K,U$。
则
$$
\operatorname{supp}u=c+U+C_K.
\tag{3.1}
$$

任意复线性形式 $\ell$ 的实部和虚部都是实线性形式。
由于
$$
|\ell(a_j)|
\le|\operatorname{Re}\ell(a_j)|
+|\operatorname{Im}\ell(a_j)|,
$$
且反向每一项都不超过 $|\ell(a_j)|$，有
$$
\ell\in\mathcal V
\Longleftrightarrow
\operatorname{Re}\ell,\operatorname{Im}\ell\in K.
\tag{3.2}
$$
这又等价于 $\ell$ 在 $U$ 上恒为零，或等价于它在
$\operatorname{span}_{\mathbb C}U$ 上恒为零。

有限维线性代数因此给
$$
\boxed{W=\operatorname{span}_{\mathbb C}U.}
\tag{3.3}
$$
这也证明了 §1 中每个坐标形式 $e_k^*L$ 属于 $\mathcal V$，以及 (1.4)。

$U$ 本身未必是复子空间。
例如全部 $a_j$ 为实数且不可和时，$U$ 可以是一条实直线，而其复线性包是一整条复直线。
证明中正是通过多项式复化使用这一区别。

## 4. 有界多项式沿柱体方向必须常数

设 $F(u)$ 本质有界，记本质上界为 $M$。
因为 $F$ 连续，必有
$$
|F(z)|\le M\qquad(z\in\operatorname{supp}u).
\tag{4.1}
$$
否则某个支撑点附近仍有 $|F|>M$，该邻域有正概率，与本质上界矛盾。

固定 $y\in C_K$，取 $U$ 的一个实基 $v_1,\ldots,v_s$。
由 (3.1)—(4.1)，
$$
P_y(t_1,\ldots,t_s)
=
F\left(c+y+\sum_{\nu=1}^st_\nu v_\nu\right)
\tag{4.2}
$$
是一个在整个 $\mathbb R^s$ 上有界的复系数多项式。
这样的多项式只能是常数：
若最高非零齐次项次数为正，选一个它不为零的实方向，沿该射线就无界。
一个非零复系数多项式不可能在全部实空间恒零，这可对变量数逐个使用一元多项式零点有限性证明。

所以
$$
P_y(t)=F(c+y)\qquad(t\in\mathbb R^s).
\tag{4.3}
$$
其多项式系数恒等也使 (4.3) 对所有复参数 $t\in\mathbb C^s$ 成立。
由 (3.3)，
$$
\boxed{
F(c+y+w)=F(c+y)\qquad(w\in W).
}
\tag{4.4}
$$
支撑点 $z=c+y+u_0$ 中的 $u_0$ 已在 $W$ 内，所以 (4.4) 等价于定理1.1的 (1.6)。

对任意满足 (1.3) 的投影 $L$，有 $z-Lz\in W$。
将 (1.6) 用于 $w=Lz-z$，得到
$$
F(z)=F(Lz)\qquad(z\in\operatorname{supp}u).
\tag{4.5}
$$
这证明 (1.7)。

反向，若有 (1.7)，则 (1.4)—(1.5) 使 $Lu$ 有界，故 $F(Lu)$ 有界。
因此三条件等价。

注意：要从 (1.7) 推回 (1.6)，可以先由其得到有界性，再用以上论证；并不声称一个只在支撑上成立的形式等式自动延拓到整个 $\mathbb C^d$。

## 5. 无绝对可和线性组合时的代数独立

若 $\mathcal V=\{0\}$，则 $W=\mathbb C^d$，可取 $L=0$。
定理1.1给：任何有界 $F(u)$ 必等于常数 $F(0)$。

还需排除一个非恒定形式多项式偶然在支撑上为常数。
这时 $U$ 的复线性包已为整个 $\mathbb C^d$。
固定任意 $y\in C_K$，由支撑柱体和 (4.4)，
$$
F(c+y+w)=F(c+y)\qquad(w\in\mathbb C^d),
$$
故 $F$ 本身是常数多项式。

特别，若 $F(u)=0$ 几乎处处，$F$ 是零多项式。
因此这些随机变量在 $\mathbb C$ 上代数独立。

更一般，设 $\deg F=p$。
有限维 Rademacher 和的每个实线性分量满足次 Gaussian 估计：
有限部分和的矩生成函数为
$$
\prod_j\cosh(t\langle\theta,a_j\rangle)
\le
\exp\left(\frac{t^2}{2}\sum_j|\langle\theta,a_j\rangle|^2\right).
\tag{5.1}
$$
这里 $\cosh x\le e^{x^2/2}$ 可由
$(\log\cosh x)'=\tanh x$ 与 $|\tanh x|\le|x|$ 积分得到。
通过几乎处处极限和 Fatou，(5.1) 传到无限和。
指数尾界给所有有限阶矩；有限维范数和多项式增长再给
$$
F(u)\in L^q\qquad(1\le q<\infty).
\tag{5.2}
$$

因此“无界”是准确的 $L^\infty$ 障碍，并不意味这些符号离开 $H$，也不构造非循环向量。

## 6. 对实际乘子和字符的结论

每个 $F(u)$ 都是有限全局 Walsh 次数的 $L^2$ 向量。
若它本质有界，定理1.1直接给一个连续代表
$$
f_{\rm cont}(y)
=
F\left(Lc+\sum_jLa_j\chi_j(y)\right).
\tag{6.1}
$$
这也给 R92 的有界实际乘子接口，而不需猜测无界各分量在物理整数0处的数值。

令
$$
\beta_L=Lc+\sum_jLa_j,
\tag{6.2}
$$
该和绝对收敛。
其实际乘子 $X_{F(u)}\in\mathcal A$ 的字符因此为
$$
\boxed{\chi(X_{F(u)})=f_{\rm cont}(0)=F(\beta_L).}
\tag{6.3}
$$
这个值不依赖补空间投影 $L$。
事实上不同选择给连续函数，且由 (1.7) 几乎处处相等；
Haar 测度对每个非空柱集均为正，故两个连续函数处处相等，特别在0相等。

如果
$$
F(\beta_L)\ne0,
$$
R92 的范数代数单位结论给 $X_{F(u)}$ 有界可逆，因而 $F(u)$ 循环。
若这个字符为零，本稿不自动排除相应乘子的核。

还可以选择 $\mathcal V$ 的复基 $\ell_1,\ldots,\ell_b$。
因为 $L$ 的坐标都是这些形式的线性组合，存在某个有限多项式 $G$，使
$$
F(u)=G(\ell_1(u),\ldots,\ell_b(u))
\tag{6.4}
$$
几乎处处，而每个 $\ell_\nu(u)$ 的系数都绝对可和。

若这些有界组合另外满足 R154 的联合超三次条件，非零 (6.4) 及任意 $\ell^2$ 第一阶指数权可直接使用其循环定理。
这里只把已经验证的组合送入已有定理，没有把任意绝对可和尾当成快尾。

## 7. 例子与形式因式化的边界

### 7.1 一个无界模式加一个有界差

设
$$
s=\sum_{j\ge1}\frac{\chi_j}{j},\qquad
b=\sum_{j\ge1}b_j\chi_j,\quad b\in\ell^1,
$$
并令 $u_1=s+b$、$u_2=s-b$。
若除此之外没有新的有界线性方向，则 $\mathcal V$ 由
$\ell(z)=z_1-z_2$ 张成。
所有有界的 $F(u_1,u_2)$ 实际都可写成关于 $u_1-u_2=2b$ 的多项式。
无需将发散的 $\sum 1/j$ 赋值成某个形式锚。

### 7.2 形式上出现无界变量，也可被有界模式关系杀掉

令 $s$ 使用与第0位不交的不可和平方可和尾，取
$$
u_1=s,\qquad u_2=\chi_0.
$$
形式多项式
$$
F(z_1,z_2)=(z_2^2-1)z_1
$$
在整个 $\mathbb C^2$ 上依赖 $z_1$，但
$$
F(u_1,u_2)=0
$$
恒成立。
所以定理1.1必须说“实际只依赖有界组合”，不能把它加强成原形式多项式的全局变量消失。

### 7.3 实支撑与复线性包不可混淆

单个实不可和 $\ell^2$ 系数模式的支撑是整条实直线，而非整个复平面。
但一个复多项式若在这条实直线上有界，仍只能为常数。
这正是 §4 的复化步骤；本稿没有把实 Rademacher 支撑错误宣布为复开集。

## 8. 保留的缺口

1. 本稿只分类有限个一阶模式的点态多项式，未分类任意无限秩有限 chaos 的有界性。
2. 有界模式可能有代数关系；归约是实际符号等式，非未经证明的形式理想分类。
3. 没有由联合分布支撑推出任何未知不变子空间中存在所需的测试向量。
4. 无界点态多项式的实际闭乘子仍需独立域构造；这里的概率支撑证明不替代 R171/R172/R176 的闭图工作。
5. 零字符的任意慢有界多项式、一般二阶核及完整 Hilbert 不变子空间问题仍未解决。

新增内容是联合 Rademacher 和的精确支撑柱体、实无界方向的复化、
有限模式点态多项式的有界性归约，以及可合法计算的实际0锚。

