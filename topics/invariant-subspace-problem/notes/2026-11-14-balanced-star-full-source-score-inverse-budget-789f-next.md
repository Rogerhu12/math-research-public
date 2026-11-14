# 平衡 star 的全源 score 逆预算与真实共同残差

本稿在[完整 Beta–binomial 相位运输](2026-11-14-balanced-star-full-source-beta-binomial-phase-transport-789f-next.md)的同一物理模型中证明一个新的全维矩阵预算。组数、组长和全部独立正权任意；它不是把各方向标量估计拼成矩阵。

记下述真实条件噪声对角矩阵为 \(D\)、组长列为 \(\boldsymbol q\)。准确有
\[
\boxed{
\mathsf G^{-1}
\preceq D^{-1}
-\frac{\boldsymbol q\boldsymbol q^*}
{(Q+2)\mathbb E_\rho[T(1-T)]}.
}
\]
等权情形取等。更重要的是，两边之差给出一个明确的同源协方差残差平方，供后续保完整非交换相位使用。本文不把这条 Loewner 界直接左右乘不同矩阵来冒称相位已闭合。

## 1. 全部量来自同一原概率

取 \(q_i\ge1\)、\(Q=\sum_iq_i\)、\(z_i>0\)，令
\[
L_i(t)=1-t+z_it,\qquad
F(t)=\prod_iL_i(t)^{q_i},\qquad
\rho(t)=F(t)\big/\int_0^1F.
\]
给定 \(T=t\)，独立取
\[
K_i\sim\operatorname{Binomial}(q_i,p_i(t)),\qquad
p_i(t)=\frac{z_it}{L_i(t)},\qquad X_i=K_i/q_i.
\]
记
\[
m=\mathbb EX,\quad n=\mathbf1-m,\quad y=2m-\mathbf1,\quad
\boldsymbol q=(q_i)_i.
\]
完整原相位的共同矩为
\[
\mathsf G=\operatorname{Cov}(X),\qquad
\mathsf H=\mathbb E\left[\frac{1-T}{T}XX^*\right],\qquad
\mathsf L=\mathbb E\left[\frac{T}{1-T}(\mathbf1-X)(\mathbf1-X)^*\right].
\]
这些已经在原稿逐项识别为同一非正交物理源的
\(g,h,\ell\) 除以同一个正标量。实际目标为
\[
\mathsf J=\mathsf H\mathsf G^{-1}\mathsf L-2\mathsf G-yy^*,
\]
\[
\boxed{\mathsf J^*\mathsf L^{-1}\mathsf J\preceq\kappa\mathsf H.} \tag{1.1}
\]

定义
\[
a(t)=t(1-t),\qquad
h_i=\mathbb E_\rho[p_i(T)(1-p_i(T))]>0,
\]
\[
D=\operatorname{diag}(h_i/q_i)>0,\qquad
h=(h_i)_i=D\boldsymbol q.
\]
条件方差分解是
\[
\boxed{\mathsf G=D+\operatorname{Cov}_\rho(p(T)).} \tag{1.2}
\]
这里的 \(D\) 是实际 binomial 噪声，不是可任意选取的对角代理。

## 2. 一次共同 score 的两个精确矩

令
\[
\boxed{
v(t)=\frac{(a(t)F(t))'}{F(t)}
=1+\sum_iq_ip_i(t)-(Q+2)t.
} \tag{2.1}
\]
最后一个等式来自
\[
a(t)(\log F)'(t)=\sum_iq_i(p_i(t)-t).
\]
因 \(F\) 在闭区间严格正且光滑，\(aF\) 在两端为零。直接积分分部给
\[
\mathbb E_\rho v=0.
\]
又 \(a p_i'=p_i(1-p_i)\)，故
\[
\mathbb E_\rho[p_i v]
=\frac{\int p_i(aF)'}{\int F}
=-\mathbb E_\rho[a p_i']
=-h_i.
\]
因此整个共同交叉为
\[
\boxed{\operatorname{Cov}_\rho(p,v)=-h=-D\boldsymbol q.} \tag{2.2}
\]

同样，
\[
\mathbb E_\rho v^2
=\frac{\int v(aF)'}{\int F}
=-\mathbb E_\rho[a v'].
\]
而
\[
v'=\sum_iq_i p_i'-(Q+2),
\]
所以
\[
\boxed{
V:=\operatorname{Var}_\rho(v)
=(Q+2)\mathbb E_\rho a-\sum_iq_i h_i.
} \tag{2.3}
\]
该标量严格正：\(v(0)=1,v(1)=-1\)，连续函数 \(v\) 在严格正密度下不可能方差为零。

置
\[
b=(Q+2)\mathbb E_\rho a.
\]
于是
\[
\boxed{b=\boldsymbol q^*D\boldsymbol q+V
>\boldsymbol q^*D\boldsymbol q.} \tag{2.4}
\]

## 3. 完整协方差下界与逆预算

(2.2) 可以不调用任何外部方差定理，直接完成平方。令
\[
r(T)=p(T)-m+\frac hV\,v(T).
\]
则
\[
\mathbb E_\rho r=0,\qquad \mathbb E_\rho[r\,v]=0,
\]
且
\[
\boxed{
R_0:=\mathbb E_\rho[r r^*]
=\operatorname{Cov}_\rho(p)-\frac{hh^*}{V}\succeq0.
} \tag{3.1}
\]
因此
\[
\boxed{
\mathsf G=G_0+R_0,\qquad
G_0=D+\frac{D\boldsymbol q\boldsymbol q^*D}{V}>0.
} \tag{3.2}
\]
所有项来自同一个 \(\rho\)、同一个 \(p\)、同一个 score。

用有限维 Sherman–Morrison 恒等式及 (2.4)，准确得到
\[
\boxed{
U:=G_0^{-1}
=D^{-1}-\frac{\boldsymbol q\boldsymbol q^*}{b}>0.
} \tag{3.3}
\]
所以
\[
\boxed{
\mathsf G^{-1}\preceq U
=D^{-1}
-\frac{\boldsymbol q\boldsymbol q^*}
{(Q+2)\mathbb E_\rho[T(1-T)]}.
} \tag{3.4}
\]
其中共同秩一扣除项不能删除后又把结论称为相同预算：它正好保留原联合回归中的全局 count 方向。

更精确地，逆之差不是任意正矩阵，而是
\[
\boxed{
R:=U-\mathsf G^{-1}
=
U R_0^{1/2}
\left(I+R_0^{1/2}UR_0^{1/2}\right)^{-1}
R_0^{1/2}U
\succeq0.
} \tag{3.5}
\]
该式不需要 \(R_0\) 可逆。

若把真实残差函数 \(r(T)\) 看作列算子
\[
\mathcal Z:\mathbb C^m\to L^2(\rho),\qquad
(\mathcal Zc)(T)=r(T)^*c,
\]
则 \(R_0=\mathcal Z^*\mathcal Z\)，并且
\[
R=
U\mathcal Z^*
(I+\mathcal ZU\mathcal Z^*)^{-1}
\mathcal ZU. \tag{3.6}
\]
这是同一实际 score 正交化残差的 Gram，明确保留了后续可用的物理来源。

## 4. 等权校准

当所有 \(z_i=1\) 时，\(\rho\) 为均匀密度，\(p_i(T)=T\)，
\[
h_i=\frac16,\qquad D=\operatorname{diag}\frac1{6q_i},
\qquad v(T)=1-2T,\qquad V=\frac13.
\]
因此 \(r(T)=0\)，
\[
\mathsf G=D+\frac1{12}\mathbf1\mathbf1^*,
\]
且 (3.4) 为等式：
\[
\mathsf G^{-1}
=D^{-1}-\frac6{Q+2}\boldsymbol q\boldsymbol q^*.
\]
这对任意组数与组长成立，不只适用于单个选定向量。

## 5. 与原非交换相位的一个合法共同因子化

(3.4) 不允许直接推断
\(\mathsf H\mathsf G^{-1}\mathsf L
\preceq\mathsf H U\mathsf L\)，因为左右因子不同。

不过 (3.5) 给一个保持全部交叉的准确因子化。令
\[
\mathcal W=[\,\mathsf L,\ -\mathsf H\,].
\]
则对任意 \(\kappa\)，原相位块恰为
\[
\begin{pmatrix}
\kappa\mathsf H&\mathsf J^*\\
\mathsf J&\mathsf L
\end{pmatrix}
=
\mathcal P_\kappa+\mathcal W^*R\mathcal W, \tag{5.1}
\]
其中
\[
\boxed{
\mathcal P_\kappa=
\begin{pmatrix}
\kappa\mathsf H-\mathsf L R\mathsf L
&
\mathsf L U\mathsf H-2\mathsf G-yy^*
\\
\mathsf H U\mathsf L-2\mathsf G-yy^*
&
\mathsf L-\mathsf H R\mathsf H
\end{pmatrix}.
} \tag{5.2}
\]
因为 \(R=U-\mathsf G^{-1}\)，右上交叉确实相消回
\(\mathsf L\mathsf G^{-1}\mathsf H-2\mathsf G-yy^*=\mathsf J^*\)。

\(\mathcal W^*R\mathcal W\) 是 (3.5)–(3.6) 的真实共同残差平方。
若今后能在相同源上支付 \(\mathcal P_\kappa\succeq0\)，便足以推出 (1.1)。
本文尚未证明这个剩余块为正，也未分别丢弃其两个对角费用后宣称完成相位预算。

本节共同因子化由并行 boundary 推导并纳入；以上所有矩、残差和非交换次序均在正文完整写出。

