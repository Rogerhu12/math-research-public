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
