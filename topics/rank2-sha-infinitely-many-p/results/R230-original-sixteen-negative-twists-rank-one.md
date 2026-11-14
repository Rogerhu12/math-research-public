# R230：原十六辅助域的负扭曲秩一严格证书

日期：2026-11-13。**状态：已证明的固定算术输入；主目标尚未完成。**

固定原曲线
$$
 E:\quad y^2+y=x^3+x^2-2x
$$
和 R153 的同一组十六个基本判别式
$$
\mathcal D=\{-7,-11,-67,-20,-24,-35,-52,-187,-232,-267,
-372,-483,-555,-795,-1435,-532\}.
\tag{1}
$$
本篇证明每个 $D\in\mathcal D$ 都满足
$$
 \boxed{\quad
 \operatorname{ord}_{s=1}L(E^{(D)},s)
 =\operatorname{rank}E^{(D)}(\mathbb Q)=1,\qquad
 \Sha(E^{(D)}/\mathbb Q)\text{ 有限}.
 \quad}
\tag{2}
$$
这里 $E^{(D)}$ 指由 $\mathbb Q(\sqrt D)$ 定义的二次扭曲；
$D$ 偶时使用该域的基本判别式作为角色导子。

(2) 对原十六域全部成立。因此 R149 的十六角色独立性、R150
的原完整类群和、R153 的全部源不分歧证书以及 R156 的原诱导族
均可原样使用。没有选择新的域、替换 $\Phi_D$，或移植旧 CM
中心证书到另一个源。

## 1. 可复算证书与精确范围

[无外部依赖的 JavaScript 脚本](../scripts/check-sixteen-negative-twist-rank-one.js)
和[实际运行输出](../notes/data/sixteen-negative-twist-rank-one-certified.json)
给出完整有限证书。运行命令为

~~~sh
node topics/rank2-sha-infinitely-many-p/scripts/check-sixteen-negative-twist-rank-one.js
~~~

两个整数算法从曲线方程独立计算 $a_n$，并逐项核对到
$60000$。非整数部分全部使用向外舍入区间；没有调用
Math.exp、Math.log、Math.sqrt、曲线数据库或秩函数。
下表是严格开区间，不是小数近似的舍入猜测。JSON 另外保存
每行的完整部分和区间、无限尾界和最后区间。

| $D$ | $N_D=389D^2$ | 使用项数 $M_D$ | 已证明的 $L'(E^{(D)},1)$ 开区间 |
|---:|---:|---:|---:|
| $-7$ | $19061$ | $440$ | $(4,5)$ |
| $-11$ | $47069$ | $691$ | $(7,8)$ |
| $-67$ | $1746221$ | $4207$ | $(58,59)$ |
| $-20$ | $155600$ | $1256$ | $(3,4)$ |
| $-24$ | $224064$ | $1507$ | $(3,4)$ |
| $-35$ | $476525$ | $2198$ | $(4,5)$ |
| $-52$ | $1051856$ | $3265$ | $(10,11)$ |
| $-187$ | $13602941$ | $11740$ | $(28,29)$ |
| $-232$ | $20937536$ | $14566$ | $(53,54)$ |
| $-267$ | $27731421$ | $16763$ | $(67,68)$ |
| $-372$ | $53831376$ | $23355$ | $(36,37)$ |
| $-483$ | $90749421$ | $30323$ | $(52,53)$ |
| $-555$ | $119821725$ | $34844$ | $(54,55)$ |
| $-795$ | $245857725$ | $49911$ | $(53,54)$ |
| $-1435$ | $801038525$ | $60000$ | $(97,98)$ |
| $-532$ | $110096336$ | $33400$ | $(42,43)$ |

例如 $D=-24$ 的最后区间包含于
$(3.30625546,3.30625553)$。最宽的一行 $D=-1435$ 仍包含于
$(97.22195,97.22640)$；其完整无限尾界小于 $0.002220$。
这里使用的是有限、严格的非零证明，随后通过已发表的
Gross--Zagier--Kolyvagin 定理推出 (2)，没有把数值近零或
有限目标素数样本当作课题完成。

## 2. 原曲线、每个导子与根数

R2、R136 已从原方程证明
$$
 c_4=112,\qquad c_6=-856,\qquad \Delta=389,
 \qquad N_E=389,\qquad w(E)=+1.
\tag{3}
$$
唯一坏位是 $389$，为 split $I_1$。本脚本重新精确检查
(1) 每个数都是基本判别式，且 $\chi_D(389)=1$；也重新
用 $\mathbb F_2$ 消元核对十六平方类独立。这个检查没有
替代 R153 的 CM 源证明，只确认所用域与原表完全相同。

设 $\chi_D$ 为导子 $|D|$ 的本原二次角色。因为
$(D,389)=1$，在 $q\mid D$ 处原曲线的 Tate 表示不分歧。
扭曲后的惯性表示是两个非平凡二次角色，其 Artin 导子
指数为 $2a_q(\chi_D)=2v_q(D)$，且惯性不变量为零。
这包括 $q=2$，不把偶判别式误按奇素数公式计算。
在 $389$，$\chi_D(389)=1$，扭曲与原曲线局部同构；
其余位仍好约化。因此
$$
                   N_D=389D^2.
\tag{4}
$$

也可直接由基变计算根数，而无需猜测偶判别式的附加符号。
$F_D=\mathbb Q(\sqrt D)$ 的所有有限好位贡献 $+1$；
$389$ 分裂为两个 split multiplicative 位，其根数乘积
是 $(-1)^2=+1$；唯一复位贡献 $-1$。于是
$w(E/F_D)=-1$。由
$L(E/F_D,s)=L(E,s)L(E^{(D)},s)$ 及 (3)，得到
$$
                 w(E^{(D)})=-1,\qquad L(E^{(D)},1)=0.
\tag{5}
$$

若 $L(E,s)=\sum a_n n^{-s}$，相同局部计算同时给出
$$
 L(E^{(D)},s)=\sum_{n\ge1}b_{D,n}n^{-s},\qquad
 b_{D,n}=a_n\chi_D(n).
\tag{6}
$$
在 $q\mid D$ 的局部因子是 $1$，正与 $\chi_D(q)=0$
一致；在 $389$ 的局部因子也保留，故 (6) 不是去坏位
$L$ 函数。

## 3. 两套独立整数系数及完整 Mellin 公式

对每个素数 $q\le60000$，第一算法建立
$$
 c_q(t)=\#\{y\bmod q:y^2+y=t\}
$$
的精确直方图，并计算
$$
       a_q=q-\sum_{x\bmod q}c_q(x^3+x^2-2x).
\tag{7}
$$
第二算法在奇 $q$ 计算判别式角色和
$$
       a_q=-\sum_{x\bmod q}
             \left(\frac{4x^3+4x^2-8x+1}{q}\right).
\tag{8}
$$
在 $q=2$ 直接使用四个仿射代入得到 $a_2=-2$。
两算法各自生成全部系数。对最小素因子 $q\mid n$、
$m=n/q$，递推为
$$
 a_n=
 \begin{cases}
 a_q,&m=1,\\
 a_q a_m-q a_{m/q},&q\mid m,\ q\ne389,\\
 a_q a_m,&\text{其余情形}.
 \end{cases}
\tag{9}
$$
这里 $a_{389}=1$ 也由原奇异三次方程的点数得到。
每个系数逐项相等，且每个好素数的 Hasse 界亦在整数上检查。
在本范围内，(7)--(8) 所有多项式中间整数绝对值小于
$4\cdot60000^3+4\cdot60000^2+8\cdot60000+1<2^{53}$，
所以这些整数计算没有浮点取整误差；角色和与递推的
整数也在此范围内。另由 $|a_n|\le2n\le120000$，在好素数
递推中暂存的 $|a_q a_{n/q}|\le4n/\sqrt q<170000$，
坏位 $a_{389}=1$；它们均小于 $2^{31}$，故脚本的 Int32
系数数组没有溢出。

令
$$
 c_D=\frac{2\pi}{|D|\sqrt{389}},\qquad
 E_1(x)=\int_x^\infty \frac{e^{-t}}t\,dt.
$$
由 (5) 的负号函数方程，在 Mellin 积分的
$1/\sqrt{N_D}$ 处分割并换元，得到
$$
 \boxed{\quad
 L'(E^{(D)},1)
      =2\sum_{n\ge1}\frac{a_n\chi_D(n)}n E_1(c_Dn).
 \quad}
\tag{10}
$$
为核对系数 $2$，置
$f_D(iy)=\sum b_{D,n}e^{-2\pi ny}$。分割后的 Mellin
积分在 $s=1$ 的导数是
$2\int_{1/\sqrt{N_D}}^\infty f_D(iy)\log(y\sqrt{N_D})\,dy$；
乘 $(2\pi)/\Gamma(1)$ 后逐项分部积分，恰给 (10)。
由于 $L(E^{(D)},1)=0$，Gamma 因子求导没有额外项。

Hasse 界与素数幂递推给
$|a_n|\le d(n)\sqrt n\le2n$。又
$0<E_1(x)\le e^{-x}/x$，所以删去 $n>M$ 的误差严格不超过
$$
 \boxed{\quad
 \left|2\sum_{n>M}\frac{a_n\chi_D(n)}n E_1(c_Dn)\right|
 \le
 \frac{4e^{-c_D(M+1)}}{c_D(M+1)(1-e^{-c_D})}.
 \quad}
\tag{11}
$$
脚本向上取 (11) 的区间端点，并对已求部分和向两侧加入
该完整尾界。不同 $D$ 使用不同 $M_D$ 只影响效率，不改变
公式或证明。

## 4. 每一项的严格区间误差

### 4.1 基本运算与常数

脚本用同一 64 位缓冲区访问 binary64 数和两个 32 位整数，
实现相邻浮点数 $\operatorname{up}$、$\operatorname{down}$。
每次加、减、乘、除后，按四个端点积或倒数的正确顺序，
分别向下一格和上一格扩张。因此基本运算的精确实数结果
总落在所得区间内；零、负数及跨位进位均由同一位操作处理。
脚本先检查字节序和 $1$ 的 binary64 表示。所用数学量
均无无穷或零分母。JSON 端点是序列化的 binary64 区间
端点；表中整数开区间则无需任何小数解释约定。

$\pi$ 使用 Machin 恒等式
$$
 \pi=16\arctan(1/5)-4\arctan(1/239),
$$
每个交错级数取 $32$ 项并加入首漏项绝对值。
$\sqrt{389}$ 则先用 BigInt 牛顿迭代精确计算
$$
 r=\lfloor10^{14}\sqrt{389}\rfloor,\qquad
 \frac r{10^{14}}\le\sqrt{389}<\frac{r+1}{10^{14}}.
$$
$r,r+1$ 都小于 $2^{53}$，其转为 Number 是精确的；
两次除法仍向外扩张。因此没有调用未经认证的平方根。

对数以
$$
 \log y=2\sum_{j=0}^{39}\frac{t^{2j+1}}{2j+1}+R,\qquad
 t=\frac{y-1}{y+1},\qquad
 |R|\le\frac{2|t|^{81}}{81(1-t^2)}
\tag{12}
$$
计算。先以 $2$ 的幂缩放到 $1\le y\le2$ 附近；
$\log2$ 本身用 $t=1/3$ 的同一公式。缩放端点可能超出
边界一个区间宽度，但始终有 $|t|<0.34$，(12) 仍有效。

Euler 常数用
$$
 \gamma=H_{64}-\log64-\frac1{128}
       +\sum_{k=1}^{5}\frac{B_{2k}}{2k\,64^{2k}}+R_\gamma,
 \qquad
 |R_\gamma|\le\frac{|B_{12}|}{12\,64^{12}},
 \quad B_{12}=-\frac{691}{2730}.
\tag{13}
$$
Euler--Maclaurin 的正实轴首漏项界给出 (13)；
每个有理项仍用向外区间计算。
故 $\gamma$ 也没有从一段未经认证的小数抄入。

### 4.2 小参数与正连分数

因为 $0<c_D<0.1$，$q_D=e^{-c_D}$ 用 $18$ 阶交错
Taylor 多项式及第 $19$ 项上界计算。
递推区间乘积 $q_D^n$ 同时保留每次乘法误差。

对 $0<x<1$ 使用
$$
 E_1(x)=-\gamma-\log x
        -\sum_{k=1}^{22}\frac{(-x)^k}{k\,k!}+R_{22},
 \qquad
 |R_{22}|\le\frac{x^{23}}{23\cdot23!}.
\tag{14}
$$
对其余正 $x$ 使用实际正连分数
$$
 e^xE_1(x)
 =\frac1{x+\dfrac1{1+\dfrac1{x+\dfrac2{1+
              \dfrac2{x+\dfrac3{1+\cdots}}}}}}.
\tag{15}
$$
记 $F_N(x)$ 为保留 $N$ 个内部分子的有限收敛子，
分子序列 $1,1,2,2,3,3,\ldots$，分母依次为
$1,x,1,x,\ldots$。全部分子和分母为正，有限分式的
行列式恒等式说明奇收敛子从下方夹逼、偶收敛子从上方
夹逼其极限。结合 (15)，对每个 $x>0$ 都有
$$
                 F_{65}(x)\le e^xE_1(x)\le F_{64}(x).
\tag{16}
$$
所以即使它们尚未接近机器精度，二者之间的全部差值也
保留在误差内。脚本分别对两个收敛子作区间运算，再乘
$q_D^n$ 的区间；没有把某个收敛子当成准确值。
区间碰到 $x=1$ 时直接使用 (16)，不存在接缝遗漏。

最后将 (14) 或 (16) 与准确整数 $2a_n\chi_D(n)$、
向外除法 $1/n$ 相乘。负系数按区间乘法反转端点。
所有逐项误差、求和误差与 (11) 一起进入最后区间。
这给出了表中各个严格正下界的完整验证链。

(14)--(15) 可见 DLMF §8.19 的公式 8.19.8、8.19.17；
(13) 的余项界见 DLMF §5.11(ii)。这里需要的截断与误差
已明确写出，不依赖特殊函数软件对精度的口头保证。

## 5. 从严格非零到同一原对象上的统一算术输入

由 (5)、表中非零及 Gross--Zagier--Kolyvagin 的已发表
解析秩一结论，每个 $E^{(D)}$ 都满足 (2)。
令 $\mathcal B$ 为以下固定有限集合的并：原 R150、R153、
R156 的例外素数；十六条已证明有限的
$\Sha(E^{(D)}/\mathbb Q)$ 的素因子；十六条固定曲线有理
挠子群阶的素因子。这里证明集合有限即可，不假称已经
计算出十六个 Sha 的准确阶。

对任意 $p\notin\mathcal B$，同时对全部 $D\in\mathcal D$，
二次基变和通常 Kummer 正合列给
$$
 \boxed{\quad
 s_-(D,p):=\dim_{\mathbb F_p}\operatorname{Sel}_p(E/F_D)^-=1.
 \quad}
\tag{17}
$$
这些是相同的、通常局部条件下的 Selmer 群。
在 $p^\infty$ 级别，负号部分的 $\mathbb Z_p$ 余秩对每个
$p$ 都是一；为了获得模 $p$ 维数恰一，才删去上述有限集。

R149--R153 的联合输入中 $p$ 无界，故删除 $\mathcal B$
保留其无穷性与全部数量主项。十六个域未变，
$2^{-16}$ 坏类密度和
$$
 64\cdot2^{-16}\frac{1-667/1000}{(667/1000)^2}<0.00075
          <0.001359
\tag{18}
$$
仍是原来的精确预算。因而仍有某一个固定原表域 $F_*$，
以及无穷多个相同输入 $p,\ell,Q$，同时满足原
$\widehat h(Q)=o(p)$、普通分裂、非异常和源不分歧条件，
并新增 (17)。这里没有与另一个未知分布的无穷集合求交。

置
$$
 r=\operatorname{rank}E(\mathbb Q)\ge2,\qquad
 d_p=\dim_{\mathbb F_p}\Sha(E/\mathbb Q)[p],\qquad
 s_+=r+d_p.
$$
R2 只在本论证中提供 $r\ge2$，不调用数据库中的上界 $2$。
R156 的同一完整原族公式现在化为
$$
 \boxed{\quad
 \nu=\max(s_+,s_-)-1=s_+-1=r-1+d_p.
 \quad}
\tag{19}
$$
因此单辅助节点的实际非零严格强于“某个节点非零”。
更准确地，在 R156 的原始族上，
$$
 \begin{split}
 &\exists\text{ 单个合法辅助素数 }q:
       \overline c_q^{E,\mathrm{raw}}\ne0\\
 &\qquad\Longleftrightarrow\quad
       \nu=1
 \quad\Longleftrightarrow\quad
       r=2,\ \Sha(E/\mathbb Q)[p^\infty]=0.
 \end{split}
\tag{20}
$$
$\nu\ge1$ 由 $s_+\ge2$ 给出；$d_p=0$ 等价于整个
$p$ 初级群为零，因为任何非零 $p$ 初级元素都有非零阶
$p$ 多重。R156 的逐节点单位比较同样把 (20) 搬到
原 $A$ 族，但没有自动给出其中的实际非零节点。

必须区分 $q$ 与构造 $C_p$ 扩张的原素数 $\ell$：
这里 $p\nmid a_\ell(E)$，而通常的 Kolyvagin 辅助素数
$q$ 满足 $a_q\equiv q+1\equiv0\pmod p$。
不能将原 $\ell$ 直接重新命名成 (20) 的辅助标签。

## 6. 对原 delta 指数实际新增的限制及未付步骤

保留原
$$
 Q=[t_0]\operatorname{Tr}_{F[\ell]/L}P[\ell]
      =\delta^a\varepsilon w,\qquad
 S=\Sha(A/F)[p^\infty].
$$
R156 已给 $S\simeq M\oplus M$ 及
$\operatorname{length}_{\mathcal O}M=a+1$。
结合 (17)，原 Kummer 直线的符号 $(-1)^a$ 给
$$
 \dim S[\delta]^+=s_+-\mathbf1_{\{a\ {\rm even}\}},\qquad
 \dim S[\delta]^-=1-\mathbf1_{\{a\ {\rm odd}\}}.
\tag{21}
$$

R146 §4 的实际原始层配对使奇长度块的正、负 socle
数相等，偶长度块每个符号的块数均为偶数。
因此 (21) 还精确说明：

- 若 $a$ 偶，恰有一对奇长度循环块；其 socle 符号
  一正一负。其余块全部为偶长度，负 socle 数为零。
- 若 $a$ 奇，所有块都为偶长度，且全为正 socle。

每种情况的同长度块均成双。因此 $s_+$ 为偶数，
$M$ 的循环块数恰为 $s_+/2$；$a$ 偶时 $M$ 恰有
一个奇长度块，$a$ 奇时没有奇长度块。逐块求最小长度给
$$
 \boxed{\quad
 a\ge
 \begin{cases}
 s_+-2=\nu-1,&a\text{ 偶},\\
 s_+-1=\nu,&a\text{ 奇}.
 \end{cases}
 \quad}
\tag{22}
$$
特别 $\nu$ 为奇数，且
$\nu\le2\lfloor a/2\rfloor+1$。
这是同一真实有限 Sha 的限制，没有把自由格或模拟有限模
当成实际群。

原首项仍是 $(\tau-1)Q$，自由格指数仍为 $a+1$。
(17) 没有消去范数关系
$N_\Gamma Y_n=a_\ell P[n]$，也没有把原诱导族全体除以
$\delta$。故不能把 R156 的 $a+1$ 改成 $a$。
(22) 对 $a$ 给下界；它保留 $a=2$、$\nu=3$ 的可能，
也容许 $\nu=1$ 但指定 $Q$ 的 $a$ 较大。

于是 R146 的 $a\le1$ 充分门保持有效，(20) 给出本次
固定算术输入后的另一条精确任务：证明同一原完整族的
某个单辅助类在无穷多个原输入 $p$ 上非零。
本篇证明的是十六个负方向已统一支付，不宣称这个跨 $p$
的原始性步骤已经完成。

## 7. 出处与依赖

- [R2](R2-explicit-rank-two-curve.md)、
  [R136](R136-noncm-e389-minus7-heegner-input.md)：原方程、
  秩下界、挠点、模型、导子及 $D=-7$ 的既有严格校准。
- [R149](R149-finite-family-splitting-and-large-prime-factors.md)、
  [R150](R150-sixteen-fields-and-complete-class-st-jets.md)、
  [R153](R153-sixteen-unramified-cm-sources.md)：原域表、
  十六角色筛预算、完整类群和及实际源不分歧。
- [R146 完整证明](../notes/2026-11-12-noncm-two-step-criterion-with-varying-heegner-field.md)
  和 [R156](R156-fixed-field-primitive-system-and-exact-index.md)：
  通常局部条件、原 Kummer 符号、原始层配对及逐节点比较。
- B. Gross--D. Zagier, *Heegner points and derivatives of L-series*,
  Invent. Math. **84** (1986), 225--320；V. Kolyvagin,
  *Euler systems*, Grothendieck Festschrift II (1990)：
  本篇只使用已发表的解析秩一结论。
- NIST DLMF，
  [8.19.8](https://dlmf.nist.gov/8.19.E8)、
  [8.19.17](https://dlmf.nist.gov/8.19.E17)、
  [5.11(ii)](https://dlmf.nist.gov/5.11.ii)：所用特殊函数恒等式
  和正实轴首漏项界；具体截断成本见 §4。
- [ECMAScript Number 运算规范](https://tc39.es/ecma262/multipage/ecmascript-data-types-and-values.html#sec-ecmascript-language-types-number-type)：
  binary64 四则与整数余数的语义。脚本在每次基本运算后
  显式外扩，未把双精度库函数的未声明误差当作严格界。
