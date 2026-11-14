# R200. 第一真实整化格的有限 graph–log Schur 核

日期：2026-11-12。**状态：以下有限对数 jet、完整联合核、正则化
Hasse 行及与原实际矩阵的等价均已证明。** 对数只使用到所需
$Z$ 次数 $q\le p-2$；没有在特征 $p$ 中宣称存在满足
$\mathcal E\eta=1$ 的完整形式函数。

## 1. 同一原格与完整 pair 矩阵

取 $p=4r-1\ge7$、$p\ne11$，令 $R=r(p-1)$。保留原平面
$$
 E_D=\mathbb Z_p[A,C]_{\le D},\qquad C=B-A,
 \quad A=w+\cdots,\quad C=v_0w^2+\cdots,\quad v_0=-22.
 \tag{1}
$$
真实整轴记作
$$
 A=\Gamma^{17}f(y),\qquad C=\Gamma^{17}c(y),\qquad
 f=y+\cdots,\quad c=v_0y^2+\cdots.
 \tag{2}
$$
设 $k=rq+s$，$0\le s<r$，
$\lceil r/2\rceil\le q\le p-2$。R196/R198 已识别同一个
连续归一矩阵的第一真实整化格为
$$
 \Lambda_1=E_D+p^{-1}H_{D,r},\qquad
 H_{D,r}=\operatorname{span}\{A^iC^j:i+j\le D,\ i+2j\ge r\}.
 \tag{3}
$$
在这个格的原对角基上，唯一写一个向量为
$$
 X=F+p^{-1}G,\qquad
 F\in\operatorname{span}\{A^iC^j:i+2j<r\},\quad
 G\in H_{D,r}.
 \tag{4}
$$
两部分的原次数都不超过 $D$。以下每条条件始终作用于同一个
$X$；并不把 $F,G$ 分别置入前缀核。

令 $\mathcal E=A\partial_A+C\partial_C$，
$\tau=pu_0\bmod p\ne0$，并记 $a=17\tau\in\mathbb F_p^\times$。
R199 的准确完整第一带式给，在 $n=rh+l<k$ 时
$$
 \boxed{\quad
 \overline J_{rh+l}(X)
 =\frac{a^h}{h!}[y^l](\mathcal E^h\overline F)(f,c)
  +\frac{a^{h-1}}{(h-1)!}[y^{l+r}]
                         (\mathcal E^{h-1}\overline G)(f,c),
 \quad}
 \tag{5}
$$
其中第二项在 $h=0$ 时定义为零，
$J_n=p^{\lfloor n/r\rfloor}[w^n]$。
所有 $h!$ 是单位。由于 $G$ 的原权至少 $r$，其整个轴值及所有
Euler 导数的轴值都被 $y^r$ 整除。式 (5) 因而等价于在每个
$h$ 块读取
$$
 (\mathcal E^h\overline F)(f,c)
       +\frac h a\,y^{-r}(\mathcal E^{h-1}\overline G)(f,c).
 \tag{6}
$$
这是 R199 保留全部角向尾的联合矩阵，不是关联对角块。

## 2. 只在所需有限 jet 中使用的径向对数

置
$$
 T(y)=c(y)/f(y)=v_0y+\cdots,\quad
 y_0(A)=f^{-1}(A),\quad
 \phi(A)=c(y_0(A)),\quad Z=C-\phi(A).
 \tag{7}
$$
因 $v_0$ 为单位，$T^{-1}$ 是严格比例单位的整形式逆。
在 $\mathbb Q_p((A))[[Z]]$ 中可以先于特征零定义
$$
 y(A,C)=T^{-1}(C/A),\qquad
 \eta(A,C)=\log\frac{A}{f(y(A,C))}.
 \tag{8}
$$
在 $Z=0$ 上，$y=y_0(A)$ 且对数的被积单位等于一。
因此 (8) 的对数按 $Z$ 展开，常数项为零。
原 Euler 算子准确满足
$$
          \mathcal E y=0,\qquad \mathcal E\eta=1
 \tag{9}
$$
作为特征零恒等式。

本篇只保留 $Z^0,\ldots,Z^q$。这些系数的对数分母只涉及
$1,\ldots,q$，所以全部是 $p$ 单位。故它们可以先在特征零
计算，再作为整 Laurent 系数约化模 $p$。
第 $h\le q$ 个 Euler 轴值只读取到 $Z^h$，不会使用未定义的
第 $p$ 阶对数系数。特别，(9) 只用于这些准确有限 jet，
不宣称它是一个完整特征 $p$ 形式函数的恒等式。

选取 $a$ 的任一整单位提升，定义这个有限 Laurent jet
$$
 \boxed{\qquad
       \mathcal H=F+\frac{\eta}{a\,y^r}G
                         \pmod{Z^{q+1}}.
 \qquad}
 \tag{10}
$$
单位提升的选择不影响所需模 $p$ 核。
在整 flowbox 中 $G$ 被 $y^r$ 整除，所以 (10) 作为所需径向
次数小于 $p$ 的 jet 是整的。这没有增加原源自由度：它仍是
同一个 (4) 的一个明确线性像。

由 (9)、$\eta|_{Z=0}=0$，在特征零先作乘法求导，得到
$$
 (\mathcal E^h\mathcal H)(A,0)
  =(\mathcal E^hF)(A,\phi(A))
    +\frac h{a\,y_0(A)^r}
               (\mathcal E^{h-1}G)(A,\phi(A)),
 \qquad 0\le h\le q.
 \tag{11}
$$
约化后，(11) 与 (6) 仅差严格输出参数 $A=f(y)$。
每个完整角向前缀及当前首剩余系数均在该换参下保持。

## 3. Laurent 阶界与不截零的完整核

在模 $p$ 的所需有限 Laurent jet 中写
$$
       \mathcal H(A,Z)=\sum_{j=0}^q H_j(A)Z^j.
 \tag{12}
$$
准确有
$$
                     H_j(A)\in A^{-2j}\mathbb F_p[[A]].
 \tag{13}
$$
证明可直接在 (8) 展开：$y-y_0$ 的第 $Z^j$ 系数有有限的
$A$ 极点，$(y-y_0)/y_0$ 的第 $j$ 项极点至多 $2j$。
因此 $\eta_j\in A^{-2j}\mathbb Z_p[[A]]$，
$[Z^j]y^{-r}\in A^{-r-2j}\mathbb Z_p[[A]]$。
原高权 $G$ 在 $C=Z+\phi(A)$ 后满足
$$
 [Z^i]G(A,Z+\phi(A))\in A^{\max(r-2i,0)}\mathbb Z_p[[A]],
$$
代入 (10) 即给 (13)。

仍置
$$
 \lambda(A)=\phi(A)-A\phi'(A)=-v_0A^2+\cdots.
 \tag{14}
$$
则 $\lambda/A^2$ 是单位，且
$\mathcal E=A\partial_A+(Z+\lambda)\partial_Z$。

**定理 1（第一整化格的完整 graph–log 核）。**
全部早期真实归一行 $\overline J_n(X)=0$、$n<k$，准确等价于
$$
 \boxed{\begin{aligned}
 \operatorname{ord}_A H_j&\ge r-2j&& (0\le j<q),\\
 \operatorname{ord}_A H_q&\ge s-2q.
 \end{aligned}}
 \tag{15}
$$
这里的右侧**不能**替换成其与零的最大值；$H_j$ 本来可能
有负 $A$ 次数。

**证明。** 由 (5)、(11) 及严格换参，早期行等价于
$(\mathcal E^h\mathcal H)(A,0)$ 在 $h<q$ 时被 $A^r$ 整除，
在 $h=q$ 时被 $A^s$ 整除。给 $(A,Z)$ 以权 $(1,2)$。
算子 $\mathcal E$ 保权，且第 $h$ 个新项准确是
$h!\lambda^hH_h$。已满足 (15) 的低 $j<h$ 项有权至少 $r$，
其全部贡献仍有 $A$ 阶至少 $r$。按 $h$ 归纳、利用
$h!$ 为单位及 $\operatorname{ord}\lambda=2$，便得 (15)
及其反方向。Laurent 下界 (13) 保证每步轴值仍是正则级数；
没有把一个负阶项单独当成真实非整输出。$\square$

## 4. 正则化 Hasse 行与逐块单位变换

定义正则级数
$$
       B_j(A)=\lambda(A)^jH_j(A)\in\mathbb F_p[[A]],\qquad
       b(A)=1-\frac{A\lambda'(A)}{\lambda(A)}\in\mathbb F_p[[A]].
 \tag{16}
$$
乘上 $\lambda^j$ 的 $A$ 阶是 $2j$；这个角向阶变化在下式中
完整保留。定理 1 等价于
$$
 \boxed{\qquad
 B_j\in A^r\mathbb F_p[[A]]\ (j<q),\qquad
 B_q\in A^s\mathbb F_p[[A]].
 \qquad}
 \tag{17}
$$
没有因此添加 $p$ 因子。

更明确地，将 $\mathcal E$ 作用后的系数同样正则化，得到准确
序列算子
$$
       (\mathcal D B)_j
          =A B_j'(A)+j\,b(A)B_j(A)+(j+1)B_{j+1}(A).
 \tag{18}
$$
于是 $(\mathcal E^h\mathcal H)(A,0)=(\mathcal D^hB)_0$。
第 $h$ 块的最高新行是 $h!B_h$；其余只含较早 $B_j$、
整级数乘法及 $A\,d/dA$。这些操作都保持完整的低角向前缀。
因此，在所需 $k$ 个有限行上，(17) 与 R199 的整个 pair 矩阵
之间是可逆的整单位行变换，而非只有核的一方向包含。

若 $X\in\Lambda_1$ 满足特征零中的真正完整前缀
$\operatorname{ord}_wX\ge k$，当前剩余行还准确满足
$$
          \boxed{\qquad
          p^q[w^{rq+s}]X\equiv a^q[A^s]B_q(X)\pmod p.
          \qquad}
 \tag{19}
$$
在第一整化格中，$B_q$ 不必被 $A^{2q}$ 整除。所以 R196 在原
整源上的 $s<2q$ 自动一层结论，不能未经计算再次使用于
$\Lambda_1$。

## 5. 最前两条真正耦合行

写 $F_j=[Z^j]F(A,Z+\phi)$、$G_j=[Z^j]G(A,Z+\phi)$，并置
$$
 \mu(A)=\frac1{a\,y_0(A)^r},\qquad
 \rho(A)=\frac{A y_0'(A)}{y_0(A)}\in1+A\mathbb F_p[[A]].
 \tag{20}
$$
由有限恒等式 $\mathcal E\eta=1$、$\mathcal Ey=0$，准确得到
$$
 \eta_1=\lambda^{-1},\qquad
 \eta_2=\frac{A\lambda'-\lambda}{2\lambda^3},\qquad
 [Z]\frac1{a\,y^r}=\frac{r\rho\mu}{\lambda}.
 \tag{21}
$$
故
$$
 \begin{aligned}
 H_0={}&F_0,\\
 H_1={}&F_1+\frac{\mu G_0}{\lambda},\\
 H_2={}&F_2+\frac{\mu G_1}{\lambda}
       +\mu\left\{\frac{A\lambda'-\lambda}{2\lambda^3}
                    +\frac{r\rho}{\lambda^2}\right\}G_0,
 \end{aligned}
 \tag{22}
$$
或者以正则行写成
$$
 \begin{aligned}
 B_0={}&F_0,\\
 B_1={}&\lambda F_1+\mu G_0,\\
 B_2={}&\lambda^2F_2+\lambda\mu G_1
       +\mu\left\{\frac{A\lambda'/\lambda-1}{2}+r\rho\right\}G_0.
 \end{aligned}
 \tag{23}
$$
每一行中的 $F$ 与 $G$ 可以真实相消；没有从其和为零推出两部分
分别为零。式 (23) 的每项整体正则，所显示的 $\mu$ 极点由原高
权条件支付。

## 6. 原列上的完全显式有限递推

为了直接计算 (17)，置
$$
 \Phi=\phi/A^2,\quad L=\lambda/A^2=-\Phi-A\Phi',\quad
 Y=y_0/A,
 \quad E_1=L^{-1},\quad M_0=(aY^r)^{-1}.
 \tag{24}
$$
这些是整单位级数。记
$\eta_j=A^{-2j}E_j$、$[Z^j](a y^r)^{-1}=A^{-r-2j}M_j$。
对所需 $j+1\le q$，准确递推为
$$
 \begin{aligned}
 E_{j+1}&=\frac{jE_j-AE_j'}{(j+1)L}&& (j\ge1),\\
 M_{j+1}&=\frac{(r+j)M_j-AM_j'}{(j+1)L}&& (j\ge0).
 \end{aligned}
 \tag{25}
$$
只除以单位 $j+1$，没有 $p!$ 损失。

对原列 $e_{m,c}=A^{m-c}C^c$，令 $\ell=m+c$。
若 $\ell<r$，其 $B_j$ 列准确为
$$
       \binom cj A^\ell L^j\Phi^{c-j},
 \tag{26}
$$
$c<j$ 时为零。若 $\ell\ge r$，使用格中的列 $p^{-1}e_{m,c}$，
其 $B_j$ 列准确为
$$
 \boxed{\quad
 A^{\ell-r}L^j
 \sum_{i=0}^{\min(c,j-1)}\binom ci\Phi^{c-i}
              \sum_{b=1}^{j-i} E_bM_{j-i-b}.
 \quad}
 \tag{27}
$$
$j=0$ 时内和为空。式 (26)–(27) 是同一原次数格的全部列；
当 $\ell\ge2r$，其角向次数小于 $r$ 的整列仍为零。

计算这些有限行只需 $\Phi,L,Y$ 至 $A^{r-1}$，也就是 R199
已经支付的 $f_1,\ldots,f_r$ 与 $c_2,\ldots,c_{r+1}$。
没有为了写 (8) 而免费引入完整高阶轴数据。

### 6.1. 同一原权 strip 除幂格的有限对数核

R199 的原对角格还允许一个不增加证明深度的推广。仍在同一
原次数空间中，定义
$$
 \mathcal M_D
   =\bigoplus_{i+j\le D}
       \mathbb Z_p\,p^{-\lfloor(i+2j)/r\rfloor}A^iC^j.
 \tag{28}
$$
它不是 R198 的一般饱和格 $\Lambda_t$。每个元素按原权 strip
唯一写成
$$
 X=\sum_{t\ge0}p^{-t}G_t,\qquad
 G_t\in\operatorname{span}\{A^iC^j:
                   i+j\le D,\ rt\le i+2j<r(t+1)\}.
 \tag{29}
$$
这里只需 $0\le q\le p-2$，不再需要第一整化格的
$q\ge\lceil r/2\rceil$。在所需 $Z^q$ jet 中取
$$
 \boxed{\qquad
 \mathcal H_{\mathcal M}(X)
     =\sum_{0\le t\le q}
          \left(\frac{\eta}{a\,y^r}\right)^tG_t
                          \pmod{Z^{q+1}}.
 \qquad}
 \tag{30}
$$
式中**没有** $t!$ 分母。$\eta$ 在 $Z=0$ 为零，故 $t>q$
不会进入这个有限 jet；R199 的实际行在 $h<t$ 时也准确为零。

具体地，先在特征零使用 (9)，得到
$$
 \left.\mathcal E^h\!
      \left(\frac{\eta^tG_t}{a^t y^{rt}}\right)\right|_{Z=0}
   =\begin{cases}
    \displaystyle
       \frac{h!}{(h-t)!a^t y_0^{rt}}
                 (\mathcal E^{h-t}G_t)(A,\phi),&t\le h,\\
    0,&t>h.
   \end{cases}
 \tag{31}
$$
乘以 $a^h/h!$、改回 $A=f(y)$ 并取 $[y^l]$，
恰是 R199 (13) 在同一向量 (29) 上的完整求和。
所用阶乘的指标均小于 $p$。

因为 $G_t$ 的原权至少为 $rt$，其第 $Z^i$ 系数有阶至少
$\max(rt-2i,0)$；而
$[Z^j](\eta^t y^{-rt})$ 的阶至少 $-rt-2j$。
于是
$$
 [Z^j]\mathcal H_{\mathcal M}(X)
                   \in A^{-2j}\mathbb F_p[[A]].
 \tag{32}
$$
所以定理 1、正则化 (16)–(18) 及当前行公式 (19) 原样适用，
只需把 $\mathcal H$ 替换为 (30)。全部负阈值仍是
$r-2j$ 和 $s-2q$，不截为零。

这个推广保留全部原 strip 的耦合。它没有把每个 $G_t$ 分别
置于前缀核，也没有把 $\mathcal M_D$ 识别为任意后续整化层。
第一整化格 (4) 则是同一有限乘法求导计算的两组版本：
$G_0=F$、$G_1=G$，第二组只要求原权至少 $r$，不要求小于
$2r$。因而 (10) 与 (30) 的区别是实际源格的除幂分配，
不是对数 jet 或输出矩阵的改变。

## 7. 同一完整矩阵的 row-space 证书

[短脚本](../scripts/check-first-saturation-graph-log.py) 仅复用
R198/R199 的 $p=23,D=7,k=30$。一边从原 $P,Q,W$ 和真正 $w$
反演构造 $J|_{\Lambda_1}\bmod23$；另一边只从已付短初段构造
(24)–(27)，读取全部 $B_j$ 前缀。两边的完整行空间相同，秩均为
三十，核维数均为六。同一脚本还在完全相同的实例上，按 (30)
作有限 $Z$ 卷积，核对原权 strip 格 $\mathcal M_D$ 的全部行空间；
其两种构造也准确一致，秩三十、核维六。第二个比较同时校准了
$t=2$ 项没有 $t!$ 的规范，没有增加素数或次数样本。

这个比较检验同一个原格的实际联合核；不会从一个关联对角块的
秩代替完整行空间。下一次 saturation 仍按 R198 的准确原像定义。
本文给出计算其核的有限 graph–log 形式，未证明这些核具有随
$D,k,p$ 统一的额外整除或严格全局范数收益。

依赖：

- [R196：原正则源的连续 Euler–Padé 核](R196-continuous-first-band-euler-pade-kernel.md)。
- [R198：真实共同像及准确 jump 旗标](R198-joint-image-saturation-and-complete-prefix-smith.md)。
- [R199：完整准确指数与全部 pair 像](R199-exact-first-band-exponential-and-complete-divided-image.md)。
