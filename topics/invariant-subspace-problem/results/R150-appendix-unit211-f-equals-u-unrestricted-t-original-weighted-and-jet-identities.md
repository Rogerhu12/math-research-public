# R150 补充：f=u、自由 t 的完整原 weighted N/P 与两条低次标量身份

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 结论与范围

本篇只施加原 $f=u$，保留任意 $t$。在真正 dual 乘法下，给出完整 weighted N/P 和两条极化 jet 的四个修正项；随后得到两条有明确原组合系数的必要式
$$
\boxed{2P_{02}(2\lambda-1)w=bc\,tK_w,\qquad
2P_{02}\lambda(2\ell-1)=bc\,tK_\lambda.}
\tag{1}
$$
两核 $K_w,K_\lambda$ 对实际 $X,Y,t$ 至多二次。它们不需要新几何首项、$\Phi$、$W$、$M$ 或 $\Delta$ 的逆；$t=0$ 也完整保留。(1) 不是完整原系统的充分条件。

这些原身份不依赖已经完成的 W / $f=u$ 排除，保留为一般原 Gram 的精确低次接口；没有为本篇重算任何已闭 W 分支。

## 2. 七自由变量的同一原 Gram

令 $b,c,p,q,X,Y,t$ 自由，定义
$$
\ell=b+c,\quad a=1-\ell,\quad u=bp+cq,\quad
V=bX+cY,
$$
$$
r=X-ap-ct,\quad s=Y-aq-bt,\quad
A_1=2u-2V+2bc\,t.
$$
使用原四行
$$
g_0=(0,0,p,q),\quad
g_1=(0,A_1,r,s),\quad
g_B=(p,r,0,t),\quad
g_C=(q,s,t,0).
\tag{2}
$$
乘法严格为
$$
v\cdot z=(v_0z_0,\ v_0z_1+v_1z_0,\ v_Bz_B,\ v_Cz_C),
$$
$\tau(v)=av_0+v_1+bv_B+cv_C$，$\mathbf1=(1,0,1,1)$，
$DK(v)_j=\tau(g_jv)$。于是
$$
d=DK(\mathbf1)=(u,d_1,X,Y),\qquad
d_1=(1+\ell)u-V,\qquad F_2=\tau(d)=2u.
$$
因此 (2) 是整个 $f=u$ 原图的自由参数构造，没有额外约束 $t$。

所有原均值使用
$$
E_j=\tau(g_j^2)-2(DK(d))_j-2(d^2)_j+2F_2d_j
$$
的原 dual 解释；特别 $j=1$ 第一项是 $2\tau(g_0g_1)$，平方项是 $-4d_0d_1$。记
$$
\mathcal N_0=N_4(g_0),\quad P_{02}=P_2(g_0),\quad
\mathcal N_j=N_4(g_0+g_1)-N_4(g_0)-N_4(g_1),
$$
$$
\mathcal P_j=3\tau\bigl((g_0-\tau(g_0)\mathbf1)^2
(g_1-\tau(g_1)\mathbf1)\bigr).
$$
$N_4$、$P_2$ 均直接由完整原定义计算，不沿用错误的 compact 均值。

再记
$$
\sigma=p+q,\quad q_*=pq,\quad S_x=X+Y,\quad
P_x=pX+qY,\quad W_1=bpX+cqY,
$$
$$
V_2=bp^2+cq^2=\sigma u-\ell q_*,\qquad T_0=V_2-2u^2,
$$
$$
E_p=bpE_B+cqE_C,\qquad
E_{W,2}=b(2p-u-X)E_B+c(2q-u-Y)E_C,
$$
$$
N_W=bN_4(g_B)+cN_4(g_C),\qquad
P_W=bP_2(g_B)+cP_2(g_C).
$$

## 3. 自由 t 的四个完整修正项

定义
$$
\Phi_*=-\sigma^2+q_*+3V_2+2\ell q_*-2u^2,
$$
$$
C_N=2t(S_x-4u)-8XY+4(qX+pY)+4uS_x+4u^2-4a q_*,
$$
$$
\begin{aligned}
C_P={}&4t^2+4t(u-S_x-\sigma)-8XY+8\sigma S_x
 +2(\sigma^2-3q_*)\\
&-18V_2-8\ell q_*+20u^2,
\end{aligned}
$$
$$
\begin{aligned}
C_J={}&2(\sigma-u)t+4W_1-2\sigma S_x-2P_x-4\sigma^2
 +4q_*\\
&+16V_2+12\ell q_*-8u^2.
\end{aligned}
$$
在全部七变量整数多项式环中，完整成立
$$
N_W=A_1T_0-4\ell u^3+2d_1E_0+bc\,tC_N,
\tag{3}
$$
$$
\begin{aligned}
2P_W={}&(1-2\ell)\mathcal N_0+3A_1T_0-8\ell u^3\\
&+2(2\ell u+d_1)E_0+2E_{W,2}+bc\,tC_P,
\end{aligned}
\tag{4}
$$
$$
2\mathcal P_j-3\mathcal N_0+6aP_{02}+3A_1T_0
 =6bc\,t\Phi_*,
\tag{5}
$$
$$
\begin{aligned}
\mathcal N_j-2\ell\mathcal N_0+2aP_{02}+2E_p
 -2uE_1-2auE_0-A_1(E_0-T_0)=bc\,tC_J.
\end{aligned}
\tag{6}
$$
在规范原图 $\sigma=2,\ q_*=Q$ 上，$\Phi_*=\Phi=T_0+4u-4+Q$。因此 (5) 保留完整原 $P_1$，而不是只保它乘以一个可能为零的因子。

这些修正项分别只有 17、22、20 个原七变量单项；$\Phi_*$ 有 10 项。它们是整个自由 $t$ 原恒等式，不由 $t=0$ 的结果外推。

## 4. 两个原低次组合

置
$$
\begin{aligned}
K_w=2\{&t^2+(5u-2S_x-\sigma)t+2XY+2P_x-2uS_x\\
&+2u^2-3\sigma u+q_*\},
\end{aligned}
$$
$$
\begin{aligned}
K_\lambda=2\{&t^2+2(3u-S_x-\sigma)t+2XY+3P_x
 +(\sigma-2u)S_x-2W_1\\
&+4u^2-8\sigma u+\sigma^2+\ell q_*\}.
\end{aligned}
$$
全原多项式逐项返回
$$
K_w=\Phi_*-C_N+\frac12C_P,\qquad
K_\lambda=K_w-C_J+2\Phi_*.
\tag{7}
$$
由 (3)—(6) 得到以下两个尚未取任何原方程商的恒等式：
$$
\begin{aligned}
0={}&N_W-P_W-\frac13\mathcal P_j+a(\mathcal N_0-P_{02})\\
&-(d_1-2\ell u)E_0+E_{W,2}+bc\,tK_w,
\end{aligned}
\tag{8}
$$
$$
\begin{aligned}
0={}&N_W-P_W+\mathcal N_j-\mathcal P_j
 +(2-3\ell)\mathcal N_0+(\ell-1)P_{02}\\
&+E_{W,2}+2E_p-2uE_1
 -\{d_1+A_1+2u(1-2\ell)\}E_0+bc\,tK_\lambda.
\end{aligned}
\tag{9}
$$
源码对 (8) 乘以 3 后检查所有整数系数，对 (9) 检查全部整数系数。所有均值和两个 weighted 值的原组合乘子都明确保留。

## 5. 回到完整原值条件

在规范原值图记
$$
w=\lambda-1-T,\quad
A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1.
$$
原值误差为
$$
n_0=\mathcal N_0-2\lambda P_{02},\quad
p_j=\mathcal P_j-3wP_{02},\quad
n_j=\mathcal N_j-4\lambda wP_{02},
$$
$$
N_S=N_W-2\lambda P_{02}(\ell+2T+A_2),\quad
P_S=P_W-P_{02}(\ell+3T+3A_2+B_3).
$$
这里 $n_j$ 由原 $N_1$ 和同一 $p_j$ 等价给出，没有遗漏原极化条件。

(8)、(9) 精确转成
$$
\begin{aligned}
2P_{02}(2\lambda-1)w-bc\,tK_w
={}&N_S-P_S-\frac13p_j+a n_0\\
&-(d_1-2\ell u)E_0+E_{W,2},
\end{aligned}
\tag{10}
$$
$$
\begin{aligned}
2P_{02}\lambda(2\ell-1)-bc\,tK_\lambda
={}&N_S-P_S+n_j-p_j+(2-3\ell)n_0\\
&+E_{W,2}+2E_p-2uE_1\\
&-\{d_1+A_1+2u(1-2\ell)\}E_0.
\end{aligned}
\tag{11}
$$
两次纯值多项式化简也由精确源完整返回。因此 (1) 在所有原条件下成立，并且两左式确属同一个原理想。没有除 $t$、$2\lambda-1$ 或两核的任何头。

当前 W 的整个 $f=u$ 已由独立的两个完整 QQ 参数投影排除；本篇不重新证明或重跑该结果。这里保留的是一般原 $f=u$ 图上覆盖所有 $t$ 的精确恒等式，供自由 $f$ 的后继原组合使用。它们也不宣称一般 $f=u$ 图没有原解。

## 6. 精确源、实际回执和未采用草稿

[自含源](../notes/2026-11-28-unit211-f-equals-u-unrestricted-t-original-weighted-jet-identities-8542.js)
共 7094 字节，SHA256
d53451f6350c755c015402122336fe6b2c0f7287c839167e3685de33a72d6bbe。
首次完整紧凑源实际 11 ms、910 次整数多项式乘法，十一条完整原差式全零；没有调用旧参数结式或旧模块门。
[小回执](../notes/2026-11-28-unit211-f-equals-u-unrestricted-t-original-weighted-jet-identities-receipt-8542.json)
保留准确范围。

此前同一新方向的原修正项构造实际 9 ms、757 次乘法，四项都完整除回 $bc\,t$。随后一个未采用紧凑草稿误将 (9) 的 $P_{02}$ 系数写成 $1-3\ell$；完整断言准确报告 24 项非零，没有数学结论由此草稿发布。更正为从原组合严格推出的 $\ell-1$ 后得到上述完整成功。该失败草稿按原字节保存，未伪称其原始断言通过；它没有改动任何已发表源或回执。
