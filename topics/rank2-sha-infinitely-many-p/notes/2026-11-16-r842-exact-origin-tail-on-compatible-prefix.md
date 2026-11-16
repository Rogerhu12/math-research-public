# R842 续注：原十三行前缀后的准确原点补偿行

日期：2026-11-16。**状态：以下原点系数式、同一兼容对的全边界表达与原 $M/J$ 长度区别已证明；指定总类在 $\mathscr W_T$ 或真实三长核上的非零仍未证明。**

接
[完整边界读取](2026-11-16-r842-actual-boundary-rows-and-horizontal-thickenings.md)
第1、2、8节。
那里已保 $r\le11$ 时不能删除的原点补偿。
本注将其写成同一实际来源的固定有限行，不把未受原短矩阵读取的余尾另赋为零。

## 1. 同一个真实兼容对

保持 R842/R836 的原曲线、十九角格与返回
$$
C=(F=0),\quad P=(0,1),\quad
\mathcal E=Y\partial_Y,\quad
e=\mathcal EF,\quad f_2=\mathcal E^2F,\quad e(P)\ne0,
$$
$$
R=qt^rG,\qquad G\in\mathcal H_3,\qquad
V_0=G|_C,\quad V_1=(\mathcal EG)|_C.
\tag{1}
$$
取 $V_0\in\mathscr W_T$，$V_1\in\mathscr V_T$ 是其唯一兼容伴随。
于是沿原曲线支 $Y=\psi(t)$，
$$
\boxed{
V_i=t^T v_i(t),\qquad v_i\in k[[t]],\qquad
T=T_M=s-r-13,\quad p=6s-1.
}
\tag{2}
$$
这里 $V_1$ 不是任意局部 normal。
两值须已经由同一个原 $G$ 实现；
全部实现只差 $F^2\mathcal H_1$。

所有偏导仍保持原 $Y$ 不变。沿 $C$ 准确有
$$
dY=-\frac{YF_t}{e}\,dt,\qquad
de=\left(\mathcal EF_t-\frac{f_2F_t}{e}\right)dt.
\tag{3}
$$
原 $q$ 的各 Euler 项完整保留，尤其 $q=Y\widetilde q$
不允许改写成 $\mathcal Eq=q$。

## 2. 全部 $W'$ 项精确相消

保持完整的原权
$$
W=t^{r+1-s}(1-t)^{3s},\qquad
c_s=\frac{3(-1)^s}{17}.
$$
完整边界注定义
$$
\mathcal D_R=c_s(\mathcal ER)|_C
\left[-d(WF_t/e)+(W'F_t+WF_{tt})dt/e\right].
\tag{4}
$$
定义同一个原曲线上的有理函数
$$
\boxed{
K_F=
\left(
\frac{2F_t\mathcal EF_t}{e^2}
-\frac{F_t^2f_2}{e^3}
\right)\bigg|_C.
}
\tag{5}
$$
它在 $P$ 正则；不假设其常数项为单位。

**引理。** 在原函数域上有完整恒等式
$$
\boxed{
\mathcal D_R
=c_s\,t^{2r+1-s}(1-t)^{3s}
K_F\left(q|_C\,V_1+(\mathcal Eq)|_C\,V_0\right)dt.
}
\tag{6}
$$

证明。由 (3)，
$$
d(F_t/e)
=\left[
\frac{F_{tt}}e
-\frac{2F_t\mathcal EF_t}{e^2}
+\frac{F_t^2f_2}{e^3}
\right]dt.
$$
代入 (4)，两个 $W'$ 项及两个 $WF_{tt}/e$ 项分别准确相消，
只剩 $WK_Fdt$。
又原乘积法则给
$$
(\mathcal ER)|_C
=t^r\left(q|_C\,V_1+(\mathcal Eq)|_C\,V_0\right),
$$
得到 (6)。此过程没有在任何分歧点把 $e$ 当成单位；
(6) 在这些点仍是同一个亚纯微分恒等式。
只有读取 $P$ 时使用已付的 $e(P)\ne0$。证毕。

式 (6) 同时表明，改变实现
$G\mapsto G+F^2L$ 不改变整条 $\mathcal D_R$：
它的两个全局输入 $V_0,V_1$ 都不变。
因而下述每个边界算子都继续来自同一对，而不是另选其法向提升。

## 3. 原 $M$ 窗口的有限余尾

置
$$
J_V(t)=K_F(t)
\left(q(t,\psi(t))v_1(t)
+(\mathcal Eq)(t,\psi(t))v_0(t)\right)\in k[[t]].
\tag{7}
$$
由 (2)、(6)，准确有
$$
\mathcal D_R=c_s\,t^{r-12}(1-t)^{3s}J_V(t)\,dt.
\tag{8}
$$
因此
$$
\operatorname{Res}_P\mathcal D_R
=c_s[t^{11-r}](1-t)^{3s}J_V(t)
\quad(1\le r\le11),
$$
而 $r\ge12$ 时为零。

这里仅需 $0,\ldots,11-r$ 阶，最高为10，严格小于 $p$。
在这些阶上，所有 $j!$ 为单位；
由 $3s=(p+1)/2\equiv1/2\pmod p$，
二项系数逐项给
$$
(1-t)^{3s}\equiv(1-t)^{1/2}\pmod{t^{12-r}}.
$$
所以得到准确原短行
$$
\boxed{
\mathcal P_r(V_0)=
\begin{cases}
\displaystyle
c_s[t^{11-r}]
(1-t)^{1/2}K_F
\bigl(q|_C\,v_1+(\mathcal Eq)|_C\,v_0\bigr),
&1\le r\le11,\\[4pt]
0,&r\ge12.
\end{cases}
}
\tag{9}
$$
平方根取常数项1的形式支，只作为这段固定短系数的记号。
**原全局 $W$ 没有被替换为分数幂。**

式 (9) 最多读取每个 $v_i$ 的 $12-r$ 个系数。
特别原 $r=2$ 读取 $[t^9]$，每个 $v_i$ 只需十个实际余尾系数，
再按 (7) 合成一条行。
它们由同一个全局 $G$ 决定；
原矩阵只要求 $V_i$ 的 $<T$ 前缀消失，
没有要求这些 $T$ 阶以后的系数也消失。
本注没有把这条边界读数作为免费新增的物理输出。

## 4. 整个剩余类的原点部分现已完全明确

令 $\omega_1\in H^0(C,\omega_CN^{-1}(TP))$
为第一层注的同一真实全局延拓。
在当前 $\mathscr W_T$ 上，$V_1\in t^T k[[t]]$，
而 $e(P)$ 为单位，故
$$
\boxed{\operatorname{Res}_P(V_1\omega_1/e^2)=0.}
\tag{10}
$$
这不适用于只有 $V_0\in\mathscr V_T$、尚未满足兼容方程的任意提升。

记 $\mathfrak B_{\mathcal D}(R)$ 为 (4) 在 $P$ 与原非固定分歧开集之外的
全部分支残数和，包括两个水平、六个底纤维、十九角和所有 conductor／剩余域迹。
完整边界注的 (10) 于是化为
$$
\boxed{
[b_0](V_0)
=-\mathfrak B_{\mathcal D}(qt^rG)-\mathcal P_r(V_0),
\qquad V_0\in\mathscr W_T.
}
\tag{11}
$$
(6) 说明右边全部使用同一对 $(V_0,V_1)$。
负水平原 Jacobian 纤维商、正水平全 trace 及原固定纤维的已付消去
可以代入同一个 (11)，但不能逐块另选来源。

若使用负水平的全局 mask 将其有限行移到正水平和底无穷远，
该 mask 在 $P$ 正则：其底分母 $t-t_Q$ 为单位，
且原对偶化生成元 $dY/F_t=-dt/F_Y$ 因 $e(P)\ne0$ 而正则。
因此 (9) 在这次合法全局转移后逐字不变。
它仍可与那些完整边界补偿，不能单独凭某个系数非零收尾。

最后明确原 $J/M$ 区别：
若另用相对长窗口 $T_J=s-r$，
(6) 中同样的归一 $V_i=t^{T_J}v_i$ 给 $t^{r+1}$，
所以其原点残数确实为零。
这个结论不能移给 (2) 的原 $M$：
恢复原 $w^{13}U_0$ 后，指数准确变为 $r-12$，
差出的 (9) 正是必须继续保留的原点行。
原单位下三角逆、charge 四十、$P_{134}/U_0$ 和全部 native 行仍按 R836/R842 运输，
本注没有重新选择 gauge。

(11) 仍是指定类的实际有限读取，不是其非零证明。
更小三长核、唯一第二值／同一个 $cF^3$ 尾、第四短行和整个
$\mathcal W_D$ 的其它列全部保持。
