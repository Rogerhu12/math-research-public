# R256 — 原八挠平移的两个单位与十七处分歧给出的对数分离

日期：2026-11-13。**状态：R246/R250 中实际纯八挠平移常数的两个明确生成元、它们的乘法独立性、四个原八次 ray 对数与固定 prime-to-17 挠点对数的代数系数线性分离，均已证明。包含原 norm-two、norm-five、norm-seventeen 尺度的十一维独立性也已证明。没有将非恒定 Mellin 对数项替换成这些常数；混合十七挠点常数另须处理。**

沿用 $E_0:y^2=x^3-x$、$K=\mathbf Q(i)$、
$r=(x-1)/(x+1)$、$\beta=4-i$、$\alpha=4+i$、
$\pi=2+i$、$\bar\pi=2-i$。所有 $p$ 进对数都用同一个
$\overline{\mathbf Q}\hookrightarrow\overline{\mathbf Q}_p$ 和标准分支。

## 1. 实际纯八挠位移的全部值

R246 §7 的 $\mathcal V$ 分支和 R250 §8 的 $Q_{+,v}$ 分支，
其对数常数都为 $\log_p r(T)$，其中
$$
T=(a_0+b_0i)\Omega/8,\qquad a_0,b_0\text{ 均为奇数}.
\tag{1}
$$
这里使用原方格周期 $\Omega\mathbf Z[i]$。因此
$4T=T_0=(1+i)\Omega/2$，$x(T_0)=0$。
由原倍点公式
$$
x(2z)=\frac{(x(z)^2+1)^2}{4x(z)(x(z)^2-1)}
\tag{2}
$$
得 $x(2T)=i$ 或 $-i$。令 $t=r(T)$，把
$x=(1+t)/(1-t)$ 代入 (2)，得到
$$
x(2T)=\frac{(1+t^2)^2}{4t(1-t^2)}.
$$
所以 (1) 中的八个不同 $r$ 值恰好为
$$
\begin{aligned}
f_+(t)&=t^4+4it^3+2t^2-4it+1,\\
f_-(t)&=t^4-4it^3+2t^2+4it+1
\end{aligned}
\tag{3}
$$
的全部根；这里 $f_+$ 对应 $x(2T)=i$。共有十六个点，
$T\leftrightarrow-T$ 两两给同一个 $x$；(3) 的八个根互异。

取下面固定复嵌入中的正实根：
$$
a=\sqrt2,\quad A=\sqrt{2a-2},\quad
B=\sqrt{2a+2}=2/A=A(a+1),
$$
并定义
$$
\boxed{u=A+i(a-1),\qquad v=-i(a+1+B).}
\tag{4}
$$
准确因式分解为
$$
f_+(t)=\bigl(t^2-2i(a-1)t-1\bigr)
        \bigl(t^2+2i(a+1)t-1\bigr).
\tag{5}
$$
故 $f_+$ 的根为 $u,-u^{-1},v,-v^{-1}$，$f_-$ 的根是它们的负数。
这证明实际常数的完整化简
$$
\boxed{r(T)\in\{\pm u,\pm u^{-1},\pm v,\pm v^{-1}\},\qquad
\log_p r(T)\in\{\pm\log_pu,\pm\log_pv\}.}
\tag{6}
$$
无需选择新的 $p$ 进对数支；$\log_p(-1)=0$。
两个单位的选择只固定 (6) 中的标签，结论不依赖复根的命名。

## 2. 两个全局单位的独立性及固定二次幂数域

令 $M=K(a,A)$。由 (3) 的首一性与常数项一，$u,v$ 和它们的逆
都是全局代数整数。它们是全局单位。

准确有 $[M:K]=4$。首先 $a\notin K$。若 $A=c+da$，$c,d\in K$，
比较平方给 $cd=1$、$c^2+2d^2=-2$，所以 $c^2=-1+i$ 或 $-1-i$。
但这两数在 $K/\mathbf Q$ 下的范数都是二，不是有理数的平方，
不可能是 $K$ 中的平方。因此 $A\notin K(a)$。
另一方面
$$
a=\frac{u-u^{-1}+2i}{2i},\qquad A=u-i(a-1),
$$
所以 $K(u)=M$，(3) 的 $f_+$ 就是 $u$ 的最小多项式。

两个 $K$ 自同构可取
$$
\sigma(a)=a,\quad\sigma(A)=-A;\qquad
\tau(a)=-a,\quad\tau(A)=2i/A.
\tag{7}
$$
它们交换且均阶二，给出 $\operatorname{Gal}(M/K)\simeq C_2^2$。
其中 $\sigma(u)=-u^{-1}$、$\tau(u)=-v^{-1}$、
$\sigma\tau(u)=v$。

在选定复嵌入中，$|u|=1$，而 $|v|=a+1+B>1$。
$u$ 的共轭 $v$ 绝对值大于一，故 $u$ 不是根单位。
若 $u^m v^n$ 是根单位，先取此嵌入的绝对值得 $n=0$，
再由 $u$ 非根单位得 $m=0$。因此
$$
\boxed{u,v\text{ 在 }M^\times/\mu(M)\text{ 中乘法独立。}}
\tag{8}
$$
精确判别式是
$$
\operatorname{disc}(f_+)=-2^{16},\qquad
f_+f_-=t^8+20t^6-26t^4+20t^2+1,
\quad\operatorname{disc}(f_+f_-)=2^{64}.
\tag{9}
$$
因 $M=K(u)$ 且 $u$ 整，数域相对判别式整除其多项式判别式，
所以 $M/K$ 只可能在二处分歧，特别在 $\beta$ 处不分歧。

## 3. 原十七单位数域在 $\beta$ 处全分歧

沿用 R253 的 $L=K(x(P))$，其中 $P\in E_0[\beta]\setminus\{O\}$。
该篇已证明 $L/K$ 是八阶循环 Galois 扩张，并定义
$r_j=r(3^jP)$、$0\le j\le3$。四单位乘法独立，且
$r_{j+4}=r_j^{-1}$。

原八次 division 多项式是
$$
K_8(X)=\beta X^8+(-12+20i)X^6+(28+10i)X^4
                 +(-20-12i)X^2-i.
$$
对 $Y=1/x(P)$，准确反转并乘 $i$ 得
$$
\boxed{
iY^8K_8(Y^{-1})
=Y^8+i\beta\bigl[(-4-4i)Y^6+(6+4i)Y^4
                         +(-4+4i)Y^2+1\bigr].}
\tag{10}
$$
这是 $\beta$-Eisenstein 多项式：全部非首项系数都被 $\beta$ 整除，
常数 $i\beta$ 的 $\beta$ 赋值准确为一。因此 $L/K$ 在 $\beta$ 处
全分歧，局部次数也是八。特别，$L/K$ 的任何非平凡中间域
都在 $\beta$ 处分歧。

## 4. 与任意固定不分歧数域中单位对数的分离

**命题。** 设 $M'/K$ 为有限 Galois 扩张，在 $\beta$ 处不分歧。
取有限个 $a_1,\ldots,a_s\in M'^\times$，在当前 $p$ 进嵌入下均为单位。
令
$$
V_{M',p}=\operatorname{span}_{\overline{\mathbf Q}}
  \{\log_pa_1,\ldots,\log_pa_s\}.
$$
则 R253 的四个实际常数满足
$$
\boxed{\operatorname{span}_{\overline{\mathbf Q}}
  \{C_1,C_3,C_5,C_7\}\ \cap\ V_{M',p}=0.}
\tag{11}
$$
这里所有标量通过同一个固定嵌入解释；不要求 $a_j$ 是全局单位。

**证明。** 由全分歧与不分歧性，$L\cap M'=K$，故
$\operatorname{Gal}(LM'/M')\simeq\operatorname{Gal}(L/K)$。
又由 $r_{j+4}=r_j^{-1}$，
$$
N_{LM'/M'}(r_j)=N_{L/K}(r_j)=1.
\tag{12}
$$
从 $\{\log_pa_j\}$ 中取一个 $\mathbf Q$ 线性基，仍由其中的若干
对数构成。若该基与四个 $\log_pr_j$ 有有理系数关系，清分母后为
$$
\log_p\left(\prod_{j=0}^3r_j^{n_j}\,a\right)=0,
\qquad a\in M'^\times.
$$
括号内是局部单位，故为根单位 $\xi$。取 (12) 的范数，得到
$a^8=N(\xi)$ 是根单位，因而 $a$ 本身是根单位。
于是 $\prod r_j^{n_j}$ 也是根单位；R253 的乘法独立性给全部
$n_j=0$。选定的 $\mathbf Q$ 基再给其余系数全零。

Brumer 的 $p$ 进对数定理把这组代数单位对数的 $\mathbf Q$ 线性
独立提升为 $\overline{\mathbf Q}$ 线性独立。最后用 R253 中可逆的
Vandermonde 变换
$$
C_k=4\sum_{j=0}^3\zeta_8^{-kj}\log_pr_j,\qquad k=1,3,5,7,
$$
即得 (11)。这只使用线性独立定理，没有对对数乘积作推断。证毕。

## 5. 实际 prime-to-17 挠点常数的适用范围

取任意固定整数 $m$，$17\nmid m$。$E_0$ 在 $\beta$ 处好约化，
而 $[m]$ 的微分为可逆元 $m$，故 $E_0[m]$ 是该局部整数环上的
有限 étale 群概形。其全部点可在最大不分歧扩张中定义。
因此有限 Galois 扩张
$$
M'=K(E_0[m])/K
$$
在 $\beta$ 处不分歧，满足 §4 的条件。

对 $Q\in E_0[m]$，只要 $r(Q)$ 既非零也非无穷，它就在 $M'$ 中。
排除 $p\mid2m$，prime-to-$p$ 挠点的约化单射保证 $Q$ 不会在
约化后变成 $r$ 的二挠零极点，故 $r(Q)$ 是 $p$ 进单位。
所以 **任意固定有限批 prime-to-17 挠点的实际 $\log_pr(Q)$**
都可放入 (11) 的右侧。

这既覆盖 §1 的纯八挠常数，也覆盖 R251 有限 $N^j$ 展开所引入的
固定 $2^a5^b$ 挠点常数。对这些实际二、五幂阶点，$p>19$ 已排除
所有挠点阶数的坏素数。额外固定代数比例若也在这样一个不分歧
数域中且为当前 $p$ 进单位，可以同时加入；无需逐一计算它们的
最小多项式。

**混合十七挠点不在此范围。** 例如把真实共轭十七逆像与
dyadic 分支组合会出现 $r(T+aP+Q)$，其中 $Q\in E_0[\bar\beta]$。
其字段含十七挠点，不能由本节判为 $\beta$ 不分歧，不能把其对数
预先化入 $\log_pu,\log_pv$。应先用真实分布式或实际 Galois 范数
计算可消去的组合。

## 6. 十一个固定对数的代数系数线性独立

对 $p>19$，以下十一数在 $\overline{\mathbf Q}$ 上线性独立：
$$
\boxed{\begin{gathered}
C_1,C_3,C_5,C_7,\quad\log_pu,\log_pv,\quad\log_p2,\\
\log_p5,\quad\log_p(\pi/\bar\pi),\quad
\log_p17,\quad\log_p(\alpha/\beta).
\end{gathered}}
\tag{13}
$$
为核定全部独立性，先在 $M$ 中比较
$2,5,\pi/\bar\pi,17,\alpha/\beta$ 的有限赋值。
按 $(1+i),(\pi),(\bar\pi),(\alpha),(\beta)$ 排列，忽略每一行
共同的正分歧指数后，其五列准确为
$$
\begin{pmatrix}
2&0&0&0&0\\
0&1&1&0&0\\
0&1&-1&0&0\\
0&0&0&1&1\\
0&0&0&1&-1
\end{pmatrix},\qquad\det=8\ne0.
\tag{14}
$$
$u,v$ 是全局单位，所以任何根单位关系先由 (14) 消去这五个
指数，再由 (8) 消去 $u,v$ 的指数。所得七个对数在 $\mathbf Q$ 上
线性独立。由 §4 与 $M/K$ 在 $\beta$ 处不分歧，加入四个
$\log_pr_j$ 后仍独立；再由 Brumer 和原 Vandermonde 变换得 (13)。

因此原中央转置中已经明确为这些固定常数的部分可以作唯一的
代数系数分解。然而 R246/R250 的 $f(u-1),f(u-2)$、$W$ 项及
交换差中的非恒定对数仍是实际解析泛函。本篇没有证明它们属于
(13) 的线性空间，也没有证明它们在三条原中央行同时零时消失。
完成这些实际比较，才可能由 (11) 或 (13) 排除原三零。

## 精确证书和来源

- [脚本](../scripts/check-dyadic-log-units-and-ramification.py) 与
  [输出](../scripts/check-dyadic-log-units-and-ramification.json) 核定实际
  倍点变换、两个四次因子、全部根与自同构恒等式、两判别式、
  原 division 的 Eisenstein 反转及五列赋值行列式；没有素数扫描。
- 原分支位置和完整中央连接：R246 §7、R250 §8、R251 §7。
  原四单位的全部 Galois 作用、严格乘法独立证书和 $C_k$ 定义：R253。
- A. Brumer，*On the units of algebraic number fields*，Mathematika
  **14** (1967)，121–124，Theorem 1，
  [DOI](https://doi.org/10.1112/S0025579300003703)。本篇使用的准确
  局部单位对数形式见 R. Sharifi，
  [Iwasawa Theory，Theorem 1.5.17](https://math.ucla.edu/~sharifi/notes/iwasawa-ch01.html)，
  已于 2026-11-13 核读。
