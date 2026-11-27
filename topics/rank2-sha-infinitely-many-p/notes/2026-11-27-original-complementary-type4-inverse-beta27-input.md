# 原另一 dyadic 三线的 inverse-beta27 固定中央值输入

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
