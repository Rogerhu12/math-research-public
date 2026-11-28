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

## 27. 同一原半权热来源的 Riccati 系数与两行共同分子

本节把(114)--(117)的两条实际 Gaussian 槽，返回同一个固定
水平质量函数和同一 Gauss--Manin 方程的两个有限系数。
其用途是给出保全部阶乘和所需三位精度的可执行输入；
没有把这次返回本身当成新的 canonical 必要零行。

取 $p>211,\ p\equiv5\pmod6$，仍记 $d=p+1$、
$N=d/2$。本节另要求 $p$ 是
[固定代数水平格](../notes/2026-11-16-algebraic-horizontal-theta-frame-and-original-divided-rows.md)
§5 的好素数：即排除该文已经固定、先于 $p$ 的有限整模型坏集
$\Sigma_{\rm flat}$。这里不新增随 $p$ 选择的 cover、分母或来源。
以下所有求导和整性都在同一个所选好整模型及其原 CM 点进行；
没有把这个有限坏集未经计算改称为空。

### 27.1 原 $S_{34}$ 的固定水平质量

物理曲线及参数导子分别为
$$
 y^2=x^3-\frac{g_2x}{4}-\frac{g_3}{4},\qquad
 L_2=6g_3\partial_{g_2}+\frac{g_2^2}{3}\partial_{g_3}.
$$
固定 $P:(g_2,g_3)=(0,-4)$，所以物理纤维是本续证§26的
$E_1:y^2=x^3+1$。原截面准确为
$$
 \begin{aligned}
 S_1(z)&=\sigma_1(z)^{34}R_S(x(z)),\\
 R_S(x)&=\frac{x^2}{7}(x^3+1)(x^3-8)
                   (7x^6-4x^3+16),\\
 S_1(z)&=z^6+O(z^{12})\in z^6\mathbf Q[[z^6]] .
 \end{aligned}
 \tag{118}
$$
$\sigma_1$、原 $c_\sigma$ 和§26的 $g_1,g_2,\gamma$ 均不改变。
特别本节参数 $g_2$ 与 Gaussian 第二槽 $g_2$ 是两种对象；
在同时出现时第二槽写作 $g_{2,p}$。

令 $\mathscr V_{34}=H^0(E,\mathcal O(34O))$，使用 R855 的完整
连接
$$
 \mathcal H_{34}R
   =\mathcal LR-\frac{33}{2}xR-\frac{D_z^2R}{68}.
$$
在上述固定有限 étale 覆盖上取原水平基 $h_{34,a}$，
其质量为 $f_{34,a}=\varepsilon_{34}(h_{34,a})$。
先在固定点 $\widetilde P$ 展开整个原向量
$R_S=\sum_a\gamma_a h_{34,a}|_{\widetilde P}$，再固定这些
代数常数 $\gamma_a$，定义
$$
 R_S^{\rm flat}=\sum_a\gamma_a h_{34,a},\qquad
 \mathfrak f=\sum_a\gamma_a f_{34,a}.
 \tag{119}
$$
这正是该笔记(37)--(42)的原 $S$ 提升。
它不是在参数曲线上把一个恒等零质量的向量随意冻结，
也不是任取一个具有三阶零点的函数。
R855 的完整热递推给所有 $r\ge0$ 的准确等式
$$
 \begin{gathered}
 \mathsf T_0=1,\quad \mathsf T_1=L_2,\qquad
 \mathsf T_{r+1}
  =L_2\mathsf T_r-\frac{r(2r-1)}{24}g_2\mathsf T_{r-1},\\
 D_z^{2r}S_1(0)=68^r(\mathsf T_r\mathfrak f)(\widetilde P).
 \end{gathered}
 \tag{120}
$$
此处是全物理 jet 身份；$L_2$ 在形成算子时对所有参数完整求导。
尤其
$\mathfrak f(P)=L_2\mathfrak f(P)=L_2^2\mathfrak f(P)=0$、
$L_2^3\mathfrak f(P)=90/34^3$。

### 27.2 同一 Riccati 方程的完整形式解

在参数曲线 $g_2^3-27g_3^2=-432$ 上，用实际加性流参数 $s$
表示 $P_s$，即
$$
 P_0=\widetilde P,\qquad \frac{d}{ds}=L_2.
$$
$s$ 不是物理变量 $z$，也不是§26的 Newton 权变量。
置 $a(s)=g_2(P_s)/12$，并取下列两个唯一的特征零形式解：
$$
 \begin{gathered}
 \mathsf A''+a\mathsf A=0,\qquad
 \mathsf B''+a\mathsf B=0,\\
 (\mathsf A(0),\mathsf A'(0))=(1,0),\qquad
 (\mathsf B(0),\mathsf B'(0))=(0,1),\\
 \mathsf b=\mathsf B/s,\qquad
 \mathsf R=\mathsf A/\mathsf b,\qquad
 \ell=\log\mathsf R,\qquad
 v=\mathsf B/\mathsf A=s/\mathsf R .
 \end{gathered}
 \tag{121}
$$
所有常数项为一的幂、平方根及对数均按这个固定常数项取支。
这些是固定的真实周期方程解，不把 $\mathsf A,\mathsf B$ 声称为
固定代数函数。

为同时支付半权乘法，给任意固定 $k\in\mathbf Q$ 定义
$$
 \mathsf T^{(k)}_0=1,\quad\mathsf T^{(k)}_1=L_2,\qquad
 \mathsf T^{(k)}_{r+1}
   =L_2\mathsf T^{(k)}_r-r(r+k-1)a\mathsf T^{(k)}_{r-1}.
 \tag{122}
$$
$k=1/2$ 时准确等于(120)，因为
$r(r-\tfrac12)a=r(2r-1)g_2/24$。
本式也是修正 Serre 算子的原正规式，所用规范是
$E_4=12g_2$。无需调用全局权过滤定理即可证明以下全形式身份：
$$
 \boxed{
 \begin{aligned}
 \mathcal K_f^{(k)}(v)
   &:=
     \sum_{r\ge0}(\mathsf T_r^{(k)}f)(P)\frac{v^r}{r!}
       =\mathsf A(s(v))^k f(P_{s(v)}),\\
 (\mathsf T_r^{(k)}f)(P)
   &=r!\,[s^r]\!
       \left\{f(P_s)\mathsf b(s)^{k-2}
                      \mathsf R(s)^{r+k-1}\right\}.
 \end{aligned}
 }
 \tag{123}
$$

证明如下。递推(122)的指数母函数满足
$$
 (1+av^2)\partial_v\mathcal K
     =L_2\mathcal K-kav\mathcal K,\qquad
 \mathcal K(P,0)=f(P).
$$
从 $(P,v_0)$ 出发的特征曲线上，令
$\lambda(s)=\mathsf B(s)-v_0\mathsf A(s)$。
则 $v(s)=-\lambda(s)/\lambda'(s)$ 满足
$v'=-1-av^2$，且
$d\log\lambda'/ds=av$。
当 $v_0=\mathsf B(s_*)/\mathsf A(s_*)$ 时，
$v(s_*)=0$。Wronskian
$\mathsf A\mathsf B'-\mathsf A'\mathsf B=1$
又给 $\lambda'(s_*)=1/\mathsf A(s_*)$。
沿同一特征曲线积分便得第一式。
这是形式唯一解的计算，不要求选择任何新的复数或 $p$ 进周期。
最后
$dv=ds/\mathsf A^2$，故
$$
 [v^r]\mathcal K
  =\operatorname{Res}_{s=0}
      f(P_s)\mathsf A^{r+k-1}\mathsf B^{-r-1}\,ds,
$$
代 $\mathsf B=s\mathsf b$ 即为第二式，符号及 $r!$ 都已固定。

### 27.3 所需窗口的真实整性与三重型

这里分别证明底层代数函数和两个连接解的整性，
不把 $L_2^p=0$ 直接移给非代数的 $\mathsf A,\mathsf B$。

参数曲线写成
$Y^2=X^3+16$，其中 $X=g_2/3,Y=g_3$，
则 $L_2X=2Y,L_2Y=3X^2$。
在 $p\equiv5\pmod6$ 时该曲线的 Hasse 系数为零，故
$L_2^p=0$ 于其特征 $p$ 函数域。
在原固定 étale 覆盖上导子延拓唯一，$L_2^p$ 仍为零。
因此在§27.1的局部整模型 $\mathcal R$ 上，
$L_2^p\mathcal R\subset p\mathcal R$。
若 $n=up+j<p^2$、$0\le j<p$，迭代这个整算子即给
$$
 L_2^n\mathcal R\subset p^u\mathcal R,\qquad
 v_p(n!)=u.
 \tag{124}
$$
所以每个原整函数 $f$ 的实际流展开 $f(P_s)$
在所有 $n<p^2$ 的系数都整。
这尤其适用于 $a(s)$ 和 $\mathfrak f(P_s)$。
这里的原系数域及固定点、基变换已包括在 $\Sigma_{\rm flat}$ 的
既定整模型中；没有按 $p$ 临时选择 $f$。

原流方程 $g_2'=6g_3,\ g_3'=g_2^2/3$ 在三次单位 $\omega$ 下给
$$
 a(\omega s)=\omega a(s),\qquad
 \mathsf A(\omega s)=\mathsf A(s),\qquad
 \mathsf B(\omega s)=\omega\mathsf B(s).
 \tag{125}
$$
这些式子也可由常微分方程的唯一形式解逐系数证明。
令 $Y=\sum Y_ns^n$；两周期解的递推为
$$
 (n+2)(n+1)Y_{n+2}=-\sum_{i+j=n}a_iY_j .
$$
在 $p$ 以下所有非零分母均为单位。
第一对含 $p$ 的分母对应 $Y_p,Y_{p+1}$。
由(125)，$\mathsf A_p=0$；$\mathsf A_{p+1}$ 是其第一个
可能带 $p$ 分母的系数。
对 $\mathsf B$，这两个次数都不是 $1\bmod3$，
所以 $\mathsf B_p=\mathsf B_{p+1}=0$ 精确成立。
次数 $p+2$ 的分母又是单位。因此
$$
 \begin{gathered}
 [s^j]\mathsf A\in\mathcal O_F\quad(0\le j\le p),\\
 [s^j]\mathsf B\in\mathcal O_F\quad(0\le j\le p+2),\qquad
 [s^j]\mathsf b\in\mathcal O_F\quad(0\le j\le d).
 \end{gathered}
 \tag{126}
$$
这没有声称 $\mathsf A_{p+1}$ 整。

由(118)、(120)、(123)，
$\mathcal K_{\mathfrak f}^{(1/2)}(v)$ 只含 $v^{3j}$。
再用(125)、$v(\omega s)=\omega v(s)$，准确得到
$$
 \mathfrak f(P_s)\in s^3\overline{\mathbf Q}[[s^3]],\qquad
 [s^3]\mathfrak f(P_s)=15/34^3.
$$
因此本节所需 $\mathsf R,\ell$ 最多到 $d-3=p-2$；
它们在这个窗口全部整，且 $\ell\in s^3\mathcal O_F[[s^3]]$
在此有限意义下成立。
取对数只除以至多 $\lfloor(d-3)/3\rfloor<p$ 的整数。
半整数二项式系数在奇素数处整，所以
$\mathsf b^{-3/2}$、$\mathsf b^{-2}$ 也保持所示整窗。
$\mathsf A_d$ 的潜在首分母乘以 $\mathfrak f$ 后最早在 $s^{d+3}$，
严格不入本次两系数。

### 27.4 两个固定系数和完整三位共同分子

定义
$$
 \begin{gathered}
 \mathsf F(s)=\mathfrak f(P_s)\mathsf b(s)^{-3/2},\qquad
 \mathsf F_2(s)=\mathsf F(s)\mathsf R(s)^{1/2},\\
 E_N=[s^N]\mathsf F(s)\exp(p\ell(s)/2),\qquad
 E_d=[s^d]\mathsf F_2(s)\exp(p\ell(s)),\\
 \mathsf a_p=\frac{p\,68^N N!}{d!},\qquad
 \mathsf b_p=\frac{p\,68^d d!}{(2d)!}.
 \end{gathered}
 \tag{127}
$$
$\mathsf F,\mathsf F_2,\mathsf R$ 是同一固定函数与同一周期方程形成的
特征零形式函数；$p$ 只进入显示的指数、下标和阶乘。
由 $v_p(d!)=1,\ v_p((2d)!)=2,\ v_p(N!)=0$，
$\mathsf a_p,\mathsf b_p$ 都是单位。
它们在需要的精度使用完整值，而非先任意约成一个 Legendre 符号。

(120)、(123)分别给
$\alpha_d=68^NN!E_N/d!$ 与
$\alpha_{2d}=68^dd!E_d/(2d)!$。
用同一个 $\gamma=34pc_\sigma$，遂有准确式
$$
 \boxed{
 g_1=\frac{\mathsf a_pE_N}{p},\qquad
 g_{2,p}=\frac{p\mathsf b_pE_d-\gamma\mathsf a_pE_N}{p^2}.
 }
 \tag{128}
$$
第二式的两项先合成原共同分子，然后再除 $p^2$。
它包含原 $-34c_\sigma\alpha_d$，没有少一次 Gaussian。
R614 的真实整性保证该共同分子在 $p^2\mathcal O_F$ 中。

以下是足够且可直接使用的有限精度：
$$
 \begin{aligned}
 E_N&\equiv
  [s^N]\mathsf F\!
       \left(1+\frac p2\ell+\frac{p^2}{8}\ell^2\right)
                                      \pmod{p^3\mathcal O_F},\\
 E_d&\equiv
  [s^d]\mathsf F_2(1+p\ell)
                                      \pmod{p^2\mathcal O_F}.
 \end{aligned}
 \tag{129}
$$
证明中所有实际参与的 $\ell^j$ 至多满足
$3j\le d-3$，所以 $j<p$、$j!$ 为单位。
前式余下的 $j\ge3$ 各项在 $p^3$，
后式余下的 $j\ge2$ 各项在 $p^2$。
前节已证明系数本身整，故没有借无界形式指数的系数界。
由(128)，(129)准确决定 $g_1\bmod p^2$ 和
$g_{2,p}\bmod p$；共同分子误差在 $p^3$，除 $p^2$ 后恰在 $p$。
只保前式的一次 $\ell$ 项一般不足以读出第二槽。

### 27.5 与同一 canonical 第二位、二阶首位相认

在原首层失败 $g_1\in p$ 时，(128)给 $E_N\in p^2$。
又因 $g_{2,p}$ 整，必有 $E_d\in p$。
置两条真实整系数
$$
 X_p=\mathsf a_pE_N/p^2,\qquad
 Y_p=\mathsf b_pE_d/p .
$$
它们分别是原 $g_1/p$ 和原 $\alpha_{2d}$；
这里后者的整性只在上述首层失败范围内使用。
(115)和(128)遂准确成为
$$
 \boxed{
 \frac{j_1}{p^2}\equiv
       \frac{2\gamma X_p-Y_p}{\gamma^2},\qquad
 \frac{j_2}{p^2}\equiv
       \frac{Y_p-\gamma X_p}{\gamma^2}\pmod p .
 }
 \tag{130}
$$
因此(117)恰为
$(2\gamma X_p-Y_p)(Y_p-\gamma X_p)=0\bmod p$。
真正 $J'(0)=0$ 所给的是
$2\gamma X_p-Y_p=0\bmod p$；
没有把 $X_p$ 与 $Y_p$ 分别赋零。
等价地，该第二位使用原共同分子
$2\gamma\mathsf a_pE_N-p\mathsf b_pE_d\bmod p^3$。
这与§26是同一来源的两种完整表示，
不是以固定函数的首三阶非零代替本次指定高系数的非零。

## 28. 两半权来源的全卷积及真实权一周期

本节记录(123)给出的完整乘法；它不提供一个可以省去 mixed
项的平方规则。对同一参数曲线上的任意两个实际函数 $f,g$，
$$
 \boxed{
 \mathsf T_r^{(k+l)}(fg)
   =\sum_{j=0}^r\binom rj
        (\mathsf T_j^{(k)}f)(\mathsf T_{r-j}^{(l)}g).
 }
 \tag{131}
$$
证明直接在(123)第一式中相乘：
$\mathsf A^kf\cdot\mathsf A^lg=\mathsf A^{k+l}fg$，
再比较指数母函数的系数。
这在整个参数 germ 成立，故包含 $L_2$ 对全部参数的作用。

可取 $f=\mathfrak f$，并取 $g$ 为原 degree2 参考
$\Theta_2(z)=\sigma_1(z)^2x(z)$ 在同一固定覆盖和同一 $P$
上的准确水平质量；它由原参考向量的水平坐标构造，
且 $g(P)=1$。
则两条 $k=1/2$ 的完整热核之积恰为 $k=1$ 的核：
$$
 \mathcal K_{\mathfrak f}^{(1/2)}(v)
 \mathcal K_g^{(1/2)}(v)
   =\mathcal K_{\mathfrak fg}^{(1)}(v)
   =\mathsf A(s(v))\mathfrak f(P_{s(v)})g(P_{s(v)}).
 \tag{132}
$$
这里的物理因子分别为原 $68^r$ 和 $4^r$；
(131)先在各自真实热规范中形成全卷积。
不能把它直接改成 $S_1(z)\Theta_2(z)$ 的同一条物理 Taylor 行，
也不能把全卷积改成 $r=N$ 的逐项乘积。

令 $\zeta=\mathsf A/\mathsf B=1/v$。
Wronskian给 $d\zeta=-ds/\mathsf B^2$。
故权一的 $r=d=p+1$ 行准确是
$$
 \boxed{
 \frac{\mathsf T_d^{(1)}(\mathfrak fg)(P)}{d!}
  =-\operatorname{Res}_{s=0}
        \mathfrak f(P_s)g(P_s)\mathsf A(s)\,
                          \zeta(s)^p\,d\zeta(s).
 }
 \tag{133}
$$
负号和整数 $p$ 次幂均来自同一个变元替换。
这确实把两半权核放到“原代数函数乘真实秩二周期”的权一读者。
但 $\mathsf A$ 和 $\zeta$ 是(121)的指定水平 GM 解，
不是固定代数 cover 上可以自由施加 Frobenius 的标量函数。
若要把(133)进一步认成 crystalline 配对，仍须证明
**该**周期框架、Frobenius 初值和整个 mixed 卷积的整比较；
本节未作这种替换。

作为正常化交叉核，(122)与
Ahlgren--Raum--Richter,
*Theta Cycles of Modular Forms Modulo $p^2$*,
[arXiv:2604.06049v1](https://arxiv.org/pdf/2604.06049)
(1.9) 在 $k=1/2,1$ 的系数一致。
本文的(123)、(131)已由原微分方程自行证明，
不调用该文只对 scalar modular forms 给出的全局 filtration 定理，
也不把全局 $q$-展开非零迁移成原 CM 点的单位。

本节与§27均未运行数学程序。
当前可直接消费的新输入是(127)--(130)的同源有限系数、
共同 $p^2$ 分子和明确精度，以及(131)--(133)保全 mixed 项的真实权一返回。
四个原 canonical 坏条件的共同不相容性仍须额外证明。

## 29. 原全乘积的固定权三类与完整半权 Bockstein 层

本节继续§§27--28的同一有限水平覆盖和同一所选点。
记 $D=L_2$、$f=\mathfrak f$，并令 $g$ 是§28原参考
$\Theta_2=\sigma_1^2x$ 的冻结水平质量。所有 $\mathsf T_r$ 没有上标时
仍是 $k=1/2$ 的原算子；上标 $(1)$ 才表示完整权一卷积。
不把本节的普通卷积换成 R66、R82 另一来源的 Hadamard 平方。

### 29.1 一个明确非零的固定 parabolic de Rham 类

用§27.1固定的原系数定义
$$
 \Theta_f(\tau)=\sum_a\gamma_a\vartheta_{34,a}(\tau,0),\qquad
 \Theta_g(\tau)=\sum_b\delta_b\vartheta_{2,b}(\tau,0).
$$
$\delta_b$ 同样由原参考向量在同一 CM 纤维展开后固定，
不是新选的质量一函数。
原水平框架笔记(11)--(14)给
$$
 f=\sqrt{2\pi}\lambda^{-1/2}\Theta_f,\qquad
 g=\sqrt{2\pi}\lambda^{-1/2}\Theta_g,\qquad
 \Phi_{f,g}(\tau)=\eta(\tau)^4\Theta_f(\tau)\Theta_g(\tau).
 \tag{134}
$$
这里 $\eta$ 是 Dedekind eta，$\lambda,\mu$ 是原有向完整周期，
$\tau=\mu/\lambda$。
也允许取 $g=f$，此时完整系数向量仍是同一个 $\gamma\otimes\gamma$。

取杀掉原完整 theta/eta 矩阵、$\eta^2$ 和 $\eta^4$ 有限乘子的共同有限覆盖，
再与一个固定无挠 full-level 覆盖交，得到固定无挠群 $\Gamma$。
这个选择先于 $p$，保留原 $\gamma,\delta$ 和所有根相位；
不声称只需 level68，也不从一个 projective 表示省去 eta 相位。
在此覆盖上 $\Phi_{f,g}$ 是实际权三 cusp form：
每个 cusp 处全部 theta 变换都是原有限 theta 向量的线性组合，
各分量展开的阶非负；$\eta^4$ 在该 cusp 有严格正阶。
若 $g=f$ 或上述实际参考，则两 theta 函数都不恒零，
所以它们的乘积不恒零。

这一形式是原固定 GM 系统中的一个明确代数来源。
在参数覆盖上令
$$
 \mathcal E=H^1_{\rm dR}(E/\text{参数覆盖}),\qquad
 e_0=[\omega],\quad e_1=[x\omega],\quad
 \omega=dx/(2y).
$$
原周期公式 $D\lambda=-\eta_\lambda$、$D\eta_\lambda=a\lambda$
和 Legendre 正规
$\eta_\lambda\mu-\eta_\mu\lambda=2\pi i$
给
$$
 \nabla e_0=e_1\,ds,\qquad \nabla e_1=-a e_0\,ds,\qquad
 \langle e_0,e_1\rangle=1 .
$$
定义同一代数系数的一形式
$\boldsymbol\omega_{f,g}=fg\,e_0\,ds$。
其 Betti 比较不是未指明的比例；由
$\Delta_0=(2\pi/\lambda)^{12}\eta^{24}$ 和
$ds=\lambda^2d\tau/(2\pi i)$ 得
$$
 \boxed{
 \operatorname{per}\boldsymbol\omega_{f,g}
 =-4\pi^2i\,\Delta_0^{-1/6}
       \Phi_{f,g}(\tau)\binom{1}{\tau}\,d\tau .
 }
 \tag{135}
$$
$\Delta_0=-432$ 的分支按原(10)固定。
这是在复比较中写出的等式；没有把复周期本身送入 $\mathbf C_p$。
交换两个固定 Betti 坐标后，右端就是标准
$\Phi_{f,g}(\tau)(\tau,1)^t d\tau$。

该 parabolic de Rham 类非零可以直接付清。
对标准实二维局部系统使用行列式交替配对，有
$$
 \left\langle
  \Phi(\tau)\binom{\tau}{1}d\tau
  \wedge
  \overline{\Phi(\tau)\binom{\tau}{1}d\tau}
 \right\rangle
 =4|\Phi(\tau)|^2y\,dx\wedge dy,\qquad \tau=x+iy.
 \tag{136}
$$
积分为四倍实际权三 Petersson 范数，有限且严格正。
若这个 parabolic 类为 exact，对基本域截去 cusp 后用 Stokes，
成对边互相抵消，cusp 边因 cusp form 的指数衰减趋零。
在每个 cusp 的平坦 Betti 框架中，原函数的导数正是指数衰减乘
有限次 $\tau$ 多项式；逐项积分给一个平坦常数加同类衰减项。
故即使保留该常数，也不足以留下边界贡献。
于是(136)的正积分将为零，矛盾。
由此支付的是(135)这个**具体固定来源**的非零，
不是任意固定上同调空间中“存在某个非零类”。

### 29.2 同一 moving 主部的两个相邻读者

令 $h=fg$ 或 $h=f^2$，并保留原 $A,B$ 周期解
$\mathsf A,\mathsf B$。置 $\zeta=\mathsf A/\mathsf B$；
由(123)和 $d\zeta=-ds/\mathsf B^2$，有精确向量式
$$
 \boxed{
 \binom{(\mathsf T_p^{(1)}h)(P)/p!}
       {(\mathsf T_d^{(1)}h)(P)/d!}
 =-\operatorname{Res}_{s=0}
       h(P_s)\binom{\mathsf B(s)}{\mathsf A(s)}
                      \zeta(s)^p\,d\zeta(s).
 }
 \tag{137}
$$
第一项是
$\operatorname{Res}h\mathsf A^p\mathsf B^{-p-1}ds$，
第二项是(133)。
所以两项确来自同一 period 向量和同一个整数 $p$ 次主部。

(137)尚不是(135)的 Frobenius 矩阵元：
其相对于 $(\mathsf A,\mathsf B)h\,ds$ 另有真实
$\mathsf B^{-2}$ 与 moving $\zeta^p$。
对这些因子未付的替换不能以(136)的正定性补上。
下面先把这个读者在原 theta 来源上的全部除 $p$ 层明确还回。

### 29.3 原 Hurwitz 行给出的完整混合降阶

仍记 $d=p+1$、$N=d/2$，并固定原特征零 Hasse 多项式
$H=H_p$。令
$$
 C_0=(DH)(P)=(p+1)c_p^{\rm int},\qquad
 c_p^{\rm int}=\binom{3s-1}{2s-1},\qquad p=6s-1.
$$
$C_0$ 是实际单位；以下模 $p$ 时仍用它的约化。
原 R856(19)--(21)作用在同一物理截面上，给
$$
 (\mathsf T_{N+k}u)(P)
 \equiv\varepsilon_u C_0(k+\tfrac12)
                 (\mathsf T_ku)(P)\pmod p,\qquad 0\le k\le N,
 \tag{138}
$$
其中 $u=f,g$ 分别来自 degree $m=34,2$，
$\varepsilon_u=(\frac{2m}{p})$，故
$\varepsilon_f=(\frac{17}{p})$、$\varepsilon_g=1$。
证明直接将 Hurwitz 关系
$j_{m,p+2k+1}\equiv mC_0(2k+1)j_{m,2k}$
除以同一个 $(2m)^{N+k}$。
它不是把两个不同物理尺度 $68,4$ 先行相同化。

为不丢下一位，定义准确的原单位及指定缺陷
$$
 \begin{gathered}
 e_{m,p}=(2m)^{-(p-1)/2},\\
 \mathcal B_{u,k}
 =\frac{(\mathsf T_{N+k}u)(P)
       -e_{m,p}C_0(k+\tfrac12)(\mathsf T_ku)(P)}p
 =(2m)^{-(N+k)}
       \mathcal D_{m,p,\,2k+1}(R_u)\big|_P .
 \end{gathered}
 \tag{139}
$$
右端准确是 R856(39)的原整 Hurwitz 行：
$R_u$ 为该原水平来源在 $P$ 的实际向量。
故所有 $\mathcal B_{u,k}$ 都整并已由原来源指定，
并非可以自由选择的 Bockstein 初值。
$H(P)=0$ 在特征零精确成立，故(139)没有漏一个 $Hj$ 项。
特别不能把 $e_{34,p},e_{2,p}$ 在模 $p^2$ 时直接换为两个 Legendre 符号；
它们的完整下一位必须保留。

以下所有 $\mathsf T_j u$ 均在 $P$ 取值。
令 $b_j=\binom dj/p$，$2\le j\le p-1$，这些数全为整数。
由 $f(P)=Df(P)=0$、$g(P)=1,Dg(P)=0$，
完整乘法(131)逐项给**特征零**等式
$$
 \begin{aligned}
 \frac{\mathsf T_d^{(1)}(fg)-\mathsf T_df}{p}
 ={}&C_0\sum_{j=2}^{N-1}b_j(N-j+\tfrac12)
     \left\{
       e_{2,p}(\mathsf T_jf)(\mathsf T_{N-j}g)
      +e_{34,p}(\mathsf T_{N-j}f)(\mathsf T_jg)
     \right\}\\
 &+p\sum_{j=2}^{N-1}b_j
     \left\{
       (\mathsf T_jf)\mathcal B_{g,N-j}
       +\mathcal B_{f,N-j}(\mathsf T_jg)
     \right\}\\
 &+b_N(\mathsf T_Nf)(\mathsf T_Ng).
 \end{aligned}
 \tag{140}
$$
两端 $j=0,d$ 只留下 $\mathsf T_df$；
$j=1,d-1$ 精确为零。
每一对 $j,d-j$ 均在(140)中保留一次，中点 $j=N$ 另列；
没有少一次系数二，也没有把中点吸收到两半和。

只取第一位时，
$b_j\equiv(-1)^j/(j(j-1))$、
$N+\tfrac12\equiv1\pmod p$，
且 $\mathsf T_Nf\equiv0$。
因此
$$
 \begin{aligned}
 \frac{\mathsf T_d^{(1)}(fg)-\mathsf T_df}{p}
 &\equiv C_0\sum_{j=2}^{N-1}\frac{(-1)^{j+1}}j
     \left\{
       \varepsilon_g(\mathsf T_jf)(\mathsf T_{N-j}g)
       +\varepsilon_f(\mathsf T_{N-j}f)(\mathsf T_jg)
     \right\},\\
 \frac{\mathsf T_d^{(1)}(f^2)}p
 &\equiv2\varepsilon_f C_0
       \sum_{j=2}^{N-1}\frac{(-1)^{j+1}}j
           (\mathsf T_jf)(\mathsf T_{N-j}f)
 \qquad\pmod p .
 \end{aligned}
 \tag{141}
$$
后一式的两个端点都因 $f(P)=0$ 消失。
这确将原全 weight1 类的首除 $p$ 行接到实际低 half-jet 卷积；
保留了所有 mixed 项，未认成 $(\mathsf T_Nf)^2$。

对于原 $g_{2,p}$，仍要再保一位。
(127)准确给
$\mathsf T_df=d!E_d$，故
$\mathsf T_df/p=(d!/p)E_d$。
在 $g_1\in p$ 的原范围，
$E_d\in p$、$\mathsf T_Nf=N!E_N\in p^2$。
所以(140)的中点项在模 $p^2$ 已消，
但整个第二行的 $p\mathcal B$ mixed 层一般仍须保留。
真正要取得 $E_d/p\bmod p$，必须使用(140)模 $p^2$，
不能只用(141)。
(136)的非零类及(141)本身均未使这一中间层自动为零。

## 30. 真实 Hasse 框架的第一完整修正

本节把上一节的主部框架与 R856 已定的实际 Hasse 缺陷接合。
它不更换§27的周期解，也不从一个模 $p$ 的解选取新的任意提升。

### 30.1 由原非齐次项唯一给出的修正

置
$$
 \mathcal R_p=\frac{D^2H+aH}{p},\qquad
 \mathsf U_p=\frac{H(P_s)/C_0-\mathsf B(s)}p,\qquad
 \mathsf V_p=\mathsf U_p/\mathsf B .
 \tag{142}
$$
$\mathcal R_p$ 必须使用 R856(35)的完整多项式，
包含其三项，而非仅在 CM 点的零值。
它给
$$
 \begin{gathered}
 \mathsf U_p''+a\mathsf U_p=\mathcal R_p(P_s)/C_0,\qquad
 \mathsf U_p(0)=\mathsf U_p'(0)=0,\\
 (\mathsf B^2\mathsf V_p')'
       =\mathsf B\,\mathcal R_p(P_s)/C_0,\qquad
 \mathsf V_p(0)=0 .
 \end{gathered}
 \tag{143}
$$
后一式由 $\mathsf U_p=\mathsf B\mathsf V_p$ 直接展开；
等价的双积分按这两个零初值唯一确定，所以没有遗留积分常数。

R856(36)--(38)给
$\mathcal R_p(P_s)\in s^2\mathbf Q[[s^3]]$
及 $[s^2]\mathcal R_p\equiv55c_p$。
故
$$
 \mathsf U_p\in s^4F[[s^3]],\qquad
 \mathsf V_p\in s^3F[[s^3]],\qquad
 [s^3]\mathsf V_p\equiv\frac{55}{12}\pmod p .
 \tag{144}
$$
这里 $p>211$，因此所示首系数确为单位。
这是实际 frame 缺陷的首系数，不是目标高系数的非零结论。

所需整性也由真实受迫方程支付。
$\mathcal R_p$ 是原整参数多项式，因此按(124)，
$\mathcal R_p(P_s)$ 在 $s$ 次数小于 $p^2$ 的窗口整。
$\mathsf U_p$ 的 type1 受迫递推只除以 $n(n-1)$；
第一次含 $p$ 的次数 $n=p,p+1$ 都是禁型，精确为零，
到 $p+2$ 的分母再为单位。
所以 $\mathsf U_p$ 至次数 $p+2$ 整；
由 $\mathsf B=s\mathsf b$ 和(126)，
$\mathsf V_p$ 至次数 $d$ 整。
这证明(142)在本窗实际可以除 $p$，
而非从形式上写出商就宣布整。

### 30.2 两条原系数的精确框架运输

定义
$$
 \widehat{\mathsf b}=\frac{H(P_s)}{C_0s}
      =\mathsf b(1+p\mathsf V_p),\qquad
 \widehat{\mathsf R}=\frac{\mathsf A}{\widehat{\mathsf b}},
 \qquad \widehat\ell=\log\widehat{\mathsf R},
 \qquad \widehat{\mathsf F}=f(P_s)\widehat{\mathsf b}^{-3/2}.
$$
这些是原 Hasse lift 和原 $\mathsf A,\mathsf B$ 唯一确定的量。
$(1+p\mathsf V_p)$ 的常数为一，所有幂按原常数项取支。
由(127)逐因子替换，得到准确式
$$
 \boxed{
 \begin{aligned}
 E_N&=[s^N]\widehat{\mathsf F}\,
          \exp(p\widehat\ell/2)
             (1+p\mathsf V_p)^{(p+3)/2},\\
 E_d&=[s^d]\widehat{\mathsf F}\,
          \widehat{\mathsf R}^{1/2}\exp(p\widehat\ell)
             (1+p\mathsf V_p)^{p+2},\\
 \frac{\mathsf T_d^{(1)}h(P)}{d!}
      &=[s^d]h(P_s)\mathsf A\widehat{\mathsf b}^{-2}
          \exp(p\widehat\ell)(1+p\mathsf V_p)^{p+2}.
 \end{aligned}
 }
 \tag{145}
$$
第三行对 $h=fg,f^2$ 都成立。
它明确保留了固定 GM 成分 $\mathsf A$、
实际 Hasse 的二极以及同一 $\mathsf V_p$ 修正。
不能先删最后一个因子，再以固定 cohomology 的结论补回。

在(129)所需的相同精度，(145)成为
$$
 \begin{aligned}
 E_N\equiv[s^N]\widehat{\mathsf F}
  \bigg\{1+\frac p2(\widehat\ell+3\mathsf V_p)
      +p^2\left(
        \frac{\widehat\ell^2}{8}
       +\frac{3\widehat\ell\mathsf V_p}{4}
       +\frac{\mathsf V_p}{2}
       +\frac{3\mathsf V_p^2}{8}\right)\bigg\}
       &\pmod{p^3},\\
 E_d\equiv[s^d]\widehat{\mathsf F}\widehat{\mathsf R}^{1/2}
           \{1+p(\widehat\ell+2\mathsf V_p)\}
       &\pmod{p^2},\\
 \frac{\mathsf T_d^{(1)}h(P)}{d!}
   \equiv[s^d]h(P_s)\mathsf A\widehat{\mathsf b}^{-2}
           \{1+p(\widehat\ell+2\mathsf V_p)\}
       &\pmod{p^2}.
 \end{aligned}
 \tag{146}
$$
模数均在原好整模型的系数环内读取。
$f$ 从 $s^3$ 起，故所需 $\widehat\ell,\mathsf V_p$ 仍只到 $d-3$；
所有对数、二项式和指数余项按§27.3--27.4的同一有限整窗估计。
特别 $(1+pV)^{(p+3)/2}$ 的线性项是
$3pV/2+p^2V/2$，二次项是 $3p^2V^2/8$；
这两项都未以“mod $p$ Hasse 框架”省去。

(134)--(146)支付了两个实际输入：
原全 ordinary 乘积的一个明确非零固定 parabolic 类，
以及同一原 $g_1,g_{2,p}$ 与该全乘积的完整 mixed Bockstein、
Hasse 框架和所需精度之间的指定关系。
尚未证明 moving 主部(137)的除 $p$ 值是这个非零固定类的一个非退化
Frobenius 矩阵元；也没有把(144)的首系数、
(136)的正范数或(141)的低卷积各自认成 canonical 非零。
本节没有数学数值运行。

## 31. 原临界混合行的完整 Rankin–Cohen 源及第二个 CM 域

本节仍取§29的实际冻结质量 $f,g$，不更换 $\gamma_a,\delta_b$。
$g$ 是原 $\Theta_2=\sigma_1^2x$ 的水平延拓；其在同一 CM 点满足
$g(P)=1,Dg(P)=0$。记
$F=\Theta_f,\ G=\Theta_g,\ D_\tau=(2\pi i)^{-1}d/d\tau$。
这里的 $q=e^{2\pi i\tau}$ 是模形式变量，不是原反圆分参数。

### 31.1 固定全部周期常数的真正括号

对任意整数 $n\ge0$ 定义实际代数函数
$$
 \mathscr R_n(f,g)
 =\sum_{j=0}^n(-1)^j
       \binom{n-\tfrac12}{n-j}\binom{n-\tfrac12}{j}
       (\mathsf T_jf)(\mathsf T_{n-j}g).
 \tag{RC1}
$$
两个 $\mathsf T$ 均为原半权算子。相应的经典括号规定为
$$
 [F,G]_n
 =\sum_{j=0}^n(-1)^j
       \binom{n-\tfrac12}{n-j}\binom{n-\tfrac12}{j}
       (D_\tau^jF)(D_\tau^{\,n-j}G).
$$
对同一完整周期 $\lambda$，准确有
$$
 \boxed{\quad
 \mathscr R_n(f,g)
   =(-1)^n(2\pi/\lambda)^{2n+1}[F,G]_n(\tau).
 \quad}
 \tag{RC2}
$$
右端作为这一规范的组合为代数函数；不把 $2\pi/\lambda$
或每个未归一导数单独称为代数函数。

给出包括符号的证明。先在任意指定参数点把 $\mathsf A,\mathsf B$
按(121)初始化，写 $q_0=\eta_{\lambda,0}/\lambda_0$、
$c=2\pi i/\lambda_0^2$。同一周期方程与 Legendre 正规给
$$
 \lambda(s)=\lambda_0\mathsf A(s)(1-q_0v),\qquad
 \tau(s)=\tau_0+\frac{cv}{1-q_0v},\qquad v=\mathsf B/\mathsf A.
$$
所以原生成函数准确为
$$
 \mathcal K_f^{(1/2)}(v)
 =\sqrt{2\pi/\lambda_0}\,(1-q_0v)^{-1/2}
          F\!\left(\tau_0+\frac{cv}{1-q_0v}\right),
 \tag{RC3}
$$
并有相同的 $g,G$ 公式。初值处的第 $j$ 导数就是 $\mathsf T_jf$。

所需的括号协变性只是有限乘法法则。若
$z=(av+b)/(cv+d)$、$\delta=ad-bc$，则
$$
 \frac{d^j}{dv^j}\{(cv+d)^{-k}A(z)\}
 =\sum_{r=0}^j
   \binom jr(-1)^{j-r}(k+r)_{j-r}
   c^{j-r}\delta^r(cv+d)^{-k-j-r}A^{(r)}(z).
$$
将两份公式代入权 $(k,l)$ 的括号，
总导数阶小于 $n$ 的各项由二项式恒等式相消，
留下
$\delta^n(cv+d)^{-k-l-2n}[A,B]_n(z)$。
这里 $(k,l)=(1/2,1/2)$；在(RC3)的 $v=0$，
乘子为 $(2\pi/\lambda_0)c^n$。
再把普通 $\tau$ 导数换成 $D_\tau$，额外乘 $(2\pi i)^n$，
合为
$(2\pi/\lambda_0)(-4\pi^2/\lambda_0^2)^n$，这就是(RC2)。

在杀掉完整 theta/eta 表示和所需有限乘子的共同固定群上，
$[F,G]_n$ 是权 $2n+1$ 的实际模形式，全部原系数和相位不变。
当 $n>0$ 时它在每个 cusp 消失：任一 cusp 的变换仍是全部
原 theta 分量括号的线性组合；其 Fourier 常数项中每个项
至少有一边受到正次导数，故均为零。
本节没有断言每个 $n$ 的括号都非零。

### 31.2 原全部六十八余类的二元调和 theta 身份

设
$$
 K_{17}=\mathbf Q(\sqrt{-17}),\qquad
 \mathcal O_{17}=\mathbf Z[\sqrt{-17}],\qquad
 \mathfrak p_{17}=(17,\sqrt{-17}),\qquad
 \mathfrak m=2\mathfrak p_{17}.
$$
这些对象先于研究素数 $p$ 固定。
有
$$
 \mathfrak m=34\mathbf Z+2\sqrt{-17}\,\mathbf Z,\qquad
 \#(\mathcal O_{17}/\mathfrak m)=68 .
$$
因此原 $a\bmod34,\ b\bmod2$ 的每一对恰为一个实际余类，
不是删去非单位后的一个新 ray 子集。

对 $x\equiv a\pmod {34},\ y\equiv b\pmod2$ 写
$$
 \alpha=x+y\sqrt{-17},\qquad
 Q(x,y)=\frac{x^2+17y^2}{68},\qquad
 c_n=\frac{\binom{2n}{n}}{4^n}.
$$
原 theta 定义给
$\vartheta_{34,a}=\sum_xq^{x^2/68}$、
$\vartheta_{2,b}=\sum_yq^{y^2/4}$，于是逐项准确有
$$
 \boxed{\quad
 [\vartheta_{34,a},\vartheta_{2,b}]_n
 =\frac{(-1)^nc_n}{2(2\sqrt{17})^{2n}}
     \sum_{\substack{x\equiv a\ (34)\\y\equiv b\ (2)}}
       \bigl(\alpha^{2n}+\bar\alpha^{\,2n}\bigr)q^{Q(x,y)} .
 \quad}
 \tag{RC4}
$$
其中 $\sqrt{17}$ 取与原复杂规范相容的正实根；分母中的幂为偶数，
所以该式没有新的根选择歧义。

证明只用两个精确有限恒等式：
$$
 \binom{n-\tfrac12}{n-j}\binom{n-\tfrac12}{j}
   =c_n\binom{2n}{2j},
$$
$$
 \sum_{j=0}^n(-1)^j\binom{2n}{2j}A^jB^{n-j}
 =\frac{(\sqrt B+i\sqrt A)^{2n}
             +(\sqrt B-i\sqrt A)^{2n}}2.
$$
第一式清掉半整数分母后两边都是
$(2n)!^2/(4^n n!^2(2j)!(2n-2j)!)$。
在第二式取 $A=x^2/68,\ B=y^2/4$；
可直接用有符号的 $\sqrt A=x/(2\sqrt{17})$、
$\sqrt B=y/2$，因为只出现偶幂。
有
$\sqrt B+i\sqrt A=i\bar\alpha/(2\sqrt{17})$，
另一项为 $-i\alpha/(2\sqrt{17})$，
所以恰产生(RC4)的 $(-1)^n$。
正定 $Q$ 保证在上半平面绝对收敛，故所有有限次微分和求和可交换。

现在保持完整冻结权，定义
$$
 \mathcal H_{2n}(\tau)
   =\sum_{a\bmod34,\ b\bmod2}\gamma_a\delta_b
        \sum_{\substack{x\equiv a\ (34)\\y\equiv b\ (2)}}
         \bigl(\alpha^{2n}+\bar\alpha^{\,2n}\bigr)q^{Q(x,y)} .
$$
合并(RC2)、(RC4)，两个 $(-1)^n$ 正好相消，得到
$$
 \boxed{\quad
 \mathscr R_n(f,g)
   =\frac{c_n}{2(2\sqrt{17})^{2n}}
      (2\pi/\lambda)^{2n+1}\mathcal H_{2n}(\tau).
 \quad}
 \tag{RC5}
$$
这给出了原括号的同一个完整二元调和来源，
包括全部非 primitive 余类、固定权和周期常数。
这里的 CM 域是 $K_{17}$，与原物理 $j=0$ 曲线的
$\mathbf Q(\sqrt{-3})$ 不同。
没有将这份带全部权的 theta 和先行认成一个单独 Hecke 本征形式，
也没有赋任一分量以原 canonical 坏条件。

### 31.3 临界括号的真实两层整除

仍取原 $p>211$、$p\equiv5\pmod6$，
$N=(p+1)/2,\ d=2N$，并删去原固定 $\Sigma_{\rm flat}$。
全部 $\mathsf T_jf,\mathsf T_jg$ 在原好局部格上整。
有
$$
 c_N=\binom{p/2}{N},\qquad
 \beta_p=c_N/p\in\mathcal O^\times,\qquad
 \beta_p\equiv(-1)^{N-1}\pmod p .
$$
事实上半整数降阶积恰含一个 $p/2$，
且其余分子和 $N!$ 都是单位；
除以 $p$ 后模 $p$ 为 $(-1)^{N-1}/(2N)$，
而 $2N=p+1$。
对 $1\le j\le N-1$，两个半整数二项式各含一个 $p$，所以
$$
 \frac{(-1)^j}{p^2}
       \binom{p/2}{N-j}\binom{p/2}{j}
   \equiv\frac{(-1)^{N+j}}{4j(N-j)}\pmod p .
 \tag{RC6}
$$

在指定 CM 点，(138)与 $f(P)=0$ 给 $\mathsf T_Nf(P)\in p\mathcal O$。
括号的 $j=0$ 项因 $f(P)=0$ 消失，
$j=N$ 项为 $(-1)^Nc_N\mathsf T_Nf(P)$；
所有中间项已经被 $p^2$ 整除。
故准确有
$$
 \mathscr R_N(f,g)(P)\in p^2\mathcal O,\qquad
 r_p:=\mathscr R_N(f,g)(P)/p^2\in\mathcal O .
$$
再用 $Df(P)=Dg(P)=0$ 删除两个准确零项，得到
$$
 \boxed{\quad
 r_p\equiv
   -\frac{\mathsf T_Nf(P)}p
   +\frac{(-1)^N}{4}
       \sum_{j=2}^{N-2}
       \frac{(-1)^j(\mathsf T_jf)(P)
                    (\mathsf T_{N-j}g)(P)}{j(N-j)}
       \pmod p .
 \quad}
 \tag{RC7}
$$
所有分母小于 $p$，没有遗漏任何新的整格费用。
该式只对原指定 CM 点断言除 $p^2$ 整性；
全参数域中的 $\mathscr R_N/p$ 虽整，
$\mathscr R_N/p^2$ 不据此成为整函数。

### 31.4 两个真实 Frobenius 符号及同一原混合行

写 $H=H_p,\ C=DH$，仍取原固定特征零提升。
原水平 theta 的全域模 $p$ 式为
$$
 \mathsf T_Nu\equiv
       \varepsilon_u(HD+C/2)u,\qquad
 \varepsilon_f=\left(\frac{17}{p}\right),\quad
 \varepsilon_g=1.
$$
在(RC1)除以 $p$ 后，中间项都消失，
故有以下两个准确的全域首层：
$$
 \boxed{
 \begin{array}{ll}
 \mathscr R_N/p\equiv
       \beta_p\varepsilon_g\,D(Hfg),
       &\varepsilon_f=(-1)^N\varepsilon_g,\\[2mm]
 \mathscr R_N/p\equiv
       \beta_p\varepsilon_g\,H(fDg-gDf),
       &\varepsilon_f=-(-1)^N\varepsilon_g .
 \end{array}}
 \tag{RC8}
$$
第一种符号恰等价于
$\left(\frac{-17}{p}\right)=-1$；
第二种恰等价于其为 $+1$。
这里保留了 $C/2$ 的两份贡献：在第一种相加成 $Cfg$，
在第二种才相消。不能在两个射线上使用同一个错误的 scalar 符号。

在第一种射线上，(141)的完整低半权卷积可准确改写为
$$
 \boxed{\quad
 \frac{(\mathsf T_d^{(1)}(fg))(P)
             -(\mathsf T_df)(P)}p
 \equiv-2\varepsilon_f C_0
        \left(r_p+\frac{(\mathsf T_Nf)(P)}p\right)\pmod p .
 \quad}
 \tag{RC9}
$$
证明把(141)第二项换下标 $j\mapsto N-j$。
因为 $Dg(P)=Df(P)=0$，端点 $j=1,N-1$ 可准确补入或删去。
在 $\varepsilon_f=(-1)^N\varepsilon_g$ 时，
合并后的系数为
$$
 (-1)^{j+1}\varepsilon_g
       \left(\frac1j+\frac1{N-j}\right)
 =-\varepsilon_g N\,\frac{(-1)^j}{j(N-j)}.
$$
将(RC7)代入，再用 $N\equiv1/2$，便得到(RC9)。
没有把 $j=N$ 的中点项重复计入。

在原 $g_1\in p$ 的范围，(127)--(130)给
$\mathsf T_Nf(P)\in p^2$ 和 $\mathsf T_df(P)\in p^2$，
因此(RC9)还给
$$
 \frac{(\mathsf T_d^{(1)}(fg))(P)}p
      \equiv-2\varepsilon_fC_0r_p\pmod p .
 \tag{RC10}
$$
这是两个实际未被赋零的读者之间的关系。
它没有把左边或 $r_p$ 自动判为零；
原 $g_{2,p}$ 的下一位仍须保留(140)中的完整 $p\mathcal B$ 层。

### 31.5 同一完整二元源的精确 Fermat 差

现在只在 $\left(\frac{-17}{p}\right)=-1$ 的原射线上工作。
对每个 $\alpha=x+y\sqrt{-17}\in\mathcal O_{17}$，写
$n_\alpha=\alpha\bar\alpha=x^2+17y^2$。
下面是特征零中的逐项恒等式：
$$
 \boxed{\quad
 \alpha^{p+1}+\bar\alpha^{\,p+1}
    -n_\alpha-n_\alpha^p
 =-(\alpha^p-\bar\alpha)(\bar\alpha^p-\alpha).
 \quad}
 \tag{RC11}
$$
直接展开右边四项即可证明。
由于 $p$ 在 $K_{17}$ 惰性，其剩余 Frobenius 是复共轭，
两括号都在 $p\mathcal O_{17,(p)}$。
这也包括 $\alpha=0$ 以及 $p\mid n_\alpha$ 的项；
本证明没有除以 $n_\alpha$，
因而没有删去任何非 primitive 余类。

令
$$
 \Theta_{\rm bin}=FG
   =\sum_{a,b}\gamma_a\delta_b
       \sum_{x\equiv a,\ y\equiv b}q^{Q(x,y)}
$$
以及整 Fourier 系数的实际全余项
$$
 \Xi_p
  =\sum_{a,b}\gamma_a\delta_b
       \sum_{x\equiv a,\ y\equiv b}
       \frac{\alpha^p-\bar\alpha}{p}
       \frac{\bar\alpha^p-\alpha}{p}\,q^{Q(x,y)}.
$$
在原好系数格内，对每个指数都是有限求和。
对(RC11)按同一全部固定权求和，得到精确形式级数等式
$$
 \boxed{\quad
 \mathcal H_{p+1}
    =68D_\tau\Theta_{\rm bin}
       +68^pD_\tau^{\,p}\Theta_{\rm bin}
       -p^2\Xi_p .
 \quad}
 \tag{RC12}
$$
这里 $D_\tau^p$ 是 $p$ 次微分，
没有把原 $\gamma_a,\delta_b$ 作系数 Frobenius，
也不是把 $q$ 换成 $q^p$。
等式中的 $68^p$ 与 $68$ 不可相认。
将其放回(RC4)，因 $v_p(c_N)=1$，
该具体原余项首次进入括号的 $p^3$ 层；
它为临界括号提供了保全六十八余类的真正模 $p^3$ Fourier 输入。

### 31.6 与指定 CM 除 $p$ 值之间尚需完成的比较

(RC2)、(RC5)、(RC7)--(RC12)都是原输入的身份，
而不是仅将一个自由的二元 theta 函数接到原问题。
它们支付完整周期、原固定权、两个 CM 域的不同符号、
全部非 primitive 项，以及原下一层的准确 Fermat 余项。
这与§29的固定权三类提供两个可以继续比较的真实输入。

但是(RC12)两项微分的表面权不同，普通 $D_\tau$ 也带准模项。
一个整 Fourier 同余本身不容许直接在 supersingular CM 点
取值、除以 $p$ 或除以 Hasse。
尤其在 $H(P)=0$ 的同一点，需要同权的实际 $E_2$/Hasse 修正、
原几何 Frobenius/Spencer 连接、完整系数作用和所有除 $p$ 成本。
本节没有用(CM)标签、原全 theta 的经典非零、
或单个本征因子的 ordinary 性代替这些费用。
下一步继续把(RC12)的全余项与(140)、(145)--(146)
的同一实际读者接合，争取原 canonical 的跨素数非零。
本节所有式子为上述逐项证明；没有数学数值运行。

## 32. 原完整权一读者的相对 Frobenius、Serre 对偶与全局 Cartier 返回

沿用§§27--31的固定覆盖、原 CM 点和冻结的全部水平坐标。
这里的 Frobenius 矩阵属于**物理椭圆曲线族**的相对一阶上同调；
Serre 对偶及 Cartier 所在的曲线则是**参数曲线或其固定水平覆盖**。
以下均为手证。取原好素数 $p>211$、$p\equiv5\bmod6$，$d=p+1$。

### 32.1 族 Frobenius 的两条准确截断行

在原参数曲线 $E_{16}$ 取实际代数参数及不变微分
$$
 t=-g_2/24,\qquad g_3=-4\sqrt{1-32t^3},\qquad
 ds=J(t)dt,\qquad J(t)=(1-32t^3)^{-1/2}.
$$
一切平方根在原点取常数一。此处 $t$ 与原 $s$ 的一阶系数相同。
在此光滑形式盘上，对目标盘坐标 $T$ 取 Frobenius 提升 $T\mapsto t^p$。
有限 étale 水平覆盖上用原点及其相对 Frobenius 像所在的两个形式盘。
在剩余域扩张时使用 **relative** 约定：目标为 Frobenius twist，
将物理系统从 $\mathbf Z_p$ 标量扩张，以 $T\mapsto t^p$ 线性拉回目标坐标。
若再用绝对半线性记法把目标认回原盘，输出系数须作相应的逆 Frobenius；
并未把带水平结构的点假设为 $\mathbf F_p$ 有理。输入的
$h=fg$（亦可 $h=f^2$）始终是源盘上的实际全函数。

以§29的代数基 $e_0,e_1$ 写相对晶体 Frobenius
$W(t):\varphi^*\mathcal E\to\mathcal E$，列为像。该矩阵为光滑
proper 物理族的一阶 Gauss--Manin 晶体在这个提升上的矩阵；
其系数是几何 Frobenius 在代数基中的 $p$ 进系数。
记 $A,B$ 为(121)的解，$A',B'$ 一律对 $s$ 求导，作为 $t$ 的函数时
代入 $s(t)$。Wronskian 与连接给
$$
 M(t)=\begin{pmatrix}A&A'\\B&B'\end{pmatrix},\quad
 M(0)=I,\quad \det M=1,\qquad
 W(t)=M(t)^{-1}C M(t^p),\quad
 C=\begin{pmatrix}0&u\\-p/u&0\end{pmatrix}.
 \tag{F1}
$$
确实，$M$ 把代数基坐标送到以原点为初值的水平坐标，
从而 Frobenius 水平性给中间常矩阵 $W(0)$。这些物理周期形式解
及 $t$ 均定义于 $\mathbf Q_p$，所以目标物理矩阵无需另换系数。
在物理 $E_1:y^2=x^3+1$ 上，三次 CM 使两条特征线上的 Frobenius
互换：若用有三次单位根的非分歧扩张，其系数 Frobenius 交换两个特征值。
杯积乘 $p$ 给 $\det C=p$。原 de Rham 整格上，Frobenius 整且
模 $p$ 杀 Hodge 线，因为相对 Frobenius 拉回正则微分为零；
$e_0,e_1$ 为好整基（其杯积为单位）。故 $u\in\mathbf Z_p^\times$。
这也证明族矩阵的首列模 $p$ 为零。这里所用的一般整比较见
P. Berthelot, L. Breen, W. Messing, *Théorie de Dieudonné cristalline II*,
LNM 930 (1982), Prop. 3.3.7 与 Th. 2.5.6（阿贝尔概形的反变
Dieudonné 晶体即相对一阶晶体上同调）；提升上的 de Rham 比较见
P. Berthelot, *Cohomologie cristalline des schémas de caractéristique
$p>0$*, LNM 407 (1974), Cor. V.2.3.7。对本文的光滑有限型特殊纤维及
其 $p$ 进平坦光滑提升，Q. Yan, *A local construction of zip period maps
of Shimura varieties*, Rend. Sem. Mat. Univ. Padova **151** (2024),
[pp. 219--223, Lemma 2.1(3),(4), Remark 2.5, Theorem 2.6,
(2.1),(2.2), Remark 2.7](https://doi.org/10.4171/RSMUP/137)
明确给出 étale 及完备盘变基、整水平 $F,V$、$FV=VF=p$、Hodge 线
的 Frobenius pullback 等于 $F\bmod p$ 的核及抬升后过滤的比较。
这些命题适用于这里的一般椭圆族。杯积的精确乘子也可用原主极化：
相对 Frobenius 的对偶同源为 Verschiebung，故
$\langle Fx,Fy\rangle=\langle x,VFy\rangle=p\langle x,y\rangle$。

实际底行是
$$
 W_{21}=-uB B(t^p)-(p/u)A A(t^p),\qquad
 W_{22}=-uB B'(t^p)-(p/u)A A'(t^p).
$$
其中 $A,B$ 不带复合者在 $t$ 处。由(125)，$B=t+O(t^4)$、
$A=1+O(t^3)$、$A'=O(t^2)$、$B'=1+O(t^3)$。
故 $W_{21}=-pA/u+O(t^{p+1})$、$W_{22}=-uB+O(t^{2p})$，
这些是特征零的次数界。令
$$
 U(t)=W_{21}(t)/W_{21}(0),\quad
 V(t)=W_{22}(t)/(t\,\partial_tW_{22}(0)),\quad R(t)=U(t)/V(t).
 \tag{F2}
$$
三个常数项均为一。$W_{21}(0)=-p/u$、
$\partial_tW_{22}(0)=-u$，所以 **两未知标量在各自归一行中消去**。
$U=A+O(t^{p+1})$、$V=B/t+O(t^{2p-1})$。整性只需§27的有限窗；
任一好整函数由 $t$ 代入。逆变量 $s(t)=\int J(t)dt$ 在所需
$n\le p+2$ 范围整：可能的非单位分母 $n=p$ 与 $n\equiv1\bmod3$
冲突。首列含一次 $p$，所以统一按原矩阵求三位归一行时，
$W_{21},W_{21}(0)$ 保模 $p^4$、$W_{22},\partial_tW_{22}(0)$
保模 $p^3$ 总是足够。

$f,h$ 在 $P$ 至少三阶消失，于是下式皆为**准确系数相等**：
$$
 \begin{aligned}
 E_N&=[t^N]fJ\,V^{-3/2}R^{p/2},\qquad
 E_d=[t^d]fJ\, V^{-3/2}R^{p+1/2},\\
 L_r(h)&:=\frac{\mathsf T_r^{(1)}h(P)}{r!}
       =[t^r]hJ\,V^{-1}R^r,\qquad r=p,d.
 \end{aligned}
 \tag{F3}
$$
直接对(123)最后的留数换元，保留 $ds=Jdt$。三重零使 $V,U$ 最多
读到 $d-3=p-2$，全在(F2)准确窗内。将(F3)代(128)--(130)即得原
两条 Gaussian 读数及共同分子的相同三位/两位精度。
$R^p=(1+(R-1))^p$ 使用全部
$\binom{p}{j}(R-1)^j$，包括每个落在本窗且 $0<j<p$ 的项；
此处不作仅两端的特征 $p$ 对称幂替换，(140)的 mixed 行仍完整适用。

### 32.2 原固定权三截面上的两条 Serre 类及准确相对迹

记 $X$ 为§29固定覆盖的光滑紧化，$L$ 为延至 cusps 的物理 Hodge 线。
沿用杀全部原乘子的同一覆盖。在 $P$ 旁用 $e_0$ 作 $L$ 的基。
由(135)及权三 cusp 条件，$\omega_h=h e_0 ds$ 延为
$H^0(X,K_X\otimes L)$ 的截面：局部 cusp 参数中 $d\tau$ 有对数极，
cusp form 的正阶已抵消此极。这是标准 $S_3\simeq H^0(K_X\otimes L)$
的具体截面。其 $P$ 处的三重零给
$\omega_h\in H^0(X,K_X\otimes L(-3P))$。
令 $\operatorname{pp}_{>3,P}$ 保留 $t^{-4}$ 至最高极项；
对 $L^{-1}(3P)$ 而言其余项都已正则。由单点主部的连接同态取两条类
$$
 \begin{aligned}
 q_{d,p}&=\partial\operatorname{pp}_{>3,P}
      \{t^{-p-2}U V^{-2}R^p e_0^\vee\},\\
 q_{p,p}&=\partial\operatorname{pp}_{>3,P}
      \{t^{-p-1}V^{-1}R^p e_0^\vee\}
          \quad\in H^1(X,L^{-1}(3P)).
 \end{aligned}
 \tag{F4}
$$
连接号取 Serre 配对为正留数的约定。(F2)给同(137)实际主部相同的类；
例如第一行只用至 $t^{p-2}$，不存在被隐藏的最后一格。
于是 $\langle\omega_h,q_{r,p}\rangle=L_r(h)$ 精确成立。
这将两条随 $p$ 主部放在固定维的 coherent 群，并指定其在
**同一个** $\Phi_{f,g}$ 上的值；并未从§29的正范数推这些值非零。

同一配对也有真实相对 Frobenius 迹。置
$$
 K_p(t)=t^{-2}V^{-2}R^p,\qquad \mathcal V(t)=pW(t)^{-1}.
$$
$K_p\omega_h$ 在 $P$ 正则且至少一阶消失。定义
$\operatorname{Tr}_{t^p/T}(\sum a_nt^ndt)
 =\sum_m a_{pm+p-1}T^m dT$；
这是有限映射 $T=t^p$ 的微分迹，因为
$dt=dT/(pt^{p-1})$ 且函数迹杀掉所有非 $p$ 的倍数次幂。
在目标的代数基中有准确式
$$
 \boxed{
 \left.\frac{\operatorname{Tr}_{t^p/T}
       (\mathcal V(t) K_p(t)\,\omega_h)}{dT}\right|_{T=0}
   =p C^{-1}\binom{L_d(h)}{L_p(h)}
   =\binom{-u L_p(h)}{p L_d(h)/u}.}
 \tag{F5}
$$
确实 $\mathcal V=p M(T)^{-1}C^{-1}M(t)$；
目标框架可移出迹，在目标点为 $I$。源端 $M(t)e_0=(A,B)^t$，
取 $t^{p-1}$ 及(F2)正给(F4)的两个留数。此证明也说明第二输出的
额外 $p$ 不能在给定精度的 trace 中无成本除去。
输入含指定局部函数 $K_p$，不是把固定类单独施加一次 Frobenius。
若原水平系数在扩域，(F5)的有限映射用前述相对约定逐项作用于
完整 $h$；不向每个 $\gamma_a,\delta_b$ 擅加固定性。

### 32.3 超奇异处的真实首分母与全局有理 Cartier 核

$H$ 准确是 R856(5) 的 Hasse 系数。模 $p$ 时，物理族的 Verschiebung
在微分上给 $\mathcal V(e_0)=H e_0^{(p)}$：直接对
$dx/(2y)=(x^3-g_2x/4-g_3/4)^{(p-1)/2} dx/(2y^p)$ 用相对
Cartier 提取 $x^{p-1}$ 系数即可。在特征 $p$ 这与几何
Verschiebung 对不变微分的拉回一致。由水平性、$\nabla e_0=e_1ds$
和目标 pullback 基连接的导数模 $p$ 为零，
$\mathcal V(e_1)=(DH)e_0^{(p)}$。在 $P$ 得 $-u\equiv C_0$。
由(F1)底行第一项及整首列，取 $t^{p+1}$ 给
$$
 p[t^{p+1}]A\equiv-u^2\equiv-C_0^2\ne0\pmod p .
 \tag{F6}
$$
这里 $BB(t^p)$ 的指定系数为一，$A(t^p)-1=O(t^{3p})$。
所以(126)的首个可能分母在物理族的指定解中确实发生。
它与低窗的整性相容。$B/t$ 至 $t^{p+1}$ 整且常数一，
故 $p[t^p](A/B)\equiv-u^2$，由 $d(A/B)=-ds/B^2$ 得
$$
 [t^{p-1}]\,\frac{C_0^2 J}{H^2}
   \equiv [t^{p-1}]\frac{J}{B^2}
   \equiv C_0^2\pmod p .
 \tag{F7}
$$
第一次替换确需 $B/t$ 到 $t^{p+1}$ 的模 $p$ 同余，
由§30 (142)--(144)的全 $d$ 窗及上述整换参得到。

在参数 $E_{16,\mathbf F_p}$ 上，从(F7)得到全局相对 Cartier 恒等式
$$
 \mathscr C(ds/H^2)=ds^{(p)}. \tag{F8}
$$
证明：$H$ 的唯一可能极是 $O$，其极阶至多 $(p-1)/2$，
因 $g_2,g_3$ 极阶为 $2,3$，R856(5)中每个单项式的加权极阶
都是 $3(p-1)/2-(p-1)$。$H(P)=0,(DH)(P)\ne0$ 使其非恒定。
因此任何零的重数 $m<p$；模 $p$ 的 $D^2H+aH=0$ 与
$ds$ 处处无零迫 $m=1$，否则最低项含非零 $m(m-1)$。
在每个简单零，写 $H$ 本身为坐标，则
$ds/H^2=H^{-2}(DH)^{-1}dH$，其留数为
$-D^2H/(DH)^3$ 在此零处的值，因方程为零。
相对 Cartier 杀掉各二极的极部，输出全局正则。
属一曲线上其比例由 $P$ 的值确定，(F7)正给一。
R79 的 Legendre 规范在另一参数上有相类公式；
此处所用 $E_{16}$、不变 $ds$、原 $H$ 和 $C_0$ 均按本题模型确定。

进一步在 $K=\mathbf F_p(E_{16})$ 中取 $t$ 为分离参数。
$p$-基分解 $K=\bigoplus_{i=0}^{p-1}K^p t^i$ 及(F8)给唯一
$Q_p\in\bigoplus_{i=1}^{p-1}K^p t^i$ 满足
$$
 dQ_p=ds/H^2-t^{p-1}J^p dt . \tag{F9}
$$
实际上相对 Cartier 把右侧第二项送到 $J^{(p)}dT$，
故右差的 $t^{p-1}dt$ 分量为零；对剩余 $i=0,\ldots,p-2$
逐项以 $t^{i+1}/(i+1)$ 积分即可。$P$ 旁 $Q_p$ 的 Laurent 展开
没有 $t^{jp}$ 项，特别无常数项；由(F9)在此至多简极。
$A/B$ 在 $t^{-1},\ldots,t^{p-1}$ 整，其常数项由三次型为零。
在此截窗中 $d(A/B)=-ds/B^2\equiv -C_0^2 ds/H^2$，
比导数只需到 $t^{p-2}dt$，此时(F9)最后一项还未参与。
于是该整窗内 $A/B\equiv-C_0^2 Q_p\bmod p$。
不要把这个同余扩大到 $t^p$，(F6)准确给出那一格的分母。

由于 $(tA/B)^p\equiv1$ 在所需模 $p$ 的 $p-2$ 窗内，将(F4)的
两个主部约化后可用**全球有理系数**替换为
$$
 \begin{aligned}
 q_{p,p}:&\quad C_0\,t^{-p}/H,\\
 q_{d,p}:&\quad -C_0^3\,t^{-p}Q_p/H .
 \end{aligned}
 \tag{F10}
$$
每行省写共同的 $e_0^\vee$，在 $P$ 仍只取 $>3$ 极阶再用连接同态，
不把全局有理函数的所有极同时当成只在 $P$ 的主部。
因此对原水平覆盖上的**整项** $h$ 有
$$
 \begin{aligned}
 L_p(h)&\equiv C_0
   \left.\mathscr C(h\,ds/H)/dT\right|_{P^{(p)}},\\
 L_d(h)&\equiv -C_0^3
   \left.\mathscr C(h Q_p\,ds/H)/dT\right|_{P^{(p)}}
                                      \pmod p .
 \end{aligned}
 \tag{F11}
$$
这里把 $H,Q_p,ds$ 全部拉回原固定覆盖，
relative Cartier 在各点有(F5)的模 $p$ 系数提取式；
两输入在 $P$ 因 $h$ 三重零均正则。(F11)是原两个实际读者的
全局有理 **mod $p$** 返回。(F3)--(F5)则在同一来源上保留
准确的全部高位，不能拿(F10)的首层替代(F2)的更深矩阵系数。
(F8)的非零没有消掉(F11)中的原 $h$，也不决定(130)的第二位。

### 32.4 完整两位、三位读者的代数 Frobenius 差

(F11)以外的精度也可在实际代数图上保留。先在参数曲线去掉
$O,g_3=0,g_3=4$，留下包含所选 $P$ 的仿射开集。其方程仍为
$g_3^2=16(1-32t^3)$，对 $t$ 是 étale 图。在其 $p$ 进完备环上
$T\mapsto t^p$ 有确定的相对 Frobenius 提升：送目标 $g_3$ 至
$$
 g_3^p\left\{16(1-32t^{3p})/g_3^{2p}\right\}^{1/2}.
$$
花括号模 $p$ 为一，平方根取一模 $p$ 的支；
在 $P$ 的限制正是原来 $T=t^p$ 的提升。所逆的函数模 $p$ 仍被送至单位，
故此图上定义。由于原完整水平覆盖有限 étale，其到目标 Frobenius twist
的相对 Frobenius 由形式 étale 性唯一提升至这些完备图。
若只在源的系数域中书写，仍按§32.1的相对标量约定；
下面的 $W,G,S,R$ 来自定义于 $\mathbf Z_p$ 的物理族。

物理族在此图光滑 proper，原相对一阶晶体在提升上给整矩阵 $W$。
$e_0,e_1$ 在图上作基，因杯积为单位且组成各纤维两维格的基。
模 $p$ 的 Hodge 结论及 $\det W=p$ 给
$$
 S=W_{22},\qquad G=W_{21}/p,\qquad
 S\equiv H,\quad W_{12}\equiv-DH\pmod p .                  \tag{F12}
$$
后两式也由 $\mathcal V=\operatorname{adj}W$ 及§32.3对两基的
几何 Verschiebung 像得到。$S(P)=0$ 在特征零准确成立。
本图 $t=0$ 只含所选分支，且 $(g_3-4)(g_3+4)=-512t^3$，
故 $S\in t\widehat{\mathcal O}$。再在特殊纤维限制到 $H/t$ 为单位
的开集；其值在 $P$ 为 $C_0\ne0$。相应完备图上 $S/t$ 为单位。
因此(F2)的 $U=-uG, V=-S/(ut)$ 和
$$
             R=t u^2G/S
$$
都为这同一个图上的整 $p$ 进函数，$R(P)=1$，$V$ 可逆。
它们在每个 $p^m$ 上由这个仿射代数环的实际元素给出：
$p$ 进完备对模 $p^m$ 不改变原环的商。这里并不需要把
$W$ 的特征零系数说成代数函数，亦未沿超奇异盘引入 ordinary splitting。

真实底行还给一个含准确两位修正的原函数。
由 $M'=M\left(\begin{smallmatrix}0&-a\\1&0\end{smallmatrix}\right)$
（此处 $'=D$）及(F1)，令
$c(t)=t^{p-1}J(t^p)/J(t)$，则
$$
 D W_{21}=-W_{11}+p c(t)W_{22},\qquad
 D W_{22}=-W_{12}-p c(t)a(t^p)W_{21}.
$$
取商、用行列式并乘 $ds$ 给准确微分
$$
 d(G/S)=-\frac{ds}{S^2}
       +t^{p-1}J(t^p)\big\{1+p^2 a(t^p)(G/S)^2\big\}dt .
 \tag{F13}
$$
因此 $-G/S$ 以原几何 $S$ 给出(F9)的模 $p^2$ 微分提升，
其未约的误差从所示 $p^2$ 项开始。模 $p$ 有 $G/H+Q_p\in K^p$，
由同一物理 $W$ 决定该 $p$ 次幂项；并未从(F9)单独恢复它的全局值。
(F13)按所示亚纯系数恒等地使用，在 $P$ 可取 Laurent 展开。

定义这个实际函数的一次 Frobenius 差
$$
 \mathfrak d_p(R)=\frac{R^p-\varphi^*R}{p}.                 \tag{F14}
$$
因 $R$ 来自物理 $\mathbf Z_p$ 图，分子在全图可除以 $p$；
故它是指定的整函数，在每个有限精度都是代数剩余类。
$R(P)=1$ 保证在 $P$ 有 $\varphi^*R=1+O(t^p)$。
于是 $R^p$ 的本次完整 $p-2$ 窗**准确等于**
$1+p\mathfrak d_p(R)$ 的相同窗口。
代入(F3)得
$$
 \begin{aligned}
 E_N&\equiv [t^N] fJ V^{-3/2}
   \left(1+\frac p2\mathfrak d_p(R)
             -\frac{p^2}{8}\mathfrak d_p(R)^2\right)\pmod{p^3},\\
 E_d&\equiv [t^d] fJ V^{-3/2}R^{1/2}
   \left(1+p\mathfrak d_p(R)\right)\pmod{p^2}.
 \end{aligned}                                                  \tag{F15}
$$
上式的平方根取原局部常数一分支；第二行括号在所需窗实际精确。
这里是**同一个**几何 Frobenius 差而不是从两端模 $p$ 数据
猜一组中项。即使 $R=1+X$，(F14)的分子仍保留
$\sum_{i=1}^{p-1}\binom pi X^i$ 和真实 $X^p-\varphi^*X$。
(F15)前行须保 $\mathfrak d_p(R)\bmod p^2$，
后行须保 $\mathfrak d_p(R)\bmod p$，同时按各自模数保 $V$ 等前因子。

最后，这个差直接给原 $h$ 的全局微分迹两层。
写 $\mathcal T(\xi)=(\operatorname{Tr}_\varphi(\xi)/dT)(P^{(p)})$。
此处 $\varphi$ 是上述完整水平图的相对提升。
在模 $p$ 图上相对 Frobenius 有限平坦次数 $p$，其上述 $p$ 进提升
亦有限局部自由：可局部提升特殊纤维的模基，用 $p$ 进完备性逐次生成；
关系逐次除以 $p$，由 $p$ 平坦性及分离性得线性无关。
在所选目标点的完备盘只有原源点的分支（特殊纤维相对 Frobenius
为根式态射、且水平覆盖 étale），因此全局亚纯微分迹在此盘
就是(F5)的系数迹。以下微分均在所取源点正则。
从 $B\sim-S/u$、$A\sim-uG$ 的(F2)准确截窗，得到
$$
 \begin{aligned}
 L_p(h)&=-u\big\{\mathcal T(h\,ds/S)
                   +p\mathcal T(\mathfrak d_p(R)h\,ds/S)\big\},\\
 L_d(h)&=-u^3\big\{\mathcal T(hG\,ds/S^2)
                   +p\mathcal T(\mathfrak d_p(R)hG\,ds/S^2)\big\}.
 \end{aligned}                                                   \tag{F16}
$$
具体地，留数最初在两行的括号中各有乘子 $R^p$；
代(F14)，然后用迹的投影公式移出 $\varphi^*R$。
目标值 $R(P^{(p)})=1$ 因物理函数及物理 $P$ 均从 $\mathbf Z_p$
取得。整段只对源 $h$ 取完整 trace，没有让 $\varphi$ 固定任一
$\gamma_a,\delta_b$。(F16)为准确等式；其模 $p^2$ 必须同时读第一项
到两位和第二项到一位。这把原固定权三截面的两个 moving 配对的
深层校正落到真正有限精度的代数 Frobenius 核上，
但还未证明原 canonical 第二位在无穷素数非零。

## 33. 原冻结 $f$ 与两条 canonical 分子的同一全局一阶迹

本节使用(F2),(F3),(F12)--(F16)的同一 $W$，
直接处理原半权质量 $f$。完整水平覆盖、$\gamma_a$ 及(127)的
$\mathsf a_p,\mathsf b_p,\gamma$ 照旧。

### 33.1 固定二盖及其两个低阶返回

在 $E_{16}$ 取固定二盖 $z^2=t$，归一化后把原完整水平覆盖拉回。
底层曲线在仿射图的方程为 $g_3^2=16(1-32z^6)$。
对上述好素数它在 $z=0,g_3=-4$ 光滑，$z$ 是参数；在此处
二盖确实分歧，输入的 $f$ 因而从 $z^6$ 开始。
在这张图的光滑完备提升上**直接**定义目标 $Z\mapsto z^p$ 和
§32.4所给 $g_3$ 的 Hensel 像（代入 $t=z^2$）。其平方为 $t^p$，
故与原参数 Frobenius 交换；此处未将从 $t$ 盘到 $z$ 盘的分歧
态射当成 étale。随后拉回的完整水平覆盖才是有限 étale，
由形式 étale 性唯一提升相对 Frobenius。本段仍在原 $D(H/t)$ 的逆像，
它包含所选 $z=0$ 点且特征 $p$ Frobenius 原像保持此开集；
故完备后的提升仍以此开集为目标。相对 Frobenius 有限局部自由
次数 $p$，证明同(F16)，或在 $z$ 形式坐标直接用 $1,z,\ldots,z^{p-1}$。

为使所有函数在同一固定二盖上读取，取两个明确 Taylor 多项式
$$
 n(t)=\sum_{j=0}^{p-2}\binom{-3/2}{j}(V(t)-1)^j,\qquad
 r(t)=\sum_{j=0}^{p-2}\binom{1/2}{j}(R(t)-1)^j .
 \tag{G1}
$$
这些是物理图上的整 $p$ 进函数，在每个有限精度均为代数函数的
剩余类。因 $V(0)=R(0)=1$，它们在所选点的模 $t^{p-1}$ 截窗
分别准确等于 $V^{-3/2}$ 和 $R^{1/2}$。
无需再加随 $p$ 更动的平方根盖。下文在 $z$ 盘上出现的
$f,J,n,r,R$ 均在 $t=z^2$ 处取值，不动其中任何原水平常数。

定义真正同源的两条正则局部微分
$$
 \beta=z^{-2}fJn\,dz,\qquad \beta_2=(r/z)\beta .
$$
它们在 $z=0$ 分别至少为四阶、三阶；在全图作亚纯微分。
对相对全局迹记
$$
 \mathcal U_i(\theta)=[Z^i]\operatorname{Tr}_{\varphi_z}(\theta)/dZ,
 \qquad i=0,1 .
$$
在原点的完备盘有
$\mathcal U_0(B\,dz)=[z^{p-1}]B$、
$\mathcal U_1(B\,dz)=[z^{2p-1}]B$；
特殊纤维相对 Frobenius 普遍单射，故全局迹在此点正给此唯一局部
分支的迹。$\beta$ 对 $z\mapsto-z$ 反不变、$\beta_2$ 不变，
故分别读取迹展开首个允许的偶阶、奇阶系数。
原(127)的两系数为
$$
 E_N=\mathcal U_0(r^p\beta),\qquad
 E_d=\mathcal U_1(R^p\beta_2).
 \tag{G2}
$$
证明：前者读 $[z^{p+1}]fJn r^p$，且 $p+1=2N$；后者读
$[z^{2p+2}]fJn rR^p$，且 $2p+2=2d$。由 $f$ 三重零，
两式所用 $n,r$ 都只到 $t^{p-2}$，(G1)准确给(F3)所需的幂。
这不是将 $f$ 与参考 $g$ 作乘法后再反推半权，式中为原 $f$ 本身。

### 33.2 单一一阶迹及三位共同分子

对 $k=1,2$，形成一个在原点正则的全图亚纯微分
$$
 \Xi_{k,p}=\beta\left(
 k\gamma\mathsf a_p(zr)^p-p\mathsf b_p (r/z)R^p\right).
$$
由于 $\varphi_z^*Z=z^p$，迹的投影公式和(G2)给准确等式
$$
 \boxed{\quad
 \mathcal U_1(\Xi_{k,p})
  =k\gamma\mathsf a_p E_N-p\mathsf b_p E_d .\quad}          \tag{G3}
$$
该微分对 $z\mapsto-z$ 不变，其迹的常数系数因而为零。
在 $g_1\in p$ 的原范围，置(130)的 $X_p,Y_p$，遂有
$$
 \frac{\mathcal U_1(\Xi_{2,p})}{p^2}=2\gamma X_p-Y_p,\qquad
 -\frac{\mathcal U_1(\Xi_{1,p})}{p^2}=Y_p-\gamma X_p .
 \tag{G4}
$$
这里两条分子先各自整合再除 $p^2$；各自再乘 $\gamma^{-2}$ 的约化
才是(130)指定之位。仅第一条是 $J'(0)=0$ 的指定第二位条件。

还可在同一来源把对称幂的完整校正分开，令
$\mathfrak d_p(r)=(r^p-\varphi^*r)/p$，它与(F14)一样全图整。
拉到目标盘 $r=r(Z^2)$、$R=R(Z^2)$，
故二者常数一、一次项零；即使使用完整水平覆盖也不改变这一物理事实。
由投影公式，
$$
 \mathcal U_0(r^p\beta)=\mathcal U_0(\beta)
               +p\mathcal U_0(\mathfrak d_p(r)\beta),\qquad
 \mathcal U_1(R^p\beta_2)=\mathcal U_1(\beta_2)
               +p\mathcal U_1(\mathfrak d_p(R)\beta_2).
 \tag{G5}
$$
所以(G3)的三位需保第一组的三位/两位和第二组的两位/一位。
在(G2)的有效截窗中，$\mathfrak d_p(r)$ 准确给
$(\sqrt{1+p\mathfrak d_p(R)}-1)/p$ 的相同窗口，因为(G1)、
$\varphi^*r=\varphi^*R=1+O(t^p)$；比较整数精度给(F15)的同一
$-p^2\mathfrak d_p(R)^2/8$。无论在原图还是二盖，
没有把一阶迹非零、非退化或其跨 $p$ 行为当作已得结论。

## 34. 全惰性素数的真实周期短多项式及原共同分子的第三位尾

在§32的同一参数中取 $w=32t^3$，$p=12m+e$，其中
$e=5$ 或 $11$。本节给(G3)的一项能在 $E_d$ 两位删除、
但须在 $E_N$ 三位保留的实际尾部。

### 34.1 两种惰性剩余类的完整原周期

$D=\sqrt{1-32t^3}\,\partial_t$、$a=-2t$。因而
$D^2Y+aY=0$ 即
$(1-32t^3)Y_{tt}-48t^2Y_t-2tY=0$。
写 $\theta=t\partial_t$，同一方程成为
$$
 \{\theta(\theta-1)-32t^3(\theta+1/4)^2\}Y=0 .
$$
其两个初值解由递推在特征零唯一确定，给
$$
 A={}_2F_1(1/12,1/12;2/3;w),\qquad
 B/t={}_2F_1(5/12,5/12;4/3;w)
      =L_e(w)\,{}_2F_1(e/12,e/12;4/3;w),
 \tag{G6}
$$
$L_5=1$、$L_{11}=(1-w)^{1/2}=-g_3/4$。
第二个写法在 $e=11$ 时就是 Euler 变换：代
$Y=(1-w)^{1/2}Z$ 于第二个超几何方程，新的两个上参
均为 $4/3-5/12=11/12$，相同常数一初值保证等式。
初值 $B'_s(0)=1$ 与 $t'_s(0)=1$ 一致。
因此(G6)是(F2)在实际所需窗内的两条**同一**物理行。
没有另换 Legendre 族、原 $H$ 的提升或归一单位。

令 $M=(p-2)/3$（为整数），写 $(a)_j$ 为上升阶乘。置
$$
 c_j=\frac{(e/12)_j^2}{(4/3)_j j!},
 \qquad P_m(w)=\sum_{j=0}^m c_j w^j,\qquad b_0=L_eP_m .
$$
取 $0\le j\le M$，所有 $(4/3)_j j!$ 为 $p$ 单位：
$3i+4$ 的首个为 $p$ 倍数的正值为 $2p$，而
$0\le i<j\le M$ 给 $3i+4\le p-1$，且 $j<p$。
上参 $e/12=-m+p/12$。若 $j>m$，乘积中唯一的 $p$ 因子
在 $i=m$ 处，准确等于 $p/12$；其余因子均为单位。
因此 $v_p(c_j)=2$，且
$$
 \frac{c_j}{p^2}\equiv
 \frac{(m!(j-m-1)!)^2}{144(4/3)_j j!}\pmod p
 \qquad(m<j\le M).                                         \tag{G7}
$$
若 $j\le m$，令 $S_j=\sum_{i=0}^{j-1}(i-m)^{-1}$、
$S_j^{[2]}=\sum_{i=0}^{j-1}(i-m)^{-2}$（空和为零），则
$$
 c_j\equiv\frac{(-m)_j^2}{(4/3)_j j!}
 \left\{1+\frac p6 S_j+\frac{p^2}{144}
               (2S_j^2-S_j^{[2]})\right\}\pmod{p^3}.        \tag{G8}
$$
这由 $\prod_i(1+p/[12(i-m)])^2$ 展开直接得到。
特别 $P_m$ 在此处保留原系数的完整前缀，不能先用裸 $(-m)_j^2$
取代它。$A$ 的(G6)在相同 $w$ 窗也整：分母 $(2/3)_j$ 的首个
可能 $p$ 因子在 $i=(p-2)/3=M$，故首次影响 $j=M+1$。
这些界与(F6)的首分母位置一致。

### 34.2 在原 $X_p,Y_p$ 的两位和三位中分配该尾

在 $w$ 的 $M$ 窗定义
$$
 T_p(w)=\sum_{j=m+1}^{M}
       \frac{(m!(j-m-1)!)^2}{144(4/3)_j j!}\,w^j .
$$
由(G7)，在此前缀
$B/t\equiv b_0+p^2 L_eT_p\bmod p^3$。
$b_0(0)=1$，它在 $p$ 下的 $N$ 或 $d$ 读者中可取原正规幂。
由(F3)或原留数取 $A$ 的实际(G6)，置
$$
 E_N^0=[t^N]fJ\, A^{p/2} b_0^{-(p+3)/2},\qquad
 E_d^0=[t^d]fJ\, A^{p+1/2} b_0^{-p-2}.
$$
这是只截去了已明确指定的 $B/t$ 后缀，并保留整 $f$、$A$、$J$
和原前缀 $b_0$。令
$$
 I_p=[t^N]fJ b_0^{-5/2} L_eT_p .
$$
则
$$
 E_N\equiv E_N^0-\tfrac32 p^2I_p\pmod{p^3},\qquad
 E_d\equiv E_d^0\pmod{p^2}.                                  \tag{G9}
$$
确实全核最多读 $t^{d-3}=t^{p-2}$，即给定的 $w$ 窗。
$E_N$ 的指数为 $-(p+3)/2$，故 $p^2$ 修正只入一次；
模 $p$ 该指数是 $-3/2$。对剩下的因子
$A^{p/2} b_0^{-p/2}$，两支平方根常数均一，
其 $p$ 次幂在 $t$ 的 $p-2$ 窗模 $p$ 均为一。
这给上述 $I_p$ 全系数。$E_d$ 的修正至少 $p^2$ 直接消失。
$T_p$ 的单项只要落入 $I_p$ 仍须经过真实 $f$ 的全部卷积；
各 $c_j/p^2$ 为单位不意味着 $I_p$ 为单位。

特别(G3)的同一一阶迹现在满足
$$
 \mathcal U_1(\Xi_{k,p})\equiv
 k\gamma\mathsf a_p E_N^0-p\mathsf b_p E_d^0
          -\tfrac{3k}{2}\gamma\mathsf a_p p^2 I_p
                                      \pmod{p^3},\quad k=1,2 .
 \tag{G10}
$$
在 $g_1\in p$ 的原范围，(G9)亦使 $E_N^0\in p^2$、
$E_d^0\in p$；故 $I_p$ 给第一条 canonical 第二位
$(2\gamma X_p-Y_p)/\gamma^2$ 的实际校正
$-3\mathsf a_p I_p/\gamma\bmod p$。第二条读者依(G4)保相反符号
及 $k=1$ 的因子。至此(G7)中此前可能被整体丢掉的第三位尾已按
原权幂、真实 $f$ 及两条 canonical 分子的精度准确分配；
尚未得到前缀与此尾合成后的无穷非零。本节未运行数学程序。

## 35. 第三位尾的两个固定受迫周期与原 $I_p$ 的跨素数系数

取(G6)--(G10)的同一 $p=12m+e$（$e=5,11$），置
$a=e/12,c=4/3,\lambda=1-a$。定义两个固定的特征零 germ
$$
 Z_e(w)={}_3F_2(1,1,1;c+\lambda,1+\lambda;w).
$$
记 $D_e=(12-e)(16-e)$，故 $D_5=77,D_{11}=5$。真实单位
$$
 k_p=\frac{(m!)^2}{144(c)_{m+1}(m+1)!}
     \equiv c_m/D_e\pmod p
$$
使用(G8)的同一 $c_m$。分母在原窗为单位，后式由
$144(c+m)(m+1)\equiv D_e$ 直接得到。
则(G7)的全尾在 $w^M$ 窗精确给
$$
 T_p(w)\equiv k_p w^{m+1} Z_e(w)\pmod p.                 \tag{H1}
$$
确实 $j=m+1+k$ 时(G7)与其首项的比为
$(k!)^2/((c+m+1)_k (m+2)_k)$，用 $m\equiv-a$ 正是 $Z_e$ 的
第 $k$ 系数。此式只在给定窗内约化，未将特征零 $Z_e$ 的任意
高系数声称为 $p$ 整。

令 $b=B/t$（同(G6)），$f_*(w)$ 是原 $f(t)$ 按 $w=32t^3$
写出的同一 germ；其存在由§27.3的三次型与实际换参。
在(G9)的 $I_p$ 中可将 $b_0$ 模 $p$ 换回 $b$。因 $N$ 为三的倍数，
得到跨 $p$ 的准确公式
$$
 I_p\equiv k_p\,32^{N/3}
 [w^{m+(e-5)/6}]
       f_*(w)(1-w)^{-1/2} b(w)^{-5/2} L_e(w)Z_e(w)
                                                      \pmod p.\tag{H2}
$$
这两个被提取的形式 germ 在各自剩余类上与 $p$ 无关，
并保留了原冻结质量。公式带 $b^{-5/2}$；
没有据 $Z_e$ 的超几何方程断言整个乘积为 D-finite。

在 $\Theta=w\partial_w$ 下令
$\mathcal L_a=\Theta(\Theta+c-1)-w(\Theta+a)^2$。
直接用 $Z_e$ 的系数比得
$$
 \mathcal L_a(w^\lambda Z_e)=\lambda(\lambda+c-1)w^\lambda .
 \tag{H3}
$$
除常数项外的各系数均由该比相消；这里
$\lambda(\lambda+c-1)=D_e/144$。
在固定四盖 $t=x^4$ 上取 $w^{1/12}=32^{1/12}x$ 的一致支，
记 $Y=(1-32x^{12})^{1/2}=-g_3/4$，
$$
 y_e=t L_e(w) w^\lambda Z_e(w).
$$
在此盖 $w^{m+1}=32^{p/12}x^p w^\lambda$，其中 $x^p$ 确为
$t\mapsto t^p$ 的相容提升 $X\mapsto x^p$ 对目标坐标的拉回。
故(H2)的等价写法为
$$
 I_p\equiv k_p32^{p/12}
   [x^{p-1}]\,x^{-7} f(x^4)J(x^4)b(x^4)^{-5/2}y_e
                                                   \pmod p.    \tag{H4}
$$
两条射线都有**同一**固定乘子及同一次 $x^{p-1}$ 提取。
若未扩张系数域以含 $32^{1/12}$，直接用(H2)即可。
(H4)中 $y_e$ 采用上述特征零规范并只在所需整窗读取。

由(G6)的算子或直接求导，
$(D^2+a_{\rm GM})(tL_e F)=9t^{-1}L_e\mathcal L_a F$，
这里 $a_{\rm GM}=g_2/12$。故这两行准确来自原 GM 连接下的
两条固定代数一形式
$$
 \begin{aligned}
 \Omega_5&=(D^2+a_{\rm GM})y_5\,e_0 ds
     =\tfrac{77}4\,32^{7/12}\,(x^6/Y)e_0\,dx,\\
 \Omega_{11}&=(D^2+a_{\rm GM})y_{11}\,e_0 ds
     =\tfrac54\,32^{1/12}\, e_0\,dx .
 \end{aligned}                                                  \tag{H5}
$$
用的是 $ds=4x^3dx/Y$。
例如 $(Dy_e)e_0-y_e e_1$ 的协变导数正是所示 $\Omega_e$；
这给归一解析 germ 的实际来源。

## 36. 两条固定尾来源的完整边界特征空间

令 $C$ 为 $Y^2=1-32x^{12}$ 的光滑紧化，$D_\infty$ 为两个无穷点。
以下特征零计算可在代数闭系数域进行；选取的四盖先于 $p$。
先用有理规范
$$
 E_-=(x^6/Y)e_0 dx,\qquad E_+=e_0 dx,
$$
最后按(H5)乘回常数。两无穷点分别以
$l=\lim Y/x^6=\pm\sqrt{-32}$ 标记。取
$u_0=xe_0,u_1=e_1/x,\xi=1/x$，连接关于 $d\xi/\xi$ 的留数为
$$
 N_l=\begin{pmatrix}-1&-8/l\\-4/l&1\end{pmatrix}.
 \tag{H6}
$$
实际上
$\nabla u_0=u_0dx/x+x^2 u_1 ds$、
$\nabla u_1=-u_1dx/x+2x^2u_0 ds$，而 $x^2ds=4x^6(dx/x)/Y$。
因 $l^2=-32$，$N_l^2=0$，$[u_0]\ne0$ 于 $\operatorname{coker}N_l$。
这给在此正规对数延拓中的真实留数
$$
 \operatorname{res}_l E_-=-l^{-1}[u_0],\qquad
 \operatorname{res}_l E_+=-[u_0].                              \tag{H7}
$$
它们在两个 coinvariant 线上线性独立。
局部对数复形的留数落在 $\operatorname{coker}N_l$；
对数正则原函数的协变导数在此为零。即使允许亚纯原函数，
有极阶 $n>0$ 时首项矩阵 $-nI+N_l$ 可逆，不能产生至多对数的一形式，
故(H7)也排除亚纯 exact。在任一有限曲线覆盖上，留数及 $N_l$ 均乘
当地正分歧指数，勒除极阶的相同论证仍适用。
特别(H3)的两个指定非齐次 germ 不能是有限代数延拓上的代数原函数。

还能准确算出这两个特征上完整的 logarithmic de Rham 空间。
固定 $g,h$：$g(x,Y)=(\zeta_{12}x,Y)$，物理变换的同质因子
为 $\zeta_{12}^4$；$h(x,Y)=(x,-Y)$，物理同质因子为 $i=\zeta_{12}^3$。
物理变换在纤维写为 $(x_{\rm ph},y_{\rm ph})\mapsto
(\lambda^2x_{\rm ph},\lambda^3y_{\rm ph})$。
这正使目标的 $6t$ 和 $Y$ 成为原系数的 $\lambda^4,\lambda^6$ 倍；
$e_0,e_1$ 分别受 $\lambda^{-1},\lambda$ 作用（按拉回）。
二操作交换。$E_-,E_+$ 的 $(g,h)$ 特征分别为 $(i,i),(-i,-i)$。

令 $L$ 为对数延拓中的 Hodge 线，其在有限处以 $e_0$ 为基，
在无穷处以 $u_0$ 为基，故 $L=\mathcal O_C(D_\infty)$（由 $e_0$
指定同构），$\mathcal E/L=L^{-1}$ 由杯积给出。
考虑对数复形
$[\mathcal E\to\mathcal E\otimes K_C(D_\infty)]$ 的 Hodge 过滤。
其三个 graded 对第一超上同调的贡献的总维数给过滤后各特征维数的上界，
不要求预先证明谱序列退化。具体为：

1. 顶项 $H^0(K_C L(D_\infty))$ 的基为
   $x^k(dx/Y)e_0$（$0\le k\le6$）及 $e_0dx$。
   因 $dx/Y$ 在有限处处处非零，正则系数来自
   $\overline{\mathbf Q}[x,Y]/(Y^2-1+32x^{12})$；
   两无穷点同时的极阶界给 $k\le6$，带 $Y$ 的系数只准常数。
   七项特征为 $(\zeta_{12}^{k-3},i)$，最后的 $e_0dx$ 为 $(-i,-i)$。
   两指定特征各仅占一维。
2. 中间复形为 $[L\to L^{-1}K_C(D_\infty)]$ 的 Kodaira--Spencer 映射，
   在有限处由 $ds=4x^3 dx/Y$ 给，在两无穷点由(H6)的
   $-4/l\ne0$ 给。它单射，余核只在 $x=0,Y=\pm1$ 各长三。
   其六个局部 jets 用 $x^jdx\, e_0^\vee$（$j=0,1,2$）表示，
   $g$ 在两点分别固定，特征均为 $\zeta_{12}^{5+j}$；
   无 $(i,i)$ 或 $(-i,-i)$ 分量。
3. 底项 $H^1(L^{-1})$ 与 $H^0(K_C L)$ 对偶。
   后者按第一项去掉两 cusp 的简单极，基为
   $x^k(dx/Y)e_0$、$0\le k\le5$。
   其对偶特征 $(\zeta_{12}^{3-k},-i)$ 中既无 $(i,i)$，
   也无 $(-i,-i)$（后者需 $k\equiv6\bmod12$）。

这个上界与(H7)的精确下界相等。因此在每个指定特征中，
完整第一对数 de Rham 上同调恰为一维，并经留数同构到对应的边界线；
两特征之和经留数同构到两无穷点的完整 coinvariant 直和。
这给(H4)中两指定受迫周期的来源各自**没有 parabolic 分量**。
原§29的 $\Phi_{f,g}$ 及(H4)的实际 $fJ b^{-5/2}$ 从未由此被删去。
若在原完整水平覆盖上看同一来源，只断言上述两类的拉回保有非零留数，
不把附加覆盖全部特征空间的维数仍称作一。
