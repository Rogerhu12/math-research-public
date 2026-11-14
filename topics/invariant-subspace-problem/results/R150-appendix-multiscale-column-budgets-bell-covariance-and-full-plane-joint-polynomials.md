# R150 附录：真实多尺度全柱、Bell 线性协变与双全平面谱的全多项式类

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf。

状态：完整证明；根代理与 kernel_resume_1cf 已全文独立核查。

本稿处理唯一线性中心恰为最高符号根后的一条真实新入口。对去中心的原 first 另付中心发散、头绝对量及尾预算，然后分别归一；不从一次中心比收敛自动推出这些条件。直接的原伴随核投影证明不需要任何 first 空谱。固定有限多行的版本同时支付混合自然词、全部 Bell 修正和线性重参数化。

## 1. 固定有限多行的真实尺度条件

取固定整数 $q\ge1$ 及原复 first
$$
u_\nu=a_{\nu,*}+\sum_{j\ge0}a_{\nu j}\chi_j,
\qquad a_{\nu\cdot}\in\ell^2(\mathbb C),\quad 1\le\nu\le q.
$$
令 $X_\nu=X_{u_\nu}$ 为原规范闭 first。这里不要求它们空谱、最大增生或互相具有完整相对域。

取递增穷尽的有限物理位集 $F_n$，置
$$
d_n=|F_n|,\quad
s_{\nu n}=a_{\nu,*}+\sum_{j\in F_n}a_{\nu j},\quad
b_{\nu n}=\sum_{j\in F_n}|a_{\nu j}|,\quad
g_{\nu n}=\|a_{\nu,F_n^c}\|_2.
$$
假设每行分别满足
$$
|s_{\nu n}|\to\infty,\qquad
b_{\nu n}/|s_{\nu n}|\le C,
\tag{1.1}
$$
以及同一个全柱尾预算
$$
\boxed{
\varepsilon_n=\sum_{\nu=1}^q\frac{g_{\nu n}}{|s_{\nu n}|},
\qquad \sqrt{d_n}\,\varepsilon_n\to0.
}
\tag{1.2}
$$
只需沿一条共同递增子列成立。各行中心允许不同增长速度和不同复相位。

对非恒定标量多项式
$$
G(z)=\sum_{\alpha\in E}c_\alpha z^\alpha,\qquad c_\alpha\ne0,
$$
记
$$
M_n(G)=\max_{\alpha\in E}\prod_{\nu=1}^q|s_{\nu n}|^{\alpha_\nu}.
$$
因为全部中心模趋无穷且 $G$ 非恒定，$M_n(G)\to\infty$。

要求沿同一子列有一个固定 $\delta>0$，使
$$
\boxed{
|G(s_{1n},\ldots,s_{qn})|\ge\delta M_n(G).
}
\tag{1.3}
$$
这允许多个最大单项式同阶，但要求它们在实际中心上不发生比主尺度更深的相消。

**定理 1。** 在 (1.1)—(1.3) 下，对全部 $\lambda\in\mathbb C$、整数 $r\ge1$ 和原复 $\ell^2$ first 指数权 $w$，
$$
\boxed{
[G(u_1,\ldots,u_q)-\lambda]^r e^w
\text{ 对原实际 }A\text{ 循环。}
}
\tag{1.4}
$$
不要求 $G$ 首一，也不要求某个最高普通齐次符号非零于单一线性中心方向。

## 2. 固定多行的实际混合全柱预算

在原真实伴随词域上写
$$
X_\nu^*/\overline{s_{\nu n}}
=I+H_{\nu n}+T_{\nu n},
$$
其中
$$
H_{\nu n}
=\sum_{j\in F_n}\frac{\overline{a_{\nu j}}}{\overline{s_{\nu n}}}
(V_j^*-I)
$$
是有限头，$T_{\nu n}$ 为原规范尾 first 的相应归一伴随。

[R251 §§2—3](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md)给任意有限位集的真实进位和整个 $Q_{F_n}H$ 上的补集尾域；不是只在一个尾真空上使用范数。以下说明其多行混合形式所需的常数。

对 $|z_\nu|=1$，组合有限头 $\sum_\nu z_\nu H_{\nu n}$ 的系数绝对和不超过 $qC$。故其 $h$ 次幂有
$$
\left\|\left(\sum_\nu z_\nu H_{\nu n}\right)^h\right\|
\le C_q^h\quad(h\ge0),\qquad
\left\|\left(\sum_\nu z_\nu H_{\nu n}\right)^h\right\|
\le C_q^h e^{-\gamma h^4}
\quad(h\ge\max(2d_n,16)).
\tag{2.1}
$$

$\gamma>0$ 为原实际 carry 常数。

有限多变量 Cauchy 系数公式给同样的混合头词界。确实，
$\prod_\nu H_{\nu n}^{h_\nu}$ 是上述幂的相应系数除以一个正整数多项式系数，且 $\sum h_\nu=h$；无需增加依赖 $d_n$ 的成本。

组合尾的系数 $\ell^2$ 范数不超过 $\varepsilon_n$。同一 R251 补集指数尺度证明及有限多变量 Cauchy 极化给
$$
\boxed{
\left\|\prod_\nu T_{\nu n}^{t_\nu}Q_{F_n}\right\|
\le(C_q\varepsilon_n\sqrt t)^t,\qquad
t=\sum_\nu t_\nu.
}
\tag{2.2}
$$
对应的全部自然混合词域同时成立。有限头保持这些域且与尾域交换，所以任意混合头/尾词由 (2.1)、(2.2) 的乘积控制。

这是从真实组合 first 的相同域/尺度估计抽取有限混合系数；没有把单个无界算子幂的形式极化当作未经证明的域恒等式。R251 的共同补集尺度逐次识别自然词，原有限家族的 R186 共同正则器也可以一次支付所需固定深度。

由 (1.2)，可选整数 $p_n$ 使
$$
p_n/d_n\to\infty,\qquad
\varepsilon_n\sqrt{p_n}\to0.
\tag{2.3}
$$
例如当 $\varepsilon_n\sqrt{d_n}>0$ 时，取
$p_n=\lceil d_n/(\varepsilon_n\sqrt{d_n})\rceil$；零尾时另取 $p_n=d_n^2$，删去有限初始指标即可。

## 3. 完整 Bell 的逐偏导形式

原多行生成函数的实际局部因子为
$$
H(z,V)=e^{-zV}(\cosh z\,I+V\sinh z).
$$
对原 $w=w_*+\sum_jw_j\chi_j$，R145/R186 的真实范数整函数给
$$
\mathcal B_w(t)
=\prod_jH\!\left(w_j+\sum_\nu t_\nu a_{\nu j},V_j\right)
H(w_j,V_j)^{-1},
\qquad \mathcal B_w(0)=I.
$$
记
$$
C_\alpha^w=\partial^\alpha\mathcal B_w(0)\in\mathcal A\subseteq\mathfrak C=A',
\qquad C_0^w=I.
$$
这些都是固定有界系数，并保持全部所需原共同自然词域。

对固定标量多项式 $K$，完整 Bell 核心准确为有限和
$$
\boxed{
P_K(X_1,\ldots,X_q)
=\sum_{\alpha\ge0}\frac{C_\alpha^w}{\alpha!}
(\partial^\alpha K)(X_1,\ldots,X_q).
}
\tag{3.1}
$$
求和只到 $|\alpha|\le\deg K$。使用的是原全部 cumulant，所有正阶项都按具体偏导降低相应变量次数；不仅是笼统地降低普通总次数。

[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)给其规范最大实现 $\mathcal P_K$、完整 $C$ 自伴性以及原循环指数图核心。更明确地，置
$$
B_w=\prod_jH(w_j,V_j).
$$
[R145 §§2、8](R145-multimode-bell-mixed-domains-cyclicity.md)把 $w$ 作为第 $q+1$ 个模式、把其参数固定为1，给出原范数整单位 $B(t,1)$ 及共同整轨道
$V(t,1)=B(t,1)^{-1}e^{w+\sum_\nu t_\nu u_\nu}$。
因此 $B_w=B(0,1)$、$\mathcal B_w(t)=B(t,1)B_w^{-1}$；
$\xi_w=V(0,1)=B_w^{-1}e^w$ 属于全部原 $X_\nu$ 自然混合词域。
各修正系数属于 $\mathcal A$，且 $\chi(C_\alpha^w)=0$ 于 $\alpha\ne0$，因为上述单位比的字符恒为1。
对这个共同整轨道直接作有限参数偏导，准确得到
$$
K(u_1,\ldots,u_q)e^w=B_w\mathcal P_K\xi_w.
\tag{3.2}
$$
$B_w$ 为有界交换单位，$\xi_w$ 循环并产生相应图核心。因此排除 $\ker\mathcal P_K$ 后，$C$ 自伴性给像稠密，再由 (3.2) 及该图核心得到原目标循环。

### 3.1 中心代入的逐偏导预算

现在取
$$
K=(G-\lambda)^r.
$$
对充分大的 $n$，全部 $|s_{\nu n}|\ge1$，且
$$
|K(s_n)|\ge(\delta/2)^r M_n(G)^r.
\tag{3.3}
$$
因为 $M_n(G)\to\infty$，固定 $\lambda$ 不能改变这个下界。

有限多项式展开给每个 $\alpha$
$$
\boxed{
|(\partial^\alpha K)(s_n)|
\le C_{G,\lambda,r,\alpha}M_n(G)^r
\prod_\nu |s_{\nu n}|^{-\alpha_\nu}.
}
\tag{3.4}
$$
证明可以逐单项式完成：$K$ 的每个原项来自至多 $r$ 个 $G$ 项及常数 $\lambda$ 的乘积，其尺度不超过固定常数乘 $M_n(G)^r$；微分只减去对应 $\alpha_\nu$ 个指数，下降的阶乘由固定次数控制。这些偏导不会产生新的高次单项式。

由 (3.3)—(3.4)，完整 Bell 在中心上的常数系数满足
$$
\left\|
\frac{P_K(s_n)}{K(s_n)}-I
\right\|
\le
C\sum_{\alpha\ne0}
\prod_\nu |s_{\nu n}|^{-\alpha_\nu}
\longrightarrow0.
\tag{3.5}
$$
这里 $P_K(s_n)$ 是将各无界变量换成实际标量中心后的有界系数和。各项 $C_\alpha^w$ 没有被替成其字符。

## 4. 原伴随核投影及三组测试

反设 $\ker\mathcal P_K\ne0$，令 $\Pi$ 为到该核的正交投影。在原共同伴随深词域中，形式伴随 $P_K^*$ 与 $\mathcal P_K^*$ 一致，故
$$
\Pi P_K^*=0.
\tag{4.1}
$$
定义仅在这些实际词域上使用的多项式
$$
\mathscr T_n=I-\frac{P_K^*}{\overline{K(s_n)}}.
\tag{4.2}
$$

按
$X_\nu^*=\overline{s_{\nu n}}(I+H_{\nu n}+T_{\nu n})$
展开。由 (3.5)，常数系数 $\delta_n\to0$ 按算子范数。其余单项式次数介于1与
$D=\deg K$，全部系数范数一致有界。

最后一点也由 (3.4) 的逐单项式证明直接得到：每个完整 Bell 原单项式的尺度，除以 $|K(s_n)|$ 后有固定界；正阶偏导还带相应中心的负幂。于是固定有限展开的绝对系数和有统一常数。全部有界伴随系数与原归一头/尾交换并保持共同词域。

将 $\mathscr T_n^{p_n}$ 完全展开，记一个项中常数因子数为 $c$、头总次数为 $h$、尾总次数为 $t$。有
$$
h+t\ge p_n-c,\qquad h+t\le D(p_n-c).
$$
因此至少 $c,h,t$ 中一项不小于 $p_n/3$。

- $c\ge p_n/3$ 时，费用含 $\|\delta_n\|^{p_n/3}$；
- $h\ge p_n/3$ 时，(2.3) 保证最终 $h\ge2d_n$，实际头费用含 $e^{-c_0p_n^4}$；
- 其余项有 $t\ge p_n/3$，尾费用至多
  $(C\varepsilon_n\sqrt{Dp_n})^{p_n/3}$，最终底数趋零。

所有固定次数和混合行数的系数费用只增一个 $C_D^{p_n}$ 因子。结合 (2.3)，得到
$$
\boxed{
\|\mathscr T_n^{p_n}Q_{F_n}\|^{1/p_n}\longrightarrow0.
}
\tag{4.3}
$$
R251 已付整个 $Q_{F_n}H$ 的全部所需有限自然词域；这些迭代没有对未知核要求额外光滑。

由 (4.1) 逐次回传，
$$
\Pi Q_{F_n}=\Pi\mathscr T_n^{p_n}Q_{F_n}\to0.
$$
而 $Q_{F_n}\to I$ 强，所以 $\Pi=0$，矛盾。§3 的原最大图和指数图核心完成 (1.4)。定理1证毕。

## 5. 线性去中心的完整 Bell 协变

取原两行 $u,v$ 和固定复数 $\beta$，令
$$
z=v-\beta u,\qquad
G(x,z)=F(x,\beta x+z).
\tag{5.1}
$$
新行系数和常数是原数据的准确线性组合。记原两个参数为 $(s',t')$，新参数为 $(s,t)$。逐个真实局部因子给
$$
\boxed{
\mathcal B_{(u,z),w}(s,t)
=\mathcal B_{(u,v),w}(s-\beta t,t).
}
\tag{5.2}
$$
有限乘积中等式直接成立，原范数局部一致极限保等式及每个固定导数。

若原 Bell 系数为 $C_{ij}$，新系数准确为
$$
\boxed{
\widetilde C_{ij}
=\sum_{\ell=0}^j\binom j\ell(-\beta)^{j-\ell}
C_{i+j-\ell,\ell}.
}
\tag{5.3}
$$
同时在原共同深域上
$X_z=Y-\beta Z$；只在已付共同域中使用这条自然式，不把自然差的全域宣称为一个已闭实现。

有限链式法则给
$$
G(\partial_s,\partial_t)
=F(\partial_{s'},\partial_{t'})
$$
作用于 (5.2) 及相应真实生成轨道，因为
$\partial_s=\partial_{s'}$、
$\partial_t=-\beta\partial_{s'}+\partial_{t'}$。
所以完整两份 Bell 多项式在共同深域逐项相同，不会额外产生仅由“总次数降低”所允许的伪高项。

原/新全部 first 纳入同一个 R186 正则族后，两侧最大图也相同：对任意一侧域内向量，用固定充分深幂 $R(t)^N$ 逼近；正则后的向量在共同词域，两侧输出相同，原侧输出按图收敛。另一侧的闭性给一个域包含，反向同理。这付清了完整规范实现的协变。

### 5.1 去中心后必须新增的实际预算

若原两中心为 $\sigma_n,\tau_n$，新中心准确为
$$
\omega_n=\tau_n-\beta\sigma_n.
$$
除了原主行预算，还须另证
$$
\boxed{
|\omega_n|\to\infty,\quad
\frac{\sum_{F_n}|\nu_j-\beta\zeta_j|}{|\omega_n|}\le C,\quad
\frac{\sqrt{d_n}\|(\nu-\beta\zeta)_{F_n^c}\|_2}
{|\omega_n|}\to0.
}
\tag{5.4}
$$
这些不由 $\tau_n/\sigma_n\to\beta$ 推出。

若 (5.4) 成立，定理1可对原 $u,z$ 使用两尺度 $(\sigma_n,\omega_n)$。只要
$$
|G(\sigma_n,\omega_n)|
\ge\delta\max_{(i,j)\in\operatorname{supp}G}
|\sigma_n|^i|\omega_n|^j,
$$
原 $[F(u,v)-\lambda]^re^w$ 就循环。

例如 $G(x,z)=z^m-x^k$ 时，完整 Bell 的所有项都来自
$(z^m-x^k-\lambda)^r$ 的实际偏导。即使 $m>k$，也不能凭“低总次”擅自添加一个 $x^{m-1}$；(5.2)—(5.3) 和 (3.1) 正是排除这类错误的步骤。

有限更多行的任何固定可逆线性变换同理：其真实 Bell 参数按转置矩阵变换，有限链式法则和同一正则器支付规范图。每条新增余行仍须单独满足 (1.1)—(1.2)，不作形式递归降阶。

## 6. 严格分离中心尺度使全部多项式可用

假设两行中心除满足 (1.1)—(1.2) 外，还满足
$$
|s_{1n}|\to\infty,\quad |s_{2n}|\to\infty,\qquad
\boxed{\frac{|s_{2n}|^N}{|s_{1n}|}\to0
\quad\text{对每个固定整数 }N\ge1.}
\tag{6.1}
$$
任取非恒定 $G(x,z)$。在其有限支撑中，先选最大的 $x$ 次数 $i_0$，再在该行选最大的 $z$ 次数 $j_0$。则该单项式唯一支配：

- 同 $i_0$ 而较小 $j$ 的比值由 $|s_2|\to\infty$ 付；
- 较小 $i$ 的任意项由 (6.1) 付。

所以
$$
G(s_{1n},s_{2n})
=c_{i_0j_0}s_{1n}^{i_0}s_{2n}^{j_0}(1+o(1)),
$$
满足 (1.3)。因此这一对原模式的全部非恒定二元多项式、全部 $\lambda,r,w$ 均循环。

固定有限 $q$ 行也一样：若中心按顺序满足
$|s_{\nu+1,n}|^N/|s_{\nu n}|\to0$ 对每个固定 $N$、每个相邻 $\nu$ 成立，那么有限支撑中的字典序最高单项式唯一支配。定理1给全部非恒定 $q$ 元多项式的结论。

## 7. 唯一线性根的具体慢余行

取
$$
a_j=\frac1{j+2},\qquad
d_j=\frac1{(j+2)\log(j+2)},
$$
$$
u=\sum_ja_j\chi_j,\qquad
z=\sum_jd_j\chi_j,\qquad
v=\beta u+z.
\tag{7.1}
$$
以实际前 $n$ 位为 $F_n$。初等积分比较给
$$
s_{1n}\sim\log n,\qquad s_{2n}\sim\log\log n,
$$
$$
g_{1n}^2=O(n^{-1}),\qquad
g_{2n}^2=O\bigl(n^{-1}(\log n)^{-2}\bigr).
\tag{7.2}
$$
两行正系数使头绝对量与中心相同，所以
$$
\sqrt n\left(\frac{g_{1n}}{s_{1n}}
+\frac{g_{2n}}{s_{2n}}\right)
=O\!\left(\frac1{\log n}
+\frac1{\log n\,\log\log n}\right)\to0.
\tag{7.3}
$$
(6.1) 同样成立。

原 $(u,v)$ 中心比收敛到 $\beta$，而去中心后 (5.4) 已由 (7.2)—(7.3) 实际支付。故
$$
\boxed{
[F(u,v)-\lambda]^re^w
\text{ 对每个非恒定 }F\in\mathbb C[x,y]
\text{ 及全部 }\lambda,r,w\text{ 循环。}
}
\tag{7.4}
$$

特别，对任意 $m>k\ge1$，
$$
\boxed{
[(v-\beta u)^m-u^k-\lambda]^re^w
\text{ 循环。}
}
\tag{7.5}
$$
原普通最高符号为 $(y-\beta x)^m$，其在唯一线性中心 $(1,\beta)$ 处为零；因此 (7.5) 确实使用新增的余行尺度。

这里 $d$ 甚至满足
$\sum_jd_j^2/a_j<\infty$。这不把相对界零本身当作排核理由；真正补上的信息是余行中心 $\log\log n$ 发散及其已付全柱尾。

## 8. 两条 first 都为全平面连续谱的具体类

将 (7.1) 两条行同时乘以同一个实符号振幅
$$
\eta_j=1+2(-1)^j
=
\begin{cases}3,&j\text{ 偶},\\-1,&j\text{ 奇}.\end{cases}
$$
记
$$
\widetilde u=\sum_j\eta_j a_j\chi_j,\qquad
\widetilde z=\sum_j\eta_j d_j\chi_j.
\tag{8.1}
$$
两条基本正幅度都递减到零，交错级数的部分和有统一界。因此
$$
\widetilde s_{1n}=\log n+O(1),\qquad
\widetilde s_{2n}=\log\log n+O(1).
$$
头绝对量至多相应正头的3倍，尾平方至多正尾平方的9倍。所以 (7.3) 和全部尺度分离仍成立。

这里还可以准确核验两条 first 的谱。使用已读
[R138 §§1、7，式(1.1)、(1.4)](R138-first-chaos-complete-spectrum-classification.md)：对原复 $\ell^2\setminus\ell^1$ 行 $c$，若每个 $\theta$ 都使
$$
\mathcal D(c,\theta)
=\sum_j(|c_j|-\operatorname{Re}(e^{-i\theta}c_j))
=\infty,
$$
则其原 first 的谱和近似谱均为 $\mathbb C$，全部谱点连续。

对于 $c_j=\eta_j b_j$，其中 $b=a$ 或 $d$，偶、奇两个正子和都发散；例如各行满足 $b_{2k+1}/b_{2k}\to1$ 且总和发散。准确有
$$
\boxed{
\mathcal D(c,\theta)
=3(1-\cos\theta)\sum_{j\ {\rm 偶}}b_j
+(1+\cos\theta)\sum_{j\ {\rm 奇}}b_j
=\infty
\quad\text{对每个 }\theta.
}
\tag{8.2}
$$
两个非负系数不可能同时为零。故
$$
\sigma(X_{\widetilde u})
=\sigma(X_{\widetilde z})=\mathbb C,
$$
并且都全为连续谱。

实际上，这个二维非恒定线性包中没有空谱 first。若 $\alpha\ne0$，
$$
(\alpha a_j+\beta d_j)/a_j\longrightarrow\alpha.
$$
乘以 $3/-1$ 后，两子列的方向分别趋向 $\alpha$ 和 $-\alpha$。对固定 $\theta$，两个极限缺陷系数
$|\alpha|\mp\operatorname{Re}(e^{-i\theta}\alpha)$ 不可能同时为零；相应一条子列的缺陷最终至少为某个正数乘 $a_j$，其和发散。
若 $\alpha=0,\beta\ne0$，直接对 $d$ 用 (8.2) 的旋转版本。
故每个 $\alpha\widetilde u+\beta\widetilde z$（$(\alpha,\beta)\ne(0,0)$）的 first 都是全平面连续谱；加任意常数也不改变该分类。这里仅用同一个已付 R138 判据，不另计结论。

尽管没有空谱 first，定理1与§6仍给
$$
\boxed{
[F(\widetilde u,\widetilde z)-\lambda]^re^w
\text{ 对每个非恒定 }F\in\mathbb C[x,y]
\text{ 及全部 }\lambda,r,w\text{ 循环。}
}
\tag{8.3}
$$
谱分类只用于说明这个明确实例的范围；循环性证明本身不依赖 R138。

## 9. 旧范围扣除与剩余问题

[R243](R243-partial-sum-centers-and-log-tail-polynomial-cyclicity.md)已处理单 first 的部分和中心及相应全柱幂界；[R173](R173-rank-bounded-gauge-orbits-and-slow-polynomial-joint-cyclicity.md)/[R180](R180-unbounded-first-class-independence-and-l2-polynomial-gauge-cyclicity.md)给一般慢模式有限 gauge 联合循环，并非本稿同一个多模式点态向量的循环。[R154](R154-supercubic-modes-all-polynomials-exponential-weights.md)的全多项式结论要求联合超三次快尾，不含 (7.1)、(8.1)。旧[R150 矩形角](R150-empty-spectrum-anchor-rectangular-polynomial-cyclicity.md)和[R155 有界辅助](R155-empty-anchor-bounded-auxiliary-polynomials.md)分别保留其首系数/辅助有界条件；与本稿交集按旧来源扣除。

新增内容是固定有限原行的独立尺度全柱检验、全部偏导 Bell 成本、完整线性协变，以及由真实去中心慢余行得到的 (7.4) 与明确双全平面谱类 (8.3)。

条件 (5.4) 不能省略。一般唯一中心根可能有有界余行、中心反复相消或尾大于其余尺度；这些不被本稿排除。多个同阶单项式若在实际中心发生深相消，仍须另有预算，不能把非线性残差自动当作新 first。一般多模式、任意向量循环性、真正常见证聚合上界和普通复 Hilbert ISP 继续开放。
