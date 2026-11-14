# 工作接口：完整 ordinary Bell 的曲线临界簇与符号分母边界

> 2026-11-13 后续更新：本稿中保留的六模式候选待证状态，现由[精确有理jet与真实Bell逆证明](../results/R150-appendix-six-mode-exact-jacobian-jets-and-all-square-fibers.md)完成为指定F²的全部λ及指数权；原曲线/符号方法障碍和不扩一般外Q的范围不变。

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：完整合并矩生成式、有限代数及理想边界已逐项核验。本稿不把标量临界点视为真实算子的谱点或核向量。

本稿接[六连续模式的固定阶目标障碍](2026-11-13-six-consecutive-log-modes-curve-spectrum-and-single-layer-pure-power-obstruction-1cf.md)。
除了给出 $F^2$ 的准确完整 ordinary Bell 多项式，还构造全部 $F^h$、$h\ge2$ 的显式曲线临界簇。
因此，一类试图以 first 的**符号幂**代替 Jacobian 单位的证书确实失败。
完整 ordinary Bell 幂含高矩修正，并不受这个排除结论限制。

## 1. 全部有限合并变量与归一系数

使用连续正实指数的归一模式
$$
U_j=u_j/j,\qquad 1\le j\le q,
$$
并把有限标量一次变量记为 $x_0,\ldots,x_{q-1}$。
对应物理曲线为
$$
v(z)=(1,z,\ldots,z^{q-1}).
$$
固定一个目标多项式的次数上限 $D$。
全部合并矩变量记为
$$
W_{d,m},\qquad 2\le d\le D,\quad0\le m\le(q-1)d.
$$
第一层直接用 $W_{1,j}=x_j$。
这里已经合并所有相同 $(d,m)$ 的原矩，不把重复物理行当独立变量。

定义常系数微分算子
$$
\mathcal D_{d,m}
=\sum_{\substack{0\le i_1,\ldots,i_d\le q-1\\i_1+\cdots+i_d=m}}
\partial_{i_1}\cdots\partial_{i_d}.
$$
该和按有序指标计数，故
$$
(v(z)\cdot\nabla)^d=\sum_m z^m\mathcal D_{d,m}.
\tag{1.1}
$$
对 $\deg H\le D$，完整 ordinary 矩变换准确为
$$
\mathcal Q_H(x,W)=
\exp\!\left[
\sum_{d=2}^{D}\frac{(-2)^{d-1}}{d!}
\sum_mW_{d,m}\mathcal D_{d,m}
\right]H(x).
\tag{1.2}
$$
指数在有限多项式上自动终止。
它与[完整合并矩生成式](../results/R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)一致。

特别，
$$
\partial_{W_{d,m}}\mathcal Q_H
=\frac{(-2)^{d-1}}{d!}\mathcal Q_{\mathcal D_{d,m}H}
\quad(d\ge2),
\qquad
\partial_{x_j}\mathcal Q_H=\mathcal Q_{\partial_jH}.
\tag{1.3}
$$
本稿的临界理想使用 (1.2) 的**全部显示变量**。
实际 Bell 还含已付的快累积量修正；没有在本稿删掉那些修正后作算子结论。

设 $F$ 为齐次二次式，满足
$$
F(v(z))\equiv0.
\tag{1.4}
$$
写
$$
F(x)=\frac12x^{\mathsf T}Kx,\qquad K=K^{\mathsf T}.
$$
以下临界簇构造不要求 $K$ 可逆。
前稿的六模式
$$
F=(x_2x_6-5x_3x_5+4x_4^2)
+i(x_1x_6-5x_2x_5+4x_3x_4)
+(5x_1x_5-32x_2x_4+27x_3^2)
$$
使用从1开始的旧坐标编号，满足 (1.4)，且其 Hessian 可逆。

## 2. $F^2$ 的完整普通矩公式

对 $d>2$，由 (1.4)，
$$
F(x+s v(z))=F(x)+s\,v(z)\cdot\nabla F(x),
$$
所以 $(v(z)\cdot\nabla)^dF^2=0$。
再由 (1.1) 的有限系数比较，
$\mathcal D_{d,m}F^2=0$。
因此 $\mathcal Q_{F^2}$ 准确地只依赖第一、二阶变量。

令
$$
H=(H_{ij})_{0\le i,j\le q-1},
\qquad H_{ij}=W_{2,i+j}.
$$
注意 $H$ 是对称 Hankel 矩阵；没有再除以2。
(1.2) 的二阶指数恰为
$$
\mathcal L_H=-\sum_{i,j}H_{ij}\partial_i\partial_j.
\tag{2.1}
$$
由 $v(z)^{\mathsf T}Kv(z)=0$ 得每条反对角的 $K$ 元素和为零，故
$$
\operatorname{tr}(KH)=0.
$$
直接求导给
$$
\mathcal L_HF^2=-2x^{\mathsf T}KHKx,
\qquad
\mathcal L_H^2F^2=4\operatorname{tr}((KH)^2),
\qquad
\mathcal L_H^3F^2=0.
$$
因此
$$
\boxed{
\mathcal Q_{F^2}(x,H)=
F(x)^2-2x^{\mathsf T}KHKx
+2\operatorname{tr}((KH)^2).
}
\tag{2.2}
$$
末项是矩阵乘积平方的迹，绝不是 $2[\operatorname{tr}(KH)]^2$。

任取 $x=t v(z)$，令
$$
H=\frac12xx^{\mathsf T},
\qquad
W_{2,m}=\frac12t^2z^m.
\tag{2.3}
$$
它确是允许的 Hankel 矩阵，且 $F(x)=0$。
对第 $m$ 条反对角的单位矩阵 $H_m$，
$$
\partial_{W_{2,m}}\mathcal Q_{F^2}
=-2x^{\mathsf T}KH_mKx
+4\operatorname{tr}(KH_mKH)=0,
$$
因为 (2.3) 使两项准确相消。
一次梯度为
$$
\nabla_x\mathcal Q_{F^2}
=2F(x)Kx-4KHKx=0.
$$
(2.2) 本身也为零。
所有更高显示变量的导数已在上面证明恒零。
所以 (2.3) 是**完整** $\mathcal Q_{F^2}$ 的零临界簇。

## 3. 一条统一的有限累积量截面

上一节不限于平方。
对任意固定次数上限 $D$，定义显示变量的有限截面
$$
x_j=t z^j,\qquad
W_{d,m}=\frac{(d-1)!}{2^{d-1}}t^d z^m
\quad(2\le d\le D).
\tag{3.1}
$$
在有限变量 $s=(s_0,\ldots,s_{q-1})$ 中，置
$\xi=t\,v(z)\cdot s$。
(1.2) 的完整指数生成函数在 (3.1) 上成为
$$
\exp\!\left[
\sum_{d=1}^{D}\frac{(-1)^{d-1}}d\,\xi^d
\right]
=1+\xi
\quad\text{模总次数 }>D.
\tag{3.2}
$$
只比较有限次数系数；这里没有定义任何无界指数算子。

因此对所有 $\deg H\le D$，
$$
\boxed{
\left.\mathcal Q_H\right|_{(3.1)}
=H(0)+t\,v(z)\cdot\nabla H(0).
}
\tag{3.3}
$$
这也再次核验 (2.3) 的 $1/2$ 因子。
其余 $d\ge3$ 参数对 $\mathcal Q_{F^2}$ 没有影响，但对一般目标保留为 (3.1)。

## 4. 所有高次外层的真实完整标量临界值

取任意非恒定一变量多项式 $Q$，满足
$$
Q'(0)=0,
\qquad G=Q(F).
\tag{4.1}
$$
写 $Q(y)=q_0+\sum_{k\ge2}q_k y^k$，并取 $D=\deg G$。
则 (3.1) 给
$$
\mathcal Q_G=q_0,
$$
因为 $G$ 除常数以外的次数至少为4。

现在核全部偏导。
对每个 $k\ge2$ 及物理方向 $v(\zeta)$，
(1.4) 使
$$
(v(\zeta)\cdot\nabla)^dF^k=0
\quad(d>k).
$$
当 $1\le d\le k$ 时，这个导数为齐次多项式，次数为
$$
2k-d\ge k\ge2.
$$
所以 (3.3) 同样把它送为零。
由 (1.1) 对 $\zeta$ 的有限系数比较，
所有 $\mathcal Q_{\mathcal D_{d,m}G}$ 均在 (3.1) 上为零。
再用 (1.3)，完整显示梯度全部为零。

得到准确命题：
$$
\boxed{
Q'(0)=0
\ \Longrightarrow\
(3.1)\text{ 是完整 }\mathcal Q_{Q(F)}
\text{ 的临界簇，临界值为 }Q(0).
}
\tag{4.2}
$$
特别，任意 $h\ge2$ 的 $\mathcal Q_{F^h}$ 都具有这个零临界簇。

有限 $z$ 已足够下面的理想结论。
若需射影无穷端点，直接取一次变量 $x=t e_{q-1}$，
且每层只令 $W_{d,d(q-1)}=(d-1)!t^d/2^{d-1}$ 非零；
同一个一变量生成式给 (3.3)—(4.2)。
因此不存在遗漏的无穷方向。

## 5. 哪一类 Jacobian 分母确实被排除

令
$$
\mathcal J=
\left(
\mathcal Q_{Q(F)}-Q(0),
\ \partial_{x_j}\mathcal Q_{Q(F)},
\ \partial_{W_{d,m}}\mathcal Q_{Q(F)}
\right),
\qquad Q'(0)=0.
\tag{5.1}
$$
取任意非零仿射一次符号
$$
a(x)=a_0+\sum_{j=0}^{q-1}a_j'x_j.
$$
在临界簇上，
$$
a(t v(z))=a_0+t\sum_j a_j'z^j.
$$
它不是恒零的二变量多项式：
若恒零，先取 $t=0$ 给 $a_0=0$，再比较 $z$ 系数给所有 $a_j'=0$，矛盾。
所以任何正整数 $N$ 都有
$$
\boxed{a(x)^N\notin\sqrt{\mathcal J}.}
\tag{5.2}
$$
这里只用“理想中多项式在其全部零点上为零”的必要条件，不需要反向 Nullstellensatz。

同理，若 $a_1,\ldots,a_s$ 是有限个非零仿射一次符号，
则它们在 (3.1) 上各为非零二变量多项式；
$\mathbb C[t,z]$ 无零因子给
$$
\boxed{
\prod_{\nu=1}^s a_\nu(x)^{N_\nu}
\notin\sqrt{\mathcal J}
\quad(N_\nu\ge1).
}
\tag{5.3}
$$
这排除的是在**完整 ordinary 显示多项式理想**中，
以这类一次符号乘积作分子的 Jacobian 除法证书。
它不依赖这些一次符号对应的真实 first 是否空谱。

## 6. 完整 Bell 幂仍是不同的候选

必须保留以下区别。
对齐次一次符号 $a(x)=r\cdot x$，
其完整二次 ordinary Bell 为
$$
\mathcal Q_{a^2}(x,H)
=(r\cdot x)^2-2r^{\mathsf T}Hr.
\tag{6.1}
$$
在 (2.3) 上它恰为零。
更一般，由 (3.3)，
$$
\left.\mathcal Q_{a^n}\right|_{(3.1)}=0
\qquad(n\ge2).
\tag{6.2}
$$
所以本稿**不能**排除这些完整 Bell 多项式的幂进入 $\mathcal J$ 或其根理想。
若 $a(U)$ 是已付的空谱 first，
[完整单 first Bell 逆](../results/R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md)仍提供真实有界逆。
是否能为它们建立原 $\mathcal Q_G$ 的准确理想证书、再支付实际快修正和原反射顺序，
是另一个尚未完成的问题。

同样，没有排除多 first 的完整矩形 Bell、多阶算子目标、真实快累积量的额外恒等式或其他核证明。
(4.2) 是标量显示空间的临界簇；未证明这些显示数值由实际联合谱实现。
它不能被改写成不循环向量或非平凡不变子空间。

六模式例的一次 $[F(U)-\lambda]e^w$ 对所有 $\lambda,w$ 的循环性，
仍由前稿 Hessian 可逆后的实像判据成立。
本稿没有撤回该实际结论。

## 7. 六连续模式的二阶矩准确消元

本节仅对前述具体六模式 $F$。为保持全部有限系数为实整数，先作**标量多项式**坐标变换
$$
x_j=i^j y_j,\qquad W_{2,m}=i^m w_m,\qquad 0\le j\le5.
$$
它不是对原实际 first 或 Hilbert 空间作未付的相似。变换后
$$
F'(y)=g_6(y)-g_7(y)-g_8(y)=\tfrac12y^{\mathsf T}K'y,
$$
其中
$$
K'=\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix}.
\tag{7.1}
$$
令 $H_m$ 为第 $m$ 条反对角上的 $6\times6$ 单位指示矩阵，即 $(H_m)_{ij}=1_{i+j=m}$，并定义
$$
H(w)=\sum_{m=0}^{10}w_mH_m,\qquad
b_m(y)=(K'y)^{\mathsf T}H_m(K'y),\qquad
J'_{mn}=\operatorname{tr}(K'H_mK'H_n).
\tag{7.2}
$$
这些 $H_m$ 不是单个矩阵单位；有序的两个对称位置均保留。

### 7.1 一个可逐项重算的非零行列式

令 $k'(z,u)=v(z)^{\mathsf T}K'v(u)$。由指标求和，
$$
J'_{mn}=[z^mu^n]\,k'(z,u)^2.
\tag{7.3}
$$
因此 (7.1)—(7.3) 已明确给出全部 $121$ 个整数条目。准确整数消元给
$$
\boxed{\det K'=-25600,\qquad
\det J'=-64701092257700249600\ne0.}
\tag{7.4}
$$
原未变换的复矩阵 $J$ 的行列式为相反数。

这里附上完全可复算的[整数与有理数证书脚本](2026-11-13-six-mode-second-moment-exact-certificate.js)和[完整消元数据](2026-11-13-six-mode-second-moment-exact-data.json)。脚本先独立比较迹公式与卷积公式，然后使用分数自由 Bareiss 消元；所有整除均实际检查。取从0开始的行编号，换行为
$$
(0,8),\ (1,7),\ (2,6),\ (3,5).
$$
顺次主元为
$$
\begin{gathered}
25,\ -8000,\ -12512000,\ 47245312000,\ 236887994368000,\\
-894489066733568000,\ -1398980900371300352000,\\
447673888118816112640000,\ 11191847202970402816000000,\\
214023623696213816115200.
\end{gathered}
$$
最后剩余条目即 (7.4) 的 $\det J'$。四次换行总符号为正。
有理逆另外逐条验证 $J'(J')^{-1}=I$，没有使用浮点阈值判断可逆。

### 7.2 完整临界理想化成一个六变量四次式

由 (2.2)，该实际**完整 ordinary 标量多项式**准确为
$$
P(y,w)=F'(y)^2-2b(y)^{\mathsf T}w+2w^{\mathsf T}J'w.
$$
定义
$$
\boxed{
R(y)=F'(y)^2-\tfrac12 b(y)^{\mathsf T}(J')^{-1}b(y),\qquad
z=w-\tfrac12(J')^{-1}b(y).
}
\tag{7.5}
$$
配方得到恒等式
$$
\boxed{P=R+2z^{\mathsf T}J'z.}
\tag{7.6}
$$
特别，$\nabla_wP=4J'z$，所以每个临界点唯一确定
$$
w=\tfrac12(J')^{-1}b(y).
\tag{7.7}
$$
这是完整二阶矩消元，没有删去任何合并坐标。

更准确地，在全部显示变量的多项式环中，
$$
\boxed{
(P,\nabla_yP,\nabla_wP)
=(z_0,\ldots,z_{10},\partial_{y_0}R,\ldots,\partial_{y_5}R).
}
\tag{7.8}
$$
证明：$J'$ 可逆首先把 $\nabla_wP$ 与 $z$ 相互生成；模 $z$ 后 $\nabla_yP=\nabla R$。$R$ 是齐次四次式，Euler 恒等式 $4R=\sum_j y_j\partial_jR$ 把 $P$ 本身也放入右侧。反向包含同样由这些等式逐项给出。原先的三、四阶显示变量没有出现在 $P$ 中；(7.8) 对加入这些自由变量后的完整环仍成立。

附带数据给出 $R$ 的全部102个非零有理系数，亦逐系数验证
$$
R(v(t))=0,\qquad \nabla R(v(t))=0.
$$
这些核验只确认已证曲线包含，**没有证明它穷尽临界簇**。其他临界分支必须继续识别。

### 7.3 完整 Bell 平方候选的准确剩余问题

对固定有限一次符号 $a'(y)=r^{\mathsf T}y$，记
$$
c_m(r)=\sum_{i+j=m}r_ir_j.
$$
其完整普通 Bell 平方经 (7.7) 化为明确二次式
$$
\boxed{
B_r(y)=(r^{\mathsf T}y)^2-c(r)^{\mathsf T}(J')^{-1}b(y).
}
\tag{7.9}
$$
由 (7.8)，对任意 $N\ge1$，
$$
\boxed{
\mathcal Q_{(a')^2}^{\,N}\in(P,\nabla P)
\iff
B_r^{\,N}\in(\partial_{y_0}R,\ldots,\partial_{y_5}R).
}
\tag{7.10}
$$
这是有限标量理想的准确等价，不是已经证明左侧有解。多个完整 Bell 因子的乘积也可用同一商逐个代入。

使用任何解之前，还要把 $a'$ 还原成原一次符号 $a(x)=\sum_j i^{-j}r_jx_j$，验证该**原** first 的真实全域逆，并支付原 Bell 快修正、共同域及反射顺序。本节没有完成这些后续步骤；既有一次全部位移结论与当前未闭的高次目标范围均保持不变。

## 8. 两个曲线外的准确临界点与三个空谱 first 候选

本节接 §7 的实化坐标
$$
x_j=i^j y_j,\qquad W_{2,m}=i^m w_m,\qquad0\le j\le5.
$$
于是 $K'=DKD$ 为已列出的实整数矩阵，$F'=g_6-g_7-g_8$。
记 $H'_{ij}=w_{i+j}$，
$$
\mathcal Q'=
F'(y)^2-2y^{\mathsf T}K'H'K'y+
2\operatorname{tr}((K'H')^2).
$$
以下先给完整 $\mathcal Q'$ 的两个精确临界点，再构造已知具有实际全域逆的 first 候选。
不声称临界簇只有这些点与原曲线。

### 8.1 两个完整有理临界点

令两组参数为
$$
(s_+,p_+,q_+)=\left(5,\frac{32}{5},\frac85\right),
\qquad
(s_-,p_-,q_-)=\left(-27,\frac{864}{5},-\frac{864}{5}\right).
\tag{8.1}
$$
一次坐标取 $y^\pm=n^\pm/n^\pm_0$，其中
$$
n^+=(990895,1153105,2063840,4524760,11260192,30644640),
$$
$$
n^-=(143682655,-222517655,664053920,
-4306767840,39985265088,-450141192000).
\tag{8.2}
$$
因此两点都按 $y_0=1$ 归一。

二阶 Hankel 矩由前三项及真实有限递推完整确定：
$$
w_m=s_\pm w_{m-1}-p_\pm w_{m-2}+q_\pm w_{m-3},
\qquad 3\le m\le10.
\tag{8.3}
$$
正号点的前三项为
$$
(w_0,w_1,w_2)=
\frac1{198179^2}
(16101657680,21318672120,33195718080).
\tag{8.4}
$$
负号点的前三项为
$$
w_0=\frac{683860887117640}{825788213913961},
\quad
w_1=-\frac{22949602239620}{22318600376053},
\quad
w_2=\frac{1138708823114240}{825788213913961}.
\tag{8.5}
$$

对每一个点，准确有理数相乘给
$$
F'(y)=0,\qquad
H'K'y=0,
\tag{8.6}
$$
以及对所有 $0\le m\le10$，
$$
\operatorname{tr}(K'H_mK'H')
=\frac12y^{\mathsf T}K'H_mK'y.
\tag{8.7}
$$
这里 $H_m$ 是第 $m$ 条反对角的单位矩阵。
(8.6)—(8.7) 直接给 $\mathcal Q'=0$、六个一次梯度和十一个二阶梯度全为零。
更高显示变量的偏导由 §2 恒为零。
所以这是完整 ordinary 多项式的临界点，而不只是截断梯度的零点。

同时，$y_0y_2-y_1^2\ne0$，故两点均不在原有理正规曲线上。
可重算的[自含有理证书](2026-11-13-six-mode-extra-critical-points-empty-first-candidates-certificate.js)
保存全部坐标，并以 BigInt 有理数逐项核验
(8.6)—(8.7)、完整梯度、临界值以及下面全部候选恒等式。
代码不依赖浮点数、外部库或某次有限域的点计数。

为说明这些坐标的来源，令
$$
k'(z,w)=v(z)^{\mathsf T}K'v(w)=(z-w)^2\ell'(z,w).
$$
置 $u=z+w,v=zw$，则
$$
\ell'=(5-v)u^2-u^3+6uv-32v+5v^2.
$$
三个不同参数两两 $\ell'=0$ 的对称数 $(s,p,q)$ 满足
$$
-s^2+4s+5p-27=0,
$$
$$
s^3-3s^2+22s-5sp-p+4q=0,
$$
$$
5s^2-ps^2-s^3+6sp-32p+5p^2-(3s+5)q=0.
$$
本节选用下面的解族；代入可直接核验以上三个余式均为零：
$$
p=\frac{s^2-4s+27}{5},\qquad
q=\frac{-4s^2+21s+27}{20},\qquad
s^2+22s-135=0.
$$
故出现 (8.1) 的两组三次
$5z^3-25z^2+32z-8$ 与
$5z^3+135z^2+864z+864$。
这个构造只用来产生上面的点，未被当作全部临界点的分类。

### 8.2 坐标 Bell 平方不能直接作该理想分母

令
$$
C^\pm=y^\pm(y^\pm)^{\mathsf T}-2H'^\pm.
$$
对任意线性符号 $a=r\cdot y$，
完整二次 ordinary Bell 在该点的值为
$$
\mathcal Q_{a^2}=r^{\mathsf T}C^\pm r.
\tag{8.8}
$$
在正号点，六个对角值 $C^+_{jj}$ 全部非零；证书逐项保存其精确值。
例如
$$
C^+_{00}=\frac{7071600681}{198179^2},
\qquad
C^+_{11}=-\frac{13205390519}{198179^2},
\qquad
C^+_{55}=-\frac{6877955415040}{198179^2}.
$$
回到原坐标只给第 $j$ 项乘 $(-1)^j$，非零性不变。

所以各坐标完整 Bell $\mathcal Q_{U_j^2}$，
以及有限个这些多项式的任意正幂乘积，
都不属于$\mathcal Q_{F^2}$ 的完整零纤维临界理想的根基。
这里的幂是该**完整显示多项式**的普通代数幂，
不是点态高次 $U_j^{2N}$ 的另一完整 Bell 多项式。

这与 §6 的范围相容：原曲线临界簇不能排除完整 Bell 平方，
而这两个新增点确实排掉了最直接的坐标选择。
它仍不排一般 first 的线性组合。

### 8.3 两个节点的零条件化为两个小整数二次式

取实化一次方向
$$
r=(A,B,0,0,0,1).
$$
从 (8.8) 直接清去非零有理比例后，
$r^{\mathsf T}C^+r=0$ 与 $r^{\mathsf T}C^-r=0$
准确等价于
$$
f(A,B)=
-279A^2-242AB-65856A
+521B^2-46784B+271360=0,
\tag{8.9}
$$
$$
g(A,B)=
-1769A^2+2738AB-16087680A
-969B^2+19820160B+140341248=0.
\tag{8.10}
$$
所有六个二次系数与实际节点的 $3\times3$ 子矩阵比例均由证书准确核验。

令 $d=B-A$。
(8.9) 变成
$$
160(5d-704)A+521d^2-46784d+271360=0.
$$
从而取
$$
\boxed{
A=-\frac{521d^2-46784d+271360}{160(5d-704)},
\qquad B=A+d,
}
\tag{8.11}
$$
并令
$$
\boxed{
3725d^3-43931504d^2+6080833024d+52565262336=0.
}
\tag{8.12}
$$
代入 (8.9)—(8.10)，通分后的两个多项式模 (8.12) 余数都严格为零。
分母的根 $d=704/5$ 不是 (8.12) 的根。

(8.12) 在三个互不相交区间
$$
(-9,-8),\qquad(144,149),\qquad(11600,11700)
$$
两端各异号。
因此恰有三个不同实根；对每个根，(8.11) 给实数 $A,B$。
不需要数值近似来定义任何候选。
作为校准，第一组约为 $A=5.772908288$、$B=-2.389803331$。

### 8.4 每个候选确实具有已付的实际全域逆，但理想证书仍欠

回原模式，可取
$$
\boxed{a=iA\,U_1+B\,U_2+U_6.}
\tag{8.13}
$$
它在实化坐标中的系数是 $i r$，
所以 $\mathcal Q_{a^2}$ 在两个点上的值都是
$-r^{\mathsf T}C^\pm r=0$。
它在原曲线临界簇上也为零，来自 §6。

另一方面，(8.13) 的真实未倾斜行是
$$
c_p=\frac{L_p^5+B L_p+iA}{p+2},
\qquad L_p=\log(p+2).
$$
它属于 $\ell^2\setminus\ell^1$，尾部实部为正，并且
$$
|c_p|-\operatorname{Re}c_p
=\frac{(\operatorname{Im}c_p)^2}
{|c_p|+\operatorname{Re}c_p}
=O\!\left(\frac1{p(\log p)^5}\right).
$$
因此 [R138](../results/R138-first-chaos-complete-spectrum-classification.md)
确实给这个原 first 空谱。
原固定中心和任意固定复 $w$ 倾斜只加已付的有界交换扰动；
其逆仍由拟幂零预解因式给出，不能仅靠形式行来宣称。

由[单 first 完整 Bell 逆](../results/R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md) §4，
$a^2e^w$ 的真实规范实现具有全域有界 $A'$ 逆。
这是候选自身已经成立的算子性质。

但本节尚未证明以下任何一步：
这些点与曲线穷尽完整临界簇；
$\mathcal Q_{a^2}$ 的某个代数幂进入完整 Jacobian 理想；
该证书经过真实快累积量修正后在原核上给有效近单位。
所以目前只有“真实可逆候选同时杀掉已知临界点”的准确进展，
没有由此宣布 $F(U)^2e^w$ 循环。

任何有限域的点数或小次数 membership 筛选均不用于替代这三个尚欠步骤。
