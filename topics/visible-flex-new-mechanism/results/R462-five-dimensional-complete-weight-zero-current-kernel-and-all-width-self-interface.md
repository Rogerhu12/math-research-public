# R462：完整权零内部 current 核的五维缩减与全宽 self 匹配入口

日期：2026-11-16。**原已付结果的只读消费与纸面证明。没有执行新的符号、矩阵、秩、profile、积分、科学程序或人工测试。**

[R459](R459-one-common-signed-witness-for-all-internal-fluxes-of-the-equal-width-library.md) 已在从起点选择的同一物理宽度库上构造一个有号成本：它保全部 $J^+$，且同时清全部角色和全部实际副本的两个内部 partial。该稿最后使用的完整响应可以混合真权。因此，其同宽结论不能直接用于所有正伸缩查询，更不能直接当作新的 actual 联合截面。

本文先把这个具体缺口压缩到完整原响应中的一个很小空间。记
$$
\mathcal R_{E,0}=\mathcal R_0\cap\ker E,\qquad
\mathcal K_0=\mathcal R_0\cap\ker E\cap\ker\mathscr C,
\quad E=(\pi,\mathcal Q),
\tag{1}
$$
其中 $\mathscr C$ 是 R433/R434 的三后缀、全部形式 jets 上的完整 Af current，始终采用 $\mathcal K/4$ 的39坐标规范。结论为
$$
\boxed{\dim\mathcal R_{E,0}=6,\qquad
\operatorname{rank}(\mathscr C|_{\mathcal R_{E,0}})=1,\qquad
\dim\mathcal K_0=5.}
\tag{2}
$$
另一方面，原49个已付 self 方向所选完整成本模块 $\mathscr M_{49}$ 的真权零部分恰为
$$
\boxed{(\mathscr M_{49})_0
=\operatorname{span}\{K_8,V_{51},V_{52}\}\subset\mathcal K_0.}
\tag{3}
$$
它们在 R455 的一个固定物理镜对上的完整 self 多项式像仍恰为三维。

所以，原49模块以外尚有恰两维**完整成本**需要处理。本文没有把它们的 self 像预授为两维，也没有证明当前权零目标在五维核的像中。以下给出准确的全宽匹配判据、旧输出定位，以及尚需的新原式读出。

## 1. 两个原维数已经由完整旧结果支付

[R201 §5(9)](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md) 使用 R196 的完整真实空间，给出
$$
\dim\mathcal R_0=16,\qquad
\dim\pi(\mathcal R_0)=3,\qquad
\dim(\mathcal R_0\cap\ker\pi)=13.
\tag{4}
$$
这里的 $\mathcal R_0$ 是整个原响应空间的真权零部分，包含原 $E_8\otimes W$ 的全部分支；不是原144标签的某个子空间。

[R316 §§1—2](R316-complete-weight-zero-self-membership-and-positive-character-representative.md) 随后明确以这**全部13维 pure 核**为比较域。它逐个原非主元减去 R201 的三个 pure 基，得到13个完整响应基，whole-$\mathcal Q$ 的忠实 T/Euler 像秩准确为7。因此秩—零化度直接给
$$
\boxed{\dim\mathcal R_{E,0}=13-7=6.}
\tag{5}
$$
本稿没有再计算这个7，也没有重新编译 R126/R316 原 mixed 根。

为使来源可以直接核对，R316 的首次公开实际为：

| 项目 | 原值 |
|---|---|
| run | 43735872441 |
| job | 132878270740 |
| source | ca186db057ed753abe565d0c3c2c8305278b5af7 |
| 主 COMPLETE_REPORT 时间戳 | 2026-11-15T16:31:27.0689291Z |
| 主 JSON 加 LF 字节 | 61441 |
| 主 SHA256 | 731ffae43cc8f06346801c444a7de010fe2cf6f9f05ecf4b650d319fa2ee06fd |

同一日志在16:31:16另有 development 的 COMPLETE_REPORT，不能要求整个 tag 唯一。主报告中的
$complete\_response\_pure\_kernel.kernel\_dimension=13$，
$all\_pure\_kernel\_branches\_in\_this\_weight\_included=true$，
以及 $decision.comparison\_self\_rank=7$
是(5)使用的实际记录。

主报告确实保存13条完整原列组合，以及各列全部 T/Euler；它**没有直接公布六维 whole-E 核的一组成本组合**。本稿只使用已付秩，不把尚未公布的六核组合称为已消费，也不为取得它们重做旧消元。

## 2. 完整 current 的真权：只剩两个权零坐标

沿用 [R459 §3](R459-one-common-signed-witness-for-all-internal-fluxes-of-the-equal-width-library.md) 已从同锚原式得到的准确输运。令
$$
(C_{H,c}u)(y)=u((y-c)/H),\qquad
T_{H,c}n=(n_0,cn_0+Hn_1,c^2n_0+2cHn_1+H^2n_2).
$$
若 $F_V=\mathcal K_{V,n}/4$ 表示 Af 上的完整 current，则
$$
\boxed{
F_{P_{H,c}V}(x,u,p,r;n)
=H^{-1}F_V(Hx+c,u,p/H,r/H^2;T_{H,c}n).
}
\tag{6}
$$
真实下端和全部右锚同时输运，没有新增 primitive 常数。

取 $c=0$。一个 monomial
$x^ju^\alpha p^\beta r^\gamma n_k$
的**原成本真权**是
$$
\sigma=j-\beta-2\gamma+k-1.
\tag{7}
$$
它不是 profile 评价本身的表面缩放次数。

R433 §3.2 的每个后缀块由六个完整含 $u$ 形式列和七个 $p$ 列组成。六列必须连同其原 $p$ 部分一起输运，不能只选一个含 $u$ 单项。由其原式(18a)—(18c)逐项读出：

| current 坐标（乘 $n_k$） | 真权 |
|---|---:|
| $A_0$ | $k-3$ |
| $A_1$ | $k-2$ |
| $A_2$ | $k-1$ |
| $B_0$ | $k-4$ |
| $B_1$ | $k-3$ |
| $C_0$ | $k-5$ |
| $p^3$ | $k-4$ |
| $p^2r$ | $k-5$ |
| $xp^2r$ | $k-4$ |
| $pr^2$ | $k-6$ |
| $xpr^2$ | $k-5$ |
| $x^2pr^2$ | $k-4$ |
| $S_7=2xp^3-5x^2p^2r+3x^3pr^2$ | $k-3$ |

例如 $A_1$ 完整列的各项是 $xup^2,upr,x^2p^3,x^3p^2r,x^4pr^2$ 的固定组合；它们在(7)中全具有权 $k-2$。$A_2$ 的 $u^3$ 项及其余原项也统一具有权 $k-1$。

由于 $k=0,1,2$，39维形式 current 空间的权零部分恰为
$$
\boxed{
(\mathscr F_{39})_0
=\operatorname{span}\{A_1^{\,2},A_2^{\,1}\}.
}
\tag{8}
$$
上标表示真实矩 $n_k$，不是幂，也不是成本编号。

## 3. 全响应的 current 秩恰为一，核恰为五

[R434](R434-complete-self-kernel-and-three-tail-current-image-on-144-original-responses.md)
已在原144列的 whole-E 核上完整求得32维 current 像，并给七条充要关系。
[R454](R454-complete-response-self-principal-trace-and-seven-ordered-current-invariants.md)
随后用全部原 $\mathcal R$ 的 trace 身份证明：原32个 lifts 已经给整个响应的准确像
$$
\mathscr C(\mathcal R\cap\ker E)=\ker D\subset\mathscr F_{39}.
\tag{9}
$$
本稿使用(9)，没有把144标签自动当成整个 $\mathcal R$。

在(8)中，七条关系仅剩
$$
\boxed{A_1^{\,2}+\tfrac12A_2^{\,1}=0.}
\tag{10}
$$
所以 $\dim(\ker D)_0=1$，并且该空间非零。例如取
$A_1^{\,2}=1,A_2^{\,1}=-2$，其它37坐标零，即满足全部七关系。

由(9)，这条非零形式 current 有一个真实 $R\in\mathcal R\cap\ker E$ lift。它起初可混权，故还需保持原作用的投影步骤。整个 $\mathcal R\cap\ker E$ 对正伸缩稳定，原有限真权投影 $\Pi_0$ 是有限个足够接近1的正伸缩的**有号**线性组合。由(6)，
$$
\mathscr C(\Pi_0R)=\Pi_0\mathscr C(R)=\mathscr C(R).
$$
于是该非零行确由 $\mathcal R_{E,0}$ 实现。这是完整成本的有号谱投影，不声称投影系数为正时间。

因此
$$
\operatorname{rank}(\mathscr C|_{\mathcal R_{E,0}})=1.
\tag{11}
$$
结合(5)，得到
$$
\boxed{\dim\mathcal K_0=6-1=5.}
\tag{12}
$$
由于全部响应的自然函数恒零，$\mathcal K_0$ 中的成本也保持当前 $A$、$O_{\rm all}$；但(12)只给线性成本空间，不提供新的 actual 原型截面。

## 4. 原49模块的权零部分只有三条完整成本

这里的 $\mathscr M_{49}$ 指 R443/R448 选定的十一条 $K_n$ 和38条独立 self 成本 $V_i$ 的 span。它们的 self current 已证明独立，所以这些**完整成本本身**也独立。没有把所有53个 current 核关系都称为独立成本。

原 $E_8=(P,R,S,L,U,V,T,Y)$ 的真权为
$$
(-3,-2,-2,-1,-1,0,0,1).
\tag{13}
$$
R261 原第三方向的权为
$$
\operatorname{wt}H_j=j-5,\qquad
\operatorname{wt}J_j=j-3,
$$
$$
\operatorname{wt}(\chi_{30},\chi_{32},\chi_{34},\chi_{37},
\chi_{40},\chi_{100},\chi_{104},\chi_{109})
=(-4,-3,-3,-2,-1,-2,-1,0).
\tag{14}
$$
每个响应 $\mathcal B_E\tau$ 的真权是两者之和。
以下分组是对 R443 已付原组合标签逐项读(13)—(14)，没有再求 self 秩：

| 真权 | 38个独立 $V_i$ 的原编号 |
|---:|---|
| $-7$ | 9 |
| $-6$ | 8，10，11 |
| $-5$ | 12，13，15，16，20 |
| $-4$ | 17，22，23，25，26，28，33 |
| $-3$ | 18，27，29，30，35，36，40，41，46 |
| $-2$ | 31，37，38，42，43，47，48 |
| $-1$ | 44，45，49，50 |
| $0$ | 51，52 |

每个所列原组合本身齐次；不是只看其 self 的最高 $x$ 项。另由原局部轨道
$\operatorname{wt}K_n=n-8$，十一条 K 中仅 $K_8$ 为权零。
于是(3)成立。

为固定最后两条的完整标签，原已付组合是
$$
\begin{aligned}
V_{51}={}&-\tfrac1{44160}\mathcal B_YH_4
-\tfrac1{4416}\mathcal B_VH_5
-\tfrac1{35328}\mathcal B_TH_5\\
&+\tfrac1{52992}\mathcal B_LH_6
-\tfrac1{52992}\mathcal B_UH_6
-\tfrac7{920}\mathcal B_YJ_2\\
&+\tfrac{224}{23}\mathcal B_Y\chi_{40}
-\tfrac{16}{23}\mathcal B_Y\chi_{104}
+\mathcal B_V\chi_{109},
\end{aligned}
\tag{15}
$$
$$
\begin{aligned}
V_{52}={}&-\tfrac{17}{132480}\mathcal B_YH_4
+\tfrac7{66240}\mathcal B_VH_5
-\tfrac{31}{264960}\mathcal B_TH_5\\
&-\tfrac{19}{198720}\mathcal B_LH_6
+\tfrac7{794880}\mathcal B_UH_6
+\tfrac{37}{920}\mathcal B_YJ_2\\
&+\tfrac{1024}{23}\mathcal B_Y\chi_{40}
+\tfrac{124}{23}\mathcal B_Y\chi_{104}
+\mathcal B_T\chi_{109}.
\end{aligned}
\tag{16}
$$
本节的 $V$ 是 $\Phi_{p_1}$，$Y$ 是 $\Phi_{p_2}$，不混用早期端口稿中的另一别名。
这两条均在 whole-E 核和全部 current 核内；K 轨道也同样成立。因此(3)确是完整 $\mathcal K_0$ 的三维子空间。

本次只读的 R443 原日志是 run43801705436、job133083261189、source9c796878a2f7f1b910ebcebadd0b2d05dc0d42ac。原 record seq55、56 给(15)—(16)，seq108、109给它们的完整 Af self current。所有原 rank、fresh 证书及原响应表均未重跑。

## 5. 这三条在固定物理镜对上也没有降秩

令当前实际镜对的共同 jets 为
$$
u_*=h_*r_*,\qquad p_* =s_*r_*,
\quad h_*>0,\ s_*>0,\ r_*>0,
$$
右镜点把 $p_*$ 换成 $-p_*$。这是 R455 新初选母的实际范围。

本节 self partial 始终是
$$
\mathcal F_x(V;u)=\int_{\ell_u}^{x}u'\Sigma_V(u)'',
\tag{17}
$$
没有除以4，不能与(6)的 ordered current 归一混用。

在左对应族中，固定 jets 并让物理根位置 $x$ 变化，除去共同非零 $r_*^5$。R443 完整原 current 的常数与 $x^7$ 系数分别为
$$
\begin{array}{c|cc}
&V_{51}&V_{52}\\ \hline
[x^0]&-\frac9{23}h_*^3s_*^2&\frac{31}{69}h_*^3s_*^2\\
[x^7]&-\frac{67}{1104}s_*&\frac{11}{138}s_*
\end{array}
\tag{18}
$$
两列最高次数均为7。该小行列式的手算为
$$
\boxed{-\frac{13}{3312}h_*^3s_*^3\ne0.}
\tag{19}
$$
原 $K_8$ 的 $x^8$ 系数则非零，且 $V_{51},V_{52}$ 没有该项。因此
$$
\boxed{\dim\mathcal F_{\rm mirror}((\mathscr M_{49})_0)=3.}
\tag{20}
$$
这已经由一个完整对应族的多项式读出得到，不需要选择新的 profile 或执行点值秩。
(20)不把三个系数的有号解当作实际路径，也不说原全部五维核在该镜对上有五维像。

## 6. 为什么全正伸缩匹配会准确落回权零

固定 R459 的真实母及共同物理镜对，设目标 $V_0\in U_0$ 已满足 $J^+=0$、$\mathscr C(V_0)=0$。只考察 self partial。

假设某个 $W\in\mathscr M_{49}$ 能同时匹配该母的全部中心和一个非空开区间的正宽度。先将这些查询全部拉回一个共同合法窗口；有限原次数保证它们是真有限 Laurent—多项式关系。
取 $c=0$，原 self partial 协变为
$$
\mathcal F_x(P_{H,0}V;u)
=H^2\mathcal F_{Hx}(V;C_{H,0}u).
\tag{21}
$$
因此，对同一个固定母的全部中心，按真权分解 $W=\sum_\sigma W_\sigma$ 后，
全宽匹配等价于
$$
\sum_\sigma H^\sigma\mathcal F_x(W_\sigma;u)
=\mathcal F_x(V_0;u)
\tag{22}
$$
在一段正 $H$ 上恒成立。不同整权 Laurent 项独立，故必要的是
$$
\mathcal F_x(W_0;u)=\mathcal F_x(V_0;u),
$$
而每个非零权分量的整镜对查询都为零。
反过来，一个权零 $W_0$ 若在同一宽度的全部中心准确匹配，则(21)直接给全部正伸缩的匹配，保同一原作用及真实端点。

因为 $\mathscr M_{49}$ 的每条所选基都齐次，$W_0$ 仍属于(3)。得到准确判据
$$
\boxed{
\begin{aligned}
&\text{原49模块能在整正仿射查询族上匹配 }V_0\\
&\quad\Longleftrightarrow\
\mathcal F_{\rm mirror}(V_0)
\in\operatorname{span}\{\mathcal F(K_8),\mathcal F(V_{51}),\mathcal F(V_{52})\}.
\end{aligned}}
\tag{23}
$$
这里“整族”是成本函数的有限仿射闭包；在几何使用时先保证所需有限查询和辅助路径有共同合法窗口。没有声称任意预先冻结的窄区间容纳全部无限伸缩。

R459 只需要同一物理宽度，其19维镜对像足够；(23)说明不能将那一条混权右逆免费提升为整仿射闭包右逆。本文尚未评价当前具体 $V_0$ 在(23)中的成员性。

## 7. 完整响应的下一最小问题：两维成本余部

由(3)、(12)，在完整成本空间中可以选一个补空间
$$
\mathcal K_0=(\mathscr M_{49})_0\oplus\mathscr B_2,
\qquad \dim\mathscr B_2=2.
\tag{24}
$$
这是有限维线性代数的存在陈述，不是两条已经读取的原组合。
它们的 self partial 可能增加零、一或二维像；不能从补空间维数倒推 self 观察秩。

整个 $\mathcal K_0$ 的全宽匹配准确等价于同宽完整镜对目标属于
$$
\mathcal F_{\rm mirror}(\mathcal K_0),
\tag{25}
$$
因为每条成本都是真权零。(25)的空间维数在3与5之间，但当前目标的成员性仍未付。

若要从既存数据选择(24)的明确原代表，旧定位已经完全固定：
R316 主报告的13条 pure 核，以 R126 old-column 非主元
$$
1,4,5,7,8,9,10,11,12,13,15,17,19
$$
编号；每条原组合、mixed SHA、全 T/Euler 都在该主报告。另需施加(10)的唯一 current 行。旧报告没有公布它的六个 whole-E 核代表，也没有公布这些代表的完整 self-cap，故本稿不声称它们已经可以从一句成员回执抄出。

一个后续观察若确有必要，只应消费这些已付列及其原根定位，新增所需 current/self contraction与完整原差重构；不应重复原 pure、whole-Q 秩、旧 mapper 验证或 profile 查询。具体选择与执行仍由另一个明确新目标支付，本稿没有执行它。

本稿完成的是：整个真权零响应的 **6→1→5** 精确缩减、原49模块的准确三维权零部分，以及同宽与全宽的必要充分范围区分。实际增广锥、全部正权原型成本、固定有限词的截面以及最后同一个十三行规范，均不由(2)—(25)自动得到。
