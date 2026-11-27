# 原另一 dyadic 三线的 inverse-beta27 固定中央值输入

**2026-11-27 21:55 UTC 审计更正（优先于下文原登记）。** [共同因子与连续性审计](2026-11-27-original-psi4-common-factor-digit-and-continuity-audit.md)已证明固定底数幂不能修复完整双阶乘的离散不连续，并定位 Kriz Proposition7.20 的共同连通延拓、Corollary7.21 的换点/定义域，以及§9.3负权 primitive 的未付接合。因此经过这条链的“连续几何 cross”“负端点等于原 AJ”“共同几何因子为单位”现均为**条件结论**。正整数权原来源、完整 fixed-base 图和直接 proper-fp 公式、纯 Newton 函数及其整数恒等式保持独立有效；不得用后者命名缺失的几何族。本更正没有断言被引用定理为假。

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

本注核定原 $F_-=(1-P_4)\nabla_{34}^2S$真正出现的三个新固定角色。第6节已消费公开 Actions 的严格全值回执，三个中央值均为正；不以此声称原 canonical 条件或无穷素数门已完成。

## 1. 原补空间的完整角色

原 R798 的 whole type4 有六维。R806(4)已经准确区分
$$
(v_+,j'=2,8,14)\ \oplus\ (v_-,j=4,10,16).
$$
$P_4$取第二部分，$F_-$在第一部分。
对第二部分保持原 $l_j=j-9=-5,1,7$和
$$
\eta_j((\alpha))
 =\epsilon_2(\alpha)\vartheta_{l_j}(\alpha)^{-1}.
\tag{1}
$$
第一部分的实际标签为 $j'=18-j$，所以 $l_{j'}=-l_j$。
几何 $\omega$的标签仍是 $g=\omega^2$：
$v_+$上的本征值1与 $\tau_{j'}(g_0^{12})=\omega$给 type4。
其 idèle 单位角色在2处为 $\epsilon_2$、17处为 $\vartheta_{-l_j}$；
单位 $\omega$的两个值相乘为1。连同原3处 uniformizer 的
$-1$及2、17的值1，类数一给全局身份
$$
\boxed{\eta_{j'}^+=\eta_j^{-1}.}
\tag{2}
$$
这不是只将一个 CM13 根取共轭。
对应最高线的新标签是
$\lambda_j^+=\psi_0^3\eta_j$，与原
$\lambda_j=\psi_0^3\eta_j^{-1}$分别保留。

在同一个固定
$\operatorname{AI}(\psi_{27}^2)$的双核中，把 $\eta_j$
换成(2)，第二个实际 rank-one 槽准确为
$$
\boxed{\beta_j^+=\psi_{27}\eta_j^{-1}.}
\tag{3}
$$
它不是 R994 已算的 $\psi_{27}\eta_j$，也不是后者的
$K/\mathbf Q$共轭 $\bar\psi_{27}\eta_j^{-1}$。
故其真空不能由 R994 的三个正值直接推出。

## 2. 排重和不同来源的定位

已核 R806、R809§§3--4：那里是原 type4 负二来源及原
nine-character 连接，没有计算(3)的 weight2 中央值。
R991(9)--(10)、R994、R998中 level31212 的三个固定值
都是 $\psi_{27}\eta_j$。R826提到的
$\eta_j^{-2}\psi_0$、$\eta_j^{-7}\psi_0$在3处与(3)不同：
(3)具有 $\psi_{27}$的 wild conductor $\delta^2$，
前者仅有 $\psi_0$的 conductor $\delta$。

(3)也不等于固定 $E_{17}$、$E_{17^3}$或$E_{17^5}$的
椭圆 CM 角色。它在17惯性上的有限部分准确阶18；
这些 $\mathbf Q$上 $j=0$曲线的 sextic twist 部分在17的阶
均整除6。因而本次是三个未支付的 fixed inputs，不重复旧值，
亦不进行任何 $p$扫描。

## 3. 全导子、root 和 Mellin 公式

在 R991(5)的同一 idèle 规范下，$\beta_j^+$的 unitary 部分为
$$
\begin{array}{c|c|c}
v&\text{单位值}&\text{uniformizer值}\\ \hline
2&\epsilon_2&-1\text{ 于 }2\\
3&u\text{ 于 }\mu_6&-i\text{ 于 }\delta\\
17&\vartheta_{-l_j}&-1\text{ 于 }17 .
\end{array}
\tag{4}
$$
这里固定 $\epsilon_2=\operatorname{Teich}_{\mu_3}$；主理想值与 idèle 单位值互逆。旧 $\eta_j$的主理想值为 $\epsilon_2\vartheta_{l_j}^{-1}$，逆角色的主理想值为 $\epsilon_2^{-1}\vartheta_{l_j}$；故(4)与下方(8)保持同一规范。

因此完整导子仍为 $(34\delta^2)$，weight2 theta level为
$$
N=|D_K|\,\mathrm N(34\delta^2)=31212.
\tag{5}
$$
有限坏 Euler 因子为1；restriction to rational idèles与
R994相同，故 theta 的 nebentypus平凡。

root可相对于 R991/R994已付的 $\beta_j$逐处核定。
2处标准 trace 加性角色在 $\mathbf F_4$上给
$$
G(\epsilon_2)=G(\epsilon_2^{-1})
 =1-\omega-\omega^2=2.
$$
原 different 的2处单位剩余类为1，uniformizer值又相同，
故两个局部 epsilon相同。
17处两个非平凡角色都在 $\mathbf F_{17}^{\times}$上平凡，
且 $\vartheta_{\pm l_j}(\delta)=-1$，所以同一个 trace求和给
$$
G(\vartheta_{l_j})=G(\vartheta_{-l_j})=-17.
$$
3处整个 character，包括主单位和$\delta$，与旧$\beta_j$
完全相同；无穷型也相同。所有 good places未变为ramified。
因此
$$
\boxed{W(\beta_j^+)=W(\beta_j)=+1.}
\tag{6}
$$
这里尚未从 $+1$推非零。

写
$$
L(\beta_j^+,s)=\sum_{n\ge1}a_{n,j}^+n^{-s},\qquad a_{1,j}^+=1 .
$$
由(5)--(6)的 weight2 函数方程，将 Mellin 积分在
$1/\sqrt N$分开，给准确的完整等式
$$
L(\beta_j^+,1)
=2\sum_{n\ge1}\frac{a_{n,j}^+}{n}
   \exp(-2\pi n/\sqrt N).
\tag{7}
$$
这是本次执行所用的公式。

## 4. 精确理想枚举和无限尾

每个素于3的理想恰有一个
$\alpha=a+b\omega\equiv1\bmod3$的生成元。
保持 R735 的
$g_0=(6,8)\in\mathbf F_{289}^{1}$、$g_0^6=\omega$。
若
$$
\epsilon_2(\alpha)=\omega^k,\qquad
\alpha^{16}\bmod17=g_0^e,
$$
则本次每个完整理想的贡献为
$$
\boxed{\beta_j^+((\alpha))
 =\alpha\,\zeta_{18}^{-6k+l_je}.}
\tag{8}
$$
只反转 $\eta_j$的指数，$\psi_{27}$的 primary generator
$\alpha$不取共轭。
源码使用 $\mathbf Z[\zeta_{18}]$的精确六坐标，
先完整累加理想，再逐项核实系数为实及三个
$j=10\to16\to4\to10$的 $\zeta_{18}\mapsto\zeta_{18}^7$
Galois关系。所有三个坏位均从原primitive Euler表移去。

参数固定为 $M=4096$、Arb256 bits。令
$q=\exp(-2\pi/\sqrt{31212})$。由
$|a_{n,j}^+|\le d(n)\sqrt n\le2n$，完整无限尾满足
$$
\left|
L(\beta_j^+,1)-2\sum_{n=1}^{M}a_{n,j}^+q^n/n
\right|
\le\frac{4q^{M+1}}{1-q}<2^{-180}.
\tag{9}
$$
最后的不等式由 Arb 的 outward intervals核实。
因此 enclosure是真正全值区间，而非没有尾的截断值。

独立脚本是
[check-original-inverse-beta27-central-values.py](../scripts/check-original-inverse-beta27-central-values.py)。
它沿用原 R994 算法，只把(8)的 $\eta$指数反转；
不重算 R994的旧三个角色。生产 guard在所有数学执行前检查
原 public Actions环境。没有写入 Fourier数组、枚举表或缓存。
输出只含新三个完整区间、来源和系数哈希、固定参数及实际
all_three_exclude_zero。即使某个区间含0，也会保存准确
COMPLETE回执，并保留“零未决定”的数学范围。

原算法依赖：
[check-r994-original-beta27-central-values.py](../scripts/check-r994-original-beta27-central-values.py)，
本次读取的 Git blob为
d6c27dca373eaccc77d4a349e572ec434f549cfe。
新脚本为自包含文件；不以执行该旧脚本作为前置步骤。

## 5. 本次输入将支付的门

第6节的三个新区间均排除零，因此原新的 positive theta 真空均非零。
这允许对 $F_-$的三条实际 finite sources，按已经支付的
full9双核、共同整模型及 fixed-base $p^2$族构造各自
真实几何读者。必须保留(2)--(3)的新 highest 和 mixed标签，
不把它们写成原 $F_+$的三条线。

原 canonical 二阶导数另有 $\zeta$扩展连接或等价的
横向 heat jet。它不因(3)的非零而变成一个 bounded theta
截面；后继的完整一阶关系仍须保留该 jet。


## 6. 三个新全值的实际公开回执

公开 Actions [run 46061560954](https://github.com/Rogerhu12/math-research-public/actions/runs/46061560954)，job **140716799525**，source
`5dc5780cc9c4835a54c615fcb3f723ccb00fdc78`，
于2026-11-27 20:08:41 UTC返回 **COMPLETE**，
`all_three_exclude_zero=true`。root已亲读完整job日志并核对本次脚本哈希。
原输入和参数恰为第4节，未改变角色或枚举截断。

完整精确累加包含1236个理想；全部系数实性、三条Galois关系、
全部坏Euler因子检查均通过。Arb的完整无限尾严格小于 $2^{-180}$。
将全值区间向外放宽为有理数区间，实际证明为

| 原 $j$ | 补块 $j'=18-j$ | 完整中央值 |
|---:|---:|---|
| $4$ | $14$ | $1/5<L(\beta_4^+,1)<21/100$ |
| $10$ | $8$ | $17/5<L(\beta_{10}^+,1)<7/2$ |
| $16$ | $2$ | $7/4<L(\beta_{16}^+,1)<9/5$ |

这里每个不等式都包括完整无限尾，不是仅对4096项的部分和。
因此三个真实 $\beta_j^+$的 positive theta 真空均非零。
这只支付第5节指定的固定输入；未据此制造原 canonical 坏条件的零关系。

复现与审计只保脚本、参数、run和摘要哈希，不另存Fourier数组或日志：

- 脚本8033B，SHA256 `c4386fbec87ba1b761698f9aa15435e55f930c63849129e0697186f473e5cfb8`。
- stdout2738B，SHA256 `0e222982e71122e6cad674141e0cc2c2fa0b86b69881f2d803e708f5d4730433`。
- 完整joblog11730B，SHA256 `74d594c036a68ec670e767061c98a1cbef05ca2ffa89ac2c02858a963941ae73`。
- 全部精确系数摘要 `befb8e58c4acab1fbf85e9376e2f71925cb8fa92901329c17056298f7cad495f`；
  完整理想计数摘要 `197a27aea74f2b3ddc258474696fc12bf41d9948bed9a761c9c87cc99d92ab00`。
- request标识中的2013只作唯一标识；实际提交/执行时刻是20:08UTC，以上真实回执为准。

## 7. 补块的实际 Schwartz、三个规范来源和真实 Artin 基

本节使用§6的三个完整中央值非零，不重新执行该计算。为避免把
新旧两种标签混同，记
$$
\mathcal I=\{(-,4),(-,10),(-,16),(+,14),(+,8),(+,2)\},
\qquad
\eta_{-,j}=\eta_j,\quad
\eta_{+,18-j}=\eta_j^{-1}.
\tag{10}
$$
对新补块，实际有限向量是 R806(18)--(21) 的同一个 Weil projector
所给的 $f_{j'}$，但二处取
$$
v_+=(1,t_+,-1,t_+),\qquad
t_+=(1+\sqrt3)/\sqrt2,\qquad j'=18-j .
\tag{11}
$$
即
$$
\phi_{2,j'}=f_A+t_+f_B,\quad
\phi_{3,j'}=\mathbf1_{3^{-1}\mathbf Z_3},\quad
\phi_{17,j'}=\sum_a f_{j'}(a)\mathbf1_{a/17+\mathbf Z_{17}},
$$
$$
a'_{j',n}=v_+(n\bmod4)f_{j'}(3n\bmod17).
\tag{12}
$$
三处的支撑、Fourier 变换、different 和 canonical 半特征全部原样保留。
二处范数是 $3+\sqrt3$；十七处仍保实际
$n'_{j'}=\sum_a|f_{j'}(a)|^2$，不以旧 $n_j$ 代替。
Hilbert90 的原方向 $g=u/\bar u=u^{-16}$ 及 quadratic splitting
给十七处标签 $9-l_j=18-j$。二处的实际单位角色是
$\epsilon_2$；这是§1说明的 idèle 单位值，
与主理想上的 $\epsilon_2^{-1}$ 互逆。

由 R806(4) 的全有限分解，(12)恰是
$(1-P_4)V_4$，没有额外平坦二挠 twist。
CM13 的共同标量仍是 $-\omega^2$，而二处标签由
$\omega^2$ 换成 $1$。所以原完整十三点 trace 的特征值为
$$
\mu'_{j'}=-\omega^2\zeta_{18}^{14j'}
 =\mu_j^{-1},\qquad (\mu'_{j'})^3=-\omega^2 .
\tag{13}
$$
这同时核对 R798 的 $T^3+\omega^2$，没有仅由这个多项式猜
finite characters。

首 $z^4$ 行在 $(1-P_4)\sigma^{34}$ 上准确为
$-136/13122\ne0$，因为 $\sigma^{34}$ 本身的首阶为34，
而 R798(10)的对应条目是 $136/13122$。
$T^3+\omega^2$ 在 $K$ 上不可约，三条来源是其完整
$K$-Galois 轨道，故该行不能杀其中任何一条。
于是存在唯一原模型规范
$$
S'_{j',\Lambda}(Z)=s'_{j'}D'_{j',1}(\Omega_0Z),
\qquad [z^4]D'_{j',1}=1,\quad s'_{j'}\in\mathbf R^\times .
\tag{14}
$$
全源按(12)定义，故这里的实性与原 R806 一样来自实际实偶
Fourier 序列，而不是另取谱向量。若需要精确抽取，可在
$(1-P_4)V_4$ 上应用
$$
\frac{\mathcal A_{13}^2+\mu'_{j'}\mathcal A_{13}
 +(\mu'_{j'})^2}{3(\mu'_{j'})^2}
$$
再按(14)规范。返回原 $b=17$ 仍严格是
$D'_{j',17}(z)=\theta^{-4}D'_{j',1}(\theta z)$。

Yang 的同一全权公式在这个实际向量上给
$$
C'_{j'}=
 \frac{\pi\sqrt{102\sqrt3}}
 {17\sqrt3(3+\sqrt3)n'_{j'}},
\qquad
L(\eta_j^{-1}\psi_0^{2m+1},m+1)
 =C'_{j'}\frac{(4\pi)^m}{m!}(b'_{j',m})^2 ,
\quad m\equiv4\bmod6.
\tag{15}
$$
二处两个非平凡三次字符的 Gauss 和同为2；
十七处 $\vartheta_{\pm l}$ 的 Gauss 和同为 $-17$；
三处整个字符、uniformizer 和无限处均未改变。
因此同一个 Hermitian 类和 Haar 体积确实适用(15)。
特别 $m=4$ 与(14)给新固定 $c'_{j'}\ne0$，其中
$$
\frac{(2\pi/\sqrt3)^m
 L(\eta_j^{-1}\psi_0^{2m+1},m+1)}
 {m!\varpi_0^{2m+1}}
 =c'_{j'}34^{-m}([z^m]D'_{j',1})^2.
\tag{16}
$$
现在在原同一 $54$ 条 degree34 图、原完整 $L/H$ corestriction
和原 full9 lift 上把 $e_{\eta_j}$ 换成
$e_{\eta_j^{-1}}$。取此前未平方 theta 来源中相同的六步
绝对相位，定义其实际正权 toric 值 $\mathcal T'_{j',5}$，
并置
$$
\boxed{B'_{j'}=\frac{17\delta}{9}\mathcal T'_{j',5}.}
\tag{17}
$$
这里先定义实际值，再使用平方恒等式；不从平方值任意选根。
原二处三商矩阵在两条非平凡 $C_3$ 字符上的本征标量相同，
因为其对角元相同、非对角元相同且非平凡字符和为零。
十七处同理；三处向量完全相同。因此 R1049 的已付局部常数
保留，给
$$
(B'_{j'})^2
=-972\omega\,34^4\epsilon_0^{-3}
 c'_{j'}\gamma'_{j'},\qquad
\gamma'_{j'}=\frac{L(\psi_{27}\eta_j^{-1},1)}{\Omega}.
\tag{18}
$$
§6、(15)说明(17)非零。原 Artin 等变性逐项作用于全图与
系数后给 $B'_{j'}\in(HE)^{\eta_j^{-1}}$。
这条真实线与旧 $B_j\in(HE)^{\eta_j}$ 不混同。

## 8. 整个六维来源的条件未平方几何因子

本节继承 full54 的连续几何比较，故现须额外支付页首审计中的正权交织、换点定义域和负权 primitive 接合。六条真实来源、全值和正权代数身份保留，几何因子及其单位性暂不可无条件调用。

将(14)、(17)同旧 $D_{j,1},B_j$ 合记为 $D_i,B_i$，
$i\in\mathcal I$。令 $\mathcal I_{i,p}$ 为对应原 fixed54 循环的
R1049 模型基读数；最高表示为
$\eta_i^{-1}\chi_{27}^3\varepsilon^{-1}$。
新三条的 $\eta_i=\eta_j^{-1}$，故最高线确为
$\eta_j\chi_{27}^3\varepsilon^{-1}$，不是旧三条的重新命名。
在各自真实 Artin 基 $a_i$ 下记
$h_{i,p}=a_i^{-1}\mathcal I_{i,p}$。

固定 inert $p$，删除此前共同有限坏集和新增固定常数的有限
支撑。对全部六条使用同一个
$$
d=p+1,\quad c_\sigma=[z^d]\log(\sigma_0/z),\quad C=34c_\sigma,
$$
$$
J_i(v)=\sum_{r\ge0}C^{-r}
 [z^{dr-2}](D_i e^{-Cz^d})(v)_r,\qquad
K_i(v)=\frac{J_i(v)}{pv}.
\tag{19}
$$
原 Hurwitz/Newton 证明是整个 bounded $V_4$ 的证明，
故 $K_i\in\mathcal O\langle v\rangle$ 对六条全部成立。

必须说明为什么得到跨两个 dyadic 块的同一因子，而不只是
分别得到两组三线比例。已发布的
[完整 geometric cross 证明](2026-11-27-original-inert-full54-geometric-newton-cross-identity.md)
§3.1比较的是旧 $m=4$ split character $\nu_{27}^{-4}$ 与
固定 weight3 的 $\nu_{27}^2$；其比是 $\nu_{27}^6$。
在二处它在整个 compact 上为1，故对实际
$v_+$ 和 $v_-$ 都是点值恒等，不是两次另选交织标量。
三处完整单位函数也相同，$\delta$ lift 给同一个 $-1$；
$Ph$ 的 determinant 为二处单位，不引入另一 dyadic 号。
十七处原全部 balls 与 Fourier 变换保留。
两条 factor characters 的比较分别是恒等和
$\nu_{27}^{12}$，后者在所有坏处 compact 及 $\delta$ 上为1。
good split 的球函数、compact Haar 及 principal norm-one
消估值步骤与字符标签无关。因此这个接合在整个六维有限
空间上是同一实际算子，不依赖 $\pm$ 或 $j$。

现在对六个真实非零 positive vacua
$\beta_i=\psi_{27}\eta_i$ 同时取该证明§3的固定共同 cover：
取六个实际 Schwartz 函数及其 Fourier 变换的共同支撑、
周期和 Heisenberg semicharacter 的公倍数 $M$，令
$N=34M^2$。
采用同一个 $h_\infty$ 以及
$\Theta_{\beta_i}(Mz/(\Omega_0h_\infty))/
\Theta_{\beta_i}(0)$ 定义整模型。
于是六个 beta Newton 因子均满足
$$
J_{\beta_i}(v)\in1+p\mathcal O\langle v\rangle,
\qquad J_{\beta_i}(0)=1.
\tag{20}
$$
这里所有 covers 的扩大只改变同一个正权标量，不能逐条
偷偷重定变量。

实际经典源因而在每个 $n\equiv4\bmod6$ 有
$$
\mathcal T_i(n)
 =c_n B_i [z^n]D_i\,[z^{n+2}]E_{\beta_i},
\tag{21}
$$
其中 $c_n\ne0$ 对整个 $\mathcal I$ 共同。
其共同性来自上述全有限算子与同一个无限处 Hermite 积分；
(17)保留了实际真空相位，并未用(18)倒推共同号。

固定同一局部参数 $n(u)=(p^2-1)u-2$、$v(u)=(p-1)u$。
Kriz/BDP 的待补接合连续族、原 complete fixed-base
$p^2$ level sum 和 full54/Artin 方向对六条同时适用：
CRT 代表在原306级上为1，所以 $\eta_i$ 与其逆在这些代表上
同为1；$H$、$L$、$[L:H]=432$ 均不改变。
每个正整数 $u$ 的公共 Hecke 因子仍是
$p(p+1)(1-p^{-2})$，端点仍为 $(p^2-1)\mathcal I_{i,p}$。
令相应连续函数为 $\mathscr L_i(u)$，以同一常数
$q_{\rm fp}\ne0$ 规范，使
$\mathscr L_i(0)=q_{\rm fp}\mathcal I_{i,p}$。

正权先消所有共同因子，再取连续极限，完整得到
$$
\boxed{
\mathscr L_i(u)B_lK_l(v)J_{\beta_l}(v)
 =\mathscr L_l(u)B_iK_i(v)J_{\beta_i}(v)
\quad(i,l\in\mathcal I).
}
\tag{22}
$$
特别
$$
\boxed{\mathcal I_{i,p}B_lK_l(0)
 =\mathcal I_{l,p}B_iK_i(0)\quad(i,l\in\mathcal I).}
\tag{23}
$$
这里包括每个旧块与新块之间的交叉等式。

若至少一条 $K_*(0)$ 是单位，则所有 $\mathcal I_{i,p}$ 有
同一个标量 $F_p$：
$$
\mathcal I_{i,p}=F_pB_iK_i(0),\qquad
h_{i,p}=F_p(B_i/a_i)K_i(0).
\tag{24}
$$
在 R1049 已付 cofinite 新增 NS/整格范围内，
同一原 Čech、full54 及不同 $\eta_i$ 逐项投影给
$F_p\in\mathcal O^\times$、$\bar F_p=-432$。
这只把先前的共同因子扩到实际完整六维 source；
没有新增“无穷多个 $p$ 存在单位”的断言。

### 8.1 真正零质量组合的一阶返回

这个应用只需连续性，不需先假设 $\mathscr L_i$ 或公共因子
有单独的权导数。在 $0$ 的某个邻域，由(22)与
$K_*(0)J_{\beta_*}(0)\ne0$ 可写
$$
\mathscr L_i(u)/q_{\rm fp}
 =G_p(u)B_iK_i(v(u))J_{\beta_i}(v(u)),
\quad G_p\text{ 连续},\quad G_p(0)=F_p .
\tag{25}
$$
给定固定系数 $b_i$，若且仅在已实际支付
$$
\sum_i b_iB_iK_i(0)=0
\tag{26}
$$
的范围内，右侧内和是一个在0为零的解析函数。
差商直接给完整、存在的一阶导数
$$
\boxed{
\left.\frac{d}{du}
 \sum_i b_i\,\mathscr L_i(u)/q_{\rm fp}\right|_{u=0}
 =(p-1)F_p
 \sum_i b_iB_i
 \bigl(K_i'(0)+K_i(0)J_{\beta_i}'(0)\bigr).
}
\tag{27}
$$
$J_{\beta_i}'(0)\in p\mathcal O$，但原 bounded
$K_i'(0)$ 也在 $p\mathcal O$；若后续除 $p$，两项同阶，
不得删去 beta 修正。若用下降基，则同时把左侧除 $a_i$
并在右侧相应改为 $B_i/a_i$；不能只改一边。
没有(26)时，不从本证明宣称左侧各自可微。


还可在这里准确支付式(27)除 $p$ 后的首层，而不删 beta 修正。
沿 [R614](../results/R614-original-addition-integrality-window-and-complete-newton-tail.md)
(9)，置 $p=6s-1>211$、$L=s(p-1)$、
$w=z^6$、$W=z^2x$、$Y=-z^3y$、
$U=(\sigma_0/z)e^{-c_\sigma z^d}$。$U,W,Y$ 在 $w$ 次数 $<L$ 全整。
写 $D_i=\sigma^{34}\sum_{k=0}^5q_{i,k}x^{3k}$，则
$
D_ie^{-Cz^d}
=z^4U^{34}\sum_{k=0}^5q_{i,k}w^{5-k}W^{3k}.
$
所有幂非负，固定分母已在共同坏集外；故
$
a_{i,h}:=C^{-h}[z^{dh-2}](D_ie^{-Cz^d})\in p^h\mathcal O
\quad(1\le h\le p-1).
$
对 beta 的实际固定整模型，$E_{\beta_i}=\sigma^NP_i(x,y)$，
每项 $x^ay^\epsilon$ 满足 $2a+3\epsilon\le N$。
其 type0 使 $N-2a-3\epsilon$ 为非负六倍数，完成 Gaussian 后每项准确是
$
c_{a,\epsilon}(-1)^\epsilon
w^{(N-2a-3\epsilon)/6}U^NW^aY^\epsilon .
$
因此 $C_\beta=Nc_\sigma$、$a_{\beta_i,h}\in p^h\mathcal O$
至少对 $1\le h\le p-2$ 成立；这里读取 $hs<L$，
不把 $h=p-1$ 的边界算成整。

令 $d_{i,r}=[z^r]D_i$、$e_{i,r}=[z^r]E_{\beta_i}$，
并置
$
\begin{aligned}
\gamma&=pC,&\gamma_\beta&=pC_\beta,\\
g_{i,1}&=d_{i,p-1},&
g_{i,2}&=d_{i,2p}-Cd_{i,p-1},&
g_{\beta_i,1}&=e_{i,p+1}-C_\beta .
\end{aligned}
\tag{27a}
$
三个 $g$ 都是完整 Gaussian 余项的整系数；尤其不将 $d_{i,2p}$
和 $Cd_{i,p-1}$ 分别当成整。
由 $(v)_2/v=v-1$、$(v)_3/v=(v-1)(v-2)$，
$K_i'(0)/p\equiv(a_{i,2}-3a_{i,3})/p^2$；
整窗进一步给 $a_{i,3}\in p^3\mathcal O$。
所有 $h\ge4$ 用原完整尾界落在所需 $p^2$。
beta 的 $h\ge3$ 全尾在 $p^2$，而 $a_{\beta_i,2}\in p^2\mathcal O$，
所以 $J_{\beta_i}'(0)\equiv a_{\beta_i,1}\pmod{p^2}$。
最终式(27)内每条完整斜率满足
$
\boxed{
\frac{K_i'(0)+K_i(0)J_{\beta_i}'(0)}p
\equiv
\frac{g_{i,2}}{\gamma^2}
+\frac{g_{i,1}g_{\beta_i,1}}{\gamma\gamma_\beta}
\pmod p .
}
\tag{27b}
$
所有除法先在整环中按真实整除作出。第二项与第一项同阶，
仍是原 beta 槽的实际费用；本式没有把它归零。

## 9. 与原 canonical 热 jet 的精确接点

原热 jet、完整连接和纯 Newton 首层仍保；凡将其读成§8的实际几何权斜率，均须同一审计门全部支付，不以热公式补造几何连续性。

R855 的真实算子是
$$
H_m=\frac{D^2}{2m}+\frac{m g_2z^2}{24},\qquad
(L_2-H_m)(\sigma^mR)=\sigma^m\mathcal H_mR .
\tag{28}
$$
取原 $m=34$ canonical $S$，以及原齐次提升的
$\dot S=L_2\widetilde S|_{\rm CM}$。
已付完整多项式是
$$
Q_S=\frac{\sigma^{34}}7
 (-1024-117760X-46848X^2-26992X^3-1900X^4+210X^5),
$$
$$
D^2S=68\dot S+Q_S,\qquad
Q_S=-68\sigma^{34}\mathcal H_{34}\widetilde R_S|_{\rm CM}.
\tag{29}
$$
所以真正 heat-flat theta family 通过该 $S$ 的一级 jet 是
$$
\boxed{
\dot S_{\rm flat}=\dot S+Q_S/68=D^2S/68 .
}
\tag{30}
$$
这是支付原齐次 lift 与固定有限 Schwartz 的 heat-flat lift
之间的准确差，不是宣称二者延拓相同。
$Q_S$ 在(14)和旧三条构成的整六维空间内有唯一固定谱分解，
故其六个 bounded Newton 因子可用(22)--(27)同一个公共因子返回。

但是 $\dot S_{\rm flat}$ 本身不是 bounded $V_4$ 来源。
它的第 $m$ 个正系数准确为
$$
[z^m]\dot S_{\rm flat}
 =\frac{(m+2)(m+1)}{68}[z^{m+2}]S .
\tag{31}
$$
相应完整 Newton 身份保持原 canonical：
$$
\boxed{
K_{\rm flat}(v)
 =\frac{d(dv-1)}{68p}J_S(v),\qquad
K_{\rm flat}(0)=0,\qquad
K_{\rm flat}'(0)=-\frac d{68p}J_S'(0).
}
\tag{32}
$$
第一零值是原质量零恒等式，不是某个新几何非消失的矛盾。
原坏条件只作用在(32)的斜率；不能据此给六条
$K_i(0)$ 分别赋零。

尤其真实半周期投影沿族也须移动。
若 $P_4$ 是原 full canonical lift 的热水平延拓，
$P_4S_{\rm flat}=0$ 给
$$
0=\dot P_4 S+P_4D^2S/68.
\tag{33}
$$
式(33)的 $P_4$ 是作用于全 Jacobi jet 的实际平移，不是把
R798 的 bounded 六维常矩阵直接作用到非有界 $D^2S$。
因此(24)支付了整个 bounded 补项 $Q_S$ 的同一几何因子，
而(29)--(33)仍保留原 canonical 所需的指定扩展连接。
后继必须消费这个真实 jet 或(27)的已付零质量组合；
不能用两个 dyadic 块各自的非零值替代它。

原投影移动本身也已显式支付：见[canonical二阶笔记§10](2026-11-27-original-canonical-second-derivative-newton-and-full-connection.md)。其原有限连接给 $L_2\mathsf P+[B_{34},\mathsf P]=0$，所以 $(L_2\mathsf P)R_S=-P_4(Q_S/\sigma^{34})/68$；这个完整费用与 heat-flat 的有理系数 jet $Q_S/(68\sigma^{34})$ 正好相消。
