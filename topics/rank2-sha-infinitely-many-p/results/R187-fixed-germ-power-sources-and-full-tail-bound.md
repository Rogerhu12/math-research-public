# R187. 固定逆级数的整幂源、四倍前缀与完整尾项界

日期：2026-11-12。**状态：下述实际原多项式、首分母、全部尾项、
原次数和完整旗标指数均已证明。** 本篇直接使用原固定级数，
不把任意整轴级数当作原源。主目标的无穷素数非零尚未证明。

## 1. 同一个固定逆级数与实际恒等式

固定惰性素数 $p\ge19$，令
$$
 r=(p+1)/4,\quad R=r(p-1),\quad m=p^q,\quad q\ge1,
 \qquad \varpi^R=p,\quad \lambda=\varpi^r,\quad\gamma=\varpi^p.
 \tag{1}
$$
沿用原坐标
$$
 a=e^{t(s)},\quad b=sa,\qquad
 A=a^{17}P(s),\quad B=a^{17}Q(s),\quad D_0=B-A.
$$
这里 $P=s+O(s^2)$、$Q-P=-22s^2+O(s^3)$，并且
$P,Q\in\mathbb Z[1/5][s]$。置
$$
 y=V(s)=Q(s)/P(s)-1=-22s+O(s^2),\quad
 S(y)=V^{-1}(y),\quad H(y)=A(S(y)).
 \tag{2}
$$
$S\in y\mathbb Z_p[[y]]$，$S'(0)=-1/22$ 是单位；$H$ 是
同一个不随 $p$ 改变的有理形式级数。定义
$$
 K(y)=\frac{y}{H(y)},\qquad
 U_m(y)=K(y)^m=\sum_{j\ge0}u_j^{(m)}y^j.
 \tag{3}
$$
$K(0)=-22$，故 $u_0^{(m)}=(-22)^m\ne0$。
以下所有截断均由 (3) 的准确有理系数给定。

在原曲线上，$y=D_0/A$、$A=H(y)$。因此有准确形式恒等式
$$
 \boxed{\quad D_0^m=A^{2m}U_m(D_0/A).\quad}
 \tag{4}
$$
式 (4) 的右边整体是一个合法的原曲线形式级数。
只有下文所示有限截断写回环境多项式；没有把其中的
$A^{-1}$ 当成原多项式源的自由生成元。

R186 的第一范数块系数满足
$c_j=-u_j^{(p)}$ 对 $0\le j<p$ 成立。本篇继续取到
$j=2m$，得到另一种实际原多项式；它不再是圆分范数的单个
齐次块截断，不需要把 $j\ge m$ 的系数误认作那个块。

## 2. 全部系数的尺度与准确首分母

令 $\sigma_q$ 满足
$$
 \sigma_q^{R p^{q-1}}=p.
$$
则 $R v_p(\sigma_q)=p^{1-q}$。R183 的实际幂级数结论为
$$
 a(\sigma_q T)^m-1\in\lambda\mathcal O'[[T]],
 \qquad
 [s^j]a(s)^m\in\mathbb Z_p\quad(j<rm),
 \tag{5}
$$
且 $d_{rm}=[s^{rm}]a(s)^m$ 满足 $v_p(d_{rm})=-1$。
所有环可放在同一个含有所需根的有限扩张中。

写
$$
 h(y)=\frac{y}{P(S(y))},\qquad
 K(y)=h(y)a(S(y))^{-17}.
 \tag{6}
$$
$h\in\mathbb Z_p[[y]]^\times$，$h(0)=-22$。
先由整严格代换 $S(\sigma_q T)/\sigma_q\in T\mathcal O'[[T]]$
把 (5) 代入，再作单位的负十七次幂，得到
$$
 a(S(\sigma_q T))^{-17m}-1\in\lambda\mathcal O'[[T]].
 \tag{7}
$$

这里不能遗漏 (6) 的有理单位因子。置
$Z=h(\sigma_q T)/(-22)-1\in\sigma_q T\mathcal O'[[T]]$。
对 $1\le k\le p^q$，准确有
$$
 v_p\binom{p^q}{k}=q-v_p(k).
$$
所以 $(1+Z)^m-1$ 的每项的赋值至少
$$
 \min_{0\le j\le q}\left(q-j+\frac{p^j}{R p^{q-1}}\right)
 =\frac pR>\frac rR.
 \tag{8}
$$
最后一个等号成立，因为 $p/R<1$，而 $j<q$ 的项至少一。
结合 (7)–(8)，有完整级数结论
$$
 U_m(\sigma_q T)/(-22)^m-1\in\lambda\mathcal O'[[T]],
$$
从而对每个 $j\ge1$，
$$
 \boxed{\quad Rv_p(u_j^{(m)})+p^{1-q}j\ge r.\quad}
 \tag{9}
$$
这控制全部尾项，并非只给一个有限整窗口。

另一方面，(5) 及整单位的反幂、整严格代换、乘法给
$$
 \boxed{\quad u_j^{(m)}\in\mathbb Q\cap\mathbb Z_p\quad(0\le j<rm).
 \quad}
 \tag{10}
$$
在 $j=rm$，唯一可能的首个非整贡献来自 $d_{rm}$。准确地，
$$
 u_{rm}^{(m)}
 \equiv-17(-22)^m(-22)^{-rm}d_{rm}\pmod{\mathbb Z_p}.
 \tag{11}
$$
其余项都只用更低的整系数。因此
$v_p(u_{rm}^{(m)})=-1$。本篇未假设整个 $U_m$ 都整。

## 3. 原次数准确 2m，实际前缀至少 4m+1

因为 $r\ge5$，有 $2m<rm$。定义原多项式
$$
 \boxed{\quad
 \mathcal S_m(A,B)=D_0^m-
   \sum_{j=0}^{2m}u_j^{(m)}A^{2m-j}D_0^j,
 \qquad D_0=B-A.
 \quad}
 \tag{12}
$$
(10) 说明 $\mathcal S_m\in(\mathbb Q\cap\mathbb Z_p)[A,B]$。
所有 $A$ 指数均非负。原次数 $m$ 的块恰为 $D_0^m$，
故 $\mathcal S_m$ 是 primitive；次数 $2m$ 的块不为零，
因为在整线性坐标 $(A,D_0)$ 中其 $A^{2m}$ 系数为 $-(-22)^m$。
$(A,D_0)\leftrightarrow(A,B)$ 保持次数和 Gauss 范数。于是
$$
 \deg_{A,B}\mathcal S_m=2m,
 \qquad\|\mathcal S_m\|_{\mathrm{Gauss},p}=1.
 \tag{13}
$$
这里不声称它关于 $B$ 是次数 $m$ 的首一多项式。

把 (4) 代回 (12)，得到准确余项
$$
 \mathcal S_m(A(s),B(s))
 =A(s)^{2m}\sum_{j\ge2m+1}u_j^{(m)}V(s)^j.
 \tag{14}
$$
$A$ 和 $V$ 都有一阶零，因此在原输出 $w=z^4$ 中也有
$$
 \boxed{\quad \operatorname{ord}_{w}\mathcal S_m(A(w),B(w))
                         \ge4m+1.\quad}
 \tag{15}
$$
$s(w)=w+O(w^2)$ 保持这个准确形式消失阶。
(15) 是真实原源的共同前缀，不是自由余项空间的维数结论。

## 4. 包括首分母之后的全部尾项

这里先付清从代数参数 $s$ 到原输出 $w$ 的运输。
R54 给 $W_x=z^2x_E=1+\sum_{j\ge1}A_jw^j$、
$v_p(A_j)\ge-j/R$。因此
$$
 W_x(\gamma T)\in1+\varpi^{p-1}T\mathcal O'[[T]],\qquad
 s(w)=wW_x(w)^{-2},\qquad s(\gamma T)/\gamma\in T+T^2\mathcal O'[[T]].
$$
将 R170/R177 的 $s$ 尺度沿这个整严格代换运输，得到
$$
 a(\gamma T)\in1+\lambda\mathcal O'[[T]],\quad
 b(\gamma T)\in\gamma T\mathcal O'[[T]].
$$
因 $a$ 是单位，代入 (2) 后
$$
 A(\gamma T),\ y(\gamma T)\in\gamma T\mathcal O'[[T]]
 \tag{16}
$$
成立。这里的 $\gamma T$ 是原 $w$ 参数，保留完整的原曲线。

对 (14) 中 $2m+1\le j<rm$，由 (10) 得
$$
 Rv_p(u_j^{(m)})+pj\ge p(2m+1).
 \tag{17}
$$
对全部 $j\ge rm$，由 (9) 得
$$
 \begin{aligned}
 Rv_p(u_j^{(m)})+pj
 &\ge r+(p-p^{1-q})j\\
 &\ge prm-R>p(2m+1).
 \end{aligned}
 \tag{18}
$$
最后的严格不等式是
$pm(r-2)>R+p$；由 $m\ge p$、$p\ge19$ 直接成立。
(18) 的右端随 $j$ 线性增长，还保证此代入的所有尾和收敛。
结合 (14)、(16)–(18)，得到
$$
 \boxed{\quad
 \mathcal S_m(A(\gamma T),B(\gamma T))
                  \in\gamma^{4m+1}\mathcal O'[[T]].
 \quad}
 \tag{19}
$$
这不是从整窗口向无限尾外推：首坏 $rm$ 以及其后全部系数
均由 (18) 单独支付。

例如 $q=1$ 时，R180/R183 的原尺度为
$\lambda^p\gamma^{2p}$。由 (19)，
$$
 \mathcal S_p(A(\gamma T),B(\gamma T))
       /(\lambda^p\gamma^{2p})\in p^7\mathcal O'[[T]],
 \tag{20}
$$
因为
$$
 \left\lfloor\frac{p(2p+1)-r}{R}\right\rfloor-1=7
 \qquad(p\ge19).
$$
这个七层精度和 (15) 同时发生在原次数 $2p$ 的同一个多项式上。

## 5. 原完整源格与十五层除幂

设 $E_D=\mathbb Z_p[A,B]_{\le D}$，沿原曲线取值。
R173 在输出参数 $v=b(w)=w+O(w^2)$ 中的逐系数完整基线为
$$
 e_p(k)=0\ (k<r),\qquad
 e_p(k)=n+\left\lfloor\frac{n-1}{p-1}\right\rfloor\ (k\ge r),
 \quad n=\lfloor k/r\rfloor.
 \tag{21}
$$
对全部 $k\ge0$，令 $\delta_k=pk/R-e_p(k)$，则
$0\le\delta_k<2$。定义整数
$$
 x_m=\frac{p(4m+1)}R,\qquad a_m=\lfloor x_m\rfloor-1.
 \tag{22}
$$
由上一节，$b(\gamma T)/\gamma\in T+T^2\mathcal O'[[T]]$，
其形式逆也整。因此 (16)、(19) 可完整地运到 $v=\gamma T$。
任意 $F\in E_D$ 在该尺度上的 Gauss 范数至多一，故
$$
 v_p([v^k]F)\ge-e_p(k)
$$
是 R173 的逐系数结论，而 (19) 另使 $\mathcal S_m^uF$ 满足
$$
 v_p([v^k]\mathcal S_m^uF)
 \ge\lceil u x_m-pk/R\rceil.
$$
系数属于 $\mathbb Q_p$，故此处可以取整数上整。因为
$$
 \lceil u x_m-\delta_k\rceil
 \ge\lfloor u x_m\rfloor-1
 \ge u(\lfloor x_m\rfloor-1)=u a_m\quad(u\ge1),
$$
准确得到
$$
 v_p([v^k](p^{-a_mu}\mathcal S_m^uF))\ge-e_p(k).
 \tag{23}
$$
这是同一个 $v$ 输出中全部系数的界；无需先把 $F$ 拆成自由商余列。
下面先在这个参数里对整个格求和，再限制到真实共同前缀。

取 $t\le\lfloor D/(2m)\rfloor$，令
$$
 \mathcal L_t=E_D+
 \sum_{u=1}^t p^{-a_mu}\mathcal S_m^uE_{D-2mu}.
 \tag{24}
$$
(23) 与原 $E_D$ 的逐系数界使整个 $\mathcal L_t$ 保留同一个
$e_p$ 基线。由于 $v=w+O(w^2)$，在任何真实前缀核上，其首个
非零系数与 $w$ 的首系数准确相同；所以所得完整 jet 界也是原
$w$ 平凡化的界。这里没有单独把未经消去前缀的各个 summand
套入 R173 的 $w$ 前缀结论。令
$F_u=\mathcal S_m^uE_{D-2mu}\subset E_D$。由于
$\mathcal S_m$ primitive，Gauss 范数乘法性给
$F_u\cap pE_D=pF_u$；次数相加还保证商仍在规定的有限次数内。
所以 $F_u$ 是饱和子格，且 $F_{u+1}\subset F_u$。
在这个有限饱和嵌套格上取适配整基，得到准确指数
$$
 \boxed{\quad
 \operatorname{length}_{\mathbb Z_p}(\mathcal L_t/E_D)
   =a_m\sum_{u=1}^t\binom{D-2mu+2}{2}.
 \quad}
 \tag{25}
$$
这一证明只用 primitive 性，不需要 (12) 关于 $B$ 首一。

R181 的完整旗标等式于是给：在同一全部真实跳跃上，
$E_D$ 的 log-jet 范数总和，等于 $\mathcal L_t$ 的相应总和
减去 (25) 乘 $\log p$。不同 $u$ 的共同早行和高尾始终保留。
由 (15)，第 $u$ 块只能从输出阶 $u(4m+1)$ 起改变前缀。

特别，$q=1$、$p\ge19$ 时
$$
 x_p=16+\frac{4p+16}{p^2-1},\qquad a_p=15.
 \tag{26}
$$
所以原源中可以准确使用
$p^{-15u}\mathcal S_p^uE_{D-2pu}$，其指数为
$15\sum_u\binom{D-2pu+2}{2}$。

## 6. 一个可变次数版本和累计范围

上述同一固定级数还给更多原源。对整数
$$
 2m\le d\le rm-r-1
$$
定义
$$
 \mathcal S_{m,d}
 =A^{d-2m}D_0^m-
       \sum_{j=0}^{d}u_j^{(m)}A^{d-j}D_0^j.
 \tag{27}
$$
它是 primitive、原次数准确 $d$ 的整多项式，并有
$$
 \operatorname{ord}_w\mathcal S_{m,d}\ge2d+1,\qquad
 \mathcal S_{m,d}(\gamma T)\in\gamma^{2d+1}\mathcal O'[[T]].
 \tag{28}
$$
证明与 (14)–(19) 相同；尾的分界现在是
$p(d+1)\le p(rm-r)<prm-R$。因此可取安全除层
$a_{m,d}=\lfloor p(2d+1)/R\rfloor-1$，并用 $d$ 替换 (24)–(25)
中的 $2m$。这些都是实际多项式，未新增任意横向列。

然而，无论使用 (12) 还是 (27)，都有
$$
 a_{m,d}<\frac{2pd}{R},
$$
因为 $p/R<1$。所以同时使用这些源的任意乘积，只要支付的
原总次数至多 $D$，其除层总和仍小于 $2pD/R$。由此构成的格
包含于 $p^{-\lfloor2pD/R\rfloor}E_D$，总指数至多
$$
 \binom{D+2}{2}\left\lfloor\frac{2pD}{R}\right\rfloor
 =O(D^3/p).
 \tag{29}
$$
这是这套明确除幂构造已支付的累计范围，并非原完整饱和
前缀的上界或下界。它尚未给 R159 所需的严格惰性主预算。
继续工作须实际使用双完整中央条件，或得到新的全深共同前缀收益。

## 7. 依赖和校准

- [R183：原 $p^q$ 幂的全部尺度和首坏窗口](R183-arbitrary-precision-original-theta-source.md)。
- [R184：固定原图、真实圆分范数和原次数](R184-cyclotomic-norm-source-and-exact-degree-support.md)。
- [R186：同一固定逆级数和全部第一范数块](R186-first-norm-block-and-integral-central-constraints.md)。
- [R181：原整格与全部真实跳跃的指数等式](R181-actual-monic-source-division-and-saturated-flag-gain.md)。
- [独立原有理级数校准脚本](../scripts/check-fixed-germ-power-sources.py)。

根端在 $p=19,31$ 直接由有理 $P,Q,t$ 构造 (12)，再用
$w=s\{\sum_{j\ge0}\binom{2j}{j}s^j/(4^j(4j+1))\}^4$ 的准确逆
换回原 $w$。首次非零项分别为 $77,125$，并核到 $83,131$ 阶，
全部满足 (19) 的尺度下界和十五层安全除法。

有限校准只检查准确恒等式、原次数、整系数和真实前缀；
全部尾项和任意 $q$ 的结论由上面的证明给出，不由扫描外推。
