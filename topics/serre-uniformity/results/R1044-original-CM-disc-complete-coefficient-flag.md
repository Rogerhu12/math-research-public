# R1044：原最低型 CM 圆盘的全部模 p 系数旗标

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
global_route / root；o1_theta 与 o2_high_coefficient 已全文独审 normal 几何与有限角常数。

**已证明：R1033 原整圆盘的全部非恒定模 \(p\) 系数，
按从高到低的顺序，与一组明确的 Cauchy 列构成同一个旗标。**
每一步都来自同一 full-\(p\) 源的完整 normal 层；
较高层中出现的 CM holomorphic 自由项也包含在证明中。
没有把全型的秩结论替代实际 Mordell–Weil 消去后的非零断言。

## 1. 原参数、列与结论

保持
\[
p=12g-1>37,\quad m=(p-1)/2=6g-1,\quad
e_0=m(p+1),\quad \pi_0^{e_0}=p,\quad \varepsilon=\pi_0^m.
\]
原曲线仍是 \(X_1\)，原点仍是 \(c_1\)，原整目标仍是
R1029/R1030 的 \(e_1\)，不更换为独立 CM 商。
令 \(S=\{A_p=0\}\)，\(\deg A_p=d=6g-2\)，
并用 R1023 的同一个基
\[
e_s=\theta_sf_s,\qquad
\langle f_s,\omega_t\rangle=-2\delta_{s,t},\qquad
L=\sum_{s\in S}L_s\omega_s.
\]
原中心首层是
\[
\varepsilon R_L(b)\,db,\qquad
R_L(b)=\frac2m\sum_{s\in S}\frac{L_s\theta_s}{(b-s)^2}.
\tag{1044.1}
\]

原 CM 尾和参数为
\[
D:\ y^2=x(x^{2g}+A_{\rm tail}),\quad Q=(0,0),\quad t=\sqrt x,
\]
\[
z=\frac{a-1}{\varpi^{3p(p-1)}},\qquad
w=\frac{a-1}{p^3},\qquad z=\varepsilon^3w,\qquad
\lambda_0=\left.\frac{d\bar z}{dt}\right|_Q\ne0.
\tag{1044.2}
\]
\(\kappa_1\) 仍是 R1032 的原单位
\(b_{\rm lift}-1=\kappa_1\varepsilon^3\psi_3+\cdots\)。
\(\lambda_0,\kappa_1,\sqrt{A_{\rm tail}}\) 均不设为一。

R1033 给原规范 Abel-log 的完整模 \(p\) 轮廓
\[
\overline{\mathcal H}(w)=\sum_{n=1}^{4g-1}V_n w^n,
\qquad
\mathcal H=\frac{\log(\operatorname{Abel}(P(w)-c_1))}{p\varepsilon}.
\]
对 \(i\ge0\) 定义实际底 Lie 列
\[
J_i=\sum_{s\in S}\frac{e_s}{(1-s)^{i+2}}.
\tag{1044.3}
\]
本篇的完整结论是：对每个 \(1\le k\le4g-1\)，
\[
\boxed{\quad
V_{4g-k}\equiv u_kJ_{k-1}
 \pmod{\langle J_0,\ldots,J_{k-2}\rangle},
\quad}
\tag{1044.4}
\]
其中空的 span 为零，且准确单位为
\[
\boxed{\quad
u_k=
\frac{(-1)^k\kappa_1^k(2\sqrt{A_{\rm tail}})^{3k-2}}
     {m(3k-1)}
\,\lambda_0^{-(4g-k)} .
\quad}
\tag{1044.5}
\]
当 \(k=1,2\) 时分别恢复 R1033 和 R1042。
本篇不将每条同余中的先前列倍数设为零。

## 2. 同一 full-Dickson 源上的全部参考多项式

### 2.1 恒等式和准确正规化

在 R1030 的同一 full-\(p\) 坐标中，置
\[
C=X^pY-XY^p,\qquad
c=A_0^{p+1}-B_0^{p+1},\quad
U=(A_0^{p+1}+B_0^{p+1})/2,\quad V=A_0B_0 .
\]
这里 \(c\) 是 \(C\) 的固定非零倍数，且
\[
A_{\rm tail}=c^2/4,\quad
U^2=V^{p+1}+A_{\rm tail},\quad
x=V^6,\quad y=UV^3,\quad F=UV^{p-2}=x^{2g-1}y.
\]
所有 Weil 配对分支同时保留。
R1030 证明 \(EF=F\)，其中 \(E=e_1\) 是真正整的有限角投影。

用 R1042 的真实 derivation
\[
\Theta=X^p\partial_X+Y^p\partial_Y,\qquad
\Theta V=2U,\quad\Theta U=V^p,\quad\Theta A_{\rm tail}=0.
\tag{1044.6}
\]
它与完整 \(\operatorname{GL}_2(\mathbf F_p)\) 换基及 \(E\) 交换。
对每个 \(1\le k\le4g-1\)，令
\[
n_k=3k-3,\qquad
a_k=\frac{(-1)^{n_k}(n_k+2)!}{2},\qquad
\boxed{\quad H_k=a_k^{-1}\Theta^{n_k}F.\quad}
\tag{1044.7}
\]
这里只是定义参考多项式；它同原 global source 的身份将在 §§3–5 证明。

\(H_k\) 是齐次次数 \(3k(p-1)\) 的原全分支多项式，
\(EH_k=H_k\)。
在同一个 ordinary 无穷支，
\(U\sim V^{(p+1)/2}\)，且 \(z_D=V^{-3}\) 是
R1032 的无穷参数。
在最高 \(V\) 次项上，\(\Theta\) 等于
\(2V^{(p+1)/2}\partial_V\)。
从 \(F\) 的最高次数 \(3m\) 开始，第 \(j\) 次微分的新因子是
\[
2(j+3)m=-(j+3)\quad\text{于 }k .
\]
因此 \(\Theta^{n_k}F\) 的最高系数恰为 \(a_k\)，并有
\[
\boxed{\quad H_k=z_D^{-km}+\text{较低极阶项}.\quad}
\tag{1044.8}
\]
不是只知道最高系数为某个未指定单位。

### 2.2 原 CM 点的最低 Taylor 项

在 \(Q\) 处，\(V=0\)、\(t=V^3\)、\(U(Q)=\sqrt{A_{\rm tail}}\)。
在 \(n_k\) 次微分中，唯一最低 \(V\) 次项来自每次都用
\(2U\partial_V\)；任何使用 \(\Theta U=V^p\) 的项都会提高次数。
故它的系数是
\[
2^{n_k}U(Q)^{n_k+1}(p-2)_{n_k},
\quad
(p-2)_{n_k}=(-1)^{n_k}(n_k+1)! .
\]
除以 (1044.7) 的准确 \(a_k\)，得到
\[
\boxed{\quad
H_k(t)=
\frac{(2\sqrt{A_{\rm tail}})^{3k-2}}{3k-1}\,
 t^{4g-k}
+\text{更高 }t\text{ 次项}.
\quad}
\tag{1044.9}
\]
整个范围中
\[
n_k\le p-5,\quad n_k+2=3k-1\le p-3,\quad3k\le p-2.
\tag{1044.10}
\]
所有阶乘、\(3k-1\)、\(k!\) 和最后的 Taylor 次数都为 \(p\) 单位。
本式没有跨过一个 \(p\)-分母。

## 3. 任意实际 normal 微分的齐次表示

这一节支付原微分与参考多项式之间的接口。
不能只从一个无穷最高项就假定原微分已经有多项式 primitive。

### 3.1 真正不变的 \(\eta\)

固定一个实际 full-Dickson 分支 \(C=c_0\ne0\)。
在其仿射坐标环中，\(X,Y\) 都是单位，且
\[
dC=-Y^p\,dX+X^p\,dY=0 .
\]
因此
\[
\boxed{\quad
\eta=\frac{dX}{X^p}=\frac{dY}{Y^p},
\qquad dG=(\Theta G)\eta.
\quad}
\tag{1044.11}
\]
\(\eta\) 是这个仿射曲线的无零、无极微分。
若 \(X'=aX+bY\)、\(a,b\in\mathbf F_p\)，则
\(dX'=X'^p\eta\)，所以它在完整 \(\operatorname{GL}_2(\mathbf F_p)\)
换基下不变，连同换基所置换的全部 \(C\) 分支一起成立。

原平面闭包是
\[
X^pY-XY^p=c_0 Z^{p+1}.
\tag{1044.12}
\]
三偏导数是 \(-Y^p,X^p,-c_0Z^p\)，没有共同射影零点；
故闭包光滑，次数 \(p+1\)。
在每个无穷点，若 \(X\ne0\)，取
\(v=Z/X\)、\(u=Y/X\)。
方程给 \(u-u^p=c_0v^{p+1}\)；
\(v\) 是参数，而仿射 \(X=v^{-1}\)，于是
\[
\eta=-v^{p-2}dv.
\]
\(X=0\) 的点使用 \(Y\) 完全相同。因此
\[
\operatorname{div}(\eta)=(p-2)\sum_{\infty}[\infty].
\tag{1044.13}
\]

### 3.2 极阶界给真实 polynomial representative

从这个 full 分支到原 \(D\) 的无穷点，实际分歧指数是六。
可直接用同一个 \(x=V^6\) 核准：
full 无穷的 \(V\) 极阶为二，故 \(x\) 极阶十二；
\(D\) 上 \(x\) 的极阶是二。
所以一条 \(D\) 上极阶至多 \(km+1\) 的微分，
拉回后的极阶至多 \(6km+1\)。

若 \(\Omega_k\) 是这样的仿射正则微分，写
\(\Omega_k=f_k\eta\)。
由 (1044.13)，\(f_k\) 在每个 full 无穷点的极阶至多
\[
D_k=6km+p-1=(3k+1)(p-1).
\tag{1044.14}
\]
没有其它极点。

无穷除子正是 (1044.12) 的超平面截面。
平面 hypersurface 的标准 exact sequence
\[
0\to O_{\mathbf P^2}(D_k-p-1)
 \to O_{\mathbf P^2}(D_k)
 \to O_{\overline D_{\rm full}}(D_k)\to0
\]
及 \(H^1(\mathbf P^2,O(a))=0\) 给满射。
后一个 vanishing 亦可由三个标准仿射图的单项式 Čech 计算直接得到。
故 \(f_k\) 确有总次数 \(\le D_k\) 的 \(X,Y\) 多项式代表，
不是由最高极阶猜出的形式形状。

### 3.3 原惯性和全部分支使代表准确齐次

写原 full-\(p\) 基变换为
\(\varpi^{p^2-1}=p\)、\(\pi_0=\varpi^2\)，
并令 \(\sigma(\varpi)=\upsilon\varpi\)，
\(\upsilon\in\mu_{p^2-1}\)。
R1021 的实际归一化参数满足
\[
\sigma(X)=\upsilon^{-1}X,\qquad
\sigma(Y)=\upsilon^{-1}Y.
\tag{1044.15}
\]
这里是原 framing/inertia，不能换成另一个只同型的局部表示。
权 \(m\) 的原 Hodge 微分满足
\(\sigma\Omega=\upsilon^{p-1}\Omega\)。
故第 \((3k+1)m\) normal 层的权是
\(\upsilon^{-3k(p-1)}\)。
另一方面 (1044.11) 的 \(\eta\) 权为 \(\upsilon^{p-1}\)。
所以 \(f_k\) 的准确权是
\[
\upsilon^{-D_k}.
\tag{1044.16}
\]

固定 \(C=c_0\) 的惯性稳定子为 \(\mu_{p+1}\)。
在上节 polynomial representative 上对它平均，
只有次数 \(D_k-j(p+1)\) 的齐次项保留。
若这样的项为 \(P_{D_k-j(p+1)}\)，将它换成
\[
c_0^{-j}C^j P_{D_k-j(p+1)}.
\]
在 \(C=c_0\) 上值不变，而次数准确为 \(D_k\)。
求和即得真实齐次多项式 \(P_k\in\operatorname{Sym}^{D_k}(k^2)\)
表示 \(f_k\)。

\(\mu_{p^2-1}\) 在所有实际非零 \(C\) 分支上传递：
\(C\mapsto\upsilon^{-(p+1)}C\)，其像是
\(\mathbf F_p^\times\)，正是这些分支的比值群。
(1044.16) 与 \(P_k\) 的齐次性因此证明 **同一个** \(P_k\)
在全部分支上同时表示实际 \(f_k\)。
不是在每个分支各自选一套无关系数。
这也保留了原 tame CM 标记；它在 full 图上的作用与这些操作相容。

## 4. 完整有限角图像恰是一维

对所有 \(1\le k\le4g-1\)，有
\[
D_k\le(p-1)^2<p^2-1 .
\tag{1044.17}
\]
R1042 §4 的完整 \(C\)-过滤适用，给
\[
E(C\operatorname{Sym}^{D_k-p-1})=0 .
\]
评价 quotient \(W_0\) 的两个因子是平凡模和 Steinberg。
\(E\) 在前者为一、在后者为零（Steinberg 无 nonsplit-Cartan
固定向量），而幂等元作用 exact。因此
\[
\boxed{\quad
\dim E\operatorname{Sym}^{D_k}(k^2)=1 .
\quad}
\tag{1044.18}
\]
没有将一个非整中央幂等元用于此断言。

另一方面
\[
dH_k=(\Theta H_k)\eta,\qquad E(\Theta H_k)=\Theta H_k .
\]
其无穷最高系数是 \(-km\ne0\bmod p\)，因为 \(k<p\) 且
\(m\ne0\bmod p\)。故它是 (1044.18) 的非零生成元。

将 §3 所得齐次代表 \(P_k\) 换成 \(EP_k\)，便仍表示原
\(E\)-固定微分：\(E(P_k\eta)=(EP_k)\eta\)。
不必预先假定初选代表本身被 \(E\) 固定。
于是任何满足 §3 极阶和角色条件的实际 \(E\)-固定微分都必须是
\(dH_k\) 的唯一标量倍数。
若它的最高极阶 \(km+1\) 系数为零，这个微分就为零。
这一步也处理了全部较低极部和 holomorphic 自由项；
它们没有被事先删掉，也没有被假定有 global primitive。

R1021/R1030 的 full-\(p\) 换基在整个 \(R/(p)\) 仿射模型上为
常线性作用，固定 \(\pi_0\)，所以 \(E\) 逐 normal 层相容。
当前范围的最大 normal 次数为
\[
(3(4g-1)+1)m=(p-1)m<e_0,
\tag{1044.19}
\]
确实全部仍在这个已证明的仿射精度内。

## 5. 全部 global normal 层的归纳

定义底 Hodge 旗标
\[
\mathcal F_j=
\{L:R_L(1)=R_L'(1)=\cdots=R_L^{(j-1)}(1)=0\},
\qquad\mathcal F_0=\text{整个底空间}.
\tag{1044.20}
\]
我们逐个证明：若 \(L\in\mathcal F_{k-1}\)，
则原 \(\Omega=e_1\Omega_L\) 在 CM 尾上
\[
\Omega|_D\equiv0\pmod{\pi_0^{(3k+1)m}},
\]
且准确的当前层为
\[
\boxed{\quad
\overline{\varepsilon^{-(3k+1)}\Omega|_D}
=\frac{\kappa_1^kR_L^{(k-1)}(1)}{k!}\,dH_k .
\quad}
\tag{1044.21}
\]

\(k=1\) 的所有更早层已由 R1032 完整证明。
以下归纳并非只重复该首层的参考计算。

假设此前的断言成立，且 \(L\in\mathcal F_{k-1}\)。
每个此前的 CM 层都为零。
该尾的所有仿射微分角色是 \(3m\) 的倍数；
所以在相邻 \((3j+1)m\) 之间没有额外 normal 层。
这保证归纳所需的全部更早 CM 层都为零，而不只某个最高系数为零。

中心在 \(n<e_0\) 的可能层只有
\[
n=m+d(p+1),\qquad d\ge0 .
\tag{1044.22}
\]
因为当前 \(b=1\) 尾的更早 CM 层全零，这些中心层在这个标记
没有来自该尾的 polar input。另两个 CM 尾可能已有非零返回；
它们的既定 principal parts 完整保留，不能由 (1044.20) 删除。
这些极部在当前 \(b=1\) 标记正则。

严格消费 R1032 §3 时，先保留所有已规定的节点主部，
再提升中心自身 smooth deformation 的剩余项。
可取有效除子 \(D_{\rm aux}\)，支撑于 \(S\) 及其它已规定的极点，
避开当前 \(b=1\) 标记；非空时
\(H^1(I,\Omega_I^1(D_{\rm aux}))=0\)。
因此这种非齐次提升仍能在当前标记保持正则，
并没有声称整个中心层在另两个 CM 标记也正则。
所有真正节点 residue 仍由原 compact-type 树和 residue 定理付清。
这些事实保留中心的非齐次变形和全部 holomorphic 自由项，
不是把中心模型当成常数。

在实际厚度三的节点，中心第 \(n\) 层 regular 项
\(cw^a\,dw\) 只在 \(n+3(a+1)\) 或更高层传入。
因此当前 \((3k+1)m\) 层的极阶至多 \(km+1\)；
若 \(d\ge1\)，相应的最大 \(a+1\) 是
\[
km-\frac{d(p+1)}3=km-4gd<km,
\tag{1044.23}
\]
所以最高极部只能来自第 \(m\) 中心层。
也可直接用原 Kummer 参数核全部允许指数：
第 \(m+d(p+1)\) 层的 \(u^{-2d}db\) 在 CM 节点的指数为
\(m-1-4gd\)，乘一个 regular \(r^\ell\) 项后增加 \(\ell m\)。
其到达层准确为 \((4+3\ell)m\)，极阶为
\((\ell+1)m+1-4gd\)。
当前层对应 \(\ell=k-1\)，再次得到 (1044.23)。
这些公式只读取 regular Taylor 项；更早全层为零已经由归纳
处理，不把各个中心项的未知系数分别擅设为零。

该层准确是 \(\varepsilon R_L(b)db\)。
由于 \(L\in\mathcal F_{k-1}\)，其在 \(b=1\) 的首项是
\[
\frac{R_L^{(k-1)}(1)}{(k-1)!}
 (b-1)^{k-1}d(b-1).
\]
同一个原 quotient 的
\(b_{\rm lift}-1=\kappa_1\varepsilon^3\psi_3+\cdots\)
于是给最高 polar part
\[
\frac{\kappa_1^kR_L^{(k-1)}(1)}{k!}\,d(\psi_3^k),
\qquad \psi_3=z_D^{-m}+\text{较低极阶项}.
\tag{1044.24}
\]
\(\psi_3\) 只在该 node 使用，不被冒作全局函数。
原节点单位和更高坐标项，要么乘已为零的先前 Taylor 系数，
要么提高 normal 次数或降低当前极阶。
所以 (1044.24) 的最高系数准确，包含原 \(\kappa_1^k\)。

当前层在仿射尾仍正则；可能增加的任何 CM 全纯自由项同样满足
这个极阶界。§§3–4 于是适用于 **全部** 当前层，
迫它是 \(dH_k\) 的倍数。
用 (1044.8) 比较最高极部，标量恰为 (1044.21)。
如果 \(L\) 还属于 \(\mathcal F_k\)，该层全零，
完成下一步归纳。

特别地，当 \(k\) 增大到首次允许 CM holomorphic 自由项之后，
证明仍未把这些项删除；它们被 §4 的完整一维图像论证一起处理。

## 6. 从原 normal 层回到完整 \(w\) 系数

设 \(L\in\mathcal F_{k-1}\)。
此前的整个 CM 层已为零，所以将特殊纤维参数
\(\bar z(t)=\lambda_0t+O(t^2)\) 代入 (1044.21) 时，
其更高项不能降低 (1044.9) 的最低 Taylor 次数。
混合特征参数的更高 normal 项只乘此前的零层，
或提高当前 normal 次数。
于是最低 primitive 次数 \(4g-k\) 的准确系数乘
\(\lambda_0^{-(4g-k)}\)。

原恒等式
\[
(3k+1)m+3m(4g-k)=e_0+m
\tag{1044.25}
\]
使这一项在除去 \(p\varepsilon\) 后正好为单位尺度。
次数 \(4g-k\) 介于 \(1\) 与 \(4g-1<p\)，积分分母为单位。
R1033 的完整尾界已经包括所有其它次数，
尤其所有 \(p\) 倍次数；本篇没有从微分约化忽略 \(w^p\) 项。
同一精确惯性还保证，固定此 \(z\) 次数的更高 normal 项
相差整 \(e_0\)，所以不再改变当前模 \(p\) 系数。

由 (1044.9)、(1044.21)，
\[
[w^{4g-k}]\overline{H_\Omega}
=
\frac{\kappa_1^kR_L^{(k-1)}(1)}{k!}
 \frac{(2\sqrt{A_{\rm tail}})^{3k-2}}{3k-1}
 \lambda_0^{-(4g-k)}.
\tag{1044.26}
\]
而
\[
R_L^{(k-1)}(1)
=\frac2m(-1)^{k-1}k!
 \sum_{s\in S}\frac{L_s\theta_s}{(1-s)^{k+1}} .
\tag{1044.27}
\]
将原 Serre 配对 \(-2\) 代入，得到
(1044.4)–(1044.5) 在
\(\mathcal F_{k-1}\) 上的准确等式。
在整个底空间上，它恰等价于模前 \(k-1\) 列的同余。
所有未定的前列倍数保留。

## 7. 完整系数空间、秩和指定消去测试

### 7.1 原全型轮廓的准确核

\(J_0,\ldots,J_{4g-2}\) 线性独立。
确切地，令 \(t_s=(1-s)^{-1}\)；
这些 \(t_s\) 两两不同，且都非零。
各列在 \(e_s\) 基中的值为
\(t_s^2,t_s^3,\ldots,t_s^{4g}\)。
任取 \(4g-1\) 个不同根，相应矩阵的 determinant 是非零单位
乘 Vandermonde
\(\prod_{s<t}(t_t-t_s)\)。
因此
\[
\boxed{\quad
\langle V_1,\ldots,V_{4g-1}\rangle
=\langle J_0,\ldots,J_{4g-2}\rangle,\qquad
\dim=4g-1.
\quad}
\tag{1044.28}
\]
原全部模 \(p\) primitive 同时为零的底 Hodge 子空间恰是
\(\mathcal F_{4g-1}\)，维数
\((6g-2)-(4g-1)=2g-1\)。

这是整个实际类型块的结论。
它没有断言这个核就是旧 \(\delta=1\) 空间，
也没有将其与某个有理简单商或 MW 饱和空间混同。

### 7.2 原 \(B\)-泛函为零的完整 contact 条件

继续用 R1036/R1037 的实际双线性型
\[
B(e_s,e_t)=\frac{q_s}{2}\mathbf1_{t=s^p},
\qquad q_s=-\frac{f(s)}{A_p'(s)^2}\in\mathbf F_p,
\quad f=(1-b^3)^{8g-2}.
\]
对任意 \(k\)-系数多项式 \(c\)、\(\deg c<d\)，
令 \(T_c\) 为唯一次数 \(<d\) 的多项式，满足
\[
T_c\equiv \frac{f\,c(b^p)}{A_p'}\pmod{A_p}.
\tag{1044.29}
\]
\(c(b^p)\) 保持外部系数不变，不能换成任意 \(c^p\)。

因为 \(S\subset\mathbf F_{p^2}\) 且 \(q_{s^p}=q_s\)，
重标完整根集后，
\[
2B(c,J_i)
=-\sum_{s\in S}
 \frac{T_c(s)}{A_p'(s)(1-s)^{i+2}}.
\]
同一完整部分分式
\[
\frac{T_c(b)}{A_p(b)}
=\sum_{s\in S}\frac{T_c(s)}{A_p'(s)(b-s)}
\]
因而给准确公式
\[
\boxed{\quad
2B(c,J_i)
=\frac{(-1)^i}{(i+1)!}
 \left(\frac{T_c}{A_p}\right)^{(i+1)}(1),
\quad0\le i\le4g-2.
\quad}
\tag{1044.30}
\]
所有分母为单位，\(A_p(1)\ne0\)。

结合 (1044.28)，原 \(B(c,\overline{\mathcal H}(w))\)
这个完整多项式恒为零，当且仅当存在 \(\gamma\in k\) 使
\[
\boxed{\quad
(b-1)^{4g}\ \mid\ T_c-\gamma A_p .
\quad}
\tag{1044.31}
\]
这来自 \(1,\ldots,4g-1\) 阶导数同时为零；
\(4g<p\)，没有特征 \(p\) Taylor 的例外项。

对 R1037 的真实本原 MW 消去泛函，必须取
\[
c=D\,\overline{\mathcal Q}\,\bar v,\qquad
\bar v=(1-\overline{\mathcal Q})\lambda .
\]
(1044.31) 保留完整的 \(\overline{\mathcal Q}^2\lambda\)；
没有将它删成一个裸 rational derivative。
本篇给这个指定完整原多项式为零的准确判据，
尚未证明该指定 \(T_c\) 违反 (1044.31)。

即便该多项式不恒零，也还须控制原 \(v_p(w)>0\) 子盘上的
低系数和零点。全型的 (1044.28) 不能替代这一步，
更不能替代 O0 的全局覆盖及绝对界。

## 来源与核查范围

- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)：
  actual full-\(p\) 模型、原归一化参数和整个 \(R/(p)\) 的常线性作用。
- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md)、
  [R1030](R1030-integral-finite-corner-projector-and-original-CM-affine-action.md)：
  实际整 \(e_1=E\)、原 full 分支、\(U,V,F\) 与其准确投影。
- [R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md)：
  原 \(R_L,\theta_s,\kappa_1\)、中心 smooth deformation、
  residue 及最初的完整 CM normal 层。
- [R1033](R1033-original-rational-CM-disc-exact-lowest-type-scale-and-tail.md)：
  原 \(z,w,\lambda_0\)、\(p\varepsilon\) 尺度与包括 \(p\) 倍次数的完整尾界。
- [R1042](R1042-original-CM-disc-second-column-and-finite-corner.md)：
  完整 \(C\)-过滤、所有终端简单因子以及 \(D<p^2-1\) 的真实整投影。
- [R1036](R1036-original-integral-alternating-test-and-complete-MW-annihilation.md)、
  [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)：
  \(B,q_s\)、系数固定的 \(T_c\) 及真实 MW 泛函。

所有新恒等式来自原几何、纸面多项式、完整角色和有限格。
没有数学程序执行，也没有重复已有有限素数窗口。
