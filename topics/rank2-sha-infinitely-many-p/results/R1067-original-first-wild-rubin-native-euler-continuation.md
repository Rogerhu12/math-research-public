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

取杀掉原完整 theta/eta 矩阵和 $\eta^4$ 有限乘子的共同有限覆盖，
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
