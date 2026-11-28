# R150 补充：原 A1=t=0 的完整 jet 身份与值判别式零

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

## 1. 结论

在原 unit211 Frobenius Gram 和原 $N_0,N_1,P_1$、均值条件中，若
$$
A_1=t=0,\qquad P_{02}\ne0,
$$
则
$$
T=-\ell,\qquad A_2=\ell,\qquad
D=\ell A_2-T^2=0.
\tag{1}
$$
这里 $A_1$ 是 Gram 二重点的一阶对角坐标，$t$ 是两 singleton 间的 Gram 坐标；它们不是值矩 $A_2$。

结论不要求 $\Phi=0$ 或 W，不倒 $M$、$Q$、$P_f$ 或任何头。它本身是一个原判别式零结论，不排除 $D=0$ 碰撞图。

结合已经更正的原紧凑均值，在 $Q\rho\ne0$、$P_{02}D\ne0$ 的实际归一图中，
$$
\boxed{t=0\ \Longrightarrow\ f=u.}
\tag{2}
$$
原 $t=0,V=f$ 因子因而完整排除；其中 $V=bX+cY$。这是正确原式的新用途，不借用已撤回的旧 first-head 或其任何单位。

## 2. 同一原 Gram 与真实乘法

令 $a=1-b-c$、$\ell=b+c$，保留六个独立变量 $b,c,p,q,r,s$。原四行为
$$
g_0=(0,0,p,q),\qquad g_1=(0,0,r,s),
$$
$$
g_B=(p,r,0,0),\qquad g_C=(q,s,0,0).
\tag{3}
$$
这正是原 $A_1=t=0$ 的全部 Gram，没有取一个特殊 $p/q$、权嵌入或 dual-number 近似。

使用
$$
\operatorname{vm}(x,y)=(x_0y_0,x_0y_1+x_1y_0,x_By_B,x_Cy_C),
$$
$$
\tau(x)=a x_0+x_1+b x_B+c x_C,\qquad
\mathbf1=(1,0,1,1).
$$
令 $DK(x)_j=\tau(\operatorname{vm}(g_j,x))$、$d=DK(\mathbf1)$、$F_2=\tau(d)=2f$。于是
$$
d=(u,R_0,ap+r,aq+s),\qquad
u=bp+cq,\quad R_0=br+cs,
$$
$$
f=au+R_0=V.
\tag{4}
$$
由一般原恒等式 $A_1=2f-2V+2bc\,t$，(3) 与 $t=0,V=f$ 完全等价。

原均值 $E_j$ 按真实 $\operatorname{vm}(d,d)$ 定义；特别 $E_1$ 中的二次项是 $-4d_0d_1$。令
$$
\mathcal N_0=N_4(g_0),\qquad
\mathcal N_1=N_4(g_0+g_1)-N_4(g_0)-N_4(g_1),
$$
$$
P_{02}=P_2(g_0),\qquad
\mathcal P_1=3\tau((g_0-u\mathbf1)^2(g_1-R_0\mathbf1)),
$$
并记 $E_p=bpE_B+cqE_C$。

## 3. 两条完整原多项式身份

对 (3) 的全部六个自由参数，严格有
$$
\boxed{2\mathcal P_1-3\mathcal N_0+6aP_{02}=0,}
\tag{5}
$$
$$
\boxed{
\mathcal N_1-2\ell\mathcal N_0+2aP_{02}
+2E_p-2uE_1-2auE_0=0.
}
\tag{6}
$$
这两式没有使用原方程为零；是原多项式环中的完整身份。

给出直接代数证明。设
$$
V_j=bp^j+cq^j,\quad
R_j=bp^jr+cq^js,\quad
S_j=bp^jr^2+cq^js^2,\quad
W_1=aV_2+R_1,\quad T_0=V_2-2u^2.
$$
由真实乘法直接展开得到
$$
P_{02}=V_3-3uV_2+2u^3,\qquad
\mathcal P_1/3=R_2-2uR_1-T_0R_0,
$$
$$
\mathcal N_0=2aV_3+2R_2-2fV_2-4uW_1+4fu^2,
$$
$$
E_0=T_0-2W_1+4uf,\qquad
E_1=2\ell R_1-2S_0+4(f-u)R_0,
$$
$$
E_p=a(1-2a)V_3+2(1-2a)R_2-2fV_2-2uR_1-2S_1+4fW_1,
$$
$$
\mathcal N_1
=4\left[aR_2+S_1-(f+au)R_1-uS_0-R_0W_1+2fuR_0\right].
$$
代入 $f=au+R_0$、$a+\ell=1$，分别消去 $V_3,R_2,S_0,S_1,W_1$，即得 (5)、(6)。没有除参数。

## 4. 回到原值和 jet 条件

在真实原系统中，归一条件为
$$
\mathcal N_0=2\lambda P_{02},\qquad
\mathcal P_1=3wP_{02},\qquad
\mathcal N_1=4\lambda wP_{02},
$$
且原均值全部为零。由 (5) 和 $P_{02}\ne0$ 得
$$
w=\lambda-a.
$$
原值均值给 $w=\lambda-1-T$，所以
$$
T=a-1=-\ell.
$$
再代入 (6)，有
$$
4\lambda(\lambda-a)-4\ell\lambda+2a=0.
$$
因 $a+\ell=1$，这就是
$$
2\lambda^2-2\lambda+a=0.
$$
故原值二阶矩
$$
A_2=2\lambda^2-2\lambda+1=\ell,
$$
从而得到 (1)。

最后，在 $p+q=2$、$p-q=2\rho$ 的归一图上，正确原 $R_2$ 在 $t=0$ 为
$$
R_{2,\mathrm{true}}=8\rho Q^2(f-u)(V-f).
$$
原均值使它为零。$Q\rho\ne0$ 时若 $f\ne u$，则 $V=f$，由 (1) 得 $D=0$。在原物理 $D\ne0$ 图中只能 $f=u$，即 (2)。

## 5. 新精确小证书

源：
[2026-11-28-unit211-original-bipartite-Gram-two-jet-identities-8542.js](../notes/2026-11-28-unit211-original-bipartite-Gram-two-jet-identities-8542.js)。

- Git blob：`ba846f518dad0cd77d94396d2c54952c7c44dde6`。
- SHA256：`277c1c978d07f65308eedbc291513e1039c69e99f179b0e2b9c6e472334450ff`。
- 3545 字节，自含纯 V8 BigInt。
- 首次实际执行 5 ms、495 次整数多项式乘法。
- 原 $F_2=2V$ 及 (5)、(6) 三条完整差式均为零。
- [实际小回执](../notes/2026-11-28-unit211-original-bipartite-Gram-two-jet-identities-execution-8542.json)。

源码使用六个自由参数和完整原 Gram，没有把 $\gamma^2$ 置零、没有只核某个数值点、没有执行旧矩阵或更正后的四头计算。本证明只给上述原分支结论，不宣称剩余 $f=u,t=0$ 支、整个 Phi 或普通 ISP 已完成。
