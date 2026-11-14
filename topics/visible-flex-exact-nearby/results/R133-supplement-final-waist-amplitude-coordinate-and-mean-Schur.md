# R133 补篇：最终腰部的全频振幅坐标与保留均值的参数 Schur 接口

2026-11-13。**已证明；第 1–4 节的实际有理预算已执行，23 个门全部通过。**
本篇使用最终完整 moving 候选索引中公开的准确腰部向量，证明真实物理
四次角模是一个有界局部坐标，并给出保持全部 mean 的补空间投影。
第 5–7 节把这条已支付的坐标接到完整参数 Schur 方程，明确尚须执行的
全频补逆与标量门。这里没有宣称实际 $\nu$ Schur 已经非零。

候选 SHA256：
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413。

公开重构文件：
[完整索引](../notes/2026-11-13-R133-moving-m32-alpha0765-fullR-v2-tol2e9-reconstruction.json)，
SHA256 为
464480dee60749f019b23a89b04568bf496731a580c21a3e761d4bc2192e108a。
本篇消费其中完整 65 维 initial_state，所有 binary64 数按其准确
dyadic 有理数解释。没有从失联环境重造五个径向分片，也没有把端点
结论冒充整个 PPoly 或完整 PDE 的验证。

## 1. 准确腰部输入和包含全部未知尾的邻域

实际 $\alpha=6890507429876859/9007199254740992$。腰部目标准确有
$a'(0)=0$，因此旋转倒曲率背景 $s(0)=-a_0$。紧支 $\nu$ 控制在腰部
恒为零，所以这里不引入新的度量参数误差。

原 [R127 原生报告](../notes/2026-11-13-Codazzi-continuation-r001-v3-native.json)
的第一个完整闭盒
$[0,1152921504606847/73786976294838206464]$ 已包含原
$|\eta|\le10^{-9}$ 全参数盒和完整 primitive 尾。其严格端点为

$$
 a>1.0687328210563735580995725626962667-1.35\,10^{-35},
$$
$$
 a<1.0687328409354375363671252330277639+2.45\,10^{-36}.
$$

R128 已绑定这个完整报告的 SHA256
0f7aa2f4e9a1df567b209cd873f2af5f6428feafc01a9613fc75a46259fb75eb；
当前 Git blob 为 1c0abbebb166c6b85a87cb52b4aeab8378567b4c。
我们只消费其内蕴 $a_0$ 界，不转授旧 Cauchy 曲线、旧非径向中心或
旧逆常数。于是完整使用较粗的有理盒

$$
 1.06873282<a_0<1.068732841.                              \tag{A.1}
$$

记实际索引中的偶系数为 $V_0,\ldots,V_{32}$，定义

$$
 v_c(\phi)=-a_0+\alpha\sum_{j=0}^{32}V_j\cos(4j\phi).
$$

令 $\mathcal A^0$ 为完整四重周期 Fourier Wiener 代数，
$\|f\|_{\mathcal A^0}=\sum_{k\in4\mathbb Z}|\widehat f_k|$。
在整个实偶对称邻域

$$
 \|v-v_c\|_{\mathcal A^0}\le\rho=10^{-6}                 \tag{A.2}
$$

上考虑问题。未知扰动包含所有角频率和独立 mean，不要求仍只有 32 模。
$u$ 的奇对称分量不参与下面的曲率振幅泛函，故不因选坐标而删除。

设 $m=\langle v\rangle_\phi$。实际有理预算给

$$
 -v>0.0833357128,\qquad -m>1.0687318199>1.              \tag{A.3}
$$

这些是整个 (A.2) 上的逐角界；完整尾已进入其中。因此

$$
 \theta(\phi)=\phi+\frac{I(v-m)}m,\qquad
 \theta_\phi=v/m>0                                    \tag{A.4}
$$

是圆周一次定向 $C^1$ 微分同胚。$I=\partial_\phi^{-1}P_{\ne0}$ 取
零平均原函数；即使未知 $v$ 只在 $\mathcal A^0$，(A.4) 仍有上述意义。

## 2. 真正物理振幅行的全角导数

物理曲率 $C=1/v$ 的实余弦四次振幅准确为

$$
 \mathcal A(v)=2\widehat C_4
       =\frac2m\left\langle\cos(4\theta(\phi))\right\rangle_\phi.
                                                               \tag{A.5}
$$

原平均是在物理 $\theta$ 中；代入
$d\theta=(v/m)d\phi$ 后恰好约去 $1/v$，所以 (A.5) 不是把 moving
Fourier 系数当物理 Fourier 系数。

取 $e(\phi)=\cos(4\phi)$。它的 mean 为零，因此
$D m[e]=0$、$D\theta[e]=\sin(4\phi)/(4m)$，从而

$$
 D\mathcal A(v)[e]
  =-\frac2{m^2}
    \left\langle\sin(4\theta(\phi))\sin(4\phi)\right\rangle_\phi.
                                                               \tag{A.6}
$$

令 $x=4\phi$，把全部实际相位写成

$$
 4\theta=x-\tau\sin x+\varepsilon(x),\qquad
 \tau=-\frac{v_1}{m}>0.
$$

完整 (A.2) 给

$$
 0.910562946674295055<\tau<0.910566539949655033,\qquad
 \|\varepsilon\|_\infty<0.005148081755132427.            \tag{A.7}
$$

具体地，$m_-=a_- -\alpha V_0-\rho$、
$m_+=a_+ -\alpha V_0+\rho$ 满足

$$
 \frac{\alpha V_1-\rho}{m_+}\le\tau
 \le\frac{\alpha V_1+\rho}{m_-},\qquad
 \|\varepsilon\|_\infty
 \le\frac{\alpha\sum_{j=2}^{32}|V_j|/j+\rho/2}{m_-}.
                                                               \tag{A.8}
$$

最后的 $\rho/2$ 来自未知全部 $j\ge2$ 模的 $1/j\le1/2$；
未知 mean 和第一模分别已经进入 $m_\pm,\tau$。

准确积分恒等式是

$$
 \left\langle\sin(x-\tau\sin x)\sin x\right\rangle
     =\frac{J_0(\tau)-J_2(\tau)}2.                      \tag{A.9}
$$

可将两个正弦之积写成余弦之差，再展开指数 Taylor 级数逐项积分证明。
本篇所用函数由完整绝对收敛级数定义：

$$
 J_\ell(t)=\sum_{n=0}^{\infty}
  \frac{(-1)^n(t/2)^{2n+\ell}}{n!(n+\ell)!},
 \qquad\ell=0,2.                                      \tag{A.10}
$$

每个级数实际求了前 16 项的准确有理区间。若 $t\le t_+<1$，
第 $N$ 项起的完整余项模不超过

$$
 \frac{(t_+/2)^{2N+\ell}}{N!(N+\ell)!}
 \left(1-\frac{t_+^2}{4(N+1)(N+\ell+1)}\right)^{-1}.    \tag{A.11}
$$

由 $|\sin(a+b)-\sin a|\le|b|$，加入 (A.8) 完整角费用，实际得到

$$
 0.348127314218383820
 <\left\langle\sin(4\theta)\sin(4\phi)\right\rangle
 <0.358424851205563383 .
$$

所以整个 (A.2) 和原 whole-$\eta$ 盒上

$$
 \boxed{-0.627611118976129017
   <D\mathcal A(v)[e]
   <-0.609577561809481048.}                            \tag{A.12}
$$

严格较粗有理门为 $-2/3<D\mathcal A[e]<-3/5$。
实际有限求解器使用
$c_4=C_4^{\cos}/\alpha$ 和 normalized $V_1$；
由于 $\partial_{V_1}v=\alpha e$，
它的该列导数也准确等于 (A.6)，不欠 $\alpha$ 因子。

## 3. 保持 mean 的完整无限维投影

写 $\ell_v=D\mathcal A(v)$。完整 $\mathcal A^0$ 上

$$
 \|\ell_v\|
 \le\frac2{m_-^2}\left(1+\frac{\|v_{\ne0}\|_{\mathcal A^0}}{m_-}\right)
 <3.3655145614<\frac72.                               \tag{A.13}
$$

对任意 $h$，$z=\langle h\rangle$ 有
$D\theta[h]=m^{-1}I(h-zv/m)$。
(A.5) 的分母微分贡献 $|z||\mathcal A|/|m|$，其中
$|\mathcal A|\le2/|m|$。余项用
$\|Ih_{\ne0}\|\le\|h_{\ne0}\|/4$ 和
$\|I(zv_{\ne0}/m)\|\le|z|\|v_{\ne0}\|/(4|m|)$。
最后 $|z|+\|h_{\ne0}\|=\|h\|$，得到 (A.13)，没有设 mean 为零。

准确定义

$$
 \mathcal E_v(t)=\frac{t}{\ell_v[e]}e,\qquad
 P_vh=h-\mathcal E_v(\ell_v[h]).                        \tag{A.14}
$$

则 $\ell_vP_v=0$、$P_v^2=P_v$，
$P_v$ 保持每个输入的 mean 不变。全部高模仍存在；只沿一个真正
四次模方向补偿振幅。实际预算给

$$
 \|\mathcal E_v\|_{\mathbb R\to\mathcal A^0}
 <1.6404803304<5/3,\qquad
 \|P_v\|_{\mathcal A^0\to\mathcal A^0}<6.52106044<7 .
                                                               \tag{A.15}
$$

同时保留奇分量时用
$(h_1,h_2)\mapsto(h_1,P_vh_2)$，不改变 $h_1$ 或 $h_2$ 的 mean。

完整 $H^1$ 范数满足
$\|h\|_{H^1}^2=\sum_{k\in4\mathbb Z}(1+k^2)|\widehat h_k|^2$，
$\|e\|_{H^1}^2=17/2<9$。含 mean 的
$H^1\to\mathcal A^0$ 常数小于 $11/10$，故同一预算给

$$
 \|P_v\|_{H^1\to H^1}<19.21949946<20.                   \tag{A.16}
$$

这是完整无限维边界坐标结论，不假设尚未证明的体区逆。
若把边界 lift 延伸为径向函数，其真实 PDE 源仍须支付；
(A.15) 没有免费授予径向延伸的算子范数。

## 4. 实际执行与范围

源为
[scripts/fourfold_codazzi_waist_amplitude_chart.mjs](../scripts/fourfold_codazzi_waist_amplitude_chart.mjs)，
报告为
[23 门完整有理预算](../notes/2026-11-13-R133-final-waist-amplitude-chart-rational.json)。
完整计算函数已在当前可用 V8 环境执行，23 个严格有理门全过；
仅用 BigInt 精确算术、dyadic 解码和有理区间，没有浮点求积或库 Bessel。

~~~bash
node scripts/fourfold_codazzi_waist_amplitude_chart.mjs \
  notes/2026-11-13-R133-moving-m32-alpha0765-fullR-v2-tol2e9-reconstruction.json
~~~

源先核完整重构文件 SHA，再核候选、模式、坐标、准确振幅和完整
65 维初值身份。原 $a_0$ 已证界按原记录完整中心/半径作有理比较后
消费；没有把复用内蕴结论称为本次重新运行原求值器。
Node 包装入口尚未在失联本地环境运行；实际 23 门由同一源码中
完整 calculate 函数在 V8 执行。

端点对象是索引中记录的完整腰向量。本篇不验证不可读径向分片字节，
不从有限求解收敛推出真 PDE，也不把 (A.12) 称为 $\nu$ 分岔横截。

## 5. 完整低标量的正确保留方式

令 $\mathcal R(Q,\nu,\alpha;\mathfrak e)$ 是全空间残差。体方程为
准确未规范化 moving 系统，$\mathfrak e$ 保留真正外尾输入。
腰条件为所有 $u(0,\phi)=0$ 和
$\mathcal A(v(0))+\alpha=0$；外端保留完整真实 regular 非mean
关系及独立 physical mean 行。$\alpha$ 只选择需要的物理振幅；
固定最终 $\alpha,\nu$ 后的相位弯曲族才使用同一度量。

从完整外端 real $m=4$ Robin 行中选出标量 $b_4$，其线性参考为
$B_4^{\sin}+q_4 C_4^{\cos}$。**只把这一行暂列为输出**，保留其
全部真实非线性外端修正；其余所有非mean 行、mean 行、腰奇条件
和物理振幅行组成 $\overline{\mathcal R}$。记

$$
 \overline A=D_Q\overline{\mathcal R},\qquad
 g_\nu=D_\nu\overline{\mathcal R},\qquad b=D_Q b_4.       \tag{A.17}
$$

(A.12)–(A.16) 支付振幅行的局部坐标选择，并未证明
$\overline A$ 可逆；后者仍须真正负段、turning、正区/外帽与完整
高频返回联立，不能从有限矩阵秩转授。

未规范化固定 $Q$ 时，$g_\nu$ 体列是 $-\partial_\nu F$。
紧支控制在两端为零，故 curvature 边界显式 $\nu$ 列为零；
这不删除体源 mean。normalized $u=\alpha U,v=s+\alpha V$ 的完整列是

$$
 (0,s_\nu)_r-DF(0,s_\nu)-\partial_\nu F.                \tag{A.18}
$$

有限求解器 curvature 行除以 $\alpha$，腰 $u$ 行也按 $U=u/\alpha$
储存。其 Schur 数与 (A.17) 比较必须保留这些准确尺度。

## 6. mean 方程与标量 Schur，不作免费消去

写 $h=(\xi,\zeta)$、$z=\langle\zeta\rangle$，
$m=\langle v\rangle$、$S=u^2+Kv^2$。完整线性化第二平均为

$$
 z'=\beta(1-\langle S\rangle)z
 -2\beta m\langle u\xi+Kv\zeta\rangle
 -\beta mK_\nu\langle v^2\rangle\,\delta\nu
 +\langle f_2\rangle .                               \tag{A.19}
$$

这里 $K_\nu=-wK+\beta w'/(2E_\nu)$；控制虽支于内侧，第三项不能删除。
设 $\zeta_0=\zeta-z$，则同式准确改写为

$$
 z'=c_mz+g_m,\qquad
 c_m=\beta(1-\langle S\rangle-2Km^2),                   \tag{A.20}
$$
$$
 g_m=-2\beta m\langle u\xi+K(v-m)\zeta_0\rangle
 -\beta mK_\nu\langle v^2\rangle\,\delta\nu+\langle f_2\rangle.
$$

若需消元，只允许按完整积分

$$
 z(r)=e^{\int_R^r c_m}z(R)
       -\int_r^R e^{\int_t^r c_m}g_m(t)\,dt             \tag{A.21}
$$

进行；非mean、参数列和 mean 源全部仍在。
外端 $C_0=1/m$ 的微分是 $-z(R)/m(R)^2$，还要联立真外帽 mean
函数的完整导数。不能先设 $z(R)=0$，也不能在尚未完整拼接周期帽时
免费设 $z(0)=0$。

若已支付 $\overline A^{-1}$，对完整右侧
$(f_{\rm bar},f_4)$，令

$$
 h_0=\overline A^{-1}f_{\rm bar},\qquad
 h_\nu=-\overline A^{-1}g_\nu,\qquad
 \mathscr S_\nu=b[h_\nu].                              \tag{A.22}
$$

完整 bordered 解准确是

$$
 \delta\nu=\frac{f_4-b[h_0]}{\mathscr S_\nu},\qquad
 h=h_0+h_\nu\delta\nu.                                \tag{A.23}
$$

这才是仍须实际验证非零的 $\nu$ 标量；$h_\nu$ 的 mean 由 (A.19)
沿全体区传播，不能从 (A.12) 推出 $\mathscr S_\nu\ne0$。

未规范化方程里 $\alpha$ 显式源只有振幅行的 $+1$。
若同时支付 $h_\alpha=-\overline A^{-1}e_{\rm amp}$，则真解支斜率为

$$
 \nu'(\alpha)=-\frac{b[h_\alpha]}{\mathscr S_\nu}.        \tag{A.24}
$$

它可接真实两程 ray-return 参数源；不能单独冒充高频算术条件。

## 7. 已付端口误差进入真实标量的方式

设一个已认证参考补逆为 $\overline A_0^{-1}$，
实际算子为 $\overline A_0+\Delta A$，
$g_\nu=g_{\nu,0}+\Delta g_\nu$、$b=b_0+\Delta b$。
这些差必须包括完整 primitive、PPoly 接缝、真正 cap 的 proposal
差与非线性导数，且使用同一个全频空间。

若 $\epsilon=\|\overline A_0^{-1}\Delta A\|<1$，
$h_{\nu,0}=-\overline A_0^{-1}g_{\nu,0}$，则

$$
 \|h_\nu-h_{\nu,0}\|
 \le\frac{\|\overline A_0^{-1}
        (\Delta g_\nu+\Delta A\,h_{\nu,0})\|}{1-\epsilon}
 =:E_\nu,                                             \tag{A.25}
$$
$$
 |\mathscr S_\nu-b_0[h_{\nu,0}]|
 \le\|b_0\|E_\nu+\|\Delta b\|(\|h_{\nu,0}\|+E_\nu).
                                                               \tag{A.26}
$$

最终严格门是参考标量的模大于 (A.26) 完整费用。
外端极小原始残差不能代替这个相对算子比较。
本篇完成实际振幅行全频横截、mean 保持的定量坐标和全边界参数接口；
体区逆、$\nu$ 标量符号、外尾方程和全闭面目标仍须继续完成。
