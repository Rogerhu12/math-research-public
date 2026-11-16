# R150：九个原目标乘一个 31 后的完整湮灭理想

作者：Astra-ISP-789f / literature_audit，使用 GPT-6 Astra Pro。  
日期：2026-11-16。  
状态：已完成原来源尾层的只读审计，以下均为同一个原模中的精确结论。

## 1. 完整理想，而不只是三个正恒等式

令
$$
p=31,\qquad D=\mathbb Z_{(31)},\qquad R=D[s],\qquad x=s-2,
$$
保留原十七方程、全部 6188 个次数不超过三的来源和全部 4367 个输出：
$$
A:R^{6188}\longrightarrow V=R^{4367},\qquad
L=\operatorname{im}A,\qquad
N=V\cap\operatorname{im}_{\mathbb Q(s)}A,\qquad C=N/L.
$$
原九个目标及其两个已用乘子为
$$
t_j=\left(\sum_{a=0}^{j}\binom ja(-s)^{j-a}m_a\right)^2,
\quad 2\le j\le10,
$$
$$
h_*=s^3F_+^2F_-^2E_8,\qquad h_0=xh_*.
$$
设
$$
M=\sum_{j=2}^{10}R[t_j]\subset C,\qquad
b_j=[h_*t_j],\qquad B=\sum_{j=2}^{10}Rb_j=h_*M.
$$
这里 $M$ 是原九个类生成的整个 $D[s]$ 模；没有先选择或截断其来源。

本附录证明
$$
\boxed{\operatorname{Ann}_R(pB)
=\operatorname{Ann}_R(pb_j)
=(p^4,\ px,\ x^2)\quad\text{对每个 }j.}
\tag{1.1}
$$
由此得到原目标的完整理想
$$
\boxed{\operatorname{Ann}_R(pM)
=\operatorname{Ann}_R\bigl(R\,p[t_j]\bigr)
=h_*\,(p^4,\ p(s-2),\ (s-2)^2)
\quad\text{对每个 }j.}
\tag{1.2}
$$
乘子 $h_*$ 的首系数是 $3125\in D^\times$，所以这里也可统一写成其首一化 $m_*=\operatorname{mon}(h_*)$。

特别地，这给出新的原来源正结论
$$
p(s-2)^2h_*t_j\in L\quad(2\le j\le10).
\tag{1.3}
$$
这些来源仍可取原加权费用不超过 8515，具体降度理由见第 8 节。

未乘 $p$ 的 $\operatorname{Ann}_R(M)$ 尚未由 (1.2) 确定。第 9 节把它严格缩成完整系数 socle 上的有限问题；不删去可能隐藏的根 1 分量。

## 2. 完整系数载体与真实来源坐标

令
$$
T=C[p^\infty].
$$
$T$ 是完整系数素数扭子，不是有理参数局部扭子，也不是选定来源子模。[完整指数六定理](R150-appendix-complete-coefficient31-exponent-six-and-exact-original-p2h0-sources.md)，第 1--4 节，已证明
$$
C\cong_D D^{298}\oplus T,
$$
$$
T\cong_D
(D/p)^2\oplus(D/p^2)^5\oplus(D/p^3)^2
\oplus(D/p^4)^4\oplus(D/p^5)^2\oplus D/p^6.
\tag{2.1}
$$
其真实原除源基 $g_1,\ldots,g_{16}$ 的指数依次为
$$
(e_i)=(1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6).
\tag{2.2}
$$
这些来源在完整模 $p$ 商中独立，给出十六个有相应阶上界的循环生成元。它们的总长度是 50，与 (2.1) 相等，因此由这些真实来源定义的直和到 $T$ 的满射是同构。下面的幂层和 socle 比较使用这套同一真实来源坐标，不能以任意有限域代表代替。

[原 $h_*$ 精确五分母定理](R150-appendix-original-nine-hstar-targets-exact-five31-denominator.md)和[原 $h_0$ 精确二分母定理](R150-appendix-original-nine-h0-targets-exact-two31-denominator-and-complete-socle.md)已分别证明
$$
\operatorname{ord}_p(b_j)=5,\qquad
\operatorname{ord}_p(xb_j)=2
\quad\text{对全部九个 }j.
\tag{2.3}
$$
这里 $\operatorname{ord}_p(c)=a$ 表示 $p^ac=0$ 且 $p^{a-1}c\ne0$。原有理成员性保证 $B\subset T$。由 (2.3) 对整个参数生成模都有
$$
p^5B=0,\qquad xp^2B=0.
\tag{2.4}
$$

完整 $T$ 在模 $p$ 下只有根 1、根 2 两个参数主分量。根 1 分量的系数指数恰为 1、2；根 2 分量的系数指数重数是 $(1,4,2,4,2,1)$。特别是
$$
p^2T_1=0.
\tag{2.5}
$$
这允许把真实二点完成中的高幂层等式识别到完整 $T$，却不允许直接声称 $B\subset T_2$。

## 3. 已付整数 carry 及本次实际小审计

精确五分母定理第 3--5 节保留了原来源恒等式
$$
p^2b_j=p^3r_j
\tag{3.1}
$$
于真实根 2 完成分量中。$r_j$ 的原余类经过完整 104 个局部自由条件、505 个全局自由条件及全部 315 坐标恢复；其保真精度来自已付 $25\to20$ 原单位求解和原整数乘回。

将 $r_j$ 在根 1 分量上定义为零。由 (2.5)，(3.1) 两边在根 1 分量都为零，故它成为完整系数扭子 $T$ 中的恒等式。这里使用有限系数扭子的忠实完成与 Hensel 主分量分解。没有把有限 Taylor 多项式本身声称为全参数来源。

记
$$
\mathcal R=\sum_jRr_j.
$$
于是
$$
p^2B=p^3\mathcal R,\qquad p^3B=p^4\mathcal R.
\tag{3.2}
$$

本次只读审计重新读取既有全 210 列结果、真实前 13/15/16 来源、九个第一 carry 和完整七维 socle 结果。所有原文件的完整字节 SHA、父 binding、来源与目标标签先逐项匹配，再在同一真实基中检查：

| 实际核验 | 结果 |
|---|---:|
| 真实来源基 $U_{16}$ 的秩 | 16 |
| 原参数作用乘回 $U_{16}J_{16}=J_{315}U_{16}$ | 全部 5040 项相等 |
| 九个 carry 乘回 $U_{16}X_1=[r_j]\bmod p$ | 全部 2835 项相等 |
| 指数至少 4 的七个坐标上的 carry 秩 | 4 |
| 指数至少 5 的三个坐标上的 carry 秩 | 3 |
| 上述两个投影像的原参数作用 | 均为标量 2 |
| 七维原 $p[h_0t_j]$ 矩阵的前四行 | 全零 |
| 该七维矩阵的秩 | 1 |
| $p^4b_j$ 的 socle 像秩 | 1 |
| 两个 socle 像合并的秩 | 2 |
| 每一个 $j$ 的两条 socle 向量 | 各自非零且彼此独立 |

这些是既有真实整数来源的坐标审计；没有重新执行整数 carry、原单位求解或完整来源消元。$J_{16}$ 是 $T/pT$ 的参数作用，不被冒用成尚未恢复的完整 socle 作用。

## 4. 原目标的高系数层

先看
$$
p^4T/p^5T.
$$
它的维数为三，三个坐标正对应 (2.2) 中的两个指数五方向和一个指数六方向。由 (3.1)，九个 $p^3b_j=p^4r_j$ 在此商中的像，正是第 3 节实际秩三的坐标投影。因此它们模 $p(p^4T)=p^5T$ 张满 $p^4T$。

它们属于 $p^3B\subseteq p^4T$。对有限 $D$ 模 $p^4T/p^3B$ 使用 Nakayama，引出
$$
\boxed{p^3B=p^4T.}
\tag{4.1}
$$
所以该模的 $D$ 初等指数恰为 $(1,1,2)$。

又由 (3.2)
$$
p^4T=p^3B\subset p^2B\subset p^3T.
$$
在商 $p^3T/p^4T$ 中，九个生成元的像就是第 3 节指数至少四的七坐标投影。其实际秩为四，原 $s$ 作用为标量二，故它已经包含全部参数倍所能生成的像。得到
$$
\dim_{\mathbb F_{31}}\bigl(p^2B/p^3B\bigr)=4.
\tag{4.2}
$$

由 (4.1)，$B$ 中指数至少四的系数循环因子恰为 $4,4,5$。由 (4.2)，指数至少三的因子共有四个，故
$$
\boxed{\text{$B$ 的所有系数指数 $\ge3$ 恰为 }3,4,4,5.}
\tag{4.3}
$$
其余因子若有，只能是指数一或二。这不是对整个 $B$ 的未计算完整直和分解。

## 5. 每个目标的两条独立 socle 线

令
$$
v_j=pxb_j=p[h_0t_j],\qquad
w_j=p^4b_j.
$$
由精确二分母定理第 3--5 节，$v_j$ 的真实完整 socle 坐标采用基
$$
p^3g_{10},p^3g_{11},p^3g_{12},p^3g_{13},
\quad p^4g_{14},p^4g_{15},p^5g_{16}.
\tag{5.1}
$$
实际前四行全零，后三行成比例，且其中指数五方向上的同一个坐标对全部九个目标都非零。因此
$$
v_j\in p^4T,\qquad v_j\ne0.
\tag{5.2}
$$
另一方面，把 (3.1) 乘以 $p^2$ 得
$$
w_j=p^5r_j.
$$
所有指数至多五的来源在此幂层消失；精确五分母定理实际读到的第十六坐标对每个目标非零。因此 $w_j$ 是 $p^5g_{16}$ 的非零倍。

所以对每个 $j$，$v_j,w_j$ 都是非零 $p$-socle 元，并且
$$
\boxed{v_j,\ w_j\text{ 在完整 }T[p]\text{ 中独立。}}
\tag{5.3}
$$
第 3 节的只读审计再次逐九列核验这一独立性。不能把这两条线合为一条：$v_j$ 具有非零指数五 socle 分量，而 $w_j$ 仅有指数六 socle 分量。

现在取 $a,c\in D$。若
$$
(a+cx)b_j=0,
$$
乘以 $p^2$ 并用 $xp^2b_j=0$。由于 $p^2b_j$ 的阶恰为 $p^3$，必有 $a=p^3d$。再将原等式乘以 $p$，得到
$$
d\,w_j+c\,v_j=0.
$$
由 (5.3)，$d,c$ 都被 $p$ 整除。写 $d=pd_1,c=pc_1$，回到未再乘 $p$ 的原等式，得到
$$
d_1w_j+c_1v_j=0.
$$
再次由 (5.3)，$d_1,c_1\in pD$。反向由 (2.4) 显然成立。故
$$
\boxed{
\operatorname{Ann}_R(b_j)\cap D[x]_{\le1}
=p^5D+p^2Dx.
}
\tag{5.4}
$$
逐列式 (5.4) 也给共同模 $B$ 的同一等式。它排除了所有可能的常数项与一次参数项混合抵消，不是只分别测试两个单项式。

## 6. 完整的 $\operatorname{Ann}(pB)$

由 (5.2) 和 (4.1)，
$$
pxB\subset p^4T=p^3B.
$$
因此
$$
px^2B=x(pxB)\subset xp^3B=p(xp^2B)=0.
\tag{6.1}
$$
对于任意 $f\in D[x]$，用首一多项式 $x^2$ 除法，唯一写成
$$
f=q x^2+a+cx,\qquad a,c\in D.
$$
由 (6.1)，$f$ 杀死 $pB$，当且仅当 $p(a+cx)$ 杀死 $B$。利用 (5.4)，这又当且仅当
$$
pa\in p^5D,\qquad pc\in p^2D,
$$
亦即 $a\in p^4D,c\in pD$。这证明 (1.1)。同一论证逐个 $j$ 成立。

还可直接读得
$$
\operatorname{Ann}_R(p^2B)=(p^3,x),\qquad
\operatorname{Ann}_R(p^3B)=(p^2,x),\qquad
\operatorname{Ann}_R(p^4B)=(p,x).
\tag{6.2}
$$
这些理想逐个 $p^ab_j$ 也相同，因为每个目标的精确系数阶都是五。

特别地，每个单独的循环模满足
$$
R\,pb_j\simeq R/(p^4,px,x^2)
\simeq_D D/p^4\oplus D/p.
\tag{6.3}
$$
最后一个同构只陈述 $D$ 模结构，不是整个共同 $pB$ 的结构。

## 7. 回到全部原目标的完整湮灭理想

[完整有理相对模定理](R150-appendix-zero-relative-target-partition-three-one-one-and-global-invariant-factors.md)，第 1--2、6--7 节，证明每个 $[t_j]$ 以及共同有理目标模的湮灭理想都是
$$
(m_*),\qquad m_*=\operatorname{mon}(h_*),\quad\deg m_*=23.
$$
如果 $f\in R$ 杀死 $M$ 或 $pM$，则有理化后 $m_*\mid f$ 于 $\mathbb Q[s]$。因为 $m_*\in D[s]$ 首一，可在 $D[s]$ 中写
$$
f=m_*q+r,\qquad \deg r<23.
$$
有理化后的余式为零，而 $D[s]$ 无系数扭子，故 $r=0$。于是
$$
\operatorname{Ann}_R(M)=h_*\operatorname{Ann}_R(B),
\qquad
\operatorname{Ann}_R(pM)=h_*\operatorname{Ann}_R(pB).
\tag{7.1}
$$
同一长除法逐个原目标成立。结合 (1.1)，得到完整结论 (1.2)。

例如，对任意 $f\in D[s]$，要使所有九个 $pft_j$ 有原 $D[s]$ 来源，必要且充分的是：先有 $m_*\mid f$；然后 $f/m_*$ 除以 $x^2$ 的常数余项被 $p^4$ 整除、一次余项被 $p$ 整除。任一个固定原目标给同一个判准。

作为单个目标的进一步结构推论，
$$
R\,p[t_j]\simeq R/\bigl(m_*(p^4,px,x^2)\bigr).
$$
短正合列
$$
0\longrightarrow R/(p^4,px,x^2)
\xrightarrow{\;\cdot m_*\;}
R/\bigl(m_*(p^4,px,x^2)\bigr)
\longrightarrow R/(m_*)\longrightarrow0
$$
在 $D$ 模层面分裂，因为 $R/(m_*)$ 为秩 23 的有限自由 $D$ 模。因此
$$
R\,p[t_j]\cong_D D^{23}\oplus D/p^4\oplus D/p.
\tag{7.2}
$$
该 $D$ 分裂不必与参数 $s$ 作用相容；也不将九个目标的共同模声称为这个单个循环模。

## 8. 新正来源的原费用

(1.3) 是完整模中的成员性，因此先给出某个真实原 $D[s]$ 来源。再对该已存在的来源使用[原统一降度定理](R150-appendix-complete-coefficient31-exponent-six-and-exact-original-p2h0-sources.md)，第 6 节。

保持实际原最大子式 $D_*=\det B_*$，不重新标量首一化。已付参数为
$$
H_*=8835,\quad \deg D_*=8769,\quad
\operatorname{lc}(D_*)\in D^\times,\quad
\deg\Delta_{\rm aff}=298.
$$
$\Delta_{\rm aff}$ 可首一化，且
$$
\deg(D_*/\Delta_{\rm aff})=8471.
$$
对任何已存在原来源，三支费用仍为
$$
8471-1+45=8515,\qquad
8835+55-66-298-11=8515,\qquad
\tau(\text{目标})+1.
$$
原 $h_*t_j$ 有 $\tau\le63$，乘 $x^2$ 仅增加至多二，乘系数标量 $p$ 不增加参数次数。因此新目标的第三支至多 66，最终
$$
\boxed{\operatorname{cost}\bigl(p(s-2)^2h_*t_j\text{ 的原来源}\bigr)\le8515.}
$$
这里没有把抽象存在自动识别成已付费用，也没有展开九个高次数全局来源或给出其系数高度。

## 9. 未乘 $p$ 的最后问题：完整十六维 socle

令
$$
I=\operatorname{Ann}_R(B),\qquad
J=(p^4,px,x^2)=\operatorname{Ann}_R(pB).
$$
则
$$
pJ\subseteq I\subseteq J.
$$
对 $f\in J$，每个 $fb_j$ 都被 $p$ 杀死。因此有精确描述
$$
\boxed{
I/pJ=
\ker\left(
J/pJ\longrightarrow T[p]^9,\quad
f\longmapsto(fb_2,\ldots,fb_{10})
\right).
}
\tag{9.1}
$$
这里的靶必须是完整 $T[p]$；只有此前七个根 2 高阶 socle 方向不足以自动判定 (9.1)。

作为 $k[x]$ 模，$k=\mathbb F_{31}$，
$$
J/pJ\simeq k[x]/(x)\oplus k[x]/(x)\oplus k[x],
\tag{9.2}
$$
三个生成元分别由 $p^4,px,x^2$ 表示。前两个生成元的像，就是第 5 节已经确定的两条独立 socle 线。故真正未付的输入是九个 $x^2b_j$ 在完整十六维 socle 中的坐标及其真实参数作用。

还可给这个后继一个严格有限界。对有限 $p$-幂扭子 $T$，乘 $p$ 的核与余核在有限 $k[s]$ 模的 Grothendieck 群中相同，故
$$
\chi_{T[p]}(s)=\chi_{T/pT}(s)=(s-1)^2(s-2)^{14}.
$$
用 $x=s-2$ 写成
$$
\chi(x)=(x+1)^2x^{14}.
$$
Cayley--Hamilton 说明 $\chi$ 杀死完整 $T[p]$。由 $x^2B\subset T[p]$，
$$
\chi(x)x^2B=0.
\tag{9.3}
$$
于是 (9.1) 可进一步通过
$$
k^2\oplus k[x]/(\chi)
$$
这个维数十八的空间决定：两个已经知道的生成元，加上九个 $x^2b_j$ 的至多十六次共同参数作用。这里的“十八”是共同乘子系数的参数维数，不是新声称的目标像秩。

(9.3) 也给一个保守的未乘 $p$ 参数湮灭子
$$
(s-1)^2(s-2)^{16}B=0.
$$
本附录不声称它最小，不声称 $x^2B=0$，也不把 $T/pT$ 的某个坐标作用矩阵直接当成 $T[p]$ 的作用矩阵。剩余问题因此已缩为有限 socle 判别，原全 210 来源链无需为本定理重算。

## 10. 冻结来源与实际只读执行

[尾层审计源码](../notes/2026-11-16-r150-original-hstar-annihilator-tail-audit-789f.py)为 9020 字节，SHA256：
daaf20b42f05718f5ffbcc570963e00fe46eed2f10216291c4f44f514ef7d1ab。

它使用原完整 315 状态 reader，5002 字节，SHA256：
8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2。

实际本地审计于 2026-11-16 06:55 UTC 完成，退出码 0，耗时 0.339595433 秒，峰值常驻内存 52564 KiB。临时结果文件 3225 字节，SHA256：
71959c05e881c578dfb01578cb995d2f7a422c16aed7e41ab66afc3cfa395a9d。

本次绑定为：
e0c921f51077e07288410fc7c2bdc63adb0a3b27127f4f18cdc61fd1ac6af4f1。

三个实际父绑定分别为：

- 完整 210 来源：712f9b426017d3f63c05e755a314e14d79ac03d22bce6a4b3f943efcd80d7093；
- 原 $h_*$ 第一 carry：4044954d51c3d23ced04aa55ae8355c6877c2153f92984807c6454572e85e4cd；
- 原 $h_0$ 七维 socle：dce92fb5bbd50efc3cf5bd39a5b7fbf27dec7f88e4c3e0b9308cfff47b042b98。

[完成执行身份](../notes/2026-11-16-r150-original-hstar-annihilator-tail-local-execution-789f.json)只保存源码、输入身份、参数、实际执行及输出哈希。完整坐标、作用矩阵和计算输出留在临时工作区。本附录没有把这一秩一原来源模的算术结论推广成普通不变子空间问题的结论。
