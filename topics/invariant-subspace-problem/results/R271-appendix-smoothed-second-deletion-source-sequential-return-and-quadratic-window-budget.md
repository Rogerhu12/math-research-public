# 平滑二次删除源的顺次 MP 返回与二次窗口费用

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15

## 0. 本文支付的源和未作的替换

保持原连续远尾
$$
D=D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad x\ge1.
$$
令 $\mathcal L,\mathcal T=e^{-x\mathcal L/4}$ 为前述原加权交换发生器及同一个热算子，
$$
\mathcal C_1=[D,\mathcal L^*],\qquad
\mathcal C_2=[D,[D,\mathcal L^*]].
$$
[单调漂移及真 MP 列稿](R271-appendix-monotone-exchange-drift-operator-bound-and-smoothed-second-descent-source.md)已证明
$$
\|\mathcal C_1\|\le4/x^2,\quad
\|\mathcal T\|\le e^{1/2},\quad
\|\mathcal L^*\mathcal T\|<90/x.
\tag{0.1}
$$

本文进一步支付同一明确源的顺次预像返回。它不把原 $D_3=\sum b_i^3E_i$ 换成 $\mathcal C_2$，也不声称实际 $u_Q$ 已经落在下述列像。

## 1. 同一个三阶 jet 列的准确顺次分拆

固定物理远孔层 $p$，取任意
$$
f\in K_p:=\ker D_p,\qquad
y=\mathcal L^*\mathcal Tf.
$$
已经证明
$$
y\in\ker D^3,\qquad
Dy=\mathcal C_1\mathcal Tf,\qquad
D^2y=\mathcal C_2\mathcal Tf.
\tag{1.1}
$$
记 $Q_p=D_p^\dagger$，$\Pi_{1,p}=P_{K_p}$。对任意该层 $y$，
$$
\begin{aligned}
Q_pQ_{p-1}D^2y
&=Q_p(I-\Pi_{1,p-1})Dy\\
&=(I-\Pi_{1,p})y-Q_p\Pi_{1,p-1}Dy.
\end{aligned}
\tag{1.2}
$$
因而 (1.1) 中的同一列满足
$$
\boxed{
Q_pQ_{p-1}\mathcal C_2\mathcal Tf
=(I-\Pi_{1,p})y
-D_p^\dagger\Pi_{1,p-1}\mathcal C_1\mathcal Tf.
}
\tag{1.3}
$$
这里最后一列是完整的 primitive 返回，不能由真 $(D^2)^\dagger$ 列直接删去。

## 2. 原连续尾的受限 MP 上界准确应用于返回列

[R254 相容多次原像稿](R254-appendix-compatible-multiple-preimages-and-quarter-stable-range.md)的 §3 在原连续尾上构造了合法 primitive 单次原像。取其中 $s=t=1$，将其 $a_j=(j+2)^{-2}$ 以 $j=i-1$ 重编号，输入为 $p-1$ 层，可得到
$$
\|D_p^\dagger\Pi_{1,p-1}\|
\le512\sqrt{p+1}(x+p+1)^{3/2}
\le512\sqrt{p+2}(x+p+2)^{3/2}.
\tag{2.1}
$$
这是完整逆之后压到 primitive 源的界：使用的是合法原像上界与真 MP 最小性，没有交换压缩和求逆。

由 (0.1)、(2.1) 和 $\|\Pi_{1,p-1}\|\le1$，
$$
\boxed{
\|D_p^\dagger\Pi_{1,p-1}\mathcal C_1\mathcal Tf\|
\le
\frac{2048e^{1/2}}{x^2}
\sqrt{p+2}(x+p+2)^{3/2}\|f\|.
}
\tag{2.2}
$$
$p=0$ 时删除源为零；其余自然域都是原固定层的真 MP 域，(1.1) 已给完整可行源。

因此同一二次删除源的顺次列满足
$$
\boxed{
\|Q_pQ_{p-1}\mathcal C_2\mathcal Tf\|
\le
\left[
\frac{90}{x}
+\frac{2048e^{1/2}}{x^2}
\sqrt{p+2}(x+p+2)^{3/2}
\right]\|f\|.
}
\tag{2.3}
$$

## 3. 任意真实端点 partial 保留，不增加 height 费

置
$$
\mathcal P_{p,j}=Q_pQ_{p-1}\cdots Q_{p-j+1}D^j.
$$
由 $y\in\ker D^3$，所有 $j\ge3$ 项在这个实际列上准确为零。第一项为
$\mathcal P_{p,1}y=(I-\Pi_{1,p})y$，第二项就是 (1.3)。

所以对任意原窗口的真实 partial
$$
\mathscr A_p=
\sum_{\substack{1\le j\le h\\a\le p-j\le b}}\mathcal P_{p,j},
$$
不论 $p$ 位于内部还是任一端点，均有
$$
\boxed{
\|\mathscr A_p\mathcal L^*\mathcal Tf\|
\le M_{x,p}\|f\|,
\qquad
M_{x,p}:=
\frac{180}{x}
+\frac{2048e^{1/2}}{x^2}
\sqrt{p+2}(x+p+2)^{3/2}.
}
\tag{3.1}
$$
这里第一、二项的系数各为 $0$ 或 $1$；没有把端点 partial 改成完整内部和，也没有把界再乘 $h$。

对任意互相正交的实际孔层族 $f_p\in K_p$，
$$
\sum_{p\le Q}\|\mathscr A_p\mathcal L^*\mathcal Tf_p\|^2
\le\left(\sup_{p\le Q}M_{x,p}\right)^2\sum_{p\le Q}\|f_p\|^2.
\tag{3.2}
$$
因此与任意同带 $v_p$ 的双线性配对也只付同一个 supremum 和两个完整平方和，不另付层数。

## 4. 在原二次窗口上的费用量级

若 $Q\ge\max(x,2)$，则
$$
\sqrt{p+2}(x+p+2)^{3/2}
\le3\sqrt6\,Q^2\qquad(p\le Q),
$$
故
$$
\sup_{p\le Q}M_{x,p}
\le\frac{180}{x}
+6144\sqrt6\,e^{1/2}\frac{Q^2}{x^2}.
\tag{4.1}
$$
在已付条件窗口 $Q=L_0h^2$ 中，若 $L_0$ 固定且 $h/x\le\kappa_0$，便有
$$
\boxed{
\sup_{p\le Q}M_{x,p}
\le
\left(180+
6144\sqrt6\,e^{1/2}L_0\kappa_0^2\right)Q.
}
\tag{4.2}
$$
整数取整时将固定上界 $Q/h^2$ 纳入常数即可。纯负部路线允许的 $R=d$、$h=2d$、$x=m+d$ 正在此范围内。

因此这个明确平滑源列的完整顺次返回已达到原二次窗口容许的 $O(Q)$ 规模；不需要先把 (2.2) 改成关于 $p$ 的统一常数。

## 5. 后续必须继续识别的 actual 来源

当前实际 mixed 恒等式的端点是原 $u_Q$、或 $\mathcal Tu_Q$。本文没有证明它们可用受控系数表示为
$\mathcal L^*\mathcal T f_p$、$f_p\in K_p$，也没有证明其余分量的同源返回可忽略。

因此 (4.2) 是一类真正原源的顺次返回预算，而不是 $N=M$ 的完成证明。它的收益是将此前保留的
$D^\dagger\Pi_1\mathcal C_1\mathcal T$ 返回列支付到正确窗口尺度，同时保留完整 MP、primitive 源和两端 partial；下一步仍须与 actual $u_Q$ 的共同来源相接。
