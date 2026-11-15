# 真正最小投影的带正向 gauge 窗口与原同源左配对

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

状态：完整证明。保留既有 $c=26$ 的最大无权窗口。本稿在严格大于 $25$ 的稍短窗口内，把原联合 carry 的余量用于真正正交投影和左最小代表的 $G_{1,m}$ 误差。新的结论作用于同一个实际 $v_Q,u_Q$，不止一个构造性修复。尚未支付高孔自配对、普通右费或原 $N=M$。

## 1. 原对象和明确常数

固定原 $N/Y$ 两个模型之一，取
$$
m\ge10,\qquad d=2^m,\qquad
c_*=\frac{1601}{64}=25+\frac1{64}.
$$
沿用
$$
M=\ker T,\quad N=\overline{BM},\quad W=M\ominus N,
\quad L_m=A_m+D_m.
$$
原尾孔截断记为 $P_{\le Q}^{(m)}$。
令 $V_{m,Q}$ 是支撑在尾孔数 $\le Q$、满足原全部低输出方程的闭子空间；
$K_{m,Q}=\ker L_m\cap\mathcal H_{\le Q}^{(m)}\subset V_{m,Q}$。
对同一个 $w\in W$，始终使用真正物理正交投影
$$
v_Q=P_{V_{m,Q}}w,\qquad k_Q=P_{K_{m,Q}}w,\qquad u_Q=v_Q-k_Q.
\tag{1.1}
$$
因两个空间嵌套，$u_Q$ 正是该实际来源的左最小代表，且
$\|u_Q\|,\|v_Q\|,\|P_{\le Q}^{(m)}w\|\le\|w\|$。

原有限头有
$$
A_m=F_m(B_m),\qquad
G_{1,m}=\left(\frac{F_m(B_m)}{B_m}\right)^{-1}\otimes I
       =p_m(B_m)\otimes I.
\tag{1.2}
$$
第一式中的商按标量解析延拓定义，不是对幂零 $B_m$ 取逆。
$p_m$ 是 $(F_m(z)/z)^{-1}$ 的 $<d$ Taylor 截断。
[真逆芽稿](../notes/2026-11-14-true-head-inverse-germ-twelve-half-radius-and-weighted-coefficients-789f-next.md)
给
$$
\rho_m=e^{-25d^3/2},\qquad
|p_{m,k}|\le2d_0\rho_m^{-k},\quad k<d,\qquad d_0=e^{-20}.
\tag{1.3}
$$

本稿证明：对所有整数 $4d\le Q\le e^{c_*d^3}$，
$$
\|v_Q-P_{\le Q}^{(m)}w\|,\ \|k_Q\|
    \le e^{-6d^4}\|w\|,
\qquad
\|u_Q-P_{\le Q}^{(m)}w\|\le2e^{-6d^4}\|w\|.
\tag{1.4}
$$
并有真正带权界
$$
\|G_{1,m}\|\le e^{47d^4/8}.
\tag{1.5}
$$
置 $\zeta_m=e^{-d^4/8}$。对 $H=G_{1,m}$ 或 $H=G_{1,m}^*$，因而
$$
\boxed{
\|H(v_Q-P_{\le Q}^{(m)}w)\|,\ \|Hk_Q\|
\le\zeta_m\|w\|,\qquad
\|H(u_Q-P_{\le Q}^{(m)}w)\|\le2\zeta_m\|w\|.
}
\tag{1.6}
$$
这是已付的原范数余量与真实环境范数之间的比较；没有将一个未知速率的强收敛乘以 $\|G_{1,m}\|$。

## 2. 原实际后移幂和 $35/6$ 的费用

这里使用的 bit 加性机制已有于
[R236 联合 gauge 稿 §2](../results/R236-appendix-joint-gauge-row-powers-and-carry-corrected-targets.md)；
本节只把它在当前 $G_{1,m}$ 的原权和明确半径下写全，不重计一般 gauge 机制。

原后移为
$$
Be_n=\alpha_{v_2(n)}e_{n-1},\qquad
\alpha_j=\frac{d_j}{\prod_{i<j}d_i},\qquad
W_n=\prod_{i\in\operatorname{bits}(n)}d_i,
$$
$$
d_i=e^{-\Lambda_i},\qquad
\Lambda_i=100\,16^i-105\,8^i+(150i+25)2^i.
\tag{2.1}
$$
[全局 carry 锚 §2](../notes/2026-11-15-global-weighted-shift-to-true-head-gauge-carry-and-w-anchor-789f-next.md)
已逐项核 $\alpha_j$ 严格递减。
写
$$
\alpha_j=\alpha_0\prod_{h=1}^j\frac{\alpha_h}{\alpha_{h-1}}.
$$
任意连续 $k$ 个正整数中，$2^h$ 的整倍数至少有
$\lfloor k/2^h\rfloor$ 个；初始区间 $1,\ldots,k$ 对所有 $h$ 同时取等。
每个比值 $\alpha_h/\alpha_{h-1}\le1$，故全部长度 $k$ 的真实权积不超过初始权积 $W_k$。输入 $e_k$ 取得该值，得到
$$
\|B^k\|=W_k,\qquad
\|B_m^k\|=W_k\quad(0\le k<d).
\tag{2.2}
$$

令 $t=25d^3/2$ 和 $\omega_k=-\log W_k$。
每个 $i<m$ 有 $2^it-\Lambda_i>0$：
$\Lambda_i\le100\,16^i$，而
$100\,8^i\le(25/2)d^3$，最高位也因原负次高项严格小于。
所以
$$
kt-\omega_k
=\sum_{i\in\operatorname{bits}(k)}(2^it-\Lambda_i)
\le(d-1)t-\sum_{i<m}\Lambda_i.
\tag{2.3}
$$
原权的准确求和是
$$
\sum_{i<m}\Lambda_i
=\frac{20}{3}d^4-15d^3+(150m-275)d+\frac{850}{3}.
$$
因此 (1.3)、(2.2)–(2.3) 给
$$
\begin{aligned}
\log\|G_{1,m}\|
&\le \log(2dd_0)
 +\frac{35}{6}d^4+\frac52d^3
 -(150m-275)d-\frac{850}{3}\\
&\le \frac{35}{6}d^4+3d^3
 \le\frac{47}{8}d^4.
\end{aligned}
\tag{2.4}
$$
最后只用 $d\ge1024>72$。
这是当前整个有限头算子的范数，不是某一列、形式系数范数或压缩逆。

## 3. 较短窗口中的完整联合 carry 余量

以下重用
[c26 原联合 carry 稿](../notes/2026-11-14-joint-positive-carry-budget-and-twenty-six-window-actual-sources-789f-next.md)
的同一矩阵支配、相容右逆、修复和物理空间；只改变用于估计的正参数。

对 $p\ge m$，置
$$
z=2^p,\qquad
\mathcal R_p^*=\exp\!\left(\frac{1605}{32}z^3\right),
\qquad
\xi_p=\frac{d_0}{4\mathcal R_p^*},\qquad
t_p=\log\xi_p^{-1}.
$$
于是
$$
t_p=\frac{1605}{32}z^3+20+\log4
\le\frac{803}{16}z^3.
\tag{3.1}
$$
这里 $1605/32-2c_*=1/8$。所以对
$Q\le e^{c_*d^3}$，原每一步右逆参数仍满足
$$
R_0\le512(Q+5z)^2\le\mathcal R_p^*.
\tag{3.2}
$$
确实，$\log R_0\le2c_*d^3+7+2\log(1+5z)$，而最后两项不超过 $z^3/8$。
实际低输出右逆的 $R_0\le2048Q^2$ 也被 $\mathcal R_m^*$ 控制。
提高估计参数不改变原右逆或原来源。

令
$$
g_p(s)=\sum_{i<p}b_i\frac{s^{2^i}}{d_i-s^{2^i}},
\qquad b_i=(i+1)^{-2}.
$$
这是原 $N/Y$ 两个真实有限头函数的共同非负系数支配。
$\xi_p\le e^{-50z^3}$，故对 $1\le i<p$，
$$
\log\frac{\xi_p^{\,2^i-1}}{d_i}
\le100\,16^i-50z^3(2^i-1)
\le-\frac{25}{2}z^3\,2^i\le-25z^3.
$$
原最低项和其余分母的同一几何级数估计遂给
$$
g_p(\xi_p)\le2\xi_p/d_0,\qquad
\mathcal R_p^*g_p(\xi_p)
e^{2\mathcal R_p^*g_p(\xi_p)}\le e/2.
\tag{3.3}
$$

写真实新位误差
$$
K_p=L_{p+1}-L_p=
\begin{pmatrix}0&C_p\\0&0\end{pmatrix}.
$$
原正系数跨块和依次支配
$|A_m^jC_pA_m^k|$，并把两个 factorial 和收进
$\mathcal R_p^*g_p(B_{p+1})e^{2\mathcal R_p^*g_p(B_{p+1})}$。
保留全部原权后，$(u,z+v)$ 条目准确带因子
$$
\frac{d_pW_v}{W_u}\xi_p^{-(z+v-u)},
\qquad0\le u,v<z.
$$
如 c26 §3，所有 bit 贡献 $2^it_p-\Lambda_i$ 正，
所以最坏原位置仍是 $u=0,v=z-1$，不是分别取不同列的最坏值。
使用原准确和
$$
\sum_{i=0}^{p}\Lambda_i
=\frac{320}{3}z^4-120z^3+(300p-250)z+\frac{850}{3},
$$
包括全部 $z^2$ 条目后的对数上界为
$$
-\frac{151}{24}z^4+120z^3+2\log z+1
\le-\frac{37}{6}z^4.
\tag{3.4}
$$
最后一步是
$120/z+(2\log z+1)/z^4\le1/8$，对 $z\ge1024$ 成立。
因此原完整联合预算锐为
$$
\boxed{
R\sum_{j,k<2^m}
\frac{R^{j+k}}{(j+1)!\,k!}
\|A_m^jK_pA_m^k\|
\le e^{-(37/6)16^p},
\qquad0<R\le\mathcal R_p^*.
}
\tag{3.5}
$$
$A_m$ 在更大头上仍按恒等张量延拓。
(3.5) 保留最高跨块次数 $2z-1$ 和真实 $Y$ 几何级数，没有额外重复乘一次 carry 衰减。

## 4. 同一个母提升与真正低输出投影

首先对 $k\in K_{m,Q}$，沿 c26 §4 的同一步骤
$$
c_p=\sum_{j<z}(-A_{p+1})^jR'_{j+1}K_pk_p,\qquad
k_{p+1}=k_p-c_p
$$
及真实关系
$D_{p+1}^{\ell}K_pk_p=K_p(-A_p)^\ell k_p$，
(3.5) 给
$$
\|c_p\|\le e^{-(37/6)z^4}\|k_p\|.
$$
原孔数、自然右逆域和支撑均不变。
因此同一个母提升 $\Lambda_{m,Q}:K_{m,Q}\to N$ 满足
$$
\|\Lambda_{m,Q}k-k\|
\le4e^{-(37/6)d^4}\|k\|
\le e^{-6d^4}\|k\|.
\tag{4.1}
$$
其进入 $N$ 的理由也不变：修复在每个固定指数孔权中可和，
最终落在原 $M\cap X_3\subseteq N$。

还必须支付真正 $v_Q$ 的误差，不能只用 (4.1)。
固定 $A=A_m,D=D_m,\mathcal E=L_m-T=-\sum_{p\ge m}K_p$ 和
$R=\mathcal R_m^*$。
原联合交换子预算为
$$
\mathcal J_m(R)
=R\sum_{j,k<d,\ a\ge0}
\frac{R^{j+k+a}}{(j+1)!\,k!\,a!}
\|A^j(\operatorname{ad}_D^a\mathcal E)A^k\|.
\tag{4.2}
$$
在每个 $p=m+r$，原逐位平方零关系给完整导数因子
$\prod_{i=m}^p(1+Rb_i)^2$。由 (3.1)，其对数至多
$$
\frac{803}{8}(r+1)d^3\le\frac18\,16^p,
$$
因为 $803(r+1)\le16^r d$。
于是 (3.5) 给
$$
\mathcal J_m(R)
\le\sum_{p\ge m}e^{-(145/24)16^p}
\le2e^{-(145/24)d^4}.
\tag{4.3}
$$
全部求和绝对收敛，仍是完整 $\mathcal E$ 而非首个新位误差。

c26 §§5–6 的粗吸收量
$$
\epsilon_m(R)=\sum_{a\ge0}\frac{R^a}{a!}
\|\operatorname{ad}_D^a\mathcal E\|,\qquad
H_m(R)=\sum_{j<d}\frac{R^j}{j!}\|A^j\|
$$
都对正 $R$ 单调。当前 $R$ 小于该稿的原参数，
故其已证 $RH_m(R)\epsilon_m(R)<1/4$ 仍成立。
对同一实际 $w\in M$，
$Dw=-Aw+\mathcal Ew$ 的完整 Leibniz 展开、有限头展开及原右逆给一个合法低输出修复 $z_Q$，满足
$$
\begin{aligned}
\|z_Q\|
&\le\mathcal J_m(R)
   (1+2RH_m(R)\epsilon_m(R))\|w\|\\
&\le4e^{-(145/24)d^4}\|w\|
 \le e^{-6d^4}\|w\|.
\end{aligned}
\tag{4.4}
$$
这是原 c26 (6.4)–(6.5) 的同一估计：
全部 $D$ 交换子和再次出现的 $\mathcal Ew$ 已保留，没有另付两个独立头幂和。

$P_{\le Q}^{(m)}w-P_{\le Q}^{(m)}z_Q$ 属于真实 $V_{m,Q}$。
由于 $v_Q$ 是同一物理正交投影，最小距离给
$$
\|v_Q-P_{\le Q}^{(m)}w\|\le e^{-6d^4}\|w\|.
$$
又 $w\perp N$ 与 (4.1) 给
$$
\|k_Q\|^2=\langle w,k_Q-\Lambda_{m,Q}k_Q\rangle
\le e^{-6d^4}\|w\|\|k_Q\|.
$$
这证明 (1.4)，包括两个真实最小化而非只包括构造 $z_Q$。
乘已付 (2.4) 得 (1.6)。

## 5. 真正反向 $V$ 投影反馈和同一顶部的全部左截断

$G_{1,m}$ 只作用原物理头，故与尾孔截断交换；它也与 $A_m,D_m$ 交换，
所以保持 $V_{m,Q}$ 和 $K_{m,Q}$。
由 $V_{m,Q}\subset\mathcal H_{\le Q}^{(m)}$，
$$
\begin{aligned}
P_{V_{m,Q}}G_{1,m}(I-P_{V_{m,Q}})w
 &=P_{V_{m,Q}}G_{1,m}
      (P_{\le Q}^{(m)}w-v_Q).
\end{aligned}
$$
因此
$$
\boxed{
\|P_{V_{m,Q}}G_{1,m}(I-P_{V_{m,Q}})w\|
\le\zeta_m\|w\|.
}
\tag{5.1}
$$
等价地，$\|P_{V_{m,Q}}G_{1,m}w-G_{1,m}v_Q\|\le\zeta_m\|w\|$。
这里未将 $G_{1,m}$ 与物理正交投影交换；(5.1) 正是该同源误差的已付上界。

取 $Q_m=\lfloor e^{c_*d^3}\rfloor$ 和同一 $u_m=u_{Q_m}$。
原实际源为
$$
r_{m,p}=A_m(u_m)_p,\qquad 4d\le p\le Q_m-d.
$$
它仍在原准确负图，且真正左最小者满足
$$
U_{m,p}r_{m,p}=P_{\le p}^{(m)}u_m.
$$
将 (1.6) 再作低孔收缩，对 $H=G_{1,m},G_{1,m}^*$ 同时得到
$$
\boxed{
\sup_{4d\le p\le Q_m-d}
\|H(U_{m,p}r_{m,p}-P_{\le p}^{(m)}w)\|
\le2\zeta_m\|w\|.
}
\tag{5.2}
$$
没有为每个 cut 重新选源，也没有额外累计 $Q_m$ 次母误差。

若 $L_{m,p}=U_{m,p}^*U_{m,p}$，头乘子保持左方程和零源核。
故 $G_{1,m}U_{m,p}r-U_{m,p}(G_{1,m}r)$ 属于真实左零源核，
而 $U_{m,p}r$ 与其正交。因此
$$
\langle U_{m,p}r,G_{1,m}U_{m,p}r\rangle
=\langle L_{m,p}r,G_{1,m}r\rangle.
$$
(5.2) 和两侧向量范数 $\le\|w\|$ 遂给
$$
\boxed{
\left|
\langle L_{m,p}r_{m,p},G_{1,m}r_{m,p}\rangle
-\langle P_{\le p}^{(m)}w,G_{1,m}P_{\le p}^{(m)}w\rangle
\right|
\le4\zeta_m\|w\|^2.
}
\tag{5.3}
$$

## 6. 已付范围及仍须保留的两项

原全局 carry 锚给
$$
|\langle w,G_{1,m}w\rangle-d_0\|w\|^2|
\le e^{-80d^4}\|w\|^2.
$$
所以 (5.3) 可准确改写为
$$
\begin{aligned}
\langle L_{m,p}r_{m,p},G_{1,m}r_{m,p}\rangle
={}&d_0\|w\|^2\\
&-\langle P_{>p}^{(m)}w,G_{1,m}P_{>p}^{(m)}w\rangle
+\mathcal R_{m,p},
\end{aligned}
\tag{6.1}
$$
其中 $|\mathcal R_{m,p}|\le(4\zeta_m+e^{-80d^4})\|w\|^2$，
全窗口一致。**高孔自配对仍保留在 (6.1) 中**；
未知速率的尾范数不能直接乘 $\|G_{1,m}\|$ 删去它。

另一方面，原同源 $G_{1,m}A_m=B_m$ 给
$$
|\langle L_{m,p}r_{m,p},G_{1,m}r_{m,p}\rangle|
\le \operatorname{flat}_{m,p}(r_{m,p})\,
       \lambda_{m,p}\!\left(B_m(u_m)_p\right).
\tag{6.2}
$$
这里 $\lambda$ 是普通完整右链费用；它与已付 $\Xi$ 中的完整裸链
$\alpha$ 不同。本稿未证明 (6.2) 第二因子的统一上界或构造其完整封口未来。

(5.1) 也不意味着 $P_{K_{m,Q}}G_{1,m}w$ 小：
该量仍包含 $P_{K_{m,Q}}G_{1,m}u_Q$。
本稿支付的是 $V$ 外侧到内侧的同源反馈，以及从 $v_Q$ 删除实际 $k_Q$
时的带权误差，不删除左最小源与低核之间的剩余非自伴块。

最后，新窗口保留原同一顶部的整窗预算，只将误差换成当前值：
$$
\sum_{p=4d}^{Q_m-d}\Xi_{m,p}(r_{m,p})^2
\le2d\bigl(\tau_m+2e^{-6d^4}\|w\|\bigr)^2,
\qquad
\tau_m=\|\mathbf1_{\{\mathcal N_{\rm tot}>4d\}}w\|\longrightarrow0.
\tag{6.3}
$$
若将来对这一实际来源证明
$\mu_{m,p}(r_{m,p})^2\le\kappa(m)\Xi_{m,p}(r_{m,p})^2$，
则 $\kappa(m)d/Q_m=O(1)$ 已是足够的平均预算；
$\kappa(m)=O(\rho_m^{-2})$ 更给
$$
\frac{\kappa(m)d}{Q_m}=O\!\left(d\,e^{-d^3/64}\right)\longrightarrow0.
$$
这只说明当前窗口容许的量级，没有把源 Schur、角度或 (6.2) 当成已证比较。
