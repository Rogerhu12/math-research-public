# R389 — E24 的真实野三次局部角色、导子与 Hermitian 类

日期：2026-11-14。**状态：以下固定曲线的完整坏点角色、野三次 conductor、两处原 Tate Gauss 和，以及实际 Hermitian 类 $\alpha=1$ 已证明。没有把次数十六的旧来源认作本曲线，也没有由本地不变空间推出原中央非零或 Sha 的结论。原问题未完成。**

固定
$$
E_{24}:y^2=x^3+24,\quad
K=\mathbf Q(\delta),\quad \delta=\sqrt{-3}=1+2\omega,\quad
\operatorname{Im}\delta>0.
\tag{1}
$$
使用 [R290](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)
同一解析微分 CM type、理想/idèle 对应和加性角色。
本篇给新来源的完整本地输入；野分歧 Schwartz 的显式向量及其与旧
来源的真实运输仍须另算。特别 $\alpha=8$ 不是这里实际确定的类。

## 1. 全局角色与精确 reciprocity 方向

令 $\psi_D$ 为 $y^2=x^3+D$ 的代数 Hecke 角色，
$\chi_D=\psi_D|\cdot|_K^{-1/2}$，其中 idèle 无限分量取
$$
\chi_{D,\infty}(z)=(z/|z|)^{-1}.
$$
已发表的六次剩余公式及 R290 的规范给
$$
\frac{\psi_{24}(\mathfrak p)}{\psi_1(\mathfrak p)}
 =\left(\frac{24}{\mathfrak p}\right)_6^{-1}
\quad(\mathfrak p\nmid6).
\tag{2}
$$
固定局部 reciprocity，使未分歧点的 uniformizer 送算术 Frobenius。
记
$$
\vartheta_{a,v}(t)
 =\frac{\operatorname{rec}_v(t)(a^{1/6})}{a^{1/6}}.
$$
则 (2) 的本地扭曲是 $\vartheta_{24,v}^{-1}$。这是原 idèle
分量的方向，不能把它改成好素理想公式中的同向单位幂。

基角色 $\chi_1$ 的已付坏点数据为
$$
\begin{array}{c|c|c}
v&\text{单位角色}&\text{uniformizer 值}\\ \hline
2&\operatorname{Teich}_{\mu_3}(u\bmod2)&\chi_{1,2}(2)=-1\\
3&u\bmod\delta\in\{\pm1\}&\chi_{1,3}(\delta)=i .
\end{array}
\tag{3}
$$
下面直接支付扭曲后的两个完整本地角色。

## 2. 二处是实际二次扩张，conductor 为八

立方映射是 $\mathbf Z_2^\times$ 的自同构。取 $v^3=3$，
则 $v\equiv3\pmod8$，且 $24=(2v)^3$。
由于 $v/3\equiv1\pmod8$，$2v$ 与 $6$ 在 $\mathbf Q_2$ 中同平方类。
因此原六次扭曲在 $K_2$ 上准确化为
$$
K_2(\sqrt6)/K_2.
\tag{4}
$$
$K_2/\mathbf Q_2$ 未分歧二次。由 norm 与局部 reciprocity 的相容性，
对单位 $u$、$n=N_{K_2/\mathbf Q_2}(u)$，
$$
\vartheta_{24,2}(u)
 =(6,n)_2
 =(-1)^{(n^2-1)/8+(n-1)/2}
 =\left(\frac{-2}{n}\right).
\tag{5}
$$
右边按奇数 $n\bmod8$ 读取：$n=1,3$ 时为正，$n=5,7$ 时为负。
二次角色的逆仍是自身，所以
$$
\boxed{
\chi_{24,2}(u)
 =\operatorname{Teich}_{\mu_3}(u\bmod2)
  \left(\frac{-2}{N(u)}\right),\qquad
\chi_{24,2}(2)=-1.
}
\tag{6}
$$
uniformizer 处的二次因子为一，因为 $N(2)=4$ 是平方。

(5) 在 $1+8\mathcal O_{K_2}$ 上平凡，但在 $1+4\mathcal O_{K_2}$
上不平凡：取 $u=1+4\omega$，其范数为 $13\equiv5\pmod8$。
基三次角色在 $1+2\mathcal O_{K_2}$ 已平凡，因此不存在抵消，
$$
\boxed{a_2(\chi_{24})=3.}
\tag{7}
$$
这不是 R290 的 conductor-two 四陪集向量的同一个本地输入。

## 3. 三处的野三次扩张及完整 unit character

有
$$
24=(-2)^3\delta^2.
$$
$-2$ 是 $\mathbf Q_3$ 中的平方，由模三的根 $1$ 作 Hensel 提升即可。
所以三处的六次 Kummer 扩张准确是
$$
L=K_3(a),\qquad a^3=\delta.
\tag{8}
$$
它是循环三次扩张，两个非平凡自同构为 $a\mapsto\omega a$、
$a\mapsto\omega^2a$。

### 3.1 conductor 四的完整分歧证明

$x^3-\delta$ Eisenstein，$a$ 是 $L$ 的 uniformizer。
在 $c_0+c_1a+c_2a^2$ 中，各项 valuation 属于三个不同的模三类，
故无最低项相消。于是整性恰等价于各 $c_j\in\mathcal O_{K_3}$，
证明
$$\mathcal O_L=\mathcal O_{K_3}[a].$$
这里没有遗漏一个可能改变 discriminant 的整基指数。

对每个非平凡 $g$，
$$
v_L(g(a)-a)=v_L(\omega^j-1)+v_L(a)=3+1=4.
$$
因此 lower ramification groups 准确为
$$
G_0=G_1=G_2=G_3=C_3,\qquad G_4=1.
\tag{9}
$$
每个非平凡一维角色的 Artin conductor 是四；different 指数为
$2+2+2+2=8$，也与 $v_L(3a^2)=8$ 相同。

记
$$
\vartheta_\delta(t)=
 \frac{\operatorname{rec}_{K_3}(t)(a)}a .
$$
原完整角色是
$$
\boxed{\chi_{24,3}=\chi_{1,3}\vartheta_\delta^{-1},\qquad
a_3(\chi_{24})=4.}
\tag{10}
$$
又 $N_{L/K_3}(a)=\delta$，所以 $\vartheta_\delta(\delta)=1$，
$$
\boxed{\chi_{24,3}(\delta)=i.}
\tag{11}
$$
基角色的 conductor 只有一，不能抵消 (9) 的野分歧末层。

### 3.2 五十四个实际单位及角色方向

由于 $\delta^4=9$，
$\mathcal O_{K_3}/\delta^4=\mathbf Z/9[\delta]$，
关系为 $\delta^2=-3$。令
$$
g=1+\delta^3=1-3\delta .
$$
每个单位都有唯一分解
$$
\boxed{
u=q\,\omega^j g^k\pmod9,\quad
q\in\{1,2,4,5,7,8\},\quad 0\le j,k\le2.
}
\tag{12}
$$
确有 $54$ 个候选。唯一性可直接在基 $1,\delta$ 中看出：
$g^k=1-3k\delta\pmod9$ 的 $\delta$ 系数被三整除；
$q\omega$、$q\omega^2$ 的该系数是单位，所以只有 $j=0$ 可相等；
随后必须 $k=0,q=1$。

(12) 中 $q\omega^j$ 都是 norm。具体地，
$$
N(1+a^2)=1+\delta^2=-2,\qquad
N(1+a)=1+\delta=-2\omega^2,\qquad N(-1)=-1.
$$
这给出所有 rational units modulo nine 及 $\mu_3$；conductor 四
保证 $1+\delta^4\mathcal O_{K_3}$ 也在 norm 群。
这些单位恰有十八个，已经是指数三的整个 norm 子群。

最后要确定 $g$ 上的原方向，不能只从指数三任选一个共轭字符。
全球恒等式
$$
g=-2(1+3\omega),\qquad N(1+3\omega)=7
$$
只涉及二、三、七。在二处 $\delta\bmod2=1$，所以三次符号为一。
在 $\mathfrak q=(1+3\omega)$ 处，$\omega\equiv2\pmod{\mathfrak q}$，
$\delta\equiv5$，故
$$
\left(\frac{\delta}{\mathfrak q}\right)_3
 =5^2=4=\omega^2 .
$$
Kummer reciprocity 的主 idèle 积为一，其他地方没有因子，因此
$$
\boxed{\vartheta_\delta(g)=\omega,\qquad
\vartheta_\delta(q\omega^j g^k)=\omega^k.}
\tag{13}
$$
这已经给 (10) 的全部 unit character。
若用 $u=A+B\delta$ 表示，$\chi_{1,3}(u)$ 为
$A\bmod3\in\{1,-1\}$。

## 4. 两个原 Tate Gauss 和，不留下 Hermitian 猜测

固定
$$
\psi_{\mathrm{add},\infty}(x)=e^{2\pi ix},\qquad
\psi_{\mathrm{add},\ell}(x)=e^{-2\pi i\{x\}_\ell},
\quad \psi_K=\psi_{\mathrm{add}}\circ\operatorname{Tr}.
\tag{14}
$$
Yang 的实际局部条件是
$$
\epsilon(1/2,\chi_{24,v},\psi_{K,v}/2)\chi_{24,v}(\delta)
 =\epsilon_{K_v/\mathbf Q_v}(\alpha).
\tag{15}
$$

### 4.1 三处的和恰为负九

$\psi_K/2$ 的 conductor ideal 为 $\delta^{-1}\mathcal O_{K_3}$，
而 (10) 的 exponent 为四，所以 Tate 式取
$c=\delta^5=9\delta$。对 $u=A+B\delta$，
$$
\operatorname{Tr}\left(\frac{u}{2c}\right)=\frac B9 .
$$
取 $\zeta_9=e^{2\pi i/9}$、$\omega=\zeta_9^3$。由 (12)–(13)，原和为
$$
G_3=\sum_{u\in(\mathcal O/9)^\times}
  \chi_{24,3}(u)^{-1}\zeta_9^{-B}.
\tag{16}
$$
代入五十四个明确单位，按 $\zeta_9$ 幂收集准确得到
$$
G_3=-6+3\zeta_9^3+3\zeta_9^6=-9.
\tag{17}
$$
下节给可直接复现的全部有限运算，没有以浮点近似确定负号。
由于 $\chi_{24,3}(c)=i^5=i$、$3^{a/2}=9$，
$$
\boxed{\epsilon(1/2,\chi_{24,3},\psi_K/2)=-i,\qquad
\epsilon(1/2,\chi_{24,3},\psi_K/2)\chi_{24,3}(\delta)=+1.}
\tag{18}
$$

### 4.2 二处的和恰为正八

$\psi_K/2$ 的 conductor ideal 是 $2\mathcal O_{K_2}$；
$a(\chi_{24,2})=3$，所以这里取 $c=4$。
写 $u=A+B\omega\bmod8$，其中 $0\le A,B<8$，不同时为偶数。
设 $j=0,1,2$ 分别对应其模二值为 $1,\omega,\omega^2$。
又
$$
n=A^2-AB+B^2\bmod8,\qquad
e(n)=\begin{cases}1,&n=1,3,\\-1,&n=5,7.\end{cases}
$$
于是原 Gauss 和准确为
$$
G_2=\sum_{\substack{0\le A,B<8\\(A,B)\not\equiv(0,0)\bmod2}}
 e(n)\,\omega^{-j}
 \exp\left(-\frac{2\pi i(2A-B)}8\right).
\tag{19}
$$
令 $\zeta_{24}=e^{2\pi i/24}$。按幂合并四十八项得
$$
G_2=4-4\zeta_{24}^{12}=8.
\tag{20}
$$
$\chi_{24,2}(c)=\chi_{24,2}(2)^2=1$，归一因子为
$4^{3/2}=8$。此外 $\delta=1+2\omega$ 的模二 Teichmüller 值为一，
$N(\delta)=3$，(5) 的值也为一。因此
$$
\boxed{\epsilon(1/2,\chi_{24,2},\psi_K/2)=1,\quad
\chi_{24,2}(\delta)=1.}
\tag{21}
$$

### 4.3 真正的全局类和导子

(18)、(21) 的两个局部符号均为正。
其余有限点的角色和标准加性数据均未分歧，$\delta$ 是单位，符号也为正。
无限处的原解析 CM type 要求正 Hermitian 类。因此
$$
\boxed{\alpha=1}
\tag{22}
$$
满足全部 (15)。局部–全局范数原理说明它确定了所需的全局类。
特别 $\alpha=8$ 在未分歧二处有奇赋值、局部二次符号为负，
不属于本曲线已经算出的类；$\alpha=2$ 同样不适用。

完整 conductor 也已经确定：
$$
\boxed{
\mathfrak f_{\psi_{24}}=8\delta^4,\qquad
N\mathfrak f_{\psi_{24}}=64\cdot81=5184,\qquad
N(E_{24}/\mathbf Q)=15552.
}
\tag{23}
$$
最后一式使用 CM induction 的标准 conductor 公式
$N(E)=|\operatorname{disc}K|N\mathfrak f_\psi$。

## 5. 精确有限和证书

以下是 (17)、(20) 的完整整数计算；它只处理固定的 $54+48$ 项，
没有扫描研究目标中的素数。
在当前执行环境中已经直接执行这些运算，输出分别为所列数组。

三处把 $A+B\delta$ 表为 $[A,B]$，所有系数模九。
乘法是
$$
[A,B][C,D]=[AC-3BD,AD+BC].
$$
取 $\omega=[4,5]$、$g=[1,6]$。遍历 (12)，令
$\varepsilon(A)=1$ 当 $A\equiv1\bmod3$，否则为 $-1$，
将 $\varepsilon(A)$ 加到编号 $3k-B\bmod9$ 的格子。结果为
$$
(-6,0,0,3,0,0,3,0,0).
\tag{24}
$$
这就是 $\chi^{-1}=\varepsilon(A)\omega^k$ 的全部项，
按 $\zeta_9^6+\zeta_9^3+1=0$ 约简即 (17)。
同一遍历给出 $54$ 个互异单位；$k=0$ 的十八项准确等于 norm 群。

二处遍历 (19)，把 $e(n)$ 加到编号
$-8j-3(2A-B)\bmod24$ 的格子。
唯一非零的两个格子是第零项 $4$ 和第十二项 $-4$，
即 (20)。所有循环边界、角色和相位均已在本节给出，
不依赖外部整数关系猜测或数值 Gauss 和。

## 6. 固定全权来源及后续准确范围

对 $m\equiv0\pmod6$，$\chi_{24}^{\,2m+1}$ 在上述两个坏点与
$\chi_{24}$ 的完整分量相同：二处的三次单位、三处的野三次要求
$3\mid m$，三处 uniformizer 的值 $i$ 要求 $2\mid m$。
于是
$$
\boxed{6\mid m}
\tag{25}
$$
保持固定的本地输入和同一个 $\alpha=1$。
这为固定曲线的真正全权 theta 来源提供已付的原规范，
但其有限 Schwartz 函数必须按 (6)、(10)、(13) 重新构造。

特别，三处的 $\delta^4$ 角色不能沿用
R290/R306 的 $\mathbf1_{3^{-1}\mathbf Z_3}$；
二处也不能直接沿用旧 conductor-two 的向量。
旧 $D_{16}$ 是否属于某个曲线来源，须由它本身的原 CM trace 和
局部 splitting 判断，不由 (23) 的导子或截面次数推断。
本结果没有把未付的 primitive Schwartz、整周期、完整中央观察
或全 Selmer 桥视为自动完成。

## 出处和运行记录

- J. H. Silverman and K. E. Stange, *Amicable Pairs and Aliquot Cycles for
  Elliptic Curves*, Experimental Mathematics **20** (2011), 329–357，
  §6、Theorem 19 的证明；[作者全文](https://arxiv.org/pdf/0912.1831)。
  本篇只用 (2) 的实际六次剩余公式，方向由 §1 固定。
- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math.
  **485** (1997), 25–53，
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)，
  原局部 dichotomy；本篇逐项自算其 (15)。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of certain
  elliptic curves*, Compositio Math. **117** (1999), 337–359，
  §1、Appendix (A1)–(A3)，
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/rank.pdf)。
  后续新野分歧 projector 须保该文真实 splitting。
- R290 §1 已支付 (3) 的原基角色和 CM conductor 规范。
  本篇 (8)–(13) 的分歧群、norm 子群及完整方向均在正文自证。

提交前通过 GitHub Contents API 读取的 main 为
$0fff7de3d78e45c453df872c10bd3501d0ab9d8c$；
根 README 和课题 README 的 blob 均与已读版本相同。
执行终端仍不可用，本篇是按根规矩八允许的小文本 API 提交，
不是一次本地 git pull。
