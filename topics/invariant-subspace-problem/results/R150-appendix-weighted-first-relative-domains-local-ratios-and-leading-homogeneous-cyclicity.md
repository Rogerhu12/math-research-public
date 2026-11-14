# R150 附录：加权 first 的实际相对域、局部有界比率与最高齐次非零的多模式循环性

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf / normal_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：已证明。根与 normal 完整核验相对图估计、范数尾收敛、局部单位和原 Bell 最大图；主行加权增强另经 kernel/normal 交叉核验。
完整证明稿。主新增是实际系数条件产生的域包含与范数比率演算；
空谱 first 的单位最高系数多项式机制沿用 R134/R176，不重复登记为抽象新定理。

## 1. 准确范围与主结论

固定
$$
a_j\ge0,\qquad a\in\ell^2\setminus\ell^1,\qquad
X=X_{\sum_j a_j\chi_j},\qquad L=X^{-1}.
\tag{1.1}
$$
R128/R134 给 $X$ 的真实空谱实现、$L\in A'$ 有界且拟幂零。

对复行 $d$，定义
$$
\|d\|_a^2=\sum_{\{j:a_j>0\}}\frac{|d_j|^2}{a_j}.
\tag{1.2}
$$
本稿使用的加权行还要求 $d_j=0$ 于 $a_j=0$ 的位。
若 (1.2) 有限，则 $d\in\ell^2$，因为 $a$ 有界。
不要求 $d\in\ell^1$，也不要求 $|d_j|/a_j$ 一致有界。

**相对域定理。** 若 $\|d\|_a<\infty$，令 $Y_d=X_{\sum d_j\chi_j}$。
则
$$
\boxed{\operatorname{Dom}X\subseteq\operatorname{Dom}Y_d,}
\tag{1.3}
$$
且 $Y_d$ 相对 $X$ 的界为零。
实际全域有界算子
$$
B_d=Y_dL
\tag{1.4}
$$
满足
$$
\boxed{
B_d=\lim_{n\to\infty}\left(\sum_{j<n}d_jV_j\right)L
\quad\text{按算子范数收敛}.
}
\tag{1.5}
$$
所以若
$$
\mathcal B=\overline{\operatorname{alg}}(I,\mathcal A,L),
$$
则 $B_d\in\mathcal B$。
这个交换 Banach 代数有唯一字符 $\phi$，且
$$
\phi(L)=\phi(B_d)=0.
\tag{1.6}
$$
特别 $B_d$ 真正拟幂零。

下面允许有限多个辅助模式。
设
$$
u_0=u_{0,*}+\sum_j(a_j+d_{0j}+e_{0j})\chi_j,
$$
$$
u_\nu=u_{\nu,*}+\sum_j(\gamma_\nu a_j+d_{\nu j}+e_{\nu j})\chi_j,
\qquad 1\le\nu\le q,
\tag{1.7}
$$
其中 $q<\infty$，所有常数和 $\gamma_\nu$ 均可复，
每个 $e_\nu\in\ell^1(\mathbb C)$，每个 $\|d_\nu\|_a<\infty$（这里包括 $\nu=0$）。
零 $a_j$ 位上的其它系数必须由真正的 $\ell^1$ 余项承担。

令标量多项式 $F(x_0,\ldots,x_q)$ 总次数为 $p\ge1$，
最高齐次部分为 $F_p$。
若
$$
\boxed{F_p(1,\gamma_1,\ldots,\gamma_q)\ne0,}
\tag{1.8}
$$
则对每个 $\lambda\in\mathbb C$、整数 $r\ge1$、
任意复 $\ell^2$ first 指数权 $w$，
$$
\boxed{[F(u_0,\ldots,u_q)-\lambda]^r e^w
\text{ 是实际 }A\text{ 的循环向量}.}
\tag{1.9}
$$
实际上相应完整 Bell 规范闭实现有一个全空间有界逆。

特别取 $q=1$，
$F(x,y)=G(x,y-x^2)$，其中 $G(x,z)$ 对 $z$ 首一 $m$ 次且总次数不超过 $m$。
则 $F_{2m}(x,y)=(-1)^m x^{2m}$，所以 (1.8) 自动成立。
这关闭当前加权复辅助类的全部剪切碰撞和全部固定点态幂。

## 2. 去重和已有实际输入

[R130](R130-quadratic-carry-number-weight-estimates.md) 与
[R207](R207-first-column-norm-commutators-quasidiagonality-and-bounded-branch-cost.md)
已给 Walsh 创建/删除/占据分解及有界真实 carry。
本稿把通常次数改为主行的实际非负权 $a_j$，
由 (1.2) 取得对同一个 $X$ 的相对图估计；
这不是已有按通常次数的 $\ell^2$ 行估计的原结论。

[R201](R201-positive-first-ratio-domain-obstruction-and-full-plane-spectrum.md)
排除了仅凭逐项支配推出一般相对域包含。
本稿增加的 (1.2) 不被该反例满足：
例如 $d_j=\pm a_j$ 的非可和实交替辅助给
$\|d\|_a^2=\sum_j a_j=\infty$。

只使用以下原空间接口：

1. 有限 Walsh 柱是每个实际 first 的图核心。
2. Walsh 基上纯一位算子为创建减删除加两倍占据。
3. 真实差 $V_j-S_j$ 有 $\|V_j-S_j\|\le8\eta_j$。
4. R186 给全部有限混合词、完整普通 Bell 及共同正则核心。
5. $\mathcal A$ 为原快解析闭代数，唯一字符记为 $\chi$。

不把未知闭子空间的通常伴随域或 $C$ 自伴性当作输入。

## 3. 主行加权的纯 first 二次型估计

在 Walsh 基上用 $c_j^+$、$c_j^-$、$n_j$ 分别记创建、删除、占据矩阵。
不同位作用交换，并有
$$
S_j=c_j^+-c_j^-+2n_j,\qquad
[c_j^-,c_j^+]=I-2n_j.
\tag{3.1}
$$
定义非负对角权
$$
N_a\chi_E=\left(\sum_{j\in E}a_j\right)\chi_E.
$$
以下先在有限 Walsh 柱 $f$ 上计算。
置 $K=\|d\|_a$、$g=\|d\|_2$。

向量形式的 Cauchy–Schwarz 给
$$
\left\|\sum_jd_jc_j^-f\right\|^2
\le K^2\sum_j a_j\|c_j^-f\|^2
=K^2\langle N_af,f\rangle.
\tag{3.2}
$$
对 $\bar d$ 同样成立。
令 $D_{\bar d}=\sum_j\bar d_jc_j^-$，其形式伴随为
$\sum_jd_jc_j^+$。
有限部分的局部交换子给
$$
\left\|\sum_jd_jc_j^+f\right\|^2
-\|D_{\bar d}f\|^2
=\sum_j|d_j|^2\langle(I-2n_j)f,f\rangle
\le g^2\|f\|^2.
\tag{3.3}
$$
创建尾在有限柱上按 $\ell^2$ 收敛，因此 (3.3) 的极限合法。

占据项也享有同一半次权。
逐个有限 Walsh 支撑 $E$ 应用标量 Cauchy–Schwarz，
$$
\left|\sum_{j\in E}d_j\right|^2
\le K^2\sum_{j\in E}a_j.
$$
所以
$$
\boxed{\left\|\sum_jd_jn_jf\right\|^2
\le K^2\langle N_af,f\rangle.}
\tag{3.4}
$$
这一步允许 $|d_j|/a_j$ 无界。

由 (3.1)—(3.4)，纯 first $Y_d^0=\sum d_jS_j$ 满足
$$
\boxed{\|Y_d^0f\|\le4K\sqrt{\langle N_af,f\rangle}+g\|f\|.}
\tag{3.5}
$$

## 4. 真实 carry 和主行图范数

置
$$
E_a=\sum_j a_j(V_j-S_j),\qquad
E_d=\sum_j d_j(V_j-S_j),\qquad
\kappa=8\|\eta\|_2.
$$
真实范数绝对收敛给
$$
\|E_a\|\le\kappa\|a\|_2,\qquad
\|E_d\|\le\kappa g.
\tag{4.1}
$$
这些 carry 算子属于 UHF；
这里没有把它们单独说成 $\mathcal A$ 元素。

因 $a_j$ 实非负，纯创建减删除部分的二次型为纯虚数。
因此对有限柱，
$$
\operatorname{Re}\langle Xf,f\rangle
=2\langle N_af,f\rangle+
\operatorname{Re}\langle E_af,f\rangle.
\tag{4.2}
$$
从而
$$
\langle N_af,f\rangle
\le\tfrac12\|Xf\|\|f\|+\tfrac12\|E_a\|\|f\|^2.
$$
把它代入 (3.5)，并加实际 carry $E_d$，得
$$
\boxed{
\|Y_df\|
\le2\sqrt2K\sqrt{\|Xf\|\|f\|}
+\left[2\sqrt2K\sqrt{\|E_a\|}+(1+\kappa)g\right]\|f\|.
}
\tag{4.3}
$$
仅使用原空间二次型，甚至不需要 R161 的通常伴随同域结论。

对任意 $\epsilon>0$，Young 不等式给
$$
\|Y_df\|\le\epsilon\|Xf\|+
\left[\frac{2K^2}{\epsilon}
+2\sqrt2K\sqrt{\|E_a\|}+(1+\kappa)g\right]\|f\|.
\tag{4.4}
$$
取有限柱的 $X$ 图核心逼近 $f\in\operatorname{Dom}X$。
对逼近向量之差使用 (4.4)，可知 $Y_d f_n$ Cauchy。
实际 $Y_d$ 闭，故 $f\in\operatorname{Dom}Y_d$，并且 (4.3)—(4.4) 延到完整 $\operatorname{Dom}X$。
这证明 (1.3) 及相对界零。

## 5. 实际有界比率的范数截断与唯一字符

由 $LH=\operatorname{Dom}X\subseteq\operatorname{Dom}Y_d$，
$B_d=Y_dL$ 在全 $H$ 有定义且闭，因此有界。
它与 $A$ 交换，所以 $B_d\in A'$。

在 (4.3) 中取 $f=Lh$，得到明确界
$$
\boxed{
\|B_d\|
\le2\sqrt2K\sqrt{\|L\|}
+\left[2\sqrt2K\sqrt{\|E_a\|}+(1+\kappa)g\right]\|L\|.
}
\tag{5.1}
$$
对尾行 $d^{(\ge n)}$ 同样成立；其加权范数与普通 $\ell^2$ 范数均趋零。
因此
$$
\|Y_{d^{(\ge n)}}L\|\longrightarrow0.
\tag{5.2}
$$
有限去项是实际闭域等式，故 (5.2) 正好给 (1.5)。
这里的有限系数截断按图的右侧 $L$ 获得了算子范数收敛；
不是引用一般系数截断在任意 first 域向量上收敛。

每个有限 $(\sum_{j<n}d_jV_j)L$ 属于 $\mathcal B$。
$\mathcal B$ 中的任意字符限制到 $\mathcal A$ 必为 $\chi$；
而 $L$ 在 $B(H)$ 中拟幂零，故其在 $\mathcal B$ 中也有谱半径零。
所以每个字符必须把 $L$ 送到0。
$\mathcal A$ 和 $L$ 生成 $\mathcal B$，因而字符唯一。
取 (1.5) 的范数极限得到 $\phi(B_d)=0$。
在交换有单位 Banach 代数中谱由字符值给出，遂有 $\sigma_{\mathcal B}(B_d)=\{0\}$；
全空间算子谱为其子集，故 $B_d$ 在 $B(H)$ 中拟幂零。

若
$$
c=\gamma a+d+e,\qquad e\in\ell^1,\quad\|d\|_a<\infty,
$$
则 $E=X_{\sum e_j\chi_j}\in\mathcal A$ 有界，并有
$$
Y_cL=\gamma I+B_d+EL\in\mathcal B,\qquad
\boxed{\phi(Y_cL)=\gamma.}
\tag{5.3}
$$
这个域等式由有限柱和共同图闭包得到；
它不要求三个自然域交之外存在未经证明的求和规则。

## 6. 全部共同词域准确归到同一个 X

先令 $Y_\nu=X_{\sum(\gamma_\nu a+d_\nu+e_\nu)\chi_j}$，
$B_\nu=Y_\nu L\in\mathcal B$。
由已证域包含，在 $\operatorname{Dom}X$ 上有
$$
\boxed{Y_\nu f=B_\nu Xf.}
\tag{6.1}
$$
因为 $LXf=f$，等式右端正是 $Y_\nu LXf$。
有界 $B_\nu\in A'$ 保持全部自然 $X$ 幂域并作域交换。

归纳得：若 $f\in\operatorname{Dom}X^k$，
则 $X,Y_1,\ldots,Y_q$ 的每个长度至多 $k$ 的有序自然词都在 $f$ 上有定义，
且一个含 $\ell_\nu$ 个 $Y_\nu$、总长度 $\ell$ 的词作用为
$$
\left(\prod_\nu B_\nu^{\ell_\nu}\right)X^\ell f.
\tag{6.2}
$$
反向共同词域包含 $X^k$ 本身，所以准确地
$$
\boxed{
\mathcal D_k(X,Y_1,\ldots,Y_q)=\operatorname{Dom}X^k.
}
\tag{6.3}
$$
所有混合顺序都已支付，没有只验证一种排序。

主行的加权余项也可以保留。置
$$
B_0=I+B_{d_0}\in\mathcal B,\qquad \phi(B_0)=1.
$$
所以 $B_0$ 是实际有界单位。
常数、$\ell^1$ 余项和任意复 first 指数倾斜给实际有界 $\mathcal A$ 项 $H_\nu$；
原 first 在有限柱上准确写为
$$
U_0=B_0X+H_0,\qquad U_\nu=B_\nu X+H_\nu.
\tag{6.4}
$$
$B_0X+H_0=B_0(X+B_0^{-1}H_0)$ 在 $\operatorname{Dom}X$ 上闭，
且其图范数与 $X$ 图范数等价。
因此有限柱的原图闭包正是 (6.4) 的完整主 first，
没有把加权 $d_0$ 误称为有界扰动。

所有系数均与 $X$ 完整域交换。
正向按 (6.2) 运算，反向使用实际式
$X=B_0^{-1}(U_0-H_0)$ 作有限自然词归纳，
得到 $U_0,\ldots,U_q$ 的长度至多 $k$ 共同词域也准确为
$\operatorname{Dom}X^k$。
可以把 $X$ 同时保留在 R186 共同正则器的坐标中。

## 7. 完整多模式 Bell 的实际最高系数

以原始各行 (1.7) 和原指定 $w$ 构造完整普通混合 Bell 多项式。
所有高阶混合 cumulant 和 Bell 系数按 R186 均为真实 $\mathcal A$ 元素；
它们没有被改成去掉 $\ell^1$ 或加权余项后的其它行的系数。

对
$$
H(x)=[F(x)-\lambda]^r,\qquad N=pr,
$$
其完整 Bell 多项式只含 $H$ 的有限混合导数。
正阶导数降低普通总次数。
所以最高总次数 $N$ 项准确为 $F_p^r$，
没有任何其它 Bell 项进入该最高次数。

把实际 first 写为
$$
U_0=B_0X+H_0,\qquad U_\nu=B_\nu X+H_\nu
$$
后，在 §6 的完整自然域上得到
$$
\mathcal P(X)=\sum_{k=0}^{N}A_kX^k,\qquad A_k\in\mathcal B,
$$
最高系数为
$$
\boxed{
A_N=F_p(B_0,B_1,\ldots,B_q)^r,\qquad
\phi(A_N)=F_p(1,\gamma_1,\ldots,\gamma_q)^r\ne0.
}
\tag{7.1}
$$
因 $\mathcal B$ 只有一个字符，$A_N$ 是其中的实际有界单位。

令
$$
Q=\mathcal P(X)L^N
=A_N+\sum_{k<N}A_kL^{N-k}\in\mathcal B.
\tag{7.2}
$$
其字符同样非零，所以 $Q$ 也是实际单位。
在 $\operatorname{Dom}X^N$ 上
$$
\mathcal P(X)=QX^N.
$$
右端闭，且
$$
\boxed{\mathcal P(X)^{-1}=L^NQ^{-1}\in\mathcal B.}
\tag{7.3}
$$
这里使用实际单位逆，未除任何仅形式非零的最高系数。

还要把这个闭自然多项式与原 Bell 的 R186 规范最大闭实现识别。
二者在充分深的共同自然域上由 (6.2) 相同。
对原规范图内向量用足深共同正则器幂作图逼近，
$\mathcal P(X)$ 的闭性给一个包含；
对 $\operatorname{Dom}X^N$ 内向量用同一个正则器作 $X^N$ 图逼近，
原规范图的闭性给反向包含。
全部有界系数和正则器都在 $A'$ 中，故这些图逼近同时保持其相应算子像。
因此原规范 Bell 图的完整域确为 $\operatorname{Dom}X^N$，
并具有 (7.3) 的全空间有界逆。

最后，R186 的原指定循环指数向量及混合图核心给
$$
[[F(u_0,\ldots,u_q)-\lambda]^re^w]_A
=\overline{\operatorname{Ran}\mathcal P(X)}=H.
$$
证明 (1.9)。甚至无需把单射再通过未知限制的共轭变成稠密像；
此处原闭实现已经满射。

## 8. 新的非可和复辅助例与保留边界

取
$$
a_j=(j+1)^{-\sigma},\qquad
d_j=\omega_j(j+1)^{-\tau},\qquad|\omega_j|=1,
$$
其中
$$
\frac12<\sigma<1,\qquad \frac{1+\sigma}{2}<\tau\le1.
$$
则 $d\notin\ell^1$，其相位可以完全任意，而
$$
\sum_j\frac{|d_j|^2}{a_j}
=\sum_j(j+1)^{-(2\tau-\sigma)}<\infty.
$$
例如 $\sigma=3/5,\tau=9/10$。
主行的归一化柱尾比在标准幂尾下保持正量级，
其计数比为无穷；此前全实辅助二分并不自动覆盖这些任意复相位。
本稿给出它们的全部剪切类和更一般 (1.8) 的多模式范围。

新结论不是“任意两个 first 都有共同相对域”。
若加权和发散，尤其 $d_j=\pm a_j$，本稿没有由系数大小支配恢复该域包含。
最高齐次方向条件也不能删除：
若 $F_p(1,\gamma_1,\ldots,\gamma_q)=0$，
(7.1) 的最高系数可能落入实际局部根基，本文不将它当单位。
一般复受控同阶辅助、真正切向多项式、独立多慢模和完整 ISP 仍须继续。
