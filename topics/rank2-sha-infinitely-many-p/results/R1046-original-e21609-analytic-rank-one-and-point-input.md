# R1046 — 原 E21609 的完整解析一阶证书与点输入

日期：2026-11-27 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

**已证明：§5.1 的唯一实际公开回执严格给同一 $E_D$ 的 $L'(1)>0$，故解析秩恰一。§§6–9 用原有理 CM Rubin 定理和固定点接回同一个原 mixed 一阶矩，支付其非零及完整深度首项。原中央坏条件仍不能直接给角函数的新强迫零；主目标未完成。**

本篇消费 R1040 §15 的真实原一阶来源。它的有限向量和原 CRT
奇字负号按该节保留；本篇不再执行旧 R1037 全谱、R1038 的126
返回或 R1045 的三条九阶计算。

## 1. 固定原曲线、完整角色和根数

置
$$
K=\mathbf Q(\delta),\quad \delta=1+2\omega,\quad \omega^2+\omega+1=0,
\qquad E_D:\ y^2=x^3+21609=x^3+147^2.
\tag{1}
$$
记 $\psi_0$ 为 R302 的原 $y^2=x^3+1$ 角色，
$\psi_{63}$ 为 R1038 已完全识别的 $E_{3969}$ 角色。
因为 $147^2\cdot63^2=21^6$，两个三次扭曲准确互逆，故
$$
\boxed{\psi_D=\psi_0^2/\psi_{63}.}
\tag{2}
$$
(2) 是固定 CM 角色等号，保持原算术 Frobenius、同一代数微分
和同一无穷 type $(1,0)$。

沿 R1038 的
$g=1-3\delta$、
$u=q\omega^jg^k\bmod9$，
$q\in\{1,2,4,5,7,8\}$、$0\le j,k\le2$，
令 $\varepsilon(q)=q\bmod3\in\{\pm1\}$。
把原 R302/R1038 的完整局部表代入 (2)，得到
$$
\boxed{\begin{array}{c|c|c}
\text{地点}&\text{单位角色 }\chi_D&\text{指定 uniformizer 值}\\ \hline
2&\operatorname{Teich}_{\mu_3}&\chi_D(2)=-1\\
\delta&\varepsilon(q)\omega^{j+k}&\chi_D(\delta)=i\\
\mathfrak q=(\gamma_7)&u^4&\chi_D(\gamma_7)=\gamma_7/\sqrt7\\
\bar{\mathfrak q}&u^4&
 \chi_D(\bar\gamma_7)=\bar\gamma_7/\sqrt7
\end{array}}
\tag{3}
$$
这里 $\gamma_7=3+\omega$；两个七剩余嵌入分别为
$\omega\mapsto4$、$\omega\mapsto2$。
七处最后一列的 $\omega$ 因子确实已经相消：
原 $\psi_0$ 给
$\omega\gamma_7/\sqrt7,\ \omega^2\bar\gamma_7/\sqrt7$，
平方后除 R1038 的
$\omega^2\gamma_7/\sqrt7,\ \omega\bar\gamma_7/\sqrt7$，
正好是 (3)。这不是只用紧单位角色作好位猜测。

三进角色在 $g=1+\delta^3$ 上为 $\omega$，
故导子恰 $\delta^4$；二、两七处导子恰一次。
因而 Hecke 导子、对应有理 level 及坏 Euler 因子准确为
$$
\mathfrak f_D=(2\delta^4\cdot7),\qquad
N_D=|D_K|\operatorname N\mathfrak f_D
 =2^2\,3^5\,7^2=47628,
\qquad L_2=L_3=L_7=1.
\tag{4}
$$

保持 R1038 的负有限加性角色、Tate 参数 $c_3=9\delta$。
令 $\zeta=\zeta_9$；其完整54项 Gauss 和是
$$
\begin{split}
G_{D,3}
 &=\sum_{q,j,k}\varepsilon(q)\,
          \omega^{-j-k}\zeta^{-B(q,j,k)}=9,\\
B(q,0,k)&=-3qk,\quad
B(q,1,k)=q(5-3k),\quad
B(q,2,k)=q(4-3k)\pmod9 .
\end{split}
\tag{5}
$$
证明完全有限：k 和只留 $q=1,4,7$，其符号均为正。
j=0 给 $+9$；j=1、2 分别是三个相隔三次幂的 $\zeta$ 项之和，
故为零。于是 $\epsilon_3=+i$；
二处为原 $+1$、两个七处 epsilon 乘积为一、无穷处为 i，
全根数准确为 $-1$。公开消费者另外在
$\mathbf Z[\zeta_9]$ 的六维整数基中核全部 (5)。

## 2. 所有 Euler 系数的原始重建

对与42互素的 $a=A+B\omega$，定义
$t_2(a)$ 为 mod2 的 Teich 指数。
其三处分解仍用上面的全部54个单位；
两个七处指数 $e_7(a),e_{\bar7}(a)$ 准确由
$$
(A+4B)^4=4^{e_7(a)}\pmod7,\qquad
(A+2B)^4=2^{e_{\bar7}(a)}\pmod7
\tag{6}
$$
定义，指数均在 $\mathbf Z/3$ 中。
于是 (3) 的主 idèle 公式为
$$
\boxed{
\psi_D((a))
 =\varepsilon(q)\,a\,
 \omega^{-t_2(a)-j-k-e_7(a)-e_{\bar7}(a)}.}
\tag{7}
$$
所有单位乘子已在 (7) 中支付。特别六个 associates 给同一个
理想值，共轭生成元给共轭值，绝对平方为 $\operatorname N(a)$。

公开消费者从模9乘法构造整个54单位表，核其全部
$54^2=2916$ 个乘法关系；另外核完整二处、两个七处单位乘法，
六个全局单位在 (7) 中的理想值皆为一。
不是只在少量好位测试一个候选公式。

对好有理素数 $\ell\equiv1\bmod3$，从
$A^2-AB+B^2=\ell$ 枚举一个实际生成元 a，
取 $v=\psi_D((a))=v_0+v_1\omega$，则
$$
a_\ell=2v_0-v_1\in\mathbf Z.
$$
对好 $\ell\equiv2\bmod3$，$a_\ell=0$。
所有素数幂及互素合成数都用完整关系
$$
\begin{aligned}
a_1&=1,\\
a_{\ell^{r+1}}&=a_\ell a_{\ell^r}-\ell a_{\ell^{r-1}}
 &&(\ell\nmid42),\\
a_{\ell^r}&=0 &&(\ell\mid42,\ r\ge1),\\
a_{mn}&=a_ma_n &&((m,n)=1).
\end{aligned}
\tag{8}
$$
每个 split 素数都同时核 (7) 的六 associate、共轭、
$v\bar v=\ell$，以及全等号
$\psi_D((a))\psi_{63}((a))=\psi_0((a))^2$。

三个可直接纸笔检查的固定规范锚为
$$
\boxed{
\begin{array}{c|c|c}
a&\psi_D((a))&a_{\operatorname N a}\\ \hline
4+\omega&1-3\omega&5\\
5+2\omega&-3-5\omega&-1\\
6+\omega&-5-6\omega&-4
\end{array}}
\tag{9}
$$
例如第一行的三处分解为 $q=2,j=2,k=2$，两个七单位值都是一，
二、三乘积为 $-\omega^2$。其逆乘 $4+\omega$ 正是 $1-3\omega$。
第二行取 $q=1,j=2,k=1$；
第三行取 $q=7,j=1,k=1$，逐式得到 (9)。
这些只是完整构造的规范检查，不代替其它素数和合成数系数。

## 3. 同一个 L 函数的精确导数表示

令
$$
c=\frac{2\pi}{\sqrt{N_D}}=\frac{\pi}{63\sqrt3},\qquad
\Lambda(s)=c^{-s}\Gamma(s)L(E_D,s).
\tag{10}
$$
原根数 $-1$ 给 $\Lambda(s)=-\Lambda(2-s)$。
将 Mellin 积分在1处分开并使用同一个新形式的函数方程，
$$
\Lambda(s)=
 \sum_{n\ge1}a_n\int_1^\infty e^{-cnt}
                   \{t^{s-1}-t^{1-s}\}\,dt .
$$
在 $s=1$ 微分，再将 $\log t$ 分部积分，得到
$$
\boxed{
L'(E_D,1)=2\sum_{n\ge1}\frac{a_n}{n}E_1(cn),\qquad
E_1(x)=\int_x^\infty\frac{e^{-u}}u\,du .}
\tag{11}
$$
因为 $L(E_D,1)=0$，微分 $\Gamma$ 和 $c^{-s}$ 时没有额外中央项。
本篇计算的是原 primitive $L'$，不是去掉好位因子的 imprimitive 值。

## 4. 固定有理区间与全部无穷尾

唯一参数固定为
$$
N=1024,\quad J=144,\quad D=10^{18},\quad
M_\gamma=128,\quad
n_{\arctan}=32,\quad n_{\log}=24 .
\tag{12}
$$
不按结果临时改变截断。

### 4.1 圆周率、平方根、对数与 Euler 常数

圆周率使用
$\pi=16\arctan(1/5)-4\arctan(1/239)$；
每个 arctan 取32项交错和和下一项误差，外向取整到分母 D。

平方根只用整数平方根：
$$
r=\lfloor\sqrt{3D^2}\rfloor,\qquad
r^2<3D^2<(r+1)^2,\qquad
\sqrt3\in[r/D,(r+1)/D].
\tag{13}
$$
(13) 的两侧整数平方在消费者中准确核验，不调用浮点平方根。
由 $\pi_\pm$、$\sqrt3_\pm$ 取
$$
c_-=\frac{\pi_-}{63\sqrt3_+},\qquad
c_+=\frac{\pi_+}{63\sqrt3_-}.
$$
它们严格包含 c，且直接核
$1/35<c_-<c_+<1/34$、$1024c_+<31$。

对数先以2的整数幂缩到 $1\le x\le2$；
置 $t=(x-1)/(x+1)\in[0,1/3]$。准确的24项界是
$$
0\le
\log x-2\sum_{j=0}^{23}\frac{t^{2j+1}}{2j+1}
\le
\frac{2t^{49}}{49(1-t^2)} .
\tag{14}
$$
还原2的幂时，负指数交换上下界。
Euler 常数则用同一已证明的 Euler–Maclaurin 界：
$$
\begin{split}
B_M&=H_M-\log M-\frac1{2M}+\frac1{12M^2}
                         -\frac1{120M^4},\\
B_M&\le\gamma\le B_M+\frac1{252M^6},
\qquad M=128 .
\end{split}
\tag{15}
$$
$\log M$ 的误差按 (14) 保留。

### 4.2 每个 E1 项及有符号系数

对任意本次出现的 $0<x<31$，
$$
E_1(x)=-\gamma-\log x+
       \sum_{k=1}^{144}\frac{(-1)^{k+1}x^k}{k\,k!}+R(x),
\qquad
0\le R(x)\le\frac{x^{145}}{145\,145!}.
\tag{16}
$$
截断之后的项严格递减；即使前面若干项不递减也不影响这个
完整尾界。所有运算都在有理数中完成。
再用 $E_1$ 单调递减，以 $c_+n$ 的下界和 $c_-n$ 的上界夹
$E_1(cn)$；乘负 $a_n$ 时交换上下端点。
最后外向取整到 $10^{-12}$，所打印区间本身就是证书。

### 4.3 n 大于1024的全尾

由原纯 CM 角色的每个理想系数绝对值 $\sqrt n$，
$$
|a_n|\le d(n)\sqrt n\le2n .
$$
取 $z=(1+c_-)^{-1}$，由
$E_1(x)\le e^{-x}/x$、$e^{-c_-}<z$ 得
$$
\boxed{
\left|2\sum_{n>1024}\frac{a_n}{n}E_1(cn)\right|
\le
\frac{4z^{1025}}{1025\,c_-(1-z)}
<10^{-10}.}
\tag{17}
$$
这个尾包含所有合成数和所有未显式枚举的素数。
最后的数值界也有短的自给估计：
$c_->1/35$，故右侧小于
$5(35/36)^{1025}$。
由二项式前五项，
$(36/35)^{36}>8/3$；
又 $1025>28\cdot36$ 且
$(3/8)^4=81/4096<1/50$，
所以它小于
$5/50^7<10^{-10}$。
消费者另外核其实际有理数版本。

## 5. 唯一新公开消费者和实际输出门

源码：
[check-original-e21609-complete-lprime.py](../scripts/check-original-e21609-complete-lprime.py)。

其固定四个原输入是：

| 原文件 | SHA256 |
| --- | --- |
| R302 原 degree2 全权平方 | bd3204188d1c795053d4e0b15ebdef082cd688a918d3dae4b87f17b8bd549507 |
| R391 原 wild3 全九维模型 | 5ee9acc1a7efb4374ed53a91bcca49d6fff0e4d951e20734ffbd4c027dc24cf9 |
| R1038 原 E3969 全 CM 角色 | e0b474e876efc74af006e151d45293aa9f7a31aaa5dbb7d91a7f3bf5b1f3a950 |
| 原 check-r732-two-cubic-rank-one-bounds.py | abc12f49db1818351534889f31bd9b7bac7876a78cbd043a060834d97c2a8289 |

唯一源码的 SHA256 为
$$
\texttt{b71e67d970ab7388759ea97e6a1ad9bbb2f0c74fbc5b30de7648bb6229f8a7a3}.
\tag{18}
$$
它只在原公开仓库 GitHub Actions 中运行，
锁定 python-flint==0.9.0。
输出一个紧凑 JSON，包含全部1024个新系数、所有所需素数的
$a_\ell$、全54单位/2916乘法和54项 Gauss 检验、六 associate、
(2) 的逐 split 素数回乘、四个输入 hash，以及最终完整有理区间。
成功时不依赖 stderr，也不把输出缓存成以后生产的输入。

实际运行信息、stdout/payload/log 的全文 hash 和准确区间
应由真实公开回执填入本节：
$$
[L'_-,L'_+]\ni L'(E_D,1).
\tag{19}
$$
只有该回执严格证明
$$
0\notin[L'_-,L'_+]
\tag{20}
$$
后，才得到同一个 $E_D$ 的解析秩恰一。
若 (20) 未通过，程序报告
$\mathrm{INCONCLUSIVE\_NONVANISHING}$，不会伪报一阶或改参数。
执行前的判定门保持；实际结果见紧接的§5.1。


### 5.1 唯一实际公开回执：原解析一阶已证

公开 [run46008071578](https://github.com/Rogerhu12/math-research-public/actions/runs/46008071578)，
job140536202708，原 source commit
`60a44f52494882b380b909f294835d409c7efc1c`。
步骤于2026-11-27 13:33:06–13:33:15 UTC成功完成，
数学部分耗时1.3750599569999977秒，固定参数完全沿(12)。
全部四个输入 pin、54个单位及2916乘法、完整Gauss和、
81个split素数的六associate/共轭/绝对范数/互逆twist、
1024个完整Euler系数及全部无穷尾均通过。

返回的精确有理区间为
$$
\boxed{
\frac{3128612740737}{500000000000}
 \ \le L'(E_D,1)\le\
\frac{6257225481477}{1000000000000}.
}
\tag{20a}
$$
两端严格为正；结合原根数 $-1$，得到
$\operatorname{ord}_{s=1}L(E_D,s)=1$。
这个结论来自同一 primitive 全角色及全尾，不来自有限素数样本。

| 已消费对象 | 字节数 | SHA256 |
|---|---:|---|
| 执行源码 | 12618 | b71e67d970ab7388759ea97e6a1ad9bbb2f0c74fbc5b30de7648bb6229f8a7a3 |
| 完整stdout，含末尾换行 | 5912 | 734f2679e045fba3b6382876a30e6daa78bf88689d83f78eb1e329bb3ae4a497 |
| 紧凑JSON payload，不含换行 | 5911 | 075f26648972ae21baf21f5cfe83fda55fff043841e9f6fbd69b17a5ebd108e6 |
| 完整实际job日志，UTF8含BOM | 16179 | bfa6249b6e7899bd9c0a8ab678a10e5a487984470720626c7259ffd73baed802 |

完整1024系数数组的SHA256为
`44a7f11507e17aa0f02714f40578f34504ff64908adbfe537f6e03ee1adb298d`；
全有限角色序列化的SHA256为
`394d3d61598915edd280717f7e8eb09230b9ae818e73680e13773e2528ee1f70`。
根从实际日志的JSON重建完整stdout，字节数及SHA与工作流回执一致；
只作文本/JSON核验，没有在本地重新执行数学。
可重算数组、输出JSON和完整日志只在Actions中，未写入仓库。
本项已完整消费，不再运行。

### 直接依赖

完整角色方向使用
[R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)、
[R1038 §§8–9](R1038-e3969-two-independent-points-and-complete-cm-character.md)；
原全 wild3 核及绝对 splitting 使用
[R391](R391-e24-original-wild-three-schwartz-and-heisenberg-transport.md)。
真实 $U_K$ 源及其 CRT 奇字负号、正权角色、原一阶矩见 R1040 §15。
严格 E1 方法使用原 R735/R1045 已付的积分推导；
本篇新增的是完整 $E_D$ 角色、level47628 的实际1024系数、
$\sqrt3$ 区间及其相应全尾，未重做三条旧九阶来源的计算。


## 6. 野三处仍适用的原 Rubin 定理及固定非挠点

本节从第5节同一个固定曲线的实际严格区间出发。
使用的是 Bertolini–Darmon–Prasanna 2012 已发表全文
[Theorem1，印刷第262页，式(1-1)](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf)
所明确陈述的 Rubin1992 定理：有理 CM 椭圆曲线在解析秩准确为一时，
其共轭 Katz 值是一个无限阶有理点 logarithm 的平方，
模其 CM 域的非零代数因子。
此处不调用该文 Theorem2/3.32 的一般高维版本；
后者要求判别式恰除导子一次，不能处理本篇的 $\delta^4$。

原 Rubin 文献为
*p-adic L-functions and rational points on elliptic curves with complex multiplication*,
Invent. Math.107 (1992),323–350，
[DOI](https://doi.org/10.1007/BF01231893)。
本篇以上述作者提供的已发表 BDP 全文所陈述的原定理为直接核对入口，
没有声称已从公开入口读到 Rubin 的订阅全文。

### 6.1 定理的全部实际输入

| 定理所需输入 | 本篇的实际核定 |
|---|---|
| $A/\mathbf Q$ 的几何 CM 环为 $\mathcal O_K$ | $A=E_D:y^2=x^3+21609$，$K=\mathbf Q(\sqrt{-3})$，$j=0$，全部 CM 在 $K$ 定义 |
| 曲线自身的 type$(1,0)$ 角色 | 第1节及 R1040(126)–(127) 的 $\psi_D$，不是一个仅在好位同谱的角色 |
| 好分裂普通素数 | 原射线 $p>211$、$p\equiv1\bmod3$，且 $p\nmid2\cdot3\cdot7$ |
| 解析秩准确为一 | 原 root$=-1$ 及第5节的严格 $L'(E_D,1)>0$ |
| 同一个 Katz 函数 | R1040(130) 的 primitive $\mathcal K_{(126)}(\widehat{\bar\psi}_D)$；二、三、双七处全部保原分歧，不另删 Euler 因子 |
| 普通微分与周期 | 下述 $\omega_D=dx/(2y)$、$\omega_0=dx/(2y)$ 及 (23) 的实际代数同构规范 |

Rubin 定理在此直接给一个无限阶
$\widetilde P_{D,p}\in E_D(\mathbf Q)$；
不用把一个高维 CM 簇的任意坐标认作椭圆 logarithm。

本曲线有明确的固定点
$$
\boxed{P_D=(-12,141),\qquad (-12)^3+147^2=141^2.}
\tag{21}
$$
它非挠：原整短 Weierstrass 判别式是
$-432\cdot147^4$，而 $47^2\mid141^2$、$47\nmid432\cdot147$。
Lutz–Nagell 的整点判别因此排除挠点。
这一步只给非挠，并未替代第5节的解析秩一证明。

解析秩一的 Gross–Zagier–Kolyvagin 结论给
$\dim_{\mathbf Q}E_D(\mathbf Q)\otimes\mathbf Q=1$。
故 $\widetilde P_{D,p}$ 与 (21) 在该空间内相差
$\mathbf Q^\times$，可将其平方准确吸收到 Rubin 定理的
$K^\times$ 因子中；挠点对 logarithm 为零。

### 6.2 实际三次点域、微分和原普通周期

取固定代数根 $\vartheta_D^3=147$，以及原
$\theta_{17}^6=17$。真正同构为
$$
\boxed{
\phi_D:E_D\longrightarrow E_0,\qquad
(x,y)\longmapsto(x/\vartheta_D^2,y/147),\qquad
\phi_D^*\omega_0=\vartheta_D\omega_D.}
\tag{22}
$$
因而
$\log_{\omega_0}(\phi_DP)=\vartheta_D\log_{\omega_D}(P)$。
这是几何微分尺度，不能以一个未定 $p$-adic unit 代替。

同时选取真正匹配的复周期及普通周期：
$$
\boxed{
\varpi_D=\varpi_0/\vartheta_D,\qquad
\Omega_{p,D}=\Omega_{p,0}/\vartheta_D,\qquad
\Omega_{p,0}=\theta_{17}\Omega.}
\tag{23}
$$
Katz 插值在这一次共同代数变更下保持原函数，
沿 BDP Theorem3.1 的同一 period rule。
特别这里的 primitive conductor 一直是 $(126)$，
没有把 wild 三处删成 $(14\delta)$ 或 $(42\delta)$。

## 7. 同一个原负一值的完整一次 logarithm

令 $I_{D,p}$ 和非零代数数 $c_D$ 严格沿
[R1040](R1040-new-e3969-whole-companion-frame-and-sixth-degree-carry.md)
(123)、(129)–(130) 的归一。
其原 whole sigma 平方是
$$
\mathcal K_{(126)}(\widehat{\bar\psi}_D)
 =126c_D\theta_{17}^{11}\Omega\,I_{D,p}^{\,2}.
\tag{24}
$$
全部 positive-weight Gaussian、Hermite 范数、普通 Euler 极限
均已在此式中支付，不能重设 $c_D$ 为任意单位。

第6节的原曲线定理、(21)–(23) 则准确给
$$
\boxed{
\mathcal K_{(126)}(\widehat{\bar\psi}_D)
 =\epsilon_{D,p}\Omega_{p,D}^{-1}
                  \log_{\omega_D}(P_D)^2
 =\frac{\epsilon_{D,p}}{\vartheta_D\theta_{17}\Omega}
                  \log_{\omega_0}(\phi_DP_D)^2,\qquad
\epsilon_{D,p}\in K^\times.}
\tag{25}
$$
$\epsilon_{D,p}$ 可以随 $p$ 改变；
未声称其为单位或有统一估值界。

结合 (24)、(25)，得到同一测度变量和原 period 上的完整一次公式
$$
\boxed{
\Omega I_{D,p}=A_{D,p}\log_{\omega_0}(\phi_DP_D),\qquad
A_{D,p}^{\,2}
 =\frac{\epsilon_{D,p}}
 {126c_D\vartheta_D\theta_{17}^{12}}
 \in\overline{\mathbf Q}^{\times}.}
\tag{26}
$$
平方根取实际等式给出的那一支；其平方是非零代数数，
所以该支仍属于所固定嵌入下的 $\overline{\mathbf Q}^{\times}$。
原 $P_D$ 无限阶，对每个好普通 $p$，
先乘一个整数将其移入 formal logarithm 单射球，
即可知 $\log_{\omega_0}(\phi_DP_D)\ne0$。
于是
$$
I_{D,p}\ne0
$$
对原射线全部合格普通 $p$ 成立。
此断言不依赖有限组普通 $p$ 的数值检查。

### 7.1 与原三条九阶点来源的真实分离

置 $L=K(\vartheta_D)$。
两处 $\gamma_7,\bar\gamma_7$ 上
$v_{\gamma_7}(147)=v_{\bar\gamma_7}(147)=2$。
由于 $K$ 含 $\mu_3$、$7\ne3$，
$L/K$ 为在双七处均全分歧的循环三次扩张。

若 $\tau(\vartheta_D)=\omega\vartheta_D$，则直接用 (22) 有
$$
(\phi_DP_D)^\tau=[\omega]\phi_DP_D.
$$
这是固定代数系数后的点因子作用；
不把它延拓成 $\mathbf C_p$ 上的连续 Galois 作用。

R1045 的三个非零点 $P_j$，$j=1,7,13$，
位于其实际 $H/K$ 循环九次点域；
该域仅在2、17分歧，特别在双七处不分歧。
所以 $L\cap H=K$。
在 $LH$ 上，$\operatorname{Gal}(L/K)$ 的非平凡点因子投影
分离 $\phi_DP_D$ 和全部 $P_j$；
随后 R1045 的三个不同九阶投影分离 $P_j$。
这证明四个实际点张量在 $K$ 上直接和。

沿 R749 的固定系数 point-factor projector 和 logarithm 单射，
再保 R1045(46) 及本篇 (26) 的所有非零代数尺度，得到
$$
\boxed{
\{\Omega I_{D,p},\ \Omega I_{1,1},\
       \Omega I_{7,1},\ \Omega I_{13,1}\}
\quad\text{在 }\overline{\mathbf Q}\text{ 上线性独立}.}
\tag{27}
$$
这里是线性独立，不是代数独立。
本节只证明这些实际平凡有限字符读数的关系；
未将原曲线 Rubin 定理无证推广到任意新有限 $p$-字符。

## 8. 原六输入上的直接 mixed 负一值

保 R1040 的真实 $\mathscr P_3=\Pi_H\Pi_J\Pi_N$，
以及原 Y/K 两物理方向。
它们的全 moment identity 是
$$
Y_*(K\mathscr P_3\rho)
 =\frac{10\delta}{7}\Omega\,\nu_{D_{126,17}}.
$$
因此第7节的非零现在成为同一个完整六输入上的实际非零：
$$
\boxed{
\int_{Y\ {\rm unit}}\frac K Y\,\mathscr P_3\,d\rho
       =\frac{10\delta}{7}\Omega I_{D,p}\ne0.}
\tag{28}
$$
这里只有先对来源作 H/J/N 投影；
因这些行与 Y/K 正交，也可使用对应真实有限平均的转置。
不含一个未支付的 $Y$ 主型投影，
因为 $K/Y$ 所读的 Y 类型准确为5。

对 $t\in p\mathcal O$ 置
$$
\mathfrak j_p(t)=
 \int_{Y+tK\ {\rm unit}}(p-1)\log\langle Y+tK\rangle
                                  \,\mathscr P_3\,d\rho .
$$
此范围内 $Y+tK$ 为单位当且仅当 Y 为单位，
故原单位域严格相同。
一致收敛的对数级数给
$$
\boxed{\mathfrak j_p'(0)
 =(p-1)\frac{10\delta}{7}\Omega I_{D,p}\ne0.}
\tag{29}
$$

这里仍不能从原中央坏条件推导矛盾：
坏条件只支付
$\mathfrak j_p(0)=39\delta J'_{\Phi_{126},p}(0)=0$，
没有支付 $\mathfrak j_p(t)=0$ 的任何非零 $t$。
$Y+tK$ 也未被识别成新的 fixed rank-two canonical 族。
(28)–(29) 是真实可消费的 mixed 非零输入，不是新增的强迫零。

## 9. 同一深度参数上的准确首项及剩余接线

原六测度及 $\mathscr P_3$ 在既定 $\Omega$ 规范下为有界测度。
取其一个统一赋值下界 $b_p$，包括 $\rho$ 的 $-1/84$、
真实角平均、完整 frame 整逆和全部固定分母。
因为 $K/Y$ 在原 Y-unit 域上为整，
$$
M_m=\int_{Y\ {\rm unit}}(K/Y)^m\mathscr P_3\,d\rho
          \in p^{b_p}\mathcal O .
$$
所以整个原中央读者有准确展开
$$
\boxed{
\mathfrak j_p(t)=\mathfrak j_p(0)
 +(p-1)\sum_{m\ge1}\frac{(-1)^{m-1}}mM_m t^m,
 \qquad t\in p\mathcal O.}
\tag{30}
$$
设
$\ell_p=v_p(\mathfrak j_p'(0))<\infty$，则 $\ell_p\ge b_p$。
原 $\Omega$、$10\delta/7$ 及 $p-1$ 都保留在 (29) 的首项里。
对 $m\ge2$、$v_p(t)\ge1$ 且 $v_p(t)>\ell_p-b_p$，
有
$$
b_p+mv_p(t)-v_p(m)>v_p(t)+\ell_p,
$$
因为 $v_p(m)\le m-2$，且
$(m-1)v_p(t)-v_p(m)\ge v_p(t)$。
故若原 canonical 坏条件成立，
$$
\boxed{
v_p(\mathfrak j_p(t))
       =v_p(t)+\ell_p
\quad
\text{对所有 }0\ne t,\ 
v_p(t)\ge1,\ v_p(t)>\ell_p-b_p.}
\tag{31}
$$
特别对原 $\kappa=p\lambda^2$ 和任何固定代数单位 $\xi$，
当 $n\ge1$ 且 $n>\ell_p-b_p$ 时，
$\mathfrak j_p(\xi\kappa^n)\ne0$ 且其赋值准确为 $n+\ell_p$。
这保全部高项，不需要一个关于 $p$ 一致的 logarithm 估值界，
也允许 $b_p$、$\ell_p$ 为负。
若原 $\nu_\sigma$ 已选在整格，则本篇 $p>211$ 下
$84$、frame 整逆的 $756$ 及角平均的 $6^3$ 全为单位，
可以取 $b_p=0$；上式不依赖这一额外简化。

剩余问题因而是具体的：
必须从原 S/T、合法 whole carry 或另一个已认证完整来源，
得到同一个 $\mathfrak j_p(\xi\kappa^n)$ 的真实强迫关系，
并保所有单位补域。
不能仅因 (31) 随 $n$ 有明确首项，
便将其称为原中央坏条件已被排除。
