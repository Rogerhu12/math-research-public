# R150 附录：两点第三累积量与均值立方系数一致的完整临界分类

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 本文不预设二阶累积量的秩或支撑，完整排除两点第三累积量和均值立方系数一致时偏离已知零第三矩族的所有参数，包括无穷远。随后从原最高方程推出一个准确推论：两物理极线的公共除子次数至多一时，整个“均值在第三累积量支撑内”的临界层都属于该零第三矩族。次数至少二时仍保留明确的公共因子吸收例外。

后续：[全部两点内均值分类](./R150-appendix-rank-two-reduced-third-cumulant-inside-mean-complete-classification.md)已排除本文保留的所有公共因子吸收例外；本文原低梯度证明与执行身份不变。

## 1. 原对象与准确结论

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
二、三阶累积量是原 Hankel 张量
$$
H_{ij}=H_{i+j},\qquad V_{ijk}=V_{i+j+k}.
$$
完整普通第三矩为
$$
T_3(r)=(y^{\mathsf T}r)^3-6(y^{\mathsf T}r)(r^{\mathsf T}Hr)+4V(r,r,r).
\tag{1.1}
$$
沿用[完整原第三矩展开](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)，记
$$
F=\tfrac12y^{\mathsf T}Ky,\quad p=Ky,\quad
P(z)=p^{\mathsf T}u(1,z),\quad G(z)=u(1,z)^{\mathsf T}KHK u(1,z).
$$
令 $J_d$ 为二元核 $k(z,w)=u(1,z)^{\mathsf T}Ku(1,w)$ 的 $d$ 次幂的完整系数矩阵。原多项式是
$$
\mathcal Q_3=G_6+4[P^3-6PG]^{\mathsf T}V+8V^{\mathsf T}J_3V,
\tag{1.2}
$$
其中方括号表示完整齐次系数，
$$
G_6=F^3-6F\,p^{\mathsf T}Hp
 +6F\operatorname{tr}((KH)^2)
 +12p^{\mathsf T}HKHp-8\operatorname{tr}((KH)^3).
\tag{1.3}
$$
这就是原完整六模式对象，没有删除三阶贡献或改变合并坐标。

取不同的射影点 $s,t$，固定非零代表 $u=u(s),v=u(t)$。

**定理 A。** 假设
$$
y=a u+b v,\qquad
V=c\,u^{\otimes3}+d\,v^{\otimes3},\qquad abcd\ne0,
\qquad cb^3=da^3.
\tag{1.4}
$$
对任意原 Hankel 二阶累积量 $H$，完整临界性恰等价于
$$
\boxed{
c=\frac{a^3}{2},\qquad d=\frac{b^3}{2},\qquad
H=\frac{a^2}{2}uu^{\mathsf T}+\frac{b^2}{2}vv^{\mathsf T}.
}
\tag{1.5}
$$
所有这些点都满足整个 $T_3=0$，故任意方向的完整 Bell 立方均零。

条件 (1.4) 与曲线代表选择无关。两个三次纯张量线性无关，所以 $c,d\ne0$ 的第三张量展平秩确为二。

**推论 B。** 写 $k_s(x)=u(s)^{\mathsf T}Ku(x)$、$k_t(x)=u(t)^{\mathsf T}Ku(x)$。若
$$
\deg\gcd(k_s,k_t)\le1,
\tag{1.6}
$$
则任何完整临界点若有非零两点第三累积量 $V=c u^3+d v^3$、$cd\ne0$，且 $y\in\operatorname{span}\{u,v\}$，都恰为 (1.5)。这里不先假设均值的两个系数非零，也不假设 (1.4) 的系数关系。

## 2. 最高方程唯一决定全部二阶矩

先证定理 A。原权缩放 $(y,H,V)\mapsto(a^{-1}y,a^{-2}H,a^{-3}V)$ 可将 $a$ 置一；将 $b/a$ 仍记为 $b$。置
$$
\tau=c/a^3=d/b_{\rm original}^3,\qquad
\lambda=\frac{1-2\tau}{3}.
$$
于是
$$
y=u+bv,\qquad V=\tau(u^3+b^3v^3),\qquad
b\tau\ne0.
\tag{2.1}
$$
记 $A=k_s,B=k_t$。它们线性无关，因为 $K$ 可逆且两个物理代表线性无关。特别 $P=A+bB$ 不是零多项式。

全部十六条原最高梯度准确是
$$
P^3-6PG+4\tau(A^3+b^3B^3)=0.
\tag{2.2}
$$
利用
$$
A^3+b^3B^3=(A+bB)(A^2-bAB+b^2B^2)
$$
并在多项式整环中取消非零 $P$，得到
$$
G=\frac{1+4\tau}{6}(A^2+b^2B^2)
+\frac{1-2\tau}{3}bAB.
\tag{2.3}
$$
没有除以 $P$ 在某个物理点的值。

从原整数 $K$ 卷积得
$$
\det K=-25600,\qquad
\det J_2=-64701092257700249600.
$$
令唯一原 Hankel 矩阵 $\mathsf B=\mathsf B_{s,t}$ 满足
$$
[(u(x)^{\mathsf T}K\mathsf B K u(x))]=[AB],
\qquad
(\mathsf B_m)_{m=0}^{10}=J_2^{-1}[AB].
\tag{2.4}
$$
(2.3) 因而唯一给出全部原二阶矩
$$
\boxed{
H=(\tfrac12-\lambda)(uu^{\mathsf T}+b^2vv^{\mathsf T})
+\lambda b\,\mathsf B,\qquad
V=\frac{1-3\lambda}{2}(u^3+b^3v^3).
}
\tag{2.5}
$$
$\mathsf B$ 一般没有二点支撑，不能把它替换为对称交叉张量。

直接展开 (1.1) 还给
$$
T_3(r)=6\lambda b\,((u+bv)^{\mathsf T}r)
\left((u^{\mathsf T}r)(v^{\mathsf T}r)-r^{\mathsf T}\mathsf B r\right).
\tag{2.6}
$$
所以 $\lambda\ne0$ 的剩余支确实可以有大于三的本质维数，不能直接套用本质三空间的旧分类。下面由原低梯度排除它。

## 3. 保留全部两点三阶贡献的低梯度

写
$$
h=Hp,\quad b_0=p^{\mathsf T}Hp,\quad
\tau_2=\operatorname{tr}((KH)^2),\quad
P_s=p^{\mathsf T}u,\ P_t=p^{\mathsf T}v,
$$
$$
G_s=u^{\mathsf T}KHK u,\qquad G_t=v^{\mathsf T}KHK v,
\quad c=\tau,\quad d=\tau b^3.
$$
直接从 (1.2) 对完整原坐标求偏导，得到
$$
\begin{aligned}
\Gamma={}&(F^2-2b_0+2\tau_2)y-4FHp+8HKHp\\
&+4c(P_s^2-2G_s)u+4d(P_t^2-2G_t)v,
\end{aligned}
\tag{3.1}
$$
$$
\begin{aligned}
N={}&Fyy^{\mathsf T}-2FH-2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH\\
&+4cP_s uu^{\mathsf T}+4dP_t vv^{\mathsf T},
\end{aligned}
\tag{3.2}
$$
$$
\nabla_y\mathcal Q_3=3K\Gamma,\qquad
\partial_{H_m}\mathcal Q_3=-6n_m,\quad
n_m=[z^m]u(1,z)^{\mathsf T}KNKu(1,z).
\tag{3.3}
$$
因此完整临界点必有全部六个 $\Gamma_i=0$。

源码重建全部六个 mean、十一条二阶和十六条最高方程。为核对三阶线性和二次贡献，它还保留
$$
\mathcal Q_3
=G_6+4c(P_s^3-6P_sG_s)+4d(P_t^3-6P_tG_t)
+16cd\,k(s,t)^3.
\tag{3.4}
$$
在 (2.5) 的最高解上，该式准确等于 $G_6-16cd\,k(s,t)^3$。对 $s,t,b,\lambda$ 每个参数逐一核验
$$
\partial_\theta\mathcal Q_3
=3(K\Gamma)^{\mathsf T}\partial_\theta y
-6\sum_m n_m\partial_\theta H_m
+4\sum_m[\text{最高式}]_m\partial_\theta V_m.
\tag{3.5}
$$
十六个最高式在构造后准确为零。原三阶贡献一直保留，不能仅对 $G_6$ 求导。

## 4. 有限不同支撑的完整有理数消元

有限图取 $u=(1,s,\ldots,s^5)$、$v=(1,t,\ldots,t^5)$，且 $s\ne t$。把 (2.5) 代入 (3.1)，逐项准确除法给
$$
\Gamma_i=\lambda^2b^2(s-t)^4\{A_i(s,t)+bB_i(s,t)\},
\qquad 0\le i\le5.
\tag{4.1}
$$
这里 $A_i,B_i$ 是由原 $K,J_2^{-1}$ 和 (2.4)、(3.1) 唯一确定的有理数多项式。源码对全部六条核余式为零、$\lambda$ 次数为零以及 $b$ 次数至多一；这不是忽略高次项的展开。

假设 $\lambda\ne0$。由于 $b(s-t)\ne0$，完整 mean 方程给
$$
A_i+bB_i=0.
$$
于是所有二阶子式 $A_iB_j-A_jB_i$ 均零。它们另有交替因子 $s-t$。对
$$
(i,j)=(0,1),(0,2),(1,2),(3,4)
$$
定义
$$
D_{ij}(s,t)=\operatorname{prim}
\left(\frac{A_iB_j-A_jB_i}{s-t}\right),
\tag{4.2}
$$
其中 $\operatorname{prim}$ 先清有理数分母，再除整数内容，最后令 lex 最高系数为正。它只乘非零有理常数。四个准确除法余式均零，四个 $D_{ij}$ 都是 $(16,16)$ 双次数的非零整数多项式。

现在取两个原完整 Sylvester 结式
$$
R_1(s)=\operatorname{Res}_t(D_{01},D_{02}),\qquad
R_2(s)=\operatorname{Res}_t(D_{12},D_{34}).
\tag{4.3}
$$
任一假想有限临界参数 $(s,t)$ 都使 $R_1(s)=R_2(s)=0$。这个必要性在特殊 $s$ 导致某些 $t$ 首项消失时仍成立：对原固定 Sylvester 矩阵特殊化后，已有共同有限根仍使其奇异。未除首项，也未删特殊纤维。

完整准确计算为
$$
\deg R_1=\deg R_2=512,\qquad
\gcd_{\mathbb Q[s]}(R_1,R_2)=1.
\tag{4.4}
$$
此外，以原512次次数构造整个1024阶 Sylvester 矩阵；模1009两个首项仍非零，并实际得到
$$
\boxed{\det\operatorname{Sylv}(R_1,R_2)\equiv802\pmod{1009}.}
\tag{4.5}
$$
这里不是小子块，而是整个1024阶矩阵。

(4.5) 严格给特征零结论。$D_{ij}$ 为显示规则唯一确定的整数多项式，(4.3) 也是整数多项式；源码对所用每个有理数系数仍核分母为1009单位。完整固定行列式因而定义于 $\mathbb Z_{(1009)}$。它的非零约化使原有理数行列式非零，故两个原多项式没有共同复根。这与 (4.3) 的必要性矛盾。

因此所有有限不同 $s,t$ 均有 $\lambda=0$。没有剩余有限例外点或待付降次支。

## 5. 全部射影边界

只须处理 $t=\infty$、$s$ 有限，因为交换两个物理点后重新作非零权缩放覆盖 $s=\infty,t$ 有限；两个点不能同时为 $\infty$。

直接令 $v=e_5$，按原 (2.4)、(2.5)、(3.1) 重建全部对象。没有把有限图最高次项删去后当成新张量。六个原 mean 式准确为
$$
\Gamma_i=\lambda^2b^2\{\widetilde A_i(s)+b\widetilde B_i(s)\}.
\tag{5.1}
$$
若 $\lambda\ne0$，两个原子式
$$
E_{01}=\operatorname{prim}(\widetilde A_0\widetilde B_1-\widetilde A_1\widetilde B_0),
\quad
E_{02}=\operatorname{prim}(\widetilde A_0\widetilde B_2-\widetilde A_2\widetilde B_0)
$$
同时为零。准确次数都是16，QQ gcd 为一；两个首项模1009保次，整个32阶 Sylvester 行列式实际为
$$
\boxed{\det\operatorname{Sylv}(E_{01},E_{02})\equiv78\pmod{1009}.}
\tag{5.2}
$$
同一有理数提升排除所有有限 $s$。至此射影边界完整排除非零 $\lambda$。

## 6. 必要性、充分性与第三矩零性

上述两图给 $\lambda=0$，即 $\tau=1/2$，(2.5) 唯一成为 (1.5)。恢复原非零权缩放，得定理 A 的必要性。

对 (1.5)，完整普通矩生成函数可取
$$
(1+a\,u^{\mathsf T}r)(1+b\,v^{\mathsf T}r).
$$
其次数大于二的普通矩全零；原 $F_0^3$ 的非零物理导数所需普通矩次数至少三。这给全部原临界方程，亦见[已登记的零第三矩完整分类](R150-appendix-nonzero-mean-zero-third-moment-critical-classification.md) §1A、§5。当前源码另外核全部三十三梯度在 $\lambda=0$ 恒等为零。

直接展开 (1.1) 也得 $T_3=0$，或由 (2.6) 立即得到。这里不需要 $u^{\mathsf T}Kv=0$。故定理的必要性、充分性和任意方向 Bell 零性均成立。

## 7. 从最高方程得到整个小公共除子内均值层

现不假设 (1.4) 的立方系数关系，只取
$$
V=c u^3+d v^3,\quad cd\ne0,\qquad y=a u+b v.
$$
写原二元极线
$$
k_s=gG,\qquad k_t=gH,\qquad \gcd(G,H)=1,\quad e=\deg g.
\tag{7.1}
$$
两个极线线性无关，所以 $G,H$ 仍线性无关，且同为正次数 $5-e$。

$y=0$ 不可能：最高方程会使 $c k_s^3+d k_t^3$ 恒零，从而非恒定的有理函数 $k_s/k_t$ 的立方为常数，矛盾。

若 $a=0$ 或 $b=0$，最高整除式立即给 $G\mid g^2$ 或 $H\mid g^2$。特别
$$
5-e\le2e.
\tag{7.2}
$$
所以在 $e\le1$ 时两种情况均不可能，必有 $ab\ne0$。

设 $ab\ne0$，置 $\overline P=aG+bH$。最高方程给准确整除
$$
\overline P\mid g^2(cG^3+dH^3).
\tag{7.3}
$$
由于 $\gcd(\overline P,H)=1$，且模 $\overline P$ 有
$$
a^3(cG^3+dH^3)\equiv(a^3d-b^3c)H^3,
$$
得到完整二分
$$
\boxed{a^3d=b^3c\quad\text{或}\quad \overline P\mid g^2.}
\tag{7.4}
$$
这是包括根重数和无穷远的二元齐次整除，没有取消可能为零的点值。

若 $e\le1$，则 $\deg\overline P=5-e>2e$，第二项不可能。因此必须立方系数一致，定理 A 给 (1.5)。推论 B 证毕。

若 $e\ge2$，(7.4) 的公共因子吸收项保持真实开放；不能把定理 A 无条件改写成所有内均值点的分类。一般均值不在 $\operatorname{span}\{u,v\}$、二重 jet 型秩二 $V$ 及其他高秩层也未由本文处理。

## 8. 当前源码与实际执行身份

[自含原式验证器](../notes/2026-11-26-r150-rank-two-v-aligned-mean-pencil-verify.py)从整数 $K$ 卷积原 $J_2$，准确核逆矩阵，生成全部原最高及低梯度，保全部两点 $V$ 贡献和四参数链式法则。它随后计算 (4.2)–(4.5) 及全部无穷远门。

实际源码 SHA256：
d4f7eb77f0cb49adfe1c1fdbc87f47eab90fddae9b74f0e6659050282273b160。

于2026-11-26在本地 Python 3.12.14、python-flint 0.9.0 实际执行，exit 0；源内用时61.711515938004595秒。有限图的两个512次整式、1024阶门802和无穷远16/16次、32阶门78均完整通过，全部原链式法则和 $\lambda=0$ 的三十三梯度也通过。完整标量回执见[实际执行记录](../notes/2026-11-26-r150-rank-two-v-aligned-mean-pencil-execution.json)。可重算的512次长系数数组不入库。

本稿的新内容是未预设二阶支撑时对非零 $\lambda$ 全支的原式排除，以及 (7.4) 导出的完整 $e\le1$ 内均值结论；已有两原子零第三矩族本身不重新作为新发现。原全局 Bell 自然幂、算子费用桥及普通 Hilbert ISP仍未关闭。

