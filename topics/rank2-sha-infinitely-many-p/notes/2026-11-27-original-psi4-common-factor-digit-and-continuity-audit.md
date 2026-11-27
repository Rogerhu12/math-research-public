# 原 psi4 双核共同正权因子的离散连续性审计

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

本注给出一个完整的离散障碍及其准确适用门。它不把未知层级微分倍率
$\Omega_\Gamma$置为单位，不宣称 Kriz 的定理为假，也不通过补入未证明的
Gamma 因子保住某个插值式。原完整双核的正权代数身份及 proper 几何身份
与这里的连续性接合分开核验。

## 1. 原 Hermite 正权标量中的阶乘

使用原未平方来源笔记 §§10–11 的同一正常排序核，记
$a=17/2$、$G=51\sqrt3$、
$b=2(\omega-1)/\sqrt G$、$h_\infty=\sqrt G/(204\pi i)$。
在实际两 Hermite 变量中，
$\Theta_\pm(T)=\sum_m b_{\pm,m}T^m/m!$，
而 $b_{\pm,m}=m!s_\pm(\Omega_0h_\infty)^m$ 乘原普通 Taylor 系数。
故未除幂的 $\partial_Z^n\partial_W^{n+2}$ 确实给两个阶乘
$n!(n+2)!$。

完整 $e^{-cZW}$ 不能随意删除；本次它的合法出现来自
$c=(4\pi a\operatorname{Im}\omega)^{-1}$ 及原逐项恒等
$a^n\mathcal L_{n,n+2}=\delta_3^n(z^2e^{2\pi ia|z|^2\tau})/
e^{2\pi ia|z|^2\tau}$。
例如 $n=1,2$ 的低项分别是
$-3/(4\pi y)$ 和
$-8a|z|^2/(4\pi y)+12/(4\pi y)^2$。
因此本节不是以未证明的无交叉项代替原核。

原 archimedean 提槽给
$$
\frac{A_n}{A_4}
=\frac{n!(n+2)!}{4!6!}\,
 \left[a(-ib)^2(\Omega_0h_\infty)^2\right]^{n-4},
\qquad
a(-ib)^2(\Omega_0h_\infty)^2
=-\frac{\omega\Omega_0^2}{408\pi^2}
=\frac{\omega}{102}
 \left(\frac{\Omega_0}{2\pi i}\right)^2 .
\tag{1}
$$
(1)只说明原 coherent 提槽及普通迭代的规范；从它到实际 Kriz
algebraic toric sum 仍须同一微分/level 比较，不能省略。

## 2. 固定底数幂不能修复的完整离散障碍

设 $p\ge5$，
$A=p^2-1$、$B=p-1$，固定 $K,\zeta\in\mathbf C_p^\times$。
对正整数 $u$ 定义
$$
g(u)=K\zeta^u\,
 \frac{((Au)!/(Bu)!)^2}{Au-1}.
\tag{2}
$$
若两个连续函数 $L,R:\mathbf Z_p\longrightarrow\mathbf C_p$
对每个正整数满足
$$
L(u)=g(u)R(u),
\tag{3}
$$
则必有 $L=R=0$。

证明如下。写 $s_p(m)$ 为整数 $m$ 的 $p$ 进数字和，并置
$$
\Delta(u)=\frac{s_p(Au)-s_p(Bu)}{p-1}.
$$
Legendre 公式准确给
$$
v_p\!\left(\frac{(Au)!}{(Bu)!}\right)
=pu-\Delta(u).
\tag{4}
$$
由于 $A$ 的数字是 $(p-1,p-1)$、$B$ 的数字是 $(p-1)$，
$\Delta(1)=1$。

若 $R$ 非零，正整数稠密性给一个正整数 $u_0$ 使 $R(u_0)\ne0$；
由(2)–(3)亦有 $L(u_0)\ne0$。
令 $u_m=u_0+p^m$。当 $m$ 大于 $Au_0$ 与 $Bu_0$ 的数字长度时，
两段数字互不重叠，所以
$$
\Delta(u_m)=\Delta(u_0)+1.
\tag{5}
$$
同时 $Au_0-1\ne0$，故对充分大 $m$，
$v_p(Au_m-1)=v_p(Au_0-1)$。
由(2)、(4)、(5)得到精确式
$$
v_p(g(u_m))-v_p(g(u_0))
=\bigl(v_p(\zeta)+2p\bigr)p^m-2.
\tag{6}
$$
另一方面 $L,R$ 连续且在 $u_0$ 非零，故
$g(u_m)=L(u_m)/R(u_m)\to L(u_0)/R(u_0)=g(u_0)\ne0$。
非阿基米德范数于是要求(6)最终等于0。
若 $v_p(\zeta)+2p\ne0$，其绝对值趋于无穷；若等于0，(6)恒为$-2$。
两者均矛盾。因此 $R=0$，再由(3)及稠密性得 $L=0$。证毕。

这个论证不要求 $L,R$ 可微或解析，也不要求任何指定参考端点非零；
唯一非零假设只是某个正整数处 $R(u_0)\ne0$。

## 3. 它对当前公共因子提出的准确门

原新 cross 使用
$n=Au-2$、$r=Bu$ 及整数身份
$$
\delta^{-(dr-2)}d_{k,dr-2}s_{k,dr}
=-3q_\delta^{-r}\frac{C_+^{2r}}{(r!)^2}
 J_{-,k}(r)J_{+,k}(r).
\tag{7}
$$
假设实际 algebraic comparison 另能证明
$q_{p,n}=q_{p,0}Q_p^n$，其中 $q_{p,0},Q_p$ 固定非零；
结合(1)，其整数公共因子
$q_{p,n}c_n\,prC_+^{2r}/(r!)^2$
就严格化成(2)。这里用的是
$$
n!(n+2)!\frac{pr}{(r!)^2}
=\frac{p}{(p+1)(Au-1)}
 \left(\frac{(Au)!}{(Bu)!}\right)^2 .
\tag{8}
$$
所有固定 period、$\Omega_\Gamma$、degree17、Gaussian 常数与有限相位
都只能改变 $K,\zeta$，不能改变(6)中的 $-2$。

所以，“同一个连续 Kriz 读者在每个正整数等于这个纯固定幂标量乘原
Newton 读者”与“该 Newton 读者非零”不能同时成立。
只把参考质量或另一个端点非零补进来不会修复它。
本结论要求继续核验实际 $q_{p,n}$ 与原 toric sum 的接合；
它没有先断言两者已经由现有引用完全识别。

## 4. 已定位的实际接合及待核之处

Kriz 书版(6.51)–(6.52)的系数
$\binom{j+k-1}{i}\binom ji i!$ 是未除幂迭代；
(8.16)将 $L^{\rm alg}$写为相应 toric derivative sum，
(8.21)再显示固定 period 的权幂。
因此不能仅通过把书中算子改称“除幂”来消掉(1)。

真正连续性的输入是(6.56)–(6.58)的
$q_{\rm dR}^{1/p}$ 上 $\flat$-投影。将它换成 usual
$p$-depletion 的具体门是 Proposition7.20(7.14)，再由(7.16)
回到底点的正权值。该处所写下降分别在
$U\subset Y(\Gamma)^{\rm ss}$ 与 ordinary locus 上；
仅在二者不交并集上援引 rigidity 不足以支付相等。
若存在同一个连通 overconvergent 域及两个截面的真实延拓，
须实际给出并证明它与本题所选 good 点、level 基、权和 period 相容。
目前本注未取得此额外接合，也不把其缺失直接称为原定理的反例。

还有一个须独立支付的点位问题。采用书中的右作用约定，令
$$
g_1=\operatorname{diag}(p,1),\qquad
g_2=\operatorname{diag}(1,p),\qquad y'=yg_1 .
\tag{9}
$$
对函数 $h_j=p^j\theta_k^jF^{(p),\flat}$，固定 pullback 满足
$$
(g_2^*h_j)(y')=h_j(y'g_2)=h_j(y\cdot pI).
\tag{10}
$$
Theorem6.21与good-point界先给的是 $h_j$ 在 $y'$ 及相应good邻域上的
连续性。固定群作用确实连续，但它同时运输函数的定义域：
若 $h_j$ 的连续族只在 $U$ 已证，则 $g_2^*h_j$ 的族只在
$Ug_2^{-1}$ 由此得到。(10)要在原 $y'$ 评价，仍需在 $y\cdot pI$
有该连续族；不能仅由 $h_j(y')$ 连续推出。

对书中本次惰性 CM 规范，$|\hat z(y)|=1$、
$|\hat z(y')|=p$；中心元 $pI$ 不改变该比值，所以
$|\hat z(y\cdot pI)|=1$。因此这不是同一个good点的无成本重标记。
若以原bad点的更细 $q_{\rm dR}^{1/p^2}$ 坐标直接建立连续性，
须同时运输真实 $\flat$ 投影、整个 $p^2$ 对应、所有
$\omega$／Kodaira–Spencer 基和相应正权式；它不能仅凭形式
$p^{2j}$ 被命名为 usual $p$-depletion。

(9)–(10)只指出 Corollary7.21 应补的域与点位接合。
本注未声称不同定义域上原定理的完整断言已经被推翻。

本注要求暂停依赖“纯固定幂公共因子非零连续延拓”的新应用；
原正权 theta、全图/cup、原 Newton 整数回卷、以及有明确前提的交叉
代数式应按各自实际证明范围保留，不用一个未核插值门覆盖它们。

原始依据：
- 本课题原未平方来源笔记 §§10–11；新 psi4 来源与全图 cross 笔记。
- D. J. Kriz, *Supersingular p-adic L-functions, Maass–Shimura Operators
  and Waldspurger Formulas*, AMS212 (2021), (6.51)–(6.58),
  Proposition7.20、(7.16)、(8.16)、(8.21)。
  可读书版：https://dokumen.pub/supersingular-p-adic-l-functions-maass-shimura-operators-and-waldspurger-formulas-ams-212-9780691225739.html

## 5. “♭”与通常 $p$-depletion 的接合审计：有限层下降不等于共同延拓

2026-11-27 UTC，geometry 独立核对。本节只定位当前证明链尚未支付的接合；不据一个证明缺格断言所引用定理为假，也不改写已经独立证明的正整数权或 proper finite-polynomial 公式。

### 5.1 两个算子的真实定义不同

Kriz 专著第6章 Definition6.18 从一个固定点的 $q_{\rm dR}^{1/p^b}$ 展开定义 $\flat$。令 $X=q_{\rm dR}^{1/p^b}$，把该展开写为 $F_y(X)=\sum_{m\ge0}a_m(y)(X-1)^m$，则
$$
 \mathcal A_{y,b}F_y(X)=\frac1p\sum_{a=0}^{p-1}F_y(\zeta_p^aX),
 \qquad F_y^\flat=(1-\mathcal A_{y,b})F_y .
 \tag{A1}
$$
右边始终使用同一个点的系数 $a_m(y)$。定义的收敛域通过全部系数的整性条件限制；一个点附近有此展开，不等于它已在一个较大的有限层严格邻域统一延拓。

通常的 $p$-depletion 则为原 Hecke 算子
$$
 w^{(p)}=w-a_p(w)V_pw+\varepsilon_w(p)p^{k-1}V_p^2w
 \tag{A2}
$$
这里 $w$ 为 weight $k$ 的实际 Hecke 本征源，并明定经典 $V_pf(q)=f(q^p)$；书第230页 Lemma8.12 的第三项也保 $\varepsilon_w(p)p^{k-1+2j}$。本题 $k=3$、$a_p=0$、$\varepsilon_w(p)=-1$，故 $w^{(p)}=w-p^2V_p^2w$。它使用真正的同源及其微分运输。两种操作在 ordinary Serre–Tate 坐标中可比较；在一个 supersingular CM 点，(A1)与(A2)相认还需要实际的同源/展开交织。

项目原来使用 Proposition7.20 的关键结论，正是将已经作了(A2)的来源再作(A1)，而不改变所需正权值。至少必须证明
$$
 \mathcal A_{y,b}\bigl(F^{(p)}_y\bigr)=0
 \tag{A3}
$$
在实际使用的所有 CM 点、原微分和级结构上成立，或证明足以给同一全部 raised 读数的对应等式。不能用(A1)的定义自身推出(A3)。

### 5.2 Proposition7.20 中需要补的连接

专著 Proposition7.15 给好 CM 点轨道附近的局部区域；Proposition7.20 的证明（印刷页213–214）把两待比截面下降到某个
$$
 U\subset Y(\Gamma)^{\rm ss}.
$$
ordinary 比较另沿 Igusa 覆盖下降到 $Y(\Gamma)^{\rm ord}$。该证明随后在 $U\cup Y(\Gamma)^{\rm ord}$ 上使用 rigidity。

这一步单凭所写下降不能成立。按该文的定义，
$Y^{\rm ss}=Y\setminus Y^{\rm ord}$，所以两个显示的区域不交。若其并集按证明所用方式是 admissible open，则它有这两个不交开集组成的有限 admissible cover。结构层的粘合立即给
$$
 \mathcal O\bigl(U\sqcup Y(\Gamma)^{\rm ord}\bigr)
 =
 \mathcal O(U)\times\mathcal O\bigl(Y(\Gamma)^{\rm ord}\bigr).
 \tag{A4}
$$
因而在 $U$ 上取1、在 ordinary 部分取0就是一个截面；它在 ordinary 部分为零而在 $U$ 上非零。对线丛截面可在 $U$ 的一个非空平凡化子域作同样检验。ambient 模曲线的连通性并不将一个仅在这个不交开集上定义的截面自动延拓出去。

这里不是说 canonical-subgroup 区域都不连通。有限层上可以另取连到 ordinary 部分的 Hasse 严格邻域。真正还需支付的是：

- 两个待比截面在同一个这样的连通邻域上都有实际延拓；
- $\flat$ 展开的全部系数在该邻域上满足所用的一致收敛/整性条件，且原权下降仍成立；
- 这两个延拓分别限制为原 CM 区域上的截面及 ordinary 上已经比较的截面。

只有取得这些条件，才能在各相关连通分支上使用恒等原理。好 CM 点处存在一个 canonical subgroup、局部 period 不等式以及局部权下降，分别都不等于上述共同延拓。此次独立审读尚未从所引用的 Proposition7.15、7.18 或7.20中取得它。

另一个可接受的补法是直接在本项目的固定 theta 来源上证明(A3)，连同其 raised 算子、全部级结构和 finite trace。这样的证明可以绕开共同延拓，但必须给实际同源算子等式，不能仅用全局 $L$ 因子相同。

### 5.3 负权 Coleman/fp 接合有同一个费用

专著第9章印刷页245–247的(9.11)–(9.16)再次使用 ordinary 部分和上述 $U$ 的比较。(9.12)先在 ordinary 部分把 $G_{-1}$认作 $w^{(p)}$的 Coleman primitive，随后用解析延拓/唯一性将其带到 supersingular CM 区域，再以 Hodge 值配对读取 $H_{-(j+1)}$。

在共同延拓尚未补上时，这一步不能由普通区域的等式给出。尤其不能只说两个原函数至多差一个水平常数：尚须在 supersingular 区域证明它们具有同一个微分及 Frobenius 归一。对一个只由(A1)和权极限构造的局部对象，普通部分的 primitive 身份本身不支付这两件事。BDP 的 primitive 配对公式在已有真正 Coleman primitive 后适用，不反向证明它就是(A1)的负权值。

因此本项目的 $H_{-2}$到同一 proper-fp Abel–Jacobi 读数的接合，必须与正权(A3)同时标为待证；不能撤去正权连续插值却单独保留该负端点识别。

### 5.4 项目中保留及收紧的范围

以下独立内容不因这个缺格而撤回：原有限 Schwartz 与完整 Weyl 相位、两个实际 Hermite 槽及其所有合法正整数权身份、真实 fixed-base $p^2$ Hecke 全和、单独的 proper finite-polynomial 图杯积公式、纯 Newton 的完整尾界及连续函数、直接晶体/Manin 残余公式，以及普通情形的有限代数点载体。

需要改成条件陈述的是：用 Proposition7.20/Corollary7.21把 $\flat$ 连续权族与(A2)的全部经典正权值相接，再用第9章上述步骤把该族的负端点认作实际几何值。旧 full54、新六线及新 $\psi_4$ 图的全精度 cross 若经过这条接合，其几何端点结论均保留这一明确前提。

在正整数权上消去共同非零常数只得到那里本来的代数等式。若没有已证明的连续几何族及其实际端点，就不能用正整数权稠密性将这条等式带到 Abel–Jacobi 值。反过来，独立 Newton 函数可以继续使用，但不得以其定义替换缺失的几何族。

本节未执行数学程序，也未声称已有反例。需要补的确切门是(A3)或§5.2的共同连通延拓，再加§5.3的微分/Frobenius相容。

**原文定位。** D. Kriz, *Supersingular p-adic L-functions, Maass–Shimura Operators and Waldspurger Formulas*, Annals of Mathematics Studies212，Definitions6.18–6.19、Propositions7.15、7.18、7.20与第9章(9.11)–(9.16)。[出版社 DOI](https://doi.org/10.1515/9780691225739)。审读的书页转录为 [专著全文页](https://dokumen.pub/supersingular-p-adic-l-functions-maass-shimura-operators-and-waldspurger-formulas-ams-212-9780691225739.html)。本节对不交并集的(A4)为自给证明，不把一般 rigidity 口号当作缺失的延拓。

## 6. 一个固定正整数权的精确非零核验输入

本节选定一次 $p=227$、$u=1$，没有扫描目标素数。它在原双 Newton 的 $p>211$ 范围内，且不在固定坏集合 $\{2,3,7,17\}$。原两个普通 Taylor 指标为
$$
n=(p^2-1)u-2=51526,\qquad n+2=51528.
$$
在 $q=z^6$ 中写
$$
D_-(z)=z^4G_-(q),\qquad S(z)=z^6G_+(q).
$$
两个所需系数都准确是 $[q^{8587}]G_\pm$，完整计算精度为 $q^{8588}$。辅助模数固定为 $\ell=65537$；它只证明有理系数在特征零非零，不是目标 $p$ 的单位测试，也不给无穷素数结论。

### 6.1 全部系数及独立身份

置 $x=\wp(z)=z^{-2}X(q)$。原 $y^2=x^3+1$ 给
$$
X_0=1,\quad X_1=-1/7,\quad
X_m=\frac{6\sum_{i=1}^{m-1}X_iX_{m-i}}
{(6m-2)(6m-3)-12}\quad(m\ge2).
$$
整窗另检验一阶身份
$$
(-2X+6qX')^2=4X^3+4q\pmod{q^{8588}}.
$$
再由
$$
\log(\sigma(z)/z)
=-\sum_{m\ge1}\frac{X_mq^m}{(6m-1)(6m)}
$$
按精确递推生成 $E_{34}=(\sigma/z)^{34}$ 与 $E_{102}=(\sigma/z)^{102}$，各自整窗检验 $E_c'=c(\log(\sigma/z))'E_c$ 及常数1。

完整正源用原多项式
$$
S=\sigma^{34}\frac{x^2}{7}(x^3+1)(x^3-8)
          (7x^6-4x^3+16).
$$
完整负源使用原两 Weyl 词的和
$$
R_{102}(x,y)=\sum_{a=1,4,7,10,13,16}r_ax^a
\bigl[(-2\delta)^a(y+\delta)^a(y-\delta)^{34-2a}
 +(2\delta)^a(y-\delta)^a(y+\delta)^{34-2a}\bigr],
$$
其中 $r=(256,1376,1216,58,-37,1)$、$\delta^2=-3$。奇次 $y$ 项消去，全部偶次用 $y^2=x^3+1$ 返回，得到 $R_{102}=xP_{16}(x^3)$。脚本生成并读取全部17项，独立断言最高项为301056，再取 $D_-=\sigma^{102}R_{102}/301056$；不截去任一 Weyl 词或负源尾项。

在所需精度内，所有递推和积分分母均为 $\ell$ 单位：递推分母可写 $6(m-1)(6m+1)$，其出现的正因子都小于 $\ell$；$7$、$301056$ 也不被 $\ell$ 整除。因此若两个模 $\ell$ 系数非零，它们就是原两个有理系数的严格特征零非零证书。由原完整整数回卷(7)，这将给 $R_{\rm can}(p-1)\ne0$，足以使用§2的连续性障碍；它不支付§4–5尚缺的实际toric比较。

### 6.2 执行、审计范围与保存

公开 Actions 的固定脚本为
[check-original-psi4-fixed-positive-p227.py](../scripts/check-original-psi4-fixed-positive-p227.py)，使用 python-flint0.9.0。临时 C 例程只做两条显示卷积递推；全部累计量有精确的有符号64位上界，FLINT另检整窗椭圆身份及两个指数微分身份。原前缀只在进程内存在，报告保脚本/输入/hash、两个残余值与身份状态，不写前缀、矩阵或重算输出文件。

本节发布时仅提交固定输入与脚本，尚无执行结果。若残余为零，不由它推原系数为零；须按实际返回决定下一严格核验。若非零，也只给这个单一正权的特征零结论。

脚本初版 SHA256：95c9e8892f8b6b834cb6ecc1ad64bd38775cfce8eb719c4e0061eb3bed8f30b2（7527B）。

### 6.3 真实公开回执与所付结论

固定输入在 [公开 run46073583710](https://github.com/Rogerhu12/math-research-public/actions/runs/46073583710) 的 job140756005342 成功；源提交为38d4107ce0fa11b0fdf5c99a6df6596d6c3c32f5，2026-11-27 21:57:33 UTC 返回。实际报告确认两个所需模 $\ell$ 系数均非零，整窗椭圆身份、两条完整指数微分身份及两源首项归一全部通过，且脚本SHA与上节完全相同。

因此现在已经严格支付
$$
[z^{51526}]D_-\ne0,\qquad [z^{51528}]S\ne0,\qquad
R_{{\rm can},227}(226)\ne0.
$$
最后一步仅使用原完成的整数Newton回卷及非零标量。它不要求这两个数是227单位，不读取augmentation，也不提供任何无穷素数结论。

这使§2–3的非零前提在一个合法固定 $p$ 真实成立：若实际几何正权比较最终只有所示固定底数幂，那么它不能同时是上述纯Newton读者的非零连续倍数。必须补付或更正真实flat/同源/微分比较；加一个未证Gamma因子或说参考端点可能为零都不解决这个已显示的障碍。仍不由本节宣称被引用定理本身为假。

按规则15只登记脚本、输入、run和hash，不在仓库保存可重算前缀或结果文件。stdout为1239B，SHA256为b74f221e90348e596670facaa5d0f0e868ee0e7c4351565d8ed477725ee8019f；两个完整前缀hash由同一run现场报告。

实际job日志读取为10040B，SHA256 4cdeb95d353a5131ad33e76ea7f5fe624d6c44c42cd41cd1495b54e5f4b7ef5d，未落库。

## 7. 原通常剔除正整数序列的固定张量倍率与非连续性

本节的对象是原实际 fixed-base、完整十八图/finite word、通常 $p$-depletion、未除幂 raising 所定义的正整数序列。它不先把该序列称为已经连续的 $\flat$ 读者。所有 fixed CM 微分与 level 比较保留；尤其不令 $\Omega_\Gamma=1$ 或宣称它为单位。

### 7.1. 同一完整 raised 张量的固定基比较

在固定 CM 点取代数微分 $\omega_0$ 和代数余切基 $e_0$。用实际 CM splitting 作完第 $n$ 次普通 Gauss--Manin/Maass--Shimura raising 后，得到的同一张量属于
$$
\mathscr W_n=\omega^{\otimes3}\otimes(\Omega^1)^{\otimes n}.
\tag{Q1}
$$
这里没有除以 $n!$。设另一套实际基为
$\omega_* =a_p\omega_0$、$e_*=b_p e_0$，其中
$a_p,b_p\in\mathbf C_p^\times$ 固定。若
$v_n=t_n\omega_0^3e_0^n=t_n^*\omega_*^3e_*^n$，则准确有
$$
t_n^*=a_p^{-3}b_p^{-n}t_n.
\tag{Q2}
$$
这是对已经完成的同一张量换基，不是先把一个非恒定函数移过连接、再迭代新算子；因此没有遗漏换基函数的导数项。

实际 KS、两个固定 level 的余切比较以及同一个 CM period 的比较，都是固定点上的线丛同构。逐次张量后各自只添一个固定非零标量的 $n$ 次幂。无穷嵌入和 $p$ 进嵌入均先比较同一代数 raised 张量，不能把复数 $\Omega_0/\pi$ 直接嵌入 $\mathbf C_p$。当前来源的 finite Haar、完整 projector 和 raw 幅度均已固定；没有另按权除 raised-vector 范数或 Whittaker Gamma。

因此，针对当前明定的未除幂正整数序列，任何仅由这些真实固定张量基构成的比较必为
$$
q_{p,n}=q_{p,4}\,Q_p^{\,n-4},
\qquad q_{p,4},Q_p\ne0,
\quad n\equiv4\pmod6.
\tag{Q3}
$$
$Q_p$ 保留全部实际 KS 与 level 比较值，不对其估值作断言。

原 full $p^2$ orbit 的这一归约不增加隐含随权和：新 cross §7.2 已逐项保留代表 $\alpha_D$ 的微分运输，原 $\alpha_D^{-(3+2n)}$ 与其 weight-$3+2n$ transport 准确相消；§6 的完整 usual-depleted Euler 和是
$$
E_p=p(p+1)(1-p^{-2}),
\tag{Q4}
$$
与 $n$ 无关且非零。degree17 的 $17^n$ 已在实际 $\mathcal T_k(n)$ 中支付。故 (Q3) 适用于这个完整 usual-depleted 正整数对象；它尚未把任何 $\flat$ 投影认作该对象。

### 7.2. 7.19 与 7.22 的 determinant 费用

对 $g_2=\operatorname{diag}(1,p)$，Kriz (7.13) 给
$g_2^*\omega_{\rm can}=p\omega_{\rm can}$ 及
$g_2^*dz_{\rm dR}=p\,dz_{\rm dR}$。因此 (Q1) 的实际张量基倍率是
$$
g_2^*(\omega_{\rm can}^3(dz_{\rm dR})^n)
=p^{3+n}\omega_{\rm can}^3(dz_{\rm dR})^n.
\tag{Q5}
$$
这就是 Definition7.19 使用的基与倍率。

可用 determinant 线精确记账。令
$\mathscr D=\det H^1_{\rm dR}$；保持同源等变性的 KS 写为
$\Omega^1\simeq\omega^2\otimes\mathscr D^{-1}$。于是
$$
\mathscr W_n
 \simeq\omega^{3+2n}\otimes\mathscr D^{-n}.
\tag{Q6}
$$
degree-$p$ pullback 在 $\mathscr D$ 上的倍率为 $p$，所以右边的倍率仍为
$p^{3+2n}p^{-n}=p^{3+n}$。中心 $pI$ 的微分倍率为 $p$、determinant 倍率为 $p^2$，而 $dz_{\rm dR}$ 不变，也给相同核对。书中紧接 (7.14) 的脚注明确要求这个 $\det^{-1}$ 扭曲。

Proposition7.22 显示 $p^{3+2n}$，其证明使用未显示 determinant 因子的 $\omega_{\rm can}^{3+2n}$ 基。若把它作为一个另行 re-trivialized、untwisted weight-line 数列的定义，则与 (Q5) 相差的正是 $p^n$ 型固定幂费用。当前审计未取得把这两套 Hecke 线性化认作同一个 $F_n'$ 的额外 KS 识别，因此不把 $p^{3+2n}$ 当作已经独立审定的原 (Q1) 倍率，也不以任意“隐藏 determinant”替作者补证。

这个区别不影响 (Q3)：保 determinant 的实际比较和字面使用 (7.22) 定义的另一正整数序列，都只把 $Q_p$ 换成另一个固定底数。它不能改变任何阶乘。这里不宣称该书的完整定理为假。

### 7.3. 原 Hermite 两阶乘在代数规范下仍全部存在

原完整正常排序核确给 $n!(n+2)!$，不是单一阶乘。用同一代数 CM 张量实现其 archimedean 比较后，存在固定非零底数 $\xi$，使
$$
c_n=\frac{n!(n+2)!}{4!\,6!}\,\xi^{\,n-4}.
\tag{Q7}
$$
理由是原审计(1)已经给出 archimedean 的固定幂比，而从该实现到 (Q1) 的代数实现正是 (Q2) 的同一次张量比较。后者只改变底数，不添加或删除 Gamma 因子。

(Q7)不要求为一个复周期任意选择 $p$ 进像。也可完全从实际代数值锁住所需底数：$\mathcal T_k(n)$、$B_k$ 与原 Taylor 系数均按原定义代数；$n=4$ 及本次 $n_*=51526$ 的 canonical 值都非零。因此 (Q7)在复实现中的 $\xi^{51522}$ 是一个非零代数数，故 $\xi$ 本身代数；沿原固定嵌入取其像即可。更换允许的有限根只改固定底数，不改下述结论。这个论证用的是已付同一张量比较，不能用于一个另按 $n$ 任意重归一的来源。

### 7.4. 固定 $p=227$ 已排除这个 literal 序列的连续延拓

令
$$
n=(p^2-1)u-2,\qquad r=(p-1)u.
$$
保原 common $B_k$、Gaussian 和 degree102/34 的整数 Newton 回卷，将
(Q3)、(Q7)代回原正权值，得到
$$
L^{\rm lit}_{k,p}(u)
=K_{k,p}\mathfrak q_p^u
 \frac{\left(((p^2-1)u)!/((p-1)u)!\right)^2}
      {(p^2-1)u-1}\;
 R_{k,p}((p-1)u),
\quad u\in\mathbf Z_{>0},
\tag{Q8}
$$
其中 $K_{k,p},\mathfrak q_p\ne0$ 固定；$R_{k,p}$ 是原已证明连续的完整 Newton 函数。全部 period、KS、determinant、$E_p$ 和其它固定尺度都在这两个常数内，没有删除一项低卷积。

原公开 run46073583710/job140756005342 已精确证明
$$
[z^{51526}]D_-\ne0,\qquad [z^{51528}]S\ne0,
\qquad R_{{\rm can},227}(226)\ne0.
\tag{Q9}
$$
固定辅助模数65537的真实回执只证明两系数在特征零非零，不宣称227单位；不在此复制可重算结果表。源提交38d4107ce0fa11b0fdf5c99a6df6596d6c3c32f5，全部 source、完整两指数及椭圆整窗身份保留。详细回执见原审计§6。

对 $p=227$，若 (Q8)的 literal 数列有连续延拓到 $\mathbf Z_p$，则原审计§2的数字分块引理应用于
$R(u)=R_{{\rm can},227}(226u)$，将迫 $R=0$，与 (Q9)矛盾。因此：

**由当前完整正整数来源、通常 depletion、未除幂 raising 及固定张量规范组成的 literal 数列，不存在连续延拓。**

这已经不是“参考端点或许为零”的条件问题。它要求实际 $\flat$ 族与该 literal 数列之间另有尚未支付的算子/定义域/规范变化；不能再将二者无条件认同。若以后引入非固定幂的权归一，必须从原算子证明它并重新核对其实际 proper-fp 端点，不能为消数字障碍而补入一个无来源的 Gamma 因子。

本节保留原全部 positive-weight、proper 图与纯 Newton 结论。它不由一个已显示的接合不相容断言 Kriz 定理本身为假，也不据此生成原 canonical 新零行。

**依据。** 原审计§§1–6；原 psi4 full-graphs cross §§3、6、7.2（这里只用独立正整数身份）；Kriz专著 (7.13)、Definition7.19及其脚注、Proposition7.22。书页转录：https://dokumen.pub/supersingular-p-adic-l-functions-maass-shimura-operators-and-waldspurger-formulas-ams-212-9780691225739.html
