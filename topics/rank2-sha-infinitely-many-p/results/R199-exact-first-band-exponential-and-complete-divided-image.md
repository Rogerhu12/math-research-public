# R199. 完整第一带的准确共同指数与原除幂格的全部模 p 像

日期：2026-11-12。**状态：准确第一带公式、完整除幂像矩阵及其
轴系数读取范围均已证明。** 本篇把此前的关联缺阶块放回同一个
完整连续矩阵；没有将它的列独立前缀化，也没有把这个明确子格
称为所有后续层的完全饱和格。

## 1. 原源、整轴与两个不同的阶

取惰性素数 $p=4r-1\ge7$，排除 $p=11$，置 $R=r(p-1)$。
仍用原源
$$
 E_D=\mathbb Z_p[A,C]_{\le D},\qquad C=B-A,\qquad
 A=w+\cdots,\quad C=v_0w^2+\cdots,\quad v_0=-22.
 \tag{1}
$$
原整基为
$$
 e_{m,c}=A^{m-c}C^c,\qquad 0\le c\le m\le D,\qquad
 \ell=m+c .
 \tag{2}
$$
$m$ 是原多项式次数，$\ell$ 是其整轴最低角向阶；二者不能
互换。其底层 $a,b$ 齐次次数是 $17m$。

R179、R185 的同一整截面给
$$
 A=\Gamma^{17}f(y),\qquad C=\Gamma^{17}c(y),\qquad y=\zeta,
 \quad f=y+\cdots,\quad c=v_0y^2+\cdots.
 \tag{3}
$$
其中 $f,c\in\mathbb Z_p[[y]]$；它们是原函数在 $U=0$ 处的
轴级数。写
$$
 g_{m,c}(y)=f(y)^{m-c}c(y)^c
                \in y^\ell\mathbb Z_p[[y]],\qquad
 \tau_p=pu_0\in\mathbb Z_p^\times,\quad \tau=\tau_p\bmod p.
 \tag{4}
$$
为避免与列下标混淆，后文使用 $g_e$ 表示 (4)。
常数列单独取 $g_{0,0}=1$。

## 2. 完整第一带的准确指数分解

**定理 1。** 在同一真实 $w$ 参数下，准确有
$$
 \boxed{\quad
 A(w)\equiv e^{17u_0w^r}f(w),\qquad
 C(w)\equiv e^{17u_0w^r}c(w)\pmod{w^{R+1}\mathbb Q_p[[w]]}.
 \quad}
 \tag{5}
$$
因此对任意原多项式 $P\in E_D$，设
$\mathcal E=A\partial_A+C\partial_C$，则对 $n=rh+j\le R$、
$0\le j<r$ 有
$$
 \boxed{\quad
 p^h[w^{rh+j}]P(A(w),C(w))
 =\sum_{i=0}^h
   p^{h-i}\frac{(17\tau_p)^i}{i!}
   [y^{j+r(h-i)}](\mathcal E^iP)(f(y),c(y)).
 \quad}
 \tag{6}
$$
在这个范围 $h\le p-1$，所以所有 $i!$ 都是 $p$ 单位。
式 (6) 是特征零中的准确等式，未丢掉任何 $p$ 进高精度尾。
$i=0$ 时 $\mathcal E^0$ 是恒等算子。

**证明。** R185 (22) 的完整 Teich 平均是
$$
 \begin{aligned}
 U(\eta,w)&=\sum_{j\ge0}\xi_{rj}u^{(j)}(\eta)w^{rj},\\
 V(\eta,w)&=\sum_{j\ge0}b_{1+rj}u^{(j+1)}(\eta)w^{1+rj},
 \qquad
 u(\eta)=\sum_{n\equiv1\ (p-1)}\frac{\eta^n}{n!}.
 \end{aligned}
 \tag{7}
$$
给 $\eta$ 权 $r$、$w$ 权一。第一行的非零项满足
$\eta$ 次数加 $j$ 同余于 $1\bmod p-1$，第二行除以 $w$
后同余于零。故
$$
 U=\eta+u_0w^r+O_{\rm wt}(pr),\qquad
 V=w+O_{\rm wt}(R+1).
 \tag{8}
$$
同一个 $U=0$ 截面有
$\eta_{\rm sec}(w)=-u_0w^r+O(w^{pr})$。由
$\Gamma=\exp(\eta-\eta_{\rm sec}(w))$，
$$
 \log\Gamma=U+O_{\rm wt}(pr),\qquad
 \zeta-V=O_{\rm wt}(R+1).
 \tag{9}
$$
第二式使用 $\zeta$ 只依赖 $s=b/a$，以及
$\zeta(\gamma(w))=w+O(w^{R+1})$。
加权首部 $(\eta,w)\mapsto(\eta+u_0w^r,w)$ 可逆，故这些
准确形式阶在 $(U,V)$ 中保持。这个论证在 $\mathbb Q_p$ 上
进行；并没有把 $u_0$ 或未显示的高阶系数称为整。

对正齐次 $H=\Gamma^d g_H(\zeta)$、$g_H(0)=0$，(9) 给
$$
 H(U,V)-e^{dU}g_H(V)\in O_{\rm wt}(R+1),
 \qquad
 [U^iV^j]H=\frac{d^i}{i!}[y^j]g_H
                       \quad(ri+j\le R).
 \tag{10}
$$
再沿原曲线代入
$U(w)=u_0w^r+O(w^{pr})$、
$V(w)=w+O(w^{R+1})$，得到 (5)。
多项式代入保留模 $w^{R+1}$ 的等式；将 $P$ 按原次数 $m$
分解，并用 $\mathcal E^iP_m=m^iP_m$，即得 (6)。
常数列直接满足相同公式。$\square$

此证明没有使用 $p\nmid m$。R185 关于完整 Stokes 权赋值的
单位假设，不是本篇有限第一带形式恒等式的假设。
端点 $n=R$ 只有 $j=0$，也由 (10) 保留；$n>R$ 的首 carry
不在这里被删去。

## 3. 所有原对角除幂列的完整像

对 (2) 写
$$
 \ell=rt+j_0,\qquad t=\lfloor\ell/r\rfloor,\qquad
                         0\le j_0<r,
 \tag{11}
$$
并仍在同一原有理次数空间中取
$$
 \mathcal M_D=\bigoplus_{m,c}\mathbb Z_p\,p^{-t}e_{m,c}.
 \tag{12}
$$
这是 R194 的实际对角除幂格。以下保持全部连续目标行
$J_n=p^{\lfloor n/r\rfloor}[w^n]$，其中 $0\le n<k\le R+1$。

**定理 2。** $J(\mathcal M_D)\subset\mathbb Z_p^k$。在其所示
原基上，全部模 $p$ 矩阵条目准确为
$$
 \boxed{
 \overline J_{rh+j}(p^{-t}e_{m,c})=
 \begin{cases}
 \displaystyle
 \frac{(17\tau)^{h-t}}{(h-t)!}\,
       m^{h-t}\,[y^{rt+j}]\overline g_e(y),&h\ge t,\\[6pt]
 0,&h<t .
 \end{cases}}
 \tag{13}
$$
$m^0=1$ 的约定包含常数列；$h-t>0,m=0$ 时该因子为零。
式 (13) 保留了 $j>j_0$ 的全部角向尾，不只给 $j=j_0$ 的
关联对角块。

**证明。** 在 (6) 中，若 $h-i<t$，则
$j+r(h-i)<rt\le\ell$，对应的 $g_e$ 系数准确为零。
剩下的每个 summand 含 $p^{h-i}$，因而可整体除以 $p^t$。
这先证明整性。取模 $p$ 时仅 $i=h-t$ 可能保留，给出 (13)；
$h<t$ 时所有 summand 都为零。$\square$

因 $\operatorname{ord}g_e=rt+j_0$，$j<j_0$ 的条目为零；
$j=j_0$ 的系数是 $v_0^c$。所以每个关联 $j_0$ 块确实是
R194 的缺阶 Hermite 块，明确列单位为
$v_0^c(17\tau)^{-t}$。同时 (13) 给出这些块之间原先不能删去
的实际尾系数。

更精确地，把第 $h$ 行除去单位 $(17\tau)^h$，再把第
$(m,c)$ 列乘 $(17\tau)^t$，关联块成为
$v_0^c m^{h-t}/(h-t)!$。这里是同一完整矩阵上的实际单位
行、列操作；它不把不同余类的非对角项置零。

## 4. 真实第一整化格的共同第二层矩阵

设 $k=rq+s$，$0\le s<r$、
$\lceil r/2\rceil\le q\le p-2$。R196 已证明真正第一层恰为
$$
 \Lambda_1=E_D+p^{-1}H_{D,r},\qquad
 H_{D,r}=\operatorname{span}_{\mathbb Z_p}\{e_{m,c}:\ell\ge r\}.
 \tag{14}
$$
取基时，$\ell<r$ 的列不除，$\ell\ge r$ 的列只除一次。
对这个同一个完整源，准确有
$$
 \boxed{
 \overline J_{rh+j}(e_{m,c})=
  \frac{(17\tau)^h m^h}{h!}[y^j]\overline g_e
                      \quad(\ell<r),}
 \tag{15}
$$
$$
 \boxed{
 \overline J_{rh+j}(p^{-1}e_{m,c})=
 \begin{cases}
 \displaystyle
 \frac{(17\tau)^{h-1}m^{h-1}}{(h-1)!}
                   [y^{j+r}]\overline g_e,&h\ge1,\\[6pt]
 0,&h=0
 \end{cases}
                      \quad(\ell\ge r).}
 \tag{16}
$$
若 $\ell\ge2r$，(16) 整列为零；这些列在第二层仍可继续
整化，但它们不必穷尽第二层的核。

式 (15)–(16) 由 (6) 同时保留其第一个未消失 summand 得到。
它们的目标行完全相同，因此第二层所需的是这个**联合矩阵**
的核。低权列与除幂高权列可以在同一行中相消；不能分别计算
它们的核再拼接。

## 5. 全部角向输入只到 f_r 与 c_(r+1)

写
$$
 f=yF,\qquad c=v_0y^2G,\qquad F(0)=G(0)=1.
 \tag{17}
$$
对 (13) 中非零的条目，
$$
 [y^{rt+j}]g_e
   =v_0^c[y^{j-j_0}]F^{m-c}G^c,\qquad
                  0\le j-j_0\le r-1.
 \tag{18}
$$
故整个 $\mathcal M_D$ 的第一带模 $p$ 像，不论 $D$ 多大，
都只读取
$$
 \boxed{\qquad
 f_1,\ldots,f_r,\qquad c_2,\ldots,c_{r+1}\pmod p.
 \qquad}
 \tag{19}
$$
而 (5) 和 $f(0)=c(0)=c'(0)=0$ 还准确给
$$
 f_j=[w^j]A\ (1\le j\le r),\qquad
 c_j=[w^j]C\ (2\le j\le r+1).
 \tag{20}
$$
所以 (19) 本身只需原 $w$ 级数的这些短初段，既不需要高阶
Cartan 反演，也不需要用未知中央泛函来生成输入。
对于 (15)–(16) 也成立：高权列只读
$j+r-\ell\le r-1$，低权列的范围更小。
这里并没有把这些轴系数当成可自由选择的实际源。

特别，原第二条中央轴向量 $(f_{2r},c_{2r})$ 不进入任何上述
条目；$r\ge2$ 使 $r+1<2r$（$r=2$ 时仍为 $3<4$）。
第一中央对 $(f_r,c_r)$ 则不是完全不可见，但它的系数依赖
仅能出现在 $j=r-2,r-1$ 这最后两个角向行：
$f_r$ 在 $F$ 中的次数为 $r-1$，$c_r$ 在 $G$ 中的次数为
$r-2$，而 (18) 只读 $j-j_0$。

因此 R195 的两个独立中央方向，不能被直接等同于
$J(\Lambda_1)\bmod p$ 上两组新的可读独立行。第二中央方向
需要下一精度或后续实际 Schur 消元；R185 的
$f_r-b_{17}^{-1}f_{2r}\equiv0\bmod p^2$ 等条件仍保留在那里。
本结论只定位准确输入，不否定这些高精度条件可能产生的收益。

## 6. 同一已用矩阵的有限校准

[短证书](../scripts/check-complete-divided-first-band-image.py) 只用
R198 已有的 $p=23,D=7,k=30$。它从原 $P,Q,W$ 和真正的
$w=s\mathcal L(s)^4$ 反演取得原连续矩阵；另从至多 $r+1$
阶的原级数按 (20) 构造 (19)，然后逐项核对：

- 原 $\Lambda_1$ 的全部 $30\times36$ 条目与 (15)–(16) 一致；
- 原 $\mathcal M_D$ 的全部条目与 (13) 一致，包含跨余类尾；
- 只用 (19) 的短轴矩阵，得到同一个实际秩 $30$。

这个检查不增加新的素数样本，也不以有限矩阵代替定理 1–2。
任意层的准确格仍按 R198 的
$\Lambda_{t+1}=p^{-1}\Lambda_t\cap J^{-1}(\mathbb Z_p^k)$ 定义；
只有第一层已由 (14) 完全识别。

依赖：

- [R185 的准确 Teich 支撑与整轴](R185-integral-axis-stokes-functional-and-complete-central-tests.md)，(22)–(24)。
- [R194 的原除幂格与缺阶关联块](R194-sparse-jet-smith-and-actual-lacunary-hermite-blocks.md)。
- [R196 的完整第一层核](R196-continuous-first-band-euler-pade-kernel.md)。
- [R198 的真实共同像、核与累计旗标](R198-joint-image-saturation-and-complete-prefix-smith.md)。

本篇尚未给出无穷多个素数的中央非零，也未证明严格的全次数
惰性 jet 预算。
