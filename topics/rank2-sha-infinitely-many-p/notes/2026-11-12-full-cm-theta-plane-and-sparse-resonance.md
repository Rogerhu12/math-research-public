# 全 CM theta–sigma 平面、稀疏共同共振与准确一次除 p

日期：2026-11-12。
**状态：以下多项式映射、整性、逐阶递推及最佳分母赋值已证明。**
本文扩展 R167 的整数倍乘；没有据此宣称 R159 所需的全部饱和
前缀格严格预算已经成立。

## 1. 固定对象与结论

沿 R166–R167，固定

$$
E_0:y^2=x^3-x,\qquad K=\mathbb Q(i),\qquad
R=\mathbb Z[i,1/2],
$$
$$
\omega=dx/(2y),\quad z=\log_{E_0},\quad
u=x^{-1/2},\quad s=u^4,\quad w=z^4,\quad
\vartheta=\sigma/u.
$$

这里平方根及 sigma 均按原点首项固定：
$u=z+O(z^5)$、$\sigma=z+O(z^5)$、$\vartheta(0)=1$。
取 R167 的同一个真实平面

$$
a=\vartheta^4=x^2\sigma^4,\qquad b=\sigma^4,\qquad
\gamma(w)=(a(w),b(w)).
\tag{1.1}
$$

基点为 $(1,0)$，且

$$
\gamma'(0)=(1/3,1),\qquad s=b/a.
\tag{1.2}
$$

R167 已证明 $a,b$ 代数独立，并把原来的两条秩二输入写成固定齐次
次数十七的 $R[1/5][a,b]$ 多项式。本文不改变这些原输入。

**主命题。** 对每个非零 $\beta\in\mathbb Z[i]$，存在齐次次数
$d=N\beta$ 的映射

$$
F_\beta\in R[a,b]^2,\qquad
F_\beta\gamma(w)=\gamma(\beta^4w).
\tag{1.3}
$$

它固定 $(1,0)$，满足

$$
F_\alpha F_\beta=F_{\alpha\beta},\qquad
F_\epsilon=\mathrm{id}\quad(\epsilon\in\{1,-1,i,-i\}),
\tag{1.4}
$$

以及准确的 Jacobian

$$
J_\beta(1,0)=
\begin{pmatrix}
d&(\beta^4-d)/3\\
0&\beta^4
\end{pmatrix}.
\tag{1.5}
$$

因此实际切向特征值是 $\beta^4$，横向特征值是 $N\beta$。
这里的范数不是 $\beta^2$；也没有留下随 $\beta$ 变化的二次指数
修正因子。

## 2. 奇范数 sigma 除法：半特征与指数均已固定

设方格周期格为 $\mathcal L=\Omega\mathbb Z[i]$。
经典 sigma 的准周期式给

$$
\sigma(z+\lambda)
=\epsilon(\lambda)
 \exp\bigl(\eta(\lambda)(z+\lambda/2)\bigr)\sigma(z).
\tag{2.1}
$$

若 $\lambda=m\Omega+ni\Omega$，则
$\epsilon(\lambda)=(-1)^{m+n+mn}$；其模 $2\mathcal L$ 的值为零类取
$1$，其他三个类取 $-1$。同时

$$
\sigma(iz)=i\sigma(z),\qquad
\eta(i\lambda)=-i\eta(\lambda),\qquad
\eta(\beta\lambda)=\bar\beta\,\eta(\lambda).
\tag{2.2}
$$

最后一个式子来自 $\eta$ 的整数线性，而非把它当成复线性函数。
原始准周期公式见 [DLMF 23.2.17](https://dlmf.nist.gov/23.2.E17)；
本项目较早的
[CM sigma 除法笔记](2026-11-12-cm-sigma-division-and-common-resonance.md)
也给出了 (2.2) 的完整推导。

现在设 $d=N\beta$ 为奇数。$\beta$ 模 $2$ 是 $1$ 或 $i$，
因而置换三个非零类，保留上述 sigma 符号。令

$$
\Psi_\beta(z)=\frac{\sigma(\beta z)}{\sigma(z)^d}.
\tag{2.3}
$$

在 $z\mapsto z+\lambda$ 下，指数差准确为

$$
\bar\beta\eta(\lambda)(\beta z+\beta\lambda/2)
 -d\eta(\lambda)(z+\lambda/2)=0.
$$

符号差亦为一，所以 (2.3) 是椭圆函数。其除子及首项为

$$
\operatorname{div}\Psi_\beta=[\beta]^*(O)-d(O),\qquad
\Psi_\beta(z)=\beta z^{1-d}+\cdots.
\tag{2.4}
$$

除子在 $K$ 上定义，首项固定常数，故由 Galois 下降
$\Psi_\beta\in K(E_0)$。奇范数必有 $d\equiv1\pmod4$，从而
$\Psi_\beta(iz)=\Psi_\beta(z)$。它只有 $O$ 处一个极点，故

$$
\Psi_\beta\in K[x^2],\qquad
\deg_{x^2}\Psi_\beta=(d-1)/4,\qquad
\text{最高系数为 }\beta.
\tag{2.5}
$$

这也支付了 theta 半特征：$T=(0,0)$ 是唯一被 $[i]$ 固定的非零
二挠点，而奇范数 $\beta$ 满足 $[\beta]T=T$。下面由
$\vartheta^2=x\sigma^2$ 及原点值一确定其准确乘法式，不另选可能改变
常数或指数的 theta 规范。

若将 sigma 改成 $\sigma_c(z)=e^{cz^2/2}\sigma(z)$，(2.3) 会新增
$e^{c(\beta^2-d)z^2/2}$。本文使用的 $c=0$ 是由固定 CM 对称性选择的
原规范。特别不能先任意选补空间，再把这个因子略去。

## 3. 奇范数的两个整多项式

令

$$
\phi_\beta(x)=x([\beta]P)\Psi_\beta(x)^2.
$$

在每个非零核点处，$\Psi_\beta^2$ 的二重零消去 $x([\beta]P)$ 的
二重极点；在 $O$ 处首项是 $z^{-2d}$。因此
$\phi_\beta\in K[x]$ 是次数 $d$ 的首一多项式。
由于 $[\beta]T=T$，$[\beta]^{-1}T$ 包含 $T$，其他点以 $\{P,-P\}$
配对。$x$ 在 $T$ 的二重零给多项式的简单根 $x=0$；
其余每对给二重根。因此唯一存在首一多项式 $h_\beta$，使

$$
\phi_\beta=xh_\beta^2,\qquad
\deg_xh_\beta=(d-1)/2.
\tag{3.1}
$$

与 $[i]$ 交换给 $\phi_\beta(-x)=-\phi_\beta(x)$；
$h_\beta$ 的次数为偶数及首一性于是给 $h_\beta(-x)=h_\beta(x)$。
故置 $m=(d-1)/4$ 后

$$
H_\beta(s)=x^{-2m}h_\beta(x),\qquad
D_\beta(s)=x^{-2m}\Psi_\beta(x)
\tag{3.2}
$$

属于 $K[s]$、次数至多 $m$，且

$$
H_\beta(0)=1,\qquad D_\beta(0)=\beta.
\tag{3.3}
$$

### 3.1 包括除范数素数在内的整性

准确结论是

$$
h_\beta,\Psi_\beta\in R[x],\qquad H_\beta,D_\beta\in R[s].
\tag{3.4}
$$

特别不要求所考察的奇素数避开 $N\beta$。
以下给出此处不能省略的整模型及无竖直因子论证。

$E_0/R$ 是光滑椭圆曲线，$[i](x,y)=(-x,iy)$ 在其上定义，
故 $[\beta]=[a]+[b][i]$ 是该椭圆曲线的实际端同态。
它与 $[-1]$ 交换，下降为

$$
g_\beta:\mathbb P^1_R=E_0/\{\pm1\}\longrightarrow\mathbb P^1_R.
$$

其每个纤维的次数为 $d$：椭圆曲线上拉回一个次数一线丛的次数在
连通底上恒定，泛纤维的次数为 $d$，因此没有常值特殊纤维。
在商上同样得到次数 $d$。又因为 $R$ 是 PID，

$$
g_\beta^*\mathcal O(1)\simeq\mathcal O(d)
$$

没有剩余的底空间线丛扭曲。因此 $g_\beta$ 可用两个在任何几何点都
不同时为零的齐次次数 $d$ 整多项式 $(A_\beta,B_\beta)$ 表示。
$g_\beta(\infty)=\infty$ 使

$$
B_\beta(1,0)=0,\qquad A_\beta(1,0)\in R^\times.
$$

乘一个 $R$ 中的单位后可令 $A_\beta(1,0)=1$。
这一步使用的是 $\infty$ 处真实 rigidification，故即使
$p\mid N\beta$ 也不需要除以 $p$。

在泛纤维，(3.1) 的分子 $xh_\beta^2$ 首一，而与之互素的分母为
$\Psi_\beta^2$。归一化的齐次坐标唯一，故

$$
A_\beta(x,1)=xh_\beta(x)^2,\qquad
B_\beta(x,1)=\Psi_\beta(x)^2.
$$

于是两个平方均在 $R[x]$ 中。$R[x]$ 整闭，
$h_\beta,\Psi_\beta\in\operatorname{Frac}(R[x])$ 又分别满足相应的
首一平方方程，故它们也在 $R[x]$ 中。这证明 (3.4)，并消除了只用
水平除子却未控制竖直素数因子的隐患。

### 3.2 准确乘法式与闭合映射

由 (3.1)–(3.3)，按首项 $\beta$ 选取平方根，得到

$$
\frac{u(\beta z)}{u(z)}=\frac{D_\beta(s)}{H_\beta(s)}.
$$

将其与 (2.3) 合并：

$$
\boxed{\quad
\vartheta(\beta z)=H_\beta(s)\vartheta(z)^d,\qquad
s(\beta z)=s\left(\frac{D_\beta(s)}{H_\beta(s)}\right)^4.
\quad}
\tag{3.5}
$$

这是精确恒等式，原点首项已经排除残余符号、根单位及指数因子。
定义齐次化

$$
\mathcal H_\beta=a^mH_\beta(b/a),\qquad
\mathcal D_\beta=a^mD_\beta(b/a).
$$

则所需的真实多项式映射为

$$
\boxed{\quad
F_\beta(a,b)=
\bigl(a\mathcal H_\beta(a,b)^4,\,
      b\mathcal D_\beta(a,b)^4\bigr).
\quad}
\tag{3.6}
$$

它在 $R$ 上齐次次数 $1+4m=d$，并满足 (1.3)。

## 4. 最小偶范数与两个明确的非实例子

令 $\lambda=1+i$。此时不能把 sigma 的未平方除法式当成椭圆函数。
准确式是

$$
\left(\frac{\sigma(\lambda z)}{\sigma(z)^2}\right)^2=2ix(z).
\tag{4.1}
$$

其证明为：平方的除子等于 $2(T)-2(O)=\operatorname{div}x$，
而首项是 $\lambda^2z^{-2}=2iz^{-2}$；也可直接由 sigma 加法式得到。
加法公式同时给

$$
x([\lambda]P)=\frac{x^2-1}{2ix}.
$$

所以对同一个 $(a,b)$，

$$
\boxed{\quad
F_{1+i}(a,b)=\bigl((a-b)^2,-4ab\bigr).
\quad}
\tag{4.2}
$$

这里第二坐标为 $\sigma(\lambda z)^4=-4x^2\sigma(z)^8$；
再乘 $x([\lambda]P)^2$ 得第一坐标。这同时核准了符号。
其平方准确为 R167 的

$$
F_{1+i}^{\circ2}
=\bigl((a+b)^4,16ab(a-b)^2\bigr)=F_2,
\tag{4.3}
$$

因为 $(1+i)^2=2i$ 而 $i^4=1$。

任意非零 $\beta$ 可写为 $(1+i)^e\gamma$，其中 $N\gamma$ 奇。
用 (4.2) 与 (3.6) 组合即得所有 $\beta$ 的 (1.3) 及整性。
$\gamma(w)$ 的 Zariski 稠密性又使沿它成立的组合公式成为平面
多项式恒等式，证明 (1.4)。

两组小的准确多项式为

$$
\begin{array}{c|c|c}
\beta&D_\beta(s)&H_\beta(s)\\ \hline
2+i&(2+i)-is&1+(-1+2i)s\\
3+2i&(3+2i)+(7-4i)s+(-11+10i)s^2+s^3&
1+(-11+10i)s+(7-4i)s^2+(3+2i)s^3 .
\end{array}
\tag{4.4}
$$

$D_\beta$ 可由上述旧 CM 除法笔记的两个 Laurent 计算取 $17=1$
得到。为独立固定 $H_\beta$ 的常数及方向，也可用

$$
\log\vartheta(z)=\frac{w}{12}-\frac{w^2}{280}
 +\frac{w^3}{4950}+O(w^4),\qquad
s=w-\frac25w^2+\frac7{75}w^3+O(w^4).
\tag{4.5}
$$

将 $\exp(\log\vartheta(\beta z)-d\log\vartheta(z))$ 写成 $s$ 的多项式，
分别匹配至次数一或三；(3.2) 已给准确次数界，所以这些匹配确定
整个多项式，而不只是近似式。

## 5. 真实切向、横向与同一图形递推

由齐次性及 $F_\beta(1,0)=(1,0)$，Jacobian 第一列为 $(d,0)$。
第二坐标含因子 $b$。对 (1.3) 在 $w=0$ 求导，利用 (1.2)，即得
(1.5)。特别切向量 $(1/3,1)$ 的特征值为 $\beta^4$，横向协向量
$(3,-1)$ 的特征值为 $d$。
$(\beta^4-d)/3$ 确在 $\mathbb Z[i]$ 中，因为在 $\mathbb F_9$ 中
$\beta^3=\bar\beta$。

写实际图形

$$
a=f(b)=1+\sum_{k\ge1}c_kb^k,\qquad c_1=1/3.
$$

令 $f_{<k}=1+\sum_{i<k}c_ib^i$，并定义

$$
\mathcal R_{\beta,k}
=[b^k]\left\{
F_{\beta,1}(f_{<k}(b),b)
-f_{<k}\bigl(F_{\beta,2}(f_{<k}(b),b)\bigr)
\right\}.
\tag{5.1}
$$

它属于 $R[c_1,\ldots,c_{k-1}]$，且准确递推为

$$
\boxed{\quad
(\beta^{4k}-N\beta)c_k=\mathcal R_{\beta,k}.
\quad}
\tag{5.2}
$$

证明与 R167 同一：左侧未知 $c_k$ 的线性贡献为 $N\beta$；
右侧外层 $f$ 的贡献为 $(\beta^4)^k$。因为
$F_{\beta,2}$ 含因子 $b$，其自身第 $k$ 次变化不含 $c_k$。
因此没有遗漏低阶系数、阶乘或与 $\beta$ 有关的指数修正。
不同 $\beta$ 给不同的真实分子 $\mathcal R_{\beta,k}$，不能将它们
擅自视作同一个数。

## 6. 惰性共同共振由 p 级间距稀疏到 p² 级间距

固定 $p\equiv3\pmod4$、$p\ge7$，在未分歧二次扩张
$K_p=\mathbb Q_p(i)$ 中归一化 $v_p(p)=1$。置

$$
r=(p+1)/4,\qquad R_p=(p^2-1)/4=r(p-1).
$$

模 $p$ 时 $\bar\beta=\beta^p$。当 $p\nmid N\beta$，
(5.2) 的分母模 $p$ 为

$$
\beta^{4k}-\beta^{p+1}.
$$

奇范数 Gaussian 整数的模 $p$ 剩余类遍历 $\mathbb F_{p^2}^\times$：
这是模 $p$ 与模 $2$ 的中国剩余定理。因此全部这类分母同时被 $p$
除，当且仅当

$$
p^2-1\mid4k-p-1.
$$

准确共同共振集合为

$$
\boxed{\quad k\equiv r\pmod{R_p}.\quad}
\tag{6.1}
$$

第一项为 $r$，第二项为 $r+R_p=pr$。整数倍乘 R167 的
$k\equiv r\pmod{(p-1)/2}$ 只是较大的候选集合；非实 CM 的实际
闭合映射排除了其中绝大部分分母共振。

更强地，全部 Gaussian 乘子的最佳估值准确为

$$
\boxed{\quad
\min_{\beta\in\mathbb Z[i],\ p\nmid N\beta}
v_p(\beta^{4k}-N\beta)
=
\begin{cases}
0,&k\not\equiv r\pmod{R_p},\\
1,&k\equiv r\pmod{R_p}.
\end{cases}
\quad}
\tag{6.2}
$$

非共振时已由循环群给出估值零。共振时所有估值至少一，而两个
奇范数的实际乘子

$$
\beta_1=1+2p,\qquad \beta_2=1+2ip
$$

满足

$$
\begin{aligned}
\beta_1^{4k}-N\beta_1&\equiv2p(4k-2)\pmod{p^2},\\
\beta_2^{4k}-N\beta_2&\equiv8kip\pmod{p^2}.
\end{aligned}
\tag{6.3}
$$

奇素数不可能同时除 $4k-2$ 与 $4k$，故其中至少一个估值恰为一。
这说明整数乘子最优式中的额外 $v_p(4k-2)$ 确被 CM 的第二方向
消除。此处用的仍是准确图形递推，不是自由的对数模型。

甚至每个 $p$ 只需三张实际多项式映射：选一个奇范数 $\beta_p$
使其模 $p$ 为 $\mathbb F_{p^2}^\times$ 的本原元，则它处理全部
非共振 $k$；(6.3) 的两张映射处理全部共振 $k$。可将
$N\beta_p=O(p^2)$，另两者也为 $O(p^2)$。
这些是随 $p$ 选取的整映射；其次数成本没有因此消失。

## 7. 全阶系数依赖与保留的旧分母

固定 $p$，令

$$
\mathcal S_p=\{r+hR_p:h\ge0\}.
$$

对所有 $k\ge1$，(5.2)–(6.2) 给出实际有限递推：

$$
c_k\in\mathcal O_{K_p}
 [\,c_m:m\le k,\ m\in\mathcal S_p\,].
\tag{7.1}
$$

而在 $k\in\mathcal S_p$ 时有更具体的

$$
pc_k\in\mathcal O_{K_p}[c_1,\ldots,c_{k-1}].
\tag{7.2}
$$

(7.1) 的含义是：每个非共振系数都由先前的真实共振系数通过整
多项式表达；不声称这些共振系数代数独立，也不声称它们可自由指定。
(7.2) 只除一次 $p$，并不抹掉右侧先前已经出现的分母。

可以保留有用的次数信息：给变量 $c_m$ 赋权 $m$，则 (7.1) 可取为
加权次数至多 $k$ 的多项式。事实上，(5.1) 每个系数单项式的
总指标至多 $k$；对嵌套部分，外层的 $c_i$ 与内层必有的 $b^i$
正好给相同的指标预算。逐阶代入保持此性质。

因此在第二个共振之前，

$$
c_k\in\mathcal O_{K_p}[c_r],\qquad
\deg_{c_r}\le\lfloor k/r\rfloor
\quad(1\le k<pr).
\tag{7.3}
$$

R167 的首极计算给

$$
v_p(c_r)=-1,\qquad
pc_r\equiv C_p/(17r)\pmod p,\qquad
C_p=p[s^{r-1}]W'(s)\not\equiv0\pmod p.
$$

所以 (7.3) 包含全段的真实估值下界

$$
v_p(c_k)\ge-\lfloor k/r\rfloor\qquad(k<pr).
\tag{7.4}
$$

在 $k=pr$ 已进入新的共振，(7.3) 的单变量结论不能越过该边界。
R160 的首个 $p$ 倍相位 carry 正好位于相同的 $pr$ 位置，
与这里的精确 CM 共振相容；二者不能互相替代未付的更高分子计算。

## 8. 真实源格及下一步的准确范围

对同一个平面源 $E_D^{ab}=R[a,b]_{\le D}$，已证明的实际拉回为

$$
F_\beta^*:E_D^{ab}\longrightarrow E_{(N\beta)D}^{ab}.
\tag{8.1}
$$

在每个奇素数处它是整算子。若再有 $p\nmid N\beta$，则它还是
**等距饱和嵌入**。证明如下：由 (1.5)，$F_\beta$ 的约化在
$(1,0)$ 的 Jacobian 可逆，因而该约化映射为 dominant，
在剩余域多项式环上的 pullback 单射。于是任何 primitive 源
多项式的 pullback 仍 primitive，给出 Gauss 系数范数的相等。
若 $pH=F_\beta^*P$，模 $p$ 单射又迫 $P=pP_1$，从而
$H=F_\beta^*P_1$；逐次使用即得像格饱和。

令 $S_{D,k}$ 为 $E_D^{ab}\otimes\mathcal O_{K_p}$ 中沿真实
$\gamma(w)$ 消失到次数至少 $k$ 的子格。准确恒等式 (1.3) 给

$$
F_\beta^*S_{D,k}
=F_\beta^*E_D^{ab}\cap S_{(N\beta)D,k},\qquad
[w^k](F_\beta^*P)(\gamma(w))
=\beta^{4k}[w^k]P(\gamma(w)).
\tag{8.2}
$$

因此原源的全部准确前缀及其第一个非零 jet，与扩大源中的这个
饱和像子格完全等距。单次 pullback 自身没有降低这些 jet 范数；
扩大源中的其他列和多张映射的联合消元仍需另行分析。

这里还需区分有限次数源与局部完成。写 $X=a-1$，
$\mathfrak m=(X,b)$。同一个 Jacobian 单位确使 $F_\beta^*$ 在
$\mathcal O_{K_p}[[X,b]]$ 及每个
$\mathcal O_{K_p}[[X,b]]/\mathfrak m^{q+1}$ 上为整可逆映射。
但取次数 $D$ 的代表只保留模 $\mathfrak m^{D+1}$，沿 $\gamma$
仅能统一保证到 $w^D$ 的输出；例如被丢弃的 $b^{D+1}$ 的阶数
准确为 $D+1$。若仅依靠这种一般局部截断来保持第 $k$ 阶行，
要取模 $\mathfrak m^{k+1}$、即次数至多 $k$ 的代表。
在斜率方法的 $D\asymp\sqrt{k}$ 区间，不能把这个更大的局部
GL 作用当成原 $E_D^{ab}$ 上免费可逆的源变换。这不排除某个
经过实际证明的多图共同前缀构造。

将 $\mathbb Z_p$ 格扩到未分歧的 $\mathcal O_{K_p}$ 保持 Smith
指数及饱和前缀范数；图形的 $c_k$ 本身仍为有理数。这使上述
CM 递推可用于原来的有理 jet 格，但不提供反向次数比较。

尚未证明的是：利用这些非线性整递推及实际的两条中央失败条件，
对每个 $D,k$ 同时控制整个

$$
\ker\!\left(E_D^{ab}\longrightarrow
 \mathbb Q_p[[b]]/(b^k)\right)
\ \xrightarrow{\ [b^k]\ }\ \mathbb Q_p
\tag{8.3}
$$

的像理想，取得 R159 所需的严格总预算。逐个 $c_k$ 的 (7.4)、
单个最优分母的 (6.2)，以及源次数增长 (8.1)，都不能单独替代
(8.3) 的共同饱和消元。

最后，(6.1) 的来源是 $\beta^{4k}-N\beta$，而不是
$\beta^k-1$。R41 的两个未扭曲乘子共同深度求和不能直接代入。
所有惰性素数的首共振 $r$ 仍然存在，且其真实首极已经由上式证明
非零。

## 来源与依赖

- [DLMF 23.2.7–8、23.2.17](https://dlmf.nist.gov/23.2)：
  固定 sigma、zeta 关系及准周期公式；(2.2) 的 CM 反线性与全部整
  模型论证在本文给出。
- [较早的非实 CM sigma 除法证明](2026-11-12-cm-sigma-division-and-common-resonance.md)：
  $\Psi_{2+i}$、$\Psi_{3+2i}$ 的 Laurent 与群律双重证书及
  $[1+i]$ 的平方公式。本文在 $E_0$ 规范下重新固定 theta 乘法式。
- [R166 完整 theta 除法与 Frobenius](2026-11-12-actual-theta-division-frobenius-and-full-ghosts.md)、
  [R167 真实平面与整倍乘](2026-11-12-closed-theta-sigma-plane-and-integral-dynamics.md)：
  实际平面、源比较及第一共振系数。
- [R163 全阶相位赋值](2026-11-12-actual-theta-inert-valuation-and-even-power-jet-resonance.md)、
  [R160 首 carry](2026-11-12-inert-theta-carry-and-common-degree-spectrum.md)：
  与 $pr$ 边界的相容性；没有把有限 carry 结论外推到全部前缀。
