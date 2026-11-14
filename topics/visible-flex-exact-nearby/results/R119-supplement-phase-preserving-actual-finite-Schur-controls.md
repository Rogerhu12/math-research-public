# R119 续篇：保持真实两相位的内部位移与有限 Schur 共振控制

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇给当前强首剪切尾的两个真实局部度量控制。
第一项平移同一个下降 log-ramp，准确保持零标签主旋转和完整首密度相位，
并把真实两端 Robin Wronskian 化成一个明确的三角多项式。
第二项处理前一种控制不能处理的纯旋转/透明共振：在原下降坡未占用的
固定子区间内，构造一个 compact 度量方向；通过已有两个 bump 的实际逆，
可以准确保持同样两个相位，而给该共振非零的一阶 Wronskian 变化。

这些是实际新候选的局部控制，不是将一个背景的固定边界换成任意方便的边界。
全文指出什么时候两侧数据确实固定，保留完整 ordinary/weak/mean 源。
有限窗非恒零及有限窗正距离并未被提升成所有移动窗口的统一下界。
原全标签图、外有限 connector、第四允许线以及整个 nonlinear
\(\mathcal F_c=0\) 仍须按最终选定候选重新实例化。

## 1. 固定的真实下降坡、端口与允许新参数

采用
[强首剪切实际几何](R119-supplement-stronger-deep-first-shear-and-complete-local-map.md)
和第50束的同一径向 \(\Gamma^0\)。
物理材料坐标是 \(t=\log r\)，原 \(y=\sqrt{12}\,t\)。
同一胞元有
\[
 \delta_j=(2/25)2^{-j},\qquad
 \eta_j=\delta_j^{3/2}/(4\sqrt2).
\]
四个过渡在 \(y\) 中各长 \(\eta_j\)，三个中间常平台各长
\(\delta_j\)，两个端平台各长 \(\eta_j\)。
只允许从 \(j\ge8193\) 起加入下述新控制，前面的全部有限前缀保持。

每个内部负分量含唯一一条下降坡，写其 \(t\) 长度为
\[
                  a_j=\eta_j/\sqrt{12}.
\]
两边均有 \(Q=-A=7\) 常平台。第二条下降坡较短一侧至少有一个完整
端平台，故可在坡两侧各取长 \(a_j/4\) 的缓冲。
记这两个缓冲外缘为固定 \(t=a,b\)，其中间窗口长 \(3a_j/2\)。
它位于严格负区；两个真正转向根、全部上升坡和正型分量均在窗口之外。

径向 raw Jacobi 方程，含四重模 \(m\in4\mathbb Z\)，是
\[
 (\mu h_m')'+m^2\mu Qh_m
       =f_m-(F_m^t)'-imF_m^\theta,\qquad
 \mu={w\over a_{\rm phys}},\quad(\log\mu)'=-1-Q.             \tag{P.1}
\]
prime 在本篇表示 \(t\) 导数。physical 高度是原 raw \(h\)；
与固定 ambient height 的负号仍按原整体合同统一，不在本篇更换。

齐次密度高度 \(u=\sqrt\mu\,h\) 满足准确方程
\[
 u''+\left(m^2Q+\frac12Q'
                      -\frac14(1+Q)^2\right)u=0.          \tag{P.2}
\]
对 \(m\ne0\) 置
\[
 k_m=\sqrt{7m^2-16}>0,\qquad
 Y_m=(\sqrt{k_m}u,\ u'/\sqrt{k_m})^T.                     \tag{P.3}
\]
这只是两侧常平台中的共同 wave 单位。
在 \((u,u')\) 以及 \(Y_m\) 中 Wronskian 相同，因为转换 determinant为1。

## 2. 整坡平移：端值、两相位和准确共轭

在上述固定窗口，把整条下降坡及其中已有两个 bump 同时平移 \(\ell\)，
两侧对应增加和减少等长 \(Q=7\) 平台：
\[
                  |\ell|<L_j:=a_j/16.                   \tag{P.4}
\]
这是一个实际的 \(p_\ell(t)\)；两端仍为原高、低平台值。
其中
\[
 Q_\ell(t)=Q_0(t-\ell)
\]
在移动坡上，窗口其余部分为7。平台端的二阶 log jets仍为0。
\(\mu_\ell\) 由实际
\[
 \mu_\ell(t)=\hbox{原固定因子}\ e^{-8t}p_\ell(t)
\]
定义；在对应移动坡点有
\[
             \mu_\ell(t)=e^{-8\ell}\mu_0(t-\ell).         \tag{P.5}
\]
但是在两个**固定**缓冲外缘及整个窗口之外，
\(p_\ell,\mu_\ell\) 及所需端 jets 与原值准确相同。
不能漏掉 (P.5) 的因子，也不能把移动点与固定端口混同。

设 \(S=\int_{I_-}\sqrt Q\,dt\) 是原负分量的真实光学积分；
主旋转 \(\omega\) 使用原固定倍数和方向约定。
真实首密度相位为第49束的
\[
 \beta=-\frac14\operatorname{FP}\int_{I_-}\kappa\,dt,\quad
 \kappa={Q'\over2\sqrt Q}
 -{(1+Q)^2\over4\sqrt Q}
 +{5Q'^2\over16Q^{5/2}}-{Q''\over4Q^{3/2}}.                \tag{P.6}
\]
两个 root collars和有限部减项完全不变。
窗口内的整个非constant profile及其导数只平移，
左右补删的是同一个 \(Q=7\) 常数。故对每个允许 \(\ell\)，准确有
\[
                    S(\ell)=S(0),\qquad
                    \beta(\ell)=\beta(0).               \tag{P.7}
\]
这是完整 density potential 的等式，不只保持 principal action。
它不声称非径向标签背景下的两相位自动保持；那仍要消费实际两参数选择。

令
\[
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 R(\theta)=e^{\theta J}.
\]
在常平台中 (P.2) 准确是 \(u''+k_m^2u=0\)，所以 (P.3) 的传播为
\(R(k_m s)\)。若 \(C_m(0)\) 是从固定 \(a\) 到固定 \(b\) 的完整
齐次矩阵，则
\[
 \boxed{\quad C_m(\ell)
       =R(-k_m\ell)\,C_m(0)\,R(k_m\ell).\quad}             \tag{P.8}
\]
证明是原有序乘积
\(R(k_m(a_j/4-\ell))\,C_{D,m}\,R(k_m(a_j/4+\ell))\)，
其中整下降坡在 (P.2) 的系数仅被平移，
\(C_{D,m}\) 不随 \(\ell\) 改变。右根方向或其它固定片不能在此乘积中丢掉；
它们在第3节准确搬到两侧数据。

(P.5) 保证固定 \(a,b\) 的 physical 端口恢复矩阵也是固定的：
\[
 h={u\over\sqrt\mu},\qquad
 p_{\rm bare}=\sqrt\mu\,(u'+4u).                           \tag{P.9}
\]
因此 (P.8) 是同一真实两迹之间的共轭；不是任意改变端口 norm。

## 3. 真两侧 Robin 行与完整三角分母

在窗口左、右给实际固定的实 Robin 线。
将窗口外的固定真实 Cauchy 片精确搬回 \(a,b\)，再在 (P.3) 中归一化为
两个实单位列 \(l_m,r_m\)。写
\([v,w]=v_1w_2-v_2w_1\)。真实分母就是
\[
                         \Delta_m(\ell)=[r_m,C_m(\ell)l_m].
                                                               \tag{P.10}
\]
这适用于以下两种明确合同。

* 全部窗口外度量和外端边界保持时，真正深端允许线和外端regular线
  都独立于该局部 \(\ell\)，所以 (P.10) 是该全两端问题的分母。
* 在无限网络的局部负分量 Schur 中，消费两侧**实际正型双端 DN 的
  对角行**。两条正型区与其根 germs完全未变，因此其两个实 Robin
  行固定。正型 DN 的 off-diagonal、ordinary/weak affine contact
  全部保留为相邻输入及源，绝不设为0。此时 (P.10) 是这个明确的
  局部 diagonal Schur 的分母。

若随后根据整个新尾重新停止第四 connector或重新选择外 \(t_0\)，
其传回来的全局右线一般会改变。不能继续把那个新全局问题的
\(r_m\) 当作固定数据使用 (P.10)；必须另加它的完整参数导数。
第二种局部 DN 合同不受这个问题影响。

把真正 \(C_m(0)\in SL(2,\mathbb R)\) 唯一写成
\[
 C=aI+bJ+cS+dT,\quad
 S=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
 T=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
则
\[
 a^2+b^2-c^2-d^2=1,\quad
 \varrho_m=\sqrt{c^2+d^2},\quad
 \sigma_m=\|C\|_2=\sqrt{1+\varrho_m^2}+\varrho_m.           \tag{P.11}
\]
完整 conjugation 给
\[
 \boxed{\quad
 \Delta_m(\ell)=A_m+B_m\cos(2k_m\ell)
                          +D_m\sin(2k_m\ell),\quad
 B_m^2+D_m^2=\varrho_m^2.
 \quad}                                                   \tag{P.12}
\]
这里
\(A_m=a[r,l]+b[r,Jl]\)；
\(B_m=c[r,Sl]+d[r,Tl]\)，
\(D_m=-d[r,Sl]+c[r,Tl]\)。
最后的等式使用 \(Sl,Tl\) 是同长正交列，因而对任意真实单位 \(l,r\)
都成立，不假定它们是 Dirichlet 线。

## 4. 反射非零分支的明确排除及完整源逆

对任意实 \(A\)、\(\varrho>0\)、\(0<\tau\le1\)，每个完整周期中
\(\{|A+\varrho\cos x|<\tau\varrho\}\) 的长度至多 \(4\pi\sqrt\tau\)。
可在两个单调半周应用
\(1-\cos x\ge2x^2/\pi^2\)，并在端点切分证明。
把长度 \(4k_mL_j\) 的实际区间盖上整周期，得到
\[
 {\big|\{\ell\in(-L_j,L_j):|\Delta_m(\ell)|<\epsilon\sigma_m\}\big|
        \over 2L_j}
 \le16\left(1+\frac1{k_mL_j}\right)
                  \sqrt{\epsilon\sigma_m/\varrho_m}.      \tag{P.13}
\]
若右侧大于1仍是合法上界。

因为
\[
 \frac{\varrho_m}{\sigma_m}
       \ge\frac{\min(\varrho_m,1)}3,
\]
给任意 \(0<u<1\)，选
\[
 \epsilon_{j,m}=2^{-16}u^2\min(\varrho_m,1)
               \left(\frac{k_mL_j}{1+k_mL_j}\right)^2      \tag{P.14}
\]
便使该坏集比例小于 \(u/8\)。
于是每个真正反射非零的模都有严格正的、实际可读的分母下界；
其大小仍包含真实 \(\varrho_m\)，不能无根据地删去它。

可以同时选所有层与所有这类模。对第 \(j\) 层、\(m=4n>0\)，取
\(u_{j,n}=2^{-10}(j-8192)^{-2}n^{-2}\)；
每层至多两个下降坡，且 \(\sum_{n\ge1}n^{-2}<2\)。
实际乘积测度中全部坏集的总测度小于 \(1/128\)。
这使用每个坐标的条件估计：相邻全部源列保留，而本节固定的两侧行
不依赖该坐标。负频率由实共轭取得。
本句只同时选择反射非零的那些模；纯旋转模在下一节处理。

完整有源方程写成
\[
 Y(b)=C_m(\ell)Y(a)+g_m,\qquad
 g_m=\int_a^b U_m^\ell(b,s)\mathcal J_m^\ell(s)\,ds.
\]
若两边实际 affine 行为
\([l,Y(a)]=g_L,\ [r,Y(b)]=g_R\)，则准确解是
\[
 Y(a)=z l-g_LJl,\qquad
 z={g_R+g_L[r,C_m(\ell)Jl]-[r,g_m]\over\Delta_m(\ell)}.
                                                               \tag{P.15}
\]
两个端点行和整个 \(g_m\) 都参与，没有反解正型 tiny transmission。

下述 source 单位下，整个窗口的双向 Cauchy 可安全取
\[
             K_j=2^{6000}(j+5)^8\delta_j^{-16}.            \tag{P.16}
\]
这不是新数值假定：原参考全频 theorem只用 \(Q\) 单峰、实际
\(Q,Q',Q''\)、长度和 \(\mu\) 比；平移没有改变这些门。
从其原密度平衡到固定 (P.3) 的两侧转换，使用 \(Q\ge7\)、
\(k_m/|m|\in(2,3)\) 和
\(\omega_m\le2^8(j+5)\delta_j^{-1}\)，
各次可付 \(2^{20}(j+5)\delta_j^{-1}\)。
这落在 (P.16)，并同时保留 source 原两分量。
故若 \(|\Delta_m|\ge\epsilon\sigma_m\)，则 (P.15) 给
\[
 \sup_{a\le t\le b}|Y(t)|
 \le4K_j^2\epsilon^{-1}
       \bigl(|g_L|+|g_R|+\|\mathcal J_m^\ell\|_{L^1_t}\bigr).
                                                               \tag{P.17}
\]
这里尚未把 (P.17) 的实际 \(\epsilon_{j,m}^{-1}\) 在移动窗口中统一求和。

## 5. 纯旋转共振为何还需要另一控制

若 \(\varrho_m=0\)，那么 \(C=aI+bJ\) 是真实旋转，
(P.8) 完全不改变它。此时 (P.12) 退化为常数；
它可以等于0，不能用“平移非零”或零标签主相位代替证明。
若 \(\varrho_m\) 很小，(P.14) 也真实变小。
下面用原方程证明一个保持两相位的独立方向，
不以纯旋转情形在数值上“通常不发生”作为依据。

## 6. 原下降坡上的两个相位变分核

在下降坡标准坐标 \(x\) 中取未被已有两 bump 占用的开区间
\[
                 J_x=(7/16,15/32).
\]
原两个支集为 \([1/4,3/8]\)、\([3/16,7/32]\)，故在此
\[
 Q(t)=7+\mathcal B S'(x(t)),\qquad
 \mathcal B=\sqrt{12}\Delta/\eta_j,\qquad
 S'(x)=30x^2(1-x)^2                                      \tag{P.18}
\]
是真正非constant四次多项式。线性 \(x(t)\) 的方向按该下降坡的
原向外坐标固定；在这个子区间 \(Q'\ne0\)。
有 \(S'>7/4\)、\(S''>7/8\)，因此它离峰顶、转向根和原接缝都有正距离。

令 \(\psi\) 是支集在 \(J_x\) 内的实 \(C^5\) 函数。
取真实 profile
\[
                  p_\varepsilon=p_0 e^{\varepsilon\psi},
 \quad \mu_\varepsilon=\mu_0e^{\varepsilon\psi},
 \quad Q_\varepsilon=Q_0-\varepsilon\psi'.                \tag{P.19}
\]
prime仍是 \(t\) 导数，不能漏掉 \(dx/dt\)。
平台端值、根 germs、两侧固定 physical 端口全都准确不变。
把 \(\|\psi\|_{C_x^4}\) 归一到至多1，取足够小
\(|\varepsilon|<2^{-20}\) 后，(P.18) 的正性、单调性及原严格
几何包络保持；这用 \(\Delta>j/2>64\)，不依赖频率。

紧支撑变分没有 root 有限部端项，故
\[
 \dot S=\int\phi_S(t)\psi(t)\,dt,\qquad
                   \phi_S=-{Q'\over4Q^{3/2}}.             \tag{P.20}
\]
对 (P.6) 分部积分，紧支撑变分可以准确使用局部泛函
\[
 \beta=\int\left\{{(1+Q)^2\over16\sqrt Q}
                 +{Q'^2\over64Q^{5/2}}\right\}dt
                   +\hbox{与本变分无关的端项}.
\]
所以
\[
 \dot\beta=\int\phi_\beta(t)\psi(t)\,dt,\qquad
 \phi_\beta=\frac d{dt}\left[
 {3\sqrt Q+2Q^{-1/2}-Q^{-3/2}\over32}
 +{5Q'^2\over128Q^{7/2}}-{Q''\over32Q^{5/2}}\right].       \tag{P.21}
\]
这两个核都是 \(t,Q,\sqrt Q\) 的代数函数，在真实区间取正平方根。
它们线性无关：对 (P.18) 的复多项式延拓，最高次 \(Q\sim c t^4\)
给两个不同的无穷远主阶
\(\phi_S\asymp t^{-3}\)、\(\phi_\beta\asymp t\)，系数均非零。

## 7. 真 Wronskian 变分及对称平方恒等式

固定 \(m\ne0\)，令 \(\lambda=m^2\ge16\)。
假设实际固定两侧行在当前背景有共振；取其非zero实解 \(h\)。
变分保持左侧数据，以相同物理 Wronskian 归一化。
Green恒等式给右端分母导数等于一个非zero固定实因子乘
\[
 \int_{J_x}K_\lambda(t)\psi(t)\,dt,\qquad
 K_\lambda=\mu\{h'^2-2\lambda hh'+\lambda h^2\}.           \tag{P.22}
\]
这里 \(dt\) 是原材料测度。推导为
\[
 \int[\dot\mu\,h'^2-\lambda\dot{(\mu Q)}h^2]
 =\int\mu\psi(h'^2-\lambda Qh^2)
                      +\lambda\int\mu\psi'h^2
 =\int K_\lambda\psi ,
\]
使用 \(\mu'/\mu=-1-Q\)；端项因 compact 支撑准确为0。
两侧是实际固定数据，所以没有隐藏的 Robin 导数。
若是已重停的全局外边界，仍须另加第3节指出的完整边界变化。

下面的恒等式是本篇控制透明情形的关键。
置
\[
 A=\mu h^2,\quad B=\mu hh',\quad C=\mu h'^2.
\]
直接由原 (P.1) 的齐次方程，准确有
\[
 A'=-(1+Q)A+2B,\quad B'=C-\lambda QA,\quad
 C'=(1+Q)C-2\lambda QB,\quad K_\lambda=C-2\lambda B+\lambda A.
\]
因此
\[
 \boxed{\quad
 K_\lambda''=
 [Q^2+(2-4\lambda)Q+1+Q']K_\lambda
       +2\lambda(\lambda-1)Q' A .
 \quad}                                                   \tag{P.23}
\]
这是完整两态的恒等式，既非高频近似也不依赖 \(h\) 在区间内无零点。

## 8. 不存在相位核张成的退化方向：完整复延拓理由

声称
\[
                  K_\lambda\notin
                  \operatorname{span}_{\mathbb R}\{\phi_S,\phi_\beta\}.
                                                               \tag{P.24}
\]
证明反设在真实开区间有该关系。
由于 \(Q\) 为非constant多项式、\(\lambda(\lambda-1)\ne0\)、\(Q'\ne0\)，
(P.23) 给
\[
 A=\frac{K_\lambda''-
          [Q^2+(2-4\lambda)Q+1+Q']K_\lambda}
                        {2\lambda(\lambda-1)Q'}.
\]
于是 \(A\) 的这个局部解析 germ 是代数函数。
此处不把局部 \(\sqrt Q\) 强行绕 branchpoints 延成单值函数。
只需取它满足的一个非zero多项式关系
\(\mathcal P(t,A)=0\)。

把真实 \(h,h'\) 在区间内任一点的值作为初值，
用同一个多项式 \(Q(t)\) 解原线性 ODE 的**整个复平面**延拓。
系数是整函数，故这个初值解 \(h(t)\) 整；
\(\mu(t)=\mu(t_*)\exp[-\int_{t_*}^t(1+Q)]\) 也整且处处非zero。
因此 \(A=\mu h^2\) 是同一 germ 的整延拓。
整函数 \(\mathcal P(t,A(t))\) 在原开区间为0，恒等定理使它在全平面为0。
这一步只延拓多项式关系，不对任何 branch 作非法单值化。

整的代数函数必为多项式：将 \(\mathcal P\) 看成关于 \(A\) 的多项式，
其系数为 \(t\) 的多项式；根的初等 Cauchy 上界给足够大圆外
\(|A(t)|\le C(1+|t|)^N\)，再由整函数 Cauchy估计使高于 \(N\) 的
Taylor系数为0。因为 \(h\) 非zero，\(A\) 是非zero多项式。
在它的有限零点之外，令 \(r=h'/h\)，则
\[
 r=\frac12\left(1+Q+\frac{A'}A\right)
                        =\frac{1+Q}{2}+O(t^{-1})
\]
于复无穷远。另一方面原方程准确给
\[
                    r'+r^2-(1+Q)r+\lambda Q=0.
\]
代入上式，其最高次项为 \(-Q^2/4\)。
\(r'\)、\(\lambda Q\)、\(Q A'/A\) 的次数都严格小于
\(2\deg Q\)，不可能消去它。这与 \(Q\) 非constant矛盾，证明 (P.24)。
\(\lambda=0,1\) 没有被此论证授予；物理 mean及刚体槽仍另保。

## 9. 明确有限程序产生控制，并准确保持两相位

在 \(J_x\) 取
\[
 b_J(x)=(x-7/16)^6(15/32-x)^6
\]
于区间内，区间外为0；它为 \(C^5\)。
用真实候选函数 \(\psi_n=b_J(x)x^n,\ n=0,1,\ldots\)。
(P.20)、(P.21)、(P.22) 的三个矩泛函在其线性包上满秩3：
否则某个非zero线性组合核与所有这些测试函数正交。
正权 \(b_J>0\) 和多项式一致逼近便使该连续核在整个区间为0，
这违反两相位核的独立性及 (P.24)。

因此枚举三指标，总会找到一个非zero \(3\times3\) 矩 determinant。
取该矩阵前两行的 cofactors作 \(\psi\) 的系数，便准确有
\[
                    \dot S=\dot\beta=0,\qquad
                      \int K_\lambda\psi\ne0.             \tag{P.25}
\]
最后只除以其正有限 \(C_x^4\) norm进行归一化。
这给真正可执行的有限结束构造；尚未给其指标上界或非zero量的统一下界，
因此不把“会结束”当作移动所有模的已付数值门。

原两个 disjoint bump 的真实 \((S,\beta)\) Jacobian 已在
[两参数相位定理](R119-supplement-actual-two-parameter-complete-phase-arithmetic.md)
及[联合选择](R119-supplement-joint-actual-principal-and-beta-selection.md)
中证明可逆。其支集与 \(J_x\) 不交。
对 (P.19) 的小第三参数应用这个真实二维逆，存在一条实解析
\((\gamma_1(\varepsilon),\gamma_2(\varepsilon))\)，使整个新 profile的
\(S,\beta\) **准确恒定**。
由 (P.25)，两个补偿参数的一阶导数均为0，故真实 Wronskian 的
一阶变化仍是 (P.22) 的非zero值。
所有端 jets和 root减项仍完全相同。

对任一指定的有限频率集合，当前非共振模由连续性保留；
每个共振模的相位保持控制泛函不为0。
在共同两相位核空间中避开有限个真超平面，可以用同一个有限
多项式组合，使每个共振的导数都非zero。
于是足够小的一个实 \(\varepsilon\ne0\) 消除该有限集合中的全部共振。
这覆盖第5节的纯旋转情形，而不需要先证明反射系数有正下界。

## 10. 两 weak 分量、ordinary source、mean及新候选权限

为完整支付 source，令
\[
 F_u^t=\mu^{-1/2}F^t,\quad F_u^\theta=\mu^{-1/2}F^\theta,\quad
 f_u=\mu^{-1/2}\left(f-\tfrac12(\log\mu)'F^t\right).
\]
以 \(\pi=u'+F_u^t\) 为第二态，准确方程是
\[
 \partial_t\binom u\pi=
 \begin{pmatrix}0&1\\
 -m^2Q-Q'/2+(1+Q)^2/4&0
 \end{pmatrix}\binom u\pi
                  +\binom{-F_u^t}{f_u-imF_u^\theta}.      \tag{P.26}
\]
(P.17) 的实际输入范数是这个源对经 (P.3) 的完整 \(L^1_t\) norm：
\[
 \mathcal J_m=
 \binom{-\sqrt{k_m}F_u^t}
       {k_m^{-1/2}(f_u-imF_u^\theta)} .
\]
没有引入 \((F^t)'\) 的范数。
原 ordinary Darboux 源仍须用真实 \(f=w^2e\)，不是任选一个 scalar
冒充 metric源。实际 metric方向 (P.19) 自身给
\[
 \dot G=\mu
 \begin{pmatrix}\psi&0\\0&\psi'-Q\psi\end{pmatrix},
 \qquad
 P\dot h=-\operatorname{div}(\dot G\nabla h).              \tag{P.27}
\]
因此其完整 weak源是 \(\dot G\nabla h\)，并按 (P.26) 保留由 height
共轭产生的 ordinary修正。两个补偿 bump的源也照此相加。

fixed平台端口的总物理 flux恢复为
\[
          p_{\rm tot}=\sqrt\mu\,(\pi+4u),\qquad
          p_{\rm bare}=p_{\rm tot}-F^t .                  \tag{P.28}
\]
要给 bare迹仍须另付实际 \(F^t\) 的端点迹；体源 \(L^1\) norm不授该迹。

mean 不在 \(k_m^{-1}\) 中伪代 \(m=0\)。
它始终使用原径向
\[
 (p_0^{\rm tot})'=f_0,\qquad
 (h_0)'=\mu^{-1}(p_0^{\rm tot}-F_0^t),
\]
并保留独立整体高度常数。
常平台的密度 mean矩阵准确为
\[
 E_0(\ell)=
 \begin{pmatrix}\cosh4\ell&\sinh4\ell/4\\
                 4\sinh4\ell&\cosh4\ell\end{pmatrix}.
\]
总 mean resistance \(\int\mu_\ell^{-1}\) 一般改变；
平移方向 \(\partial_\ell\log\mu_\ell=Q_\ell-7\) 给其准确导数
\(-\int(Q_\ell-7)\mu_\ell^{-1}\)。
不能因为 (P.7) 就声称 mean或height积分不变。
实际背景高度由 \(Z=Z_e-\int_{a_e}^{a}w\,da\) 定义；
compact方向的变化是 \(-\int_{a_e}^{a}w\psi\,da\)，与移动点项区别。
原两端总 flux、正型 DN 的 mean交叉和共同常数仍留在网络。

整坡平移不改变实际 \(Q\) 的导数、单峰和密度比门；
三阶 profile几何 bounds至多付固定余量，深端仍按原正幂趋0。
compact第三方向取上述小参数也保这些局部门。
但本篇未把它们升级为新整尾标签图或完整 reach：
真正新的低窗误差、两处接缝、第四允许线与停止、外全模好集、
原 \(\mathcal X_\beta\) 强源、非径向两相位选择及全族重建均须
在最后选择的整个新候选上核付。
尤其 (P.25) 的有限非zero导数没有未经证明的全层正下界；
它正是继续量化移动 Schur 的下一输入。

精确代数与充分有理门见
\(\texttt{scripts/fourfold_phase_preserving_finite_Schur_controls_20261114.js}\)
及
\(\texttt{notes/2026-11-14-R119-phase-preserving-finite-Schur-controls-budget.json}\)。
该新 BigInt 程序只核对显示恒等式和常数；存在性、完整复延拓及
所有模/源的权限由正文证明，不以有限频率采样替代。
