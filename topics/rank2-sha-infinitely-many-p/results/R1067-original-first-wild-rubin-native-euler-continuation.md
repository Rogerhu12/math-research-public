# R1067 续证：原 Euler 的完整 native 窗口与真实中央返回

日期：2026-11-28。接[原文 §§19–21](R1067-original-first-wild-rubin-even-multiplicity.md)及[R1062 的实际 Norm17 来源](R1062-original-translated-miller-jets-and-critical-weight-germs.md)。本篇完整有限返回、既定精度的框架消去及原中央两槽返回已证明；主目标仍未完成。

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


## 24. 除去原 forced 四阶后的实际 Euler 读者

本节只在原 bad 条件推出的 $\mathcal A_p\in T^4\mathcal O_L[[T]]$
范围使用整除；它不把第一 wild Hall 的高赋值改成精确零。
仍取 $p>211$、$s_0=1/(p-1)$，并使用 R1062(G73)--(G85)的
实际 $Na=17$ reference。完整两 Hall germ 记作 $G_{34}$、
$G_2^a$，其中全部中心、原 $\lambda_Q$、$17r$、模型及微分规范不变。
由原文§21和 $Na=17$，
$$
 \mathcal A_p(x(t))=U_{r,0}F(t)^2,\qquad
 F=G_{34}/G_2^a,\qquad
 x(t)=\nu_r(\gamma)q_{\rm ac}^{Mt}-1,\qquad
 U_{r,0}\in\mathcal O_F^\times
 \tag{102}
$$
是原同一个 $\mathcal A_p$ 的等式。$U_{r,0}$ 是已固定常数。
置 $\partial=b_M^{-1}d/dt$、$c=\Delta\log q_{\rm ac}$，
则 $\partial x=c(1+x)$、$v_p(c)=1$。
$\nu_r(\gamma)$ 是本次非平凡第一 wild 字，故
$t_r=x(0)$ 是某个原始 $p$ 次根减一，$v_p(t_r)=s_0$。

### 24.1 非交换连接和准确目标精度

令 $D_T=(1+T)d/dT$、$E_T=D_T^p-D_T$。
由于模 $p$ 时 $D_T^p=D_T$，
$E_T C\in p\mathcal O_L[[T]]$ 对每个整 $C$ 成立。
原 bad 条件给 $B=\mathcal A_p/T^4$ 整，因此真正的新读者是
$$
 \boxed{
 \begin{aligned}
 \mathscr L_r(F^2)
 &:=\left.x^4(\partial^p-c^{p-1}\partial)(x^{-4}F^2)\right|_{t=0}\\
 &=U_{r,0}^{-1}c^p t_r^4(E_TB)(t_r)
       \in p^{p+1}t_r^4\mathcal O_F .
 \end{aligned}}
 \tag{103}
$$
右侧精度为 $p+1+4s_0$。不能把 $\partial$ 与 $x^{-4}$ 交换。
其完整展开可用
$$
 \begin{aligned}
 K_j(x)
  &=c^j\sum_{k=0}^j {j\brace k}(-4)_k
                  \left(\frac{1+x}{x}\right)^k,\qquad K_0=1,\\
 \mathscr L_r(F^2)
  &=\sum_{j=0}^p\binom pj K_{p-j}(t_r)\partial^j(F^2)(0)
       -c^{p-1}\{\partial(F^2)(0)+K_1(t_r)F(0)^2\}.
 \end{aligned}
 \tag{104}
$$
花括号内为第二类 Stirling 数。
特别 $v_pK_j(t_r)\ge j(1-s_0)\ge0$。
等价地，令 $\nabla_4=\partial-4c(1+x)/x$，则
$\mathscr L_r(F^2)=(\nabla_4^p-c^{p-1}\nabla_4)F^2|_0$；
这一表达右边没有再乘一个 $x^4$。

### 24.2 完整浅部只有两个原系数

无须 bad，R303 已给原 $\mathcal A_p\in T^2\mathcal O_L[[T]]$。
准确写成
$$
 \mathcal A_p=\mathfrak a_2T^2+\mathfrak a_3T^3+T^4C(T),\qquad
 \frac{\mathcal A_p}{T^4}=\mathfrak a_2T^{-2}+\mathfrak a_3T^{-1}+C(T).
$$
对 $k=1,2$，由
$D_T^p=\sum_{j=1}^p{p\brace j}(1+T)^j(d/dT)^j$，
中间 $2\le j<p$ 的 Stirling 系数均被 $p$ 整除。
又因 $(1+t_r)^p=1$，逐项准确得到
$$
 \begin{aligned}
 E_T(T^{-1})(t_r)&=-p!\,t_r^{-p-1}+R_1,
       &v_pR_1&\ge-s_0,\\
 E_T(T^{-2})(t_r)&=-(p+1)!\,t_r^{-p-2}+R_2,
       &v_pR_2&\ge-s_0.
 \end{aligned}
 \tag{105}
$$
所以两式的精确赋值分别为 $-2s_0$、$-3s_0$。
第二式中 $j=p-1$ 的 $p!$ 也必须保留；其赋值为
$1-2s_0>-s_0$，其余中间项由上述界控制。

关键是原 $\mathfrak a_2,\mathfrak a_3$ 属于**未分歧**的 $\mathcal O_L$，
故其非零赋值为整数。两种浅部的赋值不可能相同：
整数之差不能等于 $s_0$。
而 $(E_TC)(t_r)\in p\mathcal O_F$。
因此下述是双向等价，不只是充分条件：
$$
 \boxed{
 \mathscr L_r(F^2)\in p^{p+1}t_r^4\mathcal O_F
 \quad\Longleftrightarrow\quad
 \mathfrak a_2,\mathfrak a_3\in p^2\mathcal O_L .
 }
 \tag{106}
$$
若把 $\mathcal A_p$ 改成任意分歧系数域上的整函数，
上述不抵消论证不再自动成立；本文始终是原 R303 的整系数。
式(106)也说明，不能把目标增加的 $4s_0$ 算成四个自由新行。
对所有非平凡第一 wild 标签 $r$，右侧都是同一个
$\mathfrak a_2,\mathfrak a_3\in p^2\mathcal O_L$；逐标签重写完整读者
不会增加独立必要行。

这个范围确实比单纯的局部低导数界强。仅作逻辑核对，取
$A_{\rm toy}(T)=(T^2+pT)^2$。
它整、$\mu=0$，所有零都是偶重数；
在 $t_r$ 处的第 $k$ 个 normalized 导数
$c^kD_T^kA_{\rm toy}$ 对 $0\le k\le4$ 均满足
$k+(4-k)s_0$ 的下界，其 $T^2$ 首系数赋值也是偶数2。
但 $A_{\rm toy}/T^4=1+2pT^{-1}+p^2T^{-2}$，
其 $E_T$ 值的唯一最浅项为
$-2p\,p!t_r^{-p-1}$，赋值 $1-2s_0<1$。
它不满足(106)。这只是排除“已列低门形式上蕴含新读者”，
没有把 toy 认作原来源，也没有赋予它未核的原 functional equation。

## 25. 同一个完整来源所需的实际有限窗口

(104)的所有系数在 $\mathcal O_F$。
所以将完整 $F^2$ 的全部 $0,\ldots,p$ 阶 jet 算到
$p^{p+2}$，便足以判定(103)的 $p+1+4s_0$ 模数。
原 reference mass 是单位；整三角商递推不再损失精度。

### 25.1 未移角的真实 log/native 窗口

原(94)的同一个 gauge 论证，现在给
$$
 \begin{aligned}
 \boldsymbol\mu((\log u)^k)
 &\equiv\sum_{n=k}^{p+4}\frac{k!\mathfrak s(n,k)}{n!}
       \sum_{j=0}^n(-1)^{n-j}\binom nj M_j
                           \pmod{p^{p+2}},\qquad1\le k\le p,\\
 M_j&\equiv\sum_{i=1}^j C_{ji}a_{i\Delta}\pmod{p^{q-3}},
       \qquad 1\le j\le p+4,\qquad v_pC_{ji}\ge i-2 .
 \end{aligned}
 \tag{107}
$$
$C_{ji}$ 是(96)的原精确 Lagrange 系数，不改变公式。
对 $n\ge p+5$，log 尾的下界
$\lfloor n(1-\tau)\rfloor-v_p(n!)+v_p(k!)$ 至少 $p+2$：
其线性下界在 $n=p+5$ 严格超过 $p+1$，
差为 $(p^2-11p-8)/\Delta>0$，以后递增。
$n\le p+4<2p$ 的显示系数至多带一份 $p^{-1}$，
所以各 $M_j$ 输入精度须为 $p^{p+3}$。
在新增的 $j=p+4$，仍有
$v_p((j\Delta)!)-pj=j-2$，并完整保留 $j=p$ 的 $1/j$；
(95)的严格 log 高项误差也仍至少为 $q-3$。

代入原(97)全 carry 后，只需
$t\le p+4-i$、$l\le i-1$，所以本次 actual
$R^a_{T,l+t}$ 的最大指标是 $p+3=d+2$。
绝不把这一结论缩回旧的 $p+2$。

### 25.2 第一连接必须留下，全部更高尾可以真截断

(101)只有 $p^{p+1}$ 精度，在本节不能继续用它删除框架。
也不能将完整 $G_N$ 直接换成 bare $\mathcal M_N$。
R1066(N7)--(N11)给准确的首块返回
$$
 \begin{aligned}
 G_N(t)
 &=\mathcal M_N(t)+\mathfrak b_{N,d}p^d(Mt)_d\,
          \boldsymbol\mu_N[X^{-d}u^{b_Mt}]
          +\mathcal R_N(t),\\
 \mathfrak b_{34,d}&=34c_\sigma,\qquad
 \mathfrak b_{2,a,d}=2a^d c_\sigma,\\
 \partial^j\mathcal R_N(0)&\in p^{p+2}\mathcal O_F
                    \qquad(0\le j\le p).
 \end{aligned}
 \tag{108}
$$
reference 的 $a^d$ 是实际物理缩放，不能用 $Na=17$ 换掉。
首块有正号；它来自整个
$(z/v)^N E_{\rm c}(z)^N$ 的真实系数。
对全部其余支撑 $h\ge2d$，
$$
 h-\lfloor h\tau\rfloor-\lceil h\tau\rceil\ge2p-3>p+2 .
$$
falling factorial 的各导数整，而 $\log u$ 在原 completed gauge
中整，因此该界同时支付本次所有 $p$ 阶以内导数。

首块的 shifted log 测试也有一个小的、完整的 native 返回。
令
$$
 \begin{aligned}
 V_k&=p^{-pk}D^{k\Delta-d}P_H(0),\qquad1\le k\le5,\\
 \beta_{j,n}&=[z^n]\frac{\log(1+z)^j}{1+z},\\
 \boldsymbol\mu[X^{-d}(\log u)^j]
 &\equiv\sum_{n=0}^4\beta_{j,n}
       \sum_{i=0}^n(-1)^{n-i}\binom ni V_{i+1}
                                      \pmod{p^2}.
 \end{aligned}
 \tag{109}
$$
若 $j\ge5$，右侧为0。这里用的恒等式是
$X^{-d}=p^{-p}X^{\Delta-d}u^{-1}$。
原 gauge 对被截项给
$\lfloor n(1-\tau)\rfloor-2-v_p(n!)\ge2$（$n\ge5$），
所以(109)不是将一个 $p^{-p}$ 当作单位。
显示的 $n\le4$ 系数全整。
因 $\mathfrak b_{N,d}p^d$ 的估值为 $p$，
(109)正好支付(108)所需的 $p^{p+2}$ 输出精度。

这里的 $V_k$ 继续由同一 strict LT 逆代换读取：
$$
 V_k\equiv
 p^{-pk}(k\Delta-d)!
 \sum_{\ell=1}^k
 \frac{\ell\Delta-d}{k\Delta-d}
 \binom{-(k\Delta-d)}{k-\ell}\ell_q^{\,k-\ell}
       a_{\ell\Delta-d}\pmod{p^{q-3}} .
$$
$k\le5$ 时 $p\nmid k\Delta-d$，
$v_p((k\Delta-d)!)-pk=k-3$，故第 $\ell$ 项系数
至少为 $\ell-3$。
按 $p^2$ 精度用原 G50 展开它，仅需
$t\le4-\ell$、$l\le\ell-1$；这里 actual 乘子指标至多3。
所以首连接没有把(107)所需的最大窗口继续增大。

### 25.3 新增第三个 frame 校正与最终读取顺序

由于 $p+3<2d$，原 $K_a(w)=1+k_1w^d+O(w^{2d})$ 直接给
$$
 \boxed{
 \begin{aligned}
 R^a_{T,k}
 &=\epsilon_Q(h_{Q,k}-k_1h_{Q,k-d}),
            &&0\le k\le p+3,\\
 h_{Q,k}&=[w^k]H_a(w\oplus Q),&
 k_1&=(34-2a^d)c_\sigma .
 \end{aligned}}
 \tag{110}
$$
除旧 $k=d,d+1$ 的两项外，本次明确增加
$k=d+2$ 的第三项 $-k_1h_{Q,2}$。
此窗全在 $k<q$，故也可写 $h_{Q,k}=D^kH_a(Q)/k!$，
但必须保 $k!$。
原 $\lambda_Q\epsilon_Q=\lambda'_{[a]Q}$、全 independent Hall
和及实际 reference $A_{2,T'}([a]v)$ 仍沿(97)保留。

实际顺序是：由(110)和 full carry 得 native 系数；
用(107)、(109)得 bare 与 shifted log jet；
以(108)恢复全部第一连接；
对未删改的参考作整三角商及平方；
最后代(104)。没有沿用较浅的(101)消项，
也没有把 $H_a(Q)$ 从 Hall 求和中提出。
本节给的是同一原来源的明确有限读者。
它在(106)已精确降为两个原系数条件；
下一节继续把这两个条件送回原 canonical Newton 读数，
判断实际增加了哪一层精度。


## 26. 原平凡有限角色的中央 germ 与第三个 Rubin 系数

本段沿 R303 的同一个 $\mathcal A_p$、同一个 signed 整基及
$E_{17}/E_1$ 的模型同构，不另换 Rubin 函数。取
$p>211,\ p\equiv5\bmod6$，$d=p+1$，
$\vartheta^6=17$，并记
$J=J_p$、$J_0=J_{0,p}$ 为 R303(4) 的两条原完整 Newton 函数。
特别 $J(0)=0$、$J_0(0)=1$，且
$J\in pu\mathbf Z_p\langle u\rangle$、
$J_0\in1+p\mathbf Z_p\langle u\rangle$。

### 26.1 平凡有限角色下的实际比较标量

把§21(83)--(88)的同一 CM-pair tensor 图用于 $\nu=1$。
共同模数现在为 $34\delta$；不再带两边公共的 $p^2$ 标记及
分歧 Artin 线。原(84a)的 Betti/Tate 基方块仍系数1，
而原模型微分仍一次给 $\vartheta^{-(2m+1)}$。
共同 $p$ Euler 因子此时是 $1+1/p$，赋值为 $-1$，
须在两图均保留后才相消；参考的原十七处因子仍为 $18/17$。
公共 Gamma/Tate 因子及同一辅助 smoothing 也按原图先保后消。
因此对 $m>0,\ d\mid m$，
$$
 \mathcal A_p(q_{\rm ac}^m-1)\mathscr E_{1,m}
  =\kappa_1\vartheta^{-(2m+1)}\mathscr E_{17,m},
 \qquad \kappa_1\in\mathcal O_F^\times .
 \tag{111}
$$
$\kappa_1$ 是这一平凡 Artin 图中原固定 primitive 基的相对常数，
在对椭圆单位类取值之前定义；不以零的目标临界值求商。
§21已逐图说明余相对费用只有该常数与显示的 tensor 幂。
此处没有事后乘一份未标记的 $\Lambda^\times$。
也不需要断言 $\kappa_1$ 与所有 wild 标签的 $\kappa_r$ 数值相等：
两种情况沿用相同的模型权幂，有限 Artin 的固定标记仍各自保持。

R303(22)给
$\mathscr E_{17,m}/\mathscr E_{1,m}
 =6\kappa_0\,17^{-m}s_m^2/\beta_m^2$，
其中 $\kappa_0=48940416$，且
$s_m=\vartheta^{m-6}\alpha_m$。
所以(111)右端的完整物理比为
$6\kappa_0\kappa_1\vartheta^{-1}17^{-m-2}
 \alpha_m^2/\beta_m^2$。
再在 $m=dk$ 用 R303(23)的两个准确有限卷积：
$\alpha_{dk}/\beta_{dk}=17^kJ(k)/J_0(k)$。
两个 $k!$ 和原 Gaussian 倍率在这里都已经准确相消。
得到
$$
 \boxed{
 \mathcal A_p(q_{\rm ac}^{du}-1)
   =C_0\,17^{-(p-1)u}
          \left(\frac{J(u)}{J_0(u)}\right)^2,\qquad
 C_0=\frac{6\kappa_0\kappa_1}{17^2\vartheta}
                  \in\mathcal O_F^\times .
 }
 \tag{112}
$$
整数 $k\ge1$ 时，这先是同一原类的精确等式。
因 $17^{-(p-1)}\in1+p\mathbf Z_p$、$q_{\rm ac}\in1+p\mathcal O_L$，
右侧是闭单位盘上的真实 Tate 解析函数，参考 $J_0$ 可逆；
左侧也因 $q_{\rm ac}^{du}-1\in p\mathcal O_L\langle u\rangle$ 而解析。
正整数点稠密，故(112)在整个盘成立，随后才允许求导。

这里 $17^{-m}$ 是§21的原物理权；$17^{2k}$ 是两条不同 charge
的 Newton 返回。二者合成 $17^{-(p-1)k}$，不能漏掉后一项，
也不能把 wild 的 physical 参数直接改名为本段的 $u$。
R303已证 $J\ne0$，故存在正整数 $k$ 使 $J(k)\ne0$。
在该点读取已定义的(112)，还给 $C_0\in L$；
连同原单位性质，实际有 $C_0\in\mathcal O_L^\times$。
这一步只确定常数所在的域，没有用它重新定义该常数。

### 26.2 保全部参考、权幂和参数变换的二、三系数

写
$$
 \begin{gathered}
 J(u)=j_1u+j_2u^2+O(u^3),\qquad
 j_1=J'(0),\quad j_2=J''(0)/2,\\
 J_0(u)=1+b_1u+O(u^2),\qquad
 h=d\log q_{\rm ac},\qquad w_{17}=(p-1)\log17 .
 \end{gathered}
$$
$v_p(h)=1$，$b_1,w_{17}\in p\mathcal O_L$。
令 $\mathfrak a_i=[T^i]\mathcal A_p(T)$。
从 $T=\exp(hu)-1$、$u=h^{-1}\log(1+T)$，(112)逐项准确给
$$
 \boxed{
 \begin{aligned}
 \mathfrak a_2&=\frac{C_0j_1^2}{h^2},\\
 \mathfrak a_3&=
 \frac{C_0j_1}{h^3}
   \left\{2j_2-(2b_1+w_{17}+h)j_1\right\}.
 \end{aligned}
 }
 \tag{113}
$$
其中 $2b_1$ 来自真实参考的倒数平方，
$w_{17}$ 来自原物理权，$h$ 来自反参数的二阶项。
没有将其中任何一项先设为零，也没有假设
$\mathfrak a_3=-\mathfrak a_2$ 的未付 inversion 规范。

原反圆分单位满足 $\bar q_{\rm ac}=q_{\rm ac}^{-1}$，故 $\bar h=-h$。
(112)中除 $C_0,h$ 外的中央函数系数都在 $\mathbf Q_p$。
令 $\iota(T)=-T/(1+T)$，于是同一实际式还严格给出
$$
 \overline{\mathcal A_p}(\iota(T))
   =\lambda_0\mathcal A_p(T),\qquad
 \lambda_0=\bar C_0/C_0;\qquad
 \overline{\mathfrak a_2}=\lambda_0\mathfrak a_2,\quad
 \overline{\mathfrak a_3}
       =-\lambda_0(\mathfrak a_3+2\mathfrak a_2).
$$
这里是系数的非平凡共轭，而不是删除它后的线性 inversion。
归一后的 $(\mathfrak a_3+\mathfrak a_2)/C_0$ 仍有真实的反不变方向；
因此这一已推导的关系也不允许将第三系数替成第二系数的负号。

### 26.3 原来源的完整尾使第三系数返回两条实际 Gaussian 槽

仍在 R303 的 $E_1$ 来源 $A(z)=\sum\alpha_mz^m$ 上，明确记
$c_\sigma=[z^d]\log(\sigma(z)/z)$；它与(108)的原 sigma 常数相同，
不同于§24的 $c=\Delta\log q_{\rm ac}$。置
$$
 \gamma=34pc_\sigma\in\mathbf Z_p^\times,\qquad
 g_r=[z^{dr}]\{A(z)e^{-34c_\sigma z^d}\},\qquad
 N_r=\left(\frac p\gamma\right)^r g_r .
 \tag{114}
$$
这样 $J(u)=\sum_{r\ge1}N_r(u)_r$。
$N_r$ 是 Newton 系数，不能与 $\mathfrak a_i$ 混用。

R614(21)给 $g_r$ 在 $1\le r\le p-1$ 全整。
该文的 $b=17$ 与本段 $b=1$ 由 R301(2)的已付单位齐次缩放相接；
Gaussian 的同次幂也一起运输，故这里没有换来源。
特别 $N_3\in p^3\mathbf Z_p$。
对全部 $r\ge4$，R301(20)的全系数界为
$$
 v_p(N_r)\ge
 \left\lceil\frac{r(p-1)+6}{2p}\right\rceil\ge3 .
$$
该下界随 $r$ 趋于无穷；每个 $(u)_r$ 的普通系数是整数。
所以完整 $r\ge3$ 尾在 $p^3\mathbf Z_p\langle u\rangle$ 内，
而非只某个有限截断如此。因此
$$
 \boxed{
 \begin{aligned}
 j_1&\equiv \frac p\gamma g_1
                   -\frac{p^2}{\gamma^2}g_2\pmod{p^3},\\
 j_2&\equiv \frac{p^2}{\gamma^2}g_2\pmod{p^3},
       \qquad j_2\in p^2\mathbf Z_p .
 \end{aligned}
 }
 \tag{115}
$$
$g_1=\alpha_d$，但 $g_2=\alpha_{2d}-34c_\sigma\,\alpha_d$
是带真实 Gaussian 的完整整组合；不得只保 $\alpha_{2d}$。

### 26.4 新 localized 门在同一中央来源上的准确含义

由(113)、$v_p(h)=1$，首先
$\mathfrak a_2\in p^2\mathcal O_L$ 当且仅当
$j_1\in p^2\mathbf Z_p$。
在这个范围内，(113)中
$(2b_1+w_{17}+h)j_1^2/h^3$ 的赋值至少为2。
所以
$$
 \boxed{
 \begin{aligned}
 \mathfrak a_3
   &\equiv \frac{2C_0j_1j_2}{h^3}\pmod{p^2\mathcal O_L},\\
 (\mathfrak a_2,\mathfrak a_3)\in p^2\mathcal O_L^2
   &\iff
       j_1\in p^2\mathbf Z_p
       \ \text{且}\ j_1j_2\in p^5\mathbf Z_p .
 \end{aligned}
 }
 \tag{116}
$$
若 $j_2/p^2$ 为单位，第三系数条件准确返回
$j_1\in p^3\mathbf Z_p$；若 $j_2\in p^3\mathbf Z_p$，
它在 $j_1\in p^2\mathbf Z_p$ 下自动成立。

进一步，$j_1\in p^2$ 等价于 $g_1\in p$；
在此范围内由(115)把(116)写成同一个原有限来源的式
$$
 \boxed{
 \left(
   \frac{g_1}{p\gamma}-\frac{g_2}{\gamma^2}
 \right)
 \frac{g_2}{\gamma^2}\equiv0\pmod p .
 }
 \tag{117}
$$
第一个因子是原 $j_1/p^2$ 的真实第二位，第二个因子是
原 $j_2/p^2$ 的首位。两个因子使用同一 $A$、同一 Gaussian 和
同一个 $c_\sigma$，并非环境中两条可以独立指定的行。

在真正的 canonical 坏假设 $j_1=J'(0)=0$ 下，(113)给
$\mathfrak a_2=\mathfrak a_3=0$ 的精确恒等。
在只知道首层失败时，(116)则未必自动；
它准确成为“原首导数再深一位”或“原二阶系数已深一位”的选择。
因此不能把新的 localized 表达式额外计作与全部原 Newton
必要行独立的 forcing。它提供的是一个已付来源的非线性返回，
而不是假定坏条件对任意乘法封闭。
