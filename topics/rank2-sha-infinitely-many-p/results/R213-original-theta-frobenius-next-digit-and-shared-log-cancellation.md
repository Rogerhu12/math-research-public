# R213 — 原首行的 Frobenius 下一位与同一 log 校正的整消去

日期：2026-11-12。**状态：原首行模 $p^2$、第二行负层的准确比较和首行失败后的整行消去已证明。没有证明原后继子式非零，更没有证明无穷素数结论。**

本篇接续 [R211](R211-actual-theta-connection-fixed-and-remaining-log.md)，回答其中实际 $\log h$ 强迫与被除一次 $p$ 的原第一行之间的关系。二者确实含有**同一个**对数校正；它可在第二行的一个整操作中消去，但仍保留在原第一行的下一位。

## 1. 保留原两列和特征零级数

令 $p=4r-1\ge7$ 为素数，$O=\mathbf Z_p$。沿用 R197/R208 的
$$
s=u^4,\qquad z=uF(s),\qquad w=z^4=W(s)=sF(s)^4,
$$
其中
$$
F(s)=\sum_{j\ge0}\frac{\binom{2j}{j}}{4^j(4j+1)}s^j,\qquad
G(s)=\frac1{\sqrt{1-s}}=F(s)+4sF'(s).
\tag{1}
$$
写
$$
L(s)=\log\vartheta(z(s))^{68},\qquad
\mathbf A(s)=e^{L(s)}(P(s),Q(s)).
\tag{2}
$$
$P,Q$ 始终是 R197 的原次数十六多项式，均从 $s$ 开始；不换成任意 theta 截面。令
$$
c=68k_r=[w^r]L(s(w)),\qquad
\ell_r=[s^r]L(s),\qquad
a=\overline{pc}=68\kappa\in\mathbf F_p.
\tag{3}
$$
因为这里 $p\equiv3\pmod4$，$p\ne17$，故 $a$ 为单位；下面的等式本身不以该单位性作输入。

由 R197，$c\in p^{-1}O$，原整 gauge
$$
\widehat{\mathbf A}(s)
=e^{-cW(s)^r}\mathbf A(s)\pmod{s^{2r+1}}
\tag{4}
$$
在所用全部正次系数中是整的，且从 $s$ 开始。原两权行为
$$
\mathbf R_1=[w^r]\mathbf A(s(w)),\qquad
\mathbf R_2^{\rm raw}=[w^{2r}]\mathbf A(s(w)),\qquad
\widehat{\mathbf R}_2=\mathbf R_2^{\rm raw}-c\mathbf R_1\in O^2.
\tag{5}
$$
这里 $\mathbf R_1=\widehat{\mathbf R}_1\in O^2$。

注意两个初等整性事实。首先，$F,G$ 到所需次数的系数在 $O$；$L$ 在次数小于 $r$ 的系数也在 $O$。其次，$s(w)$ 首项为 $w$，其到次数 $r$ 的系数整。因此将 $L$ 复合到 $s(w)$ 后，次数 $r$ 的唯一可能非整贡献是 $\ell_r$ 本身，从而
$$
c-\ell_r\in O,\qquad \overline{p\ell_r}=a.
\tag{6}
$$

以下两个向量是**同一固定特征零级数**的系数，而不是自由选择的新行：
$$
\begin{aligned}
\boldsymbol\alpha(s)&=\frac{\mathbf A(s)G(s)}{F(s)^2},&
\mathbf T_1&=[s^r]\boldsymbol\alpha(s)\in O^2,\\
\boldsymbol\beta(s)&=\frac{\mathbf A(s)G(s)}{F(s)^3},&
\mathbf T_2&=[s^{2r}]\boldsymbol\beta(s)\in p^{-1}O^2.
\end{aligned}
\tag{7}
$$
因为 $P,Q$ 从一次开始，$\mathbf T_1$ 不读 $L$ 的第一个坏系数。在第二权内，(4) 的展开
$$
\mathbf A=\widehat{\mathbf A}
   +cW^r\widehat{\mathbf A}\pmod{s^{2r+1}}
\tag{8}
$$
已经完整：指数平方项从 $s^{2r}$ 开始，再乘 $\widehat{\mathbf A}\in sO[[s]]$ 后超出窗口。这证明 (7) 中至多只有一层 $p^{-1}$，并准确标明它来自哪里。

## 2. 原第一行模 p²：实际 log h 就是 Frobenius 校正

Lagrange 公式及 (1) 给出特征零等式
$$
\mathbf R_1
=[s^r]\frac{\mathbf A(s)G(s)}{F(s)^{p+2}}
=[s^r]\boldsymbol\alpha(s)F(s)^{-p}.
\tag{9}
$$
在所读次数小于 $p$ 的范围，$F(0)=1$，$\log F$ 整，而且
$$
F^{-p}=\exp(-p\log F)\equiv1-p\log F\pmod{p^2}.
\tag{10}
$$
定义
$$
\mathbf l=
\overline{[s^r]\boldsymbol\alpha(s)\log F(s)}
\in\mathbf F_p^2.
\tag{11}
$$
则
$$
\boxed{\quad
\mathbf R_1\equiv\mathbf T_1-p\mathbf l\pmod{p^2}.
\quad}
\tag{12}
$$
式中的 $p\mathbf l$ 指任意整提升再乘 $p$，故模 $p^2$ 无歧义。

这正是 R211 的原配对，没有换一个近似对数。令 $h=\bar F$ 为 R211 的二项式多项式。在 (11) 所读窗口，
$$
\overline{\mathbf A}=\Gamma(P,Q),\qquad
\bar G=(1-s)^{(p-1)/2},\qquad
\overline{\log F}=\log h.
$$
所以
$$
\mathbf l
=[s^r]\Gamma(s)(P(s),Q(s))
  \frac{(1-s)^{(p-1)/2}}{h(s)^2}\log h(s)
=\mathbf L_{\rm fix}+\mathbf L_{\rm rem}.
\tag{13}
$$
前式只使用 $\mathbf A$ 的低整系数；不对整个非整原 $\mathbf A$ 作约化。

特别，原首行失败 $\mathbf R_1\in pO^2$ 等价于 $\mathbf T_1\in pO^2$。这时才定义
$$
\mathbf u=\overline{\mathbf R_1/p},\qquad
\mathbf v=\overline{\mathbf T_1/p},
$$
并有实际的下一位等式
$$
\boxed{\quad \mathbf u=\mathbf v-\mathbf l.\quad}
\tag{14}
$$
因此只用 $\mathbf T_1/p$ 代替原除 $p$ 行，会漏掉 (13) 的整个同一对数项。

## 3. 第二行的唯一负层及其正确约化

第二权的准确 Lagrange 核为
$$
\mathbf R_2^{\rm raw}
=[s^{2r}]\frac{\mathbf A(s)G(s)}{F(s)^{2p+3}}
=[s^{2r}]\boldsymbol\beta(s)F(s)^{-2p}.
\tag{15}
$$
在 $\boldsymbol\beta$ 的系数具有下界 $-1$ 的前提下，
$$
F^{-2p}=1-2p\log F+p^2(\text{整级数})
$$
给出
$$
\mathbf R_2^{\rm raw}-\mathbf T_2
=-2p[s^{2r}]\boldsymbol\beta\log F+pO^2.
\tag{16}
$$
特别左端是整向量；可以约化的是该**差**，而不是未经证明整的 $\mathbf R_2^{\rm raw}$ 或 $\mathbf T_2$。

准确读取负层时，由 (8)
$$
p\boldsymbol\beta
\equiv aW^r\frac{\widehat{\mathbf A}G}{F^3}\pmod p.
$$
在相关有限窗，$W^r=s^rF^{p+1}\equiv s^rh$。乘 $\log F$ 并取 $s^{2r}$ 系数后，$s^r$ 将读数降至第一个权：
$$
\overline{p[s^{2r}]\boldsymbol\beta\log F}
=a[s^r]\Gamma(P,Q)\frac{(1-s)^{(p-1)/2}}{h^2}\log h
=a\mathbf l.
\tag{17}
$$
因此
$$
\boxed{\quad
\overline{\mathbf R_2^{\rm raw}-\mathbf T_2}
=-2a\mathbf l.
\quad}
\tag{18}
$$
同一计算不乘 $\log F$ 时给
$$
\overline{p\mathbf T_2}=a\,\overline{\mathbf T_1}.
\tag{19}
$$
于是 $\mathbf T_2-c\mathbf T_1\in O^2$ **无条件成立**；若原首行失败，则 $\mathbf T_2\in O^2$，这一步先支付了后面单独约化 $\mathbf T_2$ 所需的整性。

由 (12)、(18)，对上述整向量得到
$$
\boxed{\quad
\overline{\mathbf T_2-c\mathbf T_1}
=\overline{\widehat{\mathbf R}_2}+a\mathbf l.
\quad}
\tag{20}
$$
与 R211 的
$$
\overline{\widehat{\mathbf R}_2}
=\mathbf R_2^\circ+4C_p\overline{\mathbf R_1}-a\mathbf l
$$
比较，还得到准确关系
$$
\overline{\mathbf T_2-c\mathbf T_1}
=\mathbf R_2^\circ+4C_p\overline{\mathbf R_1}.
\tag{21}
$$
因此 (7) 没有制造一个独立的第二条件：它就是 R211 多项式连接行的整提升，保留同一个共同 gauge 方向。

## 4. 首行失败后的整消去及一条短表达

现在假设 $\mathbf R_1\in pO^2$。定义共同后继行
$$
\mathbf K=\overline{\widehat{\mathbf R}_2}-a\mathbf u.
\tag{22}
$$
这是对原后继矩阵 $(\mathbf u,\overline{\widehat{\mathbf R}_2})$ 的同一个整行操作，所以
$$
\det(\mathbf u,\overline{\widehat{\mathbf R}_2})
=\det(\mathbf u,\mathbf K).
\tag{23}
$$
由 (14)、(20) 或直接由 (12)、(18)，准确有
$$
\boxed{\quad
\mathbf K
=\overline{\mathbf T_2-2c\mathbf T_1}
=\overline{\mathbf T_2-2\ell_r\mathbf T_1}
=\mathbf R_2^\circ-a\mathbf v.
\quad}
\tag{24}
$$
第一项中的 $\mathbf T_2$、$c\mathbf T_1$ 在本假设下均已证明整；第二项使用 (6) 和 $\mathbf T_1\in pO^2$。同一 $\log h$ 校正在这个第二行中完全消去，未被重复计两次。

也可以先在特征零记录一个无条件的精度式：
$$
\mathbf R_2^{\rm raw}-2c\mathbf R_1
-\mathbf T_2+2c\mathbf T_1\in pO^2.
\tag{25}
$$
它是四项组合的整精度声明；在没有首行失败时，不能据此将每一项各自约化到 $\mathbf F_p$。

式 (24) 的中间项还可写成同一固定连接的一条系数：
$$
\boxed{\quad
\mathbf K=
\overline{
[s^{2r}]
e^{\,L(s)-2\ell_rs^rF(s)}
(P(s),Q(s))\,\frac{G(s)}{F(s)^3}
}.
\quad}
\tag{26}
$$
这里的整体系数由 (24) 已证明整。证明只需展开修正指数：二次项从 $s^{2r}$ 开始，而 $(P,Q)$ 从 $s$ 开始，故该权完全不见它；一次项恰为 $-2\ell_r\mathbf T_1$。

还有一个准确的局部留数解释。令
$$
t=u(z)^p z=s^rF(s).
$$
从 $ds=4u^3G^{-1}dz$ 及留数在四次分歧参数下的关系，直接得到
$$
\mathbf T_n
=\operatorname{Res}_{z=0}
  \frac{\mathbf A(s(z))}{z\,t^n}\,dz,
\qquad n=1,2.
\tag{27}
$$
所以 (26) 是同一混合参数 $t$ 下乘 $e^{-2\ell_rt}$ 后的第二个留数。$t$ 仍含原椭圆对数 $z$；(27) 没有把它冒称 R207 的裸有理参数或一个新的独立非零行。

## 5. 保留的真实剩余项及 R207 比较的边界

(24) 使第二行不再显式含 $\log h$，但第一行仍是 (14)。故真实目标是
$$
\boxed{\quad
\det(\mathbf u,\mathbf K)
=
\det(\mathbf v-\mathbf L_{\rm fix},\mathbf K)
-\det(\mathbf L_{\rm rem},\mathbf K).
\quad}
\tag{28}
$$
消去第二行的共同对数强迫不等于消掉整个目标中的剩余因子。若要证明该剩余项消失，需要一条针对同一实际 $\mathbf K$ 的新等式；R211 的原 $\widehat{\mathbf R}_1$ 配对不能无条件替代它。

R207 的 $\kappa\cdot2261/81920$ 是原裸有理 $b$ 的完整迹。式 (26) 仍含原 $e^L$、原 $P,Q$、原 $\ell_r$ 及原参数核，(28) 仍保留原除 $p$ 行。当前没有给出把这个裸迹单位映到 (28) 的整比较，也没有从它推导 (28) 非零。

### 5.1. 完整中央双零其实强迫整个 K 行为零

对 R203 的范围 $p\ne11$，还有比 (23) 的子式更强的实际测试。
令 $b=17u_0$ 为 R199/R203 的**原**共同 Cartan 指数；这里不把它与
R207 的有理函数 $b$ 混同。R197 §5.1 已证明 $c-b\in O$。
R203 (19) 对原两列的行列式一变换给出同一个有限目标格：
$$
\mathbf t_1=\frac{\mathbf R_1}{p},\qquad
\mathbf t_2=\frac{\mathbf R_2^{\rm raw}-2b\mathbf R_1}{2p}.
\tag{29}
$$
两个原完整中央导数均为零时，$\mathbf t_1,\mathbf t_2\in O^2$。
首行失败后，$2(c-b)\mathbf R_1\in pO^2$，故 (24) 准确给出
$$
\overline{\mathbf R_2^{\rm raw}-2b\mathbf R_1}
=\mathbf K.
$$
于是前两个有限整测试本身等价于
$$
\boxed{\quad
\mathbf t_1,\mathbf t_2\in O^2
\quad\Longleftrightarrow\quad
\mathbf T_1\in pO^2,\qquad
\mathbf T_2-2\ell_r\mathbf T_1\in pO^2.
\quad}
\tag{30}
$$
这只等价于两个有限测试，不声称它们等价于完整中央双零。
特别，完整中央双零强迫 $\mathbf K=0$，而不只是
$\det(\mathbf u,\mathbf K)=0$。因此，在原首行已经失败的前提下，
只要 (26) 的**任一原坐标**非零，就能排除两个完整导数同时为零。
这里检测的是 $2p\mathbf t_2$ 除去已知精度后的剩余值；
不能把 $\mathbf t_2$ 作为有理向量本身非零当作违反其整性的证据。

由于 (26) 不显式含 $\log h$，新的直接比较点可以取这个整个
$\mathbf K$ 行。其原 theta 连接仍完整存在；R207 裸迹单位到它的比较尚未证明。

## 6. 同一 p43 的真实除 p 校准

[精确脚本](../scripts/check-original-theta-frobenius-next-digit.py) 从原有理 $L,F,P,Q$ 生成所有系数，验证 (12)、(18)、(20)、(25)；[输出](../scripts/check-original-theta-frobenius-next-digit.json) 随脚本保存。这里只复用已有的 $p=43$。

原两列给
$$
a=19,\qquad
\mathbf R_1\bmod43^2=(899,1683),\qquad
\widehat{\mathbf R}_2\bmod43=(22,2),
$$
$$
\mathbf T_1\bmod43^2=(340,565),\qquad
(\mathbf T_2-c\mathbf T_1)\bmod43=(33,24),
$$
$$
\mathbf l=(30,17),\qquad
\mathbf L_{\rm fix}=(29,23),\qquad
\mathbf L_{\rm rem}=(1,37).
$$
例如 $(340,565)-43(30,17)\equiv(899,1683)\pmod{43^2}$，与 (12) 一致。

为实际校准一个可除 $p$ 的原列，作行列式为一的整列变换
$(A,B)\mapsto(A,B-20A)$。其第二列首项模 $43$ 为零，而原第一行向量仍非零。对这一个真实列有
$$
u=8,\quad v=27,\quad l=19=2+17,\quad
\overline{\widehat R_2}=35,\quad K=12.
$$
准确满足
$$
8=27-19,\qquad
12=35-19\cdot8\pmod{43}.
$$
其中固定对数项为 $2$，剩余项为 $17$；若在原除 $p$ 行中省掉剩余项，会把 $u=8$ 错算成 $25$。这只校准实际整提升，**不**声称两条原首行同时为零，亦不排除仅在该双零条件下成立的新比较。

## 7. 固定导数系数的同一接口

两条 $\mathbf T_n$ 也可只用固定导数级数写出。对 $n=1,2$，
由 (1) 和对 $\mathbf A/F^n$ 的逐项微分，有特征零准确等式
$$
\boxed{\quad
\mathbf T_n=
\frac4n[s^{nr-1}]\frac{\mathbf A'(s)}{F(s)^n}
-p[s^{nr}]\frac{\mathbf A(s)}{F(s)^n}.
\quad}
\tag{31}
$$
确实令 $M=[s^{nr}]\mathbf A/F^n$，则
$nrM=[s^{nr-1}]\mathbf A'/F^n-n[s^{nr-1}]\mathbf A F'/F^{n+1}$；
代回 $\mathbf T_n=M+4[s^{nr-1}]\mathbf A F'/F^{n+1}$，并用
$4r=p+1$，即得 (31)。

特别写
$$
\boldsymbol\Xi_r=[s^{r-1}]\frac{\mathbf A'}F,
\qquad
\mathbf C_1=[s^r]\frac{\mathbf A}F,
$$
则二者均整，$\mathbf T_1=4\boldsymbol\Xi_r-p\mathbf C_1$。
首行失败等价于 $\boldsymbol\Xi_r\in pO^2$，且
$$
\mathbf v=4\,\overline{\boldsymbol\Xi_r/p}-\overline{\mathbf C_1}.
\tag{32}
$$
这把 O3/R52 的固定导数接口保留到原下一位，不增加一个独立条件。
当 $n=2$ 时，(31) 各项在证明相应整性之前可能属于 $p^{-1}O^2$；
必须沿用 §3 的差与组合的整性处理，不能把它们各自无证约化。

## 8. 同一混合参数的实际整 theta 参考

令 $t=s^rF(s)$，仍只读次数 $<2r$。原级数可以作一次具体、
可核查的整参考修正：
$$
\widetilde\Gamma(s)
=\exp\bigl(L(s)-\ell_rt(s)\bigr)\pmod{s^{2r}}.
\tag{33}
$$
它整且 $[s^r]\log\widetilde\Gamma=0$。确实
$$
L-\ell_rt=(L-cW^r)+(c-\ell_r)t+c\,t(F^p-1).
$$
首项由原 gauge 整，第二项由 (6) 整，最后一项由
$F^p-1\in pO[[s]]$ 在此有限窗口内整；所有指数展开阶乘也小于 $p$。
零系数条件由 $[s^r]L=\ell_r$ 和 $[s^r]t=1$ 直接给出。

设 $d=\overline{c-\ell_r}$，并用 R211 的 $\mathcal V_p,C_p$。
同一窗口内的模 $p^2$ 展开 $F^p-1\equiv p\log F$ 给
$$
\overline{\widetilde\Gamma}
=\Gamma\,e^{dt}(1+a t\log h)
=\exp\bigl(\mathcal V_p+(4C_p+d)t\bigr)\pmod{s^{2r}}.
$$
第二个等号使用 R211 的真实 $\log h$ 强迫，两个校正准确抵消。
再比较刚才证明的 $s^r$ 零系数，得到无需保留未知共同标量的形式
$$
\boxed{\quad
\overline{\widetilde\Gamma}
=\exp\bigl(\mathcal V_p-[s^r]\mathcal V_p\cdot s^rh(s)\bigr)
\pmod{s^{2r}}.
\quad}
\tag{34}
$$
这里的 $t$ 在有限域窗口中是 $s^rh$。因而 (33) 的连接在这个
有限窗里由一个明确多项式给出，已没有显式 $\log h$ 项。

原两行与它的关系仍是准确的：
$$
\mathbf T_1=[s^r]\widetilde\Gamma(P,Q)G/F^2,
\qquad
\mathbf T_2-\ell_r\mathbf T_1
=[s^{2r}]\widetilde\Gamma(P,Q)G/F^3.
\tag{35}
$$
第一式不读从 $s^r$ 开始的参考修正；第二式展开同一指数的一次项即可。
右端均整。首行失败后，$\mathbf K$ 是第二式再减
$\ell_r\mathbf T_1$ 的约化，而不是把 (35) 的第二式本身当作 $\mathbf K$。

(33) 是从原 theta 明确构造的有限整参考，不是任意可更换的辅助函数。
但是 (34) 仍只是一份原点有限 jet：没有据此把 $t$ 宣称为全局有理参数，
也没有把该参考在 $h$ 的根处的多项式值等同于原 theta 的全局值。
R211 已指出完整连接多项式到次数 $p-1$ 的积分会遇到非单位分母；
本篇不无代价扩大这个窗口。

主问题仍是证明原完整中央失败必要条件在无穷多个素数处不成立。本篇使第一行下一位、第二行及其共同 $\log h$ 校正处于同一整公式中，未把该新的准确表示冒称非零定理。

