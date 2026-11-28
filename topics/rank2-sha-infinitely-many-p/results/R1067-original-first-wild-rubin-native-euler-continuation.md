# R1067 续证：原 bare Euler 读者的完整 native 窗口

日期：2026-11-28。接[原文 §§19–21](R1067-original-first-wild-rubin-even-multiplicity.md)及[R1062 的实际 Norm17 来源](R1062-original-translated-miller-jets-and-critical-weight-germs.md)。本篇有限返回与框架消去已证明；主目标仍未完成。

本文件续接 R1067 §§19--21，使用同一原 Hall 来源、原 Katz dual、
原 $\mathcal A_p$ 与同一个 normalized weight 导子 $\partial$。
它把实际 Euler 表达压到原固定来源的有限系数，并支付其中
exact-norm 框架费用的消去；尚不宣称剩余行与已有条件独立。

## 22. 所有 p 阶 jet 共用一个真正的有限 native 窗口

继续写 $q=p^2$、$\Delta=q-1$、$d=p+1$、
$\tau=p/\Delta$，$X=c_1$、$u=X^\Delta/p^p$。
本节的 $\boldsymbol\mu$ 是 R1065--1067 已构造的原整 Hall dual，
或 R1062(G83)的实际 norm-$17$ reference dual。
其 norm 不超过1。标量扩张、全 Haar 和原中心仍按原定义；
下列积分不是把 $\mathbf C_p$ 值函数免费当作普通测度测试。

记
$$
 P_H(v)=\sum_{n\ge0}a_n v^n,\qquad
 M_j=\boldsymbol\mu(u^j)
   =p^{-pj}D^{j\Delta}P_H(0),\qquad M_0=a_0 .
 \tag{93}
$$
这些是同一 actual dual 的矩；使用任意非负整数 $j$ 只为读取该
有限系数身份，不增加新的 automorphic 零条件。

### 22.1 原对数尾：所有 k≤p 同时截到 p+3

令 $\mathfrak s(n,k)$ 为带符号第一类 Stirling 数。
对 $1\le k\le p$，原测试给
$$
 (\log u)^k
 =\sum_{n\ge k}\frac{k!\mathfrak s(n,k)}{n!}(u-1)^n .
$$
R1066(N4)的实际 gauge 是
$(u-1)^n\in p^{\lfloor n(1-\tau)\rfloor}\mathscr C_{\rm Gal}$
（在原完成标量扩张后同样使用）。
因此第 $n$ 项的整 gauge 估值至少
$$
 \lfloor n(1-\tau)\rfloor-v_p(n!)+v_p(k!).
$$
对所有 $n\ge p+4$，由 Legendre 界得它严格大于
$n(1-\tau-(p-1)^{-1})-1$。
后者在 $n=p+4$ 已严格大于 $p$：
差为 $(p^2-9p-7)/\Delta>0$。
整 gauge 故至少 $p+1$，并随该线性下界趋于无穷。
于是同一实际 dual 无损给
$$
 \boxed{
 \boldsymbol\mu((\log u)^k)
 \equiv
 \sum_{n=k}^{p+3}\frac{k!\mathfrak s(n,k)}{n!}
       \sum_{j=0}^{n}(-1)^{n-j}\binom nj M_j
 \pmod{p^{p+1}\mathcal O_F}.
 }
 \tag{94}
$$
因 $p+3<2p$，显示的系数至多带一份 $p^{-1}$。
所以按 $p^{p+2}$ 精度输入各 $M_j$，足够支付(94)所需的
$p^{p+1}$ 输出精度。特别不以 pointwise 的小范数代替 gauge。

### 22.2 原严格 LT 逆代换，而非把高 Lie 矩当 ordinary 系数

写
$$
 z(v)=\sum_{h\ge0}\ell_hv^{1+h\Delta},\qquad
 \ell_0=1,\qquad\ell_1=\ell_q=(p^q-p)^{-1}.
$$
从 $z(pv-v^q)=pz(v)$ 逐系数准确得到
$$
 (1-p^{h\Delta})\ell_h
  =\sum_{a=1}^{h-1}
       (-1)^{h-a}\binom{1+a\Delta}{h-a}p^{aq-h}\ell_a
      \quad(h\ge2).
 \tag{95}
$$
故在本次需要的 $2\le h\le p+2$ 有
$v_p(\ell_h)\ge q-h-1$；这是由(95)按 $h$ 归纳的原严格参数界。

Lagrange 逆代换给
$$
 [z^{j\Delta}]v(z)^{i\Delta}
   =\frac ij[v^{(j-i)\Delta}](z(v)/v)^{-j\Delta}.
$$
对 $1\le i\le j\le p+3$，含某个 $\ell_h$、$h\ge2$ 的项，
连同外部 $p^{-pj}(j\Delta)!$，估值至少 $q-3$。
确实：其内部估值至少 $q-(j-i)-1$，
$v_p((j\Delta)!)-pj=j-2$，而 $v_p(j)\le1$。
所以本次 full native 返回是
$$
 \boxed{
 \begin{aligned}
 M_j&\equiv\sum_{i=1}^{j}C_{ji}a_{i\Delta}
                  \pmod{p^{q-3}\mathcal O_F},\\
 C_{ji}
  &=p^{-pj}(j\Delta)!\,
      \frac ij\binom{-j\Delta}{j-i}\ell_q^{\,j-i},\\
 v_p(C_{ji})&\ge i-2,\qquad1\le j\le p+3 .
 \end{aligned}}
 \tag{96}
$$
其中 $(i/j)\binom{-j\Delta}{j-i}$ 为整数：它就是整形式逆
$v+\ell v^q$ 的 $v^{i\Delta}$ 对应系数中的 $\ell^{j-i}$ 系数。
这一点同时保留 $j=p$ 的可能 $1/j$，未将其漏掉。
$j=p,p+1,p+2,p+3$ 的阶乘均仍给
$v_p((j\Delta)!)-pj=j-2$；$j>p$ 时三层 Legendre 项必须同算。
$a_0$ 不进入正次 Lie 导数。

### 22.3 所需的实际乘子最多只有 p+2 阶

在 R1062(G50)的 actual norm-$17$ 规范中，
reference 必须是 $A_{2,T'}([a]v)$，不能继续用 $[\beta]$ 版本。
记其整 native 系数为 $r_{Q,n}^{a}$。
用 $k=l+t$ 改写完整 carry，准确有
$$
 a_{i\Delta}
 =\frac1{\sqrt d}\sum_Q\lambda_Q
   \sum_{\substack{l,t\ge0\\ql+t\le i\Delta}}
       (-1)^l\binom{l+t}{l}p^t R^a_{T,l+t}\,
                 r^a_{Q,i\Delta-ql-t}.
 \tag{97}
$$
所有 $q$ 次 carry 都在式中。
代入(96)并按 $p^{p+2}$ 精度保留时，
$v_p(C_{ji})\ge i-2$ 说明只需
$$
 t\le p+3-i,\qquad l\le i-1 .
$$
于是 $l+t\le p+2$。结合(94)，**整个**原 bare
$p$ 阶 Euler 表达（包括全部低阶商导数及混合项），
只需要原 $R^a_{T,k}$ 的 $0\le k\le p+2$：
$$
 \boxed{
 R^a_{T,k}
  =\epsilon_Q\{h_{Q,k}-k_1h_{Q,k-d}\},\quad
 h_{Q,k}=[w^k]H_a(w\oplus Q),\quad
 k_1=(34-2a^d)c_\sigma .
 }
 \tag{98}
$$
这是 R1062(G85)的真实表。负指标为0，
$h_{Q,k}=D^kH_a(Q)/k!$ 仅在这里的 $k<q$ 窗中使用，
并保整个 $k!$。
原有限词已证明 $\lambda_Q\epsilon_Q=\lambda'_{[a]Q}$，
所以(97)--(98)准确回同一 reference covector 与同一个
$H_a(w)=S_{34}(z(w))/\Theta_2(a z(w))$ 的加法系数。
它没有未知的逐 $Q$ 单位，也没有从求和中提出 $H_a$。

输入(94)以后，用R1067(79)的整三角商递推读取所有商 jet。
参考 mass 是原实际单位，故这个递推不损失精度。
最后按(74)代入全部整数多项式；没有选择若干 jet 自由赋值。
这是一份精确有限算式，尚未在本节把其余数宣告为零或非零。

## 23. exact-norm 的首 Fermat 框架项在当前 Euler 精度自动消去

令
$$
 \widetilde P_H(v)=K_a(P(v))P_H(v).
$$
$K_a$ 和逆是原整单位，$\varphi K_a$ 在完整 $p$ 核下不变；
所以乘后仍是同一非平凡 kernel 角色的整 Katz 来源。
对整个 Hall 和亦然。R1062(G83)给它的准确来源：
$$
 \widetilde P_H(v)
 =\frac1{\sqrt d}\sum_Q\lambda'_{[a]Q}
       A_{2,T'_{[a]Q}}([a]v)\,H_a(P(v)\oplus Q).
 \tag{99}
$$
原未乘的 $P_H$ 仍由 $K_a(P(v))^{-1}$ 准确恢复；
下面只比较同一 Euler 精度，不把两测度命名为相同。

置 $B(z)=K_a(v(z))=\sum b_hz^h$。
R1062(G76)和严格 LT 变量给
$b_0=1$、$b_d=k_1\in\mathcal O_L$、其余非零次数都是 $d$ 的倍数。
由原 $u\leftrightarrow v$ 在严格 $R<R_E$ 的等距返回及
$K_a^{\pm1}$ 整性，
$v_p(b_h)\ge-\lfloor h/\Delta\rfloor$。
原 $[p]$ pull 乘法对 Lie 矩严格转置为
$$
 \widetilde{\mathcal M}(s)-\mathcal M(s)
 =k_1p^d(\Delta s)_d\,
        \boldsymbol\mu[X^{-d}u^s]
 +\sum_{\substack{h\ge2d\\d\mid h}}
      b_hp^h(\Delta s)_h
        \boldsymbol\mu[X^{-h}u^s].
 \tag{100}
$$
这里先对整数 $s$ 作实际有限 Leibniz 返回，再在原共同 weight
分量上读 germ；不能把 $p^{-ps}$ 单独当作解析函数。
$s=b_Mt$，所以它的 $s$ 导数就是原 $\partial$。

所有 $h\ge2d$ 项连同任意不超过 $p$ 阶的归一导数，
整 gauge 至少
$$
 h-\lfloor h/\Delta\rfloor-\lceil h\tau\rceil
 \ge h(1-(p-1)^{-1})-1>p+1.
$$
对 $u^s$ 求导产生 $\log u$，它在同一 completed gauge 中为整，
故该全尾不变浅。这里只用了原 unit-coset 测试，不把普通
$\mathbf C_p$ 范数当作整范数。

首项记 $P_*(m)=(m)_d$。原§19已经给
$P_*^{(p)}(0)=-p!p(p+1)/2$，估值为2；
且 $P_*\bmod p=m^{p+1}-m^2$。
$X^{-d}$ 的 gauge 费用为 $p^{-2}$，因此前因子 $p^d$
剩 $p^{p-1}$。第 $p$ 导数中：

- 纯 $P_*^{(p)}$ 项至少 $p+1$；
- $3\le j\le p-1$ 的 $P_*^{(j)}$ 另含 $p$，
  Leibniz 的 $\binom pj$ 也含 $p$，仍至少 $p+1$；
- $j=1,2$ 剩余的 $(\log u)^{p-j}$ 用(94)同一 gauge
  分别至少 $p-3$，故更深；
- $j=0$ 因 $P_*(0)=0$ 消失。

于是
$\partial^p(\widetilde{\mathcal M}-\mathcal M)(0)\in p^{p+1}$。
同一计数给一阶差至少 $p$，二、三阶差至少 $p-1$，
$4\le j\le p-1$ 的差至少 $p$。
把商平方的交叉项完全写出。令
$$
 \delta=\widetilde{\mathcal M}-\mathcal M,\qquad
 A=\frac{2\mathcal M}{(\mathcal M_2^a)^2},\qquad
 B=(\mathcal M_2^a)^{-2};
 \quad
 \left(\frac{\widetilde{\mathcal M}}{\mathcal M_2^a}\right)^2
 -\left(\frac{\mathcal M}{\mathcal M_2^a}\right)^2
       =A\delta+B\delta^2 .
 \tag{100a}
$$
所有 jet 均在0读取。已有
$\delta_0=0$、$v_p\delta_p\ge p+1$、
$v_p\delta_1\ge p$、$v_p\delta_2,v_p\delta_3\ge p-1$，
以及 $v_p\delta_j\ge p$（$4\le j\le p-1$）。
§20的实际 target/reference 低导数界及原参考单位给
$A^{(p-2)},A^{(p-3)}\in p\mathcal O_F$；
其余本次使用的 $A,B$ jet 均整。
在 $(A\delta)^{(p)}$ 中，纯 $\delta_p$ 项已深；
每个真正 mixed 项都有 $\binom pj$ 的一份 $p$。
$j=2,3$ 还用上述两项 $A$ 导数补一份 $p$，
其余 $1\le j\le p-1$ 自动达到 $p+1$。
在 $(B\delta^2)^{(p)}$ 中，每个非零项至少含两个正次
$\delta$ jet，故估值至少 $2p-2\ge p+1$。
最后，平方差的一阶导数至少 $p$；乘 $c^{p-1}$ 后也足够深。
因此，记 $\mathcal M_2^a$ 为未改动的原 scaled reference，有
$$
 \boxed{
 \begin{aligned}
 &(\partial^p-c^{p-1}\partial)
       \left(\frac{\widetilde{\mathcal M}}{\mathcal M_2^a}\right)^2(0)\\
 &\hspace{10mm}\equiv
   (\partial^p-c^{p-1}\partial)
       \left(\frac{\mathcal M}{\mathcal M_2^a}\right)^2(0)
       \pmod{p^{p+1}\mathcal O_F}.
 \end{aligned}}
 \tag{101}
$$
这与§20的原完整 connection 消去相容。
又因§21及 $Na=17$ 给 $\mathcal U_r^a(t)=U_{r,0}$，
当前真实 Euler 剩余已经回到(99)的同一整来源。

(101)严格说明：原 Fermat-$17$ 项在 exact-norm 规范中进入的
$k_1$ frame 修正，不是这一级模数上的新增 forcing。
这个结论甚至不需要中央 bad 条件。
它并未证明(99)剩下的 $H_a$ 加法行自动满足全部更深必要条件；
也未用六重零、整性或一个非零字代替该行的实际求值。
