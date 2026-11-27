# R1046 — 原 E21609 的完整解析一阶证书与点输入

日期：2026-11-27 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

**状态：§§1–4 的原全角色、Euler 系数构造、函数方程及严格有理
E1 全尾已经证明。§5 给唯一新公开消费者及固定参数；执行前不填
$L'(1)$ 区间或解析秩结论。实际点/周期桥由后继 §6 接回同一个原
一阶矩，不能从单个中央值为零推其角导数为零。**

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
当前正文不预填实际结果。

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
