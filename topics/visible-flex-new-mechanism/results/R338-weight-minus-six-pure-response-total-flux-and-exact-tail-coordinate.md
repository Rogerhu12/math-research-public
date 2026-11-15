# R338：完整权负六响应纯核的总通量零门与准确尾坐标

日期：2026-11-15。**完整纸面证明；没有新原式编译、profile 求积、程序消元或科学运行。**

[R335](R335-complete-response-flux-identity-with-quadratic-tail-Green-correction.md) 已纠正一般响应的总通量公式：原二次左尾产生真实 Green 项，不能直接把正式 pure 投影前放 $1/5$，也不能在一般实输入上无条件使用 $16/5$。

本稿利用 [R144](R144-seventh-G-translation-and-230-query-control.md) 的完整权 $-6$ 响应空间与 [R207](R207-complete-weight-minus6-pure-image-equals-three-dimensional-response.md) 已发表的完整 pure 坐标，证明一个确实成立的限定结论：
$$
\boxed{
\int u'''V(u^2,0)=0
\quad\text{对所有 }V\in\mathcal R_{-6}\cap\ker\pi
\text{ 及所有实紧 }u.
}
\tag{1}
$$
证明保留全部 20 个原标签、原 16 条保留列和真 Green 尾。不是把 R335 的一般未解范围改称已付。

另给最低权响应 $\mathcal K$ 的全部代数 $\delta$ 后继的总通量零身份。这个后果不表示其完整 self 为零；尤其不与 $\mathcal Q(\delta\mathcal K)>0$ 混同。

## 1. 三个原空间与固定规范

对共同右 collar，仍用
$$
J(F)(x)=\int_x^{r_*}F(t)\,dt.
$$
令
$$
\Omega_u(V)=\int_\ell^{r_*}u'''V(u^2,0),\qquad
\mathcal L_u(V)=\int_\ell^{r_*}u'''\pi V(u).
\tag{2}
$$
$\pi$ 使用 R247/R254 以及 R207 原 canonical 相位 $-4$ 系数的规范：
$$
\pi\mathcal B_E(\tau)(u)
=\frac18\{D T_\tau(u)[\Phi_E(u,u)]-2\Phi_E(u,T_\tau(u))\}.
\tag{3}
$$
它等于 raw $\mathcal B_E(\tau)(0,u)$ 的 $1/16$。

$U$ 是原完整 canonical 成本空间，$\mathcal R\subset U$ 是完整真实响应空间；下标 $-6$ 是真正仿射权，不是 profile 中出现的某个幂标签。R144 已证明
$$
\dim\mathcal R_{-6}=16.
$$
R207 已进一步证明
$$
\pi U_{-6}=\pi\mathcal R_{-6}
=\operatorname{span}\{\rho_0,\rho_2,\rho_3\},
\qquad\dim\pi\mathcal R_{-6}=3.
\tag{4}
$$
本稿不重算这两个实际秩。

下文 $R_j$ 只表示 **R144 的原权 $-6$ 第 $j$ 列**。它不是 R126 的原权零列号，也不是 R316/R329 的 13 列 pure 核下标。R207 的三条基为
$$
\rho_0=\pi R_0,\qquad \rho_2=\pi R_2,\qquad \rho_3=\pi R_3.
\tag{5}
$$

## 2. 本次手算只需四条真实尾矩

沿 R335 写
$$
\mu=m(u,u),\quad q_E=\Phi_E(u,u),\quad
\nu_E=m(u,q_E),
$$
其中
$$
m(a,b)=
\left(\int a''b'',\ \int xa''b'',\
\int(x^2a''b''+2a'b')\right).
\tag{6}
$$
尤其
$$
\mu_0=\int(u'')^2,\qquad M_3=\int(u'')^3.
$$
所有积分都在原共同区间，右尾不设为零。

记
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ V=\Phi_{p_1},\
U_1=\Phi_{s_1},\ T_1=\Phi_{t_1}.
$$
这里 $V$ 出现在算子下标时是 $\Phi_{p_1}$；一般成本仍写 $V_{\rm cost}$ 或由上下文注明。置 $v=u',r=u'',s=u'''$，则
$$
\begin{aligned}
q_P'&=-r^2,&q_P''&=-2rs,\\
q_R'&=2vr+J(r^2)-xr^2,&q_R''&=2(v-xr)s,\\
q_S'&=-xr^2,&q_S''&=-r^2-2xrs.
\end{aligned}
$$
普通分部积分只用 $u$ 的平端 jets，给
$$
\boxed{
(\nu_P)_0=0,\quad
(\nu_P)_1=\frac23M_3,\quad
(\nu_R)_0=(\nu_S)_0=-\frac13M_3.
}
\tag{7}
$$
例如
$$
\int vrs=-\frac12\int r^3,\qquad
\int xr^2s=-\frac13\int r^3.
$$
式 (7) 没有预设第三尾或任一 $\nu_E$ 全零。

对二次尾 $p,q$，
$$
\mathcal G(p,q)=p''q-p'q'+pq''
=2p_2q_0-p_1q_1+2p_0q_2.
\tag{8}
$$
原尾表为
$$
\begin{array}{c|c}
E&p_E(\mu)\\ \hline
L&(\mu_2-x^2\mu_0)/4\\
V&-x^2\mu_1/4\\
p_2&-x^2\mu_2/4\\
P&\mu_0\\
R&x\mu_0\\
S&\mu_1\\
U_1&x\mu_1+\mu_2/2\\
T_1&x\mu_2
\end{array}
\tag{9}
$$
其他紧交叉输入只需把 $\mu$ 换成其真实 $m(a,b)$。

R335 已证明，对完整交换子 $C(A,B)$，
$$
\begin{aligned}
\mathfrak C_{E;A,B}(u)={}&
\mathcal G\!\left(p_E(\mu),p_A(\nu_B)-p_B(\nu_A)\right)\\
&-\mathcal G\!\left(p_A(\mu),p_B(\nu_E)\right)
+\mathcal G\!\left(p_B(\mu),p_A(\nu_E)\right),
\end{aligned}
\tag{10}
$$
以及全部响应的准确身份
$$
\boxed{5\Omega_u(V)-16\mathcal L_u(V)=4\mathfrak C_u(V).}
\tag{11}
$$
第三对角核 $Z$ 产生的响应在 (11) 三项均为零。

## 3. 原 20 标签的完整穷尽

原 E8 参数顺序是
$$
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1),
$$
真权是
$$
(-1,0,1,-3,-2,-2,-1,0).
$$
第三空间 retained 序列为 $0,\ldots,27,30,32,34,37,40,100,104,109$。前 28 个为按上述 E8 顺序枚举 $i<j$ 的完整交换子；后八真权依次是
$$
(-4,-3,-3,-2,-1,-2,-1,0).
$$
这些是 [原 scaling-block 源码](../scripts/literature_total_P1_scaling_blocks.py) 的已冻结定义。原 [G successor 编排](../scripts/literature_G_translation_successor.py) 按 E8 外循环、第三 retained 内循环，只保两权之和 $-6$，因此准确得到下表的 20 个标签。

用 $C_j$ 表示原第 $j$ 个第三交换子。需要的三个额外模板按 [R254](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md) 为
$$
\begin{aligned}
\tau_{30}&=(3C_2+C_{20})/256+\chi_{30},\\
\tau_{32}&=(C_3-3C_4-C_8)/128-C_{21}/512+\chi_{32},\\
\tau_{34}&=-(C_3+5C_4+3C_8)/128-3C_{21}/512+\chi_{34}.
\end{aligned}
\tag{12}
$$
全部 $\chi$ 均在 $Z$，故在 (10)–(11) 中贡献零。这里使用的是已发表的完整原差，不是只把第三对角值相等当成完整模板相等。

表中 $c_j$ 按恒等式
$$
\mathfrak C_u(R_j)=\frac{\mu_0M_3}{6}c_j
\tag{13}
$$
定义；**没有除以可能为零的 $\mu_0M_3$**。最后三列是正式 pure 坐标：
$$
\pi R_j=a_j\rho_0+b_j\rho_2+d_j\rho_3.
$$

| R144 原列 | 外二次算子 | 原第三模板 | $c_j$ | $a_j$ | $b_j$ | $d_j$ |
|---:|---|---|---:|---:|---:|---:|
| 0 | $L$ | $C_{18}=C(P,R)$ | $1$ | $1$ | $0$ | $0$ |
| 1 | $L$ | $C_{19}=C(P,S)$ | $3$ | $3$ | $0$ | $0$ |
| 2 | $P$ | $C_3=C(L,R)$ | $1$ | $0$ | $1$ | $0$ |
| 3 | $P$ | $C_4=C(L,S)$ | $3$ | $0$ | $0$ | $1$ |
| 4 | $P$ | $C_8=C(V,P)$ | $-4$ | $7/2$ | $0$ | $-5/2$ |
| 5 | $P$ | $C_{21}=C(P,T_1)$ | $0$ | $-10$ | $-8$ | $6$ |
| 6 | $P$ | $C_{23}=C(R,U_1)$ | $4$ | $-3$ | $-8$ | $5$ |
| 7 | $P$ | $C_{25}=C(S,U_1)$ | $0$ | $-6$ | $-3$ | $3$ |
| 8 | $P$ | $\tau_{32}$ | $-1/32$ | $-1/128$ | $3/128$ | $-1/64$ |
| 9 | $P$ | $\tau_{34}$ | $-1/32$ | $-3/128$ | $5/128$ | $-1/64$ |
| 10 | $R$ | $C_2=C(L,P)$ | $0$ | $-1$ | $1$ | $0$ |
| 11 | $R$ | $C_{20}=C(P,U_1)$ | $4$ | $0$ | $-5$ | $3$ |
| 12 | $R$ | $C_{22}=C(R,S)$ | $2$ | $-3/2$ | $-1$ | $3/2$ |
| 13 | $R$ | $\tau_{30}$ | $1/64$ | $-3/256$ | $-1/128$ | $3/256$ |
| 14 | $S$ | $C_2=C(L,P)$ | $0$ | $-3$ | $0$ | $1$ |
| 15 | $S$ | $C_{20}=C(P,U_1)$ | $0$ | $3$ | $6$ | $-3$ |
| 16 | $S$ | $C_{22}=C(R,S)$ | $0$ | $-3$ | $3$ | $0$ |
| 17 | $S$ | $\tau_{30}$ | $0$ | $-3/128$ | $3/128$ | $0$ |
| 18 | $U_1$ | $C_{18}=C(P,R)$ | $0$ | $3$ | $3$ | $-2$ |
| 19 | $U_1$ | $C_{19}=C(P,S)$ | $0$ | $9$ | $9$ | $-6$ |

### 3.1. 尾列如何由四条积分完整得到

(7)、(9)、(10) 已足够给表中全部尾数，不需要其他 cubic 积分的值。具体地，下列恒等覆盖非额外模板的每一项：
$$
\begin{array}{c|c}
(E;A,B)&\mathfrak C_{E;A,B}\\ \hline
(L;P,R)&\mu_0M_3/6\\
(L;P,S)&\mu_0M_3/2\\
(P;L,R)&\mu_0M_3/6\\
(P;L,S)&\mu_0M_3/2\\
(P;V,P)&-2\mu_0M_3/3\\
(P;P,T_1)&0\\
(P;R,U_1)&2\mu_0M_3/3\\
(P;S,U_1)&0\\
(R;L,P)&0\\
(R;P,U_1)&2\mu_0M_3/3\\
(R;R,S)&\mu_0M_3/3\\
(S;L,P),(S;P,U_1),(S;R,S)&0\\
(U_1;P,R),(U_1;P,S)&0.
\end{array}
\tag{14}
$$
例如 $(P;L,S)$ 的第一项是 $\mu_0M_3/6$，而
$$
\mathcal G(p_L(\mu),p_S(\nu_P))=-\mu_0M_3/3,\qquad
\mathcal G(p_S(\mu),p_L(\nu_P))=0,
$$
故准确为 $\mu_0M_3/2$。第二个数不是漏尾时得到的首项。

再如 $(P;V,P)$，
$$
p_V(\nu_P)=-x^2M_3/6
$$
给 (10) 首项 $-\mu_0M_3/3$，第三项又是 $-\mu_0M_3/3$，总和为 $-2\mu_0M_3/3$。

对 $(P;R,U_1)$，首项没有二次尾，第二项为
$$
-\mathcal G(x\mu_0,x(\nu_P)_1+(\nu_P)_2/2)
=\mu_0(\nu_P)_1=2\mu_0M_3/3.
$$
对 $(R;R,S)$，只有第一项贡献
$-\mu_0(\nu_S)_0=\mu_0M_3/3$。这些例子也展示了未列出的 $\nu$ 分量为何取消，而不是将其假设为零。

将 (12) 线性代入 (14)，余四行立即为
$$
\mathfrak C_P(\tau_{32})=\mathfrak C_P(\tau_{34})
=-\mu_0M_3/192,\quad
\mathfrak C_R(\tau_{30})=\mu_0M_3/384,\quad
\mathfrak C_S(\tau_{30})=0.
$$

### 3.2. 既有完整关系与 pure 表的来源分开

原 16 条保留列是
$$
0,1,2,3,4,5,6,7,8,9,11,12,13,15,16,17.
\tag{15}
$$
这些行的三条 pure 坐标逐项来自 R207 第 5 节的公开实际原函数关系。它们不是本稿重新作三点评价或只看幂尾所得。

四条未保留列还可直接由 R247 的完整三槽 Jacobi 身份写为
$$
\boxed{
R_{10}=R_2-R_0,\quad
R_{14}=R_3-R_1,\quad
R_{18}=R_{11}-R_6,\quad
R_{19}=R_{15}-R_7.
}
\tag{16}
$$
例如第一条是
$$
\mathcal B_R C(L,P)+\mathcal B_L C(P,R)
+\mathcal B_P C(R,L)=0.
$$
所以表中四个未保留行的 pure 坐标由已付 16 行和 (16) 得到。这里没有重跑 R144 的四条机器原差、独立 minor 或 20 个 mixed 根。

## 4. 真尾恰通过已付三维 pure 像因子化

由三条基的独立性，在 (4) 的实际空间上定义
$$
\boxed{
\ell_{\rm tail}(a\rho_0+b\rho_2+d\rho_3)=a+b+3d.
}
\tag{17}
$$
这是与正特征 $\lambda_+$ 不同的线性读出。

第 3 节表逐行有
$$
c_j=a_j+b_j+3d_j.
\tag{18}
$$
因此对全部 $V\in\mathcal R_{-6}$，
$$
\boxed{
\mathfrak C_u(V)
=\frac{\mu_0M_3}{6}\,\ell_{\rm tail}(\pi V).
}
\tag{19}
$$
这个结论保留了 R335 的非零尾：例如 $R_0$ 的 (19) 正是其明确反例中的 $\mu_0M_3/6$，没有把该反例撤回。

代回 R335，得到本稿的准确权 $-6$ 公式：
$$
\boxed{
\Omega_u(V)
=\frac{16}{5}\int u'''\pi V(u)
+\frac{2}{15}\mu_0M_3\,\ell_{\rm tail}(\pi V),
\qquad V\in\mathcal R_{-6}.
}
\tag{20}
$$
所以若 $\pi V=0$，右端两项同时为零，证明 (1)。

这是全 13 维原 pure 核的结论：
$$
\dim(\mathcal R_{-6}\cap\ker\pi)=16-3=13.
$$
不是只读 $\mathcal B(E,Z)$ 或一个方便的最低权串。13 是原实际秩的维数差，不是本稿新求的数。

## 5. 一个在全部 R 上真为零的限定成本读出

R207 的 (4) 也覆盖 $\pi U_{-6}$，故对 $V\in U_{-6}$ 可以合法定义
$$
\boxed{
\mathcal A_u(V)=
\Omega_u(V)-\frac{16}{5}\int u'''\pi V(u)
-\frac{2}{15}\mu_0M_3\,\ell_{\rm tail}(\pi V).
}
\tag{21}
$$
它对成本 $V$ 线性，对 $u$ 五次齐次，且
$$
\mathcal A_u(\mathcal R_{-6})=0.
\tag{22}
$$
令 $\Pi_{-6}$ 为原有限真权投影，则
$$
V\longmapsto\mathcal A_u(\Pi_{-6}V)
\tag{23}
$$
在整个 $\mathcal R$ 上为零。这使用原真缩放直和与响应权稳定，不把某个固定输入上的缩放当成新的任意几何变换。

(23) 是准确的响应 annihilator 接口，但尚未证明它在 $U$ 上非零。若它在 $U$ 上也恒零，就不是新障碍；若某个真实 $U$ 成本给非零，则必须再比较其物理 range 含义与全局控制。本文不在尚未读取该原成本之前选择其中一种结论。

对 pure-zero 的 $V\in U_{-6}$，(21) 简化为 $\mathcal A_u(V)=\Omega_u(V)$。但不能由此把 R333 的 whole universal self 支付或 R330 的两个内部通量支付，直接视为这个总通量已经支付。

## 6. 最低权 K 的整个有限导子串总通量都零

这一独立命题不依赖第 3 节的表。沿
[R330](R330-two-actual-packet-degenerate-fluxes-and-twenty-observation-control.md)，令
$$
\mathcal K=\mathcal B_P C(P,R),\qquad
\mathscr D=x^2D_x-2x,\qquad
\delta V=\mathscr D_{\rm out}V-\sum_{\rm in}V(\ldots,\mathscr D\,\cdot,\ldots).
\tag{24}
$$
这里 $\delta$ 是原代数导子；不将它解释为同一个实际几何的任意非仿射坐标改动。

原完整 self 输出是
$$
\mathcal K(u^2,0)
=-\frac13r^4-\frac23L_u\{P(u,u)\}.
\tag{25}
$$
由 [R181](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md) 的原通量身份，
$$
u'L_u(w)''
=\partial_x\{A_u(u'w''-u''w')\},\qquad
A_u=6u'u'''-2(u'')^2.
$$
$u$ 平端，但 $w$ 可有真实外尾。两次分部积分和上述两端零给
$$
\int u'''L_u(w)=\int u'L_u(w)''=0.
$$
另
$$
\int u'''r^4=\frac15\int(r^5)'=0.
$$
故
$$
\Omega_u(\mathcal K)=0
\quad\text{作为所有紧 }u\text{ 上的完整函数身份。}
\tag{26}
$$

对任意完整四次成本 $V$，紧 $u$ 给
$$
(\mathscr D u)'''=x^2u^{(4)}+4xu''',
$$
以及
$$
\int u'''\mathscr D\{V(u^2,0)\}
=-\int(\mathscr D u)'''V(u^2,0).
$$
把四个输入槽的真实变分一起保留，准确得到
$$
\boxed{\Omega_u(\delta V)=-D_u\{\Omega_u(V)\}[\mathscr D u].}
\tag{27}
$$
因此
$$
\boxed{\Omega_u(\delta^j\mathcal K)=0\qquad(j\ge0)}
\tag{28}
$$
对所有存在的原有限后继成立。即使某一后继在代数上已为零，(28) 仍只是同一身份，不增加新方向。

(28) 与 $\mathcal Q(\delta\mathcal K)=2\int r^2(u''')^2>0$ 不矛盾：总通量和左二次 self 坐标是不同读出。尤其不能因为 K 串的总通量为零，就让它在保 whole self 的新联合问题中自由改变内部退化通量。

## 7. 已完成与下一项原成本问题

本稿完成：

- 全部原 20 列的真 Green 尾，而非只保无尾主项；
- 同一个已付三维 pure 像的准确尾因子化；
- 完整权 $-6$ 的全部 pure-zero 响应总通量零；
- K 的整个代数后继串总通量零；
- 一个可直接对真实 $U_{-6}$ 原成本使用的线性读出 (21)。

还没有完成的是 (21) 在真实 $U_{-6}$ 的值。后续必须从完整 normal 族或真实 canonical 成本的 mixed/self **输出函数**读取；R207 的 pure 坐标、R316/R329 的左二次 self 数据都不能替代这一原输入。该检查不需要重跑已付三维 pure 像或 16 维响应秩，也不能先以预期的非零或零作为计算前提。