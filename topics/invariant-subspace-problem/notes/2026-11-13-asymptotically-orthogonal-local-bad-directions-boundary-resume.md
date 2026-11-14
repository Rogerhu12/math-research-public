# 局部最小能量坏方向可以渐近正交于真实核

日期：2026-11-13（UTC）。作者：boundary_resume / Astra-ISP-0c。状态：已证明的范围校准；不构造真实缺陷。

本补充使用[局部最小能量下界与真实投影约束](../results/R239-appendix-local-minimal-energy-lower-bound-and-true-projection-constraints.md)的全部原参数和配对向量 $h_{m,q},g_{m,q}$。取
$$
m=m(q),\quad d=2^m,\quad
t=\left\lfloor(3\log q/800)^{1/3}\right\rfloor,
\quad J=m+2q,
$$
并简写
$$
S_J=\sum_{j\ge J}(j+1)^{-4},\qquad
B_t=\sqrt{t!}\,S_J^{t/2},\qquad
\rho=\langle h_{m,q},g_{m,q}\rangle.
$$
以下只需充分大的整数 $q$。

## 1. 改选实际头方向仍保留最小修复下界

原有限头路径已证
$$
A_m^t e_t=\kappa_t e_0,\qquad \kappa_t\ge e^{-100t^4}.
$$
故
$$
n_t:=\|(A_m^*)^t e_0\|\ge\kappa_t>0.
$$
取
$$
x_q=\frac{(A_m^*)^t e_0}{n_t},\qquad
v_q=x_q\otimes h_{m,q},\qquad
u_q=x_q\otimes g_{m,q}.
$$
三个向量均为单位向量，$v_q$ 属于原低输出精确核。
此外
$$
\|A_m^t x_q\|
\ge|\langle A_m^t x_q,e_0\rangle|=n_t.
$$
因此对任意有限加宽窗口，乃至整个无限高尾，原配对下界给
$$
\lambda^{[\infty]}_{m(q),q}(v_q)
\ge\frac{\rho n_t}{B_t}
\ge\frac{\rho\kappa_t}{B_t}.
$$
特别
$$
\boxed{
\liminf_{q\to\infty}
\frac{\log\lambda^{[\infty]}_{m(q),q}(v_q)}
 {(\log q)^{4/3}}
\ge c_0,\qquad
c_0=\frac{3(3/2)^{4/3}}{4^{4/3}100^{1/3}}>0.
}
\tag{1.1}
$$
改选头方向没有把坏能量换成指定右逆的范数。

## 2. 对偶方向与整个真实核几乎正交

令 $P_M$ 为原真实 $M=\ker T$ 的正交投影。对任意单位 $w\in M$，原稿的真实全局相容恒等式给
$$
\left\|
A_m^t(I\otimes\langle g_{m,q},\cdot\rangle)
P_q^{(m)}w
\right\|
\le B_t+26t\,6^{t-1}\eta_{m-1}.
$$
取其 $e_0$ 坐标，得到
$$
|\langle w,u_q\rangle|
\le\frac{B_t+26t\,6^{t-1}\eta_{m-1}}{n_t}.
$$
所以
$$
\|P_Mu_q\|
\le \frac{B_t}{\kappa_t}
+\frac{26t\,6^{t-1}\eta_{m-1}}{\kappa_t}.
\tag{2.1}
$$

第一项由原优化直接满足
$$
\frac{B_t}{\kappa_t}
\le\exp[-(c_0-o(1))(\log q)^{4/3}].
$$
第二项必须保留这里的实际 $t$，不能粗换成 $d$。
事实上
$$
100t^4=(c_0/3+o(1))(\log q)^{4/3},
\qquad
d^4\ge (4\log(q+2))^{4/3}.
$$
因此由 $\eta_{m-1}\le e^{-80d^4}$，
$$
\begin{aligned}
\log\frac{26t6^{t-1}\eta_{m-1}}{\kappa_t}
&\le -80d^4+100t^4+O(t+\log t)\\
&\le[-80\cdot4^{4/3}+c_0/3+o(1)](\log q)^{4/3},
\end{aligned}
$$
其指数远小于第一项。最终
$$
\boxed{
\|P_Mu_q\|
\le\exp[-(c_0-o(1))(\log q)^{4/3}].
}
\tag{2.2}
$$

## 3. 真正低输出坏向量本身也渐近离开 M

配对构造满足 $\rho\ge e^{-2/(m+1)}$，从而
$$
\|h_{m,q}-g_{m,q}\|^2=2(1-\rho)
\le\frac4{m+1}.
$$
利用正交投影的收缩性，
$$
\boxed{
\|P_Mv_q\|
\le \frac2{\sqrt{m(q)+1}}
+\exp[-(c_0-o(1))(\log q)^{4/3}]
\longrightarrow0.
}
\tag{3.1}
$$
于是这组单位低输出向量同时满足：

- 任意宽度的真正最小高尾修复至少有 $\exp(c(\log q)^{4/3})$ 规模；
- 到真实核的正交投影范数趋于零，故其到真实核的距离趋于1。

这定位了该局部坏族，没有把它误作真实核内坏向量。若
$C_{m,q}:M\to\mathscr V_{m,q}$ 是真实低方程投影的限制，则对
$v_q\in\mathscr V_{m,q}$ 有
$C_{m,q}^*v_q=P_Mv_q$，所以 (3.1) 同时是实际投影范围的一个准确对偶约束。

它不排除真实范围上的其他坏方向，也没有控制完整 Gram 逆能量。下一步仍须利用真实核相容性处理那些不能被 (3.1) 消掉的部分。
