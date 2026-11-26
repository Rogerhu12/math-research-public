# R150 附录：秩一第三累积量的三重均值极线乘二次余因子分支

日期：2026-11-26。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 本稿整理前会话已经成功执行、尚未登记的原有理数证明源。它完整分类
$P_y\propto\Delta_s^3(q_s/\Delta_t)$、$q_s(t)=0$ 的原秩一第三累积量分支；
仅有四个射影参数上的同点临界族存活，其完整第三普通矩恒为零。
这里不假设 $s\ne t$、$q_s$ 无重根或节点有限。

## 1. 原标量多项式、矩与完整梯度

全程在 $\mathbb C$ 上工作。对 $x=[a:b]\in\mathbb P^1$，令
$$
u(x)=(a^5,a^4b,a^3b^2,a^2b^3,ab^4,b^5)^{\mathsf T},\qquad
K=\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix}.
$$
原变量是 $y\in\mathbb C^6$、十一条二阶 Hankel 矩 $H_m$ 及十六条三阶 Hankel 累积量 $V_m$：
$$
H_{ij}=H_{i+j},\qquad V_{ijk}=V_{i+j+k}\qquad(0\le i,j,k\le5).
$$
置
$$
p=Ky,\quad F=\tfrac12y^{\mathsf T}Ky,\quad h=Hp,\quad
b_0=p^{\mathsf T}Hp,\quad c=p^{\mathsf T}HKHp,\quad
\tau_j=\operatorname{tr}((KH)^j).
$$
用 $b_0$ 区别标量 $b_0$ 与射影坐标 $b$。令
$$
P_y(x)=p^{\mathsf T}u(x),\quad
G_H(x)=u(x)^{\mathsf T}KHK u(x),\quad
k(x,x')=u(x)^{\mathsf T}Ku(x').
$$
对 $j=2,3$，$J_j$ 是 $k((1,z),(1,\zeta))^j$ 的完整系数矩阵；
其指标为 $0\le m,n\le5j$。特别是
$$
(J_2)_{mn}=\sum_{i+a=m,\ j+b=n}K_{ij}K_{ab}.
\tag{1.1}
$$
写 $[g]$ 为二元齐次多项式的完整系数列，始终补足指定的齐次次数。
准确的原六次多项式为
$$
\mathcal Q_3
=G_6+4[P_y^3-6P_yG_H]^{\mathsf T}V+8V^{\mathsf T}J_3V,
$$
$$
G_6=F^3-6Fb_0+6F\tau_2+12c-8\tau_3.
\tag{1.2}
$$
这也可由有限微分式
$\mathcal Q_3=\exp(L_2+L_3)F^3$ 定义，其中
$$
L_2=-\sum_{i,j}H_{i+j}\partial_i\partial_j,\qquad
L_3=\tfrac23\sum_{i,j,k}V_{i+j+k}\partial_i\partial_j\partial_k.
$$
指数展开按次数有限终止；$K$ 各反对角线的和为零，因而
$u(x)^{\mathsf T}Ku(x)=0$、$\operatorname{tr}(KH)=0$ 和 $K:V=0$。
逐项求导给完整原梯度
$$
\partial_{V_m}\mathcal Q_3
=4\,[x^m]\{P_y^3-6P_yG_H+4(J_3V)(x)\},
\tag{1.3}
$$
$$
\tfrac13K^{-1}\nabla_y\mathcal Q_3
=\Gamma
=(F^2-2b_0+2\tau_2)y-4FHp+8HKHp
 +4V(p,p,\cdot)-8V:(KHK),
\tag{1.4}
$$
$$
\partial_{H_m}\mathcal Q_3=-6n_m,\qquad
n_m=[x^m]u(x)^{\mathsf T}KNKu(x),
$$
$$
N=Fyy^{\mathsf T}-2FH-2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH+4V_p.
\tag{1.5}
$$
在 (1.3)、(1.5) 中，$[x^m]$ 指齐次系数，分别有十六和十一项。
例如 (1.4) 由 (1.2) 的三个 summand 求导，
三阶项分别贡献 $4V(p,p,\cdot)$ 与 $-8V:(KHK)$；
(1.5) 中三阶项贡献 $4V_p$。
因此下面只在证明这些贡献确为零后才删除它们。
所有系数亦可从 (1.1)、(1.2) 作有限有理数运算重新取得。

## 2. 射影极线与本稿的准确分支

设 $V$ 的一阶展平秩为一且 $V\ne0$。对称性先迫 $V=v a^{\otimes3}$。
Hankel 性迫 $a_i a_j$ 只依赖 $i+j$：选一个非零 $a_k$，对三阶合并式除以这个固定非零标量即可。
若 $a_0\ne0$，由 $a_0a_{j+1}=a_1a_j$ 递推得到等比数列；
若首个非零坐标 $a_j$ 满足 $1\le j\le4$，则
$a_j^2=a_{j-1}a_{j+1}=0$ 矛盾；余下仅 $a_5\ne0$。
故恰有
$$
V=v\,u(s)^{\otimes3},\qquad v\ne0,\quad s\in\mathbb P^1.
\tag{2.1}
$$
对 $s=[s_0:s_1]$ 令 $\Delta_s(x)=s_0b-s_1a$，$k_s(x)=k(s,x)$。
直接展开原 $K$ 给
$$
k_s(x)=-\Delta_s(x)^2q_s(x),
\tag{2.2}
$$
其中二元三次式 $q_s$ 对 $s$ 也齐次三次；在有限图 $s=(1,s)$、$x=(1,z)$，
$$
q_s(z)=q_0(s)+q_1(s)z+q_2(s)z^2+q_3(s)z^3,
$$
$$
\begin{split}
q_0&=s^3-5s^2,\
q_1&=s^3-3s^2+22s,\
q_2&=-3s^2-3s-5,\
q_3&=s+1.
\end{split}
\tag{2.3}
$$
齐次式由把每个 $q_i$ 补为 $s_0,s_1$ 的三次式、再乘 $a^{3-i}b^i$ 得到。
特别地
$$
q_\infty(a,b)=a^2(a+b),\qquad
q_{-1}(a,b)=-a(6a^2+26ab+5b^2).
\tag{2.4}
$$
由于 $\det K=-25600$，$k_s$ 对任何射影 $s$ 均非零；故 $q_s$ 也从不恒零。

(1.3) 在 (2.1) 下等价于全部十六条系数恒等式
$$
P_y^3-6P_yG_H+4v k_s^3=0.
\tag{2.5}
$$
它迫 $P_y\ne0$ 且 $P_y\mid k_s^3$。
本稿只考察满足如下**齐次多项式等式**的完整临界点：
$$
q_s(t)=0,\qquad
P_y=\sigma f_{s,t},\qquad
f_{s,t}=\Delta_s^3\frac{q_s}{\Delta_t},\qquad \sigma\ne0.
\tag{2.6}
$$
因为 $q_s(t)=0$，$q_s/\Delta_t$ 是一个非零二元二次式；
没有除以参数函数、判别式或 $s-t$。
该定义包含合流 $s=t$，也包含 $q_s$ 的所有重根与射影边界。

**定理。** (2.1)、(2.6) 下的完整原临界点，经原权缩放后恰为
$$
s=t\in\{0,2,-6,\infty\},\qquad
y=-u(s),\quad H=\frac{1-\eta}{6}u(s)u(s)^{\mathsf T},\quad
V=\frac\eta4u(s)^{\otimes3},
\tag{2.7}
$$
其中 $\eta\ne0$ 任意。所有这些点的完整第三普通矩为零。
若容许 $V=0$，同式也包含 $\eta=0$，但并非定理秩一非零假设所需。

## 3. 最高方程唯一确定同一原参数族

$\mathcal Q_3$ 对 $(y,H,V)$ 的权为 $(1,2,3)$，总权六。
乘以 $(\sigma^{-1},\sigma^{-2},\sigma^{-3})$ 保持临界性。
因此可规范 $P_y=f_{s,t}$，置 $\eta=4v/\sigma^3$。
由 (2.2)、(2.6)，
$$
w_{s,t}:=\frac{k_s^3}{f_{s,t}}
=-\Delta_s^3q_s^2\Delta_t
\tag{3.1}
$$
是二元十次多项式，且仍被 $\Delta_s^3$ 整除。
原矩阵 (1.1) 满足
$$
\det J_2=-64701092257700249600\ne0.
\tag{3.2}
$$
于是 (2.5) 给全部十一条二阶矩的唯一值
$$
\boxed{
y=K^{-1}[f_{s,t}],\qquad
H_m=X_m+\eta Y_m,\quad
X=\tfrac16J_2^{-1}[f_{s,t}^2],\quad
Y=\tfrac16J_2^{-1}[w_{s,t}],\qquad
V=\tfrac\eta4u(s)^{\otimes3}.
}
\tag{3.3}
$$
因为 $f_{s,t}$ 是非零多项式，(2.5) 可在多项式整环中取消它；
此处没有把在某些 $x$ 上为零的数值当作可逆元。
反向代回即得全部十六条最高方程。

由 $f_{s,t}(s)=w_{s,t}(s)=0$，
$$
P_y(s)=G_H(s)=0.
$$
故原 (1.4)、(1.5) 的三阶贡献确有
$$
V(p,p,\cdot)=0,\qquad V:(KHK)=0,\qquad V_p=0.
\tag{3.4}
$$
完整低梯度于是恰是
$$
\Gamma=(F^2-2b_0+2\tau_2)y-4FHp+8HKHp,
$$
$$
N=Fyy^{\mathsf T}-2FH-2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH.
\tag{3.5}
$$
下文始终从 (3.3)、(3.5) 构造全部六个 $\Gamma_i$ 和十一个 $n_m$；
仅取其中三个作为排除所需的必要条件，绝未以它们替换完整临界性。

## 4. 有限图中的精确消元门

有限 $s,t$ 时定义不带任何参数分母的商式
$$
d_{s,t}(z)=(q_1+q_2t+q_3t^2)+(q_2+q_3t)z+q_3z^2.
\tag{4.1}
$$
它满足恒等式
$$
q_s(z)=(z-t)d_{s,t}(z)+q_s(t).
\tag{4.2}
$$
在整个 $\mathbb A^2_{s,t}$ 上先取
$$
f=(z-s)^3d_{s,t}(z),\qquad
w=-(z-s)^3q_s(z)^2(z-t),
\tag{4.3}
$$
再按 (3.3) 构造 $y,H,V$。原最高方程的残差准确是
$$
f^3-6fG_H+\eta k_s^3
=-\eta(z-s)^6q_s(z)^2q_s(t).
\tag{4.4}
$$
因此在原约束 $q_s(t)=0$ 上，(4.3) 与全部原最高方程准确相同。

写 $n_i=A_i\eta^2+B_i\eta+C_i$。由 (1.1)、(3.3)、(3.5) 可直接确定
$A_i,B_i,C_i\in\mathbb Q[s,t]$。精确展开给
$$
\deg_s[\eta^j]n_i\le24-3j,\qquad
\deg_t[\eta^j]n_i\le8-3j\quad(j=0,1,2).
\tag{4.5}
$$
对形式二次多项式 $a=a_2\eta^2+a_1\eta+a_0$、
$b=b_2\eta^2+b_1\eta+b_0$，定义固定四阶 Sylvester 行列式
$$
\mathscr R_2(a,b)
=(a_2b_0-a_0b_2)^2
 -(a_2b_1-a_1b_2)(a_1b_0-a_0b_1).
\tag{4.6}
$$
若 $a,b$ 有共同有限根，则 (4.6) 为零；即使首项特殊化后消失，这个必要性仍然成立。
令
$$
R_{01}=\mathscr R_2(n_0,n_1),\qquad
R_{02}=\mathscr R_2(n_0,n_2),
$$
$$
A(s)=\operatorname{Res}_t(q_s(t),R_{01}(s,t)),\qquad
B(s)=\operatorname{Res}_t(q_s(t),R_{02}(s,t)).
\tag{4.7}
$$
它们均为由本文有限公式完全确定的有理数多项式。
任一有限图完整临界点必使 $A(s)=B(s)=0$。
这里 $t$ 的结式先在 $\mathbb Q[s]$ 上计算；
即使特殊 $s$ 使 $q_s(t)$ 降次，存在共同有限 $t$ 根仍使这个固定 Sylvester 行列式为零。

已执行的原有理数源给如下完整恒等式和非零门：

| 对象 | 精确值或结论 |
|---|---|
| $\deg_tR_{01},\deg_tR_{02}$ | 均为 $20$ |
| $\deg A,\deg B$ | 均为 $248$ |
| 两者共同的明确因子 $D(s)$ | $s^{24}(s-2)^8(s+6)^8(s+1)^{24}$ |
| $A_0=A/D$、$B_0=B/D$ | 在 $\mathbb Q[s]$ 中除法余式均为零，次数均为 $184$ |
| 原有理数系数的模 $1009$ 可约性 | 每个分母均为 $1009$ 的单位，两首项也非零 |
| 完整 $368\times368$ Sylvester 行列式 | $\det\operatorname{Sylv}(\bar A_0,\bar B_0)=774\pmod{1009}$ |

为明确这个有限计算如何构成特征零证明，取
$\mathbb Z_{(1009)}=\{a/b:1009\nmid b\}\subset\mathbb Q$。
上表保证 $A_0,B_0$ 及固定 Sylvester 矩阵均定义于这个环。
其行列式的模 $1009$ 像为 $774\ne0$，故有理数行列式非零。
因此 $A_0,B_0$ 在 $\overline{\mathbb Q}$，从而在 $\mathbb C$ 中没有共同根。
这里没有把某个有限域上的无解性未经提升地当作复数无解。
又因 $A=DA_0,B=DB_0$，所有完整临界点的有限 $s$ 必满足
$$
s\in\{0,2,-6,-1\}.
\tag{4.8}
$$
所有整除均在 $\mathbb Q[s]$ 完成，非零行列式使用完整矩阵，未作抽样或截断。

## 5. 四个有限例外纤维全部返回原方程

由原 (2.3) 有准确因式分解
$$
\begin{array}{c|c|c|c}
s&q_s(t)&q_{\rm rem}(t)&\deg_t R_{01}(s,t)\\\hline
0&t^2(t-5)&t-5&20\\
2&(t-2)(3t^2-17t+6)&3t^2-17t+6&20\\
-6&(t+6)(-5t^2-65t-66)&-5t^2-65t-66&20\\
-1&-5t^2-26t-6&-5t^2-26t-6&12
\end{array}
\tag{5.1}
$$
对每一行，从同一原 $R_{01}$ 先特殊化，再按上表的**真实次数**计算
$$
c_s=\operatorname{Res}_t\bigl(q_{\rm rem}(t),R_{01}(s,t)\bigr)\in\mathbb Q.
\tag{5.2}
$$
原源分别核验四个 $c_s$ 的分母均为 $1009$ 单位，并给
$$
(c_0,c_2,c_{-6},c_{-1})\equiv(686,568,864,483)\pmod{1009}.
\tag{5.2a}
$$
因此它们在 $\mathbb Q$ 中均非零，两个相应多项式没有共同复根。
这就排除全部 $q_{\rm rem}$ 根；并非仅排某一个数值近似根。

所以 $s=-1$ 的整个有限纤维为空，另三个纤维只能有
$$
(s,t)=(0,0),(2,2),(-6,-6).
\tag{5.3}
$$
其中 $s=0,t=0$ 的重数二已经保留；没有除去它。
尤其 $s=-1$ 使用二次的原 $q_{-1}$ 和十二次的原 $R_{01}(-1,t)$，
不能把一般纤维的次数直接沿用至这里。

## 6. 射影无穷远的全部三种组合

齐次 (2.3) 给 $q_\infty(a,b)=a^2(a+b)$，故 $s=\infty$ 时只能
$t=-1$ 或 $t=\infty$；又 $q_s(\infty)=0$ 在有限 $s$ 下恰是 $s=-1$。
因此未被有限图覆盖的组合正好是
$$
(\infty,-1),\quad(-1,\infty),\quad(\infty,\infty).
\tag{6.1}
$$
没有第四种边界。

对前两组，直接取原齐次公式 (3.1)、(3.3)，其仿射多项式为

| $(s,t)$ | $u(s)$ | $f(1,z)$ | $w(1,z)$ |
|---|---|---|---|
| $(\infty,-1)$ | $e_5$ | $-1$ | $(1+z)^3$ |
| $(-1,\infty)$ | $(1,-1,1,-1,1,-1)^{\mathsf T}$ | $(1+z)^3h(z)$ | $(1+z)^3h(z)^2$ |

这里 $h(z)=5z^2+26z+6$。表中的 $f,w$ 始终解释为五次、十次齐次式的完整系数；
比如第一行的 $f$ 是 $-a^5$，绝不把其仿射次数零误当作少掉一支。
两行直接满足原最高方程。

分别重建 (3.5) 的 $n_0(\eta),n_1(\eta)$。
原源核验它们均为二次式、分母均为 $1009$ 单位，
且它们的完整四阶 Sylvester 行列式依表顺序为
$$
462,\quad85\pmod{1009},
$$
均非零。
与 §4 相同的局部化提升给特征零非零结式，故不存在共同有限 $\eta$ 根。
因此 (6.1) 的前两组全为空，包含 $\eta=0$ 及所有非零 $\eta$。

最后一组使用
$$
f_\infty=a^4(a+b)=-k_\infty,\qquad
w_\infty=-a^8(a+b)^2=-k_\infty^2.
\tag{6.2}
$$
它属于下一节的同点族。

## 7. 存活族的完整临界性及 Bell 零性

在 (5.3) 中 $s=t$，由 (2.2)、(2.6) 得
$$
f_{s,s}=\Delta_s^2q_s=-k_s,\qquad w_{s,s}=-k_s^2.
\tag{7.1}
$$
无穷远 (6.2) 是同一齐次身份。由 (3.3)，
$K^{-1}[-k_s]=-u(s)$，而 $J_2[u(s)^{\otimes2}]$ 的系数列正是 $[k_s^2]$。
故所有存活族恰为 (2.7)；没有剩余自由二阶矩。

现直接证明其完整临界性。记 $u=u(s)$，则 $u^{\mathsf T}Ku=0$；
$y=-u$、$H=(1-\eta)u u^{\mathsf T}/6$ 给
$$
F=0,\quad Hp=0,\quad HKH=0,\quad (KH)^2=0.
$$
所以 (1.4)、(1.5) 的全部低梯度均为零。
另一方面，$P_y=-k_s$、$G_H=(1-\eta)k_s^2/6$，于是
$$
P_y^3-6P_yG_H+\eta k_s^3
=\{-1+(1-\eta)+\eta\}k_s^3=0.
$$
全部十六条最高梯度也为零。

完整第三普通矩是
$$
T_3=y^{\otimes3}-2\operatorname{Sym}_{\Sigma}(y\otimes H)+4V,
$$
其中 $\operatorname{Sym}_{\Sigma}$ 为三个位置之和。
代入 (2.7) 给
$$
T_3=-u^{\otimes3}+(1-\eta)u^{\otimes3}+\eta u^{\otimes3}=0.
\tag{7.2}
$$
因此对任意 $r\in\mathbb C^6$，完整匹配 Bell 立方
$$
S_r=(r\cdot y)^3-6(r\cdot y)r^{\mathsf T}Hr+4V(r,r,r)
=T_3(r,r,r)
$$
均为零。这是完整三阶张量的零性，强于只核三个指定匹配方向。
退回原尺度后，所有张量项同乘 $\sigma^3$，故零性不变。
定理证明完毕。

## 8. 原计算身份与可复核有限证书

证明源为
[`2026-11-20-r150-rank-one-v-three-plus-one-plus-one-classification-b2a9.py`](../notes/2026-11-20-r150-rank-one-v-three-plus-one-plus-one-classification-b2a9.py)。
其 SHA-256 为
`914f0d8857394ffa16b6e45b56c1ce39c4d94c82e14fff5144a686d9ecbe489d`。

完整成功执行是
[run44737710336](https://github.com/Rogerhu12/math-research-public/actions/runs/44737710336)，
job136293190180，标签 `rankone_v_three_one_one`；触发提交
`2b27f6da9af4b7e80ec9e94d75d10b504e34c7aa`。
原回执记 exit0、源内计时1.408915秒、外层1.474634363000007秒，stdout SHA-256
`e4e117f8f9fb19acf38220ab0ed8323286cade318ad8c35819ef3ee2b0602670`；
完整任务日志 SHA-256 为
`824b3e684ebd71d62cc230a52e2d7f492df7a6bc940c395af1c583cbaa4feda3`。
执行身份保存在
[`2026-11-20-exact-source-run44737710336-b2a9.json`](../notes/2026-11-20-exact-source-run44737710336-b2a9.json)。

源从整数 $K$ 开始重新构造 $J_2,K^{-1},J_2^{-1}$，核验其完整乘积，
重建原十一二阶、六 mean、十六最高方程以及 $s,t,\eta$ 三方向的完整链式法则；
再在 $\mathbb Q$ 上执行 (4.7)、准确除法与全部有限边界结式。
最后只将已明确定义的完整有理数 Sylvester 矩阵约化模1009求非零行列式。
计算没有随机取样、参数插值、有限维截断或未知的有理数恢复。
按根规则不保存可重算展开数组，本文公式、源及运行身份已给出全部输入。

本附录只关闭 (2.6) 这一完整原分支；其他秩一除子型、高秩 $V$、
完整全局 Jacobian 自然幂来源及普通 Hilbert ISP 仍须另外解决。
