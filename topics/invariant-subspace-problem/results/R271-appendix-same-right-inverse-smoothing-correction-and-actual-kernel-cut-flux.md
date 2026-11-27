# R271 附录：同一右逆的光滑修正、有限孔行与真实核截断通量

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

本稿继续[同一实际右逆的全部物理孔指数尺度](R271-appendix-single-actual-right-inverse-on-all-physical-exponential-scales.md)。所有算子仍为原 $T_N,T_Y$；沿用固定 $\lambda>\kappa_0$、$Q$、$R_q$、$R$、$E$、$U=(I+E)^{-1}$ 与 $\mathcal G_\lambda=RU$。这里没有更换右逆或规范来源。

## 1. 有界光滑修正与双侧孔层支撑

令
$$
C=\mathcal G_\lambda E.
\tag{1.1}
$$
由于 $E:H\to X_{\kappa+\lambda}$、$\mathcal G_\lambda:X_{\kappa+\lambda}\to X_\kappa$，同一个 $C$ 满足
$$
C:H\longrightarrow X_\kappa\quad\text{有界，对每个 }\kappa\ge0.
\tag{1.2}
$$
先在 $X_\lambda$ 上使用 $UE=EU=I-U$，得到
$$
\boxed{\mathcal G_\lambda=R-C.}
\tag{1.3}
$$
(1.1) 在整个 $H$ 上定义；(1.3) 不把 $R$ 或 $\mathcal G_\lambda$ 扩成全 $H$ 有界算子。

上一稿的同一逐层误差界给
$$
\|E\mathsf P_q\|_{H_q\to X_\nu}
\le2e^{c_\lambda(1+\nu)^2}e^{-28(q+Q)^2}.
$$
因此，对每个固定 $\kappa$ 有有限 $A_{\lambda,\kappa}$，使
$$
\boxed{
\|C\mathsf P_q\|_{H_q\to X_\kappa}
\le A_{\lambda,\kappa}e^{-28(q+Q)^2}
\quad(q\ge0).
}
\tag{1.4}
$$
特别，真正有界伴随 $C^*$ 还满足
$$
\|\mathsf P_qC^*v\|
\le A_{\lambda,0}e^{-28(q+Q)^2}\|v\|,
$$
$$
\boxed{
\|e^{28\mathcal N^2}C^*v\|
\le
\frac{A_{\lambda,0}e^{-28Q^2}}{\sqrt{1-e^{-112Q}}}\|v\|.
}
\tag{1.5}
$$
$q=0$ 包含在等比和中；临界系数 $28$ 由保留的正 $Q$ 余量支付。

同一个 $R_q$ 有比上一稿单侧上界更细的支撑：
$$
\boxed{
R_qH_q\subset
H_{[\max(0,q-m(q)+1),\,q+d(q)+m(q)]}.
}
\tag{1.6}
$$
证明直接来自
$$
R_q=\left.\Delta^{-1}
\sum_{k=0}^{d(q)-1}(-H_{m(q)})^k(Q')^{k+1}\Delta
\right|_{H_q}.
$$
若输入头孔数为 $r\le m(q)$，第 $k$ 项尾孔数准确增加 $k+1$，输出头孔数仍介于 $0$ 与 $m(q)$；故该项的总孔数介于 $q-m(q)+k+1$ 与 $q+m(q)+k+1$。有限对角因子保孔次数，遂得 (1.6)。这不假设 $H_m$ 保持物理孔分级。

## 2. 真实有限孔测试行与可闭性

把 $R$ 看作 $H$ 上定义域 $X_\lambda$ 的稠密定义算子。对任意 $p\ge0$，(1.6) 表明
$$
R_q^*H_{\le p}=\{0\}
\quad\text{只要 }q-m(q)+1>p.
\tag{2.1}
$$
因为 $m(q)=O(\log q)$，仅有限个 $q$ 不被 (2.1) 排除。更明确地，当 $q\ge Q\ge64$ 时，
$$
m(q)\le1+\tfrac12\log_2(2q)\le q/2.
$$
所以
$$
\boxed{
H_{\le p}\subset D(R^*),\qquad
R^*H_{\le p}\subset H_{\le\max(Q,2p)}.
}
\tag{2.2}
$$
这里 $R^*\xi=\sum_qR_q^*\xi$ 是有限个实际孔层的 Hilbert 和。它不是仅在有限整数行上定义的形式转置；每个孔层仍允许无限位支撑。

有限物理孔向量在 $H$ 稠密，因此 $R$ 可闭。由 (1.3)，$\mathcal G_\lambda$ 也可闭，且对有限孔 $\xi$，
$$
\mathcal G_\lambda^*\xi=R^*\xi-C^*\xi\in\mathscr E_\infty.
\tag{2.3}
$$
(1.5) 支付第二项的全部正指数域。

记 $\overline{\mathcal G_\lambda}$ 为此 Hilbert 图闭包，则
$$
T\,\overline{\mathcal G_\lambda}v=v
\quad(v\in D(\overline{\mathcal G_\lambda})).
\tag{2.4}
$$
这是由 $T$ 有界及原图中的实际右逆恒等式取极限得到的。其值域
$$
Y_\lambda=\operatorname{Ran}\overline{\mathcal G_\lambda}
$$
是闭子空间：若 $y_n=\overline{\mathcal G_\lambda}v_n\to y$，则由 (2.4) 有 $v_n=Ty_n\to Ty$，图闭性给 $y=\overline{\mathcal G_\lambda}Ty$。并且
$$
Y_\lambda\cap\ker T=\{0\}.
\tag{2.5}
$$
没有声称 $Y_\lambda=(\ker T)^\perp$，或其与 $\ker T$ 的和具有正角。

## 3. 同一个规范来源的实际块公式

对 $w\in N^\perp$，令 $h(w)$ 为旧稿同一规范形式解 $T^*h(w)=w$。它未必属于 $H$。上一稿的对偶表示与 (1.3) 给
$$
\boxed{
\mathsf P_qh(w)=R_q^*w-\mathsf P_qC^*w
\quad(q\ge0).
}
\tag{3.1}
$$
因此各项都是实际 Hilbert 孔块，且扣除项满足 (1.5) 的统一 Gaussian 权。记 $r(w)$ 为实际孔块 $r_q(w)=R_q^*w$ 定义的形式向量，则
$$
h(w)=r(w)-C^*w.
\tag{3.2}
$$
由原 $S=B^*$ 在 $H$ 有界，
$$
\boxed{
Sh(w)\in H\quad\Longleftrightarrow\quad Sr(w)\in H.
}
\tag{3.3}
$$
式 (3.3) 中 $S$ 在形式坐标上仍为原唯一前驱的加权右移，故有无歧义的逐坐标作用。等价的准确求和是
$$
\sum_{n\ge0}\alpha_{v_2(n+1)}^2|r(w)_n|^2<\infty.
\tag{3.4}
$$
对真正 $w\in W$，这是旧同源 $\Gamma$ 有限性所需的同一个实际输出域；没有用未经证明的全 $H$ 伴随来改换来源。Gaussian 修正已支付，(3.4) 的主项仍待支付。

## 4. 任意真实核近似的费用与弱核心判据

令 $f\in M=\ker T$，取任意 $f_n\in\mathscr E_\infty$ 且 $f_n\to f$ 于 $H$。写
$$
v_n=RTf_n,\qquad
k_n=f_n-\mathcal G_\lambda Tf_n.
\tag{4.1}
$$
这两个式子有真实定义域：$T$ 保持 $\mathscr E_\infty$，而 $\mathcal G_\lambda$ 保持该空间。于是
$$
k_n\in M\cap\mathscr E_\infty\subset N.
\tag{4.2}
$$
又因为 $Tf_n\to0$，有
$$
CTf_n\longrightarrow0\quad\text{于 }H,
\qquad
\mathcal G_\lambda Tf_n=v_n-CTf_n.
\tag{4.3}
$$

对每个有限物理孔测试向量 $\xi$，(2.2) 给
$$
\langle \xi,v_n\rangle
=\langle R^*\xi,Tf_n\rangle\longrightarrow0.
\tag{4.4}
$$
因此，若 $\{v_n\}$ 有一条有界子列，该子列由 (4.4) 和稠密性弱趋于 $0$。沿同一子列，(4.1)–(4.3) 给 $k_n\rightharpoonup f$。$N$ 为闭线性子空间，故弱闭，得到
$$
\boxed{
\liminf_n\|RTf_n\|<\infty
\quad\Longrightarrow\quad f\in N.
}
\tag{4.5}
$$
这里只需真实修复量有界子列，不要求它按范数趋零。

反过来，若 $f\in M\setminus N$，则对每一条上述实际 $\mathscr E_\infty$ 近似都有
$$
\boxed{\|RTf_n\|\longrightarrow\infty.}
\tag{4.6}
$$
否则有有界子列，违反 (4.5)。这不声称 $f\in N$ 时每条近似的费用有界。

尤其，对同一个 $w\in W$，可以取原全部物理孔截断
$$
f_n=P_{\le n}w.
$$
它允许无限位支撑，但属于 $\mathscr E_\infty$。由 $w\perp k_n$，
$$
\boxed{
\langle w,RT P_{\le n}w\rangle
=\|P_{\le n}w\|^2+\langle w,CT P_{\le n}w\rangle
\longrightarrow\|w\|^2.
}
\tag{4.7}
$$
(4.7) 是原两型、原同一 $w$ 的准确通量；完整进位均在实际 $T$ 中。若 $w\ne0$，则 (4.6) 迫这个特定修复量的全序列范数趋于无穷，同时 (4.4) 对每个固定有限孔测试仍趋零。不存在把小残量 $TP_{\le n}w\to0$ 直接换成小修复量的步骤。

目前尚未证明 (4.5) 的有界子列条件对全部真实 $w\in W$ 成立。原核正则化的下一项准确费用就是 $RT P_{\le n}w$，光滑 $C$ 项、有限孔测试行及同一个规范来源的修正已经支付；$N=M$ 与普通 ISP 均未关闭。
