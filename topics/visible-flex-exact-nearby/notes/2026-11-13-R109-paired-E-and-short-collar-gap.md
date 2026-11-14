# R109 补充：配对主矩阵误差与短领口的真实 gap 下界

2026-11-13，independent-audit。

**状态：完整恒等式、全算子上界及实际 62 个准确有理数门已执行。**
本补充保持原 R109 文件、源和报告不变。对同一实际参数盒
$|\delta-\delta_5|\le10^{-9}$，它支付 R109 线性势 Airy 试解的完整
主矩阵误差贡献，并对同一短领口的紧支 primal/dual 构造给出严格下界。

在 $H=49/102400$、canonical 高输入 $|k|>256$ 上，全部主矩阵误差
贡献的 energy gap 小于 $.000071462239$，相应高根与 regular 联合
contact 贡献小于 $.000535727775$。但对该构造中的单个单位输入
$k=257$，**完整 gap 严格大于 $1.3189203219$**。
后一个结论针对指定根值和根通量、都在 $H$ 外为零的试函数/通量；
它不是实际 DN 差的下界，也不排除精确帽解。它表明必须扩大试函数的
真实支持域，或用真实外端 matching 取代这个短域的紧支延拓。

## 1. 同一个实际帽、测度和算子

全部空间和测度沿用 R96/R103/R108：canonical 圆长 $\ell=2\pi/q$，
使用 $L^2(d\phi)$ 的正交归一基
$e_k=\ell^{-1/2}\exp(4iqk\phi)$，只取四重子空间；
regular 标量使用物理圆上的单位常数。所有相对密度均经同一真实 Piola
换元，能量不另外乘 $q$ 或 $2\pi$。

置
$$
 C_0=\operatorname{diag}(1,y),\quad C=C_0+E,\quad
 A=\tau^{-2}C,\quad
 P_*=-\operatorname{div}(C\nabla)+V,\quad
 P_0=-\operatorname{div}(C_0\nabla)+V .
$$
采用 R96 的真实 height，故 $C_{11}=1$，$E_{11}=0$。
本补充不把结论转授给另一个未付的 height。准确 gauge 恒等式为
$$
 P_*(\tau^{-1})=0.                                      \tag{S1}
$$
它来自 $P_*=\tau[-\operatorname{div}(A\nabla)]\tau$ 对常数1的作用，
包含真实零阶项。

已付实际常数统一取
$$
 \varepsilon=\frac{1552858}{10^{12}},\quad
 G=33.417980,\quad \tau_{\min}=1.1568,\quad L=2.257,
 \quad q>q_-=9.72,\quad q<10,
$$
$$
 (1-\varepsilon)C_0\le C\le(1+\varepsilon)C_0,\quad
 |\nabla\log\tau|_{C_0}\le G,\quad
 A^{-1}\le L C_0^{-1},\quad \tau\ge\tau_{\min}.             \tag{S2}
$$
$L$ 已包含 R108 的完整 $(1-\varepsilon)^{-1}$，不是仅取 $\tau_{\max}^2$。
$G$ 是 R96 的完整 $|\partial_y\log\tau|^2+
H|\partial_\phi\log\tau|^2$ 上界的平方根，不遗漏角分量。
此外
$$
 \tau_0<1.477443,\qquad |\mu|<24.940215,\qquad
 \mu=(\partial_y\log\tau)|_{y=0}.                         \tag{S3}
$$
原 R96 的较宽参数盒包含本盒；所有参数使用自己的真实根。

## 2. 不微分 $E$ 的准确配对通量

令 $W=\chi U$，其中 $U$ 是原 R109 的完整逐输入试解，$\chi$ 是第5节
明确的径向截断。定义
$$
 v=\tau W,\qquad g=\nabla\log\tau,\qquad
 j^*=\tau^{-1}C_0\nabla W-WC\nabla(\tau^{-1}).              \tag{S4}
$$
直接求差并用(S1)微分，得到
$$
 \boxed{
 A\nabla v-j^*=\tau^{-1}E\nabla W,\qquad
 \operatorname{div}j^*
   =-\tau^{-1}\big(P_0W-g\cdot E\nabla W\big).
 }                                                        \tag{S5}
$$
例如散度中的两个交叉项是
$\nabla(\tau^{-1})\cdot C_0\nabla W-
\nabla W\cdot C\nabla(\tau^{-1})$，恰等于
$\tau^{-1}g\cdot E\nabla W$。剩下的零阶项由(S1)准确成为
$-\tau^{-1}VW$。没有估计 $\partial E$，也没有删去它们：它们已在准确
配对中相消。

对任意通量 $p=(p_y,p_\phi)$，设 $\Pi$ 为去均值投影，定义
$$
 \mathcal S p=
 \left(\Pi p_y,\quad
  \langle p_\phi,e_0\rangle e_0-\partial_\phi^{-1}\Pi\partial_y p_y
 \right).
$$
则 $j=\mathcal S j^*$ 严格散度零。$\chi$ 的零端 jets 使 $(v,j)$
可沿真实 Piola 公式零延拓到完整帽，真实外尾的 Robin mismatch 和
regular trace/flux 为零。根处 $E=0$，故
$$
 p_0=(A\nabla v)_y|_0
     =\tau_0^{-1}\big(U_y(0)+\mu U(0)\big),\qquad
 j_y(0)=\Pi p_0.                                         \tag{S6}
$$
均值 $m=\langle p_0,e_0\rangle$ 仍是 R109 已付的完整均值，不被设成零。

若 $f=\operatorname{div}j^*$，则
$$
 j^*-\mathcal S j^*=
 \left[\left(m+\int_0^y\langle f(s),e_0\rangle ds\right)e_0,\
                       \partial_\phi^{-1}\Pi f(y)\right]. \tag{S7}
$$
因此完整 defect $A\nabla v-j$ 分为：均值列、$P_0W$ 的 stream、
$\tau^{-1}E\nabla W$，以及 $\tau^{-1}g\cdot E\nabla W$ 的 stream。
最后两项是本补充真正支付的部分；$P_0W$ 包含全部 $\chi',\chi''$。
不能把(S5)中的 $P_0W$ 换成 $\chi P_0U$。

## 3. 已付 $E$ 的真实径向 profile

R87 的准确六阶图给
$E_{12}=s^6 e_{12}$、$E_{22}=s^7 e_{22}$，$s=r-t(\delta)$。
R96 的每一格用真实 $y/s\ge a_*>.9830630241$，且 $H< a_*h$、
$h=1/2048$，支付
$$
 \varepsilon_{\rm cell}\ge
 \frac{e_{12,*}h^6}{\sqrt{a_*h}}+
 \frac{e_{22,*}h^7}{a_*h}.
$$
对固定 $0<y\le H$，$s\le y/a_*$；第一项的相对阶为 $11/2$，
第二项为6。逐格沿用同一原始界，因而
$$
 \|C_0^{-1/2}E C_0^{-1/2}\|
       \le \varepsilon (y/H)^{11/2}.                     \tag{S8}
$$
这里没有从外端值猜测内部 profile；使用的是已经支付整个径向段的
根除法上界。

对高输入 Hilbert 空间 $\mathscr U=P_{>K}L^2$，记
$$
 {\cal G}_p=
 \left\|(y/H)^{p/2}\nabla W:
     \mathscr U\longrightarrow L^2(C_0\,dy\,d\phi)\right\|.
$$
直接 $E$ 部分满足
$$
 \|\tau^{-1}E\nabla W\|_{L^2(A^{-1})}
 \le\frac{\varepsilon}{\sqrt{1-\varepsilon}}{\cal G}_{11}.
                                                               \tag{S9}
$$
设 $a=\tau_{\min}^{-1}G\varepsilon$。$gE$ 源被
$a(y/H)^{11/2}|\nabla W|_{C_0}$ 控制。径向 Volterra 算子的
Hilbert–Schmidt 范数为
$$
 \left[\int_0^H\int_0^y(s/H)^{11}\,ds\,dy\right]^{1/2}
                   =H/\sqrt{156}.
$$
角向逆在所有非零四重模上至多 $(4q_-)^{-1}$，于是
$$
 \boxed{
 {\cal R}_E\le
 \frac{\varepsilon}{\sqrt{1-\varepsilon}}{\cal G}_{11}
 +\sqrt L\,a\left[
       \frac{H^2}{156}{\cal G}_0^2+
       \frac{{\cal G}_{10}^2}{(4q_-)^2H}
                \right]^{1/2}.}                           \tag{S10}
$$
径向均值和全部角输出均保留。两项 stream 的平方可相加，因为(S2)
使用对角的真实 inverse-density majorant；直接 $E$ 项再用三角不等式。
若后续需要保持输入侧强增益，可改用
$H{\cal G}_{10}/\sqrt6$ 控制径向 Volterra 部分；本次数值不依赖这一改进。

## 4. 从完整 Wiener 数据恢复有限角导数

令 $x=4q\phi$，$M_r(b)=\sum |k|^r|\widehat b_k|$。
R99 的各行给
$$
 N_{K,a,1}(b)=\sum |k|
       (1+|k|/(K+1))^a|\widehat b_k|.
$$
真实有限参考和它的完整系数误差分别为 $F_{K,a},E_{K,a}$。
因此
$$
 N_{K,a,1}\ge\max(0,F_{K,a}^{\rm lo}-E_{K,a}^{\rm up}).
                                                               \tag{S11}
$$
结合准确多项式恒等式
$$
 \begin{split}
 M_2&=(K+1)(N_{K,1,1}-N_{K,0,1}),\\
 M_3&=(K+1)^2(N_{K,2,1}-2N_{K,1,1}+N_{K,0,1}),
 \end{split}                                                   \tag{S12}
$$
正项取完整上界、负项取(S11)下界，得到严格上界。没有把两个上界相减。
对所有真实 $K$ 行取最小有效界；$v_1$ 摘要本来记录 $v_1/3$，
整个结果准确乘3。得到可用整数：
$$
 \begin{array}{c|rrrr}
 &M_0&M_1&M_2&M_3\\ \hline
 v_0&5176&1186&38571&15886958\\
 v_1&2076980&429337&17700807&14496863115 .
 \end{array}                                                   \tag{S13}
$$
这些数含完整 Fourier 尾、真实角图误差和整个参数盒；不是截断系数的样本矩。

## 5. 明确截断函数和全矩阵梯度预算

取 $\chi=1$ 于 $0\le y\le H/2$。在 $H/2\le y\le H$，
$u=2y/H-1$，置
$$
 \chi=1-10u^3+15u^4-6u^5,\qquad
 \chi'=-60u^2(1-u)^2/H ;
$$
$y\ge H$ 取0。两端的两阶 jets 匹配，足以零延拓上述弱解与通量。
对非负整数 $p$，
$$
 L_p=\int_0^H(y/H)^p|\chi'|^2dy
 =\frac{1800}{H\,2^p}
  \sum_{r=0}^p {p\choose r}\frac{(r+4)!\,4!}{(r+9)!}.
                                                               \tag{S14}
$$
特别 $L_0=20/(7H)$。这是准确的 $\chi'$ 费用，未以“平滑 cutoff”代替。

写 $F=c\operatorname{Ai}$，$c$ 与 R109 相同。第9节给出无需新数值
积分的改进初值夹：
$$
 .4<F(0)<.432,\qquad .295<-F'(0)<.306.
$$
对全部 $z\ge-1/4$，
$$
 |F|\le.513,\quad |F'|\le.323,\quad |F''|\le.224,\quad
 |F'''|\le.738.                                             \tag{S15}
$$
对 $z\ge0$，进一步有
$|F(z)|\le.432e^{-2z^{3/2}/3}$、
$\sup\sqrt z|F'(z)|<.335$、$\sup z|F(z)|<.224$。

以下给全部 lag 的预算，避免把逐列 norm 当成矩阵 norm。
令 $V_r,W_r$ 是(S13)，$\Lambda<4q(K+1)$、$l<\Lambda^{1/3}$。
置 $t=W_0/\Lambda^2<1/2$，$u<(1-t)^{1/3}$。
对 $a_j=(\lambda^2+v_1)^{1/3}$，
$$
 |a_j-\lambda^{2/3}|\le\lambda^{-4/3}A_0,\qquad
 |\partial_x^r a_j|\le\lambda^{-4/3}A_r\quad(1\le r\le3),
$$
其中
$$
 \begin{split}
 A_0&=W_0/(3u^2),\quad A_1=W_1/(3u^2),\\
 A_2&=W_2/(3u^2)+2W_1^2/(9u^5\Lambda^2),\\
 A_3&=W_3/(3u^2)+2W_1W_2/(3u^5\Lambda^2)
                         +10W_1^3/(27u^8\Lambda^4).
 \end{split}                                                 \tag{S16}
$$
设 $b_j=(1+v_1/\lambda^2)^{-2/3}$，其0至3阶导数上界可取
$$
 \begin{split}
 B_0&=u^{-2},\\
 B_1&=2W_1/(3u^5\Lambda^2),\\
 B_2&=2W_2/(3u^5\Lambda^2)+10W_1^2/(9u^8\Lambda^4),\\
 B_3&=2W_3/(3u^5\Lambda^2)+10W_1W_2/(3u^8\Lambda^4)
                              +80W_1^3/(27u^{11}\Lambda^6).
 \end{split}                                                 \tag{S17}
$$
定义
$$
 Z_r=HA_r+\sum_{k=0}^r{r\choose k}V_k B_{r-k}.
$$
则 $|Z_j-y\lambda^{2/3}|\le\lambda^{-4/3}Z_0$，
$|\partial_x^r Z_j|\le\lambda^{-4/3}Z_r$。所有真实根参数的负部
不超过 $S=V_0/(\Lambda l u^2)<1/4$。

对于任意符号族 $b_j(x)$，若0、2阶真实导数分别被 $b_0,b_2$ 统一控制，
则每个 lag 的共同包络为
$\min(b_0,b_2/|n-j|^2)$，所以
$$
 \|\operatorname{Op}(b_j)\|_{L^2\to L^2}
 \le b_0+\frac{\pi^2}{3}b_2
 < b_0+\frac{10}{3}b_2.                                  \tag{S18}
$$
这同时控制所有行和列。相同公式适用于两个频锥、低输出和均值。

记 $U^{\rm free}_j=\lambda^{-1/3}F(y\lambda^{2/3})e_j$，
$\Delta U=U^{\rm lin}-U^{\rm free}$。对
$\Delta U,\partial_y\Delta U,\lambda\Delta U,\partial_xU^{\rm lin}$
分别使用(S16)–(S18)，得到完整算子上界 $C_v,C_r,C_p,C_x$。
源码逐项展开；其0/2阶标量界准确为
$$
 \begin{array}{c|l|l}
 &0\text{阶}&2\text{阶}\\ \hline
 v&M_1Z_0\Lambda^{-5/3}
   &M_2Z_1^2\Lambda^{-3}+M_1Z_2\Lambda^{-5/3}\\
 r&M_1A_0\Lambda^{-5/3}+M_2Z_0\Lambda^{-1}
   &M_1A_2\Lambda^{-5/3}+2M_2A_1Z_1\Lambda^{-3}
      +(6/5)M_3Z_1^2\Lambda^{-7/3}
      +(6/5)M_2Z_2\Lambda^{-1}\\
 p&M_1Z_0\Lambda^{-2/3}
   &M_2Z_1^2\Lambda^{-2}+M_1Z_2\Lambda^{-2/3}\\
 x&M_1Z_1\Lambda^{-5/3}
   &M_3Z_1^3\Lambda^{-13/3}
       +3M_2Z_1Z_2\Lambda^{-3}+M_1Z_3\Lambda^{-5/3}.
 \end{array}                                                 \tag{S19}
$$
这里 $M_1=.323,M_2=.224,M_3=.738$ 是 Airy 导数界。
实际计算以严格 $l$ 付每个分数幂，不把小数立方根当成准确下界。
$4q<40$，故 canonical 角梯度费用是 $C_p+40C_x$。

自由 Airy 的全半线能量严格等于 $\operatorname{Ai}(0)^2<.36^2$。
当 $p>0$，(S15)给另一真界
$g_p=\sqrt{(.335^2+.224^2)/p}$；取 $g_0=.36$。因此
$$
 \boxed{
 {\cal G}_p\le g_p+
  \frac{.432}{l}\sqrt{L_p}
  +C_r\sqrt{\frac H{p+1}}
  +(C_p+40C_x)\frac H{\sqrt{p+2}}
  +C_v\sqrt{L_p}.}                                        \tag{S20}
$$
中间第二项和最后一项都是实际 $\chi'$ 项；其余用 $|\chi|\le1$。
所有量是完整输入到整个角圆的算子范数。

## 6. 实际上界：小的是 $E$，不是完整截断源

62个准确有理数门全部通过；下表向外放宽。

|$K$|$\mathcal G_0$|$\mathcal G_{10}$|$\mathcal G_{11}$|全部 $E$ gap|高根与 regular 联合 contact 的 $E$ 贡献|
|---:|---:|---:|---:|---:|---:|
|64|18.434422|5.567223|5.085185|.000449043991|.003601132576|
|128|5.623019|1.697508|1.551598|.000136920112|.001054558045|
|256|2.918597|.885949|.811130|.000071462239|.000535727775|

最后一列只用了同一完整帽的真实最小能量延拓：
$$
 \|\text{$E$-contact}\|_{H^{-1/3}_{>K}\oplus\mathbb C}
 \le \sqrt{E_K+E_{\rm reg}}\,{\cal R}_E .
$$
体内未作 Fourier 压缩，regular 槽仍存在。这里的 trial 输入范数是
$L^2$，尚未把数值升格为右乘 $\Gamma^2$ 后的强余项常数，也没有乘上
尚需接线的整个 incoming/outgoing frame 逆。

仅在 $K=256$，(S20)的自由 cutoff 项已为 $1.550449528$，
差解 cutoff 项为 $.795730914$。下面给一个下界，说明这个现象不能只靠
更精细的 triangle 估计消除。

## 7. 指定根数据的任何短域 compact pair 都有大 gap

选择单位输入 $e_J$，$J=K+1>0$。其真实频率
$\lambda=4qJ$ 满足 $\Lambda<\lambda<\Lambda^+=40J$。
设
$$
 \begin{gathered}
 a_-=(1-t)^{1/3}\text{的已付下界},\quad
 a_+=(1+t)^{1/3}\text{的已付上界},\\
 f_- =.4-.323S,\quad f_+=.432+.323S,\\
 b_- =.295-.224S,\quad b_+=.306+.224S,\quad
 T_0=1.477443,\quad M_\mu=24.940215 .
 \end{gathered}
$$
全部数值严格正，$F(Z)$ 在根介于 $f_-,f_+$，
$-F'(Z)$ 介于 $b_-,b_+$。由(S6)，去掉 $e_J$ 后的根 inward flux
是实负函数，且其绝对值至少
$$
 p_-=\frac{a_-l\,b_- - M_\mu f_+/l}{T_0}>0.               \tag{S21}
$$
因此 $p_0$ 的第 $J$ Fourier 系数绝对值至少 $p_-$。
$\Pi$ 只删第0行，不改变这个第 $J$ 系数。

现在允许任意完整合法 $(v,j)$，只要求：

- $v(0)=\tau_0U_J^{\rm lin}(0)$；
- $j$ 严格散度零，$j_y(0)=\Pi p_0$；
- $v$ 和 $j$ 在 $y\ge H$ 为零。

并不要求采用(S4)或某个特定 $\chi$。
由 $A\ge L^{-1}C_0$、$v(H)=0$，一维 Cauchy 给
$$
 E_v:=\int\nabla v^*A\nabla v
 \ge\frac{\tau_{\min}^2 f_-^2}
           {LH(\Lambda^+)^{2/3}}.                         \tag{S22}
$$
另一方面，$A^{-1}\ge\tau_{\min}^2C_0^{-1}/(1+\varepsilon)$。
散度零和 $j_y(H)=0$ 给第 $J$ 模
$\left|\int_0^H(j_\phi)_Jdy\right|
  =|(p_0)_J|/\lambda\ge p_-/\Lambda^+$。
再用权 $y$ 的 Cauchy，
$$
 E_j:=\int j^*A^{-1}j
 \ge\frac{2\tau_{\min}^2p_-^2}
          {(1+\varepsilon)H^2(\Lambda^+)^2}.               \tag{S23}
$$
均值及其余模只增加非负能量，不被删除。

完整 gap 恒等式准确为
$$
 {\cal R}^2=E_v+E_j+2\operatorname{Re}
                 \langle\tau_0U(0),\Pi p_0\rangle.        \tag{S24}
$$
height 在未去均值的根配对中准确消去。若 $m_K$ 是原 R109 已付
完整根均值上界，则
$$
 2\left|\langle\tau_0U(0),\Pi p_0\rangle\right|
 \le 2a_+ f_+b_+
      +\frac{2M_\mu f_+^2}{l^2}
      +\frac{2T_0f_+m_K}{l}.                              \tag{S25}
$$
最后一项专门保留 $\Pi$ 所产生的真实均值；它没有被默认为零。

将原 R109 的
$m_{64}<.319257441203$、
$m_{128}<.066876973974$、
$m_{256}<.028872948656$
代入，实际准确有理数预算给：

|$K$|$E_v$ 下界|$E_j$ 下界|(S25)上界|完整 $\mathcal R$ 下界|
|---:|---:|---:|---:|---:|
|64|.7433840062|3.4631910672|.4809072388|1.9301989106|
|128|.5971737075|3.2286778788|.3378770389|1.8676119906|
|256|.4029603795|1.6350577738|.2984673378|1.3189203219|

这些是整个实际参数盒上的严格不等式。
它们只限制上述短域 compact 比较法；真实调和帽解延伸到 $H$ 外，
不满足这里的紧支假设。因此本结论不能被转述成实际 DN 差大于该值、
帽反射不存在或非线性构造不可能。

## 8. 另一个已付真实系数：$V_2$

R87 物理多项式 $B_+$ 的准确根数据为
$B_+(0)=-v_0$、$(B_+)_y(0)=v_1/3$。它不等于体内的
$-v_0+yv_1/3$，所以必须保留差。写
$$
 D=V-B_+-2y(B_+)_y.
$$
R96 的完整报告分别支付
$\|D/y^2\|_{\operatorname{Mult}(H^{2/3})}$
和 $\|(B_+)_{yy}\|_{\operatorname{Mult}(H^{2/3})}$。
对后者的径向 Taylor 积分，严格有
$$
 \left\|\frac{B_+-B_+(0)-y(B_+)_y(0)}{y^2}\right\|
 \le\frac12\sup\|(B_+)_{yy}\|,\quad
 \left\|\frac{2((B_+)_y-(B_+)_y(0))}{y}\right\|
 \le2\sup\|(B_+)_{yy}\|.
$$
于是
$$
 \left\|V_2=\frac{V+v_0-yv_1}{y^2}\right\|_{\operatorname{Mult}(H^{2/3})}
 <2211544228.664430666+\frac52\,161752798.673799634
 <2615926225.348930.                                      \tag{S26}
$$
使用的是完整报告的 DB_without_Cphi 和 LB_normal，各自真实根阶
为2和0；没有把含 $2yC_\phi$ 的另一个系数混进来。
R96 的 $C^0/C^1$ 乘法插值同时控制正、负 $2/3$ 窗口。

(S26)是新的真实有限数字，但仍很粗。鉴于第7节的构造下界，接下来优先
延伸支持域/接真实外端，不再用它重复生成一个窄域的大 cutoff 源上界。

## 9. Airy 常数与精确执行方式

本次改进初值不依赖新的浮点 Gamma 调用。对 $a=1/3,2/3$，
$[0,1]$ 上指数的10阶偶 Taylor 和给
$$
 \int_0^1t^{a-1}e^{-t}dt
 \le\sum_{n=0}^{10}\frac{(-1)^n}{n!(n+a)}.
$$
对 $t\in[1,2]$，凸函数 $t^{-1/3}$ 被连接 $1,4/5$ 的直线控制，
$t^{-2/3}$ 被连接 $1,2/3$ 的直线控制；$t\ge2$ 分别用这些右端值。
以 $e^{-1}<(\sum_{n=0}^{10}1/n!)^{-1}$ 得
$$
 \Gamma(2/3)<1.371059106722,\qquad
 \Gamma(1/3)<2.712898273703 .
$$
结合 R96 的准确 Airy 初值公式和已付上界，得到
$.35<\operatorname{Ai}(0)<.36$、
$.25<-\operatorname{Ai}'(0)<.26$。因
$F(0)^2=\operatorname{Ai}(0)^3/[-\operatorname{Ai}'(0)]$、
$F'(0)^2=\operatorname{Ai}(0)[-\operatorname{Ai}'(0)]$，
遂得第5节的四个初值界。

在 $[-1/4,0]$ 上，设 $a=\sup|F|,b=\sup|F'|$。
一阶积分式给 $a\le.432+b/4$、$b\le.306+a/32$，
故 $a<.513,b<.323$。在正轴用 R109 已证衰减，
$F''=zF$、$F'''=F+zF'$，即得(S15)。
$e^{2/3}>157/81$ 足以支付全部展示的指数比较。
自由半线能量用 Airy 方程积分，边界衰减已由 R96 支付。

实际源：
scripts/fourfold_phase_paired_E_compact_gap_budget.mjs。

实际执行报告：
notes/2026-11-13-R109-paired-E-and-compact-gap-budget.json。

本次纯 BigInt 核在 functions.exec V8 执行器真实运行，62门全部通过；
Node 文件读取入口尚未运行，报告明确区别。上界正运算向上舍入到30位
十进制，平方/立方根在24位作整数包围；下界运算用准确有理数及向下舍入。
每个需要相减的 moment 采用(S11)，不是默认上界相减仍是上界。

六个小报告的完整 UTF-8 SHA 在本次运行中再次核验。
大型 R96 报告没有经工具重建；实际用到的两个 scalar_terms 来自已固定
Git blob 的 UTF-8 行范围，并在新报告保存原始完整球字符串、blob SHA、
原完整报告 SHA 和读取口径。Node 重放入口要求读取并核验原完整报告，
再提取相同两项。它不会用摘要数值伪造未取得的几何 cell。

## 10. 对下一步的准确含义

当前工作已把主矩阵项的导数膨胀改成了真实小的配对能量费用。
但当 $K=256$ 时，真实 Airy 尺度 $\lambda^{-2/3}$ 仍大于短截断宽度；
第7节已对这一具体构造给出可核验的数值限制。
后续应使用已经存在的较宽真实图或连续物理正帽证书，重新支付同一个
primal/dual 的延拓，或者按 R96 的完整外端 Wronskian接入真实 DN/regular
形式。后者必须保留外端 shear、全部低高耦合和 regular cross 项。
本补充既没有删去外端，也没有把当前 $L^2$ 能量常数冒称为完整强反馈逆。
