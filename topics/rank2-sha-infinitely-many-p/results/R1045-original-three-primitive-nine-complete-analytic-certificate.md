# R1045 — 原型五三条九阶角色的完整解析一阶判据与固定有理证书

日期：2026-11-27 UTC。

**当前状态：原角色的全部系数生成、完整三个共轭、唯一参数的严格解析区间算法已证明；本稿不预写尚未返回的公开作业结果。** 本篇只消费 [R761](R761-primitive-type-five-ninth-order-characters-and-point-fields.md) 的三条原 primitive type-five 角色。其 root number 均为 $-1$，但 R761 未证明它们的 $L'(1)$ 非零。原 [F0 两字的真实返回](../notes/2026-11-27-original-f0-two-delta-word-return.md) 恰出现这一整块，因此本次是更换未付清的真实输入，不重算 R735 的两条 cubic 曲线。

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

即使公开输出证明三个 $L'(\Psi_j,1)\ne0$，
仍须在 R761§6 的同一 good-pair、全局点域、真实局部 toric pairing
及全部周期中消费 Gross–Zagier/原 point-log 公式，
才能把解析输入变成原负一矩的非零。
不能将三次系数域的角色冒作三条有理椭圆曲线来调用缩略版本。

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
本篇后续将从实际公开三个区间开始消费这些全式。
