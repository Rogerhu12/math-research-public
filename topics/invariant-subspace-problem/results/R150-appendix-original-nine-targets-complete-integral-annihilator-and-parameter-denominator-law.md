# R150：原九目标的完整整系数湮灭理想与精确参数—分母判准

作者：Astra-ISP-789f / literature_audit，使用 GPT-6 Astra Pro。  
日期：2026-11-16。  
状态：同一次实际 Actions 任务完成原来源重建、全部四组目标读取及完整共同/逐列核；以下为原模中的精确结论。

## 1. 完整结论

令

$$
p=31,\qquad D=\mathbb Z_{(31)},\qquad R=D[s],\qquad x=s-2.
$$

保留原十七方程、全部 6188 个次数不超过三的来源和全部 4367 个输出：

$$
A:R^{6188}\longrightarrow V=R^{4367},\quad
L=\operatorname{im}A,\quad
N=V\cap\operatorname{im}_{\mathbb Q(s)}A,\quad C=N/L.
$$

原九个目标仍为

$$
t_j=\left(\sum_{a=0}^{j}\binom ja(-s)^{j-a}m_a\right)^2,
\qquad 2\le j\le10.
$$

置

$$
h_*=s^3F_+^2F_-^2E_8,\qquad h_0=xh_*,
$$

$$
M=\sum_{j=2}^{10}R[t_j]\subset C,\qquad
b_j=[h_*t_j],\qquad B=h_*M.
$$

其中 $h_*$ 的次数为 23，首系数为 $3125\in D^\times$。本次完整确定

$$
\boxed{
\operatorname{Ann}_R(B)=\operatorname{Ann}_R(b_j)
=(p^5,\ p^2x,\ x^2)
\quad\text{对全部九个 }j.
}
\tag{1.1}
$$

因此原九目标模和每个单目标的完整湮灭理想都是

$$
\boxed{
\operatorname{Ann}_R(M)
=\operatorname{Ann}_R([t_j])
=h_*\,(31^5,\ 31^2(s-2),\ (s-2)^2).
}
\tag{1.2}
$$

将 $h_*$ 首一化为 $m_*=\operatorname{mon}(h_*)$ 不改变这个理想。

特别地，旧全局有限精度目标 $H_{25}=(s-2)^2h_*$ 现在得到精确无 31 分母的原来源：

$$
\boxed{H_{25}t_j\in L\qquad(2\le j\le10).}
\tag{1.3}
$$

其原统一加权来源费用可取不超过 8515。这里的“无 31 分母”指来源系数属于 $D[s]$，不额外声称所有其他素数的分母也已消除。

## 2. 已证明的完整有限接口

[乘一个 31 后的完整湮灭理想](R150-appendix-original-nine-targets-one31-scaled-annihilator-and-hstar-tail.md)以及[原四次参数湮灭与四参数判准](R150-appendix-original-hstar-fourth-parameter-annihilator-and-complete-four-scalar-test.md)已在同一个原模中证明：

$$
T=C[p^\infty],\qquad
p^6T=0,\qquad B\subset T_2,
$$

其中 $T_2$ 为完整系数扭子的剩余参数根 2 主分量；根 1 分量的消失由原全局 $H_{25}$ 来源和有限载体证明，没有由有限域支持猜测。

真实除源基的系数指数为

$$
(e_i)=(1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6).
$$

它们在完整模 $p$ 商中独立，所给原循环来源的总长度为 50，恰等于完整 $T$ 的长度。因此这些真实来源构成 $T$ 的 $D$ 不变量因子基；其用途不限于一组任意有限域坐标。

上述两篇证明进一步给出

$$
\operatorname{Ann}_R(pB)
=\operatorname{Ann}_R(pb_j)
=J:=(p^4,px,x^2),
$$

$$
x^2B\subset S:=p^3T\cap T[p],\qquad
xS\subset p^4T\cap T[p],\qquad
xp^4T=0.
$$

空间 $S$ 是真实七维 socle，采用以下同一来源基：

$$
p^3g_{10},p^3g_{11},p^3g_{12},p^3g_{13},
\quad p^4g_{14},p^4g_{15},p^5g_{16}.
\tag{2.1}
$$

由此得到

$$
K:=(p^5,p^2x,px^2,x^4)\subseteq I:=\operatorname{Ann}_R(B)\subseteq J
$$

和完整有限判准

$$
I/K=
\ker\left(
\mathbb F_{31}^4\longrightarrow S^9,\quad
(\alpha,\beta,\gamma,\delta)\longmapsto
(\alpha p^4b_j+\beta pxb_j+\gamma x^2b_j+\delta x^3b_j)_j
\right).
\tag{2.2}
$$

这里 $J/K$ 的四个基为 $p^4,px,x^2,x^3$；$x$ 只把第三基送到第四基。式 (2.2) 确定整个理想，不是参数次数三以内的受限测试。逐个 $j$ 的同一七维判准也完整。

## 3. 同一次任务中的真实来源重建

实际运行是

$$
\texttt{run }43830684123,\qquad
\texttt{job }133175032397.
$$

任务于 2026-11-16 08:22 UTC 启动，08:33 UTC 完成，整体状态为 success。所有大数组、来源链及数学输出只在同 job 的临时目录和完成日志中使用；仓库身份文件只保存源、参数、run 和输出 SHA。

首先恢复四组历史输入：原十四文件、六个小系统、四族真来源及原整数模型/jet map、历史 $H_{25}$ 来源。恢复逐项核固定历史提交、成员路径、完整字节和 SHA。没有重建旧整个数 GB 来源链，也没有重算完整 210 列。

所需真来源按原配方的依赖闭包重建：

$$
8\longrightarrow7\longrightarrow3\longrightarrow1.
$$

这次实际重建完成全部 30 阶段，耗时 $211.847615678$ 秒。它保留原精度链

$$
25\longrightarrow20\longrightarrow15\longrightarrow10\longrightarrow5,
$$

原 $p^7$ 整数乘回、完整单位求解以及全部原来源运输。固定 $G,V$ 缓存除绑定头外的数学字节与旧完整计算相同；原 $F_2,F_3$ 配方在所取列的依赖闭包外严格为零，故没有省掉一个可能有贡献的来源。

前三个新除源族逐列匹配已付完整 315 类，最后一列与它们组合后再次核得同一个完整 $U_{16}$ 和 $J_{16}$：

| 身份 | SHA256 |
|---|---|
| 完整 $U_{16}$，$315\times16$ | 679132fd4727fd305b77c82beb5d3f2e002df1860045200c3392158ab8eb48b9 |
| 完整参数作用 $J_{16}$，$16\times16$ | 59d09cbeec71ebf7cda6f12ddd21c1b7ffe1c83a3f9de81b776df0a97df687d8 |

更关键的是，后续四组读取都在这一个新父来源 pack 内重新计算。每次子 binding 转换逐原 6188 行核来源标签和被选择的全部高 $p$ 系数，原 $G,V$ 数学 payload 也逐字节相同。并未仅因 $U_{16}\bmod p$ 一致，就把两套高 $p$ socle 坐标视为同一套。

## 4. 原整数尾链与本次精确读数

四组目标读取如下。

- 第一组重新计算原 $h_*$ 的首次 carry，重现全部九个目标系数阶恰为五，并由真实等式 $p^2b_j=p^3r_j$ 得到 $p^4b_j=p^5r_j$ 的 socle 坐标。
- 第二组重新计算原 $h_0=xh_*$ 的七维 socle，重现每个 $xb_j$ 系数阶恰为二，读取 $pxb_j$。
- 第三组直接计算 $x^2h_*t_j$，使用旧已验证的完整全局模 $p^3$ 来源作为起点。
- 第四组用同一个起点在 Taylor 变量中乘 $x=[0,1]$，直接计算 $x^3h_*t_j$。

后两组的初始原整数式为

$$
w-AY=p^3r_3,\qquad
w=x^2h_*t_j\ \text{或}\ x^3h_*t_j.
$$

原 native 计算的是 target 减原 $A$ 乘积，保留普通平方的非对角系数 2 和原全部归一常数。随后在完整原商中依次消去

$$
r_3=G_{13}a+Aq_3+pr_4,\qquad
r_4=G_{15}d+Aq_4+pr_5.
$$

每次来源补偿与整数 carry 同时保留，最后使用 $p^6T=0$ 得

$$
[w]=p^3G_{13}a+p^4G_{15}d+p^5G_{16}f.
\tag{4.1}
$$

这里读取的是 $w$ 本身，不是 $pw$。七个坐标分别为 $a$ 的四个指数四坐标、$d$ 的两个指数五坐标、$f$ 的唯一指数六坐标。

$15\to10\to5$ 的保真范围来自已付原 $G$ 最大 Smith 指数五及[嵌套精度引理](../notes/2026-11-15-r150-saturated-pages-integer-carry-and-nested-jet-precision-789f.md)。有限解的全部实际计算项仍逐原 $G$ 乘回，最后每一类保留全部 104 个局部自由条件、505 个全局自由观察、315 个原商坐标和原参数作用。其完成模解释使用第 2 节的完整有限载体与忠实完成；不把有限 Taylor 插值直接称为全参数多项式来源。

实际结果是：

| 读取 | 实际阶段数 | 数学耗时（秒） | 结果 |
|---|---:|---:|---|
| 同基 $h_*$ 首次 carry | 8 | 82.345290447 | 九目标系数阶均为五 |
| 同基 $h_0$ 七 socle | 16 | 95.042755233 | 九目标系数阶均为二，$pxb_j$ 像秩一 |
| $x^2h_*t_j$ 完整 socle | 16 | 95.122320656 | 全部 $7\times9$ 坐标为零 |
| $x^3h_*t_j$ 完整 socle | 16 | 94.522983255 | 全部 $7\times9$ 坐标为零 |
| 最终共同与逐列四参数核 | — | 0.004106351 | 共同及逐列秩均为二 |

两组新零矩阵的原 63 字节逻辑 SHA 均为

c7723fa1e0127975e49e62e753db53924c1bd84b8ac1ac08df78d09270f3d971。

全部 $63\times4$ 矩阵的字节 SHA 为

b27638011f625941db5a36dba6c5201f153b97387ffd2b8b3301fc50a9c219b5。

实际前两轴对每一个目标都非零且独立；后两轴严格为零。因此共同核与每个单目标核均为

$$
\operatorname{span}_{\mathbb F_{31}}
\{(0,0,1,0),(0,0,0,1)\}.
\tag{4.2}
$$

全部 63 行、九个单独 $7\times4$ 块、核乘回、核的 $x$ 稳定性都已核验。

## 5. 从完整核到完整理想

将 (4.2) 代入完整判准 (2.2)，即得

$$
I=K+(x^2,x^3)=(p^5,p^2x,x^2).
$$

每个单目标的完整判准有同一个核，故逐个理想也相同。这证明 (1.1)。

也可以用首一除法直接解释其全次数范围。任意 $f\in D[x]$ 唯一写成

$$
f=q(x)x^2+a+cx,\qquad a,c\in D.
$$

实际 $x^2b_j=0$ 已消去整条高次部分。此前完整两轴独立性给出

$$
(a+cx)b_j=0
\quad\Longleftrightarrow\quad
a\in p^5D,\quad c\in p^2D.
$$

因此不存在尚未检查的高次乘子，也不存在常数项和一次项之间隐藏的混合抵消。

回到原目标，已付有理定理给出每个 $[t_j]$ 及共同 $M_{\mathbb Q}$ 的最小多项式 $m_*=\operatorname{mon}(h_*)$。任意整湮灭子有理化后被 $m_*$ 整除。由于 $m_*$ 首一，$D[s]$ 中的长除余式也严格为零，故

$$
\operatorname{Ann}_R(M)=m_*\operatorname{Ann}_R(B),
$$

逐个目标同理。由 $h_*/m_*\in D^\times$，得到 (1.2)。

## 6. 任意参数乘子的精确 31 分母公式

令 $v_p(0)=+\infty$。对任意 $f(s)\in D[s]$，展开于 $s=2$：

$$
f(s)\equiv f(2)+f'(2)x\pmod{x^2}.
$$

将 (1.1) 应用于 $p^ef(s)$，得到每个目标和所有九目标共同的精确最小指数

$$
\boxed{
\min\{e\ge0:p^ef(s)h_*t_j\in L\}
=
\max\{0,\ 5-v_p(f(2)),\ 2-v_p(f'(2))\}.
}
\tag{6.1}
$$

右端对所有九个 $j$ 完全相同。它给出整个参数—系数取舍，而不仅是三个单项式例子：

| 参数乘子 $f$ | 精确最小 31 指数 |
|---|---:|
| $1$ | 5 |
| $s-2$ | 2 |
| $(s-2)^2$ 及其任意倍 | 0 |

更一般地，某个 $g(s)t_j$ 存在系数为有理数的原多项式来源，首先必须且只须 $m_*\mid g$ 于 $\mathbb Q[s]$。当 $g\in D[s]$ 时首一长除给 $g=m_*f$，随后由 (6.1) 决定所需 31 指数；用 $h_*$ 代替 $m_*$ 只相差一个 $D$ 单位。

原 $h_*$ 后所需额外首一参数因子的最小次数因此恰为二。确有 $x^2$ 可用；任何首一次式的 $x$ 系数为 1，不可能满足 (1.1)。

## 7. 单目标的完整循环模与缩放链

对每一个 $j$，同一完整理想给出

$$
Rb_j\simeq R/(p^5,p^2x,x^2)
\simeq_D D/p^5D\oplus D/p^2D.
\tag{7.1}
$$

因此每个单目标 $b_j$ 的系数长度恰为七。第二个同构只陈述 $D$ 模结构；参数 $x$ 把第一生成元送到第二生成元，再送到零。

共同理想的商环也有长度七，但这不能冒称整个九生成元模 $B$ 的长度为七。共同湮灭理想只说明 $B$ 是该环上的忠实模，不能由此断言它是循环模。

对原未乘 $h_*$ 的单目标，有

$$
R[t_j]\simeq R/(m_*I),\qquad I=(p^5,p^2x,x^2),
$$

以及精确短正合列

$$
0\longrightarrow R/I
\xrightarrow{\ \times m_*\ }
R/(m_*I)
\longrightarrow R/(m_*)
\longrightarrow0.
$$

最后一项是秩 23 的自由 $D$ 模，所以作为 $D$ 模该短列分裂，得到

$$
\boxed{
R[t_j]\simeq_D D^{23}\oplus D/p^5D\oplus D/p^2D.
}
\tag{7.2}
$$

这不是声称该短列作为 $D[s]$ 模也分裂。

完整缩放链亦已确定：

$$
\operatorname{Ann}_R(p^aB)
=
(p^{\max(5-a,0)},\
p^{\max(2-a,0)}x,\
x^2)
\qquad(a\ge0).
\tag{7.3}
$$

式 (7.3) 对每个单目标同样成立；当 $a\ge5$ 时右侧为单位理想。原 $p^aM$ 的理想为 $m_*$ 乘 (7.3)。

## 8. 原来源存在与统一费用

由 (1.1)，下面三组原目标都有真正的 $D[s]$ 来源：

$$
p^5h_*t_j,\qquad
p^2(s-2)h_*t_j,\qquad
(s-2)^2h_*t_j.
$$

沿用[完整系数指数六与统一原来源费用](R150-appendix-complete-coefficient31-exponent-six-and-exact-original-p2h0-sources.md)，第 6 节，保持实际 $D_*=\det B_*$ 的原归一不变。其三个来源降度支为

$$
8515,\qquad8515,\qquad\tau(\text{目标})+1.
$$

原 $\tau(h_*t_j)\le63$；系数标量 $p^a$ 不改变参数次数。上述三组目标的第三支分别至多为 $64,65,66$，所以每组九个来源的统一费用均至多为 8515。

这给精确来源的存在与次数界，没有展开全部全局来源或提供系数高度。对于任意更高次参数倍 $f$，同一论证给上界 $\max\{8515,64+\deg f\}$，只在 (6.1) 指定的真实成员性条件满足后使用，不声称任意高次目标都具有与次数无关的费用。

## 9. 实际来源、输出身份与独立复核

完整源及参数由[输入 manifest](../notes/2026-11-16-r150-original-hstar-four-parameter-complete-manifest-789f.json)和[完整接口](../notes/2026-11-16-r150-original-hstar-four-parameter-complete-interface-789f.md)固定。最终核消费者为

[2026-11-16-r150-original-hstar-complete-four-scalar-kernel-789f.py](../notes/2026-11-16-r150-original-hstar-complete-four-scalar-kernel-789f.py)。

其源码为 13275 字节，SHA256：

f2607b2df00e44fd0a77da4fc01a72cc72a359b1751b2007e8852d6ae1db4758。

实际最后步骤的 execution source 为

d5b7bfc6a39c63890b9cae3e72cd268c1e670911。

实际身份见[最终步骤记录](../notes/r150-hstar-four-parameter-execution-789f/43830684123-complete-original-hstar-four-scalar-annihilator.json)。最后消费者的数学耗时为 $0.004106351$ 秒，进程墙钟为 $0.064094956$ 秒。最终绑定为

9a83cce4164d9e1a1f425caa86ef7157dc52a96f8a62cc73bf69205bb1263042。

同一次真实父来源绑定为

a19758638abbd51829fd2381aeb70dddcbabf4f31878bc3c66a08e18ec240625。

六个数学步骤的完整临时 receipt 身份如下，均退出零并已完成：

| 步骤 | bytes | SHA256 |
|---|---:|---|
| 8→7→3→1 真来源重建 | 27369 | f2d33c57d04f609e6b5e39a69da9933cfc68f56f7a55b67a4dc0853f4f2dff48 |
| 同基 $h_*$ 首 carry | 17203 | 273eff195255b544005740b1a382b3a5c3ab2ee6f55593f98599f45c63aa393e |
| 同基 $h_0$ 七 socle | 23917 | cf79d372a7f297422803fcdd6bb0cf12ca2721898814222ee15f7acb0a73247f |
| 同基 $x^2h_*$ | 26336 | a58a0b5c289d09a2eb5a25a6198aa59625929bbffc78bb9d825fe9fc2f4755bd |
| 同基 $x^3h_*$ | 26339 | 8881a23a87a5c95161564960bb6c5ad75106057d40357cdc7d522c8fd3f28779 |
| 完整四参数核 | 12803 | 15e8dd4229d99debd70e967d2970be74adac6589b0dfd8bfa7c5f44538a9eeb0 |

最后实际结果文件为 9443 字节，SHA256：

b6414bfdab4143224c946c9a5a92c399d2f6d0372e1e8257068f87e7e1ea1f2b。

完成后，独立的[只读日志审计](../notes/2026-11-16-r150-original-hstar-four-scalar-completed-log-audit-789f.js)在 V8 中实际执行：保留日志内 Python 数字的原字面，恢复上述六份完整数学 receipt 的字节并逐 SHA 匹配；再由四个父结果重新拼接全部 252 坐标，逐九块与共同矩阵独立消元，并核 126 个新坐标全部为零。根审计另独立核了六个数学 binding、全部父 raw receipt、30/8/16/16/16 阶段、五项完整原门槛和选源支持，并从新父结果重新构造四轴；共同与九个单块的十四个矩阵字节 SHA 全部匹配，逐九原两轴子式均为单位。以上都是对已完成真实计算的独立小复核，没有重新执行大来源链。

本附录完成该原秩一来源模在系数素数 31 处的共同与逐九完整湮灭理想。它不把这一结论提升为一般非秩一梯度理想或普通不变子空间问题的解答。
