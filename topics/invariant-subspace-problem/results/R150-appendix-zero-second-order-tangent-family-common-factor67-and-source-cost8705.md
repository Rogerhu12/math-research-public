# 原有限零点的二阶切向变形、公共因子 K67 与条件来源界 8705

日期：2026-11-15。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿不运行新计算。它将真实切向族的二阶消失直接用于原有限参数 $s=0$，证明原全部最大子式在此至少消失二十一阶；由此把已知有限公共因子从 $K_{60}$ 提升为 $K_{67}$。与已经证明的同选无穷远 $43/42/41$ 阶结合后，原九目标的**条件性**来源界降为 $8705$。原目标成员性和相关最高系数的 $31$ 单位性仍是独立的未付条件。

## 1. 有限零点使用原物理参数，不是零均值

这里 $y(s)=v(s)=(1,s,\ldots,s^5)^{\mathsf T}$，所以 $s=0$ 时 $y=e_0\ne0$。使用原十一条 $N$ 和六条 $\Gamma$，以及来源次数至多三、输出次数一至五的完整矩阵

$$
A(s):\mathbb Q[[s]]^{6188}\longrightarrow
\mathbb Q[[s]]^{4367},
\qquad A(s)=A_0+sA_1+\cdots.
\tag{1.1}
$$

[原零点完整临界证明](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md)
§§3–5 已给出

$$
\operatorname{rank}_{\mathbb Q}A_0=4340.
\tag{1.2}
$$

具体上界来自原 $170\times135$ 投影的七个独立整数核；同一完整原矩阵的模七下界夹成等号。因此不能把这一特征零秩仅解释成有限域观测。

令切向坐标为 $c=m_0,d=m_1$，横向坐标为 $m_2,\ldots,m_{10}$。旧证明还给出：至少含两个横向因子的全部 $4212$ 维输出空间属于 $\operatorname{im}A_0$，恰好一个横向因子的 $135$ 维空间被覆盖 $128$ 维，纯切向的 $20$ 个坐标全部在余空间中。因此完整余空间为 $20+7=27$ 维。

函数域完整秩仍为原已付的 $4354$，本稿没有改变原矩阵或来源字典。

## 2. 全部十七式在真实切向图上可被 s² 整除

原配对恒等式给

$$
y^{\mathsf T}Ky=y^{\mathsf T}Ky'=0,
\qquad
g(s)=y'(s)^{\mathsf T}Ky'(s)
=-2s^2(s-2)(s+6).
\tag{2.1}
$$

具体原 $K$ 的推导见
[零第三矩完整分类](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md)
§5。取

$$
M(s;c,d)=c\,yy^{\mathsf T}
+d\bigl(yy'^{\mathsf T}+y'y^{\mathsf T}\bigr).
\tag{2.2}
$$

它是完整真实 Hankel 矩，坐标可直接写成

$$
m_j(s;c,d)=c s^j+d j s^{j-1}\quad(0\le j\le10),
\tag{2.3}
$$

其中 $j=0$ 的第二项定义为零。在 $s=0$，(2.3) 准确回到 $m_0=c,m_1=d$、其余为零的原切向平面。

置 $p=Ky$。由 (2.1)，

$$
Mp=0,\qquad MKM=d^2g(s)yy^{\mathsf T}.
\tag{2.4}
$$

$yM$ 是由 $y^3$ 及其导数构成的真实 Hankel 三阶张量，原最高方程唯一性给 $\mathcal L_y(M)=yM$。原完整低式是

$$
N=4MKM+6(\mathcal L_y(M))_p,
$$

$$
\Gamma=2\operatorname{tr}((KM)^2)y
+8MKMp-12\mathcal L_y(M):(KMK).
$$

因为 $Mp=y^{\mathsf T}p=0$，有 $(yM)_p=0$。又有
$\operatorname{tr}((KM)^2)=0$、$MKMp=0$，并且

$$
(yM):(KMK)
=\tfrac13\left[y\operatorname{tr}(MKMK)+2MKMKy\right]=0.
$$

故在同一真实图上

$$
\boxed{N=4d^2g(s)yy^{\mathsf T}=O(s^2),\qquad \Gamma=0.}
\tag{2.5}
$$

$O(s^2)$ 是原多项式环中的准确整除性。原十一条 $N$ 系数及六条 $\Gamma$ 坐标全部保留，非零常数方程缩放也不改变它。

## 3. 零点完整第一连接至多七维

任取 $v\in\ker A_0$，按原来源将它写成次数至多三的系数 $a_i(m)$。令

$$
P(s,m)=\sum_{i=1}^{17}a_i(m)F_i(s,m).
$$

$A_0v=0$ 给 $P(0,m)\equiv0$，故 $P=sP_1+O(s^2)$，其中 $P_1$ 对应 $A_1v$。把 (2.2) 代入，(2.5) 给 $P(s,M(s;c,d))=O(s^2)$。因此

$$
P_1(c,d,0,\ldots,0)=0.
\tag{3.1}
$$

完整第一连接

$$
\beta_0:\ker A_0\longrightarrow\operatorname{coker}A_0,
\qquad v\longmapsto[A_1v]
$$

于是被全部二十个纯切向泛函杀掉。由第 1 节余空间的完整 $20+7$ 分解，

$$
\boxed{\operatorname{rank}_{\mathbb Q}\beta_0\le7.}
\tag{3.2}
$$

在 $\mathbb Q[[s]]$ 的 Smith 形式中，完整矩阵有 $4340$ 个单位不变量和十四个正指数 $s^{\alpha_j}$。第一连接秩等于其中 $\alpha_j=1$ 的个数。因此至少七个 $\alpha_j\ge2$，给

$$
\sum_{j=1}^{14}\alpha_j\ge21.
$$

所以

$$
\boxed{s^{21}\text{ 整除每个原 }4354\text{ 阶最大子式。}}
\tag{3.3}
$$

这不要求第一连接恰有秩七，也不提供 Smith 指数的上界。

## 4. 已知有限公共因子升为 K67

沿用
[原最大子式公共因子](R150-appendix-projective-minor-divisor-degree-and-finite-cover-certificate.md)
中的互不相交原根集合。旧有限因子为

$$
K_{60}(s)
=s^{14}(s-2)^9(s+6)^9F_+(s)^2F_-(s)^2E_8(s)^2,
$$

$$
F_+=5s^3-25s^2+32s-8,\qquad
F_-=5s^3+135s^2+864s+864.
$$

其余因子在 $s=0$ 均非零，原根集合的互素性已有完整证明。用 (3.3) 替换原 $s^{14}$ 因子，得到

$$
\boxed{
K_{67}(s)=s^7K_{60}(s)
=s^{21}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2.}
\tag{4.1}
$$

于是 $K_{67}$ 整除每个原最大子式，$\deg K_{67}=67$，最高系数仍为原 $5^6$，是 $31$ 单位。这仍只是已经证明的公共下因子，不是完整 gcd。

与
[无穷远第一连接的七维上界](R150-appendix-infinity-first-connection-seven-dimensional-bound-and-common-order-twentyone.md)
结合，全部自然齐次最大子式还共同含相应的 $s^{21}t^{21}$ 因子，总已知齐次下因子次数为 $88$。但下节指定子式已用更强的无穷远 $43$ 阶；不能再把公共无穷远 $21$ 阶与 $43$ 阶相加。

## 5. 同一非零子式和 q 的真实上下界

保持
[同选 Koszul 曲线的 43 阶来源界](R150-appendix-selected-koszul-curves-infinity-order43-and-source-cost8712.md)
的原行列集合：

$$
B=A_{I,J},\quad |I|=|J|=4354,\quad
D=\det B\ne0,\quad H=8770.
$$

原来源和输出权为 $a_\ell,b_i$，来源成本权 $\delta_\ell=a_\ell-10$，并有
$\max a_\ell=55$、$\max\delta_\ell=45$。

同一 $29$ 维真实 selected Koszul 曲线已给：

- $D$ 的无穷远消失至少 $43$ 阶；
- 任意换入一个外来源后的最大子式至少 $42$ 阶；
- 每个 $4353$ 阶 cofactor 至少 $41$ 阶。

这里仅使用该已付来源论证，不把有限域核当成真实来源曲线。令

$$
d_*=D/K_{67},\qquad q=\deg d_*.
$$

同一 $D$ 在模 $31$ 非零，且其约化被原完整 $315$ 次仿射最大子式 gcd 整除，所以 $\deg D\ge315$。结合有限因子次数 $67$ 和指定无穷远阶 $43$，

$$
\boxed{248\le q\le8770-43-67=8660.}
\tag{5.1}
$$

没有把模 $31$ 的 $315$ 次因子提升为特征零因子；它只用于这个次数下界。

## 6. 完整原输出的条件降度

对任一原来源列 $A_\ell$，定义

$$
P_\ell=\operatorname{adj}(B)(A_\ell)_I/K_{67}.
$$

每个分量是一个换列最大子式除以已付公共因子，所以它是多项式。原函数域完整秩给全部 $4367$ 输出上的准确恒等式

$$
A_JP_\ell=d_*A_\ell.
\tag{6.1}
$$

换列的自然权和 $42$ 阶无穷远消失给

$$
\deg(P_\ell)_j
\le H-a_j+a_\ell-42-67.
\tag{6.2}
$$

现在且仅现在，**假设**某个原目标
$b_\nu=h_0t_\nu$ 已有 $\mathbb Q[s]$ 来源，其中

$$
t_\nu=
\left(\sum_{k=0}^{\nu}\binom\nu k(-s)^{\nu-k}m_k\right)^2,
\qquad 2\le\nu\le10,\qquad \deg h_0=24.
$$

原目标共同权满足 $\tau_\nu\le64$。
将非基来源系数除以 $d_*$，再由 (6.1) 移入基来源，可保持同一目标并令

$$
\deg y_\ell<q\quad(\ell\notin J).
$$

在这个已有成员性的前提下，

$$
T_\nu=\operatorname{adj}(B)(b_\nu)_I/K_{67}
$$

也是多项式，且

$$
d_*y_j=(T_\nu)_j-
\sum_{\ell\notin J}(P_\ell)_j y_\ell.
\tag{6.3}
$$

cofactor 的 $41$ 阶无穷远消失给

$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-41-67.
\tag{6.4}
$$

故非基来源成本至多

$$
q-1+45\le8704.
$$

由 (6.2)–(6.4)，基来源成本至多

$$
\begin{aligned}
\deg y_j+\delta_j
&\le\max\left\{
H+\tau_\nu-41-67-10-q,\max_\ell(H+a_\ell-42-67-11)
\right\}\\
&\le\max\left\{
8770+64-41-67-10-248,8770+55-42-67-11
\right\}\\
&=\max\{8468,8705\}=8705.
\end{aligned}
$$

因此得到新的准确条件定理

$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\ \Longrightarrow\ 
\exists y^{(\nu)}:\ Ay^{(\nu)}=h_0t_\nu,
\quad\operatorname{cost}(y^{(\nu)})\le8705.}
\tag{6.5}
$$

有限因子增加七阶使基转移上界减少七；目标分支仍为 $8468$，因为同一 $q$ 的下界也从 $255$ 降为 $248$，两项准确抵消。不能把目标分支再无条件减七。

## 7. 仍保留的条件

$K_{67}$ 的最高系数为 $31$ 单位，所以单位首项除法给
$d_*,P_\ell\in\mathbb Z_{(31)}[s]$。但还没有证明
$\operatorname{lc}(d_*)$ 或等价的 $\operatorname{lc}(D)$ 是 $31$ 单位。

若以后支付该额外条件，同一降度可逐个用于含零因子的
$\mathbb Z_{(31)}/31^n$，并保固定的目标乘子 $31^e$；
本稿不把一次模 $31^6$ 成员性替换成无界精度，更不据此宣布原特征零成员性。

本稿新增的是原零点的真实二阶切向消失、公共 $K_{67}$ 和由此得到的条件次数界。原目标本身是否属于多项式来源模、完整 Smith 长度以及普通 ISP 均未由这些结论完成。
