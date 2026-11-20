# R150 附录：秩一第三累积量与同点五重均值极线的完整排除

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 原有理数源已冻结执行，全部原矩控制、完整固定 $160\times160$ Sylvester 门及无穷远的 $4\times4$ 门均通过。本稿排除一个第三累积量非零的指定秩一分支，未声称全局匹配 Bell 证书或普通不变子空间问题已完成。

本文使用原六模式、原物理 Hankel 合并键以及[完整第三矩消元](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md) §§1–5。没有把第三累积量置零；最终结论只排除下面指定的秩一非零第三累积量分支。

## 1. 原齐次记号与待排除分支

令
$$
u(a,b)=(a^5,a^4b,\ldots,b^5)^{\mathsf T},\qquad
K=\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix}.
$$
沿用原
$$
p=Ky,\quad P_y(a,b)=p^{\mathsf T}u(a,b),\quad
H_{ij}=H_{i+j},\quad V_{ijk}=V_{i+j+k}.
$$
原非零三阶 Hankel 张量若一阶展平秩为一，必有
$$
V=v\,u(s)^{\otimes3},\qquad v\ne0,\quad s\in\mathbb P^1.
\tag{1.1}
$$
这里可直接证明，不需要 generic Waring 分解：一阶展平像是一条直线，对称性迫整个张量由该直线的三次幂表示；Hankel 性又迫生成向量的平方矩阵为 Hankel。若首个非零坐标在第 $j$ 位，$1\le j\le4$，反对角相等式 $a_j^2=a_{j-1}a_{j+1}$ 矛盾。首坐标非零时递推为等比数列，首个非零坐标在第 $5$ 位时即曲线的无穷远点。因此 (1.1) 覆盖这个准确的秩一条件。

对 $s=[s_0:s_1]$，记
$$
\Delta_s(a,b)=s_0b-s_1a,\qquad
k_s(a,b)=u(s)^{\mathsf T}Ku(a,b).
$$
曲线在原二次型上，且原二元极线有恒等因子
$$
\Delta_s^2\mid k_s.
\tag{1.2}
$$
本稿的排除命题是：

> 原完整 $\mathcal Q_3$ 临界集上，不存在同时满足 (1.1) 与
> $$
> P_y=\sigma\,\Delta_s^5,\qquad \sigma\ne0
> \tag{1.3}
> $$
> 的点。这里 $s$ 为任意射影点；不排除极线在 $s$ 具有三重或四重根的特殊值，也不排除任何有限的剩余标量参数。

(1.3) 是一般秩一第三累积量的一个分支，不是全部分支。

## 2. 最高方程准确确定本分支的全部参数

令
$$
G_H(a,b)=u(a,b)^{\mathsf T}KHK u(a,b).
$$
原完整第三矩梯度为
$$
P_y^3-6P_yG_H+4v k_s^3=0.
\tag{2.1}
$$
在一般秩一非零情形，(2.1) 已迫 $P_y\ne0$ 且 $P_y\mid k_s^3$。对于本分支 (1.3)，由 (1.2)，
$$
w_s=\frac{k_s^3}{\Delta_s^5}
\tag{2.2}
$$
是二元十次多项式，并且仍被 $\Delta_s$ 整除。这是多项式整除，未局部化于 $\Delta_s$、任何极线剩余因子或任何判别式。

原 $\mathcal Q_3$ 对 $(y,H,V)$ 的权分别为 $1,2,3$，总权为六。因此用非零 $\sigma$ 作原加权缩放保留完整临界性。缩放后置
$$
f_s=\Delta_s^5,\qquad \eta=\frac{4v}{\sigma^3}.
$$
原 $J_2$ 是 $k(z,\zeta)^2$ 的完整 $11\times11$ 系数矩阵，满足
$$
\det J_2=-64701092257700249600\ne0.
$$
若方括号表示完整二元系数列，全部参数只能是
$$
\boxed{
y=K^{-1}[f_s],\quad
X_s=\frac16J_2^{-1}[f_s^2],\quad
Y_s=\frac16J_2^{-1}[w_s],\quad
H=X_s+\eta Y_s,\quad
V=\frac{\eta}{4}u(s)^{\otimes3}.
}
\tag{2.3}
$$
$X_s,Y_s$ 按其十一条系数解释为原 Hankel 矩阵。反过来，(2.3) 对每个 $s,\eta$ 满足全部十六条原最高方程。故使用这组参数没有丢失 (1.1)、(1.3) 下的任何完整临界点。

在有限图 $s=(1,s)$、$(a,b)=(1,z)$，
$$
f_s(z)=(z-s)^5.
$$
其 $z^5$ 系数恒为一；计算 (2.2) 的多项式长除没有参数分母。在无穷远图 $s=(0,1)$，直接使用
$$
f_\infty(a,b)=-a^5,\qquad
k_\infty(a,b)=-a^4(a+b),\qquad
w_\infty(a,b)=a^7(a+b)^3.
\tag{2.4}
$$
其仿射系数分别是 $-1,-1-z,(1+z)^3$。这里始终保留原齐次次数 $5,5,10$，不把仿射次数下降误当成缺失支撑。

## 3. 剩余原低梯度仍完整，且 V 的贡献在本分支上确实为零

仍记
$$
F=\tfrac12y^{\mathsf T}Ky,\quad h=Hp,\quad
b=p^{\mathsf T}Hp,\quad
\tau_j=\operatorname{tr}((KH)^j),\quad
c=p^{\mathsf T}HKHp.
$$
原 Hankel 性给 $\operatorname{tr}(KH)=0$。六条归一化 mean 梯度及十一条归一化二阶梯度分别是
$$
\Gamma=(F^2-2b+2\tau_2)y-4FHp+8HKHp
       +4V(p,p,\cdot)-8V:(KHK),
\tag{3.1}
$$
$$
n_m=[z^m]u(1,z)^{\mathsf T}KNKu(1,z),\qquad
N=Fyy^{\mathsf T}-2FH-2(yh^{\mathsf T}+hy^{\mathsf T})
  +4HKH+4V_p .
\tag{3.2}
$$
准确归一化是
$$
\nabla_y\mathcal Q_3=3K\Gamma,\qquad
\partial_{H_m}\mathcal Q_3=-6n_m.
\tag{3.3}
$$
这些原公式见[完整低梯度](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md) §§2–3；本文不继承该文几何应用中的本质维数假设，(3.1)–(3.3) 是对全部原参数成立的恒等式。

由 $f_s(s)=0$ 与 $\Delta_s\mid w_s$，(2.3) 给
$$
P_y(s)=0,\qquad G_H(s)=0.
$$
故
$$
V(p,p,\cdot)=\frac{\eta}{4}P_y(s)^2u(s)=0,\quad
V:(KHK)=\frac{\eta}{4}G_H(s)u(s)=0,\quad
V_p=\frac{\eta}{4}P_y(s)u(s)u(s)^{\mathsf T}=0.
\tag{3.4}
$$
因此本分支的完整低梯度等于 (3.1)–(3.2) 去掉已严格为零的显示三项后的值。这不是把 $V$ 当成零；(2.3) 中 $V$ 仍一般非零，$H$ 也一般不在前稿 $V=0$ 的图上。

定义
$$
G_6=F^3-6Fb+6F\tau_2+12c-8\tau_3.
$$
在本最高方程族上，原完整 $\mathcal Q_3$ 的值等于 $G_6$。冻结源还独立核验
$$
\partial_\eta G_6=-6\sum_m n_m\,\partial_\eta H_m,
$$
$$
\partial_s G_6=
3(K\Gamma)^{\mathsf T}\partial_s y
-6\sum_m n_m\,\partial_s H_m.
\tag{3.5}
$$
(3.5) 包含全部原低梯度的链式求导控制；不是从限制多项式的两个驻点条件反向替代完整临界性。

## 4. 三个二阶梯度给固定 $160\times160$ 特征零门

在有限 $s$ 图中，$y$ 的 $s$ 次数至多五，$X_s,Y_s$ 的 $s$ 次数至多十，$H$ 对 $\eta$ 是一次式。由 (3.2) 每一项，
$$
n_m(s,\eta)\in\mathbb Q[s,\eta],\qquad
\deg_s n_m\le20,\quad \deg_\eta n_m\le2.
\tag{4.1}
$$
源对全部十一条实际原 $n_m$ 逐一核验这个界；全部六条 $\Gamma_i$ 也构造并核验 $\deg_s\le25,\deg_\eta\le2$。

若
$$
a(\eta)=a_2\eta^2+a_1\eta+a_0,\qquad
b(\eta)=b_2\eta^2+b_1\eta+b_0,
$$
采用固定二次齐次化的四阶 Sylvester 行列式
$$
\mathcal R_2(a,b)
=(a_2b_0-a_0b_2)^2
 -(a_2b_1-a_1b_2)(a_1b_0-a_0b_1).
\tag{4.2}
$$
即使某个二次首项在特殊 $s$ 变为零，只要 $a,b$ 有同一个有限 $\eta$ 根，(4.2) 仍为零；因此没有借助“首项非零”的 generic 限制。

置
$$
R_{01}(s)=\mathcal R_2(n_0,n_1),\qquad
R_{02}(s)=\mathcal R_2(n_0,n_2).
$$
由 (4.1)–(4.2)，两者的准确先验 $s$ 次数界为八十。源先在 $\mathbb Q$ 上构造它们，核验全部有理系数分母在 $103$ 处为单位，再核验两个有理多项式及其模 $103$ 约化的实际次数都等于八十。

取固定 $160\times160$ 矩阵 $\mathsf S$：行按 $s^0,\ldots,s^{159}$；前八十列为 $s^jR_{01}$，后八十列为 $s^jR_{02}$，其中 $0\le j<80$。冻结源已验证
$$
\det(\mathsf S\bmod103)\ne0.
\tag{4.3}
$$
因为矩阵的全部有理分母为 $103$ 单位，(4.3) 严格推出原有理矩阵 $\det\mathsf S\ne0$。这是一个固定有限矩阵的特征零正证书。

若某个复 $s_*$ 同时使 $R_{01},R_{02}$ 为零，则非零行向量
$$
(1,s_*,\ldots,s_*^{159})
$$
湮灭 $\mathsf S$，与其可逆性矛盾。故二者没有共同复根。一个原完整临界点必须同时满足 $n_0=n_1=n_2=0$，进而使两个 resultant 同时为零，故有限 $s$ 图中无此临界点。

这里没有使用“模某素数未找到点”作推理，也没有把一个可能降次的模 gcd 当成特征零证据。原有理实际次数、模首项保留、全部单位分母和完整固定维数行列式都是证书的组成部分。

## 5. 无穷远图单独关闭

使用 (2.4) 在原 $\mathbb Q$ 上构造 $y,X_\infty,Y_\infty,H,V$。原最高式、(3.4)、全部十七条低梯度仍逐项保留。

此时 $n_0,n_1$ 是 $\eta$ 的有理二次式。源已验证其完整 $4\times4$ Sylvester 行列式在模 $103$ 为非零，且直接公式 (4.2) 与该矩阵的结果一致。分母单位门同样涵盖这一图。所以它们在复数中没有共同根，排除全部有限 $\eta$。

有限 $s$ 与 $s=\infty$ 覆盖全部 $\mathbb P^1$，从而完成 §1 命题。原 $\eta\ne0$ 对应非零 $V$；证书实际还排除了这一指定参数族内的 $\eta=0$，但不据此对一般 $V=0$ 临界点作空性结论。

## 6. 冻结源码与成功执行证据

[冻结验证源码](../notes/2026-11-20-r150-rank-one-v-quintuple-at-own-point-exclusion-b2a9.py)在 GitHub Actions [run 44736004677](https://github.com/Rogerhu12/math-research-public/actions/runs/44736004677)、job $136287438240$ 中，以标签 $\texttt{rankone_v_quintuple}$ 成功执行并以 exit code $0$ 结束。触发提交为
$$
\texttt{88de2e120c5c0272b67cd988bfa97580cbcab738}.
$$
实际运行时间 $1.90793$ 秒，峰值 RSS 为 $39736$ KiB。固定上限为 wall $180$ 秒、内存 $1024$ MiB。

原源核验全部 $11+6$ 低梯度、全部 $16$ 最高式、原 $K,J_2$ 及有理逆的全部条目、两个原完整链式求导，以及 $1897$ 个构造系数在 $103$ 处的单位分母。实际记录给
$$
\deg_{\mathbb Q}R_{01}=\deg_{\mathbb Q}R_{02}
=\deg_{\mathbb F_{103}}\overline R_{01}
=\deg_{\mathbb F_{103}}\overline R_{02}=80,
$$
$$
\boxed{\det\overline{\mathsf S}=27\ne0,\qquad
       \det\overline{\mathsf S}_\infty=77\ne0
       \quad(\bmod103).}
\tag{6.1}
$$
两项都是完整固定维数的行列式，不是截断矩阵或抽样。

可复核 SHA-256 记录如下：

| 对象 | SHA-256 |
|---|---|
| 冻结源码 | $\texttt{9fc5376eb3323a4b1ce5bd8556fbc41e9f5d00b916d0eddb13fd0fa9f4e8de13}$ |
| 有限图全部十七条原低梯度 | $\texttt{1083ee69cfae6f55dd16c7aa10adc29fbf13c4a3954c36bfef4994f0e264b8b2}$ |
| 有限图两个原 Hankel 头 | $\texttt{5fcc8561e942af926a68922748bfb9d49ab147c26ff6a1b69db44d8445e6cf05}$ |
| 两个有理 resultant | $\texttt{49a73001c7e6f64e8a6735e30b55d5e4fe0b602ca83c7c8797d03dedbadc0209}$ |
| 完整 $160\times160$ 模 Sylvester 矩阵 | $\texttt{c9d2280204d889b84409b2ac3350539bc73fd3fca88282702a9b5963d5cc4809}$ |
| 无穷远全部十七条原低梯度 | $\texttt{36c65641c3ab78315e3788cd535fbd689710b8d353ff95f1d96f10d40f74a5da}$ |
| 无穷远有理 resultant | $\texttt{4d3a9049c26cea04a76e0f5a581148a72d6b197a97572af8e4e679a012008469}$ |
| 本成功标签完整 stdout | $\texttt{688140b9a50fa7252d161ee012841f21f383efb86735a9bda58b0aba8951526b}$ |

源码只输出小 JSON 记录，没有把矩阵、系数数组或中间检查点写入仓库。该 job 内另一个独立标签的超时不改变本标签的实际 exit code $0$、完整核验输出和 (6.1)。

## 7. 严格范围

本稿只处理 $V$ 一阶展平秩一且 $P_y$ 是 $\Delta_s^5$ 的分支。一般秩一 $V$ 仍只有必要整除 $P_y\mid k_s^3$；其它根重数分配不由本稿关闭。第三累积量秩更高、完整匹配 Bell 自然幂的全局 Jacobian 归属，以及原普通不变子空间目标也不由这一有限分支排除解决。
