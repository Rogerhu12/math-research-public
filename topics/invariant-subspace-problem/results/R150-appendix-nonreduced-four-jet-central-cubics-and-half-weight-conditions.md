# R150 附录：满秩重支撑的中心矩三次曲线与全部半权条件

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。

状态：**已证明。** 对原非 secant、外 mean、本质三维且 $H$ 秩四的完整立方临界截面，将唯一长度四支撑的各局部 jets 按同一个 $\lambda$ 归一后，$T_3$ 准确成为该长度四交换代数上的三阶中心矩。本文给全部非约化重数分拆的显式平面方程、奇点、可约性及原物理有理曲线所迫的条件。

结论中，$3+1$ 的单点权必须为 $1/2$；$2+1+1$ 的两个单点权 $b,c$ 必须满足 $b=1/2$、$c=1/2$ 或 $b+c=1/2$。$2+2$ 总是节点三次曲线或光滑二次曲线乘一直线。所有不可约三次情形的奇点都是普通节点，**没有尖点情形**。四重支点的代数模型也列出，但它在原核下已由[四重 jet 排除稿](R150-appendix-quadruple-jet-supports-have-no-full-rank-outer-mean-critical-point.md)删除。这里只给剩余完整临界点的必要条件，没有声称满足表中权条件即可满足原全部梯度。

## 1. 原收缩关系给出的有限代数，而非另加的矩模型

由[四 jets 归约](R150-appendix-essential-cubic-conormal-and-four-jet-support-reduction.md)，有唯一长度四支撑 $g$、四维空间 $E=E_g$、非零三次张量的本质空间 $W\subset E$，以及 $\lambda\in E^*$，使
$$
\lambda|_W=0,\qquad\lambda(y)=1,\qquad
H=2V\lambda,\qquad y=8V\lambda\lambda.
\tag{1.1}
$$
设支撑的局部长度为 $n_i$，$\sum_i n_i=4$，且局部曲线的除阶乘展开为
$$
\nu_i(t)=\sum_{j\ge0}u_{ij}t^j.
$$
原 Hankel 张量的各支撑块准确为
$$
V_i=\sum_{j=0}^{n_i-1}v_{ij}[t^j]\nu_i(t)^{\otimes3}.
\tag{1.2}
$$
$E$ 中不同支撑块的 jet 向量共同构成基；收缩保留块分解。在第 $i$ 块，$H$ 的系数矩阵沿反对角线都是 $2v_{i,n_i-1}\lambda(u_{i0})$，反对角线以外的高侧全为零。因此 $H$ 秩四准确迫每块
$$
v_{i,n_i-1}\lambda(u_{i0})\ne0.
\tag{1.3}
$$
于是可在每个局部环中使用同一泛函作可逆归一：
$$
\widehat\nu_i(t)=\frac{\nu_i(t)}{\lambda(\nu_i(t))}
\pmod{t^{n_i}}.
$$
归一后的第零向量取 $\lambda$ 值一，其余 jets 取零。变换是可逆的三角变换，仍准确表示原 $H,V,y$，没有换掉支撑或最高 jet。

令
$$
\mathcal A=\bigoplus_i\mathbb C[\varepsilon_i]/(\varepsilon_i^{n_i}).
$$
对 $r\in E^*$，以 $X_i(t)=r(\widehat\nu_i(t))\bmod t^{n_i}$ 识别 $r$ 与 $X\in\mathcal A$。归一后的 (1.2) 给一个线性泛函 $\tau:\mathcal A\to\mathbb C$，使
$$
\boxed{
\tau(1)=1,\quad y(r)=\tau(X),\quad
H(r,r)=\tfrac14\tau(X^2),\quad V(r,r,r)=\tfrac18\tau(X^3).
}
\tag{1.4}
$$
其中 $\tau=8$ 倍归一后各 jet 系数泛函；$\tau(1)=8V(\lambda,\lambda,\lambda)=\lambda(y)=1$。$H$ 满秩等价于双线性型 $(X,Y)\mapsto\tau(XY)$ 非退化，故各长度大于一的局部块的最高幂取值非零，各单点权非零。

现在直接代入原 $T_3$：
$$
\begin{aligned}
T_3(r)
 &=\tau(X)^3-\tfrac32\tau(X)\tau(X^2)+\tfrac12\tau(X^3)\\
 &=\boxed{\tfrac12\tau\bigl((X-\tau(X)1)^3\bigr).}
\end{aligned}
\tag{1.5}
$$
所有权都是复数，$\tau$ 只作为线性泛函使用，没有正性假设。这在 $X\mapsto X+c1$ 下不变。因此它是 $\mathcal A/\mathbb C1$ 上的三元齐次式，而该商正对应原 $W$ 的三维坐标。下面所有换元都可逆，并保留原 $\lambda$；它们不是任意选取另一个三次曲线。

## 2. 三重支点加单点：单点权准确等于一半

取
$$
\mathcal A=\mathbb C[\varepsilon]/(\varepsilon^3)\oplus\mathbb C,
\quad \tau(1_{\rm single})=a\ne0,
\quad \tau(\varepsilon)=\alpha,\quad\tau(\varepsilon^2)=\beta\ne0.
$$
三重块的总权为 $1-a$。减去常数后，可取 $X=(x+u\varepsilon+v\varepsilon^2,0)$。记
$$
m=\tau(X)=(1-a)x+\alpha u+\beta v,\qquad n=m-x.
$$
因 $\beta\ne0$，$(n,x,u)$ 是商空间的坐标。由
$$
\tau(X^2)=2xm-(1-a)x^2+\beta u^2,\qquad
\tau(X^3)=3x^2m-2(1-a)x^3+3\beta xu^2
$$
得到准确方程
$$
\boxed{2T_3=2n^3-3a x^2n-a x^3-3\beta n u^2.}
\tag{2.1}
$$
该三次式对所有 $a\beta\ne0$ 都不可约。若它有直线因子且该直线可写为 $u=An+Bx$，代入后的 $x^3$ 系数仍为 $-a$，不可能恒零；若直线只含 $n,x$，则 $u^2$ 系数迫该直线为 $n=0$，而此时余式 $-ax^3$ 非零。另一个坐标图 $x=0$ 同样不成为因子。三次式可约必有直线因子，故证毕。

其 $u$ 偏导为 $-6\beta n u$。奇点若 $n=0$，方程迫 $x=0$，其 $n$ 偏导又迫 $u=0$，不可能。因此奇点必须 $u=0$。另两个偏导给
$$
6n^2-3a x^2=0,\qquad -3ax(2n+x)=0.
$$
故准确有
$$
\boxed{\text{三次曲线奇异}\iff a=\tfrac12,\quad
\text{唯一奇点 }[n:x:u]=[-1:2:0].}
\tag{2.2}
$$
在 $x=1$、$n=-1/2+\eta$ 的图中，(2.1) 的二阶项是 $-3\eta^2+\tfrac32\beta u^2$，非退化，所以是普通节点。

原最高梯度使原有理曲线的三维物理投影落在 (2.1) 上；因其张成整个平面且三次式不可约，像就是该三次曲线。光滑平面三次曲线不能被 $\mathbb P^1$ 非恒定覆盖：其函数域若嵌入 $\mathbb C(z)$，Lüroth 定理迫其为有理函数域，与光滑平面三次曲线的属一矛盾。因此完整临界点必须满足 $a=1/2$，没有其他单点权。

## 3. 两个双支点：一般是节点三次，一种半权值给二次分支

取两块的总权为 $\mu,1-\mu$，最高 nilpotent 权为 $\alpha,\beta$，其中 $\alpha\beta\ne0$。减去第二块常数，写
$$
X=(x+u\varepsilon,v\eta),\qquad m=\mu x+\alpha u+\beta v.
$$
则
$$
\tau(X^2)=\mu x^2+2\alpha xu,\qquad
\tau(X^3)=\mu x^3+3\alpha x^2u.
$$
置
$$
n=m-\tfrac12x,\qquad
U=u-\frac{n}{2\alpha}-\frac{1-2\mu}{4\alpha}x.
$$
可逆换元给
$$
\boxed{T_3=n^3-3\alpha xnU+\frac{1-2\mu}{8}x^3.}
\tag{3.1}
$$
若 $\mu\ne1/2$，把它视为 $U$ 的一次式，系数 $xn$ 与常数项 $n^3+(1-2\mu)x^3/8$ 互素；Gauss 引理即给不可约。其 $U$ 偏导迫奇点满足 $xn=0$，方程再迫 $x=n=0$。所以唯一奇点是 $[n:x:U]=[0:0:1]$，二阶项 $-3\alpha xn$ 非退化，恰是普通节点。

若 $\mu=1/2$，则
$$
\boxed{T_3=n(n^2-3\alpha xU).}
\tag{3.2}
$$
二次因子秩三，因而是光滑二次曲线；直线与它在两个不同点相交。原物理像不可约且张成平面，所以只能落在这个二次因子上。这是必要的几何分支；尚未由此证明存在原完整临界点。

## 4. 一个双支点与两个单点：全部三个半权条件

设两个单点权为 $b,c\ne0$，双点的 nilpotent 权为 $\alpha\ne0$，其总权为 $1-b-c$。减去双点常数，写
$$
X=(u\varepsilon,x,y),\qquad m=\alpha u+bx+cy.
$$
$(m,x,y)$ 是可逆坐标，而
$$
\boxed{2T_3=2m^3-3m(bx^2+cy^2)+bx^3+cy^3.}
\tag{4.1}
$$
若存在奇点，$m=0$ 会由 $x,y$ 偏导迫 $x=y=0$，故可归一为 $m=1$。两个偏导准确给
$$
x\in\{0,2\},\qquad y\in\{0,2\},
$$
再用 $m$ 偏导，得到全部可能：

| 权条件 | 奇点 $[m:x:y]$ |
|---|---|
| $b=1/2$ | $[1:2:0]$ |
| $c=1/2$ | $[1:0:2]$ |
| $b+c=1/2$ | $[1:2:2]$ |

除此以外没有奇点。在 $m=1$ 图中，每个上述点的二阶型对角系数分别由 $\pm3b,\pm3c$ 给出；因 $bc\ne0$，均非退化。所以每个都是普通节点。

若没有任何半权条件，曲线光滑，原有理物理像不可能覆盖它，故排除。若恰一个条件成立，则只有一个普通节点，曲线不可约：可约且约化的平面三次若为直线加二次曲线，会有两个横截交点，或一个非普通的相切奇点；三个直线也不能只产生一个普通节点。重复因子则产生非孤立奇异集，同样不符上述完整奇点计算。

多个条件能同时成立的唯一允许值是 $b=c=1/2$；另两种重合会使一个单点权为零。此时准确分解为
$$
\boxed{
4T_3=(x+y-2m)\bigl(x^2-xy+y^2-m(x+y)-2m^2\bigr).
}
\tag{4.2}
$$
第二因子是光滑二次曲线。例如用 $S=x+y,D=x-y$，它等于
$$
\tfrac14(S-2m)^2+\tfrac34D^2-3m^2,
$$
明显秩三。它与直线在上述两个不同普通节点相交。原非退化物理像只能是二次因子。

所以该重数分拆的准确必要条件是
$$
\boxed{b=\tfrac12\quad\text{或}\quad c=\tfrac12
\quad\text{或}\quad b+c=\tfrac12.}
\tag{4.3}
$$
其中 $b=c=1/2$ 给二次像，其余允许值给不可约节点三次像。

## 5. 单个四重支点的代数模型

为把全部非约化类型覆盖完整，取 $\mathcal A=\mathbb C[\varepsilon]/(\varepsilon^4)$，并记
$$
\tau(1)=1,\quad\tau(\varepsilon)=\alpha,
\quad\tau(\varepsilon^2)=\beta,
\quad\tau(\varepsilon^3)=\gamma\ne0.
$$
减去常数后 $X=u\varepsilon+v\varepsilon^2+w\varepsilon^3$。取
$$
m=\tau(X),\qquad U=v+\frac\beta{2\gamma}u,
$$
直接得到
$$
\boxed{T_3=m^3-3\gamma muU+\tfrac12\gamma u^3.}
\tag{5.1}
$$
与 §3 同理，此式总是不可约节点三次，唯一节点 $[m:u:U]=[0:0:1]$。但[原核的四重 jet 排除](R150-appendix-quadruple-jet-supports-have-no-full-rank-outer-mean-critical-point.md)已经证明：这类抽象中心矩模型没有满足本文原完整临界条件的物理实现。因此不能把代数上有理的三次曲线当作实际解。

## 6. 对剩余物理截面的准确影响

汇总已经支付的必要条件：

| 支撑重数 | 原满秩临界点的必要条件 | 三维物理像 |
|---|---|---|
| $3+1$ | 单点权 $a=1/2$ | 不可约普通节点三次 |
| $2+2$ | 块权 $\mu\ne1/2$ | 不可约普通节点三次 |
| $2+2$ | 块权 $\mu=1/2$ | 光滑二次曲线 |
| $2+1+1$ | $b=1/2$、$c=1/2$、$b+c=1/2$ 中恰一个 | 不可约普通节点三次 |
| $2+1+1$ | $b=c=1/2$ | 光滑二次曲线 |
| $4$ | 原核已全部排除 | 无完整临界点 |

由[原二次曲面的光滑中心与双有理投影](R150-appendix-four-jet-smooth-quadric-center-and-birational-projection.md)，这里的物理投影都是双有理。节点三次情形的完整线性系公共因子次数是二；二次情形次数是三。结合[长度四投影的至多一个简单基点](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md)，二次情形必须具有那个原四维基点，且后续中心除子长度为二，并与支撑 $g$ 互素。节点三次的四维投影可无基点或有一个基点，对应中心除子长度二或一。

这些结论只缩小原完整临界候选。尚须在每种剩余支撑上付清原极化核、二次关系及全部低梯度；也没有覆盖 $H$ 降秩、mean 的 Hankel 秩降落或本质维数四至六。全局自然幂成员关系、实际算子逆与普通 Hilbert 空间 ISP 均仍开放。
