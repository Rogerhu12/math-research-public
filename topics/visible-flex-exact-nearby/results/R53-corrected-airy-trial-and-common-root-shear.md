# R53：校正Airy试解、共同根剪切与二阶接线误差

2026-11-12，visible-exact-astra-f6a2。

**状态：已证明的中间算子结论。** R43和R45分别与未校正的根frame比较，
会留下4/3阶误差。本篇构造一个明确的共同根剪切和两侧匹配试解：负侧真实传播
与完整试解矩阵相差二阶平滑，正侧试解的完整物理源增益为5/3，从而在共同frame
中得到二阶的帽反射误差。普通源、均值和所有角耦合均保留。

这里的负侧比较对象仍是明确的完整Airy矩阵。将其在strict cut上再写成首逆频率
符号加二阶强余项，需要作同一矩阵的有限符号提取；本篇不从逐列渐近直接授予
那一结论，也不声称当前候选已填入所有canonical系数/正帽输入。

## 1. 同一个实际canonical负组件

用物理根角 \(\phi\in\mathbb R/(\ell\mathbb Z)\)，置 \(q=2\pi/\ell\)。
考虑同一个真实算子
\[
 L_V=\partial_\xi^2-\xi\partial_\phi^2+V(\xi,\phi),
 \qquad 0\le\xi\le\delta\le1.
\tag{53.1}
\]
\(V\)为实数。输入其实际两阶径向及下述有限角导数；不要求小振幅。
对一个有限实阶 \(s\)，记
\[
 p_s=2|s|+10,
 \quad w_p(l)=(1+|l|)^p e^{|\rho|\omega(|l|)},
\]
\[
 \mathcal V=\sum_{a=0}^2\sum_{b=0}^4
 \sum_l w_{p_s}(l)\sup_{0\le\xi\le\delta}
                  |(\partial_\xi^a\partial_\phi^bV)_l(\xi)|<\infty.
\tag{53.2}
\]
\(\omega\)是非负递增次可加权，例如R49的直接log权。径向sup位于Fourier和
内部。负权空间按R41/R49的Hilbert完成解释。

下面的 \(\Gamma\) 在 \(j\ne0\) 上为 \(\lambda_j=q|j|\)，在均值上为1；
\(\epsilon_j=\operatorname{sgn}j\)、\(\epsilon_0=0\)。沿用R39的
\(c=c_A^{-1/2}\)、\(Y_\sigma(z)=\operatorname{Bi}(z)+i\sigma\operatorname{Ai}(z)\)，
\(\sigma=\pm1\)，以及**完整含均值**的自由frame \(F_*(\xi)\)。

## 2. 两个真实输运系数及根部光滑性

置 \(\tau(\xi)=2\xi^{3/2}/3\)。对 \(\xi>0\) 定义
\[
 \begin{aligned}
 B(\xi,\phi)&=-\frac1{4\sqrt\xi}\int_0^\xi
 \frac{V(t,\phi+\tau(\xi)-\tau(t))
       +V(t,\phi-\tau(\xi)+\tau(t))}{\sqrt t}\,dt,\\
 C(\xi,\phi)&=\frac14\int_0^\xi
 \frac{V(t,\phi+\tau(\xi)-\tau(t))
       -V(t,\phi-\tau(\xi)+\tau(t))}{\sqrt t}\,dt.
 \end{aligned}\tag{53.3}
\]
它们都为真实实函数。以 \(D=\sqrt\xi B\) 相加减可直接验证
\[
 D_\xi+\sqrt\xi C_\phi=-\frac{V}{2\sqrt\xi},
 \qquad C_\xi+\sqrt\xi D_\phi=0.
\]
所以准确有
\[
 \boxed{\quad B+2\xi B_\xi+2\xi C_\phi=-V,
                    \qquad C_\xi+\xi B_\phi=0.\quad}
\tag{53.4}
\]

这些式子并未在根处引入奇异系数。令
\(\eta(t)=\tfrac23(1-t^{3/2})\)，将 \(t\)缩放到[0,1]。第 \(l\) 个Fourier系数为
\[
 B_l(\xi)=-\frac12\int_0^1t^{-1/2}V_l(\xi t)
                    \cos(ql\eta(t)\xi^{3/2})dt,
\]
\[
 C_l(\xi)=\frac{i\sqrt\xi}{2}\int_0^1t^{-1/2}V_l(\xi t)
                    \sin(ql\eta(t)\xi^{3/2})dt.
\tag{53.5}
\]
这里的三角函数只是对实位移Fourier系数的准确写法，不是复域估计。
对 \(B\) 的二次径向微分，唯一形式上含 \(\xi^{-1/2}\) 的项同时含
\(\sin(ql\eta\xi^{3/2})\)，用 \(|\sin z|\le|z|\) 消去其奇性。
对 \(C\) 使用
\[
 f(\xi)=\sqrt\xi\sin(a\xi^{3/2}),\quad
 |f|\le|a|\xi^2,\quad |f'|\le2|a|\xi,
\]
\[
 f''=-\tfrac14\xi^{-3/2}\sin(a\xi^{3/2})
       +\tfrac94a\cos(a\xi^{3/2})
       -\tfrac94a^2\xi^{3/2}\sin(a\xi^{3/2}).
\tag{53.6}
\]
这些式子及 \(|a|\le(2/3)|ql|\)证明两系数真实延拓到根，至少为所用的
\(C^2\)函数，并给
\[
 B(0)=-V(0),\qquad B_\xi(0)=-\tfrac13V_\xi(0),
 \qquad C(0)=C_\xi(0)=0,\qquad C_{\xi\xi}(0)=V_\phi(0).
\tag{53.7}
\]
根处各式也可直接由(53.4)逐阶比较。

对所需 \(0\le a,b\le2\)，(53.5)–(53.6)在Fourier包络范数中给安全上界
\[
 \mathcal A_{p_s,\rho}(\partial_\xi^a\partial_\phi^b B),\quad
 \mathcal A_{p_s,\rho}(\partial_\xi^a\partial_\phi^b C)
 \le8\mathcal V,
\tag{53.8}
\]
其中 \(\mathcal A\)指(53.2)的一项，仍取逐系数径向sup。
例如 \(B_{\xi\xi}\)分别由 \(V_{\xi\xi},2V_{\xi\phi},(4/3)V_{\phi\phi}\)
控制；\(C_{\xi\xi}\)由
\((2/3)V_{\xi\xi\phi},(8/3)V_{\xi\phi},(5/3)V_\phi,V_{\phi\phi}\)
控制，故8足够。角微分再把这些阶数至多提高到(53.2)的四阶。

因为 \(w_p\)次乘性，\(\mathcal A\)是Banach代数。于是
\[
 \boxed{\quad
 \mathcal A_{p_s,\rho}(L_VB),\quad
 \mathcal A_{p_s,\rho}(L_VC)
 \le24\mathcal V(1+\mathcal V).\quad}
\tag{53.9}
\]
这一步保留了 \(VB,VC\)，不把有界势当作可以删掉的项。

## 3. 完整双通道试解及准确残差

对 \(j\ne0\) 的输入 \(e^{iqj\phi}\)，定义第 \(\sigma\) 列
\[
 \boxed{\begin{aligned}
 U_{\sigma j}^{\rm app}={}&c\lambda_j^{-1/3}e^{iqj\phi}
 \left[(1+i\epsilon_j\lambda_j^{-1}C)
                 Y_\sigma(-\xi\lambda_j^{2/3})\right.\\
 &\hspace{37mm}\left.
       +\lambda_j^{-4/3}B\,Y_\sigma'(-\xi\lambda_j^{2/3})\right].
 \end{aligned}}\tag{53.10}
\]
其第二Cauchy槽始终是完整的 \(\partial_\xi U^{\rm app}\)。
均值输入使用R39的真实自由列 \(c(1+i\sigma\xi/\pi)\)，其真实残差为
\(V c(1+i\sigma\xi/\pi)\)，不设置成零。

**命题53.1。** 对每个非零输入列，准确有
\[
 \boxed{\begin{aligned}
 L_V U_{\sigma j}^{\rm app}
 =c e^{iqj\phi}\left[
 i\epsilon_j\lambda_j^{-4/3}(L_VC)
                 Y_\sigma(-\xi\lambda_j^{2/3})\right.\\
 \left.\hspace{25mm}
 +\lambda_j^{-5/3}(L_VB)
                 Y_\sigma'(-\xi\lambda_j^{2/3})\right].
 \end{aligned}}\tag{53.11}
\]

证明只用 \(Y''(z)=zY(z)\)。未归一化的Ai系数为
\[
 i\epsilon\lambda^{-1}L_VC+
                [V+B+2\xi B_\xi+2\xi C_\phi],
\]
Ai′系数为
\[
 \lambda^{-4/3}L_VB
       -2i\epsilon\lambda^{-1/3}(C_\xi+\xi B_\phi).
\]
两方括号恰由(53.4)消失，乘以 \(c\lambda^{-1/3}\)得到(53.11)。
特别，主角导产生的 \(2iqj\partial_\phi\) 项已经参与抵消。
只用径向的 \(B+2\xi B_\xi=-V\) 会漏掉这些项，不能用于非径向势。

## 4. 残差进入真实源槽后具有二阶强增益

令 \(\mathcal R^{\rm app}\)为(53.11)及完整均值残差组成的行算子。
真实普通源槽仍是R39的
\[
 \Gamma_f=\frac{i\pi}{2c^2}\binom{-D_-f}{D_+f}.
\tag{53.12}
\]
设
\[
 Q=\max(1,q,q^{-1},c,c^{-1}),\qquad
 L_s=2^{4|s|+30}(1+\pi)Q^8(1+\mathcal V)^2.
\tag{53.13}
\]
则一个共同的粗但明确上界是
\[
 \boxed{\quad
 \|\Gamma_{\mathcal R^{\rm app}}(\xi):
       E_{s,\rho}\to E_{s+2,\rho}\|
 \le L_s(1+\xi^{-1/2}),\qquad 0<\xi\le\delta.
 \quad}\tag{53.14}
\]

这里不是把逐输入列的界直接相加。以下给完整矩阵合并。
R39的实际全轴Airy界为
\[
 |Y_\sigma(-t)|\le10(1+t)^{-1/4},\quad
 |Y_\sigma'(-t)|\le10(1+t)^{1/4}.
\]
对非零输入 \(j\) 和输出 \(k\)，第一种源乘积由
\[
 50\pi\,\xi^{-1/2}\lambda_k^{-1/2}\lambda_j^{-3/2}
                      |(L_VC)_{k-j}|
\tag{53.15}
\]
控制；第二种由
\[
 50\pi\left(\lambda_k^{-1/2}\lambda_j^{-3/2}
           +\lambda_k^{-1/3}\lambda_j^{-5/3}\right)
                      |(L_VB)_{k-j}|
\tag{53.16}
\]
控制。第二式用
\((1+t_j)^{1/4}/(1+t_k)^{1/4}
 \le\max(1,(\lambda_j/\lambda_k)^{1/6})\)。两通道矩阵再付因子2。
每个指数对的和均为2；在输出乘 \(\langle k\rangle^{s+2}W_\rho(k)\)、
输入除以 \(\langle j\rangle^sW_\rho(j)\) 后，Peetre及次可加性只增加
\((1+|k-j|)^{|s|+2}e^{|\rho|\omega(|k-j|)}\)及有限的二次幂常数。
\(\lambda_j^{-a}\le 2^{a/2}q^{-a}\langle j\rangle^{-a}\)支付物理频率换算。
对lag作离散Young，(53.9)即支付完整无限矩阵。

均值输出行用 \(|D_\sigma(\xi,0)|\le2c\)，实际均值输入列用
\(V D_\sigma(\xi,0)\)。当一指标为零时，另一个指标本身就是lag；
(53.2)的 \(p_s=2|s|+10\) 足以直接支付其所需有限正负阶。
例如第一类均值行的系数至多
\(10\pi\lambda_j^{-4/3}|(L_VC)_{-j}|\)，第二类至多
\(64\pi Q^2\langle j\rangle^{-3/2}|(L_VB)_{-j}|\)。
均值输入的非零输出列由
\(20\pi Q\langle k\rangle^{-1/3}|V_k|\)控制。
它们的加权 \(\ell^2\) norm均被相应 \(\ell^1\) 包络控制。
上述所有因子之和小于(53.13)，得到(53.14)，没有投影掉均值或跨号块。

## 5. 精确共同根剪切及实际传播比较

记 \(v_0=V(0,\phi)\)、\(v_1=V_\xi(0,\phi)\)。定义真实自伴算子
\[
 P_0=\Gamma^{-1}M_{v_0}\Gamma^{-1},\qquad
 \mathscr S_0=\begin{pmatrix}I&P_0\\0&I\end{pmatrix},
 \qquad Q_0=F_*(0)^{-1}\mathscr S_0F_*(0).
\tag{53.17}
\]
\(\mathscr S_0\)准确保持物理Green通量，逆为把 \(P_0\)换成 \(-P_0\)；
所以 \(Q_0\)准确为onto \(J\)-unitary。它不是事后形式的flux修补。
\(Q_0-I\)增益4/3，其全部有限窗口norm由实际 \(v_0\) 的Fourier包络及R39
根frame直接给出。

对非零输入，(53.7)、(53.10)在根处给
\[
 U^{\rm app}(0)=U^{\rm free}(0)+M_{v_0}\Gamma^{-2}p^{\rm free}(0),
\]
\[
 p^{\rm app}(0)=p^{\rm free}(0)
                    +\tfrac13M_{v_1}\Gamma^{-2}p^{\rm free}(0).
\tag{53.18}
\]
所以第一槽与(53.17)的差为
\([M_{v_0},\Gamma^{-1}]\Gamma^{-1}p^{\rm free}\)，第二槽之差为
(53.18)显示的二阶项。确切矩阵恒等式
\[
 ([M_v,\Gamma^{-1}])_{kj}
    =v_{k-j}(\lambda_j^{-1}-\lambda_k^{-1})
\tag{53.19}
\]
在 \(j,k\ne0\) 时由
\(|\lambda_j^{-1}-\lambda_k^{-1}|
\le q^{-1}|k-j|/(|k||j|)\)控制。
放回根frame后第一槽增益7/3，第二槽增益2。均值行/列按上一节保留实际有限
光滑列。因此，若
\[
 W^{\rm app}(\xi)=F_*(\xi)^{-1}
                    \binom{U^{\rm app}(\xi)}{\partial_\xi U^{\rm app}(\xi)},
\]
则
\[
 \|W^{\rm app}(0)-Q_0:E_{s,\rho}\to E_{s+2,\rho}\|\le L_s.
\tag{53.20}
\]
(53.19)逐lag的权最多再增加一次 \(|k-j|\)，仍在(53.2)内。
Ai初值及逆Wronskian的费用已经小于(53.13)。

记 \(C(\xi,\eta)\)为R39的**真实**传播，使用同一实际 \(V\)。令
\[
 K_{s+2}=100\pi\max(1,2^{1/3}q^{-2/3})
                           M_{s+7/3,\rho}(V).
\]
完整Volterra式给 \(\|C(\xi,\eta)\|_{E_{s+2,\rho}}\le e^{\delta K_{s+2}}\)。
短collar门成立时可将该数换成 \(e^{1/10}\)。由(53.11)–(53.14)、(53.20)，
准确Duhamel比较为
\[
 C(\xi,0)Q_0-W^{\rm app}(\xi)
 =-C(\xi,0)(W^{\rm app}(0)-Q_0)
   -\int_0^\xi C(\xi,t)\Gamma_{\mathcal R^{\rm app}}(t)dt.
\tag{53.21}
\]
从而
\[
 \boxed{\quad
 \|C(\xi,0)Q_0-W^{\rm app}(\xi):E_{s,\rho}\to E_{s+2,\rho}\|
 \le e^{\delta K_{s+2}}L_s(1+2\sqrt\delta+\delta).
 \quad}\tag{53.22}
\]
这是同一个真实负组件的二阶强余项，包含全部Fourier矩阵。

带外部普通源 \(f\) 时，准确解仍是
\[
 z(\xi)=C(\xi,0)Q_0z_{\rm in}
               +\int_0^\xi C(\xi,t)\Gamma_f(t)dt.
\tag{53.23}
\]
本篇仅在第一项中给(53.22)；第二项按R39/R49的完整源空间和常数携带。
没有因齐次试解改善而删除或猜测普通源的正则性。

## 6. 正侧匹配只需有限Taylor数据

同一个根的正侧使用 \(y=-\xi>0\)。将整体符号变为正能量约定后，实际算子写成
\[
 P_+=-\partial_y^2-y\partial_\phi^2+V_+(y,\phi)
                         -\operatorname{div}(E\nabla),
\tag{53.24}
\]
其中全部系数仍来自真实坐标/height。假设实际有限jet支付
\[
 E=y^5e,\qquad E_y=y^4\widetilde e,
 \quad V_+(0)=-v_0,\quad (V_+)_y(0)=v_1.
\tag{53.25}
\]
这是明确的匹配门，不是假设正侧有椭圆Cauchy解。R47的有限延拓机制在更高
有限阶照样适用：例如保留负侧真实坐标六阶、height五阶Taylor，多项式延拓
后直接核对(53.25)、实际Jacobian和height下界。若未供这些jet，不能调用本节。

取明确的两个实多项式
\[
 B_+(y,\phi)=-v_0(\phi)+\tfrac13v_1(\phi)y,
 \qquad C_+(y,\phi)=\tfrac12(v_0)_\phi(\phi)y^2.
\tag{53.26}
\]
对 \(j\ne0\)，用与R47同样已付的cutoff \(\chi\)定义
\[
 Q_j^+=c\lambda_j^{-1/3}\chi(y)e^{iqj\phi}
 \left[(1+i\epsilon_j\lambda_j^{-1}C_+)\operatorname{Ai}(y\lambda_j^{2/3})
       +\lambda_j^{-4/3}B_+\operatorname{Ai}'(y\lambda_j^{2/3})\right].
\tag{53.27}
\]
均值定义 \(\lambda_0=1,\epsilon_0=0\)，并始终直接算
\(P_+Q_0^+\)；非零频率的自由消去公式不用于均值。

令 \(L_+=-\partial_y^2-y\partial_\phi^2+V_+\)。在 \(\chi=1\) 的区域，
非零列的完整无E残差是
\[
 \begin{aligned}
 c e^{iqj\phi}\big[&\lambda_j^{-1/3}D_B\operatorname{Ai}
 -2i\epsilon_j\lambda_j^{-2/3}D_C\operatorname{Ai}'\\
 &+i\epsilon_j\lambda_j^{-4/3}(L_+C_+)\operatorname{Ai}
 +\lambda_j^{-5/3}(L_+B_+)\operatorname{Ai}'\big],
 \end{aligned}\tag{53.28}
\]
Ai自变量均为 \(y\lambda_j^{2/3}\)，且
\[
 D_B=V_+-B_+-2y(B_+)_y+2y(C_+)_\phi=O(y^2),
\]
\[
 D_C=(C_+)_y+y(B_+)_\phi=\tfrac13(v_1)_\phi y^2.
\tag{53.29}
\]
准确的 \(D_B/y^2\) 可写成
\[
 \int_0^1(1-t)(V_+)_{yy}(ty,\phi)dt+y(v_0)_{\phi\phi},
\tag{53.30}
\]
所以没有用浮点相消来解释O项。

由R47的真实Ai矩、全部Fourier lag及物理 \(y=r a(r,\theta)\) 源变换，
(53.28)的四项分别有下表的 \(L^2\) 径向指数：

|项|R47三元组 \((k,\alpha,d)\)|指数 \(\alpha-2k/3-1/3\)|
|---|---|---:|
|\(D_B\operatorname{Ai}\)|(2,−1/3,0)|−2|
|\(D_C\operatorname{Ai}'\)|(2,−2/3,1)|−7/3|
|\((L_+C_+)\operatorname{Ai}\)|(0,−4/3,0)|−5/3|
|\((L_+B_+)\operatorname{Ai}'\)|(0,−5/3,1)|−2|

E项的最差原Ai项为 \(E_{22}\partial_\phi^2Q\)，其三元组
(5,5/3,0)给−2；其余原Ai项不差于−2。带C、B的项再多一个
\(\lambda^{-1}\)或 \(\lambda^{-4/3}\)，角与径向乘积求导逐项保留，均不差于−5/3。
cutoff导数在 \(y\ge h/2\) 支撑：准确写
\(\chi''=y^2(\chi''/y^2)\)、\(\chi'=y^3(\chi'/y^3)\)，
其有限系数费由既定cutoff导数及h给出，所有这些项也不差于−5/3。
均值使用其实际完整残差的有限角导数/径向norm，按R47的均值列界加入。

因此存在由这些**有限实际系数**明确计算的 \(K_s^+\)，使真实物理源满足
\[
 \boxed{\quad P_{\rm ph}Q_{\rm ph}^+:
 H^s\longrightarrow L^2_rH^{s+5/3},\qquad
 \|P_{\rm ph}Q_{\rm ph}^+\|\le K_s^+.\quad}
\tag{53.31}
\]
计算 \(K_s^+\) 的具体规则就是：展开(53.28)、
\(-\chi''U-2\chi'U_y-\operatorname{div}(E\nabla(\chi U))\)，
连同实际 \(J_\Psi/t\) 物理源因子，将每项归为上表/R47形式；
选整数 \(p>|s+5/3|+1\)，对每项用R47(3.7)的实际有限Bell多项式和Ai矩
取 \(M_0,M_p\)，再相加、乘R47(1.3)及(4.4)的lag/真实角图常数。
mean另按同一有限列规则加入。这个规则只含有限和、明确Gamma函数矩及已列的
真实sup，不用一个未说明的存在性常数。

## 7. 同一正帽在共同根frame中的二阶反射

保留R45的同一个whole正组件、完整Dirichlet/Poisson/source/contact实现。
(53.27)在其它端邻域为零。真实物理边界迹仍须按R47的 \(B_\partial\)及
normal shear同时转换；不能把canonical迹直接当物理迹。

非零频率的根处准确有
\[
 A_{\rm trial}=A_A+M_{v_0}\Gamma^{-2}C_A,
 \qquad C_{\rm trial}=C_A+\tfrac13M_{v_1}\Gamma^{-2}C_A.
\tag{53.32}
\]
这正是负侧(53.18)，而不是两个分别选取的frame。
与 \(\mathscr S_0(A_A,C_A)^t\) 比较，第一个根迹的归一误差增益7/3，
第二个增益2，由(53.19)的同一个全lag界支付。

把试解接到同一个真实Poisson解，R45完整恒等式给
\[
 C_{\rm trial}-\Lambda A_{\rm trial}=K(PQ^+).
\tag{53.33}
\]
式中物理表示准确包含R47的 \(B_\partial^*K_{\rm ph}\) 及height shear。
R45的 \(K:L^2H^t\to H^{t+1/3}\)，再经过根动量归一化
\(C_A^{-1}\) 的1/3增益，把(53.31)变成7/3阶的归一contact误差。
所以在共同frame \(\mathscr S_0F_*(0)\) 中，这个真实cap的反射满足
\[
 \boxed{\quad R_{\rm cap}^{S}=-I+E_2,
              \qquad E_2:H^s\to H^{s+2}.\quad}
\tag{53.34}
\]
均值与 \(-I\) 的差保留在实际有限光滑列中，其norm由完整R45 DN/Poisson界
和(53.27)的真实mean列控制；没有把mean原来的端口关系改成Dirichlet。

这里无需假定试解的incoming映射可逆。对非零频率先将Ai试解输入取为
\(h=2i x\)，因为自由Ai列准确对应 \(F_*(0)(x,-x)^t\)；mean仍按上面的实际
有限列支付。确切地，将实际Poisson解的incoming/
outgoing分别写成 \(A_{\rm in}=I+E_A\)、\(A_{\rm out}=-I+E_B\)，两误差均有上述
二阶强界，且真实关系为 \(R_{\rm cap}^{S}A_{\rm in}=A_{\rm out}\)。直接得到
\[
 R_{\rm cap}^{S}+I=E_B-R_{\rm cap}^{S}E_A,
\tag{53.35}
\]
只需同一个实际反射在输出 \(H^{s+2}\) 的界。因此(53.34)的具体norm至多
\(\|E_B\|+\|R_{\rm cap}^{S}\|_{H^{s+2}}\|E_A\|\)；前两项由(53.31)–(53.33)、
根frame/commutator及物理迹常数逐项计算。

这个新frame的反射存在性及有限Sobolev界也不能免费假定。由R45，旧frame反射
\(R_{\rm cap}\)在L²为onto unitary。\(Q_0^{\pm1}\)为有界 \(J\)-unitary且
与I之差增益4/3。把旧中性图 \((a,R_{\rm cap}a)\) 乘 \(Q_0^{-1}\)，其incoming
映射为
\[
 A=I+K_0=(Q_0^{-1})_{++}+(Q_0^{-1})_{+-}R_{\rm cap}.
\tag{53.36}
\]
\(K_0\)增益4/3，故A为Fredholm指数零。通量及 \(Q_0\) 的有界逆给
\(\|Aa\|_2\ge\|Q_0\|_2^{-1}\|a\|_2\)，从而A onto，
\(\|A^{-1}\|_2\le\|Q_0\|_2\)。outgoing映射是 \(R_{\rm cap}\) 加compact，
同样为指数零且有同一正下界，所以也onto。这定义同一个onto unitary
\(R_{\rm cap}^S\)。

有限普通Sobolev窗口可显式bootstrap：对 \(t\ge0\) 取整数n使 \(4n/3\ge t\)，
在已付窗口以
\[
 A^{-1}=\sum_{j=0}^{n-1}(-K_0)^j+(-K_0)^nA^{-1}
\tag{53.37}
\]
给出有限和/乘积常数。最后一项从L²逐步增益到 \(H^t\)，其余项用各自同档界；
负窗口对 \(A^*\)作相同计算再取对偶。全部 \(K_0\) norm由实际R45反射和
(53.17)的有限乘子表供应。没有另设一个未检验的低模可逆矩阵。

若使用非零log权，本节(53.31)–(53.35)须同时使用已付的正负权cap/contact及
新frame Robin窗口；普通L²通量不等于正权自伴。R35的实际交换子/宽度门可用来
支付这些量，但未填入之前本节只声明普通有限Sobolev结论。

## 8. 与完整相位和下一步接线的关系

(53.22)和(53.34)解释了为什么不能把单侧根误差4/3直接认作完整双侧网络必有的
不可改善误差：两侧最先的修正都是同一个真实 \(P_0\) shear，接线时须一致携带。
本篇已经证明它与完整试解之间的强二阶差。

在固定strict cut，(53.10)的标量首振荡项含
\(\epsilon C-\sigma\sqrt\xi B\)。由(53.3)，它准确等于
\[
 \frac\sigma2\int_0^\xi
       \frac{V(t,\phi+\sigma\epsilon[\tau(\xi)-\tau(t)])}{\sqrt t}dt.
\tag{53.38}
\]
这与R43同一实际射线积分相符，根frame剪切没有引入新的独立 \(1/j\) 常数。
但(53.38)本身仍不是把全矩阵 \(W^{\rm app}(\delta)\)写成R43的自伴ordering
加二阶余项的证明。须继续支付该完整矩阵的同号/跨号/mean及固定cut Airy展开，
再与R46/R49、真实变角/共轭、正帽和全部普通源接齐。

当前实际图的canonical系数、局部正延拓jet、完整帽realization及所有数值常数
仍需各自验证。低频/持握约束、R37残差因子Newton和最终可见闭族也未由本篇完成。
