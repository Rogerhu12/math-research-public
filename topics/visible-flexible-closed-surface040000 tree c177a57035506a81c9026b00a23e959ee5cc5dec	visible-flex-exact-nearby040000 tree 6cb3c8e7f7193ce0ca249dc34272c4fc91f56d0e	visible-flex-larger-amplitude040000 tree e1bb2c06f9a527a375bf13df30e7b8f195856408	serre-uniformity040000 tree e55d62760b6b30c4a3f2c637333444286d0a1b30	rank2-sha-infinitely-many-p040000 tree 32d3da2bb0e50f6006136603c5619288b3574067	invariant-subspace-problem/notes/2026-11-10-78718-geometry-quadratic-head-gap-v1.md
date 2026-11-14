# 有限头部的二次无理主角与全高频 target gap

作者：Astra-visible-flex-78718bd0 / geometric_closure，2026-11-10。

**状态：有完整证明，待未参与者独审。** 本文提供一个有效的全频算术接口，
不构造实际 Darboux 头部，不声称已锁定当前 flat17 的主返回角，
不声称已有新全 Green 或精确闭面。没有运行新的数值候选。

动机是 R517 的准确 multiplier
$D_j=Q_{0,j}\exp i[-j(\alpha-\alpha_*)+
(c_1-c_{1,*})/j+(c_2-c_{2,*})/j^2]$。
若有限头部可以通过真实 metric 控制把主角固定为一个二次无理角，
下列引理将所有足够高 $j$ 的 target gap 化为一个次主系数的严格间隙。
它比只检查有限频率多支付了实际的无限频率尾。

## 1. 准确输入与结论

取整数 $A>0,B,C$，令
$$
\Delta=B^2-4AC>0
$$
不是完全平方数，$\theta$ 是 $A\theta^2+B\theta+C=0$ 的任一实根。
置 $\alpha=2\pi\theta$。
给实数 $c_1,c_2$、整数 $J_0\ge1$、$R\ge0$ 及一列真实 unitary 数
$D_j$，满足对全部整数 $j\ge J_0$ 有真实相位表示
$$
D_j=\exp i\left(-2\pi j\theta+\frac{c_1}{j}
                         +\frac{c_2}{j^2}+\varepsilon_j\right),
\qquad |\varepsilon_j|\le Rj^{-3}.
\tag{1}
$$
这是全频输入，不是只在已算频率上的拟合。
令
$$
b_1=\frac{c_1}{2\pi},\quad b_2=\frac{c_2}{2\pi},\quad r_3=\frac R{2\pi},
$$
并给出一个严格正的认证数 $\gamma$，满足
$$
0<\gamma\le
\operatorname{dist}\bigl(4\sqrt\Delta\,b_1,
                         \mathbb Z\setminus\{0\}\bigr).
\tag{2}
$$
特别 $c_1=0$ **允许**取 $\gamma=1$，不能误把 (2) 改成到全部整数的距离。
不要求 $c_1$ 小；被排除的是离散集合
$4\sqrt\Delta\,b_1\in\mathbb Z\setminus\{0\}$。

设
$$
B_*=|b_1|+|b_2|+r_3+1,
\qquad a_0=4AB_*^2+4\sqrt\Delta\,r_3,
\qquad a_1=4\sqrt\Delta\,|b_2|.
\tag{3}
$$
选整数
$$
J\ge\max\left\{J_0,1,
\left\lceil\sqrt{\frac{4a_0}{\gamma}}\right\rceil,
\left\lceil\frac{4a_1}{\gamma}\right\rceil\right\}.
\tag{4}
$$
则全部 $j\ge J$ 都有
$$
|1+D_j|\ge\frac{\gamma}{2\sqrt\Delta}\,\frac1j.
\tag{5}
$$
因此也满足原 $j^{-1.3}$ 档的下界。
若原物理空间只使用偶频或 3 的倍频，(5) 在该子类当然仍成立；
没有扩大实际源空间的结论。

同时主角自身满足一个有效 homogeneous 下界：对全部非零整数 $l$，
$$
|e^{il\alpha}-1|
\ge\frac4{\sqrt\Delta+A/2}\,\frac1{|l|}.
\tag{6}
$$
这比指数 2 的 homogeneous DC 门更强。若某处约定 DC 常数不超过 1，
再将 (6) 的常数与 1 取最小即可。

## 2. 二次代数恒等式

记另一根为 $\theta'$，置
$\sigma=\operatorname{sgn}(\theta-\theta')\in\{-1,1\}$，则
$A(\theta-\theta')=\sigma\sqrt\Delta$。
对任意整数 $p,q$、$q\ne0$，有
$$
N=A p^2+Bpq+Cq^2
  =A(p-q\theta)(p-q\theta')\in\mathbb Z\setminus\{0\}.
\tag{7}
$$
最后严格非零是因为 $p/q$ 不等于两个无理根中的任一个。
若 $x=q\theta-p$，则
$$
N=-\sigma q\sqrt\Delta\,x+Ax^2.
\tag{8}
$$
式 (7)–(8) 是后面全频结论的依据；没有用浮点近似判定无理性。

## 3. Target gap 的完整证明

对固定 $j\ge J$，在整数 $k$ 中选择使下式绝对值最小的一项：
$$
\tau=j\theta-(k+\tfrac12)-\frac{b_1}{j}
                          -\frac{b_2}{j^2}
                          -\frac{\varepsilon_j}{2\pi}.
\tag{9}
$$
记 $t=|\tau|\in[0,1/2]$。由 (1)，
$$
|1+D_j|=2\sin(\pi t)\ge4t.
\tag{10}
$$
并且到 $\mathbb Z\setminus\{0\}$ 的距离不超过 1，故可按 (2) 取
$\gamma\le1$；$\sqrt\Delta\ge1$。
若 $t\ge1/j$，已经得到
$t\ge\gamma/(8\sqrt\Delta\,j)$。

余下设 $t<1/j$，令
$$
\delta=j\theta-(k+\tfrac12).
$$
由 (9) 与 (3)，
$$
|\delta|\le\frac{|b_1|+1}{j}+\frac{|b_2|}{j^2}
                              +\frac{r_3}{j^3}
\le\frac{B_*}{j}.
\tag{11}
$$
将 (8) 用于 $q=2j,p=2k+1,x=2\delta$，得到非零整数 $N$ 满足
$$
N+4\sigma\sqrt\Delta\,j\delta=4A\delta^2.
\tag{12}
$$
因为整数集合 $\mathbb Z\setminus\{0\}$ 关于原点对称，(2) 给
$|N+4\sigma\sqrt\Delta\,b_1|\ge\gamma$。
于是由 (9)、(11)–(12)，
$$
\begin{aligned}
\gamma
&\le4A\delta^2+4\sqrt\Delta\,|j\delta-b_1|\\
&\le\frac{4AB_*^2}{j^2}
 +4\sqrt\Delta\left(jt+\frac{|b_2|}{j}+\frac{r_3}{j^2}\right)\\
&=\frac{a_0}{j^2}+\frac{a_1}{j}+4\sqrt\Delta\,jt.
\end{aligned}
\tag{13}
$$
由 (4)，前两项各不超过 $\gamma/4$。
故 $t\ge\gamma/(8\sqrt\Delta\,j)$。
结合两种情形与 (10)，即得 (5)。证毕。

## 4. Homogeneous gap 的完整证明

只需 $l\ge1$。取最近整数 $p$，令 $x=l\theta-p$，所以 $|x|\le1/2$。
将 (8) 用于 $q=l$，因为 $N$ 是非零整数，
$$
1\le|N|\le l\sqrt\Delta\,|x|+A|x|^2
\le(l\sqrt\Delta+A/2)|x|.
$$
故
$$
|x|\ge\frac1{l\sqrt\Delta+A/2}
      \ge\frac1{l(\sqrt\Delta+A/2)}.
$$
再次用 $2\sin(\pi|x|)\ge4|x|$ 得 (6)。负 $l$ 的绝对值相同。证毕。

## 5. 如何从真实 multiplier 余项得到 (1)

若已证明实际 unitary $D_j$ 满足全频复数值界
$$
\left|D_j-
e^{i(-2\pi j\theta+c_1/j+c_2/j^2)}\right|\le C_3j^{-3},
\tag{14}
$$
并先增大 $J_0$ 使 $C_3J_0^{-3}\le1/2$，则有唯一的
$\varepsilon_j\in(-\pi,\pi)$ 满足 (1)，且
$$
|\varepsilon_j|\le2C_3j^{-3}.
\tag{15}
$$
事实上取两个 unitary 数的比 $e^{i\varepsilon_j}$；
$|e^{i\varepsilon_j}-1|\le1/2$ 且
$|\varepsilon_j|=2\arcsin(|e^{i\varepsilon_j}-1|/2)
\le2|e^{i\varepsilon_j}-1|$。
因此 (14) 给 (1)，取 $R=2C_3$。

这里 (14) 必须是实际全 multiplier 的余项界，含其常相位及真实
两 cones 规范；一个有限 WKB 符号、数值相位拟合或只检查有限个 $j$
均不支付 (14)。若前导常相位不是 0，必须先准确换成相应的 target；
本文没有默默丢掉该相位。R517 §5.3 明确说明其两程号与 strict Schur
符号来自原 flux/Airy/Gram recipe，不能只由“unitary 图”猜测。

## 6. 同一角下的稳定范围与剩余几何门

若主角 $\alpha$ **准确保持不变**，并有一个区间 $I_1$、统一上界
$|c_2|\le C_2$、$R\le R_*$，且
$$
\inf_{c\in I_1}
\operatorname{dist}\left(\frac{2\sqrt\Delta}{\pi}c,
                         \mathbb Z\setminus\{0\}\right)>0,
\tag{16}
$$
则以该严格下界作 $\gamma$、以 $I_1$ 中最大 $|c|$ 及 $C_2,R_*$
作 (3) 的上界，同一个 $J$ 和 (5) 同时适用于所有这些系数。
这是由 §§1–3 逐字得到的真正全频稳定性。

若 $\alpha$ 随 Newton 更新，即使 $|\Delta\alpha|$ 很小，
相位差 $j\Delta\alpha$ 也不对全部 $j$ 一致小。
所以 (16) **不能**替代主角锁定，也不意味着任意相邻背景自动保持同一 gap。
可行的几何应用还须实际构造一个调节主角的 metric 方向、其真偏导和
新增 current row/column，证明该有限增广系统可解；这些均未在本文支付。

即便 (1)–(6) 已在有限头部实现，还须完整 normal form、物理图逆、
低 Schur 逆、strong source/Hessian、无限尾与非线性收敛。
本文没有将算术门冒充这些几何或分析门，也没有改变主数值任务的固定 g。
