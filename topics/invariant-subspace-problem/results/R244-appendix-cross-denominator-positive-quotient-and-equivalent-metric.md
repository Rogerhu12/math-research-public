# R244 后续附录：交叉分母的正向量与有界等价正化

日期：2026-11-13（UTC）。作者：normal_resume_1cf；Astra-ISP-1cf8c51d 已核查全部链映射、Bézout 下界、正度量与拓扑直和。

状态：已证明，完整的有界链计算。对真秩二正见证及任意两行广义预解数据，把原向量 (Cf_1,Cf_2) 放入一个新的实际二重放大旗子商；原预解中间商有界嵌入该新商，且其先前的双向量配对由一个明确的有界正可逆算子正化。交叉分母不要求单射，因此新商不被称为比例算子的图。没有证明共同最小图等于最大交域，没有把商上的正向量泛函变成原 H 上的秩一见证。

## 0. 与既有结论的区别

[R228A 正见证与零子商](R228-appendix-minimal-witnesses-and-positive-quotient-orbits.md) §§1–2 已从任何有限秩分离泛函构造正见证，并从正见证构造循环的 S 零子商。本文不重复这种一般正化。

R244 的秩二有界链附录已在原分母 (R_1,R_2) 上构造非零商 Q，并得到 q=P_Qg、z_Q=P_Qz 以及 <q,z_Q>=Tr rho>0；只有 D_1=D_2=I 的特殊参数曾直接给 (Cf_1,Cf_2)∈Q。

本稿处理一般 D_i：给出完全有界的新链、原 Q 到新链的闭像嵌入、参数决定且与见证向量无关的正可逆 G，以及精确等式 Gq=z_Q。单凭一对向量的正配对也能抽象选某个正度量；本稿多出的内容是实际链映射、下界及其两分母/两分子直和分解。

以下内积对第一变量线性。公式中的 Tr rho、<x,y> 分别统一写成 $\tau$、$\langle x,y\rangle$。

## 1. 原参数的全部有界恒等式

记 $\mathfrak C=A'$，每个 $F\in\mathfrak C$ 都满足 $F^*=CFC$，且 $\mathfrak C$ 交换。设
$
 \rho=f_1\otimes f_1+f_2\otimes f_2,\qquad
 \tau=\|f_1\|^2+\|f_2\|^2>0,
 \qquad \phi(F)=\sum_i\langle Ff_i,f_i\rangle,
$
且实际慢算子 S 在全 H 单射，满足 $\phi(S\mathfrak C)=0$。
原来只写 $\phi(S\mathcal A)=0$ 时，可用 R88 的有界强多项式逼近及有限向量泛函的强连续性延到这里。

令 $M_i=X_{Cf_i}$ 为原最小闭乘子，取任意广义预解数据
$
 L_i=M_iU_i+F_i,\quad U_i\in\mathfrak C^\times,\quad
 \lambda_i\in\rho(L_i),
$
$
 R_i=(L_i-\lambda_iI)^{-1},\quad
 B_i=F_i-\lambda_iI,\quad D_i=M_iR_i\in\mathfrak C.
$
为使链计算短而不混淆两类变量，记
$
 a=R_1,\quad b=R_2,\quad c=D_1,\quad d=D_2,
 \qquad u=U_1,\ v=B_1,\ s=U_2,\ t=B_2.
$
全部都是有界交换子，且
$
 uc+va=I,\qquad sd+tb=I. \tag{1.1}
$
记 $x_1=Cf_1,\ x_2=Cf_2$。真实域交换给
$
 ax_1=c1,\qquad bx_2=d1. \tag{1.2}
$
例如 $aM_1 1=M_1a1=c1$，其中 $1\in\operatorname{Dom}M_1$，有界 a 保持该域并与 M_1 交换。

令
$
 g_1=ux_1+v1,\qquad g_2=sx_2+t1.
$
它们正是 $(L_i-\lambda_iI)1$，并且 (1.1)--(1.2) 逐项给
$
 ag_1=bg_2=1,\qquad cg_1=x_1,\quad dg_2=x_2. \tag{1.3}
$

真正态还给
$
 h=bcf_1+adf_2=0. \tag{1.4}
$
此处重述支付域的理由：$abH\subseteq\operatorname{Dom}M_1\cap\operatorname{Dom}M_2$，所以
$h=M_1abf_1+M_2abf_2$ 是实际 H 向量。对任意 $F\in\mathfrak C$，利用最小乘子的双线性对称性、$M_i1=Cf_i$ 及域交换，
$
 B(FSh,1)=\sum_i\langle FSabf_i,f_i\rangle
          =\phi(SabF)=0.
$
因为 $1$ 对 A 循环，$B(FSh,1)=B(Sh,F1)$ 对所有多项式 F 为零迫 $Sh=0$；全空间 S 单射给 (1.4)。没有取消未知定义域，也没有用单个因子理想湮灭代替这个向量等式。

## 2. 新交叉分母与准确正向量

对任意 $p,q\in\mathfrak C$ 定义
$
 d_0^{p,q}w=(qw,pw),\qquad d_1^{p,q}(y_1,y_2)=py_1-qy_2,
$
$
 N(p,q)=\overline{\operatorname{Ran}d_0^{p,q}},\quad
 K(p,q)=\ker d_1^{p,q},\quad Q(p,q)=K(p,q)\ominus N(p,q).
$
它们都是实际 $A^{(2)}$ 的闭旗。F 的商作用记为
$
 \pi_{p,q}(F)=P_{Q(p,q)}F^{(2)}|_{Q(p,q)}.
$
这是有界代数表示，$\|\pi_{p,q}(F)\|\le\|F\|$。

原商为 $Q=Q(a,b)$。新取
$
 a'=ad,\qquad b'=bc,\qquad Q'=Q(a',b').
$
a'、b' 可能非单射；以下证明不要求它们有单值闭逆。

**定理 2.1。** 原正向量
$
 x=(Cf_1,Cf_2)=(x_1,x_2)
$
准确属于 $Q'$，且对全部 $F\in\mathfrak C$，
$
 \boxed{\phi(F)=\langle\pi_{a',b'}(F)x,x\rangle,\qquad
        \|x\|^2=\tau.} \tag{2.1}
$

证明必须核两个不同方向。由 (1.2)，
$
 a'x_1-b'x_2=ad x_1-bc x_2=dc1-cd1=0.
$
因此 x 属于 K(a',b')。另一方面，原 C 对称性及 (1.4) 给
$
 (d_0^{a',b'})^*x=(bc)^*Cf_1+(ad)^*Cf_2
                 =C(bcf_1+adf_2)=0.
$
所以 x 与 N(a',b') 正交，确有 $x\in Q'$。

最后，R228 §1 的 C 对称恒等式直接给
$
 \sum_i\langle FCf_i,Cf_i\rangle
 =\sum_i\langle Ff_i,f_i\rangle.
$
压缩不改变与 x 的配对，得到 (2.1)。证毕。

因此新商非零。这里没有声称 $S_{Q'}=0$；(2.1) 只给这个正向量对 $S\mathfrak C$ 的矩为零。R228A 的进一步循环零子商构造当然可以另外应用。

原有界链引理不要求分母单射，故同一无权反线性等距
$J(y_1,y_2)=(Cy_2,-Cy_1)$ 保持 Q'，且 $J^2=-I$、$J\pi_{a',b'}(F)=\pi_{a',b'}(F)^*J$。实际多项式强单位也照常下降。于是 Q' 无限维，且其 A 商算子没有循环向量；这是既有一般引理在新链上的应用，不是把 Q' 认作原 H。

## 3. 原商的有界嵌入及明确下界

置
$
 \Delta=\operatorname{diag}(c,d),\qquad
 \nabla=\operatorname{diag}(d,c).
$
以下四个有界等式支付全部链与边界：
$
 \Delta d_0^{a,b}=d_0^{a',b'},\qquad
 d_1^{a',b'}\Delta=(cd)d_1^{a,b},
$
$
 \nabla d_0^{a',b'}=d_0^{a,b}(cd),\qquad
 d_1^{a,b}\nabla=d_1^{a',b'}. \tag{3.1}
$
所以它们诱导有界商映射
$
 \mathcal L=P_{Q'}\Delta|_Q:Q\longrightarrow Q',\qquad
 \mathcal V=P_Q\nabla|_{Q'}:Q'\longrightarrow Q,
$
并与全部 F 的商作用交织。

对任意 p,q，事实上
$
 \pi_{p,q}(p)=\pi_{p,q}(q)=0. \tag{3.2}
$
若 $y\in K(p,q)$，则
$p^{(2)}y=(qy_2,py_2)=d_0^{p,q}y_2$，
$q^{(2)}y=(qy_1,py_1)=d_0^{p,q}y_1$，故 (3.2) 无需任何闭值域或单射假设。

由 (3.1)，在复合中插入的中间正交投影只删去边界，其像仍是另一链的边界。因此
$
 \mathcal V\mathcal L=\pi_{a,b}(cd). \tag{3.3}
$
而 (1.1)、(3.2) 给
$
 \pi_{a,b}(u)\pi_{a,b}(c)=I,\qquad
 \pi_{a,b}(s)\pi_{a,b}(d)=I.
$
交换性使
$
 \pi_{a,b}(us)\mathcal V\mathcal L=I_Q. \tag{3.4}
$
所以 $\mathcal L$ 单射、有闭像，并有一个实际有界左逆。

令 $m=\max(\|c\|,\|d\|)$。这里 Q 非零，故 m>0。由
$\|\Delta\|=\|\nabla\|=m$ 得
$
 \boxed{\frac{\|y\|}{\|us\|m}\le\|\mathcal Ly\|\le m\|y\|
 \qquad(y\in Q).} \tag{3.5}
$
这不是由普通环境稠密性推出的图逆；下界来自两个精确 Bézout 等式。

## 4. 同一个正可逆度量准确送 q 到 z_Q

沿用原商的向量
$
 g=(g_1,g_2),\qquad
 z=(c^*Cf_1,d^*Cf_2)=\Delta^*x,\qquad
 q=P_Qg,\quad z_Q=P_Qz.
$
(1.3) 给 g 属于 K(a,b) 及 $\Delta g=x$；(1.4) 给 z 与 N(a,b) 正交。因此 g-q 属于 N(a,b)，(3.1) 与定理 2.1 给
$
 \mathcal Lq=P_{Q'}\Delta g=x. \tag{4.1}
$
置
$
 G=\mathcal L^*\mathcal L.
$
由 (3.5)，G 是 Q 上有界正可逆算子，且
$
 \boxed{(\|us\|m)^{-2}I_Q\le G\le m^2I_Q.} \tag{4.2}
$
更准确，x 已在 Q'，故
$
 \boxed{Gq=\mathcal L^*x=P_Q\Delta^*x=z_Q.} \tag{4.3}
$
结合交织关系及 (2.1)，对全部 $F\in\mathfrak C$，
$
 \boxed{\phi(F)
   =\langle\mathcal L\pi_{a,b}(F)q,\mathcal Lq\rangle
   =\langle\pi_{a,b}(F)q,Gq\rangle.} \tag{4.4}
$

特别，G 由有界参数及其闭旗决定，并不以此处某一个 g 或 x 为定义。等价 Hilbert 内积
$\langle y,w\rangle_G=\langle y,Gw\rangle$
使原泛函成为正向量泛函。若要使用原 Hilbert 内积，令
$
 \widetilde\pi(F)=G^{1/2}\pi_{a,b}(F)G^{-1/2},\qquad
 \xi=G^{1/2}q.
$
则
$
 \phi(F)=\langle\widetilde\pi(F)\xi,\xi\rangle,\qquad
 \|\xi\|^2=\tau,\qquad
 \|\widetilde\pi(F)\|\le\|us\|m^2\|F\|. \tag{4.5}
$
这不声称 $\phi$ 在未改变内积的原 $\pi_{a,b}$ 上已由某个正密度实现，更不产生原 H 上的正秩一密度。

## 5. 新商的精确两分母/两分子直和

还可以说明新商为何没有偷偷丢失原商。令
$
 Q_D=Q(c,d),\qquad
 W(y_1,y_2)=(by_2,ay_1).
$
W 同时从 K(c,d) 映入 K(a',b')、从 K(a',b') 映入 K(c,d)，并把相应边界送到边界。直接核验：
$
 d_1^{a',b'}W=-ab\,d_1^{c,d},\quad
 d_1^{c,d}W=-d_1^{a',b'},
$
$
 Wd_0^{c,d}=d_0^{a',b'},\quad
 Wd_0^{a',b'}=d_0^{c,d}(ab).
$
故有
$
 \mathcal L_D=P_{Q'}W|_{Q_D},\qquad
 \mathcal V_D=P_{Q_D}W|_{Q'}.
$
压缩计算给
$
 \mathcal V_D\mathcal L_D=\pi_{c,d}(ab),\quad
 \mathcal L_D\mathcal V_D=\pi_{a',b'}(ab),\quad
 \mathcal L\mathcal V=\pi_{a',b'}(cd). \tag{5.1}
$
在 Q_D 上 c,d 都作用为零，所以 (1.1) 给
$\pi_{c,d}(vt)\pi_{c,d}(ab)=I_{Q_D}$。
因此 $\mathcal L_D$ 也有有界左逆，像闭。

两个交叉复合为零：
$
 \mathcal V\mathcal L_D=0,\qquad
 \mathcal V_D\mathcal L=0. \tag{5.2}
$
例如若 $cy_1=dy_2=w$，则
$\nabla W y=(bd y_2,ac y_1)=(bw,aw)$
为原 (a,b) 链边界。若 $ay_1=by_2=w$，则
$W\Delta y=(bd y_2,ac y_1)=(dw,cw)$
为 (c,d) 链边界。商投影只删去被另一映射送入边界的项，故两式完整成立。

将两个 Bézout 式相乘，再在 Q' 使用 $\pi_{a',b'}(ad)=\pi_{a',b'}(bc)=0$，得到
$
 I_{Q'}=\pi_{a',b'}(us)\mathcal L\mathcal V
        +\pi_{a',b'}(vt)\mathcal L_D\mathcal V_D. \tag{5.3}
$
(3.4)、(5.1)--(5.2) 表明右侧两项为互补有界幂等算子。因此
$
 \boxed{Q'=\operatorname{Ran}\mathcal L\ \dotplus\
              \operatorname{Ran}\mathcal L_D
        \ \simeq\ Q(a,b)\ \dotplus\ Q(c,d).} \tag{5.4}
$
这是有界拓扑直和，不声称正交或酉。它对任何满足 (1.1) 的有界交换参数成立。

真见证向量 x 由 (4.1) 属于第一分量；它不会被新增的分子缺陷替代。也可直接看
$
 (ab)^{(2)}x=(bc1,ad1)=d_0^{a',b'}1,
$
所以 $\pi_{a',b'}(ab)x=0$，(5.3) 的第二幂等算子消去 x。

## 6. 尚未跨过的边界

本稿的正性是原正矩在一个具体有界链中的准确实现。新的 Q' 仍是 H 的二重放大旗子商；其交叉分母未必单射，不能把它称为原最小闭乘子的比例图。G 改变 Q 的内积，未证明 G 与全部商算子交换，也未给原 H 上的正秩一因子分解。

这些链映射和下界均未支付 $Cf_1\in\operatorname{Dom}M_2$ 或 $Cf_2\in\operatorname{Dom}M_1$，没有真空的共同分母原像，也没有使共同最小图成为最大交域。普通 Hilbert ISP 的完成标准尚未达到。
