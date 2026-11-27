# R1045 — 原型五三条九阶角色的完整解析一阶判据与固定有理证书

日期：2026-11-27 UTC。

**状态：§8 的公开实际回执证明三个原角色均解析一阶；§§9–11 完成同一点域/全部周期桥，证明原三个负一值与实际五sigma奇部的负一值非零。原中央sum-unit读者继续保持。** 本篇只消费 [R761](R761-primitive-type-five-ninth-order-characters-and-point-fields.md) 的三条原 primitive type-five 角色。其 root number 均为 $-1$，但 R761 未证明它们的 $L'(1)$ 非零。原 [F0 两字的真实返回](../notes/2026-11-27-original-f0-two-delta-word-return.md) 恰出现这一整块，因此本次是更换未付清的真实输入，不重算 R735 的两条 cubic 曲线。

生产脚本：

[check-original-r761-three-primitive-nine-lprime.py](../scripts/check-original-r761-three-primitive-nine-lprime.py)。

它只允许运行于原公开仓库的 GitHub Actions。全文不使用数据库值、不使用浮点 $L$ 值、不从低素数拟合角色，不在源码中保存 Fourier 系数或预填输出。运行完成后，只有实际打印的三个有理区间都排除零，才登记三条解析一阶非零。

## 1. 原三个完整角色与准确对象

固定
$$
K=\mathbf Q(\omega),\qquad \omega^2+\omega+1=0,\qquad
\delta=1+2\omega,\qquad
\zeta=\exp(2\pi i/9).
\tag{1}
$$
另置 $\zeta_{18}=-\zeta^5=\exp(\pi i/9)$。
R761 的原十七处环面生成元为
$$
g_0=2+4\delta=6+8\omega\pmod {17},\qquad
g_0^{18}=1,\quad g_0^6=\omega.
\tag{2}
$$
标签及指数严格为
$$
j\in\{1,7,13\},\qquad l_j=j-9\in\{-8,-2,4\}.
\tag{3}
$$
对 $u\in\mathbf F_{289}^{\times}$，令
$$
u^{16l_j}=g_0^{e_j(u)},\qquad 0\le e_j(u)<18,
\qquad \vartheta_{l_j}(u)=\zeta_{18}^{e_j(u)}.
\tag{4}
$$
这固定复嵌入和全部字符值。R761 已支付
$$
\vartheta_{l_j}|_{\mathbf F_{17}^{\times}}=1,\quad
\vartheta_{l_j}(\delta)=1,\quad
\vartheta_{l_j}(\omega)=\omega,\quad
\operatorname{ord}\vartheta_{l_j}=9.
\tag{5}
$$

原有限 Hecke 角色满足
$$
\eta_{j,2}=\operatorname{Teich}_{\mu_3}^{-1},\qquad
\eta_{j,17}=\vartheta_{l_j},\qquad
\eta_j((a))=
\left(\operatorname{Teich}(a\bmod2)^{-1}
          \vartheta_{l_j}(a\bmod17)\right)^{-1}.
\tag{6}
$$
其余有限分歧和三个指定 uniformizer 值完整沿用 R761(6)–(11)。
[原 degree-two 锚 R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)(6) 给
$$
\psi_0((a))=
a\,\operatorname{Teich}(a\bmod2)^{-1}\epsilon_\delta(a),
\tag{7}
$$
其中 $\epsilon_\delta(a)\in\{\pm1\}$ 是 $a\bmod\delta$ 的值。
本篇计算的对象恰为
$$
\Psi_j=\psi_0\eta_j^{-1}.
\tag{8}
$$

令 $a=A+B\omega$ 素于 $34\delta$，
$a\bmod2=\omega^{t(a)}$，$t(a)\in\{0,1,2\}$，
$\epsilon_\delta(a)=1$ 或 $-1$ 分别对应
$A+B\equiv1$ 或 $2\bmod3$。由 (6)、(7)，得到脚本实际使用的全式
$$
\boxed{
\Psi_j((a))=
\epsilon_\delta(a)\,a\,
       \zeta^{-6t(a)}\zeta_{18}^{e_j(a\bmod17)} .
}
\tag{9}
$$
这里 $-6t$ 是原 $\operatorname{Teich}^{-2}$；不能删掉二处角色。

对于单位 $\omega$，式 (9) 的三个非实因子依次乘
$\omega,\omega^{-2},\omega$，乘积为一；对于 $-1$，
$a$ 和 $\epsilon_\delta$ 同时变号。因此 (9) 在全部六个生成元代表上相同。
$h_K=1$ 使它给出每个好理想的实际值。复共轭满足
$$
\Psi_j((\bar a))=\overline{\Psi_j((a))},\qquad
\Psi_j((a))\overline{\Psi_j((a))}=N(a).
\tag{10}
$$

R761 的原完整导子、根数和系数域是
$$
\mathfrak f_{\Psi_j}=(34\delta),\qquad
N_{\mathrm{classical}}=|D_K|N(\mathfrak f_{\Psi_j})=10404,
\qquad w(\Psi_j)=-1,
\tag{11}
$$
$$
E^+=\mathbf Q(\zeta+\zeta^{-1}),\qquad [E^+:\mathbf Q]=3.
\tag{12}
$$
这是同一个实三次系数域的 CM 权二轨道，不是三条 $E/\mathbf Q$。
下文的“解析一阶”只指相应 $L(\Psi_j,s)$ 在 $s=1$ 的消失阶。

## 2. 全有限字符和全部 Fourier 系数的重建

脚本使用真正的六维整环
$$
\mathbf Z[\zeta]=
\mathbf Z[T]/(T^6+T^3+1),
\quad\text{有序基 }(1,\zeta,\ldots,\zeta^5).
\tag{13}
$$
乘法逐项约化 $T^6=-T^3-1$，复共轭为 $\zeta\mapsto\zeta^8$。
没有代数数小数表示。

有限体写作
$$
\mathbf F_{289}=\mathbf F_{17}[w]/(w^2+w+1).
$$
脚本生成 (2) 的全部十八个元素，检查其准确阶、范数一和
$g_0^6=\omega$；随后在全部 $288$ 个非零元素上生成 (4)。
每个标签都核 (5)、全部九阶值及共轭逆。另选真正阶 $288$ 的生成元，
逐一检查其 $288$ 个幂和字符指数的加法关系，支付整个乘法字符，
不是只检查若干好素数。

写
$$
L(\Psi_j,s)=\sum_{n\ge1}a_j(n)n^{-s}.
\tag{14}
$$
系数的原局部规则如下。

* $a_j(1)=1$。
* 对 $\ell\in\{2,3,17\}$，导子中的实际角色分歧，局部 Euler 因子为一；
  因此 $a_j(\ell^r)=0$，$r\ge1$。
* 对好惰性素数 $\ell\equiv2\bmod3$，$a_j(\ell)=0$。
* 对好分裂素数 $\ell\equiv1\bmod3$，选 $a=A+B\omega$，
  $A^2-AB+B^2=\ell$，置
  $a_j(\ell)=\Psi_j((a))+\overline{\Psi_j((a))}$。

好素数的完整递推为
$$
a_j(\ell^{r+1})
=a_j(\ell)a_j(\ell^r)-\ell a_j(\ell^{r-1}).
\tag{15}
$$
互素部分相乘。分裂生成元由
$$
4\ell-3B^2=C^2,\qquad A=(B+C)/2
\tag{16}
$$
整式寻找；六个 associates、复共轭及范数恒等式 (10) 全部逐素数核回。
这只生成本次必要的 $1\le n\le512$，不计算目标普通素数 $p$。

三个完整共轭的对应为
$$
a_7(n)=\sigma_7(a_1(n)),\qquad
a_{13}(n)=\sigma_4(a_1(n)),\qquad
\sigma_u(\zeta)=\zeta^u.
\tag{17}
$$
$\sigma_7,\sigma_4$ 都固定 $K$；(4) 的指数为偶数，
故 $\zeta_{18}=-\zeta^5$ 的符号也与此式相容。
脚本独立构造三个标签，而后对全部 $0\le n\le512$ 核 (17) 和实性。
因此某一个共轭的输出不能替代另两个。

## 3. 原 completed functional equation 给出的 $E_1$ 身份

置
$$
c=\frac{2\pi}{\sqrt{10404}}=\frac{\pi}{51},\qquad
F_j(t)=\sum_{n\ge1}a_j(n)e^{-cnt}.
$$
权二、level10404、根数 $-1$ 的原完成函数满足
$$
\Lambda_j(s)=\left(\frac{51}{\pi}\right)^s
\Gamma(s)L(\Psi_j,s),\qquad
\Lambda_j(s)=-\Lambda_j(2-s).
\tag{18}
$$
把 Mellin 积分在 $t=1$ 分开，再用原 Fricke 变换，
$$
\Lambda_j(s)=
\int_1^\infty F_j(t)\bigl(t^{s-1}-t^{1-s}\bigr)\,dt.
$$
在 $s=1$ 求导；$L(\Psi_j,1)=0$ 使完成因子的导数不额外贡献。
分部积分
$$
\int_1^\infty e^{-cnt}\log t\,dt=\frac{E_1(cn)}{cn}
$$
于是给精确公式
$$
\boxed{
L'(\Psi_j,1)=
2\sum_{n\ge1}\frac{a_j(n)}n E_1(cn),\qquad
E_1(x)=\int_x^\infty\frac{e^{-u}}u\,du.
}
\tag{19}
$$
下文同时保原系数的三个实嵌入和整个无穷尾。

## 4. 唯一参数及全部严格区间

固定参数如下，没有根据输出调参的隐藏循环：
$$
N=512,\quad J=144,\quad
J_{\cos}=32,\quad D_{\mathrm{round}}=10^{18},
\quad M_\gamma=128.
\tag{20}
$$
Machin 每个 arctangent 使用 $32$ 项，log 使用 $24$ 项。
参数不接受命令行覆盖。

### 4.1 $\pi$、log 和 Euler 常数

Machin 式
$$
\pi=16\arctan(1/5)-4\arctan(1/239)
$$
分别用交错级数前 $32$ 项及下一项给双边有理界。
所有后继舍入均向外到 $D_{\mathrm{round}}^{-1}\mathbf Z$。

对 $1\le x\le2$，令 $t=(x-1)/(x+1)\in[0,1/3]$，则
$$
2\sum_{k=0}^{23}\frac{t^{2k+1}}{2k+1}
\le\log x\le
2\sum_{k=0}^{23}\frac{t^{2k+1}}{2k+1}
+\frac{2t^{49}}{49(1-t^2)}.
\tag{21}
$$
一般正有理数按 $x=2^e x_0$、$1\le x_0\le2$ 返回；
$e<0$ 时交换 $\log2$ 的端点，不能沿用同号端点。

Euler–Maclaurin 的交错余项给
$$
H_M-\log M-\frac1{2M}+\frac1{12M^2}-\frac1{120M^4}
\le\gamma
$$
$$
\le H_M-\log M-\frac1{2M}+\frac1{12M^2}
       -\frac1{120M^4}+\frac1{252M^6},
\qquad M=128.
\tag{22}
$$
因此 $\gamma$ 也没有浮点输入。

### 4.2 三次系数域的实际实嵌入

对于 (13) 中已核为实的元素 $a=\sum_{r=0}^5a_r\zeta^r$，
$$
a=\sum_{r=0}^5a_r\cos(2\pi r/9).
\tag{23}
$$
每个 cosine 在有理 $\pi$ 区间上以
$$
\sum_{k=0}^{31}\frac{(-1)^kx^{2k}}{(2k)!}
$$
和绝对余界 $x_{\mathrm{upper}}^{64}/64!$ 包围。
正系数使用同向端点，负系数交换端点。
(17) 的三个独立系数数组均在这个固定原复嵌入内求值；
没有以一个任意近似根替换三个标签。

### 4.3 $E_1$ 的全项和交错尾

对本次所有输入 $x$，有 $0<x<145$。准确展开是
$$
E_1(x)=-\gamma-\log x+
 \sum_{k=1}^{144}(-1)^{k+1}\frac{x^k}{k\,k!}
 +R_{144}(x).
\tag{24}
$$
第 $144$ 项以后绝对项严格递减，因为
$$
\frac{x^{k+1}/((k+1)(k+1)!)}{x^k/(k\,k!)}
=\frac{xk}{(k+1)^2}<1,\qquad k\ge144.
$$
第 $145$ 项为正，故
$$
0\le R_{144}(x)\le \frac{x^{145}}{145\cdot145!}.
\tag{25}
$$
前 $144$ 项即使早期不递减也全部精确有理相加，未使用不适用的交错界。
$E_1$ 在正实轴严格递减，所以若 $c_-\le c\le c_+$，实际每项取
$$
E_1(cn)\in
\left[\operatorname{lower}E_1(c_+n),
      \operatorname{upper}E_1(c_-n)\right].
\tag{26}
$$
两个有理区间相乘取四个端点积的最小、最大值，允许 $a_j(n)$ 的任意符号。

## 5. 所有三个嵌入共用的严格无穷尾

由 (10)，每个好素数的两个 Satake 根在每个复嵌入下模都为 $\sqrt\ell$。
(15) 给
$$
|a_j(n)|\le d(n)\sqrt n\le2n.
\tag{27}
$$
最后一个不等式只用正因子成对，$d(n)\le2\sqrt n$。
坏素数系数为零，不增加上界。

对 $x>0$，
$$
0<E_1(x)\le \frac{e^{-x}}x,\qquad
e^{-c}\le(1+c_-)^{-1}=:z<1.
$$
因此三条无穷尾都由同一个有理数控制：
$$
\boxed{
\left|2\sum_{n>N}\frac{a_j(n)}n E_1(cn)\right|
\le
\frac{4z^{N+1}}{c_-(N+1)(1-z)}.
}
\tag{28}
$$
脚本以精确有理运算断言 (28) 小于 $10^{-10}$，
而实际双边界加入的是 (28) 的全有理值，不以 $10^{-10}$ 猜代。

这补齐了有限截断到整个 $L'$ 的证明。任何输出非零必须同时通过
原角色检查、全部递推、三个共轭和 (28)，不能仅凭部分和的符号。

## 6. 生产回执与唯一执行范围

生产脚本固定 SHA256：
$$
\texttt{8abde6978d29dbe16bbb582ff7304ee1ae95a4ca34f3b6a81d789c2b6077c6fe}.
\tag{29}
$$
文件为 $14113$ 字节，Python 依赖为
$\texttt{python-flint==0.9.0}$。
源码还在数学开始前逐字核三个原输入：

| 输入 | 字节数 | SHA256 |
|---|---:|---|
| R302 原 degree-two 锚 | 14759 | bd3204188d1c795053d4e0b15ebdef082cd688a918d3dae4b87f17b8bd549507 |
| R761 原完整 primitive 三线 | 23792 | db00a32be62403a016bb78f169cd478aefeb8d0354410c5b6373087d34f7a4b6 |
| 旧 E1 算法原脚本 | 4060 | abc12f49db1818351534889f31bd9b7bac7876a78cbd043a060834d97c2a8289 |

第三行只作为已支付有理区间方法的原文 pin；本次不 import、不执行它，
不重新生成其中两条旧曲线的系数。

输出严格为一个紧凑 JSON。它包括完整原输入哈希、十八环面和
$288$ 单位字符验收、所有六个 associates、所有 $512$ 系数和三共轭的验收、
完整系数数组哈希、三个真实 $a_{13}$ 六坐标、三个向外舍入到
$10^{-12}\mathbf Z$ 的 $L'$ 区间、无穷尾验收。
计算中没有文件输出。时间字段不参与任何数学判断。

只有三个**打印区间本身**都排除零时，
$\texttt{all_three_nonzero=true}$ 且总状态为 $\texttt{PASS}$。
否则总状态为 $\texttt{INCONCLUSIVE_NONVANISHING}$；
这不是解析秩大于一的证明，更不是本课题完成。

## 7. 原五 sigma 余项的后续入口

已执行的原 F0 返回给
$$
B_{\rm odd}
=\frac{\sigma(4z)\sigma(3z)\sigma(\delta z)^3}{1118208\delta}.
\tag{30}
$$
其真实负 $xy$ 基多项式是
$$
P_{\rm odd}(X)=
-\frac{3X(X+4)(X^2+20X-8)}{93184},\qquad
B_{\rm odd}=-\sigma^{34}xyP_{\rm odd}.
\tag{31}
$$
两条 R735 cubic rank-one 线的原投影准确为零；
(31) 是非零的整个 primitive 三维余块。
因为 $T^3+\omega$ 在 $K$ 上不可约，且 (31) 定义于 $K$，
它在 R761(26) 的三个几何特征线上都非零。
本次解析输入正为这三个实际分量逐一准备。

§8 的实际区间现已证明三个 $L'(\Psi_j,1)\ne0$。
§§9–11 用同一 good-pair、全局点域、完整局部 toric pairing
及全部周期，消费一般 Hecke 角色的 Gross–Zagier/原 point-log 公式，
得三个原负一值及 (31) 的非零。
三次系数域的角色始终按其实际 CM 簇与椭圆点张量处理。

此外原 F0 的完整后继是
$$
J_{\Phi_{126}}(v)=\frac1{18}
\iint_{x+y\in\mathbf Z_p^\times}
 \langle x+y\rangle^{(p-1)v}\,
 d\nu_{W_{51}}(x)\,d\nu_{\mathcal U_+C_1}(y),
\tag{32}
$$
其中原 degree51 因子、两个完整 Miller 字、共同 Gaussian 和 sum-unit
域都已固定。裸负一非零本身不允许把 (32) 改成两个独立单位域，
也不允许把带 $\log\langle x+y\rangle$ 的中央读者赋零。
§§9–11 已消费实际三个区间至有限点空间；(32) 的中央转置仍保全部费用。


## 8. 已完成的公开回执：三个原角色都严格解析一阶

唯一原请求实际运行如下，未再次执行旧两条曲线。

- run：[46004443574](https://github.com/Rogerhu12/math-research-public/actions/runs/46004443574)；
  job：140523950861；
- source commit：f13b8deaeeadc706a6f5fc1f1fe96c88a043eff4；
- 数学步骤：2026-11-27 13:07:52–13:08:01 UTC；
  producer 数学用时约0.847075275秒；
- producer：14113字节，SHA256仍为(29)，全部三个原输入 pin 一致；
- stdout：2755字节，SHA256
  371c1e80cac97d4bc15cd6b6ae2c25967704c11973d2e79318d284aa1373d178；
- 紧凑JSON本体：2754字节，SHA256
  7bee4b27ac061dab6aaae66fe90c6c853188c510d2d9cb949f416636b87d47ce；
- 完整job日志：11756字节，SHA256
  6ab1b5164b442f2de77377bc665cca4ffe8956874e2f61bdb95156cdb2811d37。

根实际读取全部回执，并从其中的单JSON重建原stdout字节核对其哈希。
这不是仅依据job绿色状态判断数学结论。

全部288有限单位、三个完整角色、45个好分裂素数的全部六个
associates/共轭/范数、512个系数的三个Galois返回，以及(28)的
完整无穷尾均通过。完整系数数组的SHA256是
8c5f75ac3eacd309b5793510812d9bc59b31773431822a166fe2442294a11b0d；
没有把该数组或日志作为仓库数据缓存。

证明非零所需的三个**实际打印有理区间**为：

| 原标签 $j$ | $L'(\Psi_j,1)$ 的下界 | $L'(\Psi_j,1)$ 的上界 |
|---|---:|---:|
| 1 | $5152227132381/10^{12}$ | $2576113566191/(5\cdot10^{11})$ |
| 7 | $1197928404807/(250000000000)$ | $4791713619229/10^{12}$ |
| 13 | $3574372413439/10^{12}$ | $174529903/48828125$ |

每个下界严格为正；每个区间已含全部尾项和向外舍入费用。
结合原root number $-1$，严格得到
$$
\boxed{\operatorname{ord}_{s=1}L(\Psi_j,s)=1
       \quad\text{对全部 }j=1,7,13.}
\tag{33}
$$
这里不由三个嵌入之一外推另两个。它也没有将这些CM实三次系数域
新形式改称三条有理椭圆曲线。

本节结论是以下真实点桥的解析输入；原sum-unit中央转置仍按 (32) 保持。


以下各节从实际 (33) 出发，证明
$$
L'(\Psi_j,1)\ne0\ \Longrightarrow\
I_{j,1}\ne0
\quad\text{在每个原好 ordinary }p.
\tag{33a}
$$
## 9. 一般 CM 角色的实际点公式：逐项核定假设

### 9.1 使用的完整定理和所有条件

使用 Bertolini–Darmon–Prasanna 2012，
*p-adic Rankin L-series and rational points on CM elliptic curves*，
[作者全文](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf)，
**Theorem 2，p.265；Proposition 3.31、Theorem 3.32，p.299**。
Theorem 2 是一般代数 Hecke 角色的版本；它的点非零条件明确是
$L'(\nu,1)\ne0$。这里不使用只针对有理椭圆曲线的 Theorem 1，
也不使用 §3G 的额外特例 Theorem 3.35。

把 $\nu=\Psi_j$ 代入，全部假设如下。

| 定理的条件 | 原三线的核定 |
|---|---|
| Infinity type $(1,0)$ | $\psi_0$ 为原 type$(1,0)$，$\eta_j$ 为有限阶，见 (8) |
| (1-6) $\nu|_{\mathbf A_\mathbf Q^\times}=\epsilon_K N$ | $\psi_0$ 为原 $E_0:y^2=x^3+1$ 角色，$\eta_j$ 在有理 idèle 上平凡，见 R761(8) |
| (1-7) root number $-1$ | 原2、3、17、无穷 epsilon 乘积，见 R761(13) |
| (1-8) $D_K$ 为奇数 | $D_K=-3$ |
| (1-9) 导子被 $\mathfrak d_K$ 恰除一次 | $\mathfrak f_{\Psi_j}=(34\delta)$，$34$ 素于3 |
| §3E 的普通素数条件 | 原 $p>211$、$p$ 在 $K$ 分裂，且 $p\nmid34\delta$ |
| §3F 的有限域下降条件 (3-37) | 下述 $H/K$ 为阿贝尔且 $\Psi_j\circ N_{H/K}=\psi_0\circ N_{H/K}$ 取值于 $K$ |

作者 §3G 后加的“单位群阶二”条件不属于上述一般定理；
本篇 $K=\mathbf Q(\sqrt{-3})$ 使用 Theorem 3.32，保原六单位全部体积，
没有借一个排除 $D=3$ 的特例。

系数域仍是
$$
E=\mathbf Q(\zeta_9),\qquad [E:K]=3.
$$
Theorem 2 的 $B_{\Psi_j}$ 是定义于 $K$ 的三维 CM 阿贝尔簇。
它不是一条定义于 $\mathbf Q$ 的椭圆曲线。
本篇用 Theorem 3.32 将其指定 CM 分量返回共同椭圆曲线的点张量，
不将三维簇整体的一个 $p$-adic 坐标与某椭圆曲线对数混同。

### 9.2 同一 good-pair 和反向 Gross–Zagier 的局部因子

这一段解释 (33a) 为什么不是倒用 R748 的单向论证。

对于固定 $j,p$，按原 R761(41) 和
[R748](R748-original-type-five-ramified-good-pair-and-point-eigenspaces.md)§2
取 good pair $(\psi,\xi)$：
$$
\psi\xi^{-1}=\Psi_j,\qquad
L(\psi^*\xi^{-1},1)\ne0.
\tag{34}
$$
$\psi$ 的 cyclic conductor 避开 $2,3,17,p$；
原2、17有限九阶角色真实留在 $\xi$ 中，不换成只有 $p$ 分歧的字符。
BDP Definition 3.19、Proposition 3.28 正是此构造的原出处。
这里有限 $p$-character 是平凡角色，故不需要把其 prime-to-$p$
定理无证延伸到 ramified $p$ 分支。

同一个 good pair 的 Rankin 导数准确为
$$
L'(\theta_\psi,\xi^{-1},1)
 =L'(\Psi_j,1)L(\psi^*\xi^{-1},1).
\tag{35}
$$
BDP Lemma 3.25 和紧随的 Remark 3.26 使用一般 Gross–Zagier 公式，
并明确保全原坏处 local zeta integrals 的非零。
这一步是反向的必要费用：若 (35) 非零，
**实际选择的 Heegner 点**非挠，而不是任意挑一个形式点。
R748§3(17) 同时保普通 local $Q_p$、有限体积、
Gauss 和和原代数微分；R761(42) 沿同一规范使用这些因子。
在本次未分歧 ordinary $p$，真实 Euler 因子非零；
一旦其等于零，会迫一个 Frobenius 根满足与其复绝对值矛盾的有限阶或范数等式。
其余坏处非零是 good-vector 的完整局部结论，不以“只差一个单位”代替。

两 toric 点经原有限 CM twist isogeny 返回同一 holomorphic 分量：
$$
\psi\xi^{-1}=\Psi_j,\qquad
\frac{N}{\psi^*}(\xi^*)=\frac{N}{\Psi_j^*}=\Psi_j.
\tag{36}
$$
R748(22a)–(22c) 已保持两 CM loci 的不同 reciprocity 和同一系数嵌入，
故 (36) 没有把 $\eta_j$ 点与 $\eta_j^{-1}$ 点误认。
全部 auxiliary conductor 经这个真实 isogeny 从点因子上消去；
保留在代数标量中的有限角色和微分费用不被删去。

BDP Theorem 2、Proposition 3.27 的双向非零结论正汇总 (34)–(36)。
本篇只取已经成立的方向“$L'$ 非零推出这个点非零”。
它与 R748 为一般有限角色规定“当 Katz 为零时可取零点”的表述不同；
不能仅从那条存在性表述推出 (33a)。

### 9.3 准确的共同点域和点特征

由 R761(38)–(39)，置
$$
H=K^{\ker\eta_1}=K^{\ker\eta_7}=K^{\ker\eta_{13}},
\qquad \operatorname{Gal}(H/K)\simeq C_9.
\tag{37}
$$
其二处惯性阶3、十七处惯性阶9、三处及本次普通 $p$ 不分歧。
系数域 $E$ 和点坐标域 $H$ 不相认。

$\eta_j$ 限制到 $G_H$ 为平凡，因此
$$
\Psi_j\circ N_{H/K}=\psi_0\circ N_{H/K}.
\tag{38}
$$
BDP§3F(3-37) 因而可直接取 $F=H$，
对应椭圆曲线取 **原** $E_0/H$，代数微分
$\omega_0=dx/(2y)$。
原有理模型的 CM 角色恰为右边，不需另一个 sextic twist。

Proposition 3.31 的点条件是
$$
\phi_\mathfrak a(P)=\Psi_j(\mathfrak a)P^{\sigma_\mathfrak a}.
$$
在 $E_0$ 上 $\phi_\mathfrak a=[\psi_0(\mathfrak a)]$，
代入 (8) 立即给
$$
P^{\sigma_\mathfrak a}=\eta_j(\mathfrak a)P.
\tag{39}
$$
这是固定代数系数后的 **点因子**作用。
它不是同时共轭 $\zeta_9$ 系数的自然 semilinear 作用。

Theorem 3.32 因而给
$$
P_j\in
  \bigl(E_0(H)\otimes_{\mathbf Z}\mathbf Q\bigr)
                \otimes_K E,\qquad
g_{\rm pt}P_j=\eta_j(g)P_j,
\tag{40}
$$
其非零恰由 (35) 支付。
若改变 good pair，只改变对应非零代数比例和同一 CM 点直线的生成元；
不能把点域扩大后忘掉 (39) 的实际下降。

## 10. 普通对数单射、原周期和全部三个负一值

### 10.1 非零点张量到指定 ordinary 对数

固定原嵌入 $\iota_p:\overline{\mathbf Q}\hookrightarrow\mathbf C_p$。
[R749](R749-point-factor-projectors-and-finite-character-extraction.md)
Theorem 1 给实际映射
$$
\mathscr L_p:
\bigl(E_0(\overline{\mathbf Q})\otimes\mathbf Q\bigr)
              \otimes_{K,\iota_p}\overline{\mathbf Q}
 \longrightarrow\mathbf C_p,
\quad
P\otimes a\longmapsto a\log_{\omega_0}P
\tag{41}
$$
单射。其使用范围在此逐项满足：

1. (40) 只含有限多个实际代数点，全部坐标在固定 $H$；
2. 所有系数在代数域 $E$，没有任意 $\mathbf C_p$ 系数；
3. $E_0$ 为简单椭圆曲线，原 $\operatorname{End}^0(E_0)=K$；
4. 取有限指数可将这些点同时放入 formal exponential 的单射域；
5. 对 K 独立点的对数，R749 所引 p-adic analytic subgroup theorem
   给其代数数线性独立，故 (41) 在这个有限 tensor 上确为单射。

因此由 $P_j\ne0$ 真正得到
$$
\log_{\omega_0}P_j\ne0.
\tag{42}
$$
这不是“三维簇非挠点的一枚 arbitrary 坐标一定非零”的猜测；
它使用了 (38)–(41) 的完整椭圆点返回。

### 10.2 原 primitive Katz 和 sigma 周期的全比较

使用同一个 $\theta=17^{1/6}$、原 $\Omega_p$，
以及 R761(24)、(27) 的实际首阶 $r_j$ 和归一：
$$
D_{j,17}(z)=\theta^{-r_j}D_{j,1}(\theta z),
\qquad \Omega_{p,0}=\theta\Omega_p,
\qquad
I_{j,1}=\int_{\mathbf Z_p^\times}x^{-1}d\nu_{D_{j,17}}(x).
\tag{43}
$$
本篇不重新规定 dyadic splitting 或 $s_j$，全部沿 R761 的
完整 Hermite/Gaussian/有限范数。

Theorem 3.32 及 (34)–(36) 的准确代数 normalization 给
$$
\mathcal K_{34\delta}(\eta_j\widehat{\bar\psi}_0)
=\varepsilon_{j,p}\,\Omega_{p,0}^{-1}
         \log_{\omega_0}(P_j)^2,
\qquad \varepsilon_{j,p}\in\overline{\mathbf Q}^{\times}.
\tag{44}
$$
代数性和非零性使用原 BDP finite-twist period rule
及 R748§3 的完整 Rankin–Katz 规范；
$\varepsilon_{j,p}$ 不被宣称是 $p$-adic 单位，
也不以未知 Iwasawa unit 代替。

R761(35) 在同一原 primitive conductor、同一嵌入中是
$$
\mathcal K_{34\delta}(\eta_j\widehat{\bar\psi}_0)
=34c_j\theta^{2r_j+1}\Omega_p I_{j,1}^{\,2},
\qquad c_j\in\overline{\mathbf Q}^{\times}.
\tag{45}
$$
两个 ordinary Euler 因子及其高正权极限已经包含在此式。
若中间使用 imprimitive 记号，必须按 R748§3 恢复准确 Euler 因子，
不能把不同 primitive conductor 的 Katz 函数直接相等。

由 (44)、(45)，
$$
\boxed{
\Omega_p I_{j,1}=A_{j,p}\log_{\omega_0}(P_j),\qquad
A_{j,p}^{\,2}=
 \frac{\varepsilon_{j,p}}{34c_j\theta^{2r_j+2}}
 \in\overline{\mathbf Q}^{\times}.
}
\tag{46}
$$
符号按实际相等选取。周期多出来的 $\theta$ 来自
$\Omega_{p,0}=\theta\Omega_p$，不能漏掉。
(42)、(46) 完成 (33a)。
在全部原 ordinary 射线素数上都成立，
不需要对 $p$ 作新扫描，也不以有限一组 $p$ 的非零代替证明。

### 10.3 三个点特征和有限门的直接和

三个 $\eta_1,\eta_7,\eta_{13}$ 在 $\operatorname{Gal}(H/K)$ 上不同。
按 R749 的点因子幂等元
$$
e_{\eta_j}^{\rm pt}
=\frac19\sum_{g\in\operatorname{Gal}(H/K)}
               \eta_j(g)^{-1}g_{\rm pt},
\tag{47}
$$
保持 (46) 的代数系数不动。
由 (33)，三个解析输入都非零，故三个 $P_j$ 都非零；
(41)、(47) 给
$$
\{\Omega_p I_{1,1},\Omega_p I_{7,1},\Omega_p I_{13,1}\}
\quad\text{在 }\overline{\mathbf Q}\text{ 上线性独立}.
\tag{48}
$$
这是线性独立，不是代数独立。

对于 R761 已付的任意有限 $p$-character，原点因子在 chosen
$p$-units 上为 $\chi^{-1}$，在17处仍为对应 $\eta_j$。
因此固定有限门的 Fourier 展开中，不同 $(j,\chi)$ 可在同一个有限点域中
逐项分离；零值分量允许为零。若一条本篇非零来源所乘有限函数的
平凡 Fourier 系数非零，则其完整负一有限门值非零。
这只消费已付的**有限**点载体，没有把 (47) 延拓到无证明连续的
无限 logarithm 极限。

## 11. 对实际 F0 primitive 余项的准确非零消费

### 11.1 实际 $b=1$ 返回与原 $b=17$ 周期运输

第7节 (30)、(31) 的实际多项式计算使用 $E_0:y^2=x^3+1$。
此处明确记该来源为 $B_{\rm odd,1}$，不能把其数值多项式直接写成
$E_{17}$ 上的同一个多项式。

它在三条 $b=1$ 线上的完整分解是
$$
B_{\rm odd,1}=\sum_{j\in\{1,7,13\}}b_jD_{j,1},
\qquad b_j\in\overline{\mathbf Q}^{\times}.
\tag{49}
$$
全部 $b_j\ne0$ 的理由是 §7 的实际非零余块与不可约
$T^3+\omega$，不是由首个 Taylor 系数猜 eigenvector。
原 R735 两线投影为零已经由原公开全式核过，故 (49) 没有漏项。

保原 $\Omega_{p,0}=\theta\Omega_p$ 和同一物理测度变量，
R761(27) 的完整测度运输逐条是
$$
\nu_{D_{j,1}}=\theta^{r_j}\nu_{D_{j,17}}.
$$
所以原返回的负一值准确为
$$
\boxed{
\int_{\mathbf Z_p^\times}x^{-1}d\nu_{B_{\rm odd,1}}(x)
 =\sum_jb_j\theta^{r_j}I_{j,1}\ne0,
}
\tag{50}
$$
其中非零由第8节的实际三个严格正区间和 (48) 给出。
$\theta^{r_j}$ 是非零代数数，不能漏掉或吸收入未定 $p$-adic unit。

也可定义真实首阶五的 $b=17$ 运输
$$
B_{\rm odd,17}(z)=\theta^{-5}B_{\rm odd,1}(\theta z).
$$
于是
$$
B_{\rm odd,17}
 =\frac{3\,\sigma_{17}^{34}x_{17}^4y_{17}
             (X_{17}+4\cdot17)
             (X_{17}^2+20\cdot17X_{17}-8\cdot17^2)}{93184},
\tag{50a}
$$
且仍准确是同一五个 $\sigma_{17}$ 的乘积
除以 $1118208\delta$。
其负一值为 $\theta^{-5}$ 乘 (50)，因而也非零。
这里首阶五的缩放专属于奇部；
没有把不同首阶的完整 $\mathcal B_+$、$\mathcal B_-$
分别按同一个首阶五常数重新归一。

### 11.2 完整差值与有限门

在原 $b=1$ 的两个 actual Miller 返回中，
$$
\mathcal B_+-\mathcal B_-=2B_{\rm odd,1}.
$$
(50) 因而给它们在同一负一泛函上的非零差。
更一般地，对有限、代数值、平凡 Fourier 系数非零的原单位门，
(49) 和有限点特征分离给其同一完整差值非零。
对应 $b=17$ 输入必须使用上述全周期运输，再保原两字各自的绝对常数。

原 rank-two 中央来源的读取仍是 (32)：
$W_{51}$ 的整个测度、两个 actual Miller 字、Gaussian 和
$x+y\in\mathbf Z_p^\times$ 的耦合域全部保留。
(50) 不是把 $\mathcal U_+C_1$ 乘任意解析权后仍非零的定理；
也不能把由 (32) 产生的无限 $\log\langle x+y\rangle$ 展开施
未证明连续的点因子投影。
后继需要将这些已经非零的有限点分量接到同一 sum-unit
完整转置，不能由裸负一非零直接宣告原中央非零。

### 本节 primary 文献入口

- M. Bertolini, H. Darmon, K. Prasanna,
  *p-adic Rankin L-series and rational points on CM elliptic curves*,
  Pacific J. Math. **260** (2012), 261–303，
  [DOI](https://doi.org/10.2140/pjm.2012.260.261)，
  [作者全文](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf)：
  Theorem 2（p.265）、Definition 3.19（p.287）、
  Lemma 3.25 / Remark 3.26（pp.290–291）、
  Propositions 3.27–3.28（p.291）、
  Proposition 3.31 / Theorem 3.32（p.299）。
- [R748](R748-original-type-five-ramified-good-pair-and-point-eigenspaces.md)
  §3–4：原 good-pair、primitive normalization、local $Q$、
  两 CM loci 和同一 holomorphic 点分量。
- [R749](R749-point-factor-projectors-and-finite-character-extraction.md)
  Theorem 1、§2、§5：真实椭圆点 logarithm 单射和固定系数点因子投影。
- [R761](R761-primitive-type-five-ninth-order-characters-and-point-fields.md)
  (35)、(38)–(46)：本次完整三角色、准确 cyclic9 点域、共同周期与原 Katz 平方。
