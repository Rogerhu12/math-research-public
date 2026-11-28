# 原 Gaussian 两位 Lucas 分解与指定 Hurwitz 高窗

**状态：已证明的有限系数 reduction；未证明所读系数非零。** 日期：2026-11-28 Asia/Taipei。

本工作稿沿 R1168 的同一 Gaussian 模型、同一微分和
Hurwitz–Eisenstein 归一，把其实际四次、八次矩中
$p^2$ 窗口的系数降到安全低块及次数至多五的明确
$p$-sections。唯一可抵分母的 Lucas carry 及首次不整边界
全部保留。它不是把 R1161 的 $\le p-3$ 反射延伸到高权。

## 1. 原逆椭圆积分与有限范围

设
$$
p=4h+3\ge41,\qquad e=p^2-1,\qquad
J=e/4,\qquad m=(p-1)/2=2h+1,\qquad r_0=3h+2.
$$
原模型为 $y^2=x^3+ax$，$a\in\mathbb Z_p^\times$，
其还原仍记为 $a\in\mathbb F_p^\times$。
取 $\omega=dx/(2y)$，原点处选
$$
u=x^{-1/2},\qquad
y=-u^{-3}(1+au^4)^{1/2}.
$$
于是 $\omega=(1+au^4)^{-1/2}du$。
特征零 formal logarithm $v=\int\omega$ 因而准确写为
$$
v=u\,\mathsf F(u^4),\qquad
\mathsf R(T)=(1+aT)^{-1/2}
 =\sum_{j\ge0}R_jT^j,
$$
$$
R_j=\frac{(-a)^j}{4^j}\binom{2j}{j},
\qquad
\mathsf F(T)=\sum_{j\ge0}\frac{R_j}{4j+1}T^j .
\tag{G2.1}
$$
这里 $u$ 是本节的逆 $x$ 参数，不是 R1168 的
未分歧 normal 变量 $u=z^e$。

沿原 relative Cartier，
$$
\beta=b_E=[x^{p-2}](x^3+ax)^m
 =\binom{m}{h}a^{h+1}\in\mathbb F_p^\times .
\tag{G2.2}
$$
特别 $\beta=-\delta$，没有另选 period 或单位尺度。
以下先证明 $\mathsf F$ 的所有次数 $<J$ 的系数均 $p$ 整，
再在这个范围内还原。边界 $J$ 另行处理。

## 2. 唯一能抵消分母的 Lucas carry

写 $j=\ell p+r$，$0\le r<p$、$j<J$。
则 $\ell\le h$；若 $r=r_0$，必有 $\ell<h$。
因为 $2\ell+1<p$，中央二项式只可能有一处低位 carry。

若 $0\le r\le m$，没有 carry，且 $p\nmid4r+1$。
Lucas 身份及 $a^p=a$ 给
$$
\frac{R_{\ell p+r}}{4(\ell p+r)+1}
 \equiv R_\ell\,\frac{R_r}{4r+1}\pmod p .
\tag{G2.3}
$$
若 $m<r<p$ 且 $r\ne r_0$，
中央二项式被 $p$ 整除，但分母是单位，所以该系数为零。

剩余且唯一的情形是 $r=r_0$。
此时 $4r_0+1=3p$，完整分母是
$p(4\ell+3)$，而 $4\ell+3<p$。
将各阶乘中的 $p$ 因子逐项提出，得到
$$
\frac1p\binom{2(\ell p+r_0)}{\ell p+r_0}
 \equiv
 -\frac{(2\ell+1)!}{(\ell!)^2}\,
  \frac{(2r_0-p)!}{(r_0!)^2}\pmod p .
\tag{G2.4}
$$
这里 $2r_0-p=m$。
负号来自 numerator 比两个 denominator 多一组
$1,\ldots,p-1$，不能丢掉。

定义实际常数
$$
C=-\left(\frac{-a}{4}\right)^{r_0}
       \frac{m!}{(r_0!)^2}.
$$
于是唯一 carry 系数为
$$
\boxed{\qquad
\frac{R_{\ell p+r_0}}{4(\ell p+r_0)+1}
 \equiv C\,\frac{2\ell+1}{4\ell+3}R_\ell,
\qquad 0\le\ell<h.
\qquad}
\tag{G2.5}
$$
所有 $j<J$ 的系数由 (G2.3)–(G2.5) 覆盖，
故均为 $p$ 整。

常数 $C$ 能在原 $\beta$ 尺度中完全化简。
Wilson 给
$r_0!h!=(-1)^{h+1}$、$(m!)^2=1$；
原 $p\equiv3\bmod4$ 的二次补充律给
$(-4)^h=-1/2$，故 $(-1/4)^{r_0}=-1/2$。
结合 (G2.2)，准确得到
$$
\boxed{\qquad \beta C=2a,\qquad C=\frac{2a}{\beta}.\qquad}
\tag{G2.6}
$$
例如化简中 $h+1\equiv1/4$，而
$a^{r_0+h+1}=a^p=a$。
这个计算只除原 Cartier 单位与安全阶乘；
不除任何 Bernoulli 数。

## 3. 原级数的完整低块分解及首个不整边界

定义下列实际低块：
$$
\begin{aligned}
F_{\rm lo}(T)&=\sum_{r=0}^{m}\frac{R_r}{4r+1}T^r,\\
R_h(T)&=\sum_{\ell=0}^{h}R_\ell T^\ell,\qquad
F_h(T)=\sum_{\ell=0}^{h}\frac{R_\ell}{4\ell+1}T^\ell,\\
S_{h-1}(T)&=\sum_{\ell=0}^{h-1}
            \frac{(2\ell+1)R_\ell}{4\ell+3}T^\ell .
\end{aligned}
\tag{G2.7}
$$
所有显示分母均为 $p$ 单位。
若沿旧原式记
$\mathsf G(T)=3\sum_{\ell\ge0}R_\ell T^\ell/(4\ell+3)$，
则在 $\ell<h$ 的安全范围内
$S=(\mathsf R-\mathsf G/3)/2$；
这只是同一旧积分的身份，不删除 $\mathsf G$ 项。

在 $\mathbb F_p[T]/(T^J)$ 中，(G2.3)–(G2.6) 给出
$$
\boxed{
\mathsf F(T)
 =F_{\rm lo}(T)\,R_h(T^p)
   +\frac{2a}{\beta}\,T^{r_0}S_{h-1}(T^p).
}
\tag{G2.8}
$$
右边按 $T^J$ 截断。
尤其不能只用无 carry 的第一个乘积。
最高的 $S$ 指数只需 $h-1$，故没有读取
$4h+3=p$ 的未付分母。

同一计算还准确决定首次不整边界。
$J=hp+r_0$、$4J+1=p^2$；
(G2.4) 仍只给一个 binomial 的 $p$ 因子。
又由同一 Wilson 化简，$R_h=\beta/a$（此处 $R_h$ 指
(G2.1) 的第 $h$ 个系数）。因此
$$
\boxed{
p\,[T^J]\mathsf F(T)
 \equiv C(2h+1)R_h=-1\pmod p.
}
\tag{G2.9}
$$
所以 $v(u)$ 的首个不整系数恰在 $u^{p^2}$，
其 $p$ 倍还原为 $-1$。
这与原 $\varpi^{p^2-1}=p$ 的高度二尺度相合；
本节并不把该边界项作为可直接约化的整系数。
全部后继读取都严格小于 $J$。

## 4. R1168 的全部 Gaussian 高窗降到这些原低块

原 Hurwitz 归一为
$$
x(v)=v^{-2}+\sum_{\substack{M\ge4\\M\ {\rm even}}}
                  (M-1)G_M\,v^{M-2}.
$$
对 $M\equiv0\bmod4$，特征零 Laurent Lagrange 公式准确给
$$
\boxed{
G_M=-\frac{2}{(M-1)(M-2)}
       [T^{M/4}]\mathsf F(T)^{\,2-M}.
}
\tag{G2.10}
$$
它来自
$[v^{M-2}]u(v)^{-2}
 =-2[T^{M/4}]\mathsf F^{2-M}/(M-2)$。
没有另乘一个第四根换元次数。

现在取原 R1168 的
$$
d\in\{4,8\},\qquad i\in\{0,2,\ldots,d\},\qquad
M_{d,i}=e-pd+(p-1)i .
$$
这些权都为四的倍数，且 $M_{d,i}<e$。
此外
$$
M_{d,i}\equiv-(i+1)\pmod p,
$$
所以 $(M_{d,i}-1)(M_{d,i}-2)\equiv(i+2)(i+3)$ 是单位。
(G2.10) 因而也独立支付这些 $G_{M_{d,i}}$ 的整性。

关键指数身份是
$$
2-M_{d,i}=(i+3)+p(d-i)-p^2.
$$
在 (G2.8) 的真实有限环中，
$\mathsf F(T)^{p^2}=\mathsf F(T^{p^2})=1$。
因此完整指数准确化为
$$
\mathsf F(T)^{2-M_{d,i}}
 =\mathsf F(T)^{i+3}\,F_h(T^p)^{d-i}
       \pmod{T^J}.
$$
把 (G2.8) 代入，得到全部原高窗的有限读式
$$
\boxed{
G_{M_{d,i}}\equiv
-\frac{2}{(i+2)(i+3)}
[T^{M_{d,i}/4}]
 \left(F_{\rm lo}(T)R_h(T^p)
       +\frac{2a}{\beta}T^{r_0}S_{h-1}(T^p)\right)^{i+3}
 F_h(T^p)^{d-i}\pmod p .
}
\tag{G2.11}
$$
这里 $\mathsf F(T^{p^2})^{-1}$ 被删除的理由是其首个
非常数项超出整个指定窗口，而不是近似改动负指数。
最高外幂 $i+3$ 为十一，原 $a,\beta$ 均保持。

### 4.1. 只需次数至多五的明确 $p$-section

为使 (G2.11) 的输入大小完全明确，
对任意实际多项式 $H(T)$ 及 $0\le r<p$ 定义
$$
\operatorname{Sec}_rH(Z)
 =\sum_{b\ge0}[T^{pb+r}]H(T)\,Z^b.
$$
对 $0\le\ell\le i+3$，写
$$
M_{d,i}/4-\ell r_0=pq_\ell+r_\ell,\qquad 0\le r_\ell<p;
$$
若左边为负，该项按零。
则 (G2.11) 等价于
$$
\boxed{
\begin{aligned}
G_{M_{d,i}}\equiv
-\frac{2}{(i+2)(i+3)}
 \sum_{\ell=0}^{i+3}\binom{i+3}{\ell}
   \left(\frac{2a}{\beta}\right)^\ell
 [Z^{q_\ell}]\,\bigl(
 &\operatorname{Sec}_{r_\ell}
           (F_{\rm lo}^{\,i+3-\ell})(Z)\\
 {}\cdot{}&
 R_h(Z)^{i+3-\ell}S_{h-1}(Z)^\ell F_h(Z)^{d-i}
 \bigr).
\end{aligned}}
\tag{G2.12}
$$
因 $\deg F_{\rm lo}=m$，其中每个 section 的次数至多
$\lfloor11m/p\rfloor\le5$。
又 $q_\ell\le h$，而 $\ell\ge1$ 时 $q_\ell\le h-1$。
所以右边最多十二项，只使用
(G2.7) 的安全低块和这些明确的次数至多五的多项式，
最后只读至 $Z^h$。
没有隐藏一个新的 $p^2$ 长度级数或不安全的 $S_h$。

## 5. 首个 Gaussian 读数的完整示例及余项边界

令
$$
A_3=[T^{r_0}]F_{\rm lo}(T)^3,\qquad C=2a/\beta.
$$
对 $d=4,i=0$，写 $R,F,S$ 为 (G2.7) 的安全低块。
(G2.12) 的四个 $\ell$ 项中，最后一项确为零：
其 section residue 为 $2h+2\ne0$，而被读取多项式是 $1$。
其余三项准确给
$$
\boxed{
\begin{aligned}
G_{p^2-4p-1}\equiv-\frac13\bigg\{&
 A_3[Z^{h-1}]R^3F^4
 +3C[Z^{h-1}]R^2SF^4\\
 &+3C^2\frac{R_{h+1}}{4h+5}
           [Z^{h-2}]RS^2F^4
 \bigg\}\pmod p .
\end{aligned}}
\tag{G2.13}
$$
这里 $R_{h+1}$ 是 (G2.1) 的原系数，
$4h+5\equiv2\bmod p$。
没有把 $A_3$ 或后两个实际乘积设为零。

这个 section 也有一个准确的中间权来源。
在 $r_0<p$ 范围，(G2.8) 只有
$[T^{r_0}]\mathsf F=C/3$ 这一 carry，
所以 $[T^{r_0}]\mathsf F^3=A_3+C$。
将 (G2.10) 用于 $M=3p-1$，得到
$$
\boxed{\qquad
A_3+C=-3G_{3p-1}\pmod p .
\qquad}
\tag{G2.14}
$$
这个中间权系数也是原 Hurwitz 系数，且在本次积分窗口内整；
并没有证明它等于某个旧低权系数或为零。
特别不能把 (G2.13) 简写成只保第一项，
也不能先以 $A_3=-C$ 代入。

## 6. 对原任务的准确范围

R1168 (1168.25)、(1168.28)–(1168.29) 的原矩系数，
现在可以直接逐项代入 (G2.11) 或 (G2.12)，
保其 $\binom di\beta^i/(i+1)$、
$\omega^i\eta^{d-i}$ 和 actual Fontaine–Laffaille frame。
这只减少实际 Hurwitz 读取的有限输入，
不改变原矩、root convention、tame trace 或 PD gauge。

本稿没有从低块每个分母为单位推出其和非零；
没有把 (G2.14) 的中间权反射猜成 R1161 的旧反射；
也没有把这些新系数并入原 abelian good mask。
原两点分离仍要控制 R1161 的指定 residue 或完整 weighted
joint 条件。所有上述恒等式均为纸面证明，无数学程序执行。


## 7. 同一 carry 的原超奇异 primitive 身份与换元边界

本节进一步把 (G2.8) 的两个低块接到原
$\Psi=D^{p-2}x$，其中 $D=\omega^{-1}d$。
原 supersingular 规范给
$D\Psi=-\beta=\delta$，且 $\Psi$ 仅在 $O$ 有 $p$ 阶极，
其 $u^{-p}$ 首项为一。
以下所有函数仍在同一个 Gaussian 曲线上；
没有用另一个至多相差单位的 primitive。

### 7.1. 真实有理 primitive 及其二挠点补偿

在特征 $p$ 置
$$
\mathcal L
 =uF_{\rm lo}(u^4)\mathsf R(u^4)^p
 =-\frac{x^{(3p-1)/2}F_{\rm lo}(x^{-2})}{y^p}.
\tag{G2.15}
$$
右式表明它确下降到原椭圆曲线函数域。
因为
$$
\frac d{du}\bigl(uF_{\rm lo}(u^4)\bigr)
 =(1+au^4)^m,
\qquad
\mathsf R(u^4)^p(1+au^4)^m=\mathsf R(u^4),
$$
准确有 $D\mathcal L=1$。

定义 $\mathcal H=-\beta\mathcal L-(x^2/y)^p$。
则 $D\mathcal H=-\beta$。
它除 $O$ 和二挠点外没有极，各二挠点的极阶至多 $p$。
在 $(0,0)$，分子最低 $x$ 次数为 $(p+1)/2$，
故除以 $y^p$ 后正则。
在另外两个二挠点 $x_T^2=-a$，
分子的常数由下面完整有限 beta 和消去：
$$
\begin{aligned}
F_{\rm lo}(-1/a)
 &=\sum_{r=0}^m\frac{(-1)^r\binom mr}{4r+1}
 =\frac{m!\,h!}{4r_0!},\\
\beta F_{\rm lo}(-1/a)&=(-a)^{h+1}.
\end{aligned}
\tag{G2.16}
$$
第一式使用
$\sum(-1)^r\binom mr/(z+r)=m!/(z)_{m+1}$，
这里 $z=1/4=h+1$，全部因子小于 $p$。
第二式由与 (G2.6) 相同的 Wilson 身份得到。

于是 $\mathcal H$ 在这两个点的 $p$ 阶极系数为零。
因其导数全纯，任何剩余的 $1,\ldots,p-1$ 阶极都会
给出不可消的导数极，所以这些点也正则。
在 $O$，$\mathcal H$ 的首项为 $u^{-p}$，极阶至多 $p$；
它关于 $[-1]$ 为奇。
与同一原 $\Psi$ 相减后，导数为零、仅在 $O$ 有至多 $p$ 阶极，
故差是一个至多有一阶极的函数的 $p$ 次方。
椭圆曲线不存在非恒定的一阶极函数，奇性又排掉常数。
因此是全函数域的准确身份
$$
\boxed{\qquad
\beta\mathcal L=-\Psi-\left(\frac{x^2}{y}\right)^p .
\qquad}
\tag{G2.17}
$$
这里的 $(x^2/y)^p$ 是付清二挠点极的实际补偿，不能丢掉。

### 7.2. 在逆 $x$ 参数中的完整低权 Frobenius 项

令原 Weierstrass $\zeta$ 沿同一 logarithm $v$ 满足
$\zeta(v)=v^{-1}-\sum_{j\ge4}G_jv^{j-1}$。
直接积分 $d\zeta/dv=-x$，或沿原 Gaussian 加法式，可得
$$
\zeta(v(u))
 =\frac1{u\mathsf R(u^4)}
       -\frac a3u^3\mathsf G(u^4).
$$
因 $x^2/y=-u^{-1}\mathsf R(u^4)$，
在 $u$ 次数 $<p$ 的安全范围准确有
$$
\boxed{\qquad
2au^3S(u^4)=\zeta(v(u))+\frac{x^2}{y}.
\qquad}
\tag{G2.18}
$$
这里 $S$ 只读 (G2.7) 中的 $\ell<h$；
首个未付的 $\mathsf G$ 分母恰在 $u^p$，未被使用。

记 $\zeta^{<p}_u$ 为 $\zeta(v(u))$ 的 Laurent 前缀，
保 $u^{-1}$ 及所有次数严格小于 $p$ 的项。
它的系数都是 $p$ 整，且来自原 $G_4,\ldots,G_{p-3}$
及同一安全换元。
将 (G2.18)、$C=2a/\beta$ 代入 (G2.8)，再用 (G2.17)，得到
$$
\boxed{\qquad
\Psi(E(u))
 =\bigl(\zeta^{<p}_u\bigr)^p-\beta\,v(u)
       \pmod{u^{p^2}} .
\qquad}
\tag{G2.19}
$$
本式先在已付的整系数前缀还原后成立；
其中 $v(u)$ 只取次数 $<p^2$。
$\zeta^{<p}_u$ 的负首项和 $(x^2/y)^p$ 的负首项确切抵消，
不是额外添加一个全纯函数。

### 7.3. 换回 logarithm 时必须缩小的范围

不能把 (G2.19) 的 modulus 原样搬到 characteristic-zero
logarithm 参数 $v$。
由 (G2.9)，逆换元 $u(v)$ 首个可能不整的项在 $v^{p^2}$，
其系数有一个 $p$ 分母。
而 $\Psi$ 在 $O$ 有 $p$ 阶极：
将这个项代入 $u^{-p}$，可能已经影响
$v^{p^2-p-1}$。
所以本节只在严格更低的范围作 reduction。

在该范围，各整 Laurent 前缀的换元均可约化，
负 $p$ 首项的上述边界尚未进入；
将 $\zeta^{<p}_u$ 换回同一 $v$，
其 $p$ 次方只需原权 $\le p-3$ 的安全项。
因而实际得到
$$
\boxed{
\Psi(E(v))
 \equiv v^{-p}-\beta v
     -\sum_{\substack{4\le r\le p-3\\4\mid r}}
                  G_r^{\,p}v^{p(r-1)}
 \quad\text{在所有次数 }<p^2-p-1 .
}
\tag{G2.20}
$$
左边取原整多项式 $D^{p-2}x$ 的 characteristic-zero lift
后作同一 logarithm 读取；
在这个严格范围内，它与 (G2.19) 的 reduction 相容。
保持同一极阶至多 $p$ 的不同整 lift，其 $p$ 倍差也尚不能在此范围贡献：
其极阶至多 $p$，首个可能由不整换元抵消的 $p$ 因子
同样不早于 $p^2-p-1$。

这是一条带明确极点损失的桥。
不能在未补精度时将它乘上 $\Psi$ 的高幂，
也不能把右端的低精度相等用于更高 pole 的乘积。

### 7.4. 此桥实际读到的高权系数

因为在 characteristic zero 中
$\Psi(E(v))=(d/dv)^{p-2}x(v)$，
可以在 (G2.20) 的安全范围直接比较系数。
当 $M=pr$ 时，下降乘积与 $(M-1)$ 合成 $-1$，
故
$$
\boxed{\qquad
G_{pr}\equiv G_r^p=G_r\pmod p,
\qquad 4\mid r,\quad 4\le r\le p-3.
\qquad}
\tag{G2.21}
$$
这里 $G_{pr}$ 整，因为 $pr-1$ 是单位且相应的
$x(v)$ 系数仍在首个不整边界前。
最大被读次数为 $p^2-4p<p^2-p-1$。

当 $M=pr+1$ 时，下降乘积与原系数合成 $-rpG_M$。
相应 $pG_M$ 整，且 (G2.20) 的非 $p$ 倍指数项只有 $-\beta v$。
因此
$$
\boxed{
pG_{p+1}\equiv\beta,\qquad
pG_{pr+1}\equiv0
\quad(1<r\le p-2,\ r\equiv1\bmod4).
}
\tag{G2.22}
$$
这里 $r$ 为单位，最大被读次数为 $p^2-3p+1$，
同样未到边界。
其它 Gaussian 不允许的权原本为零，不据本式增加观测。

(G2.21)–(G2.22) 只覆盖显示的两个指数类别。
R1168 的 $M_{d,i}\equiv-(i+1)\bmod p$ 一般不在其中，
所以仍须保 (G2.11)–(G2.14) 的实际 section 和完整乘积。
本节固定了原 $\Psi$、低权 $\zeta$ 与新两位 carry 的同源关系，
没有由此宣称任一原 joint minor 或最高中央项为单位。


## 8. 原二次 primitive 给出中间权单位，并将首个高矩接回 $\mathcal H_p$

本节在 §§5、7 的同一原模型上进一步读取；所有等式在
$\mathbf F_p$ 中，写 $G_M$ 时指上述整 Hurwitz 系数的 reduction。
原 $\beta=-\delta\ne0$ 不改尺度。
令
$$
\mathcal R=D^{p-3}x,\qquad D\mathcal R=\Psi,\qquad D\Psi=-\beta.
$$
则有完整函数域身份
$$
\boxed{\qquad \Psi^2+2\beta\mathcal R=x^p.\qquad}
\tag{G2.23}
$$

### 8.1. 二次身份及安全的 $v^{2p}$ 读取

左边的 $D$-导数为零，且仅在 $O$ 有至多 $2p$ 阶极。
在完美常数域上它是一个函数的 $p$ 次方，其根属于
$L(2O)=\langle1,x\rangle$。
原 $\Psi$ 的首项 $v^{-p}$ 把 $x^p$ 的系数固定为一。
在原 Gaussian $\mu_4$ 作用下，
$\Psi\mapsto i\Psi$、$\mathcal R\mapsto-\mathcal R$、
$x\mapsto-x$，所以常数项必须为零。这证明 (G2.23)，
没有另选 primitive 的常数。

把 (G2.20) 用于这一次平方时，误差范围必须再减去 $p$：
可能最早影响的次数为 $p^2-2p-1$。
对本篇 $p\ge41$，有
$2p<p^2-2p-1$，所以读取 $v^{2p}$ 合法。
记 $\zeta_{<p}$ 为同一安全低权 Laurent 前缀。
平方中的交叉项
$2\beta v\zeta_{<p}^{\,p}$ 全部指数为 $1\bmod p$，
$\beta^2v^2$ 也不贡献 $v^{2p}$。
因此
$$
[v^{2p}]\mathcal R
 =\frac{\bigl([v^2](x-\zeta_{<p}^{\,2})\bigr)^p}{2\beta}
 =\frac{5G_4}{2\beta}
 =-\frac{a}{6\beta}.
\tag{G2.24}
$$
这里 $x=v^{-2}+3G_4v^2+\cdots$、
$\zeta=v^{-1}-G_4v^3+\cdots$，且原 $G_4=-a/15$；
右边的 $p$ 次方系数等于本身，因为模型和这些系数在
$\mathbf F_p$ 上。

另一方面，直接在 characteristic zero 对原
$\mathcal R=D^{p-3}x$ 读取同一项后约化：
$$
[v^{2p}]\mathcal R
 =(3p-2)(3p-3)_{\underline{p-3}}G_{3p-1}
 \equiv(-2)(p-3)!\,G_{3p-1}=G_{3p-1}.
$$
最后使用 $(p-3)!=-1/2$。这个权仍在 §5 已付整窗口内，
而 $\mathcal R$ 的极阶至多 $p-1$，此次换元没有越过首个不整边界。
于是 (G2.14) 的真实中间权及 section 被准确固定为
$$
\boxed{\qquad
G_{3p-1}=-\frac{a}{6\beta}\ne0,\qquad
A_3=-\frac{3C}{4},\qquad C=\frac{2a}{\beta}.
\qquad}
\tag{G2.25}
$$
特别，不能以 $A_3=-C$ 消掉原三项式；正确值是显示的
$-3C/4$。

### 8.2. 三个真实 section 的完整合并

先由原 binomial 系数直接得到
$$
R_h=\frac{\beta}{a},\qquad
\frac{R_{h+1}}{R_h}
 =-\frac{a(2h+1)}{2(h+1)}=a,\qquad
F_{h+1}=\frac{R_{h+1}}{4h+5}=\frac{\beta}{2}.
$$
因而 $C^2F_{h+1}=aC$。
将这些值和 (G2.25) 代入 (G2.13) 的全部三项，并把最后一项
按 $T$ 移一阶，严格得
$$
G_{p^2-4p-1}
 =C[T^{h-1}]F^4
       \left(\frac{R^3}{4}-R^2S-aTRS^2\right).
\tag{G2.26}
$$
此处 $R,F,S$ 仍指 (G2.7) 的安全低块；
下式只在所需次数 $\le h-1$ 使用它们。

令
$$
Y(T)=\sum_{\ell\ge0}\frac{R_\ell}{4\ell+3}T^\ell
     =\frac13\,{}_2F_1(3/4,1/2;7/4;-aT).
$$
这是原第二类积分的低前缀，不能与曲线的 $y$ 坐标混淆。
由 (G2.7) 的定义，
$S=(R-Y)/2$，且 $R^2(1+aT)=1$。
不删任何乘积的直接化简给
$$
\frac{R^3}{4}-R^2S-aTRS^2
 =-\frac14\left(R-2Y+aTRY^2\right).
\tag{G2.27}
$$

### 8.3. 原 Appell 列与实际第一层矩的精确桥

使用
[R1135 (1135.10)、(1135.13)、(1135.16)](../results/R1135-original-Gaussian-low-row-fiber-constraint.md)
已经固定的同一原对象
$$
C_2(v)=\zeta(v)^2-x(v),\qquad
\mathcal H_p=[v^{p-5}]C_2(v).
$$
在 $T=u^4$、$v=uF(u^4)$、$dv=R(u^4)\,du$ 下，
完整第二类积分是
$$
\zeta(v(u))=\frac{1}{uR(u^4)}-au^3Y(u^4),
$$
故
$$
C_2(v(u))
 =au^2\left(1-2R^{-1}Y+aTY^2\right).
$$
于是 (G2.27) 的括号等于
$-RC_2(v(u))/(4au^2)$。
由于 $4(h-1)+2=p-5$，(G2.26) 成为
$$
G_{p^2-4p-1}
 =-\frac1{2\beta}
       [u^{p-5}]\,F(u^4)^4R(u^4)C_2(v(u)).
\tag{G2.28}
$$

最后一次使用原残数换元，保其 Jacobian：
$$
\begin{aligned}
[v^{p-5}]C_2(v)
 &=\operatorname{Res}_{v=0}C_2(v)v^{-(p-4)}\,dv\\
 &=[u^{p-5}]C_2(v(u))R(u^4)F(u^4)^{4-p}\\
 &=[u^{p-5}]C_2(v(u))R(u^4)F(u^4)^4.
\end{aligned}
$$
最后一步只在次数 $p-5<p$ 的整前缀使用
$F^{-p}\equiv1$；$C_2$ 从 $u^2$ 开始，
所以没有负次项把高 carry 拉回。得到
$$
\boxed{\qquad
G_{p^2-4p-1}=-\frac{\mathcal H_p}{2\beta}
           =\frac{\mathcal H_p}{2\delta}.
\qquad}
\tag{G2.29}
$$

这是 [R1168 (1168.25)、(1168.28)](../results/R1168-original-unramified-PD-contraction-and-CM-moment-readout.md)
原 $d=4$ 矩中 $\eta^4$ 系数的准确读取：
该项原来的 $\binom40\beta^0/(0+1)$ 恰为一，
没有新增 Fontaine–Laffaille frame 单位、Tate 标度或标签反除。

(G2.25) 支付了一个真实中间权单位；(G2.29) 则把一个实际高权矩
接回原首标签的 $\mathcal H_p$，没有证明 $\mathcal H_p$ 非零。
在原共同纤维的 $\mathcal H_p=0$ 分支，这个高权矩系数准确为零。
其它 $i=2,4$ 槽、$d=8$ 矩、原最高中央值及 arithmetic
unsmoothing 均不由此消失，仍须保各自全部乘积和实际 Bernoulli mask。
全部推导为原函数、有限系数与残数的纸面恒等式，无数学程序执行。


## 9. 两个完整 Appell 类别与原八次矩的前两槽

本节只扩展上节已经核准的正 multiple-$p$ 读取。
为避免与原 Kronecker 的 $c_s,d_s$ 混用，写
$$
\mathcal R_j=D^{p-j-1}x\quad(1\le j\le4),
\qquad \mathcal R_1=\Psi,\quad
D\mathcal R_j=\mathcal R_{j-1}\quad(2\le j\le4).
$$
在同一原函数域中有
$$
\boxed{\begin{aligned}
6\beta^2\mathcal R_3
 &=\Psi^3-3x^p\Psi-2y^p,\\
24\beta^3\mathcal R_4
 &=-\Psi^4+6x^p\Psi^2+8y^p\Psi+3x^{2p}
      +\epsilon_{\rm inv},
\qquad \epsilon_{\rm inv}\in\mathbf F_p .
\end{aligned}}
\tag{G2.30}
$$
这里完整保留第二式的常数，未将它认成原 $c_4$ 或设为零。

### 9.1. 三次、四次身份的函数域证明

第一式右边的导数是
$3\beta(x^p-\Psi^2)=6\beta^2\mathcal R_2$。
两边的差因此是 $p$ 次方。
三个最高 $3p$ 阶极的系数分别为 $1,-3,2$，恰相消；
其根属于 $L(2O)$。
差的 $\mu_4$ 角色为 $i^3=-i$，而该空间的 $p$ 次方
只有常数与 $x^p$ 的角色，故差为零。

再对第二式右边的非恒定部分求导，得第一式的
$4\beta$ 倍，恰为 $24\beta^3\mathcal R_3$。
差同样是 $p$ 次方；其 $4p$ 阶首系数
$-1+6-8+3$ 为零，根属于 $L(3O)$。
这一次角色为一，$L(3O)=\langle1,x,y\rangle$ 中只剩常数。
所有函数在 $\mathbf F_p$ 上，得到 (G2.30) 所写的
$\epsilon_{\rm inv}\in\mathbf F_p$。
这个证明没有消去任何低乘积。

### 9.2. 两个带安全范围的正指数读取

由 (G2.23)、(G2.20)，在正 multiple-$p$ 次数中，
$\mathcal R_2$ 只贡献
$-(C_2)^p/(2\beta)$；
其余项的指数为 $1$ 或 $2\bmod p$。
直接读取 $D^{p-3}x$ 的下降积仍为一，故
$$
\boxed{
G_{pr-1}
 =-\frac{[v^{r-1}]C_2(v)}{2\beta},
\qquad 3\le r\le p-4,\quad r\equiv3\pmod4 .
}
\tag{G2.31}
$$
最大的实际读取次数为 $p(p-5)$，严格小于
平方后首个可能误差 $p^2-2p-1$。
这条式子同时包含上节的 $r=3$ 和 $r=p-4$。

对 (G2.30) 第二式，代入
$\Psi=\zeta_{<p}^{\,p}-\beta v$。
除去 $v$ 的正次项后，其非恒定 multiple-$p$ 部分恰为
$-C_4(v)^p$，其中 $C_4$ 是 (1135.10) 的完整原列，
包括 $-3x^2-12a/5$。
$\epsilon_{\rm inv}$ 及这里的常数差都只贡献指数零。
其它展开项的 $v$ 次数为 $1,2,3,4\bmod p$，不会贡献本次读取。

对 $M=pr-3$，原
$[v^{p(r-1)}]D^{p-5}x$ 的下降积与 $(M-1)$ 合成
$(-4)(p-5)!=1/6$。
因此
$$
\boxed{
G_{pr-3}
 =-\frac{[v^{r-1}]C_4(v)}{4\beta^3},
\qquad 5\le r\le p-6,\quad r\equiv1\pmod4 .
}
\tag{G2.32}
$$
四次乘积的保守误差界是 $p^2-4p-1$，
而本式最大的读取为 $p(p-7)$，严格更低。
原 $C_4$ 的最大总权 $r+3\le p-3$，
所以所需 $\zeta$ 前缀也全部在已付安全权内。
这些界同时控制有界整 lift 的差及 logarithm 换元；
没有将低精度 $\Psi$ 的四次方用于未支付的高窗口。

### 9.3. 原 $d=8$ 矩的实际前两槽

按 R1135 §1、(1135.7)、(1135.10) 的原列定义，
$$
d_1=\frac12[v^{p-9}]C_2(v),\qquad
c_3=\frac1{24}[v^{p-7}]C_4(v).
$$
在 (G2.31) 取 $r=p-8$，在 (G2.32) 取 $r=p-6$，准确得
$$
\boxed{\qquad
G_{p^2-8p-1}=-\frac{d_1}{\beta},\qquad
G_{p^2-6p-3}=-\frac{6c_3}{\beta^3}.
\qquad}
\tag{G2.33}
$$
代回原 (1168.29)，保其 binomial、$(i+1)^{-1}$ 及 Hodge 基：
$$
\begin{aligned}
\mathcal R_{8,1}(y_8)
={}&-\frac{d_1}{\beta}\eta^8
    -\frac{56c_3}{\beta}\omega^2\eta^6\\
 &+14\beta^4G_{p^2-4p-5}\omega^4\eta^4
    +4\beta^6G_{p^2-2p-7}\omega^6\eta^2
    +\frac{\beta^8}{9}G_{p^2-9}\omega^8 .
\end{aligned}
\tag{G2.34}
$$
所以原 $\mathcal H_p,d_1,c_3$ 已在同一个实际第一层矩中
得到准确系数识别，而不是从两套多项式同形猜一个单位。

特别，(G2.32) 没有包含 $r=p-2$：
原 $d=4,i=2$ 的 $G_{p^2-2p-3}$ 仍超出这里的
四次安全读取，不能直接附送该槽。
(G2.34) 的后三项及原中央算术去平滑也完整保留。
这些身份不改变角色是否实际出现或是否 good，
也未证明 $\mathcal H_p=0$、$\Delta_{\rm low}=0$ 的联合条件不可能。


## 10. 共同整坐标中的完整抵消与四次矩的中间槽

§9 的保守界不覆盖 $d=4,i=2$。
本节不逐个高极单项外推 (G2.20)，而是在同一个整截断坐标中
使用 (G2.30) 的完整多项式抵消。
所得端点仍是一个原系数的准确身份，不是单位结论。

### 10.1. 整截断坐标与实际 logarithm 的比较

在 characteristic zero 取原
$v(u)=u\mathsf F(u^4)$，并令
$$
V_0(u)=[v(u)]_{<p^2}\in\mathbb Z_p[u],\qquad
\tau=\overline{V_0(u)}\in\mathbf F_p[[u]].
\tag{G2.35}
$$
(G2.8)–(G2.9) 保证所显示的截断整，且首项为 $u$，
故 $\tau$ 是一个真正的形式坐标。
这里不把它称为完整 logarithm，也没有给出形式群同态。

若一个原整有理函数在 $O$ 的极阶至多 $k$，
则其在 $\tau$ 中的约化系数与原 characteristic-zero
logarithm 读取，在所有次数
$$
N<p^2-k-1
\tag{G2.36}
$$
相同。理由是 $v(u)-V_0(u)$ 从 $u^{p^2}$ 才开始；
逆换元的差代入一个至多 $k$ 阶极，最早从
次数 $p^2-k-1$ 才能贡献。
这个比较先在 characteristic zero 的 Laurent series 中按次数成立，
再只约化所需的整前缀；不需要约化首个不整系数。

特别，原整 lift $D^{p-5}x$ 的极阶至多 $p-3$。
因此本次
$$
N=p^2-3p<p^2-p+2
$$
满足 (G2.36)。可以先在 $\tau$ 中计算
$[\,\tau^N\,]\mathcal R_4$，然后返回原 Hurwitz 读取。

### 10.2. 高极误差须作为完整多项式处理

在这个共同坐标中，$x,y,\Psi,\mathcal R_j$ 全部表示原有理函数。
令
$$
Z(\tau)=\zeta_u^{<p}(u(\tau)),\qquad
E(\tau)=\Psi-\bigl(Z(\tau)^p-\beta\tau\bigr).
$$
由 (G2.19)，准确有 $E=O(\tau^{p^2})$。
置
$$
\mathcal F_4(z)=-z^4+6x^pz^2+8y^pz+3x^{2p}.
$$
(G2.23)、(G2.30) 逐式给
$$
\mathcal F_4'(\Psi)=-24\beta^2\mathcal R_3,\qquad
\mathcal F_4''(\Psi)=24\beta\mathcal R_2.
$$
所以完整的有限差不是估计，而是
$$
\boxed{\quad
\mathcal F_4(\Psi-E)-\mathcal F_4(\Psi)
 =24\beta^2\mathcal R_3E
   +12\beta\mathcal R_2E^2+4\Psi E^3-E^4 .
\quad}
\tag{G2.37}
$$
$\mathcal R_3,\mathcal R_2,\Psi$ 的极阶分别至多
$p-2,p-1,p$。
故右边首个可能次数至少 $p^2-p+2$，严格高于本次 $N$。
这里 $x,y$ 从未各自改用另一个截断参数；
它们的高极项已经在 (G2.37) 的原函数身份中共同抵消。

把 $\Psi-E=Z^p-\beta\tau$ 代入左边。
含 $\tau^j$、$1\le j\le4$ 的各项，其余因子均为 $p$ 次方，
所以不贡献正 multiple-$p$ 指数 $N=p(p-3)$。
原 $\epsilon_{\rm inv}$ 也只贡献指数零。于是
$$
[\,\tau^{p(p-3)}\,]\mathcal R_4
 =-\frac{\bigl([\,\tau^{p-3}\,]
          C_4(Z(\tau),x(\tau),y(\tau))\bigr)^p}{24\beta^3}.
\tag{G2.38}
$$
这里 $C_4(z,x,y)=z^4-6xz^2-8yz-3x^2-12a/5$，
仍是原完整 Appell 多项式。

最后，选上述整截断的 characteristic-zero lift。
$Z-\zeta$ 从次数 $p$ 才开始，
但
$\partial_z C_4=4(z^3-3xz-2y)=4C_3$，
而这个完整 $C_3$ 在原 Gaussian 原点为 $O(v)$。
因此在 $C_4$ 中替换 $Z$ 为原 $\zeta$，
首个线性差从次数 $p+1$ 才开始；其余高次差也更晚。
所需的 $v^{p-3}$ 系数完全相同。
它可以用全部整的 $Z,x,y$ 前缀计算，故自身 $p$ 整。
定义
$$
\mathcal J_p=[v^{p-3}]C_4(v)\in\mathbf F_p .
\tag{G2.39}
$$

原 $D^{p-5}x$ 在此次数的下降积仍是
$(M-1)(M-2)_{\underline{p-5}}\equiv1/6$，
其中 $M=p^2-2p-3$。
结合 (G2.36)、(G2.38)，准确得到
$$
\boxed{\qquad
G_{p^2-2p-3}=-\frac{\mathcal J_p}{4\beta^3}.
\qquad}
\tag{G2.40}
$$

### 10.3. 中间槽的原低权 heat 来源

(G2.39) 还可直接由已付的安全低权模参数多项式计算。
先在一般短模型上定义
$$
\mathcal H_p(a,b)=\frac25\,\partial G_{p-5}(a,b),
\qquad
\partial=6b\partial_a-\frac{4a^2}{3}\partial_b ,
$$
最后再取 $b=0$。这就是 R1135 中原 $C_2$ 首标签的全模参数延拓。
在 [R1135 (1135.43)](../results/R1135-original-Gaussian-low-row-fiber-constraint.md)
取 $v=p-5,n=3$，保留其中的 $2vbG_v$，得到
$$
\begin{aligned}
\mathcal J_p(a,b)
 &=\frac{\partial^3G_{p-5}
       -10bG_{p-5}-(13a/3)\partial G_{p-5}}{15}\\
 &=\frac16\partial^2\mathcal H_p
       -\frac{13a}{18}\mathcal H_p-\frac23 bG_{p-5}.
\end{aligned}
\tag{G2.41}
$$
这里第一行定义一般模型上的同一个 Appell 系数；
在 $b=0$ 就是 (G2.39)。
所有模参数微分都在取 $b=0$ 以前完成。
因此 Gaussian 点上有
$$
\boxed{\qquad
\mathcal J_p
 =\left[\frac16\partial^2\mathcal H_p
          -\frac{13a}{18}\mathcal H_p\right]_{b=0}.
\qquad}
\tag{G2.42}
$$
输入 $G_{p-5}$ 的权小于 $p-1$，分母也全部为单位；
这是 $\mathcal J_p$ 的另一条原整来源，不需要反除 Bernoulli 数。
在 $\mathcal H_p=0$ 分支，它仍是未知的
$(\partial^2\mathcal H_p)(a,0)/6$。

### 10.4. 保留全部低卷积的首边界检查

令 $\mathsf E(v)=\sum_{m\ge4,\ 4\mid m}G_mv^m$、
$\vartheta=v\,d/dv$。
直接把原 $x,\zeta,y$ 代入 $C_4$，恒有
$$
\begin{aligned}
v^4(C_4+12a/5)
={}&-4(\vartheta^2-1)\mathsf E
 +4\mathsf E(\vartheta^2-1)\mathsf E
 -3((\vartheta-1)\mathsf E)^2\\
 &-2(\vartheta-1)\mathsf E^3+\mathsf E^4 .
\end{aligned}
\tag{G2.43}
$$
读取权 $p+1$。
线性项是
$-4((p+1)^2-1)G_{p+1}\equiv-8\beta$，
这里恰使用 (G2.22) 的 $pG_{p+1}=\beta$。
三次项的整系数被 $p$ 杀掉；
二次、四次项的每个 Hurwitz 输入都在安全权 $\le p-3$。
把二次和对称化后，完整得到
$$
\boxed{\quad
\mathcal J_p=-8\beta
 -\sum_{\substack{i+j=p+1\\i,j\ge4,\ 4\mid i,j}}
        (7ij+2)G_iG_j
 +\sum_{\substack{i+j+k+l=p+1\\i,j,k,l\ge4\\4\mid i,j,k,l}}
        G_iG_jG_kG_l .
\quad}
\tag{G2.44}
$$
两和均按有序指标计算。
特别不能因 $-8\beta$ 为单位而删去其余完整卷积。

原 (1168.28) 现在准确成为
$$
\boxed{
\mathcal R_{4,1}(y_4)
 =-\frac{\mathcal H_p}{2\beta}\eta^4
  -\frac{\mathcal J_p}{2\beta}\omega^2\eta^2
  +\frac{\beta^4}{5}G_{p^2-5}\omega^4 .
}
\tag{G2.45}
$$
顶槽 $G_{p^2-5}$ 没有由本节支付。
(G2.37) 的完整抵消也没有把 actual good-mask 的共同纤维条件
变成任意模参数导数为零，或证明 $\mathcal J_p$ 为单位。
本节只把同一个实际中槽接到原 $\mathcal H_p$ 的精确二阶源，
保全部首 $p$ 进位与低乘积。


## 11. 完整低阶 Appell 反射与两个实际矩的全部槽

本节把 §10 的共同坐标方法用于原 $C_j$、$1\le j\le10$。
常数项沿原低权反射准确锁定，因此也能读取此前保留的两个顶槽。
结论是全部 $d=4,8$ 矩的原有限系数公式；
不会把这些矩的每个分量增添成一个 actual good 角色。

### 11.1. 同一原核的 Appell 多项式与 $D$ 作用

以同一个 $\sigma$、$\omega$ 和 logarithm 参数定义
$$
U\mathscr K(T,U)
 =\sum_{j=0}^{10}\frac{C_j(T)}{j!}U^j+O(U^{11}),
\qquad C_0=1,\quad C_1=\zeta.
$$
令 $\mathcal C_j(z;x,y,a)$ 为将其中的 $\zeta(T)$ 替换成
独立变量 $z$ 的多项式。一个保全部低项的有限定义是
$$
\frac{U}{\sigma(U)}
 \exp\!\left(zU-\sum_{r=2}^{10}
                  \frac{D^{r-2}x}{r!}U^r\right)
 =\sum_{j=0}^{10}\frac{\mathcal C_j(z;x,y,a)}{j!}U^j
       +O(U^{11}).
\tag{G2.46}
$$
这里 $D^{r-2}x$ 先按原短模型化成 $x,y,a$ 的多项式。
所用权至多十、所有阶乘及原 $G_4,G_8$ 分母均为 $p$ 单位，
所以这确是一组整多项式。
例如 $\mathcal C_4$ 正是上节的
$z^4-6xz^2-8yz-3x^2-12a/5$。

有限定义直接给
$$
\partial_z\mathcal C_j=j\mathcal C_{j-1}.
$$
另由同一核在 $T=0$ 的展开
$\mathscr K(T,U)=T^{-1}+\zeta(U)+O(T)$，得到
$$
C_j(T)\ \text{在 }T=0\text{ 正规},\qquad
C_j(0)=-j!G_j\quad(2\le j\le10).
\tag{G2.47}
$$
这里约定此范围内非四倍数的 $G_j$ 为零，特别 $G_2=0$；
没有把 $C_1=\zeta$ 的一阶极混入 (G2.47)。

设
$$
\mathcal C_j^{\rm F}(z)=\mathcal C_j(z;x^p,y^p,a^p),
\qquad
\mathcal R_j=D^{p-j-1}x\quad(1\le j\le10).
$$
函数域导子始终是原 $D=\omega^{-1}d$，不是
$\partial_z$ 或模参数 $\partial$。
由于 $D(x^p)=D(y^p)=D(a^p)=0$、$D\Psi=-\beta$，
准确有
$$
D\,\mathcal C_j^{\rm F}(\Psi)
 =-j\beta\,\mathcal C_{j-1}^{\rm F}(\Psi).
\tag{G2.48}
$$

### 11.2. 全函数域反射及两个常数的锁定

沿用 (G2.35) 的共同 $\tau$ 坐标。
(G2.19) 给
$\Psi=Z^p-\beta\tau+O(\tau^{p^2})$。
由 (G2.46) 的 Appell 公式，
$$
\mathcal C_j^{\rm F}(Z^p-\beta\tau)
 =\sum_{\ell=0}^j
       \binom j\ell(-\beta\tau)^\ell
              C_{j-\ell}(Z,x,y,a)^p .
\tag{G2.49}
$$
对 $j-\ell\ge2$，原 (G2.47) 表明相应前缀正规；
$Z$ 与原 $\zeta$ 从次数 $p$ 才开始不同，
不影响这里的极部及常数。
唯一可能有负极的是 $j-\ell=1$，
其极阶至多 $p-j+1$。
首误差 $O(\tau^{p^2})$ 即使用逐幂保守界，也不贡献负极或常数，
因为 $j\le10<p$。
因此对 $2\le j\le10$，$\mathcal C_j^{\rm F}(\Psi)$ 仅在 $O$ 有至多
$p-j+1<p$ 阶极。

从 $j=1$ 的 $\mathcal C_1^{\rm F}(\Psi)=\Psi$ 开始，
使用 (G2.48) 归纳：
$$
\mathcal C_j^{\rm F}(\Psi)
 -(-1)^{j-1}j!\beta^{j-1}\mathcal R_j
$$
导数为零，且只可能有严格小于 $p$ 的极。
其 $p$ 次根没有极，所以差为常数。
两项的原 $\mu_4$ 角色都是 $i^j$；
若 $4\nmid j$，这个常数为零。

只剩 $j=4,8$。
(G2.49) 的常数为 $-j!G_j$：
$\ell=1,\ldots,j$ 各项的指数模 $p$ 都非零，
只有 $\ell=0$ 贡献原 (G2.47) 的常数。
另一方面，原整 $\mathcal R_j$ 的 logarithm 常数准确是
$$
[v^0]\mathcal R_j=(p-j)!\,G_{p+1-j}.
$$
只消费 R1114、R1135 已付的原低权反射
$$
G_{p+1-j}
 =-(j-1)!\delta^{1-j}G_j
 =(j-1)!\beta^{1-j}G_j\qquad(j=4,8),
$$
以及 Wilson 的 $(p-j)!(j-1)!=1$。
于是第二项的常数也恰为 $-j!G_j$，不留自由项。

完整得到
$$
\boxed{\qquad
\mathcal C_j^{\rm F}(\Psi)
 =(-1)^{j-1}j!\beta^{j-1}D^{p-j-1}x,
\qquad 1\le j\le10 .
\qquad}
\tag{G2.50}
$$
特别，(G2.30) 中此前保留的常数现在被准确固定为
$\epsilon_{\rm inv}=12a/5$。
这一步使用了原低反射；不是仅由 $D$-导数为零便删除常数。

### 11.3. 完整敏感度支付所有实际端点

记 $E=\Psi-(Z^p-\beta\tau)=O(\tau^{p^2})$。
对固定 $j\le10$，Appell 的完整有限差为
$$
\mathcal C_j^{\rm F}(\Psi-E)
 -\mathcal C_j^{\rm F}(\Psi)
 =\sum_{\ell=1}^j
    \binom j\ell(-E)^\ell\mathcal C_{j-\ell}^{\rm F}(\Psi).
\tag{G2.51}
$$
当 $j-\ell\ge1$ 时，(G2.50) 使该项的极阶至多
$p-j+\ell+1$。
因此整个误差从次数 $p^2-p+j-2$ 才开始；
$\ell=j$ 的 $E^j$ 项更晚。
原整 lift $\mathcal R_j$ 的极阶至多 $p-j+1$，
故 (G2.36) 返回真实 logarithm 的安全界也是
$$
N<p^2-p+j-2 .
\tag{G2.52}
$$
这里始终使用同一 $\tau,x,y,\Psi$，未对各个高极单项分别换元。

现令
$$
\begin{gathered}
d\in\{4,8\},\qquad 0\le i\le d,\quad i\ {\rm even},\\
j=i+2,\qquad
M_{d,i}=p^2-1-pd+(p-1)i,\qquad
\rho_{d,i}=p-d-1+i,\\
N_{d,i}=p\rho_{d,i}.
\end{gathered}
$$
本次 (G2.52) 的右界减去 $N_{d,i}$ 恰为
$p(d-i)+i>0$。
所以连 $i=d$ 的最高读取 $N=p^2-p$ 也严格在安全界内。

(G2.49) 中只有 $\ell=0$ 贡献正 multiple-$p$ 指数
$N_{d,i}$，其余 $\ell=1,\ldots,j<p$ 的指数模 $p$ 非零。
所需的低系数为
$[v^{\rho_{d,i}}]C_j(v)$，且 $\rho_{d,i}\le p-1$。
当 $i\ge2$ 时，$j\ge4$，
$\partial_z\mathcal C_j=jC_{j-1}$ 的原 Gaussian 前缀正规，
所以 $Z-\zeta=O(v^p)$ 不会影响任何次数 $\le p-1$ 的读取；
$i=0$ 则由 $\rho_{d,0}\le p-5$ 和已付二次界直接保证。
这些系数也因此都有原整来源。

直接读取 $\mathcal R_j=D^{p-j-1}x$：
因为 $j$ 为偶数，
$$
(M_{d,i}-1)(M_{d,i}-2)_{\underline{p-j-1}}
 \equiv(-j)(p-j-1)!=\frac1{(j-1)!}.
$$
结合 (G2.50) 得到全部实际 Hurwitz 系数的统一式
$$
\boxed{
G_{M_{d,i}}
 =-\frac{[v^{\,p-d-1+i}]C_{i+2}(v)}
          {(i+2)\beta^{i+1}},
\qquad d=4,8,\quad 0\le i\le d,\quad i\ {\rm even}.
}
\tag{G2.53}
$$
模型和这些系数在 $\mathbf F_p$ 上，故读取中的
$p$ 次方没有另一个半线性尺度。

特别，两个原顶槽现在精确为
$$
\boxed{\quad
G_{p^2-5}=-\frac{[v^{p-1}]C_6(v)}{6\beta^5},
\qquad
G_{p^2-9}=-\frac{[v^{p-1}]C_{10}(v)}{10\beta^9}.
\quad}
\tag{G2.54}
$$
没有把这些新系数设成单位或删除其低乘积。

### 11.4. 两个完整矩来自各自同一个原 heat 源

记原核的系数
$$
f_n^{v,0}=[T^{v+n-1}U^n]\mathscr K(T,U)
$$
（此处上标 $v$ 是整数权索引）。
由 $C_{i+2}/(i+2)!=[U^{i+1}]\mathscr K$，
(G2.53) 的低读取准确是
$$
[v^{p-d-1+i}]C_{i+2}(v)
 =(i+2)!\,f_{i+1}^{p-d-1,0}.
$$
代入 R1168 的同一个原 binomial 及 $(i+1)^{-1}$ 后，
整个矩成为
$$
\boxed{
\mathcal R_{d,1}(y_d)
 =-\frac1\beta
   \sum_{\substack{0\le i\le d\\i\ {\rm even}}}
       \frac{d!}{(d-i)!}\,
       f_{i+1}^{p-d-1,0}(a,0)\,\omega^i\eta^{d-i},
\qquad d=4,8 .
}
\tag{G2.55}
$$
所以四次矩用同一原 $G_{p-5}$ 的列 $1,3,5$，
八次矩用同一原 $G_{p-9}$ 的列 $1,3,5,7,9$。
例如 $f_1^{p-5,0}=\mathcal H_p/2$、
$f_3^{p-5,0}=\mathcal J_p/24$、
$f_1^{p-9,0}=d_1$、$f_3^{p-9,0}=c_3$，
与 §§8–10 的四个尺度逐一相同。

原 heat 方程直接给这些列的完整有限递推
$$
f_0^{v,0}=-G_v,\qquad f_{-1}^{v,0}=0,\qquad
(n+1)(v+n)f_{n+1}^{v,0}
 =\partial f_n^{v,0}+\frac a3 f_{n-1}^{v,0}.
\tag{G2.56}
$$
对 $v=p-d-1$、$0\le n\le d$，所有显示分母均为单位。
因此 (G2.55) 的每一项都是相同低权 $G_v$ 的一个明确有限
模参数微分，而不再需要一个 $p^2$ 长度的展开。
这些微分始终先在 $(a,b)$ 上完成，最后才取 $b=0$。

下一步 $n=d+1$ 则含真实因子
$(d+2)p f_{d+2}^{v,0}$。
这一列涉及 $T^p$，不能因为前面的 $p$ 就把它设为零；
原 $\zeta$ 的首个 $1/p$ 系数必须另保。
特别 $d=4,8$ 的 $G_{d+2}$ 在 Gaussian 点由 $\mu_4$ 为零，
也不意味着沿模参数的全部 carry 及其微分为零。
本节没有据此制造一个齐次高阶方程或断言任一指定 minor 为单位。

(G2.55) 识别的是既定矩的全部实际分量。
原共同纤维只要求已经出现且 good 的指定标签相同，
并不要求这些完整奇数阶 heat 列全为零。
原 Bernoulli mask、两点范围、中央算术去平滑及其后续比较
均保持原来的量词。


## 12. 三个原二同源商的完整 Appell 运输与全部 primed 槽

本节只处理 R1135 §8、R1168 §§10–11 的三个实际商曲线。
它们来自同一个原 Gaussian 曲线及其三个非零二挠点，
并有已指定的 CM 第二类直线。
不用一个未经支付的一般 supersingular 反射；
尤其不删除标准 $G_{p-1}$ 的首位，也不把商曲线当成
$\mathbf F_p$ 上的 Gaussian 模型。

### 12.1. 实际商、CM shear 与同一完整核

在原未分歧二次系数域中，令
$$
\epsilon\in\{0,e,-e\},\qquad e^2=-a,\qquad
Q_\epsilon=(\epsilon,0),\qquad
m_\epsilon=\frac y{x-\epsilon}.
$$
写 $x_\epsilon=x(T+Q_\epsilon)$、$y_\epsilon=y(T+Q_\epsilon)$。
原二挠加法律及 normalized quotient 是
$$
\begin{gathered}
m_\epsilon^2=x+x_\epsilon+\epsilon,\qquad
Dm_\epsilon=x-x_\epsilon,\\
X_\epsilon=x+x_\epsilon-\epsilon,\qquad
Y_\epsilon=y+y_\epsilon,\\
E_\epsilon:\quad Y_\epsilon^2=X_\epsilon^3+
 A_\epsilon X_\epsilon+B_\epsilon,\\
A_\epsilon=-4a-15\epsilon^2,\qquad
B_\epsilon=-7\epsilon(3\epsilon^2+a),\qquad
q_\epsilon^*\omega_\epsilon=\omega .
\end{gathered}
\tag{G2.57}
$$
所有 logarithm 参数都按原点常数零和首项一刚化；
故沿 $q_\epsilon$ 的共同参数仍是原 $v$。
R1135.21–23 已逐极部、乘子及首项支付
$$
\begin{gathered}
\widehat\zeta_\epsilon=\zeta_\epsilon-\epsilon v
 =2\zeta+m_\epsilon,\qquad
q_\epsilon^*((X_\epsilon+\epsilon)\omega_\epsilon)
 =2x\omega-dm_\epsilon,\\
\widehat{\mathscr K}_\epsilon(T,U)
 =e^{-\epsilon TU}\mathscr K_\epsilon(T,U)
 =\mathscr K(T,2U)+\mathscr K_{Q_\epsilon}(T,2U).
\end{gathered}
\tag{G2.58}
$$
因此 $\eta_\epsilon+\epsilon\omega_\epsilon$ 才是实际 CM
对向直线。其 pullback 为 $2\eta$ 加显示的 exact 项；
R1159 的 inverse coefficient map 则为
$\omega_\epsilon\mapsto\omega/2$、
$\eta_\epsilon\mapsto\eta-\epsilon\omega/2$。
本节不会把这两个方向混同。

令 $\mathcal C_{j,\epsilon}(z)$ 是 $E_\epsilon$ 的
**标准短模型** Appell 多项式，以 (G2.46) 的有限定义生成；
其中使用 $X_\epsilon,Y_\epsilon,A_\epsilon,B_\epsilon$。
CM-gauged 系数是
$$
\widehat C_{j,\epsilon}(T)
 =\mathcal C_{j,\epsilon}
       (\zeta_\epsilon(T)-\epsilon T).
$$
这个多项式本身不把 $X_\epsilon$ 改成 $X_\epsilon+\epsilon$：
$\widehat\sigma_\epsilon=e^{-\epsilon U^2/2}\sigma_\epsilon$
在 $U/\widehat\sigma_\epsilon$ 中的二次项，
正与 $\widehat\zeta_\epsilon'=-X_\epsilon-\epsilon$ 的二次项抵消。
例如
$\widehat C_{2,\epsilon}=(\zeta_\epsilon-\epsilon T)^2-X_\epsilon$。

从 (G2.58) 逐 $U$ 系数读取，且同时乘
$\exp(2(z-\zeta(T))U)$，得到真正的多项式身份
$$
\boxed{
\mathcal C_{j,\epsilon}(2z+m_\epsilon)
 =2^{j-1}\left\{
 \mathcal C_j(z;x,y,a)
 +\mathcal C_j(z+m_\epsilon;x_\epsilon,y_\epsilon,a)
 \right\},\qquad 0\le j\le10.
}
\tag{G2.59}
$$
这个证明不把 $\zeta$ 当成函数域中的独立坐标；
共同有限指数恰消去它，所得各系数就是显示的多项式。
$j=0$ 时右边是 $(1+1)/2$，没有少一个 $U^{-1}$。
$j=2$ 可直接用
$m_\epsilon^2=x+x_\epsilon+\epsilon$ 核准，没有另留常数。

### 12.2. 全函数域 Appell 反射：不反除 Bernoulli

记
$$
\Psi_\epsilon=D_\epsilon^{p-2}X_\epsilon,\qquad
\beta_\epsilon=
 \frac{C_{\rm rel}(X_\epsilon\omega_\epsilon)}{\omega_\epsilon'},
\qquad
\mathcal R_{j,\epsilon}=D_\epsilon^{p-j-1}X_\epsilon.
$$
沿原 quotient 拉回，
$$
\begin{gathered}
\Psi_\epsilon=\Psi+\Psi(T+Q_\epsilon)
             =2\Psi+m_\epsilon^p,\qquad
\beta_\epsilon=2\beta\in\mathbf F_p^\times,\\
\mathcal R_{j,\epsilon}
 =\mathcal R_j+\mathcal R_j(T+Q_\epsilon)
 \qquad(1\le j\le10).
\end{gathered}
\tag{G2.60}
$$
第二个等号也可不借 addition convention 自证：
$\Psi(T+Q_\epsilon)-\Psi-m_\epsilon^p$ 导数为零，
原 $p$ 阶主部全消；其 $p$ 次根无极，故为常数。
三项在二挠平移后仍为奇函数，常数因此为零。
$\beta_\epsilon=2\beta$ 也直接由 (G2.58) 和
supersingular Cartier 得到。

对 (G2.59) 作系数 Frobenius，再令 $z=\Psi$。
原 (G2.50) 及其 $Q_\epsilon$ 平移逐项给
$$
\boxed{
\mathcal C_{j,\epsilon}^{\rm F}(\Psi_\epsilon)
 =(-1)^{j-1}j!\beta_\epsilon^{j-1}
                         \mathcal R_{j,\epsilon},
\qquad 1\le j\le10.
}
\tag{G2.61}
$$
这是原 quotient 函数域中的等式：
拉回由 separable degree-two 映射检验，因而仍为单射。
它没有另用一个未定的低权反射去锁商曲线常数；
全部常数已由同一完整核 trace 和原 Gaussian 两项确定。

一个必要的边界核准是 $j=2$。
在原共同参数中
$m_\epsilon=-v^{-1}-\epsilon v+\cdots$，
所以 $\Psi_\epsilon$ 的 $v^p$ 项是 $-\epsilon^p v^p$，
而 $\widehat C_{2,\epsilon}(0)=-2\epsilon$。
读取 (G2.61) 的常数准确得到
$$
\boxed{\qquad
G_{p-1}(E_\epsilon,\omega_\epsilon)
 =\frac{\epsilon^p}{\beta_\epsilon}.
\qquad}
\tag{G2.62}
$$
此处 $G_{p-1}$ 是这个**实际 quotient lift** 在共同 logarithm
参数中的整值；不主张它只依一般 supersingular reduction。
不能把 $\epsilon^p$ 改成 $\epsilon$，也不能由 $G_2=0$
将 (G2.62) 置零。
对偶数 $4\le j\le10$，同一常数读取才给
$G_{p+1-j}(E_\epsilon)
 =(j-1)!\beta_\epsilon^{1-j}G_j(E_\epsilon)^p$。
这些是各点上的值等式，不据此沿模参数横向微分。

### 12.3. 包括奇数槽、最高端点的共同精度

(G2.19) 的同一整截断坐标 $\tau$ 沿 $q_\epsilon$ 保持，
因为 (G2.57) 在原点是 étale，且共同 differential 不变。
令 $Z$ 为原 §11 的低 $\zeta$ 前缀，置
$Z_\epsilon=2Z+m_\epsilon$。
(G2.60) 准确给
$$
\Psi_\epsilon
 =Z_\epsilon^p-\beta_\epsilon\tau+O(\tau^{p^2}).
$$
每个 $X_\epsilon,Y_\epsilon$ 都按同一实际有理映射展开；
没有逐个高极单项分别换坐标。
(G2.61) 给完整敏感度的极界至多 $p-j+1$。
故与 (G2.51)–(G2.52) 完全一样，
第 $j$ 个完整 Appell 式的误差首阶至少为
$p^2-p+j-2$。

现在允许全部
$$
d=4,8,\qquad 0\le i\le d,\qquad
j=i+2,\quad \rho=p-d-1+i,\quad M=M_{d,i}.
$$
不再仅取偶 $i$：商曲线不具有原标准 $\mu_4$ 帧。
$N=p\rho$ 与安全上界的差仍为 $p(d-i)+i>0$。
原 $\widehat C_{j,\epsilon}$ 对 $j\ge2$ 在 $v=0$ 正规，
且 $Z_\epsilon-\widehat\zeta_\epsilon$ 的首未读项从次数 $p$
开始。因此 $j\ge3$ 时所有 $\rho\le p-1$ 都安全；
$j=2$ 则用 $\rho\le p-5$ 的既定低界。
这些低系数全部有原整来源。

本次下降阶乘对奇偶 $j$ 统一为
$$
(M-1)(M-2)_{\underline{p-j-1}}
 =\frac{(-1)^j}{(j-1)!}\pmod p.
$$
与 (G2.61) 的 $(-1)^{j-1}$ 相乘后，最终号始终为负。
于是
$$
\boxed{
\begin{aligned}
G_{M_{d,i}}(E_\epsilon,\omega_\epsilon)
 &=-\frac{
      \bigl([v^\rho]\widehat C_{i+2,\epsilon}(v)\bigr)^p}
          {(i+2)(2\beta)^{i+1}},\\
\sigma G_{M_{d,i}}(E_\epsilon,\omega_\epsilon)
 &=-\frac{[v^\rho]\widehat C_{i+2,\epsilon}(v)}
          {(i+2)(2\beta)^{i+1}} .
\end{aligned}}
\tag{G2.63}
$$
第二行使用实际 coefficient field 为 $\mathbf F_{p^2}$、
$\sigma^2=1$ 及 $2\beta\in\mathbf F_p$。
它正是 R1168.49 所需的 $\sigma G_M$，
不能先在第一行删除 $p$ 次方。

### 12.4. 每个实际 primed 矩只需同一个低 heat 源

置 $r_d=p-d-1$，并定义
$$
F_{d,i}=f_{i+1}^{r_d,0}(a,0),\qquad
\widehat F_{\epsilon,d,i}
 =[T^{r_d+i}U^{i+1}]\widehat{\mathscr K}_\epsilon(T,U).
$$
原 gauge 给完整有限式
$$
\boxed{
\widehat F_{\epsilon,d,i}
 =\sum_{q=0}^{i+1}\frac{(-\epsilon)^q}{q!}\,
            f_{i+1-q}^{r_d,0}(A_\epsilon,B_\epsilon).
}
\tag{G2.64}
$$
每项均来自同一个 $G_{r_d}$，
先用 (G2.56) 的一般 $(A,B)$ heat 递推，再取
$(A_\epsilon,B_\epsilon)$，最后乘显示的固定 gauge。
所需 $n\le d+1$ 的所有递推分母均为单位。
这不是把 $\epsilon$ 随意当成横向 heat 参数，
也没有越过下一列的 $p$ 倍 carry。

设
$$
L_{d,i}=\frac{d!}{(d-i)!\,\beta},\qquad k_d(2)=4-2^{-d}.
$$
将 (G2.63) 代入 R1168.49 的**实际 raw** 两式，
全部原 binomial、$i+1$、$\sigma$ 和 $\beta$ 因子得到
$$
\boxed{
\begin{aligned}
\mathcal A_{d,i}
 &=-L_{d,i}\,k_d(2)\,F_{d,i},\\
\mathcal A'_{\epsilon,d,i}
 &=-L_{d,i}
       \left(2^{-i}\widehat F_{\epsilon,d,i}
                        -2^{-d}F_{d,i}\right),
\qquad d=4,8,\quad0\le i\le d .
\end{aligned}}
\tag{G2.65}
$$
这些是 R1168 的原 $\omega^i\eta^{d-i}$ 坐标；
没有在最后一步把标准 $\eta_\epsilon$ 偷换成 CM 对向线。
CM shear 已完整包含于 (G2.58)、(G2.64)，
而 (G2.65) 使用的是原 primed theta 在原形式盘上的直接读取。
原曲线的奇 $i$ 给 $F_{d,i}=0$；
对应商曲线的 $\widehat F_{\epsilon,d,i}$ 则仍须保留。

全二挠 trace (1135.24) 还给一个完整规范自检：
$$
\sum_{\epsilon=0,e,-e}\widehat F_{\epsilon,d,i}
 =2^i(4+2^{1-d})F_{d,i},
\qquad
\sum_\epsilon\mathcal A'_{\epsilon,d,i}=\mathcal A_{d,i}.
\tag{G2.66}
$$
先在特征零读完整核，再在 (G2.63)–(G2.64)
已经支付整性的指定系数约化。
因此这里即使最高 total weight 超过 $p-3$，
也没有把旧安全 band 未经证明地外推。

### 12.5. 原 same-kernel 相关项的完整低系数式

最后只对 R1168.51 的同一个实际 $B_{k,l}$ 代入，
得到
$$
\boxed{
B_{k,l}=L_{4,k}L_{8,l}
 \left\{(16+2^{-11})F_{4,k}F_{8,l}
       -2^{-(k+l)}
          \sum_{\epsilon=0,e,-e}
             \widehat F_{\epsilon,4,k}
             \widehat F_{\epsilon,8,l}\right\}.
}
\tag{G2.67}
$$
两个 primed 因子仍来自同一个 $\epsilon$。
本式可直接进入既定 ordered/BCH 与 $\Pi_2$ 读取；
没有把它的三个同源值换成单点 scalar，也未反除任何
Bernoulli 数或断言指定相关项非零。

实际 CM $i$ 交换 $\epsilon=e,-e$，完整 gauge 同时运输。
此处 coefficient 的 total weight 为
$p-d+1+2i$，故
$$
\widehat F_{-e,d,i}=(-1)^i\widehat F_{e,d,i},
\qquad
F_{d,i}=\widehat F_{0,d,i}=0\quad(i\ {\rm odd}).
$$
所以 $k+l$ 奇时 (G2.67) 为零；
但两个奇槽的乘积不被此奇偶性删除，准确保留为
$$
B_{k,l}
 =-2^{1-k-l}L_{4,k}L_{8,l}\,
       \widehat F_{e,4,k}\widehat F_{e,8,l}
 \qquad(k,l\ {\rm odd}).
\tag{G2.68}
$$
这特别排除了只因原 Gaussian 矩没有奇槽，
便删去全部 primed odd–odd 贡献的做法。

本节消去的是原三个二同源商中全部所需的 $p^2$ 窗口：
输入现在是各自同一个低权 $G_{p-5}$ 或 $G_{p-9}$ 的有限 heat
列，以及原指定 $\epsilon$ gauge。
没有增加一个 actual good 角色，没有证明原 Gaussian
共同纤维被分离，也没有把算术去平滑或未知中央值设为零。
全部为纸面推导，无数学程序执行。


## 13. 同核二同源 Fay 读取与原 mask 上的第二中央首槽

本节保留 §12 的全部 primed 槽。
先将同一二挠点上的乘积 trace 化为原核的完整 Fay 式，
并清除两种对角极，给出没有展开顺序歧义的有限系数取法。
随后直接计算原第二中央相关项的一个指定槽，
明确它在原 joint mask 上的共同因子；不以该因子化替代非零证明。

### 13.1. 同时平移的原 Fay 身份

仍令 $\mathscr K_O=\mathscr K$。
原 Kronecker 核的完整 Fay 恒等式为
$$
\mathscr K(T,U)\mathscr K(S,V)
=\mathscr K(T-S,U)\mathscr K(S,U+V)
 +\mathscr K(S-T,V)\mathscr K(T,U+V).
$$
对 $Q\ne O$，同时把 $T,S$ 平移同一个 $Q\in E[2]$，
再乘原规范中的 $\exp(-\zeta(Q)(U+V))$，最后作
$(U,V)\mapsto(2U,2V)$。此时实际相位为
$\exp(-2\zeta(Q)(U+V))$；$Q=O$ 直接用原 Fay 式。
得到
$$
\begin{aligned}
\mathscr K_Q(T,2U)\mathscr K_Q(S,2V)
={}&\mathscr K(T-S,2U)\mathscr K_Q(S,2(U+V))\\
 &+\mathscr K(S-T,2V)\mathscr K_Q(T,2(U+V)).
\end{aligned}
\tag{G2.69}
$$
两项的指数相位完全相同；这里始终是同一个 $Q$，
不是两次独立 Norm 的乘积。

用原全二挠分布
$\sum_{Q\in E[2]}\mathscr K_Q(T,2U)=2\mathscr K(2T,U)$，
再使用 (G2.58)，准确得到
$$
\boxed{\begin{aligned}
\sum_{\epsilon=0,e,-e}
 \widehat{\mathscr K}_\epsilon(T,U)
 \widehat{\mathscr K}_\epsilon(S,V)
={}&2\mathscr K(T,2U)\mathscr K(2S,V)
  +2\mathscr K(S,2V)\mathscr K(2T,U)\\
 &+2\mathscr K(T-S,2U)\mathscr K(2S,U+V)\\
 &+2\mathscr K(S-T,2V)\mathscr K(2T,U+V).
\end{aligned}}
\tag{G2.70}
$$
为核常数，令 $A=\mathscr K(T,2U)$、$B=\mathscr K(S,2V)$。
左边先展开成三个 $AB$、两个 nonzero-$Q$ 一次和及一个同核乘积和。
把各和补回 $Q=O$ 后，$AB$ 的系数是 $3-1-1-1=0$。
所以 (G2.70) 没有另一个 $AB$ 补项，也未省略 primed odd–odd 乘积。

### 13.2. 两个对角极在完整分子中消去

直接分别展开 (G2.70) 的最后两项，会人为引入
$T-S$、$U+V$ 的 Laurent 展开顺序。
以下取法消除这个问题。
定义正规的原二变量级数
$$
\mathscr H(T,U)=TU\,\mathscr K(T,U).
$$
它满足
$\mathscr H(T,0)=T$、
$\mathscr H(0,U)=U$、
$\mathscr H(-T,-U)=-\mathscr H(T,U)$。
置
$$
\begin{aligned}
\mathscr N={}&
 VT\,\mathscr H(T-S,2U)\mathscr H(2S,U+V)\\
 &-US\,\mathscr H(S-T,2V)\mathscr H(2T,U+V).
\end{aligned}
$$
在 $T=S$ 时，用 $\mathscr H(0,2U)=2U$、
$\mathscr H(0,2V)=2V$，两项严格相消。
在 $V=-U$ 时，用
$\mathscr H(S-T,-2U)=-\mathscr H(T-S,2U)$
以及 $\mathscr H(2S,0)=2S$、$\mathscr H(2T,0)=2T$，
两项也严格相消。
换变量 $X=T-S$、$W=U+V$ 后，这正表示
$\mathscr N$ 的每个单项同时含 $X,W$。
因此正规级数
$$
\mathscr D=\frac{\mathscr N}{(T-S)(U+V)}
$$
唯一存在；这两次 monic 线性除法不引入任何整数分母。
(G2.70) 现在等价于无对角极的整形式
$$
\boxed{
\begin{aligned}
2TSUV\sum_\epsilon
 \widehat{\mathscr K}_\epsilon(T,U)
 \widehat{\mathscr K}_\epsilon(S,V)
={}&\mathscr H(T,2U)\mathscr H(2S,V)\\
 &+\mathscr H(S,2V)\mathscr H(2T,U)+\mathscr D.
\end{aligned}}
\tag{G2.71}
$$
这里先在同一特征零 sigma 来源上作恒等式。
“无对角极”和“除法不增加分母”不表示每个高权
$\mathscr H$ 系数都可单独约化模 $p$；
原首 $p$ carry 仍须在完整式中保留。

### 13.3. 原相关项的有限、无歧义系数泛函

令右边 (G2.71) 为 $\mathscr B(T,S,U,V)$。
对原 $0\le k\le4$、$0\le l\le8$，准确有
$$
\boxed{
\sum_\epsilon
 \widehat F_{\epsilon,4,k}\widehat F_{\epsilon,8,l}
 =\frac12
 [T^{p-4+k}S^{p-8+l}U^{k+2}V^{l+2}]\,\mathscr B.
}
\tag{G2.72}
$$
这是同一个 (G2.67) 中的完整 same-kernel 和，
不是新定义的独立双线性泛函。
所读取的总次数为
$$
L=2p-8+2(k+l)\le2p+16.
$$
$\mathscr H$ 从次数一开始，
而 $\mathscr N$ 外部的次数二与两次线性除法的次数二抵消。
所以 (G2.72) 只使用
$\mathscr H$ 的总次数至多 $L-1$ 的有限截断；
不需要一个 $p^2$ 长度的核。
按 $X,W$ 的正规除法取该有限齐次部分即可，
不把 $1/(T-S)$ 或 $1/(U+V)$ 任意选成某个区域的级数。

完整读取的整性由左边 §12 支付：
每个 $\widehat F$ 都是低权 $G_{p-5}$ 或 $G_{p-9}$
经单位分母 heat 递推及固定 gauge 得到的整值。
因此若右边某个单独高权输入带 $1/p$，
须先完成 (G2.71)–(G2.72) 的有理系数恒等式再约化；
不能把那个输入的 $p$ 倍先置零。
本式可与 (G2.67) 共同使用，不删除任何低乘积或 principal 边界。

### 13.4. 先列原 actual-good 的必要条件

以下仍只比较同一原 Gaussian coarse component 的不同点；
两 twist 的运输使用 R1135 §10，原 $S=0$、
$P_{\rm pair}=0$ 范围均保留。
由 R1127，若 $p\mid B_{p-3}$，实际 $R=2$ 已有 affine 单位行。
所以尚需处理的非对角共同纤维必须在
$p\nmid B_{p-3}$ 分支。
此时原 forced good 行 $R=p-3$ 给
$$
\mathcal A_{p-3}(Z)=\frac{\mathcal H_p}{4}Z,
\qquad
F_{4,0}=\frac{\mathcal H_p}{2}=0.
\tag{G2.73}
$$

在另外满足 $p\mid B_{p-7}$、$p\nmid B_{p-5}$ 的原支路，
实际 low $R=4$ 和 forced good $R=p-5$ 才同时可用。
R1135.3、.7–.8 给出的必要条件准确是
$$
\boxed{\qquad
c_2F_{8,0}+G_{p-7}F_{8,2}
 =c_2d_1+G_{p-7}c_3=\Delta_{\rm low}=0 .
\qquad}
\tag{G2.74}
$$
$G_{p-7}=-48a^2/(5\delta^7)$ 为原已付单位。
这里 $c_2=f_2^{p-7,0}$ 是另一条原 heat 源；
不能将它替换成 $F_{4,2}$。

(G2.73)–(G2.74) 没有要求
$F_{4,2}=\mathcal J_p/24$、
$F_{8,0}=d_1$、其它 $F_{d,i}$ 或任一
$\widehat F_{\epsilon,d,i}$ 为零。
其余 Bernoulli 支路仍逐条保留原 mask，不因 §12
给出了完整矩便增加观测。

### 13.5. 第二中央相关项的一个原代数／jet 配对

现计算 R1169.8 的原
$Z_{2,\rm corr}^{\rm BCH}\in\operatorname{Sym}^8H(4)$。
令 $c_\omega$ 表示原
$\langle\omega,\eta\rangle$ 在既定 Tate frame 中的单位系数；
若使用 normalized symplectic frame，则 $c_\omega^2=1$。
由原 normalized contraction
$\Pi_2(v^4,w^8)=\langle v,w\rangle^2v^2w^6$，
输出 $\eta^8$ 的三个可能输入分别满足
$$
\begin{aligned}
[\eta^8]\Pi_2(\omega^2\eta^2,\eta^8)&=c_\omega^2/6,\\
[\eta^8]\Pi_2(\omega\eta^3,\omega\eta^7)&=-c_\omega^2/16,\\
[\eta^8]\Pi_2(\eta^4,\omega^2\eta^6)&=c_\omega^2/28 .
\end{aligned}
$$
例如可在
$\Pi_2((\eta+t\omega)^4,(\eta+s\omega)^8)
=c_\omega^2(t-s)^2(\eta+t\omega)^2(\eta+s\omega)^6$
中比较 $t^ks^l$。
原 BCH 因子 $(k-l)/(2(k+l+2))$ 使中间项准确为零，
并非因为 $B_{1,1}$ 本身为零。
因此
$$
[\eta^8]Z_{2,\rm corr}^{\rm BCH}
 =c_\omega^2\left(\frac{B_{2,0}}{24}
                         -\frac{B_{0,2}}{112}\right).
\tag{G2.75}
$$

这里两条原 even–even 系数可以完整求出。
取 $\lambda=1+i$，则
$G_m(E_0)=\lambda^mG_m(E)$。
对本次偶槽，两个非 Gaussian 商的 $G_m$ 相同；
R1168.50 遂给
$$
\sigma G_m(E_{\pm e})
 =\frac{2+2^{-d}-\lambda^m}{2}G_m(E),
\qquad m=M_{d,k}.
$$
所用高权系数都已由 §12 或 R1168.48 支付整性。
对 $(d,k)=(4,2),(8,0)$，
$\lambda^m$ 分别是 $1/4,1/16$；
对 $(4,0),(8,2)$，分别是 $-1/4,-1/16$。
故三商同核乘积的比例分别为
$14541/8192$、$19701/8192$。
代回 R1168.51，再保原 binomial，得到
$$
\boxed{
B_{2,0}=\frac{4557}{1024\beta^2}\mathcal J_p d_1,
\qquad
B_{0,2}=\frac{3267\cdot28}{512\beta^2}\mathcal H_pc_3 .
}
\tag{G2.76}
$$
没有把两个 primed 槽分开求 Norm。

(G2.75) 因而准确成为
$$
\boxed{
[\eta^8]Z_{2,\rm corr}^{\rm BCH}
 =\frac{c_\omega^2}{8192\beta^2}
       \left(1519\mathcal J_p d_1
                    -13068\mathcal H_p c_3\right).
}
\tag{G2.77}
$$
在原必要条件 $\mathcal H_p=0$ 上，
(G2.42) 给更明确的 jet 因子化
$$
\boxed{
[\eta^8]Z_{2,\rm corr}^{\rm BCH}
 =\frac{1519\,c_\omega^2}{49152\beta^2}
        (\partial^2\mathcal H_p)(a,0)\,d_1,
\qquad \mathcal H_p=0 .
}
\tag{G2.78}
$$
$1519=7^2\cdot31$，所以显示的外因子在本范围均为单位。
这准确定位了该**实际相关槽**在原 $H_p=0$ locus 上的共同因子。
若此槽另为零，则必有 $\partial^2H_p=0$ 或 $d_1=0$；
在还满足 (G2.74) 的支路，后者又迫 $c_3=0$。

以上仍没有把相关槽的值认作未平滑中央值。
R1169.17 的原 $J_{2,2}$、$B_{2,2}$ 算术补项及
R1171 的实际仿射同源运输必须保留；
原共同纤维本身也没有要求 (G2.75) 在参考 CM 点等于零。
因此 (G2.78) 是一个精确的原 jet 配对和退化因子，
不是对共同零的排除。
后继继续控制这些实际因子或原完整余对差值，
不把完整矩消失加入原 good-mask 假设。
全部为纸面推导，无数学程序执行。


## 14. 原奇列的二同源消去、二次 norm 与首个 \(p\) 强迫

本节仍使用同一个原 Gaussian 参数 $v$，所有撇号均表示
固定 $a$ 后的 $d/dv$，不是模参数导子 $\partial$。
把 §12 的四个实际奇列化回原 $C_2,C_4$，再给这两个
指定函数的完整微分与首 $p$ 边界。
这个边界是非零的；其余有限卷积仍保留，不把它缩成
一个尚未证明的奇列单位。

### 14.1. 两个非 Gaussian 商的奇 band

令 $e^2=-a$、$e\ne0$，沿 (G2.57) 写
$m_e=y/(x-e)$。原第五 Appell 多项式为
$$
\mathcal C_5(z)
 =z^5-10xz^3-20yz^2-(15x^2+12a)z-4xy .
$$
这里仍包含原 sigma 分母；并非裸的 $\sigma^{(5)}/\sigma$。
使用 $x_e=m_e^2-x-e$、
$y_e=m_e(x-x_e)-y$，逐次幂直接得到
$$
\begin{aligned}
\mathcal C_3(z+m_e;x_e,y_e)
 &=z^3+3m_ez^2+3(x+e)z+y,\\
\mathcal C_5(z+m_e;x_e,y_e)
 &=z^5+5m_ez^4+10(x+e)z^3+10yz^2\\
 &\qquad +(5x^2-10ex+3a)z+(x-5e)y .
\end{aligned}
\tag{G2.79}
$$
又 $m_e-m_{-e}=2ex/y$，所以两个完整差为
$$
\begin{aligned}
C_{3,Q_e}-C_{3,Q_{-e}}
 &=6e\left(\zeta+\frac xy\zeta^2\right),\\
C_{5,Q_e}-C_{5,Q_{-e}}
 &=10e\left(\frac xy\zeta^4+2\zeta^3-2x\zeta-y\right).
\end{aligned}
\tag{G2.80}
$$
这些是同一原特征零函数的身份，没有只比较首项。

以下只在取实际奇 $i=1,3$ 的指定系数时，使用
$\widehat F_{-e,d,i}=-\widehat F_{e,d,i}$。
令 $Q_0=(0,0)$、$\lambda=1+i$，并取
$$
u(v)=x(v)^{-1/2}=v+O(v^5),\qquad
\mathscr A(v)=uC_2(v),\quad
\mathscr B(v)=u\left(C_4(v)+\frac{12a}{5}\right).
$$
由原 (1135.11) 及 $x_{Q_0}=a/x$，
$$
\begin{gathered}
\zeta+\frac xy\zeta^2
 =\frac i2\,\frac xy C_2(\lambda v),\\
\frac xy\zeta^4+2\zeta^3-2x\zeta-y
 =-\frac14\,\frac xy C_4(\lambda v)
                  -\frac{3a}{5}\frac xy,\\
\frac{x(v)}{y(v)}=-\frac{u(\lambda v)}{\lambda}.
\end{gathered}
\tag{G2.81}
$$
最后一式来自
$x(\lambda v)=1/(2i(x/y)^2)$，原点首项固定其负号。
第二式的常数 $3a/5$ 不能删掉。

定义四个**原**系数
$$
a_4=[v^{p-4}]\mathscr A,\quad
a_8=[v^{p-8}]\mathscr A,\qquad
b_4=[v^{p-2}]\mathscr B,\quad
b_8=[v^{p-6}]\mathscr B.
$$
在 (G2.59) 先取 $e,-e$ 的差，再除相应的 $3!,5!$，
使用 $\lambda^{p+1}=2$，得到全部四个尺度
$$
\boxed{
\begin{array}{c|cc}
 &i=1&i=3\\ \hline
d=4&\widehat F_{e,4,1}=e\,a_4/4
   &\widehat F_{e,4,3}=-e\,b_4/12\\
d=8&\widehat F_{e,8,1}=-e\,a_8/16
   &\widehat F_{e,8,3}=e\,b_8/48 .
\end{array}}
\tag{G2.82}
$$
例如 $i=1$ 的一般因子是
$-ie\lambda^{p-d-1}$，$i=3$ 的一般因子是
$e\lambda^{p-d+1}/6$。本式只使用 §12 已付整性的
低系数，所读次数均小于 $p$；
不把相应 band 身份扩成一个没有投影的整函数等式。

### 14.2. 指定两个函数的完整 norm 与微分方程

写
$$
s=u'=\sqrt{1+au^4},\qquad
\mathscr W=u\mathscr A'-s\mathscr A.
$$
原 $\zeta'=-u^{-2}$、$y=-s/u^3$ 给
$$
\boxed{
\begin{gathered}
\mathscr W=2(s/u-\zeta),\qquad
\mathscr W'=2au^2,\qquad
\mathscr A''=2au^2\mathscr A+2au,\\
u\mathscr B=\mathscr A^2-\mathscr W^2+4au^2 .
\end{gathered}}
\tag{G2.83}
$$
证明可完全在原函数内完成：
$C_2'=-2u^{-2}\zeta+2s/u^3=\mathscr W/u^2$，
故第一、二式直接成立；对 $uC_2$ 求两次导数，
其中所有一次 $\zeta$ 项严格相消，得第三式。
最后原 Appell 恒等式
$$
C_4=C_2''+2\zeta C_2'+C_2^2-\frac{2a}{5}
$$
以及 $C_2'=\mathscr W/u^2$、$\mathscr W'=2au^2$
给第四式。全部常数由原点首项核准：
$$
\mathscr A=\frac a3v^3+O(v^7),\qquad
\mathscr W=\frac{2a}{3}v^3+O(v^7),\qquad
\mathscr B=4av+O(v^5).
$$
这不是仅给一个抽象的相同微分方程；
三个函数及其积分常数都由原 sigma 源固定。

### 14.3. 首个 \(p\) 系数不能作为整系数约化

$u(v)$ 在本节需要的次数 $\le p$ 内整。
$\mathscr A,\mathscr W$ 的次数 $<p$ 也整，
但它们的第 $p$ 项恰有一个必须保留的分母。
由原 (G2.22) 的 $pG_{p+1}=\beta$，
$$
[v^{p-1}]C_2
 =-(p+2)G_{p+1}
     +\sum_{\substack{i+j=p+1\\i,j>0}}G_iG_j .
$$
和式中的非零 $i,j$ 都是四的倍数且不超过 $p-3$，
所以其中全部项整。乘回原 $u=v+O(v^5)$ 后，
其它贡献仍只使用安全系数。因此准确有
$$
\boxed{
p[v^p]\mathscr A=-2\beta,\qquad
p[v^p]\mathscr W=2\beta
\quad\text{在 }\mathbb F_p\text{ 中}.
}
\tag{G2.84}
$$
第二式也直接由
$\mathscr W=u\mathscr A'-u'\mathscr A$ 得到：
可能不整的首项给 $(p-1)[v^p]\mathscr A$，
其它系数均整。

在 (G2.83) 的 $\mathscr A''$ 中读取 $v^{p-2}$，
左边为 $p(p-1)[v^p]\mathscr A=2\beta$，并非零。
故得到只含安全低系数的指定非零 forcing
$$
\boxed{\qquad
a[v^{p-2}]\bigl(u^2\mathscr A+u\bigr)=\beta\ne0 .
\qquad}
\tag{G2.85}
$$
左边的 $\mathscr A$ 最高只读到 $v^{p-4}$。
本式保留所有低卷积，不能将其改成
$a\,a_4=\beta$ 或用模 $p$ 的形式求导先删掉
(G2.84)。

其中 $u$ 的边界本身也有准确原值：
$$
\boxed{\qquad [v^{p-2}]u=\frac{\chi(a)}{\beta},
\qquad \chi(a)=a^{(p-1)/2}\in\{1,-1\}.\qquad}
\tag{G2.86}
$$
给一个自足的有限证明。令
$F(z)={}_2F_1(1/4,1/2;5/4;z)$、
$b_j=[z^j]F(z)^2$。
将 $F$ 的二阶方程代入其平方的三阶方程，系数递推为
$$
j(j+\tfrac12)(j+\tfrac14)b_j
 =j(j-\tfrac12)(j-\tfrac14)b_{j-1},\qquad b_0=1.
$$
因此在 $0\le j\le h=(p-3)/4$ 的单位分母范围，
$$
b_h=\frac{(3/4)_h}{(2h+1)(5/4)_h}.
$$
真实 Lagrange 换元 $v=uF(-au^4)$ 给
$$
[v^{p-2}]u
 =-\frac12(-a)^h b_h
 =(-a)^h\frac{h!}{(1/2)_h}\pmod p.
$$
这里用 $F^{2-p}\equiv F^2$ 的次数 $4h<p$ 前缀，
并用
$(3/4)_h=(-1)^hh!$、
$(5/4)_h=(-1)^h(1/2)_h$。
再乘原 $R_h=\beta/a=(-a)^h(1/2)_h/h!$，
得到 (G2.86)。所用所有阶乘、rising 因子均为单位；
没有执行数学程序，也没有用未付的高阶 Clausen 截断。

### 14.4. 原 mask 上的完整条件，及未消去的低卷积

写
$$
u=vU(v^4),\qquad \mathscr A=v^3A_0(v^4),\qquad U(0)=1.
$$
原 (G2.73) 的 $\mathcal H_p=0$ 准确是
$[t^{h-1}]A_0/U=0$。
因此 (G2.85)–(G2.86) 在这个**实际**必要条件上给
$$
\boxed{\quad
a[t^{h-1}](U^2-U^{-1})A_0
 =\beta-\frac{a\chi(a)}{\beta},
\qquad \mathcal H_p=0 .
\quad}
\tag{G2.87}
$$
$U=1+(a/10)t+\cdots$，故 $U^2-U^{-1}$ 的首项为
$3at/10$。左边不再含 $a_4$，其最高 $\mathscr A$
系数是 $a_8$，但所有更低系数仍须保留。
右边的两个单位可能相消；这里没有称该差为单位。

在 (G2.74) 的额外真实 Bernoulli 分支，
令 $g=G_{p-7}$。同一对象中的 $\Delta_{\rm low}=0$ 还可
准确写成
$$
\begin{gathered}
[v^{p-5}]\frac{\mathscr A}{u}=0,\\
2\left[v^{p-6}\right]
       \frac{\mathscr A'-\mathscr W\mathscr A/2}{u}
 \left[v^{p-9}\right]\frac{\mathscr A}{u}
 +g\left[v^{p-7}\right]\frac{\mathscr B}{u}=0 .
\end{gathered}
\tag{G2.88}
$$
第一式就是原 $\mathcal H_p=0$，第二式是 $24\Delta_{\rm low}=0$。
它使用
$C_3=(\mathscr A'-\mathscr W\mathscr A/2)/u$；
$\mathscr B/u$ 比原 $C_4$ 多的常数在该正次数不贡献。
本式没有引入新的 good 行，也没有把 $\mathscr A$、
$\mathscr B$ 的四个指定系数分别置零。
(G2.83)、(G2.84)、(G2.87) 的 forcing
必须连同这两个原条件一起消费。

### 14.5. 原 odd–odd 配对及两个已付中央相关槽

由 (G2.82)、$e^2=-a$ 和原 (G2.68)，准确得到
$$
\boxed{
\begin{aligned}
\widehat F_{e,4,3}\widehat F_{e,8,1}
 -\widehat F_{e,4,1}\widehat F_{e,8,3}
 &=-\frac a{192}(b_4a_8-a_4b_8),\\
B_{3,1}&=\frac a{8\beta^2}b_4a_8,\qquad
B_{1,3}=\frac{7a}{8\beta^2}a_4b_8 .
\end{aligned}}
\tag{G2.89}
$$
这里的 $B_{k,l}$ 是 R1168.51 的 actual same-kernel
相关项，不是另外构造的 Hankel 矩阵。

还可在两个已经付完整局部读取的中心之间，消掉一个
共同的 even–even 项。定义同一原 frame 中的标量
$$
\mathcal Z_0=[\omega^4\eta^8]Z_{0,\rm corr}^{\rm BCH},
\qquad
\mathcal Z_2=c_\omega^{-2}
               [\omega^2\eta^6]Z_{2,\rm corr}^{\rm BCH}.
$$
R1168、R1169 的 normalized contractions 准确给
$$
\begin{aligned}
\mathcal Z_0&=\frac{B_{4,0}}3+\frac{B_{3,1}}6
                    -\frac{B_{1,3}}6-\frac{B_{0,4}}3,\\
\mathcal Z_2&=\frac{B_{4,0}}3+\frac{5B_{3,1}}{96}
                    +\frac{3B_{1,3}}{224}-\frac{B_{0,4}}{14}.
\end{aligned}
\tag{G2.90}
$$
第二行可逐项由
$(t-s)^2(t^2+12ts+15s^2)
=t^4+10t^3s-8t^2s^2-18ts^3+15s^4$
核准，并除原 $\binom4k\binom8l$。
$k=l=2$ 的 BCH 因子为零，不要求 $B_{2,2}=0$。

原 $\mathcal H_p=0$ 时 $B_{0,4}=0$：
这由 §12 的 even-band trace 和 $F_{4,0}=0$ 得到，
并非增加观测。于是 (G2.89)–(G2.90) 给
$$
\boxed{\qquad
\mathcal Z_2-\mathcal Z_0
 =-\frac{11a}{768\beta^2}
       (b_4a_8-11a_4b_8),
\qquad \mathcal H_p=0 .
\qquad}
\tag{G2.91}
$$
完整 odd–odd 权没有被换成不带权的单一 determinant。

(G2.91) 是两个已登记 **correlation** 槽的具体原配对；
原共同纤维并没有要求它们在参考 CM 点各自为零或相等。
它也不替代 R1172 最低 $\Pi_4$ 槽的
$\lambda_\infty X\gamma_5$、原 cyclotomic 端点和算术
去平滑补项。
本节新增的是指定奇列的完全原源、二次 norm、
首 $p$ 非零 forcing 及其原 mask 下的有限约束；
尚未证明 (G2.87)–(G2.88) 无共同解，
不把任何一个显示的外单位当作最后的非零结论。
全部为纸面推导，无数学程序执行。
