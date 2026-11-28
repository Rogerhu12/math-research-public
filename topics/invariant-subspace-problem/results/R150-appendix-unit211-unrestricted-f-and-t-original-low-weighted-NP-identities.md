# R150 补充：自由 f、t 的完整原低次 weighted N/P 恒等式

日期：2026-11-28（Asia/Taipei）。会话 Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 完整结论

本篇解除 $f=u$ 的限制。采用完整原 unit211 Gram、真正 dual 乘法，
令 $\eta=f-u$、$\sigma=p+q$。
在原均值和全部原值/jet 条件下，有两条新的必要式
$$
\boxed{2P_{02}(2\lambda-1)w
=bc\,t\{K_w+4\eta(t-\sigma)\},}
\tag{1}
$$
$$
\boxed{2P_{02}\lambda(2\ell-1)
=4u\eta A_1+bc\,t\{K_\lambda+4\eta(t-2\sigma)\}.}
\tag{2}
$$
$K_w,K_\lambda$ 的完整低次定义见 §2。
这两式来自 §4 明确给出的原理想组合，不只是同解集的必要范数。
没有除 $\eta,t,\lambda,2\lambda-1$、任何均值头或新权因子。
在当前规范 $p+q=2$ 上，直接令 $\sigma=2$；
$f=u$、$t=0$ 及其交点仍被完整包括。

本篇本身不排除原图，也不宣称满足 (1)、(2) 就满足全部原条件。
它给后继同点原消元较低次数的输入；未重做任何 W 参数投影、
Phi 头零覆盖或已冻结的模型门。

## 2. 八个自由变量与两个核

取 $b,c,p,q,X,Y,t,\eta$ 为八个自由变量，定义
$$
\ell=b+c,\quad a=1-\ell,\quad u=bp+cq,\quad f=u+\eta,\quad
V=bX+cY,
$$
$$
r=X-ap-ct,\quad s_G=Y-aq-bt,\quad A_1=2f-2V+2bc\,t.
$$
原四行
$$
g_0=(0,0,p,q),\quad g_1=(0,A_1,r,s_G),\quad
g_B=(p,r,0,t),\quad g_C=(q,s_G,t,0)
\tag{3}
$$
在真正乘法
$$
(vz)_1=v_0z_1+v_1z_0,\qquad
\tau(v)=av_0+v_1+bv_B+cv_C
$$
下给
$$
d=DK(\mathbf1)=(u,d_1,X,Y),\quad
d_1=2f-V-au,\quad F_2=\tau(d)=2f.
$$
所有均值 $E_j$ 都用原 $-2(d^2)_j$，特别
$E_1$ 的该项是 $-4ud_1$，不是 $-2d_1^2$。

沿用[自由 t、f=u 的完整原身份](R150-appendix-unit211-f-equals-u-unrestricted-t-original-weighted-and-jet-identities.md)
的**小参数定义**，但本篇的 $E_j,N/P,d_1,A_1$ 都由 (3) 的自由 $f$ 重新构造。
记
$$
q_*=pq,\quad S_x=X+Y,\quad P_x=pX+qY,\quad
W_1=bpX+cqY,\quad V_2=bp^2+cq^2,\quad T_0=V_2-2u^2,
$$
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
\tag{4}
$$
置
$$
\widehat K_w=K_w+4\eta(t-\sigma),\qquad
\widehat K_\lambda=K_\lambda+4\eta(t-2\sigma).
\tag{5}
$$
它们对实际 $f,X,Y,t$ 至多二次。新增项是完整原八变量返回，
不是把旧 $f=u$ 身份任意延拓。

## 3. 两个低次原组合的准确 eta 余项

使用原
$$
\mathcal N_0=N_4(g_0),\quad P_{02}=P_2(g_0),\quad
\mathcal N_j=N_4(g_0+g_1)-N_4(g_0)-N_4(g_1),
$$
$$
\mathcal P_j=3\tau((g_0-\tau(g_0)\mathbf1)^2
(g_1-\tau(g_1)\mathbf1)),
$$
$$
N_W=bN_4(g_B)+cN_4(g_C),\quad P_W=bP_2(g_B)+cP_2(g_C),
$$
$$
E_p=bpE_B+cqE_C,\qquad
E_{W,2}=b(2p-u-X)E_B+c(2q-u-Y)E_C.
$$
注意这里 $E_{W,2}$ 的乘子保留写定的 $u$，没有把它偷换为 $f$。

定义两个未取商的原组合
$$
\begin{aligned}
\mathcal L_w={}&N_W-P_W-\mathcal P_j/3
+a(\mathcal N_0-P_{02})\\
&-(d_1-2\ell u)E_0+E_{W,2}+bc\,tK_w,
\end{aligned}
$$
$$
\begin{aligned}
\mathcal L_\lambda={}&N_W-P_W+\mathcal N_j-\mathcal P_j
+(2-3\ell)\mathcal N_0+(\ell-1)P_{02}\\
&+E_{W,2}+2E_p-2uE_1
-\{d_1+A_1+2u(1-2\ell)\}E_0+bc\,tK_\lambda.
\end{aligned}
$$
在整个八变量整数多项式环，本次准确得到
$$
\mathcal L_w=\eta R_w,\qquad
\mathcal L_\lambda=\eta R_\lambda,
\tag{6}
$$
其中
$$
\boxed{R_w=-2E_0+4bc\,t(\sigma-t),}
$$
$$
\boxed{R_\lambda=R_w-4uA_1+4bc\,\sigma t.}
\tag{7}
$$
第一次对 $3\mathcal L_w$ 检查全部整数系数，再完整除回 $3\eta$；
第二次完整除回 $\eta$。这些是多项式可除身份，结论不要求
$\eta$ 非零。

两个完整商分别只有 12、18 个单项。其规范序列由八变量升序指数及
整数系数字符串给出，SHA256 分别为
3dd5ab30079285cc5e065fe6ced6802d23690e1d94a7103a8869f735bb0d559f、
05b1367603f039ea2507b992a00d49acc7d6149fbca6b0020b5426f6320176f9。
一个独立的 38 次乘法小参数识别仅展开 (7)，准确匹配这两个已返回的商；
没有重跑原 Gram 门。

可直接核对第一式：原
$$
E_0=V_2-2W_1-2u^2+4fu
$$
给
$$
-2E_0=4W_1-2V_2-4u^2-8u\eta,
$$
再加 $4bc\,t(\sigma-t)$ 即是返回的十二项。第二商与第一商之差
正是 $-4uA_1+4bc\,\sigma t$。

## 4. 两条完整原理想身份

由 (6)、(7) 移项，完整有
$$
\begin{aligned}
0={}&N_W-P_W-\mathcal P_j/3+a(\mathcal N_0-P_{02})\\
&-(d_1-2\ell u-2\eta)E_0+E_{W,2}
+bc\,t\widehat K_w,
\end{aligned}
\tag{8}
$$
$$
\begin{aligned}
0={}&N_W-P_W+\mathcal N_j-\mathcal P_j
+(2-3\ell)\mathcal N_0+(\ell-1)P_{02}\\
&+E_{W,2}+2E_p-2uE_1
-\{d_1+A_1+2u(1-2\ell)-2\eta\}E_0\\
&+4u\eta A_1+bc\,t\widehat K_\lambda.
\end{aligned}
\tag{9}
$$
这是自由 $f,t$ 原 Gram 上的恒等式，不依赖 $\Phi$、W 或值判别式。

在原非零最高值的规范层，设
$$
w=\lambda-1-T,\quad A_2=2\lambda^2-2\lambda+1,\quad
B_3=4\lambda^3-6\lambda^2+3\lambda-1,
$$
并记原值误差
$$
n_0=\mathcal N_0-2\lambda P_{02},\quad
p_j=\mathcal P_j-3wP_{02},\quad
n_j=\mathcal N_j-4\lambda wP_{02},
$$
$$
N_S=N_W-2\lambda P_{02}(\ell+2T+A_2),\quad
P_S=P_W-P_{02}(\ell+3T+3A_2+B_3).
$$
按原前三矩化简值部分，(8)、(9) 等价于
$$
\begin{aligned}
2P_{02}(2\lambda-1)w-bc\,t\widehat K_w
={}&N_S-P_S-p_j/3+a n_0\\
&-(d_1-2\ell u-2\eta)E_0+E_{W,2},
\end{aligned}
\tag{10}
$$
$$
\begin{aligned}
2P_{02}\lambda(2\ell-1)-4u\eta A_1-bc\,t\widehat K_\lambda
={}&N_S-P_S+n_j-p_j+(2-3\ell)n_0\\
&+E_{W,2}+2E_p-2uE_1\\
&-\{d_1+A_1+2u(1-2\ell)-2\eta\}E_0.
\end{aligned}
\tag{11}
$$
这里纯值多项式部分与前篇已经完整返回的两条标量恒等式相同；
本次新增的全部 $\eta$ 项则由 (6)、(7) 支付。令所有原误差为零即得 (1)、(2)。

尤其在已经用原定义恒等恢复 $E_0=n_0=p_j=0$ 的后继坐标中，左端简化为
$$
L_w=N_S-P_S+E_{W,2},
$$
$$
L_\lambda=N_S-P_S+N_1+E_{W,2}+2E_p-2uE_1.
$$
因此在原均值上保留 $N_S,L_w$ 也保留 $P_S$；第二式在这些条件和
原 $N_1$ 下冗余，不能冒充另一条独立新增条件。

## 5. 任意 f 的两个原 jet

定义
$$
\Phi_*=T_0+2\sigma u-\sigma^2+q_*,
$$
$$
\begin{aligned}
C_J={}&2(\sigma-u)t+4W_1-2\sigma S_x-2P_x-4\sigma^2
+4q_*+16V_2+12\ell q_*-8u^2.
\end{aligned}
$$
本次还直接在八变量原环返回
$$
2\mathcal P_j-3\mathcal N_0+6aP_{02}+3A_1T_0
=6bc\,t\Phi_*,
\tag{12}
$$
$$
\begin{aligned}
\mathcal N_j-2\ell\mathcal N_0+2aP_{02}
+2E_p-2uE_1-2auE_0-A_1(E_0-T_0)\\
=bc\,tC_J+\eta\{-4uA_1+4bc\,\sigma t\}.
\end{aligned}
\tag{13}
$$
在 $p+q=2$ 上，$\Phi_*=\Phi$。
故整个 $\Phi=0$ 原图都有
$A_1T_0=2(\ell+T)P_{02}$，不再要求 $f=u$。
(13) 的额外项也完整保留，不能把旧 $f=u$ 的第二 jet 原封不动外推。

## 6. 实际源和范围

[八变量原源](../notes/2026-11-28-unit211-unrestricted-f-and-t-original-low-weighted-NP-identities-8542.js)
为 6454 字节，SHA256
933df4a9dd085bc26d415c3220ab7273ed2392ffb22f048f684e6dfe51ffd0e8。
唯一首次纯 V8 实际 12 ms、855 次整数多项式乘法、六个完整零差返回；
两个低组合与第二 jet 的三个 $\eta$ 商都完整乘回。
这是新的八变量原输入，没有执行旧结式、GB 或已登记的原排空门。

[紧凑小参数识别](../notes/2026-11-28-unit211-unrestricted-f-and-t-compact-eta-quotients-8542.js)
为 3775 字节，SHA256
2647ac9d3d0069a0bd292e493d9a440258e2babf05c6843beb0fc34cba1a913f；
实际 2 ms、38 次乘法，仅识别 (7) 的两个小参数。

[小回执](../notes/2026-11-28-unit211-unrestricted-f-and-t-original-low-weighted-NP-identities-execution-8542.json)
保存上述真实身份、参数 SHA 与完整差式状态，不保存展开大系数。
所有原零面仍须按各自来源处理；本篇不完成整个 unit211 或普通 Hilbert ISP。
