# R150 附录：一个正时间半群与有限正预解积的混合分母完整行分类

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf / kernel_resume_1cf；AI 辅助：GPT-6 Astra Pro。三方独立推导同一接口，根与 kernel 已分别完整核验共同词域及统一整逆像。

状态：已证明。一个固定正时间半群、固定有限正锚族和固定有限预解次数；不将半群像误当成其生成元的全域。

## 1. 主定理

固定
$$
a\in\ell^2,\quad a_j\ge0,\qquad
b^\nu\in\ell^2,\quad b^\nu_j\ge0
\quad(1\le\nu\le q),
$$
其中 $q\ge0$ 有限；允许任意这些行是零行或绝对可和行。
记实际第一阶乘子及半群
$$
X=X_a,\qquad B_\nu=X_{b^\nu},\qquad S_a(t)=e^{-tX}.
$$
固定参数
$$
t>0,\qquad s_\nu>0,\qquad N_\nu\ge1,
$$
并定义实际有界交换子
$$
\boxed{
R=S_a(t)\prod_{\nu=1}^q(I+s_\nu B_\nu)^{-N_\nu}.
}
\tag{1.1}
$$
$q=0$ 时空乘积为 $I$。
置非负总权
$$
w_j=a_j+\sum_{\nu=1}^q b^\nu_j,
\tag{1.2}
$$
以及
$$
\mathscr J_w
=\ell^1+
\left\{d:d_j=0\ (w_j=0),\
\sum_{w_j>0}|d_j|^2/w_j<\infty\right\}.
\tag{1.3}
$$

对任意复 $c\in\ell^2$，令 $Y=Y_c$。
以下条件等价：

1. $RH\subseteq\operatorname{Dom}Y$。
2. 自然 $YR$ 的域为全 $H$，且有界。
3. 存在 $\gamma_1,\ldots,\gamma_q\in\mathbb C$，使
   $$
   \boxed{
   c-\sum_{\nu=1}^q\gamma_\nu b^\nu\in\mathscr J_w.
   }
   \tag{1.4}
   $$

自然 $YR$ 总是闭且稠密定义；
它有一个全域有界延拓，当且仅当上述条件成立。
条件 (1.4) 不依赖所选固定正 $t,s_\nu$ 和固定正整数 $N_\nu$。
所以只要其中一组参数全域有界，就对全部这些固定参数组全域有界；这不声称统一的参数范数界。

半群主行 $a$ 贡献总权，却没有被免费加入线性斜率空间。
特别，$q=0$ 恰是已推
[正时间半群分类](R150-appendix-positive-time-semigroup-first-domain-classification.md)；
$a=0$ 恰是有限正预解积的同一行分类。
不把这两端的已有结果重复计作独立结论。

## 2. 预备：真实闭域与总占据形式

对非负行 $v\in\ell^2$，定义占据算子
$$
\mathcal N_v\chi_F
=\left(\sum_{j\in F}v_j\right)\chi_F.
$$
实际第一阶分解为 $X_v=X_v^0+E_v$，
其中
$$
\|E_v\|\le\kappa\|v\|_2,\qquad
\kappa=8\|\eta\|_2.
$$
有限柱上的真实二次型等式是
$$
2\|\mathcal N_v^{1/2}f\|^2
=\operatorname{Re}\langle X_vf,f\rangle
-\operatorname{Re}\langle E_vf,f\rangle.
\tag{2.1}
$$

这条等式延到完整 $\operatorname{Dom}X_v$，并且
$$
\operatorname{Dom}X_v\subseteq
\operatorname{Dom}\mathcal N_v^{1/2}.
\tag{2.2}
$$
具体取有限柱 $f_n$ 在 $X_v$ 图范数下逼近 $f$。
将 (2.1) 用于 $f_n-f_m$，其右侧绝对值由
$$
\|X_v(f_n-f_m)\|\|f_n-f_m\|
+\|E_v\|\|f_n-f_m\|^2
$$
控制并趋零。
故 $\mathcal N_v^{1/2}f_n$ Cauchy；闭性付域，随后原等式取极限。

若 $d$ 是 (1.3) 中的加权行，记
$$
K_d^2=\sum_{w_j>0}|d_j|^2/w_j.
$$
实际产生、消灭、占据及 carry 估计给
$$
\boxed{
\operatorname{Dom}\mathcal N_w^{1/2}
\subseteq\operatorname{Dom}Y_d,\qquad
\|Y_df\|
\le4K_d\|\mathcal N_w^{1/2}f\|
+(1+\kappa)\|d\|_2\|f\|.
}
\tag{2.3}
$$
这是半群分类稿 §4 在总权 $w$ 上的同一个估计：
先在有限柱上用加权 Cauchy–Schwarz，
再以 $\mathcal N_w^{1/2}$ 的有限柱图核心及 $Y_d$ 闭性延到形式域。
不要求 $f$ 在 $X_w$ 的域中。

## 3. 充分性：各锚域加上半群形式域

记
$$
Q=\prod_{\nu=1}^q(I+s_\nu B_\nu)^{-N_\nu}.
$$
每个预解因子和 $S_a(t)$ 都是 $A'$ 中的收缩；
它们保持每个实际第一阶完整域，并在域上交换。
因每条预解锚至少出现一次，
$$
RH\subseteq\operatorname{Dom}B_\nu,\qquad
B_\nu R\in B(H).
\tag{3.1}
$$
例如保留第 $\nu$ 个因子一次，使用
$$
B_\nu(I+s_\nu B_\nu)^{-1}
=s_\nu^{-1}[I-(I+s_\nu B_\nu)^{-1}].
$$
可取粗界 $\|B_\nu R\|\le2/s_\nu$；零行时当然可取0。

半群分类稿的真实 Duhamel 平滑给
$$
\|\mathcal N_a^{1/2}S_a(t)\|
\le H_a(t):=t^{-1/2}+2\|E_a\|\sqrt t.
$$
由于 $Q$ 收缩，
$$
\|\mathcal N_a^{1/2}R\|\le H_a(t).
\tag{3.2}
$$
对各 $b^\nu$，将 (2.1)—(2.2) 用于 $Rh$，并使用 $\|R\|\le1$，得到
$$
\|\mathcal N_{b^\nu}^{1/2}R\|^2
\le\frac12\|B_\nu R\|+\frac12\|E_{b^\nu}\|.
\tag{3.3}
$$
总占据形式是有限个非负形式的和，故
$$
\boxed{
RH\subseteq\operatorname{Dom}\mathcal N_w^{1/2},\qquad
\|\mathcal N_w^{1/2}R\|^2
\le H_a(t)^2+
\frac12\sum_\nu
\bigl(\|B_\nu R\|+\|E_{b^\nu}\|\bigr).
}
\tag{3.4}
$$
这里没有声称 $RH\subseteq\operatorname{Dom}X$。

设条件 (1.4) 成立，即
$c=\sum_\nu\gamma_\nu b^\nu+e+d$。
由 (3.1)、(3.4) 和 (2.3)，$R$ 的像同时进入全部 $B_\nu$ 与 $Y_d$ 的域；
$Y_e$ 全域有界。
实际第一阶的线性等式于是给
$$
YRh=\sum_\nu\gamma_\nu B_\nu Rh+Y_eRh+Y_dRh.
\tag{3.5}
$$
域依据也可直接表述为：
对有限族 $B_\nu,Y_d$，R186 给有限柱共同图核心；
用它逼近任意共同域向量，核心上的系数和等式右侧收敛，
再用 $Y$ 闭性识别左侧。
不预设无界自然和已经闭。

于是 $YR$ 自然全域有界，并有明确上界
$$
\begin{aligned}
\|YR\|
\le{}&
\sum_\nu|\gamma_\nu|\|B_\nu R\|+6\|e\|_1\\
&+4K_d
\left[
H_a(t)^2+
\frac12\sum_\nu
\bigl(\|B_\nu R\|+\|E_{b^\nu}\|\bigr)
\right]^{1/2}
+(1+\kappa)\|d\|_2.
\end{aligned}
\tag{3.6}
$$

## 4. 必要性所用的共同核两态

取实有限支撑 $\theta$，满足
$$
\|\theta\|_\infty\le1,\qquad
\sum_jw_j\theta_j^2\le1,\qquad
\sum_jb^\nu_j\theta_j=0
\quad(1\le\nu\le q).
\tag{4.1}
$$
只限制预解锚的线性核；不限制 $\sum_j a_j\theta_j$。

取单位有限乘积态
$$
\xi(\theta)=\bigotimes_j
\left(\cos\beta_j\,1+i\sin\beta_j\,\chi_j\right),
\qquad
\beta_j=-\tfrac12\arcsin\theta_j.
$$
令 $v(x)=1-\sqrt{1-x^2}$。其纯局部期望为 $v(\theta_j)+i\theta_j$。
主行与预解行的中心分别是
$$
\alpha=\sum_j a_j[v(\theta_j)+i\theta_j],
\qquad
\delta_\nu=\sum_j b^\nu_jv(\theta_j).
$$
由 (4.1)，
$$
\boxed{
0\le\operatorname{Re}\alpha\le1,\qquad
0\le\delta_\nu\le1.
}
\tag{4.2}
$$
$\operatorname{Im}\alpha$ 不要求有界。
对 $-\theta$ 同样成立。

置
$$
T_a=X-\alpha I,\qquad
T_\nu=B_\nu-\delta_\nu I.
$$
下面必须同时控制 $T_a$ 的正向整级数与固定 $T_\nu$ 词，
而不能把有界正向逆像直接送进未付清的多锚自然域。

## 5. 同一参考态尺度上的真实混合整预算

### 5.1 任意固定混合词

在以 $\xi(\theta)$ 为真空的指数激发空间
$$
H_\tau(\theta)=\operatorname{Dom}e^{\tau\mathcal N_\theta},
\qquad0\le\tau\le1,
$$
正时间半群分类稿 §5 对任意实际系数行 $v$ 给同一个估计
$$
\|(X_v-\text{其纯均值}):
H_\tau(\theta)\to H_{\tau-\varepsilon}(\theta)\|
\le C_*\|v\|_2\,\varepsilon^{-1/2},
\quad0<\varepsilon\le\tau.
\tag{5.1}
$$
纯中心化块在激发次数上只有产生、消灭和占据三个部分；
真实 carry 字串支撑 $L+1$ 位，指数权代价至多 $e^{L+1}$，
其级数由 $e\eta_*<1$ 绝对收敛。
因此常数对全部局部参考态及其有限支撑统一；
所有映射都由原闭 first 与指数权的闭性识别。

给任意预解锚有序词 $T_{\nu_1}\cdots T_{\nu_p}$ 及 $k\ge0$，
取 $k+p$ 步、每步损失 $1/(k+p)$。
从相对真空的 $H_1$ 范数1出发，得到实际自然域及
$$
\boxed{
\|T_{\nu_1}\cdots T_{\nu_p}T_a^k\xi(\theta)\|
\le
\bigl(C_*\sqrt{k+p}\bigr)^{k+p}
\|a\|_2^k\prod_{\ell=1}^p\|b^{\nu_\ell}\|_2.
}
\tag{5.2}
$$
$k+p=0$ 时为范数1。
任意顺序的混合词同样成立，因为逐步尺度估计不需要先交换无界词。
零系数行使相应中心算子为0，与此界一致。

### 5.2 正向整逆像同时进入所有固定预解词域

令
$$
F_\theta(t)=
e^{t\alpha}
\sum_{k=0}^\infty\frac{t^k}{k!}T_a^k\xi(\theta).
\tag{5.3}
$$
半群分类稿已给
$$
S_a(t)F_\theta(t)=\xi(\theta).
\tag{5.4}
$$
现在进一步支付预解词。
对每个固定 $p$，(5.2) 给
$$
\sum_{k=0}^\infty
\frac{t^k}{k!}
\bigl(C_*\sqrt{k+p}\bigr)^{k+p}
\|a\|_2^k\prod_{\ell=1}^p\|b^{\nu_\ell}\|_2<\infty.
\tag{5.5}
$$
其 $k$ 次根最终为 $O(k^{-1/2})$，所以收敛；
常数不依赖 $\theta$。
又 $|e^{t\alpha}|\le e^t$。
用 $B_\nu=T_\nu+\delta_\nu I$、$|\delta_\nu|\le1$ 展开，
同一结论也控制每个固定 $B_\nu$ 词。

这确实给全部所需自然域。
对 (5.3) 的部分和，同时记录长度至多 $m$ 的所有 $B_\nu$ 词；
(5.5) 说明每个记录都收敛。
R186 的完整共同词图是完备的，
等价地可按每个中间词逐次用单个 $B_\nu$ 的闭性。
所以 $F_\theta(t)$ 属于这些真实共同词域，且词的作用可逐项取极限。
没有把一般自然多项式或一般自然复合预设成闭算子。

## 6. 固定多项式预像与准确取消

令
$$
m=\sum_\nu N_\nu,\qquad
P_b=\prod_{\nu=1}^q(I+s_\nu B_\nu)^{N_\nu},
$$
按固定顺序在完整共同 $m$ 阶词域上使用。
§5 给 $F_\theta(t)$ 在该域内，并且
$$
\boxed{
\sup_{\theta\text{ 满足 }(4.1)}
\|P_bF_{\pm\theta}(t)\|<\infty.
}
\tag{6.1}
$$
这里的常数可以依赖全部固定行、时间与次数，但不依赖有限测试支撑。

有界预解保持各 first 的完整域，并在域上交换。
因此在这些已经付清的共同词输入上逐个取消匹配因子，得到
$$
Q P_bF_{\pm\theta}(t)=F_{\pm\theta}(t).
$$
再用 (5.4)，
$$
\boxed{
R\,[P_bF_{\pm\theta}(t)]=\xi(\pm\theta).
}
\tag{6.2}
$$
不声称 $P_b$ 在整个 $H$ 上自然定义，也不在本稿把它识别成某个全空间闭逆。

假设自然 $YR$ 全域有界。
(6.1)—(6.2) 立即给
$$
\sup_{\theta\text{ 满足 }(4.1)}
\|Y\xi(\pm\theta)\|<\infty.
\tag{6.3}
$$
纯辅助行两次期望之差为 $2i\sum_jc_j\theta_j$；
真实有界 carry 各付一次范数，故
$$
\boxed{
\left|\sum_jc_j\theta_j\right|\le C
\quad\text{对全部 }(4.1)\text{ 的 }\theta.
}
\tag{6.4}
$$

## 7. 有限维消元给准确系数类

定义
$$
\mathscr E_w=c_0\cap\ell^2(w),\qquad
\|z\|_{\mathscr E_w}
=\max\left(\|z\|_\infty,
\sqrt{\sum_jw_j|z_j|^2}\right).
$$
在有限列上置
$$
T(z)=\left(\sum_jb^\nu_jz_j\right)_{\nu=1}^q,
\qquad C_0(z)=\sum_jc_jz_j.
$$
(6.4) 经齐次性和实虚分开，
使 $C_0|_{\ker T}$ 是 $\mathscr E_w$ 范数下的有界复泛函。

直接用复 Hahn–Banach 将其延拓为 $\ell\in\mathscr E_w^*$；
不需要 $\ker T$ 在 $\mathscr E_w$ 中稠密。
于是 $C_0-\ell$ 在有限列上消掉 $\ker T$，
降为有限维 $\operatorname{Ran}T\subseteq\mathbb C^q$ 上的线性泛函。
取其有限维延拓，存在 $\gamma_\nu$ 使
$$
C_0(z)-\ell(z)=
\sum_\nu\gamma_\nu\sum_jb^\nu_jz_j.
\tag{7.1}
$$
这个步骤不把 $T$ 误认为整个 $\mathscr E_w$ 上的连续算子。

等距嵌入
$$
z\mapsto(z,\sqrt w\,z)
\quad\text{于 }c_0\oplus_\infty\ell^2
$$
并再次用 Hahn–Banach，得到
$$
\ell(z)=\sum_je_jz_j+\sum_j\zeta_j\sqrt{w_j}\,z_j,
\qquad e\in\ell^1,\quad\zeta\in\ell^2.
$$
对坐标向量比较 (7.1)，给
$$
c=\sum_\nu\gamma_\nu b^\nu+e+d,\qquad
d_j=\sqrt{w_j}\zeta_j.
$$
这正是条件 (1.4)。
所以必要性也已完成。

## 8. 自然闭图、边界与可检查形式

自然域是
$$
\operatorname{Dom}(YR)=\{h:Rh\in\operatorname{Dom}Y\}.
$$
$R$ 有界、$Y$ 闭，故 $YR$ 闭。
由于 $R\in A'$，取 R186 正则器 $J_\varepsilon$，
满足 $J_\varepsilon H\subseteq\operatorname{Dom}Y$、
$J_\varepsilon\to I$ 强。
$R$ 保持 $\operatorname{Dom}Y$，所以
$J_\varepsilon H\subseteq\operatorname{Dom}(YR)$；
自然域稠密。
闭图定理给条件1与2等价。
若自然图有全域有界延拓，按域内稠密逼近和闭性，也迫它原本就全域。

对任意给定 $\gamma$，令 $z=c-\sum_\nu\gamma_\nu b^\nu$。
条件 $z\in\mathscr J_w$ 准确等价于
$$
\boxed{
\sum_{w_j=0}|z_j|
+\sum_{w_j>0}
\min\!\left(|z_j|,\frac{|z_j|^2}{w_j}\right)<\infty.
}
\tag{8.1}
$$
证明是在正位按 $|z_j|>w_j$ 分割到可和部分，其余放入加权平方部分；
反向用
$\min(|e+d|,|e+d|^2/w)\le2|e|+4|d|^2/w$。
零位全部由可和部分承担。

$\gamma$ 一般不唯一。
若 $\gamma^0$ 可行，全部可行向量为
$$
\gamma^0+
\left\{\delta\in\mathbb C^q:
\sum_\nu\delta_\nu b^\nu\in\mathscr J_w\right\}.
\tag{8.2}
$$

若全部总权可和，(1.4) 退化为 $c\in\ell^1$；
这与所有分母因子都是有界单位一致。
若只有半群行 $a$ 可和，也有
$\mathscr J_{a+\sum b^\nu}=\mathscr J_{\sum b^\nu}$：
对加权余项按权比例拆成 $d_a=d\,a/w$ 和
$d_b=d\,(\sum b^\nu)/w$，前者由 Cauchy–Schwarz 可和，后者保相应加权平方界。
故加入一个有界可逆的半群因子不会改变原预解分类。

一个明确的非对称例子是：
$a$ 与 $b$ 支撑不交、各自非负不可和且平方可和。
对 $q=1$，辅助行 $c=b$ 由预解因子付清；
$c=a$ 则不满足 (1.4)，因为在 $a$ 的支撑上残差始终是 $a$，而
$\sum\min(a,a^2/a)=\infty$。
所以即使同时带着任意固定正预解幂，半群仍没有免费支付自己的生成元域。

本稿没有处理无限正则器、无限阶分母、一般多元多项式逆的准确范围或未知旗子商。
它也没有得到正常分离见证的聚合成本上界，完整 ISP 仍未解决。

## 9. 同一个混合分母的明确收缩强*主理想单位

本节承接 R230 对正预解式采用有界正规化逆词的机制，
给本稿固定 $R$ 的完整有界乘子和实际尾估计。
不把无界多项式 $P_b$ 当成全域有界的逆。

记
$$
H_m=\sum_{j<m}a_jV_j\in\mathcal A,\qquad
U_m=e^{tH_m}\in\mathcal A.
$$
由半群分类附节的实际前缀取消，
$$
S_a(t)U_m=e^{-tX_{a^{\ge m}}}=:K_m,\qquad
\|K_m\|\le1,\qquad K_m\to I\ \mathrm{SOT}^*.
\tag{9.1}
$$

对每条预解锚和 $\varepsilon>0$，令
$$
Q_{\nu,\varepsilon}=(I+\varepsilon B_\nu)^{-1},
$$
$$
G_{\nu,\varepsilon}
=(I+s_\nu B_\nu)Q_{\nu,\varepsilon}
=\frac{s_\nu}{\varepsilon}I+
\left(1-\frac{s_\nu}{\varepsilon}\right)Q_{\nu,\varepsilon}.
\tag{9.2}
$$
第二个等式证明它是全域有界的 $A'$ 算子。
第一个式子也有真实域依据：
$Q_{\nu,\varepsilon}H\subseteq\operatorname{Dom}B_\nu$。
因此与原预解准确取消，得到
$$
(I+s_\nu B_\nu)^{-1}G_{\nu,\varepsilon}
=Q_{\nu,\varepsilon}.
\tag{9.3}
$$
全部这些有界算子在交换的 $A'$ 中，故有限幂和不同锚的因子可以合法交换。

定义
$$
V_{m,\varepsilon}
=U_m\prod_{\nu=1}^qG_{\nu,\varepsilon}^{N_\nu}\in A'.
$$
每个 $V_{m,\varepsilon}$ 都实际有界，但不要求范数随参数一致。
(9.1)—(9.3) 给全空间准确恒等式
$$
\boxed{
RV_{m,\varepsilon}
=K_m\prod_{\nu=1}^qQ_{\nu,\varepsilon}^{N_\nu},
\qquad
\|RV_{m,\varepsilon}\|\le1.
}
\tag{9.4}
$$

这里还有明确的同一核心收敛界。
对有限 Walsh 多项式 $g$，记其实际有界乘子为 $X_g\in\mathcal A$，$X_g1=g$。
因为
$$
B_\nu1=\sum_jb^\nu_j\chi_j,
$$
预解恒等式在这个真实域输入上给
$$
\|(Q_{\nu,\varepsilon}-I)1\|
=\varepsilon\|Q_{\nu,\varepsilon}B_\nu1\|
\le\varepsilon\|b^\nu\|_2.
$$
各因子收缩，有限积按因子 telescoping；再用所有因子与 $X_g$ 交换以及 (9.1) 的尾界，得到
$$
\boxed{
\|(RV_{m,\varepsilon}-I)g\|
\le\|X_g\|
\left[
t\|a^{\ge m}\|_2+
\varepsilon\sum_{\nu=1}^qN_\nu\|b^\nu\|_2
\right].
}
\tag{9.5}
$$
因此可以明确取
$$
V_n=V_{n,1/n}.
$$
有限柱稠密与 (9.4) 的统一收缩界给 $RV_n\to I$ 强；
$RV_n\in A'$ 的 $C$ 对称性再给伴随强收敛。
所以
$$
\boxed{
\|RV_n\|\le1,\qquad RV_n\longrightarrow I
\quad\mathrm{SOT}^*.
}
\tag{9.6}
$$

除仅有半群因子的情形外，这里一般只证明 $V_n\in A'$，
没有声称 $V_n\in\mathcal A$。
R88 的强闭包定理仍给
$$
I\in\overline{R\mathcal A}^{\mathrm{SOT}},
$$
但不据此免费宣称可以把 (9.6) 换成保同一收缩界的多项式乘子序列。

## 10. 所有实际闭不变子空间和有限放大旗上的用途

若 $M$ 为任意闭 $A$ 不变子空间，
R88 保证 $R,V_n$ 都保持 $M$。
对 $x\in M$，
$$
RV_nx\in RM,\qquad RV_nx\to x.
$$
因此
$$
\boxed{\overline{RM}=M.}
\tag{10.1}
$$
若 $Rx=0$，则交换性给 $RV_nx=V_nRx=0$，取极限得 $x=0$。
所以 $R|_M$ 也单射。

更一般，固定有限 $d$ 和闭 $A^{(d)}$ 不变旗 $N\subseteq M$。
对角放大的 $R,V_n$ 保持该旗，实际 Hilbert 子商上诱导的乘积仍收缩且强趋于商恒等。
同样的两行论证给
$$
\boxed{
R_{M/N}\text{ 单射且稠密像。}
}
\tag{10.2}
$$
对商的结论来自同一组有界强单位，不是将环境中的稠密像无证下传。

这些实际主理想单位也使每个正常正泛函在 $RV_n$ 上取值趋于其单位取值。
但是本稿没有证明任意假想正湮灭见证满足某个指定配对域或聚合能量上界；
(9.6) 单独不补上这一步。
