# R1039：原 p≡5 mod12 行的完整 CM normal jet 与有理盘准确尺度

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126。
o1_theta / root；双中心与 Raynaud 接口另经 global_route 讨论核对。

**已证明：R1038 的实际整最低惯性型，在原 CM 尾的第 \(4m\)
normal 层由一个明确的底 Hodge 线性泛函给出。**
本篇保留 \(p\equiv5\pmod{12}\) 的两个 Igusa 中心、两端节点、
图环路与实际 Raynaud 好约化部分，先证明所有相关环带留数严格为零，
再计算完整同阶主部。真实整有限角消去低极部，留下原最高系数。

换回同一个 \(w=(a-1)/p^3\) 后，整个类型块的原 Abel-log 与
formal map 的共同尺度准确为 \(p\varepsilon\)，约化最高次数为
\((p-2)/3\)。这不是指定简单商的 Néron 尺度定理，也不由最高系数
非零断言最低单位项或原盘唯一零点。

## 1. 原对象与准确结论

全篇保持 R1038 的原 \(X_1,J_1,c_1,D_0\)、原六标记、
\(\kappa_4\) 下降、实际幂等元 \(e_1\) 以及 Raynaud 扩张
\[
0\longrightarrow T\longrightarrow G\longrightarrow B\longrightarrow0.
\]
设
\[
p=12g+5\ge41,\qquad m=6g+2=(p-1)/2,\qquad h=m/2=3g+1,
\]
\[
e_0=m(p+1),\qquad \pi_0^{e_0}=p,\qquad
\varepsilon=\pi_0^m,\qquad \varpi^2=\pi_0.
\tag{1039.1}
\]
R1038 已构造实际好 BT 因子
\[
\mathcal G_1=e_1B[p^\infty]\simeq e_1G[p^\infty].
\]
它的特殊晶体只有最低 \(\pm m\) 两格，Hodge 纯为一格；
原权 \(m\) 整 Hodge 提升在该因子内模 \(p\) 唯一。
以下所有 Hodge 提升先取于实际 abelian scheme \(B\)，
再经饱和注入 \(\omega_B\hookrightarrow\omega_G\simeq\omega_{\mathcal J^0}\) 使用。

令 \(S=\{A_p=0\}\) 为 R1038 的全部 \(e_s=1\) 超奇异尾。
它们避开三个 CM 支持 \(b^3=1\)；\(j=1728\) 在本行 ordinary，
不属于 \(S\)。原尾及原配对为
\[
D_s:\quad Y_s^2=X_s(X_s^{2h+1}+A_s),\qquad
\omega_s=dX_s/Y_s,\qquad \langle f_s,\omega_s\rangle=-2.
\tag{1039.2}
\]
这里 \(f_s\) 是两个无穷端的同一个真实 Čech 类，不是单端归一。
底 Hodge 向量写成 \(L=\sum_sL_s\omega_s\)，定义
\[
R_L(b)=\frac2m\sum_{s\in S}\frac{L_s\theta_s}{(b-s)^2},
\qquad
\mathcal J(L)=\sum_{s\in S}\frac{L_s\theta_s}{(1-s)^2}.
\tag{1039.3}
\]
\(\theta_s\) 完全保留 R1038 的真实 quotient-Hasse 与节点尺度。

原 \(c_1\) 尾是
\[
D:\quad y^2=x(x^{2g+1}+A_{\rm tail}),\qquad
Q=(0,0),\qquad t=\sqrt{x},\qquad F=x^{2g}y.
\tag{1039.4}
\]
保留 §6 的实际 coarse/fine 单位 \(\kappa_1\)。
本篇首先证明
\[
(e_1\Omega_L)|_D\equiv0\pmod{\pi_0^{4m}},\qquad
\boxed{\quad
\overline{\varepsilon^{-4}(e_1\Omega_L)|_D}
       =\kappa_1R_L(1)\,dF .
\quad}
\tag{1039.5}
\]
除法只读取此分量的首 normal 层，不声称它给全模型整微分。

## 2. 实际好约化部分消去全部环路留数

本行的图有环路，不能使用 compact-type 树的叶端论证。
先在严格未分歧底上分裂全部节点，并将厚度二、六的节点正规细分。
Coleman–Iovita 的曲线单值化算子为
\[
N_X=\partial\operatorname{Res}.
\]
他们证明 \(N_X=N_J\)，其中 Raynaud 定义的 \(N_J\)
通过 \(H^1_{\rm dR}(T)\) 因子化。一个来自 \(\omega_B\) 的微分
在 \(T\) 上限制为零，故其 \(N_J\) 严格为零。

另一方面，所有节点的残数向量属于图的 cycle space；
\(\partial\operatorname{Res}=0\) 又将它放在 coboundary space。
这两个空间交为零：在有理数上，整数边配对正定，
或等价地图拉普拉斯只有逐连通分支的常数核；再扩标量到 \(K\)。
所以
\[
\boxed{\quad
\operatorname{Res}_e(\Omega)=0
\text{ 对每条环带 }e,\quad \Omega\in\omega_B .
\quad}
\tag{1039.6}
\]
这是泛纤维中的准确零，而不只是特殊纤维的零。
整微分的留数属于无挠底环，因而整地为零。
细分链各边的留数相同，故回到原厚度二、六节点仍成立。
原节点单位没有被改成一。

这里用到的原文是 Coleman–Iovita，Chapter I §1 的
\(N_X=\partial\operatorname{Res}\)、§2 的 Raynaud 算子、
§3 末的算子比较和图 cycle 配对。
下文的 \(\Omega_L\) 和中心自由提升 \(\Omega_I\) 都来自
\(\omega_B\)，所以 (1039.6) 在逐层 Mittag–Leffler 递推中始终有效。

## 3. 本行的真实整有限角与中心自由修正

### 3.1 整有限角确实等于实际 \(e_1\)

令
\[
\mathsf G=\operatorname{PGL}_2(\mathbf F_p),\qquad
N=N_{\rm ns}/\mathbf F_p^\times,\qquad
E=(e_{\rm triv}+e_{\theta_1})e_N.
\]
R434 §§1–3 的本原有限群整格本来对全部 \(p\equiv2\pmod3\) 有效。
因此 R1030 §2 的完整系数证明给
\[
E\in e_N\mathbf Z_p[\mathsf G]e_N,\qquad E^2=E.
\tag{1039.7}
\]
本行新增的 quadratic principal-series 和 quadratic Steinberg
必须保留在 canonical spectrum 中；它们既不是 trivial，也不是
\(\theta_1\)，所以 \(E\) 在其上为零。trivial holomorphic 部分
仍因 \(S_2(H_6)=0\) 消失。因此在原 generic Hodge 空间，
\(E\) 与 R1038 的 \(e_1\) 相同。
特征零微分实现的忠实性及整格无挠给原整作用上的
\[
E=e_1.
\tag{1039.8}
\]
full-\(p\) 模 \(p\) 常线性作用、全部配对分支及逐 normal 层相容性，
使用 R1021 的真实仿射模型；不固定一条分支后冒充完整 \(E\)。

### 3.2 两个中心中的实际自由方向

原两个中心各是同一 Igusa 曲线的 \(C_4\) 商。
在原 Hasse 标架中写
\[
u^h=h_p(b),\qquad
h_p=(1-b^3)^{2g+1}A_p(b),\qquad u=\mathfrak a^4,
\tag{1039.9}
\]
其中 \(\mathfrak a\) 是原 Igusa Hasse 根。
若各中心标架的常数单位不同，保留于以下首系数与节点单位中；
零极阶与角色不变。

在 \(A_p\) 的简单根处，\(u\) 的阶为一、\(db\) 的阶为 \(h-1\)；
在 \(b^3=1\) 处，两者的阶分别为 \(2g+1\)、\(h-1=3g\)；
在无穷远 \(u\) 极阶为四。因此该 \(u^{-1}\) 角色的全部
holomorphic 空间恰为
\[
\left\langle1,b,b^2\right\rangle\,db/u.
\tag{1039.10}
\]
其中 \(db/u\) 在原 \(b=1\) 标记有准确阶 \(g-1\)，首系数为单位。
此分类同时排除了其它有限点的分母：任何这样的分母都会产生极点；
无穷远则迫多项式次数至多二。

完整惯性的偶次子群固定每个中心；若
\(\sigma(\pi_0)=\xi\pi_0\)，则其平方在 \(u\) 上为
\(\xi^{2(p+1)}\)。两中心并上的 (1039.10) 分成两个完整惯性扩张，
其中有权
\[
w_I=e_0-(p+1)
\]
的一支。选该支中在 \(b=1\) 首系数非零的向量，并在实际
\(\omega_B\) 中提升、tame 平均，得整 \(\Omega_I\)。
这里没有把交换中心的 \(\sigma\) 写成单一中心上的标量。
原 deck 满足 \(\delta(b)=\zeta^2b,\ \delta(u)=\zeta^2u\)，
所以 \(db/u\) 的 deck 角色为一。

置
\[
\Delta\Omega=\pi_0^{3m+2}\Omega_I .
\]
它的完整权为 \(m\)，早于 \(3m+2\) 的层全零。
中心首 regular 阶 \(g-1\) 经原厚度六节点传入 CM 尾的层为
\[
(3m+2)+6g=4m.
\]
该层非零 polar 首阶为 \(g+1\)。
置 \(\nu=x^{2g}dx/y\)；它在两无穷端的首部分别为
\(\mp z^{-g-1}dz,\ z=1/x\)。
完整惯性交换两端，迫传入项有这同一对符号；该角色没有
holomorphic 自由项。因此 \(\Delta\Omega\) 在此尾的首 normal
层为某个非零原单位乘 \(\nu\)。

还须在所有配对分支同时运输。取原
\[
c=A_0^{p+1}-B_0^{p+1},\quad
U=(A_0^{p+1}+B_0^{p+1})/2,\quad V=A_0B_0,
\]
\[
A_{\rm tail}=c^2/4,\qquad x=V^6,\qquad y=UV^3 .
\]
norm 为 \(d\) 的 Cartan 元使
\[
c\mapsto dc,\quad U\mapsto dU,\quad V\mapsto dV,\quad
\nu\mapsto d^{p-3}\nu=d^{-2}\nu,\quad
A_{\rm tail}\mapsto d^2A_{\rm tail}.
\]
由完整 \(N\)-不变性及分支的单一 norm 轨道，上述首层恰为
\(\kappa A_{\rm tail}\nu,\ \kappa\ne0\)。
另一方面 \(e_1\Delta\Omega\in p\,e_1\omega\)：
同权 \(m\) 的实际最低型提升模 \(p\) 唯一，而 \(\Delta\Omega\)
特殊纤维为零。因 \(4m<e_0\)，(1039.7)–(1039.8) 的逐层作用给
\[
\boxed{E(A_{\rm tail}\nu)=0.}
\tag{1039.11}
\]
没有将随分支变化的 \(A_{\rm tail}\) 从 \(E\) 中提出。

### 3.3 最高多项式由同一角投影固定

仍有真实齐次多项式
\[
F=UV^{p-2}
=\frac{A_0^{2p-1}B_0^{p-2}+A_0^{p-2}B_0^{2p-1}}2
=x^{2g}y .
\]
在 \(\operatorname{Sym}^{3p-3}(k^2)\) 中，完整 \(N\)-固定线恰为
\(kF\)：Cartan 固定的两个指数是 \(p-2,2p-1\)，normalizer 交换它们。
对每个非零 \((\alpha,\beta)\in\mathbf F_p^2\)，有
\(A_0^p=B_0\)、\(F=(A_0B_0)^{p-1}=1\)。
所以 evaluation functional 的总和为 \(p^2-1=-1\)。
\(E\) 的 augmentation 为一，遂得到
\[
EF=F,\qquad E(dF)=dF.
\tag{1039.12}
\]
这是完整有限域恒等式，未执行求和或试算。
记 \(\mu=x^{4g+1}dx/y\)，直接微分同时给
\[
dF=(3g+1)\mu+\frac{4g+1}{2}A_{\rm tail}\nu
   =-\frac14\mu-\frac13A_{\rm tail}\nu\quad\text{于 }k.
\tag{1039.13}
\]

## 4. 两个中心第 \(m\) 层的完整系数

在 \(D_s\) 两无穷端取 \(z_s=1/X_s\)，则
\[
Y_s=\pm z_s^{-h-1}S_s,\qquad
S_s^2=1+A_sz_s^{2h+1},\qquad S_s(0)=1.
\]
R1038 的同一真实 quotient 给
\[
b_{{\rm lift},\pm}-s=\varepsilon\theta_s\psi_{s,\pm}
                         +\text{更高层},
\qquad
\psi_{s,\pm}=\pm z_s^{-h}S_s^{-1}
                         +\text{regular 项}.
\tag{1039.14}
\]
两个 exact germs 可分别取原 \(\beta^{p-1},\alpha^{p-1}\)；
此处只读其所需主部。对应
\(\omega_s\) 的首项为 \(\mp z_s^{h-1}dz_s\)。

把中心微分 \(\varepsilon a(b-s)^{-2}db\) 拉回 plus 端，
得到 \(-ah\,z_s^{h-1}dz_s/\theta_s\)；minus 端同时反号。
因此两中心准确为同一系数
\[
a=\frac{L_s\theta_s}{h}=\frac{2L_s\theta_s}{m}.
\]
第 \(m\) 中心层的完整惯性角色为零，下降到双中心并的
\(\mathbf P^1_b\) 商。其所有极点在 \(S\)，上述 double poles
已确定；§2 消去全部 simple residues，三个 CM 标记及无穷远正则。
两种表达的差是 \(\mathbf P^1\) 上全纯微分，因而为零。故
\[
\boxed{\quad
\text{两个中心的完整第 \(m\) 层都是 }\varepsilon R_L(b)\,db.
\quad}
\tag{1039.15}
\]
在无穷远 \(R_Ldb=O(b^{-2})db\)，也直接符合所需正则性。

## 5. 全部早于第 \(4m\) 的 CM 层为零

在原节点 \(zw=\rho\pi_0^e,\ \rho\in R^\times\)，
邻分量第 \(n\) 层的 regular 项 \(cw^k\,dw,\ k\ge0\)，
给本分量的 polar 项
\[
-c\,\bar\rho^{\,k+1}
 \pi_0^{n+e(k+1)}z^{-k-2}\,dz .
\tag{1039.16}
\]
新 polar part 只来自更低层的邻分量 regular part。
高阶坐标或单位修正只提高 normal 次数或降低已经确定的首极阶；
\(\rho\) 保留。

两个中心自身的 smooth deformation 也要保留。
分别选足够大的 \(D_S\)，只支撑 \(S\) 的标记，则
\[
H^1(I_\pm,\Omega^1(D_S))
 \simeq H^0(I_\pm,O(-D_S))^\vee=0.
\]
逐阶 meromorphic 提升可始终在 CM 标记正则，并再 tame 平均；
所有 holomorphic 自由项仍保留。principal-parts 的可解条件
由 §2 的真实全阶零 residue 支付，不由上述消失式代替。
CM 仿射范围则使用 R1021 到整个 \(R/(p)\) 的原模型。

中心权为 \(p+1\) 的倍数，所以权 \(m\) 的提升在
\(0<n\le4m\) 中只可能有
\[
n=m,\qquad n=3m+2.
\tag{1039.17}
\]
CM holomorphic 权为 \(3m(2j+1),0\le j<g\)；
若作为第 \(n\) 层自由项出现，要求
\(n+3m(2j+1)\equiv m\bmod e_0\)。
最小可能正 \(n\) 至少为 \((6g+8)m>4m\)，所以本范围没有这种自由项。

第一中心层 (1039.15) 在 CM 标记正则。
\(b-1\) 的中心阶为 \(h\)，原节点厚度六，故首次传入
\[
m+6h=4m.
\]
若更早 CM 层全零，第二中心层 \(3m+2\) 在该节点无 incoming polar；
中心自身变形也可保持此处正则。其角色为 \(-(p+1)\)，
即 (1039.10) 的 \(u^{-1}\) 角色，迫 regular 阶至少 \(g-1\)。
因此首次传入仍为
\[
(3m+2)+6g=4m.
\]
最早非零层反证即给第 \(4m\) 层以前全部 CM normal 层为零。
第 \(4m\) 层的两个输入极阶分别至多 \(3g+2\)、\(g+1\)。

## 6. 原 quotient 决定最高极部，而非参考式归一

必须继续使用 R1038 的原 trace-zero ordinary quotient。
R1021 的真实 target fine 参数以及原 coarse \(b-1\) 的三次零给
一个原单位 \(\kappa_1\)，使
\[
b_{{\rm lift},\pm}-1
 =\kappa_1\varepsilon^3\psi_{3,\pm}+\text{更高层},
\]
\[
\psi_{3,\pm}
 =\pm z^{-3g-1}
        (1+A_{\rm tail}z^{2g+1})^{-3/2}
          +\text{所需精度之外的项},\qquad z=1/x.
\tag{1039.18}
\]
全部所用有限 binomial 截断次数小于 \(p\)。
本式没有在特征 \(p\) 中任意定义无限分数幂。
原交换两 ordinary charts 的惯性使 \(\varepsilon\mapsto-\varepsilon\)，
同时交换两个 exact germs 并给其相反首符号；
所以两端使用同一个 \(\kappa_1\)。节点、fine/coarse 和 target
generator 的全部单位都包含其中，未被设成一。

(1039.15) 在第 \(4m\) 层的最高项遂为
\[
\kappa_1R_L(1)d\psi_{3,\pm}.
\tag{1039.19}
\]
完整负主部可额外核对为
\[
\psi_{3,\pm}
 =\pm\left(z^{-3g-1}-\frac32A_{\rm tail}z^{-g}\right)
       +\text{regular},
\]
\[
F=\pm\left(z^{-3g-1}+\frac12A_{\rm tail}z^{-g}\right)
       +\text{regular},\qquad
\nu=\mp z^{-g-1}dz+\text{regular}.
\]
因此参考 \(d\psi_3\) 的第二类延拓是
\(dF-2gA_{\rm tail}\nu\)。
它只校验原最高极部；第二中心层及 smooth deformation 的全部
返回仍可能改变 \(\nu\) 的系数，不能删去。

## 7. 完整角色空间、真实投影与原 marked jet

第 \(4m\) 层的角色为 \(-3m\)，只在两个无穷远有极，
极阶至多 \(3g+2\)。全部 affine regular 微分分为
\(x^jdx/y\) 与 \(x^jdx\)。后一类角色是偶数倍 \(3m\)，
不可能等于 \(-3m\)。前一类要求
\[
j\equiv-1\bmod(2g+1),\qquad 0\le j\le4g+1.
\]
所以完整所需空间恰为
\[
\langle\mu,\nu\rangle=\langle dF,\nu\rangle.
\tag{1039.20}
\]
最高系数 (1039.19) 因而准确确定原层为
\[
\kappa_1R_L(1)dF+b_LA_{\rm tail}\nu
\tag{1039.21}
\]
于全部配对分支上；\(b_L\) 保留所有同阶反馈。
应用 (1039.11)–(1039.12) 的真实 \(E=e_1\)，证明 (1039.5)。

在原 \(Q\) 点，
\[
F=t^{4g+1}\sqrt{A_{\rm tail}+t^{4g+2}},
\]
所以原准确首项为
\[
\overline{\varepsilon^{-4}(e_1\Omega_L)|_D}
=\frac{2\kappa_1}{m}\mathcal J(L)
  \left((4g+1)\sqrt{A_{\rm tail}}\,t^{4g}
                         +O(t^{8g+2})\right)dt .
\tag{1039.22}
\]
这里 \(n_0=4g+1=(p-2)/3<p\)，故积分分母为单位。
使用同一个 \(\langle f_s,\omega_s\rangle=-2\)，该 Abel-log
系数向量为
\[
\boxed{\quad
-\frac{\kappa_1\sqrt{A_{\rm tail}}}{m}
   \varepsilon^4
      \sum_{s\in S}\frac{\theta_s}{(1-s)^2}f_s .
\quad}
\tag{1039.23}
\]
这是与 R1038 完整首 log 在同一个实际整格中的列。
\(\mathcal J(L)\) 可以为零；本篇不声称每一个底向量都给单位 jet。

## 8. 换回原有理 \(w\) 盘，保全部积分分母

R378 §§2–4 的几何参数对本行有效：
\[
z=\frac{a-1}{\varpi^{3p(p-1)}},\qquad
w=\frac{a-1}{p^3},\qquad z=\varepsilon^3w,\qquad
\sigma z=\xi^{3m}z .
\tag{1039.24}
\]
这是整形式完成 \(R[[z]]\) 上的准确恒等式。
原 Dickson 一次项及 tame 三次商给
\[
\lambda_0=(d\bar z/dt)_Q\in k^\times .
\]
不使用 R378 已撤回的 CM 秩零商身份。

对实际最低型的整权 \(m\) 微分写
\[
\Omega=\sum_{n\ge1}a_nz^{n-1}dz.
\]
(1039.5) 给所有 \(a_n\in\pi_0^{4m}R\)，而
\[
a_{n_0}\equiv
\varepsilon^4\kappa_1R_L(1)n_0\sqrt{A_{\rm tail}}
                   \lambda_0^{-n_0}
          \pmod{\pi_0^{4m+1}}.
\tag{1039.25}
\]
令 \(r_n\) 为 \(m-3mn\bmod e_0\) 的最小非负代表。
完整惯性给 \(a_n=\pi_0^{r_n}c_n,\ c_n\in W(k)\)。
代入 (1039.24) 得
\[
\varepsilon^{-1}\Omega
 =\sum_{n\ge1}p^{d_n}c_nw^{n-1}dw,\qquad
d_n=\left\lceil\frac{3n-1}{p+1}\right\rceil .
\tag{1039.26}
\]
原以 \(c_1\) 为零常数的 primitive
\[
H_\Omega(w)=\frac1{p\varepsilon}\int_{c_1}^{P(w)}\Omega
\]
于是满足
\[
v_p([w^n]H_\Omega)\ge d_n-1-v_p(n).
\tag{1039.27}
\]

对 \(1\le n\le n_0\)，有 \(d_n=1\) 且 \(n\) 为单位。
特殊次数 \(n=n_0+1=4g+2=(p+1)/3\) 仍有 \(d_n=1,r_n=m\)，
但真实 normal 下界 \(a_n\in\pi_0^{4m}R\) 迫同角色改进为
\(a_n\in\pi_0^{e_0+m}R\)，所以此项额外含一个 \(p\)。
若 \(n\ge n_0+2\) 且 \(p\nmid n\)，则 \(d_n\ge2\)。
若 \(r=v_p(n)\ge1\)，则 \(n\ge p^r\)，而
\[
3p^r-1>(r+1)(p+1)\qquad(p>3,r\ge1),
\]
故 \(d_n\ge r+2\)。这包括所有 \(p\) 倍积分次数。
下界随 \(n\) 趋向无穷，得到完整 Tate 收敛及
\[
H_\Omega\in W(k)\langle w\rangle,\qquad
\deg\overline{H_\Omega}\le n_0.
\tag{1039.28}
\]
没有把 \(O(\pi_0)\) 当成 \(O(p)\)；整数赋值来自 (1039.26)。

由 \(4m+3mn_0=e_0+m\)，最高系数准确为
\[
\boxed{\quad
[w^{n_0}]\overline{H_\Omega}
 =\frac{2\kappa_1\sqrt{A_{\rm tail}}}{m}
       \lambda_0^{-n_0}
        \sum_{s\in S}\frac{L_s\theta_s}{(1-s)^2}.
\quad}
\tag{1039.29}
\]
\(S\) 非空且每个 \(\theta_s/(1-s)^2\) 为单位，所以此泛函在
整个底 Hodge 空间非零。
整个实际类型块的最高约化次数恰为 \(n_0\)，
其 \(\varepsilon^{-1}\) 归一 Abel-log 的共同 \(p\) 系数尺度准确为
\[
M=1.
\tag{1039.30}
\]

## 9. 原 formal map 与 log 具有同一轮廓

原点差 \(P(w)-c_1\) 在此小盘中落于 \(\mathcal J\) 的形式零邻域；
经形式 Raynaud 同构进入 \(\widehat G\)，投到 \(\widehat B\)，
再作用真正 \(e_1\)，得到实际 \(\widehat{\mathcal G}_1\) 中的点。
这里不对 prime-to-\(p\) 挠点定义 \(e_1\)。

取该形式因子的整参数 \(Y_i\)，其零截面一次项与整 Hodge 基相配。
完整 tame 平均使 \(\sigma Y_i=\xi^mY_i\) 为形式环的准确等式。
同一角色预算、拉回的零常数项与整性给
\[
\varepsilon^{-1}Y_i(P(w))\in pW(k)\langle w\rangle .
\]
整形式群的不变微分经径向积分，log 总次数 \(d\) 项仅需分母 \(d\)。
因此对 \(d\ge2\)，除去 \(p\varepsilon\) 后非线性项赋值至少
\[
(d-1)\left(1+\frac1{p+1}\right)-v_p(d)>1.
\]
界随 \(d\) 趋向无穷，故
\[
\frac{\log_i(P(w))-Y_i(P(w))}{p\varepsilon}
                     \in pR\langle w\rangle .
\tag{1039.31}
\]
实际 formal map 与 (1039.28) 的积分具有同一模 \(p\) 轮廓，
所以整个类型块的 formal map 也具有准确共同尺度 (1039.30)。

## 10. 实际后继范围

本篇闭合原 p5 行的完整首 CM normal 泛函、
原有理盘无限尾界和整个实际最低型的 \(M=1\)。
更高 normal 层的低 Taylor 系数没有被最高系数取代。
原最低非零 \(w\) 系数、真实 MW 饱和消去后的单位值、
指定有理简单商的相对 Néron 格以及 O0 的全局覆盖，
仍须继续证明；不据 (1039.29) 宣称原深盘只有中心零点。

R378 已登记的实际候选深度与有限尾证书，
可按本篇已经支付的 \(k_i=1,M=1\) 消费，不重跑旧窗口。

## 来源与审核

- [R1038：实际 p5 Raynaud、整最低型与完整首 log](R1038-original-p5-Raynaud-lowest-type-and-complete-first-log.md)：两个中心、厚度二/六、原 \(\theta_s,f_s\)、真正 \(e_1\) 和纯 Hodge 格。
- [R434](R434-primitive-cartan-trace-and-scalar-invariant-cm-logarithm.md) §§1–3：所有 \(p\equiv2\pmod3\) 的独立有限群整格；不恢复已撤回的旧全局商身份。
- [R1030](R1030-integral-finite-corner-projector-and-original-CM-affine-action.md)：整角的系数公式、全分支 evaluation 与 norm 运输。本篇另支付 p5 的新谱和中心自由方向。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)：原 full-\(p\) 仿射模型到 \(R/(p)\)、常线性 level 作用和真实 target fine 参数。
- [R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md)、[R1033](R1033-original-rational-CM-disc-exact-lowest-type-scale-and-tail.md)：此前 p11 行的方法；本篇重新支付双中心、双无穷、图留数和厚度六输入。
- [R378](R378-actual-cm-disc-parameter-and-uniform-integral-tail.md) §§2–4：原 Dickson 整参数与有理盘；只用其更正后保留的几何。
- R. Coleman–A. Iovita, *The Frobenius and monodromy operators for curves and abelian varieties*, [作者预印本](https://arxiv.org/pdf/math/9701229)，Chapter I §§1–3：曲线残数算子、Raynaud 单值化、两者相容及图 cycle 配对。
- Edixhoven–Parent, [2021 原文](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)，Theorems 3.3、3.5；原 p5 模型和惯性由 R1038 已逐项对齐。

o1_theta 给出本行完整纸面证明；root 独核图留数门、
双节点来源及原整格接口。没有执行数学程序或重扫旧窗口。
Serre 主目标仍 OPEN。
